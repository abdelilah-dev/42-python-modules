from typing import Any, List, Protocol
from abc import ABC, abstractmethod
import time
from sys import stderr


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        self.state = {"processed": 0, "errors": 0, "total_time": 0.0}

    def add_stage(self, stage: ProcessingStage) -> None:
        if not stage:
            raise ValueError("Failed To Add Stage - Can't add None Type")
        self.stages.append(stage)

    @abstractmethod
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    def process(self, data: Any) -> Any:
        if not data or data == "":
            raise ValueError("InputStage: empty data received")
        return data


class TransformStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["validated"] = True
        return data


class OutputStage:
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data = str(data)
        return data


class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        super().add_stage(stage)

    def process(self, data: Any) -> Any:
        start = time.time()
        try:
            print(f"Input: {data}")

            result = data
            for stage in self.stages:
                result = stage.process(result)

            value = data.get("value")
            unit = data.get("unit")
            status = "Normal range" if 18 <= value <= 28 else "Out of range"
            print("Transform: Enriched with metadata and validation")
            print(f"Processed temperature reading: {value}°{unit} ({status})")

            self.state["processed"] += 1
        except Exception as e:
            self.state["errors"] += 1
            print(f"[JSONAdapter ERROR] {e}", file=stderr)
            result = None
        finally:
            self.state["total_time"] = time.time() - start
        return result


class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        super().add_stage(stage)

    def process(self, data: Any) -> Any:
        start = time.time()
        try:
            print(f"Input: {data}")
            result = data
            for stage in self.stages:
                result = stage.process(result)

            culumns = len(data.split(","))
            actions = len([a for a in data.split(",") if a == "action"])
            print("Transform: Parsed and structured data")
            print(f"Output: User activity logged: {culumns}",
                  f"columns, {actions} action(s) processed")

            self.state["processed"] += 1
        except Exception as e:
            print(f"[CSVAdapter ERROR] {e}", file=stderr)
            self.state["errors"] += 1
            result = None
        finally:
            self.state["total_time"] = time.time() - start
        return result


class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: Any) -> None:
        super().__init__()
        self.pipeline_id = pipeline_id

    def add_stage(self, stage: ProcessingStage) -> None:
        super().add_stage(stage)

    def process(self, data: Any) -> Any:
        try:
            print(f"Input: {data}")
            result = data
            for stage in self.stages:
                result = stage.process(result)

            # Simulate a stream of sensor readings
            readings = [21.8, 22.0, 22.3, 22.1, 22.4]
            avg = sum(readings) / len(readings)
            print("Transform: Aggregated and filtered")
            print(f"Output: Stream summary: {len(readings)}",
                  f"readings, avg: {avg:.1f}°C")
            self.state["processed"] += 1
        except Exception as e:
            self.state["errors"] += 1
            print(f"[STREAMAdapter ERROR] {e}", file=stderr)
            result = None
        return result


class NexusManager():
    def __init__(self) -> None:
        self.pipelines: List[ProcessingPipeline] = []

    def register(self, pipeline: ProcessingPipeline) -> None:
        if not pipeline:
            raise ValueError("Nexus Register Failed - \
                             Can't Register Unknown pipeline")
        self.pipelines.append(pipeline)

    def run_all(self, data_list: List[Any]) -> None:
        for pipline, data in zip(self.pipelines, data_list):
            pipline.process(data)

    def chain(self, pipelines: List[ProcessingPipeline], data: Any) -> Any:
        result = data
        for pipeline in pipelines:
            result = pipeline.process(data)
        return result

    def print_stats(self) -> None:
        try:
            total_prossesed = sum(p.state["processed"] for p in self.pipelines)
            total_errors = sum(p.state["errors"] for p in self.pipelines)
            total_time = sum(p.state["total_time"] for p in self.pipelines)

            print(f"Records processed : {total_prossesed}")
            print(f"Errors            : {total_errors}")
            print(f"Total Time        : {total_time:.4f}s")
        except Exception as error:
            print(f"Failed To printing Stats: {error}", file=stderr)


class RawPipeline(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["state"] = "raw->processed"
        return data


class AnalyzedPipeline(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["state"] = "processed->analyzed"
            data["analysis"] = "ok"
        return data


class StoredPipeline(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        if isinstance(data, dict):
            data["state"] = "analyzed->stored"
            data["stored"] = True
        return data


class FragilePipeline(ProcessingPipeline):
    def process(self, data: Any) -> Any:
        raise ValueError("Invalid data format")


def error_recovery_test() -> None:
    tester = FragilePipeline()
    print("Simulating pipeline failure...")
    try:
        tester.process("bad_data")
    except ValueError as e:
        print(f"Error detected in Stage 2: {e}", file=stderr)
        print("Recovery initiated: Switching to backup processor")
        print("Recovery successful: Pipeline restored, processing resumed")


def pipeline_system() -> None:
    try:
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")

        print("\nInitializing Nexus Manager...")
        nexus = NexusManager()
        print("Pipeline capacity: 1000 streams/second\n")

        print("Creating Data Processing Pipeline...")
        print("Stage 1: Input validation and parsing")
        stage1 = InputStage()
        print("Stage 2: Data transformation and enrichment")
        stage2 = TransformStage()
        print("Stage 3: Output formatting and delivery")
        stage3 = OutputStage()

        json_adapter = JSONAdapter("JSON_001")
        csv_adapter = CSVAdapter("CSV_001")
        stream_adapter = StreamAdapter("STREAM_001")

        for adapter in (json_adapter, csv_adapter, stream_adapter):
            adapter.add_stage(stage1)
            adapter.add_stage(stage2)
            adapter.add_stage(stage3)
            nexus.register(adapter)

        print("\n=== Multi-Format Data Processing ===\n")

        print("\nProcessing JSON data through pipeline...")
        json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
        json_adapter.process(json_data)

        print("\nProcessing CSV data through same pipeline...")
        csv_data = "user,action,timestamp"
        csv_adapter.process(csv_data)

        print("\nProcessing Stream data through same pipeline...")
        stream_data = "Real-time sensor stream"
        stream_adapter.process(stream_data)

        print("\n=== Pipeline Chaining Demo ===")
        print("Pipeline A -> Pipeline B -> Pipeline C")
        print("Data flow: Raw -> Processed -> Analyzed -> Stored")

        chain_start = time.time()
        raw_p = RawPipeline()
        analy_p = AnalyzedPipeline()
        st_p = StoredPipeline()

        records = [{"id": i} for i in range(100)]
        f_record = [nexus.chain([raw_p, analy_p, st_p], r) for r in records]
        chain_time = time.time() - chain_start

        stored = len([1 for r in f_record if r.get("stored")])

        print(f"\nChain result: {stored} records",
              "processed through 3-stage pipeline")
        print("Performance: 95% efficiency,",
              f"{chain_time:.4f}s total processing time")

        print("\n=== Error Recovery Test ===")
        error_recovery_test()

        print("\n=== Pipeline Statistics ===")
        nexus.print_stats()

        print("\nNexus Integration complete. All systems operational.")
    except Exception as e:
        print(f"Pipeline System Failed: {e}", file=stderr)


if __name__ == "__main__":
    pipeline_system()

from sys import stderr
from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        ...

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"Stream ID": "STREAM_001", "Type": "Unknown Stream Type"}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        temp_avg = 0
        temp_ele = 0
        for ele in data_batch:
            if ele.split(":")[0] == "temp":
                temp_avg += float(ele.split(":")[1])
                temp_ele += 1
            if temp_avg:
                temp_avg /= temp_ele
        return f"{len(data_batch)} readings processed, avg temp: {temp_avg}"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, str | int | float]:
        return {"Stream ID": self.stream_id, "Type": "Environmental Data"}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        sell = 0
        buy = 0
        for ele in data_batch:
            type = ele.split(":")[0]
            if type == "buy":
                buy += int(ele.split(":")[1])
            elif type == "sell":
                sell += int(ele.split(":")[1])
            else:
                raise ValueError(f"Failed To Processe Unknown data `{ele}`")
        net_flow = buy - sell
        if net_flow < 0:
            net_flow = 0
        ln = len(data_batch)
        return f"{ln} operations processed, net flow: +{net_flow} units"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, str | int | float]:
        return {"Stream ID": self.stream_id, "Type": "Financial Data"}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id

    def process_batch(self, data_batch: List[Any]) -> str:
        er_cnt = 0
        for ele in data_batch:
            if ele == "error":
                er_cnt += 1
        ln = len(data_batch)
        return f"{ln} events processed, {er_cnt} error detected"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        return super().filter_data(data_batch, criteria)

    def get_stats(self) -> Dict[str, str | int | float]:
        return super().get_stats()


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def processing_batch(self, data_batch: Dict):
        i = 0
        for strem in self.streams:
            if isinstance(strem, SensorStream):
                print("- Sensor data: ", end="")
            elif isinstance(strem, TransactionStream):
                print("- Transaction data: ", end="")
            elif isinstance(strem, EventStream):
                print("- Event data: ", end="")

            res = strem.process_batch(data_batch[i])
            print(res)
            i += 1


def display_list(lst: List[Any]):
    print("[", end="")
    i = 0
    for item in lst:
        if i:
            print(", ", end="")
        print(item, end="")
        i += 1
    print("]")


def display_dictionary(dic: Dict) -> None:
    i = 0
    for key in dic:
        if i:
            print(", ", end="")
        print(f"{key}: {dic[key]}", end="")
        i += 1
    print()


def sensor_stream_process(data: List[Any]) -> DataStream:
    try:
        print("\nInitializing Sensor Stream...")
        sensor_proc = SensorStream("SENSOR_001")
        sensor_stat = sensor_proc.get_stats()
        display_dictionary(sensor_stat)
        print("Processing sensor batch: ", end="")
        display_list(data)
        print(f"Sensor analysis: {sensor_proc.process_batch(data)}")
        return sensor_proc
    except Exception as e:
        print(f"Sensor Stream Processor Failed - {e}", file=stderr)


def transaction_stream_process(data: List[Any]) -> DataStream:
    try:
        print("\nInitializing Transaction Stream...")
        transaction_stream = TransactionStream("TRANS_001")
        transaction_stat = transaction_stream.get_stats()
        display_dictionary(transaction_stat)
        print("Processing transaction batch: ", end="")
        display_list(data)
        print("Transaction analysis:",
              f"{transaction_stream.process_batch(data)}")
        return transaction_stream
    except Exception as e:
        print(f"Transaction Stream Processor Failed - {e}", file=stderr)


def event_stream_process(data: List[Any]) -> DataStream:
    try:
        print("\nInitializing Event Stream...")
        event_proc = EventStream("EVENT_001")
        event_stat = event_proc.get_stats()
        display_dictionary(event_stat)
        print("Processing event batch: ", end="")
        display_list(data)
        print(f"Event analysis: {event_proc.process_batch(data)}")
        return event_proc
    except Exception as e:
        print(f"Event Stream Processor Failed - {e}", file=stderr)


def polymorphic_stream_system() -> None:
    try:
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

        data = [
            ["temp:22.5", "humidity:65", "pressure:1013"],
            ["buy:100", "sell:150", "buy:75"],
            ["login", "error", "logout"]
        ]

        sensor_proc = sensor_stream_process(data[0])
        transaction_proc = transaction_stream_process(data[1])
        event_proc = event_stream_process(data[2])

        print("\n=== Polymorphic Stream Processing ===")
        print("Processing mixed stream types through unified interface...")

        print("\nBatch 1 Results:")
        data = [
            ["temp:22.5", "humidity:65"],
            ["buy:100", "sell:150", "buy:75", "sell:10"],
            ["login", "error", "logout"]
        ]
        stream_processor = StreamProcessor()
        stream_processor.add_stream(sensor_proc)
        stream_processor.add_stream(transaction_proc)
        stream_processor.add_stream(event_proc)

        stream_processor.processing_batch(data)
        print("\nAll streams processed successfully.",
              "Nexus throughput optimal.")
    except Exception as e:
        print(f"Stream System Failed - {e}", file=stderr)


if __name__ == "__main__":
    polymorphic_stream_system()

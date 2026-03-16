from typing import Any, List, Dict, Union, Optional
from abc import ABC, abstractmethod
from sys import stderr


class DataStream(ABC):
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        ...

    def filter_data(self, data_batch: List[Any],
                    criteria: Optional[str] = None) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {"<Unknown Type>": "<Unknown Value>"}


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data: Any = None

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            raise ValueError("Can't Processing Empty Data")
        self.data = data_batch
        return f"{len(data_batch)} readings processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        types = [e.split(":")[0] for e in data_batch]
        amounts = [e.split(":")[1] for e in data_batch]
        data_dict = {type: amount for type, amount in zip(types, amounts)}
        if criteria == "temp":
            return [float(data_dict[e]) for e in data_dict if e == "temp"]
        return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        temp_avg = 0
        temp_ele = 0
        for ele in self.data:
            if ele.split(":")[0] == "temp":
                temp_avg += float(ele.split(":")[1])
                temp_ele += 1
            if temp_avg:
                temp_avg /= temp_ele
        return {"avg temp": f"{temp_avg}°C"}


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.sell = 0
        self.buy = 0

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            raise ValueError("Can't Processing Empty Data")
        sell = 0
        buy = 0
        for ele in data_batch:
            tp = ele.split(":")[0]
            if tp == "buy":
                buy += int(ele.split(":")[1])
            elif tp == "sell":
                sell += int(ele.split(":")[1])
            else:
                raise ValueError(f"Failed To Processe Unknown data `{ele}`")
        ln = len(data_batch)
        self.sell = sell
        self.buy = buy
        return f"{ln} operations processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        if criteria == "large":
            amount = [int(e.split(":")[1]) for e in data_batch]
            return [e for e in amount if e > 100]
        return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        flow = self.buy - self.sell
        return {"net flow": f"+{flow} units"}


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
        self.data = None

    def process_batch(self, data_batch: List[Any]) -> str:
        if not data_batch:
            raise ValueError("Failed To Processe Empty Data ")
        ln = len(data_batch)
        self.data = data_batch
        return f"{ln} events processed"

    def filter_data(self, data_batch: List[Any],
                    criteria: str | None = None) -> List[Any]:
        if criteria == "error":
            return [ele for ele in data_batch if ele == "error"]
        return data_batch

    def get_stats(self) -> Dict[str, str | int | float]:
        er_cnt = 0
        for event in self.data:
            if event == "error":
                er_cnt += 1

        return {"error detected": er_cnt}


class StreamProcessor:
    def __init__(self) -> None:
        self.streams: list[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def processing_batch(self, data_batch: Dict) -> List[Any]:
        if not data_batch or self.streams == []:
            raise ValueError("Can't Processing Empty Data")
        return [stm.process_batch(d) for stm, d
                in zip(self.streams, data_batch)]


def display_list(lst: List[Any]) -> None:
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


def sensor_stream_process(data: List[Any]) -> Optional[DataStream]:
    try:
        print("\nInitializing Sensor Stream...")
        sensor = SensorStream("SENSOR_001")
        print(f"Stream ID: {sensor.stream_id}, Type: Environmental Data")
        print("Processing sensor batch: ", end="")
        display_list(data)
        sensor_process = sensor.process_batch(data)
        sensor_stat = sensor.get_stats()
        print(f"Sensor analysis: {sensor_process}, ", end="")
        display_dictionary(sensor_stat)
        return sensor
    except Exception as e:
        print(f"Sensor Stream Processor Failed - {e}", file=stderr)


def transaction_stream_process(data: List[Any]) -> Optional[DataStream]:
    try:
        print("\nInitializing Transaction Stream...")
        transaction_stream = TransactionStream("TRANS_001")
        print(f"Stream ID: {transaction_stream.stream_id},",
              "Type: Financial Data")
        print("Processing transaction batch: ", end="")
        display_list(data)
        transaction_process = transaction_stream.process_batch(data)
        transaction_stat = transaction_stream.get_stats()
        print(f"Transaction analysis: {transaction_process}, ", end="")
        display_dictionary(transaction_stat)
        return transaction_stream
    except Exception as e:
        print(f"Transaction Stream Processor Failed - {e}", file=stderr)


def event_stream_process(data: List[Any]) -> Optional[DataStream]:
    try:
        print("\nInitializing Event Stream...")
        event_proc = EventStream("EVENT_001")
        print(f"Stream ID: {event_proc.stream_id}, Type: System Events")
        print("Processing event batch: ", end="")
        display_list(data)
        event_process = event_proc.process_batch(data)
        event_stat = event_proc.get_stats()
        print(f"Event analysis: {event_process}, ", end="")
        display_dictionary(event_stat)
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

        processing_res = stream_processor.processing_batch(data)
        i = 0
        for stream in stream_processor.streams:
            if isinstance(stream, SensorStream):
                print("- Sensor data: ", end="")
            elif isinstance(stream, TransactionStream):
                print("- Transaction data: ", end="")
            elif isinstance(stream, EventStream):
                print("- Event data: ", end="")
            print(processing_res[i])
            i += 1

        print("\nStream filtering active: High-priority data only")

        criteria = ["temp", "large", "error"]
        filterd_data = [s.filter_data(d, t) for s, d, t in
                        zip(stream_processor.streams, data, criteria)]

        print(f"Filtered results: {len(filterd_data[0])}",
              f"critical sensor alerts, {len(filterd_data[1])}",
              "large transaction")

        print("\nAll streams processed successfully.",
              "Nexus throughput optimal.")
    except Exception as e:
        print(f"Stream System Failed - {e}", file=stderr)


if __name__ == "__main__":
    polymorphic_stream_system()

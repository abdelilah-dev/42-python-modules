from typing import Any, List, Optional
from abc import ABC, abstractmethod
from sys import stderr


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        ...

    @abstractmethod
    def validate(self, data: Any) -> bool:
        ...

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not data:
                raise ValueError("Can't Processing Empty Data")
            ln = 1
            sm = data
            if data.__class__ == [].__class__:
                ln = len(data)
                sm = sum(data)
            avg = sm / ln
            process = f"Processed {ln} numeric values, sum={sm}, avg={avg:.1f}"
            return process
        except (TypeError, ZeroDivisionError, ValueError) as error:
            print("[ERROR] - Failed To Processing Numeric data",
                  f"{data}: {error}",
                  file=stderr)

    def validate(self, data: Any) -> bool:
        if data.__class__ == (0).__class__:
            return True
        if data.__class__ == [].__class__:
            for item in data:
                if item.__class__ != (0).__class__:
                    return False
            return True
        else:
            return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not data:
                raise ValueError("Can't Processing Empty Data")
            ln = len(data)
            words = len(data.split(" "))
            return f"Processed text: {ln} characters, {words} words"
        except (TypeError, ValueError) as error:
            print("[ERROR] Failed To Processing Text data",
                  f"\"{data}\": {error}",
                  file=stderr)

    def validate(self, data: Any) -> bool:
        if data.__class__ == "".__class__:
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not data:
                raise ValueError("Can't Processing Empty Data")
            log_level = data.split(" ")[0]
            msg = None
            for item in data.split(" ")[1:]:
                if not msg:
                    msg = item
                else:
                    msg = msg + " " + item
            if log_level == "ERROR:":
                proc_result = f"[ALERT] ERROR level detected: {msg}"
            elif log_level == "INFO:":
                proc_result = f"[INFO] INFO level detected: {msg}"
            elif log_level == "WARNING:":
                proc_result = f"[WARNING] WARN level detected: {msg}"

            return proc_result
        except ValueError as error:
            print(f"[ERROR] Failed To Processing log data \"{data}\": {error}",
                  file=stderr)

    def validate(self, data: Any) -> bool:
        log_level = data.split(" ")[0]
        if (log_level == "ERROR:" or
           log_level == "INFO:" or log_level == "WARNING:"):
            return True
        return False

    def format_output(self, result: str) -> str:
        return super().format_output(result)


def processing_numeric_data(data: Any) -> DataProcessor:
    try:
        print("\nInitializing Numeric Processor...")
        num_proc = NumericProcessor()
        print(f"Processing data: {data}")
        if num_proc.validate(data):
            print("Validation: Numeric data verified")
            output = num_proc.process(data)
            print(num_proc.format_output(output))
        else:
            print("Validation: Numeric data unverified!!")
            print(num_proc.format_output("Can't Processing Unverified Data"))
    except Exception as error:
        print(f"[ERROR] - Processing Numeric Data Problem: {error}",
              file=stderr)
    return num_proc


def processing_text_data(data: Any) -> DataProcessor:
    try:
        print("\nInitializing Text Processor...")

        text_proc = TextProcessor()
        print(f"Processing data: \"{data}\"")
        if text_proc.validate(data):
            print("Validation: Text data verified")
            output = text_proc.process(data)
            print(text_proc.format_output(output))
        else:
            print("Validation: Text data unverified!!")
            print(text_proc.format_output("Can't Processing Unverified Data"))
    except Exception as error:
        print(f"[ERROR] - Processing Text Data Problem: {error}", file=stderr)
    return text_proc


def processing_logs(data: Any) -> DataProcessor:
    try:
        print("\nInitializing Log Processor...")

        log_proc = LogProcessor()
        print(f"Processing data: \"{data}\"")
        if log_proc.validate(data):
            print("Validation: Log entry verified")
            output = log_proc.process(data)
            print(log_proc.format_output(output))
        else:
            print("Validation: Log entry unverified")
            print(log_proc.format_output("Can't Processing Unverified Data"))
        return log_proc
    except Exception as error:
        print(f"[ERROR] - Processing logs Problem: {error}", file=stderr)
    return log_proc


def data_processor() -> None:
    try:
        print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
        num_proc = processing_numeric_data([1, 2, 3, 4, 5])
        txt_proc = processing_text_data("Hello Nexus World")
        log_proc = processing_logs("ERROR: Connection timeout")

        print("\n=== Polymorphic Processing Demo ===")
        processors = [num_proc, txt_proc, log_proc]
        data: Optional[List | str] = [
            [1, 2, 3, 4, 5],
            "Hello Nexus World",
            "INFO: System ready"
        ]
        i = 0
        for proc in processors:
            result = proc.process(data[i])
            if result:
                print(f"Result {i + 1} {proc.process(data[i])}")
            i += 1
        print("\nFoundation systems online. Nexus ready for advanced streams.")
    except Exception as error:
        print(f"[ERROR] - Data Processor System Failed: {error}", file=stderr)


if __name__ == "__main__":
    data_processor()

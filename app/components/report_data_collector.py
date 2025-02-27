from lxml import etree
import csv
from enum import Enum


class Fields(Enum):
    NAME = "Name"
    TOTAL = "Total"
    FAILED = "Failed"
    FAILED_RATE = "Rate"


class DataRecord:
    def __init__(self, name: str, total_tests: int, failed: int, errors: int, skipped: int):
        self.name = name
        self.total = total_tests - skipped
        self.failed = failed + errors
        self.failure_rate = (self.failed / self.total) * 100

    def to_string(self):
        return f"Suite: {self.name},\nTotal tests: {self.total}\nFailed: {self.failed}\nFailed Rate: {self.failure_rate:.2f}\n"

    def to_map(self):
        return {Fields.NAME.value: self.name, Fields.TOTAL.value: self.total, Fields.FAILED.value: self.failed,
                Fields.FAILED_RATE.value: f"{self.failure_rate: .2f}"}


class DataCollector:

    def __init__(self, xpath: str):
        self.collection = []
        self.xpath = xpath

    def process_report_file(self, report_file):
        xml = etree.parse(report_file)
        suites = xml.xpath(self.xpath)
        for suite in suites:
            record = DataRecord(
                suite.attrib['name'],
                int(suite.attrib['tests']),
                int(suite.attrib['failures']),
                int(suite.attrib['errors']),
                int(suite.attrib['skipped'])
            )
            self.collection.append(record)

    def print_report(self):
        self.create_summary_record()
        print("==================================")
        for record in self.collection:
            print(record.to_string())

    def create_summary_record(self):
        if self.collection[len(self.collection) - 1].name == str(Fields.TOTAL.value):
            return
        total = 0
        failed = 0
        for record in self.collection:
            total = total + record.total
            failed = failed + record.failed
        self.collection.append(DataRecord(str(Fields.TOTAL.value), int(total), int(failed), int(0), int(0)))

    def to_csv_file(self, file_full_name):
        self.create_summary_record()
        with open(file_full_name, 'w', newline='') as csvfile:
            field_names = [Fields.NAME.value, Fields.TOTAL.value, Fields.FAILED.value, Fields.FAILED_RATE.value]
            writer = csv.DictWriter(csvfile, field_names)
            writer.writeheader()
            for record in self.collection:
                writer.writerow(record.to_map())
        csvfile.close()

    def main(self):
        print("Here it is")

    if __name__ == '__main__':
        obj = DataCollector()
        obj.main()
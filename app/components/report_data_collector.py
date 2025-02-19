from lxml import etree
import csv
from enum import Enum


class Fields(Enum):
    NAME = "Name",
    TOTAL = "Total",
    FAILED = "Failed",
    FAILED_RATE = "Rate"


class DataRecord:
    def __init__(self, name: str, total_tests: int, failed: int, errors: int, skipped:int):
        self.name = name
        self.total = total_tests - skipped
        self.failed = failed + errors
        self.failure_rate = (self.failed/self.total)*100

    def to_string(self):
        return f"Suite: {self.name},\nTotal tests: {self.total}\nFailed: {self.failed}\nFailed Rate: {self.failure_rate}\n"

    def to_map(self):
        return {Fields.NAME: self.name, Fields.TOTAL: self.total, Fields.FAILED: self.failed, Fields.FAILED_RATE: self.failure_rate}

class DataCollector:

    def __init__(self, xpath:str):
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
            self.collection.append(record.to_map())

    def print_report(self):
        for record in self.collection:
            print(record)

    # def to_csv_file(self, file_full_name):
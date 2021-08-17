from abc import ABC, abstractmethod
import csv
import os.path


class DataHandler(ABC):
    """
    Общий Класс для обработки хранимых данных
    """
    @staticmethod
    @abstractmethod
    def get_data_from(file: str) -> dict:
        raise NotImplementedError


class CSVHandler(DataHandler):
    """
    Класс для обработки хранимых данных для csv формата
    """
    @staticmethod
    def get_data_from(file: str) -> dict:
        if not os.path.isfile(file):
            raise Exception('No data storage')
        result_dict = {}
        with open(file) as csv_file:
            reader = csv.reader(csv_file, delimiter=';')
            for row in reader:
                result_dict[row[0]] = {'show_count': int(row[1]), 'categories': row[2:]}

        return result_dict

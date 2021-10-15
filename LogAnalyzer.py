import abc

'''
# 情境1: 先做一個手刻假物件
# 情境2: 改用隔離框架
'''


class ILogger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def logError(errMsg: str) -> None:
        pass


class LogAnalyzer:
    def __init__(self, logger: ILogger) -> None:
        self.minNameLength = 5
        self.__logger__ = logger
        pass

    def analyze(self, fileName: str):
        if(len(fileName) < self.minNameLength):
            self.__logger__.logError('too short')

        pass

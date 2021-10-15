import abc

'''
# 情境1: 先做一個手刻假物件
# 情境2: 改用隔離框架
# 情境3: 用隔離框架, 模擬有回傳值的方法
'''


class ILogger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def logError(errMsg: str) -> None:
        pass


class IFileNameRules(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def isValidLogFileName(fileName: str) -> bool:
        pass


class LogAnalyzer:
    def __init__(self, logger: ILogger, rulesUtil: IFileNameRules = None) -> None:
        self.minNameLength = 5
        self.__logger__ = logger
        self.__rulesUtil__ = rulesUtil
        pass

    def validSomeRules(self, fileName: str):
        return self.__rulesUtil__.isValidLogFileName(fileName)

    def analyze(self, fileName: str):
        if(len(fileName) < self.minNameLength):
            self.__logger__.logError('too short')

        pass

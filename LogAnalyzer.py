import abc

'''
# 情境1: 先做一個手刻假物件
# 情境2: 改用隔離框架
# 情境3: 用隔離框架, 模擬有回傳值的方法
# 情境4:
    # 同時使用 虛設常式與模擬物件 兩個假物件
    # log 紀錄拋出例外
    # Anylazer 接收例外後, 呼叫 webService 方法
'''


class ILogger(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def logError(errMsg: str) -> None:
        pass


class IFileNameRules(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def isValidLogFileName(fileName: str) -> bool:
        pass


class IWebService(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def write(errMsg: str) -> None:
        pass


class LogAnalyzer:
    def __init__(self, logger: ILogger, rulesUtil: IFileNameRules = None, webService: IWebService = None) -> None:
        self.minNameLength = 5
        self.__logger__ = logger
        self.__rulesUtil__ = rulesUtil
        self.__webService__ = webService
        pass

    def validSomeRules(self, fileName: str):
        return self.__rulesUtil__.isValidLogFileName(fileName)

    def analyze(self, fileName: str):
        if(len(fileName) < self.minNameLength):
            try:
                self.__logger__.logError('too short')
            except Exception as e:
                self.__webService__.write('mocked log error')

        pass

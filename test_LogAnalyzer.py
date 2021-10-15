import pytest

from LogAnalyzer import ILogger, LogAnalyzer


# class FakeLogger(ILogger):
#     lastError = ""

#     def logError(self, errMsg: str) -> None:
#         self.lastError = errMsg
#         pass


def test_analyze_tooShortFileName_callLogger(mocker):
    # logger = FakeLogger()

    # mock class (use full path of namespace)
    logger = mocker.patch('LogAnalyzer.ILogger')

    # fake method of mock class
    moker_method = mocker.patch.object(logger, 'logError')

    # fake variable of mock class (only demo)
    mocker.patch.object(logger, 'lastError', 'too short')
    analyzer = LogAnalyzer(logger)
    analyzer.minNameLength = 6
    analyzer.analyze('a.txt')
    assert moker_method.called == True  # chack calld

    # 以前去驗證方法有沒有被呼叫, 所以可以去掉(mock 框架已提供了驗證方法). 為了方便說明所以用 mark
    # assert 'too short' == logger.lastError

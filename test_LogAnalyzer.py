import pytest

from LogAnalyzer import ILogger, LogAnalyzer


class FakeLogger(ILogger):
    lastError = ""

    def logError(self, errMsg: str) -> None:
        self.lastError = errMsg
        pass


def test_analyze_tooShortFileName_callLogger():
    logger = FakeLogger()
    analyzer = LogAnalyzer(logger)
    analyzer.minNameLength = 6
    analyzer.analyze('a.txt')
    assert 'too short' == logger.lastError

import pytest

from api import *


class Test_Api:
    # test that the status code is successful when searching for the word ignore (the word ignore exists in website.).
    def test_status_ignore(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/ignore'
        req = http_request(url)
        actual = status(req)
        expected = True
        assert actual == expected

    # test that the status code is failure when searching for the word yauoza.(the word yauoza does not exist in website.)
    def test_status_yauoza_N(self):
        url = 'https://api.dictionaryapi.dev/api/v2/entries/en/yauoza'
        req = http_request(url)
        actual = status(req)
        expected = False
        assert actual == expected

    # test that the word you look up, appears in the body webpage.
    def test_word_in_body(self):
        actual = search_and_find_word_in_body("human")
        expected = True
        assert actual == expected





import pytest
from api.api import IpApi

ia = IpApi()


@pytest.mark.parametrize('test', [
    '8.8.8.8',          # google dns
    '5.255.255.70'])    # yandex.ru
def test_request_working(test):
    """ Проверяем запрос api с корректными и рабочими ip """
    status, result = ia.check_ipapi_full(test)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert "error" not in result


@pytest.mark.parametrize('test', [
    '10.8.8.8',         # Private network
    '127.0.0.1',        # localhost
    '169.254.2.4',      # Subnet
    '203.0.113.0'])     # Assigned as TEST-NET-3, documentation and examples.
def test_request_reserved(test):
    """ Проверяем запрос api с зарезервированными ip """
    status, result = ia.check_ipapi_full(test)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert "error" in result
    assert result["reason"] == 'Reserved IP Address'


@pytest.mark.parametrize('test', [
    'a.8.8.8',
    '.0.1',
    '69...4',
    'sdfgygfhj'])
def test_request_not_correct(test):
    """ Проверяем запрос api с зарезервированными ip """
    status, result = ia.check_ipapi_full(test)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert "error" in result
    assert result["reason"] == 'Invalid IP Address'


@pytest.mark.parametrize('test', [
    'city',
    'region',
    'timezone',
    'utc_offset'])
def test_request_field_correct(test):
    """ Проверяем запрос к отдельным полям ответа api к DNS Google"""
    status, result = ia.check_ipapi_field("8.8.8.8", test)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 200
    assert len(result) > 0


@pytest.mark.parametrize('test', [
    'cityedgf',
    '*',
    '////45',
    '123/json'])
def test_request_field_incorrect(test):
    """ Проверяем запрос к отдельным полям ответа api к DNS Google"""
    status, result = ia.check_ipapi_field("8.8.8.8", test)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 404    # URL not found


# def test_request_daily_limit():
#     """ Проверяем запрос к api после превышения дневного лимита запросов
#     ОСТОРОЖНО - примерно 1000 запросов (~5-10мин), дальнейшие проверки в этот день не будут работать"""
#     while True:
#         status, result = ia.check_ipapi_field("8.8.8.8", 'city')
#         if status == 429:
#             break
#     # Сверяем полученные данные с нашими ожиданиями
#     assert status == 429
#     assert result["reason"] == 'RateLimited'

import json
import requests
from serializers.ip_response import IPResponse


class IpApi:
    """API сайта https://ipapi.co"""

    def __init__(self):
        self.base_url = "https://ipapi.co/"

    def check_ipapi_full(self, ip: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате JSON,
         кроме того проводит валидацию JSON-ответа"""

        res = requests.get(self.base_url + ip + "/json/")
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        # проверка необходимости валидации - вернулся JSON с полными данными
        if status == "200" and "error" not in result:
            result = IPResponse(**result)

        return status, result

    def check_ipapi_field(self, ip: str, suffix: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат"""

        res = requests.get(self.base_url + ip + '/' + suffix + '/')
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text

        return status, result

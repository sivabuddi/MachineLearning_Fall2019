from requests import get
from requests.exceptions import RequestException
from contextlib import closing


def validate_web_page_response(response):
    html_type = response.headers['Content-Type']
    return (response.status_code == 200
            and html_type is not None
            and html_type.lower().find('html') > -1)


def read_web_page(web_url):
    try:
        with closing(get(web_url, stream=True)) as response:
            if validate_web_page_response(response):
                return response.content
            else:
                return None

    except RequestException as requestException:
        print("Exception raised {0} - {1}".format(web_url, str(requestException)))
        return None

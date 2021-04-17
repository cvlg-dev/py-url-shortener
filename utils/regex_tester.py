import re

url_pattern = re.compile(r"(http|ftp|https)://([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:/~+#-]*[\w@?^=%&/~+#-])?")

def test_url_regex_pattern(url: str, pattern: re.compile=url_pattern)-> str:
    """

    :param url:
    :param pattern:
    :return:
    """

    match = re.match(url_pattern, url)
    if match is not None:
        return match.group()
    else:
        return None

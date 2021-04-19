import re


REQUEST_TYPE = 'GET'
REQUEST_RETURN = 'style.css'
REQUEST_RESPONSE = r'2\d\d'
REQUEST_FROM = r'22/Mar/2009:07:40:06'
REQUEST_TO = r'30/Mar/2009:13:43:28'


REQUEST_TIMERANGE = r'\[(22/Mar/2009:(0[7-9]|1\d|2[0-3]):[45]\d:(0[6-9]|[1-5]\d)|' \
                    r'2[3-9]/Mar/2009:\d\d:\d\d:\d\d|' \
                    r'30/Mar/2009:(0\d|1[1-3]):([0-3]\d|4[0-3]):([01]\d|2[0-8])) \+\d{4}]'


def main():
    count = 0
    pattern = re.compile(r'.*' + REQUEST_TIMERANGE + r'.*' + REQUEST_TYPE + r' /' + REQUEST_RETURN + r' .*'
                         + REQUEST_RESPONSE + r' .*')
    with open('access.log', 'r') as f:
        contents = f.read()
        matches = pattern.finditer(contents)
        for match in matches:
            print(match.group(0))
            count += 1
        print(count)
    f.close()


if __name__ == '__main__':
    main()

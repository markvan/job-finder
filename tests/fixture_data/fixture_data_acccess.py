# convert url to appropriate file name depending on page query
def file_name_from_url(url):
    files = {
        '1': '../../tests/fixture_data/multi_page_1.html',
        '2': '../../tests/fixture_data/multi_page_2.html',
        '3': '../../tests/fixture_data/multi_page_3.html',
    }
    url_ending = url[-7:]
    if not (url_ending=='&page=2' or url_ending=='&page=3'):
        page_number_char = '1'
    else:
        page_number_char = url[-1:]
    return files.get(page_number_char)


# get the html from a file depending on page query
# this is used in monkeypatching to mock http resquest during testing
def page_source_from_file_name(would_be_self, url):
    print("**************------------------*****************"+url)
    with open(file_name_from_url(url), 'r') as content_file:
        content = content_file.read()
    return content

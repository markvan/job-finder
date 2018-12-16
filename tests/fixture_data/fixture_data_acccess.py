def single_page(would_be_self):
    with open('../../tests/fixture_data/single_page.html', 'r') as content_file:
        content = content_file.read()
    return content


print(single_page(1))

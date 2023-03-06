class Config:
    url = 'https://wikipedia.org'
    url_1 = 'wiki'



class Wikipedia:
    url_2 = 'World war 1'
    search_field_id = 'searchInput'
    search_button_id = '//*[@id="search-form"]/fieldset/button'
    expected_element = 'Verden'

    def __init__(self, url):
        self.url = f'{url}'
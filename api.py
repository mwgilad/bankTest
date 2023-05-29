import requests

#request access the Api code of a website
def http_request(url):
    res = requests.get(url)
    return res

# return True if the status of the website passed 200-399 and False if Failed 400-599
def status(request_url):
    if 200 <= request_url.status_code <400:
        print(f'Success : {request_url.status_code}')
        return True
    else:
        print(f'FAILED : {request_url.status_code}')
        return False

# look up a word and search for that word in the body of the webpage to see if it appears.
def search_and_find_word_in_body(word):
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}'
    req = http_request(url).text
    if word in req:
        return True
    else:
        return False


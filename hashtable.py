#hash table for voters
voted = {}

def check_voter(name):
    if voted.get(name):
        print ("refuse vote")
    else:
        voted[name] = True
        print ("allow voting")

check_voter("Shola")
check_voter("Shola")
check_voter("Baxton")

#hash table that checks if a url is cached
# if not server runs and returned data is cached
cache = {}

def get_page(url):
    if cache.get(url):
        return cache(url)
    else:
        data = get_data_from_server(url)
        cache[url] = data
        return data
import urllib.parse as up
import urllib.request as ur
import json
import gzip
from io import BytesIO

WORDS_1 = ['pneumatico', 'volante', 'freno a mano']

def get_indexes_by_word(word):
    service_url = 'https://babelnet.io/v6/getSynsetIds'

    lemma = word
    lang = 'IT'
    key  = '5da132f9-c606-4832-9a4f-3c2e3f739cf7'

    params = {
            'lemma' : lemma,
            'searchLang' : lang,
            'key'  : key
    }

    url = service_url + '?' + up.urlencode(params)
    request = ur.Request(url)
    request.add_header('Accept-encoding', 'gzip')
    response = ur.urlopen(request)

    if response.info().get('Content-Encoding') == 'gzip':
            buf = BytesIO( response.read())
            f = gzip.GzipFile(fileobj=buf)
            data = json.loads(f.read())
            for result in data:
                    return result['id']


def get_synset_by_id(id):
    service_url = 'https://babelnet.io/v6/getSynset'

    key  = '5da132f9-c606-4832-9a4f-3c2e3f739cf7'

    params = {
        'id' : id,
        'key'  : key,
        'targetLang' : 'IT'
    }

    url = service_url + '?' + up.urlencode(params)

    request = ur.Request(url)
    request.add_header('Accept-encoding', 'gzip')
    response = ur.urlopen(request)
    
    if response.info().get('Content-Encoding') == 'gzip':
        buf = BytesIO(response.read())
        f = gzip.GzipFile(fileobj=buf)
        data = json.loads(f.read())

        # retrieving BabelSense data
        senses = data['senses']
        for result in senses:
            lemma = result.get('lemma')
            language = result.get('language')
            if language != None:    
                print(str(language.encode('utf-8')) + "\t" + str(lemma.encode('utf-8')))

        print('\n')
        # retrieving BabelGloss data
        glosses = data['glosses']
        for result in glosses:
            gloss = result.get('gloss')
            language = result.get('language')
            if language != None:
                print(str(language.encode('utf-8')) + "\t" + str(gloss.encode('utf-8')))

        print('\n')

index = get_indexes_by_word("mela")
print(index)
if index != []:
    get_synset_by_id(index)
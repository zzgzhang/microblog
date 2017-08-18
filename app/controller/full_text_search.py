from whoosh.fields import TEXT, Schema
from whoosh.index import create_in, open_dir
from whoosh.qparser import QueryParser
from app import app
from os import mkdir

def create_index(user_id, post_id, nickname, post_body):
    schema = Schema(user_id=TEXT(stored=True), post_id=TEXT(stored=True), nickname=TEXT(stored=True), content=TEXT(stored=True))
    try:
        ix = open_dir(app.config['WHOOSH_BASE'])
    except:
        mkdir(app.config['WHOOSH_BASE'])
        ix = create_in(app.config['WHOOSH_BASE'], schema)

    writer = ix.writer()
    writer.add_document(user_id=str(user_id), post_id=str(post_id), nickname=nickname, content=post_body)
    p = writer.commit()

def query(key):
    rt = []
    try:
        ix = open_dir(app.config['WHOOSH_BASE'])
        with ix.searcher() as searcher:
            query_key =  QueryParser('content', ix.schema).parse(key)
            results = searcher.search_page(query_key, 1, app.config['MAX_SEARCH_RESULTS'], sortedby='post_id', reverse=True)
            #results = searcher.search(query_key)

            for item in results:
                user_id = item.fields()['user_id']
                post_id = item.fields()['post_id']
                nickname = item.fields()['nickname']
                post_body = item.fields()['content']
                rt.append({'user_id': int(user_id), 'post_id' : int(post_id), 'nickname' : nickname, 'post_body' : post_body})
    except:
        print('there is no post exist!')
    finally:
        return rt

if __name__ == '__main__':
    #create_index('wzy', 1, 'Kevin', 'This is first documents!')
    #create_index('wzy', 2, 'Kevin', 'This is second documents, two!')
    rt = query('weather')
    print(rt)

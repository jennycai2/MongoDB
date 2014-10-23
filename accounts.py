def get_db(db_name):
    from pymongo import MongoClient
    client = MongoClient('localhost:27017')
    db = client[db_name]
    return db


def porsche_query():
    # Please fill in the query to find all autos manuafactured by Porsche
    query = {}
    return query


def find_porsche(db, query):
    return db.autos.find(query)


if __name__ == "__main__":

    db = get_db('examples')
    query = porsche_query()
    p = find_porsche(db, query)
    import pprint
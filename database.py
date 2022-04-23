import sqlite3

class DB:

    DATABASE=None
    client=None


    @staticmethod
    def init():
        client = sqlite3.connect('flask_tutorial.db')
        DB.DATABASE = client.cursor()
        return 'done'

    @staticmethod
    def insert(tablename,):
        query=''''''
        DB.DATABASE.execute()

    @staticmethod
    def get_one(collection, query):
        query=''''''
        return DB.DATABASE.execute(query).fetchone()

    @staticmethod
    def get_all(collection, objID, data, upsert=True):
        return DB.DATABASE[collection].find_one_and_update({"_id": objID}, {"$set": data}, upsert=upsert)

    @staticmethod
    def findone_proj(collection, query, project):
        return DB.DATABASE[collection].find_one(query, project)

    @staticmethod
    def findmany(collection, query, project):
        mali = DB.DATABASE[collection].find(query, project)
        return mali

    @staticmethod
    def findall_proj(collection, myli, project):
        boo = [i for i in DB.DATABASE[collection].find({"_id": {"$in": myli}}, project)]
        return boo

    @staticmethod
    def findany_proj(collection, field, myli, project):
        boo = [i for i in DB.DATABASE[collection].find({field: {"$in": myli}}, project)]
        return boo

    @staticmethod
    def find_searches(collection, qry, proj):
        boo = [i for i in DB.DATABASE[collection].find(qry, proj, limit=20)]
        return boo

    @staticmethod
    def find_and_update(collection, objID, data, upsert=True):
        boo = DB.DATABASE[collection].update_one({"_id": objID}, {"$addToSet": data}, upsert=upsert)
        return boo

    @staticmethod
    def bulk_change(collection, opertns, orderd):
        boo = DB.DATABASE[collection].bulk_write(opertns, ordered=orderd)
        return boo

    @staticmethod
    def aggregate(collection, pipeline):
        boo = DB.DATABASE[collection].aggregate(pipeline)
        return boo

    @staticmethod
    def delete_one(collection, id):
        boo = DB.DATABASE[collection].delete_one({"_id": id})
        return boo

    @staticmethod
    def db_close():

        if DB.client is not None:
            DB.client.close()
            DB.DATABASE.close()
        else:
            pass


















import graphene
import pymongo
import json

from config import db_url

print(db_url)


class SongType(graphene.ObjectType):
    rank = graphene.Int()
    title = graphene.String()
    artist = graphene.String()


class ChartType(graphene.ObjectType):
    date = graphene.String()
    BUGS = graphene.List(SongType)
    GENIE = graphene.List(SongType)
    MELON = graphene.List(SongType)
    NAVER = graphene.List(SongType)


class Query(graphene.ObjectType):
    chart = graphene.List(ChartType)

    def resolve_chart(self, info, **kwargs):
        client = pymongo.MongoClient(db_url)
        db = client.get_database('test')
        collection = db.get_collection('charts')

        return list(collection.find().sort('date', pymongo.DESCENDING).limit(24))


schema = graphene.Schema(query=Query)

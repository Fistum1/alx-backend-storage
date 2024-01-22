#!/usr/bin/env python3
"""
It changes a school topics
"""


def update_topics(mongo_collection, name, topics):
    """
    It changes all topics of a school
     document based on the name

    :param mongo_collection:
    :param name:
    :param topics:
    :return:
    """
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})

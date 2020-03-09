import uuid
from database import Database
import datetime

__author__ = "laurenbanawa"

# The arguments that go into the Post are objects, something that models a real-life thing
# the class defines that the properties exist
class Post(object):

    def __init__(self, blog_id, title, content, author, date=datetime.datetime.utcnow(), id=None):
        # all the things that go into a post
        # this function/method allows customization of the components of ea post so they don't have to be the same
        # title, content, etc. are properties
        # we set the values of the properties by the arguments we pass in
        # default value of id is None (helpful tip: can only have default parameters at the end)
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.created_date = date
        # Mongodb uses the property "id" for storage
        # uuid is the and stands for unique identifier -- uuid4 is a method that generates a new random id for ea post
        # .hex gives us a 32 character string
        self.id = uuid.uuid4().hex if id is None else id

    def save_to_mongo(self):
        # a stored action to put data in the mongo database
        Database.insert(collection='posts',
                        data=self.json())

    def json(self):
        # Mongodb only stores json data, so we need to represent our objects in json to allow for storage in mongodb
        # pymongo library converts python dictionaries to json
        return {
            'id': self.id,
            'blog_id': self.id,
            'author': self.author,
            'content': self.content,
            'title': self.title,
            'created_date': self.created_date
        }

    @classmethod
    # get a post from an id
    def from_mongo(cls, id):
        post_data = Database.find_one(collection='posts', query={'id': id})
        return cls(blog_id=post_data['blog_id'],
                   title=post_data['title'],
                   content=post_data['content'],
                   author=post_data['author'],
                   date=post_data['created_date'],
                   id=post_data['id'])

    @staticmethod
    # get all the posts from a specific blog
    def from_blog(id):
        return [ post for post in Database.find(collection='posts', query={'blog_id': id})]
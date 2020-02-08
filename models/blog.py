## Import libraries
import uuid
import datetime
from database import Database
from models.post import Post

## Blog Class
class Blog(object):

    def __init__(self, author, title, description, id=None):
        self.author = author
        self.title = title
        self.description = description
        self.id = uuid.uuid4().hex if id is None else id

    def new_post(self):
        """Allows user to create a new post with title and content"""
        title = input("Enter Post Title: ")
        content = input("Enter Post Content: ")
        date = input("Enter Post Date (DDMMYYYYY), or leave blank for today:")

        if date == "":
            date=datetime.datetime.utcnow()
        else:
            date=datetime.datetime.strptime(date, "%d%m%Y")

        post = Post(blog_id=self.id,
                    title=title,
                    content=content,
                    author=self.author,
                    date=date)

        post.save_to_mongo()

    def get_posts(self):
        """Retrieve posts associated with the given blog"""
        return Post.from_blog(self.id)

    def save_to_mongo(self):
        """Save blog details to mongo blogs collection"""
        Database.insert(collection='blogs',
                        data=self.json())

    def json(self):
        """JSON model for our application to mongo"""
        return {
            'author': self.author,
            'title': self.title,
            'description': self.description,
            'id': self.id
        }

    @classmethod
    def from_mongo(cls, id):
        """Retrieve our data from mongo based on supplied blog id"""
        blog_data = Database.find_one(collection='blogs',
                                      query={'id': id})

        return cls(author=blog_data['author'],
                    title=blog_data['title'],
                    description=blog_data['description'],
                    id=blog_data['id'])
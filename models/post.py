## Import libraries
from database import Database

## Post Class
## Used to place blog posts into our mongo instance
class Post():

    def __init__(self, blog_id, title, content, author, post_id, created_date):
        self.blog_id = blog_id
        self.title = title
        self.content = content
        self.author = author
        self.post_id = post_id
        self.created_date = created_date

    def save_to_mongo(self, json):
        Database.insert(collections='posts', data=self.json())

    def json(self):
        """Create JSON representation of the blog post"""
        return {
            'id': self.post_id,
            'blog_id': self.blog_id,
            'author': self.author,
            'title': self.title,
            'content': self.content,
            'created_date': self.created_date
        }
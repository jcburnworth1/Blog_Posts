## Import libraries
from database import Database
from models.post import Post

## Initilize Database
Database.intialize()

## Create post object
post = Post('Title Post','Content Post','Author Post')

print(post.title)
print(post.author)
print(post.content)
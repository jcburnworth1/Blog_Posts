## Import libraries
from database import Database
from models.blog import Blog

## Menu Class
class Menu(object):

    def __init__(self):
        self.user = input("Enter your author name: ")
        self.user_blog = None

        if self._user_has_account():
            print("Welcome back {0}".format(self.user))
        else:
            self._prompt_user_for_account()

    ## Private method to check user account
    def _user_has_account(self):
        """Check is user has already signed up for blogs"""
        blog = Database.find_one('blogs', {'author': self.user})

        if blog is not None:
            self.user_blog = Blog.from_mongo(blog['id'])
            return True
        else:
            return False

    ## Private method to add a new user
    def _prompt_user_for_account(self):
        """Prompt if user is not already in our database"""
        title = input("Enter Blog Title: ")
        description = input("Enter Blog Description: ")
        blog = Blog(author=self.user,
                    title=title,
                    description=description)
        blog.save_to_mongo()
        self.user_blog = blog

    ## Will launch the menu to read or write blog posts
    def run_menu(self):
        """Ask user if they want to read or write once they have logged in"""
        read_or_write = input("Do you want to read (R) or write (W) blogs?")

        if read_or_write == "R":
            self._list_blogs() ## List blogs
            # self._view_blogs() ## Allow user to pick one
        elif read_or_write == "W":
            self.user_blog.new_post()
        else:
            print("Thank you for blogging!")

    def _list_blogs(self):
        """Look into mongo and retrieve all posts associated with user"""
        blogs = Database.find(collection='blogs', query={})

        for blog in blogs:
            print("ID: {}, Title: {}, Author: {}".format(blog['id'], blog['title'], blog['author']))

    def _view_blogs(self):
        """Retrieve the post details"""
        blog_to_see = input("Enter the ID of the blog you'd like to read:" )
        blog = Blog.from_mongo(blog_to_see)
        posts = blog.get_posts()

        for post in posts:
            print("Date: {}, Title: {}\n\n{}".format(post['created_date'], post['title'], post['content']))
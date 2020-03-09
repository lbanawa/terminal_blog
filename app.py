from database import Database
#from models.post import Post
from menu import Menu
from models.blog import Blog

__author__ = "laurenbanawa"

Database.initialize()

# TO MAKE A NEW POST
#post = Post(blog_id='123',
            #title='Another great post',
            #content='This is some sample content',
            #author='Jose')

#post.save_to_mongo()
# in the terminal use db.posts.find({}).pretty() to see if the post is in the database


# TO FIND A POST WITHIN THE PROGRAM
#post = Post.from_mongo('167c45c979d44a5e83c5feeab347e1f3') # input the id of the post
#print(post)
# can also do post = Post.from_blog() -- just enter in the blog_id
#   from post in posts:
#      print (post) -- for loop to find and print all the posts from the blog

#blog = Blog(author='Jose',
            #title='Sample title',
            #description='Sample description')

#blog.new_post()

#blog.save_to_mongo()

#from_database = Blog.from_mongo(blog.id)

#print(blog.get_posts()) # equivalent to post.from_blog(id)

menu = Menu()

menu.run_menu()
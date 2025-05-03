from typing import List
from pydantic import BaseModel

# Define the output format as a Pydantic model
class Post(BaseModel):
	post_title: str
	post_url: str
	num_comments: int
	hours_since_post: int
	register_status: str
	logout_status: str
	login_status: str
	confirmation_message: str

class Posts(BaseModel):
	posts: List[Post]



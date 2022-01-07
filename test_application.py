# File hello_world.py:
def hello():
	return "Hello, World!"

# File helloworld.py:
def hello():
	return "Hello, World!"

# File callhelloworld.py:	
import hello_world
import helloworld

hello_world.hello()
helloworld.hello()

import requests
import os

class FBGraphInspector:
	def __init__(self, helmet_id):
		self.helmet_id = helmet_id

	def inspect(self):
		# build url with {helmet_id}
		# get app access token
		self.__get_app_access_token()
		# get object id and number of shares 
		# get number of likes
		# update zodinet api
		pass 

	def __get_app_access_token(self):
		# call api to get access_token
		# set self.access_token = token
		res = requests.get('https://graph.facebook.com/v2.7/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials'
			.format(self.__get_env("CLIENT_ID"), self.__get_env("CLIENT_SECRET")))
		self.access_token = res.json().get('access_token')
		pass

	def __get_object_id(self):
		# no acess_token required
		# get share number over link
		# extract open-graph object ID: og_id
		pass

	def __get_likes(self):
		# get like with submitting of access_token 
		pass 

	def __update_zodinet_api(self):
		# {helmet: "id"}
		pass

	def __get_env(self, key):
		return os.environ[key]

class MyCronJob:
	def __init_(self):
		pass

	def start_job(self):
		# Get list of helmet ids from zodinet API
		# Inspect likes/shares on each ID then update Zodient API
		# Aggregate report to Rollbar
		pass

if __name__ == '__main__':
	print "Start MyCronJob ..."
	inspector = FBGraphInspector("100")
	inspector.inspect()

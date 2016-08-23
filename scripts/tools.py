import requests
import os
from requests.auth import HTTPBasicAuth

class FBGraphInspector:
	def __init__(self, helmet_id):
		self.helmet_id = helmet_id

	def inspect(self):
		print "==> Inspecting item with ID = {}".format(self.helmet_id)
		# get app access token
		access_token = self.__get_app_access_token()
		# get object id and number of shares 
		self.__get_object_id(self.__build_url(self.helmet_id))
		# get number of likes
		self.__get_likes()
		# update zodinet api
		self.__update_zodinet_api()

	def __build_url(self, id):
		return self.__get_env("SPECIFIC_HELMET_URL_FORMAT").format(id)

	def __get_app_access_token(self):
		# call api to get access_token
		# set self.access_token = token
		res = requests.get('https://graph.facebook.com/v2.7/oauth/access_token?client_id={}&client_secret={}&grant_type=client_credentials'
			.format(self.__get_env("CLIENT_ID"), self.__get_env("CLIENT_SECRET")))
		self.access_token = res.json().get('access_token')
		return self.access_token

	def __get_object_id(self, url):
		res = requests.get('https://graph.facebook.com/?id={}'.format(url))
		self.og_id = res.json().get('og_object').get('id')
		self.share_count = res.json().get('share').get('share_count')
		return self.og_id, self.share_count

	# Get number of LIKES of an object_id
	def __get_likes(self):
		res = requests.get('https://graph.facebook.com/v2.7/{}/likes?access_token={}&summary=true'
			.format(self.og_id, self.access_token))
		self.likes = res.json().get('summary').get('total_count')
		return self.likes

	def __update_zodinet_api(self):
		print 'likes = {} || shares = {}'.format(self.likes, self.share_count)
		# {helmet: "id"}

	def __get_env(self, key):
		return os.environ[key]

class MyCronJob:
	def __init_(self):
		pass

	def start_job(self):
		# Get list of helmet ids from zodinet API
		self.ids = self.__get_all_helmets()
		# Inspect likes/shares on each ID then update Zodinet API
		for helmet_id in self.ids:
			FBGraphInspector(helmet_id).inspect()
		# Aggregate report to Rollbar

	# Read all ids of helmet from Zodinet Database
	def __get_all_helmets(self):
		print "Retrieving list of helmet ids from Zodinet ..."
		res = requests.get(self.__get_env('ZODINET_ALL_HELMET_URL'),
		 auth=HTTPBasicAuth(self.__get_env('USER'), self.__get_env('PASSWORD')))
		return res.json().get("ids")

	def __get_env(self, key):
		return os.environ[key]

if __name__ == '__main__':
	print "Start MyCronJob ..."
	job = MyCronJob()
	job.start_job()

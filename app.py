import web
urls = (
'/', 'index'
)

app = web.application(urls, globals())
class index:
	def GET(self):
		greeting = "Hello test 1"
		return greeting
if __name__ == "__main__":
	app.run()

import datetime
import json

import psycopg2
import falcon

class Handler(object):
	# def on_options(self, req, resp):
	# 	resp.append_header('Access-Control-Allow-Origin','*')
	def on_post(self, req, resp):
		self.do(req, resp)
	def on_get(self, req, resp):
		self.do(req. resp)
	def do(self, req, resp):
		resp.append_header('Access-Control-Allow-Origin','*')
		urlparams = falcon.util.uri.parse_query_string(req.query_string)
		source = urlparams['source']
		target = urlparams['target']
		rawpostdata = str(req.stream.read(),'UTF-8')
		js = json.loads(rawpostdata)

		conn = psycopg2.connect("dbname='sampleapp' user='sampleapp' host='db' password='sampleapp'")
		cur = conn.cursor()
		sql = """
SELECT st_asgeojson(
	st_transform(
		st_setsrid(
			ST_GeomFromGeoJSON(%s)
			, %s
		)
		, %s
	)
)"""
		print(sql)

		cur.execute(sql,
		(
			rawpostdata,
			int(source),
			int(target)
		))

		res = cur.fetchone()
		resp.body= res[0]



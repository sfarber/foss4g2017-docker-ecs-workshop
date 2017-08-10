import falcon
import service

falconApi = falcon.API()
falconApi.add_route("/sampleapp",  service.Handler())

# Import Python Package
import http.client

conn = http.client.HTTPSConnection("classdemo.us.auth0.com")

payload = "{\"client_id\":\"FrOGKqI4wfsyQA50cZ2M3IJFDx9u9X4r\",\"client_secret\":\"G5f8ESNYnWtIve2cGQX4wyLCu95-HdEnNWx8znUhuHYCkkG-ZTqNluFwJEUmVR6J\",\"audience\":\"image\",\"grant_type\":\"client_credentials\"}"

headers = { 'content-type': "application/json" }

conn.request("POST", "/oauth/token", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
from email import message
from endpoints import Endpoint

endpoint = Endpoint(prefix='')

@endpoint.router.get("/")
async def home():
    return {"yo momma":"fat"}

import requests 
import urllib.parse
import aiohttp
import asyncio
import json 

def get_request(link='', params=None,header=None):   
    """
        Asynchronous and parallel request to api link
    Parameters: 
         link : api link
         params : additional parameters to url
         header : header to api 
    Returns: 
        res : response data and status code """

    if params:
        url=link + urllib.parse.urlencode(params)
    else:
        url=link

    asyncio.set_event_loop(asyncio.new_event_loop())
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(get(url))]
    loop.run_until_complete(asyncio.wait(tasks))
  
    for task in tasks : 
        res= task.result()
        print("Request for {} is {}".format(url, res[1]))
        print(res[0])
        return res[0],res[1]
  
async def get(url=''):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json(), response.status



  
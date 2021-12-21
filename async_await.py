import asyncio
import requests

url = 'https://jsonplaceholder.typicode.com/posts'

async def num():
    for i in [1,2,3,4,5,6]:
        print(i)
        await asyncio.sleep(5)
    
    

asyncio.run(num())
# print(asyncio.sleep(5))
# print('welcome after 5 seconds')  
import asyncio
import aiohttp
import json
import time


async def get_post(post_id):
    url = f'https://jsonplaceholder.typicode.com/posts/{post_id}'
    async with aiohttp.ClientSession() as session:
        async with session.get(url, ssl=False) as response:
            return await response.json()


async def main():
    file = 'data.json'
    post_ids = range(1, 78)

    tasks = [asyncio.create_task(get_post(post_id)) for post_id in post_ids]
    results = await asyncio.gather(*tasks)

    with open(file, 'w') as f:
        json.dump(results, f, indent=4)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main())
    end = time.time()
    print(end - start)


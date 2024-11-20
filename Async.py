import time
import asyncio
import requests


async def function1():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url)
    open('google1.ico', 'wb').write(r.content)
    print("Func 1")

async def function2():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url)
    open('google2.ico', 'wb').write(r.content)
    print("Func 2")

async def function3():
    url = 'http://google.com/favicon.ico'
    r = requests.get(url)
    open('google3.ico', 'wb').write(r.content)
    print("Func 3")

async def main():
    l = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    # print(l)
    # task = asyncio.create_task(function1())
    # await function1()
    # await function2()
    # await function3()

asyncio.run(main())
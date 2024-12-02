import asyncio
import fastapi
from fastapi import FastAPI

import asyncio


runers = [{"ім'я": "Андрій", "швидкість": 10}, {"ім'я": "Марк", "швидкість": 11}, {"ім'я": "Ілля", "швидкість": 52}]
async def run(runer):
    time = 100/runer['швидкість']
    await asyncio.sleep(time)
    print(f'учасник {runer["ім\'я"]} прийшов до фінішу')
    return runer["ім'я"], time


async def main():
    tasks = [asyncio.create_task(run(runer)) for runer in runers]
    a = await asyncio.gather(*tasks)
    winer  = min(a,key=lambda x: x[1])
    print(winer)


asyncio.run
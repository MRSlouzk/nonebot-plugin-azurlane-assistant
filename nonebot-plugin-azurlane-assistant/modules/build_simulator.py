# Python Script Created by MRS
import json, random
from typing import List

async def build_simulate(
        pool_type: str,
        *args,
        times: int = 1
    )-> List[dict]:
    with open("./data/azurlane/data/pool.json", "r", encoding="utf-8") as f:
        cot = json.load(f)
    che_lst: dict = cot["data"][pool_type]
    quality_lst = []
    for _ in range(0, times):
        rnd = random.random()
        for k in che_lst.keys():
            rnd = rnd - che_lst.get(k)
            if(rnd <= 0):
                quality_lst.append(k)
                break

    res_lst: List[dict] = []
    for quality in quality_lst:
        pool: list = cot[pool_type][quality]
        res = random.choice(pool)
        res_lst.append({
            "name": res,
            "quality": quality
        })
    return res_lst

if __name__ == '__main__':
    import asyncio
    lst = asyncio.run(build_simulate("qx", times=10))
    print(lst)
    # for i in range(0, 2):
    #     print("a")
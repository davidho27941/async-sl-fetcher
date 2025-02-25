import random
import asyncio

from fastapi import FastAPI

app = FastAPI(debug=True)

async def page_processor(idx):
    print(f"Going to process page {idx}")
    interval = random.randint(1,5)
    await asyncio.sleep(interval)
    print(f"Page {idx} processed. Tooks {interval} sec.")

    # data model validation
    
    # upload to some where
    

@app.get("/v1/test/", status_code=200)
async def fetch_data():
    tasks = [asyncio.create_task(page_processor(idx)) for idx in range(3)]
    
    await asyncio.gather(*tasks)
    
    return {"result": "success"}
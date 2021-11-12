from fastapi import FastAPI
from enum import Enum

app = FastAPI()

class AvailableCuisines(str, Enum):
    bangali = "bangali"
    american = "american"
    italian = "italian"

food_items = {
    'bangali' : ["biryani", "Bharta"],
    'american' : ["burger", "sandwich"],
    'italian' : ["pizza", "pasta"]
}

coupon_code = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/get_items/{cuisine}")
async def get_item(cuisine: AvailableCuisines):
    return food_items.get(cuisine)

@app.get("/get_coupon/{code}")
async def get_item(code: int):
    return {'discount_amount': coupon_code.get(code)}
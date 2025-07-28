import asyncio
import httpx
import random

MINIKUBE_IP = "<IP_ADDRESS>"
PORT = "30007"

USER_URL = f"http://{MINIKUBE_IP}:{PORT}/api/v1/users"
PRODUCT_URL = f"http://{MINIKUBE_IP}:{PORT}/api/v1/products"
ORDER_URL = f"http://{MINIKUBE_IP}:{PORT}/api/v1/orders"

async def send_cycle(i, client):
    print(f"\n=== Cycle {i+1} ===")

    # Create user
    user_data = {
        "name": f"User_{i+1}",
        "email": f"user_{i+1}@example.com"
    }
    user_res = await client.post(USER_URL, json=user_data)
    print(f"[User] {user_res.status_code} | {user_res.text}")
    user_id = user_res.json().get("id") if user_res.status_code == 200 else None

    # Create product
    product_data = {
        "name": f"Product_{i+1}",
        "price": round(random.uniform(10.0, 100.0), 2)
    }
    product_res = await client.post(PRODUCT_URL, json=product_data)
    print(f"[Product] {product_res.status_code} | {product_res.text}")
    product_id = product_res.json().get("id") if product_res.status_code == 200 else None

    # Create order
    if user_id and product_id:
        order_data = {
            "user": {"id": user_id},
            "items": [
                {
                    "product": {"id": product_id},
                    "quantity": 1
                }
            ]
        }
        order_res = await client.post(ORDER_URL, json=order_data)
        print(f"[Order] {order_res.status_code} | {order_res.text}")
    else:
        print("[Order] Skipped: Missing user_id or product_id")

async def main():
    async with httpx.AsyncClient() as client:
        for i in range(12):  # 12 cycles, every 5 sec ~ 1 minute
            await send_cycle(i, client)
            await asyncio.sleep(5)

if __name__ == "__main__":
    asyncio.run(main())


# from fastapi import FastAPI

# app = FastAPI()


# @app.get("/")
# def get_root():
#     return {"message": "Hello, GET request!"}


# @app.post("/")
# def post_root(post_data: str):
#     return {"message": f"Hello, POST request! You sent: {post_data}"}


# @app.put("/")
# def put_root(put_data: str):
#     return {"message": f"Hello, PUT request! You sent: {put_data}"}


# @app.patch("/")
# def patch_root(patch_data: str):
#     return {"message": f"Hello, PATCH request! You sent: {patch_data}"}


# @app.delete("/")
# def delete_root():
#     return {"message": "Hello, DELETE request!"}


# if __name__ == "__main__":
#     import uvicorn

#     uvicorn.run(app, host="localhost", port=8000)
from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from customer import Customer, sessionmaker

# class PostData(BaseModel):
#     post_data: str

# class PutData(BaseModel):
#     put_data: str

# class PatchData(BaseModel):
#     patch_data: str



app = FastAPI()

class CustomerSchema(BaseModel):
    first_name: str
    last_name: str
    email: str
    gender: str

    class Config:
        orm_mode=True

@app.get("/")
def get_root():
    customer = session.query(Customer).all()
    return {"message": "Hello, GET request!"}

@app.get("/customer/{id}")
def get_one_customer(id:int)->CustomerSchema:
    single_customer = session.query(Customer).filter_by().first()
    return single_student

# @app.post("/students/")
# def post_root(post_data: PostData):
#     return {"message": f"Hello, POST request! You sent: {post_data.post_data}"}

@app.post("/customer/")
def add_data(customer: CustomerSchema)->CustomerSchema:
    customer = Customer (customer)
    session.add(customer)
    session.commit()

    return customer

@app.put("/customer/")
def put_root(put_data: PutData):
    return {"message": f"Hello, PUT request! You sent: {put_data.put_data}"}


@app.patch("/customer/")
def patch_root(patch_data: PatchData):
    return {"message": f"Hello, PATCH request! You sent: {patch_data.patch_data}"}


@app.delete("/customer/{id}")
def delete_root():
    return {"message": "Hello, DELETE request!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="localhost", port=8000)

import grpc
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

def place_order(stub, order_type, order_id, items):
    try:
        response = None
        if order_type == "FoodOrder":
            response = stub.FoodOrder(restaurant_pb2.RestaurantRequest(orderID=order_id, items=items))
        elif order_type == "DrinkOrder":
            response = stub.DrinkOrder(restaurant_pb2.RestaurantRequest(orderID=order_id, items=items))
        elif order_type == "DessertOrder":
            response = stub.DessertOrder(restaurant_pb2.RestaurantRequest(orderID=order_id, items=items))
        elif order_type == "MealOrder":
            response = stub.MealOrder(restaurant_pb2.RestaurantRequest(orderID=order_id, items=items))
        
        print(f"{order_type} response received: ")
        print(response)
        print(f"Status: {restaurant_pb2.RestaurantResponse.Status.Name(response.status)}")
    except grpc.RpcError as e:
        print(e.details())
        print(e.code())

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = restaurant_pb2_grpc.RestaurantStub(channel)
        print("-------------- FoodOrder --------------")
        place_order(stub, "FoodOrder", "12345abc", ["burger"])
        print("--------------")
        place_order(stub, "FoodOrder", "12345abc", ["beer"])
        print("-------------- DrinkOrder --------------")
        place_order(stub, "DrinkOrder", "12345abd", ["beer"])
        print("-------------- DessertOrder --------------")
        place_order(stub, "DessertOrder", "12345abe", ["brownie", "pancakes"])
        print("-------------- MealOrder --------------")
        place_order(stub, "MealOrder", "12345abf", ["burger", "beer", "brownie"])
        print("--------------")
        place_order(stub, "MealOrder", "12345abg", ["burger", "beer", "water"])
        print("--------------")
        place_order(stub, "MealOrder", "12345abh", ["burger", "brownie", "water"])
        print("--------------")
        place_order(stub, "MealOrder", "12345abh", ["burger", "brownie"])

if __name__ == '__main__':
    run()
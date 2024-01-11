from concurrent import futures
import grpc
import sys
from proto import restaurant_pb2
from proto import restaurant_pb2_grpc

RESTAURANT_ITEMS_FOOD = ["chips", "fish", "burger", "pizza", "pasta", "salad"]
RESTAURANT_ITEMS_DRINK = ["water", "fizzy drink",
                          "juice", "smoothie", "coffee", "beer"]
RESTAURANT_ITEMS_DESSERT = ["ice cream", "chocolate cake",
                            "cheese cake", "brownie", "pancakes", "waffles"]


class Restaurant(restaurant_pb2_grpc.RestaurantServicer):

    # Logic goes here
    def FoodOrder(self, request, context):
        item_messages = [restaurant_pb2.items(itemName=item) for item in request.items]
        if all(item in RESTAURANT_ITEMS_FOOD for item in request.items):
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID,
                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED,
                    itemMessage=item_messages,
                )
        else:
            return restaurant_pb2.RestaurantResponse(
                orderID=request.orderID,
                status=restaurant_pb2.RestaurantResponse.Status.REJECTED,
                itemMessage=item_messages,
            )
        
    def DrinkOrder(self, request, context):
        item_messages = [restaurant_pb2.items(itemName=item) for item in request.items]
        if all(item in RESTAURANT_ITEMS_DRINK for item in request.items):
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID,
                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED,
                    itemMessage=item_messages,
                )
        else:
            return restaurant_pb2.RestaurantResponse(
                orderID=request.orderID,
                status=restaurant_pb2.RestaurantResponse.Status.REJECTED,
                itemMessage=item_messages,
            )
        
    def DessertOrder(self, request, context):
        item_messages = [restaurant_pb2.items(itemName=item) for item in request.items]
        if all(item in RESTAURANT_ITEMS_DESSERT for item in request.items):
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID,
                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED,
                    itemMessage=item_messages,
                )
        else:
            return restaurant_pb2.RestaurantResponse(
                orderID=request.orderID,
                status=restaurant_pb2.RestaurantResponse.Status.REJECTED,
                itemMessage=item_messages,
            )
        
    def MealOrder(self, request, context):
        # only receive orders that contains only 3 items according to the following order: 
        # 1 food, then 1 drink, and finally 1 dessert
        item_messages = [restaurant_pb2.items(itemName=item) for item in request.items]

        if len(request.items) != 3:
            return restaurant_pb2.RestaurantResponse(
                orderID=request.orderID,
                status=restaurant_pb2.RestaurantResponse.Status.REJECTED,
                itemMessage=item_messages,
            )
        else:
            if (request.items[0] in RESTAURANT_ITEMS_FOOD and request.items[1] in RESTAURANT_ITEMS_DRINK and request.items[2] in RESTAURANT_ITEMS_DESSERT):
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID,
                    status=restaurant_pb2.RestaurantResponse.Status.ACCEPTED,
                    itemMessage=item_messages,
                )
            else:
                return restaurant_pb2.RestaurantResponse(
                    orderID=request.orderID,
                    status=restaurant_pb2.RestaurantResponse.Status.REJECTED,
                    itemMessage=item_messages,
                )


def serve():

    # Logic goes here
    # Remember to start the server on localhost and a port defined by the first command line argument
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    restaurant_pb2_grpc.add_RestaurantServicer_to_server(Restaurant(), server)
    server.add_insecure_port('[::]:' + sys.argv[1])
    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    serve()

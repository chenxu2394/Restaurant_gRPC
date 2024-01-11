# gRPC Restaurant Service

This repository hosts a gRPC-based restaurant service system, developed as part of an assignment I completed for the Cloud Software and Systems course offered by the Department of Computer Science at Aalto University. The project demonstrates the use of gRPC to build a restaurant ordering system, involving server-client communication to handle food orders.

## Background

gRPC (gRPC Remote Procedure Call) is an open-source framework by Google that facilitates efficient and robust communication between services in a distributed system. This project utilizes gRPC's key features, including efficient serialization and streamlined communication.

Through this restaurant service system, the project showcases how gRPC can enhance communication in distributed applications, leveraging its efficient serialization and streamlined approach in a Python-based environment.

## Project Overview

The Restaurant_gRPC is a simple, yet effective demonstration of remote procedure calls using gRPC. The application simulates a restaurant environment where clients can place orders for various items, and the server processes these orders. It includes the following components:

- **Restaurant Server**: The gRPC server that processes orders for food, drinks, and desserts.
- **Restaurant Client**: The gRPC client that sends order requests to the server.

The system handles different types of orders, including food, drinks, desserts, and full meals. It demonstrates the fundamentals of gRPC, including defining service methods, generating client and server stubs from the `.proto` file, and handling server-client communication.

## Testing

To test the gRPC Restaurant Service, follow these steps:

1. **Clone the Repository**

    Start by cloning this repository to a local machine:

    ```bash
    git clone git@github.com:chenxu2394/Restaurant_gRPC.git
    cd Restaurant_gRPC
    ```
    
2. **Install Requirements**

    Install the necessary Python packages using the provided `requirements.txt`:

    ```bash
    # Make sure you are in the project root directory
    pip install -r requirements.txt
    ```

3. **Generate gRPC Code**

    Generate the Python gRPC code from the `.proto` file:

    ```bash
    # Make sure you are in the project root directory
    python -m grpc_tools.protoc -I . --python_out=. --pyi_out=. --grpc_python_out=. ./proto/restaurant.proto
    ```

    This step creates the necessary gRPC files from the Protocol Buffers definition.

4. **Start the Server**

    Run the server on the local machine, specifying the port number 50051:

    ```bash
    python restaurant_server.py 50051
    ```

    Ensure that the server starts without errors and is listening on the specified port.

5. **Run the Client**

    In a separate terminal window, execute the client script to send requests to the server:

    ```bash
    python restaurant_client.py
    ```

    Observe the client's output, which should reflect the responses received from the server.

By following these steps, one can test the functionality of the gRPC Restaurant Service in a local environment.

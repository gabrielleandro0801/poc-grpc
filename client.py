import grpc

from config import crypto_service_pb2_grpc as pb2_grpc, crypto_service_pb2 as pb2


class FetchPrices:
    def __init__(self):
        print("Creating channel to connect to server\n")
        self.channel = grpc.insecure_channel("localhost:50061")
        self.stub = pb2_grpc.GExchangeStub(self.channel)

    def get_price(self, name):
        print(f"Requesting to server to get_price of [{name}]")
        request = pb2.cryptocurrency(name=name)
        response = self.stub.get_price(request)
        return response


if __name__ == "__main__":
    client = FetchPrices()
    print(client.get_price("Bitcoin"))
    print(client.get_price("Ethereum"))
    print(client.get_price("Cardano"))

import flwr as fl

# Example of a possible strategy 
# strategy = fl.server.strategy.FedAvg(
#     fraction_fit=0.1,  # Sample 10% of available clients for the next round
#     min_fit_clients=10,  # Minimum number of clients to be sampled for the next round
#     min_available_clients=80,  # Minimum number of clients that need to be connected to the server before a training round can start
# )
strategy = fl.server.strategy.FedAvg()
fl.server.start_server(config=fl.server.ServerConfig(num_rounds=3))
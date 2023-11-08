#!/usr/bin/env python3
# Sample python file with an executable main function which prints hello world

# import tensorflow as tf
import tensorflow_federated as tff

def setup_test():
    # this will test if the tff package is installed properly
    print(tff.federated_computation(lambda: 'Hello World')())

if __name__ == "__main__":
    setup_test()
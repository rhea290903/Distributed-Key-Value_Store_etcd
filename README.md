# Etcd3 Operations in Python

This project provides Python code for interacting with an etcd3 cluster, including basic operations such as putting, getting, deleting keys, and listing keys.
It also includes unit tests using unittest and mocking techniques to ensure the functionality of these operations.

Install the required packages:

pip install etcd3

Usage

Basic Operations
1.Import the etcd3 library:
import etcd3

2.Connect to the etcd cluster:
client = etcd3.client()

3.Use the following functions for basic operations:
put_key_value(key, value): Put a key-value pair into etcd.
get_value(key): Get the value for a specific key.
delete_key(key): Delete a key-value pair from etcd.
list_keys(): List all keys in etcd.

Running Tests

The project includes unit tests to validate the functionality of etcd3 operations. To run the tests, execute the following command:

python -m unittest unittest.py





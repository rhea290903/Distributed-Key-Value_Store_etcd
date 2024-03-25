import etcd3

# Connect to the etcd cluster
client = etcd3.client()



def list_keys():
    # List all keys in etcd
    #keys = client.get_all()
    return [(m.key).decode('utf-8') for (_, m) in client.get_all()]
    #return [key.decode('utf-8').split(':', 1)[0] for key, _ in keys]

def get_value(key):
    # Get the value for a specific key
    value, _ = client.get(key)
    return value.decode('utf-8') if value else None

def put_key_value(key, value):
    # Put a key-value pair into etcd
    client.put(key, value)

# Example usage
print("List of keys:", list_keys())
key_to_get = input("Enter the key to get its value: ")
print("Value for key", key_to_get, ":", get_value(key_to_get))
key_to_put = input("Enter the key to put: ")
value_to_put = input("Enter the value to put: ")

put_key_value(key_to_put, value_to_put)
print("Key-value pair put into etcd.")


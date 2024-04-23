import etcd3

# Connect to the etcd cluster
def create_etcd_client():
    try:
        client = etcd3.client()
        return client
    except grpc.RpcError as e:
        print("Connection error:", e.details())
        return None

# Connect to the etcd cluster
client = create_etcd_client()
#client = etcd3.client()



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
def delete_key(key):
    # Delete a key-value pair from etcd
    client.delete(key)
print("Available options: put, get, delete, list")
print("List of keys:", list_keys())
while True:
        option = input("Enter an option: ")

        if option == "put":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            put_key_value(key, value)
            print("Key-value pair put into etcd.")
        elif option == "get":
            key = input("Enter the key to get its value: ")
            value = get_value(key)
            if value is not None:
                print("Value for key", key, ":", value)
            else:
                print("Key not found:", key)
        elif option == "delete":
            key = input("Enter the key to delete: ")
            delete_key(key)
            print("Key-value pair deleted from etcd.")
        elif option == "list":
            keys = list_keys()
            print("Keys:", keys)
        else:
            print("Invalid option. Please try again.")

    
'''print("List of keys:", list_keys())
key_to_get = input("Enter the key to get its value: ")
print("Value for key", key_to_get, ":", get_value(key_to_get))
key_to_put = input("Enter the key to put: ")
value_to_put = input("Enter the value to put: ")

put_key_value(key_to_put, value_to_put)
print("Key-value pair put into etcd.")'''


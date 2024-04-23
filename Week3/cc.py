import etcd3
import grpc

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
    if client is None:
        return []  # Return an empty list if client is None
    return [(m.key).decode('utf-8') for (_, m) in client.get_all()]


def get_value(key):
    # Get the value for a specific key
    value, _ = client.get(key)
    return value.decode('utf-8') if value else None

def put_key_value(key, value):
    # Put a key-value pair into etcd
    client.put(key, value)

def ListKeyValue():
    try:
        keys = client.get_all()
        print("All keys:")
        for v1,value in keys:
            print((value.key).decode('utf-8'),":",v1.decode('utf-8'))
    except Exception as e:
        print(f"Error listing keys: {e}")

# Example usage
def delete_key(key):
    # Delete a key-value pair from etcd
    client.delete(key)
if __name__ == "__main__":
    print("Available options: put, get, delete, list, exit ")
    
    ListKeyValue()
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
           
            elif option=="exit":
                exit()
            else:
                print("Invalid option. Please try again.")

        
    '''print("List of keys:", list_keys())
    key_to_get = input("Enter the key to get its value: ")
    print("Value for key", key_to_get, ":", get_value(key_to_get))
    key_to_put = input("Enter the key to put: ")
    value_to_put = input("Enter the value to put: ")

    put_key_value(key_to_put, value_to_put)
    print("Key-value pair put into etcd.")'''
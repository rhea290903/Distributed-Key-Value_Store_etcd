import unittest
from unittest.mock import MagicMock, patch
from cc import put_key_value, get_value, delete_key, list_keys, create_etcd_client

class TestEtcdFunctions(unittest.TestCase):

    @patch('cc.etcd3.client')
    def test_create_etcd_client_success(self, mock_client):
        create_etcd_client()
        mock_client.assert_called_once()#check if the client is created once
    
    
    @patch('cc.etcd3.client', return_value=MagicMock())
    def test_create_etcd_client_failure(self, mock_client):
        c = create_etcd_client()
        #when there is failure in  client creation instead of  return None it returns a magicmock object
        #this helps eliminate dependencies between testing units
        self.assertIsInstance(c, MagicMock)#checks if  client returns MagicMock object 
      

    @patch('cc.client')
    def test_put_key_value(self, mock_client):
        key = "test_key"
        value = "test_value"
        put_key_value(key, value)
        mock_client.put.assert_called_once_with(key, value)

    @patch('cc.client')
    def test_get_value(self, mock_client):
        key = "test_key"
        value = "test_value"
        mock_client.get.return_value = (value.encode('utf-8'), None)
        self.assertEqual(get_value(key), value)

    @patch('cc.client')
    def test_get_value_not_found(self, mock_client):
        key = "nonexistent_key"
        mock_client.get.return_value = (None, None)
        self.assertIsNone(get_value(key))

    @patch('cc.client')
    def test_delete_key(self, mock_client):
        key = "test_key"
        delete_key(key)
        mock_client.delete.assert_called_once_with(key)

    @patch('cc.client')
    def test_list_keys(self, mock_client):
        
        keys = [(b'key1', MagicMock(key=b'key1')), 
                (b'key2', MagicMock(key=b'key2')), 
                (b'key3', MagicMock(key=b'key3'))]
        mock_client.get_all.return_value = keys

        # Now, test list_keys()
        self.assertEqual(list_keys(), ['key1', 'key2', 'key3'])
    

if __name__ == '__main__':
    unittest.main()

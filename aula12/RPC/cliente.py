# Cliente XML-RPC
import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/")
print(proxy.soma(2, 3))  # 5

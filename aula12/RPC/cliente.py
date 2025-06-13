# Cliente XML-RPC
import xmlrpc.client
try:
    proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8000/")
    print(proxy.soma(2, 3))  # 5
    print(proxy.soma(6, 4))  # 10
except ConnectionRefusedError:
    print('Servidor Não encontrado ')
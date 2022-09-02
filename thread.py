import threading

token_received = threading.Event()

def get():
    print('retrieving token')
    token_received.wait()

thread_1 = threading.Thread(target=get)
thread_1.start()

token = input("Input the auth code: ")
print('Token is received')
token_received.set()
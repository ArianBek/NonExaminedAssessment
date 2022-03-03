#Import from the libraries needed for the code to Function
import socket
import pickle


class Network: #Network Function
    def __init__(self):
        #Setting all the Variables from the Self Initialisation Function
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.hostname = socket.gethostname()  #This gets the hostname 
        self.ip_address = socket.gethostbyname(self.hostname) #This gets the IPv4 address using socket.gethostbyname() method

        self.server = str(self.ip_address) #Turning IP Address into String
        
        self.port = 5555 #Port to Conenct to
        self.addr = (self.server, self.port)
        self.p = self.connect()

    def getQuestions(self): #Getting the Questions Function
        return self.p

    def connect(self): #Connecting Function
        try:
            self.client.connect(self.addr) #Address of the Client
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data): #Sending Data Function
        try:
            self.client.send(pickle.dumps(data)) #Sends the Data from server to client
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)
import SOAPpy

server = SOAPpy.SOAPProxy("http://localhost:5001/")
print (server.mytxt())

##TODO LOGIC
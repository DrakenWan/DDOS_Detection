import numpy as np
import sys
import pickle
    
def icmp_test(attributes):
    model = pickle.load(open("./saved_model/icmp_data.sav", 'rb'))
    result = model.predict([attributes])
    print(result)

def udp_test(attributes):
    model = pickle.load(open("./saved_model/udp_data.sav", 'rb'))
    result = model.predict([attributes])
    print(result)

def tcp_syn_test(attributes):
    model = pickle.load(open("./saved_model/tcp_syn_data.sav", 'rb'))
    result = model.predict([attributes])
    print(result)

if __name__ == "__main__":
    if sys.argv[1] == "icmp": 
        icmp_test(sys.argv[2:])
    elif sys.argv[1] == "tcp_syn":
        tcp_syn_test(sys.argv[2:])
    elif sys.argv[1] == "udp":
        udp_test(sys.argv[2:])
    else:
        sys.exit("Incorrect protocol has been chosen for testing. Try again.")
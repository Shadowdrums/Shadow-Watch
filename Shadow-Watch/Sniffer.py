from scapy.all import *
import time

target_ip = get_if_addr(conf.iface) # Use host IP as target
print("Monitoring network for suspicious traffic...")

dir_path = os.path.dirname(os.path.realpath(__file__))

filename = "suspicious_traffic.txt"

file_path = os.path.join(dir_path, filename)
if not os.path.exists(file_path):
    open(file_path, "a").close()

# Open output file
with open("suspicious_traffic.txt", "a") as f:
    # Start an infinite loop
    while True:
        # Define packet handler function
        def detect_packet(pkt):
            if pkt.haslayer(TCP) and pkt.haslayer(Raw) and b"MS_T120" in pkt[Raw].load:
                message = f"[+] Remote Desktop connection detected from {pkt[IP].src}:{pkt[TCP].sport}"
                print(message)
                f.write(message + "\n")
            
            if pkt.haslayer(ICMP) and pkt.getlayer(ICMP).type == 8:
                message = f"[+] Ping detected from {pkt[IP].src}"
                print(message)
                f.write(message + "\n")
            
            if pkt.haslayer(TCP) and pkt.getlayer(TCP).flags == "S":
                message = f"[+] SYN packet detected from {pkt[IP].src}:{pkt[TCP].sport}"
                print(message)
                f.write(message + "\n")
            
            if pkt.haslayer(IP) and pkt.haslayer(TCP) and pkt[IP].dst == target_ip:
                message = f"[+] Outbound connection detected to {target_ip} from {pkt[IP].src}:{pkt[TCP].sport}"
                print(message)
                f.write(message + "\n")
        
        # Use sniff() function to capture and handle packets
        sniff(filter="tcp or icmp", prn=detect_packet, store=0, timeout=10, iface=conf.iface)

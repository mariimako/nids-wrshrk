import subprocess
import smtplib
from email.mime.text import MIMEText


# usually en0 anyway, but analyze using ifconfig the using netwrok interfaces
# potentially, use this applcation
#  to analyze not only wifi but other things
def find_network_interface():
    network_interfaces = subprocess.Popen(
        ['ifconfig'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return

def start_process():
    # Start Tshark process
    tshark = subprocess.Popen(
        ['sudo', 'tshark', '-i', 'en0', '-T', 'fields', '-e', 'frame.time', '-e', 'ip.src', '-e', 'ip.dst', '-e', 'tcp.port', '-e', 'udp.port'],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )

    for packet in tshark.stdout:
        packet_data = packet.decode('utf-8').strip().split('\t')
        print("Packet Detail: ", packet_data)
        packet_analysis(packet_data)

def packet_analysis(packet_data):
    # blaclisted IPs
    # other other other
    malicious_ips = ['192.168.1.100']  

    if packet_data[1] in malicious_ips or packet_data[2] in malicious_ips:
        send_alert(packet_data)
        print("Malicious packet detected")


def send_alert(packet_data):
    msg = MIMEText(f"Malicious packet detected:\n{packet_data}")
    msg['Subject'] = 'NIDS Alert'
    msg['From'] = 'example@gmail.com'
    msg['To'] = 'example@gmail.com'

    with smtplib.SMTP('smtp.example.com') as server:
        server.login('example@gmail.com', 'password')
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
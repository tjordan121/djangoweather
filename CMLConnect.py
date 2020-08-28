from netmiko import ConnectHandler

breakout_host_ip = "172.16.40.128"
cmd = "show ip int brief"

iosv_1 = {
    "device_type": "cisco_ios_telnet",
    "host": breakout_host_ip,
    "port": 9000,
    "global_delay_factor": 2,
}

print(f"Connecting to: {breakout_host_ip}...")
net_connect = ConnectHandler(**iosv_1)
print("Connected!")
print(f"Executing command:\n{cmd}")
sh = net_connect.send_command(cmd)
print(sh)
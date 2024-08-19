
>> Analyze the output and determine WiFi (Ususally en0)

	1.	Interface Name:
	•	Appears at the start of each section (e.g., en0, lo0).
	•	Indicates the name of the network interface.
	2.	Flags:
	•	These describe the status and configuration of the interface.
	•	Common flags include:
	•	UP: The interface is up and running.
	•	BROADCAST: Supports broadcasting (used for sending data to all devices in a network).
	•	RUNNING: The interface is operational.
	•	MULTICAST: Supports multicast (used for sending data to multiple devices at once).
	•	LOOPBACK: Indicates a loopback interface (used for internal communication within the machine).
	3.	Ether:
	•	Shows the MAC (Media Access Control) address of the interface.
	•	Example: ether 01:23:45:67:89:ab.
	4.	inet / inet6:
	•	inet: Displays the IPv4 address assigned to the interface.
	•	inet6: Displays the IPv6 address assigned to the interface.
	•	Example: inet 192.168.1.2 netmask 0xffffff00 broadcast 192.168.1.255.
	5.	Netmask:
	•	Shows the subnet mask for the interface, which defines the network’s size.
	•	Example: netmask 0xffffff00 corresponds to a subnet mask of 255.255.255.0.
	6.	Broadcast:
	•	The broadcast address, used to send data to all devices in the network.
	•	Example: broadcast 192.168.1.255.
	7.	Status:
	•	Indicates the operational status of the interface.
	•	Common values:
	•	active: The interface is connected and operational.
	•	inactive: The interface is not connected.
	8.	Media:
	•	Displays the type and speed of the network connection.
	•	Example: media: autoselect (1000baseT <full-duplex>) indicates a gigabit Ethernet connection.
	9.	MTU (Maximum Transmission Unit):
	•	The largest packet size that can be transmitted over the network interface without fragmentation.
	•	Example: mtu 1500.
	10.	RX and TX:
	•	RX (Receive): Information about packets received.
	•	TX (Transmit): Information about packets transmitted.
	•	Includes counts of packets, errors, and dropped packets.


en0: flags=8863<UP,BROADCAST,SMART,RUNNING,SIMPLEX,MULTICAST> mtu 1500
    ether 01:23:45:67:89:ab
    inet 192.168.1.2 netmask 0xffffff00 broadcast 192.168.1.255
    inet6 fe80::1234:5678:9abc:def0%en0 prefixlen 64 secured scopeid 0x4
    inet6 2001:0db8:85a3:0000:0000:8a2e:0370:7334 prefixlen 64 autoconf secured
    nd6 options=201<PERFORMNUD,DAD>
    media: autoselect (1000baseT <full-duplex>)
    status: active

	•	en0: Interface name, typically Wi-Fi.
	•	flags=8863: Indicates the interface is UP, supports broadcasting, is running, and supports multicast.
	•	ether 01:23:45:67:89:ab: MAC address of the interface.
	•	inet 192.168.1.2: IPv4 address assigned to the interface.
	•	netmask 0xffffff00: Subnet mask (255.255.255.0).
	•	broadcast 192.168.1.255: Broadcast address.
	•	inet6: Two IPv6 addresses assigned to the interface.
	•	media: autoselect (1000baseT ): Indicates a gigabit Ethernet connection.
	•	status: active: The interface is active and operational.
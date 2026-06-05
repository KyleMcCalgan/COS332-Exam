# COS332 Semester Test — 16 May 2026

**Course:** Computer Science  
**Paper:** COS332  
**Time:** 90 minutes  
**Marks:** 50

## Question 1

In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### 1.1

A BER value in ASN.1 is, in principle, encoded as a triple consisting of:

A. A type, a subtype and a value.  
B. A type, a length and a value.  
C. A type, a value and two sentinels.  
D. A variable name, as well as its minimum and maximum values.  
E. The same value encoded in binary, text and hexadecimal.

### 1.2

Which of the following is not a valid data type in ASN.1?

A. SET  
B. CHOICE  
C. SEQUENCE  
D. ARRAY  
E. INTEGER

### 1.3

According to RFC4511 all LDAP messages use a shared envelope that is defined using the universal SEQUENCE:

```asn1
LDAPMessage ::= SEQUENCE { ... }
```

This means that all LDAP messages:

A. Start with the word SEQUENCE.  
B. Conform to the definition of SEQUENCE, which is a non-terminal defined elsewhere in the RFC.  
C. Consist of a sequence as specified in the braces that follow the constructor SEQUENCE.  
D. Start with a sequence number.  
E. More than one of the above.

### 1.4

Which ISO OSI layer provides checkpoints, such that only messages sent since the last checkpoint have to be retransmitted after a connection has been lost?

A. 2  
B. 3  
C. 4  
D. 5  
E. 6

### 1.5

Suppose A and B are communicating via TCP. A has `n` bytes to transmit. As far as A is aware, the window size at B is `m < n`. This means that:

A. A cannot transmit.  
B. A can transmit `m` bytes.  
C. A can transmit `n` bytes.  
D. More than one of the above.  
E. All of the above.

### 1.6

Say a damaged packet arrives at its destination. The recipient may, for example, determine that the checksum does not match. Which protocol may be used to NAK — negative acknowledgement — to the original sender to request retransmission? Suppose A sends a TCP segment to B, but it arrives damaged at B. How is this resolved?

A. B sets the NAK TCP flag and sends it as a response to A.  
B. B discards the segment; B does not acknowledge it; the retransmission timer at A expires and the packet is sent again.  
C. B requests the network layer at B to deal with the error and this triggers a retransmission of the segment.  
D. B corrects the damaged segment and eventually acknowledges receipt.  
E. The lower layer protocols perform error checking, so a damaged segment will never arrive; errors will always be corrected.

### 1.7

Suppose A is connected to node B via TCP. When the persistent timer at A expires it implies that:

A. B has not yet acknowledged the last segment A sent to B.  
B. A is waiting for space to free up in B's window before further data can be sent.  
C. Since the connection is idle, A will send a probe to ensure that it is still present.  
D. More than one of the above.  
E. All of the above.

### 1.8

A TCP connection in the TIME-WAIT state means that:

A. The node is waiting for data from the node that it is connected to.  
B. The connection is about to time-out if no further data is transmitted soon.  
C. The connection will soon be established, as soon as the handshake is completed.  
D. The node is waiting for lost traffic to arrive at the port that is no longer in use, before it will be available for reuse.  
E. The network is congested.

### 1.9

A TCP node that is in the LISTEN state:

A. Is starting as a client and has sent a SYN message.  
B. Is acting as a client and has sent a SYN message.  
C. May act as a client after sending a SYN message.  
D. More than one of the above.  
E. None of the above.

### 1.10

TCP typically transports:

A. Fixed size packets.  
B. Structured data.  
C. Single characters.  
D. Byte streams.  
E. A stream of bits.

### 1.11

UDP headers do not contain sequence numbers. How does the node that transmits UDP data ensure that packets arrive in the correct sequence?

A. The sending node only sends the next packet after reception of the previous packet has been acknowledged.  
B. There is no way in which one packet can pass another packet on the wire — hence packets arrive in the same sequence that they were sent.  
C. UDP is never used to send any data in an IP system — hence the fact that packets may arrive in a different sequence than the sequence in which they were sent is irrelevant.  
D. When the arrival sequence of UDP packets matter, they are encapsulated in a TCP packet.  
E. UDP is only used to carry streams of data where the application still functions sufficiently well even if some UDP datagrams are received in the incorrect order.

### 1.12

What does the claim that QUIC is a quick protocol mean?

A. It manages the lower layer to transmit raw data at higher bit rates.  
B. It manages connection establishment in a single connection.  
C. Where multiple parts of a message has to be transported it ensures that parts of the message are delivered quickly even if some parts are delayed.  
D. More than one of the above.  
E. All of the above.

### 1.13

Which of the following headers are always present in a long QUIC header? Include cases where the length of the field will be present and may be 0, meaning that the field itself may be omitted.

A. Version.  
B. Source connection ID.  
C. Destination connection ID.  
D. More than one of the above.  
E. All of the above.

### 1.14

Assume a client establishes a new QUIC connection at time `t0` with a server. The server acknowledges the connection at time `t1` and immediately sends its response, with frames, at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which application data may originate be sent?

A. `t0`  
B. `t3`  
C. `t4`  
D. It is impossible to say.  
E. `t5`

### 1.15

The private class B IPv4 addresses are:

A. `172.10.0.0–172.15.255.255`  
B. `172.20.0.0–172.35.255.255`  
C. `172.16.0.0–172.31.255.255`  
D. `172.8.0.0–172.15.255.255`  
E. `172.16.0.0–172.31.255.255`

### 1.16

An IP datagram addressed to `10.10.1.2` arrives at node R. R is not directly connected to the destination network. The routing table at R includes the entries below. To which next hop does R forward the datagram?

| Destination | Next hop | Interface |
|---|---|---|
| `10.10.1.0/24` | `192.168.1.1` | `eth1` |
| `10.10.0.0/16` | `192.168.2.2` | `eth2` |
| `10.0.0.0/8` | `192.168.3.3` | `eth3` |
| `0.0.0.0/0` | `192.168.4.4` | `eth4` |

A. `192.168.1.1`  
B. `192.168.2.2`  
C. `192.168.3.3`  
D. `192.168.4.4`  
E. More than one of the above.

### 1.17

If one sends a message to an IP multicast address, the message will be delivered to:

A. The node to which that IP address has been assigned.  
B. All nodes on the local network.  
C. All nodes that are members of some group.  
D. The nearest node that is also on the network.  
E. To the network gateway that connects the network to other networks.

### 1.18

Suppose a router receives an IP datagram `d` and `d`'s TTL becomes 0. What may the router do?

A. Discard `d`.  
B. Forward `d` to the next hop.  
C. Send a time exceeded ICMP message to the source.  
D. More than one of the above.  
E. All of the above.

### 1.19

Suppose an entry in node A's routing table indicates that node B is the next node on the path from A to Z. Suppose node B's routing table indicates that the next hop on the path to Z is A. The resulting problem is addressed by using the following IP header field.

A. TTL  
B. Source address  
C. Destination address  
D. Network unreachable  
E. Bear-there flag

### 1.20

A typical ARP message looks as follows:

A. Who has `01-10-12-cf`?  
B. Who has `00-04-38-76-da-00`? Tell `00-11-43-ef-ba-4d`.  
C. `GET / HTTP/1.1`  
D. What is the IP of `x.co.za`?  
E. What is the name of `196.4.79`?

### 1.21

ICMP is used to:

A. Report errors that occur on the IP layer.  
B. Test network functions.  
C. Monitor routes.  
D. More than one of the above.  
E. All of the above.

### 1.22

On which layer of ISO OSI does ICMP fit?

A. 3  
B. 4  
C. 5  
D. 6  
E. 7

### 1.23

Consider the IPv6 address:

```text
fda2:3456:789a:bcde:f0fe:dcba:9876:5432
```

Which of the following is true about the part `fda2:3456:789a`?

A. It was supplied by an IISP/RIR.  
B. It locates a subnet.  
C. It is a random number.  
D. It was calculated from the MAC address of the interface.  
E. None of the above.

### 1.24

Consider the IPv6 address:

```text
fe80::1234:5678:9abc:def0:fedb:a987:6543/128
```

This address:

A. Is an SLA address.  
B. Is a link-local address.  
C. Is a site-local address.  
D. Is a global address.  
E. Would currently not be a legal address.

### 1.25

The routing prefix in an IPv6 address typically consists of the ___ of the address.

A. first 32 bits  
B. final 32 bits  
C. first 64 bits  
D. final 64 bits  
E. first 128 bits

---

## Question 2

Two nodes, A and B, are communicating using TCP. At time `t0` node A is ready to send byte 100, expects byte 300, has a window size of 500 and thinks that B has a window size of 300. These values perfectly match what node B knows about the connection. Nodes A and B subsequently exchange a couple of messages, `m1` to `m5`. The following table provides the length, direction, transmission and arrival time of each message. Some messages are received almost instantaneously, while other messages are received only after some delay. However, no acknowledgement time-outs ever occur.

| Message | Direction | Length | Transmission time | Arrival time |
|---|---|---:|---|---|
| `m1` | A → B | 10 | `t1` | `t1` |
| `m2` | B → A | 20 | `t2` | `t2` |
| `m3` | A → B | 30 | `t3` | `t4` |
| `m4` | B → A | 40 | `t3` | `t4` |
| `m5` | A → B | 50 | `t5` | `t5` |

Provide the values of the following header fields of the various messages.

1. Acknowledgement number of `m1`.
2. Sequence number of `m2`.
3. Acknowledgement number of `m3`.
4. Acknowledgement number of `m4`.
5. Window advertisement of `m5`.

---

## Question 3

You are strongly encouraged to write your answers in your script and copy them afterwards to your answer sheet — in particular for this question.

The computer H is a host on Acme Corporation's network. Its IP address is `222.222.222.222`. At this stage Acme Corporation does not use any subnetting. Provide all IP addresses in CIDR notation. Note that CIDR notation is never used for a netmask.

1. Provide Acme Corporation's network address.
2. Provide the broadcast address for Acme Corporation.
3. Provide the netmask used by Acme Corporation.

Acme Corporation wants to subnet its network into at least 10 subnets, such that each subnet can handle at least 50 hosts. Assume the IP address of host H is not changed.

4. Provide the netmask that Acme Corporation now uses on its internal network.
5. Provide the network address of the subnet on which H now resides.
6. Provide the broadcast address of the subnet on which H now resides.
7. According to Acme Corporation's plan ten subnets, numbered from 0 to 9, had to be created. What is the number of the subnet on which H is now located? A logical answer would be a number from 0 to 9. However, the subnetting process could have created more than these ten subnets.
8. According to Acme Corporation's plans, each subnet would support at least 50 hosts, numbered from 1 to 50. However, the subnetting process could have created support for host numbers beyond 50. What is the host number of H on its new subnet?

Acme Corporation now finds that it needs one subnet that can handle more hosts than what they initially anticipated. They therefore decide to supernet exactly four subnets. One of the four subnets to be used is the subnet on which H resides. The IP address of H has to remain unchanged.

9. Provide the network address of the new supernet that is now created.
10. Provide the netmask to be used on this new supernet.

---

## Question 4

Some TCP timers are created when necessary. Other TCP timers exist for the duration of a connection. When the former timers are created, they start counting down. When the pre-existing timers are activated, they start counting down. For both these counter types we will simply say that they are activated. A counting timer may be stopped; for the former type of counters, stopping would mean that they are deleted; for the latter type, the counter may simply remain in this stopped state. When a timer reaches 0, it is said to expire; again this may cause the timer to be deleted or to just remain with a 0 value until they are activated again. A counter may be reset, which would mean it starts counting down from its initial value again. For the questions that follow, only provide the name of the timer. If the answer is the persistent timer, simply say persistent. Note that the timer would always be local to the endpoint at which the event, such as receiving a segment, occurs.

1. Name a timer that is activated when an endpoint transmits a segment containing data.
2. Name a timer that is activated when an endpoint receives a segment containing data.
3. Name a timer that is reset whenever an endpoint receives any segment.
4. Name a timer that would cause a probe to be transmitted if it expires.
5. Name a timer that may be stopped when an endpoint receives a segment that contains an acknowledgement number.

---

## Question 5

Consider the two routing tables provided below.

Let's call the first router R1. R1 has a number of interfaces with names ranging from `eth0` to `eth11`. It also has a loopback interface, `lo`. It runs the EdgeOS operating system, which you have presumably not seen before. However, you should be able to interpret its output based on your knowledge of what one would expect in a routing table.

```text
$ show ip route
Codes: K - kernel, C - connected, S - static, R - RIP, B - BGP
       O - OSPF, IA - OSPF inter area,
       N1 - OSPF NSSA external type 1, N2 - OSPF NSSA external type 2
       E1 - OSPF external type 1, E2 - OSPF external type 2
       > - selected route, * - FIB route, p - stale info

IP Route Table for VRF "default"
S    *> 0.0.0.0/0 [1/0] via 192.168.2.14, eth9
C    *> 10.1.0.0/16 is directly connected, eth0
C    *> 127.0.0.0/8 is directly connected, lo
C    *> 192.168.2.0/24 is directly connected, eth9
```

Let's call the second router R2. The address associated with one of the network interfaces of R2 is `192.168.2.14`. Besides being a router, R2 is also a NAT box that serves as a default route: it would replace the source address of any packet that it cannot deliver with its public address and then forward the IP datagram using the PPPoE protocol to another router from which it will travel to its ultimate destination. R2 uses a version of Linux with which you are presumably not familiar. Some columns of its routing table are not shown to simplify matters. Note the use of Genmask in Linux, which is similar to a netmask. Note the use of Gateway to indicate the next hop, which is `0.0.0.0` for a direct delivery.

```text
# netstat -r
Kernel IP routing table
Destination     Gateway        Genmask          Flags  Metric  Iface
10.1.0.0        192.168.2.13   255.255.0.0      UG     1       br0
41.170.74.97    0.0.0.0        255.255.255.255  UH     0       ppp0
192.168.1.0     192.168.2.13   255.255.255.0    UG     1       br0
192.168.2.0     0.0.0.0        255.255.255.0    U      0       br0
```

Here is the initial output of a `tracert` command executed from a host on the network. Let's call this host H.

```text
C:\>tracert -d 8.8.8.8

Tracing route to 8.8.8.8 over a maximum of 30 hops

  1    <1 ms    <1 ms    <1 ms    10.1.1.13
  2    <1 ms    <1 ms    <1 ms    192.168.2.14
  3     2 ms     2 ms     1 ms    41.170.74.97
  ...
```

Some questions below will ask you about a route, or path, that will be traced by `tracert` or `traceroute`. For the case above this route, or path, would refer to `10.1.1.13`, `192.168.2.14`, `41.170.74.97`, ... The `-d` flag used with the command simply means “Do no resolve” — in other words, it should provide the IP addresses, rather than attempt to find a name in the DNS that matches an address.

Assume C1 is a computer connected as `192.168.1.1` and C2 is connected as `192.168.2.1`. Now answer the following questions about the network.

1. To which interface on which router is H connected?
2. R1 and R2 are obviously directly connected. Name the interface of R1 and the interface of R2 that are connected.
3. Assume the command `traceroute -d 192.168.2.1` is executed on C1. Provide the path that will be returned.
4. Assume the command `traceroute -d 192.168.1.1` is executed on C2. C2 is just a plain workstation without any additional network functionality. The route shown will still either be `192.168.2.13` followed by `192.168.1.1`, or it will be `192.168.2.14`, `192.168.2.13` and `192.168.1.1`. Which one of C2's configuration parameters will determine which of the two outcomes will be observed?
5. Suppose the command `traceroute -d 10.10.10.10` is executed on C1. Provide the second node on the path that would be returned by this command.

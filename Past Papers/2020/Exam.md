# COS 332 — Computer Networks
## June 2020 Examination

**Score:** 72 / 100 | **Time:** 3 hours (08:00 – 11:00)

---

**Instructions:**
- Closed-book test.
- "COS332 Hamming Code" refers to Hamming code using **even parity**, with bits numbered **right to left**.

---


## Question 1

### 2.

**The routing prefix in an IPv6 address (normally) consists of the ___ of the address.**

- A: First 32 bits
- B: First 48 bits
- C: First 64 bits
- D: First 128 bits


---

### 3.

**The ASCII value of A is 41 (hex). Which of the following is a quoted-printable representation of "A=B"?**

- A: A=3DB
- B: =41=3D=42
- C: 41 3D 42
- D: A=B


---

### 4.

**The software providing services on the internet is often known as a ___.**

- A: Server process
- B: Daemon
- C: Driver
- D: Middleware


---

### 5.

**HTTP is on the ___.**

- A: Transport layer
- B: Network layer
- C: Application layer
- D: Session layer


---

### 6.

**Which of the following countries is not directly linked to SEACOM?**

- A: Kenya
- B: South Africa
- C: Tanzania
- D: DRC


---

### 7.

**To terminate an FTP session, the following command(s) may be used:**

- A: quit only
- B: quit and/or bye
- C: disconnect
- D: close


---

### 8.

**Which of the following is (are) bootstrapping protocols?**

- A: DHCP only
- B: BOOTP only
- C: DHCP and BOOTP
- D: SNMP and DHCP


---

### 9.

**The HTTP header contains a Host field in order to support ___.**

- A: Persistent connections
- B: Virtual hosting
- C: Chunked transfer encoding
- D: Proxy caching


---

### 10.

**To share a secret between n persons so that at least k of them have to cooperate to determine the secret, one may use the method of ___.**

- A: Diffie-Hellman
- B: RSA
- C: Blakley
- D: Shamir


---

### 11.

**Which aspect is NOT standardised by RS-232?**

- A: Mechanical
- B: Electrical
- C: Functional
- D: Procedural


---

### 12.

**If the receiver wants to react positively to an RS-232 RTS request, it will send a ___.**

- A: DTR
- B: DSR
- C: CTS
- D: DCD


---

### 13.

**A null modem is ___.**

- A: A modem used between an analog device and a digital medium
- B: A cable that connects two DTEs directly by crossing the transmit/receive lines, without actual modems
- C: A wireless modem with no signal
- D: A modem used between a digital device and a digital medium


---

### 14.

**The entry 0.0.0.0/0 in a routing table is used to provide information about the ___.**

- A: Loopback interface
- B: Broadcast address
- C: Default gateway
- D: Subnet mask


---

### 15.

**Which transport layer protocol(s) is/are used by DNS?**

- A: TCP only
- B: UDP
- C: Both UDP and TCP
- D: SCTP


---

### 16.

**Given that the speed of light is 3 × 10⁸ m/s, how long does it take a signal to travel from an earth station to a geostationary satellite and back to another earth station?**

- A: 0,06 s
- B: 0,12 s
- C: 0,24 s
- D: 0,48 s


---

### 17.

**In MACA, RTS is an acronym for ___.**

- A: Ready To Send
- B: Request To Send
- C: Received Terminal Signal
- D: Routing Table Signal


---

### 18.

**The TTL field in an IP datagram ___.**

- A: Specifies the time in seconds the packet may exist on the network
- B: Determines the maximum number of hops over which the packet can be forwarded
- C: Indicates the time the packet was created
- D: Sets the retransmission timeout for TCP


---

### 19.

**A zone transfer refers to the process of ___.**

- A: Transferring files between two DNS clients
- B: Moving a domain from one registrar to another
- C: Copying DNS entries from a primary server to a secondary server
- D: Updating the root DNS servers


---

### 20.

**Suppose the first octet of a UTF-8 character is 193. How long (in octets) will the entire character be?**

- A: 1
- B: 2
- C: 3
- D: 4


---

### 21.

**Hop count refers to ___.**

- A: The number of times a packet has been bounced between two specific routers
- B: The number of intermediate nodes (routers) a packet traverses between source and destination
- C: The round-trip time of a packet
- D: The number of physical links in the path


---

### 22.

**When TCP uses a three-way handshake, the first ACK is for ___ data byte(s).**

- A: 1
- B: Whatever the first message included
- C: The server's initial sequence number
- D: 0


---

### 23.

**A modem ___.**

- A: Converts digital signals to analog signals only
- B: Modulates a digital signal so that it can be transmitted via an analog medium over a long distance
- C: Amplifies signals for long-distance transmission
- D: Converts analog signals to digital signals only


---

### 24.

**Which field does NOT occur in the UDP header?**

- A: Source port
- B: Checksum
- C: Length
- D: Sequence number


---

### 25.

**TFTP ___.**

- A: Uses TCP for reliable delivery
- B: Uses UDP
- C: Supports user authentication
- D: Provides directory listing functionality


---

### 26.

**Which of the following is NOT a valid ASN.1 constructor?**

- A: SEQUENCE
- B: CHOICE
- C: SET
- D: RECORD


---

### 27.

**Two stations communicate using HDLC (basic mode, modulo-8). Station A sent 15 frames to B; B sent 9 frames to A. All frames received. B now sends another frame. What are N(R) and N(S)?**

- A: N(R)=15, N(S)=9
- B: N(R)=7, N(S)=1
- C: N(R)=0, N(S)=0
- D: N(R)=6, N(S)=0


---

### 28.

**Free Space Optics (FSO) is a technology that ___.**

- A: Uses radio waves to transmit data through the atmosphere
- B: Transmits data using modulated beams of light (laser or LED) through the atmosphere
- C: Requires a physical fiber cable between endpoints
- D: Only works in indoor environments


---

### 29.

**Consider the problem of transparency in SMTP. Which of the following is true?**

- A: Users must avoid starting a line with a period, as SMTP cannot handle it transparently
- B: In most e-mail programs users should avoid typing a full stop on a line of its own, because that will prematurely terminate the body of the message
- C: The SMTP protocol handles this transparently: the client doubles any leading period in a message line, and the server removes the extra period
- D: SMTP does not have a transparency problem since it uses binary encoding


---

### 30.

**Which of the following message description languages allow(s) one to prescribe the exact number of space characters that may occur in a message?**

- A: BNF only
- B: ABNF only
- C: Both BNF and ABNF
- D: ASN.1 only


---

### 31.

**An application protocol will typically respond with a message in the ___-range when it successfully completed a request.**

- A: 100s
- B: 200s
- C: 300s
- D: 400s


---

### 32.

**SAT3 is a ___.**

- A: Communications satellite
- B: Terrestrial radio relay
- C: Undersea cable
- D: Microwave tower network


---

### 33.

**Which well-known port is reserved for HTTPS?**

- A: 80
- B: 110
- C: 443
- D: 8080


---

### 34.

**ADSL ___.**

- A: Is symmetric, providing equal upload and download speeds
- B: Is used between the exchange and the user of the telephone service
- C: Is asymmetric — it provides faster download speeds than upload speeds, using existing copper telephone lines
- D: Uses fiber optic cable in the local loop


---

### 35.

**Two stations communicate using HDLC (extended mode, modulo-128). Station A sent 15 frames to B; B sent 9 frames to A. All frames received. B now sends another frame. What are N(R) and N(S)?**

- A: N(R)=7, N(S)=1
- B: N(R)=14, N(S)=8
- C: N(R)=15, N(S)=9
- D: N(R)=0, N(S)=0


---

### 36.

**Let S = source address, D = destination address, N = netmask, & = bitwise AND. If S&N = D&N, the router will ___.**

- A: Forward the packet to the next hop
- B: Drop the packet
- C: Directly deliver the packet
- D: Send an ICMP redirect


---

### 37.

**If an HTTP server has insufficient storage available to process a request, it should return the following status code:**

- A: 403
- B: 404
- C: 500
- D: 507


---

### 38.

**Assume you are writing a server intended to be accessed by a Telnet client. Which of the following correctly describes how the server should handle echoing?**

- A: The server should issue an ANSI escape sequence to disable local echoing at the client
- B: The client always handles its own echoing; the server should not interfere
- C: The server should use Telnet option negotiation (IAC WILL ECHO / IAC DONT ECHO) to disable client-side echoing and perform server-side echoing
- D: The server should use UDP to bypass the Telnet echo mechanism


---

### 39.

**The UTF-8 representation of U+05D0 is ___.**

- A: C5 D0
- B: D7 90
- C: E0 85 90
- D: 05 D0


---

### 40.

**On which ISO OSI layer does the World Wide Web fit?**

- A: Layer 4 (Transport)
- B: Layer 5 (Session)
- C: Layer 6 (Presentation)
- D: Layer 7 (Application)


---

### 41.

**Latency refers to ___.**

- A: The maximum possible speed at which a network can operate
- B: The number of packets lost per second
- C: The time delay from when a signal is transmitted to when it is received at the destination
- D: The total bandwidth of a network link


---

### 42.

**Which of the following is the latest ratified (accepted) standard for WLANs?** *(as of July 2020)*

- A: IEEE 802.11g
- B: IEEE 802.11n
- C: IEEE 802.11ac
- D: IEEE 802.11ax


---

### 43.

**An application protocol will typically respond with a message in the ___-range when security or configuration errors prevented it from completing a request.**

- A: 200s
- B: 300s
- C: 400s
- D: 500s


---

### 44.

**If SMTP cannot deliver a message, it may ___.**

- A: Silently discard the message with no notification
- B: Send the message to a secondary server
- C: Immediately return an error to the sender without retrying
- D: Queue the message and retry delivery, and if ultimately unsuccessful, return an NDR (bounce) to the sender


---

### 45.

**"Peer" in ISO OSI terminology refers to ___.**

- A: A router in the same autonomous system
- B: Software on the same layer as other software
- C: A physical connection between two network devices
- D: The adjacent layer above or below


---

### 46.

**If a computer wants to send data to a modem, RS-232 lines are activated in the following order:**

- A: RTS, CTS, DTR, DSR, TD
- B: DTR, DSR, RTS, CTS, TD
- C: DSR, DTR, CTS, RTS, TD
- D: TD, RTS, CTS, DTR, DSR


---

### 47.

**In data communications a protocol is always ___.**

- A: A physical standard for cables and connectors
- B: An agreement between two hardware vendors
- C: A detailed description of the rules to be followed when communicating
- D: A software library for network programming


---

### 48.

**The most important use(s) of RFCs is (are) ___.**

- A: All of the above
- B: Publishing proposed and accepted Internet standards and protocols
- C: Defining hardware manufacturing specifications
- D: Setting legally binding Internet regulations


---

### 49.

**An email message containing a PDF attachment may use the following MIME subtype:**

- A: text/plain
- B: application/pdf
- C: multipart/mixed
- D: multipart/alternative


---

### 50.

**To use POP3 anonymously, one uses the command ___.**

- A: ANON
- B: USER anonymous
- C: AUTH ANONYMOUS
- D: None of the above


---

### 51.

**X.509 is a standard of the ___.**

- A: IEEE
- B: IETF
- C: ISO
- D: ITU-T


---

### 52.

**Fewer collisions occur with the slotted Aloha protocol than with pure Aloha, since ___.**

- A: Slotted Aloha uses collision detection
- B: Slotted Aloha uses acknowledgements for every frame
- C: Slotted Aloha reduces the number of frames that overlap partially
- D: Slotted Aloha uses smaller frame sizes


---

### 53.

**Which of the following is NOT a valid UTF-8 sequence?**

- A: C2 A3
- B: E2 82 AC
- C: F0 90 80 80
- D: F2 B3 7F BA


---

### 54.

**The advantage of a crossbar switch over a bus is the fact that it ___.**

- A: Is cheaper to implement
- B: Requires fewer connection points
- C: Allows multiple simultaneous connections between different pairs of ports
- D: None of the above *(original exam answer)*


---

### 55.

**Ethernet addresses have to be unique. This is accomplished as follows:**

- A: The network administrator assigns a unique address to each card
- B: Addresses are assigned dynamically by a DHCP server
- C: The operating system generates a unique address at boot time
- D: The IEEE allocates blocks of addresses (OUIs) to manufacturers, who burn a globally unique address into each NIC


---

### 56.

**Multicast (Class D) IP addresses may be used to establish ___.**

- A: Point-to-multipoint TCP connections
- B: Broadcast domains
- C: Multicast groups for one-to-many communication (UDP-based)
- D: Anycast routing paths


---

### 57.

**The theoretical upper time bound in a CSMA/CD protocol to send frame n is ___ slots.**

- A: 2ⁿ − 1
- B: n × 512
- C: 2ⁿ
- D: None of the above


---

### 58.

**The layer 2 data delineation problem is about ___.**

- A: Addressing frames on the network
- B: Error correction in transmitted data
- C: Marking the boundaries of a frame
- D: Routing packets between subnets


---

### 59.

**The structure used to store data used by SNMP is known as ___.**

- A: OID
- B: MIB
- C: PDU
- D: TLV


---

### 60.

**When a token is lost in an IEEE 802.5 network, the network uses the following algorithm to regenerate the token:**

- A: Ring Maintenance Protocol
- B: Bully
- C: Election by lowest address
- D: Flooding


---

### 61.

**Which of the following is NOT an SNMP request?**

- A: GetRequest
- B: SetRequest
- C: GetNextRequest
- D: Reboot


---

### 62.

**Received COS332 Hamming value: `111010010111`. At most one bit changed. Which bit changed? (0 = no change)**

- A: 0
- B: 3
- C: 6
- D: 9


---

### 63.

**Received COS332 Hamming value: `110110011011`. What 12-bit string was originally transmitted?**

- A: 110110011011
- B: 110110010011
- C: 110110001011
- D: 111110011011


---

### 64.

**Received COS332 Hamming value: `111011111001`. At most one bit changed. Which bit changed?**

- A: 0
- B: 4
- C: 8
- D: 12


---

### 65.

**Received COS332 Hamming value: `101101111100`. What 12-bit string was originally transmitted?**

- A: 101101111100
- B: 111101111100
- C: 001101111100
- D: 101101101100


---

### 66.

**Received COS332 Hamming value: `101010001011`. At most one bit changed. Which bit changed?**

- A: 0
- B: 3
- C: 6
- D: 9


---

### 67.

**Received COS332 Hamming value: `101110010100`. At most one bit changed. Which bit changed?**

- A: 1
- B: 3
- C: 5
- D: 0


---

### 68.

**Received COS332 Hamming value: `010010000010`. At most one bit changed. What decimal number was supposed to have been sent?**

- A: 32
- B: 64
- C: 128
- D: 48


---

### 69.

**Received COS332 Hamming value: `100110010100`. At most one bit changed. What decimal number was supposed to have been sent?**

- A: 128
- B: 175
- C: 200
- D: 211


---

### 70.

**Convert the byte sequence `EE AA B2` from UTF-8 to Unicode. (Omit U+, give four hex digits.)**

- A: EAAB
- B: EAB2
- C: EEAB
- D: EA32


---

### 71.

**Convert U+8F18 to UTF-8. (2-digit bytes separated by a single space.)**

- A: E8 BC 98
- B: E8 BD 98
- C: E9 BC 98
- D: E8 BC 88


---

### 72.

**Convert the byte sequence `EE A5 B2` from UTF-8 to Unicode. (Omit U+, give four hex digits.)**

- A: EEA5
- B: EA52
- C: E972
- D: E9B2


---

### 73.

**Convert the byte sequence `EE B4 87` from UTF-8 to Unicode. (Omit U+, give four hex digits.)**

- A: EEB4
- B: EB07
- C: ED17
- D: ED07


---

### 74.

**Convert U+4EE8 to UTF-8. (2-digit bytes separated by a single space.)**

- A: E4 BA A8
- B: E4 BB A8
- C: E4 BB B8
- D: E5 BB A8


---

*Questions 75–79 are based on the TCP scenario below.*

**Scenario:** A has just sent to B: SEQ=100, LEN=500, ACK=1000, WIN=2000. B then sent to A: LEN=300, WIN=1000. The following events occur in order (events 3 and 4 happen simultaneously and arrive a split second later):
1. A sends to B with LEN=200.
2. B consumes 500 bytes from its buffer.
3. A sends to B with LEN=600.
4. B sends to A with LEN=200.
5. A consumes 1000 bytes from its buffer.
6. A sends to B with LEN=300.

*Messages 1, 3, 4, and 6 refer to the messages sent in events 1, 3, 4, and 6 respectively.*

---

### 75.

**What is the SEQ value sent along with message 1?**

- A: 100
- B: 500
- C: 600
- D: 800


---

### 76.

**What is the window advertisement value sent along with message 4?**

- A: 300
- B: 800
- C: 1000
- D: 1300


---

### 77.

**What is the ACK value sent along with message 3?**

- A: 1000
- B: 1300
- C: 1600
- D: 800


---

### 78.

**What is the ACK value sent along with message 4?**

- A: 600
- B: 700
- C: 800
- D: 1000


---

### 79.

**What is the ACK value sent along with message 1?**

- A: 1000
- B: 1300
- C: 1600
- D: 800


---

### 80.

**The start of frame delimiter follows the preamble in an Ethernet frame. What is its binary value?**

- A: 10101010
- B: 11111111
- C: 10101011
- D: 01010101


---

### 81.

**The process of inserting special values into SDLC/HDLC messages to ensure that data is not mistaken for delimiting characters is known as ___.**

- A: Byte stuffing
- B: Flag insertion
- C: Bit stuffing
- D: Escape encoding


---

### 82.

**The start of a token ring message is indicated by the octet `JK0JK000`. Using `^` for "high" and `_` for "low", what is the actual signal, starting with a low signal?**

- A: `_^___^^^_^_^_`
- B: `__^^^___^^^_^_^_`
- C: `_^_^_^^^___^^^`
- D: `^^___^^^_^_^__`


---

### 83.

**The payload of an Ethernet frame cannot exceed ___ octets.**

- A: 512
- B: 1024
- C: 1500
- D: 9000


---

### 84.

**The bit pattern `01111110` used in SDLC/HDLC to delineate frames is known as a ___.**

- A: Preamble
- B: Delimiter
- C: Flag
- D: Sentinel


---

*Questions 85–92 use the following scenario:*
*Your company uses a classless IPv4 address with a **14-bit** network prefix. One address on the network is **99.33.22.13**. The organisation is subnetted to handle 10 subnets with 200 hosts each, using netmask **255.255.192.0 (/18)**. Subnets are numbered starting from 1.*

---

### 85.

**What is the network address of your company? (CIDR notation)**

- A: 99.33.0.0/14
- B: 99.32.0.0/14
- C: 99.0.0.0/14
- D: 99.32.0.0/16


---

### 86.

**What is the broadcast address of your company?**

- A: 99.33.255.255
- B: 99.34.255.255
- C: 99.35.255.255
- D: 99.32.255.255


---

### 87.

**What netmask will you use to handle 10 subnets with 200 hosts each?**

- A: 255.255.255.0 (/24)
- B: 255.255.192.0 (/18)
- C: 255.255.128.0 (/17)
- D: 255.255.224.0 (/19)


---

### 88.

**What is the network address of subnet 1? (CIDR notation)**

- A: 99.32.0.0/18
- B: 99.32.64.0/18
- C: 99.32.128.0/18
- D: 99.33.0.0/18


---

### 89.

**What is the broadcast address of subnet 12?**

- A: 99.34.255.255
- B: 99.35.0.255
- C: 99.35.63.255
- D: 99.35.127.255


| Subnet | Network Address |
|--------|-----------------|
| 1 | 99.32.64.0/18 |
| 2 | 99.32.128.0/18 |
| 3 | 99.32.192.0/18 |
| 4 | 99.33.0.0/18 |
| 5 | 99.33.64.0/18 |
| 6 | 99.33.128.0/18 |
| 7 | 99.33.192.0/18 |
| 8 | 99.34.0.0/18 |
| 9 | 99.34.64.0/18 |
| 10 | 99.34.128.0/18 |
| 11 | 99.34.192.0/18 |
| **12** | **99.35.0.0/18** |

---

### 90.

**What is the network address of subnet 4? (CIDR notation)**

- A: 99.32.128.0/18
- B: 99.32.192.0/18
- C: 99.33.0.0/18
- D: 99.33.64.0/18


---

### 91.

**On which subnet is the address 99.32.134.178 located?**

- A: 1
- B: 2
- C: 3
- D: 4


---

### 92.

**On which subnet is the address 99.34.20.77 located?**

- A: 6
- B: 7
- C: 8
- D: 9


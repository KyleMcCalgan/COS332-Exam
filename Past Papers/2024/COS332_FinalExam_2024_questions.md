# COS332 Final Exam — 19 July 2024

**Course:** Computer Science  
**Paper:** COS332  
**Marks:** 100

---

## Question 1 [50]

In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

1. Which of the following is a popular application used to inspect traffic that flows on a network?
   - A. SniffAndSnort
   - B. telnet
   - C. nslookup
   - D. tracert / traceroute
   - E. Wireshark

2. The ASCII standard standardises a(n) ... character code.
   - A. 7-bit
   - B. 8-bit
   - C. 9-bit
   - D. More than one of the above
   - E. All of the above

3. On which layer is SSL/TLS usually positioned?
   - A. 6
   - B. 5
   - C. “Just above 5”
   - D. “Just above 4”
   - E. 4

4. A BER value in ASN.1 is, in principle, encoded as a triple consisting of:
   - A. A type, a subtype and a value.
   - B. A type, a length and a value.
   - C. A constructor and two operands.
   - D. A variable name, as well as its minimum and maximum values.
   - E. The same value encoded in binary, text and hexadecimal.

5. EBNF is:
   - A. An abbreviation for Extended Backus-Naur Form
   - B. Often used by RFCs to specify the content of data messages
   - C. Standardised in an RFC which is deemed as the authoritative definition of EBNF
   - D. More than one of the above
   - E. All of the above

6. Suppose an HTTP request contains the following in its header:

   ```http
   Accept-Charset: Shift_JIS
   ```

   Suppose a Web site is visited that contains text in “plain” ASCII and the server does not support Shift JIS. What will happen?

   - A. The browser will display an error message to indicate that the content cannot be displayed.
   - B. Google Translate will be called to translate the page to a language that can be represented in Shift JIS.
   - C. The server will serve ASCII and the browser will interpret it as Shift_JIS, resulting in a garbled display.
   - D. The `Accept-Charset` header given implies ISO-8859-1, so the pages should be served and displayed without problems.

7. According to RFC4511 all LDAP messages are “transferred using a subset of ASN.1 Basic Encoding Rules ([BER]).” This means that messages will:
   - A. Use an octet as a type descriptor at the start of any value.
   - B. The length of the actual data will be explicitly specified.
   - C. The actual data will be encoded in its native format, such as binary for integers.
   - D. More than one of the above
   - E. All of the above

8. Which of the following is a valid ASN.1 encoding?
   - A. BER
   - B. ASCII
   - C. EBCDIC
   - D. ISO OSI
   - E. Grammar

9. Which of the following is not a valid ASN.1 constructor?
   - A. SEQUENCE
   - B. MESSAGE
   - C. CHOICE
   - D. SET

10. The syntactic structure of an ASN.1 message is defined using:
    - A. A grammar
    - B. An informal description in a natural language
    - C. A diagrammatic depiction of the message
    - D. A bit pattern
    - E. A list of the types of the components of the message

11. If MIME is deemed to be a data communications protocol it would fit best on layer ... of the ISO OSI model.
    - A. 7
    - B. 6
    - C. 5
    - D. 4
    - E. 3

12. Which character set is assumed to be understood by all parties involved in an HTTP exchange?
    - A. ASCII
    - B. EBCDIC
    - C. Unicode
    - D. UTF-8
    - E. ISO-8859-1

13. Suppose computers A and B both use extended ASCII to represent characters. There is no character conversion mechanism between A and B. Assume that every byte transmitted will be received correctly; no data loss or transmission errors will occur. What challenge(s) may be experienced when these two computers communicate?
    - A. When A sends a digit or one of the 26 Latin characters, in either lower or uppercase, the recipient may interpret at least one of these 62 characters incorrectly.
    - B. A may mark up a character, for example `&eum1;`, and such characters may be received incorrectly at the destination.
    - C. It is possible that at least one of the following seven punctuation marks may not be communicated correctly: `? ! , . " % : &`
    - D. These computers will not experience any challenges since they use the same character encoding.
    - E. None of the problems listed above will occur, but other challenges may exist.

14. Which Content-Transfer-Encoding would be most appropriate to transfer a PNG image via SMTP?
    - A. 8bit
    - B. binary
    - C. quoted-printable
    - D. base64
    - E. 7bit

15. Say a damaged packet arrives at its destination. The recipient may, for example, determine that the packet is damaged when the checksum does not match. In many protocols it may then send a NAK, negative acknowledgement, to the original sender to request retransmission. Suppose A sends a TCP segment to B, but it arrives damaged at B. How is this resolved?
    - A. B sets the NAK TCP flag and sends it as a response to A.
    - B. B discards the segment and does not acknowledge it; the retransmission timer at A expires and the packet is sent again.
    - C. B requests the network layer at B to deal with the error, and this triggers a retransmission of the segment.
    - D. B corrects the damaged segment and eventually acknowledges receipt.
    - E. The lower layer protocols perform error checking, so a damaged segment will never arrive; errors will always be corrected on a lower layer.

16. Which well-known port is used for control messages by an FTP server?
    - A. 20
    - B. 21
    - C. 22
    - D. 23
    - E. 24

17. Which of the following fields does not occur in a TCP header?
    - A. Source port
    - B. Window advertisement
    - C. Sequence number
    - D. Options
    - E. Length

18. A program that wants to open a socket in order to act as a server needs to specify the following:
    - A. The address of the server
    - B. The address of the client
    - C. The port on the server
    - D. The port on the client
    - E. More than one of the above

19. Which command enables one to see the status of transport layer connections on a host, in most operating systems?
    - A. netstat
    - B. ping
    - C. tracert / traceroute
    - D. tcp-show
    - E. ps

20. What type of port is port 55555?
    - A. Registered
    - B. Well-known
    - C. Dynamic
    - D. Practical
    - E. Temporary

21. What does the claim that QUIC is a quick protocol mean?
    - A. It manages the lower layers to transmit raw data at higher bit rates.
    - B. It reduces latency when establishing or re-establishing a connection.
    - C. Where multiple parts of a message have to be transported it ensures that parts of the message are delivered quickly even if some parts are delayed.
    - D. More than one of the above
    - E. All of the above

22. Which of the following actions always happen(s) when a client establishes a QUIC connection with a server?
    - A. The client chooses a connection ID to be used by the server.
    - B. The client includes initial data encrypted with the server’s public key.
    - C. The client informs the server which cryptographic suite will be used.
    - D. The client sends an initial packet numbered 0 on the wire.
    - E. None of the above

23. QUIC connections can migrate. Which party can initiate such a migration in QUICv1 or QUICv2?
    - A. The client
    - B. The server
    - C. The network management system
    - D. More than one of the above
    - E. All of the above

24. Which of the following headers are always present in a long QUIC header? Include cases where the length of the field will be present and may be 0, meaning that the field itself may be omitted.
    - A. Version
    - B. Source connection ID
    - C. Destination connection ID
    - D. More than one of the above
    - E. All of the above

25. Assume a client establishes a new QUIC connection at time `t0` with a server. The server receives the initial packet at time `t1` and immediately sends its response(s), which arrive(s) at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server transmitting at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which application data may sometimes be sent?
    - A. `t0`
    - B. `t1`
    - C. `t2`
    - D. `t3`
    - E. It is impossible to say.

26. Assume a client establishes a new QUIC connection at time `t0` with a server. The server receives the initial packet at time `t1` and immediately sends its response(s), which arrive(s) at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server transmitting at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which 1-RTT application data may sometimes be sent?
    - A. `t0`
    - B. `t1`
    - C. `t2`
    - D. `t3`
    - E. None of the above

27. Assume a client establishes a new QUIC connection at time `t0` with a server. The server receives the initial packet at time `t1` and immediately sends its response(s), which arrive(s) at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server transmitting at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which the connection may be deemed to be fully established?
    - A. `t0`
    - B. `t1`
    - C. `t2`
    - D. `t3`
    - E. None of the above

28. What is the address, in CIDR notation, of the netblock 41.32.0.0 to 41.39.255.255?
    - A. 41.32.0.0/10
    - B. 41.32.0.0/11
    - C. 41.32.0.0/12
    - D. 41.32.0.0/13
    - E. None of the above

29. If one sends a message to an IP multicast address, the message will be delivered to:
    - A. The node to which that IP address has been assigned.
    - B. All nodes on the local network.
    - C. All nodes that are members of some group.
    - D. The network itself, rather than to a host on the network.
    - E. To the network gateway that connects the network to other networks.

30. An IP datagram may be fragmented to:
    - A. Expedite routing.
    - B. Fit IP datagrams in size-constrained layer 2 frames.
    - C. Ensure that fixed size packets are sent to the lower layer.
    - D. Fit IP datagrams in size-constrained layer 4 segments.
    - E. Minimise data loss if a packet is discarded.

31. Which of the following IPv4 addresses is/are routable on the public Internet?
    - A. 137.215.103.222
    - B. 169.254.201.102
    - C. 192.168.192.168
    - D. More than one of the above
    - E. All of the above

32. An IP datagram addressed to 10.10.1.2 arrives at node R. R is not directly connected to the destination address. The routing table at R includes the entries below. To which next hop does R forward the datagram?

    ```text
    10.10.10.0/24   192.168.1.1   eth1
    10.10.0.0/16    192.168.2.2   eth2
    10.0.0.0/8      192.168.3.3   eth3
    0.0.0.0/0       192.168.4.4   eth4
    ```

    - A. 192.168.1.1
    - B. 192.168.2.2
    - C. 192.168.3.3
    - D. 192.168.4.4
    - E. More than one of the above

33. The following command, followed by an IP address, may be used on a *nix host to obtain details about the owner of the specified IP address:
    - A. whois
    - B. nslookup
    - C. dig
    - D. ping
    - E. traceroute

34. Consider the IP routing algorithm. Assume it has reached the point where it either consulted the routing table and found no match, or it noted that no routing table exists. For the purpose of this question we assume that these two outcomes are identical. The next step can therefore assume that no routing table exists. What is this next step that it will attempt after establishing that no routing table exists?
    - A. Check whether a default gateway is defined and, if one is defined, forward the packet to such a default gateway.
    - B. Transfer the packet to layer 4 in the protocol stack.
    - C. Directly deliver the packet.
    - D. Discard the packet.
    - E. More than one of the above

35. NAT boxes are often used at the edge of a network based on private addresses. Messages from the hosts on the network to an external host are assigned a public address by the NAT box when the message moves outward via the NAT box. When the NAT box receives a response to such a message, it replaces the public address with the original private address, which enables the NAT box to transmit the message to the original host on the inside of the network.

    Consider the following argument: Since the NAT box converts internal addresses to external addresses and vice versa, the addresses used inside the network are immaterial. Since the private addresses inside the network are never used outside the network, it does not matter whether they are public or private. An organisation can therefore choose to use public addresses inside their network, irrespective of whom they belong to — as long as the NAT box properly hides the addresses used inside the network from ever “escaping”. Critique this argument.

    - A. The argument makes perfect sense. Public addresses can be used without any further restriction inside the network.
    - B. The argument does not consider the fact that public IP addresses are allocated to specific countries. This will confuse routers inside the organisation. However, if only public addresses allocated to the country where the network is located are used inside the network, using public addresses presents no problem.
    - C. The fact that public addresses are associated with specific parties will cause intellectual property challenges if the solution is used. As an example, any network that uses the address 137.215.0.0/16 for its own purposes needs to obtain permission from the University of Pretoria to do so. This would even mean that it is illegal to build an isolated network where one uses the addresses that belong to someone else.
    - D. Using public addresses inside the network will work fine, as long as one subnets the internal addresses exactly as they are subnetted on the public Internet.
    - E. The flaw of the argument is that one would be unable to reach some addresses on the public Internet from inside the network.

36. An IPv4 multicast packet:
    - A. Should be delivered to all subscribed parties.
    - B. In TCP/IP has an IP address with a first byte between 224 and 239, both included.
    - C. Is routed like a class C packet.
    - D. More than one of the above
    - E. All of the above

37. Which ISO OSI layer is generally expected to “throttle” network communication on a busy network to ensure stability of the network?
    - A. 6
    - B. 5
    - C. 4
    - D. 3
    - E. 2

38. IP address 172.16.5.79 is a ... address.
    - A. Class A
    - B. Class B
    - C. Class C
    - D. Class D
    - E. Class E

39. ICMP is used to:
    - A. Report errors that occur on the IP layer.
    - B. Test network functions.
    - C. Modify routes.
    - D. More than one of the above
    - E. All of the above

40. Consider the IP routing algorithm. Suppose one sends an IP datagram to a network address, such as 8.0.0.0, assuming 8.0.0.0/8 is indeed a network address. What should happen to the datagram?
    - A. It should be sent to the destination network and delivered once it reaches that network.
    - B. At the first router the routing algorithm will note that the destination is a network address and discard the datagram.
    - C. The datagram should arrive at the final router. However, that router will not be able to find a host 0, and therefore discard the datagram.
    - D. More than one of the above
    - E. All of the above

41. Suppose `i` is an IPv4 address. Suppose `n` is the network address on which `i` resides. Suppose `m` is the netmask used on `n`. Suppose `b` is the broadcast address of network `n`.

    Let `+` indicate the logical bitwise OR operator. Hence `100 + 101 = 101`. Let `-` indicate the logical bitwise NOT operator. Hence `-101 = 010`. Let `.` be the logical bitwise AND operator. Hence `100 . 101 = 100`.

    Which of the following claims is/are true?

    - A. `i . m = n`
    - B. `i + (-m) = b`
    - C. `i + (-b) = n`
    - D. More than one of the above
    - E. All of the above

42. IEEE 802.3 defines:
    - A. Ethernet
    - B. LLC
    - C. HDLC
    - D. Token ring
    - E. More than one of the above

43. HDLC accomplishes transparency by using:
    - A. Bit stuffing
    - B. Byte stuffing
    - C. Known field lengths
    - D. All of the above
    - E. None of the above

44. When one node polls another, it wants to know whether:
    - A. The other node has something to send.
    - B. The other node is communicating.
    - C. It may send something to the other node.
    - D. None of the above

45. Which of the following is not a function of the data link control layer?
    - A. Data delineation
    - B. Error control
    - C. Encoding
    - D. Media access control
    - E. None of the above

46. When no monitor’s presence is detected on an 802.5 network:
    - A. The hub appoints a new monitor.
    - B. The previous monitor resumes its duties.
    - C. The station with the highest priority starts acting as monitor.
    - D. A new monitor is elected by the remaining nodes.
    - E. The network simply continues operating because it does not really need a monitor.

47. IEEE 802.11 standardises:
    - A. Ethernet
    - B. Token bus
    - C. Token ring
    - D. Security
    - E. Wireless LANs

48. What does data delineation refer to on layer 2?
    - A. Limiting the size of layer 2 frames.
    - B. Marking the boundaries of a frame.
    - C. Picking a data code for data representation.
    - D. Controlling access to a shared medium.
    - E. Encoding data in a form that can be transmitted via layer 1.

49. A master-slave protocol may solve the following problem on layer 2:
    - A. Media access control
    - B. Error control
    - C. Routing
    - D. Polling
    - E. None of the above

50. Suppose a node using SDLC has to transmit the data `01111110`. The data will be observed on the line as:
    - A. `011111010`
    - B. `01111110`
    - C. `011111100`
    - D. `011111110`
    - E. `011111x10`

---

## Question 2 [5]

Provide the following commands/requests that a client would send to a server. Case is not important, but punctuation is. Where the command/request consists of more than one line, you only have to provide the first line of the request.

1. A POP3 client tells the server it wants to download message 5 from the server. (1)
2. An SMTP client informs the server that the destination address of an email is `d@xx.co.za`. (1)
3. An SMTP client informs the server that it is about to send the email, consisting of the email headers and email body, to the server. (1)
4. An HTTP client requests the default/start page from a server. It uses version 1.1 of HTTP. The name of this start page is not known. It may, for example, be `index.html`, but it may also be almost anything else. (1)
5. An FTP client instructs a server to use passive mode. (1)

---

## Question 3 [5]

In the following table Dijkstra’s algorithm was used to calculate the cheapest routes from node A. Complete the table by writing the values that have been omitted, and indicated with lowercase letters in brackets, on your answer sheet. Question marks also indicate values that have been omitted but you do not have to supply those values.

### Network

Edges shown in the diagram:

```text
A-B: 2
A-D: 12
A-F: 13
B-C: 10
B-D: 9
B-F: 8
C-D: 0
D-E: 4
E-F: 1
```

### Table

| Step | S | W | X | Cost B | Cost C | Cost D | Cost E | Cost F | Prior B | Prior C | Prior D | Prior E | Prior F |
|---|---|---|---|---:|---:|---:|---:|---:|---|---|---|---|---|
| 1 | A | ? | B | 2 | ∞ | ? | ∞ | 13 | A | - | A | - | A |
| 2 | A, B | ? | ? | 2 | (a) | (b) | ∞ | 10 | A | ? | B | - | B |
| 3 | ? | ? | ? | 2 | ? | ? | ? | (c) | A | ? | B | ? | B |
| 4 | ? | ? | ? | 2 | ? | ? | ? | 10 | A | (d) | B | ? | B |
| 5 | ? | ? | ? | 2 | (e) | ? | ? | 10 | A | ? | B | ? | B |

---

## Question 4 [5]

Suppose a network uses the Bellman-Ford algorithm to perform routing. At some time `t0` the routing tables at routers C, D and E contain the information provided below. Each routing table consists of three columns: destination, cost, and the next hop to achieve delivery at the indicated cost.

```text
Node C              Node D              Node E
A  7  B             A  20 E             A  6  F
B  1  B             C  3  C             B  1  F
D  3  D             E  2  E             D  2  D
F  2  B             F  7  E             F  4  F
```

The only exchanges of routing tables that occur during the time period of interest are the following: At time `t1 > t0` node C sends its routing table to node D. At time `t2 > t1`, node E sends its routing table to node D.

1. What will the entry for destination A be in node D’s routing table, after receiving and processing the routing table from node C, but prior to `t2`? (1)
2. What will the entry for destination B be in node D’s routing table, after receiving and processing the routing table from node C, but prior to `t2`? (1)
3. What will the entry for destination A be in node D’s routing table, after receiving and processing the routing table from node E? (1)
4. What will the entry for destination B be in node D’s routing table, after receiving and processing the routing table from node E? (1)
5. What will the entry for destination F be in node D’s routing table, after receiving and processing the routing table from node E? (1)

---

## Question 5 [10]

Assume computer addresses consist of single digits. Consider the following zone files at various DNS servers. Assume that records and fields that are not shown, such as SOA records, are not material. Node 1 is the root name server.

> The scan contains a table of zone files at nodes 1 to 6. Use the zone-file table from the paper when answering the questions below.

Perform recursive name resolutions for the following FQDNs. Each line starts with the query that should be performed for the FQDN, A, NS or MX. Name resolution will lead to an address, which, as stated, will consist of a single digit. Write this digit on your answer sheet. If the query cannot be resolved with the information provided, write `N/A` on your answer sheet.

1. `NS b.a` (1)
2. `A b.a` (1)
3. `MX b.a` (1)
4. `NS a.a.a` (1)
5. `MX a.a.a` (1)
6. `A b.a.b` (1)

Now insert resource records in the appropriate zone files to achieve the goals set out in the questions below. If you, for example, want to insert an NS record of the form `c NS 7` at node 5, simply write `At 5: c NS 7`. Note that more than one answer may be correct. Provide only one correct answer for each question.

7. Mail to `b.a` should be delivered to address 9. Consider question (h) and any relevant pre-existing RR entry before answering this question. (1)
8. If node 9 is unavailable, mail to `b.a` should be delivered to address 8. Consider question (g) and any relevant pre-existing RR entry before answering this question. (1)
9. `c.a.a` should be an alias for `b.a.b`. (1)
10. The IPv6 address of `a.a.b` is `2001::2001`. (1)

---

## Question 6 [5]

You receive a sequence of bytes that are supposed to be UTF-8 encoded. This sequence of bytes is provided below; it is one long sequence that has been split into several lines for the sake of readability. Unfortunately, some bytes have been lost during transmission. You are expected to recover all the characters that can be extracted. Where a sequence of one or more bytes does not constitute a character, you have to indicate it using an `X`. Use the form `U+xxxx` to represent the Unicode characters. Suppose you find five subsequences in the sequence where subsequence 1, 2 and 4 are valid Unicode characters, but subsequence 3 and 5 are not, then your answer may look as follows: `1) U+0001 2) U+0002 3) X 4) U+0009 5) X`. Note that more spaces may have been provided on the answer sheet than actual subsequences of characters.

The single byte sequence to process is the following:

```text
C9 90 E1 83 90 F0 9F
A4 E2 9A 93 E1 E1 61
A0 F0 9F 90 A0 F0 9F
8C 8D F2 99 E1 80 80
```

---

## Question 7 [5]

Two TCP nodes, A and B, are busy communicating. At some time A is ready to transmit byte 5000, has just received byte 3000, has a window of 2000 bytes and thinks that the window at B consists of 100 bytes.

A wants to transmit 1000 bytes. It sends the largest segment possible. Provide the values that it places in the following header fields. Note that some fields may consist of components or be implied; you are expected to provide the “logical” value in terms of a byte count, rather than the actual way in which it may be represented in the TCP header.

1. Sequence number
2. Acknowledgement number
3. Length
4. Window advertisement
5. SYN flag

---

## Question 8 [10]

Your organisation uses the following IP address as part of the block assigned to them:

```text
204.204.204.204/18
```

They decide to subnet their address space such that they have at least 250 subnets that can each handle at least 50 hosts.

1. What netmask will they use for the subnets? (1)
2. Consider subnet number 204. What is the network address of this subnet? Express it using CIDR notation. (2)
3. What is the broadcast address of subnet 204? (1)
4. What is the last or “biggest” address that may be assigned to a host on subnet 85? (1)
5. On which subnet will the host with the IP address `204.204.204.204` be? Just provide the number of the subnet. (1)

The organisation decides that it needs a much bigger subnet in the laboratory where `204.204.204.204` is located. They decide to combine a number of subnets into a supernet that can handle at least 2000 hosts. However, they want to sacrifice as few subnets as possible to create this supernet.

6. Provide the netmask associated with this supernet. (1)
7. Provide the network address of this supernet using CIDR notation. (2)
8. When using this supernet, it is possible to address more hosts than would have been possible using the subnets that have been sacrificed to create the supernet. How many more? (1)

---

## Question 9 [5]

1. Which IPv4 header field makes it possible to implement the `traceroute` or `tracert` command? Name a header field that is intentionally set by this command, but has no special meaning to implement, say, the `ping` command. (1)
2. Which ICMP message is typically used to implement the `traceroute` command, given the context of question (a)? Provide the name or number of the ICMP message. (1)
3. Which ICMP request is sent by the client to perform a `ping` command? Provide the name or number of the ICMP command. (1)
4. Which IPv4 addresses are reserved for link-local addresses? Provide the answer in CIDR notation. (1)
5. Provide the IPv4 entry that is used as the destination in a routing table to identify the default gateway. Note that the question deals with the destination and not the next hop. Use CIDR notation to provide your answer. (1)

---

**Total:** 100

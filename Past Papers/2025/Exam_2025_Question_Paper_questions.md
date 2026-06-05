# COS332 Exam 2025 Question Paper

**Course:** Computer Science  
**Paper:** COS332  
**Date:** 10 June 2025  
**Format:** Questions only, transcribed from the supplied PDF. Handwritten notes/circled answers have been omitted.

---

## Question 1

In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### 1)
A layer in the protocol stack generally provides services for:

A. The layer above it  
B. The layer below it  
C. Its peer layer  
D. The application layer  
E. The physical layer

### 2)
Which ISO layer enables process-to-process communication via the network?

A. 6  
B. 5  
C. 4  
D. 3  
E. 2

### 3)
What is the name of layer 5 of the ISO OSI reference model?

A. Application layer  
B. Presentation layer  
C. Session layer  
D. Transport layer  
E. Network layer

### 4)
When a message moves through the protocol stack towards the physical layer, headers are:

A. Appended  
B. Removed  
C. Added  
D. Modified  
E. Rearranged

### 5)
A user is sending mail from `jack@up.hill` to `jill@down.hill` where we assume `.hill` is a valid TLD. Which of the following SMTP commands will be used as part of the SMTP sequence of commands?

A. `rcpt to: jill@down.hill`  
B. `rcpt from: jack@up.hill`  
C. `mail for: jill@down.hill`  
D. `mail from: jill@down.hill`  
E. `mail to: jill@down.hill`

### 6)
HTTP responses, Internet messages (RFC2822 / RFC822), and many other protocols use the same mechanism to separate the header and body of the message. They are separated by:

A. A special ASCII character.  
B. A specific keyword or tag.  
C. The session layer.  
D. A blank line.  
E. None of the above

### 7)
Which condition code will be returned by an SMTP server after successfully handling a `helo` or `ehlo` message?

A. 0  
B. 150  
C. 250  
D. 350  
E. 450

### 8)
After an SMTP client has sent a `data` command, it will usually send several lines of data. It signals to the server that the entire data block has been transmitted by sending the following line:

A. `/data`  
B. `quit`  
C. `.`  
D. A blank line  
E. `fin`

### 9)
The following is an example of an IGP.

A. BGP  
B. OSPF  
C. Dijkstra  
D. More than one of the above  
E. All of the above

### 10)
The class of protocols used for routing between autonomous systems is known as:

A. IGPs  
B. BGPs  
C. EGPs  
D. RIP  
E. Peering

### 11)
The software deployed at a network node that is managed using SNMP from some central location is known as:

A. A manager  
B. An agent  
C. A client  
D. A server  
E. The MIB

### 12)
The `Host:` line, including the name of the host as specified in the URL, forms one of the headers in an HTTP GET request. Why is it necessary?

A. Security/access control. A user should not be able to access an unknown web server using only the address of the server.  
B. Security/integrity. Connecting to the server and informing the server about the expected domain ensures that an incorrect site would not be served.  
C. Virtual hosting. The server may host more than one site.  
D. There is no such `Host:` header.  
E. There is no GET request in HTTP. Some other HTTP requests may include a `Host:` header.

### 13)
Consider a scenario in RIP where a router `r` sends its routing table to a router `s`. An entry in `r`'s table indicates that it can reach a network `n` at a cost of 5. Before receiving the message, the routing table at `s` indicated that it could reach `n` at a cost of 8. What will the cost from `s` to `n` be according to the routing table at `s` after `s` processed the message from `r`?

A. 5  
B. 6  
C. 7  
D. 8  
E. More information about `r` is required to answer the question.

### 14)
A network uses the Bellman-Ford algorithm. The entry in node B's routing table for destination D is currently `(A, 20)`. The cost associated with the link between B and C is 5. C's entry for destination D is currently `(E, 5)`. After C has sent routing information to B, the entry at B for destination D changes to:

A. `(A, 20)`  
B. `(E, 5)`  
C. `(E, 10)`  
D. `(C, 5)`  
E. `(B, 10)`  
F. None of the above

### 15)
Suppose computers A and B both use extended ASCII to represent characters. There is no character conversion mechanism between A and B. Assume that every byte transmitted will be received correctly; no data loss or transmission errors will occur. What challenge(s) may be experienced when these two computers communicate?

A. When A sends a digit or one of the 26 Latin characters, in either lower or uppercase, the recipient may interpret at least one of these 62 characters incorrectly.  
B. A may mark up a character, for example `&euml;`, and such characters may be received incorrectly at the destination.  
C. It is possible that at least one of the following seven punctuation marks may not be communicated correctly: `? = ! , . " % : &`.  
D. These computers will not experience any challenges since they use the same character encoding.  
E. None of the problems listed above will occur, but other challenges may exist.

### 16)
The ASCII for `0` is `30₁₆`. To convert a character `k` to a digit, the following formula(e) may therefore be used:

A. `k - 00001111₂`  
B. `k + 00001111₂`  
C. `k AND 00001111₂`  
D. `k - 48₁₀`  
E. More than one of the above

Note: `OR` is used to denote the logical OR and `AND` the logical AND.

### 17)
Which of the following is not a valid ASN.1 constructor?

A. SEQUENCE  
B. MESSAGE  
C. CHOICE  
D. SET

### 18)
A BER value in ASN.1 is, in principle, encoded as a triple consisting of:

A. A type, a subtype and a value.  
B. A type, a length and a value.  
C. A constructor and two operands.  
D. A variable name, as well as its minimum and maximum values.  
E. The same value encoded in binary, text and hexadecimal.

### 19)
The syntactic structure of an ASN.1 message is defined using:

A. A grammar  
B. An informal description in a natural language  
C. A diagrammatic depiction of the message  
D. A bit pattern  
E. A list of the types of the components of the message

### 20)
Assume an HTTP request includes the following:

```http
Accept-Charset: iso-8859-1, utf-8;q=0.5, *;q=0.7
```

Suppose further that the server supports only UTF-8 and UTF-16. Which code will be used?

A. ISO-8859-1  
B. UTF-8  
C. UTF-16  
D. ASCII  
E. None of the above

### 21)
An email message that contains a PDF document as an attachment may use the following MIME subtype to encapsulate the mail message and its attachment.

A. `multipart/mixed`  
B. `multipart/digest`  
C. `multipart/alternative`  
D. `multipart/plain`  
E. `text/plain`

### 22)
Which of the following is not a common content transfer encoding used for MIME types?

A. 8bit  
B. raw  
C. base64  
D. binary  
E. quoted-printable

### 23)
A “universal” representation may be designed for a data structure that exists at the core of some network protocol; this enables one to transfer a copy of such a data structure from one server that represents the data structure in its own internal format to another server, which uses its own internal structure. To achieve this, the structure is exported from one server into this “universal” representation; it is then imported to the new server's internal format from this “universal” format. The structure associated with the following protocol is a well-known example, along with the name of the “universal” format.

A. SNMP, MIB  
B. LDAP, LDIF  
C. IMAP4, MBOX  
D. DNS, ZONEFILE  
E. HTTP, HTML

### 24)
Huffman code achieves compression by:

A. Spreading 7-bit ASCII characters across 8-bit bytes, thereby “packing” characters more densely.  
B. Representing words using short tokens, rather than by representing each individual character separately.  
C. Assigning codes to characters such that the length of the code inversely correlates with the prevalence of the character.  
D. Rearranging a linear character sequence into a hierarchy, and then by serialising the hierarchy into an efficient linear representation.  
E. More than one of the above

### 25)
In multipart messages the parts are often separated by what looks like a random sequence of characters. Where the multipart structure is introduced, this pattern, which is unlikely to occur inside the parts, is declared as the:

A. nextpart  
B. separator  
C. divider  
D. split  
E. boundary

### 26)
UDP uses the following flow-control mechanism:

A. Stop and Wait  
B. Sliding window  
C. Unrestricted  
D. More than one of the above  
E. All of the above

### 27)
Suppose node A is connected to node B via TCP. When the persistence timer at A expires it implies that:

A. B has not yet acknowledged the last segment A sent to B.  
B. A is waiting for space to free up in B's window before further data can be sent.  
C. A has no data to send, so it transmits a single byte to indicate that it is still present.  
D. More than one of the above  
E. All of the above

### 28)
A TCP connection in the TIME-WAIT state means that:

A. The node is waiting for data from the node that it is connected to.  
B. The connection is about to time-out if no further data is transmitted soon.  
C. The connection will soon be established, as soon as the handshake is completed.  
D. The node is waiting for “lost” traffic to arrive at the port that is no longer in use, before it will be available for reuse.  
E. The network is congested.

### 29)
A TCP node that is in the LISTEN state:

A. Is acting as a server and waiting for a SYN message.  
B. Is acting as a client and has sent a SYN message.  
C. May act as a client after sending a SYN message.  
D. More than one of the above  
E. None of the above

### 30)
Which command enables one to see the status of transport layer connections on a host, in most operating systems?

A. `netstat`  
B. `ping`  
C. `tracert` / `traceroute`  
D. `tcp-show`  
E. `ps`

### 31)
The transport layer protocol that is predicted to eventually replace TCP is:

A. TPO  
B. IP  
C. TCPv2  
D. QUIC  
E. ARPA

### 32)
What does the claim that QUIC is a quick protocol mean?

A. It manages the lower layers to transmit raw data at higher bit rates.  
B. It reduces latency when establishing or re-establishing a connection.  
C. Where multiple parts of a message have to be transported it ensures that parts of the message are delivered quickly even if some parts are delayed.  
D. More than one of the above  
E. All of the above

### 33)
Which of the following actions always happen(s) when a client establishes a QUIC connection with a server?

A. The client chooses a connection ID to be used by the server.  
B. The client includes initial data encrypted with the server's public key.  
C. The client informs the server which cryptographic suite will be used.  
D. The client sends an initial packet numbered 0 on the wire.  
E. None of the above

### 34)
QUIC connections can migrate. Which party can initiate such a migration in QUICv1 or QUICv2?

A. The client  
B. The server  
C. The network management system  
D. More than one of the above  
E. All of the above

### 35)
Which of the following protocol(s) is/are used on the transport layer by DNS?

A. TCP  
B. UDP  
C. IP  
D. More than one of the above  
E. All of the above

### 36)
Multicast class D IP addresses may be used to establish:

A. Point-to-multipoint TCP connections.  
B. Multipoint-to-multipoint TCP connections.  
C. Mesh TCP connections, where every point is effectively connected to every other point.  
D. More than one of the above  
E. None of the above

### 37)
What is the range of the private class B address block?

A. 192.168.0.0-192.168.255.255  
B. 192.168.0.0-192.168.0.255  
C. 192.168.0.0-192.168.168.255  
D. 192.168.0.0-192.169.255.255  
E. 192.168.0.0-192.171.255.255

### 38)
Suppose a router receives an IP datagram `d` and its TTL becomes 0. What may the router do next?

A. Discard `d`.  
B. Forward `d` to the next hop.  
C. Send a time exceeded ICMP message to the source.  
D. More than one of the above  
E. All of the above

### 39)
An IPv6 address consists of:

A. 128 bits.  
B. 16 octets.  
C. 8 hexadecimal numbers, separated by colons.  
D. More than one of the above  
E. All of the above

### 40)
The routing prefix in an IPv6 address typically consists of the ... of the address.

A. first 32 bits  
B. final 32 bits  
C. first 64 bits  
D. final 64 bits

### 41)
ICMP is used to:

A. Report errors that occur on the IP layer.  
B. Test network functions.  
C. Modify routes.  
D. More than one of the above  
E. All of the above

### 42)
How many class B IP network addresses can potentially exist?

A. ±16 000  
B. ±64 000  
C. ±1 000 000  
D. ±4000  
E. ±8000

### 43)
Hop count refers to:

A. The number of times a packet has been bounced between a client and a server.  
B. A routing metric.  
C. The number of frames that have been dropped.  
D. The number of times a packet has been bounced between two routers.  
E. The number of times an RFC has been revised.

### 44)
IEEE 802.3 defines:

A. Ethernet  
B. LLC  
C. HDLC  
D. Token ring  
E. More than one of the above

### 45)
Which of the following is/are not a function of ISO/OSI's layer 2?

A. Contention control  
B. Data delineation  
C. Dialogue control  
D. Error control  
E. More than one of the above

### 46)
Advantages of a LEO satellite for data communications include the following:

A. Since it is placed closer to earth than geosynchronous satellites, a smaller transmitter can be used from earth.  
B. It orbits around the earth.  
C. It is not affected as much as geosynchronous satellites by mountains and other natural obstacles.  
D. More than one of the above  
E. All of the above

### 47)
SAT3 is a:

A. GEO satellite  
B. LEO satellite  
C. Performance measure  
D. Undersea cable  
E. Time zone in South Africa

### 48)
Which historical event had a profound impact on many design decisions for the Internet, or ARPAnet then?

A. Cold War  
B. Suez Canal Crisis  
C. Rise of the Global South  
D. Bay of Pigs Invasion  
E. Lockerbie Bombing

### 49)
A proprietary network protocol is a protocol that:

A. Has been standardised by some national standards body.  
B. Is owned by a specific vendor.  
C. Is developed as an open source protocol.  
D. Is now so old that using it has been deprecated.  
E. Describes the properties of other network protocols.

### 50)
Which South African Act specifically regulates “wiretapping”?

A. POPIA  
B. RICA  
C. PAIA  
D. The Constitution  
E. The Bill of Rights

---

## Question 2

All values in this question are expressed in hexadecimal notation.

Convert the following Unicode characters to UTF-8 byte sequences. Represent byte sequences as 2-digit hexadecimal numbers with a space between all bytes. Your answers will therefore be similar to a string such as `12 bf 3a`.

### a)
`U+1842`  
**[1]**

### b)
`U+10AD0`  
**[1]**

### c)
`U+2CA0`  
**[1]**

UTF-8 encoding is self-synchronising. Consider the following byte sequence, which is not a valid UTF-8 encoding:

```text
9D CE B5 C4 85 F1 9C A0
```

### d)
Provide the first valid Unicode character that occurs in this sequence. Provide an answer in the form `U+xxxx`.  
**[1]**

### e)
Provide the second valid Unicode character that occurs in this sequence. Provide an answer in the form `U+xxxx`.  
**[1]**

### f)
Provide the subsequence of bytes that are invalid.  
**[1]**

### g)
Convert the bytes starting at the point where synchronisation is re-established, convert those that form the first Unicode character, and provide that character in the typical format `U+xxxx` on your answer sheet.  
**[1]**

### h)
Provide the last valid Unicode character that occurs in this sequence. Provide an answer in the form `U+xxxx`.  
**[1]**

Some emojis are represented by a combination of Unicode characters. One set of these combinations join so-called Regional Indicator Symbols. The first is Regional Indicator Symbol Letter A at `U+1F1E6` and it continues up to Regional Indicator Symbol Letter Z at `U+1F1FF`. When these Regional Indicator Symbols are rendered in isolation, they are typically rendered as black squares. However, when a pair is used, the flag of the country represented by that standard two-letter country code will be rendered, on platforms that support this functionality, such as iPhones, X and WhatsApp.

### i)
Provide the UTF-8 byte stream that will render the South African flag as an emoji.  
**[2]**

**[10]**

---

## Question 3

Currently the IPv4 block of addresses `41.1.16.0` — `41.1.31.255` is assigned to Vodacom for use in their Wimax services. Assume that Vodacom no longer offers Wimax services and that AfriNIC is therefore keen to assign these addresses to other ISPs. However, given the scarcity of IPv4 addresses, AfriNIC wants to subnet this block into at least 20 subnets that each would be able to accommodate at least 100 hosts.

### a)
What is the network address of the block `41.1.16.0` — `41.1.31.255`? Provide your answer in CIDR notation.  
**[2]**

### b)
What is the network address of the first subnet that will be created within this block? Provide your answer in CIDR notation.  
**[2]**

### c)
Note that subnetting may result in more than 20 subnets. What is the network address of the 20th subnet that will be created in this block? This address will have the value 19 in the subnet portion of its address. Provide your answer in CIDR notation.  
**[2]**

### d)
AfriNIC realises that such subnetting does indeed result in more than ten subnets. They decide to supernet the last four of these subnets into a supernet for use by Vodacom. What is the network address of this supernet? Provide your answer in CIDR notation.  
**[2]**

### e)
Provide the broadcast address of the supernet created in the previous question.  
**[1]**

### f)
What was the broadcast address of the original block `41.1.16.0` — `41.1.31.255`?  
**[1]**

**[10]**

---

## Question 4

Consider the following trace obtained from Wireshark. The first host is the sender, while the second in each line is the recipient. Hence, as an example, line 1 represents a segment transmitted from the Client to the Server.

```text
1)  Client  Server  [SYN]       Seq=0   Ack=0   Win=64240   Len=0
2)  Server  Client  [SYN, ACK]  Seq=0   Ack=1   Win=64240   Len=0
3)  Client  Server  [ACK]       Seq=1   Ack=1   Win=263168  Len=0
4)  Client  Server  [ACK]       Seq=1   Ack=1   Win=263168  Len=365
5)  Server  Client  [ACK]       Seq=1   Ack=366 Win=64128   Len=0
6)  Server  Client  [ACK]       Seq=1   Ack=366 Win=64128   Len=568
7)  Server  Client  [FIN, ACK]  Seq=569 Ack=366 Win=64128   Len=0
8)  Client  Server  [ACK]       Seq=366 Ack=570 Win=262400  Len=0
9)  Client  Server  [FIN, ACK]  Seq=366 Ack=570 Win=262400  Len=0
10) Client  Server  [FIN, ACK]  Seq=366 Ack=570 Win=262400  Len=0
11) Server  Client  [ACK]       Seq=570 Ack=367 Win=64128   Len=0
```

Wireshark was configured to show layer 4 packets by default. All the packets shown are TCP packets. Only two IP addresses were associated with the captured packets; those addresses have been replaced by the words Client and Server in the trace above. The port number associated with the client was a high-order port, while the port associated with the server was 80. For the sake of readability, the port numbers are not shown in the trace. Following the Wireshark convention, TCP flags that are set in a segment are shown in uppercase in square brackets; flags that are not shown are reset in the segment. Other relevant header and calculated fields complete the trace summary. For ease of reference, lines have been numbered in a style that differs from the style used by Wireshark.

Answer the questions that follow based on the trace provided.

### a)
Which line completes the opening handshake? Simply provide a number from 1 to 3.  
**[1]**

### b)
Line 2 implies that line 1 contained a data byte. State the observation from line 2 from which this can be derived.  
**[1]**

### c)
In contrast to the previous question, line 1 stipulates that `Len=0`; therefore line 1 does not seem to carry a data byte at all. What type of byte is “included” in the packet from line 1?  
**[1]**

### d)
Does line 3 “include” a similar byte to that mentioned in the previous question? Why not?  
**[1]**

### e)
The packet from line 4 carries 365 data bytes to the server. How many bytes has the server apparently consumed at the time it first acknowledges the packet from line 4?  
**[1]**

### f)
The server then, in line 6, sends a response consisting of 568 bytes to the client. In which line does the client first acknowledge this data from the server?  
**[1]**

### g)
Note that the server transmits a packet with `Seq=569` in line 7; in fact `Seq=569` is what one would expect at this time. However, in line 11 it transmits a packet with `Seq=570`. Which packet caused the sequence number to be increased? Simply provide a number from 1 to 11.  
**[1]**

### h)
How many of the 568 bytes that the server transmitted in line 6 have been consumed by the client at the time the client transmits its final message in this trace, line 10? Very briefly explain.  
**[1]**

### i)
The packet in line 7 obviously plays a role in the termination handshake, but seems unexpected at this time given the theory discussed in the module. Is it part 1, 2, or 3 of the handshake? Very briefly justify your answer.  
**[1]**

### j)
Why was it necessary to transmit the packet in line 10?  
**[1]**

**[10]**

---

## Question 5

Assume the following:

- `za1.dnsnode.net` is able to resolve names in the `za.` zone.
- `coza1.dnsnode.net` is able to resolve names in the `co.za` zone.
- `ns1.host-h-net` is able to resolve names in the `xx.co.za` zone; it is the primary name server for `xx.co.za`.
- `ns2.host-h-net` is able to resolve names in the `xx.co.za` zone; it is the secondary name server for `xx.co.za`.
- The IPv4 address of `xx.co.za` is `41.203.18.59`.
- The IPv4 address of `ftp.xx.co.za` is `197.221.2.30`.
- The IPv6 address of `xx.co.za` is `2606:4700:20::ec5`.
- The servers accepting email at `xx.co.za` are `ASPMX.L.GOOGLE.COM` and `ALT1.ASPMX.L.GOOGLE.COM`, where the latter should be used when the former is not available.

Assume that all the name servers used in this question are primary name servers.

In some questions below the zone is specified, typically `xx.co.za`. In other cases you have to infer the zone from the context; the root name servers, for example, provide information about the root zone. Recall that a zone file defines entries relative to the zone for which the zone file exists. The zone file for `com.` will have an entry that points to, say, the `ibm.com` domains; that entry will simply define `ibm` in that zone file, since the `com.` all definitions in that zone file will be followed by a `.com`.

Use names as the definitions of your resource records; you, for example, do not know what the IPv4 address of, say, `za1.dnsnode.net` is.

Use this information to provide the following zone records. Your zone records will, in general, consist of three columns: the entry being defined, the resource record type and the definition, with additional information only in cases where the resource record requires additional information.

### a)
Provide the resource record for the zone file at `a.root-servers.net` that may be useful to recursively resolve `ftp.xx.co.za`.  
**[1]**

### b)
Provide the resource record for the zone file at `za1.dnsnode.net` that may be useful to recursively resolve `ftp.xx.co.za`.  
**[1]**

### c)
Provide the resource record for the zone file at `coza1.dnsnode.net` that may be useful to recursively resolve `ftp.xx.co.za`.  
**[1]**

### d)
Provide the resource record for the zone file at `ns1.host-h-net` to indicate that it is the primary name server for `xx.co.za`.  
**[1]**

### e)
Provide the resource record for the zone file of `xx.co.za` that may be useful to recursively resolve `ftp.xx.co.za`.  
**[1]**

### f)
Provide the resource record for the zone file of `xx.co.za` that may be useful to recursively resolve `xx.co.za` to an IPv4 address.  
**[1]**

### g)
Provide the resource record for the zone file of `xx.co.za` that may be useful to recursively resolve `ftp.xx.co.za` to an IPv6 address.  
**[1]**

### h)
Provide the resource record for the zone file of `xx.co.za` that may be useful to recursively resolve the details of the primary email server for `xx.co.za`.  
**[1]**

### i)
Provide the resource record for the zone file of `xx.co.za` that may be useful to recursively resolve the details of the secondary mail server for `xx.co.za`.  
**[1]**

### j)
Provide a resource record for the zone file of `xx.co.za` that will add an entry of the form `x=1` to the zone.  
**[1]**

**[10]**

---

> Note: The supplied PDF contains scanned pages up to the displayed continuation marker after Question 5. No additional page was available in the uploaded file.

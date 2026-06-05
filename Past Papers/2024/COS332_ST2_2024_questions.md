# COS332 Semester Test 2 — 20 May 2024

**Course:** Computer Science  
**Paper:** COS332  
**Time:** 90 minutes  
**Marks:** 50

## Question 1

In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### a)
Which protocol will a diskless computer typically use to transfer an operating system image from a server to the computer, when the computer boots?

A. DHCP  
B. FTP  
C. TFTP  
D. HTTP  
E. BOOTP

### b)
Which of the following are examples of network management protocols?

A. SNMP  
B. CMIP  
C. CMOT  
D. More than one of the above  
E. All of the above

### c)
Which of the following statements about X.509 is/are true?

A. It is part of the X.500 series of standards introduced by CCITT.  
B. It is used for public key cryptography.  
C. It is used in the TCP/IP context.  
D. More than one of the above  
E. All of the above

### d)
Item which of the following protocols is an / are examples of an external gateway protocol (EGP)?

A. BGP  
B. OSPF  
C. RIP  
D. More than one of the above  
E. All of the above

### e)
In which of the following algorithms is counting to infinity a cause for concern?

A. Dijkstra  
B. Bellman-Ford  
C. RIP  
D. More than one of the above  
E. All of the above

### f)
Consider a scenario in RIP where a router `r` sends its routing table to a router `s`. An entry in `r`'s table indicates that it can reach a network `n` at a cost of 5. Before receiving the message, the routing table at `s` indicated that it could reach `n` at a cost of 8. What will the cost from `s` to `n` be according to the routing table at `s` after `s` processed the message from `r`?

A. 5  
B. 6  
C. 7  
D. 8  
E. More information about `r` is required to answer the question.

### g)
Suppose computers A and B both use extended ASCII to represent characters. There is no character conversion mechanism between A and B. Assume that every byte transmitted will be received correctly; no data loss or transmission errors will occur. What challenge(s) may be experienced when these two computers communicate?

A. When A sends a digit or one of the 26 Latin characters, in either lower or uppercase, the recipient may interpret at least one of these 62 characters incorrectly.  
B. A may mark up a character, for example `&euml;`, and such characters may be received incorrectly at the destination.  
C. It is possible that at least one of the following seven punctuation marks may not be communicated correctly: `? ! ' , . " ; :`  
D. These computers will not experience any challenges since they use the same character encoding.  
E. None of the problems listed above will occur, but other challenges may exist.

### h)
How many Unicode characters can, in principle, be represented in UTF-8 using exactly four bytes? If the answer is expressed in the form `2^n`, what is the value of `n`?

A. 14  
B. 20  
C. 21  
D. 22  
E. 27

### i)
Suppose an email consists of a message encoded in HTML and a JPG image, both included in the message. These two items are the only components of the email message. Which MIME type will be used to describe the entire email message?

A. application/email  
B. application/rfc822  
C. multipart/alternative  
D. multipart/mixed  
E. text/html

### j)
Which Content-Transfer-Encoding would be most appropriate to transfer a PNG image via SMTP?

A. 8bit  
B. binary  
C. quoted-printable  
D. base64  
E. 7bit

### k)
On which ISO OSI layer should encryption be placed, if encryption is desired?

A. 7  
B. 6  
C. 4  
D. 3  
E. It depends on factors not mentioned in the question. All of the layers mentioned above are options.

### l)
Which ISO OSI layer may provide checkpoints, such that only messages sent since the last checkpoint have to be retransmitted after a connection has been lost?

A. 2  
B. 3  
C. 4  
D. 5  
E. 6

### m)
How are the SYN and ACK packets sent during a TCP handshake differentiated from one another?

A. The flags are used to determine the type of handshake packet.  
B. These packets carry a phantom byte in which the type, SYN or ACK, is encoded.  
C. The sequence and acknowledgement numbers determine the type of packet; a sequence number of 0, for example, indicates that it is a SYN packet and a sequence number of 0 and an acknowledgement number of 1 indicate that it is a SYN+ACK packet.  
D. More than one of the above  
E. All of the above

### n)
How does the server differentiate between the ACK packet that it receives as the last part of the handshake to establish a connection, and an ACK packet that acknowledges data that has been received?

A. The handshake ACK packet will always be received before the first data acknowledgement packet.  
B. The ACK flag is only set for the handshake packet; the acknowledgement field is used to acknowledge data.  
C. For a handshake packet, the SYN or FIN flag will be set; for packets that acknowledge data neither will be set.  
D. The acknowledgement packet that acknowledges the server's SYN+ACK packet is always part of the handshake; packets that acknowledge other data are not.  
E. None of the above

### o)
What is the minimum number of timer types required by any sliding window ARQ protocol?

A. 1  
B. 2  
C. 3  
D. 4  
E. 5

### p)
The TCP quiet timer determines when a port may be used for a new TCP connection after a previous connection has been closed. Which of the following claims is/are true?

A. The port, or socket, is in the TIME-WAIT state while the quiet timer is active.  
B. The quiet timer is activated when the FIN+ACK message is sent.  
C. The quiet timer solves the problem of a packet from a previous connection being deemed part of a new connection.  
D. More than one of the above  
E. All of the above

### q)
Which command enables one to see the status of transport layer connections on a host, in most operating systems?

A. netstat  
B. ping  
C. tracert / traceroute  
D. tcp-show  
E. ps

### r)
What type of port is port 55555?

A. Registered  
B. Well-known  
C. Dynamic  
D. Practical  
E. Temporary

### s)
What does the claim that QUIC is a quick protocol mean?

A. It manages the lower layers to transmit raw data at higher bit rates.  
B. It reduces latency when establishing or re-establishing a connection.  
C. Where multiple parts of a message have to be transported, it ensures that parts of the message are delivered quickly even if some parts are delayed.  
D. More than one of the above  
E. All of the above

### t)
Which of the following actions always happen(s) when a client establishes a QUIC connection with a server?

A. The client chooses a connection ID to be used by the server.  
B. The client includes initial data encrypted with the server's public key.  
C. The client informs the server which cryptographic suite will be used.  
D. The client sends an initial packet numbered 0 on the wire.  
E. None of the above

### u)
QUIC connections can migrate. Which party can initiate such a migration in QUICv1 or QUICv2?

A. The client  
B. The server  
C. The network management system  
D. More than one of the above  
E. All of the above

### v)
Which of the following headers are always present in a long QUIC header? Include cases where the length of the field will be present and may be 0, meaning that the field itself may be omitted.

A. Version  
B. Source connection ID  
C. Destination connection ID  
D. More than one of the above  
E. All of the above

### w)
Assume a client establishes a new QUIC connection at time `t0` with a server. The server receives the initial packet at time `t1` and immediately sends its response(s), which arrive(s) at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server transmitting at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which application data may sometimes be sent?

A. `t0`  
B. `t1`  
C. `t2`  
D. `t3`  
E. It is impossible to say.

### x)
Assume a client establishes a new QUIC connection at time `t0` with a server. The server receives the initial packet at time `t1` and immediately sends its response(s), which arrive(s) at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server transmitting at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which 1-RTT application data may sometimes be sent?

A. `t0`  
B. `t1`  
C. `t2`  
D. `t3`  
E. None of the above

### y)
Assume a client establishes a new QUIC connection at time `t0` with a server. The server receives the initial packet at time `t1` and immediately sends its response(s), which arrive(s) at time `t2`. This process continues with the client transmitting at even times (`t0`, `t2`, `t4`, ...) and the server transmitting at odd times (`t1`, `t3`, `t5`, ...). What is the soonest time at which the connection may be deemed to be fully established?

A. `t0`  
B. `t1`  
C. `t2`  
D. `t3`  
E. None of the above

**[25]**

---

## Question 2

You receive a sequence of bytes that are supposed to be UTF-8 encoded. However, some bytes have been lost during transmission. You are expected to recover all the characters that can be extracted. Where a sequence of one or more bytes does not constitute a character, you have to indicate it using an `X`. Use the form `U+xxxx` to represent the Unicode characters. Suppose you find five subsequences in the sequence where subsequence 1, 2 and 4 are valid Unicode characters, but subsequence 3 and 5 are not, then your answer may look as follows: `1) U+0001 2) U+0002 3) X 4) U+0009 5) X`. Note that more spaces may have been provided on the answer sheet than actual subsequences of characters.

The byte sequence to process is the following:

```text
41 D7 90 EF BA 5E
91 D0 90 D0 F0 9F
98 80 F0 90 A4 80
F0 90 8E A0 5A 87
```

**[5]**

---

## Question 3

Node A is busy communicating with node B via a TCP connection. At some time `t` the next byte that A will send is byte number 300. The next byte that B will send is byte number 500. The window size at A is 1000. The window size at B is 100. At time `t`, both A and B have successfully received all previous messages sent by its counterpart.

At time `t + 1` A wants to send 300 bytes to node B. Call the message that A actually sends `m2`.

At time `t + 2` B consumes 200 bytes from its buffer.

At time `t + 3` B sends a message containing 50 bytes to A. Let us call this message `m3`.

At time `t + 4` A sends a message to B to acknowledge receipt of `m3`. A also includes all residual data it may have to send. Let us call this message `m4`.

At time `t + 5` B sends an empty acknowledgement message to A to acknowledge `m4`. Let us call this acknowledgement message `m5`.

### a)
What is the sequence number included with `m2`?

### b)
What is the acknowledgement number included with `m4`?

### c)
What is the length of `m4`?

### d)
What is the window advertisement included with `m4`?

### e)
What is the window advertisement included with `m5`?

**[5]**

---

## Question 4

Briefly define or describe the following terms:

### a)
TCP slow start

### b)
TCP acknowledgement timer

### c)
Round trip time

### d)
Middlebox, especially in the context of layer 4

### e)
Protocol ossification

**[5]**

---

## Question 5

Assume that the costs between nodes of a network are as follows:

```text
A-E: 2    D-E: 5
B-E: 1    D-F: 1
B-G: 1    E-F: 10
C-F: 5
```

Use Dijkstra's algorithm to determine the routes from A.

Use the notation used in this module to show your calculations, in the table provided on the answer sheet.

**[10]**

---

**TOTAL: [50]**

**END OF PAPER**

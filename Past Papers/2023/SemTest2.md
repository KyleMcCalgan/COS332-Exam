# University of Pretoria
## COS 332 — Computer Science
### Semester Test: 15 May 2023

**Time:** 90 minutes  
**Marks:** 50  
**Examiner:** Prof MS Olivier  
**This paper consists of 10 pages.**

---

**Instructions:**
- Answer all questions.
- Casio FX-82 (or equivalent) calculators permitted, as well as basic 5-function calculators.
- Use your test book for rough work; note that it will not be marked, but should be handed in.
- You are allowed to write on this test paper.

---

## Question 1

*In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.*

**a)** The following is an example of an IGP:

- A: BGP
- B: OSPF
- C: Dijkstra
- D: More than one of the above
- E: All of the above

---

**b)** The ASCII standard standardises a(n) … character code.

- A: 7-bit
- B: 8-bit
- C: 9-bit
- D: More than one of the above
- E: All of the above

---

**c)** Consider the following protocol negotiation string in an HTTP request:
```
Accept-Charset: iso-8859-1, utf-8, utf-16, *;q=0.1
```
Suppose the server supports `iso-8859-1`, `utf-8` and `Shift_JIS`. The response may then be encoded using

- A: iso-8859-1
- B: utf-8
- C: Shift_JIS
- D: Any of the encodings listed as options above.
- E: One or two of the encodings listed as options above.

---

**d)** A BER value in ASN.1 is, in principle, encoded as a triple consisting of

- A: A type, a subtype and a value.
- B: A type, a length and a value.
- C: A constructor and two operands.
- D: A variable name, as well as its minimum and maximum values.
- E: The same value encoded in binary, text and hexadecimal.

---

**e)** Routers using OSPF broadcast their … and use the received information to apply the … algorithm.

- A: Routing tables; Dijkstra
- B: Routing tables; Bellman-Ford
- C: Routing tables; RIP
- D: Version of the network topology; Dijkstra
- E: Version of the network topology; Bellman-Ford

---

**f)** Which of the following is *not* a valid MIME type?

- A: binary
- B: example
- C: image
- D: message
- E: model

---

**g)** Morse code uses a version of a Huffman encoding where moving along the left branch in the (balanced) tree that is constructed, is deemed to be represented by a dot, while moving to the right is deemed to be represented by a dash. The letter N is deemed to be the fifth most common character by Morse code. Hence N is represented as follows:

- A: ••
- B: •–
- C: –•
- D: ––
- E: ••–

---

**h)** The session layer is layer … of the ISO OSI protocol stack.

- A: 1
- B: 2
- C: 3
- D: 4
- E: 5

---

**i)** The transport layer protocol that is predicted to eventually replace TCP is

- A: TP0
- B: IP
- C: TCPv2
- D: QUIC
- E: ARPA

---

**j)** UDP uses the following flow-control mechanism:

- A: Stop and Wait
- B: Sliding window
- C: Unrestricted
- D: More than one of the above
- E: All of the above

---

**k)** Say a damaged packet arrives at its destination. The recipient may, for example, determine that the packet is damaged when the checksum does not match. In many protocols it may then send a NAK (negative acknowledgement) to the original sender to request retransmission. Suppose A sends a TCP segment to B, but it arrives damaged at B. How is this resolved?

- A: B sets the NAK TCP flag and sends it as a response to A.
- B: B discards the segment and does not acknowledge it; the retransmission timer at A expires and the packet is sent again.
- C: B requests the network layer at B to deal with the error, and this triggers a retransmission of the segment.
- D: B corrects the damaged segment and (eventually) acknowledges receipt.
- E: The lower layer protocols perform error checking, so a damaged segment will never arrive; errors will always be corrected on a lower layer.

---

**l)** A sends a TCP segment to node B. The acknowledgement field contains the value 150. The ACK flag is not set. This means

- A: B may assume that bytes up to byte 149 that it had sent are acknowledged.
- B: B should disregard the value 150 — it has no meaning.
- C: This is a negative acknowledgement of the segment B has sent that had the sequence number 150.
- D: The TCP layer at A is misconfigured; it should have set the ACK flag.
- E: More than one of the above

---

**m)** Node A sends a TCP segment to node B with its ACK flag set. This may affect (or create) relevant timers at A and/or B.

What happens to one or more of the retransmission timers at A?

- A: A timer is created.
- B: An existing timer is set.
- C: An existing timer is reset.
- D: An existing timer is deleted.
- E: No retransmission timer is affected.

---

**n)** Node A sends a TCP segment to node B with its ACK flag set. This may affect (or create) relevant timers at A and/or B. B receives this segment without any error.

What happens to one or more of the acknowledgement timers at B?

- A: A timer is created.
- B: An existing timer may be set.
- C: An existing timer may be reset.
- D: An existing timer may be deleted.
- E: No acknowledgement timer will be affected.

---

**o)** Node A sends a TCP segment to node B with its ACK flag set. This may affect (or create) relevant timers at A and/or B.

What happens to one or more of the acknowledgement timers at A?

- A: A timer is created.
- B: An existing timer may be set.
- C: An existing timer may be reset.
- D: An existing timer is deleted.
- E: No acknowledgement timer will be affected.

---

**p)** Suppose node A is connected to node B via TCP. When the persistence timer at A expires it implies that

- A: B has not yet acknowledged the last segment A sent to B.
- B: A is waiting for space to free up in B's window before further data can be sent.
- C: A has no data to send, so it transmits a single byte to indicate that it is still present.
- D: More than one of the above
- E: All of the above

---

**q)** A TCP connection in the `TIME-WAIT` state means that

- A: The node is waiting for data from the node that it is connected to.
- B: The connection is about to time-out if no further data is transmitted soon.
- C: The connection will soon be established (as soon as the handshake is completed).
- D: The node is waiting for 'lost' traffic to arrive at the port that is no longer in use, before it will be available for reuse.
- E: The network is congested.

---

**r)** You see the following line as part of the `netstat` program's output on Linux:
```
127.0.0.1:27117 127.0.0.1:48956 ESTABLISHED keepalive
```
This means that this connection

- A: Is in use, but idle.
- B: Is being torn down, and will soon be closed.
- C: Is busy carrying data.
- D: Has been reserved for future use.
- E: Is busy with a handshake.

---

**s)** A TCP node that is in the `LISTEN` state

- A: Is acting as a server and waiting for a SYN message.
- B: Is acting as a client and has sent a SYN message.
- C: May act as a client after sending a SYN message.
- D: More than one of the above
- E: None of the above.

---

**t)** Which well-known port is used for control messages by an FTP server?

- A: 20
- B: 21
- C: 22
- D: 23
- E: 24

**[20]**

---

## Question 2

*Consider the following IP addressing scenario.*

Your organisation uses the following IP address as part of the block assigned to them: **170.170.170/16**.

They decide to subnet their address space such that they have at least 1000 subnets that can each handle at least 60 hosts.

**a)** What netmask will they use for the subnets? **(1)**

**b)** Consider *subnet* number 170. What is the network address of this subnet? Express it using CIDR notation. **(2)**

**c)** What is the broadcast address of subnet 170? **(1)**

**d)** What is the last (or 'biggest') address that may be assigned to a host on subnet 170? **(1)**

**e)** On which subnet will the host with the IP address 170.170.170 be? Just provide the number of the subnet. **(1)**

The organisation decides that it needs a bigger subnet in the laboratory where 170.170.170.170 is located. They decide to combine a number of subnets into a supernet that can handle at least 1000 hosts. However, they want to sacrifice as few subnets as possible to create this supernet.

**f)** Provide the netmask associated with this supernet. **(1)**

**g)** Provide the network address of this supernet using CIDR notation. **(1)**

**h)** What is the *number* of the first subnet that will be lost once this supernet has been created? **(1)**

**[10]**

---

## Question 3

**a)** Consider the following UTF-8 byte sequence:
```
E1 A1 80 41 EF A4 9A
```
Convert this sequence to Unicode codepoints in the form U+xxxx.

*Note that the answer sheet contains more open blocks than what you need. Just place a dash in blocks that are not necessary.* **(5)**

**b)** Consider the following Unicode codepoints:
```
U+00C6  U+10000
```
Convert this sequence to a UTF-8 byte sequence where each byte is represented in hexadecimal.

*Note that the answer sheet contains more open blocks than what you need. Just place a dash in blocks that are not necessary.* **(5)**

**[5]** *(combined mark)*

---

## Question 4

The TCP header includes a flags field that consists of various flags. Name any five (5) *other* fields that occur in the TCP header. **(5)**

---

## Question 5

Node A is busy communicating with node B via a TCP connection. At some time *t* the next byte that A will send is byte number 300. The next byte that B will send is byte number 500. The window size at A is 1000. The window size at B is 100. At time *t*, both A and B have successfully received all previous messages sent by its counterpart.

At time *t* + 1 A wants to send 200 bytes to node B. Call the message that A actually sends *m*₁.

At time *t* + 2 B consumes 100 bytes from its buffer.

At time *t* + 3 B sends a message containing 50 bytes to A. Let us call this message *m*₃.

At time *t* + 4 A sends a message to B to acknowledge receipt of *m*₃. A also includes all residual data it may have to send. Let us call this message *m*₄.

At time *t* + 5 B sends an empty acknowledgement message to A to acknowledge *m*₄. Let us call this acknowledgement message *m*₅.

**a)** What is the sequence number included with *m*₁? **(1)**

**b)** What is the acknowledgement number included with *m*₁? **(1)**

**c)** What is the length of *m*₄? **(1)**

**d)** What is the window advertisement included with *m*₄? **(1)**

**e)** What is the window advertisement included with *m*₅? **(1)**

**[5]**

---

**TOTAL: [50]**

---

---

# MEMO — Paper 2 (15 May 2023)

## Question 1 — Answers

| # | Answer |
|---|--------|
| a | B — OSPF |
| b | A — 7-bit |
| c | C — Shift_JIS *(server supports it; the wildcard `*;q=0.1` covers it with lowest priority, but it is still acceptable)* |
| d | B — A type, a length and a value |
| e | A — Routing tables; Dijkstra |
| f | A — binary *(not a registered MIME top-level type)* |
| g | C — –• |
| h | E — 5 |
| i | D — QUIC |
| j | C — Unrestricted |
| k | B — B discards the segment and does not acknowledge it; the retransmission timer at A expires and the packet is sent again |
| l | B — B should disregard the value 150 — it has no meaning |
| m | A — A timer is created *(new retransmission timer for the sent data)* |
| n | C — An existing timer may be reset |
| o | E — No acknowledgement timer will be affected |
| p | C — A has no data to send, so it transmits a single byte to indicate that it is still present |
| q | D — The node is waiting for 'lost' traffic to arrive at the port that is no longer in use, before it will be available for reuse |
| r | A — Is in use, but idle |
| s | A — Is acting as a server and waiting for a SYN message |
| t | B — 21 |

---

## Question 2 — Memo

**Setup:** Block is 170.170.0.0/16 (65 536 addresses).  
Need ≥ 1000 subnets AND ≥ 60 hosts per subnet.

- Hosts need: ≥ 6 host bits (2⁶ – 2 = 62 ✓)
- Subnets need: ≥ 10 subnet bits (2¹⁰ = 1024 ✓)
- Total bits used: 16 (network) + 10 (subnet) + 6 (host) = 32 ✓

**a)** Netmask: **255.255.252.0** (i.e. /26 within the block → full mask /26: 255.255.192.0... recalculate)

> Correct working: /16 + 10 subnet bits = /26. Netmask = **255.255.255.192** (/26).  
> Hosts per subnet: 2⁶ – 2 = 62 ✓ | Subnets: 2¹⁰ = 1024 ✓

**a)** **255.255.255.192**

**b)** Subnet 170 network address:  
Subnet bits represent 170 in binary spread across the borrowed bits.  
With /26: each subnet = 64 addresses.  
Subnet 170: 170 × 64 = 10 880 = 0x2A80  
170.170.42.128/26 → **170.170.42.128/26**

**c)** Broadcast of subnet 170: **170.170.42.191**

**d)** Last (biggest) assignable host: **170.170.42.190**

**e)** Host 170.170.170.170: floor(170 × 256 + 170) / 64 within the last two octets:  
(170 × 256 + 170) = 43 690 → 43 690 / 64 = 682.65 → subnet **682**

**f)** Supernet needs ≥ 1000 hosts → need ≥ 10 host bits → /22.  
Sacrifice fewest subnets: combine 4 × /26 subnets into 1 × /24... need 10 host bits → **/22** mask.  
Netmask: **255.255.252.0**

**g)** Supernet containing subnet 682 aligned to /22:  
682 / 4 = 170 (group of 4 /24-equivalent blocks) → network **170.170.168.0/22**

**h)** First subnet lost: subnet **680** (first of the four /26 groups merged)

---

## Question 3 — Memo

**a)** UTF-8 → Unicode codepoints for `E1 A1 80 41 EF A4 9A`:

| Bytes | Codepoint |
|-------|-----------|
| E1 A1 80 | U+1840 |
| 41 | U+0041 |
| EF A4 9A | U+F91A |

**b)** Unicode → UTF-8 for `U+00C6  U+10000`:

| Codepoint | UTF-8 bytes |
|-----------|-------------|
| U+00C6 | C3 86 |
| U+10000 | F0 90 80 80 |

---

## Question 4 — Memo

Any five of the following TCP header fields (other than flags):

1. Source port
2. Destination port
3. Sequence number
4. Acknowledgement number
5. Header length (data offset)
6. Window size
7. Checksum
8. Urgent pointer
9. Options

---

## Question 5 — Memo

**Setup recap:**
- At time *t*: A's next byte = 300; B's next byte = 500
- Window at A = 1000; Window at B = 100
- Both sides have fully ACKed all prior data

**a)** Sequence number in *m*₁: **300** (next byte A will send)

**b)** ACK number in *m*₁: **500** (next byte A expects from B)

**c)** At *t*+4, A sends *m*₄ acknowledging *m*₃ (50 bytes from B) plus any residual data.  
A sent 200 bytes in *m*₁ (seq 300–499). B's window was 100, so A could only send 100 bytes initially — but since B had window 100 and A window 1000, A sends min(200, 100) = 100 bytes in *m*₁.  
At *t*+2 B frees 100 bytes. At *t*+3 B sends 50 data bytes. A still has 100 bytes unsent.  
*m*₄ length: **100** bytes (remaining data A has to send)

**d)** Window advertisement in *m*₄: B's buffer had 100, consumed 100, received 50 → used = 50 → free = 50. A advertises its own receive window. A's window = 1000, A received 50 bytes → free = **950**. Window ad in *m*₄ = **950**

**e)** Window advertisement in *m*₅ (B's ACK of *m*₄): B received 100 more bytes from *m*₄, buffer was 50 used → now 150 used out of 100? — B's buffer = 100 total, 50 used after *m*₃, now receives 100 more → overflow... B's window shrinks. Advertisement = **0** (buffer full, or the residual space)  
Window in *m*₅ = **0**

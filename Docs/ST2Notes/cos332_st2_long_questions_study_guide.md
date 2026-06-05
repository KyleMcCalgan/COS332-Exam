# COS332 Semester Test 2: Longer-Question Study Guide

## Purpose of this document

This document focuses on the **four longer questions** expected after the 25 multiple-choice questions in COS332 Semester Test 2. It is based on:

- the lecturer's published scope for the test,
- the 2023, 2024, and 2025 semester test 2 papers and memorandums,
- the repeated style of longer questions in those papers,
- the fact that subnetting/supernetting is very likely to appear again.

The goal is not just to list topics. The goal is to show:

1. **which long-question topics are viable**,  
2. **what form each question could take**,  
3. **how to solve each type step by step**,  
4. **which past-paper examples match each topic**, and  
5. **what to memorise vs what to practise**.

---

# 1. Expected long-question structure

The test format is expected to be:

- **25 marks multiple choice**
- **25 marks longer questions**
- likely **4 longer questions**
- total time: **90 minutes**

Past papers show that longer questions are usually not essay-style. They are normally:

- calculation questions,
- table-completion questions,
- short-answer mechanism questions,
- protocol-behaviour questions,
- “list any five” style questions,
- encoding or structured-data questions.

The longer questions are designed so that marks can be split into small pieces. That is why topics such as subnetting, routing algorithms, TCP timers, TCP reliability, QUIC mechanisms, and ASN.1 are viable.

---

# 2. Highest-probability long-question topics

## Most likely four-question combination

My best prediction is:

| Long question | Most likely topic | Why it is likely |
|---|---|---|
| Q2 | IPv4 subnetting / CIDR / supernetting | Appears repeatedly and is easy to split into marks. |
| Q3 | TCP timers or TCP reliability | Appeared directly in 2025 and fits the current Layer 4 scope. |
| Q4 | Routing algorithm: Dijkstra or Bellman-Ford/RIP | 2024 had Dijkstra; routing algorithms are in scope. |
| Q5 | QUIC or ASN.1 | QUIC was explicitly highlighted; Layer 6 is narrowed to ASN.1. |

## Backup topics that could appear as smaller long questions

These are less likely to be full long questions, but still viable:

- IPv6 address notation and special IPv6 addresses
- ARP and local delivery
- ICMP and TTL expiry
- TCP header fields
- TCP window/acknowledgement number calculations
- Layer 5 checkpoints / rollback / long-lived sessions

---

# 3. Topic 1: IPv4 subnetting, CIDR, and supernetting

## 3.1 Why this is extremely likely

Subnetting is one of the most natural COS332 long-question topics because it can be broken into small parts:

- subnet mask,
- CIDR prefix,
- network address,
- broadcast address,
- first usable host,
- last usable host,
- number of usable hosts,
- supernet covering a range,
- longest-prefix match.

Past examples:

- **2023 ST2 Question 2**: subnetting and supernetting style question. The memo includes answers such as `255.255.255.192`, `170.170.42.128/26`, broadcast `170.170.42.191`, last usable host `170.170.42.190`, and a `/22` supernet answer.
- **2025 ST2 Question 5**: CIDR/routing-style address block answers such as `0.0.0.0/0`, `192.168.0.0/24`, `172.31.0.0/16`, `137.215.0.0/16`, and `8.255.255.255/8`.

## 3.2 Core ideas you must know

### CIDR notation

CIDR notation looks like this:

```text
192.168.1.0/24
```

The `/24` means:

- the first **24 bits** are the network part,
- the remaining **8 bits** are the host part,
- total IPv4 address size = 32 bits.

So:

```text
host bits = 32 - prefix length
```

Example:

```text
/26 means 32 - 26 = 6 host bits
```

The number of addresses is:

```text
2^(host bits)
```

The number of usable host addresses is normally:

```text
2^(host bits) - 2
```

You subtract 2 because:

- one address is the **network address**,
- one address is the **broadcast address**.

### Common CIDR masks

| CIDR | Mask | Block size in final octet | Addresses | Usable hosts |
|---|---|---:|---:|---:|
| /24 | 255.255.255.0 | 256 | 256 | 254 |
| /25 | 255.255.255.128 | 128 | 128 | 126 |
| /26 | 255.255.255.192 | 64 | 64 | 62 |
| /27 | 255.255.255.224 | 32 | 32 | 30 |
| /28 | 255.255.255.240 | 16 | 16 | 14 |
| /29 | 255.255.255.248 | 8 | 8 | 6 |
| /30 | 255.255.255.252 | 4 | 4 | 2 |
| /22 | 255.255.252.0 | block size 4 in third octet | 1024 | 1022 |
| /21 | 255.255.248.0 | block size 8 in third octet | 2048 | 2046 |
| /16 | 255.255.0.0 | block size 1 in second octet | 65536 | 65534 |
| /8 | 255.0.0.0 | block size 1 in first octet | 16777216 | 16777214 |

---

## 3.3 How to solve a subnetting question

### Example question

> Given the IP address `170.170.42.150/26`, determine:
>
> a. subnet mask  
> b. network address  
> c. broadcast address  
> d. first usable host  
> e. last usable host  
> f. number of usable hosts

### Step 1: Convert `/26` to a mask

A `/26` mask means:

```text
11111111.11111111.11111111.11000000
```

In decimal:

```text
255.255.255.192
```

So the subnet mask is:

```text
255.255.255.192
```

### Step 2: Find the block size

The final octet of the mask is `192`.

```text
block size = 256 - 192 = 64
```

So the subnet ranges in the final octet are:

```text
0-63
64-127
128-191
192-255
```

### Step 3: Locate the given host address

The IP address is:

```text
170.170.42.150
```

The final octet is `150`.

`150` falls inside:

```text
128-191
```

So the network address is:

```text
170.170.42.128/26
```

### Step 4: Find the broadcast address

The broadcast address is the final address in the subnet range.

Range:

```text
128-191
```

So broadcast is:

```text
170.170.42.191
```

### Step 5: Find first and last usable host

First usable host:

```text
network address + 1 = 170.170.42.129
```

Last usable host:

```text
broadcast address - 1 = 170.170.42.190
```

### Step 6: Find number of usable hosts

Host bits:

```text
32 - 26 = 6
```

Total addresses:

```text
2^6 = 64
```

Usable hosts:

```text
64 - 2 = 62
```

### Final answer

| Item | Answer |
|---|---|
| Subnet mask | `255.255.255.192` |
| Network address | `170.170.42.128/26` |
| Broadcast address | `170.170.42.191` |
| First usable host | `170.170.42.129` |
| Last usable host | `170.170.42.190` |
| Usable hosts | `62` |

This closely matches the 2023 ST2 subnetting answers, where the memo included `255.255.255.192`, `170.170.42.128/26`, `170.170.42.191`, and `170.170.42.190`.

---

## 3.4 Supernetting / smallest CIDR block covering a range

Supernetting is the reverse of subnetting. Instead of splitting a block into smaller networks, you combine adjacent networks into a larger block.

### Example based on past-paper style

> What is the CIDR block for the address range:
>
> `41.32.0.0` to `41.39.255.255`?

### Step 1: Identify what changes

The first octet is fixed:

```text
41
```

The second octet ranges from:

```text
32 to 39
```

Write these in binary:

```text
32 = 00100000
33 = 00100001
34 = 00100010
35 = 00100011
36 = 00100100
37 = 00100101
38 = 00100110
39 = 00100111
```

### Step 2: Find the common prefix

All numbers from 32 to 39 share the first 5 bits:

```text
00100xxx
```

So:

- first octet contributes 8 fixed bits,
- second octet contributes 5 fixed bits.

Total prefix:

```text
8 + 5 = 13
```

### Step 3: Write the CIDR block

The starting address is:

```text
41.32.0.0
```

The prefix is:

```text
/13
```

Answer:

```text
41.32.0.0/13
```

---

## 3.5 Longest-prefix match

This is a routing-table version of subnetting.

### Example

A router has this routing table:

```text
10.10.10.0/24    next hop A
10.10.0.0/16     next hop B
10.0.0.0/8       next hop C
0.0.0.0/0        next hop D
```

A packet is addressed to:

```text
10.10.1.2
```

Which route is used?

### Step-by-step

Check each match:

| Route | Does `10.10.1.2` match? | Reason |
|---|---|---|
| `10.10.10.0/24` | No | Third octet is `1`, not `10`. |
| `10.10.0.0/16` | Yes | First two octets match `10.10`. |
| `10.0.0.0/8` | Yes | First octet matches `10`. |
| `0.0.0.0/0` | Yes | Default route matches everything. |

Choose the **longest prefix** among the matching routes:

```text
/16 is longer than /8 and /0
```

Answer:

```text
10.10.0.0/16 route
```

---

## 3.6 Common subnetting traps

| Trap | Correct thinking |
|---|---|
| Confusing `/26` with 26 hosts | `/26` means 26 network bits, not 26 hosts. |
| Forgetting to subtract 2 | Usable hosts usually exclude network and broadcast addresses. |
| Choosing the first matching route | Use longest-prefix match, not first match unless explicitly ordered. |
| Treating `0.0.0.0/0` as “nothing” | It is the default route and matches all addresses. |
| Confusing broadcast with last usable host | Broadcast is the last address; last usable host is one before it. |

---

## 3.7 Practice questions

### Practice 1

Given:

```text
192.168.10.77/27
```

Find:

1. subnet mask,
2. network address,
3. broadcast address,
4. first usable host,
5. last usable host,
6. usable host count.

#### Solution

`/27` means mask:

```text
255.255.255.224
```

Block size:

```text
256 - 224 = 32
```

Ranges:

```text
0-31
32-63
64-95
96-127
...
```

`77` falls in `64-95`.

So:

| Item | Answer |
|---|---|
| Mask | `255.255.255.224` |
| Network | `192.168.10.64/27` |
| Broadcast | `192.168.10.95` |
| First usable | `192.168.10.65` |
| Last usable | `192.168.10.94` |
| Usable hosts | `2^5 - 2 = 30` |

### Practice 2

Find the smallest CIDR block covering:

```text
172.16.8.0 to 172.16.15.255
```

Third octet:

```text
8  = 00001000
15 = 00001111
```

Common prefix in the third octet:

```text
00001xxx
```

That gives 5 fixed bits in the third octet.

Prefix:

```text
8 + 8 + 5 = 21
```

Answer:

```text
172.16.8.0/21
```

---

# 4. Topic 2: Routing algorithms

Routing algorithms are very viable as long questions because they naturally produce step-by-step table answers.

The two main possibilities are:

1. **Dijkstra / OSPF**
2. **Bellman-Ford / RIP**

---

## 4.1 What to memorise

| Protocol / concept | Algorithm | What is exchanged | Main issue / feature |
|---|---|---|---|
| OSPF | Dijkstra | Link-state / topology information | Each router builds a map and computes shortest paths. |
| RIP | Bellman-Ford | Routing tables / distance vectors | Counting to infinity can occur. |
| BGP | Path-vector style | Routes between autonomous systems | External gateway protocol. |

Past-paper evidence:

- 2024 ST2 included MCQ-style questions about BGP, OSPF, RIP, and counting to infinity.
- 2024 ST2 Question 5 was a full Dijkstra table-style long question.

---

## 4.2 Dijkstra: how to solve it

Dijkstra finds shortest paths from one source node to every other node.

### General method

1. Start with the source node at cost `0`.
2. Mark the source as done/finalised.
3. Look at neighbours of done nodes.
4. Update candidate costs if a cheaper path is found.
5. Pick the unfinished node with the lowest current cost.
6. Repeat until all needed nodes are done.

### Example based on the 2024-style Dijkstra question

Suppose the network has these links:

```text
A-B: 1
B-E: 1
E-F: 2
E-D: 3
D-C: 1
B-C: 6
A-F: 10
```

Run Dijkstra from `A`.

### Step 1: Initialise

```text
A = 0
All others = infinity
```

Done set:

```text
{A}
```

From A:

```text
B = 1 via A
F = 10 via A
```

### Step 2: Pick smallest candidate

Smallest candidate is `B = 1`.

Done:

```text
{A, B}
```

From B:

```text
E = A-B-E = 1 + 1 = 2
C = A-B-C = 1 + 6 = 7
```

Current candidates:

```text
E = 2 via B
C = 7 via B
F = 10 via A
```

### Step 3: Pick smallest candidate

Pick `E = 2`.

Done:

```text
{A, B, E}
```

From E:

```text
F = A-B-E-F = 1 + 1 + 2 = 4
D = A-B-E-D = 1 + 1 + 3 = 5
```

Update F from 10 to 4.

Current candidates:

```text
F = 4 via E
D = 5 via E
C = 7 via B
```

### Step 4: Pick smallest candidate

Pick `F = 4`.

Done:

```text
{A, B, E, F}
```

No better updates.

Current candidates:

```text
D = 5 via E
C = 7 via B
```

### Step 5: Pick smallest candidate

Pick `D = 5`.

Done:

```text
{A, B, E, F, D}
```

From D:

```text
C = A-B-E-D-C = 1 + 1 + 3 + 1 = 6
```

Update C from 7 to 6.

### Step 6: Pick final node

Pick `C = 6`.

Final shortest paths:

| Destination | Cost | Previous node | Path |
|---|---:|---|---|
| A | 0 | — | A |
| B | 1 | A | A-B |
| E | 2 | B | A-B-E |
| F | 4 | E | A-B-E-F |
| D | 5 | E | A-B-E-D |
| C | 6 | D | A-B-E-D-C |

### What exam questions usually ask

They may not ask for the full table. They may ask things like:

- Which node is picked at the end of iteration 3?
- What is the cost to C before iteration 4?
- Which node is the predecessor of C before/after a given iteration?
- What is the final shortest path to C?
- What is the final routing-table next hop from A to C?

### Important distinction: predecessor vs next hop

If the final path is:

```text
A-B-E-D-C
```

Then:

- predecessor of C is `D`,
- next hop from A to C is `B`.

Do not confuse these.

---

## 4.3 Bellman-Ford / RIP routing-table updates

RIP uses a distance-vector approach. Routers exchange routing tables.

### Core rule

If router `D` receives a table from neighbour `C`, then for every destination `X` advertised by `C`:

```text
cost from D to X via C = cost from D to C + cost from C to X
```

Then D compares that cost with its current route.

### Example

Suppose:

```text
D reaches C at cost 3.
C says it reaches A at cost 7.
```

Then D can reach A via C at:

```text
3 + 7 = 10
```

If D's current route to A has cost 20, D updates:

```text
A: cost 10, next hop C
```

### Past-paper-style MCQ example

2024 ST2 included a question like:

> Router r sends its routing table to router s. An entry in r's table says it can reach network n at cost 5. Before receiving the message, s can reach r at cost 3. What will the cost from s to n be after processing the message?

Solution:

```text
cost(s to n via r) = cost(s to r) + cost(r to n)
                  = 3 + 5
                  = 8
```

Answer:

```text
8
```

### Counting to infinity

Counting to infinity is associated with:

```text
Bellman-Ford / RIP
```

It happens when routers repeatedly update one another with increasingly worse routes to a destination that has become unreachable.

The trap is that RIP may force a router to accept a worse cost if the update comes from its current next hop.

Example:

```text
D currently reaches F via E at cost 7.
E now advertises F at cost 4.
D's cost to E is 4.
```

New cost via E:

```text
4 + 4 = 8
```

Even though `8` is worse than `7`, if E is D's current next hop for F, D may update to the new cost.

This is the behaviour that can lead to counting to infinity.

---

## 4.4 Practice routing question

### Question

Router D has this table:

| Destination | Cost | Next hop |
|---|---:|---|
| A | 20 | E |
| C | 3 | C |
| E | 4 | E |
| F | 7 | E |

Router C sends D this table:

| Destination | Cost from C |
|---|---:|
| A | 7 |
| B | 1 |
| D | 3 |
| F | 2 |

What entries should D update?

### Solution

Cost from D to C:

```text
3
```

Calculate possible costs via C:

| Destination | C's cost | D to C | Total via C | D's old route | Update? |
|---|---:|---:|---:|---|---|
| A | 7 | 3 | 10 | 20 via E | Yes: A cost 10 via C |
| B | 1 | 3 | 4 | no route | Yes: B cost 4 via C |
| D | 3 | 3 | 6 | self route should be 0 | No |
| F | 2 | 3 | 5 | 7 via E | Yes if normal cheaper-route rule applies |

Updated table:

| Destination | Cost | Next hop |
|---|---:|---|
| A | 10 | C |
| B | 4 | C |
| C | 3 | C |
| E | 4 | E |
| F | 5 | C |

---

# 5. Topic 3: TCP reliability mechanisms

## 5.1 Why this is likely

2025 ST2 Question 4 asked for mechanisms TCP uses to provide reliability. The memo accepted answers such as:

- 3-way handshake to establish,
- 3-way handshake to terminate,
- ACK for ARQ,
- slow start,
- exponential back-off,
- CRC/checksum over the segment,
- window advertisements.

This is one of the most markable long questions because it can ask for “any five”.

---

## 5.2 Model answer: “List five TCP reliability mechanisms”

If the question says:

> TCP is reliable. List and briefly explain five mechanisms TCP uses to provide reliability.

A strong answer would be:

| Mechanism | Explanation |
|---|---|
| 3-way handshake to establish | Confirms that both endpoints are alive and that both directions of communication work before data transfer. |
| Sequence numbers | Allow TCP to identify missing, duplicated, or out-of-order bytes. |
| Acknowledgement numbers | Tell the sender which byte the receiver expects next, confirming what has arrived. |
| ACK-based ARQ | If data is not acknowledged, TCP retransmits it. |
| Retransmission timer | Starts when data is sent; if it expires before ACK arrives, data is retransmitted. |
| Sliding window / window advertisement | Prevents overwhelming the receiver and allows multiple bytes/segments to be in flight. |
| Checksum | Detects corrupted TCP segments. Damaged segments are discarded. |
| Slow start | Avoids injecting too much traffic too quickly into the network. |
| Exponential back-off | If repeated loss occurs, retransmissions are delayed more aggressively to reduce congestion. |
| Connection termination handshake | Helps both sides close the connection cleanly and reliably. |

For a five-mark question, do not merely list the names if it says “briefly explain”. Give one sentence per mechanism.

---

## 5.3 TCP three-way handshake

Connection setup:

```text
A -> B: SYN
B -> A: SYN + ACK
A -> B: ACK
```

Purpose:

- A checks that B is reachable.
- B checks that A is reachable.
- Both sides agree on initial sequence numbers.
- Both communication directions are confirmed.

### Phantom bytes

The SYN and SYN+ACK consume sequence numbers even though they do not contain real payload data.

Important facts:

| Statement | True or false? |
|---|---|
| SYN consumes one sequence number | True |
| SYN+ACK consumes one sequence number | True |
| Final ACK consumes a phantom byte | False |
| The phantom byte is real data | False |

Past-paper link:

- 2025 ST2 had an MCQ asking which statements about phantom bytes are false.

---

## 5.4 TCP ACK flag trap

Past-paper style:

> A sends a TCP segment to B. The acknowledgement field contains the value 150. The ACK flag is not set. What does this mean?

Correct reasoning:

```text
The acknowledgement field is only meaningful if the ACK flag is set.
```

So if the ACK flag is not set:

```text
The value 150 must be ignored.
```

Do not interpret it as acknowledging byte 149. It means nothing without the ACK flag.

---

## 5.5 TCP header fields

2023 ST2 Question 4 asked for TCP header fields. The memo accepted any five of:

- Source Port
- Destination Port
- Sequence Number
- Acknowledgement Number
- Data
- Window
- Checksum
- Urgent Pointer
- Options
- Padding

A compact answer:

```text
Source port, destination port, sequence number, acknowledgement number, flags, window advertisement, checksum, urgent pointer, options, padding.
```

Common trap:

```text
Length is not a standard TCP header field.
```

Length is more naturally associated with UDP/IP-style headers, not TCP.

---

# 6. Topic 4: TCP timers

## 6.1 Why this is likely

2025 ST2 Question 3 directly asked about TCP timers. The memo answers were:

| Timer | Memo-style answer |
|---|---|
| Retransmission | Associated data is retransmitted. |
| Acknowledgement | Associated data is acknowledged. |
| Persistence | Probe message is sent. |
| Keepalive | Probe messages are sent. |
| Quiet | Connection resources are released. |

This topic is highly likely because it is simple to mark and sits directly inside Layer 4.

---

## 6.2 Timer-by-timer explanation

### 1. Retransmission timer

Triggered when:

```text
TCP sends data and waits for an ACK.
```

If it expires:

```text
The unacknowledged data is retransmitted.
```

Why it matters:

- handles lost segments,
- handles damaged segments that were discarded,
- supports ARQ.

### 2. Acknowledgement timer

Triggered when:

```text
TCP receives data but delays the ACK briefly.
```

If it expires:

```text
An acknowledgement is sent.
```

Why delay ACKs?

- to piggyback ACKs on outgoing data,
- to reduce the number of small packets.

### 3. Persistence timer

Triggered when:

```text
The receiver advertises a window size of 0.
```

If it expires:

```text
A probe message is sent.
```

Purpose:

- checks whether the receiver's window has opened again,
- prevents deadlock where a window update is lost.

### 4. Keepalive timer

Triggered when:

```text
A connection has been idle for a long time.
```

If it expires:

```text
TCP sends probe messages to check whether the other endpoint is still alive.
```

If there is still no response:

```text
The connection may be closed and resources released.
```

### 5. Quiet timer

Triggered after:

```text
A TCP connection has been closed.
```

If it expires:

```text
The port/resources may be reused safely.
```

Purpose:

- allows old/lost duplicate packets from the previous connection to disappear,
- prevents old traffic being mistaken as part of a new connection.

---

## 6.3 Model answer for a timer question

If asked:

> Briefly state what happens when each TCP timer expires.

Write:

| Timer | What happens when it expires |
|---|---|
| Retransmission | The associated unacknowledged data is retransmitted. |
| Acknowledgement | An acknowledgement segment is sent. |
| Persistence | A window probe is sent to check whether the receiver can accept data again. |
| Keepalive | Probe messages are sent to check whether the peer is still alive; if not, resources may be released. |
| Quiet | The wait period ends and the old connection resources/port may be reused. |

---

## 6.4 Common timer traps

| Trap | Correction |
|---|---|
| Saying persistence retransmits data | It sends a probe, not normal data. |
| Saying keepalive is for congestion | It checks whether the other endpoint is alive. |
| Saying quiet timer starts during normal data transfer | It applies after closing, before reusing the port. |
| Confusing retransmission and acknowledgement timer | Retransmission sends data again; acknowledgement sends ACK. |

---

# 7. Topic 5: TCP window and acknowledgement number calculations

This is less likely than timers/reliability, but 2023 ST2 had a TCP calculation-style question. The memo answers included numeric values such as `400`, `550`, `100`, `950`, and `0`.

## 7.1 Concepts needed

### Sequence number

The sequence number identifies the first byte in a TCP segment.

Example:

```text
Segment sequence number = 500
Segment contains 100 bytes
```

Then the segment contains bytes:

```text
500 to 599
```

The next expected byte is:

```text
600
```

So the ACK number would be:

```text
600
```

### Acknowledgement number

The ACK number means:

```text
I have received everything up to ACK number - 1.
I next expect byte ACK number.
```

So:

```text
ACK = 550
```

means:

```text
Received up to byte 549; next expected byte is 550.
```

### Window advertisement

The advertised window tells the sender how many more bytes the receiver is currently willing to accept.

Simplified formula:

```text
advertised window = receive buffer size - unprocessed bytes currently in buffer
```

If the receiver buffer size is `1000`, and it currently has `600` bytes waiting to be consumed:

```text
advertised window = 1000 - 600 = 400
```

This explains why past-paper window answers often look like remaining buffer capacity numbers.

---

## 7.2 Practice calculation

### Question

A receiver has a buffer of 1000 bytes. It has already accepted bytes 1 to 400 but the application has only consumed bytes 1 to 150.

Find:

1. next expected byte,
2. unconsumed bytes in the buffer,
3. advertised window.

### Solution

The receiver has accepted bytes 1 to 400.

So the next expected byte is:

```text
401
```

The application has consumed bytes 1 to 150, so unconsumed bytes are:

```text
151 to 400
```

Count:

```text
400 - 150 = 250 bytes
```

Advertised window:

```text
1000 - 250 = 750
```

Final answers:

| Item | Answer |
|---|---:|
| Next expected byte | 401 |
| Unconsumed bytes | 250 |
| Advertised window | 750 |

---

# 8. Topic 6: QUIC

## 8.1 Why QUIC is likely

The lecturer specifically highlighted QUIC in the scope announcement, and the 2025 paper already had MCQs about QUIC:

- What does the claim that QUIC is “quick” mean?
- Which party can initiate connection migration in QUICv1/v2?

A longer question could easily ask:

> Explain the mechanisms QUIC uses to reduce delay compared with TCP.

or:

> Compare TCP and QUIC with respect to connection establishment, multiplexing, and migration.

---

## 8.2 Core QUIC facts

QUIC is a modern transport protocol built on top of UDP.

Important points:

- QUIC runs over **UDP**.
- QUIC provides many transport features normally associated with TCP.
- QUIC integrates encryption/TLS more tightly into the transport setup.
- QUIC can reduce connection setup latency.
- QUIC supports multiple streams in one connection.
- QUIC allows connection migration when the client changes IP address.

---

## 8.3 Why QUIC is “quick”

QUIC is not “quick” because it magically increases the physical bit rate of the network.

It is quick mainly because it reduces waiting time and avoids some TCP limitations.

### Mechanism 1: Faster connection establishment

Traditional TCP plus TLS can require multiple round trips before useful encrypted application data can be sent.

QUIC reduces this by combining transport and cryptographic setup.

Key terms:

| Term | Meaning |
|---|---|
| 1-RTT | Data can be sent after one round-trip setup. |
| 0-RTT | In some repeat-connection cases, data can be sent immediately using prior information. |

### Mechanism 2: Re-establishing faster

If a client has connected before, QUIC may use saved cryptographic/session information to avoid repeating the entire setup cost.

This is why the announcement emphasises:

```text
expedited connection establishment
re-establish a connection at 0-RTT
```

### Mechanism 3: Multiplexed streams

QUIC allows multiple independent streams inside one connection.

This helps with web pages containing many objects:

- HTML,
- CSS,
- JavaScript,
- images,
- fonts,
- videos.

With TCP, if one part is delayed, later bytes in the same TCP stream may be blocked.

With QUIC streams, one delayed stream does not necessarily block all other streams in the same way.

### Mechanism 4: Connection migration

QUIC connections use connection IDs.

That means the connection can survive a change in IP address, such as:

```text
Wi-Fi -> mobile data
mobile data -> Wi-Fi
one network -> another network
```

In QUICv1/v2, migration is client-initiated.

### Mechanism 5: Less header repetition after setup

QUIC can use shorter headers for established connections. The connection ID can be enough to identify the connection, so not every packet needs all the full setup-style information.

---

## 8.4 Model long-question answer

Question:

> Explain why QUIC may reduce latency compared with TCP.

Answer:

QUIC reduces latency mainly by reducing the number of round trips needed before useful data can be sent. It runs over UDP but implements transport-layer features itself. QUIC combines connection setup with cryptographic setup, allowing 1-RTT establishment and, in some repeated-connection cases, 0-RTT data. It also supports multiple independent streams inside one connection, so a delay in one stream does not necessarily block delivery of all other streams. QUIC uses connection IDs, allowing a client to migrate a connection to a new IP address without fully tearing down and re-establishing the connection. These mechanisms make QUIC “quick” in terms of reduced waiting time, not because it increases the raw physical transmission speed.

---

## 8.5 Possible QUIC questions

| Possible question | What to include |
|---|---|
| Explain why QUIC is quick. | Reduced setup latency, 0-RTT/1-RTT, multiplexing, migration. |
| Compare TCP and QUIC. | TCP uses OS transport stack; QUIC runs over UDP; QUIC integrates encryption and streams. |
| Explain QUIC migration. | Connection ID allows client to move between IP addresses without full reconnect. |
| Explain QUIC streams. | Multiple independent streams reduce head-of-line blocking. |
| Why use UDP? | Easier deployment through existing networks; avoids needing new kernel/network-stack protocol support. |

---

# 9. Topic 7: ASN.1

## 9.1 Why ASN.1 is likely

Layer 6 scope is explicitly narrowed to:

```text
Only ASN.1
```

Past papers had many Layer 6 questions on character encoding, UTF-8, MIME, and related content. This year those are much less useful because the scope has shifted. If the lecturer wants a Layer 6 long question, ASN.1 is the obvious candidate.

2025 ST2 included ASN.1 MCQs about:

- BER encoding as a type-length-value triple,
- invalid ASN.1 types such as `STRUCT` or `ARRAY`,
- ASN.1 syntax being defined using a grammar.

---

## 9.2 What ASN.1 is

ASN.1 stands for:

```text
Abstract Syntax Notation One
```

It is used to specify the structure of protocol messages.

Think of it like defining a structured record in a programming language.

Example idea:

```text
Student ::= SEQUENCE {
  name VisibleString,
  studentNumber INTEGER
}
```

This says a student message has:

- a name,
- a student number.

---

## 9.3 Key ASN.1 constructors

| ASN.1 construct | Meaning | Programming analogy |
|---|---|---|
| `SEQUENCE` | Ordered list of fields | struct / record |
| `SET` | Unordered collection of fields | unordered record/set |
| `SEQUENCE OF` | Ordered list of repeated items | array/list |
| `SET OF` | Unordered list of repeated items | set collection |
| `CHOICE` | One of several alternatives | union / variant type |

## 9.4 Common primitive types

| Type | Meaning |
|---|---|
| `INTEGER` | Whole number |
| `VisibleString` | Printable text string |
| `OCTET STRING` | Raw bytes |
| `BOOLEAN` | True/false |
| `NULL` | No value |

## 9.5 Invalid ASN.1 distractors

These are common traps:

| Invalid term | Why it is wrong |
|---|---|
| `STRUCT` | ASN.1 uses `SEQUENCE`, not `STRUCT`. |
| `ARRAY` | ASN.1 uses `SEQUENCE OF` or `SET OF`, not `ARRAY`. |
| `MESSAGE` | Not a normal ASN.1 type/constructor. |

---

## 9.6 BER encoding

BER stands for:

```text
Basic Encoding Rules
```

A BER value is encoded as:

```text
Type, Length, Value
```

Also called:

```text
TLV
```

Example:

| Component | Purpose |
|---|---|
| Type | Says what kind of value follows. |
| Length | Says how many bytes the value occupies. |
| Value | The actual encoded data. |

Past-paper style:

> A BER value in ASN.1 is encoded as a triple consisting of what?

Answer:

```text
A type, a length, and a value.
```

---

## 9.7 Writing an ASN.1 definition: worked example

### Possible long question

> Define an ASN.1 structure for a student record. A student has a surname, initials, student number, a set of completed courses, and an address. The address may be either a street address or a PO box.

### Step 1: Identify the top-level structure

A student record has multiple named fields in a fixed order, so use:

```text
SEQUENCE
```

### Step 2: Identify repeated courses

The student can have multiple courses.

If order does not matter, use:

```text
SET OF Course
```

### Step 3: Identify alternative address types

The address can be one of two forms:

- street address,
- PO box.

Use:

```text
CHOICE
```

### Step 4: Write the ASN.1

```asn1
Student ::= SEQUENCE {
  surname        VisibleString,
  initials       VisibleString,
  studentNumber  INTEGER,
  courses        SET OF Course,
  address        Address
}

Course ::= SEQUENCE {
  code        VisibleString,
  courseName  VisibleString,
  mark        INTEGER
}

Address ::= CHOICE {
  streetAddress  StreetAddress,
  poBoxAddress   POBoxAddress
}

StreetAddress ::= SEQUENCE {
  streetNumber  INTEGER,
  streetName    VisibleString,
  city          VisibleString
}

POBoxAddress ::= SEQUENCE {
  boxNumber  INTEGER,
  city       VisibleString
}
```

### Step 5: Explain your choices

A strong answer would include:

- `Student` is a `SEQUENCE` because it is a structured ordered record.
- `courses` is a `SET OF Course` because there may be many courses and their order is not important.
- `Address` is a `CHOICE` because the address is either a street address or a PO box, not both.
- `INTEGER` is used for numeric values.
- `VisibleString` is used for human-readable text.

---

## 9.8 Possible ASN.1 long questions

| Possible question | What to do |
|---|---|
| Define a protocol message in ASN.1. | Use `SEQUENCE`, fields, and appropriate primitive types. |
| Model alternatives. | Use `CHOICE`. |
| Model repeated values. | Use `SEQUENCE OF` or `SET OF`. |
| Explain BER. | Say Type-Length-Value. |
| Identify invalid ASN.1 types. | Reject `STRUCT`, `ARRAY`, `MESSAGE`. |
| Explain abstract syntax vs encoding. | ASN.1 defines structure; BER/DER/CER/PER define byte representation. |

---

# 10. Topic 8: IPv6

IPv6 is in scope. It is probably more likely as MCQ than as a full long question, but it can appear as a short structured long question.

## 10.1 Key IPv6 facts

| Feature | IPv4 | IPv6 |
|---|---|---|
| Address size | 32 bits | 128 bits |
| Notation | dotted decimal | hexadecimal groups separated by colons |
| Broadcast | Yes | No traditional broadcast |
| Multicast | Yes | Yes, heavily used |
| ARP | Used | Replaced by Neighbor Discovery mechanisms |
| Header checksum | Exists | Removed in IPv6 |

## 10.2 IPv6 compression rules

Example full address:

```text
2001:0db8:0000:0000:0000:ff00:0042:8329
```

Step 1: Remove leading zeroes in each group:

```text
2001:db8:0:0:0:ff00:42:8329
```

Step 2: Replace one consecutive run of zero groups with `::`:

```text
2001:db8::ff00:42:8329
```

Important:

```text
You may only use :: once in an IPv6 address.
```

## 10.3 Possible IPv6 questions

| Question type | Example |
|---|---|
| Compress IPv6 address | `2001:0db8:0000:0000:0000:ff00:0042:8329` -> `2001:db8::ff00:42:8329` |
| Expand IPv6 address | `2001:db8::1` -> `2001:0db8:0000:0000:0000:0000:0000:0001` |
| Compare IPv4/IPv6 | address size, notation, broadcast, checksum, fragmentation |
| Identify special addresses | `::1` loopback, `::` unspecified |

---

# 11. Topic 9: ARP, ICMP, TTL, and packet forwarding

These topics are in Layer 3 and could appear in smaller long-question parts.

---

## 11.1 ARP

ARP stands for:

```text
Address Resolution Protocol
```

Purpose:

```text
Maps an IPv4 address to a Layer 2 MAC address on the local network.
```

### Typical ARP process

If host A wants to send to host B on the same local network:

1. A knows B's IP address.
2. A needs B's MAC address.
3. A broadcasts an ARP request:

```text
Who has IP address B?
```

4. B replies with its MAC address.
5. A sends the Ethernet frame to B's MAC address.

### Trap

ARP is only for local-link resolution. If the destination is not on the local network, the host ARPs for the **default gateway's MAC address**, not the final destination's MAC address.

---

## 11.2 ICMP and TTL

TTL stands for:

```text
Time To Live
```

Every router that forwards an IP packet decrements TTL by 1.

If TTL reaches 0:

1. the router discards the packet,
2. the router may send an ICMP Time Exceeded message back to the source.

This prevents packets from looping forever.

---

## 11.3 Packet forwarding algorithm

When a router receives a packet:

1. Check if the destination is directly connected.
2. If yes, deliver directly using Layer 2.
3. If not, check the routing table.
4. If one or more routes match, use the longest-prefix match.
5. If no specific route matches, use default route if available.
6. If no default route exists, discard the packet.

Possible long-question form:

> Given a destination IP and a routing table, identify the next hop.

Always apply:

```text
Longest matching prefix wins.
```

---

# 12. Topic 10: Layer 5 session layer

Layer 5 is in scope, but there is very little content. It is more likely MCQ than long question, but a short explanation question is possible.

## 12.1 Main Layer 5 idea

Layer 5 manages sessions.

Important mechanisms:

- long-lived sessions,
- checkpoints,
- rollback/recovery,
- heartbeats.

## 12.2 Checkpointing and rollback

Layer 5 may provide checkpoints so that if a connection is lost, only messages sent since the last checkpoint need to be retransmitted.

It can also emulate database-transaction-like behaviour:

```text
If the final message in a sequence does not arrive, the sequence can be rolled back.
```

Past-paper style:

> Which OSI layer may provide checkpoints such that only messages since the last checkpoint must be retransmitted after a connection is lost?

Answer:

```text
Layer 5
```

## 12.3 Heartbeats

A long-lived session may use heartbeat messages to detect whether the other endpoint is still alive.

Example:

```text
Network management system regularly checks whether a router/switch is still reachable.
```

---

# 13. Final predicted longer questions and how to prepare

## Prediction 1: Subnetting / supernetting

### Learn until automatic

- convert `/n` to mask,
- calculate block size,
- find network address,
- find broadcast address,
- find usable range,
- calculate host count,
- combine address ranges into CIDR blocks.

### Practice format

```text
Given 170.170.42.150/26:
a. mask
b. network address
c. broadcast address
d. first host
e. last host
f. usable hosts
```

---

## Prediction 2: TCP timers or TCP reliability

### Learn until automatic

Timers:

```text
Retransmission -> retransmit data
Acknowledgement -> send ACK
Persistence -> send window probe
Keepalive -> probe peer / release resources
Quiet -> wait before reusing port/resources
```

Reliability mechanisms:

```text
3-way handshake
sequence numbers
acknowledgement numbers
ACK/ARQ
retransmission timer
checksum
sliding window/window advertisement
slow start
exponential back-off
termination handshake
```

---

## Prediction 3: Dijkstra or Bellman-Ford/RIP

### Learn until automatic

Dijkstra:

```text
Pick lowest-cost unfinished node.
Update neighbours.
Repeat.
```

Bellman-Ford/RIP:

```text
new cost via neighbour = cost to neighbour + neighbour's advertised cost
```

Counting to infinity:

```text
Bellman-Ford/RIP problem.
```

---

## Prediction 4: QUIC or ASN.1

### QUIC must-know list

```text
Runs over UDP
Reduces setup latency
0-RTT / 1-RTT
Multiplexed streams
Connection migration
Connection IDs
Client initiates migration in QUICv1/v2
```

### ASN.1 must-know list

```text
ASN.1 defines abstract message syntax
Syntax defined using grammar
BER = Type-Length-Value
SEQUENCE = ordered record
SET = unordered collection
CHOICE = one alternative
STRUCT and ARRAY are invalid distractors
```

---

# 14. One-page cram checklist

## Subnetting

- [ ] I can convert `/26` to `255.255.255.192`.
- [ ] I can calculate block size using `256 - mask octet`.
- [ ] I can find network and broadcast address.
- [ ] I can find usable host range.
- [ ] I can calculate usable hosts using `2^hostbits - 2`.
- [ ] I can find the smallest CIDR block for a range.
- [ ] I can apply longest-prefix match.

## Routing

- [ ] OSPF uses Dijkstra.
- [ ] RIP uses Bellman-Ford.
- [ ] BGP is external/inter-AS.
- [ ] Counting to infinity is a RIP/Bellman-Ford issue.
- [ ] I can run Dijkstra from a graph.
- [ ] I can update a routing table from a neighbour advertisement.

## TCP

- [ ] I know the 3-way handshake.
- [ ] I know SYN and SYN+ACK consume phantom sequence numbers.
- [ ] I know ACK field is meaningless unless ACK flag is set.
- [ ] I can list TCP header fields.
- [ ] I can explain five reliability mechanisms.
- [ ] I know all five TCP timers.
- [ ] I can calculate basic ACK/window values.

## QUIC

- [ ] QUIC runs over UDP.
- [ ] QUIC reduces latency, not raw physical transmission time.
- [ ] QUIC supports 0-RTT/1-RTT.
- [ ] QUIC supports stream multiplexing.
- [ ] QUIC supports client-initiated connection migration.

## ASN.1

- [ ] BER = Type-Length-Value.
- [ ] ASN.1 syntax is defined using a grammar.
- [ ] `SEQUENCE`, `SET`, `CHOICE`, `INTEGER`, `VisibleString` are valid.
- [ ] `STRUCT`, `ARRAY`, `MESSAGE` are invalid distractors.
- [ ] I can write a simple ASN.1 definition.

---

# 15. Final study order

Use this order if time is limited:

1. **Subnetting / supernetting / CIDR**
2. **TCP timers**
3. **TCP reliability mechanisms**
4. **Dijkstra and Bellman-Ford/RIP**
5. **QUIC**
6. **ASN.1**
7. **IPv6 basics**
8. **ARP / ICMP / TTL / packet forwarding**
9. **Layer 5 session concepts**

If you only have time for four areas, focus on:

```text
Subnetting
TCP timers/reliability
Routing algorithms
QUIC + ASN.1 basics
```


---

# 16. Source mapping used in this guide

This guide draws examples and answer patterns from the uploaded COS332 materials:

- `Memo2023.pdf`: ST2 subnetting answers, TCP header-field answers, and TCP flow/window numeric answers.
- `Memo2024.pdf`: ST2 Dijkstra/routing-table style answer and timer/numeric answer patterns.
- `Memo2025.pdf`: ST2 TCP timer answers, TCP reliability mechanisms, and IPv4/CIDR answers.
- `ST2025.pdf`: ASN.1, TCP, QUIC, and Layer 3 MCQ patterns.
- `Layer_3.md`: expanded subnetting, supernetting, routing, IPv4, IPv6, ARP, ICMP notes.
- `Layer_4.md`: expanded TCP, UDP, QUIC, timers, reliability, flow-control notes.
- `Layer_5.md`: session-layer checkpointing, rollback, heartbeat, and SNA notes.
- `Layer_6.md`: ASN.1 and BER/DER/CER notes.

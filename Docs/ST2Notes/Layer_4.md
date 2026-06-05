# Layer 4: The Transport Layer

> **Scope note:** All of Layer 4 is examinable. Non-TCP/IP transport protocols (TP0–TP4, ATM, etc.) are explicitly **out of scope** per the lecturer's announcement. The protocols you must know are **UDP**, **TCP**, and **QUIC**.

---

## 1. Introduction — The "Pipe" Between Processes

The Transport Layer provides a **logical "pipe"** between two processes communicating across a network. At one end might be a web browser, at the other a web server; or an email program at one end and a mailbox server (IMAP4) at the other.

### Two layers of hiding
The Transport Layer hides the **network's** complexity (routing, cable access, etc.) from the application-oriented layers, *and* it hides the application's behaviour (which process talks when, what data looks like) from the network-oriented layers. As far as the application is concerned, the network is just an abstract pipe; as far as the network is concerned, it is just providing a transport service that the application can use however it wants.

### Two core design decisions for any Layer 4 protocol
1. **How to identify the processes** at the endpoints of the pipe.
2. **How reliable the pipe should be.**

### Monitoring transport-layer connections
> **MCQ fact:** The command that enables one to see the status of transport layer connections on a host (in most operating systems) is **`netstat`**. (Not `ping`, not `tracert/traceroute`, not `tcp-show`, not `ps`.)

A typical `netstat` line on Linux looks like:
```
tcp 127.0.0.1:27117 127.0.0.1:48956 ESTABLISHED keepalive
```
This shows two endpoints (local and remote IP:port), the TCP state (`ESTABLISHED`), and which timer is currently active (`keepalive`).

---

## 2. Identifying Processes — Ports and Sockets

Processes are identified by **numerical port numbers** carried in the Layer 4 header.

### Port classifications
| Range | Name | Use |
| --- | --- | --- |
| 0 – 1023 | **Well-known** | Reserved for standard internet services (HTTP=80, HTTPS=443, DNS=53, SMTP=25, FTP=21, SSH=22, etc.) |
| 1024 – 49151 | **Registered** | Registered for specific applications but usable by others if open. |
| 49152 – 65535 | **Dynamic / Private** | Ad-hoc, requested by clients from the OS for receiving responses. |

> **MCQ fact:** Port **55555** is a **Dynamic** port (it falls in the 49152–65535 range).

### Sockets
A **socket** is the combination of an IP address and a port: `<IP, port>`.

Example: when a web browser connects to a web server at `xx.co.za` on port 80, the browser opens the socket `<xx.co.za, 80>`.

### Server-socket vs client-socket
A program opening a socket to act as a **server** must:
- Specify an **address** and **port number**
- **Wait for connections** (it does not initiate)

A client, conversely, *initiates* connections.

---

## 3. Reliability Mechanisms

A protocol is **reliable** if it guarantees data is delivered (or, if delivery fails, both ends know about the failure).

### Connection-oriented vs connectionless
- **Reliable protocols** are typically **connection-oriented**: they explicitly establish, use, and tear down a connection. *Analogy:* a telephone call — you dial, talk, ask the other party to repeat unclear words, and hang up.
- **Unreliable protocols** are **connectionless**: no setup or teardown. *Analogy:* the snail-mail postal system — you send a letter blindly without knowing if the recipient is ready or even alive.

### What can go wrong on a "pipe"
- Data **changes** before arriving (corruption)
- Data **never arrives** (loss)
- Data arrives **faster** than the receiver can cope (flow problem)
- Data arrives **out of sequence**
- Data is **duplicated** and arrives multiple times

### Flow control mechanisms
Flow control prevents a fast sender from overwhelming a slow receiver:
- **Stop-and-wait:** sender transmits one message, then waits for an ACK before sending the next. Highly inefficient on long-latency links.
- **Sliding window:** a specified number of messages may be sent without waiting for each ACK.
  - **Go-Back-N:** if a message is lost, the sender re-sends the lost message *and every subsequent message*.
  - **Selective Repeat:** the sender re-sends only the specifically lost message.

### Congestion control
A mechanism to **slow down transmission** when packet loss indicates the network is congested. Ensures fair sharing of bandwidth amongst all senders on the network.

---

## 4. TCP (Transmission Control Protocol)

TCP is the standard **reliable, connection-oriented** Layer 4 protocol.

### 4.1 TCP reliability mechanisms (memorise!)
> **Exam Q (typical):** "TCP is a reliable protocol. List any **five** mechanisms used by TCP to provide this reliability."

Any **five** of the following are accepted:

1. **3-way handshake to establish** the connection
2. **3-way handshake to terminate** the connection
3. **ACK for ARQ** (Automatic Repeat reQuest)
4. **Slow start** (congestion-window control)
5. **Exponential back-off** (on repeated loss)
6. **CRC / checksum over the entire segment**
7. **Window advertisements** (sliding-window flow control)
8. **Sequence numbers / acknowledgement numbers**

### 4.2 Connection establishment (3-way handshake)
The handshake exists because we have one wire from A to B and another from B to A — both directions must be verified before reliable communication can be claimed.
```
A → B :  SYN          (Are you there, ready to talk?)
A ← B :  SYN+ACK      (Yes! Are *you* there?)
A → B :  ACK          (Yes!)
```

#### Phantom bytes — common MCQ trap
The SYN and SYN+ACK messages each consume **one sequence number** (the so-called *phantom byte*), even though they carry **no actual payload data**.

> **MCQ fact:** "Which of the following statements is/are *false* about phantom bytes used in an initial 3-way TCP/IP handshake?"
> - It is counted as part of the SYN message ✓ (TRUE)
> - It is counted as part of the SYN+ACK message ✓ (TRUE)
> - It is counted as part of the ACK message ✗ (FALSE)
> - It consists of one byte of data ✗ (FALSE — it does NOT contain payload data)
>
> Answer: **More than one of the statements above are false** (C and D are both false).

#### Differentiating handshake packets (2024 ST2)
**Q (2024 ST2 m):** "How are the SYN and ACK packets sent during a TCP handshake differentiated from one another?"
- **A: The flags are used to determine the type of handshake packet.** ✓

**Q (2024 ST2 n):** "How does the server differentiate between the ACK packet it receives as the last part of the handshake to establish a connection, and an ACK packet that acknowledges data that has been received?"
- **E: None of the above.** (The server differentiates by *which TCP state it is in* — it is in SYN-RECEIVED for the final handshake ACK, vs ESTABLISHED for data ACKs — not by any flag/sequence-number convention.)

### 4.3 Connection termination
A separate 3-way (sometimes 4-way) handshake using FIN and FIN+ACK flags.

### 4.4 TCP states
Include `LISTEN`, `SYN-SENT`, `SYN-RECEIVED`, `ESTABLISHED`, `FIN-WAIT-1`, `FIN-WAIT-2`, `CLOSE-WAIT`, `LAST-ACK`, `TIME-WAIT`, `CLOSED`.

- **`LISTEN`** — Node is acting as a **server** and waiting for a SYN message.
- **`TIME-WAIT`** — Node is waiting for **'lost' traffic to arrive at the port that is no longer in use**, before that port becomes available for reuse. (Distractor B in a 2025 ST2 MCQ ("The connection is about to time-out") is **wrong**; D is correct.)

### 4.5 TCP header fields
Standard TCP header fields include:
- Source port
- Destination port
- **Sequence number**
- **Acknowledgement number**
- **Flags** (SYN, ACK, FIN, RST, PSH, URG)
- **Window advertisement** (window size)
- Checksum
- Urgent pointer
- **Options**
- Padding

> **MCQ fact:** Which field does **NOT** occur in a TCP header? — **Length**. (Length is in the *UDP* header and in the *IP* header, not the TCP header.)

### 4.6 The ACK flag and the acknowledgement field
The acknowledgement-number field is *only valid* when the **ACK flag is set**.

> **MCQ fact:** "A sends a TCP segment to node B. The acknowledgement field contains the value 150. The ACK flag is **not** set. This means:"
> - **B: B should disregard the value 150 — it has no meaning.** ✓

> **Related fact:** Conversely, when node A *does* set the ACK flag on a segment to B, this may cause an existing **retransmission timer at A** to be **deleted/reset**, because the data it covered has now been acknowledged by B in the opposite direction. (2023 paper question: "A sends a TCP segment to node B with its ACK flag set. This may affect (or create) relevant timers at A and/or B. What happens to one or more of the **retransmission** timers at A?" → **D: An existing timer may be deleted.** Similarly the **acknowledgement** timer at A may be deleted, or **B's** acknowledgement timer may be reset.)

### 4.7 Damaged-packet handling — TCP has no NAK
TCP does **not** have a NAK (negative acknowledgement) flag.

> **MCQ fact:** "A sends a TCP segment to B, but it arrives damaged. How is this resolved?"
> - **B: B discards the segment and does not acknowledge it; the retransmission timer at A expires and the packet is sent again.** ✓

### 4.8 TCP timers — **memorise the five timers**

> **Exam Q (asked almost every year):** Very briefly state what happens when each TCP timer expires.

| Timer | When activated | What happens when it expires |
| --- | --- | --- |
| **Retransmission timer** | When a segment is sent | A segment containing data is (re)transmitted. The timer is restarted for the retransmitted segment. |
| **Acknowledgement timer** | When data is received that needs acknowledging (used to delay sending an ACK so it can be piggybacked or batched) | A segment containing an acknowledgement is transmitted. |
| **Persistence timer** | When the sender is informed that the receiver's window size has become 0 | A **probe** message (a single byte that is not part of the data stream) is sent to check whether the receiver has freed up window space. The receiver responds with the last ACK plus an updated window size. |
| **Keepalive timer** | When a TCP connection has been idle for a long time (default ~2 hours) | Either a **probe** is sent to check whether the other party is still alive (which restarts the timer if a response arrives), or — if no response — **connection resources are released**. |
| **Quiet timer** | When the final FIN is sent in the 3-way termination handshake (i.e. the connection enters `TIME-WAIT`) | The **port** that the connection occupied is freed and made available for reuse. Lasts twice the maximum segment lifetime. |

#### Notes on the persistence timer
> **MCQ fact:** "When the persistence timer at A expires, it implies that:" — **A is waiting for space to free up in B's window before further data can be sent.**

#### Round-Trip Time (RTT) for the retransmission timer
The wait time before retransmitting is based on the **measured round-trip time (RTTm)**: send a packet, measure how long the ACK takes. In practice, a series of RTT measurements are combined into a *smoothed weighted average* RTT, which is used to set the timer. The round trip is the time for a message to travel from sender to receiver *and* the ACK back.

#### Definitions (Q4-style, 2024 ST2)
- **TCP slow start:** A congestion-control mechanism. The congestion window (`cwnd`) starts small (1 segment). For each ACK received, `cwnd` increases — initially exponentially, so the sender quickly probes the network's capacity. When loss is detected, `cwnd` is halved (or reset to 1) to back off.
- **TCP acknowledgement timer:** A timer that delays sending an ACK after receiving data, so that the ACK can be piggybacked onto reverse traffic or aggregated with other ACKs. When it expires, an ACK is sent.
- **Round-trip time (RTT):** The time taken for a message to travel from sender to receiver plus the time for the ACK to return. Used to set the retransmission timer.
- **Middlebox (Layer 4 context):** A device deployed between two TCP endpoints (typically a firewall or NAT) that "digs into" TCP headers — and sometimes TCP payloads — to make decisions. Middleboxes that were designed around current TCP behaviour are the reason TCP cannot easily be updated; any change would break the middleboxes (and effectively break the Internet for those connections). This problem is called **protocol ossification**.
- **Protocol ossification:** The inability to modify a protocol because doing so would break unrelated middleboxes and equipment that have made assumptions about that protocol's on-the-wire form. QUIC was designed deliberately to avoid this (encrypts headers heavily and randomises version numbering — e.g. QUICv2 uses hex `6b3343cf`).

### 4.9 TCP flow control — sliding window in bytes

TCP's sliding window is byte-oriented (not segment-oriented like the congestion window). Each segment carries a **window advertisement** stating how much buffer space the receiver currently has free. The sender must not send more unacknowledged bytes than this window permits.

### 4.10 TCP congestion control — slow start + exponential back-off

- **Congestion window (`cwnd`):** A second window kept at the *sender* (in addition to the receiver's advertised window). `cwnd` counts **segments**, not bytes.
- **Slow start:** Begin with `cwnd = 1`. For every ACK received, increase `cwnd`. Because multiple segments can be acknowledged together, `cwnd` grows roughly exponentially up to a threshold.
- **On loss:** Halve the current `cwnd` to derive a new threshold, then reset `cwnd` to 1 and restart slow start. Once `cwnd` reaches the new threshold, growth slows to **linear** to avoid overshooting the safe rate again. This combined behaviour is "slow start + exponential back-off".

### 4.11 Minimum number of timer types for any sliding-window ARQ
**Q (2024 ST2 o):** "What is the minimum number of timer types required by any sliding window ARQ protocol?"
- **Answer: 2.** (A retransmission timer for the sender, and an acknowledgement timer for the receiver. Other timers — persistence, keepalive, quiet — are TCP-specific refinements.)

### 4.12 The TCP **Quiet** timer and TIME-WAIT (2024 ST2)
**Q (2024 ST2 p):** "The TCP *quiet* timer determines when a port may be used for a new TCP connection after a previous connection has been closed. Which of the following claims is/are true?"
- A: The port (or socket) is in the `TIME-WAIT` state while the quiet timer is active. ✓
- B: The quiet timer is activated when the FIN+ACK message is sent. (This is not quite right; activated at the 3rd-handshake stage.)
- C: The quiet timer solves the problem of a packet from a previous connection being deemed part of a new connection. ✓

Answer: **D — More than one of the above** (A and C are both true).

---

## 5. UDP (User Datagram Protocol)

UDP is an **unreliable, connectionless** Layer 4 protocol offering a "best-effort" service.

### 5.1 What UDP lacks
- No flow control (the flow-control mechanism is described as **unrestricted** — i.e. *none*)
- No congestion control
- No sequencing
- No acknowledgements
- No retransmission

### 5.2 UDP header (very simple)
- Source port
- Destination port
- **Length**
- Checksum
- Payload

(Contrast TCP, where Length is *not* present.)

### 5.3 When UDP is preferable
> **MCQ fact:** Of `Web page`, `File transfer`, `Audio`, the data stream that generally works *better* with an unreliable Layer 4 protocol is **Audio**.

Reasons:
- **Real-time speech transmission:** Dropping a small fraction of a second of audio is preferable to pausing transmission to retransmit. Reliability would introduce intolerable delays.
- **DNS lookup:** Requires only a single request and a single reply. A full TCP 3-way handshake plus tear-down would be 8 messages for a 2-message transaction — wasteful overhead.

### 5.4 DNS uses *both* TCP and UDP
> **MCQ fact:** "Which of the following protocol(s) is/are used on the transport layer by DNS?" — **D: More than one of the above** (DNS uses **UDP** for standard queries and **TCP** for zone transfers and large responses).

---

## 6. QUIC (Quick UDP Internet Connections)

QUIC is a modern, **reliable, connection-oriented** Layer 4 protocol that runs **on top of UDP**. Google began work on it in 2012; QUICv1 was standardised in RFC 9000 (2022) and QUICv2 in RFC 9369 (December 2023).

### 6.1 Key facts
- QUIC provides reliability above the unreliable UDP it sits on. The underlying UDP packets remain connectionless and unreliable; QUIC supplies the reliability on top.
- Some informally refer to QUIC as "TCP version 2". QUIC shares all TCP's goals but adds more.
- **Within 10 years of its 2012 introduction, more than 50% of Web traffic was already QUIC** rather than TCP. Many predict QUIC will eventually replace TCP entirely.
- QUIC's original full name was **Quick UDP Internet Connections** — useful for remembering its three core properties: **quick, connection-oriented, on top of UDP**.
- QUIC was originally referred to as **gQUIC** (Google's version); the standardised IETF version is sometimes called IETF QUIC.

### 6.2 Security by default
> QUIC inherently integrates **TLS 1.3** encryption. There is **no unencrypted version** of QUIC. The handshake bundles together the connection setup and the TLS handshake.

### 6.3 Connection IDs and connection migration
TCP identifies a connection by the 4-tuple `(srcIP, srcPort, dstIP, dstPort)`. If the client's IP changes (e.g. a mobile user switches from Wi-Fi to cellular), TCP drops the connection. QUIC instead uses opaque **Connection IDs**, so the connection survives an IP change.

> **MCQ fact:** In QUICv1 and QUICv2, **the client** is the party that can initiate a connection migration. (Not the server, not a network management system.)

### 6.4 Long-header fields always present
> **MCQ fact:** Which headers are always present in a long QUIC header? (Include cases where the length of the field will be 0, meaning the field itself may be omitted.)
> - **Version**
> - **Source connection ID**
> - **Destination connection ID**
> Answer: **All of the above (E).**

### 6.5 Speed — 1-RTT and 0-RTT
> **MCQ fact (memorise):** "The claim that QUIC is a *quick* protocol means that:"
> - **B:** It reduces latency when establishing or re-establishing a connection.
> - **C:** Where multiple parts of a message must be transported, it ensures that parts of the message are delivered quickly even if some parts are delayed (multiplexed streams).
> Answer: **D — More than one of the above** (both B and C are correct).

#### The 0-RTT vs 1-RTT timing question
Assume a client establishes a new QUIC connection at time `t₀` and the server replies at `t₁`. The reply arrives at the client at `t₂`. The client transmits at even times (`t₀, t₂, t₄, …`) and the server at odd times (`t₁, t₃, t₅, …`).

- **Soonest application data may (sometimes) be sent:** `t₀` (via **0-RTT** if the client has cached keys from a prior session). 0-RTT lets the client piggyback encrypted application data into the very first packet.
- **Soonest 1-RTT application data may be sent:** `t₂`. The client must wait one full round trip to receive the server's reply before sending 1-RTT data.
- **Soonest the connection may be deemed fully established:** `t₃` (the client sends a finish-handshake packet at `t₂`, the server receives and acks at `t₃`). However, some textbook-aligned versions of this question answer **E (None of the above)** — the exact answer depends on what the lecturer considers "fully established".

### 6.6 Multiplexed streams — head-of-line blocking
Within a single QUIC connection, data is transported in multiple independent **streams**. If a packet on one stream is lost, only that stream is delayed; other streams continue. This avoids TCP's "head-of-line blocking" problem.

*Example:* A browser loading a webpage requests images, CSS, and scripts in parallel. If an image packet is lost, only the image stream pauses to retransmit; CSS and scripts keep loading.

### 6.7 Packets vs frames
- **Packets:** the on-the-wire units (Initial, Handshake, 0-RTT, 1-RTT, Retry, Version Negotiation).
- **Frames:** carried inside packets — STREAM, ACK, PING, CRYPTO, etc.
- **Only packets are acknowledged and retransmitted**, not individual frames.

### 6.8 Protocol ossification — and QUIC's defences
TCP can't be upgraded because middleboxes (firewalls, NATs) make hardcoded assumptions about TCP headers and payloads — updates break those middleboxes. This is called **protocol ossification**.

QUIC defends against this in two ways:
1. **Heavy encryption of headers and metadata**, so middleboxes can't easily "dig into" packets.
2. **Randomised version numbering** — QUICv2 uses the version-field value `6b3343cf` (hex), a deliberately arbitrary number, to prevent middleboxes from assuming any pattern. Furthermore, QUICv1 and QUICv2 use *different* bit patterns to identify the same packet type, so a firewall coded to recognise QUICv1's handshake packets won't recognise QUICv2's.

### 6.9 QUIC port usage
QUIC is currently used primarily to transport HTTPS, and on the server side will commonly use the same ports TCP uses (e.g. 443 for HTTPS).

---

## Examinable Practice Questions on Layer 4

### Multiple Choice

**Q1.** Which of the following data streams generally work(s) better with an unreliable Layer 4 protocol?
A. Web page   B. File transfer   C. Audio   D. More than one of the above   E. All of the above

**Q2.** Which of the following protocol(s) is/are used on the transport layer by DNS?
A. TCP   B. UDP   C. IP   D. More than one of the above   E. All of the above

**Q3.** Which command enables one to see the status of transport layer connections on a host (in most operating systems)?
A. netstat   B. ping   C. tracert/traceroute   D. tcp-show   E. ps

**Q4.** UDP uses the following flow-control mechanism:
A. Stop and Wait   B. Sliding window   C. Unrestricted   D. More than one of the above   E. All of the above

**Q5.** A sends a TCP segment to node B. The acknowledgement field contains the value 150. The ACK flag is *not* set. This means:
A. B may assume that bytes up to byte 149 that it had sent are acknowledged.
B. B should disregard the value 150 — it has no meaning.
C. This is a negative acknowledgement of the segment B has sent that had the sequence number 150.
D. The TCP layer at A is misconfigured; it should have set the ACK flag.

**Q6.** Which of the following fields does *not* occur in a TCP header?
A. Source port   B. Window advertisement   C. Sequence number   D. Options   E. Length

**Q7.** Which of the following statements is/are *false* about phantom bytes used in an initial 3-way TCP/IP handshake?
A. It is counted as part of the SYN message.
B. It is counted as part of the SYN+ACK message.
C. It is counted as part of the ACK message.
D. It consists of one byte of data.
E. More than one of the statements above are false.

**Q8.** A TCP connection in the `TIME-WAIT` state means that:
A. The node is waiting for data from the node that it is connected to.
B. The connection is about to time-out if no further data is transmitted soon.
C. The connection will soon be established (as soon as the handshake is completed).
D. The node is waiting for 'lost' traffic to arrive at the port that is no longer in use, before it will be available for reuse.
E. The network is congested.

**Q9.** A TCP node that is in the `LISTEN` state:
A. Is acting as a server and waiting for a SYN message.
B. Is acting as a client and has sent a SYN message.
C. May act as a client after sending a SYN message.
D. More than one of the above.
E. None of the above.

**Q10.** What does the claim that QUIC is a *quick* protocol mean?
A. It manages the lower layers to transmit raw data at higher bit rates.
B. It reduces latency when establishing or re-establishing a connection.
C. Where multiple parts of a message have to be transported, it ensures that parts of the message are delivered quickly even if some parts are delayed.
D. More than one of the above.
E. All of the above.

**Q11.** QUIC connections can migrate. Which party can initiate such a migration in QUICv1 or QUICv2?
A. The client   B. The server   C. The network management system   D. More than one of the above   E. All of the above

**Q12.** Say a damaged packet arrives at its destination. Suppose A sends a TCP segment to B, but it arrives damaged at B. How is this resolved?
A. B sets the NAK TCP flag and sends it as a response to A.
B. B discards the segment and does not acknowledge it; the retransmission timer at A expires and the packet is sent again.
C. B requests the network layer at B to deal with the error.
D. B corrects the damaged segment and (eventually) acknowledges receipt.
E. The lower layer protocols perform error checking, so a damaged segment will never arrive.

**Q13.** Suppose node A is connected to node B via TCP. When the persistence timer at A expires it implies that:
A. B has not yet acknowledged the last segment A sent to B.
B. A is waiting for space to free up in B's window before further data can be sent.
C. A has no data to send, so it transmits a single byte to indicate that it is still present.
D. More than one of the above.

**Q14.** What is the soonest time at which application data may (sometimes) be sent in QUIC? (Client at even times, server at odd times.)
A. t₀   B. t₁   C. t₂   D. t₃

**Q15.** What is the soonest time at which **1-RTT** application data may be sent in QUIC?
A. t₀   B. t₁   C. t₂   D. t₃

**Q16.** What type of port is port 55555?
A. Registered   B. Well-known   C. Dynamic   D. Practical   E. Temporary

**Q17.** What is the minimum number of timer types required by any sliding window ARQ protocol?
A. 1   B. 2   C. 3   D. 4   E. 5

**Q18.** A program that wants to open a socket in order to act as a server needs to specify:
A. The address of the server   B. The address of the client   C. The port on the server   D. The port on the client   E. More than one of the above

**Q19.** Which of the following headers are always present in a *long* QUIC header? (Include cases where the length of the field will be present and may be 0, meaning the field itself may be omitted.)
A. Version   B. Source connection ID   C. Destination connection ID   D. More than one of the above   E. All of the above

**Q20.** (2024 ST2) Which ISO OSI layer may provide checkpoints, such that only messages sent since the last checkpoint have to be retransmitted after a connection has been lost?
A. 2   B. 3   C. 4   D. 5   E. 6

**Q21.** (2024 ST2) How are the SYN and ACK packets sent during a TCP handshake differentiated from one another?
A. The flags are used to determine the type of handshake packet.
B. These packets carry a phantom byte in which the type (SYN or ACK) is encoded.
C. The sequence and acknowledgement numbers determine the type of packet; a sequence number of 0 indicates a SYN, while sequence number 0 and acknowledgement number 1 indicate a SYN+ACK.
D. More than one of the above.
E. All of the above.

### Long-Form & Calculation

**Q22. TCP timers definition.** Very briefly state what happens when the following TCP timers expire:
a) Retransmission timer
b) Acknowledgement timer
c) Persistence timer
d) Keepalive timer
e) Quiet timer

**Q23. TCP reliability.** TCP is a reliable protocol. List any **five** mechanisms used by TCP to provide this reliability. Keep your answers brief; no explanation required.

**Q24. TCP flow control & sequence calculation (standard variant).** Node A is busy communicating with node B via a TCP connection. At some time *t* the next byte A will send is byte 300. The next byte B will send is byte 500. The window size at A is 1000. The window size at B is 100.
- At time *t+1* A wants to send **200** bytes to B. Call this message *m₁*.
- At time *t+2* B consumes 100 bytes from its buffer.
- At time *t+3* B sends a message containing 50 bytes to A — message *m₃*.
- At time *t+4* A sends a message to B acknowledging *m₃* (and including any residual data) — message *m₄*.
- At time *t+5* B sends an empty acknowledgement *m₅*.

a) Sequence number included with *m₁*?
b) Acknowledgement number included with *m₄*?
c) Length of *m₄*?
d) Window advertisement included with *m₄*?
e) Window advertisement included with *m₅*?

**Q25. TCP flow control & sequence calculation (2024 variant).** Same setup as Q24 except A wants to send **300** bytes at *t+1*, and B consumes **200** bytes at *t+2*. Answer the same a)–e).

**Q26. Definitions (2024 ST2 style).** Briefly define or describe the following terms:
a) TCP slow start
b) TCP acknowledgement timer
c) Round-trip time
d) Middlebox (especially in the context of Layer 4)
e) Protocol ossification

---

## Memo / Answer Key

### MCQ Answers
**A1.** C (Audio). Real-time media tolerates loss better than retransmission delay.
**A2.** D (More than one — DNS uses UDP normally and TCP for zone transfers).
**A3.** A (`netstat`).
**A4.** C (Unrestricted — UDP has no flow control).
**A5.** B (Disregard the value — without the ACK flag the field is meaningless).
**A6.** E (Length — present in UDP and IP headers, not TCP).
**A7.** E (More than one statement is false — C is false because the phantom byte is *not* counted in the final ACK, and D is false because the phantom byte does *not* consist of one byte of payload data; it only consumes one sequence number).
**A8.** D (Waiting for lost traffic on the now-unused port).
**A9.** A (Acting as a server, waiting for a SYN).
**A10.** D (More than one of the above — both B and C are correct).
**A11.** A (The client initiates connection migration via Connection IDs).
**A12.** B (TCP has no NAK; the retransmission timer drives recovery).
**A13.** B (Waiting for B's window to free up).
**A14.** A (*t₀* via **0-RTT** using cached keys from a previous session).
**A15.** C (*t₂* — one full round trip after the initial *t₀* send and the *t₁* server reply).
**A16.** C (Dynamic — 55555 is in the 49152–65535 dynamic/private range).
**A17.** B (2 — a retransmission timer at the sender and an acknowledgement timer at the receiver are the minimum for any sliding-window ARQ).
**A18.** E (More than one of the above — both an address and a port on the server must be specified, and the socket must wait for connections).
**A19.** E (All of the above — Version, Source connection ID, and Destination connection ID are always present in a long QUIC header).
**A20.** D (5 — Session Layer is responsible for checkpointing).
**A21.** A (The flags differentiate SYN from ACK from SYN+ACK).

### Long-Form Answers

**A22. TCP Timers**
- a) **Retransmission timer:** A segment containing data is (re)transmitted.
- b) **Acknowledgement timer:** A segment containing an acknowledgement is transmitted.
- c) **Persistence timer:** A probe message is sent (to check whether the receiver's window has freed up).
- d) **Keepalive timer:** Connection resources are released (or a probe is sent; if no answer, resources are released).
- e) **Quiet timer:** The port is made available for a new connection (the connection in TIME-WAIT is fully torn down).

**A23. TCP Reliability — any five of:**
1. 3-way handshake to establish the connection
2. 3-way handshake to terminate the connection
3. ACK for ARQ
4. Slow start
5. Exponential back-off
6. CRC / checksum over the entire segment
7. Window advertisements (sliding-window flow control)
8. Sequence / acknowledgement numbers

**A24. TCP flow-control & sequence calculation (200-byte variant)**

| Sub-question | Answer | Reasoning |
| --- | --- | --- |
| a) Seq # of *m₁* | **300** | The next byte A is to send is byte 300, so *m₁* starts at 300. |
| b) Ack # of *m₄* | **550** | B sent 50 bytes starting at byte 500 — bytes 500–549. A acknowledges the next expected byte: 550. |
| c) Length of *m₄* | **100** | A wanted to send 200 but B's window allows only 100. So *m₁* contained 100 bytes, leaving 100 residual to be sent in *m₄*. |
| d) Window advert in *m₄* | **950** | A's window started at 1000. A received 50 bytes from B (in *m₃*) which now occupy A's buffer. A's remaining window: 1000 − 50 = 950. |
| e) Window advert in *m₅* | **0** | B's window starts at 100. After *m₁* (100 bytes), B's window is 0. B then consumes 100 (window back to 100). *m₄* delivers another 100 residual bytes, refilling the window to 0. B's *m₅* therefore advertises 0. |

**A25. TCP flow-control & sequence calculation (300-byte variant)**

| Sub-question | Answer | Reasoning |
| --- | --- | --- |
| a) Seq # of *m₁* | **300** | (Same — next byte to send is 300.) |
| b) Ack # of *m₄* | **550** | (Same — B sent 50 bytes from 500.) |
| c) Length of *m₄* | **200** | A wanted to send 300 but B's window allowed only 100 in *m₁*. Residual = 200. B consumes 200 (so B's buffer is now bigger than 100 free), allowing A to send all 200 residual bytes in *m₄*. |
| d) Window advert in *m₄* | **950** | (Same as before — A's window 1000 − 50 received = 950.) |
| e) Window advert in *m₅* | **0** | B's buffer accommodated 200 newly freed bytes plus the original 100 buffer; *m₄* delivers 200 bytes filling that space. Window back to 0. |

**A26. Definitions**
- a) **TCP slow start:** A congestion-control algorithm. The sender's congestion window `cwnd` starts at 1 segment. For each ACK received, `cwnd` increases — initially roughly exponentially — letting the sender quickly discover the network's capacity. When loss occurs, the threshold is set to `cwnd/2`, `cwnd` resets to 1, and growth restarts (linear past the threshold) — this is the slow start combined with exponential back-off.
- b) **TCP acknowledgement timer:** A timer started after data is received, that delays sending an ACK so that it can be piggybacked onto reverse traffic or aggregated with other ACKs. When it expires, an ACK segment is transmitted on its own.
- c) **Round-trip time (RTT):** The total time for a message to travel from sender to receiver *and* the corresponding ACK to return. TCP measures it (RTTm) and smooths it over time to set the retransmission timer.
- d) **Middlebox (Layer 4 context):** Network device placed between TCP endpoints — typically a firewall, NAT, or load balancer — that "digs into" TCP headers (or payloads) to make decisions. Middleboxes break the OSI layering ideal because they operate at lower layers but inspect Layer 4 information. They are the main reason TCP cannot be safely upgraded.
- e) **Protocol ossification:** The inability to modify a protocol because too many middleboxes have made assumptions about its on-the-wire form. Updating the protocol would break those middleboxes (and the connections passing through them). QUIC was designed to combat ossification by encrypting headers and randomising version numbers (QUICv2's version field is hex `6b3343cf`).

# Chapter 1: Introduction & the ISO OSI Model

> **Scope note:** This chapter covers **Semester Test 1** material only — Chapter 1 of the textbook. All seven layers are introduced here conceptually. Detailed protocol content for each layer appears in the dedicated layer notes. ST2 does **not** re-examine this chapter directly, but assumes you can identify layers by number and name.

---

## 1. History and Background

**Proprietary protocols** are protocols owned by a specific vendor. Early networks were built entirely on these, meaning all equipment had to be purchased from a single vendor — preventing interoperability between networks.

> **MCQ fact:** A proprietary network protocol is one that **is owned by a specific vendor** (not a standardised or open-source protocol).

The **Cold War** had a profound impact on the design decisions of the early Internet (ARPAnet). The driving motivation was building a decentralised, survivable network that could function even if parts were destroyed.

> **MCQ fact:** The historical event with the most profound impact on ARPAnet design decisions was the **Cold War** (not the Suez Canal Crisis, Bay of Pigs, or Lockerbie Bombing).

The **ISO OSI model** was intended to replace proprietary protocols with an open, interoperable standard. It failed in practice because the **TCP/IP protocol suite** matured and became so widely deployed first that implementing the complex OSI protocol stack was no longer practical. Today, OSI is used strictly as an educational and reference model. The language it introduced — "layer 7", "application layer" — has, however, become universal even in TCP/IP contexts.

---

## 2. Standards and Standards Bodies

| Body | Full Name | Primary Role |
| --- | --- | --- |
| **ISO** | International Standards Organisation | General international standards (NOT an acronym — from Greek *îsos* = "the same") |
| **IETF** | Internet Engineering Task Force | Internet standards; Layers 3, 4, and 7 |
| **IANA** | Internet Assigned Numbers Authority | Manages IP address blocks and port numbers |
| **ICANN** | Internet Corporation for Assigned Names and Numbers | Global Internet governance; IANA and IETF fall under it |
| **ITU-T / CCITT** | International Telecommunication Union — Telecom Sector | Telephony and telegraphy standards; CCITT is a French acronym |
| **IEEE** | Institute of Electrical and Electronics Engineers | Physical and data link layer standards (e.g., Ethernet 802.3, Wi-Fi 802.11) |
| **ZADNA** | .za Domain Name Authority | Manages the `.za` ccTLD in South Africa |
| **ZACR** | .za Central Registry | Registry operator for `.co.za` (and others) under ZADNA |
| **UniForum SA** | — | Formerly operated the `.co.za` registry |
| **AfriNIC** | African Network Information Centre | RIR for Africa; receives delegation from IANA |

> **MCQ fact:** ISO is **not** an acronym. It derives from the Greek *îsos* meaning "the same". This is why it is written as ISO in every language, not localised to each country's acronym.

> **MCQ fact (Crucial trap):** If the ISO or IEEE adopts a standard, **no country or entity has to comply with it**. Standards are **not binding**. Compliance can only be mandated by external processes (e.g., laws, market dominance).

*(Distractor: "Standards bodies enforce compliance" — wrong. Compliance is always voluntary unless mandated by law or contract.)*

### Example 1: National ISO members
South Africa → **SABS** (South African Bureau of Standards). Namibia → **NSI**. Botswana → **BOBS**.

### Example 2: Who approves new TLDs?
If a group wants to establish a new DNS top-level domain, they must apply to **ICANN**.

---

## 3. The ISO OSI Layers — Top-Down Overview

The OSI model has **seven layers**. Protocols at each layer communicate with their **peer layer** at the destination — i.e., a header added at layer *n* at node X will be **removed by layer *n* at node Z**.

As a message moves **down** the stack (towards the physical layer), headers are **added** at each layer. At the destination, headers are **removed** layer by layer as the message moves up.

> **MCQ fact:** Layers 1–4 are collectively the **network-oriented layers**. Layers 5–7 are the **application-oriented layers**.

The term **protocol stack** is used because protocols are literally **'stacked' in layers on top of one another** to separate and manage functionality.

> **MCQ fact:** "Protocol stack" describes protocols stacked in layers — **not** a push/pop data structure, and not simply because protocols converge at layer 4.

| Layer | Number | Data unit name | Example header field |
| --- | --- | --- | --- |
| Application | 7 | Request / Response | `GET` method |
| Presentation | 6 | — | `UTF-8` encoding |
| Session | 5 | — | Session ID |
| Transport | 4 | Segment | Source/Destination Port |
| Network | 3 | Datagram / Packet | Source/Destination IP Address |
| Data Link | 2 | Frame | MAC Address |
| Physical | 1 | Bit | — |

> **MCQ fact (2024 ST1 Q2):** A header field added at layer 7: `GET`. At layer 6: encoding (e.g., `UTF-8`). At layer 4: source/destination port. At layer 3: source/destination IP address. At layer 2: MAC / flag / delimiter.

### 3.1 Layer 7 — The Application Layer

The **application layer** contains protocols that directly support end-user applications. The application layer is the reason the network exists. Note carefully: the **application software** (e.g., a web browser's GUI) is not the application layer — only the network-facing protocols are.

> **MCQ fact:** The **World Wide Web (WWW)** fits on Layer 7. An example header field at Layer 7: **`GET`**.

The **dæmon** is the software on a server that continuously listens for incoming client connections. A server socket must: (i) be specified as an address and port number, (ii) **wait for connections** (not initiate them).

> **MCQ fact (2025 ST1 Q3):** A server socket **waits for connections** (option C). It must also be specified as an address and port number. The correct answer to "what does a server socket do?" is **C: Wait for connections**, not "more than one of the above" — it opens a socket that waits.

### 3.2 Layer 6 — The Presentation Layer

Positioned between the **Session and Application** layers. Deals with **data representation**: character-code translation, compression, and encryption.

> **MCQ fact:** Example header field at Layer 6: **`UTF-8`** (or any other character encoding).

> **MCQ fact (Encryption trap):** On which OSI layer should encryption be placed? **It depends on factors not mentioned in the question; all layers from 3 to 7 are options**, depending on whether link-level, transport-level, or application-level encryption is desired. *(Distractor: "Layer 6 only" — wrong.)*

In modern TCP/IP, Layer 6 functionality is typically absorbed into Layer 7 application protocols (e.g., SMTP, HTTP, FTP each define their own data representation).

> **MCQ fact (2025 ST1 Q7):** Protocols like SMTP, POP3, and FTP include Layer 7 functionality. In addition they often include functionality from **Layers 6 and 5** — because they handle their own data formatting (L6) and session management (L5).

### 3.3 Layer 5 — The Session Layer

Positioned between the **Transport and Presentation** layers. Establishes, maintains, and terminates sessions. Enforces **dialogue control** — determining which node may transmit at any given moment.

> **MCQ fact:** The OSI layer that attempts to emulate database transactions where messages can be **"rolled back"** if the final message in a sequence is not sent is **Layer 5**. *(Distractor: Layer 4 — wrong. TCP provides reliability but not transaction-style rollback.)*

> **MCQ fact (Dialogue control trap):** Which ISO OSI layer is responsible for regulating which node is allowed to transmit next in cases where two computers are **directly connected**? Answer: **It may be Layer 2 or Layer 5 depending on factors not mentioned in the question.** Layer 2 handles physical media access control; Layer 5 handles logical dialogue control.

### 3.4 Layer 4 — The Transport Layer

Provides **process-to-process** (end-to-end) communication. Uses **port numbers** to identify processes. Can be reliable (TCP) or unreliable/best-effort (UDP).

> **MCQ fact:** Example header field at Layer 4: **Source Port / Destination Port**.

> **MCQ fact:** Which data streams work better with an *unreliable* Layer 4 protocol? **Audio (and live voice/video)** — because retransmitting a late packet is worse than a momentary glitch. *(Distractors: web pages and file transfers need reliability.)*

### 3.5 Layer 3 — The Network Layer

Responsible for **routing** packets across multiple hops. Adds source and destination **IP addresses**.

> **MCQ fact (Peer trap):** Suppose Node X sends a message to Node Y. Which nodes' Layer 3 is the peer of Layer 3 at X? **All nodes on the path, including every router up to and including Y** — because every router must process the Layer 3 header to route the packet.

**Routers** are technically called **multihomed hosts** — computers with multiple network interfaces connecting different networks.

### 3.6 Layer 2 — The Data Link Layer

Gets a message from **one hop to the next** across a direct physical connection. Adds MAC addresses.

Three primary functions (highly tested):

> **MCQ fact (2023 ST1 Q4):** The three primary functions of the data link layer are:
> 1. **Media Access Control (contention control)** — determines which node transmits when multiple nodes share a medium.
> 2. **Data delineation** — marks the start and end of a frame in a continuous bit stream.
> 3. **Error control** — detects (and sometimes corrects) transmission errors via checksums.

> **MCQ fact (Layer 1 impact):** A noisy physical layer requires **error correction** at Layer 2. A good physical layer only needs **error checking** (detection) at Layer 2.

### 3.7 Layer 1 — The Physical Layer

Deals with the physical medium (copper, fibre, radio waves), bit representation, plugs, multiplexing, and signal attenuation.

---

## 4. Terminology: Packets, Frames, and Data Units

| Layer | Term used |
| --- | --- |
| Application | Request / Response |
| Transport | Segment |
| Network | Datagram or Packet |
| Data Link | Frame |
| General | Packet (layer-agnostic) |

Every data unit typically consists of a **header** (layer-specific control information) and a **payload** (data from the layer above, to be delivered to the layer above at the destination).

---

## 5. Network Architectures (Application Layer Context)

**Client-server architecture** is the dominant model. Servers listen for orders from clients. The server software is known as a **dæmon**.

> **MCQ fact:** FTP is based on the **client-server** architecture.

**Peer-to-peer (P2P):** Nodes act as equals. Classic example: **Napster**. Also: **MANETs** (mobile ad-hoc sensor networks used in disaster scenarios where there is no central server).

**N-tier (3-tier):** Data and business logic are separated from the server and client tiers. The back-end tier typically runs a database engine.

---

## Examinable Practice Questions

### Multiple Choice

**Q1.** A proprietary network protocol is a protocol that:
A. Has been standardised by some national standards body.   B. Is owned by a specific vendor.   C. Is developed as an open-source protocol.   D. Is now so old that using it has been deprecated.   E. Describes the properties of other network protocols.

**Q2.** Which historical event had a profound impact on many design decisions for the Internet (ARPAnet)?
A. Cold War   B. Suez Canal Crisis   C. Rise of the Global South   D. Bay of Pigs Invasion   E. Lockerbie Bombing

**Q3.** When writing an application that will serve as a server in a client-server architecture, the application would (in its role as server) open a socket that would:
A. Be specified as an address and port number   B. Initiate connections   C. Wait for connections   D. More than one of the above   E. All of the above

**Q4.** The phrase "protocol stack" is used in a network context because:
A. Protocols are "stacked" in layers on top of one another.   B. A message is "pushed" down and then "popped" at the receiving end.   C. Alternative protocols may exist "next to" one another within a layer.   D. Many protocols on higher layers converge to fewer protocols on lower layers.   E. The notion of a protocol stack is not used in networking.

**Q5.** The OSI layer that, amongst others, attempts to emulate database transactions where messages can be "rolled back" if the final message in a sequence is not sent, is layer:
A. 2   B. 3   C. 4   D. 5   E. 6

**Q6.** Which ISO OSI layer is responsible for regulating which node is allowed to transmit next in cases where two computers are directly connected?
A. 5   B. 4   C. 3   D. 2   E. It may be 2 or 5 depending on factors not mentioned in the question.

**Q7.** Protocols such as SMTP, POP3, and FTP are deemed to be application layer protocols. In addition, they often include functionality associated with the following ISO OSI layer(s):
A. Only layer 6   B. Layers 6 and 5   C. Layers 5 and 4   D. Layers 4 and 3   E. Only layer 3

**Q8.** If the ISO adopts a standard, countries and organisations:
A. Must comply within 2 years.   B. Must comply if they are ISO members.   C. Must comply if their national body voted for it.   D. Do not have to comply since standards are not binding.   E. Must comply with the parts relevant to their industry.

**Q9.** Which of the following correctly describes the data unit name at the transport layer?
A. Frame   B. Datagram   C. Segment   D. Request   E. Packet

**Q10.** Which layer adds the MAC address to outgoing data?
A. Layer 7   B. Layer 4   C. Layer 3   D. Layer 2   E. Layer 1

### Long-Form & Calculation

**Q11. Layer functions.** Name the three primary functions of the data link layer and briefly explain each. Then give one example of how a noisy physical layer would impact one of these functions. [4]

**Q12. Header fields per layer.** For each of layers 7, 6, 4, 3, and 2, provide one example of a header field that would be added at that layer. [5]

**Q13. Peer layers.** Suppose node X sends a message to node Z, and the message passes through routers R1 and R2 along the way. (i) Which node's Layer 7 is the peer of Layer 7 at X? (ii) Which nodes' Layer 3 is the peer of Layer 3 at X? Explain your answers. [4]

---

## Memo / Answer Key

### MCQ Answers

**A1.** B (Proprietary = owned by a specific vendor).
**A2.** A (Cold War — ARPAnet was designed to survive nuclear attack).
**A3.** C (Wait for connections; a server does not initiate). *(The socket must also be specified as address+port, but the defining action is waiting — C is the best single answer.)*
**A4.** A (Protocols are stacked in layers on top of one another).
**A5.** D (Layer 5 — the session layer provides transaction-like rollback).
**A6.** E (It may be Layer 2 for media access control, or Layer 5 for dialogue control — depends on context).
**A7.** B (Layers 6 and 5 — SMTP, POP3, FTP all include presentation and session functionality).
**A8.** D (Standards are not binding; no country must comply).
**A9.** C (Segment is the transport layer data unit).
**A10.** D (Layer 2 — the data link layer adds the MAC address).

### Long-Form Answers

**A11. Layer 2 functions.**
- a) **Media Access Control (contention control):** Determines which node may transmit when multiple nodes share a medium (e.g., Ethernet CSMA/CD).
- b) **Data delineation:** Marks the start and end of a frame in a continuous bit stream so the receiver knows where one frame ends and the next begins.
- c) **Error control:** Checksums (e.g., CRC) are added so the receiver can detect (and sometimes correct) transmission errors.
Impact of noisy Layer 1: A noisy medium requires **error correction** at Layer 2 (e.g., FEC — forward error correction), whereas a clean medium only needs **error detection** (simpler checksums, with retransmission on error).

**A12. Header fields per layer.**
- Layer 7: `GET` (HTTP method) / `EHLO` (SMTP command)
- Layer 6: `UTF-8` (character encoding) / `base64` (Content-Transfer-Encoding)
- Layer 4: Source Port / Destination Port
- Layer 3: Source IP Address / Destination IP Address
- Layer 2: Source MAC Address / Destination MAC Address

**A13. Peer layers.**
- (i) **Layer 7 peer of X:** Only node Z. Routers R1 and R2 do not process Layer 7 headers — they only process up to Layer 3 to route the packet.
- (ii) **Layer 3 peers of X:** R1, R2, and Z — every node along the path must inspect the Layer 3 (IP) header to make routing decisions, so all of them are Layer 3 peers.

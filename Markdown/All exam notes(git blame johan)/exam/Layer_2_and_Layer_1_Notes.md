> **Scope note:** These notes cover **Layer 2 (Data Link Layer)** and **Layer 1 (Physical Layer)** of the ISO OSI model, scoped strictly to what the professor indicated will be examined. Layer 2 is a **major exam focus** covering: the three primary functions (MAC/Delineation/Error Control), Ethernet (IEEE 802.3), Token Ring (IEEE 802.5), and SDLC/HDLC. Layer 1 is a **minor focus (≤5 marks)** covering only: NRZ and Manchester encoding, and the multi-mode vs single-mode fibre distinction. **Not in scope:** Hamming code, CRC calculations, Bisync (beyond brief mention), IEEE 802.4, Reed-Solomon codes, ATM, and any Layer 1 or 2 protocols not covered in lectures.

---

## 1. Layer 2: The Data Link Layer — Overview

**The Data Link Layer (Layer 2)** is responsible for getting a frame from one node to the *next hop* across a direct physical connection. Layer 3 decides where to route a packet; Layer 2 handles the single-hop delivery.

> **MCQ fact:** The data unit at Layer 2 is called a **frame**. The header field example added at Layer 2 is the **MAC address**.

> **MCQ fact:** Layer 2 does **not** absolve higher layers from error checking. Routing errors (L3), congestion failures (L4), synchronisation errors (L5), and misrepresentation errors (L6) are all invisible to Layer 2.

### 1.1 The Three Primary Functions of Layer 2

Every data link layer protocol must address exactly three core responsibilities:

| # | Function | Problem it solves |
|---|---|---|
| 1 | **Media Access Control (MAC)** | Multiple nodes may try to transmit simultaneously on a shared medium, causing collisions. |
| 2 | **Data Delineation** | A receiver listening to a continuous bit stream must be able to identify where each frame starts and ends. |
| 3 | **Error Control** | Bits may be corrupted in transit; the receiver must detect (and possibly correct) this. |

> **MCQ fact:** The three primary functions of a data link layer protocol are **media access control, data delineation, and error control**. Encoding is *not* a Layer 2 function — it belongs to Layer 1.
>
> *(Distractor: "Encoding" appears as an option in past papers — Q45 2023 paper. It is NOT a Layer 2 function.)*

> **MCQ fact (Layer 1 impact on Layer 2):** A **noisy** Layer 1 medium requires **error correction** on Layer 2 (so the receiver can fix errors without retransmission). A **good** Layer 1 medium only needs **error detection** (retransmission handles the rare error). This is the key reason error correction is preferred on wireless networks — retransmission overhead on a noisy wireless link is prohibitive.

> **Exam Q:** Why would you prefer error *correction* over error *detection* on a wireless network?
> **Answer:** Wireless links experience far higher noise and interference than wired links. With error *detection* only, every corrupted frame must be retransmitted, consuming significant bandwidth and adding latency on a medium that is already error-prone. Error *correction* (e.g. forward error correction) allows the receiver to reconstruct the original data without retransmission, making communication far more efficient on a noisy medium.

---

## 2. Layer 2: Media Access Control

**Media Access Control (MAC)** solves the problem of determining which node may transmit at any given moment. Three broad approaches exist.

### 2.1 Master/Slave Protocols (Polling)

In a **master/slave protocol**, one node (the master) controls medium access. The master **polls** each slave in turn to ask whether it has data to send.

> **MCQ fact:** When one node polls another, it wants to know whether **the other node has something to send**.
>
> *(Distractor: "whether the other node is communicating" — wrong. Polling is specifically about data availability.)*

- Used in point-to-point and multipoint configurations.
- Simple to implement; works well with dumb terminals.
- Downside: poll messages waste bandwidth; master is a single point of failure; slaves must wait to be polled even when they have urgent data.
- **SDLC** (when used in multipoint mode) is the canonical example.

### 2.2 Token Passing

In a **token passing** protocol, all nodes are equals. A special bit pattern called a **token** circulates on the network. A node may only transmit when it holds the token. After transmitting (or if it has nothing to send), it passes the token to the next node.

> **MCQ fact:** In token ring (IEEE 802.5), the node with the **largest MAC address** wins the bully algorithm election to become active monitor.

#### Active Monitor (IEEE 802.5 / Token Ring)

Token ring requires an **active monitor** — one designated node that:
- Monitors the ring to ensure the token circulates regularly.
- Generates a new token if the existing token is lost (e.g. due to electrical interference or a node being switched off).
- Periodically broadcasts an *"active monitor present"* message so all nodes know it is alive.

**Election (Bully Algorithm) — triggered when no "active monitor present" is seen for too long:**

| Phase | Action |
|---|---|
| **Phase 1** | Any node that notices the monitor is gone forwards a call for election to its neighbour. |
| **Phase 2** | A frame carrying the highest MAC address seen so far is passed around the ring. Each node inserts its own address if it is larger. The node whose address returns unchanged is the winner. |
| **Phase 3** | The winner broadcasts a victory message; it becomes the new active monitor. |

> **MCQ fact:** When no monitor presence is detected on an 802.5 network, **a new monitor is elected by the remaining nodes** using the bully algorithm.
>
> *(Past paper Q46: Answer D — "A new monitor is elected by the remaining nodes.")*

*Example 1:* Four nodes A (`00:AA`), B (`00:BB`), C (`00:CC`), D (`00:FF`). D has the highest MAC address. When the monitor fails, phase 2 passes a frame around. D will replace the address in the frame with its own (`00:FF`). When `00:FF` returns to D, D knows it has the largest address and declares victory.

*Example 2 (token passing acknowledgement):* In IEEE 802.5, when data travels around the ring past the intended recipient, the recipient sets the **"Address Recognised"** bits. If it can copy the frame into its buffers, it also sets the **"Frame Copied"** bits. When the frame returns to the sender, the sender can determine whether delivery was successful.

### 2.3 Multiple Access: CSMA and CSMA/CD

**Multiple Access (MA):** any node may transmit whenever it wants. Works on quiet networks; degrades under heavy load due to collisions.

**CSMA (Carrier Sense Multiple Access):** a node *senses* whether the medium is busy before transmitting. Reduces (but does not eliminate) collisions.

- **1-persistent CSMA:** wait until medium is idle, then transmit immediately → near-certain collision if two nodes were waiting simultaneously.
- **Non-persistent CSMA:** if medium is busy, wait a *random* time before trying again.
- **p-persistent CSMA:** if medium is idle, transmit with probability *p*, else wait → balances utilisation and collision probability.

> **MCQ fact:** **Ethernet** uses **CSMA/CD** (Carrier Sense Multiple Access with **Collision Detection**). The corresponding IEEE standard is **IEEE 802.3**.

**CSMA/CD:** nodes keep listening while transmitting. If a collision is detected:
1. All involved nodes abort transmission.
2. A **jamming signal** is broadcast so all nodes detect the collision.
3. Nodes retry after a random back-off.

**Hidden node problem (wireless):** Node A and C cannot hear each other but both can hear B. CSMA is not viable here because A cannot detect C's transmission. Solution: **CSMA/CA** (Collision Avoidance) — used by IEEE 802.11 (WiFi).

---

## 3. Layer 2: Data Delineation

**Data delineation** is the process of marking the start and end of a frame in the continuous bit stream arriving at a node.

The core challenge is the **transparency problem**: any framing character or pattern chosen may naturally appear in the data, causing the receiver to prematurely terminate the frame.

Three techniques exist:

| Technique | Used by | Mechanism |
|---|---|---|
| Special characters (byte stuffing) | Bisync | DLE-STX and DLE-ETX; DLE escaped by inserting another DLE |
| Special bit pattern (bit stuffing) | SDLC, HDLC | Flag `01111110`; stuff a `0` after every five consecutive `1`s in the data |
| Known/fixed field lengths | Ethernet (IEEE 802.3) | Length field explicitly states payload size; no framing characters needed |
| Non-bit patterns | IEEE 802.5 Token Ring | Non-data symbols J and K (code violations in Manchester encoding) used as delimiters |

> **MCQ fact:** **HDLC accomplishes transparency by using bit stuffing** (for SDLC/HDLC). Knowledge field lengths are also used (for byte-oriented protocols like Ethernet).
>
> *(Past paper Q43: Answer A — "Bit stuffing")*

> **MCQ fact:** **Data delineation** refers to **marking the boundaries of a frame** in a continuous stream.
>
> *(Past paper Q48: Answer B.)*

### 3.1 Bit Stuffing (SDLC/HDLC)

The SDLC flag is `01111110`. To ensure this pattern cannot appear in data, the sender **stuffs** an extra `0` bit after every run of five consecutive `1`s in the data.

*Example 1:* Transmit data `01111110`.

The sender inspects the raw data and sees five consecutive `1`s followed by a `1` (would produce a flag). A `0` is inserted after the fifth `1`:

```
Original data:  0 1 1 1 1 1 1 0
After stuffing: 0 1 1 1 1 1 0 1 0
```

The transmitted frame on the wire (including framing flags) is:
`01111110` + stuffed data + `01111110`

> **MCQ fact (bit stuffing worked example):** If SDLC transmits data `01111110`, the bits observed on the wire (data portion only) are **`011111010`** — a `0` is inserted after the five `1`s.
>
> *(Past paper Q50: Answer B — `011111010`)*

*Example 2:* Receiver algorithm for SDLC:
```
ones = 0
receive 01111110       // start flag
while true:
    b = nextBit()
    if b == 1:
        ones++
        append b to received data
    if b == 0:
        if ones < 5:  append 0 to received data
        if ones == 5: discard (stuffed bit)
        if ones == 6: terminate (end flag found)
        if ones > 6:  abort
        ones = 0
```

### 3.2 IEEE 802.5 Token Ring: Non-bit Pattern Delineation

Manchester coding ensures every bit contains a **mid-bit voltage transition**. A high-high or low-low (which cannot represent a valid bit) is a **code violation**. IEEE 802.5 calls these **non-data J** and **non-data K** symbols.

- **Starting delimiter:** `JK0JK000`
- **Ending delimiter:** `JK1JK1xx`

Since J and K cannot appear in data (data only contains `0`s and `1`s), these delimiters are unambiguous — no stuffing is needed.

---

## 4. Layer 2: Error Control

**Error control** at Layer 2 determines whether bits arrived exactly as transmitted, and optionally corrects errors.

> **Lecture note:** **Do not study Hamming code or CRC calculations** — these are explicitly out of scope per the professor.

### 4.1 Error Detection vs Error Correction

| Category | Technique | Mechanism |
|---|---|---|
| Detection only | Parity | One extra bit forces total 1-count to odd or even |
| Detection only | Checksum | Modular sum of all transmitted values |
| Detection only | CRC | Polynomial division remainder *(theory only; calculations out of scope)* |
| Correction | *n*-modular redundancy | Transmit data *n* times; majority vote selects correct value |
| Correction | Hamming code | *(out of scope)* |

> **MCQ fact:** **Parity** only detects errors that change an **odd** number of bits. It detects approximately **50%** of burst errors (which randomly affect an even or odd number of bits).

> **MCQ fact:** **Checksums** are weak: if all data is forced to `0` by a broken wire, the checksum is also `0` — the error is undetected.

> **MCQ fact:** The key distinction for the exam is: use **error correction** on noisy/wireless media (to avoid retransmission overhead); use **error detection** (with retransmission via ARQ) on reliable wired media.

### 4.2 Error Correction: *n*-Modular Redundancy

The same data is transmitted *n* times. The receiver takes the majority value across all copies as the correct data.

*Example 1 (triple modular redundancy, n=3):* To send bit `1`, transmit `111`. If one bit flips to `0` due to noise, the receiver receives `101` or `110` — the majority is still `1`, so the error is corrected.

*Example 2 (realistic scenario):* A stockbroker receives three copies of a trade instruction. Two say "Buy ZAR 1,000,000 shares" and one says "Buy ZAR 1,900,000 shares." The majority message is used.

> **MCQ fact:** *n*-modular redundancy overhead for a message of size *s* is **(n−1) × s**.

---

## 5. Layer 2: Other Functions

### 5.1 The MAC and LLC Sublayers

Layer 2 is often subdivided into two sublayers (used in IEEE standards):

| Sublayer | Name | Role |
|---|---|---|
| Upper | **LLC (Logical Link Control)** — IEEE 802.2 | Medium-independent aspects: identifies Layer 3 protocol via **DSAP/SSAP** fields |
| Lower | **MAC (Media Access Control)** | Medium-dependent aspects: physical medium access and frame delineation |

> **MCQ fact:** The LLC packet format contains: `DSAP | SSAP | Control | Info`. DSAP and SSAP identify the Layer 3 protocols at destination and source respectively — analogous to port numbers for TCP.

### 5.2 Flow Control at Layer 2

- **SDLC/HDLC:** Uses the **RNR (Receiver Not Ready)** S-frame to tell the sender to pause. Must be repeated to keep the sender paused.
- **Bisync:** Uses a **WACK (Wait-before-transmit Acknowledgement)** — acknowledges received data but tells the sender to wait.
- Most modern Layer 2 protocols rely on **Layer 4** for flow control.

### 5.3 Connection-Oriented Services (SDLC/HDLC)

While most Layer 2 protocols are connectionless, SDLC and HDLC provide connection-oriented services with numbered frames and acknowledgements.

> **MCQ fact:** SDLC is a **go-back-N ARQ** protocol. HDLC adds **SREJ (Selective REJect)** making it a **selective repeat ARQ** protocol.

**SDLC/HDLC frame types:**

| Frame type | Purpose | Distinguishing bits (low 2 bits of control) |
|---|---|---|
| **I-frame** (Information) | Carries data; contains N(S) and N(R) | Bit 0 = `0` |
| **S-frame** (Supervisory) | Flow/error control; contains N(R) only | Bits 1:0 = `01` |
| **U-frame** (Unnumbered) | Commands (connect, disconnect, mode change) | Bits 1:0 = `11` |

**S-frame types:**

| S-frame | Meaning |
|---|---|
| **RR** (Receiver Ready) | Acknowledge frames up to N(R)−1; ready for more |
| **RNR** (Receiver Not Ready) | Acknowledge up to N(R)−1; pause sending |
| **REJ** (Reject) | Go-back-N reject; resend from N(R) onwards |
| **SREJ** (Selective Reject) | Reject only frame N(R); HDLC only |

> **MCQ fact:** With a 3-bit N(S)/N(R) field, SDLC allows at most **7** unacknowledged frames (frame numbers 0–7; maximum 7 outstanding). HDLC with a 16-bit control field expands this to **127** unacknowledged frames.

*Example 1 (SDLC acknowledgement):* Node A sends frames 0–5. B replies with N(R)=6, meaning B has received all frames and expects frame 6 next. A then sends frames 6, 7, 0. B sends N(R)=1, acknowledging all three.

*Example 2 (why max 7 unacknowledged):* If C sends 8 frames (0–7) and D sends N(R)=0, it is impossible to tell whether D expects frame 8 (now renumbered 0) or never received the original frame 0. Hence the rule: no more than 7 unacknowledged frames at any time.

---

## 6. Layer 2: Protocol Reference Table

| Protocol | Standard | Orientation | MAC technique | Delineation | Key facts |
|---|---|---|---|---|---|
| **Ethernet** | IEEE 802.3 | Byte | CSMA/CD | Fixed field lengths (preamble + length field) | MTU 1500 bytes; most widely used; DIX Ethernet uses Ethertype |
| **Token Ring** | IEEE 802.5 | Byte | Token passing | Non-bit patterns (J/K delimiters) | Active monitor; bully election; Address Recognised / Frame Copied bits |
| **SDLC** | IBM | Bit | Master/slave or balanced | Bit stuffing (flag `01111110`) | Go-back-N ARQ; 3-bit N(S)/N(R); used in WANs |
| **HDLC** | ISO | Bit | Master/slave or balanced | Bit stuffing (flag `01111110`) | Adds SREJ (selective repeat); 16-bit control field option |
| **Bisync** | IBM | Character (ASCII) | Master/slave | Byte stuffing (DLE) | Historical; stop-and-wait; ACK0/ACK1 |
| **IEEE 802.11** | IEEE | Byte | CSMA/CA | Fixed field lengths | WiFi; addresses hidden node problem; includes 802.11a/b/g/n/ac/ax |

> **MCQ fact:** **IEEE 802.3** standardises **Ethernet** (not LLC, not HDLC, not Token Ring).
>
> *(Past paper Q42: Answer A — "Ethernet")*

> **MCQ fact:** **IEEE 802.11** standardises **Wireless LANs** (WiFi).
>
> *(Past paper Q47: Answer E — "Wireless LANs")*

### 6.1 Ethernet (IEEE 802.3) Frame Structure

```
+----------+---------+------+------+--------+-----------+--------+----------+
| Preamble | SFD     | Dst  | Src  | Length | Data      | Pad    | CRC      |
| 7 octets | 1 octet | 6 B  | 6 B  | 2 B    | 46–1500 B | varies | 4 octets |
+----------+---------+------+------+--------+-----------+--------+----------+
```

- **Preamble:** `10101010...10` (7 octets) — allows receivers to synchronise clock.
- **SFD (Start Frame Delimiter):** `10101011` — marks frame start.
- **Length:** number of bytes in the data field (46–1500). Values ≥ 1536 indicate Ethernet II (Ethertype field).
- **Data:** minimum 46 octets (ensures sender is still transmitting if collision occurs at far end of network).
- **CRC:** 4-octet CRC for error detection.
- **Interframe gap:** 12 octets (96 bits) must be idle between frames.

> **MCQ fact:** Ethernet's **MTU is 1500 octets**. The minimum data field is **46 octets**.

> **MCQ fact (Ethernet II vs IEEE 802.3 harmonisation):** Values 46–1500 in the Length/Type field → **IEEE 802.3** (length). Values ≥ 1536 → **Ethernet II** (Ethertype — identifies the Layer 3 protocol).

> **MCQ fact:** **Jumbo frames** (MTU ≈ 9000 octets) are supported by gigabit and 10-gigabit Ethernet variants.

---

## 7. Layer 1: The Physical Layer — Overview

> **Lecture note:** Layer 1 is worth **at most 5 marks**. Only study what was covered in class: NRZ encoding, Manchester encoding, and multi-mode vs single-mode fibre.

**The Physical Layer (Layer 1)** deals with the actual physical transmission of bits between two directly connected nodes. It covers: transmission media, bit representation (line coding and modulation), physical topology, plugs, multiplexing, signal attenuation, and interference.

> **MCQ fact:** Layer 1 concerns itself with media (copper, fibre, radio), bit representation, plug types, topology, and signal attenuation — **not** with error checking or addressing (those belong to Layer 2).

---

## 8. Layer 1: Line Coding (Data Representation on Digital Media)

**Line coding** is the process of mapping logical bit values (`0` and `1`) onto voltage states on a digital medium.

### 8.1 NRZ (Non-Return-to-Zero)

**NRZ (Non-Return-to-Zero)** encodes a `1` as a high voltage and a `0` as a low voltage for the entire bit interval. The signal does not return to zero between bits.

```
Bit:    : 1 : 0 : 1 : 1 :
        :   ___   :   :___:___:
Signal: :  |   |  :   |       |
        :__|   |__|   |       |
```

- Simple and efficient.
- Problem: a long run of identical bits makes it difficult for the receiver to synchronise its clock (no transitions to lock on to).

> **MCQ fact:** **NRZ** does not guarantee a mid-bit transition. Long runs of `0`s or `1`s can cause clock synchronisation problems at the receiver.

### 8.2 Manchester Encoding

**Manchester encoding** guarantees a **mid-bit voltage transition** in every bit interval. Per IEEE 802.3 convention:
- **`1`** = low-to-high transition in the middle of the bit interval.
- **`0`** = high-to-low transition in the middle of the bit interval.

```
Bit:    : 1 : 0 : 1 : 1 :
        :_: :   :_: :_: :
        : |:| : : |:|:|: :
        :  |_|___| : |_|  :
```

*(Textbook convention per IEEE 802.3: `1` = rising transition at midpoint)*

- Advantage: guaranteed clock synchronisation (receiver always has a transition to lock on to).
- Disadvantage: requires **double the bandwidth** of NRZ (signal transitions at twice the bit rate).
- Used by: **Ethernet (IEEE 802.3)** and the **non-bit patterns** used by Token Ring (IEEE 802.5) for delineation.

> **MCQ fact:** Manchester encoding **always** produces a transition in the **middle** of each bit interval. This is what makes **non-data J and K code violations** possible — a high-high or low-low has *no* mid-bit transition and therefore cannot be a valid data bit.

### 8.3 Differential Manchester Encoding

**Differential Manchester encoding** also guarantees a mid-bit transition, but encodes information via whether a transition occurs at the *start* of the bit interval:
- **`1`** = no transition at start of interval (but transition at midpoint still occurs).
- **`0`** = transition at start of interval (plus transition at midpoint).

```
Bit:    : 1 : 0 : 1 : 1 :
(one representation)
        : _:_ :_ : _:_ :
        :| | | | |   | | :
        :|_| |_|_|   |_| :
```

- Used by: **Token Ring (IEEE 802.5)**.

*Example 1 (NRZ vs Manchester):* Transmit `1 0 1 1`. In NRZ the signal is high-low-high-high with no guaranteed midpoint transitions. In Manchester (802.3 convention), each bit has a definite rising or falling transition at its midpoint, making clock recovery trivial.

*Example 2 (why Manchester enables J/K):* In Manchester encoding, every valid bit contains exactly one mid-bit transition. A signal segment with **two transitions in the same direction** (e.g., high-high) is physically representable but is a **code violation** (non-data J or K). IEEE 802.5 uses these as unambiguous frame delimiters.

---

## 9. Layer 1: Transmission Media

### 9.1 Guided (Conducted) Media

| Medium | Notes |
|---|---|
| Copper wire pairs | Standard Ethernet cabling; RJ-45 connector |
| Coaxial cable | Older Ethernet (10Base5); BNC or vampire tap connectors |
| Optical fibre | High bandwidth; immune to electromagnetic interference |

### 9.2 Optical Fibre: Multi-mode vs Single-mode

> **Lecture note:** Know the distinction between multi-mode and single-mode fibre — this is explicitly in scope.

| Property | **Multi-mode fibre** | **Single-mode fibre** |
|---|---|---|
| Core diameter | Larger (≈50–62.5 µm) | Smaller (≈8–10 µm) |
| Light paths | Multiple light rays travel different paths (modes) | Only one light mode travels through |
| Dispersion | Higher (modes arrive at slightly different times → pulse spreading) | Very low |
| Transmission distance | Shorter (suitable for LAN / building) | Longer (suitable for WAN / metropolitan) |
| Cost | Cheaper (LED light source, lower-precision connectors) | More expensive (laser light source) |
| Typical use | Data centres, short campus links | Long-distance carrier links, undersea cables |

> **MCQ fact:** **Single-mode fibre** supports longer distances than multi-mode fibre because only one light mode travels through it, eliminating modal dispersion.

> **MCQ fact:** **Multi-mode fibre** uses a larger core and is cheaper, but suffers from **modal dispersion** — different rays take different paths and arrive at slightly different times, limiting distance.

---

## 10. Layer 1: Topology

| Topology | Description | Example |
|---|---|---|
| **Bus** | All nodes share a single cable; broadcast medium | Original Ethernet (coax) |
| **Ring** | Nodes connected in a closed loop; data travels one direction | Token Ring (IEEE 802.5) |
| **Point-to-point** | Direct link between exactly two nodes | SDLC/HDLC WAN links |
| **Multipoint** | One link shared by multiple nodes | Master/slave SDLC |
| **Mesh** | Every node connected to every other node | Internet backbone |

---

## Examinable Practice Questions

### Multiple Choice

**Q1.** Which of the following is *not* a function of the data link control layer?
A. Data delineation   B. Error control   C. Encoding   D. Media access control   E. None of the above

**Q2.** Which ISO OSI layer is responsible for regulating which node is allowed to transmit next in cases where two computers are directly connected?
A. 5   B. 4   C. 3   D. 2   E. It may be 2 or 5 depending on factors not mentioned in the question.

**Q3.** What does *data delineation* refer to on Layer 2?
A. Limiting the size of Layer 2 frames.   B. Marking the boundaries of a frame.   C. Picking a data code for data representation.   D. Controlling access to a shared medium.   E. Encoding data in a form that can be transmitted via Layer 1.

**Q4.** HDLC accomplishes transparency by using:
A. Bit stuffing   B. Byte stuffing   C. Known field lengths   D. More than one of the above   E. None of the above

**Q5.** Suppose a node using SDLC has to transmit the data `01111110`. The data will be observed on the line as:
A. `011111010`   B. `011111110`   C. `011111100`   D. `011111110`   E. `011111X10`

**Q6.** When no monitor presence is detected on an 802.5 network:
A. The hub appoints a new monitor.   B. The previous monitor resumes its duties.   C. The station with the highest priority starts acting as monitor.   D. A new monitor is elected by the remaining nodes.   E. The network simply continues operating because it does not really need a monitor.

**Q7.** IEEE 802.3 defines:
A. Ethernet   B. LLC   C. HDLC   D. Token ring   E. More than one of the above

**Q8.** IEEE 802.11 standardises:
A. Ethernet   B. Token bus   C. Token ring   D. Security   E. Wireless LANs

**Q9.** A master-slave protocol may solve the following problem on Layer 2:
A. Media access control   B. Error control   C. Routing   D. Polling   E. None of the above

**Q10.** Manchester encoding, compared to NRZ, requires:
A. Half the bandwidth   B. The same bandwidth   C. Double the bandwidth   D. Triple the bandwidth   E. This cannot be determined without knowing the bit rate.

**Q11.** Which type of optical fibre supports the longest transmission distances?
A. Multi-mode step-index   B. Multi-mode graded-index   C. Single-mode   D. Both A and B   E. Both B and C

**Q12.** In SDLC, the maximum number of unacknowledged frames at any time (with 3-bit sequence numbers) is:
A. 4   B. 6   C. 7   D. 8   E. 15

**Q13.** Why is error *correction* preferred over error *detection* on wireless networks?
A. Wireless hardware cannot implement retransmission.   B. Retransmission overhead is too high on noisy wireless links.   C. Wireless frames are too short for ARQ.   D. Error detection codes do not work on wireless media.   E. Wireless networks always use Layer 5 for error control.

**Q14.** The starting delimiter of an IEEE 802.5 frame is `JK0JK000`. What are J and K?
A. Special flag characters borrowed from ASCII.   B. Code violations (non-bit patterns) that cannot occur in valid data.   C. Bit-stuffed sequences inserted by the sender.   D. Hexadecimal values representing frame boundaries.   E. None of the above.

---

### Long-Form & Calculation

**Q15. Layer 2 functions.** Describe the three primary functions of a data link layer protocol. For each function, explain *why* it is necessary and give one concrete example of a technique used to implement it. [6]

**Q16. Error detection vs correction.** Explain the difference between error *detection* and error *correction* at Layer 2. Why would a network engineer choose error correction over error detection on a wireless network? [4]

**Q17. Token ring election.** Describe the bully algorithm used to elect a new active monitor in an IEEE 802.5 token ring network. What triggers an election, and how is the winner determined? [5]

**Q18. Bit stuffing.** Explain the transparency problem in data link layer protocols. How does SDLC solve this problem using bit stuffing? Show the bits transmitted on the wire when the data payload `0111111110` is to be sent (exclude framing flags). [5]

**Q19. Manchester vs NRZ.** Explain the difference between NRZ and Manchester encoding. Draw the signal for the bit sequence `1 0 1 0` using both schemes (using the IEEE 802.3 Manchester convention). State one advantage and one disadvantage of Manchester encoding relative to NRZ. [5]

---

## Memo / Answer Key

### MCQ Answers

**A1.** C (Encoding is a Layer 1 function, not Layer 2.)

**A2.** E (It may be Layer 2 for media access control OR Layer 5 for dialogue control, depending on context. Neither option alone is always correct.)

**A3.** B (Delineation = marking frame boundaries in the bit stream.)

**A4.** A (HDLC/SDLC are bit-oriented and use bit stuffing. Ethernet uses known field lengths, but HDLC specifically uses bit stuffing. *(If the question said "HDLC or Ethernet", answer would be D.* For HDLC alone: A.)

**A5.** A (`011111010` — a `0` is inserted after the five consecutive `1`s.)

**A6.** D (The bully algorithm elects a new monitor from the remaining nodes.)

**A7.** A (IEEE 802.3 = Ethernet.)

**A8.** E (IEEE 802.11 = Wireless LANs / WiFi.)

**A9.** A (Master/slave solves the media access control problem by having the master decide who transmits.)

**A10.** C (Each Manchester bit contains two half-intervals with opposite states, requiring double the signal transitions — hence double the bandwidth of NRZ.)

**A11.** C (Single-mode fibre eliminates modal dispersion, enabling much longer distances.)

**A12.** C (With 3-bit sequence numbers, frames are numbered 0–7; the maximum unacknowledged is 2³ − 1 = **7**.)

**A13.** B (Retransmission on a noisy link wastes bandwidth and adds latency; correction avoids retransmission entirely.)

**A14.** B (J and K are code violations — signals that cannot represent a valid Manchester-encoded bit — so they are unambiguous as delimiters.)

---

### Long-Form Answers

**A15. Layer 2 functions**
- a) **Media Access Control:** Solves the problem of multiple nodes attempting to transmit simultaneously on a shared medium, causing collisions. *Technique:* CSMA/CD (used by Ethernet) — nodes sense the medium before transmitting and detect collisions during transmission.
- b) **Data Delineation:** Solves the problem of identifying where a frame starts and ends in a continuous bit stream. *Technique:* Bit stuffing in SDLC — the flag `01111110` marks frame boundaries; a `0` is inserted after every five consecutive `1`s in the data to prevent the flag pattern appearing in the payload.
- c) **Error Control:** Detects (and optionally corrects) transmission errors caused by noise on the medium. *Technique:* CRC — a polynomial remainder is calculated over the data and appended; the receiver recalculates and verifies the remainder.

**A16. Error detection vs correction**
- **Error detection** adds a check value (e.g. parity, checksum, CRC) that allows the receiver to determine whether data was corrupted. If corruption is detected, the frame is discarded and the sender is asked to retransmit (via ARQ).
- **Error correction** adds enough redundancy (e.g. forward error correction codes) that the receiver can reconstruct the original data *without* retransmission.
- On a wireless network, the physical medium is inherently noisy (susceptible to interference, fading, obstacles). Error rates are much higher than on wired links. Every retransmission consumes scarce wireless bandwidth and adds latency. Using error correction avoids the retransmission cost entirely, making communication more efficient and reliable.

**A17. Token ring bully election**
- An election is triggered when any node does not see an *"active monitor present"* message from the current monitor for a predetermined period.
- **Phase 1:** The node that notices the absence forwards an election call to its neighbour. If a node receives a call it has not already forwarded, it passes it on; otherwise it ignores it. This ensures all nodes know an election is in progress.
- **Phase 2:** An election frame (carrying the highest MAC address seen so far) circulates the ring. Each node compares the address in the frame to its own MAC address. If its address is larger, it replaces the frame with its own address; otherwise it forwards the frame unchanged. When a node's own address returns to it, that node has the largest MAC address on the ring — it is the winner.
- **Phase 3:** The winner broadcasts a victory message around the ring and takes over as active monitor. All other nodes acknowledge and resume normal operation.
- Winner criterion: the node with the **largest MAC address**.

**A18. Bit stuffing**
- **Transparency problem:** Any framing pattern used to mark the start/end of a frame may naturally appear in the data, causing the receiver to misinterpret it as a frame boundary. The protocol must ensure this cannot happen.
- **SDLC solution:** The flag `01111110` delimits frames. Whenever the sender detects five consecutive `1`s in the data (whether or not followed by `10`), it inserts a `0` after the fifth `1`. The receiver reverses this: five `1`s followed by `0` → discard the stuffed `0`; five `1`s followed by `1` → this is a flag (or abort if more than six `1`s follow).
- **Worked example** for data `0111111110`:
  - Scan left-to-right: after five `1`s (`01111 1`), insert `0`: → `011111 0`
  - Continue with remaining `110`: no five consecutive `1`s remain.
  - Transmitted payload (on the wire, before and after the flags): **`01111101 10`**
  
  *(Verification: receiver sees `011111` → drops stuffed `0`, reconstructs original `01111111 10`.)*

**A19. Manchester vs NRZ**

NRZ for `1 0 1 0` (high = `1`, low = `0`):
```
: 1 : 0 : 1 : 0 :
:___:   :___:   :
:   |___|   |___|
```

Manchester (IEEE 802.3) for `1 0 1 0` (1 = low→high at midpoint; 0 = high→low at midpoint):
```
: 1  : 0  : 1  : 0  :
:_   :  _ :_   :  _ :
: |→ |↓  |: |→ |↓   :
:|   |___|:|   |___| :
```
*(Each bit: first half low then high for `1`; first half high then low for `0`, with transition at midpoint)*

- **Advantage of Manchester:** Guaranteed mid-bit transition in every bit interval allows the receiver to continuously synchronise its clock to the sender, eliminating clock drift.
- **Disadvantage of Manchester:** Requires double the signal bandwidth of NRZ (two signal states per bit interval instead of one), making it less bandwidth-efficient.

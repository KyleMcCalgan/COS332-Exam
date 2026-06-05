# Layer 3: The Network Layer

> **Scope note:** The lecturer's announcement states: _"Layer 3: Hopefully everything, but, at least up to the end of IPv4."_ and _"IPv6 will also be included."_ ATM and the non-TCP/IP protocols are explicitly **out of scope**. The protocols in scope are **IP (v4 and v6), ICMP, and ARP**. Routing algorithms (Dijkstra, Bellman-Ford, RIP, OSPF, BGP) and addressing (subnetting, CIDR, supernetting, NAT) are core.

---

## 1. Core Function & Characteristics

The Layer 3 (Network Layer) routes **packets** (called **datagrams**) from a source node to a destination node.

- **Dominant protocol:** the **Internet Protocol (IP)** — primarily **IPv4**, increasingly **IPv6**.
- **Service type:** IP provides an **unreliable, connectionless, "best-effort"** service. It does **not** guarantee delivery. Reliability — if needed — is added by Layer 4 (TCP, QUIC). UDP at Layer 4 adds only port-based process targeting, no reliability.

---

## 2. The IP Routing Algorithm

When a router receives a datagram, it follows this algorithm to decide what to do:

```
On receipt of datagram d destined for node B:
1. Is B on the same network as us (direct neighbour)?
       YES → use Layer 2 to deliver d directly. STOP.
       NO  → continue.
2. Is there a routing-table entry whose destination network matches B?
       YES → forward d to the "next hop" given by that entry. STOP.
       NO  → continue.
3. Is a default gateway configured?
       YES → forward d to the default gateway. STOP.
       NO  → continue.
4. Discard d (and optionally send an ICMP Destination Unreachable to the source).
```

> **MCQ fact:** "It has reached the point where it either consulted the routing table and found no match, or noted that no routing table exists. What is the next step?" **A: Check whether a default gateway is defined and, if one is defined, forward the packet to such a default gateway.** ✓

### Formal version (with AND notation)

The textbook also expresses step 2 mathematically. Given a datagram with destination address D, and a routing-table entry with network address N and netmask m, D belongs to N if `D & m = N & m` (bitwise AND). The router scans its table for matching entries and picks the one with the **longest prefix** (most specific match).

### Routing-table entries

Routing tables store triples of the form `(destination network, next hop, interface)`:

- **Destination** — the network (in CIDR notation) of where the route leads.
- **Next hop** — the IP address of the next router (or `0.0.0.0` as a placeholder when the destination is directly connected — meaning "send it straight out on this interface").
- **Interface** — the local NIC through which the packet should be sent.

#### Reading a real routing table (netstat -r)

The `netstat -r` command (Linux) or `route print` (Windows) displays the current routing table. A typical Linux output:

```
Destination     Gateway         Genmask         Flags Metric Iface
10.11.12.13     0.0.0.0         255.255.255.255 UH    0      ppp0
192.168.1.0     192.168.2.11    255.255.255.0   UG    1      br0
192.168.2.0     0.0.0.0         255.255.255.0   U     0      br0
0.0.0.0         100.127.127.113 0.0.0.0         UG    1      br0
```

- `0.0.0.0` in the Gateway column means "no next hop — deliver directly on this interface."
- `0.0.0.0/0` in the Destination column is the default route.
- Flags: `U` = route is up; `G` = uses a gateway (next hop); `H` = host route (/32).

> **Layer 3 commands:** `netstat -r` prints the routing table; `arp -a` shows the ARP cache; `ifconfig`/`ipconfig` shows interface addresses; `ping` sends ICMP Echo Requests; `traceroute`/`tracert` uses TTL manipulation (see §8.1).

### Worked example 1 — longest-prefix match (final-exam style)

An IP datagram addressed to **10.10.1.2** arrives at node R. R is not directly connected to the destination. Routing table at R:

```
10.10.10.0/24    192.168.1.1   eth1
10.10.0.0/16     192.168.2.2   eth2
10.0.0.0/8       192.168.3.3   eth3
0.0.0.0/0        192.168.4.4   eth4
```

**To which next hop is the datagram forwarded?**

10.10.1.2 matches:

- 10.10.10.0/24? — No (.10.1 ≠ .10.10)
- 10.10.0.0/16? — Yes (first 16 bits match)
- 10.0.0.0/8? — Yes (less specific)
- 0.0.0.0/0? — Yes (default)

The router picks the **longest-prefix match** = /16 → **192.168.2.2 (eth2)**. ✓

### Worked example 2 — sending to a network address

An IP datagram is sent to **8.0.0.0** (a network address, not a host). The routing algorithm forwards it normally. When it reaches the final router responsible for the 8.0.0.0/8 block, that router finds no host with address zero (all-zero host bits = the network itself, not a host). It discards the datagram.

> **MCQ fact (final-exam Q40 style):** "One sends an IP datagram to a network address such as 8.0.0.0. What should happen?" → **C: The datagram should arrive at the final router. However, that router will not be able to find a host 0, and will therefore discard the datagram.**

---

## 3. Routing Protocols

Routers don't just guess routes — they exchange them via **routing protocols**, classified by where they run.

### 3.1 Interior Gateway Protocols (IGPs) — _within_ an autonomous system

An **autonomous system (AS)** is a collection of networks under one administrative authority (e.g. one ISP, or one university). IGPs are used _inside_ an AS.

|IGP|Algorithm|Metric|What is exchanged|
|---|---|---|---|
|**OSPF** (Open Shortest Path First)|**Dijkstra**|Cost|Routers broadcast their **version of the network topology**|
|**RIP** (Routing Information Protocol)|**Bellman-Ford**|**Hop count**|Routers exchange their **routing tables**|

> **MCQ fact:** "Routers using OSPF broadcast their ... and use the received information to apply the ... algorithm." → **Version of the network topology; Dijkstra.** ✓ "The primary metric used by interior gateway protocols is" → **Hop count** (specifically the metric RIP uses).

**Why OSPF uses Dijkstra:** Every router broadcasts its local view of the network topology to all other routers. Each router then builds a complete map and runs Dijkstra locally to compute shortest paths. Because every router has the same map, paths are consistent.

**Why RIP uses Bellman-Ford:** Routers only share their routing _tables_ (not the full topology) with direct neighbours. Each router computes distance estimates incrementally based on what its neighbours report. Cheaper but limited — hop count maximum is 15 in RIP (16 = unreachable), which caps the size of the network RIP can serve.

### 3.2 External Gateway Protocols (EGPs) — _between_ autonomous systems

- **BGP (Border Gateway Protocol)** is the dominant EGP and currently the only widely used one.
- **Boundary routers** connect an AS to the outside world via BGP.
- OSPF and RIP are **not** EGPs.

#### Boundary, ingress, and egress routers

- **Boundary router:** a router that connects a network (or AS) to the broader Internet. BGP runs on boundary routers.
- **Ingress router:** the router where traffic _enters_ a network.
- **Egress router:** the router where traffic _leaves_ a network.
- When a network has only one gateway, the ingress and egress routers are the same physical device.

_Example:_ A university's single edge router is both its ingress and egress router — traffic arriving from the Internet enters there; traffic leaving exits there.

### 3.3 Counting to Infinity

> **MCQ fact:** "In which of the following algorithms is counting to infinity a cause for concern?" The answer is both **Bellman-Ford** and **RIP** (because RIP _uses_ Bellman-Ford). So the correct MCQ option is **D — More than one of the above**.

**Why it happens:** In Bellman-Ford, if your current next-hop router for some destination advertises a _new_ (possibly worse) cost to that destination, you **must adopt it immediately**, even if the new cost is higher. If a link goes down, the cost to reach the now-unreachable destination keeps incrementing as routers re-advertise back and forth — counting upward toward "infinity" (where infinity is some implementation-defined maximum, e.g. 16 in RIP).

_Example:_ Routers A and B both previously routed to network X via each other. When the direct link to X fails, A still thinks it can reach X via B at cost 2 (before B knows the link is down). B updates its table: "A says cost 2, plus 1 hop to A = cost 3 via A." A then sees B advertises cost 3, updates to cost 4 via B. They keep incrementing until the cost hits 16 (RIP's infinity), at which point the route is finally declared unreachable.

### 3.4 Dijkstra's algorithm (worked example)

**Setup:** costs between nodes (undirected): `A–B: 1 | C–D: 1 | A–F: 10 | D–E: 3 | B–C: 6 | E–F: 2 | B–E: 1`

Run Dijkstra from **A**:

|#|Finalised set|Candidates (cost via path)|Picked|Updated cost / "previous"|
|---|---|---|---|---|
|init|{A}|B(1), F(10)|—|A=0|
|1|{A,B}|B(1 — picked), F(10)|**B**|B=1 via A|
|2|{A,B,E}|from B: C(1+6=7), E(1+1=2); plus F(10)|**E**|E=2 via B|
|3|{A,B,E,F}|from E: D(2+3=5), F(2+2=4) — update F from 10 to 4; plus C(7)|**F**|F=4 via E|
|4|{A,B,E,F,D}|from F: nothing new; D(5), C(7)|**D**|D=5 via E|
|5|{A,B,E,F,D,C}|from D: C(5+1=6) — update C from 7 to 6|**C**|C=6 via D|

**Answers:**

- a) Picked at end of iteration 3 → **F** (cost 4)
- b) Cost to C _before iter 4_ → **7** (only path known so far: A→B→C)
- c) Node delivering en route to C _before iter 4_ → **B** (the only known path is A→B→C, so B is the next hop after A and the final deliverer to C)
- d) Picked at end of iteration 4 → **D** (cost 5)
- e) Cost to C _before iter 5_ → **7** (D was just picked; its neighbours haven't been evaluated yet — that happens at the _start_ of iter 5)

### 3.5 Bellman-Ford / RIP (worked example)

**Setup:** at time _t₀_ the routing tables at routers C, D, E are:

**Node C:** `A 7 B | B 1 B | D 3 D | F 2 B` **Node D:** `A 20 E | C 3 C | E 4 E | F 7 E` **Node E:** `A 6 F | B 1 F | D 2 D | F 4 F`

At _t₁ > t₀_, C sends its routing table to D. At _t₂ > t₁_, E sends its routing table to D.

**a) D's entry for A after receiving C's table (but prior to t₂)?**

- C reaches A at cost 7. D reaches C at cost 3. Total via C = 10.
- D's old route to A was cost 20.
- **D updates: A, cost 10, next hop C.**

**b) D's entry for B after receiving C's table?**

- C reaches B at cost 1. D reaches C at cost 3. Total = 4.
- D had no route to B before.
- **D updates: B, cost 4, next hop C.**

**c) D's entry for A after receiving E's table?**

- E reaches A at cost 6. D reaches E at cost 4. Total via E = 10.
- D's current route (just installed) is cost 10 via C.
- Same cost — table may keep the existing route or switch. Typical behaviour: **A, cost 10, next hop C** (or E — equivalent).

**d) D's entry for B after receiving E's table?**

- E reaches B at cost 1. D reaches E at cost 4. Total via E = 5.
- D's current route is cost 4 via C (cheaper).
- **D keeps: B, cost 4, next hop C.**

**e) D's entry for F after receiving E's table?**

- E reaches F at cost 4. D reaches E at cost 4. Total via E = 8.
- D's original route to F was cost 7 via E.
- **Critical rule:** Because D's _current next-hop router_ for F (E) is now advertising a new cost (4 → F, plus D's 4 to reach E = total 8), D **must adopt** this new cost, even though 8 > 7.
- **D updates: F, cost 8, next hop E.** (This is the mechanism that causes counting-to-infinity.)

---

## 4. The IPv4 Header

The IPv4 header carries routing and housekeeping data. All fields:

|Field|Size|Purpose|
|---|---|---|
|**Version**|4 bits|`4` for IPv4; `6` for IPv6 (same field position, retained for identification).|
|**IHL (Header Length)**|4 bits|Length of the header in 32-bit words (minimum = 5 = 20 bytes).|
|**Type of Service / Differentiated Services**|8 bits|Originally for QoS; reassigned as Differentiated Services. **Not examined in this module.**|
|**Total Length**|16 bits|Total size of the IP datagram (header + data) in bytes.|
|**Identification**|16 bits|Identifies which original datagram a fragment belongs to (all fragments of one datagram share this value).|
|**Flags**|3 bits|Bit 1: "Don't Fragment" (DF); Bit 2: "More Fragments" (MF); Bit 0: reserved.|
|**Fragment Offset**|13 bits|Position (in 8-byte units) of this fragment in the original datagram.|
|**Time-to-Live (TTL)**|8 bits|Max hops remaining; decremented by each router; discard at 0.|
|**Protocol**|8 bits|Layer 4 protocol: TCP=6, UDP=17, ICMP=1. Tells the receiving IP layer which upper-layer protocol to pass the payload to.|
|**Header Checksum**|16 bits|Validates the **header only** (not the payload). Recalculated by every router.|
|**Source Address**|32 bits|Sender's IP.|
|**Destination Address**|32 bits|Recipient's IP.|
|**Options**|Variable|Rarely used; includes source routing (strict and loose). Very few implementations support it.|
|**Padding**|Variable|Ensures the header ends on a 32-bit word boundary.|

### 4.1 TTL — Time to Live (key facts)

- Every router that forwards a packet **subtracts 1 from the TTL**.
- If TTL becomes **0**, the packet is **discarded**.
- The router **may** send an **ICMP "Time Exceeded" message** back to the source.

> ⚠️ **Critical note on ICMP types:** The textbook (written by the examiner) lists Time Exceeded as **ICMP Type 10**. The standard RFC 792 uses Type 11. Since this is the examiner's textbook, treat **Type 10 as the primary answer**. Type 11 may also be accepted, but do not default to it.

> **MCQ fact:** "A router receives an IP datagram _d_ and its TTL becomes 0. What may the router do next?"
> 
> - Discard _d_ ✓
> - Send a Time-Exceeded ICMP message to the source ✓
> - Answer: **D — More than one of the above.**

**Why TTL exists:** prevents packets bouncing forever in routing loops.

_Example:_ Router A thinks the best route to Z is via B. Router B thinks the best route to Z is via A. Without TTL, a packet for Z would bounce A→B→A→B forever. TTL kills the packet after (initial TTL) hops.

### 4.2 IPv4 fragmentation

The Layer 2 protocol carrying IP datagrams often has a **maximum PDU size** — the **MTU (Maximum Transmission Unit)**. Ethernet's MTU is **1500 octets**. If an IP datagram is larger than the MTU, the IP layer must fragment it.

> **MCQ fact:** "An IP datagram may be fragmented to:" → **B: Fit IP datagrams in size-constrained layer 2 frames.** ✓

#### Fragmentation fields

- **Identification:** all fragments of one original datagram share the same Identification value so the destination knows they belong together.
- **Fragment Offset:** position of this fragment within the original datagram, in units of **8 bytes**, so the destination can reassemble in order.
- **Flags — "More Fragments" (MF):** set on all fragments except the last one.
- **Flags — "Don't Fragment" (DF):** if set, this datagram must never be fragmented; if it is too large, the router discards it and sends ICMP Destination Unreachable back.

#### Reassembly

Reassembly is performed at the **final destination**, not at intermediate routers.

_Example:_ A 4000-byte datagram travels over Ethernet (MTU = 1500). Header = 20 bytes, so max payload per fragment = 1480 bytes.

- Fragment 1: 1480-byte payload, offset = 0, MF = 1
- Fragment 2: 1480-byte payload, offset = 1480/8 = 185, MF = 1
- Fragment 3: 1020-byte payload, offset = 2960/8 = 370, MF = 0

All three share the same Identification number; the destination reassembles using the offsets.

### 4.3 Checksum

Only the **header** is checksummed at Layer 3 — not the payload. Higher-layer protocols (TCP, UDP) provide their own checksums covering the payload.

---

## 5. IPv4 Addressing

IPv4 uses **32-bit addresses**, written in dotted-decimal notation: `1.2.3.4` = `00000001.00000010.00000011.00000100`.

The address is divided into two parts:

- **Network portion** — identifies the network.
- **Host portion** — identifies the specific host within that network.

### Key bitwise operations

- **Network address** = `host_IP & netmask` (bitwise AND — zero out all host bits)
- **Broadcast address** = `network | (~netmask)` (bitwise OR with inverted mask — set all host bits to 1)

These relationships hold for any subnet:

> **Exam Q style (final-exam Q41 pattern):** "Let `·` indicate bitwise AND and `+` indicate bitwise OR. Let `−x` indicate the bitwise NOT of x. Let `i` = host IP, `m` = netmask, `n` = network address, `b` = broadcast address. Which claims are true?"
> 
> - `i · m = n` ✓ (network = IP AND mask)
> - `i + (−m) = b` ✓ (broadcast = IP OR NOT-mask)
> - `i + (−b) = n` ✓ (also equivalent) Answer: **All of the above.**

### 5.1 Classful addressing (historical)

Originally, leading bits dictated network size:

|Class|Leading bits|First octet range|Network bits|Host bits|Example|
|---|---|---|---|---|---|
|**A**|`0xxxxxxx`|0–127|8|24|`10.0.0.0`|
|**B**|`10xxxxxx`|128–191|16|16|`172.16.0.0`|
|**C**|`110xxxxx`|192–223|24|8|`192.168.1.0`|
|**D**|`1110xxxx`|224–239|—|—|**Multicast**|
|**E**|`1111xxxx`|240–255|—|—|**Reserved / experimental**|

> **MCQ fact:** Multicast address ranges from 224.0.0.0–239.255.255.255. "If one sends a message to an IP multicast address, the message will be delivered to" → **C: All nodes that are members of some group.** ✓

_Example — class identification:_

- `172.16.5.3` → first octet 172 (128–191) → **Class B**. Network = `172.16.0.0`.
- `192.168.1.50` → first octet 192 (192–223) → **Class C**. Network = `192.168.1.0`.
- `8.8.8.8` → first octet 8 (0–127) → **Class A**. Network = `8.0.0.0`.

### 5.2 Subnetting and CIDR

Classful addressing is rigid, so CIDR (Classless Inter-Domain Routing) and subnet masks are used. The notation `a.b.c.d/n` means _n_ bits belong to the network (prefix).

**Subnetting** — dividing one large block into smaller networks by borrowing bits from the host portion.

**Supernetting** — combining several contiguous network addresses into one larger aggregate to simplify routing tables.

#### Worked CIDR translation

> **MCQ fact:** "What is the address (in CIDR notation) of the netblock `41.32.0.0` to `41.39.255.255`?"
> 
> Range: `41.32.0.0` to `41.39.255.255`. Only the second octet varies: 32 (`00100000`) to 39 (`00100111`). The first **5 bits** of the second octet (`00100`) are identical. Prefix length = 8 (first octet) + 5 = **13 bits**. Answer: **D — `41.32.0.0/13`.** ✓

_Example 2:_ Block 192.168.0.0 to 192.168.255.255 → first and second octets fixed; third and fourth vary → prefix = 16 bits → **`192.168.0.0/16`.**

### 5.3 Reserved / special IPv4 addresses (MEMORISE)

|Address / block|Meaning|
|---|---|
|**`0.0.0.0/0`**|**Default gateway** entry in routing tables. (0 bits must match → matches any destination.)|
|**`0.0.0.0/32`**|**Placeholder** for "this computer" — used as source in DHCP discovery before an address is assigned. Never used as a destination for routed traffic.|
|**`127.0.0.1` (block `127.0.0.0/8`)**|**Loopback / localhost** — traffic stays inside the machine.|
|**`255.255.255.255/32`**|**Local broadcast** — sent to all hosts on the local physical wire; not forwarded by routers.|
|**`169.254.0.0/16`**|**Link-local** — auto-assigned when no DHCP server is available. (IPv6 equivalent: `fe80::/10`.)|
|**`100.64.0.0/10`**|**Carrier-Grade NAT (CGN / shared address space)** — ISPs use this for a second layer of NAT between themselves and customer routers.|
|**`10.0.0.0/8`**|Private (Class A) range.|
|**`172.16.0.0/12`**|Private (Class B) range — spanning **`172.16.0.0` to `172.31.255.255`**.|
|**`192.168.0.0/16`**|Private (Class C) range — spanning **`192.168.0.0` to `192.168.255.255`**.|

> **MCQ fact:** "The private class B IPv4 addresses are:" → **E: `172.16.0.0`–`172.31.255.255`.** ✓

_Why `172.16.0.0/12` spans 16–31:_ /12 fixes the first 12 bits. First octet = `172`. Next 4 bits = `0001` (=16). The remaining 4 bits of the second octet vary: `0001 0000` to `0001 1111` = 16 to 31.

#### Distinguishing the two uses of `0.0.0.0`

- As **routing-table destination** (`0.0.0.0/0`): the default route; 0 bits must match → always matches.
- As **placeholder source** (`0.0.0.0` or `/32`): a temporary "I don't have an address yet" source during DHCP discovery.

### 5.4 Routing-table entries for special addresses

- **Default gateway entry:** `0.0.0.0/0`.
- **Block of 256 'class C' network addresses for private use:** `192.168.0.0/24` is the _first_ (`/24` is one class-C network). The block spans 256 such /24 networks (192.168.0.0/24 → 192.168.255.0/24).
- **Block of 16 'class B' network addresses for private use:** spans `172.16.0.0/16` → `172.31.0.0/16` (16 such /16 networks). The **last** in the block is `172.31.0.0/16`.

### 5.5 Class-based example

- `137.215.98.140` is on the UP network. The UP block is treated as a Class B (137 is in 128–191). Class-B prefix = 16 bits → **UP network = `137.215.0.0/16`.**
- `8.8.8.8` is Google DNS. As Class A (8 is in 0–127), the Class-A network is `8.0.0.0/8`, and the broadcast address (all host bits set) is **`8.255.255.255/8`.**

---

## 6. Subnetting & Supernetting — Worked Problems

### 6.1 Scenario: 170.170.170.170/16 — at least 1000 subnets, each ≥ 60 hosts

Starting block: `170.170.0.0/16` (16 bits network).

**Step 1 — How many host bits?** Need ≥ 60 hosts. 2⁶ − 2 = 62 ≥ 60 ✓ → **6 host bits.**

**Step 2 — Mask:** 32 − 6 = **/26** netmask. Subnet bits: 32 − 16 − 6 = **10 subnet bits**, giving 2¹⁰ = 1024 ≥ 1000 ✓.

**a) Netmask for subnets?** /26 → `11111111.11111111.11111111.11000000` = **`255.255.255.192`.**

**b) Subnet number 170 — network address in CIDR?**

- 170 in 10-bit binary = `00 1010 1010`.
- Insert into the next 10 bits after `/16`: 3rd octet's 8 bits + 4th octet's top 2 bits.
- 3rd octet = `00101010` = **42**.
- 4th octet = `10 000000` = **128**.
- **Network address = `170.170.42.128/26`.**

**c) Broadcast address of subnet 170?** Broadcast = network + (host bits all 1). Host range = .128 to .191. So broadcast = **`170.170.42.191`.**

**d) Last assignable host address?** Broadcast − 1 = **`170.170.42.190`.**

**e) Which subnet is `170.170.170.170` in? (provide just the number)**

- Extract the 10 subnet bits from the address `170.170.170.170`:
    - 3rd octet: 170 = `10101010`
    - 4th octet: 170 = `10101010`, top 2 bits = `10`.
- Combined subnet bits: `1010101010` = **682.**

**Supernet that holds 170.170.170.170 and ≥ 1000 hosts, sacrificing as few subnets as possible:**

**f) Netmask?** Need ≥ 1000 hosts → 2¹⁰ − 2 = 1022 ≥ 1000 ✓ → 10 host bits → **/22** mask = `255.255.252.0`.

**g) Network address of this supernet in CIDR?** Apply /22 mask to `170.170.170.170`. The 3rd octet (170 = `10101010`) ANDed with `11111100` = `10101000` = **168**. 4th octet ANDed with `00000000` = 0. **Supernet = `170.170.168.0/22`.**

**h) Number of the first subnet lost when this supernet is created?** The supernet starts at 3rd octet = 168 (`10101000`) and 4th octet = `00......`. The first 10-bit subnet ID inside this range: `1010100000` = **672.** (The supernet absorbs subnets 672–687, i.e. 2⁴ = 16 subnets, because 26 − 22 = 4 fewer subnet bits.)

### 6.2 Alternative scenario: 204.204.204.204/16 — ≥ 2000 subnets, each ≥ 30 hosts

- 30 hosts → 5 host bits (2⁵ − 2 = 30) → **/27** mask.
- 2000 subnets → 11 subnet bits (2¹¹ = 2048).
- For the **supernet** holding ≥ 2000 hosts → 11 host bits (2¹¹ − 2 = 2046) → **/21** mask.

**Question h variant: "How many MORE hosts can the supernet address than the sacrificed subnets?"**

- Moving from /27 to /21 combines 2⁶ = **64 subnets**.
- Hosts before = 64 × 30 = **1920**.
- Hosts after = 2046.
- Difference = **126 more hosts.**

---

## 7. Network Address Translation (NAT)

Because public IPv4 addresses are exhausted, organisations use **NAT**.

### How it works

- A **NAT router ("NAT box")** sits at the network edge and is assigned **one public IPv4 address**.
- Internal hosts are assigned **private addresses** (e.g. `10.x.x.x` or `192.168.x.x`).
- When an internal host requests a web page, the NAT box intercepts, **replaces the private source IP with its own public IP**, and forwards the packet to the Internet.
- When the response arrives, the NAT box looks up which internal host originated the request and reverse-translates the destination IP.

### Port tracking

To distinguish multiple simultaneous connections from internal hosts, the NAT box assigns each outgoing connection a **unique source port** on its public IP. The response targets that port, and the NAT box maps the port back to the correct internal host:port.

_Example:_ Host `10.0.0.5:12345` connects to `93.184.216.34:80`. The NAT box rewrites the packet as `203.0.113.1:54321 → 93.184.216.34:80`. When the server replies to port 54321 on the public IP, the NAT box maps it back to `10.0.0.5:12345`.

### Carrier-Grade NAT (CGN)

ISPs assign private addresses to customers and run their own NAT using the **100.64.0.0/10 (shared address space)**. This creates double-NAT (NAT at the ISP and again at the customer's home router). Addresses in 100.64.0.0/10 are routable within an ISP but not on the public Internet.

### Why private addresses are necessary

> **Final-exam Q35 (2024) — "Critique this argument":** _"Since the NAT box converts internal addresses, public addresses can be used inside the network without any restriction."_
> 
> **Correct critique (B):** The argument **does not consider** that **public IP addresses are allocated to specific countries / organisations**. Routers inside the organisation could become confused, since the addresses physically inside the LAN belong to someone else on the Internet. If those external addresses are ever queried inside the LAN, internal routers would refuse to forward to them externally. Hence private ranges exist to ensure internal addresses **never escape** onto the public Internet.

---

## 8. ICMP & ARP — Layer-3 Support Protocols

ICMP and ARP are not routing protocols and don't perform Layer-4 functions, but they support IP. They are conventionally classified on **Layer 3**.

### 8.1 ICMP — Internet Control Message Protocol

ICMP sends **control and status messages**. ICMP packets are very simple: a **Type number** (8 bits) plus an optional payload. ICMP packets are carried as the **payload of an IP packet**. The Type number indicates which control command or status is being reported. ICMP type numbers range from 0 to 255; the definitive list is maintained by IANA.

#### ICMP type table (from the textbook — memorise the bolded ones)

|Type|Name|Notes|
|---|---|---|
|**0**|**Echo Reply**|Response to a ping request.|
|**3**|**Destination Unreachable**|Sent when IP cannot deliver (no route, DF set and fragmentation needed, etc.).|
|4|Source Quench|Old congestion signal (deprecated). Recognise the name.|
|5|Redirect|Tells a host to use a different router for a destination. Recognise the name.|
|**8**|**Echo (Echo Request)**|Sent by `ping`. Requests the destination to echo the payload back.|
|9|Router Advertisement|Routers announce themselves.|
|**10**|**Time Exceeded**|Sent when TTL becomes 0. **This is the type used in the examiner's textbook.**|

> **MCQ facts:**
> 
> - `ping` sends **ICMP Type 8 (Echo)**. The reply is **Type 0 (Echo Reply)**.
> - `traceroute`/`tracert` exploits the **TTL field** and relies on **ICMP Type 10 (Time Exceeded)** messages returned by intermediate routers.

#### `traceroute` / `tracert` — mechanism

1. Send a datagram to the destination with **TTL = 1**. The first router decrements TTL to 0, discards the datagram, and returns ICMP Type 10 → router 1 is identified.
2. Repeat with **TTL = 2** → router 2 is identified.
3. Continue until the datagram reaches the destination (which replies with ICMP Type 0 or a transport-layer response).

_Example:_ Running `tracert 8.8.8.8` from your laptop might show:

```
1   1ms   192.168.0.1     (your home router)
2   8ms   196.25.1.1      (ISP router)
3  15ms   196.25.2.5      (ISP core)
```

Each line corresponds to one TTL increment. Some routers choose not to send Time Exceeded messages (or have them blocked by firewalls) and appear as `* * *`.

> **Useful exam phrasing:**
> 
> - Which IPv4 header field makes `traceroute` possible? → **TTL.**
> - Which ICMP message implements `traceroute`? → **Time Exceeded (Type 10).**
> - Which ICMP request is sent by ping? → **Echo Request (Type 8).**

### 8.2 ARP — Address Resolution Protocol

ARP translates a **known Layer-3 IP address** into the **Layer-2 MAC address** of the same host. Required because Layer 2 (Ethernet, etc.) delivers frames based on MAC addresses, not IP addresses.

#### How ARP works

1. Node `10.1.1.1` wants to send data to `10.1.1.2` on the same switch.
2. It **broadcasts** an ARP request: _"Who has 10.1.1.2? Tell 10.1.1.1."_
3. All nodes on the link receive the broadcast and compare it to their own IP.
4. Node `10.1.1.2` recognises its own IP and replies: _"10.1.1.2 is at 00-1a-92-1f-9e-0f"._
5. `10.1.1.1` stores the reply in its **ARP cache** and addresses Layer-2 frames directly to that MAC.

ARP caches translations (with a timeout) to avoid re-broadcasting for every packet.

_Example 2:_ Host at `192.168.1.50` wants to reach server at `192.168.1.1`. Checks ARP cache — no entry. Broadcasts ARP request. Server replies with its MAC. Host caches the MAC and sends the data directly.

> **Layer 3 command:** `arp -a` displays the ARP cache — all currently known IP-to-MAC mappings on the local link.

---

## 9. IPv4 Unicasting, Multicasting and Broadcasting

|Delivery type|Description|IP address range|
|---|---|---|
|**Unicast**|One sender → one specific receiver|Normal host addresses|
|**Broadcast**|One sender → all hosts on the local segment|`255.255.255.255` (local), or network broadcast address|
|**Multicast**|One sender → all _interested group members_|`224.0.0.0` – `239.255.255.255` (Class D)|

**Multicast** is more efficient than broadcasting: a node joins a multicast group (using IGMP — the Internet Group Management Protocol), and only interested segments receive the traffic. Intermediate routers must also support multicast routing to correctly forward multicast streams.

_Example:_ An online radio station streams to a multicast address. Only routers serving networks with at least one listener forward the stream. Routers on networks with no listeners do not.

---

## 10. IPv6 — The Successor to IPv4

IPv4's 32-bit space is exhausted. IPv6 uses **128-bit** addresses, written as **8 blocks of 4 hex digits** separated by colons.

### 10.1 Notation rules

- Full: `2001:0db8:0000:0000:0000:0000:0000:0123`
- Suppress **one** run of consecutive zero-blocks with `::`: `2001:0db8::0123`
- Drop leading zeros within each block: `2001:db8::123`
- **Only one `::` is allowed per address** (otherwise ambiguous).
- Each block represents **16 bits** (4 hex digits = 16 bits).

_Example — expanding `::1`:_ `0000:0000:0000:0000:0000:0000:0000:0001`.

_Example — expanding `2001:db8::123`:_ `2001:0db8:0000:0000:0000:0000:0000:0123`.

### 10.2 IPv6 header — simpler than IPv4

IPv6 deliberately simplified the header:

|Change from IPv4|Detail|
|---|---|
|**Version = 6**|Same field position as IPv4; retained for identification.|
|**TTL → Hop Limit**|Same purpose — decremented at each hop, discarded at 0. Renamed.|
|**Payload Length**|Length of the payload only (not the header).|
|**No header checksum**|Removed. Higher layers (TCP, UDP) are responsible.|
|**No fragmentation fields in main header**|Moved to extension headers. Routers do **not** fragment IPv6 packets; the source must use Path MTU Discovery and fragment at the source if needed.|
|**Extension headers**|A linked list of optional headers following the main header (for routing, fragmentation, etc.). Most everyday packets have none.|

_Why removing the checksum is acceptable:_ Link-layer protocols (Ethernet) and TCP/UDP already checksum their data. The IPv4 header checksum was redundant overhead that every router had to recalculate.

### 10.3 IPv6 address structure

In typical cases:

- Top **64 bits** = **routing prefix** (network portion, sometimes including subnet bits).
- Bottom **64 bits** = **interface identifier** (host/node ID — more precisely tied to the _interface_, not the host).

A "normal" routable address: 48-to-64-bit ISP-assigned prefix + 0-to-16 subnet bits + 64-bit interface ID.

**Addresses are bound to interfaces, not hosts.** A laptop with Ethernet and WiFi has at least two IPv6 addresses — one per active interface — plus link-local addresses on each.

### 10.4 Special prefixes (MEMORISE)

|Prefix|Name|Notes|
|---|---|---|
|**`::0/128`**|**Unspecified address**|Like IPv4 `0.0.0.0` — source placeholder before address is assigned.|
|**`::0/0`**|**Default gateway**|Like IPv4 `0.0.0.0/0` in routing tables.|
|**`::1/128`**|**Loopback / localhost**|Like `127.0.0.1`. Uses all 128 bits — no interface ID.|
|**`::ffff:0:0/96`**|**IPv4-mapped IPv6**|Represents an IPv4 address in IPv6 notation. E.g. `10.10.10.10` → `::ffff:A0A:A0A`. Routed via IPv4 stack if available, not native IPv6.|
|**`fc00::/7`**|**Unique local** ("private")|Like IPv4 `10.0.0.0/8` + `172.16.0.0/12` + `192.168.0.0/16`. Not globally routable. Split into `fc00::/8` (undefined) and `fd00::/8` (random-prefix block).|
|**`fd00::/8`**|**ULA — random-prefix**|Site picks a **40-bit random global ID** to prevent collisions when private networks merge, then a 16-bit subnet ID, then 64-bit interface ID.|
|**`fe80::/10`**|**Link-local unicast (SLAAC)**|Like `169.254.0.0/16`. Only valid on the local link; **never routed**.|
|**`2001:db8::/32`**|Documentation|Reserved for examples and documentation only.|
|**`ff00::/8`**|**Multicast**|IPv6 has **no broadcast** — multicast and anycast replace it.|

> **MCQ fact:** "Which of the following IPv6 addresses correspond with the IPv4 address `10.10.10.10`?"
> 
> `10.10.10.10` in hex = `0A.0A.0A.0A`. Group into 16-bit pieces: `0A0A:0A0A`. Suppress leading zeros: `A0A:A0A`. Prepend IPv4-mapped prefix: **Answer: `::FFFF:A0A:A0A`** (option written as `0::FFFF:A0A:A0A` in the exam).

#### Unique local address structure (`fd00::/8`)

```
| fd (8 bits) | Global ID (40 bits, random) | Subnet ID (16 bits) | Interface ID (64 bits) |
```

_Example:_ `fd12:3456:789a:bcde:f0fe:dcba:9876:5432`

- `fd` — ULA random-prefix byte
- `12:3456:789a` — 40-bit **random global ID** chosen by the site
- `bcde` — 16-bit **subnet ID**
- `f0fe:dcba:9876:5432` — 64-bit **interface identifier**

#### fe80::/10 bit-level detail

`fe80::/10` specifies the first 10 bits as `1111 1110 10`. Bits 11–63 of a link-local address are **always zero**. The last 64 bits are the interface identifier.

Because all link-local addresses share `fe80::`, a host with multiple interfaces must append the interface name to disambiguate:

- Linux: `fe80::922b:34ff:fe9a:871a%eth0`
- Windows: `fe80::a241:7d5:a1dd:f306%32`

An address where bits 11–63 are not all zero (e.g. `fe80:1234::.../128`) would be **illegal** under the current standard.

### 10.5 SLAAC — Stateless Address Autoconfiguration

A host without DHCP can autoconfigure an IPv6 address:

1. Take the `fe80::/10` (link-local) prefix.
2. Extend with zeros to `/64`: `fe80::/64`.
3. Append a randomly generated 64-bit interface identifier.
4. Run **duplicate-address detection** on the link — if no collision, use the address.

### 10.6 Address scopes

Every IPv6 address has an intended **scope** — the region within which it must be unique:

|Prefix|Scope|
|---|---|
|`::1/128`|Host-local (only this machine)|
|`fe80::/10`|**Link-local** (only this physical link/wire)|
|`fc00::/7`|**Site-local** (within the organisation)|
|Regular routable (`2001:...` etc.)|**Global** (public Internet)|
|`ff00::/8`|Multicast (scope encoded in the address)|

### 10.7 Unicast, multicast, anycast (no broadcast!)

- **Unicast:** to one specific interface.
- **Multicast** (`ff00::/8`): to **all** members of a group.
- **Anycast:** to **any one** member of a group — the nearest by routing metric. Syntactically identical to unicast; only distinguishable by administrative configuration.
- **Broadcast: does not exist in IPv6.** Its functions are taken over by multicast and anycast.

_Example of anycast:_ Many DNS servers share the same anycast address. A query is automatically routed to the nearest one with no client configuration.

### 10.8 Transitioning IPv4 → IPv6

Two main strategies:

1. **Dual stack:** the host runs both IPv4 and IPv6 stacks. When a destination has both A (IPv4) and AAAA (IPv6) DNS records, the host picks one — usually preferring IPv6.
2. **Tunnelling:** encapsulate an IPv6 packet inside an IPv4 packet (or vice versa) and forward to a tunnel endpoint. Useful when only one protocol is available end-to-end.

_Example:_ `tracert /6` on Windows forces the IPv6 stack. `tracert6` on Linux is similar.

### 10.9 Deprecated / transitional prefixes (recognise but don't memorise)

- `2002::/16` — 6to4 tunnelling
- `2001::/32` — Teredo tunnelling
- `3ffe::/16` — 6bone (deprecated)
- `::/96` — IPv4-compatible (old, deprecated; replaced by `::ffff:0:0/96`)
- `fec0::/10` — site-local (deprecated; replaced by `fc00::/7`)

---

## 11. Routing for IPv6

Like IPv4, IPv6 prefixes are assigned by IANA → RIRs → ISPs → end organisations. The routing table format `(destination, next hop, interface)` is unchanged in concept. Organisations advertise their prefixes via multicast, simplifying ISP changes.

---

## Examinable Practice Questions on Layer 3

### Multiple Choice

**Q1.** The primary metric used by interior gateway protocols is: A. Cost B. Hop count C. Distance D. Static routing tables E. Speed F. Noise

**Q2.** Which of the following protocols is/are examples of an external gateway protocol (EGP)? A. BGP B. OSPF C. RIP D. More than one of the above E. All of the above

**Q3.** In which of the following algorithms is counting to infinity a cause for concern? A. Dijkstra B. Bellman-Ford C. RIP D. More than one of the above E. All of the above

**Q4.** Routers using OSPF broadcast their ... and use the received information to apply the ... algorithm. A. Routing tables; Dijkstra B. Routing tables; Bellman-Ford C. Routing tables; RIP D. Version of the network topology; Dijkstra E. Version of the network topology; Bellman-Ford

**Q5.** Consider a scenario in RIP where a router _r_ sends its routing table to a router _s_. An entry in _r_'s table indicates that it can reach a network _n_ at a cost of 5. Before receiving the message, the routing table at _s_ indicated that it could reach _n_ at a cost of 8. What will the cost from _s_ to _n_ be according to the routing table at _s_ after _s_ processes the message from _r_? A. 5 B. 6 C. 7 D. 8 E. More information about _r_ is required to answer the question.

**Q6.** If one sends a message to an IP multicast address, the message will be delivered to: A. The node to which that IP address has been assigned. B. All nodes on the local network. C. All nodes that are members of some group. D. The network itself, rather than to a host on the network. E. The network gateway that connects the network to other networks.

**Q7.** An IP datagram may be fragmented to: A. Expedite routing. B. Fit IP datagrams in size-constrained layer 2 frames. C. Ensure that fixed-size packets are sent to the lower layer. D. Fit IP datagrams in size-constrained layer 4 segments. E. Minimise data loss if a packet is discarded.

**Q8.** Suppose a router receives an IP datagram _d_ and its TTL becomes 0. What may the router do next? A. Discard _d_. B. Forward _d_ to the next hop. C. Send a Time Exceeded ICMP message to the source. D. More than one of the above. E. All of the above.

**Q9.** The private class B IPv4 addresses are: A. 172.1.0.0–172.1.255.255 B. 172.2.0.0–172.3.255.255 C. 172.4.0.0–172.7.255.255 D. 172.8.0.0–172.15.255.255 E. 172.16.0.0–172.31.255.255

**Q10.** What is the address (in CIDR notation) of the netblock `41.32.0.0` to `41.39.255.255`? A. 41.32.0.0/10 B. 41.32.0.0/11 C. 41.32.0.0/12 D. 41.32.0.0/13 E. None of the above

**Q11.** Which of the following IPv6 addresses correspond with the IPv4 address `10.10.10.10`? A. 0::A:A:A:A B. 0::AA:AA C. 0::FFFF:A.A.A.A D. 0::FFFF:AA:AA E. 0::FFFF:A0A:A0A

**Q12.** Consider the IP routing algorithm. Assume it has reached the point where it either consulted the routing table and found no match, or it noted that no routing table exists. What is the next step it will attempt? A. Check whether a default gateway is defined and, if one is defined, forward the packet to such a default gateway. B. Transfer the packet to layer 4. C. Directly deliver the packet. D. Discard the packet. E. More than one of the above.

**Q13.** An IP datagram addressed to `10.10.1.2` arrives at node R. R is not directly connected to the destination. The routing table at R includes:

```
10.10.10.0/24    192.168.1.1   eth1
10.10.0.0/16     192.168.2.2   eth2
10.0.0.0/8       192.168.3.3   eth3
0.0.0.0/0        192.168.4.4   eth4
```

To which next hop does R forward the datagram? A. 192.168.1.1 B. 192.168.2.2 C. 192.168.3.3 D. 192.168.4.4 E. More than one of the above

**Q14.** Consider the IPv6 address `fd12:3456:789a:bcde:f0fe:dcba:9876:5432`. Which of the following is true about the part `12:3456:789a`? A. It was supplied by an ISP/RIR. B. It designates a subnet. C. It is a random number. D. It was calculated from the MAC address of the interface. E. None of the above.

**Q15.** Consider the IPv6 address `fd12:3456:789a:bcde:f0fe:dcba:9876:5432`. Which of the following is true about the part `bcde`? A. It was supplied by an ISP/RIR. B. It designates a subnet. C. It is a random number. D. It was calculated from the MAC address of the interface. E. None of the above.

**Q16.** Consider the IPv6 address `fe80:1234:5678:9abc:def0:fedb:a987:6543/128`. This address: A. Is an SLA address. B. Is a link-local address. C. Is a site-local address. D. Is a global address. E. Would currently not be a legal address.

**Q17.** Which of the following prefixes indicate an IPv4-mapped address expressed in IPv6 notation? A. `::ffff:0:0/96` B. `::ffff:0/80/96` (mistyped variant) C. `0:0:0:0:ffff:0:0/96` D. More than one of the above E. All of the above

**Q18.** IP address `172.16.5.79` belongs to: A. Class A B. Class B C. Class C D. Class D E. Class E

**Q19.** The type of router that connects an organisation's network to other networks is: A. Ingress router B. Egress router C. Boundary router D. More than one of the above E. All of the above

**Q20.** An IPv4 datagram is sent to a network address (e.g. `8.0.0.0`, where 8.0.0.0/8 is the network). What should happen? A. It is sent to the destination network and delivered once it reaches that network. B. At the first router the routing algorithm will note the destination is a network address and discard it. C. The datagram arrives at the final router, which cannot find a host 0 and discards it. D. More than one of the above. E. All of the above.

**Q21.** Let `·` denote bitwise AND, `+` denote bitwise OR, and `−x` denote the bitwise NOT of x. Let `i` = a host's IP, `m` = its netmask, `n` = its network address, `b` = its broadcast address. Which is/are true? A. `i · m = n` B. `i + (−m) = b` C. `i + (−b) = n` D. More than one of the above E. All of the above

**Q22.** ICMP is used to: A. Report errors on the IP layer. B. Test network functions (e.g. echo/ping). C. Modify routes. D. More than one of the above. E. All of the above.

### Long-Form & Calculation

**Q23. ICMP/IPv4 utilities.** Provide the answers to the following: a) Which IPv4 header field makes it possible to implement the `traceroute` command? b) Which ICMP message is typically used to implement `traceroute`? c) Which ICMP request is sent by the client to perform a `ping` command? d) Which IPv4 addresses are reserved for link-local addresses? (CIDR) e) Provide the IPv4 entry used as the destination in a routing table to identify the default gateway. (CIDR)

**Q24. IPv4 addressing (Scenario A).** Use CIDR notation for all answers. a) Which IPv4 address is used in a routing table to indicate the default-gateway entry? b) A block of 256 'class C' network addresses is reserved for private use. Provide the _first_ class C network address that occurs within this block. c) A block of 16 'class B' network addresses is reserved for private use. Provide the _last_ class B network address that occurs within this block. d) `137.215.98.140` is a host on the University of Pretoria network. What is the UP network address? e) `8.8.8.8` is a popular DNS server. If this address were still part of a class-based address, what would the broadcast address on this network be?

**Q25. Subnetting & supernetting (Scenario B).** Your organisation uses `170.170.170.170/16`. They decide to subnet so that they have at least 1000 subnets each handling at least 60 hosts. a) What netmask will they use for the subnets? b) Consider _subnet number 170_. What is the network address of this subnet in CIDR? c) What is the broadcast address of subnet 170? d) What is the last (biggest) address that may be assigned to a host on subnet 170? e) On which subnet is the host `170.170.170.170`? Provide only the number. f) The organisation needs a much bigger subnet at the same location, handling at least 1000 hosts, sacrificing as few subnets as possible. Provide the netmask of this supernet. g) Provide the network address of this supernet in CIDR. h) What is the _number_ of the first subnet that will be lost once this supernet has been created?

**Q26. Subnetting & supernetting (Scenario B').** Same as Q25 but starting from `204.204.204.204/16`, with at least 2000 subnets each handling at least 30 hosts. a)–g) (analogous to above; see memo) h) How many MORE hosts can the supernet address than the sacrificed subnets?

**Q27. Routing — Dijkstra.** Apply Dijkstra's algorithm from node A given the costs: `A–B: 1 | C–D: 1 | A–F: 10 | D–E: 3 | B–C: 6 | E–F: 2 | B–E: 1`

a) Which node is picked as the cheapest alternative at the end of iteration 3? b) Before starting iteration 4, what is the cost to reach C from A? c) Before starting iteration 4, which node will finally deliver a packet en route to C? d) Which node is added to the finalised set at the end of iteration 4? e) Before starting iteration 5, what is the cost to reach C from A?

**Q28. Routing — Bellman-Ford / RIP.** Initial tables at C, D, E:

- C: `A 7 B | B 1 B | D 3 D | F 2 B`
- D: `A 20 E | C 3 C | E 4 E | F 7 E`
- E: `A 6 F | B 1 F | D 2 D | F 4 F`

At _t₁_ C sends its table to D. At _t₂ > t₁_ E sends its table to D.

a) D's entry for **A** after receiving C's table (prior to _t₂_)? b) D's entry for **B** after receiving C's table? c) D's entry for **A** after receiving E's table? d) D's entry for **B** after receiving E's table? e) D's entry for **F** after receiving E's table?

**Q29. NAT critique.** A NAT box converts internal addresses to external addresses and vice versa. Critique the following argument: _"Since the NAT box hides internal addresses, an organisation can use any addresses internally without restriction — even public addresses allocated to other organisations."_

**Q30. IPv4 fragmentation.** A 4000-byte IP datagram must traverse an Ethernet link (MTU = 1500 bytes). The IP header is 20 bytes. a) How many fragments will be created? b) What is the payload size of each fragment? c) What is the Fragment Offset (in 8-byte units) of the third fragment? d) Which flag bit is set on the first and second fragments but not on the last?

---

## Memo / Answer Key

### MCQ Answers

**A1.** B (Hop count — the metric used by RIP). _Note: OSPF uses 'cost', but the lecturer's question phrasing about "primary metric" expects hop count as the canonical IGP answer._

**A2.** A (BGP). OSPF and RIP are IGPs, not EGPs.

**A3.** D (More than one of the above — both Bellman-Ford and RIP, because RIP _uses_ Bellman-Ford).

**A4.** D (Version of the network topology; Dijkstra).

**A5.** E (More information about _r_ is required). To update its table, _s_ must know the cost of the link from _s_ to _r_, which is not provided.

**A6.** C (All nodes that are members of some group).

**A7.** B (Fit IP datagrams in size-constrained layer 2 frames).

**A8.** D (More than one of the above — discard _and_ send ICMP Time Exceeded).

**A9.** E (172.16.0.0–172.31.255.255).

**A10.** D (41.32.0.0/13). The 5 unchanging high bits of the second octet (`00100`) plus the first 8 bits give 13 prefix bits.

**A11.** E (`0::FFFF:A0A:A0A` or equivalently `::FFFF:A0A:A0A`). 10.10.10.10 = `0A0A:0A0A` in 16-bit hex groups → leading-zero-suppressed `A0A:A0A`.

**A12.** A (Check whether a default gateway is defined and, if so, forward to it).

**A13.** B (192.168.2.2 / eth2 — longest-prefix match wins: /16 is more specific than /8 and /0).

**A14.** C (It is a random number — for a `fd00::/8` unique-local address, the 40 bits after the `fd` prefix byte are a randomly chosen global ID).

**A15.** B (It designates a subnet — the 16-bit subnet ID follows the 40-bit global ID).

**A16.** E (Would currently not be a legal address — `fe80::/10` link-local addresses must have bits 11–63 all zero; non-zero bits there are illegal under current standards).

**A17.** D (More than one — option C written out in full is the same as option A `::ffff:0:0/96`).

**A18.** B (Class B — first octet 172 is in the range 128–191).

**A19.** D (More than one — a boundary router serves both ingress and egress roles when it is the only connection to the outside).

**A20.** C (The datagram reaches the final router, which finds no host 0 and discards it).

**A21.** E (All of the above — A, B, and C are all correct bitwise formulations).

**A22.** D (More than one — ICMP reports errors and tests network functions; it does not modify routes, so C is false).

### Long-Form Answers

**A23.** a) **TTL** (Time-to-Live). b) **Time Exceeded** (ICMP **Type 10** per the textbook; RFC 792 uses Type 11 — answer Type 10 in this module). c) **Echo Request** (ICMP Type 8). d) **`169.254.0.0/16`.** e) **`0.0.0.0/0`.**

**A24.** a) `0.0.0.0/0` b) `192.168.0.0/24` (first /24 in the 192.168.0.0/16 block) c) `172.31.0.0/16` (last /16 in the 172.16–172.31 block) d) `137.215.0.0/16` (Class B → /16 prefix) e) `8.255.255.255/8` (Class A broadcast — all host bits set)

**A25. Subnetting (170.170.170.170/16; ≥1000 subnets, ≥60 hosts each)**

Need ≥60 hosts → 6 host bits (2⁶−2 = 62). Mask = /26. Subnet bits = 10 → 2¹⁰ = 1024 ✓.

a) **255.255.255.192** (/26) b) 170 in 10-bit binary = `0010101010`. 3rd octet = `00101010` = 42. 4th octet top 2 = `10` → `10000000` = 128. **`170.170.42.128/26`.** c) 128 + 63 = **`170.170.42.191`.** d) **`170.170.42.190`.** e) 3rd octet `10101010`, 4th octet top 2 `10` → combined `1010101010` = **682.** f) 10 host bits → /22. **`255.255.252.0`.** g) 3rd octet `10101010` AND `11111100` = `10101000` = 168. **`170.170.168.0/22`.** h) `1010100000` = **672.** (Subnets 672–687 absorbed; 16 subnets = 2⁴.)

**A26. Subnetting (204.204.204.204/16; ≥2000 subnets, ≥30 hosts each)**

5 host bits (2⁵−2 = 30). Mask = /27. Subnet bits = 11 → 2¹¹ = 2048 ✓.

a) **255.255.255.224** (/27) b) 204 in 11-bit = `00011001100`. 3rd octet = `00011001` = 25. Top 3 bits of 4th octet = `100` → `10000000` = 128. **`204.204.25.128/27`.** c) 128 + 31 = **`204.204.25.159`.** d) **`204.204.25.158`.** e) 3rd octet `11001100`, top 3 of 4th `110` → `11001100110` = **1638.** f) 11 host bits → /21. **`255.255.248.0`.** g) 3rd octet `11001100` AND `11111000` = `11001000` = 200. **`204.204.200.0/21`.** h) Combine 2⁶ = 64 subnets. Hosts before = 64 × 30 = 1920. Hosts after = 2046. **126 more hosts.**

**A27. Dijkstra** (as in §3.4):

- a) **F** picked at end of iter 3 (cost 4)
- b) Cost to C before iter 4 = **7**
- c) Final delivering node to C at this stage = **B**
- d) **D** picked at end of iter 4 (cost 5)
- e) Cost to C before iter 5 = **7** (D's neighbours not evaluated until start of iter 5)

**A28. Bellman-Ford** (as in §3.5):

- a) **A: cost 10, next hop C**
- b) **B: cost 4, next hop C**
- c) **A: cost 10, next hop C** (tied with E route)
- d) **B: cost 4, next hop C** (cheaper than 5 via E)
- e) **F: cost 8, next hop E** — D must adopt E's new advertisement because E is D's _current_ next hop for F, even though 8 > 7. This drives counting-to-infinity.

**A29. NAT critique.** The argument fails because **public IPv4 addresses are allocated to specific countries and organisations**. Using, say, `137.215.0.0/16` (UP's allocation) internally means internal routers cannot distinguish between internal and external hosts with that address — they would collide. Traffic destined for the real `137.215.x.y` on the public Internet would be delivered to the internal imposter. NAT boxes exist specifically to keep internal traffic within the RFC-defined private ranges (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), which are guaranteed not to appear on the public Internet.

**A30. Fragmentation.**

- Datagram payload = 4000 − 20 = 3980 bytes. Max payload per fragment over Ethernet = 1500 − 20 = **1480 bytes**.
- a) ⌈3980 / 1480⌉ = **3 fragments**.
- b) Fragment 1: **1480 bytes**; Fragment 2: **1480 bytes**; Fragment 3: **1020 bytes**.
- c) Fragment 3 offset = 2960 / 8 = **370** (in 8-byte units).
- d) The **"More Fragments" (MF)** flag is set on fragments 1 and 2 (indicating more follow); it is cleared on fragment 3 (the last).
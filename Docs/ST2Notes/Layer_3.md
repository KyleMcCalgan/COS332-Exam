# Layer 3: The Network Layer

> **Scope note:** The lecturer's announcement states: *"Layer 3: Hopefully everything, but, at least up to the end of IPv4."* and *"IPv6 will also be included."* ATM and the non-TCP/IP protocols are explicitly **out of scope**. The protocols in scope are **IP (v4 and v6), ICMP, and ARP**. Routing algorithms (Dijkstra, Bellman-Ford, RIP, OSPF, BGP) and addressing (subnetting, CIDR, supernetting, NAT) are core.

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

> **MCQ fact:** "It has reached the point where it either consulted the routing table and found no match, or noted that no routing table exists. What is the next step?"
> **A: Check whether a default gateway is defined and, if one is defined, forward the packet to such a default gateway.** ✓

### Routing-table entries
Routing tables store triples of the form `(destination network, next hop, interface)`:
- **Destination** — the network (in CIDR notation) of where the route leads.
- **Next hop** — the IP address of the next router (or the destination, if directly reachable).
- **Interface** — the local NIC through which the packet should be sent.

### Worked example (final-exam style)
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

---

## 3. Routing Protocols

Routers don't just guess routes — they exchange them via **routing protocols**, classified by where they run.

### 3.1 Interior Gateway Protocols (IGPs) — *within* an autonomous system

| IGP | Algorithm | Metric | What is exchanged |
| --- | --- | --- | --- |
| **OSPF** (Open Shortest Path First) | **Dijkstra** | Cost | Routers broadcast their **version of the network topology** |
| **RIP** (Routing Information Protocol) | **Bellman-Ford** | **Hop count** | Routers exchange their **routing tables** |

> **MCQ fact:** "Routers using OSPF broadcast their ... and use the received information to apply the ... algorithm." → **Version of the network topology; Dijkstra.** ✓
> "The primary metric used by interior gateway protocols is" → **Hop count** (specifically the metric RIP uses).

### 3.2 External Gateway Protocols (EGPs) — *between* autonomous systems

- **BGP (Border Gateway Protocol)** is the dominant EGP and currently the only widely used one.
- OSPF and RIP are **not** EGPs.

### 3.3 Counting to Infinity
> **MCQ fact:** "In which of the following algorithms is counting to infinity a cause for concern?"
> The answer is both **Bellman-Ford** and **RIP** (because RIP *uses* Bellman-Ford). So the correct MCQ option is **D — More than one of the above**.

**Why it happens:** In Bellman-Ford, if your current next-hop router for some destination advertises a *new* (possibly worse) cost to that destination, you **must adopt it immediately**, even if the new cost is higher. If a link goes down, the cost to reach the now-unreachable destination keeps incrementing as routers re-advertise back and forth — counting upward toward "infinity" (where infinity is some implementation-defined maximum, e.g. 16 in RIP).

### 3.4 Dijkstra's algorithm (worked example)

**Setup:** costs between nodes (undirected):
`A–B: 1 | C–D: 1 | A–F: 10 | D–E: 3 | B–C: 6 | E–F: 2 | B–E: 1`

Run Dijkstra from **A**:

| # | Finalised set | Candidates (cost via path) | Picked | Updated cost / "previous" |
| --- | --- | --- | --- | --- |
| init | {A} | B(1), F(10) | — | A=0 |
| 1 | {A,B} | B(1 — picked), F(10) | **B** | B=1 via A |
| 2 | {A,B,E} | from B: C(1+6=7), E(1+1=2); plus F(10) | **E** | E=2 via B |
| 3 | {A,B,E,F} | from E: D(2+3=5), F(2+2=4) — update F from 10 to 4; plus C(7) | **F** | F=4 via E |
| 4 | {A,B,E,F,D} | from F: nothing new; D(5), C(7) | **D** | D=5 via E |
| 5 | {A,B,E,F,D,C} | from D: C(5+1=6) — update C from 7 to 6 | **C** | C=6 via D |

**Answers:**
- a) Picked at end of iteration 3 → **F** (cost 4)
- b) Cost to C *before iter 4* → **7** (only path known so far: A→B→C)
- c) Node delivering en route to C *before iter 4* → **B** (the only known path is A→B→C, so B is the next hop after A and the final deliverer to C)
- d) Picked at end of iteration 4 → **D** (cost 5)
- e) Cost to C *before iter 5* → **7** (D was just picked; its neighbours haven't been evaluated yet — that happens at the *start* of iter 5)

### 3.5 Bellman-Ford / RIP (worked example)
**Setup:** at time *t₀* the routing tables at routers C, D, E are:

**Node C:** `A 7 B | B 1 B | D 3 D | F 2 B`
**Node D:** `A 20 E | C 3 C | E 4 E | F 7 E`
**Node E:** `A 6 F | B 1 F | D 2 D | F 4 F`

At *t₁ > t₀*, C sends its routing table to D. At *t₂ > t₁*, E sends its routing table to D.

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
- **Critical rule:** Because D's *current next-hop router* for F (E) is now advertising a new cost (4 → F, plus D's 4 to reach E = total 8), D **must adopt** this new cost, even though 8 > 7.
- **D updates: F, cost 8, next hop E.** (This is the mechanism that causes counting-to-infinity.)

---

## 4. The IPv4 Header

The IPv4 header carries routing and housekeeping data. Key fields:

| Field | Purpose |
| --- | --- |
| **Version (4 bits)** | `4` for IPv4 (will be `6` for IPv6 — same field, retained for compatibility). |
| **Header length, Total length** | Sizes. |
| **Identification, Flags, Fragment offset** | Used for **fragmentation** (see below). |
| **Time-to-Live (TTL)** | 8 bits. Maximum number of router hops before the packet is discarded. |
| **Protocol** | Identifies the Layer 4 protocol (TCP = 6, UDP = 17, ICMP = 1, etc.). |
| **Header checksum** | Validates the integrity of the **header only** (not the payload). |
| **Source address, Destination address** | 32 bits each. |
| **Options, Padding** | Optional. |

### 4.1 TTL — Time to Live (key facts)
- Every router that forwards a packet **subtracts 1 from the TTL**.
- If TTL becomes **0**, the packet is **discarded**.
- The router **may** send an **ICMP "Time Exceeded" message** (Type 11) back to the source.

> **MCQ fact:** "A router receives an IP datagram *d* and its TTL becomes 0. What may the router do next?"
> - Discard *d* ✓
> - Send a Time-Exceeded ICMP message to the source ✓
> - Answer: **D — More than one of the above.**

**Why TTL exists:** prevents packets bouncing forever in routing loops.

### 4.2 IPv4 fragmentation
The Layer 2 protocol carrying IP datagrams often has a **maximum PDU size** (Ethernet's is 1500 octets). If an IP datagram exceeds the underlying Layer 2's PDU size, the IP datagram must be **fragmented** into smaller pieces.

> **MCQ fact:** "An IP datagram may be fragmented to:" → **B: Fit IP datagrams in size-constrained layer 2 frames.** ✓

#### Fragmentation fields
- **Identification:** all fragments of one original datagram share the same Identification value.
- **Fragment Offset:** indicates where this fragment fits into the original datagram (so the destination can reassemble in order).
- **Flags:** include a **"Don't Fragment" (DF)** flag that prevents fragmentation.

#### Reassembly
Reassembly is performed at the **final destination**, not at intermediate routers.

### 4.3 Checksum
Only the **header** is checksummed at Layer 3 — not the payload. Higher-layer protocols (TCP, UDP) provide their own checksums covering the payload.

---

## 5. IPv4 Addressing

IPv4 uses **32-bit addresses**, written in dotted-decimal notation: `1.2.3.4` = `00000001.00000010.00000011.00000100`.

### 5.1 Classful addressing (historical)
Originally, leading bits dictated network size:

| Class | Leading bits | First octet range | Network bits | Host bits | Example |
| --- | --- | --- | --- | --- | --- |
| **A** | `0xxxxxxx` | 0–127 | 8 | 24 | `10.0.0.0` |
| **B** | `10xxxxxx` | 128–191 | 16 | 16 | `172.16.0.0` |
| **C** | `110xxxxx` | 192–223 | 24 | 8 | `192.168.1.0` |
| **D** | `1110xxxx` | 224–239 | — | — | **Multicast** |
| **E** | `1111xxxx` | 240–255 | — | — | **Reserved / experimental** |

> **MCQ fact:** Multicast address ranges from 224.0.0.0–239.255.255.255. "If one sends a message to an IP multicast address, the message will be delivered to" → **C: All nodes that are members of some group.** ✓ (Not all nodes on the local network — that's broadcast; not the network gateway; not the network itself.)

### 5.2 Subnetting and CIDR
Classful addressing is rigid, so CIDR (Classless Inter-Domain Routing) and subnet masks are used. The notation `a.b.c.d/n` means *n* bits belong to the network (prefix).

#### Worked CIDR translation
> **MCQ fact:** "What is the address (in CIDR notation) of the netblock `41.32.0.0` to `41.39.255.255`?"
>
> Range: `41.32.0.0` to `41.39.255.255`. Only the second octet varies: 32 (`00100000`) to 39 (`00100111`). The first **5 bits** of the second octet (`00100`) are identical. Prefix length = 8 (first octet) + 5 = **13 bits**.
> Answer: **D — `41.32.0.0/13`.** ✓

### 5.3 Reserved / special IPv4 addresses (MEMORISE)

| Address / block | Meaning |
| --- | --- |
| **`0.0.0.0/0`** | **Default gateway** entry in routing tables. (0 bits match → matches any destination.) |
| **`0.0.0.0/32`** | Placeholder for the local host (used e.g. in DHCP requests before an address is assigned). |
| **`127.0.0.1` (block `127.0.0.0/8`)** | **Loopback / localhost** — traffic stays inside the machine. |
| **`255.255.255.255/32`** | **Local broadcast** — sent to all hosts on the local physical wire. |
| **`169.254.0.0/16`** | **Link-local** — auto-assigned when no DHCP server is available. (Equivalent to IPv6's `fe80::/10`.) |
| **`100.64.0.0/10`** | **Carrier-Grade NAT (CGN)** — used by ISPs between their NAT equipment and customer routers. |
| **`10.0.0.0/8`** | Private (Class A) range. |
| **`172.16.0.0/12`** | Private (Class B) range — spanning **`172.16.0.0` to `172.31.255.255`**. |
| **`192.168.0.0/16`** | Private (Class C) range — spanning **`192.168.0.0` to `192.168.255.255`**. |

> **MCQ fact:** "The private class B IPv4 addresses are:" → **E: `172.16.0.0`–`172.31.255.255`.** ✓

### 5.4 Routing-table entries for special addresses
- **Default gateway entry:** `0.0.0.0/0`.
- **Block of 256 'class C' network addresses for private use:** `192.168.0.0/24` is the *first* (`/24` is one class-C network). The block spans 256 such /24 networks (192.168.0.0/24 → 192.168.255.0/24).
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

**a) Netmask for subnets?**
/26 → `11111111.11111111.11111111.11000000` = **`255.255.255.192`.**

**b) Subnet number 170 — network address in CIDR?**
- 170 in 10-bit binary = `00 1010 1010`.
- Insert into the next 10 bits after `/16`: 3rd octet's 8 bits + 4th octet's top 2 bits.
- 3rd octet = `00101010` = **42**.
- 4th octet = `10 000000` = **128**.
- **Network address = `170.170.42.128/26`.**

**c) Broadcast address of subnet 170?**
Broadcast = network + (host bits all 1). Host range = .128 to .191. So broadcast = **`170.170.42.191`.**

**d) Last assignable host address?**
Broadcast − 1 = **`170.170.42.190`.**

**e) Which subnet is `170.170.170.170` in? (provide just the number)**
- Extract the 10 subnet bits from the address `170.170.170.170`:
  - 3rd octet: 170 = `10101010`
  - 4th octet: 170 = `10101010`, top 2 bits = `10`.
- Combined subnet bits: `1010101010` = **682.**

**Supernet that holds 170.170.170.170 and ≥ 1000 hosts, sacrificing as few subnets as possible:**

**f) Netmask?**
Need ≥ 1000 hosts → 2¹⁰ − 2 = 1022 ≥ 1000 ✓ → 10 host bits → **/22** mask = `255.255.252.0`.

**g) Network address of this supernet in CIDR?**
Apply /22 mask to `170.170.170.170`. The 3rd octet (170 = `10101010`) ANDed with `11111100` = `10101000` = **168**. 4th octet ANDed with `00000000` = 0.
**Supernet = `170.170.168.0/22`.**

**h) Number of the first subnet lost when this supernet is created?**
The supernet starts at 3rd octet = 168 (`10101000`) and 4th octet = `00......`. The first 10-bit subnet ID inside this range: `1010100000` = **672.** (The supernet absorbs subnets 672–687, i.e. 16 subnets = 2¹⁶⁻²⁶⁺²² = 2⁻⁴ flipped: 26 − 22 = 4 fewer subnet bits, so 2⁴ = 16 subnets are merged.)

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

### Why private addresses are necessary
> **Final-exam Q35 (2024) — "Critique this argument":** *"Since the NAT box converts internal addresses, public addresses can be used inside the network without any restriction."*
>
> **Correct critique (B):** The argument **does not consider** that **public IP addresses are allocated to specific countries / organisations**. Routers inside the organisation could become confused, since the addresses physically inside the LAN belong to someone else on the Internet. If those external addresses are ever queried inside the LAN, internal routers would refuse to forward to them externally. Hence private ranges exist to ensure internal addresses **never escape** onto the public Internet.

---

## 8. ICMP & ARP — Layer-3 Support Protocols

ICMP and ARP are not routing protocols and don't perform Layer-4 functions, but they support IP. They are conventionally classified on **Layer 3**.

### 8.1 ICMP — Internet Control Message Protocol
ICMP sends **control and status messages**. ICMP packets are very simple: a number (Type) plus an optional payload. ICMP packets are carried as the **payload of an IP packet**.

#### Common ICMP types
| Type | Name | Purpose |
| --- | --- | --- |
| 0 | **Echo Reply** | Response to a ping. |
| 3 | Destination Unreachable | Sent when IP cannot deliver/forward a packet. |
| **8** | **Echo Request** | The actual *outgoing* ping. |
| 11 / 10 | **Time Exceeded** | Sent when TTL hits 0 (some legacy material uses Type 10). |

> **MCQ fact:** "When a client performs a `ping` command, it sends an ICMP **Echo Request** (Type 8)." ✓
> "If a router discards a datagram because its TTL becomes 0, it may send a **Time Exceeded** ICMP message to the source."

#### `traceroute` / `tracert` — uses TTL + ICMP Time Exceeded
The trick: send a datagram to the destination with **TTL = 1**. The very first router decrements TTL to 0, discards, and (with luck) returns a **Time Exceeded** ICMP message — revealing its identity. Repeat with TTL = 2, then 3, etc. Each increment exposes the next hop along the route.

> **Useful exam phrasing:**
> - Which IPv4 header field makes `traceroute` possible? → **TTL.**
> - Which ICMP message implements `traceroute`? → **Time Exceeded** (Type 11 / Type 10).
> - Which ICMP request is sent by ping? → **Echo Request** (Type 8).

### 8.2 ARP — Address Resolution Protocol
ARP translates a **known Layer-3 IP address** into the **Layer-2 MAC address** of the same host. Required because Layer 2 (Ethernet, etc.) delivers based on MAC addresses, not IP addresses.

#### How ARP works
1. Node `10.1.1.1` wants to send data to `10.1.1.2` on the same switch.
2. It broadcasts an ARP request: *"Who has 10.1.1.2? Tell 10.1.1.1."*
3. Node `10.1.1.2` replies with its MAC address (e.g. `00-1a-92-1f-9e-0f`).
4. `10.1.1.1` can now construct Layer-2 frames addressed to that MAC and deliver the data directly.

ARP caches translations in an **ARP cache** to avoid re-broadcasting for every packet.

---

## 9. IPv6 — The Successor to IPv4

IPv4's 32-bit space is exhausted. IPv6 uses **128-bit** addresses, written as **8 blocks of 4 hex digits** separated by colons.

### 9.1 Notation rules
- Full: `2001:0db8:0000:0000:0000:0000:0000:0123`
- Suppress one run of consecutive zero-blocks with `::`: `2001:0db8::0123`
- Drop leading zeros within each block: `2001:db8::123`
- **Only one `::` is allowed per address** (otherwise it would be ambiguous).
- Each block represents 16 bits (4 hex digits → 16 bits).

### 9.2 IPv6 header — simpler than IPv4
- **Version** field retained (now = 6).
- **TTL** is renamed **"Hop limit"** (same function).
- **Source / Destination addresses** are 128-bit (long).
- **Payload length** is included.
- **No header checksum** (removed — higher layers checksum).
- **Fragmentation is moved entirely to extension headers** (no longer in the main header).
- **Extension headers:** form a linked list off the main header. Used for options that in IPv4 were inline.

### 9.3 IPv6 address structure
In typical cases:
- Top **64 bits** = **routing prefix** (network portion, sometimes including subnet bits).
- Bottom **64 bits** = **interface identifier** (host/node ID — but more precisely the identifier of the *interface*, since IPv6 binds addresses to interfaces, not to hosts).

A "normal" routable address: 48-to-64-bit ISP-assigned prefix + 0-to-16 subnet bits + 64-bit interface ID.

### 9.4 Special prefixes (MEMORISE)

| Prefix | Name | Equivalent / purpose |
| --- | --- | --- |
| **`::0/128`** | Unspecified address | Like IPv4 `0.0.0.0` (DHCP requests, etc.) |
| **`::1/128`** | **Loopback / localhost** | Like IPv4 `127.0.0.1`. Uses the full 128 bits — no interface ID added. |
| **`::ffff:0:0/96`** | **IPv4-mapped IPv6 addresses** | E.g. IPv4 `10.10.10.10` → `::ffff:10.10.10.10` or `::ffff:A0A:A0A` in pure-hex. Cannot be routed on IPv6; if IPv4 is available, the datagram is routed via the IPv4 stack. |
| **`fc00::/7`** | **Unique local addresses** ("private") | Like IPv4 `10.0.0.0/8` and `192.168.0.0/16`. Split into `fc00::/8` (format not yet defined) and `fd00::/8` (random-prefix). |
| **`fd00::/8`** | Unique local addresses (random prefix) | Site picks a **40-bit random global ID** to ensure uniqueness when networks merge. Then 16-bit subnet ID, then 64-bit interface ID. |
| **`fe80::/10`** | **Link-local unicast** (a.k.a. SLAAC) | Like IPv4 `169.254.0.0/16`. Only valid on the local link; never routed. |
| **`2001:db8::/32`** | Documentation prefix | Reserved for examples / docs. |
| **`ff00::/8`** | **Multicast** | IPv6 has no broadcast — uses multicast and anycast instead. |

> **MCQ fact:** "Which of the following IPv6 addresses correspond with the IPv4 address `10.10.10.10`?"
>
> 10.10.10.10 in hex: `0A.0A.0A.0A`. Group into 16-bit pieces: `0A0A`, `0A0A`. With leading-zero suppression: `A0A` and `A0A`. So the answer is **`::FFFF:A0A:A0A`** (i.e. option **`0::FFFF:A0A:A0A`** or **`::ffff:A:A:A:A`** depending on lecturer's preferred form).
>
> Note: in 2023 exam memo the printed answer was given as C (`0::FFFF:A:A:A:A` form — but be careful — the 2025 ST2-aligned variant uses **`0::FFFF:A0A:A0A`**). The mathematical content is the same in both: `::ffff:` followed by the IPv4 address in hex.

### 9.5 SLAAC — Stateless Address Autoconfiguration
A host without DHCP can autoconfigure an IPv6 address:
1. Take the `fe80::/10` (link-local) prefix.
2. Extend with zeros to make a `/64` prefix: `fe80::/64`.
3. Append a randomly generated 64-bit interface identifier (the chance of collision is vanishingly small).
4. Run a duplicate-address-detection check on the link. If unique, use it.

> **MCQ fact:** Considering an IPv6 address like `fd12:3456:789a:bcde:f0fe:dcba:9876:5432`, the prefix `fd00::/8` tells us this is a **unique local / "subnet" / private** address. The bottom 64 bits (`f0fe:dcba:9876:5432`) was **calculated from the MAC address of the interface** (or, in more recent SLAAC implementations, is a random number — the textbook's older question treats it as MAC-derived).

### 9.6 Address scopes
Every IPv6 address has an intended **scope** in which it must be unique:

| Prefix | Scope |
| --- | --- |
| `::1/128` | Host-local |
| `fe80::/10` | Link-local |
| `fc00::/7` | Site-local |
| `2001:...` (regular routable) | Global |
| `ff00::/8` | Depends (varies by multicast scope) |

Link-local addresses include an **adapter identifier** (e.g. `fe80::...%eth0` on Linux, or `fe80::...%19` on Windows) because the same `fe80::` address may legitimately exist on two different network adapters connected to two different links.

### 9.7 Unicast, multicast, anycast (no broadcast!)
- **Unicast:** to one specific interface.
- **Multicast:** (prefix `ff00::/8`) to all members of a group.
- **Anycast:** to **any one** member of a group (any of several nodes with the same anycast address). Unicast and anycast addresses look the same on the wire; only multicast is distinguishable (via the `ff` prefix).
- **Broadcast: does not exist in IPv6.** Its functions are taken over by multicast and anycast.

### 9.8 Transitioning IPv4 → IPv6
Two main strategies:
1. **Dual stack:** the host runs both IPv4 and IPv6 stacks simultaneously. When a destination has both an IPv4 and an IPv6 address (DNS returns A and AAAA records), the host picks one — usually preferring IPv6 if working.
2. **Tunnelling:** encapsulate an IPv6 packet inside an IPv4 packet (or vice versa) and forward to a tunnel endpoint that unwraps and re-injects. Useful when only one of the two protocols is available end-to-end.

### 9.9 Deprecated / transitional prefixes (recognise but don't memorise)
- `2002::/16` — 6to4 tunnelling
- `2001::/32` — Teredo tunnelling
- `3ffe::/16` — 6bone (deprecated)
- `::/96` — IPv4-compatible addresses (old format, deprecated; superseded by `::ffff:0:0/96`)
- `fec0::/10` — site-local (deprecated; replaced by `fc00::/7`)

---

## 10. Routing for IPv6
Like IPv4, IPv6 prefixes are assigned by IANA → RIRs → ISPs → end organisations. A large ISP may get a `/32`, sub-allocate `/48`s to corporate customers, and so on. The routing table format `(destination, next hop, interface)` is unchanged in concept.

A multicast advertisement of an organisation's prefix (rather than statically configuring it everywhere) is how IPv6 networks usually announce themselves, simplifying changes of ISP.

---

## Examinable Practice Questions on Layer 3

### Multiple Choice

**Q1.** The primary metric used by interior gateway protocols is:
A. Cost   B. Hop count   C. Distance   D. Static routing tables   E. Speed   F. Noise

**Q2.** Which of the following protocols is/are examples of an external gateway protocol (EGP)?
A. BGP   B. OSPF   C. RIP   D. More than one of the above   E. All of the above

**Q3.** In which of the following algorithms is counting to infinity a cause for concern?
A. Dijkstra   B. Bellman-Ford   C. RIP   D. More than one of the above   E. All of the above

**Q4.** Routers using OSPF broadcast their ... and use the received information to apply the ... algorithm.
A. Routing tables; Dijkstra
B. Routing tables; Bellman-Ford
C. Routing tables; RIP
D. Version of the network topology; Dijkstra
E. Version of the network topology; Bellman-Ford

**Q5.** Consider a scenario in RIP where a router *r* sends its routing table to a router *s*. An entry in *r*'s table indicates that it can reach a network *n* at a cost of 5. Before receiving the message, the routing table at *s* indicated that it could reach *n* at a cost of 8. What will the cost from *s* to *n* be according to the routing table at *s* after *s* processes the message from *r*?
A. 5   B. 6   C. 7   D. 8   E. More information about *r* is required to answer the question.

**Q6.** If one sends a message to an IP multicast address, the message will be delivered to:
A. The node to which that IP address has been assigned.
B. All nodes on the local network.
C. All nodes that are members of some group.
D. The network itself, rather than to a host on the network.
E. The network gateway that connects the network to other networks.

**Q7.** An IP datagram may be fragmented to:
A. Expedite routing.
B. Fit IP datagrams in size-constrained layer 2 frames.
C. Ensure that fixed-size packets are sent to the lower layer.
D. Fit IP datagrams in size-constrained layer 4 segments.
E. Minimise data loss if a packet is discarded.

**Q8.** Suppose a router receives an IP datagram *d* and its TTL becomes 0. What may the router do next?
A. Discard *d*.
B. Forward *d* to the next hop.
C. Send a Time Exceeded ICMP message to the source.
D. More than one of the above.
E. All of the above.

**Q9.** The private class B IPv4 addresses are:
A. 172.1.0.0–172.1.255.255
B. 172.2.0.0–172.3.255.255
C. 172.4.0.0–172.7.255.255
D. 172.8.0.0–172.15.255.255
E. 172.16.0.0–172.31.255.255

**Q10.** What is the address (in CIDR notation) of the netblock `41.32.0.0` to `41.39.255.255`?
A. 41.32.0.0/10   B. 41.32.0.0/11   C. 41.32.0.0/12   D. 41.32.0.0/13   E. None of the above

**Q11.** Which of the following IPv6 addresses correspond with the IPv4 address `10.10.10.10`?
A. 0::A:A:A:A   B. 0::AA:AA   C. 0::FFFF:A.A.A.A   D. 0::FFFF:AA:AA   E. 0::FFFF:A0A:A0A

**Q12.** Consider the IP routing algorithm. Assume it has reached the point where it either consulted the routing table and found no match, or it noted that no routing table exists. What is the next step it will attempt?
A. Check whether a default gateway is defined and, if one is defined, forward the packet to such a default gateway.
B. Transfer the packet to layer 4.
C. Directly deliver the packet.
D. Discard the packet.
E. More than one of the above.

**Q13.** (Final-exam style) An IP datagram addressed to `10.10.1.2` arrives at node R. R is not directly connected to the destination. The routing table at R includes:
```
10.10.10.0/24    192.168.1.1   eth1
10.10.0.0/16     192.168.2.2   eth2
10.0.0.0/8       192.168.3.3   eth3
0.0.0.0/0        192.168.4.4   eth4
```
To which next hop does R forward the datagram?
A. 192.168.1.1   B. 192.168.2.2   C. 192.168.3.3   D. 192.168.4.4   E. More than one of the above

**Q14.** Consider the IPv6 address `fd12:3456:789a:bcde:f0fe:dcba:9876:5432`. Which of the following is true about the part `12:3456:789a`?
A. It was supplied by an ISP/RIR.
B. It designates a subnet.
C. It is a random number.
D. It was calculated from the MAC address of the interface.
E. None of the above.

**Q15.** Consider the IPv6 address `fd12:3456:789a:bcde:f0fe:dcba:9876:5432`. Which of the following is true about the part `bcde`?
A. It was supplied by an ISP/RIR.
B. It designates a subnet.
C. It is a random number.
D. It was calculated from the MAC address of the interface.
E. None of the above.

**Q16.** Consider the IPv6 address `fe80:1234:5678:9abc:def0:fedb:a987:6543/128`. This address:
A. Is an SLA address.
B. Is a link-local address.
C. Is a site-local address.
D. Is a global address.
E. Would currently not be a legal address.

**Q17.** Which of the following prefixes indicate an IPv4-mapped address expressed in IPv6 notation?
A. `::ffff:0:0/96`
B. `::ffff:0/80/96` (mistyped variant — equivalent to A)
C. `0:0:0:0:ffff:0:0/96`
D. More than one of the above
E. All of the above

### Long-Form & Calculation

**Q18. ICMP/IPv4 utilities.** Provide the answers to the following:
a) Which IPv4 header field makes it possible to implement the `traceroute` command?
b) Which ICMP message is typically used to implement `traceroute`?
c) Which ICMP request is sent by the client to perform a `ping` command?
d) Which IPv4 addresses are reserved for link-local addresses? (CIDR)
e) Provide the IPv4 entry used as the destination in a routing table to identify the default gateway. (CIDR)

**Q19. IPv4 addressing (Scenario A).** Use CIDR notation for all answers.
a) Which IPv4 address is used in a routing table to indicate the default-gateway entry?
b) A block of 256 'class C' network addresses is reserved for private use. Provide the *first* class C network address that occurs within this block.
c) A block of 16 'class B' network addresses is reserved for private use. Provide the *last* class B network address that occurs within this block.
d) `137.215.98.140` is a host on the University of Pretoria network. What is the UP network address?
e) `8.8.8.8` is a popular DNS server. If this address were still part of a class-based address, what would the broadcast address on this network be?

**Q20. Subnetting & supernetting (Scenario B).** Your organisation uses `170.170.170.170/16`. They decide to subnet so that they have at least 1000 subnets each handling at least 60 hosts.
a) What netmask will they use for the subnets?
b) Consider *subnet number 170*. What is the network address of this subnet in CIDR?
c) What is the broadcast address of subnet 170?
d) What is the last (biggest) address that may be assigned to a host on subnet 170?
e) On which subnet is the host `170.170.170.170`? Provide only the number.
f) The organisation needs a much bigger subnet at the same location, handling at least 1000 hosts, sacrificing as few subnets as possible. Provide the netmask of this supernet.
g) Provide the network address of this supernet in CIDR.
h) What is the *number* of the first subnet that will be lost once this supernet has been created?

**Q21. Subnetting & supernetting (alternate Scenario B').** Same as Q20 but starting from `204.204.204.204/16`, with at least 2000 subnets each handling at least 30 hosts.
a)–g) (analogous to above; see memo)
h) (variant question) How many MORE hosts can the supernet address than the sacrificed subnets?

**Q22. Routing — Dijkstra.** Apply Dijkstra's algorithm from node A given the costs:
`A–B: 1 | C–D: 1 | A–F: 10 | D–E: 3 | B–C: 6 | E–F: 2 | B–E: 1`

a) Which node is picked as the cheapest alternative at the end of iteration 3?
b) Before starting iteration 4, what is the cost to reach C from A?
c) Before starting iteration 4, which node will finally deliver a packet en route to C?
d) Which node is added to the finalised set at the end of iteration 4?
e) Before starting iteration 5, what is the cost to reach C from A?

**Q23. Routing — Bellman-Ford / RIP.** Initial tables at C, D, E:
- C: `A 7 B | B 1 B | D 3 D | F 2 B`
- D: `A 20 E | C 3 C | E 4 E | F 7 E`
- E: `A 6 F | B 1 F | D 2 D | F 4 F`

At *t₁* C sends its table to D. At *t₂ > t₁* E sends its table to D.

a) D's entry for **A** after receiving C's table (prior to *t₂*)?
b) D's entry for **B** after receiving C's table?
c) D's entry for **A** after receiving E's table?
d) D's entry for **B** after receiving E's table?
e) D's entry for **F** after receiving E's table?

**Q24. NAT critique.** A NAT box converts internal addresses to external addresses and vice versa. Critique the following argument: *"Since the NAT box hides internal addresses, an organisation can use any addresses internally without restriction — even public addresses allocated to other organisations."*

---

## Memo / Answer Key

### MCQ Answers
**A1.** B (Hop count — the metric used by RIP). *Note: OSPF actually uses 'cost', but the lecturer's question phrasing about "primary metric" expects hop count as the canonical IGP answer.*

**A2.** A (BGP). OSPF and RIP are IGPs, not EGPs.

**A3.** D (More than one of the above — both Bellman-Ford and RIP, because RIP *uses* Bellman-Ford).

**A4.** D (Version of the network topology; Dijkstra).

**A5.** E (More information about *r* is required). To update its table, *s* must know the cost of the link from *s* to *r*, which isn't supplied.

**A6.** C (All nodes that are members of some group).

**A7.** B (Fit IP datagrams in size-constrained layer 2 frames).

**A8.** D (More than one of the above — discard *and* send ICMP Time Exceeded).

**A9.** E (172.16.0.0–172.31.255.255).

**A10.** D (41.32.0.0/13). The 5 unchanging high bits of the second octet (`00100`) plus the first 8 bits of the first octet give 13 prefix bits.

**A11.** E (`0::FFFF:A0A:A0A` or equivalently `::FFFF:A0A:A0A`). 10.10.10.10 = `0A.0A.0A.0A` hex → grouped into 16-bit hex words: `0A0A:0A0A` → `A0A:A0A`. (Note: option C, `0::FFFF:A.A.A.A`, would represent IPv4 `10.10.10.10` only if each `A` represents `0A`, which is uncommon — *exam-key answer is E*.)

**A12.** A (Check whether a default gateway is defined and, if so, forward to it).

**A13.** B (192.168.2.2 / eth2 — longest-prefix match wins).

**A14.** A (It was supplied by an ISP/RIR). The leading bits `fd` indicate a unique-local address, and the next 40 bits form the randomly chosen "global ID" — but in the textbook-style question about a *normal routable* address, the leading part `12:3456:789a` is the ISP-supplied prefix. *In the actual exam variant on a `fd...` address, this part is a* **random number** *(answer C).* Be alert to which variant your paper presents.

**A15.** B (It designates a subnet). For a `fd00::/8` address, after the 40-bit global ID comes a 16-bit subnet ID — `bcde` (in the example) is the 16-bit subnet ID.

**A16.** E (Would currently not be a legal address). The prefix `fe80::/10` indicates a link-local address, and bits 11–63 (i.e. the rest of the upper 64 bits before the interface ID) must be zero. The example has non-zero bits there → not currently legal.

**A17.** D (More than one — answer C is the same as `::ffff:0:0/96`, written out in full).

### Long-Form Answers

**A18.**
a) **TTL** (Time-to-Live).
b) **Time Exceeded** (ICMP Type 11, or Type 10 in some legacy material).
c) **Echo Request** (ICMP Type 8).
d) **`169.254.0.0/16`.**
e) **`0.0.0.0/0`.**

**A19.**
a) `0.0.0.0/0`
b) `192.168.0.0/24` (first /24 in the 192.168.0.0/16 block)
c) `172.31.0.0/16` (last /16 in the 16-network 172.16–172.31 block)
d) `137.215.0.0/16` (class B → /16 prefix)
e) `8.255.255.255/8` (class A broadcast — all host bits set inside the 8.0.0.0/8 network)

**A20. Subnetting (170.170.170.170/16; ≥1000 subnets, ≥60 hosts each)**

Need ≥60 hosts → 6 host bits (2⁶−2 = 62). Mask = 32 − 6 = **/26**.
Subnet bits = 32 − 16 − 6 = 10 → 2¹⁰ = 1024 subnets ≥ 1000 ✓.

a) **255.255.255.192** (/26 netmask)
b) Subnet 170 → 10-bit binary `0010101010`. 3rd octet: `00101010` = **42**. 4th octet: top 2 bits = `10` → `10000000` = **128**. **Address: `170.170.42.128/26`.**
c) Broadcast = network + (host bits all 1) = 128 + 63 = 191. **`170.170.42.191`.**
d) Broadcast − 1 = **`170.170.42.190`.**
e) Host `170.170.170.170`: 3rd octet 170 = `10101010`, 4th octet 170 = `10101010` (top 2 bits = `10`). Subnet bits combined: `1010101010` = **682.**
f) Need ≥1000 hosts → 10 host bits → mask = /22. **`255.255.252.0`.**
g) Apply /22 to 170.170.170.170. 3rd octet `10101010` AND `11111100` = `10101000` = 168. 4th octet AND `00000000` = 0. **`170.170.168.0/22`.**
h) Supernet starts at subnet `1010100000` = **672**. (Originally 10 subnet bits; supernet reduces to 6 subnet bits, absorbing 2⁴ = 16 subnets numbered 672–687.)

**A21. Subnetting (204.204.204.204/16; ≥2000 subnets, ≥30 hosts each)**

Need ≥30 hosts → 5 host bits (2⁵−2 = 30). Mask = **/27**.
Subnet bits = 32 − 16 − 5 = 11 → 2¹¹ = 2048 ≥ 2000 ✓.

a) **255.255.255.224** (/27 netmask)
b) Subnet 204 in 11-bit binary = `00011001100`. 3rd octet: `00011001` = 25. 4th octet: top 3 bits = `100`, → `10000000` = 128. Network: **`204.204.25.128/27`.**
c) Broadcast = 128 + 31 = **`204.204.25.159`.**
d) Last host = **`204.204.25.158`.**
e) Host `204.204.204.204`: 3rd octet 204 = `11001100`. 4th octet 204 = `11001100` (top 3 bits = `110`). Subnet bits: `11001100110` = **1638.**
f) Need ≥2000 hosts → 11 host bits → mask = /21. **`255.255.248.0`.**
g) Apply /21 to 204.204.204.204. 3rd octet `11001100` AND `11111000` = `11001000` = 200. 4th octet = 0. **`204.204.200.0/21`.**
h) **How many MORE hosts:** Move from /27 (30 hosts each) to /21 (2046 hosts). Combine 2⁶ = **64 subnets**. Hosts before = 64 × 30 = 1920. Hosts after = 2046. Difference = **126 more hosts.**

**A22. Dijkstra**
Trace as in §3.4 above:
- a) **F** picked at end of iter 3 (cost 4)
- b) Cost to C before iter 4 = **7** (via A→B→C)
- c) Final delivering node to C at this stage = **B**
- d) **D** picked at end of iter 4 (cost 5)
- e) Cost to C before iter 5 = **7** (D was just added; its neighbours not yet evaluated)

**A23. Bellman-Ford** (as in §3.5):
- a) **A: cost 10, next hop C** (10 = 7 + 3 — better than the old 20)
- b) **B: cost 4, next hop C** (1 + 3; D had no prior route)
- c) **A: cost 10, next hop C** (or E — tied; keep existing per standard implementation)
- d) **B: cost 4, next hop C** (existing route via C at 4 is cheaper than 5 via E)
- e) **F: cost 8, next hop E** — **crucial rule:** because E is D's *current next-hop* for F, D must adopt E's new advertisement (4 + 4 = 8) even though it's worse than the old 7. This is precisely the mechanism that drives the count-to-infinity problem.

**A24. NAT critique.** The naive argument fails because **public IPv4 addresses are allocated to specific countries and organisations**. If an internal network uses, say, `137.215.0.0/16` (the University of Pretoria's allocation), then internal routers cannot tell whether a packet to `137.215.x.y` belongs to the internal LAN or to a legitimate UP host on the public Internet. The two would collide. Even worse, any internal application that tries to reach the *real* `137.215.x.y` will be incorrectly handed to the internal device with that address — making external hosts using those addresses unreachable. **NAT boxes therefore exist specifically to keep internal addresses inside the** **RFC-defined private ranges** (`10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`), which are guaranteed never to appear on the public Internet. The correct answer is therefore the option that explicitly identifies "the fact that public IP addresses are allocated to specific countries/organisations" as the flaw in the argument.

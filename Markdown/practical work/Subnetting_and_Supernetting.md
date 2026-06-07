# Subnetting and Supernetting — COS332 Study Notes

---

## 1. The Core Idea — What is an IP Address?

An IP address in CIDR notation like `222.222.222.222/22` is two pieces of information:

- The **host address** — the full 32-bit number
- The **prefix length** (`/22`) — how many of those bits belong to the **network**; the rest belong to the **host**

```
|<---- network bits ---->|<---- host bits ---->|
       22 bits                   10 bits          (for /22)
```

The **netmask** is just the prefix length written as a 32-bit number — `n` ones followed by zeros:

```
/22 → 11111111.11111111.11111100.00000000 → 255.255.252.0
```

> Note: CIDR notation is never used for a netmask — you write `255.255.252.0`, never `255.255.252.0/22`.

---

## 2. The Three Fundamental Addresses

Given any IP address and prefix length, you can always derive:

**Network address** — force all host bits to `0`. This is the identifier for the network itself.

**Broadcast address** — force all host bits to `1`. Packets sent here reach every host on the network.

**Valid hosts** — every address in between. Count = `2^(host bits) - 2` (subtract network and broadcast addresses).

### The algorithm

1. Write the IP address in binary
2. Draw a line after the nth bit (n = prefix length)
3. Everything left of the line = network portion (never changes)
4. Everything right = host portion (variable)
5. Network address = network bits + all zeros on the right
6. Broadcast address = network bits + all ones on the right

---

## 3. Worked Example — `222.222.222.222/22`

Convert to binary:

```
222 = 11011110
Full address: 11011110.11011110.11011110.11011110
```

Draw the line after bit 22 (sits inside the third octet):

```
11011110.11011110.110111|10.11011110
                        ^
                   line is here
```

| Address | Binary | Dotted decimal | CIDR |
|---|---|---|---|
| Network | `11011110.11011110.11011100.00000000` | 222.222.220.0 | /22 |
| Broadcast | `11011110.11011110.11011111.11111111` | 222.222.223.255 | — |
| Netmask | `11111111.11111111.11111100.00000000` | 255.255.252.0 | — |

---

## 4. Subnetting

### What it is

You take bits from the **host** portion and reassign them as **subnet** bits. This increases the prefix length.

```
Original:  |<-- network (22) -->|<---------- host (10) ---------->|
Subnetted: |<-- network (22) -->|<-- subnet -->|<-- host bits -->|
```

### The constraints

- Need at least **n subnets** → `2^(subnet bits) ≥ n`
- Each subnet needs at least **m hosts** → `2^(host bits) - 2 ≥ m`
- Subnet bits + host bits must equal the original host bits

### Worked example — at least 10 subnets, at least 50 hosts each

Starting with 10 host bits. Borrow `s` bits for subnets, leaving `h = 10 - s` for hosts.

- Subnets: `2^s ≥ 10` → minimum s = 4 (gives 16 subnets)
- Hosts: `2^h - 2 ≥ 50` → minimum h = 6 (gives 62 usable hosts)
- Check: 4 + 6 = 10 ✓

New prefix = 22 + 4 = **/26**

New netmask:
```
11111111.11111111.11111111.11000000 = 255.255.255.192
```

### The new address structure

```
|<-- 22 network -->|<- 4 subnet ->|<- 6 host ->|
```

Each subnet block is `2^6 = 64` addresses wide.

---

## 5. Finding Which Subnet a Host Is On

Rather than listing all subnets and counting down, read the subnet bits directly from the address.

H = `222.222.222.222` in binary:

```
11011110.11011110.11011110.11011110
|<-- 22 network -->|<4 sub>|<6 host>|
```

The 4 subnet bits straddle octets 3 and 4:
- Last 2 bits of octet 3: `10`
- First 2 bits of octet 4: `11`
- Subnet bits = `1011` = **11**

The 6 host bits are the remaining bits: `011110` = **30**

So H is **host 30 on subnet 11**.

### Finding the subnet's network and broadcast addresses

Network address — take the first 26 bits of H, zero out the rest:
```
11011110.11011110.11011110.11|000000 = 222.222.222.192/26
```

Broadcast address — take the first 26 bits of H, set the rest to ones:
```
11011110.11011110.11011110.11|111111 = 222.222.222.255
```

---

## 6. Supernetting

### What it is

The opposite of subnetting — you **combine** multiple subnets into one larger block by removing bits from the prefix. The router stops seeing boundaries between the merged subnets and treats them as a single flat network.

The key constraint: subnets being merged must be **contiguous and aligned** — they must form a natural power-of-2 block starting at a valid boundary.

### The new prefix

The prefix is always:

```
new prefix = original network bits + new subnet bits needed
```

- Merging 2 subnets → need 1 subnet bit (`2^1 = 2`) → new prefix = 22 + 1 = /23
- Merging 4 subnets → need 2 subnet bits (`2^2 = 4`) → new prefix = 22 + 2 = /24
- Merging 8 subnets → need 3 subnet bits (`2^3 = 8`) → new prefix = 22 + 3 = /25
- Merging all 16 → need 0 subnet bits → new prefix = 22 + 0 = /22 (back to original)

### Finding which group a subnet belongs to (decimal method)

1. Find the subnet number (read subnet bits directly from the address → decimal)
2. Divide by group size, take the floor → group number
3. Start of group = group number × group size → that's the first subnet in the supernet
4. Convert that subnet number to binary, slot into the address structure, zero out host bits → network address

### Worked example — merge 4 subnets, H is on subnet 11

Group size = 4.

`11 ÷ 4 = 2` remainder 3 → H is in **group 2**

Start of group 2 = `2 × 4 = 8` → **subnet 8**

Subnet 8 in binary = `1000`. Slot into the address:

```
|<-- 22 network -->|1000|000000
11011110.11011110.11011110.10|0000|000000
= 222.222.222.0
```

New prefix = 22 + 2 = **/24**

New netmask = `255.255.255.0`

---

## 7. What Supernetting Actually Means

Once you supernet 4 subnets (8, 9, 10, 11) into a /24:

- **Subnet 10 as a concept no longer exists.** There is no boundary at `222.222.222.128` anymore.
- A host at `.222.130` and a host at `.222.210` are on the **same network** and can communicate directly without routing.
- The old subnet selection bits (`00`, `01`, `10`, `11`) are still physically there in the address — they are now just part of the 8-bit host number, counting hosts 0 through 255.
- The 4 groups of 64 addresses are still sitting there in the address space. You just stopped drawing lines between them.

The only thing that changed was the prefix length — and therefore what the router considers a network boundary.

---

## 8. Quick Reference

### Address structure at each stage

```
/22 (original):
|<---- 22 network ---->|<---------- 10 host ---------->|

/26 (after subnetting):
|<---- 22 network ---->|<-- 4 subnet -->|<-- 6 host -->|

/24 (after supernetting 4 subnets):
|<---- 22 network ---->|<-- 2 -->|<------- 8 host ------>|
                                 ^ these 2 bits were subnet
                                   bits, now reclassified
                                   as host bits
```

### Netmask quick reference

| Prefix | Netmask | Host bits | Usable hosts |
|---|---|---|---|
| /22 | 255.255.252.0 | 10 | 1022 |
| /24 | 255.255.255.0 | 8 | 254 |
| /26 | 255.255.255.192 | 6 | 62 |

### Summary of answers for 222.222.222.222/22

| Question | Answer |
|---|---|
| Network address | 222.222.220.0/22 |
| Broadcast address | 222.222.223.255 |
| Netmask | 255.255.252.0 |
| New netmask (after subnetting /26) | 255.255.255.192 |
| H's subnet network address | 222.222.222.192/26 |
| H's subnet broadcast address | 222.222.222.255 |
| H's subnet number | 11 |
| H's host number | 30 |
| Supernet network address | 222.222.222.0/24 |
| Supernet netmask | 255.255.255.0 |

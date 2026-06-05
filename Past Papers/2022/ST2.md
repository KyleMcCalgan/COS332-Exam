Here are the extracted questions and their multiple-choice options from the second exam paper:

## Question 1 (Multiple Choice)

**a)** An HTTP header may indicate the character encoding(s) it is able to handle by using the ... header.
- A: Accept-Encoding
- B: Accept-Charset
- C: iso-8859-2
- D: utf-8
- E: text/html


**b)** UTF-8 is deemed to be self-synchronising because
- A: Two computers that both use UTF-8 are able to communicate in a meaningful manner.
- B: A recipient will be able to inspect the incoming octets and automatically determine that the UTF-8 encoding scheme is used.
- C: If a transmission error occurs, the recipient will be able to determine where a new character starts.
- D: The SYN and ACK characters are supported by UTF-8.
- E: None of the above, because UTF-8 is not self-synchronising.


**c)** Suppose a computer that is primarily used to work with documents in Greek requests a web page from a server that hosts only documents in Greek. In order to transmit a GET request, the browser
- A: May use F'ET as a substitute for GET.
- B: Must sent GET (encoded in US ASCII).
- C: May use ΠΑΙΡΝΩ (the Greek for 'I get') as a substitute for GET
- D: More than one of the above
- E: All of the above


**d)** Which of the following is not an ASN.1 constructor?
- A: STRUCT
- B: CHOICE
- C: SEQUENCE
- D: SET
- E: All of the above are, in fact, ASN.1 constructors.


**e)** Amultipart MIME representation uses a 'boundary' to indicate the start of a new part. This boundary contains
- A: A random string of characters.
- B: A sequence of non-printable characters.
- C: One or more carefully selected keywords that depend on the types of the various parts.
- D: A number that indicates the length of the part that follows.
- E: Words such as mixed, alternative and related, that indicate the relationship of the parts of the content to one another.


**f)** A popular content transfer encoding is base64. Base64 represents
- A: Binary data in hexadecimal.
- B: Textual data in binary.
- C: Arbitrary data in hexadecimal.
- D: Arbitrary data using 7-bit ASCII values


**g)** Reliable protocols are typically
- A: Connection-oriented.
- B: Connectionless.
- C: Neither connectionless, nor connection-oriented.
- D: Both connectionless and connection-oriented.


**h)** Suppose process A establishes a TCP connection with node B. A sends a SYN message to node B. B sends a SYN+ACK to node A. Node A sends an ACK to node B, but lightning strikes and this final ACK never reaches node B. Node A's plan was to send some brief message, M, once the connection has been established. Which of the following claims is true?
- A: The connection is not established and both A and B immediately report an error to the upper layer. A does not transmit M.
- B: A assumes the connection has been established successfully and transmits M. B considers the handshake incomplete, reports an error to its upper layers and ignores M. Only when B fails to acknowledge M after repeated transmissions of M does A abort communication and report an error to its upper layers.
- C: A sends M, which includes an ACK flag; B accepts this ACK as the final phase of the handshake. The connection is established, but M is lost (until A retransmits it).
- D: A sends M, which includes an ACK flag; B accepts this ACK as the final phase of the handshake. The connection is established, and B accepts M. Communication can proceed normally.
- E: None of the scenarios above accurately depict what will happen.


**i)** TCP attempts to reduce data loss on the network under the assumption that... is the primary cause form data loss.
- A: Jitter
- B: Network speed
- C: Data corruption
- D: Limited amount of memory available for buffers
- E: Congestion


**j)** A window advertisement in a TCP segment indicates the available memory in the... of the segment.
- A: transmit buffer of the sender
- B: receive buffer of the sender
- C: transmit buffer of the recipient
- D: receive buffer of the recipient


**k)** Some years ago the IPng version of IP was widely discussed. Currently IPng would be referred to as
- A: Simply IP
- B: IPv4
- C: IPv5
- D: IPv6
- E: None of the above


**l)** When class-based addresses were still in use, the address 120.15.1.1 would have been part of a class... network address.
- A: A
- B: B
- C: C
- D: D
- E: E


**m)** Routers within an organisation typically discover other routers on OSI layer 3 by using
- A: Unicasting
- B: Muticasting
- C: Broadcasting
- D: Anycasting
- E: Podcasting


**n)** IPv4 network addresses are typically used
- A: To broadcast messages to an entire network.
- B: In routing tables, to identify a network.
- C: For anycasting.
- D: More than one of the above
- E: All of the above


**o)** Ports are classified as dynamic, well-known or registered ports. When these classes are sorted from the class containing the lowest port number to those with the highest number, the resulting order would be
- A: Dynamic, well-known, registered
- B: Well-known, registered, dynamic
- C: Well-known, dynamic, registered
- D: Dynamic, registered, Well-known
- E: Registered, dynamic, Well-known


**p)** Which of the following is a private network address (or are private network addresses)?
- A: 176.16.0.0
- B: 172.31.0.0
- C: 172.32.0.0
- D: More than one of the above
- E: All of the above


**q)** In a routing table, the entry 0.0.0.0/0
- A: Identifies the default gateway.
- B: Would never occur.
- C: Is used by DHCP
- D: Refers to the router in whose routing table in which the entry occurs.
- E: More than one of the above


**r)** Suppose a subnet is formed that contains the network range 169.1.64.0 to 169.1.127.255. The network address of this netblock (in CIDR) is
- A: 169.1.64.0/16
- B: 169.1.64.0/17
- C: 169.1.127.0/16
- D: 169.1.127.0/17
- E: 169.1.127.0/24


**s)** If a router send a Destination unreachable ICMP message, the value of the ICMP code field will
- A: Explain the reason the destination is unreachable.
- B: Always be 0 because the code field is not used for Destination unreachable.
- C: Is by definition 3 because the code that identifies Destination unreachable is 3.
- D: Is the IP address of the unreachable destination.
- E: None of the above


**t)** The notion of port forwarding is particularly important in the context of
- A: IPv4 routers
- B: IPv6 routers
- C: NAT boxes
- D: ICMP
- E: Anycasting


**u)** Which of the following IPv6 addresses are routable on the public Internet?
- A: 2001:4860:4860::8888
- B: fe80::44d8:2601:378b:a817
- C: fc::1
- D: ::ffff:192.168.4.3
- E: More than one of the above


**v)** The 'host' f.root-servers.net is
- A: A single (virtual or physical) computer with a single IP address.
- B: A distributed set of synchronised computers that all have the same IP address.
- C: A distributed set of synchronised computers that have different IP addresses.
- D: A distributed set of computers that operate independently, but all have the same address.
- E: A distributed set of computers that operate independently, and each of them has its own IP address.


**w)** Zero suppression in IPv6 refers to the fact that
- A: It is not necessary to use four hexadecimal digits for an address field if the field starts with one or more zeroes.
- B: One continuous sequence of zero-valued field in an address may be omitted and the omission is indicated using two adjacent colons.
- C: Multiple continuous sequences of zero-valued field in an address may be omitted and each omission is indicated using two adjacent colons.
- D: More than one of the above
- E: All of the above


**x)** In order to encrypt messages on each link between routers (rather than the entire path between a client and a server) the following standard would be useful:
- A: SSL
- B: TLS
- C: IPSEC
- D: More than one of the above
- E: All of the above


**y)** In networking tunneling refers to
- A: A mechanism to get blocked traffic via a firewall.
- B: The use of higher layer protocols lower in the stack than lower layer protocols.
- C: A routing mechanism that bypasses intermediate routers and therefore reduces the length of the path between a source and a destination.
- D: Encapsulating packets of one protocol in packets of another protocol, where the second protocol was not designed (or intended) to carry packets of the former protocol.
- E: Forwarding IPv4 traffic to hosts with IPv6 addresses.



---

## Short Answer / Structured Questions

### Question 2

* Name any five (5) fields in a TCP header, excluding the Flags field, as well as excluding any specific flags that may occur in the Flags field.

### Question 3

The 'code point' (or sequence number) of a Unicode character is written as 'U+' (to indicate that it is a Unicode code point), followed by the code of the character in hexadecimal. The Latin Capital letter Z is, for example, represented as U+005A. When UTF-8 representation is used, the shortest possible sequence of bytes will be used—hence the leading byte will never encode a 0 (except for the null character).

* **a)** Translate the following characters to UTF-8. In other words, provide the sequence of bytes (in hexadecimal) that would represent the character in UTF-8.
* (i) The Cyrillic capital letter A (U+0410)
* (ii) The Anchor Emoji (U+2693)


* **b)** Consider the following string encoded in UTF-8: F0 9F 96 A7 F0 9F 92 A9. Which Unicode code points does this string represent?

### Question 4

Unlike other IPv4 addresses the so-called class E IPv4 addresses all start with the bit pattern 1111, that are followed by 28 other bits. These class E addresses have been reserved for future use. Suppose IANA decides the future is now. These class E addresses are to be distributed as blocks of routable addresses amongst the five regional Internet registries. In alphabetic order, AfriNIC is the first of the five and RIPE the last of the five. IANA decides to number them from 0 to 4. In this sequence APNIC is therefore number 1, ARIN number 2 and LACNIC number 3. The division occurs exactly like subnetting with the proviso that each of these registries will get the largest possible block of addresses (with all blocks being of equal size). The numbers provided above serve as the number of the 'subnet' for each block.

* a) What is the network address of this class E address (in CIDR notation) before it is divided?
* b) What is the network address of the block assigned to LACNIC? Provide your answer in CIDR notation.
* c) ARIN decides it will split its block into at least 100 blocks (of the same size) that are as large as possible. While it will end up with more than 100 blocks, the last of these 100 (numbered 99) is allocated to an ISP called Acme. What is Acme's network address (in CIDR)?
* d) Acme decides to split its block into network addresses that would enable a customer to address more than 1000, but less than 2000 hosts. This effectively subnets Acme's block, with subnets numbered from 0. What is the network address that is based on Acme's subnet number 99? Provide your answer in CIDR notation.
* e) The customer who obtains this 'Acme subnet 99' convinces Acme to provide it with a supernet that includes 'Acme subnet 99' but allows them to address at least 3000, but not more than 5000 hosts. What is the network address of this supernet (in CIDR notation)?
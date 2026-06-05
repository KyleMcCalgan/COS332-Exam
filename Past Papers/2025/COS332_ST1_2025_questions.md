# COS332 Semester Test 1 2025 Questions

## Question 1

In each case, select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### 1.
A proprietary network protocol is a protocol that:

A. Has been standardised by some national standards body.  
B. Is owned by a specific vendor.  
C. Is developed as an open-source protocol.  
D. Is now so old that using it has been deprecated.  
E. Describes the properties of other network protocols.

### 2.
Which historical event had a profound impact on many design decisions for the Internet, or ARPAnet then?

A. Cold War  
B. Suez Canal Crisis  
C. Rise of the Global South  
D. Bay of Pigs Invasion  
E. Lockerbie Bombing

### 3.
When writing an application that will serve as a server in a client-server architecture, the application would, in its role as server, open a socket that would:

A. Be specified as an address and port number  
B. Initiate connections  
C. Wait for connections  
D. More than one of the above  
E. All of the above

### 4.
The phrase protocol stack is used in a network context because:

A. Protocols are "stacked" in layers on top of one another.  
B. A message is "pushed" down when transmitted and then "popped" at the receiving end, such that the most recently sent message is the first one that would be retrieved by the receiver.  
C. Alternative protocols may exist "next to" one another within the layers of protocols. Examples include IPv4 and IPv6.  
D. Many protocols on the higher layers, such as layer 4, tend to converge into one protocol, or very few protocols, on layer 4. From layer 4 it "spreads out" to many lower layer protocols, especially on layers 2 and 1.  
E. The notion of a protocol stack is not used in networking.

### 5.
The OSI layer that, amongst others, attempts to emulate database transactions where messages can be “rolled back” if the final message in a sequence is not sent, is layer:

A. 2  
B. 3  
C. 4  
D. 5  
E. 6

### 6.
Which ISO OSI layer is responsible for regulating which node is allowed to transmit next in cases where two computers are directly connected?

A. 5  
B. 4  
C. 3  
D. 2  
E. It may be 2 or 5 depending on factors not mentioned in the question.

### 7.
Protocols such as SMTP, POP3, and FTP are deemed to be application layer protocols. As such, they obviously include ISO OSI layer 7 functionality. In addition, they often include functionality associated with the following ISO OSI layer(s):

A. Only layer 6  
B. Layers 6 and 5  
C. Layers 5 and 4  
D. Layers 4 and 3  
E. Only layer 3

### 8.
The `nom.za` second-level domain is intended to allow ... to register subdomains within it.

A. Nomads  
B. Individuals  
C. Parties who handle nominations for potential office bearers  
D. Those who provide authoritative definitions of nomenclature  
E. None, because no such second-level domain exists

### 9.
The `.io` TLD is a(n):

A. sTLD  
B. ccTLD  
C. gTLD  
D. Reserved TLD  
E. None of the above

### 10.
A file on a name server that maps names to IP addresses is known as a ... file.

A. Name  
B. Hosts  
C. Mapping  
D. Resolution  
E. None of the above

### 11.
The `capetown.` sTLD has to adhere to policies prescribed by:

A. ICANN  
B. ZADNA  
C. ISO  
D. More than one of the above  
E. All of the above

### 12.
The primary metric used by interior gateway protocols is:

A. Cost  
B. Hop count  
C. Distance  
D. Static routing tables  
E. Speed  
F. Noise

### 13.
Consider a scenario in RIP where a router `r` sends its routing table to a router `s`. An entry in `r`’s table indicates that it can reach a network `n` at a cost of 5. Before receiving the message, the routing table at `s` indicated that it could reach `n` at a cost of 8. What will the cost from `s` to `n` be according to the routing table at `s` after `s` processes the message from `r`?

A. 5  
B. 6  
C. 7  
D. 8  
E. More information about `r` is required to answer the question.

### 14.
Which of the following protocols is/are examples of an external gateway protocol (EGP)?

A. BGP  
B. OSPF  
C. RIP  
D. More than one of the above  
E. All of the above

### 15.
Routers using OSPF broadcast their ... and use the received information to apply the ... algorithm.

A. Routing tables; Dijkstra  
B. Routing tables; Bellman-Ford  
C. Routing tables; RIP  
D. Version of the network topology; Dijkstra  
E. Version of the network topology; Bellman-Ford

### 16.
Which protocol is primarily intended to manipulate a mailbox on a server?

A. IMAP4  
B. POP3  
C. SMTP  
D. More than one of the above  
E. All of the above

### 17.
Which condition code will be returned by an SMTP server after successfully handling a HELO or EHLO message?

A. 0  
B. 150  
C. 250  
D. 350  
E. 450

### 18.
(i) How does a CGI program send output to a browser?  
(ii) How does a CGI program receive input from a browser?

A. (i) Writes to standard output; (ii) Reads from standard input  
B. (i) Writes to the appropriate socket; (ii) Reads from standard input  
C. (i) Writes to standard output; (ii) Reads from the appropriate socket  
D. (i) Writes to the appropriate socket; (ii) Reads from the appropriate socket  
E. (i) Writes to standard output; (ii) Reads an environment variable set by the server

### 19.
To avoid the need for the ... channel to connect to the FTP client, FTP ... mode should be used.

A. data, passive  
B. data, indirect  
C. data, reversed  
D. control, passive  
E. control, indirect  
F. control, reversed

### 20.
An agent that monitors and controls network activity in an SNMP-managed network node is a(n):

A. Client  
B. Server  
C. P2P-node  
D. More than one of the above  
E. All of the above

## Question 2 [5 marks]

Fill in the blanks in the following paragraph by providing the missing words or phrases on your answer sheet:

Sam finds that the domain `xx.co.za` was not renewed and is available for registration. Sam approaches xneelo to register this domain, which xneelo does. In this scenario, xneelo acts as the **[a]** of the domain when they add the domain to the `co.za` registry. The `co.za` registry is operated by **[b]**.

After registration, Sam performs a whois query for the domain on the registry; the addresses of three parties, who may be the same, are returned as a result. In sequence, the details of the **[c]**, as well as the information to contact the **[d]** and **[e]** "departments" associated with the domain. In this particular case, the latter two responses may provide contact details at xneelo.

However, in recent years, the returned information is often of little use, since it is typically **[f]**. As an aside, the whois service is usually associated with port **[g]**.

It may also be possible to retrieve whois information from a URL that uses domain name hacking and which is available at `https://`**[h]**.

Given that the `xx.co.za` is in South Africa, it, like other South African domain names, has to abide by the general Internet policies, as well as policies imposed by **[i]**. Recall that `za.` is a **[j]** TLD.

## Question 3 [5 marks]

Compile a zone file for a name server for the domain `xx.co.za`.

- Do not include the SOA (Start of Authority) entry.
- Only provide the other resource records (RRs) that are required based on the specification below.
- Provide one RR per line on your answer sheet.
- Omit the `IN` entry, used to indicate the record is for the Internet.
- In most cases, a resource record will consist of a triple:  
  `(name, type, value)`  
  but note the few exceptions to this format and handle them correctly.

Specification:

- `xx.co.za` exists as a single computer at address `41.203.18.59`.
- It hosts a web server accessible via `https://xx.co.za`.
- The same server is also accessible via `https://www.xx.co.za`, but the owner wants to avoid multiple RRs if the IP address changes.
- The primary mail server: `ASPMX.L.GOOGLE.COM`.
- The secondary mail server: `ALT1.ASPMX.L.GOOGLE.COM`.
- The primary name server: `ns1.host-h.net`.
- The secondary name server: `ns2.host-h.net`.
- The domain has a subdomain `abc.xx.co.za`, which uses the same name servers as the main domain.
- The IPv6 address of the computer is `2001::1234`.
- The owner wants DNS to indicate that this machine is a Raspberry Pi.

The SOA record, which you are to omit, indicates that this zone file is for `xx.co.za`. Therefore, all names you include in the zone file will be interpreted as prefixes to `xx.co.za`, and must not include `xx.co.za` itself.

Leave any unused lines blank.

## Question 4 [5 marks]

Assume the costs to transmit packets in a network are as follows, regardless of direction:

| Link | Cost |
|---|---:|
| A–B | 1 |
| A–F | 10 |
| B–C | 6 |
| B–E | 1 |
| C–D | 1 |
| D–E | 3 |
| E–F | 2 |

You are applying Dijkstra’s algorithm to determine the cheapest routes from node A.

- At the end of iteration 1, you determine that routing to neighbour B, at a cost of 1, is the cheapest alternative at this stage.
- At the start of iteration 2, you add B to the set of finalised nodes, and then consider the neighbours of this updated set.

Answer the following questions based on your continued application of Dijkstra’s algorithm:

**a)** Which node is picked as the cheapest alternative at the end of iteration 3?

**b)** After completing iteration 3, but before starting iteration 4, what is the cost to reach node C from node A?

**c)** After completing iteration 3, but before starting iteration 4, which node will, at this stage, finally deliver a packet en route to node C?

**d)** Which node is added to the set of finalised nodes at the end of iteration 4?

**e)** After completing iteration 4, but before starting iteration 5, what is the cost to reach node C from node A?

## Question 5 [5 marks]

**a)** On Unix and Linux systems, BIND is a popular name server. What does the "d" in BIND stand for?

**b)** Apache is a well-known server — particularly, but not solely, on Linux systems. Apache is typically deployed to handle a specific protocol. Name the protocol. If the protocol has encrypted and non-encrypted variants, name the variant that does not use encryption.

**c)** What service does the Telnet protocol offer?

**d)** When a DNS server converts a domain name to an IP address, the correct terminology would be that the server _____ the domain name.

**e)** The Linux file `/etc/hosts` contains a list of pairs. Each pair consists of two entries separated by a space. The second entry is a name. What is the first entry of each pair?

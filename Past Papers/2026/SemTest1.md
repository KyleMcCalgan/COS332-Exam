# COS332 Semester Test — Questions

**Course:** Computer Science  
**Paper:** COS332  
**University of Pretoria**  
**Semester Test:** 19 March 2026  
**Time:** 90 minutes  
**Marks:** 40

This paper consists of 12 pages.

Answer all questions. Casio scientific (or equivalent) calculators are permitted, as well as simple 5-function calculators. If a question can be answered using an acronym, only the acronym is required. You are allowed to write on this test paper.

---

## Question 1

In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### 1. Which ISO OSI layer provides process-to-process delivery?

A. 2  
B. 3  
C. 4  
D. 6  
E. 7

### 2. The RIR for Europe is

A. RIPE  
B. EuriNC  
C. EuroNIC  
D. EurIN  
E. EPIR

### 3. When writing an application that will serve as a server in a client-server architecture, the application would, in its role as server, open a socket that would

A. Be specified as an address and port number  
B. Initiate connections  
C. Wait for connections  
D. More than one of the above  
E. All of the above

### 4. Layers 1 to 4 of the ISO OSI model are known as the

A. Network-oriented layers  
B. Application-oriented layers  
C. TCP/IP-oriented layers  
D. More than one of the above  
E. None of the above

### 5. A layer on a protocol stack communicates with its peer layer. Suppose node X sends a message to node Y. Which node's (or nodes') layer 3 is/are deemed to be the peer(s) of layer 3 of X?

A. Only Y.  
B. All the nodes on the path after X, up to and including Y.  
C. All the nodes on the path from X (including X), up to and including Y.  
D. Only the router nodes on the path after X, up to and including Y, which excludes most nodes on this path.  
E. Only the first router after X on the path to Y.

### 6. Which protocol is primarily intended to manipulate a mailbox on a server?

A. IMAP4  
B. POP3  
C. SMTP  
D. More than one of the above  
E. All of the above

### 7. To avoid the need for the ... channel to connect to the FTP client, FTP ... mode should be used.

A. data, passive  
B. data, indirect  
C. data, reversed  
D. control, passive  
E. control, indirect  
F. control, reversed

### 8. 

(i) How does a CGI program send output to a browser?  
(ii) How does a CGI program receive input from a browser?

A. (i) Writes to standard output; (ii) Reads from standard input  
B. (i) Writes to the appropriate socket; (ii) Reads from standard input  
C. (i) Writes to standard output; (ii) Reads from the appropriate socket  
D. (i) Writes to the appropriate socket; (ii) Reads from the appropriate socket  
E. (i) Writes to standard output; (ii) Reads an environment variable set by the server

### 9. The most important routing protocol at JINX is

A. RIP  
B. BGP  
C. OSPF  
D. Dijkstra  
E. Bellman-Ford

### 10. The primary metric used by interior gateway protocols is

A. Cost  
B. Hop count  
C. Distance  
D. Static routing tables  
E. Speed  
F. Noise

### 11. Routers using OSPF broadcast their ... and use the received information to apply the ... algorithm.

A. Routing tables; Dijkstra  
B. Routing tables; Bellman-Ford  
C. Routing tables; RIP  
D. Version of the network topology; Dijkstra  
E. Version of the network topology; Bellman-Ford

### 12. An agent that monitors and controls network activity in an SNMP-managed network node, is a(n)

A. Client  
B. Server  
C. P2P-node  
D. More than one of the above  
E. All of the above

### 13. If the FQDNs of DNS root name servers are ordered lexicographically, the last entry in the list is

A. b.dns.net  
B. m.dns.net  
C. n.dns.net  
D. l.root-servers.net  
E. m.root-servers.net

### 14. The bulk, if not all, of the resource records in the DNS root name servers are of the following type(s):

A. A  
B. MX  
C. NS  
D. More than one of the above  
E. All of the above

### 15. When an email is sent using SMTP the `From:` header displayed to the recipient is, in the vast majority of cases, based on

A. What was included as the parameter to the `rcpt from:` SMTP command.  
B. What was included as the parameter to the `helo` or `ehlo` SMTP command.  
C. The domain of the user from where the email originated.  
D. A header included as part of the message that followed the `data` SMTP command.  
E. What was included as the parameter to the `mail from:` SMTP command.

### 16. Which of the following is a popular application used to inspect traffic that flows on a network?

A. SniffAndSnort  
B. `telnet`  
C. `nslookup`  
D. `tracert` / `traceroute`  
E. Wireshark

### 17. The ASCII standard standardises a(n) ... character code.

A. 7-bit  
B. 8-bit  
C. 9-bit  
D. More than one of the above  
E. All of the above

### 18. Consider the following protocol negotiation string in an HTTP request:

```http
Accept-Charset: iso-8859-1, utf-8, utf-16, *;q=0.1
```

Suppose the server supports `iso-8859-1`, `utf-8` and `Shift_JIS`. The response may then be encoded using

A. `iso-8859-1`  
B. `utf-8`  
C. `Shift_JIS`  
D. Any of the encodings listed as options above.  
E. One of two of the encodings listed as options above.

### 19. Which of the following characters is not present in standard ASCII?

A. `A`  
B. `&`  
C. `#`  
D. `£`  
E. `~`

### 20. The popular network software known as `bind`

A. Acts as a name server.  
B. Connects two processes to facilitate communication.  
C. Associates a process with a port.  
D. Is used to authenticate a user.  
E. More than one of the above.

---

## Question 2

a) Which gTLD is used by American universities?

b) What is the process of converting a fully qualified domain name to an address called?

c) To create the domain `xx.co.za` the registrar of `co.za` has to insert NS entries in the `co.za` zone file; these NS entries will point to the name servers of the new domain. What is the process of inserting such entries called? *(Hint: Phrased somewhat differently, the registrar has to ... authority; the missing word should assist you to find the answer.)*

d) Who is in control of the `za.` ccTLD? Provide the acronym used by this entity; the question does not refer to the `co.za` registry operator, nor to entities that exert control over all TLDs.

e) Which committee has the authority to approve new top-level domains? Provide the acronym that identifies this committee.

---

## Question 3

In some network nodes P and Q are neighbours. Communication between them costs 6 units. Below, the partial routing tables at P and Q are provided at some initial time $t_0$. Each entry in a routing table is a triple consisting of a destination, the next hop en route to that destination and the total cost of sending data to the destination via the current route. The network uses the Bellman-Ford algorithm.

At some time $t_1$, Q shares its routing table with P, and P makes all the updates it can, based on the received information. At some later time $t_2$, P shares its updated routing table with Q and Q makes all the updates it can, based on the received update.

The questions below consist of a node (P or Q), a time ($t_1$ or $t_2$) and a destination. You are expected to consult the routing table of the node as updated by the shared information at the time noted, and provide the next-hop and cost for the destination mentioned. As an example, the initial entry in P's table for destination Q is `(P, Q, 6)`. The information received by P at time $t_1$ does not affect this entry and it therefore remains `(P, Q, 6)` after $t_1$. Therefore, the expected answer for the question "P after $t_1$" would be "Q, 6".

### Initial routing table at P

| Destination | Next hop | Cost |
|---|---:|---:|
| A | M | 15 |
| B | M | 22 |
| F | L | 14 |
| H | Q | 18 |
| K | K | 6 |
| L | K | 7 |
| R | Q | 12 |
| U | Q | 11 |

### Initial routing table at Q

| Destination | Next hop | Cost |
|---|---:|---:|
| A | P | 21 |
| C | D | 15 |
| H | P | 12 |
| K | P | 14 |
| R | R | 6 |
| U | U | 5 |
| Z | Z | 7 |

Answer the following:

a) $t_1$, C =  
b) $t_1$, H =  
c) $t_2$, K =  
d) $t_2$, H =  
e) $t_2$, Z =  

---

## Question 4

### a) Convert the following Unicode characters to UTF-8.

(i) `U+00E4`  
(ii) `U+039E`  
(iii) `U+179F`  
(iv) `U+1F9A7`

### b) Consider the following sequence of bytes. It is UTF-8 encoded, but contains some errors. Decode the characters that are properly encoded, and list them one per line in the sequence in which they occur in the byte sequence, and write them on the answer sheet separated by commas, for example `U+1234`, `U+5678`. Ignore any bytes in the byte string that do not form part of a complete UTF-8 character.

```text
EF BB AF BC C2 AA F1 83
E0 AA AA F0 90 AB C3 D5
```

---

## Question 5

The code provided below forms part of a possible submission for practical assignment 3 in a Java-like language. Recall that this assignment required you to implement a web server that emulated a clock; when one clicked on the name of a city, the local time in that city would be displayed. It should be simple enough to follow even for those not quite familiar with Java.

To help those not quite familiar with Java, consider line 06 as an example. The variable `rL` is declared and read. It reads a line from the socket just opened; hence it would read the first line of the HTTP request.

Next, consider line 08. It defines `rT` as a character `String` array with as many elements as required (indexed from 0). The content of `rL` is split into several strings; the split is made wherever a space occurs in this character string. Every substring is then stored into a subsequent element of `rT`. Hence, if the line `ab cd ef` was read, then `rT[0]` would be `ab`, `rT[1]` would be `cd` and `rT[2]` would be `ef`.

Study the code fragment and then answer the following questions. Answer the questions in terms of the protocol and not by just explaining what the code does. If you are, for example, asked about line 06 it would not be worth any marks to say that a line is read from the socket and stored in `rL`. As you know, an HTTP request consists of several lines; from studying the code, it should be clear that line 06 reads the first line of the HTTP request. Mentioning the HTTP request turns the answer into one that says something about the protocol. Please omit the initial words of your answer, such as "Its purpose is to"; start writing your answer with the word that would follow such an introduction.

a) Very briefly explain the purpose of line 17.  
b) Very briefly explain the purpose of line 18.  
c) Very briefly explain the purpose of line 19.  
d) Very briefly explain the purpose of line 24.  
e) What should the missing code in line 13 do?

```java
01  while (true) {
02      Socket clientSocket = serverSocket.accept();
03      BufferedReader in = new BufferedReader(new
            InputStreamReader(clientSocket.getInputStream()));
04      OutputStream out = clientSocket.getOutputStream();

06      String rL = in.readLine();

07      if (rL != null) {
08          String[] rT = rL.split(" ");
09          String rM = rT[0];
10          String rU = rT[1];

12          if (rM == "HEAD") {
13              ...
14          }

16          else if (rM == "GET") {
17              out.write("HTTP/1.1 200 OK\r\n");
18              out.write("Content-Type: text/html\r\n");
19              out.write("\r\n");
20              if (rU.startsWith("/?City=")) {
21                  ...
22                  String ExtractedcityName = rU.substring(7);
23                  ...
24                  out.write("<!DOCTYPE html>");
25                  out.write("<html><head>");
26                  out.write("<meta http-equiv=\"REFRESH\" content=\"4\">");
27                  out.write("<title> World Clock </title>");
28                  ...
29              }
30              else {
31                  ...
32              }
33          }
34          out.close();
35          in.close();
36          clientSocket.close();
37      }
38  }
```

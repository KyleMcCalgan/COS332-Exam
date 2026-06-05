# COS332 Semester Test 1 — 2024 Questions

**University of Pretoria**  
**Course:** Computer Science  
**Paper:** COS332  
**Semester Test:** 18 March 2024  
**Time:** 1 hour  
**Marks:** 40

## Instructions

- Answer all questions.
- No calculators permitted.
- If a question can be answered using an acronym, only the acronym is required.
- You are allowed to write on this test paper.
- Marks add up to 41; the paper is worth 40 marks.

---

## Question 1

In each case select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### a)
When the ISO and the IEEE both issue standards for the same artefact, architecture or process and the standards disagree:

A. The ISO standard takes precedence.  
B. The IEEE standard takes precedence.  
C. Both standards should be ignored until they have been harmonised.  
D. For engineering cases the IEEE standard has precedence, while the ISO standard takes precedence in most other cases.  
E. It does not matter, because standards are not binding. Adoption of standards may be mandated by processes outside the standards bodies, though.

### b)
IEEE 802.11ax is better known as:

A. WiFi 3  
B. WiFi 4  
C. WiFi 5  
D. WiFi 6  
E. WiFi 7

### c)
Which historical event had a profound impact on many design decisions for the Internet or ARPAnet then?

A. Cold War  
B. Suez Canal Crisis  
C. Rise of the Global South  
D. Bay of Pigs Invasion  
E. Lockerbie Bombing

### d)
The RIR for Europe is:

A. RIPE  
B. EurNIC  
C. EuroNIC  
D. EurIN  
E. EPIR

### e)
Which ISO OSI layer is responsible for regulating which node is allowed to transmit next in cases where two computers are directly connected?

A. 5  
B. 4  
C. 3  
D. 2  
E. It may be 2 or 5 depending on factors not mentioned in the question.

### f)
The phrase *protocol stack* is used in a network context because:

A. Protocols are “stacked” in layers on top of one another.  
B. A message is “pushed” down when transmitted and then “popped” at the receiving end such that the most recently sent message is the first one that would be retrieved by the receiver.  
C. Alternative protocols may exist “next to” one another within the layers of protocols. Examples include IPv4 and IPv6.  
D. Many protocols on the higher layers, such as layer 4, tend to converge into one protocol or very few protocols on layer 4. From layer 4 it “spreads out” to many lower layer protocols, especially on layers 2 and 1.  
E. The notion of a protocol stack is not used in networking.

### g)
Protocols such as SMTP, POP3 and FTP are deemed to be application layer protocols. As such they obviously include ISO OSI layer 7 functionality. In addition they often include functionality associated with the following ISO OSI layer(s):

A. Only layer 6  
B. Layers 6 and 5  
C. Layers 5 and 4  
D. Layers 4 and 3  
E. Only layer 3

### h)
When an email client, such as Outlook or Thunderbird, transmits an email via SMTP, in practice, it may usually connect to the following port(s) for cleartext transmissions:

A. 25  
B. 110  
C. 587  
D. More than one of the above  
E. Any of the above

### i)
Suppose one searches the Internet for SMTP servers. This may, for example, be done by crawling the Internet and attempting to connect to the relevant SMTP ports and initiating the SMTP exchange of messages. Those where one is able to successfully exchange more than one request and response are deemed to be SMTP servers. Note that one may increase the chances of finding SMTP servers by targeting hosts where the FQDN starts with `mail` or `smtp`.

Suppose that for any such server, one continues with the exchange of SMTP requests to send an email from `a@xx.co.za` to `b@xx.org.za`. In general one would observe the following outcome:

A. The server accepts the requests and forwards the message to `xx.org.za` for further processing.  
B. The server accepts the requests, but discards the message without an error message.  
C. The server accepts the requests, discards the message, and sends an error message to `a@xx.co.za`.  
D. The server continues the interaction, but reports that it does not relay messages. The message is never accepted.  
E. None of the above, because it is impossible to find SMTP servers that will initiate a conversation without first requiring login credentials.

### j)
When an email is sent using SMTP the `From:` header displayed to the recipient is, in the vast majority of cases, based on:

A. What was included as the parameter to the `rcpt from:` SMTP command.  
B. What was included as the parameter to the `helo` or `ehlo` SMTP command.  
C. The domain of the user from where the email originated.  
D. A header included as part of the message that followed the `data` SMTP command.  
E. What was included as the parameter to the `mail from:` SMTP command.

### k)
After an SMTP client has sent a `data` command, it will usually send several lines of data. It signals to the server that the entire data block has been transmitted by sending the following line:

A. `/data`  
B. `quit`  
C. `.`  
D. A blank line  
E. `fin`

### l)
The `Host:` line, including the name of the host as specified in the URL, forms one of the headers in an HTTP GET request. Why is it necessary?

A. Security/access control. A user should not be able to access an unknown web server using only the address of the server.  
B. Security/integrity. Connecting to the server and informing the server about the expected domain ensures that an incorrect site would not be served.  
C. Virtual hosting. The server may host more than one site.  
D. There is no such `Host:` header.  
E. There is no GET request in HTTP. Some other HTTP requests may include a `Host:` header.

### m)
FTP is based on the ... architecture.

A. Client-server  
B. Peer-to-peer  
C. Client-server-client-server  
D. Host-to-host  
E. Multitier

### n)
Suppose user `u` is using server `s` from workstation `w`. User `u` sees graphical output on `w` that is produced on `s`. Which protocol(s) may be used to transfer the images from `s` to `w`?

A. X11  
B. Telnet  
C. HTML  
D. More than one of the above  
E. Any of the above

### o)
A program that wants to open a socket in order to act as a server needs to specify the following:

A. The address of the server  
B. The address of the client  
C. The port on the server  
D. The port on the client  
E. More than one of the above

### p)
(i) How does a CGI program send output to a browser?  
(ii) How does a CGI program receive input from a browser?

A. (i) Writes to standard output; (ii) Reads from standard input  
B. (i) Writes to the appropriate socket; (ii) Reads from standard input  
C. (i) Writes to standard output; (ii) Reads from the appropriate socket  
D. (i) Writes to the appropriate socket; (ii) Reads from the appropriate socket  
E. (i) Writes to standard output; (ii) Reads an environment variable set by the server

### q)
A file on a name server that maps names to IP addresses is known as a ... file.

A. Name  
B. Hosts  
C. Mapping  
D. Resolution  
E. None of the above

### r)
When one enters the command:

```text
nslookup ns1.up.ac.za 8.8.8.8
```

A. `ns1.up.ac.za` will be resolved using the default DNS server and `8.8.8.8` will be ignored.  
B. `ns1.up.ac.za` will be resolved using the default DNS server and `8.8.8.8` will be reported as `8.8.8.8`, since it is already an IP address.  
C. `ns1.up.ac.za` will be resolved using the default DNS server and `8.8.8.8` will be reverse resolved to `dns.google` using the same server.  
D. `8.8.8.8` will be reverse resolved to `dns.google` using `ns1.up.ac.za`.  
E. `ns1.up.ac.za` will be resolved using `dns.google`.

### s)
To determine the address of a `.com` name server, one would set the query type to NS and then submit the following query for resolution:

A. `.com`  
B. `com`  
C. `*.com`  
D. `com.`  
E. `com.root`

### t)
The `.io` TLD is a(n):

A. sTLD  
B. ccTLD  
C. gTLD  
D. Reserved TLD  
E. None of the above

---

## Question 2 [5 marks]

As a message moves down the protocol stack, headers are typically added on each layer and then interpreted and removed by the peer layer. The headers that are thus added consist of various fields. For this question you are expected to provide one example of a field that may be added on the indicated layer. Remember to include “source” or “destination” as part of the field name where appropriate.

The header added for the application layer obviously depends on the specific application layer protocol. Assume HTTP is used; a request is sent from a browser to a server. Just provide a name for any header field, rather than a complete line from the header.

Provide one field for each of the following layers:

- 7
- 6
- 4
- 3
- 2

---

## Question 3 [5 marks]

At the time of setting this paper, the IP address of `xx.co.za` was `41.203.18.59`.

### a)
Provide a command that, when entered on the CLI of a typical modern operating system, will determine the current IP address of `xx.co.za`.

### b)
Name a FQDN that would provide ownership information of a domain such as `xx.co.za`, unless the ownership information has been redacted. The FQDN should exist and use domain name hacking.

### c)
Which type of organisation stores ownership information of domains such as `xx.co.za`?

### d)
Which type of organisation stores ownership information of IP addresses, such as `41.203.18.59`?

**Note:** An ISP owns the address; hence the question is where information about such an owning ISP is stored.

### e)
Assuming `41.203.18.59` is located in South Africa, name the organisation where WHOIS details of `41.203.18.59` can be obtained.

---

## Question 4 [5 marks]

Consider the Telnet protocol.

### a)
What is the intended purpose of Telnet? Provide your answer as a descriptive phrase, rather than stating that it enables one to execute commands on remote computers.

### b)
Which well-known port is typically used by a Telnet server?

### c)
Suppose you are using a Telnet server. The outputs of your commands are displayed correctly. However, whenever you type something at the client, you cannot see what you are typing. Which property should you adjust at the client to rectify the problem?

### d)
Suppose you want to use the Telnet client to interact with `www.example.com` using manually entered HTTP commands. Provide the full command you will enter on the command-line interface to open the connection.

### e)
When opening a Telnet connection, the Telnet client displays a character combination that one may enter to open the Telnet console. This is often `^]`. What is this sequence called by the client?

---

## Question 5 [6 marks]

Consider the following zone files at various DNS servers. Assume that records and fields that are not shown, such as SOA records, are not material.

| Server | Records |
|---|---|
| 2 | `a A 11`<br>`b A 7`<br>`a NS 4`<br>`b NS 6` |
| 3 | `a A 13`<br>`b A 10`<br>`a NS 2`<br>`b NS 5` |
| 4 | `a A 14`<br>`b A 15`<br>`a NS 2`<br>`b NS 5` |
| 5 | `a A 3`<br>`b A 5`<br>`a NS 9`<br>`b NS 2` |
| 9 | `a A 4`<br>`b A 3`<br>`a NS 3`<br>`b NS 4` |
| 10 | `a A 8`<br>`b A 12`<br>`a NS 3`<br>`b NS 5` |

Note that these files break some of the rules for zone files; the root name server, for example, contains A resource records. A number of entries create cycles. However, these issues are not material for the questions that follow. The number in bold at the top of each table is the address of the node on which that zone file occurs.

**Node 5 is the root name server.**

Perform recursive name resolutions for the following FQDNs, for the query provided. If the FQDN is preceded by an `NS`, you should perform an NS query. If the FQDN is preceded by an `A`, you should perform an A query. Write the address found as a single number, or write `N/A` if the query cannot be resolved with the information provided.

### a)
`NS b.a`

### b)
`A b.a`

### c)
`NS a.a.a`

### d)
`A a.a.a`

### e)
`NS a.b`

### f)
`A b.a.b`

---

**Total: 40 marks**

**End of paper**

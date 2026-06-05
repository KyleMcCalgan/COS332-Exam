# COS332 Semester Test 2 2025 Questions

## Question 1

In each case, select the alternative that fits the question best and write only the corresponding letter on your answer sheet.

### 1.
If MIME is deemed to be a data communications protocol, it would fit best on layer ... of the ISO OSI model:

A. 7  
B. 6  
C. 5  
D. 4  
E. 3

### 2.
Which character set is assumed to be understood by all parties involved in an HTTP exchange?

A. ASCII  
B. EBCDIC  
C. Unicode  
D. UTF-8  
E. ISO-8859-1

### 3.
Consider the following protocol negotiation string in an HTTP request:

```http
Accept-Charset: iso-8859-1, utf-8, utf-16, *;q=0.1
```

Suppose the server supports `iso-8859-1`, `utf-8`, and `Shift_JIS`. The response may then be encoded using:

A. iso-8859-1  
B. utf-8  
C. Shift_JIS  
D. Any of the encodings listed as options above  
E. One of two of the encodings listed as options above

### 4.
Which of the following is not a valid MIME type?

A. binary  
B. example  
C. image  
D. message  
E. model

### 5.
Suppose a message consists of JPG images embedded in HTML text. Which MIME type and subtype will be used to describe the message?

A. text/plain  
B. text/html  
C. image/jpeg  
D. multipart/mixed  
E. multipart/alternative

### 6.
Suppose an email consists of a message encoded in HTML and a JPG image, both included in the message. These two items are the only components of the email message. Which MIME type will be used to describe the entire email message?

A. application/email  
B. application/rfc822  
C. multipart/alternative  
D. multipart/mixed  
E. text/html

### 7.
How many Unicode characters can, in principle, be represented in UTF-8 using exactly four bytes? If the answer is expressed in the form 2ⁿ, what is the value of n?

A. 14  
B. 20  
C. 21  
D. 22  
E. 27

### 8.
Consider the byte sequence `D7 E5`. The Unicode character represented by this UTF-8 encoding is a(n):

A. Accented character  
B. Greek character  
C. Emoji  
D. Punctuation mark  
E. D7 E5 is not a valid UTF-8 encoding

### 9.
A BER value in ASN.1 is, in principle, encoded as a triple consisting of:

A. A type, a subtype and a value  
B. A type, a length and a value  
C. A constructor and two operands  
D. A variable name, as well as its minimum and maximum values  
E. The same value encoded in binary, text, and hexadecimal

### 10.
Which of the following is not a valid data type in ASN.1?

A. STRUCT  
B. CHOICE  
C. SEQUENCE  
D. ARRAY  
E. INTEGER

### 11.
The syntactic structure of an ASN.1 message is defined using:

A. A grammar  
B. An informal description in natural language  
C. A diagrammatic depiction of the message  
D. A bit pattern  
E. A list of the types of the components of the message

### 12.
The OSI layer that, among others, attempts to emulate database transactions where messages can be “rolled back” if the final message in a sequence is not sent, is layer:

A. 2  
B. 3  
C. 4  
D. 5  
E. 6

### 13.
Which of the following data streams generally work(s) better with an unreliable Layer 4 protocol?

A. Web page  
B. File transfer  
C. Audio  
D. More than one of the above  
E. All of the above

### 14.
Which of the following protocol(s) is/are used on the transport layer by DNS?

A. TCP  
B. UDP  
C. IP  
D. More than one of the above  
E. All of the above

### 15.
Which command enables one to see the status of transport layer connections on a host, in most operating systems?

A. netstat  
B. ping  
C. tracert / traceroute  
D. tcp-show  
E. ps

### 16.
UDP uses the following flow-control mechanism:

A. Stop and Wait  
B. Sliding Window  
C. Unrestricted  
D. More than one of the above  
E. All of the above

### 17.
A sends a TCP segment to node B. The acknowledgement field contains the value 150. The ACK flag is not set. This means:

A. B may assume that bytes up to byte 149 that it had sent are acknowledged  
B. A should disregard the value 150 — it has no meaning  
C. This is a negative acknowledgement of the segment B has sent that had the sequence number 150  
D. The TCP layer at A is misconfigured; it should have set the ACK flag  
E. More than one of the above

### 18.
Which of the following fields does not occur in a TCP header?

A. Source port  
B. Window advertisement  
C. Sequence number  
D. Options  
E. Length

### 19.
Which of the following statements is/are false about phantom bytes used in an initial 3-way TCP/IP handshake?

A. It is counted as part of the SYN message  
B. It is counted as part of the SYN+ACK message  
C. It is counted as part of the ACK message  
D. It consists of one byte of data  
E. More than one of the statements above are false

### 20.
A TCP connection in the TIME-WAIT state means that:

A. The node is waiting for data from the node that it is connected to  
B. The connection is about to time-out if no further data is transmitted soon  
C. The connection will soon be established, as soon as the handshake is completed  
D. The node is waiting for ‘lost’ traffic to arrive at the port that is no longer in use, before it will be available for reuse  
E. The network is congested

### 21.
A TCP node that is in the LISTEN state:

A. Is acting as a server and waiting for a SYN message  
B. Is acting as a client and has sent a SYN message  
C. May act as a client after sending a SYN message  
D. More than one of the above  
E. None of the above

### 22.
What does the claim that QUIC is a quick protocol mean?

A. It manages the lower layers to transmit raw data at higher bit rates  
B. It reduces latency when establishing or re-establishing a connection  
C. Where multiple parts of a message must be transported, it ensures that parts of the message are delivered quickly even if some parts are delayed  
D. More than one of the above  
E. All of the above

### 23.
QUIC connections can migrate. Which party can initiate such a migration in QUICv1 or QUICv2?

A. The client  
B. The server  
C. The network management system  
D. More than one of the above  
E. All of the above

### 24.
The RIR for Europe is:

A. RIPE  
B. EurNIC  
C. Euronic  
D. EurIN  
E. EPIR

### 25.
If one sends a message to an IP multicast address, the message will be delivered to:

A. The node to which that IP address has been assigned  
B. All nodes on the local network  
C. All nodes that are members of some group  
D. The network itself, rather than to a host on the network  
E. The network gateway that connects the network to other networks

## Question 2 [10 marks]

All values in this question are expressed in hexadecimal notation.

Convert the following Unicode characters to byte sequences. Represent byte sequences as 2-digit hexadecimal numbers with a space between all bytes. Your answers should resemble a format like: `12 bf 3a`.

**a)** `U+1842`

**b)** `U+10AD0`

**c)** `U+2CA0`

UTF-8 encoding is self-synchronising. Consider the following byte sequence, which is not a valid UTF-8 encoding:

```text
47 CE B5 C4 85 E1 80 AA E1 9C A0
BA AD F0 90 8F 8C 57 73 E1 83 A8
```

**d)** Provide the first valid Unicode character that occurs in this sequence. Format: `U+xxxx`.

**e)** Provide the second valid Unicode character that occurs in this sequence. Format: `U+xxxx`.

**f)** Provide the subsequence of bytes that are invalid.

**g)** Convert the bytes starting at the point where synchronisation is re-established, extract the first Unicode character formed. Format: `U+xxxx`.

**h)** Provide the last valid Unicode character in this sequence. Format: `U+xxxx`.

We did not discuss UTF-16 and UTF-32 in detail, but UTF-16 represents Unicode characters using 16-bit words. UTF-32 uses 32-bit words. When represented as bytes, endianness matters: Big-endian means `1234 → 12 34`, and `12345678 → 12 34 56 78`. Use big-endian representations for the following:

**i)** Represent `U+0048` in UTF-16 as a byte sequence.

**ii)** Represent `U+0F40` in UTF-32 as a byte sequence.

## Question 3 [5 marks]

Very briefly state what happens when the following TCP timers expire.

Keep your answers short and precise. For example, if expiration of a timer causes a segment to be transmitted, simply state: A segment containing data is transmitted.

**a)** Retransmission timer

**b)** Acknowledgement timer

**c)** Persistence timer

**d)** Keepalive timer

**e)** Quiet timer

## Question 4 [5 marks]

TCP is a reliable protocol. List five mechanisms used by TCP to provide this reliability. Keep your answers brief; no explanation are required.

## Question 5 [5 marks]

Answer the following questions about IPv4 addresses. Use CIDR notation for all your answers.

**a)** Which IPv4 address is used in a routing table to indicate that the routing table entry points to the default gateway?

**b)** A block of 256 ‘class C’ network addresses is reserved for private use. Provide the first-class C network address that occurs within this block.

**c)** A block of 16 ‘class B’ network addresses is reserved for private use. Provide the last class B network address that occurs within this block.

**d)** `137.215.98.140` is a host on the University of Pretoria network. What is the UP-network address?

**e)** `8.8.8.8` is a popular DNS server provided by Google. If this address were still part of a class-based address, what would the broadcast address on this network be?

Please recall that CIDR notation has to be used for all your answers in this question.

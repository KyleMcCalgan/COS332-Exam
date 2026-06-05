### Layer 6: The Presentation Layer Notes

The presentation layer (Layer 6) is responsible for encoding and decoding information so that data can be effectively represented on a network and accurately presented at its destination. It acts as a translator between application needs and the network's constraints, utilizing codecs (coders/decoders) to compress, encrypt, and format data for transmission. **If an application protocol like MIME is deemed a data communications protocol, it fits best on Layer 6 of the ISO OSI model**.

#### 1. Representing Text and Character Sets

- **Basic Character Encoding:** Computers rely on numerical codes to represent characters, utilizing standards like **ASCII (which explicitly standardises a 7-bit character code)**, EBCDIC (often used on mainframes), and Unicode. If two computers use different encodings, Layer 6 translates the data; for example, Computer A might send the word 'ABC' in ASCII, which is translated to Unicode for network transit, and finally translated into EBCDIC for Computer E.
- **The Diacritical Marks Problem:** Standard 7-bit ASCII lacks symbols like the British Pound (£), Euro (€), Yen (¥), and accented characters. Extended 8-bit ASCII versions added 128 extra characters, but different systems assigned different characters to these new slots. This causes presentation errors: if the sender and receiver use different extended ASCII tables, **punctuation marks and characters may not be communicated correctly**. For instance, a sentence like "Zoë’s résumé" might incorrectly display as "Zoϕ’s rδsumδ".
- **Solutions for Compatibility:**
    - **Standardization:** Using a universal set like Unicode to express almost all characters globally.
    - **Minimal Shared Sets:** Forcing the use of universally understood characters, a concept advocated by campaigns like the ASCII Ribbon Campaign for sending universally readable plain-text emails.
    - **Negotiation:** A client device explicitly tells a server which character sets it accepts (e.g., an HTTP header `Accept-Charset: iso-8859-1, utf-8, utf-16, *;q=0.1`), allowing the server to pick an optimal match or fall back to alternatives. **If the server supports iso-8859-1, utf-8, and Shift_JIS, the response may be encoded using one of the compatible options explicitly listed (e.g., iso-8859-1 or utf-8)**. **Furthermore, if no specific negotiation occurs, the ISO-8859-1 character set is generally assumed to be understood by all parties involved in an HTTP exchange**.
- **UTF-8 Encoding:** A variable-length Unicode standard that uses between 1 and 6 octets (bytes) per character **(though 4 bytes are standard for modern implementations, allowing up to 2²¹ characters to be represented)**. Standard English ASCII fits into one byte, while special characters might require two or three octets. UTF-8 is self-synchronizing, meaning if data is corrupted in transit, the system can skip corrupted bytes and immediately identify the start of the next character by looking for a byte that does not start with the binary sequence `10`.
    - **Byte Patterns for calculations:**
        - 1-byte: `0xxxxxxx`
        - 2-byte: `110xxxxx 10xxxxxx`
        - 3-byte: `1110xxxx 10xxxxxx 10xxxxxx`
        - 4-byte: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`
- **UTF-16 and UTF-32 Encoding:** **Other Unicode representations include UTF-16 (using 16-bit words) and UTF-32 (using 32-bit words). When converting to byte sequences, endianness dictates the order. In big-endian representation, the most significant bytes are placed first (e.g., the 16-bit `U+0048` becomes `00 48`)**.

#### 2. Markup Languages and Abstract Syntax

- **Separating Intent and Representation:** Instead of assigning unique binary codes to accented characters or specific fonts, markup languages use tags to apply formatting.
- **Formal Grammar Specifications:** Formal grammars like BNF (Backus-Naur Form) and its variants (EBNF, ABNF) dictate the exact syntax of protocols. EBNF is **standardised in an RFC which is deemed as the authoritative definition**. For example, the HTTP specification relies on augmented BNF to strictly mandate request formats. **Similarly, the syntactic structure of an ASN.1 message is strictly defined using a grammar**.
- **Abstract Syntax Notation One (ASN.1):** While XML is human-readable but consumes excessive network bandwidth, ASN.1 provides an abstract, highly efficient description of data structures. It relies on data constructors like `SEQUENCE`, `CHOICE`, and `SET`. **(`STRUCT`, `ARRAY` and `MESSAGE` are not valid ASN.1 types/constructors)**.
    - _Example:_ An academic record might use a `SEQUENCE` for biographical details, contain a `SET` of passed courses, and use a `CHOICE` field allowing either a street address or a PO Box.
    - ASN.1 deliberately separates abstract syntax from physical encoding. It utilizes strict encoding rules such as Basic Encoding Rules (BER). **A BER value in ASN.1 is, in principle, encoded as a triple consisting of: a type, a length, and a value**. **Protocols like LDAP (RFC4511) transfer messages using subsets of these ASN.1 BER rules**.

#### 3. Non-Textual Data and MIME

All modern data—whether video, audio, or images—is fundamentally binary. The presentation layer relies on metadata to properly interpret this binary data.

- **Enriching Binary Data:** Just as text uses markup, binary data uses embedded metadata.
- **MIME (Multipurpose Internet Mail Extensions):** Originally built to allow email to carry multimedia, MIME dictates media types and encoding across the internet. A MIME header specifies a `Content-Type` and often includes parameters.
    - **Valid top-level MIME types include `text`, `image`, `multipart`, `application`, `message`, and `model`. (`binary` is NOT a valid MIME type)**.
    - **If an email or message consists of multiple different formats—such as HTML text alongside an embedded JPG image—the MIME type and subtype used to describe the entire message is `multipart/mixed`**.
- **Content-Transfer-Encoding:** Ensures binary data isn't corrupted by legacy protocols that expect simple text, like older SMTP systems.
    - _Base64 Example:_ Translates arbitrary 8-bit binary data into safe 7-bit ASCII characters. **This makes `base64` the most appropriate encoding for transferring binary files like PNG images via SMTP**.
    - _Quoted-Printable Example:_ Keeps text human-readable but mathematically escapes special characters.

#### 4. Data Exchange Mechanisms

When isolated systems need to share data, they utilize three complementary strategies:

- **Interchange Formats:** Instead of building hundreds of unique software converters to translate between different proprietary formats (which requires n² separate converters), an intermediary "universal" format is established, requiring only 2n converters.
- **Container Formats:** Wrappers that group different pieces of media and metadata together.
- **Data Serialization:** The process of translating complex data structures into a linear sequence of values that can be transmitted over a network and accurately rebuilt at the destination.

#### 5. Data Compression

The presentation layer handles data compression to artificially increase the effective bandwidth of the underlying network. Compression can be lossy or lossless.

- **Run-Length Encoding (RLE):** Shrinks long sequences of identically repeating values.
- **Lempel-Ziv Algorithm:** Scans data for repetitive phrases and replaces subsequent occurrences with physical pointers pointing back to the original phrase.
- **Huffman Codes:** Analyzes character frequency and assigns the shortest possible bit-strings to the most common characters, and longer bit-strings to rare characters.

#### 6. Encryption and Security

Layer 6 can also provide endpoint-to-endpoint encryption, encrypting the payload before transmission and decrypting it exactly upon arrival.

- **Layer 6 Vulnerability:** Because the encryption occurs at layer 6, lower-level packet headers remain completely unencrypted. This means traffic analysis can easily reveal source and destination IP addresses, as well as the exact types of network services being used based on transport layer port numbers.
- **Link Encryption Alternative:** Encrypting at Layer 2 (like IPSEC) encrypts the entire packet, including headers, but requires decryption and re-encryption at every router along the path.

---

### Practical Questions on Layer 6: The Presentation Layer

**Multiple Choice Questions** **Q1.** If MIME is deemed to be a data communications protocol, it would fit best on layer ... of the ISO OSI model: A. 7 | B. 6 | C. 5 | D. 4 | E. 3

**Q2.** Which character set is assumed to be understood by all parties involved in an HTTP exchange? A. ASCII | B. EBCDIC | C. Unicode | D. UTF-8 | E. ISO-8859-1

**Q3.** Consider the following protocol negotiation string in an HTTP request: `Accept-Charset: iso-8859-1, utf-8, utf-16, *;q=0.1`. Suppose the server supports `iso-8859-1`, `utf-8`, and `Shift_JIS`. The response may then be encoded using: A. iso-8859-1 | B. utf-8 | C. Shift_JIS | D. Any of the encodings listed as options above | E. One of two of the encodings listed as options above

**Q4.** Which of the following is not a valid MIME type? A. binary | B. example | C. image | D. message | E. model

**Q5.** Suppose an email consists of a message encoded in HTML and a JPG image (both included in the message). These two items are the only components of the email message. Which MIME type will be used to describe the entire email message? A. application/email | B. application/rfc822 | C. multipart/alternative | D. multipart/mixed | E. text/html

**Q6.** How many Unicode characters can, in principle, be represented in UTF-8 using exactly four bytes? If the answer is expressed in the form 2ⁿ, what is the value of n? A. 14 | B. 20 | C. 21 | D. 22 | E. 27

**Q7.** Consider the byte sequence `D7 E5`. The Unicode character represented by this UTF-8 encoding is a(n): A. Accented character | B. Greek character | C. Emoji | D. Punctuation mark | E. D7 E5 is not a valid UTF-8 encoding

**Q8.** A BER value in ASN.1 is, in principle, encoded as a triple consisting of: A. A type, a subtype and a value | B. A type, a length and a value | C. A constructor and two operands | D. A variable name, as well as its minimum and maximum values | E. The same value encoded in binary, text, and hexadecimal

**Q9.** Which of the following is not a valid data type in ASN.1? A. STRUCT | B. CHOICE | C. SEQUENCE | D. ARRAY | E. INTEGER _(Note: Both STRUCT and ARRAY are invalid depending on the exact test variant, but see memo for resolution)._

**Q10.** The syntactic structure of an ASN.1 message is defined using: A. A grammar | B. An informal description in natural language | C. A diagrammatic depiction of the message | D. A bit pattern | E. A list of the types of the components of the message

**Q11.** Which Content-Transfer-Encoding would be most appropriate to transfer a PNG image via SMTP? A. 8bit | B. binary | C. quoted-printable | D. base64 | E. 7bit

**Long Form & Calculation Questions** **Q12.** All values in this question are expressed in hexadecimal notation. Convert the following Unicode characters to UTF-8 byte sequences. Represent byte sequences as 2-digit hexadecimal numbers with a space between all bytes: a) U+1842 b) U+10AD0 c) U+2CA0

**Q13.** UTF-8 encoding is self-synchronising. Consider the following byte sequence, which is not a valid UTF-8 encoding: `47 CE B5 C4 85 E1 80 AA E1 9C A0 BA AD F0 90 8F 8C 57 73 E1 83 A8` a) Provide the first valid Unicode character that occurs in this sequence. (Format: U+xxxx) b) Provide the second valid Unicode character that occurs in this sequence. (Format: U+xxxx) c) Provide the subsequence of bytes that are invalid. d) Convert the bytes starting at the point where synchronisation is re-established, extract the first Unicode character formed (Format: U+xxxx) e) Provide the last valid Unicode character in this sequence. (Format: U+xxxx)

**Q14.** UTF-16 represents Unicode characters using 16-bit words. UTF-32 uses 32-bit words. Use big-endian representations for the following: a) Represent U+0048 in UTF-16 as a byte sequence. b) Represent U+0F40 in UTF-32 as a byte sequence.

**Q15.** Character Encodings & Presentation Errors: A user sends an email containing the sentence "I have read Zoë’s résumé." using a specific extended ASCII character set. However, the receiver opens the email and sees the text presented as "I have read Zoϕ’s rδsumδ.". Explain the Layer 6 issue that caused this presentation error and propose two practical solutions to prevent this from happening.

**Q16.** Network Interruptions & UTF-8: During the transmission of a UTF-8 encoded text document, a momentary network error causes several bytes in the middle of the stream to be corrupted. Explain how the presentation layer at the receiving end can recover from this and continue reading the subsequent text without losing synchronization.

**Q17.** Multimedia over Legacy Protocols: An application needs to send a high-resolution JPEG image over an older SMTP server that only supports 7-bit ASCII characters and enforces a strict line limit of 1000 characters. What specific MIME Content-Transfer-Encoding would the presentation layer use to handle this, and how does it ensure the image is not corrupted?

**Q18.** Bandwidth Efficiency in Data Structures: Two distinct software systems need to securely and efficiently exchange complex academic records consisting of biographical details and nested course information. System A proposes formatting the data using XML, while System B proposes using ASN.1 (Abstract Syntax Notation One) with Distinguished Encoding Rules (DER). From a network bandwidth and processing perspective, which method is more efficient and why?

**Q19.** Data Compression (Run-Length Encoding): A database application allocates 30 spaces for a surname field, but needs to transmit the name "Ng" followed by 28 blank spaces. Show how character-based Run-Length Encoding (RLE) would compress this specific data using an `<ESC>` character, and calculate the exact percentage of space saved compared to transmitting the original 30 bytes.

**Q20.** Variable-Length Compression (Huffman Coding): Two network nodes are communicating using a custom Huffman code where the frequently used letter 'E' is encoded as `11` and the rare letter 'B' is encoded as `100`. If the receiver gets a continuous bit stream like `11100`, how does the receiving presentation layer know exactly where one character ends and the next begins without any spaces or delimiter tags?

---

### Memo / Answer Key

**MCQ Answers** **A1.** B (6) **A2.** E (ISO-8859-1) **A3.** E (One of two of the encodings listed as options above - since the server supports `iso-8859-1` and `utf-8` which the client explicitly accepts) **A4.** A (binary) **A5.** D (multipart/mixed) **A6.** C (21). _Step-by-step:_ A 4-byte UTF-8 character uses the format `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`. Counting the available payload 'x' bits gives us 3 + 6 + 6 + 6 = 21 bits. Therefore, 2²¹ characters can be represented. **A7.** E (D7 E5 is not a valid UTF-8 encoding). _Step-by-step:_ `D7` in binary is `11010111`. The `110` prefix indicates a 2-byte character, meaning the immediate next byte _must_ be a continuation byte starting with `10`. `E5` in binary is `11100101`. Because it starts with `111` instead of `10`, it is illegal to place it after D7. **A8.** B (A type, a length and a value) **A9.** D (ARRAY) or A (STRUCT) depending on variant. In the 2025 ST2 paper, `ARRAY` is the intended invalid type. (Both are technically not base ASN.1 constructors). **A10.** A (A grammar) **A11.** D (base64).

**Long Form Answers** **A12. UTF-8 Encoding Calculations:** a) **U+1842**:

- Binary value: `0001 1000 0100 0010` (13 significant bits). Needs a 3-byte template: `1110xxxx 10xxxxxx 10xxxxxx`.
- Pad bits to fit 16 payload slots: `0001` | `100001` | `000010`.
- Insert into template: `1110` `0001` (E1) | `10` `100001` (A1) | `10` `000010` (82).
- **Result: E1 A1 82**

b) **U+10AD0**:

- Binary value: `0001 0000 1010 1101 0000` (17 significant bits). Needs a 4-byte template: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`.
- Pad bits to fit 21 payload slots: `000` | `010000` | `101011` | `010000`.
- Insert into template: `11110` `000` (F0) | `10` `010000` (90) | `10` `101011` (AB) | `10` `010000` (90).
- **Result: F0 90 AB 90**

c) **U+2CA0**:

- Binary value: `0010 1100 1010 0000`. Needs a 3-byte template.
- Pad bits: `0010` | `110010` | `100000`.
- Insert into template: `1110` `0010` (E2) | `10` `110010` (B2) | `10` `100000` (A0).
- **Result: E2 B2 A0**

**A13. UTF-8 Decoding and Error Recovery:** Sequence: `47 CE B5 C4 85 E1 80 AA E1 9C A0 BA AD F0 90 8F 8C 57 73 E1 83 A8`

- `47` (`01000111`) is a valid 1-byte char (U+0047).
- `CE B5` (`110...` `10...`) is valid. Decodes to U+03B5.
- _Scanning forward:_ `BA` and `AD` both start with `10xxxxxx`. They are continuation bytes without a valid start byte, making them the invalid subsequence.
- Synchronisation is re-established at `F0 90 8F 8C`, which is a valid 4-byte character decoding to U+103CC.
- The final character `E1 83 A8` decodes to U+10E8. **Answers:** a) First valid: **U+0047** b) Second valid: **U+03B5** c) Invalid subsequence: **BA AD** d) First character after sync re-established: **U+103CC** e) Last valid character: **U+10E8**

**A14. UTF-16 and UTF-32 Big-Endian:** a) U+0048 in UTF-16 (16-bits/2-bytes), big-endian (largest byte first) -> **00 48**. b) U+0F40 in UTF-32 (32-bits/4-bytes), big-endian -> **00 00 0F 40**.

**A15.** The presentation error occurred because the sender and receiver are using different versions of extended 8-bit ASCII character sets. The sender's system placed characters like 'ë' and 'é' at specific numeric positions, but the receiver's system assigned different symbols (like 'ϕ' and 'δ') to those exact same numeric slots. Two practical solutions include:

1. Standardizing on a universal character set like Unicode (UTF-8) that covers all characters uniformly.
2. Negotiating the character set during the initial protocol exchange (e.g., using an HTTP `Accept-Charset` header) so both presentation layers agree on the encoding before data is sent.

**A16.** UTF-8 is specifically designed to be self-synchronizing. In a multi-byte character, trailing octets always start with the binary sequence `10`. If corruption occurs, the receiving system simply skips any octets starting with `10` and looks for the first octet that does not match this pattern. This immediately identifies the start of a new, uncorrupted character, allowing the data exchange to continue.

**A17.** The presentation layer would use `base64` Content-Transfer-Encoding. Base64 translates arbitrary 8-bit binary data into safe 7-bit ASCII characters. Because the encoded output consists entirely of 7-bit ASCII values and removes the concept of arbitrary long binary lines, lower-level legacy mechanisms like the old SMTP server can successfully transfer the file without dropping content or corrupting the image.

**A18.** System B's proposal (ASN.1 with DER) is vastly more efficient. XML relies heavily on textual representation and repetitive, human-readable tags, which consumes excessive network bandwidth. In contrast, ASN.1 separates the abstract syntax from the physical encoding, and when combined with DER, it encodes the data structure directly into compact binary values (omitting length fields where possible) without the need for bloated textual delimiters.

**A19.** Using character-based RLE, the 30-byte string would be encoded as `Ng<ESC><28><space>`. The entire transmission now only requires 5 bytes: 'N', 'g', `<ESC>`, '28', and the space character. By reducing the size from 30 bytes down to 5 bytes, the presentation layer saves 25 bytes in total, which represents an 83.3% reduction in allocated space.

**A20.** Huffman codes use a binary tree structure where the bit sequences for the common prefixes are unique; therefore, no character's code is used as a prefix for any other character. To decode `11100`, the receiver simply reads the bits and traverses the tree from the root. The first `11` leads to a leaf node for 'E', uniquely identifying the character. The traversal then restarts at the root for the next bits `100`, which safely leads to the leaf node for 'B', allowing self-synchronization without explicit delimiters.
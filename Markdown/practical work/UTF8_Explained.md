# UTF-8 Encoding — How It Actually Works

---

## The Problem UTF-8 Solves

Unicode assigns every character in existence a unique number called a **code point**, written as `U+XXXX` in hex. The problem is that some characters have small code points (like `A` = `U+0041`) and some are enormous (like 😀 = `U+1F600`). You can't just store every character as a fixed number of bytes — small characters would waste space, and you'd need 4 bytes for everything.

UTF-8 solves this by using a **variable number of bytes** — 1, 2, 3, or 4 — depending on how big the code point is. The clever part is that it embeds the length information directly into the bytes themselves, so the receiver always knows how many bytes belong together.

---

## Step 1 — Deciding How Many Bytes You Need

Convert the code point to binary and count the bits. The number of bits tells you which byte length to use:

| Bits needed | UTF-8 bytes |
|---|---|
| 1–7 bits | 1 byte |
| 8–11 bits | 2 bytes |
| 12–16 bits | 3 bytes |
| 17–21 bits | 4 bytes |

**Example:** `U+039E`

`0x039E` in binary = `1110011110` → that is 10 bits → fits in the 8–11 range → **2 bytes**

**Example:** `U+179F`

`0x179F` in binary = `1011110011111` → that is 13 bits → fits in the 12–16 range → **3 bytes**

---

## Step 2 — The Byte Templates

Each byte length has a fixed template. The `x` slots are where your actual data bits go.

```
1 byte:  0xxxxxxx
2 bytes: 110xxxxx  10xxxxxx
3 bytes: 1110xxxx  10xxxxxx  10xxxxxx
4 bytes: 11110xxx  10xxxxxx  10xxxxxx  10xxxxxx
```

### Understanding the prefixes

The leading byte prefix encodes the byte count:

- `0...` — 1 byte (no leading ones, just a zero)
- `110...` — 2 bytes (two leading ones, terminated by a zero)
- `1110...` — 3 bytes (three leading ones, terminated by a zero)
- `11110...` — 4 bytes (four leading ones, terminated by a zero)

The pattern: **the number of leading `1`s equals the total byte count, followed by a `0` to end the prefix.**

Every **continuation byte** (bytes 2, 3, 4) always starts with `10`. This prefix is never used by a leading byte, which means a continuation byte can never be mistaken for the start of a new character.

---

## Step 3 — Encoding (Code Point → UTF-8 Hex)

1. Convert the code point to binary
2. Count the bits to determine byte count
3. Pad the binary to fill exactly the available `x` slots in the template
4. Pour the bits in left to right across all `x` slots, skipping over the fixed prefix bits
5. Convert each byte back to hex

**Example: `U+00C6` (Æ)**

- Binary: `11000110` → 8 bits → 2 bytes (8–11 range), 11 slots available
- Pad to 11 bits: `00011000110`
- Template: `110xxxxx 10xxxxxx`
- Fill in: `110 00011` `10 000110`
- Hex: `C3 86`

**Example: `U+179F`**

- Binary: `1011110011111` → 13 bits → 3 bytes (12–16 range), 16 slots available
- Pad to 16 bits: `0001011110011111`
- Template: `1110xxxx 10xxxxxx 10xxxxxx`
- Fill in: `1110 0001` `10 011110` `10 011111`
- Hex: `E1 9E 9F`

---

## Step 4 — Decoding (UTF-8 Hex → Code Point)

Decoding is just encoding in reverse:

1. Read the first byte — its prefix tells you how many bytes belong to this character
2. Collect the required number of continuation bytes
3. Strip all prefix bits from every byte
4. Concatenate the remaining data bits left to right
5. Convert the resulting binary back to hex → that is your `U+XXXX`

**Example: `C3 86`**

- `C3` = `11000011` → prefix `110` → 2-byte character
- `86` = `10000110` → prefix `10` → valid continuation ✓
- Strip prefixes: `00011` + `000110`
- Combined: `00011000110` = `0xC6`
- Result: **U+00C6** (Æ)

---

## Decoding a Corrupted Stream

When given a byte string that may contain errors, the process is:

1. **Read the first byte** — its prefix tells you how many bytes to expect
2. **Check each following byte** starts with `10` — if one doesn't, the sequence is broken
3. **Discard incomplete or broken sequences** and move on to the next byte
4. **Decode only the structurally complete sequences**

### The error cases to watch for

| Situation | What to do |
|---|---|
| A `10xxxxxx` byte with no valid leader before it | Orphaned — skip it |
| A new leader byte appearing before the previous leader got enough continuation bytes | Previous character is incomplete — discard it, treat the new leader as a fresh start |
| A leader byte at the end of the stream with not enough bytes remaining | Incomplete — discard |

### Why this works — self-synchronisation

Because `10xxxxxx` is reserved exclusively for continuation bytes and never appears as a leading byte, you can always re-identify character boundaries. If you drop into the middle of a stream with no context, just skip bytes starting with `10` until you hit one that doesn't — that is the start of the next character. The stream self-heals.

**Example — corrupted stream:**

```
EF BB AF BC C2 AA F1 83 E0 AA AA F0 90 AB C3 D5
```

| Bytes | Analysis | Result |
|---|---|---|
| `EF BB AF` | `EF`=`1110...` (3-byte leader), `BB`=`10...` ✓, `AF`=`10...` ✓ | Valid — decode it |
| `BC` | `10...` continuation but no leader — orphaned | Skip |
| `C2 AA` | `C2`=`110...` (2-byte leader), `AA`=`10...` ✓ | Valid — decode it |
| `F1 83 E0` | `F1`=`11110...` (4-byte leader), `83`=`10...` ✓, `E0`=`1110...` — not a continuation | F1 sequence incomplete — discard F1 and 83 |
| `E0 AA AA` | `E0`=`1110...` (3-byte leader), `AA`=`10...` ✓, `AA`=`10...` ✓ | Valid — decode it |
| `F0 90 AB` | `F0`=`11110...` (4-byte leader), `90`=`10...` ✓, `AB`=`10...` ✓, `C3`=`110...` — not a continuation | F0 sequence incomplete — discard |
| `C3` | 2-byte leader, but `D5`=`110...` — not a continuation | Incomplete — discard |
| `D5` | 2-byte leader with nothing after it | Incomplete — discard |

Valid characters decoded: **U+FEEF, U+00AA, U+0AAA**

---

## Quick Reference

```
Bits in code point → Bytes needed → Available data slots
1–7   →  1 byte  →  7 bits  →  0xxxxxxx
8–11  →  2 bytes → 11 bits  →  110xxxxx 10xxxxxx
12–16 →  3 bytes → 16 bits  →  1110xxxx 10xxxxxx 10xxxxxx
17–21 →  4 bytes → 21 bits  →  11110xxx 10xxxxxx 10xxxxxx 10xxxxxx
```

Leading byte prefix rule: **n leading 1s followed by a 0 = n total bytes**

Continuation bytes always start with `10` — never confused with a leader.

A valid UTF-8 sequence has exactly the right number of `10xxxxxx` bytes after its leader, and nothing else.

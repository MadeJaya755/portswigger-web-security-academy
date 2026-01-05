# NoSQL Injection

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to NoSQL injection.

The focus is on abusing query operator injection and
improper handling of user-supplied data in NoSQL queries.

---

## Approach

- Identification of NoSQL-backed authentication and search functionality
- Injection of query operators (e.g. $ne, $gt, $regex)
- Enumeration of fields and values through boolean-based logic
- Bypass of authentication and access control mechanisms

---

## Tools

- Burp Suite
- Browser
- Custom scripts (Python)

---

## Notes

NoSQL injection vulnerabilities stem from treating
user input as trusted query objects.
Impact often includes authentication bypass and data extraction.
Documentation emphasizes query behavior over payload syntax.

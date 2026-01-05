# Information Disclosure

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to information disclosure issues.

The focus is on identifying unintended data exposure that can be
leveraged for further exploitation.

---

## Approach

- Analysis of error messages and debug output
- Inspection of verbose responses and stack traces
- Identification of sensitive information in headers and responses
- Abuse of unintended functionality to reveal internal details

---

## Tools

- Burp Suite
- Browser
- Manual request manipulation

---

## Notes

Information disclosure issues are often subtle but highly valuable.
Exposed details such as internal paths, credentials, or logic hints
can significantly reduce the effort required for further attacks.
Documentation focuses on actionable impact.

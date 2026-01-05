# Cross-Site Scripting (XSS)

This folder contains scripts and proof-of-work from solving
PortSwigger Web Security Academy labs related to cross-site scripting.

The focus is on exploiting execution contexts and data flow,
not on collecting payload lists.

---

## Approach

- Identification of injection points and reflection sinks
- Analysis of execution context (HTML, attribute, JavaScript)
- Bypass of input filtering and output encoding
- Verification of exploitability through controlled payload execution

---

## Tools

- Burp Suite
- Browser DevTools

---

## Notes

XSS exploitation depends on context and output handling.
Documentation is intentionally minimal and focuses on execution
and observable impact rather than payload enumeration.

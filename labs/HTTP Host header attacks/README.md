# HTTP Host Header Attacks

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to HTTP Host header attacks.

The focus is on abusing server-side trust in the Host header
rather than simple header manipulation.

---

## Approach

- Identification of server-side usage of the Host header
- Testing for host-based routing and absolute URL generation
- Abuse of Host header injection in password reset and link generation
- Validation of impact through cache poisoning or external interactions

---

## Tools

- Burp Suite
- Browser
- Custom headers and crafted requests

---

## Notes

Host header vulnerabilities depend on how the application
uses host-derived values internally.
Documentation focuses on impact, not header mutation.

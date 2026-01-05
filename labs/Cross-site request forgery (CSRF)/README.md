# Cross-Site Request Forgery (CSRF)

This folder contains scripts and proof-of-work from solving
PortSwigger Web Security Academy labs related to CSRF vulnerabilities.

The focus is on exploiting state-changing requests that lack
effective CSRF protections.

---

## Approach

- Identification of sensitive state-changing actions
- Analysis of CSRF token generation and validation
- Abuse of missing, predictable, or improperly validated tokens
- Testing same-site cookie behavior and origin checks

---

## Tools

- Burp Suite
- Browser
- HTML-based CSRF exploits

---

## Notes

CSRF vulnerabilities depend heavily on application context and user
session handling.
Documentation is kept minimal and focuses on successful exploitation.

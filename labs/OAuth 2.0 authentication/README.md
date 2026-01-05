# OAuth 2.0 Authentication

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to OAuth 2.0 authentication vulnerabilities.

The focus is on exploiting incorrect trust relationships
between the client, authorization server, and resource server.

---

## Approach

- Analysis of OAuth authorization flows (authorization code, implicit)
- Identification of missing or weak state validation
- Abuse of redirect URI handling
- Token leakage and account takeover scenarios

---

## Tools

- Burp Suite
- Browser
- Manual request manipulation

---

## Notes

OAuth vulnerabilities usually result from
misconfigured clients rather than protocol flaws.
Documentation emphasizes flow analysis and trust assumptions.

# JSON Web Token (JWT) Security Testing

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to JWT vulnerabilities.

The focus is on abusing incorrect trust assumptions in
token validation and signature handling.

---

## Approach

- Analysis of JWT structure and claims usage
- Identification of weak or missing signature verification
- Manipulation of token headers and payload claims
- Abuse of algorithm confusion and key handling issues

---

## Tools

- Burp Suite
- jwt.io
- Manual token crafting

---

## Notes

JWT vulnerabilities often arise from improper verification logic
rather than cryptographic weaknesses.
Documentation focuses on execution path and authorization impact.

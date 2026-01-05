# GraphQL API Security Testing

This folder contains scripts and proof-of-work from solving
PortSwigger Web Security Academy labs related to GraphQL APIs.

The focus is on abusing GraphQL-specific behaviors and
authorization weaknesses rather than general API issues.

---

## Approach

- Schema discovery via introspection and error analysis
- Abuse of queries, mutations, and nested objects
- Identification of authorization flaws at field and object levels
- Exploitation of excessive data exposure and logic weaknesses

---

## Tools

- Burp Suite
- Browser DevTools
- Python

---

## Notes

GraphQL APIs expose flexible data access patterns.
Security issues often arise from insufficient authorization
checks at the field or resolver level.
Documentation focuses on execution and impact.

# Web Cache Deception

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to web cache deception vulnerabilities.

The focus is on tricking caching mechanisms
into storing and serving sensitive user-specific content.

---

## Approach

- Identification of cacheable endpoints
- Manipulation of URL paths and file extensions
- Forcing cache to store authenticated responses
- Retrieval of cached sensitive data as an unauthenticated user

---

## Tools

- Burp Suite
- Browser
- Manual request manipulation

---

## Notes

Web cache deception vulnerabilities arise from
misconfigured caching rules and incorrect assumptions
about which content is safe to cache.
Impact includes exposure of sensitive user data.
Documentation emphasizes cache behavior and response headers.

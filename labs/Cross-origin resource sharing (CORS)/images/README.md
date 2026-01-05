# Cross-Origin Resource Sharing (CORS)

This folder contains scripts and proof-of-work from solving
PortSwigger Web Security Academy labs related to CORS misconfigurations.

The focus is on abusing incorrect trust decisions in cross-origin
requests rather than explaining browser security theory.

---

## Approach

- Manual inspection of CORS-related response headers
- Identification of overly permissive origin handling
- Exploitation using malicious origins and credentialed requests
- Validation of data leakage through cross-origin access

---

## Tools

- Burp Suite
- Browser DevTools

---

## Notes

CORS issues are highly context-dependent.
Documentation is kept minimal and focuses on successful exploitation
and observable impact.

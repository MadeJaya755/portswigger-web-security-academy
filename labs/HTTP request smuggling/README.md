# HTTP Request Smuggling

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to HTTP request smuggling.

The focus is on exploiting inconsistencies in HTTP request parsing
between front-end and back-end systems.

---

## Approach

- Identification of front-end and back-end request parsing behavior
- Testing CL.TE and TE.CL desynchronization scenarios
- Crafting ambiguous HTTP requests to poison or desync connections
- Validation of impact through request confusion and response anomalies

---

## Tools

- Burp Suite
- Repeater
- Custom-crafted HTTP requests

---

## Notes

HTTP request smuggling is highly environment-specific.
Successful exploitation depends on subtle differences in
request interpretation between components.
Documentation focuses on execution and impact.

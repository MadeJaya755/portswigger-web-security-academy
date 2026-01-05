# Insecure Deserialization

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to insecure deserialization.

The focus is on abusing unsafe deserialization of user-controlled data
to manipulate application behavior or achieve code execution.

---

## Approach

- Identification of serialized data in cookies, headers, or request bodies
- Analysis of serialization formats and object structures
- Modification of serialized objects to alter application logic
- Exploitation of gadget chains where applicable

---

## Tools

- Burp Suite
- Browser
- Custom payload crafting

---

## Notes

Insecure deserialization vulnerabilities arise from trusting
client-controlled serialized data.
Impact depends on how deserialized objects are used by the application.
Documentation focuses on execution path and impact.

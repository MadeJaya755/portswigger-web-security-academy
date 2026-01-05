# XML External Entity (XXE) Injection

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to XML External Entity (XXE) injection.

The focus is on abusing insecure XML parsers
to access internal files or perform out-of-band interactions.

---

## Approach

- Identification of XML input handling
- Injection of external entities into XML documents
- Extraction of local files via entity expansion
- Use of out-of-band techniques for blind XXE

---

## Tools

- Burp Suite
- Browser
- Collaborator (for blind XXE)

---

## Notes

XXE vulnerabilities arise when XML parsers
allow processing of external entities.
Impact includes file disclosure, SSRF, and internal network interaction.
Documentation emphasizes parser configuration and execution flow.

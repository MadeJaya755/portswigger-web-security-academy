# Server-Side Template Injection (SSTI)

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to server-side template injection.

The focus is on executing unintended template expressions
by abusing unsafe rendering of user-controlled input.

---

## Approach

- Identification of server-side template rendering points
- Detection of template engines (Jinja2, Twig, Freemarker, etc.)
- Injection of template expressions
- Escalation from expression evaluation to code execution

---

## Tools

- Burp Suite
- Browser
- Manual payload crafting

---

## Notes

SSTI vulnerabilities occur when user input is rendered
directly inside server-side templates.
Impact ranges from information disclosure to full remote code execution.
Documentation emphasizes template context and execution flow.

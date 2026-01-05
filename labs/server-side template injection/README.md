# Server-Side Template Injection (SSTI)

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to Server-Side Template Injection (SSTI).

The focus is on identifying unsafe template rendering
and escalating template expression injection
to sensitive data access or remote code execution.

---

## Approach

- Locate server-side rendered templates
- Detect template engine through expression evaluation
- Inject and execute template expressions
- Escalate from data leakage to code execution where possible

---

## Tools

- Burp Suite
- Browser
- Manual payload crafting

---

## Notes

SSTI vulnerabilities arise when user-controlled input
is rendered directly in server-side templates.
Severity depends on template engine configuration and sandboxing.
Documentation emphasizes execution context and escalation paths.

# Prototype Pollution

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to prototype pollution vulnerabilities.

The focus is on manipulating JavaScript object prototypes
to alter application behavior globally.

---

## Approach

- Identification of unsafe object merging or assignment
- Injection of properties into Object.prototype
- Observation of unexpected behavior across the application
- Escalation to XSS or logic bypass where applicable

---

## Tools

- Burp Suite
- Browser DevTools
- Manual payload crafting

---

## Notes

Prototype pollution occurs when user-controlled input
is merged into JavaScript objects without proper sanitization.
Impact can range from logic manipulation to code execution.
Documentation emphasizes execution path and side effects.

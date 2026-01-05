# OS Command Injection

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to OS command injection.

The focus is on executing arbitrary system commands
by abusing unsafe use of OS-level command execution.

---

## Approach

- Identification of command execution sinks
- Analysis of how user input is passed to OS commands
- Bypass of input filtering and blacklists
- Verification of command execution impact

---

## Tools

- Burp Suite
- Browser
- Manual payload crafting

---

## Notes

OS command injection vulnerabilities occur when
applications pass user input directly to system commands.
Impact depends on execution privileges and environment.
Documentation emphasizes command context and output handling.

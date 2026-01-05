# Race Conditions

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to race condition vulnerabilities.

The focus is on abusing unintended behavior
caused by concurrent or repeated requests.

---

## Approach

- Identification of non-atomic operations
- Analysis of state changes across requests
- Execution of concurrent request attacks
- Observation of inconsistent application behavior

---

## Tools

- Burp Suite (Turbo Intruder, Repeater)
- Browser
- Custom scripts (Python)

---

## Notes

Race condition vulnerabilities occur when
applications fail to properly synchronize state changes.
Impact often includes logic bypass, financial abuse, or privilege escalation.
Documentation emphasizes timing and state transitions.

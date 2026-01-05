# DOM-Based Cross-Site Scripting (DOM XSS)

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to DOM-based XSS.

The focus is on exploiting client-side JavaScript sinks and
unsafe data handling within the browser.

---

## Approach

- Identification of DOM sources controlled by user input
- Analysis of JavaScript sinks such as innerHTML, document.write, and eval
- Tracing client-side data flow from source to sink
- Crafting payloads that execute without server-side reflection

---

## Tools

- Browser DevTools
- Burp Suite
- Manual JavaScript analysis

---

## Notes

DOM-based XSS occurs entirely on the client side.
Server responses may appear safe while the vulnerability
exists in front-end JavaScript logic.
Documentation focuses on execution and impact.

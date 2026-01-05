# Web LLM Attacks

This folder contains proof-of-work from solving
PortSwigger Web Security Academy labs related to Web LLM attacks.

The focus is on exploiting unsafe integration of
Large Language Models (LLMs) within web applications.

---

## Approach

- Identification of LLM-backed application features
- Analysis of how user input is incorporated into prompts
- Prompt injection and prompt manipulation techniques
- Abuse of excessive trust in LLM-generated output

---

## Tools

- Burp Suite
- Browser
- Manual prompt crafting

---

## Notes

Web LLM vulnerabilities arise from improper trust boundaries
between user input, system prompts, and LLM output.
Impact includes data leakage, logic manipulation, and unauthorized actions.
Documentation emphasizes prompt flow and trust assumptions.

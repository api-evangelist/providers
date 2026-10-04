---
artifact_total: 0
coverage:
  checked: '2026-09-02'
  detail: Anadarko was fully absorbed into Occidental Petroleum in August 2019 and its own domain now serves nothing at all — anadarko.com keeps a CSC brand-protection A record but refuses the connection on both port 80 and port 443, and www.anadarko.com has no A record — so there is no surviving developer surface to profile.
  evidence:
  - status: 0
    url: https://www.anadarko.com/
  - status: 0
    url: https://anadarko.com/
  - status: 301
    url: https://www.oxy.com/.well-known/security.txt
  - status: 404
    url: https://www.oxy.com/openapi.json
  reason: defunct
  state: none
layout: provider
name: anadarko-petroleum
nav: Providers
network: true
random_paper: 19
slug: anadarko-petroleum
---

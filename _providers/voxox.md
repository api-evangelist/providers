---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/voxox-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://voxox.com/
coverage:
  checked: '2026-09-04'
  detail: voxox.com served a real Voxox site through 2025-11-16 and has since been a GoDaddy parking lander — a 114-byte JavaScript redirect to /lander whose catch-all answers HTTP 200 for every path including /openapi.json and all of /.well-known/ — with no MX record and with every developer, docs, api, assist, support, my, app and portal subdomain gone from DNS.
  evidence:
  - status: 200
    url: https://voxox.com/
  - status: 200
    url: https://voxox.com/lander
  - status: 200
    url: https://voxox.com/sitemap.xml
  - status: 200
    url: https://voxox.com/.well-known/security.txt
  - status: 200
    url: https://voxox.com/openapi.json
  reason: defunct
  state: none
created: '2026-09-04'
description: 'Voxox is the trade name of Telcentris, Inc., a San Diego, California cloud communications provider founded in 2006 by Bryan, Kevin and Robert Hertz. It sold hosted business phone service (Voxox Cloud Phone), wholesale SIP voice termination and A2P/wholesale SMS messaging, the latter offered to carriers and resellers over an HTTP API and SMPP. The developer surface was never published openly: the wholesale SMS API reference was issued privately by an account manager rather than posted as a public reference or machine-readable specification. As of December 2025 voxox.com resolves to a registrar parking page, the domain carries no MX record, and every developer, docs, support and application subdomain the company operated has stopped resolving.'
layout: provider
modified: '2026-09-04'
name: Voxox
nav: Providers
network: true
overview: Voxox is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Telecommunications, Communications, Cloud Communications, and VoIP.
random_paper: 13
security:
- kind: domain-security
  name: Voxox Domain Security
  slug: voxox-domain-security
  summary_line: TLSv1.3
slug: voxox
tags:
- Company
- Telecommunications
- Communications
- Cloud Communications
- VoIP
- SMS
- Messaging
- CPaaS
website: https://voxox.com/
---

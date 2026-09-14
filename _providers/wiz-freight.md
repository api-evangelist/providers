---
api_count: 0
artifact_total: 1
common:
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wiz-freight-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wiz-freight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://wizfreight.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://in.linkedin.com/company/wizfreight
coverage:
  checked: '2026-09-04'
  detail: 'Wiz Freight''s operating surface is gone: wizfreight.com now serves a GoDaddy Website Builder "Launching Soon" placeholder, the former booking portal at https://wizfreight.com/bookings returns 404 into that placeholder, and the platform host sit.wizfreight.net no longer resolves, after trade press reported in September 2025 that the Chennai digital forwarder had suspended export bookings amid an executive exodus.'
  evidence:
  - status: 200
    url: https://wizfreight.com/
  - status: 404
    url: https://wizfreight.com/bookings
  - status: 404
    url: https://wizfreight.com/openapi.json
  - status: 404
    url: https://wizfreight.com/.well-known/agent-card.json
  - status: 404
    url: https://api.github.com/orgs/wizfreight
  reason: defunct
  state: none
created: '2026-09-04'
description: 'Wiz Freight (Wiz Logtec Solutions Private Limited) was a Chennai, India based digital freight forwarder founded in 2020 by Ramkumar Ramachandran and Ramkumar Govindarajan, offering ocean, air and surface freight booking, instant rate discovery, live shipment tracking, digital documentation and multi-currency freight payments through its own technology platform. The company raised roughly $58.6M from Tiger Global Management, Nippon Express Holdings, SBI Investment, Stride Ventures, Foundamental and Axilor Ventures. Trade press reported in September 2025 that the company had suspended export bookings amid an executive exodus, and as of September 2026 its public surface is gone: wizfreight.com serves a GoDaddy Website Builder placeholder, the former booking portal path 404s, and the sit.wizfreight.net platform host no longer resolves. No developer program, API reference or machine-readable contract was ever published on a reachable host, and none survives today.'
layout: provider
modified: '2026-09-04'
name: Wiz Freight
nav: Providers
network: true
overview: Wiz Freight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Logistics, Freight, Freight Forwarding, and Supply Chain.
random_paper: 2
security:
- kind: domain-security
  name: Wiz Freight Domain Security
  slug: wiz-freight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wiz-freight
tags:
- Company
- Logistics
- Freight
- Freight Forwarding
- Supply Chain
- Shipping
- Transportation
- India
website: https://wizfreight.com/
---

---
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agicinc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://elephantech.com/en/
- group: company
  title: ''
  type: Blog
  url: https://elephantech.com/en/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://elephantech.com/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/elephantech
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://elephantech.com/en/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://elephantech.com/en/inquiry/
coverage:
  checked: '2026-09-12'
  detail: Elephantech (the current name of AgIC Inc.) manufactures inkjet printing equipment, conductive materials and flexible printed circuit boards — physical goods — and its 64-page WordPress marketing site has no developer, API or reference section at all; every probed contract path redirects to the site root.
  evidence:
  - status: 302
    url: https://elephantech.com/openapi.json
  - status: 302
    url: https://elephantech.com/.well-known/agent-card.json
  - status: 302
    url: https://elephantech.com/llms.txt
  - status: 200
    url: https://elephantech.com/sitemap.xml
  - status: 200
    url: https://elephantech.com/en/
  reason: not-a-software-company
  state: none
created: '2026-09-12'
description: Elephantech Inc. (founded January 2014 in Tokyo as AgIC Inc., renamed Elephantech in September 2017) develops, manufactures and sells precision metal inkjet printing equipment, advanced conductive materials, and flexible printed circuit board products, including its SustainaCircuits multilayer PCB line and NeuralJet printing technology. The company positions itself as decarbonizing electronics manufacturing by replacing subtractive copper etching with additive inkjet deposition. It is a hardware and materials manufacturer with roughly 150 employees, headquartered at 4-3-8 Hatchobori, Chuo-ku, Tokyo; it publishes no developer program, public API, SDK or machine-readable API contract.
image: https://elephantech.com/cms/wp-content/uploads/2024/08/elephantech_corpweb_ptc_topview.png
layout: provider
modified: '2026-09-12'
name: Elephantech
nav: Providers
network: true
overview: 'Elephantech is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Manufacturing, Electronics, Hardware, and Printed Circuit Boards.


  Elephantech''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 4
security:
- kind: domain-security
  name: Agicinc Domain Security
  slug: agicinc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agicinc
tags:
- Company
- Manufacturing
- Electronics
- Hardware
- Printed Circuit Boards
- Materials
- Sustainability
- Japan
website: https://elephantech.com/en/
---

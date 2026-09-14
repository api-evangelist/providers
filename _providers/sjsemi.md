---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sjsemi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://en.sjsemi.com/
- group: company
  title: ''
  type: News
  url: https://en.sjsemi.com/about/23368/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sjsemi-llms.txt
coverage:
  checked: '2026-08-28'
  detail: SJSemi is a contract semiconductor manufacturer — a 12-inch MEOL bumping, wafer-test and advanced-packaging foundry — whose corporate site carries only HOME / ABOUT US / SERVICE / SCM / JOIN US / CONTACT US, with no developer, API, or customer-portal section anywhere on it, and whose hosts return 404 for /openapi.json, every /.well-known/ path, robots.txt and sitemap.xml.
  evidence:
  - status: 200
    url: https://en.sjsemi.com/
  - status: 404
    url: https://en.sjsemi.com/openapi.json
  - status: 404
    url: https://en.sjsemi.com/.well-known/agent-card.json
  - status: 404
    url: https://en.sjsemi.com/.well-known/api-catalog
  - status: 404
    url: https://www.sjsemi.com/robots.txt
  reason: not-a-software-company
  state: none
created: '2026-08-28'
description: SJSemi (SJSemiconductor (Jiangyin) Corp.) is a Chinese semiconductor Middle-End-Of-Line (MEOL) pure-play foundry and outsourced assembly and test (OSAT) provider, founded in 2014 as a joint venture between JCET and SMIC and headquartered in the Jiangyin High-Tech Industrial Development Zone, Jiangsu, with offices in Shanghai and Santa Clara, California. The company operates a 12-inch wafer bumping, wafer-level chip-scale packaging, chip probing and final-test line, and supplies advanced packaging and 3D multi-die integration services — Cu pillar, RDL, fan-out, TSV and silicon interposer 2.5D — into smartphone, 5G communications, high-performance computing, data-center and automotive electronics supply chains. It is a contract manufacturer of physical semiconductor packaging services and publishes no public developer program, API, or machine-readable interface contract.
layout: provider
modified: '2026-08-28'
name: SJSemi
nav: Providers
network: true
overview: 'SJSemi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Semiconductors, Hardware, Manufacturing, and Advanced Packaging.


  SJSemi''s developer surface includes product news and 3 more developer resources.'
random_paper: 0
screenshot: https://raw.githubusercontent.com/api-evangelist/sjsemi/refs/heads/main/screenshots/sjsemi-2026-09-02T155707.png
security:
- kind: domain-security
  name: Sjsemi Domain Security
  slug: sjsemi-domain-security
  summary_line: TLSv1.3 · HSTS
slug: sjsemi
tags:
- Company
- Semiconductors
- Hardware
- Manufacturing
- Advanced Packaging
- Wafer Test
- OSAT
- China
website: https://en.sjsemi.com/
---

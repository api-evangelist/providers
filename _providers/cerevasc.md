---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cerevasc-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cerevasc.com/
- group: company
  title: ''
  type: About
  url: https://cerevasc.com/eshunt-system-cerevasc/
- group: operate
  title: ''
  type: Contact
  url: https://cerevasc.com/contact-cerevasc/
- group: company
  title: ''
  type: Blog
  url: https://cerevasc.com/press/
- group: company
  title: ''
  type: BlogRSS
  url: https://cerevasc.com/feed/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cerevasc.com/privacy-policy/
- group: other
  title: ''
  type: SecondaryMarketListing
  url: https://forgeglobal.com/cerevasc_stock/
coverage:
  checked: '2026-08-09'
  detail: CereVasc is a clinical-stage neurovascular implant maker whose product is the physical eShunt device; its WordPress site has no /developers, /api or /docs path, no api./developer./docs. subdomain resolves in DNS, and every discovery probe (/openapi.json, /llms.txt, /.well-known/agent-card.json) returned 404.
  evidence:
  - status: 404
    url: https://cerevasc.com/openapi.json
  - status: 404
    url: https://cerevasc.com/developers
  - status: 404
    url: https://cerevasc.com/llms.txt
  - status: 404
    url: https://cerevasc.com/.well-known/agent-card.json
  - status: 404
    url: https://cerevasc.com/.well-known/security.txt
  - status: 200
    url: https://cerevasc.com/
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: CereVasc, Inc. is a clinical-stage medical device company developing novel, minimally invasive treatments for patients with neurological diseases. Its lead product, the eShunt System, uses percutaneous transvenous-transdural access to the central nervous system to treat communicating hydrocephalus — including normal pressure hydrocephalus (NPH) — as a less invasive alternative to conventional neurosurgical shunt placement. The eShunt System is an investigational device limited by United States federal law to investigational use, and is being evaluated in the STRIDE pivotal study (NCT06498960). CereVasc raised a $70M Series B in 2024 and has received FDA Breakthrough Device Designation. The company builds implantable hardware and publishes no public API, developer program, or machine-readable specification.
image: https://cerevasc.com/wp-content/uploads/2023/10/CereVasc-logo-%C2%AEweb-main.svg
layout: provider
modified: '2026-08-09'
name: CereVasc
nav: Providers
network: true
overview: 'CereVasc is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Neurology, and Hydrocephalus.


  CereVasc''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 99
score:
  band: minimal
  composite: 6.7
  delta: -1.6
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: domain-security
  name: Cerevasc Domain Security
  slug: cerevasc-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cerevasc
tags:
- Company
- Medical Devices
- Healthcare
- Neurology
- Hydrocephalus
- Medical Technology
- Clinical Stage
website: https://cerevasc.com/
---

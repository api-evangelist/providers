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
  scored_at: '2026-08-24'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agnovos-bioscience-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.agnovos.com/
- group: company
  title: ''
  type: About
  url: https://www.agnovos.com/en/about-us/about-agnovos/
- group: company
  title: ''
  type: Blog
  url: https://www.agnovos.com/en/news-events/
- group: operate
  title: ''
  type: Support
  url: https://www.agnovos.com/en/contact/
- group: operate
  title: ''
  type: FAQ
  url: https://www.agnovos.com/en/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agnovos.com/en/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agnovos.com/en/terms-of-use/
- group: build
  title: ''
  type: CodeOfConduct
  url: https://www.agnovos.com/en/commitment-to-ethics/
- group: company
  title: ''
  type: Careers
  url: https://www.agnovos.com/en/careers/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/agnovos-bioscience_stock/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/agnovos-bioscience
coverage:
  checked: '2026-08-06'
  detail: AgNovos Bioscience sells a physical implant and surgical kit (AGN1 / OSSURE LOEP), not software — its 432-URL Gatsby marketing site has no products, developer, docs or integration path in its own sitemap, api./developers./docs.agnovos.com do not resolve at all, and there is no agnovos GitHub organization or package on any registry.
  evidence:
  - status: 200
    url: https://www.agnovos.com/sitemap-0.xml
  - status: 404
    url: https://www.agnovos.com/openapi.json
  - status: 404
    url: https://www.agnovos.com/llms.txt
  - status: 404
    url: https://www.agnovos.com/.well-known/agent-card.json
  - status: 404
    url: https://www.agnovos.com/.well-known/security.txt
  - status: 0
    url: https://api.agnovos.com/
  - status: 404
    url: https://api.github.com/orgs/agnovos
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'AgNovos Bioscience is a privately held medical technology company developing novel treatments for bone disease, founded in 2012 with offices in New York, Rockville (Maryland), Frankfurt and Dallas. Its lead technology is AGN1, a proprietary triphasic, calcium-based, osteoconductive implant material delivered through the OSSURE Local Osteo-Enhancement Procedure (LOEP) — a minimally invasive procedure intended to immediately, substantially and durably increase the density and strength of osteoporotic bone at sites of highest fracture risk. The company runs an active clinical program (CONFIRM, RECONFIRM, RESTORE and GRACE trials) and sponsors the ESCEO-AgNovos Young Investigator Award. AgNovos ships a physical implant and surgical kit, not software: its public web presence is a corporate and clinical-communications site with no developer program, no public API, and no machine-readable interface of any kind.'
image: https://www.agnovos.com/icons/icon-512x512.png
layout: provider
modified: '2026-08-06'
name: AgNovos Bioscience
nav: Providers
network: true
overview: 'AgNovos Bioscience is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Medical Devices, Healthcare, Life Sciences, and Biotechnology.


  AgNovos Bioscience''s developer surface includes engineering blog, support, FAQ, and 9 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.5
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agnovos-bioscience/refs/heads/main/screenshots/agnovos-bioscience-2026-08-07T161038.png
security:
- kind: domain-security
  name: Agnovos Bioscience Domain Security
  slug: agnovos-bioscience-domain-security
  summary_line: TLSv1.3 · HSTS
slug: agnovos-bioscience
tags:
- Company
- Medical Devices
- Healthcare
- Life Sciences
- Biotechnology
- Orthopedics
- Bone Health
- Osteoporosis
- Regenerative Medicine
- Clinical Research
website: https://www.agnovos.com/
---

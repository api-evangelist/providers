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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/airna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://airna.com/
- group: company
  title: ''
  type: Blog
  url: https://airna.com/news/
- group: company
  title: ''
  type: BlogRSS
  url: https://airna.com/feed/
- group: operate
  title: ''
  type: Contact
  url: https://airna.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://airna.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://airna.com/privacy-policy
- group: company
  title: ''
  type: Careers
  url: https://airna.com/join-us/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/airna-bio
- group: other
  title: ''
  type: InvestmentProfile
  url: https://forgeglobal.com/airna_stock/
coverage:
  checked: '2026-08-06'
  detail: AIRNA is a clinical-stage RNA editing biotechnology company whose product is an oligonucleotide therapeutic (lead program AIR-001 for AATD), not software; airna.com is a WordPress marketing site with no developer, API or documentation section, and every contract-discovery path returned 404.
  evidence:
  - status: 404
    url: https://airna.com/openapi.json
  - status: 404
    url: https://airna.com/developers
  - status: 404
    url: https://airna.com/.well-known/agent-card.json
  - status: 404
    url: https://airna.com/.well-known/security.txt
  - status: 404
    url: https://airna.com/llms.txt
  - status: 401
    url: https://airna.com/wp-json/mcp/mcp-adapter-default-server
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: AIRNA Corporation is a clinical-stage biotechnology company developing precision RNA editing therapeutics based on ADAR (adenosine deaminase acting on RNA), a naturally occurring human protein the company redirects to convert adenosine to inosine at a targeted RNA site — changing protein function without permanently altering DNA. Its oligonucleotide medicines are designed for durable, reversible and repeatable dosing. The lead program, AIR-001, targets alpha-1 antitrypsin deficiency (AATD), alongside cardiometabolic RNA editing programs spanning rare genetic disorders and common conditions. Founded by scientific pioneers of ADAR editing, AIRNA operates from Cambridge, Massachusetts and Tübingen, Germany (AIRNA Bio Germany GmbH). AIRNA publishes no public API, developer portal, SDK, or machine-readable specification; therapeutics, not software, are the product.
image: https://airna.com/wp-content/uploads/2025/03/AIRNA-logo.png
layout: provider
modified: '2026-08-06'
name: AIRNA
nav: Providers
network: true
overview: 'AIRNA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, RNA Editing, and Genetic Medicine.


  AIRNA''s developer surface includes engineering blog and 9 more developer resources.'
random_paper: 76
score:
  band: minimal
  composite: 10.8
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/airna/refs/heads/main/screenshots/airna-2026-08-07T161106.png
security:
- kind: domain-security
  name: Airna Domain Security
  slug: airna-domain-security
  summary_line: TLSv1.3 · DMARC
slug: airna
tags:
- Company
- Biotechnology
- Therapeutics
- RNA Editing
- Genetic Medicine
- Life Sciences
- Rare Disease
- Pharmaceuticals
website: https://airna.com/
---

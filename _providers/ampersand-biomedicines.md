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
  scored_at: '2026-08-10'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ampersand-biomedicines-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ampersand.bio/
- group: company
  title: ''
  type: Blog
  url: https://www.ampersand.bio/news
- group: operate
  title: ''
  type: Contact
  url: https://www.ampersand.bio/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ampersand.bio/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://www.ampersand.bio/cookie-policy
- group: company
  title: ''
  type: Careers
  url: https://www.ampersand.bio/careers
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ampersand-biomedicines
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/AmpersandBio
- group: company
  title: ''
  type: Investor
  url: https://www.flagshippioneering.com/companies/ampersand-biomedicines
- group: other
  title: ''
  type: Profile
  url: https://forgeglobal.com/ampersand-biomedicines_stock/
coverage:
  checked: '2026-08-06'
  detail: Ampersand Biomedicines is a preclinical therapeutics developer whose AND Platform is internal drug-discovery tooling, not a product — the corporate site at ampersand.bio has only Science, Pipeline, Team, News, Careers and Contact sections, no api/docs/developer subdomain resolves in DNS, and every contract-discovery path returned 404.
  evidence:
  - status: 200
    url: https://www.ampersand.bio/
  - status: 404
    url: https://www.ampersand.bio/openapi.json
  - status: 404
    url: https://www.ampersand.bio/llms.txt
  - status: 404
    url: https://www.ampersand.bio/.well-known/agent-card.json
  - status: 404
    url: https://www.ampersand.bio/.well-known/security.txt
  reason: not-a-software-company
  state: none
created: '2026-08-06'
description: 'Ampersand Biomedicines is a Boston-based biotechnology company founded in 2020 out of Flagship Pioneering that designs programmable biologic medicines intended to act only at the site of disease. Its computationally powered Address, Navigate, Determine (AND) Platform pairs a multi-omics "Address Map" of healthy and diseased human tissue with high-throughput microfluidic binder generation and AI-guided binder prediction to design AND-Body therapeutics, which combine a localizing element with an actuator so activity is conditional on the target tissue. The company raised a $65M Series B in March 2025 from Flagship Pioneering and Eli Lilly, and partners with Pioneering Medicines and Pfizer. It is a preclinical therapeutics developer, not a software vendor: the computational platform is internal tooling for its own drug discovery and is not offered to third parties, and the company publishes no public API, developer portal, SDK, or machine-readable specification.'
image: https://cdn.prod.website-files.com/62e1567a532ab570f765e32c/63beca5200a95d31d65346ad_Ampersand-logo-color.svg
layout: provider
modified: '2026-08-06'
name: Ampersand Biomedicines
nav: Providers
network: true
overview: 'Ampersand Biomedicines is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Biotechnology, Therapeutics, Drug Discovery, and Life Sciences.


  Ampersand Biomedicines'' developer surface includes engineering blog and 10 more developer resources.'
random_paper: 55
score:
  band: minimal
  composite: 9.2
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 12.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ampersand-biomedicines/refs/heads/main/screenshots/ampersand-biomedicines-2026-08-07T161340.png
security:
- kind: domain-security
  name: Ampersand Biomedicines Domain Security
  slug: ampersand-biomedicines-domain-security
  summary_line: TLSv1.3 · HSTS
slug: ampersand-biomedicines
tags:
- Company
- Biotechnology
- Therapeutics
- Drug Discovery
- Life Sciences
- Computational Biology
- Precision Medicine
- Flagship Pioneering
website: https://www.ampersand.bio/
---

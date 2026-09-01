---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mos.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mos.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mos.com/privacy-notice/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mos-llms.txt
coverage:
  checked: '2026-08-26'
  detail: Mos ships only a consumer scholarship-matching app — mos.com serves a marketing page plus four legal pages and nothing else; app.mos.com now 301s to the marketing site, and the one real API host, api.mos.com, is an AWS API Gateway that answers 403 Forbidden to every anonymous request including its root, so there is no developer portal, reference, spec or SDK to read.
  evidence:
  - status: 404
    url: https://mos.com/developers
  - status: 404
    url: https://mos.com/openapi.json
  - status: 403
    url: https://api.mos.com/openapi.json
  - status: 301
    url: https://app.mos.com/
  - status: 404
    url: https://mos.com/llms.txt
  reason: no-developer-program
  state: none
created: '2026-08-26'
description: 'Mos is a consumer fintech that helps students find and win money for college. Founded in 2017 by Tunisian human-rights activist Amira Yahyaoui and backed by Sequoia Capital, Lux Capital and Expa, the company began as a financial-aid application service — FAFSA filing plus human advisor support — then added a fee-free student checking account and debit card in 2021. Mos shut the banking product down and cut staff in 2023 after press and investor scrutiny of its account metrics, refocusing on its original financial-aid business. The live product at mos.com is a scholarship-matching app: students swipe through awards drawn from a database the company describes as $160 billion in available funding, with college financial-planning tools and access to a personal advisor. Sequoia''s own company page records Mos as acquired in 2025; the acquirer is not disclosed. Mos ships only an end-user consumer app — it publishes no developer portal, API documentation, SDK or machine-readable contract
  of any kind.'
image: https://mos.com/static/img/shared/phone.png
layout: provider
modified: '2026-08-26'
name: Mos
nav: Providers
network: true
overview: Mos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, Higher Education, Financial Aid, and Scholarships.
random_paper: 20
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 25.9
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Mos Domain Security
  slug: mos-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mos
tags:
- Company
- Education
- Higher Education
- Financial Aid
- Scholarships
- Student Finance
- Fintech
- Consumer Finance
website: https://mos.com/
---

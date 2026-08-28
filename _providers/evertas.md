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
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/evertas-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/evertas-llms.txt
- group: company
  title: ''
  type: Website
  url: https://evertas.com/
- group: company
  title: ''
  type: About
  url: https://evertas.com/about/
- group: other
  title: ''
  type: Team
  url: https://evertas.com/about/
- group: company
  title: ''
  type: Blog
  url: https://evertas.com/news/
- group: company
  title: ''
  type: News
  url: https://evertas.com/news/
- group: operate
  title: ''
  type: FAQ
  url: https://evertas.com/faq/
- group: company
  title: ''
  type: Careers
  url: https://evertas.com/careers/
- group: operate
  title: ''
  type: Contact
  url: https://evertas.com/contact/
- group: operate
  title: ''
  type: Support
  url: https://evertas.com/contact/
- group: commercial
  title: ''
  type: Legal
  url: https://evertas.com/legal/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://evertas.com/legal/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://evertas.com/legal/privacy-policy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Evertas-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/evertas/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Evertas
coverage:
  checked: '2026-08-12'
  detail: Evertas is a Lloyd's-backed crypto and digital-asset insurance underwriter whose entire public web presence is a 117-page Hugo marketing site plus a Brokers Portal that is only a name/email form emailing back a secure document-upload link — policies are bound through appointed brokers, and no developer portal, API reference, SDK, or machine-readable contract exists on any resolving host.
  evidence:
  - status: 200
    url: https://evertas.com/sitemap.xml
  - status: 200
    url: https://evertas.com/portal/
  - status: 404
    url: https://evertas.com/openapi.json
  - status: 404
    url: https://evertas.com/llms.txt
  - status: 404
    url: https://evertas.com/.well-known/agent-card.json
  reason: not-a-software-company
  state: none
created: '2026-08-12'
description: Evertas is a digital-asset insurance underwriter and the first company dedicated exclusively to crypto insurance. Founded in 2017 as BlockRe by J. Gdanski and Raymond Zenkich and rebranded to Evertas in 2020, it underwrites cryptocurrency mining and AI-infrastructure hardware property, platform failure, crime/theft/loss, insider theft/loss, digital property, and directors-and-officers risk. Products are underwritten by certain underwriters at Lloyd's of London and other insurers, carry AM Best and Standard & Poor's creditworthiness ratings, and offer coverage limits up to $600 million per declaration. Policies are distributed exclusively through appointed brokers. Evertas operates a marketing and content site plus an email-gated broker document-upload portal; it publishes no public API, developer portal, SDK, or machine-readable specification.
image: https://evertas.com/img/evertas-logo.svg
layout: provider
modified: '2026-08-12'
name: Evertas
nav: Providers
network: true
overview: 'Evertas is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, Cryptocurrency, Digital Assets, and Risk Management.


  Evertas'' developer surface includes engineering blog, product news, FAQ, support, legal docs, and 12 more developer resources.'
random_paper: 6
score:
  band: minimal
  composite: 10.4
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 21.2
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: domain-security
  name: Evertas Domain Security
  slug: evertas-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: evertas
tags:
- Company
- Insurance
- Cryptocurrency
- Digital Assets
- Risk Management
- Underwriting
- Financial-Services
- Blockchain
website: https://evertas.com/
---

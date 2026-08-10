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
  url: security/cleancapital-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleancapital.com/
- group: company
  title: ''
  type: About
  url: https://cleancapital.com/about/
- group: other
  title: ''
  type: Services
  url: https://cleancapital.com/services/
- group: company
  title: ''
  type: Blog
  url: https://cleancapital.com/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://cleancapital.com/feed/
- group: other
  title: ''
  type: Resources
  url: https://cleancapital.com/thought-leadership/
- group: operate
  title: ''
  type: Contact
  url: https://cleancapital.com/contact/
- group: company
  title: ''
  type: Careers
  url: https://cleancapital.com/careers/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleancapital.com/email-privacy-policy/
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cleancapital-llms.txt
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/cleancapital_stock/
coverage:
  checked: '2026-08-09'
  detail: CleanCapital is a solar and storage asset owner and fund manager whose only web property is a WordPress marketing site — every api./developer./docs./portal./login. subdomain resolves to one wildcard A record with no matching TLS certificate, and its customer portal at app.cleancapital.com 301s to the third-party Dock Energy platform rather than to anything CleanCapital operates.
  evidence:
  - status: 404
    url: https://cleancapital.com/openapi.json
  - status: 404
    url: https://cleancapital.com/.well-known/agent-card.json
  - status: 404
    url: https://cleancapital.com/llms.txt
  - status: 0
    url: https://developer.cleancapital.com/
  - status: 301
    url: https://app.cleancapital.com/api/
  reason: not-a-software-company
  state: none
created: '2026-08-09'
description: 'CleanCapital is a New York based clean energy investment firm, founded in 2015, that develops, constructs, acquires, owns and operates distributed-generation solar and energy storage projects across the United States. It concentrates on the commercial and municipal middle market between residential rooftop and utility-scale generation, selling power to businesses, schools, nonprofits, municipalities and community solar subscribers, and it buys operating and late-stage development projects from developers through a dedicated project-acquisition practice. The firm reports more than $1.5 billion of capital deployed, 450+ MW under management, 235 MW developed and constructed, 200+ energy customers and over 1,000 GWh of emissions-free generation, backed by institutional partners including Manulife Investment Management / John Hancock, BlackRock and CarVal Investors. CleanCapital is an asset owner and investment manager rather than a software vendor: it publishes no developer portal,
  no API documentation and no machine-readable API contract, and its customer portal at app.cleancapital.com now redirects to the third-party Dock Energy platform.'
image: https://cleancapital.com/wp-content/uploads/2022/09/CC_Logo_Hero-1.svg
layout: provider
modified: '2026-08-09'
name: CleanCapital
nav: Providers
network: true
overview: 'CleanCapital is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Energy, Clean Energy, Renewable Energy, and Solar.


  CleanCapital''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 89
score:
  band: minimal
  composite: 9.1
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 2.2
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 13.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
security:
- kind: domain-security
  name: Cleancapital Domain Security
  slug: cleancapital-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cleancapital
tags:
- Company
- Energy
- Clean Energy
- Renewable Energy
- Solar
- Energy Storage
- Investment
- Asset Management
- Infrastructure
- Sustainability
website: https://cleancapital.com/
---

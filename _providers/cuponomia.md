---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
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
  url: security/cuponomia-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cuponomia.com.br
- group: company
  title: ''
  type: Blog
  url: https://www.cuponomia.com.br/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.cuponomia.com.br/perguntas-frequentes
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cuponomia.com.br/privacidade
- group: start
  title: ''
  type: SignUp
  url: https://www.cuponomia.com.br/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cuponomia
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cuponomia.com.br/termos-uso
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/cuponomia-llms.txt
coverage:
  checked: '2026-08-13'
  detail: Cuponomia's own page sitemap enumerates all 16 static pages on www.cuponomia.com.br and none is a developer portal, API reference or partner-API page; no api./developers./docs./parceiros. subdomain resolves in DNS, and its GitHub org publishes only a coding-dojo repo.
  evidence:
  - status: 404
    url: https://www.cuponomia.com.br/openapi.json
  - status: 404
    url: https://www.cuponomia.com.br/llms.txt
  - status: 404
    url: https://www.cuponomia.com.br/.well-known/agent-card.json
  - status: 200
    url: https://www.cuponomia.com.br/page-sitemappp.xml
  - status: 200
    url: https://github.com/cuponomia
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: Cuponomia is a Brazilian coupons and cashback platform that helps consumers save money on online purchases from more than 2,000 partner retailers. A pioneer in popularizing free discount coupons in Brazil, the company expanded into cashback in 2019 and now operates a website, a browser extension, and mobile apps alongside a Prime membership tier. It is backed by 500 Global. Cuponomia does not currently publish a public developer API, SDK, or OpenAPI definition; this profile captures its public web presence and domain-security posture for the API Evangelist network.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cuponomia.png
layout: provider
modified: '2026-08-13'
name: Cuponomia
nav: Providers
network: true
overview: 'Cuponomia is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Coupons, Cashback, Discounts, and E-commerce.


  Cuponomia''s developer surface includes engineering blog, support, signup flow, and 6 more developer resources.'
random_paper: 77
score:
  band: emerging
  composite: 14.6
  delta: 2.9
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 11.7
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Cuponomia Domain Security
  slug: cuponomia-domain-security
  summary_line: TLSv1.2 · DMARC
slug: cuponomia
tags:
- Company
- Coupons
- Cashback
- Discounts
- E-commerce
- Affiliate Marketing
- Deals
- Brazil
- Consumer
website: https://cuponomia.com.br
---

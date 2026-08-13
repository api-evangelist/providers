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
  scored_at: '2026-08-12'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vida-health-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vida-health-llms.txt
- group: company
  title: ''
  type: Website
  url: https://www.vida.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vida.com/resource-library/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vida.com/feed/
- group: operate
  title: ''
  type: Support
  url: https://support.vida.com/hc/en-us
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vidahealth
- group: start
  title: ''
  type: SignUp
  url: https://www.vida.com/clients/onboarding/step/account-creation
- group: start
  title: ''
  type: Login
  url: https://vida.com/accounts/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.vida.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vida.com/privacy-policy/
- group: operate
  title: ''
  type: ContactUs
  url: https://www.vida.com/contact-us/
- group: company
  title: ''
  type: NewsRoom
  url: https://www.vida.com/news-center/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/vida-health_stock/
coverage:
  checked: '2026-08-05'
  detail: Vida's production API host api.vida.com is live but answers HTTP 401 (Invalid or expired access token) on every path including the entire /.well-known/ tree, and there is no developer portal — the Partners page advertises streamlined integrations with existing healthcare ecosystems but publishes no reference or spec, routing every technical question to a contact-sales form.
  evidence:
  - status: 401
    url: https://api.vida.com/openapi.json
  - status: 401
    url: https://api.vida.com/.well-known/openid-configuration
  - status: 401
    url: https://api.vida.com/graphql
  - status: 404
    url: https://www.vida.com/developers
  - status: 404
    url: https://www.vida.com/llms.txt
  - status: 200
    url: https://www.vida.com/partners/
  reason: sales-gate
  state: gated
created: '2026-08-05'
description: 'Vida Health is a San Francisco-based virtual care company founded in 2014 that combines an AI-powered mobile app with a national network of licensed clinicians, coaches and therapists to prevent, manage and reverse chronic cardiometabolic and behavioral health conditions including obesity, diabetes, hypertension, depression and anxiety. Vida sells a turnkey enterprise programme to employers and health plans, layering GLP-1 prescribing and clinical oversight on top of behavioral coaching, and its platform ingests real-time readings from more than 100 connected devices and consumer health apps to feed outcome reporting back to its enterprise buyers. Vida publishes no public developer portal or API documentation: the API host api.vida.com is live but returns 401 on every path, and data/EHR integration for health plans and employers is arranged through enterprise sales rather than self-service onboarding.'
image: https://static.vida.com/wp-content/uploads/2025/03/20211650/Enterprise-3.png
layout: provider
modified: '2026-08-05'
name: Vida Health
nav: Providers
network: true
overview: 'Vida Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Digital Health, and Virtual Care.


  Vida Health''s developer surface includes engineering blog, support, signup flow, and 11 more developer resources.'
random_paper: 15
score:
  band: emerging
  composite: 15.0
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Vida Health Domain Security
  slug: vida-health-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: vida-health
tags:
- Company
- Health
- Healthcare
- Digital Health
- Virtual Care
- Chronic Care
- Behavioral Health
- Telehealth
- Employee Benefits
- Health Plans
website: https://www.vida.com/
---

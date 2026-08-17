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
  band: agent-aware
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
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.8
  scored_at: '2026-08-17'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/plushcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://plushcare.com/
- group: operate
  title: ''
  type: Support
  url: https://support.plushcare.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://plushcare.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://plushcare.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://plushcare.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://plushcare.com/membership
- group: start
  title: ''
  type: Login
  url: https://my.plushcare.com/login
- group: commercial
  title: ''
  type: Plans
  url: plans/plushcare-plans-pricing.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/plushcare-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/plushcare-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/plushcare-lifecycle.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/plushcare-llms.txt
coverage:
  checked: '2026-08-15'
  detail: PlushCare ships only an end-user telehealth product; the single live API host, api.plushcare.com, is the patient app's own Django REST Framework backend whose router root advertises one collection (/users/) that returns 403 anonymously, and every schema path on it (/openapi.json, /swagger.json, /schema/, /docs, /redoc) returns 404, with no developer portal, docs host, SDK or package anywhere.
  evidence:
  - status: 200
    url: https://api.plushcare.com/
  - status: 403
    url: https://api.plushcare.com/users/
  - status: 404
    url: https://api.plushcare.com/openapi.json
  - status: 404
    url: https://developer.plushcare.com/
  - status: 404
    url: https://docs.plushcare.com/
  - status: 404
    url: https://plushcare.com/developers
  - status: 404
    url: https://plushcare.com/.well-known/agent-card.json
  reason: no-developer-program
  state: none
created: '2026-07-17'
description: 'PlushCare is a direct-to-consumer telehealth and virtual primary care service that connects patients with board-certified physicians for online doctor visits, available 24/7 across all 50 US states. Services include online prescriptions and refills, urgent care video visits, mental health care and therapy, weight-loss management including GLP-1 medications, chronic disease management, pediatric and preventive care, and sexual health. Founded in 2014 in San Francisco by Dr. James Wantuck and Ryan McQuaid, PlushCare accepts most major insurance and sells a $19.99/month patient membership. Ownership has changed three times: Accolade acquired PlushCare in 2021, Transcarent acquired Accolade in 2025, and effective 2026-07-31 PlushCare, Inc. became a subsidiary of Fabric Labs, Inc. As a consumer telehealth service, PlushCare publishes no public developer API, developer portal, API reference, SDK, MCP server or agent card; its one live API host, api.plushcare.com, is the patient app''s
  own private Django REST Framework backend and returns 403 anonymously. This profile captures its public web, pricing, compliance and domain-security surface.'
image: https://plushcare.com/hubfs/Logos/logo-plushcare.svg
layout: provider
modified: '2026-08-15'
name: PlushCare
nav: Providers
network: true
overview: 'PlushCare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Telehealth, Telemedicine, and Healthcare.


  PlushCare''s developer surface includes support, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Plushcare Plans Pricing
  plan_count: 1
  slug: plushcare-plans-pricing
random_paper: 73
rate_limits:
- limit_count: 0
  name: Plushcare Rate Limits
  slug: plushcare-rate-limits
score:
  band: emerging
  composite: 25.2
  delta: 13.6
  facets:
    commercial_clarity: 73.7
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 68.5
    governance: 12.5
    operational_transparency: 0.0
  previous_composite: 11.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 30.0
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: rising
security:
- kind: domain-security
  name: Plushcare Domain Security
  slug: plushcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: plushcare
tags:
- Company
- Health
- Telehealth
- Telemedicine
- Healthcare
- Primary Care
- Digital Health
- Mental Health
- Virtual Care
- Consumer Health
website: https://plushcare.com/
---

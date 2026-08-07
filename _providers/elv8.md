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
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/elv8-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.scout-financial.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://s3.us-east-1.amazonaws.com/scout.prod.public.documents/legal/Scout+Terms+of+Use+(10.29.2024).pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://s3.us-east-1.amazonaws.com/scout.prod.public.documents/legal/Scout+Privacy+Policy+2025.pdf
created: '2026-07-17'
description: ELV8 Inc. operates Scout, a financial platform built for college athletes and athletic departments navigating Name, Image, and Likeness (NIL) income. Scout provides NIL income tracking and management, financial education with one-on-one coaching, payment processing for schools (per diems, bonuses, and NIL payments), roster cap-management and compliance tooling, and business-setup assistance such as LLC formation and tax filing. ELV8 Inc. is an SEC-registered investment adviser and works with 30-plus college athletic programs serving thousands of athletes. It was surfaced as a Techstars-backed portfolio company and added to the API Evangelist network. Scout is a consumer/institutional fintech product and does not currently publish a public developer API, SDKs, or API documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/elv8.png
layout: provider
modified: '2026-07-19'
name: ELV8
nav: Providers
network: true
overview: ELV8 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Fintech, Financial Services, NIL, and College Athletics.
random_paper: 44
score:
  band: minimal
  composite: 11.1
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.9
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/elv8/refs/heads/main/screenshots/elv8-2026-07-25T213212.png
security:
- kind: domain-security
  name: Elv8 Domain Security
  slug: elv8-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: elv8
tags:
- Company
- Fintech
- Financial Services
- NIL
- College Athletics
- Payments
- Investment Advisory
- Compliance
website: https://www.scout-financial.com/
---

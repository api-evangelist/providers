---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: true
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
  score: 9.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Pico API lets developers build custom workflows and integrations on the Pico creator platform — including searching and managing contacts across an account. Every request authenticates with an X-A
  name: Pico API
  slug: pico-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pico-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://trypico.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.trypico.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.trypico.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.trypico.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.trypico.com/en/articles/5632118-using-the-pico-api
- group: operate
  title: ''
  type: Support
  url: https://help.trypico.com/
- group: auth
  title: ''
  type: Authentication
  url: authentication/pico-authentication.yml
created: '2026-07-17'
description: Pico is a creator-monetization and CRM platform for online creators, publishers, and media companies, built in New York and backed by Bloomberg Beta. It combines an audience CRM with email capture, landing pages, paywalls, memberships, and subscription payments in a single tool so creators can identify their audience, gate premium content, and convert readers into paying members. Pico raised a $6.5M round in 2021 ("Pico 2.0") and a $10M Series A in 2023, when it rebranded to Hype (hype.co). It exposes a developer API — authenticated with an X-Api-Key header and documented at docs.trypico.com — for searching and managing contacts and integrating the platform into custom workflows.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pico.png
layout: provider
modified: '2026-07-20'
name: Pico
nav: Providers
network: true
overview: 'Pico publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Economy, CRM, Memberships, and Payments.


  Pico''s developer surface includes documentation, API reference, getting-started guide, support, authentication, and 3 more developer resources.'
random_paper: 88
score:
  band: emerging
  composite: 17.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 50.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 17.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: authentication
  name: Pico Authentication
  slug: pico-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Pico Domain Security
  slug: pico-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pico
tags:
- Company
- Creator Economy
- CRM
- Memberships
- Payments
- Email Marketing
- Newsletters
- Monetization
website: https://trypico.com/
---

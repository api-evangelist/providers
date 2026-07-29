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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mycash-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://inremit.co
- group: commercial
  title: ''
  type: TermsOfService
  url: https://inremit.co/terms-condition
created: '2026-07-17'
description: MyCash (operated by IN REMIT PTE LTD, Singapore) is a mobile-only cross-border remittance service built for migrant workers. Through the MyCash Money mobile app, users send money home instantly, reload / top up mobile airtime, and pay bills across supported corridors without needing a traditional bank account. The service targets the unbanked and underbanked migrant population with low-cost digital money transfer and mobile financial services. As of this profile MyCash publishes a consumer mobile application and marketing site (inremit.co) but exposes no public developer API, OpenAPI specification, SDKs, or developer portal; this API Evangelist profile records the company's public web and security posture.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mycash.png
layout: provider
modified: '2026-07-20'
name: MyCash
nav: Providers
network: true
overview: MyCash is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Remittance, Payments, Money Transfer, and Fintech.
random_paper: 29
score:
  band: minimal
  composite: 8.4
  delta: -2.4
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 15.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Mycash Domain Security
  slug: mycash-domain-security
  summary_line: TLSv1.3
slug: mycash
tags:
- Company
- Remittance
- Payments
- Money Transfer
- Fintech
- Financial Services
- Mobile
- Cross-Border Payments
- Singapore
website: https://inremit.co
---

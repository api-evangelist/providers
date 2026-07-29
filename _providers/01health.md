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
  url: security/01health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://01health.ai/
- group: company
  title: ''
  type: About
  url: https://01health.ai/us/about
- group: start
  title: ''
  type: Login
  url: https://app.32co.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://01health.ai/us/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://01health.ai/us/privacy
created: '2026-07-17'
description: 01Health is a UK-based health technology company building clinical infrastructure that lets specialist healthcare be delivered safely inside community and dental clinics rather than only in hospitals. Founded in 2022 by Dr Sonia Szamocki, its platform centralizes patient acquisition, clinical protocols, remote specialist oversight, treatment workflows, procurement, and financial management into a single system, currently spanning orthodontics (32Co) and sleep medicine (Aerox). 01Health is backed by Balderton Capital, Gresham House Ventures, Eka Ventures, and Wavemaker360. No public developer API, OpenAPI, or developer portal has been published to date; this profile captures the company identity and the security posture of its public web surface.
image: https://01health.ai/og-meta-01Health.png
layout: provider
modified: '2026-07-17'
name: 01health
nav: Providers
network: true
overview: 01health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Dental, and Clinical.
random_paper: 34
score:
  band: minimal
  composite: 12.7
  delta: -3.4
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 16.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/01health/refs/heads/main/screenshots/01health-2026-07-25T181027.png
security:
- kind: domain-security
  name: 01Health Domain Security
  slug: 01health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 01health
tags:
- Company
- Health
- Healthcare
- Dental
- Clinical
- Digital Health
- Specialist Care
- Sleep Medicine
- Orthodontics
website: https://01health.ai/
---

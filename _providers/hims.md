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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/hims-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://forhims.com/vulnerability-disclosure-terms
- group: auth
  title: ''
  type: DomainSecurity
  url: security/hims-domain-security.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/hims-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/hims-well-known.yml
- group: company
  title: ''
  type: Website
  url: https://forhims.com
created: '2026-07-17'
description: 'Hims is the men''s brand of Hims & Hers Health, Inc. (NYSE: HIMS), a U.S.-based direct-to-consumer telehealth platform. Through forhims.com it connects patients with licensed medical providers and affiliated pharmacies to offer treatment for sexual health, hair loss, dermatology and skincare, mental health, and weight loss, including provider consultations, personalized prescriptions, and recurring subscription fulfillment shipped to the customer. Hims & Hers operates the sibling Hers brand for women and runs its own pharmacy and fulfillment operations. This API Evangelist profile tracks the company''s public developer, security, and trust surface; Hims does not currently publish a public developer API, so this record is identity- and security-focused rather than spec-bearing.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hims.png
layout: provider
modified: '2026-07-19'
name: Hims
nav: Providers
network: true
overview: Hims is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health, Healthcare, Telehealth, and Wellness.
random_paper: 28
score:
  band: minimal
  composite: 8.6
  delta: -2.2
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 10.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Hims Domain Security
  slug: hims-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Hims Vulnerability Disclosure
  slug: hims-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: hims
tags:
- Company
- Health
- Healthcare
- Telehealth
- Wellness
- Pharmacy
- Consumer
- E-commerce
website: https://forhims.com
---

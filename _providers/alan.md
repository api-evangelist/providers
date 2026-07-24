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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alan-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alan.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alan-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/alan-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alan-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://alan.com/.well-known/security.txt
created: '2026-07-17'
description: Alan is a French digital health insurance and healthcare company that combines health insurance (mutuelle / complementary health), preventive care, and daily health support in a single app. It serves businesses of every size (from independent contractors and very small companies to large enterprises) and individuals such as the self-employed, retirees, and civil servants across France. Alan offers fast reimbursements (90% processed within 24 hours), a 24/7 chat clinic (Clinique Alan) staffed by healthcare professionals, mental health support, eyewear coverage, and an HR-facing platform for administering employee health plans. It reports over one million members and 41,000+ companies. This API Evangelist profile was surfaced from the Index Ventures portfolio; Alan does not currently publish a public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alan.png
layout: provider
modified: '2026-07-17'
name: Alan
nav: Providers
network: true
overview: Alan is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Insurance, Health Insurance, and InsurTech.
random_paper: 4
score:
  band: minimal
  composite: 10.8
  delta: 2.7
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 26.1
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Alan Domain Security
  slug: alan-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Alan Vulnerability Disclosure
  slug: alan-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: alan
tags:
- Company
- Healthcare
- Insurance
- Health Insurance
- InsurTech
- Digital Health
- Employee Benefits
- France
website: https://alan.com
---

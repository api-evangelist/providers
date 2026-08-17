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
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/pluto-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.pluto.health/
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pluto-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pluto.health/
- group: company
  title: ''
  type: Blog
  url: https://pluto.health/news
- group: operate
  title: ''
  type: Support
  url: mailto:hello@pluto.health
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pluto.health/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pluto.health/terms-of-use
created: '2026-07-17'
description: Pluto (Pluto Health, trypluto.com now pluto.health) is an AI-powered clinical intelligence and care-delivery platform that unifies fragmented health data from roughly 90% of US health systems. It aggregates medical records, insurance data, and social determinants of health, then applies AI-driven clinical intelligence to surface care gaps, coordinate preventive care, screenings, vaccines and at-home lab testing, and match patients to clinical trials. Pluto offers turnkey, white-label, or API-based deployment of its clinical operations. It is backed by Sierra Ventures. As of this enrichment pass the company publishes no public developer portal, API reference, SDKs, or documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pluto.png
layout: provider
modified: '2026-07-20'
name: Pluto
nav: Providers
network: true
overview: 'Pluto is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Ai, Healthcare, Clinical Intelligence, and Health Data.


  Pluto''s developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 117
score:
  band: emerging
  composite: 15.2
  delta: 0.0
  facets:
    commercial_clarity: 36.8
    contract_quality: 0.0
    developer_ergonomics: 6.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 15.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 23.8
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: domain-security
  name: Pluto Domain Security
  slug: pluto-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Pluto Trust Center
  slug: pluto-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA
slug: pluto
tags:
- Company
- Ai
- Healthcare
- Clinical Intelligence
- Health Data
- Care Coordination
- Digital Health
- Interoperability
website: https://pluto.health/
---

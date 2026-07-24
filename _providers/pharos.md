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
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pharos-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pharos.health
created: '2026-07-17'
description: Pharos is a healthcare technology company whose stated mission is to improve hospital quality and patient safety. Backed by Felicis, it operates a gated product application (app.pharos.health) and access-restricted documentation (docs.pharos.health requires an access code), indicating an enterprise offering sold to hospitals and health systems rather than a public, self-serve developer platform. As of this enrichment pass Pharos publishes a marketing site but no public API, OpenAPI specification, SDKs, developer portal, or other machine-readable developer surface. Surfaced as a portfolio company of Felicis and added to the API Evangelist network as a lead, this profile is retained for monitoring should a public API program emerge.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pharos.png
layout: provider
modified: '2026-07-20'
name: Pharos
nav: Providers
network: true
overview: Pharos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Patient Safety, Hospitals, and Quality Improvement.
random_paper: 41
score:
  band: minimal
  composite: 7.7
  delta: 0.9
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Pharos Domain Security
  slug: pharos-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: pharos
tags:
- Company
- Healthcare
- Patient Safety
- Hospitals
- Quality Improvement
- Health Technology
- Clinical
website: https://pharos.health
---

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
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 1
apis:
- description: The Daily Journal of the United States Government
  name: Federal Register
  slug: federal-register
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/federal-register-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-register-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.federalregister.gov/reader-aids/developer-resources/rest-api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: The Daily Journal of the United States Government
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-register.png
layout: provider
modified: '2026-05-28'
name: Federal Register
nav: Providers
network: true
overview: Federal Register publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 147
score:
  band: minimal
  composite: 5.8
  delta: -2.4
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/federal-register/refs/heads/main/screenshots/federal-register-2026-06-20T181127.png
security:
- kind: domain-security
  name: Federal Register Domain Security
  slug: federal-register-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Federal Register Vulnerability Disclosure
  slug: federal-register-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: federal-register
tags:
- Government
- Public APIs
website: https://www.federalregister.gov/reader-aids/developer-resources/rest-api
---

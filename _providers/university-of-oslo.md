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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: Courses, lecture videos, detailed information for courses etc. for the University of Oslo (Norway)
  name: University of Oslo
  slug: university-of-oslo
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/university-of-oslo-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/university-of-oslo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.uio.no/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Courses, lecture videos, detailed information for courses etc. for the University of Oslo (Norway)
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/university-of-oslo.png
layout: provider
modified: '2026-05-28'
name: University of Oslo
nav: Providers
network: true
overview: University of Oslo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Open Data and Public APIs.
random_paper: 14
score:
  band: minimal
  composite: 8.2
  delta: 0.0
  facets:
    commercial_clarity: 0.0
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
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/university-of-oslo/refs/heads/main/screenshots/university-of-oslo-2026-06-20T200211.png
security:
- kind: domain-security
  name: University Of Oslo Domain Security
  slug: university-of-oslo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: University Of Oslo Vulnerability Disclosure
  slug: university-of-oslo-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: university-of-oslo
tags:
- Open Data
- Public APIs
website: https://data.uio.no/
---

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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Vaccination data for Malaysia
  name: MyVaccination
  slug: myvaccination
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/myvaccination-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/myvaccination-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://documenter.getpostman.com/view/16605343/Tzm8GG7u
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Vaccination data for Malaysia
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/myvaccination.png
layout: provider
modified: '2026-05-28'
name: MyVaccination
nav: Providers
network: true
overview: MyVaccination publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 5
score:
  band: minimal
  composite: 7.1
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 7.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/myvaccination/refs/heads/main/screenshots/myvaccination-2026-06-20T185922.png
security:
- kind: domain-security
  name: Myvaccination Domain Security
  slug: myvaccination-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Myvaccination Vulnerability Disclosure
  slug: myvaccination-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: myvaccination
tags:
- Health
- Public APIs
website: https://documenter.getpostman.com/view/16605343/Tzm8GG7u
---

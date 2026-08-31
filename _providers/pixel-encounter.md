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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: SVG Icon Generator
  name: Pixel Encounter
  slug: pixel-encounter
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/pixel-encounter-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pixel-encounter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pixelencounter.com/api
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: SVG Icon Generator
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pixel-encounter.png
layout: provider
modified: '2026-05-28'
name: Pixel Encounter
nav: Providers
network: true
overview: Pixel Encounter publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Art And Design and Public APIs.
random_paper: 16
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.7
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pixel-encounter/refs/heads/main/screenshots/pixel-encounter-2026-06-20T191735.png
security:
- kind: domain-security
  name: Pixel Encounter Domain Security
  slug: pixel-encounter-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Pixel Encounter Vulnerability Disclosure
  slug: pixel-encounter-vulnerability-disclosure
  summary_line: disclosure policy published
slug: pixel-encounter
tags:
- Art And Design
- Public APIs
website: https://pixelencounter.com/api
---

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
api_count: 1
apis:
- description: UK Government Open Data
  name: Open Government, UK
  slug: open-government-uk
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/open-government-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-government-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://data.gov.uk/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: UK Government Open Data
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-government-uk.png
layout: provider
modified: '2026-05-28'
name: Open Government, UK
nav: Providers
network: true
overview: Open Government, UK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Government and Public APIs.
random_paper: 37
score:
  band: minimal
  composite: 8.2
  delta: -1.5
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-government-uk/refs/heads/main/screenshots/open-government-uk-2026-06-20T190832.png
security:
- kind: domain-security
  name: Open Government Uk Domain Security
  slug: open-government-uk-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Open Government Uk Vulnerability Disclosure
  slug: open-government-uk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: open-government-uk
tags:
- Government
- Public APIs
website: https://data.gov.uk/
---

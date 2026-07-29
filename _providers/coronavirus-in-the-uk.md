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
- description: UK Government coronavirus data, including deaths and cases by region
  name: Coronavirus in the UK
  slug: coronavirus-in-the-uk
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/coronavirus-in-the-uk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coronavirus-in-the-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coronavirus.data.gov.uk/details/developers-guide
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: UK Government coronavirus data, including deaths and cases by region
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/coronavirus-in-the-uk.png
layout: provider
modified: '2026-05-28'
name: Coronavirus in the UK
nav: Providers
network: true
overview: Coronavirus in the UK publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Health and Public APIs.
random_paper: 26
score:
  band: minimal
  composite: 7.1
  delta: -2.6
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
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/coronavirus-in-the-uk/refs/heads/main/screenshots/coronavirus-in-the-uk-2026-06-20T175037.png
security:
- kind: domain-security
  name: Coronavirus In The Uk Domain Security
  slug: coronavirus-in-the-uk-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Coronavirus In The Uk Vulnerability Disclosure
  slug: coronavirus-in-the-uk-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: coronavirus-in-the-uk
tags:
- Health
- Public APIs
website: https://coronavirus.data.gov.uk/details/developers-guide
---

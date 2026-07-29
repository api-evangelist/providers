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
- description: Bank holidays in England and Wales, Scotland and Northern Ireland
  name: UK Bank Holidays
  slug: uk-bank-holidays
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/uk-bank-holidays-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uk-bank-holidays-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gov.uk/bank-holidays.json
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Bank holidays in England and Wales, Scotland and Northern Ireland
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uk-bank-holidays.png
layout: provider
modified: '2026-05-28'
name: UK Bank Holidays
nav: Providers
network: true
overview: UK Bank Holidays publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Calendar and Public APIs.
random_paper: 67
score:
  band: minimal
  composite: 5.7
  delta: -1.1
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uk-bank-holidays/refs/heads/main/screenshots/uk-bank-holidays-2026-06-20T195958.png
security:
- kind: domain-security
  name: Uk Bank Holidays Domain Security
  slug: uk-bank-holidays-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Uk Bank Holidays Vulnerability Disclosure
  slug: uk-bank-holidays-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: uk-bank-holidays
tags:
- Calendar
- Public APIs
website: https://www.gov.uk/bank-holidays.json
---

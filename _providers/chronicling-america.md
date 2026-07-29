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
- description: Provides access to millions of pages of historic US newspapers from the Library of Congress
  name: Chronicling America
  slug: chronicling-america
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/chronicling-america-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/chronicling-america-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://chroniclingamerica.loc.gov/about/api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Provides access to millions of pages of historic US newspapers from the Library of Congress
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/chronicling-america.png
layout: provider
modified: '2026-05-28'
name: Chronicling America
nav: Providers
network: true
overview: Chronicling America publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include News and Public APIs.
random_paper: 72
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
screenshot: https://raw.githubusercontent.com/api-evangelist/chronicling-america/refs/heads/main/screenshots/chronicling-america-2026-07-25T205313.png
security:
- kind: domain-security
  name: Chronicling America Domain Security
  slug: chronicling-america-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Chronicling America Vulnerability Disclosure
  slug: chronicling-america-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: chronicling-america
tags:
- News
- Public APIs
website: http://chroniclingamerica.loc.gov/about/api/
---

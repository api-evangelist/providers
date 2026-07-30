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
- description: Flexible, RESTful access to the user's inbox
  name: Gmail
  slug: gmail
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/gmail-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gmail-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://developers.google.com/gmail/api/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Flexible, RESTful access to the user's inbox
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gmail.png
layout: provider
modified: '2026-05-28'
name: Gmail
nav: Providers
network: true
overview: Gmail publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Business and Public APIs.
random_paper: 30
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
screenshot: https://raw.githubusercontent.com/api-evangelist/gmail/refs/heads/main/screenshots/gmail-2026-06-20T181930.png
security:
- kind: domain-security
  name: Gmail Domain Security
  slug: gmail-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Gmail Vulnerability Disclosure
  slug: gmail-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: gmail
tags:
- Business
- Public APIs
website: https://developers.google.com/gmail/api/
---

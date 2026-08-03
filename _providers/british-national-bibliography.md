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
  scored_at: '2026-08-03'
api_count: 1
apis:
- description: Books
  name: British National Bibliography
  slug: british-national-bibliography
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/british-national-bibliography-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/british-national-bibliography-domain-security.yml
- group: company
  title: ''
  type: Website
  url: http://bnb.data.bl.uk/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Books
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/british-national-bibliography.png
layout: provider
modified: '2026-05-28'
name: British National Bibliography
nav: Providers
network: true
overview: British National Bibliography publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Books and Public APIs.
random_paper: 32
score:
  band: minimal
  composite: 5.7
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.7
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/british-national-bibliography/refs/heads/main/screenshots/british-national-bibliography-2026-07-25T203931.png
security:
- kind: domain-security
  name: British National Bibliography Domain Security
  slug: british-national-bibliography-domain-security
  summary_line: DMARC
- kind: vulnerability-disclosure
  name: British National Bibliography Vulnerability Disclosure
  slug: british-national-bibliography-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: british-national-bibliography
tags:
- Books
- Public APIs
website: http://bnb.data.bl.uk/
---

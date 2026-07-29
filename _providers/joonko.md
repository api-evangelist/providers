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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/joonko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joonko.co/
created: '2026-07-17'
description: 'joonko is a company surfaced as a portfolio company of insight-partners and added to the API Evangelist network as a stub for enrichment. As of the 2026-07-20 enrichment pass its public web presence is offline: the joonko.co apex resolves no A record (AWS nameservers, domain registered through 2027) and the app.joonko.co CloudFront distribution is dead, while joonko.com is parked and listed for sale on Afternic. Email infrastructure (Google Workspace MX, SPF, DMARC p=none) remains active, but there is no reachable website, developer portal, documentation, or API surface to enroll. No API, OpenAPI, SDK, or developer artifacts could be discovered. The profile remains a dormant lead.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/joonko.png
layout: provider
modified: '2026-07-20'
name: joonko
nav: Providers
network: true
overview: joonko is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.
random_paper: 8
score:
  band: minimal
  composite: 4.1
  delta: -1.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 5.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Joonko Domain Security
  slug: joonko-domain-security
  summary_line: DMARC
slug: joonko
tags:
- Company
website: https://joonko.co/
---

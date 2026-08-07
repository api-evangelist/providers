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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-08-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/metafy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/metafy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metafy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://metafy.gg/
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/metafy-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/metafy-well-known.yml
created: '2026-07-17'
description: Metafy is a consumer marketplace for gaming coaching and mentorship, connecting players with expert coaches and professional gamers for personalized one-on-one lessons, VOD reviews, and guides across popular competitive titles. Metafy operates a consumer web platform at metafy.gg and, as of this enrichment pass, publishes no public developer API, developer portal, or API documentation; the only machine-discoverable surface found was an RFC 9116 /.well-known/security.txt security contact. Surfaced as a portfolio company of dcm-ventures.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metafy.png
layout: provider
modified: '2026-07-20'
name: Metafy
nav: Providers
network: true
overview: Metafy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Coaching, and Esports.
random_paper: 81
score:
  band: minimal
  composite: 7.5
  delta: 0.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
security:
- kind: domain-security
  name: Metafy Domain Security
  slug: metafy-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Metafy Vulnerability Disclosure
  slug: metafy-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: metafy
tags:
- Company
- Consumer
- Gaming
- Coaching
- Esports
- Marketplace
- Mentorship
website: https://metafy.gg/
---

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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 6.3
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 2
common:
- group: company
  title: ''
  type: Website
  url: https://www.moonactive.com/
- group: agent
  title: ''
  type: WellKnown
  url: well-known/moonactive-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/moonactive-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/moonactive-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/moonactive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.moonactive.com/security-report
created: '2026-07-17'
description: MoonActive is a mobile game developer and publisher best known for the casual titles Coin Master and Pet Master. It was surfaced as a portfolio company of Insight Partners and added to the API Evangelist network for enrichment. As a consumer gaming company MoonActive publishes no public developer API, SDK, or documentation surface; the enrichment pass captured its security and domain posture only (a published RFC 9116 security.txt with a security contact and disclosure page, plus probed TLS/SPF/DMARC).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/moonactive.png
layout: provider
modified: '2026-07-20'
name: MoonActive
nav: Providers
network: true
overview: MoonActive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Gaming, Mobile Games, and Entertainment.
random_paper: 76
score:
  band: minimal
  composite: 7.5
  delta: -0.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 61.1
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 8.1
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Moonactive Domain Security
  slug: moonactive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Moonactive Vulnerability Disclosure
  slug: moonactive-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: moonactive
tags:
- Company
- Consumer
- Gaming
- Mobile Games
- Entertainment
- Casual Games
website: https://www.moonactive.com/
---

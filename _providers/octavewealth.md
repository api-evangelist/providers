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
  scored_at: '2026-08-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/octavewealth-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/octavewealth-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/octavewealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://octavewealth.com
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/octavewealth-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/octavewealth-well-known.yml
created: '2026-07-17'
description: Octave Wealth (octavewealth.com) is a Y Combinator-backed company that, based on its name and branding, operates in the wealth and personal-finance space. It was surfaced as a portfolio company of Y Combinator and added to the API Evangelist network for enrichment. As of this enrichment pass the company's public web presence sits behind Cloudflare and exposes no public developer API, documentation, OpenAPI specification, or SDK surface; the only machine-discoverable artifact found was a published RFC 9116 security.txt with a security contact. This profile records that verifiable state rather than a developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/octavewealth.png
layout: provider
modified: '2026-07-20'
name: Octavewealth
nav: Providers
network: true
overview: Octavewealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Wealth Management, Personal Finance, Fintech, and Y Combinator.
random_paper: 52
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
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: domain-security
  name: Octavewealth Domain Security
  slug: octavewealth-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Octavewealth Vulnerability Disclosure
  slug: octavewealth-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: octavewealth
tags:
- Company
- Wealth Management
- Personal Finance
- Fintech
- Y Combinator
- Investing
website: https://octavewealth.com
---

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
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/haaven-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: well-known/haaven-security.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/haaven-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://haaven.com
- group: agent
  title: ''
  type: WellKnown
  url: well-known/haaven-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/haaven-security.txt
created: '2026-07-17'
description: Haaven is a company surfaced as a portfolio company of speedinvest and added to the API Evangelist network as a stub for enrichment. This profile is a lead awaiting the enrichment pipeline. The company's primary web presence is haaven.com, which sits behind a Cloudflare bot challenge; a published RFC 9116 security.txt (security@haaven.com, languages en,nl) and an api.haaven.com host were confirmed during enrichment, but no public OpenAPI, docs, or developer portal could be read.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/haaven.png
layout: provider
modified: '2026-07-19'
name: Haaven
nav: Providers
network: true
overview: Haaven is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Speedinvest, and Portfolio.
random_paper: 53
score:
  band: minimal
  composite: 6.6
  delta: -0.3
  facets:
    commercial_clarity: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 51.9
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 6.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/haaven/refs/heads/main/screenshots/haaven-2026-07-25T220507.png
security:
- kind: domain-security
  name: Haaven Domain Security
  slug: haaven-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Haaven Vulnerability Disclosure
  slug: haaven-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: haaven
tags:
- Company
- Speedinvest
- Portfolio
website: https://haaven.com
---

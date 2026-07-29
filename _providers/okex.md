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
    asyncapi_events: true
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Cryptocurrency exchange based in Seychelles
  name: OKEx
  slug: okex
artifact_total: 4
asyncapis:
- description: AsyncAPI 2.6 description of the OKX (formerly OKEx) V5 public, private, and business WebSocket APIs. OKX exposes three WebSocket endpoints, each carrying a distinct family of channels. All channels sh
  name: OKX V5 WebSocket API
  slug: okx-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/okex-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.okex.com/docs/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: Cryptocurrency exchange based in Seychelles
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/okex.png
layout: provider
modified: '2026-05-29'
name: OKEx
nav: Providers
network: true
overview: 'OKEx publishes 1 API on the [APIs.io](https://apis.io/) network: OKEx. Tagged areas include Cryptocurrency and Public APIs.


  The OKEx catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 34
rules:
- name: OKEx API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: okex-asyncapi-spectral-rules
score:
  band: emerging
  composite: 25.1
  delta: 2.8
  facets:
    commercial_clarity: 0.0
    contract_quality: 54.3
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 47.9
    operational_transparency: 0.0
  previous_composite: 22.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Okex Domain Security
  slug: okex-domain-security
  summary_line: DNSSEC
slug: okex
tags:
- Cryptocurrency
- Public APIs
website: https://www.okex.com/docs/
---

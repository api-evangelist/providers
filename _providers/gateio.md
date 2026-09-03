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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.0
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: API provides spot, margin and futures trading operations
  name: Gateio
  slug: gateio
artifact_total: 4
asyncapis:
- description: 'AsyncAPI 2.6 description of Gate.io''s WebSocket API V4 covering the public Spot and Futures channels, plus the private user-data channels reached via the same WebSocket connections. Source documents: '
  name: Gate.io WebSocket API V4
  slug: gateio-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gateio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.gate.io/api2
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
created: '2026-05-28'
description: API provides spot, margin and futures trading operations
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gateio.png
layout: provider
modified: '2026-05-28'
name: Gateio
nav: Providers
network: true
overview: 'Gateio publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cryptocurrency and Public APIs.


  The Gateio catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
random_paper: 3
rules:
- effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Gateio API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: gateio-asyncapi-spectral-rules
score:
  band: emerging
  composite: 19.4
  coverage:
    artifact_dirs: 4
    catalog_gap: 84.3
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 11.4
    contract_quality: 41.6
    developer_ergonomics: 9.5
    discoverability: 57.4
    governance: 11.4
    operational_transparency: 0.0
  previous_composite: 19.4
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gateio/refs/heads/main/screenshots/gateio-2026-06-20T181701.png
security:
- kind: domain-security
  name: Gateio Domain Security
  slug: gateio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: gateio
tags:
- Cryptocurrency
- Public APIs
website: https://www.gate.io/api2
---

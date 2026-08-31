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
  scored_at: '2026-08-30'
api_count: 1
apis:
- description: Decentralized cryptocurrency exchange
  name: dYdX
  slug: dydx
artifact_total: 5
asyncapis:
- description: AsyncAPI definition for the dYdX v4 Indexer WebSocket API. The Indexer exposes a single WebSocket endpoint that multiplexes subscriptions across several named channels (markets, trades, orderbook, sub
  name: dYdX v4 Indexer WebSocket API
  slug: dydx-asyncapi
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dydx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://docs.dydx.exchange/
- group: other
  title: ''
  type: PublicAPIsListing
  url: https://github.com/public-apis/public-apis
- group: company
  title: ''
  type: Blog
  url: https://dydx.xyz/blog
created: '2026-05-28'
description: Decentralized cryptocurrency exchange
graphqls:
- description: dYdX is a decentralized perpetuals exchange built on its own Cosmos-based L1 blockchain (dYdX Chain, v4). The indexer service provides a read-only GraphQL interface on top of the same data model expos
  name: dYdX GraphQL API
  slug: dydx-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dydx.png
layout: provider
modified: '2026-05-29'
name: dYdX
nav: Providers
network: true
overview: 'dYdX publishes 1 API on the [APIs.io](https://apis.io/) network: dYdX. Tagged areas include Cryptocurrency and Public APIs.


  The dYdX catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  dYdX''s developer surface includes engineering blog and 3 more developer resources.'
random_paper: 0
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: dYdX API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: dydx-asyncapi-spectral-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 83.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 13.6
    contract_quality: 48.7
    developer_ergonomics: 11.9
    discoverability: 57.4
    governance: 13.6
    operational_transparency: 0.0
  previous_composite: 21.9
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dydx/refs/heads/main/screenshots/dydx-2026-06-20T180339.png
security:
- kind: domain-security
  name: Dydx Domain Security
  slug: dydx-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dydx
tags:
- Cryptocurrency
- Public APIs
website: https://docs.dydx.exchange/
---

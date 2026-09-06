---
access_model:
  confidence: high
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: true
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.0
  scored_at: '2026-09-05'
api_count: 3
apis:
- baseURL: https://btcwar.net
  baseurl_source: declared
  description: Sourced and timestamped Binance Spot observations.
  name: BTC War Live Market Data API Market data API
  slug: btc-war-live-market-data-api-market-data-api
artifact_total: 14
collections:
- collection_type: open
  name: BTC War Live Market Data API
  slug: open-btc-war-live-market-data-api-market-data
common:
- group: agent
  title: ''
  type: MCPServer
  url: https://btcwar.net/mcp
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/btc-war-live-market-data-api-market-data-openapi.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/btc-war-live-market-data-api-arazzo.json
- group: other
  title: ''
  type: Overlay
  url: overlays/btc-war-live-market-data-api-market-data-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/btc-war-live-market-data-api-examples.json
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/btc-war-live-market-data-api-vocabulary.yaml
- group: design
  title: ''
  type: DataModel
  url: data-model/btc-war-live-market-data-api-data-model.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/btc-war-live-market-data-api-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/btc-war-live-market-data-api-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/btc-war-live-market-data-api-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/btc-war-live-market-data-api-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/btc-war-live-market-data-api-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/btc-war-live-market-data-api-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/btc-war-live-market-data-api-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://btcwar.net/api/status/v1.json
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/btc-war-live-market-data-api-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/btc-war-live-market-data-api-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/btc-war-live-market-data-api-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/btc-war-live-market-data-api-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/btc-war-live-market-data-api-agentic-access.yaml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/btc-war-live-market-data-api-live-crypto-price.md
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/btc-war-live-market-data-api-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/btc-war-live-market-data-api-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://btcwar.net/.well-known/api-catalog
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/btc-war-live-market-data-api-security.txt
- group: other
  title: ''
  type: ContentSignal
  url: https://btcwar.net/robots.txt
- group: auth
  title: ''
  type: Security
  url: security/btc-war-live-market-data-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/btc-war-live-market-data-api-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/btc-war-live-market-data-api-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/btc-war-live-market-data-api-packages.yml
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/VibeWhip/btc-war
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VibeWhip
- group: operate
  title: ''
  type: Support
  url: https://github.com/VibeWhip/btc-war/discussions
- group: company
  title: ''
  type: Blog
  url: https://medium.com/@binbinwangt
created: '2026-07-18'
description: 'Public, keyless, read-only real-time crypto market-data API from btcwar.net, exposing live Binance Spot snapshots and single-market observations for nine USDT pairs as JSON and Schema.org JSON-LD. Every response carries provenance, a source timestamp, a rolling 24-hour window definition and an explicit limitations statement, and the service fails closed rather than serving a stale or partial value. It ships one of the most complete agent-native discovery stacks in the catalog: OpenAPI 3.1 (canonical and self-contained bundle), an Arazzo 1.1 workflow, JSON Schema 2020-12 validation contracts, a hosted Streamable HTTP MCP server, a published Agent Skill, an agentic-access execution contract, an error catalog, an interpretation vocabulary, an RFC 9727 API catalog, a W3C DCAT 3 catalog, llms.txt and RFC 9116 security.txt.'
examples:
- key_count: 5
  name: Btc War Live Market Data Api Examples
  slug: btc-war-live-market-data-api-examples
image: https://btcwar.net/seo-scenes/modern.webp
json_schemas:
- name: BTC War Live Market Observation
  property_count: 12
  slug: btc-war-live-market-data-api-market-observation-v1.schema
- name: BTC War live market snapshot
  property_count: 12
  slug: btc-war-live-market-data-api-market-snapshot-v1.schema
jsonld:
- class_count: 0
  name: Btc War Live Market Data Api Dcat Context
  property_count: 0
  slug: btc-war-live-market-data-api-dcat
- class_count: 12
  name: Btc War Live Market Data Api Market Snapshot V1. Context
  property_count: 9
  slug: btc-war-live-market-data-api-market-snapshot-v1.context
layout: provider
mcp_servers:
- description: ''
  name: BTC War Live Market Data API MCP Server
  slug: btc-war-live-market-data-api-mcp-server
- description: Read-only, sourced and timestamped Binance Spot USDT market observations.
  name: BTC War Live Market Data API MCP Server
  slug: btc-war-live-market-data-api-mcp-server-2
modified: '2026-08-11'
name: BTC War Live Market Data API
nav: Providers
network: true
overview: 'BTC War Live Market Data API publishes 1 API on the [APIs.io](https://apis.io/) network: Market data API. Tagged areas include Finance, Cryptocurrency, Market Data, Bitcoin, and crypto-price.


  The BTC War Live Market Data API catalog on APIs.io includes 2 JSON-LD contexts.


  BTC War Live Market Data API''s developer surface includes code examples, authentication, changelog, support, engineering blog, and 29 more developer resources.'
plans:
- name: Btc War Live Market Data Api Plans Pricing
  plan_count: 1
  slug: btc-war-live-market-data-api-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Btc War Live Market Data Api Rate Limits
  slug: btc-war-live-market-data-api-rate-limits
score:
  band: developing
  composite: 47.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 71.0
    catalog_earned_first_party: 8.0
    catalog_gap: 44.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 19.7
    contract_quality: 68.7
    developer_ergonomics: 35.7
    discoverability: 92.6
    governance: 19.7
    operational_transparency: 44.7
  previous_composite: 47.9
  provenance:
    agentic_access: unknown
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.3
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/btc-war-live-market-data-api/refs/heads/main/screenshots/btc-war-live-market-data-api-2026-08-17T123059.png
security:
- kind: authentication
  name: Btc War Live Market Data Api Authentication
  slug: btc-war-live-market-data-api-authentication
  summary_line: none · 0 schemes
- kind: domain-security
  name: Btc War Live Market Data Api Domain Security
  slug: btc-war-live-market-data-api-domain-security
  summary_line: TLSv1.3
- kind: vulnerability-disclosure
  name: Btc War Live Market Data Api Vulnerability Disclosure
  slug: btc-war-live-market-data-api-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: btc-war-live-market-data-api
tags:
- Finance
- Cryptocurrency
- Market Data
- Bitcoin
- crypto-price
- binance-spot
- Orderflow
- market-depth
- JSON-LD
- Schema.org
- OpenAPI
- MCP
- Read Only
- No Authentication
- agent-native
- Arazzo
- JSON-Schema
- AgentSkill
---

---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 69.4
  scored_at: '2026-08-17'
api_count: 1
apis:
- description: Read-only REST/HTTP JSON and JSON-LD API for live Binance Spot market snapshots and single-market observations across nine USDT pairs. Keyless, cached to at most 30 seconds, fail-closed on stale data.
  name: BTC War Live Market Data API
  slug: btc-war-live-market-data-api
artifact_total: 14
collections:
- collection_type: open
  name: BTC War Live Market Data API
  slug: open-btc-war-live-market-data-api-market-data
common:
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
  name: mcp
  slug: mcp
- description: ''
  name: btc-war-live-market-data-api-mcp.yml
  slug: btc-war-live-market-data-api-mcpyml
modified: '2026-08-11'
name: BTC War Live Market Data API
nav: Providers
network: true
overview: 'BTC War Live Market Data API publishes 1 API on the [APIs.io](https://apis.io/) network: BTC War Live Market Data API. Tagged areas include finance, cryptocurrency, market-data, bitcoin, and crypto-price.


  The BTC War Live Market Data API catalog on APIs.io includes 2 JSON-LD contexts.


  BTC War Live Market Data API''s developer surface includes code examples, authentication, changelog, support, engineering blog, and 28 more developer resources.'
plans:
- name: Btc War Live Market Data Api Plans Pricing
  plan_count: 1
  slug: btc-war-live-market-data-api-plans-pricing
random_paper: 135
rate_limits:
- limit_count: 0
  name: Btc War Live Market Data Api Rate Limits
  slug: btc-war-live-market-data-api-rate-limits
score:
  band: developing
  composite: 45.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 68.7
    developer_ergonomics: 32.6
    discoverability: 75.9
    governance: 31.3
    operational_transparency: 47.4
  previous_composite: 45.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 48.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
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
- finance
- cryptocurrency
- market-data
- bitcoin
- crypto-price
- binance-spot
- order-flow
- market-depth
- json-ld
- schema.org
- openapi
- mcp
- read-only
- no-authentication
- agent-native
- arazzo
- json-schema
- agent-skill
---

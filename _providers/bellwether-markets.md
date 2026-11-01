---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bellwether Markets Agentic Access
  operation_count: 4
  slug: bellwether-markets-agentic-access
  summary_line: 4 operations
api_count: 1
apis:
- description: Unified prediction-market data API aggregating Kalshi and Polymarket.
  name: Bellwether Markets API
  slug: bellwether-markets-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/bellwether-markets/agentic-access/bellwether-markets-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bellwether-markets-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/bellwether-markets/rules/bellwether-markets-rules.yml
  title: ''
  type: Spectral
  url: rules/bellwether-markets-rules.yml
- group: design
  href: https://artifacts.apis.io/bellwether-markets/json-ld/bellwether-markets-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bellwether-markets-context.jsonld
- group: design
  href: https://artifacts.apis.io/bellwether-markets/vocabulary/bellwether-markets-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bellwether-markets-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/bellwether-markets/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/bellwether-markets/data-model/bellwether-markets-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bellwether-markets-data-model.yml
- group: design
  href: https://artifacts.apis.io/bellwether-markets/errors/bellwether-markets-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bellwether-markets-problem-types.yml
- group: design
  href: https://artifacts.apis.io/bellwether-markets/conformance/bellwether-markets-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bellwether-markets-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bellwether-markets/mcp/bellwether-markets-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bellwether-markets-mcp.yml
- group: other
  href: https://artifacts.apis.io/bellwether-markets/hosts/bellwether-markets-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bellwether-markets-hosts.yml
- group: auth
  href: https://artifacts.apis.io/bellwether-markets/security/bellwether-markets-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bellwether-markets-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bellwether.markets/
- group: docs
  title: ''
  type: Documentation
  url: https://bellwether.markets/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.bellwether.markets/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://buy.stripe.com/eVq28s7MKbIg5J64mk3cc01
created: '2026-10-30'
description: Bellwether Markets provides a unified API that aggregates prediction market data from major platforms like Kalshi and Polymarket. By normalizing disparate schemas into a single, developer‑friendly REST and MCP interface, it enables easy access to market listings, detailed market data, and cross‑venue arbitrage opportunities. The service offers free tier access with generous rate limits, supporting both real‑time data retrieval and integration into AI agents for automated trading strategies. Backed by YC and built after Polymarket’s acquisition, Bellwether aims to simplify the fragmented prediction market landscape for developers and traders alike.
jsonld:
- class_count: 2
  name: Bellwether Markets Context
  property_count: 6
  slug: bellwether-markets-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.baseframelabs.com.
  name: bellwether-markets MCP Server
  slug: bellwether-markets-mcp-yml
modified: '2026-10-30'
name: bellwether-markets
nav: Providers
network: true
overview: 'bellwether-markets is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Prediction-Market, API, FinTech, and Data-Aggregation.


  The bellwether-markets catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  bellwether-markets'' developer surface includes documentation, API reference, pricing, and 12 more developer resources.'
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: bellwether-markets API Rules
  rule_count: 9
  severity_counts:
    error: 7
    hint: 0
    info: 1
    warn: 1
  slug: bellwether-markets-rules
score:
  band: emerging
  composite: 23.4
  coverage:
    artifact_dirs: 15
    catalog_earned: 60.7
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 79.1
    contract_quality: 6.7
    developer_ergonomics: 23.1
    discoverability: 61.7
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bellwether Markets Domain Security
  slug: bellwether-markets-domain-security
  summary_line: TLSv1.3
slug: bellwether-markets
tags:
- Company
- Prediction-Market
- API
- FinTech
- Data-Aggregation
website: https://bellwether.markets/
---

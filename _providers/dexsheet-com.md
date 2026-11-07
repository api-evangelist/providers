---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
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
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: DexSheet provides fee and data APIs for crypto trading venues as documented on the developer portal.
  name: DexSheet API
  slug: dexsheet-api
- description: 'DexSheet API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-05); not the provider''s own document.'
  name: DexSheet API
  slug: dexsheet-com-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/dexsheet-com/plans/dexsheet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dexsheet-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dexsheet-com/rules/dexsheet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dexsheet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dexsheet-com/json-ld/dexsheet-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dexsheet-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dexsheet-com/vocabulary/dexsheet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dexsheet-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dexsheet-com/data-model/dexsheet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dexsheet-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/dexsheet-com/conformance/dexsheet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dexsheet-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dexsheet-com/llms/dexsheet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dexsheet-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dexsheet-com/mcp/dexsheet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dexsheet-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/dexsheet-com/hosts/dexsheet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dexsheet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dexsheet-com/vendors/dexsheet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dexsheet-com-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://dexsheet.com/okx/news/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dexsheet.com/developers/
- group: auth
  href: https://artifacts.apis.io/dexsheet-com/security/dexsheet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dexsheet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dexsheet.com/
coverage:
  checked: '2026-11-05'
  detail: Developer portal provides documentation but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts are publicly available.
  evidence:
  - status: 200
    url: https://dexsheet.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DexSheet provides independent fee, trust and availability sheets for crypto trading venues, aggregating data on transaction costs, safety measures, and service uptime across exchanges. The platform aims to help traders make informed decisions by offering transparent, up-to-date information on fees, security features, and operational reliability of crypto markets.
image: https://dexsheet.com/og/home.png
json_schemas:
- name: GetApiCheckResponse
  property_count: 2
  slug: dexsheet-com-get-api-check-response
- name: PostMcpRequest
  property_count: 4
  slug: dexsheet-com-post-mcp-request
jsonld:
- class_count: 2
  name: Dexsheet Com Context
  property_count: 6
  slug: dexsheet-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at dexsheet.com.
  name: DexSheet MCP Server
  slug: dexsheet-com-mcp-yml
modified: '2026-11-05'
name: DexSheet
nav: Providers
network: true
overview: 'DexSheet is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Fees, Data, and Analytics.


  The DexSheet catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Dexsheet Com Plans Pricing
  plan_count: 9
  slug: dexsheet-com-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: DexSheet API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: dexsheet-com-rules
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 16
    catalog_earned: 63.8
    catalog_earned_first_party: 12.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 9.5
    discoverability: 58.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: weak_tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 15.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dexsheet Com Domain Security
  slug: dexsheet-com-domain-security
  summary_line: TLSv1.3
slug: dexsheet-com
tags:
- Company
- Cryptocurrency
- Fees
- Data
- Analytics
- Trading
website: https://dexsheet.com/
---

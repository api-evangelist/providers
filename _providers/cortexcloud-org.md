---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 13
  human_in_the_loop: 0
  name: Cortexcloud Org Agentic Access
  operation_count: 26
  slug: cortexcloud-org-agentic-access
  summary_line: 26 operations · 13 acting
api_count: 1
apis:
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The Aggregation API from cortexcloud-org — 4 operation(s) for aggregation.
  name: cortexcloud-org Aggregation API
  slug: cortexcloud-org-aggregation-api
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The Bazaar / MCP API from cortexcloud-org — 1 operation(s) for bazaar / mcp.
  name: cortexcloud-org Bazaar / MCP API
  slug: cortexcloud-org-bazaar-mcp-api
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The catalog API from cortexcloud-org — 1 operation(s) for catalog.
  name: cortexcloud-org Catalog API
  slug: cortexcloud-org-catalog-api
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The Data API from cortexcloud-org — 11 operation(s) for data.
  name: cortexcloud-org Data API
  slug: cortexcloud-org-data-api
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The Discovery API from cortexcloud-org — 5 operation(s) for discovery.
  name: cortexcloud-org Discovery API
  slug: cortexcloud-org-discovery-api
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The System API from cortexcloud-org — 1 operation(s) for system.
  name: cortexcloud-org System API
  slug: cortexcloud-org-system-api
- baseURL: https://api.cortexcloud.org
  baseurl_source: declared
  description: The x402 Audit & Trust API from cortexcloud-org — 3 operation(s) for x402 audit & trust.
  name: cortexcloud-org x402 Audit & Trust API
  slug: cortexcloud-org-x402-audit-trust-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/cortexcloud-org/agentic-access/cortexcloud-org-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cortexcloud-org-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/cortexcloud-org/rules/cortexcloud-org-rules.yml
  title: ''
  type: Spectral
  url: rules/cortexcloud-org-rules.yml
- group: design
  href: https://artifacts.apis.io/cortexcloud-org/json-ld/cortexcloud-org-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cortexcloud-org-context.jsonld
- group: design
  href: https://artifacts.apis.io/cortexcloud-org/vocabulary/cortexcloud-org-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cortexcloud-org-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/cortexcloud-org/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/cortexcloud-org/data-model/cortexcloud-org-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cortexcloud-org-data-model.yml
- group: operate
  href: https://artifacts.apis.io/cortexcloud-org/changelog/cortexcloud-org-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/cortexcloud-org-changelog.yml
- group: design
  href: https://artifacts.apis.io/cortexcloud-org/errors/cortexcloud-org-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cortexcloud-org-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cortexcloud-org/conformance/cortexcloud-org-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cortexcloud-org-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cortexcloud-org/llms/cortexcloud-org-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cortexcloud-org-llms.txt
- group: build
  href: https://artifacts.apis.io/cortexcloud-org/mcp/cortexcloud-org-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cortexcloud-org-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cortexcloud-org/mcp/cortexcloud-org-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cortexcloud-org-mcp.yml
- group: other
  href: https://artifacts.apis.io/cortexcloud-org/hosts/cortexcloud-org-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cortexcloud-org-hosts.yml
- group: other
  href: https://artifacts.apis.io/cortexcloud-org/vendors/cortexcloud-org-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cortexcloud-org-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://api.cortexcloud.org/changelog
- group: auth
  href: https://artifacts.apis.io/cortexcloud-org/security/cortexcloud-org-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cortexcloud-org-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cortexcloud.org/
- group: docs
  title: ''
  type: Documentation
  url: https://api.cortexcloud.org/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.cortexcloud.org/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cortexcloud.org/
- group: operate
  title: ''
  type: Support
  url: https://api.cortexcloud.org/health
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jonahthan433/CortexCloud
- group: commercial
  title: ''
  type: Pricing
  url: https://cortexcloud.org/benchmarks.html
created: '2026-10-30'
description: CortexCloud delivers an agent‑native, pay‑per‑call on‑chain data API for AI agents. It provides token intelligence, pricing, risk scoring, wallet intelligence, whale alerts, balances, transaction history, cross‑chain comparison, and chain state. Agents discover the service via well‑known endpoints, obtain pricing through a free 402 challenge, and pay with x402 USDC on Base. The platform emphasizes evidence‑backed JSON responses, zero account requirements, and seamless integration for autonomous agents.
image: https://api.cortexcloud.org/og.png
json_schemas:
- name: NFTOwnershipRequest
  property_count: 3
  slug: cortexcloud-org-nftownership-request
- name: TokenBalancesRequest
  property_count: 4
  slug: cortexcloud-org-token-balances-request
- name: TokenPriceRequest
  property_count: 3
  slug: cortexcloud-org-token-price-request
- name: TxAggregateRequest
  property_count: 3
  slug: cortexcloud-org-tx-aggregate-request
- name: TxHistoryRequest
  property_count: 4
  slug: cortexcloud-org-tx-history-request
- name: WhaleAlertRequest
  property_count: 4
  slug: cortexcloud-org-whale-alert-request
jsonld:
- class_count: 14
  name: Cortexcloud Org Context
  property_count: 20
  slug: cortexcloud-org-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.cortexcloud.org.
  name: cortexcloud-org MCP Server
  slug: cortexcloud-org-mcp-yml
modified: '2026-10-30'
name: cortexcloud-org
nav: Providers
network: true
overview: 'cortexcloud-org publishes 7 API contracts indexed on the [APIs.io](https://apis.io/) network, including Aggregation API, Bazaar / MCP API, Catalog API, and 4 more. Tagged areas include Company, Blockchain, Artificial Intelligence, Payments, and On-Chain Data.


  The cortexcloud-org catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  cortexcloud-org''s developer surface includes changelog, documentation, API reference, support, pricing, and 18 more developer resources.'
random_paper: 9
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: cortexcloud-org API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: cortexcloud-org-rules
scopes:
- name: Cortexcloud Org Scopes
  scope_count: 0
  slug: cortexcloud-org-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.6
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 59.2
    developer_ergonomics: 21.9
    discoverability: 65.0
    operational_transparency: 10.5
  previous_composite: 36.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cortexcloud-org/cortexcloud-org-2026-11-03T125402.png
security:
- kind: authentication
  name: Cortexcloud Org Authentication
  slug: cortexcloud-org-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cortexcloud Org Domain Security
  slug: cortexcloud-org-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: token-balances
  slug: cortexcloud-org-token_balances
slug: cortexcloud-org
tags:
- Company
- Blockchain
- Artificial Intelligence
- Payments
- On-Chain Data
website: https://cortexcloud.org/
---

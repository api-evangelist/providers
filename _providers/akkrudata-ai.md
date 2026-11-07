---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.8
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: AkkruData HTTP API providing financial data, metrics, ownership, corporate events and screening.
  name: AkkruData Financial API
  slug: akkrudata-financial-api
- baseURL: https://api.akkrudata.ai
  baseurl_source: declared
  description: 'AkkruData API as documented publicly: 67 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: AkkruData API
  slug: akkrudata-ai-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/akkrudata-ai/plans/akkrudata-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/akkrudata-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/akkrudata-ai/rules/akkrudata-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/akkrudata-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/akkrudata-ai/json-ld/akkrudata-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/akkrudata-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/akkrudata-ai/vocabulary/akkrudata-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/akkrudata-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/akkrudata-ai/data-model/akkrudata-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/akkrudata-ai-data-model.yml
- group: build
  href: https://artifacts.apis.io/akkrudata-ai/cli/akkrudata-ai-cli.yml
  title: ''
  type: CLI
  url: cli/akkrudata-ai-cli.yml
- group: auth
  href: https://artifacts.apis.io/akkrudata-ai/authentication/akkrudata-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/akkrudata-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/akkrudata-ai/conformance/akkrudata-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/akkrudata-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/akkrudata-ai/llms/akkrudata-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/akkrudata-ai-llms.txt
- group: build
  href: https://artifacts.apis.io/akkrudata-ai/mcp/akkrudata-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/akkrudata-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/akkrudata-ai/mcp/akkrudata-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/akkrudata-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/akkrudata-ai/hosts/akkrudata-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/akkrudata-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/akkrudata-ai/vendors/akkrudata-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/akkrudata-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/akkrudata-ai/packages/akkrudata-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/akkrudata-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/akkrudata-ai/packages/akkrudata-ai-packages.yml
  title: ''
  type: Packages
  url: packages/akkrudata-ai-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.akkrudata.ai/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.akkrudata.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://www.akkrudata.ai/login
- group: start
  title: ''
  type: GettingStarted
  url: https://www.akkrudata.ai/documents/quickstart
- group: auth
  href: https://artifacts.apis.io/akkrudata-ai/security/akkrudata-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/akkrudata-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.akkrudata.ai/
coverage:
  checked: '2026-11-01'
  detail: Documentation provides a base URL but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://www.akkrudata.ai/documents
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: Primary-source financial facts API for AI agents, providing deep, company‑specific data from SEC EDGAR, Korean DART, Japanese EDINET, European ESEF and China A‑share filings. Every detail is preserved and every number traced to the original filing, enabling agents to retrieve structured financial information directly from the source.
image: https://www.akkrudata.ai/akkru-mark-light.png
json_schemas:
- name: GetApiV1DataCompanyListResponse
  property_count: 5
  slug: akkrudata-ai-get-api-v1-data-company-list-response
- name: PostApiV1DataCompareLineItemsResponse
  property_count: 3
  slug: akkrudata-ai-post-api-v1-data-compare-line-items-response
- name: PostApiV1DataFilingsResponse
  property_count: 4
  slug: akkrudata-ai-post-api-v1-data-filings-response
- name: PostApiV1DataLineItemsDimensionalBreakdownResponse
  property_count: 7
  slug: akkrudata-ai-post-api-v1-data-line-items-dimensional-breakdown-response
- name: PostApiV1DataLineItemsResponse
  property_count: 2
  slug: akkrudata-ai-post-api-v1-data-line-items-response
- name: PostApiV1DataStatementResponse
  property_count: 6
  slug: akkrudata-ai-post-api-v1-data-statement-response
jsonld:
- class_count: 20
  name: Akkrudata Ai Context
  property_count: 26
  slug: akkrudata-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.akkrudata.ai requiring OAuth.
  name: AkkruData MCP Server
  slug: akkrudata-ai-mcp-yml
modified: '2026-11-01'
name: AkkruData
nav: Providers
network: true
overview: 'AkkruData is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Data, Artificial Intelligence, and Filings.


  The AkkruData catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AkkruData''s developer surface includes CLI, authentication, pricing, getting-started guide, and 17 more developer resources.'
plans:
- name: Akkrudata Ai Plans Pricing
  plan_count: 3
  slug: akkrudata-ai-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Akkrudata Ai Rate Limits
  slug: akkrudata-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: AkkruData API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: akkrudata-ai-rules
scopes:
- name: Akkrudata Ai Scopes
  scope_count: 0
  slug: akkrudata-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.7
  coverage:
    artifact_dirs: 27
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 32.1
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 38.5
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Akkrudata Ai Authentication
  slug: akkrudata-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Akkrudata Ai Domain Security
  slug: akkrudata-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: akkrudata-ai
tags:
- Finance
- Data
- Artificial Intelligence
- Filings
website: https://www.akkrudata.ai/
---

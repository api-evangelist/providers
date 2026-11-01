---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 61.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Easyparser Com Agentic Access
  operation_count: 4
  slug: easyparser-com-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 1
apis:
- baseURL: https://realtime.easyparser.com
  baseurl_source: declared
  description: Realtime Amazon data operations
  name: easyparser-com Amazon API
  slug: easyparser-com-amazon-api
- baseURL: https://realtime.easyparser.com
  baseurl_source: declared
  description: Asynchronous submission and result retrieval
  name: easyparser-com Bulk API
  slug: easyparser-com-bulk-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/easyparser-com/agentic-access/easyparser-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/easyparser-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/easyparser-com/plans/easyparser-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easyparser-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/easyparser-com/rules/easyparser-com-rules.yml
  title: ''
  type: Spectral
  url: rules/easyparser-com-rules.yml
- group: design
  href: https://artifacts.apis.io/easyparser-com/json-ld/easyparser-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/easyparser-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/easyparser-com/vocabulary/easyparser-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/easyparser-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/easyparser-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/easyparser-com/data-model/easyparser-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/easyparser-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/easyparser-com/authentication/easyparser-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easyparser-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/easyparser-com/errors/easyparser-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/easyparser-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/easyparser-com/conformance/easyparser-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easyparser-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easyparser-com/llms/easyparser-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easyparser-com-llms.txt
- group: build
  href: https://artifacts.apis.io/easyparser-com/mcp/easyparser-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/easyparser-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/easyparser-com/mcp/easyparser-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/easyparser-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/easyparser-com/well-known/easyparser-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easyparser-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/easyparser-com/hosts/easyparser-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easyparser-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easyparser-com/vendors/easyparser-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easyparser-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://easyparser.gitbook.io/easyparser-documentation/getting-started
- group: auth
  href: https://artifacts.apis.io/easyparser-com/security/easyparser-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easyparser-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easyparser.com/
- group: company
  title: ''
  type: Blog
  url: https://easyparser.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://easyparser.gitbook.io/easyparser-documentation/
- group: start
  title: ''
  type: Login
  url: https://app.easyparser.com
- group: commercial
  title: ''
  type: Pricing
  url: https://easyparser.com/pricing
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://easyparser.com/policies/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://app.easyparser.com/signup?source=hero_free_plan
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easyparser.com/policies/terms-service
- group: docs
  title: ''
  type: OpenAPI
  url: https://easyparser.com/openapi.json
created: '2026-10-30'
description: Easyparser provides a real‑time Amazon product data extraction API. It offers endpoints to retrieve product details, offers, search results, and rankings as clean JSON, eliminating IP blocks and CAPTCHAs. The service supports both immediate realtime queries authenticated via an API key in the query string and bulk/data‑service operations authenticated via an api‑key header. Documentation and OpenAPI spec are publicly available.
image: https://easyparser.com/assets/img/thumbnail-xl.jpg
json_schemas:
- name: BulkOperationResult
  property_count: 0
  slug: easyparser-com-bulk-operation-result
- name: BulkRequest
  property_count: 0
  slug: easyparser-com-bulk-request
- name: BulkResponse
  property_count: 4
  slug: easyparser-com-bulk-response
- name: QueryResponse
  property_count: 3
  slug: easyparser-com-query-response
- name: ResponseEnvelope
  property_count: 5
  slug: easyparser-com-response-envelope
jsonld:
- class_count: 74
  name: Easyparser Com Context
  property_count: 181
  slug: easyparser-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.easyparser.com requiring an API key.
  name: easyparser-com MCP Server
  slug: easyparser-com-mcp-yml
modified: '2026-10-30'
name: easyparser-com
nav: Providers
network: true
overview: 'easyparser-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Amazon API and Bulk API. Tagged areas include Company, API, Amazon, Scraping, and Real-time.


  The easyparser-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  easyparser-com''s developer surface includes authentication, getting-started guide, engineering blog, documentation, pricing, signup flow, and 21 more developer resources.'
plans:
- name: Easyparser Com Plans Pricing
  plan_count: 1
  slug: easyparser-com-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Easyparser Com Rate Limits
  slug: easyparser-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: easyparser-com API Rules
  rule_count: 18
  severity_counts:
    error: 16
    hint: 0
    info: 1
    warn: 1
  slug: easyparser-com-rules
scopes:
- name: Easyparser Com Scopes
  scope_count: 0
  slug: easyparser-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 55.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.7
    contract_governance: 79.1
    contract_quality: 63.6
    developer_ergonomics: 42.1
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Easyparser Com Authentication
  slug: easyparser-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Easyparser Com Domain Security
  slug: easyparser-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: easyparser-com-realtime
  slug: easyparser-com-realtime
slug: easyparser-com
tags:
- Company
- API
- Amazon
- Scraping
- Real-time
- Data-Extraction
website: https://easyparser.com/
---

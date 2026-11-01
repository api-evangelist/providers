---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 42.8
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Tenderapi Eu Agentic Access
  operation_count: 5
  slug: tenderapi-eu-agentic-access
  summary_line: 5 operations
api_count: 1
apis:
- baseURL: https://api.tenderapi.eu/api/v1
  baseurl_source: declared
  description: The Organisations API from tenderapi-eu — 3 operation(s) for organisations.
  name: tenderapi-eu Organisations API
  slug: tenderapi-eu-organisations-api
- baseURL: https://api.tenderapi.eu/api/v1
  baseurl_source: declared
  description: The Tenders API from tenderapi-eu — 2 operation(s) for tenders.
  name: tenderapi-eu Tenders API
  slug: tenderapi-eu-tenders-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/tenderapi-eu/agentic-access/tenderapi-eu-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tenderapi-eu-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tenderapi-eu/rate-limits/tenderapi-eu-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tenderapi-eu-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tenderapi-eu/plans/tenderapi-eu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tenderapi-eu-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/rules/tenderapi-eu-rules.yml
  title: ''
  type: Spectral
  url: rules/tenderapi-eu-rules.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/json-ld/tenderapi-eu-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tenderapi-eu-context.jsonld
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/vocabulary/tenderapi-eu-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tenderapi-eu-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tenderapi-eu/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/data-model/tenderapi-eu-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tenderapi-eu-data-model.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/conventions/tenderapi-eu-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tenderapi-eu-conventions.yml
- group: auth
  href: https://artifacts.apis.io/tenderapi-eu/authentication/tenderapi-eu-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tenderapi-eu-authentication.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/errors/tenderapi-eu-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tenderapi-eu-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tenderapi-eu/conformance/tenderapi-eu-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tenderapi-eu-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tenderapi-eu/llms/tenderapi-eu-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tenderapi-eu-llms.txt
- group: build
  href: https://artifacts.apis.io/tenderapi-eu/mcp/tenderapi-eu-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tenderapi-eu-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tenderapi-eu/mcp/tenderapi-eu-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tenderapi-eu-mcp.yml
- group: other
  href: https://artifacts.apis.io/tenderapi-eu/hosts/tenderapi-eu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tenderapi-eu-hosts.yml
- group: other
  href: https://artifacts.apis.io/tenderapi-eu/vendors/tenderapi-eu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tenderapi-eu-vendors.yml
- group: auth
  href: https://artifacts.apis.io/tenderapi-eu/security/tenderapi-eu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenderapi-eu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tenderapi.eu/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dash.tenderapi.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.tenderapi.eu/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.tenderapi.eu/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.tenderapi.eu/getting-started
- group: company
  title: ''
  type: Blog
  url: https://tenderapi.eu/en/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tenderapi.eu/en/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://dash.tenderapi.eu/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tenderapi.eu/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tenderapi.eu/privacy/
- group: other
  title: ''
  type: Imprint
  url: https://tenderapi.eu/imprint/
created: '2026-10-31'
description: EU procurement data API for TED and national portals. Query public tender notices from all 27 EU member states with one REST endpoint. Updated daily. The service provides normalized tender data across Europe, accessible via a simple REST API, with free and paid plans, and includes MCP server support for AI assistants.
image: https://tenderapi.eu/favicon.svg
json_schemas:
- name: OrganisationList
  property_count: 2
  slug: tenderapi-eu-organisation-list
- name: Organisation
  property_count: 3
  slug: tenderapi-eu-organisation
- name: SearchOrganisationsRequest
  property_count: 3
  slug: tenderapi-eu-search-organisations-request
- name: SearchTendersRequest
  property_count: 5
  slug: tenderapi-eu-search-tenders-request
- name: TenderDetail
  property_count: 14
  slug: tenderapi-eu-tender-detail
- name: TenderList
  property_count: 2
  slug: tenderapi-eu-tender-list
jsonld:
- class_count: 10
  name: Tenderapi Eu Context
  property_count: 29
  slug: tenderapi-eu-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.tenderapi.eu requiring an API key.
  name: tenderapi-eu MCP Server
  slug: tenderapi-eu-mcp-yml
modified: '2026-10-31'
name: tenderapi-eu
nav: Providers
network: true
overview: 'tenderapi-eu publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Organisations API and Tenders API. Tagged areas include EU, Procurement, Tenders, API, and Data.


  The tenderapi-eu catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tenderapi-eu''s developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, and 22 more developer resources.'
plans:
- name: Tenderapi Eu Plans Pricing
  plan_count: 3
  slug: tenderapi-eu-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 6
  name: Tenderapi Eu Rate Limits
  slug: tenderapi-eu-rate-limits
rules:
- authorship: generated
  effective_rule_count: 61
  extends:
  - spectral:oas
  name: tenderapi-eu API Rules
  rule_count: 20
  severity_counts:
    error: 18
    hint: 0
    info: 1
    warn: 1
  slug: tenderapi-eu-rules
scopes:
- name: Tenderapi Eu Scopes
  scope_count: 0
  slug: tenderapi-eu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 64.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 99.3
    catalog_earned_first_party: 0.0
    catalog_gap: 15.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 63.6
    developer_ergonomics: 58.8
    discoverability: 65.0
    operational_transparency: 28.4
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
  name: Tenderapi Eu Authentication
  slug: tenderapi-eu-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tenderapi Eu Domain Security
  slug: tenderapi-eu-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 5
skills:
- name: get-organisation-tenders
  slug: tenderapi-eu-get-organisation-tenders
- name: get-organisation
  slug: tenderapi-eu-get-organisation
- name: get-tender
  slug: tenderapi-eu-get-tender
- name: search-organisations
  slug: tenderapi-eu-search-organisations
- name: search-tenders
  slug: tenderapi-eu-search-tenders
slug: tenderapi-eu
tags:
- EU
- Procurement
- Tenders
- API
- Data
website: https://tenderapi.eu/
---

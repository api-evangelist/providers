---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 41.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Proxy API exposing public procurement data from pncp.gov.br without access restrictions.
  name: PNCP API
  slug: pncp-api
- baseURL: https://api.pncp.dev
  baseurl_source: declared
  description: 'pncp-dev API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: pncp-dev API
  slug: pncp-dev-api
artifact_total: 11
common:
- group: operate
  href: https://artifacts.apis.io/pncp-dev/rate-limits/pncp-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/pncp-dev-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/pncp-dev/plans/pncp-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/pncp-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/pncp-dev/rules/pncp-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/pncp-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/pncp-dev/json-ld/pncp-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/pncp-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/pncp-dev/vocabulary/pncp-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/pncp-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/pncp-dev/data-model/pncp-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/pncp-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/pncp-dev/authentication/pncp-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/pncp-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/pncp-dev/errors/pncp-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/pncp-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/pncp-dev/conformance/pncp-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/pncp-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/pncp-dev/llms/pncp-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/pncp-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/pncp-dev/mcp/pncp-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/pncp-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/pncp-dev/well-known/pncp-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/pncp-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/pncp-dev/hosts/pncp-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/pncp-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/pncp-dev/vendors/pncp-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/pncp-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://pncp.dev/status
- group: start
  title: ''
  type: Login
  url: https://pncp.dev/app/login
- group: auth
  href: https://artifacts.apis.io/pncp-dev/security/pncp-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/pncp-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://pncp.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://pncp.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://api.pncp.dev
- group: start
  title: ''
  type: GettingStarted
  url: https://pncp.dev/docs#comecar
- group: commercial
  title: ''
  type: Pricing
  url: https://pncp.dev/precos
- group: commercial
  title: ''
  type: TermsOfService
  url: https://pncp.dev/termos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://pncp.dev/privacidade
coverage:
  checked: '2026-10-31'
  detail: Documentation is public but no machine-readable spec (OpenAPI, AsyncAPI, GraphQL, etc.) is published.
  evidence:
  - status: 200
    url: https://pncp.dev/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: pncp.dev provides an unblocked proxy to the public API of Brazil's National Procurement Portal (PNCP). It mirrors the routes of pncp.gov.br, allowing developers to replace the base address with api.pncp.dev and include their API key in a request header. The service is free to start, requires no credit card, and offers documentation, pricing, and terms in Portuguese.
image: https://pncp.dev/favicon.svg
json_schemas:
- name: GetApiConsultaV1OrgaosResponse
  property_count: 4
  slug: pncp-dev-get-api-consulta-v1-orgaos-response
jsonld:
- class_count: 1
  name: Pncp Dev Context
  property_count: 4
  slug: pncp-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.pncp.dev requiring an API key.
  name: pncp-dev MCP Server
  slug: pncp-dev-mcp-yml
modified: '2026-10-30'
name: pncp-dev
nav: Providers
network: true
overview: 'pncp-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, API Proxy, Public Data, Brazil, and Procurement.


  The pncp-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  pncp-dev''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, and 19 more developer resources.'
plans:
- name: Pncp Dev Plans Pricing
  plan_count: 4
  slug: pncp-dev-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 4
  name: Pncp Dev Rate Limits
  slug: pncp-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: pncp-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: pncp-dev-rules
scopes:
- name: Pncp Dev Scopes
  scope_count: 0
  slug: pncp-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.5
  coverage:
    artifact_dirs: 28
    catalog_earned: 84.7
    catalog_earned_first_party: 0.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 46.9
    developer_ergonomics: 40.5
    discoverability: 56.7
    operational_transparency: 44.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Pncp Dev Authentication
  slug: pncp-dev-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Pncp Dev Domain Security
  slug: pncp-dev-domain-security
  summary_line: TLSv1.3
slug: pncp-dev
tags:
- Company
- API Proxy
- Public Data
- Brazil
- Procurement
- Open Data
website: https://pncp.dev/
---

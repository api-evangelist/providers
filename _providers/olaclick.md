---
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 50.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: REST API for accessing menus, orders, customers, and other resources.
  name: OlaClick Public API
  slug: olaclick-public-api
- baseURL: https://public-api.olaclick.app
  baseurl_source: declared
  description: 'OlaClick API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: OlaClick API
  slug: olaclick-api
artifact_total: 15
common:
- group: operate
  href: https://artifacts.apis.io/olaclick/rate-limits/olaclick-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/olaclick-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/olaclick/rules/olaclick-rules.yml
  title: ''
  type: Spectral
  url: rules/olaclick-rules.yml
- group: design
  href: https://artifacts.apis.io/olaclick/json-ld/olaclick-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/olaclick-context.jsonld
- group: design
  href: https://artifacts.apis.io/olaclick/vocabulary/olaclick-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/olaclick-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/olaclick/data-model/olaclick-data-model.yml
  title: ''
  type: DataModel
  url: data-model/olaclick-data-model.yml
- group: operate
  href: https://artifacts.apis.io/olaclick/changelog/olaclick-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/olaclick-changelog.yml
- group: design
  href: https://artifacts.apis.io/olaclick/conventions/olaclick-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/olaclick-conventions.yml
- group: design
  href: https://artifacts.apis.io/olaclick/conventions/olaclick-conventions.yml
  title: ''
  type: Conventions
  url: conventions/olaclick-conventions.yml
- group: auth
  href: https://artifacts.apis.io/olaclick/authentication/olaclick-authentication.yml
  title: ''
  type: Authentication
  url: authentication/olaclick-authentication.yml
- group: auth
  href: https://artifacts.apis.io/olaclick/scopes/olaclick-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/olaclick-scopes.yml
- group: design
  href: https://artifacts.apis.io/olaclick/errors/olaclick-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/olaclick-problem-types.yml
- group: design
  href: https://artifacts.apis.io/olaclick/conformance/olaclick-conformance.yml
  title: ''
  type: Conformance
  url: conformance/olaclick-conformance.yml
- group: agent
  href: https://artifacts.apis.io/olaclick/llms/olaclick-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/olaclick-llms.txt
- group: agent
  href: https://artifacts.apis.io/olaclick/mcp/olaclick-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/olaclick-mcp.yml
- group: agent
  href: https://artifacts.apis.io/olaclick/well-known/olaclick-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/olaclick-well-known.yml
- group: other
  href: https://artifacts.apis.io/olaclick/hosts/olaclick-hosts.yml
  title: ''
  type: Hosts
  url: hosts/olaclick-hosts.yml
- group: other
  href: https://artifacts.apis.io/olaclick/vendors/olaclick-vendors.yml
  title: ''
  type: Vendors
  url: vendors/olaclick-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://olaclick.com/fr/news/olaclick-is-part-of-y-combinator/
- group: docs
  title: ''
  type: Documentation
  url: https://help.olaclick.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.olaclick.app/docs/
- group: auth
  href: https://artifacts.apis.io/olaclick/security/olaclick-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/olaclick-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.olaclick.com/?lang=en
- group: company
  title: ''
  type: Blog
  url: https://olaclick.com/blog-pt/
- group: commercial
  title: ''
  type: Pricing
  url: https://pricing.olaclick.app/pt
- group: operate
  title: ''
  type: Support
  url: https://help.olaclick.com/pt-br/help/falar-com-o-suporte
- group: start
  title: ''
  type: GettingStarted
  url: https://olaclick.com/ponto-de-venda/
coverage:
  checked: '2026-10-29'
  detail: Documentation provides a Base URL but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://developers.olaclick.app/docs#base-url
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: OlaClick provides an AI‑powered point‑of‑sale (POS) system for restaurants, offering digital menus, WhatsApp chatbot ordering, delivery integration, QR code ordering, inventory management, and analytics. Over 40,000 restaurants use the platform, backed by Google and Meta technologies, with a free trial and pricing starting at R$35 per month.
image: https://dtw3vywy1uzct.cloudfront.net/olaclick-logo-azul.webp
json_schemas:
- name: GetV1CompanyResponse
  property_count: 9
  slug: olaclick-get-v1-company-response
- name: GetV1MenuProductsIdResponse
  property_count: 7
  slug: olaclick-get-v1-menu-products-id-response
- name: GetV1MenuProductsIdVariantsResponse
  property_count: 9
  slug: olaclick-get-v1-menu-products-id-variants-response
- name: GetV1MenuProductsResponse
  property_count: 6
  slug: olaclick-get-v1-menu-products-response
- name: PostOauthTokenRequest
  property_count: 3
  slug: olaclick-post-oauth-token-request
- name: PostV1OrdersRequest
  property_count: 10
  slug: olaclick-post-v1-orders-request
jsonld:
- class_count: 19
  name: Olaclick Context
  property_count: 41
  slug: olaclick-context
layout: provider
mcp_servers:
- description: Remote MCP server at public-api.olaclick.app.
  name: OlaClick MCP Server
  slug: olaclick-mcp-yml
modified: '2026-10-29'
name: OlaClick
nav: Providers
network: true
overview: 'OlaClick is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Restaurant, POS, AI, SaaS, and Delivery.


  The OlaClick catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  OlaClick''s developer surface includes changelog, authentication, documentation, engineering blog, pricing, support, getting-started guide, and 19 more developer resources.'
random_paper: 18
rate_limits:
- limit_count: 1
  name: Olaclick Rate Limits
  slug: olaclick-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: OlaClick API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: olaclick-rules
scopes:
- name: Olaclick Scopes
  scope_count: 23
  slug: olaclick-scopes
  summary_line: 23 scopes
score:
  band: thin
  composite: 34.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 70.8
    catalog_earned_first_party: 8.0
    catalog_gap: 44.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 50.0
    discoverability: 66.7
    operational_transparency: 36.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 9
      marker_coverage: 100.0
      total: 9
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Olaclick Authentication
  slug: olaclick-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Olaclick Domain Security
  slug: olaclick-domain-security
  summary_line: TLSv1.3 · DMARC
slug: olaclick
tags:
- Restaurant
- POS
- AI
- SaaS
- Delivery
website: https://www.olaclick.com/?lang=en
---

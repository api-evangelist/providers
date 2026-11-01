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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Tcgdata Dev Agentic Access
  operation_count: 17
  slug: tcgdata-dev-agentic-access
  summary_line: 17 operations · 1 acting
api_count: 1
apis:
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Account API from tcgdata-dev — 1 operation(s) for account.
  name: tcgdata-dev Account API
  slug: tcgdata-dev-account-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Cards API from tcgdata-dev — 2 operation(s) for cards.
  name: tcgdata-dev Cards API
  slug: tcgdata-dev-cards-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Catalogue API from tcgdata-dev — 2 operation(s) for catalogue.
  name: tcgdata-dev Catalogue API
  slug: tcgdata-dev-catalogue-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The History API from tcgdata-dev — 2 operation(s) for history.
  name: tcgdata-dev History API
  slug: tcgdata-dev-history-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Images API from tcgdata-dev — 1 operation(s) for images.
  name: tcgdata-dev Images API
  slug: tcgdata-dev-images-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Japanese catalogue API from tcgdata-dev — 3 operation(s) for japanese catalogue.
  name: tcgdata-dev Japanese catalogue API
  slug: tcgdata-dev-japanese-catalogue-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Prices API from tcgdata-dev — 2 operation(s) for prices.
  name: tcgdata-dev Prices API
  slug: tcgdata-dev-prices-api
- baseURL: https://tcgdata-api.ottenniels1999.workers.dev
  baseurl_source: declared
  description: The Readable URLs API from tcgdata-dev — 4 operation(s) for readable urls.
  name: tcgdata-dev Readable URLs API
  slug: tcgdata-dev-readable-urls-api
artifact_total: 25
common:
- group: agent
  href: https://artifacts.apis.io/tcgdata-dev/agentic-access/tcgdata-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tcgdata-dev-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/tcgdata-dev/rate-limits/tcgdata-dev-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tcgdata-dev-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/rules/tcgdata-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/tcgdata-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/json-ld/tcgdata-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tcgdata-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/vocabulary/tcgdata-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tcgdata-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/tcgdata-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/data-model/tcgdata-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tcgdata-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tcgdata-dev/authentication/tcgdata-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tcgdata-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/errors/tcgdata-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tcgdata-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tcgdata-dev/conformance/tcgdata-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tcgdata-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tcgdata-dev/llms/tcgdata-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tcgdata-dev-llms.txt
- group: build
  href: https://artifacts.apis.io/tcgdata-dev/mcp/tcgdata-dev-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/tcgdata-dev-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/tcgdata-dev/mcp/tcgdata-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tcgdata-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/tcgdata-dev/hosts/tcgdata-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tcgdata-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/tcgdata-dev/vendors/tcgdata-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tcgdata-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://tcgdata.dev/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://tcgdata.dev/changelog
- group: auth
  href: https://artifacts.apis.io/tcgdata-dev/security/tcgdata-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tcgdata-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tcgdata.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://tcgdata.dev/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tcgdata.dev/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://tcgdata.dev/docs
- group: operate
  title: ''
  type: Support
  url: https://tcgdata.dev/contact
- group: company
  title: ''
  type: Blog
  url: https://tcgdata.dev/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://tcgdata.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tcgdata.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tcgdata.dev/privacy
- group: start
  title: ''
  type: SignUp
  url: https://tcgdata.dev/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tcgdata.dev/docs
created: '2026-10-31'
description: TCGdata.dev provides a REST API delivering EUR price data and daily history for major trading card games such as Pokémon, Magic, Lorcana, One Piece, and Yu‑Gi‑Oh!. The service offers endpoints for price lookup, variant search, and historical trends, supporting developers building gaming and market analytics applications. Comprehensive documentation, pricing plans, and support resources are available on the site.
image: https://tcgdata.dev/icon-512.png
json_schemas:
- name: BatchResponse
  property_count: 2
  slug: tcgdata-dev-batch-response
- name: CatalogueCardList
  property_count: 2
  slug: tcgdata-dev-catalogue-card-list
- name: CatalogueSetList
  property_count: 2
  slug: tcgdata-dev-catalogue-set-list
- name: CatalogueVariantRecordList
  property_count: 2
  slug: tcgdata-dev-catalogue-variant-record-list
- name: ReadableCardList
  property_count: 2
  slug: tcgdata-dev-readable-card-list
- name: UsageResponse
  property_count: 2
  slug: tcgdata-dev-usage-response
jsonld:
- class_count: 47
  name: Tcgdata Dev Context
  property_count: 169
  slug: tcgdata-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at tcgdata.dev requiring an API key.
  name: tcgdata-dev MCP Server
  slug: tcgdata-dev-mcp-yml
modified: '2026-10-31'
name: tcgdata-dev
nav: Providers
network: true
overview: 'tcgdata-dev publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Cards API, Catalogue API, and 5 more. Tagged areas include Company, Trading Cards, Pricing API, REST, and Gaming.


  The tcgdata-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  tcgdata-dev''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 22 more developer resources.'
plans:
- name: Tcgdata Dev Plans Pricing
  plan_count: 0
  slug: tcgdata-dev-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 2
  name: Tcgdata Dev Rate Limits
  slug: tcgdata-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: tcgdata-dev API Rules
  rule_count: 16
  severity_counts:
    error: 14
    hint: 0
    info: 1
    warn: 1
  slug: tcgdata-dev-rules
scopes:
- name: Tcgdata Dev Scopes
  scope_count: 0
  slug: tcgdata-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 30
    catalog_earned: 84.9
    catalog_earned_first_party: 0.0
    catalog_gap: 30.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 63.6
    developer_ergonomics: 63.6
    discoverability: 65.0
    operational_transparency: 50.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 31.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tcgdata Dev Authentication
  slug: tcgdata-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tcgdata Dev Domain Security
  slug: tcgdata-dev-domain-security
  summary_line: TLSv1.3
skill_count: 2
skills:
- name: list-games
  slug: tcgdata-dev-list-games
- name: search-cards
  slug: tcgdata-dev-search-cards
slug: tcgdata-dev
tags:
- Company
- Trading Cards
- Pricing API
- REST
- Gaming
- Data
website: https://tcgdata.dev/
---

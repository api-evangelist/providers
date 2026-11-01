---
agent_readiness:
  band: agent-native
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
    idempotency: verified
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Soldgraph Com Agentic Access
  operation_count: 22
  slug: soldgraph-com-agentic-access
  summary_line: 22 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Account API from soldgraph-com — 1 operation(s) for account.
  name: soldgraph-com Account API
  slug: soldgraph-com-account-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Batches API from soldgraph-com — 2 operation(s) for batches.
  name: soldgraph-com Batches API
  slug: soldgraph-com-batches-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Depop API from soldgraph-com — 1 operation(s) for depop.
  name: soldgraph-com Depop API
  slug: soldgraph-com-depop-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The eBay API from soldgraph-com — 4 operation(s) for ebay.
  name: soldgraph-com eBay API
  slug: soldgraph-com-ebay-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Facebook Marketplace API from soldgraph-com — 2 operation(s) for facebook marketplace.
  name: soldgraph-com Facebook Marketplace API
  slug: soldgraph-com-facebook-marketplace-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Jobs API from soldgraph-com — 1 operation(s) for jobs.
  name: soldgraph-com Jobs API
  slug: soldgraph-com-jobs-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Mercari API from soldgraph-com — 2 operation(s) for mercari.
  name: soldgraph-com Mercari API
  slug: soldgraph-com-mercari-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The OfferUp API from soldgraph-com — 2 operation(s) for offerup.
  name: soldgraph-com Offer Up API
  slug: soldgraph-com-offerup-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Poshmark API from soldgraph-com — 2 operation(s) for poshmark.
  name: soldgraph-com Poshmark API
  slug: soldgraph-com-poshmark-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The TCGplayer API from soldgraph-com — 2 operation(s) for tcgplayer.
  name: soldgraph-com TC Gplayer API
  slug: soldgraph-com-tcgplayer-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Vinted API from soldgraph-com — 2 operation(s) for vinted.
  name: soldgraph-com Vinted API
  slug: soldgraph-com-vinted-api
- baseURL: https://api.soldgraph.com/v1
  baseurl_source: declared
  description: The Whatnot API from soldgraph-com — 1 operation(s) for whatnot.
  name: soldgraph-com Whatnot API
  slug: soldgraph-com-whatnot-api
artifact_total: 26
common:
- group: agent
  href: https://artifacts.apis.io/soldgraph-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/soldgraph-com/agentic-access/soldgraph-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/soldgraph-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/soldgraph-com/rate-limits/soldgraph-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/soldgraph-com-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/rules/soldgraph-com-rules.yml
  title: ''
  type: Spectral
  url: rules/soldgraph-com-rules.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/json-ld/soldgraph-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/soldgraph-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/soldgraph-com/vocabulary/soldgraph-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/soldgraph-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/data-model/soldgraph-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/soldgraph-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/conventions/soldgraph-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/soldgraph-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/conventions/soldgraph-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/soldgraph-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/soldgraph-com/authentication/soldgraph-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/soldgraph-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/lifecycle/soldgraph-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/soldgraph-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/errors/soldgraph-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/soldgraph-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/soldgraph-com/conformance/soldgraph-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/soldgraph-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/soldgraph-com/llms/soldgraph-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/soldgraph-com-llms.txt
- group: build
  href: https://artifacts.apis.io/soldgraph-com/mcp/soldgraph-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/soldgraph-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/soldgraph-com/mcp/soldgraph-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/soldgraph-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/soldgraph-com/hosts/soldgraph-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/soldgraph-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/soldgraph-com/vendors/soldgraph-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/soldgraph-com-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://soldgraph.com/status
- group: commercial
  title: ''
  type: Pricing
  url: https://soldgraph.com/docs/guides/pricing-feature
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/soldgraph
- group: auth
  href: https://artifacts.apis.io/soldgraph-com/security/soldgraph-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/soldgraph-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://soldgraph.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://soldgraph.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://soldgraph.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://soldgraph.com/docs/quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://soldgraph.com/docs/api/overview
- group: start
  title: ''
  type: SignUp
  url: https://soldgraph.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://soldgraph.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://soldgraph.com/privacy
created: '2026-10-31'
description: Soldgraph provides a resale data API that aggregates sold and active listings from major marketplaces such as eBay, Poshmark, Mercari, Depop, Whatnot, OfferUp, Facebook Marketplace, Vinted, and also includes TCGplayer card price data. The service scrapes publicly available listing pages, offering JSON endpoints without requiring user authentication to the source marketplaces. It targets developers building market analysis, price tracking, and inventory tools, delivering up-to-date pricing and sales information across multiple regions and categories.
image: https://soldgraph.com/opengraph-image.jpg
json_schemas:
- name: Batch
  property_count: 6
  slug: soldgraph-com-batch
- name: FacebookListingsJob
  property_count: 7
  slug: soldgraph-com-facebook-listings-job
- name: MercariListingsJob
  property_count: 7
  slug: soldgraph-com-mercari-listings-job
- name: OfferupListingsJob
  property_count: 7
  slug: soldgraph-com-offerup-listings-job
- name: PoshmarkListingsJob
  property_count: 7
  slug: soldgraph-com-poshmark-listings-job
- name: Usage
  property_count: 8
  slug: soldgraph-com-usage
jsonld:
- class_count: 52
  name: Soldgraph Com Context
  property_count: 115
  slug: soldgraph-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.soldgraph.com.
  name: soldgraph-com MCP Server
  slug: soldgraph-com-mcp-yml
modified: '2026-10-31'
name: soldgraph-com
nav: Providers
network: true
overview: 'soldgraph-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Batches API, Depop API, and 9 more. Tagged areas include Company, Resale, Marketplace, Pricing, and Data.


  The soldgraph-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  soldgraph-com''s developer surface includes authentication, pricing, documentation, getting-started guide, API reference, signup flow, and 24 more developer resources.'
random_paper: 8
rate_limits:
- limit_count: 6
  name: Soldgraph Com Rate Limits
  slug: soldgraph-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 60
  extends:
  - spectral:oas
  name: soldgraph-com API Rules
  rule_count: 19
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 1
  slug: soldgraph-com-rules
scopes:
- name: Soldgraph Com Scopes
  scope_count: 0
  slug: soldgraph-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.9
  coverage:
    artifact_dirs: 26
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 65.3
    developer_ergonomics: 56.4
    discoverability: 65.0
    operational_transparency: 49.5
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
  name: Soldgraph Com Authentication
  slug: soldgraph-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Soldgraph Com Domain Security
  slug: soldgraph-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: soldgraph-com
tags:
- Company
- Resale
- Marketplace
- Pricing
- Data
website: https://soldgraph.com/
---

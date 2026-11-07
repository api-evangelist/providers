---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
- description: Provides MCP and REST endpoints for crypto research data as documented on the developer portal.
  name: CryptoSocials API
  slug: cryptosocials-api
- baseURL: https://api.cryptosocials.net
  baseurl_source: declared
  description: 'CryptoSocials API as documented publicly: 34 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: CryptoSocials API
  slug: cryptosocials-net-api
artifact_total: 13
common:
- group: commercial
  href: https://artifacts.apis.io/cryptosocials-net/plans/cryptosocials-net-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cryptosocials-net-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cryptosocials-net/rules/cryptosocials-net-rules.yml
  title: ''
  type: Spectral
  url: rules/cryptosocials-net-rules.yml
- group: design
  href: https://artifacts.apis.io/cryptosocials-net/json-ld/cryptosocials-net-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cryptosocials-net-context.jsonld
- group: design
  href: https://artifacts.apis.io/cryptosocials-net/vocabulary/cryptosocials-net-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cryptosocials-net-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cryptosocials-net/data-model/cryptosocials-net-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cryptosocials-net-data-model.yml
- group: design
  href: https://artifacts.apis.io/cryptosocials-net/conformance/cryptosocials-net-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cryptosocials-net-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cryptosocials-net/llms/cryptosocials-net-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cryptosocials-net-llms.txt
- group: agent
  href: https://artifacts.apis.io/cryptosocials-net/mcp/cryptosocials-net-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cryptosocials-net-mcp.yml
- group: other
  href: https://artifacts.apis.io/cryptosocials-net/hosts/cryptosocials-net-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cryptosocials-net-hosts.yml
- group: other
  href: https://artifacts.apis.io/cryptosocials-net/vendors/cryptosocials-net-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cryptosocials-net-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://cryptosocials.net/agent-access
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.cryptosocials.net</code
- group: auth
  href: https://artifacts.apis.io/cryptosocials-net/security/cryptosocials-net-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cryptosocials-net-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cryptosocials.net/
- group: docs
  title: ''
  type: Documentation
  url: https://cryptosocials.net/developers
- group: docs
  title: ''
  type: APIReference
  url: https://cryptosocials.net/developers
- group: commercial
  title: ''
  type: Pricing
  url: https://cryptosocials.net/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cryptosocials.net/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cryptosocials.net/privacy
- group: operate
  title: ''
  type: Support
  url: https://cryptosocials.net/support
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.cryptosocials.net/mcp
  - status: 200
    url: https://cryptosocials.net/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: CryptoSocials provides live crypto research data through an AI‑agent friendly platform. Users can explore lists, archives, voice‑universe discussions, and agent‑access tools. The service offers a research API (MCP & REST) delivering discover, measure, and price‑context endpoints for cryptocurrency analysis. Free browsing, paid credits, and integration guides are available, supporting developers to build on crypto‑X data.
image: https://cryptosocials.net/brand/social-preview.png
json_schemas:
- name: PostAssetsDetailRequest
  property_count: 9
  slug: cryptosocials-net-post-assets-detail-request
- name: PostAuthorsDetailRequest
  property_count: 9
  slug: cryptosocials-net-post-authors-detail-request
- name: PostListsActivityRequest
  property_count: 19
  slug: cryptosocials-net-post-lists-activity-request
- name: PostMarketHistoryRequest
  property_count: 10
  slug: cryptosocials-net-post-market-history-request
- name: PostQueryAggregateRequest
  property_count: 8
  slug: cryptosocials-net-post-query-aggregate-request
- name: PostQueryPostsRequest
  property_count: 18
  slug: cryptosocials-net-post-query-posts-request
jsonld:
- class_count: 22
  name: Cryptosocials Net Context
  property_count: 44
  slug: cryptosocials-net-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.cryptosocials.net requiring an API key.
  name: CryptoSocials MCP Server
  slug: cryptosocials-net-mcp-yml
modified: '2026-11-04'
name: CryptoSocials
nav: Providers
network: true
overview: 'CryptoSocials is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, Research, and Data.


  The CryptoSocials catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CryptoSocials'' developer surface includes getting-started guide, documentation, API reference, pricing, support, and 15 more developer resources.'
plans:
- name: Cryptosocials Net Plans Pricing
  plan_count: 3
  slug: cryptosocials-net-plans-pricing
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: CryptoSocials API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: cryptosocials-net-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 64.8
    catalog_earned_first_party: 12.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 22.0
    contract_quality: 26.0
    developer_ergonomics: 42.9
    discoverability: 48.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cryptosocials Net Domain Security
  slug: cryptosocials-net-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cryptosocials-net
tags:
- Company
- Cryptocurrency
- Research
- Data
website: https://cryptosocials.net/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 22.5
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Developer documentation hub offering RPC and WebSocket endpoints for 150+ blockchain networks.
  name: Dwellir RPC API
  slug: dwellir-rpc-api
- baseURL: https://api-ethereum-mainnet.n.dwellir.com
  baseurl_source: declared
  description: 'Dwellir API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: Dwellir API
  slug: dwellir-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/dwellir/rules/dwellir-rules.yml
  title: ''
  type: Spectral
  url: rules/dwellir-rules.yml
- group: design
  href: https://artifacts.apis.io/dwellir/json-ld/dwellir-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dwellir-context.jsonld
- group: design
  href: https://artifacts.apis.io/dwellir/vocabulary/dwellir-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dwellir-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dwellir/data-model/dwellir-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dwellir-data-model.yml
- group: design
  href: https://artifacts.apis.io/dwellir/conformance/dwellir-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dwellir-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dwellir/llms/dwellir-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dwellir-llms.txt
- group: agent
  href: https://artifacts.apis.io/dwellir/well-known/dwellir-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dwellir-well-known.yml
- group: other
  href: https://artifacts.apis.io/dwellir/hosts/dwellir-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dwellir-hosts.yml
- group: other
  href: https://artifacts.apis.io/dwellir/vendors/dwellir-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dwellir-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dwellir.com/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://status.dwellir.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dwellir.com/privacy-policy
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.dwellir.com/register
- group: auth
  href: https://artifacts.apis.io/dwellir/security/dwellir-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dwellir-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dwellir.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.dwellir.com/docs
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.dwellir.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.dwellir.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://www.dwellir.com/guides
- group: operate
  title: ''
  type: Support
  url: https://www.dwellir.com/contact
- group: company
  title: ''
  type: Blog
  url: https://www.dwellir.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.dwellir.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dwellir-public
coverage:
  checked: '2026-11-02'
  detail: Docs provide RPC endpoint lists but no owned OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://support.dwellir.com/graphql
  - status: 200
    url: https://www.dwellir.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: Dwellir provides RPC and WebSocket endpoints for over 150 blockchain networks, offering plans that scale to 5,000 requests per second with bursts up to 10,000. Each response costs one credit, with no compute units charged. As a blockchain infrastructure provider, Dwellir runs its own nodes to serve developers, trading teams, and Web3 companies, delivering reliable, high‑throughput access to a wide range of chains.
image: https://www.dwellir.com/dwellir-logo.svg
json_schemas:
- name: GetAccountLimitsResponse
  property_count: 3
  slug: dwellir-get-account-limits-response
- name: GetAuthDeriveApiKeyResponse
  property_count: 3
  slug: dwellir-get-auth-derive-api-key-response
- name: GetMarketsTickerOrderbookResponse
  property_count: 3
  slug: dwellir-get-markets-ticker-orderbook-response
- name: PostAuthApiKeyResponse
  property_count: 3
  slug: dwellir-post-auth-api-key-response
- name: PostPortfolioEventsOrdersRequest
  property_count: 7
  slug: dwellir-post-portfolio-events-orders-request
- name: PostPortfolioEventsOrdersResponse
  property_count: 3
  slug: dwellir-post-portfolio-events-orders-response
jsonld:
- class_count: 7
  name: Dwellir Context
  property_count: 20
  slug: dwellir-context
layout: provider
modified: '2026-11-02'
name: Dwellir
nav: Providers
network: true
overview: 'Dwellir is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Infrastructure, RPC, and Web3.


  The Dwellir catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Dwellir''s developer surface includes signup flow, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 16 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Dwellir API Rules
  rule_count: 44
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 2
  slug: dwellir-rules
score:
  band: emerging
  composite: 24.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.8
    catalog_earned_first_party: 0.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 22.6
    discoverability: 48.2
    operational_transparency: 10.5
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
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dwellir Domain Security
  slug: dwellir-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dwellir
tags:
- Blockchain
- Infrastructure
- RPC
- Web3
website: https://www.dwellir.com
---

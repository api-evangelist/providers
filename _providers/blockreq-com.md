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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 39.3
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Core RPC API providing public EVM RPC endpoints with archive, proof, debug, and trace capabilities across multiple networks.
  name: BlockReq RPC API
  slug: blockreq-rpc-api
- baseURL: https://arc-rpc.blockreq.com
  baseurl_source: declared
  description: 'BlockReq build API as documented publicly: 16 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BlockReq build API
  slug: build-api
- baseURL: https://arc-rpc.blockreq.com
  baseurl_source: declared
  description: 'BlockReq Getting Started API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BlockReq Getting Started API
  slug: getting-started-api
artifact_total: 14
common:
- group: commercial
  href: https://artifacts.apis.io/blockreq-com/plans/blockreq-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blockreq-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blockreq-com/rules/blockreq-com-rules.yml
  title: ''
  type: Spectral
  url: rules/blockreq-com-rules.yml
- group: design
  href: https://artifacts.apis.io/blockreq-com/json-ld/blockreq-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blockreq-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/blockreq-com/vocabulary/blockreq-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blockreq-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blockreq-com/data-model/blockreq-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blockreq-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/blockreq-com/authentication/blockreq-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blockreq-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/blockreq-com/conformance/blockreq-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockreq-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blockreq-com/llms/blockreq-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockreq-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/blockreq-com/well-known/blockreq-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockreq-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/blockreq-com/hosts/blockreq-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockreq-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockreq-com/vendors/blockreq-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockreq-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://blockreq.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/blockreq-com/security/blockreq-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockreq-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blockreq.com/
- group: docs
  title: ''
  type: Documentation
  url: https://blockreq.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://blockreq.com/docs/api
- group: commercial
  title: ''
  type: Pricing
  url: https://blockreq.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://blockreq.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blockreq.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://blockreq.com/privacy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/blockreq
coverage:
  checked: '2026-11-02'
  detail: Documentation is provided as markdown pages without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract.
  evidence:
  - status: 200
    url: https://blockreq.com/docs/build/api-reference/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BlockReq provides public EVM RPC endpoints with archive, proof, debug, and trace capabilities across 20 networks. It offers free tier access (3M requests per 30 days) and pay‑as‑you‑go pricing, supporting HTTPS and WebSocket. The service targets developers and AI assistants needing reliable blockchain data without requiring API keys for basic usage.
image: https://blockreq.com/og-image.jpg
json_schemas:
- name: GetApiDashboardCreditsResponse
  property_count: 3
  slug: blockreq-com-get-api-dashboard-credits-response
- name: PatchApiDashboardEndpointsRequest
  property_count: 2
  slug: blockreq-com-patch-api-dashboard-endpoints-request
- name: PostApiDashboardEndpointsRequest
  property_count: 2
  slug: blockreq-com-post-api-dashboard-endpoints-request
- name: PostDashboardEndpointsRequest
  property_count: 1
  slug: blockreq-com-post-dashboard-endpoints-request
- name: PostV1RpcBrq1P0000000000000000000000000000000000000000000000
  property_count: 4
  slug: blockreq-com-post-v1-rpc-brq1-p0000000000000000000000000000000000000000000000
- name: PostV1RpcPublicRequest
  property_count: 4
  slug: blockreq-com-post-v1-rpc-public-request
jsonld:
- class_count: 6
  name: Blockreq Com Context
  property_count: 10
  slug: blockreq-com-context
layout: provider
modified: '2026-11-02'
name: BlockReq
nav: Providers
network: true
overview: 'BlockReq is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including build API, Getting Started API, and 1 more. Tagged areas include Company, Blockchain, RPC, EVM, and Infrastructure.


  The BlockReq catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlockReq''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, GitHub presence, and 14 more developer resources.'
plans:
- name: Blockreq Com Plans Pricing
  plan_count: 7
  slug: blockreq-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: BlockReq API Rules
  rule_count: 48
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 4
  slug: blockreq-com-rules
score:
  band: thin
  composite: 31.8
  coverage:
    artifact_dirs: 17
    catalog_earned: 72.8
    catalog_earned_first_party: 12.0
    catalog_gap: 42.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 27.4
    discoverability: 62.5
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Blockreq Com Authentication
  slug: blockreq-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Blockreq Com Domain Security
  slug: blockreq-com-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: blockreq-com
tags:
- Company
- Blockchain
- RPC
- EVM
- Infrastructure
- Developer Tools
website: https://blockreq.com/
---

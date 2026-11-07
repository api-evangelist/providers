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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: mostly
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://virginia.builder.blockrazor.io
  baseurl_source: declared
  description: 'BlockRazor API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BlockRazor API
  slug: blockrazor-io-api
artifact_total: 11
common:
- group: commercial
  href: https://artifacts.apis.io/blockrazor-io/plans/blockrazor-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blockrazor-io-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/blockrazor-io/rules/blockrazor-io-rules.yml
  title: ''
  type: Spectral
  url: rules/blockrazor-io-rules.yml
- group: design
  href: https://artifacts.apis.io/blockrazor-io/json-ld/blockrazor-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/blockrazor-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/blockrazor-io/vocabulary/blockrazor-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/blockrazor-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/blockrazor-io/data-model/blockrazor-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/blockrazor-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/blockrazor-io/cli/blockrazor-io-cli.yml
  title: ''
  type: CLI
  url: cli/blockrazor-io-cli.yml
- group: design
  href: https://artifacts.apis.io/blockrazor-io/conformance/blockrazor-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/blockrazor-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/blockrazor-io/llms/blockrazor-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blockrazor-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/blockrazor-io/well-known/blockrazor-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/blockrazor-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/blockrazor-io/hosts/blockrazor-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blockrazor-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/blockrazor-io/vendors/blockrazor-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/blockrazor-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://blockrazor.io/terms/
- group: operate
  title: ''
  type: Support
  url: https://blockrazor.io/support/
- group: start
  title: ''
  type: SignUp
  url: https://blockrazor.io/register?redirect=onboarding
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.blockrazor.io/statement/privacy-statement
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BlockRazorinc
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.blockrazor.io/get-started/use-cases
- group: company
  title: ''
  type: Blog
  url: https://blockrazor.io/blog/
- group: auth
  href: https://artifacts.apis.io/blockrazor-io/security/blockrazor-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blockrazor-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blockrazor.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.blockrazor.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://blockrazor.io/pricing/
coverage:
  checked: '2026-11-02'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found despite accessible markdown documentation.
  evidence:
  - status: 200
    url: https://docs.blockrazor.io/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: BlockRazor provides low-latency Web3 infrastructure, offering blockchain data streams, mempool information, and transaction submission services for wallets, DEXs, trading bots, searchers, and quant trading teams across multiple chains such as BNB Chain, Solana, Robinhood Chain, Ethereum, and Base. The platform aims to deliver faster transaction processing and earlier data access for developers building high-performance blockchain applications.
image: https://blockrazor.io/razor.svg
json_schemas:
- name: GetBundlestateResponse
  property_count: 1
  slug: blockrazor-io-get-bundlestate-response
- name: PostEthSendrawtransactionRequest
  property_count: 4
  slug: blockrazor-io-post-eth-sendrawtransaction-request
- name: PostRequest
  property_count: 4
  slug: blockrazor-io-post-request
- name: PostSendbatchRequest
  property_count: 4
  slug: blockrazor-io-post-sendbatch-request
- name: PostSendbundleRequest
  property_count: 1
  slug: blockrazor-io-post-sendbundle-request
- name: PostSendtransactionRequest
  property_count: 4
  slug: blockrazor-io-post-sendtransaction-request
jsonld:
- class_count: 8
  name: Blockrazor Io Context
  property_count: 11
  slug: blockrazor-io-context
layout: provider
modified: '2026-11-02'
name: BlockRazor
nav: Providers
network: true
overview: 'BlockRazor is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Blockchain, Infrastructure, Low Latency, Web3, and Data Streams.


  The BlockRazor catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlockRazor''s developer surface includes CLI, support, signup flow, getting-started guide, engineering blog, documentation, pricing, and 15 more developer resources.'
plans:
- name: Blockrazor Io Plans Pricing
  plan_count: 3
  slug: blockrazor-io-plans-pricing
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 88
  extends:
  - spectral:oas
  name: BlockRazor API Rules
  rule_count: 47
  severity_counts:
    error: 42
    hint: 0
    info: 2
    warn: 3
  slug: blockrazor-io-rules
score:
  band: thin
  composite: 31.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 26.1
    developer_ergonomics: 21.4
    discoverability: 66.1
    operational_transparency: 2.6
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
  name: Blockrazor Io Domain Security
  slug: blockrazor-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blockrazor-io
tags:
- Blockchain
- Infrastructure
- Low Latency
- Web3
- Data Streams
- Company
website: https://blockrazor.io/
---

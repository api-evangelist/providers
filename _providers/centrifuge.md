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
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 20.7
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Centrifuge provides a GraphQL API for interacting with asset pools and financing requests, as documented on the developer portal.
  name: Centrifuge API
  slug: centrifuge-api-2
- baseURL: https://api.centrifuge.io
  baseurl_source: declared
  description: 'Centrifuge API as documented publicly: 7 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Centrifuge API
  slug: centrifuge-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/centrifuge/rules/centrifuge-rules.yml
  title: ''
  type: Spectral
  url: rules/centrifuge-rules.yml
- group: design
  href: https://artifacts.apis.io/centrifuge/json-ld/centrifuge-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/centrifuge-context.jsonld
- group: design
  href: https://artifacts.apis.io/centrifuge/vocabulary/centrifuge-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/centrifuge-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/centrifuge/data-model/centrifuge-data-model.yml
  title: ''
  type: DataModel
  url: data-model/centrifuge-data-model.yml
- group: design
  href: https://artifacts.apis.io/centrifuge/conformance/centrifuge-conformance.yml
  title: ''
  type: Conformance
  url: conformance/centrifuge-conformance.yml
- group: other
  href: https://artifacts.apis.io/centrifuge/grpc/p2p.proto
  title: ''
  type: Protobuf
  url: grpc/p2p.proto
- group: other
  href: https://artifacts.apis.io/centrifuge/grpc/generic.proto
  title: ''
  type: Protobuf
  url: grpc/generic.proto
- group: other
  href: https://artifacts.apis.io/centrifuge/grpc/error.proto
  title: ''
  type: Protobuf
  url: grpc/error.proto
- group: other
  href: https://artifacts.apis.io/centrifuge/grpc/entity.proto
  title: ''
  type: Protobuf
  url: grpc/entity.proto
- group: other
  href: https://artifacts.apis.io/centrifuge/grpc/document_common.proto
  title: ''
  type: Protobuf
  url: grpc/document_common.proto
- group: other
  href: https://artifacts.apis.io/centrifuge/grpc/coredocument.proto
  title: ''
  type: Protobuf
  url: grpc/coredocument.proto
- group: agent
  href: https://artifacts.apis.io/centrifuge/llms/centrifuge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/centrifuge-llms.txt
- group: other
  href: https://artifacts.apis.io/centrifuge/hosts/centrifuge-hosts.yml
  title: ''
  type: Hosts
  url: hosts/centrifuge-hosts.yml
- group: other
  href: https://artifacts.apis.io/centrifuge/vendors/centrifuge-vendors.yml
  title: ''
  type: Vendors
  url: vendors/centrifuge-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://centrifuge.io/terms
- group: company
  title: ''
  type: Newsroom
  url: https://centrifuge.io/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/centrifuge/
- group: company
  title: ''
  type: Blog
  url: https://centrifuge.io/blog
- group: auth
  href: https://artifacts.apis.io/centrifuge/security/centrifuge-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/centrifuge-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://centrifuge.io/
- group: docs
  title: ''
  type: Documentation
  url: https://api.centrifuge.io/
- group: docs
  title: ''
  type: APIReference
  url: https://api.centrifuge.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.centrifuge.io/
- group: start
  title: ''
  type: GettingStarted
  url: https://api.centrifuge.io/
created: '2026-10-29'
description: Centrifuge is a decentralized finance (DeFi) platform that enables businesses to tokenize real‑world assets and obtain financing through blockchain technology. The company provides a GraphQL API that developers can use to interact with asset pools, submit financing requests, and retrieve on‑chain data. Backed by Crane Venture Partners, Centrifuge focuses on bridging traditional finance and decentralized ecosystems, offering tools for asset originators, investors, and developers.
image: https://cdn.prod.website-files.com/6706324b4c48131ee537ff96/687e239782203000d816ce87_Centrifuge%20OpenGraph%20-%20Home.png
json_schemas:
- name: GetBridgeQuoteResponse
  property_count: 10
  slug: centrifuge-get-bridge-quote-response
- name: GetBridgeRoutesResponse
  property_count: 15
  slug: centrifuge-get-bridge-routes-response
- name: GetBridgeStatusResponse
  property_count: 8
  slug: centrifuge-get-bridge-status-response
- name: GetBridgeTransactionTxhashResponse
  property_count: 8
  slug: centrifuge-get-bridge-transaction-txhash-response
- name: GetPingResponse
  property_count: 2
  slug: centrifuge-get-ping-response
- name: GetTokensAddressTotalIssuanceResponse
  property_count: 1
  slug: centrifuge-get-tokens-address-total-issuance-response
jsonld:
- class_count: 7
  name: Centrifuge Context
  property_count: 32
  slug: centrifuge-context
layout: provider
modified: '2026-10-29'
name: Centrifuge
nav: Providers
network: true
overview: 'Centrifuge is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, DeFi, Asset-Tokenization, Blockchain, and Fintech.


  The Centrifuge catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Centrifuge''s developer surface includes engineering blog, documentation, API reference, getting-started guide, and 20 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Centrifuge API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: centrifuge-rules
score:
  band: emerging
  composite: 23.2
  coverage:
    artifact_dirs: 18
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 37.3
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 14.3
    contract_governance: 22.0
    contract_quality: 24.9
    developer_ergonomics: 20.2
    discoverability: 74.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 30.8
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
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/centrifuge/centrifuge-2026-11-03T123656.png
security:
- kind: domain-security
  name: Centrifuge Domain Security
  slug: centrifuge-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: centrifuge
tags:
- Company
- DeFi
- Asset-Tokenization
- Blockchain
- Fintech
website: https://centrifuge.io/
---

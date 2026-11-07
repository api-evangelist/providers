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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Documentation for Sei blockchain platform, covering EVM, nodes, tools, and ecosystem.
  name: Sei Docs API
  slug: sei-docs-api
- description: 'Sei API as documented publicly: 19 operations. Contract generated from the documentation by API Evangelist (2026-10-26); not the provider''s own document.'
  name: Sei API
  slug: seinetwork-io-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/seinetwork-io/rules/seinetwork-io-rules.yml
  title: ''
  type: Spectral
  url: rules/seinetwork-io-rules.yml
- group: design
  href: https://artifacts.apis.io/seinetwork-io/json-ld/seinetwork-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/seinetwork-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/seinetwork-io/vocabulary/seinetwork-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seinetwork-io-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/seinetwork-io/data-model/seinetwork-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seinetwork-io-data-model.yml
- group: build
  href: https://artifacts.apis.io/seinetwork-io/cli/seinetwork-io-cli.yml
  title: ''
  type: CLI
  url: cli/seinetwork-io-cli.yml
- group: operate
  href: https://artifacts.apis.io/seinetwork-io/changelog/seinetwork-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seinetwork-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/seinetwork-io/conformance/seinetwork-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seinetwork-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/seinetwork-io/llms/seinetwork-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/seinetwork-io-llms.txt
- group: other
  href: https://artifacts.apis.io/seinetwork-io/a2a/seinetwork-io-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/seinetwork-io-a2a.yml
- group: agent
  href: https://artifacts.apis.io/seinetwork-io/well-known/seinetwork-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/seinetwork-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/seinetwork-io/hosts/seinetwork-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seinetwork-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/seinetwork-io/vendors/seinetwork-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seinetwork-io-vendors.yml
- group: build
  href: https://artifacts.apis.io/seinetwork-io/packages/seinetwork-io-packages.yml
  title: ''
  type: SDKs
  url: packages/seinetwork-io-packages.yml
- group: build
  href: https://artifacts.apis.io/seinetwork-io/packages/seinetwork-io-packages.yml
  title: ''
  type: Packages
  url: packages/seinetwork-io-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.sei.io/learn/user-quickstart
- group: auth
  href: https://artifacts.apis.io/seinetwork-io/security/seinetwork-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seinetwork-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seinetwork.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.sei.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.sei.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sei-protocol
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dashboard.sei.io/terms
coverage:
  checked: '2026-10-26'
  detail: Docs site renders content via JavaScript, no machine‑readable OpenAPI spec found.
  evidence:
  - status: 404
    url: https://docs.sei.io/openapi.json
  - status: 404
    url: https://docs.sei.io/openapi.yaml
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-25'
description: Sei is a blockchain infrastructure platform focused on high-performance, low-latency trading and decentralized finance. It provides a scalable, secure layer‑1 solution optimized for financial markets, enabling institutions, funds, and developers to build fast, reliable on‑chain applications. The network emphasizes speed, reliability, and scalability for modern digital asset markets, supporting stablecoins, payments, and DeFi use cases.
image: https://www.sei.io/opengraph-image.jpg?opengraph-image.17v0n-mv.owi8.jpg?dpl=dpl_6xFxckgTSd6RGPLsgLfmr7f48qKn
json_schemas:
- name: GetWeatherResponse
  property_count: 2
  slug: seinetwork-io-get-weather-response
- name: PostRequest
  property_count: 4
  slug: seinetwork-io-post-request
- name: PostV1WalletsRequest
  property_count: 2
  slug: seinetwork-io-post-v1-wallets-request
- name: PostV1WalletsResponse
  property_count: 4
  slug: seinetwork-io-post-v1-wallets-response
- name: PostV1WalletsWalletAbc123RpcRequest
  property_count: 3
  slug: seinetwork-io-post-v1-wallets-wallet-abc123-rpc-request
- name: PostV1WalletsWalletAbc123RpcResponse
  property_count: 1
  slug: seinetwork-io-post-v1-wallets-wallet-abc123-rpc-response
jsonld:
- class_count: 6
  name: Seinetwork Io Context
  property_count: 11
  slug: seinetwork-io-context
layout: provider
modified: '2026-10-25'
name: Sei
nav: Providers
network: true
overview: 'Sei is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Blockchain, Infrastructure, Finance, and DeFi.


  The Sei catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Sei''s developer surface includes CLI, changelog, getting-started guide, documentation, engineering blog, and 16 more developer resources.'
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: Sei API Rules
  rule_count: 36
  severity_counts:
    error: 33
    hint: 0
    info: 2
    warn: 1
  slug: seinetwork-io-rules
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 21
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.1
  facets:
    access_clarity: 5.3
    contract_governance: 22.0
    contract_quality: 22.8
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 18.4
  previous_composite: 26.5
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/seinetwork-io/seinetwork-io-2026-11-03T142957.png
security:
- kind: domain-security
  name: Seinetwork Io Domain Security
  slug: seinetwork-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seinetwork-io
tags:
- Company
- Blockchain
- Infrastructure
- Finance
- DeFi
website: https://seinetwork.io
---

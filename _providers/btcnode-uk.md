---
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.8
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Bitcoin node data API with pricing and usage details.
  name: BTC Node API
  slug: btc-node-api
- baseURL: https://btcnode.uk
  baseurl_source: declared
  description: Bitcoin data from a real synced full node. No API keys. No signup. Pay per call in USDC.
  name: BTC Node API — Bitcoin node data over x402 API
  slug: btc-node-api-bitcoin-node-data-over-x402-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/btcnode-uk/rules/btcnode-uk-rules.yml
  title: ''
  type: Spectral
  url: rules/btcnode-uk-rules.yml
- group: design
  href: https://artifacts.apis.io/btcnode-uk/vocabulary/btcnode-uk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/btcnode-uk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/btcnode-uk/errors/btcnode-uk-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/btcnode-uk-problem-types.yml
- group: design
  href: https://artifacts.apis.io/btcnode-uk/conformance/btcnode-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/btcnode-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/btcnode-uk/llms/btcnode-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/btcnode-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/btcnode-uk/well-known/btcnode-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/btcnode-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/btcnode-uk/hosts/btcnode-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/btcnode-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/btcnode-uk/vendors/btcnode-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/btcnode-uk-vendors.yml
- group: auth
  href: https://artifacts.apis.io/btcnode-uk/security/btcnode-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/btcnode-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://btcnode.uk/
- group: docs
  title: ''
  type: APIReference
  url: https://btcnode.uk/openapi.json
- group: other
  title: ''
  type: Catalog
  url: https://btcnode.uk/api/catalog
- group: other
  title: ''
  type: Health
  url: https://btcnode.uk/health
created: '2026-10-30'
description: btcnode-uk provides Bitcoin node hosting services in the United Kingdom, offering reliable, secure, and scalable full-node infrastructure for developers, enterprises, and enthusiasts. Their platform enables easy deployment and management of Bitcoin Core nodes, with APIs for blockchain data access, transaction broadcasting, and network monitoring. The service emphasizes high availability, low latency, and compliance with UK data regulations, supporting both mainnet and testnet environments. Customers benefit from automated backups, real-time alerts, and detailed analytics, making btcnode-uk a comprehensive solution for integrating Bitcoin blockchain capabilities into applications and services.
layout: provider
modified: '2026-10-30'
name: btcnode-uk
nav: Providers
network: true
overview: 'btcnode-uk publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including BTC Node API — Bitcoin node data over x402 API, and 1 more. Tagged areas include Company, Bitcoin, NodeHosting, Blockchain, and UK.


  The btcnode-uk catalog on APIs.io includes 1 Spectral governance ruleset.


  btcnode-uk''s developer surface includes API reference and 12 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: btcnode-uk API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: btcnode-uk-rules
score:
  band: emerging
  composite: 22.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 55.7
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 79.1
    contract_quality: 24.0
    developer_ergonomics: 7.1
    discoverability: 62.5
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Btcnode Uk Domain Security
  slug: btcnode-uk-domain-security
  summary_line: TLSv1.3 · HSTS
slug: btcnode-uk
tags:
- Company
- Bitcoin
- NodeHosting
- Blockchain
- UK
website: https://btcnode.uk/
---

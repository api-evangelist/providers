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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.7
  scored_at: '2026-11-06'
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
overview: 'btcnode-uk publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including BTC Node API — Bitcoin node data over x402 API, and 1 more. Tagged areas include Company, Bitcoin, Node Hosting, Blockchain, and United Kingdom.


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
  composite: 15.0
  coverage:
    artifact_dirs: 14
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 24.0
    developer_ergonomics: 3.6
    discoverability: 62.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  previous_composite: 15.7
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/btcnode-uk/btcnode-uk-2026-11-03T122711.png
security:
- kind: domain-security
  name: Btcnode Uk Domain Security
  slug: btcnode-uk-domain-security
  summary_line: TLSv1.3 · HSTS
slug: btcnode-uk
tags:
- Company
- Bitcoin
- Node Hosting
- Blockchain
- United Kingdom
website: https://btcnode.uk/
---

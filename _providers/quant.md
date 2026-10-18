---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 34.4
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 25
  human_in_the_loop: 3
  name: Quant Agentic Access
  operation_count: 70
  slug: quant-agentic-access
  summary_line: 70 operations · 25 acting · 3 human-in-the-loop
api_count: 2
apis:
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Self-service management of Overledger-issued API keys
  name: Quant Network API Keys API
  slug: quant-api-keys-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Deployed smart contract registry and permissions
  name: Quant Network Contracts API
  slug: quant-contracts-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Token deposit management
  name: Quant Network Deposits API
  slug: quant-deposits-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Read-only state queries against Flow Apps
  name: Quant Network Flow Query API
  slug: quant-flow-query-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Available Flow App definitions
  name: Quant Network Flow Registry API
  slug: quant-flow-registry-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Multi-step Flow App session management
  name: Quant Network Flow Sessions API
  slug: quant-flow-sessions-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Outbound webhook subscriptions and event replay
  name: Quant Network Flow Webhooks API
  slug: quant-flow-webhooks-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Liveness and readiness probes
  name: Quant Network Health API
  slug: quant-health-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Network discovery
  name: Quant Network Networks API
  slug: quant-networks-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: DLT node management
  name: Quant Network Nodes API
  slug: quant-nodes-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Prometheus metrics
  name: Quant Network Observability API
  slug: quant-observability-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: JSON-RPC proxy to the Fusion L2 (OP-Geth) **only**. For JSON-RPC against any other connected chain, use the Fusion Proxy's multi-DLT endpoint `/dlts/{dlt}/networks/{networkId}/rpc/{apiKey}` (see the f
  name: Quant Network RPC API
  slug: quant-rpc-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Staking operations
  name: Quant Network Stakes API
  slug: quant-stakes-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Token swap quotes and execution
  name: Quant Network Swaps API
  slug: quant-swaps-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Subscribe to events emitted from / to an address
  name: Quant Network Tracker Address API
  slug: quant-tracker-address-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Subscribe to a specific contract event signature
  name: Quant Network Tracker Event API
  slug: quant-tracker-event-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Track a transaction's confirmation status with callback notifications
  name: Quant Network Tracker Transaction API
  slug: quant-tracker-transaction-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: Authenticated user profile and resource data
  name: Quant Network User API
  slug: quant-user-api
- baseURL: https://fusion-rollup.quant.dev
  baseurl_source: spec
  description: L2-to-L1 withdrawal lifecycle (initiate, prove, finalize)
  name: Quant Network Withdrawals API
  slug: quant-withdrawals-api
artifact_total: 33
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/agentic-access/quant-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/quant-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/rules/quant-rules.yml
  title: ''
  type: Spectral
  url: rules/quant-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/json-ld/quant-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/quant-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/vocabulary/quant-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/quant-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/data-model/quant-data-model.yml
  title: ''
  type: DataModel
  url: data-model/quant-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/conventions/quant-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/quant-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/conventions/quant-conventions.yml
  title: ''
  type: Conventions
  url: conventions/quant-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/errors/quant-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/quant-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/conformance/quant-conformance.yml
  title: ''
  type: Conformance
  url: conformance/quant-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/well-known/quant-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/quant-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/hosts/quant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/quant-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/vendors/quant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/quant-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://quant.network/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://quant.network/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://quant.network/news/?filter=all
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/authentication/quant-authentication.yml
  title: ''
  type: Authentication
  url: authentication/quant-authentication.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/plans/quant-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/quant-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/rate-limits/quant-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/quant-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/finops/quant-finops.yml
  title: ''
  type: FinOps
  url: finops/quant-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/security/quant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/quant-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/quantnetwork
- group: company
  title: ''
  type: Website
  url: https://www.quant.network/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.overledger.dev/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/quantnetwork
- group: company
  title: ''
  type: Blog
  url: https://quant.network/feed/
created: '2025-02-12'
description: Quant Network is a blockchain interoperability company whose Overledger platform provides APIs to issue, connect, and monitor digital assets, smart contracts, transactions, and accounts across multiple distributed ledger technologies without requiring blockchain expertise.
finops:
- has_sources: false
  method: generated
  name: Quant Finops
  primary_unit: ''
  service_category: API
  slug: quant-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/quant.png
json_schemas:
- name: FlowAppDetail
  property_count: 10
  slug: quant-flow-app-detail
- name: MintedApiKey
  property_count: 7
  slug: quant-minted-api-key
- name: Network
  property_count: 12
  slug: quant-network
- name: StepSpec
  property_count: 9
  slug: quant-step-spec
- name: Swap
  property_count: 17
  slug: quant-swap
- name: WithdrawalRecord
  property_count: 25
  slug: quant-withdrawal-record
jsonld:
- class_count: 71
  name: Quant Context
  property_count: 171
  slug: quant-context
layout: provider
modified: '2026-04-28'
name: Quant Network
nav: Providers
network: true
overview: 'Quant Network publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, Contracts API, Deposits API, and 16 more. Tagged areas include Blockchain, Distributed Ledger, Interoperability, Overledger, and Smart Contracts.


  The Quant Network catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Quant Network''s developer surface includes authentication, engineering blog, and 23 more developer resources.'
plans:
- name: Quant Plans Pricing
  plan_count: 3
  slug: quant-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Quant Rate Limits
  slug: quant-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Quant Network API Rules
  rule_count: 14
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 4
  slug: quant-rules
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 23
    catalog_earned: 63.8
    catalog_earned_first_party: 0.0
    catalog_gap: 51.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 21.1
  facets:
    access_clarity: 28.9
    contract_governance: 22.0
    contract_quality: 57.4
    developer_ergonomics: 38.1
    discoverability: 58.9
    operational_transparency: 18.4
  previous_composite: 18.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 19
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/quant/refs/heads/main/screenshots/quant-2026-06-20T192412.png
security:
- kind: authentication
  name: Quant Authentication
  slug: quant-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Quant Domain Security
  slug: quant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: quant
tags:
- Blockchain
- Distributed Ledger
- Interoperability
- Overledger
- Smart Contracts
- Digital Assets
- Web3
website: https://www.quant.network/
---

---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: true
  try_now: true
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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Dfns Agentic Access
  operation_count: 49
  slug: dfns-agentic-access
  summary_line: 49 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Login, User Action Signing, users, and credentials.
  name: Dfns Auth API
  slug: dfns-auth-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Standalone MPC keys and delegated signing.
  name: Dfns Keys API
  slug: dfns-keys-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Network fee estimates and read-only blockchain calls.
  name: Dfns Networks API
  slug: dfns-networks-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Permissions and their assignments to identities.
  name: Dfns Permissions API
  slug: dfns-permissions-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Policy engine rules and approval decisions.
  name: Dfns Policies API
  slug: dfns-policies-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Programmable non-custodial wallets, balances, NFTs, and history.
  name: Dfns Wallets API
  slug: dfns-wallets-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: Event webhooks and delivery logs.
  name: Dfns Webhooks API
  slug: dfns-webhooks-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Address Watches API from Dfns — 5 operation(s) for address watches.
  name: Dfns Address Watches API
  slug: dfns-address-watches-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Agreements API from Dfns — 2 operation(s) for agreements.
  name: Dfns Agreements API
  slug: dfns-agreements-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Allocations API from Dfns — 6 operation(s) for allocations.
  name: Dfns Allocations API
  slug: dfns-allocations-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Exchanges API from Dfns — 7 operation(s) for exchanges.
  name: Dfns Exchanges API
  slug: dfns-exchanges-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Fee Sponsors API from Dfns — 5 operation(s) for fee sponsors.
  name: Dfns Fee Sponsors API
  slug: dfns-fee-sponsors-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Payins API from Dfns — 8 operation(s) for payins.
  name: Dfns Payins API
  slug: dfns-payins-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Payouts API from Dfns — 4 operation(s) for payouts.
  name: Dfns Payouts API
  slug: dfns-payouts-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Signers API from Dfns — 17 operation(s) for signers.
  name: Dfns Signers API
  slug: dfns-signers-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Staking API from Dfns — 4 operation(s) for staking.
  name: Dfns Staking API
  slug: dfns-staking-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Swaps API from Dfns — 4 operation(s) for swaps.
  name: Dfns Swaps API
  slug: dfns-swaps-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Tenant API from Dfns — 12 operation(s) for tenant.
  name: Dfns Tenant API
  slug: dfns-tenant-api
- baseURL: https://api.dfns.io
  baseurl_source: declared
  description: The Vaults API from Dfns — 16 operation(s) for vaults.
  name: Dfns Vaults API
  slug: dfns-vaults-api
artifact_total: 39
collections:
- collection_type: open
  name: Dfns Approvals API
  slug: open-dfns-approvals-api
- collection_type: open
  name: Dfns Approvals Auth API
  slug: open-dfns-auth-api
- collection_type: open
  name: Dfns Approvals Keys API
  slug: open-dfns-keys-api
- collection_type: open
  name: Dfns Approvals Networks API
  slug: open-dfns-networks-api
- collection_type: open
  name: Dfns Approvals Permissions API
  slug: open-dfns-permissions-api
- collection_type: open
  name: Dfns Approvals Policies API
  slug: open-dfns-policies-api
- collection_type: open
  name: Dfns Approvals ServiceAccounts API
  slug: open-dfns-serviceaccounts-api
- collection_type: open
  name: Dfns Approvals Signatures API
  slug: open-dfns-signatures-api
- collection_type: open
  name: Dfns Approvals Transactions API
  slug: open-dfns-transactions-api
- collection_type: open
  name: Dfns Approvals Transfers API
  slug: open-dfns-transfers-api
- collection_type: open
  name: Dfns Approvals Wallets API
  slug: open-dfns-wallets-api
- collection_type: open
  name: Dfns Approvals Webhooks API
  slug: open-dfns-webhooks-api
- collection_type: open
  name: Dfns API
  slug: open-dfns
common:
- group: company
  title: ''
  type: Blog
  url: https://dfns.co/blog
- group: company
  title: ''
  type: BlogRSS
  url: https://dfns.co/rss.xml
- group: other
  href: https://artifacts.apis.io/dfns/capabilities/dfns-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/dfns-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/dfns/agentic-access/dfns-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dfns-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/dfns/security/dfns-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dfns-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/dfns/authentication/dfns-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dfns-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/dfns
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dfns
- group: company
  title: ''
  type: Website
  url: https://www.dfns.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.dfns.co/
- group: commercial
  href: https://artifacts.apis.io/dfns/plans/dfns-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dfns-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/dfns/rate-limits/dfns-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/dfns-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/dfns/finops/dfns-finops.yml
  title: ''
  type: FinOps
  url: finops/dfns-finops.yml
created: '2026-07-01'
description: Dfns is a wallet-as-a-service and MPC key-management infrastructure provider. Its API lets businesses create programmable, non-custodial wallets backed by multi-party-computation key shares, sign and broadcast transactions across many blockchains, and govern every action through a programmable policy engine with delegated signing, approvals, and User Action Signing.
finops:
- has_sources: true
  method: generated
  name: Dfns Finops
  primary_unit: ''
  service_category: Blockchain and Digital Asset Infrastructure
  slug: dfns-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dfns.png
layout: provider
modified: '2026-10-06'
name: Dfns
nav: Providers
network: true
overview: 'Dfns publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Keys API, Networks API, and 16 more. Tagged areas include Wallets, MPC, Key Management, Digital Assets, and Web3.


  The Dfns catalog on APIs.io includes 1 Spectral governance ruleset.


  Dfns'' developer surface includes engineering blog, authentication, documentation, and 10 more developer resources.'
plans:
- name: Dfns Plans Pricing
  plan_count: 3
  slug: dfns-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 4
  name: Dfns Rate Limits
  slug: dfns-rate-limits
rules:
- authorship: generated
  effective_rule_count: 96
  extends:
  - spectral:oas
  name: Dfns API Rules
  rule_count: 55
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 9
  slug: dfns-rules
score:
  band: thin
  composite: 31.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 47.5
    catalog_earned_first_party: 0.0
    catalog_gap: 67.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.8
  facets:
    access_clarity: 7.9
    contract_governance: 13.6
    contract_quality: 53.5
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 10.5
  previous_composite: 30.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 59.4
      total: 32
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 27.8
screenshot: https://apis.io/screenshots/dfns/dfns-2026-07-25T212051.png
security:
- kind: authentication
  name: Dfns Authentication
  slug: dfns-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Dfns Domain Security
  slug: dfns-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dfns
tags:
- Wallets
- MPC
- Key Management
- Digital Assets
- Web3
- Non-Custodial
website: https://www.dfns.co/
---

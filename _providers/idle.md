---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Idle Agentic Access
  operation_count: 3
  slug: idle-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Idle Finance REST API endpoint for Polygon zkEVM network, providing pool and TVL data for Yield Tranches vaults deployed on Polygon zkEVM.
  name: Idle Finance Polygon zkEVM API
  slug: idle-finance-polygon-zkevm-api
- description: Idle Finance REST API endpoint for the Optimism network, providing pool and TVL data for Yield Tranches vaults deployed on Optimism.
  name: Idle Finance Optimism API
  slug: idle-finance-optimism-api
- description: Best Yield and Yield Tranches vault pool data
  name: Idle Finance Pools API
  slug: idle-pools-api
- description: Historical daily yield rate data for Best Yield vaults
  name: Idle Finance Rates API
  slug: idle-rates-api
- description: Total value locked metrics per underlying token
  name: Idle Finance TVL API
  slug: idle-tvl-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Idle Finance Pools API
  slug: open-idle-pools-api
- collection_type: open
  name: Idle Finance Pools Rates API
  slug: open-idle-rates-api
- collection_type: open
  name: Idle Finance Pools TVL API
  slug: open-idle-tvl-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/idle-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/idle-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/idle-authentication.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.idle.finance/developers/introduction
- group: auth
  title: ''
  type: Authentication
  url: https://idlefinance.typeform.com/to/CzRkDH
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Idle-Finance
- group: other
  title: ''
  type: Governance
  url: https://gov.idle.finance
- group: other
  title: ''
  type: Governance Tally
  url: https://tally.xyz/gov/idle
- group: auth
  title: ''
  type: Bug Bounty
  url: https://immunefi.com/bounty/idlefinance/
- group: operate
  title: ''
  type: Status
  url: https://status.idle.finance
- group: operate
  title: ''
  type: Discord
  url: https://discord.gg/mpySAJp
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/idlefinance
- group: company
  title: ''
  type: Blog
  url: https://medium.com/idle-finance
- group: company
  title: ''
  type: Website
  url: https://idle.finance
- group: commercial
  title: ''
  type: TermsOfService
  url: https://idle.finance/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://idle.finance/privacy
created: '2026-06-14'
description: Idle Finance is a decentralized yield automation protocol that has operated since 2019, enabling users and integrators to optimize yield generation across DeFi. The platform offers REST APIs for querying Best Yield and Yield Tranches pools, APY and TVL metrics, historical rates, and governance staking information. Idle aggregates yield sources across protocols such as Compound, Aave, Morpho, and Clearpool, and supports multiple chains including Ethereum, Polygon, Polygon zkEVM, and Optimism.
examples:
- key_count: 4
  name: Get Pools
  slug: get-pools
- key_count: 4
  name: Get Rates By Address
  slug: get-rates-by-address
- key_count: 4
  name: Get Tvls
  slug: get-tvls
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/idle.png
json_schemas:
- name: Pool
  property_count: 8
  slug: pool
- name: RateRecord
  property_count: 4
  slug: rate-record
- name: UnderlyingAllocation
  property_count: 3
  slug: underlying-allocation
jsonld:
- class_count: 0
  name: Idle Finance Context
  property_count: 0
  slug: idle-finance
layout: provider
modified: '2026-06-14'
name: Idle Finance
nav: Providers
network: true
overview: 'Idle Finance publishes 3 APIs on the [APIs.io](https://apis.io/) network: Pools API, Rates API, and TVL API. Tagged areas include DeFi, Yield Optimization, Finance, Crypto, and Staking.


  The Idle Finance catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Idle Finance''s developer surface includes authentication, documentation, status page, engineering blog, and 12 more developer resources.'
plans:
- name: Plans
  plan_count: 3
  slug: plans
random_paper: 15
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Idle Finance API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: idle-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.2
  coverage:
    artifact_dirs: 15
    catalog_gap: 54.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 9.8
    contract_quality: 62.4
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 9.8
    operational_transparency: 2.6
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/idle/refs/heads/main/screenshots/idle-2026-06-20T183210.png
security:
- kind: authentication
  name: Idle Authentication
  slug: idle-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Idle Domain Security
  slug: idle-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: idle
tags:
- DeFi
- Yield Optimization
- Finance
- Crypto
- Staking
- Governance
- TVL
- APY
website: https://idle.finance
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.7
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Metalend Agentic Access
  operation_count: 17
  slug: metalend-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 1
apis:
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Machine-readable flow guide for AI agents — signing formats, wizard flows, and integration gotchas
  name: MetaLend AI Agent Guide API
  slug: metalend-ai-agent-guide-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Get challenge / verify challenge authentication
  name: MetaLend Auth API
  slug: metalend-auth-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Balance queries across pools and protocols
  name: MetaLend Balances API
  slug: metalend-balances-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Deposit operations for rebalancing
  name: MetaLend Deposits API
  slug: metalend-deposits-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Protocol and pool information
  name: MetaLend Pools API
  slug: metalend-pools-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Reward aggregation and claim data
  name: MetaLend Rewards API
  slug: metalend-rewards-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: The Services API from MetaLend — 1 operation(s) for services.
  name: MetaLend Services API
  slug: metalend-services-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Transaction cost queries
  name: MetaLend Transaction Costs API
  slug: metalend-transaction-costs-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: User rebalancer configuration management
  name: MetaLend User Configuration API
  slug: metalend-user-configuration-api
- baseURL: https://api.metalend.tech
  baseurl_source: declared
  description: Withdrawal operations from pools
  name: MetaLend Withdrawals API
  slug: metalend-withdrawals-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide API
  slug: open-metalend-ai-agent-guide-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Auth API
  slug: open-metalend-auth-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Balances API
  slug: open-metalend-balances-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Deposits API
  slug: open-metalend-deposits-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Pools API
  slug: open-metalend-pools-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Rewards API
  slug: open-metalend-rewards-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Services API
  slug: open-metalend-services-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Transaction Costs API
  slug: open-metalend-transaction-costs-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide User Configuration API
  slug: open-metalend-user-configuration-api
- collection_type: open
  name: MetaLend Rebalancing AI Agent Guide Withdrawals API
  slug: open-metalend-withdrawals-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/metalend-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/metalend-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metalend-domain-security.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: X-MCPServerCandidate
  url: mcp/metalend-mcp.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/metalend-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/metalend-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/metalend-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/metalend-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://metalend-inc.gitbook.io/litepaper/security-audits-with-sherlock
- group: design
  title: ''
  type: DataModel
  url: data-model/metalend-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/metalend-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/metalend-rebalancing-overlay.yaml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/metalend-llms.txt
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.metalend.tech
- group: docs
  title: ''
  type: Documentation
  url: https://metalend-inc.gitbook.io/litepaper
- group: docs
  title: ''
  type: APIReference
  url: https://api.metalend.tech/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://api.metalend.tech/SKILL.md
- group: commercial
  title: ''
  type: Pricing
  url: https://metalend-inc.gitbook.io/litepaper/metalend-litepaper/apy-and-fees
- group: operate
  title: ''
  type: Roadmap
  url: https://metalend-inc.gitbook.io/litepaper/metalend-litepaper/roadmap
- group: operate
  title: ''
  type: Support
  url: https://metalend-inc.gitbook.io/litepaper/metalend-litepaper/support
- group: company
  title: ''
  type: Blog
  url: https://medium.com/metalend
- group: start
  title: ''
  type: SignUp
  url: https://developer.metalend.tech
- group: commercial
  title: ''
  type: TermsOfService
  url: https://metalend-inc.gitbook.io/litepaper/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://metalend-inc.gitbook.io/litepaper/privacy-policy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/MetaLend_DeFi
- group: company
  title: ''
  type: Website
  url: https://metalend.tech/
created: '2026-07-17'
description: 'MetaLend is a DeFi "earn and spend" platform that aggregates lending pools across protocols (Aave, Morpho, Euler) and chains (Base, Ethereum, Polygon, Arbitrum, Linea) behind a single cross-chain Rebalancing API. It continuously repositions user-approved, self-custodied capital into the best-yielding pools while keeping funds instantly spendable via a debit card. The API is notably agent-native: it serves an AI agent flow guide at GET /SKILL.md, ships SIWE challenge/verify JWT auth with EIP-191/EIP-712/EIP-3009 wallet signing, and gates its services directory behind an x402 (HTTP 402) micropayment in USDC on Base. Smart contracts are audited by Sherlock. Backed by Pantera Capital.'
image: https://d26nkljutfj8pz.cloudfront.net/images/metalend-share.png
layout: provider
modified: '2026-07-20'
name: MetaLend
nav: Providers
network: true
overview: 'MetaLend publishes 10 APIs on the [APIs.io](https://apis.io/) network, including AI Agent Guide API, Auth API, Balances API, and 7 more. Tagged areas include Company, Crypto, DeFi, Lending, and Yield.


  MetaLend''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, pricing, support, and 20 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 52.1
  coverage:
    artifact_dirs: 18
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    commercial_clarity: 52.6
    contract_governance: 18.2
    contract_quality: 58.9
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 5.3
  previous_composite: 52.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 46.9
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/metalend/refs/heads/main/screenshots/metalend-2026-08-07T172645.png
security:
- kind: authentication
  name: Metalend Authentication
  slug: metalend-authentication
  summary_line: apiKey · 3 schemes
- kind: domain-security
  name: Metalend Domain Security
  slug: metalend-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: metalend
tags:
- Company
- Crypto
- DeFi
- Lending
- Yield
- Rebalancing
- Web3
- Stablecoins
- Payments
- agent-native
- Blockchain
website: https://metalend.tech/
---

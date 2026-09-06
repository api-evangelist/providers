---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Debank Agentic Access
  operation_count: 42
  slug: debank-agentic-access
  summary_line: 42 operations · 4 acting
api_count: 2
apis:
- description: OAuth 2.0 authorization-code sign-in for dApps. After a user authorizes, the dApp exchanges the code at api.connect.debank.com/oauth/token using HTTP Basic client credentials and reads the user's base
  name: DeBank Connect
  slug: debank-connect
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: The Account API from DeBank — 1 operation(s) for account.
  name: DeBank Account API
  slug: debank-account-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: Get app info
  name: DeBank App Protocol API
  slug: debank-app-protocol-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: Get chain info
  name: DeBank Chain API
  slug: debank-chain-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: The cloud API from DeBank — 5 operation(s) for cloud.
  name: DeBank Cloud API
  slug: debank-cloud-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: The official API from DeBank — 2 operation(s) for official.
  name: DeBank Official API
  slug: debank-official-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: Get pool info
  name: DeBank Pool API
  slug: debank-pool-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: Get protocol info
  name: DeBank Protocol API
  slug: debank-protocol-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: Get token info
  name: DeBank Token API
  slug: debank-token-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: Get user info such as total balance, token list, and portfolio in each protocol
  name: DeBank User API
  slug: debank-user-api
- baseURL: https://pro-openapi.debank.com
  baseurl_source: declared
  description: It is not stable at present. If you want to use it, please contact the official first.
  name: DeBank Wallet API
  slug: debank-wallet-api
artifact_total: 18
collections:
- collection_type: open
  name: DeBank OpenAPI
  slug: open-debank-pro
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/debank-pro-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/debank-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/debank-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/debank-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://debank.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://cloud.debank.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.cloud.debank.com/en
- group: docs
  title: ''
  type: APIReference
  url: https://docs.cloud.debank.com/en/readme/api-pro-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.cloud.debank.com/en/readme/open-api
- group: start
  title: ''
  type: SignUp
  url: https://cloud.debank.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.cloud.debank.com/en/terms-of-service
- group: operate
  title: ''
  type: Support
  url: mailto:hello.cloud@debank.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/DeBankDeFi
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.cloud.debank.com/en/readme/changelog
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/debank-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/debank-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/debank-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/debank-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/debank-changelog.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/debank-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/debank-rate-limits.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/debank-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/debank-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/debank-problem-types.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-08-12'
description: DeBank is a Web3 portfolio tracker and DeFi data platform operated by DeBank Global Pte. Ltd. (Singapore) that indexes wallet balances, protocol positions, NFTs, token prices and transaction history across a large set of EVM and non-EVM chains. Its developer arm, DeBank Cloud, exposes that data core as the DeBank OpenAPI (a Swagger 2.0 contract at pro-openapi.debank.com covering chain, protocol, pool, token, user-portfolio and wallet transaction-simulation endpoints), as DeBank Connect (an OAuth 2.0 authorization-code sign-in that lets a dApp read an authorizing user's base, on-chain and social data), and as an Official Account messaging API for reaching on-chain users through DeBank Hi. Access is metered in prepaid "units" bought from the DeBank Cloud dashboard, keyed by an AccessKey header, with a 14-day free trial and a documented 100 requests/second ceiling on the Pro plan.
image: https://static-assets.debank.com/files/e8aeedfa-2679-429e-ad80-b469f5ca96c2.png
layout: provider
modified: '2026-08-12'
name: DeBank
nav: Providers
network: true
overview: 'DeBank publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, App Protocol API, Chain API, and 7 more. Tagged areas include Web3, DeFi, Blockchain, Crypto, and Portfolio Tracking.


  DeBank''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, changelog, and 18 more developer resources.'
plans:
- name: Debank Plans Pricing
  plan_count: 0
  slug: debank-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Debank Rate Limits
  slug: debank-rate-limits
scopes:
- name: Debank Scopes
  scope_count: 3
  slug: debank-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: thin
  composite: 37.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 45.0
    catalog_earned_first_party: 8.0
    catalog_gap: 70.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 4.5
    contract_quality: 39.3
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 39.5
  previous_composite: 37.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 10
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/debank/refs/heads/main/screenshots/debank-2026-08-17T080851.png
security:
- kind: authentication
  name: Debank Authentication
  slug: debank-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Debank Domain Security
  slug: debank-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: debank
tags:
- Web3
- DeFi
- Blockchain
- Crypto
- Portfolio Tracking
- On-Chain Data
- Wallets
- token-data
- NFT
- Ethereum
- Authentication
- Market Data
website: https://debank.com/
---

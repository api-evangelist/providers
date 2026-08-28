---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 2
apis:
- description: Public Antelope/EOSIO Chain API for the WAX blockchain — query chain state (get_info, get_account, get_table_rows, get_currency_balance) and submit signed transactions (push_transaction/send_transacti
  name: WAX Chain API (Antelope RPC)
  slug: wax-chain-api-antelope-rpc
- description: Hyperion full-history API for the WAX chain — query historical actions, transactions, and state deltas at /v1/history/* and /v2/*.
  name: WAX Hyperion History API
  slug: wax-hyperion-history-api
artifact_total: 4
common:
- group: company
  title: ''
  type: Website
  url: https://wax.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.wax.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.wax.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.wax.io/build/dapp-development/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.wax.io/learn/about-wax/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/worldwide-asset-exchange
- group: company
  title: ''
  type: Blog
  url: https://medium.com/wax-io
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wax.io
- group: start
  title: ''
  type: SignUp
  url: https://all-access.wax.io
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wax.io/wcw-tos/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wax.io/privacy-policy/
- group: build
  title: ''
  type: Packages
  url: packages/wax-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/wax-packages.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wax-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/wax-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/wax-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/wax-lifecycle.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wax-domain-security.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/wax-llms.txt
created: '2026-07-17'
description: WAX (Worldwide Asset eXchange) is a purpose-built, carbon-neutral layer-1 blockchain and protocol token for NFTs, blockchain gaming, and e-commerce, built as an Antelope (EOSIO fork) chain. Developers build dApps against the public Antelope Chain API (/v1/chain/*) and the Hyperion History API, and integrate the WAX Cloud Wallet through the official @waxio JavaScript SDKs (waxjs, sdk-react-native). Read RPC endpoints are unauthenticated; state changes are authorized by client-side secp256k1 transaction signatures rather than API keys or OAuth. WAX also operates microservices such as WAX Cloud Wallet, the WAX RNG oracle, and vIRL. Backed by Pantera Capital.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wax.png
layout: provider
modified: '2026-07-21'
name: WAX
nav: Providers
network: true
overview: 'WAX publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Blockchain, NFT, and Web3.


  WAX''s developer surface includes documentation, API reference, getting-started guide, engineering blog, signup flow, authentication, and 13 more developer resources.'
random_paper: 0
score:
  band: thin
  composite: 26.9
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 59.5
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 18.4
  previous_composite: 26.9
  provenance:
    conformance: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
security:
- kind: authentication
  name: Wax Authentication
  slug: wax-authentication
  summary_line: none/signature · 3 schemes
- kind: domain-security
  name: Wax Domain Security
  slug: wax-domain-security
  summary_line: TLSv1.3 · DMARC
slug: wax
tags:
- Company
- Crypto
- Blockchain
- NFT
- Web3
- Gaming
- Antelope
- Wallets
website: https://wax.io/
---

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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The Assets API from Mesh — 2 operation(s) for assets.
  name: Mesh Assets API
  slug: mesh-assets-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Bi'
  name: Mesh Balance API
  slug: mesh-balance-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The BrokerAccountDetail API from Mesh — 1 operation(s) for brokeraccountdetail.
  name: Mesh BrokerAccountDetail API
  slug: mesh-brokeraccountdetail-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The recommended approach for account authentication. Front manages multiple authentication flows and handles all authentication steps such as MFA codes and OAuth redirect through our web and mobile SD
  name: Mesh Managed Account Authentication API
  slug: mesh-managed-account-authentication-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The Managed Transfers API from Mesh — 10 operation(s) for managed transfers.
  name: Mesh Managed Transfers API
  slug: mesh-managed-transfers-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Op'
  name: Mesh Portfolio API
  slug: mesh-portfolio-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: Not recommended approach. Using this approach, the API client is responsible for handling multiple authentication flows and supporting future updates and changes.
  name: Mesh Self Managed Account Authentication API
  slug: mesh-self-managed-account-authentication-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: '### Supported integrations: ```Robinhood``` ```ETrade``` ```Alpaca``` ```WeBull``` ```Stash``` ```InteractiveBrokers``` ```Public``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Bi'
  name: Mesh Transactions API
  slug: mesh-transactions-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: '### Supported integrations: ```Robinhood``` ```Coinbase``` ```Kraken``` ```CoinbasePro``` ```CryptoCom``` ```Binance``` ```Gemini``` ```OkCoin``` ```KuCoin``` ```BinanceInternational``` ```Bitstamp```'
  name: Mesh Transfers API
  slug: mesh-transfers-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The BlockchainQuery API from Mesh — 4 operation(s) for blockchainquery.
  name: Mesh Blockchain Query API
  slug: mesh-blockchainquery-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The CatalogGasSponsorship API from Mesh — 3 operation(s) for cataloggassponsorship.
  name: Mesh Catalog Gas Sponsorship API
  slug: mesh-cataloggassponsorship-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The CatalogSubscription API from Mesh — 5 operation(s) for catalogsubscription.
  name: Mesh Catalog Subscription API
  slug: mesh-catalogsubscription-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: Mesh's cross-chain bridging engine as a pure API, with no Mesh-hosted UI or SDK. Discover bridged routes, quote a pay-in amount and generate a single-use deposit address that bridges funds to the dest
  name: Mesh Headless Bridging API
  slug: mesh-headless-bridging-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The Integrations account information API from Mesh — 1 operation(s) for integrations account information.
  name: Mesh Integrations account information API
  slug: mesh-integrations-account-information-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The RampKyc API from Mesh — 1 operation(s) for rampkyc.
  name: Mesh Ramp Kyc API
  slug: mesh-rampkyc-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The RampPayment API from Mesh — 3 operation(s) for ramppayment.
  name: Mesh Ramp Payment API
  slug: mesh-ramppayment-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The RampSession API from Mesh — 2 operation(s) for rampsession.
  name: Mesh Ramp Session API
  slug: mesh-rampsession-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The TokenNetworkPairs API from Mesh — 1 operation(s) for tokennetworkpairs.
  name: Mesh Token Network Pairs API
  slug: mesh-tokennetworkpairs-api
- baseURL: https://integration-api.meshconnect.com
  baseurl_source: declared
  description: The Wallets API from Mesh — 2 operation(s) for wallets.
  name: Mesh Wallets API
  slug: mesh-wallets-api
artifact_total: 36
asyncapis:
- description: ''
  name: Mesh Transfers Webhooks
  slug: mesh-transfers-webhooks
collections:
- collection_type: open
  name: Mesh Connect Integration Assets API
  slug: open-mesh-assets-api
- collection_type: open
  name: Mesh Connect Integration Assets Balance API
  slug: open-mesh-balance-api
- collection_type: open
  name: Mesh Connect Integration Assets BrokerAccountDetail API
  slug: open-mesh-brokeraccountdetail-api
- collection_type: open
  name: Mesh Connect Integration Assets Managed Account Authentication API
  slug: open-mesh-managed-account-authentication-api
- collection_type: open
  name: Mesh Connect Integration Assets Managed Transfers API
  slug: open-mesh-managed-transfers-api
- collection_type: open
  name: Mesh Connect Integration Assets Portfolio API
  slug: open-mesh-portfolio-api
- collection_type: open
  name: Mesh Connect Integration Assets Self Managed Account Authentication API
  slug: open-mesh-self-managed-account-authentication-api
- collection_type: open
  name: Mesh Connect Integration Assets Transactions API
  slug: open-mesh-transactions-api
- collection_type: open
  name: Mesh Connect Integration Assets Transfers API
  slug: open-mesh-transfers-api
common:
- group: company
  title: ''
  type: Website
  url: https://meshconnect.com
- group: other
  href: https://artifacts.apis.io/mesh/capabilities/mesh-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/mesh-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/mesh/overlays/mesh-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/mesh-integration-api-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.meshconnect.com/overview
- group: docs
  title: ''
  type: Documentation
  url: https://docs.meshconnect.com/overview
- group: docs
  title: ''
  type: APIReference
  url: https://docs.meshconnect.com/api-reference/managed-transfers/get-integrations
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.meshconnect.com/build/15min-quickstart
- group: start
  title: ''
  type: Login
  url: https://dashboard.meshconnect.com/login
- group: company
  title: ''
  type: Blog
  url: https://www.meshpay.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FrontFin
- group: operate
  title: ''
  type: StatusPage
  url: https://status.meshconnect.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meshpay.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meshpay.com/privacy-policy
- group: auth
  title: ''
  type: Compliance
  url: https://www.meshpay.com/security
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.meshpay.com/security
- group: auth
  href: https://artifacts.apis.io/mesh/authentication/mesh-authentication.yml
  title: ''
  type: Authentication
  url: authentication/mesh-authentication.yml
- group: design
  href: https://artifacts.apis.io/mesh/conventions/mesh-conventions.yml
  title: ''
  type: Conventions
  url: conventions/mesh-conventions.yml
- group: design
  href: https://artifacts.apis.io/mesh/errors/mesh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/mesh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/mesh/lifecycle/mesh-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/mesh-lifecycle.yml
- group: operate
  href: https://artifacts.apis.io/mesh/changelog/mesh-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/mesh-changelog.yml
- group: design
  href: https://artifacts.apis.io/mesh/conformance/mesh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/mesh-conformance.yml
- group: design
  href: https://artifacts.apis.io/mesh/data-model/mesh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/mesh-data-model.yml
- group: start
  href: https://artifacts.apis.io/mesh/sandbox/mesh-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/mesh-sandbox.yml
- group: design
  href: https://artifacts.apis.io/mesh/asyncapi/mesh-transfers-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/mesh-transfers-webhooks.yml
- group: agent
  href: https://artifacts.apis.io/mesh/mcp/mesh-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/mesh-mcp.yml
- group: build
  href: https://artifacts.apis.io/mesh/packages/mesh-packages.yml
  title: ''
  type: Packages
  url: packages/mesh-packages.yml
- group: build
  href: https://artifacts.apis.io/mesh/packages/mesh-packages.yml
  title: ''
  type: SDKs
  url: packages/mesh-packages.yml
- group: design
  href: https://artifacts.apis.io/mesh/components/mesh-components.yml
  title: ''
  type: Components
  url: components/mesh-components.yml
- group: agent
  href: https://artifacts.apis.io/mesh/llms/mesh-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/mesh-llms.txt
- group: agent
  href: https://artifacts.apis.io/mesh/well-known/mesh-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/mesh-well-known.yml
- group: auth
  href: https://artifacts.apis.io/mesh/security/mesh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/mesh-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/mesh/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mesh is the first global crypto payments network, connecting hundreds of exchanges, wallets, and financial platforms into a single, unified infrastructure layer so businesses can let users pay, get paid, deposit, and transfer digital assets from any wallet on any chain. The Mesh Connect Integration API lets developers programmatically generate Link tokens for Mesh's hosted connection UX, initiate managed crypto transfers (deposit, payment, onramp, withdrawal), read holdings, balances, and transaction history across connected exchange and self-custody accounts, verify wallet ownership, and receive HMAC-signed transfer-status webhooks. Mesh handles credential validation, MFA, OAuth, and per-integration error handling on the developer's behalf. Formerly Front Finance. SOC 2 Type II certified. Backed by Anthemis and General Catalyst.
image: https://cdn.prod.website-files.com/656cc624086b77872a31a084/68d8116f8f0a10f661523cea_Favicon_new.png
layout: provider
modified: '2026-09-16'
name: Mesh
nav: Providers
network: true
overview: 'Mesh publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Balance API, BrokerAccountDetail API, and 16 more. Tagged areas include Company, Cryptocurrency, Payments, Digital Assets, and Financial Services.


  The Mesh catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Mesh''s developer surface includes documentation, API reference, getting-started guide, engineering blog, authentication, changelog, sandbox, and 25 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 93
  extends:
  - spectral:oas
  name: Mesh API Rules
  rule_count: 52
  severity_counts:
    error: 44
    hint: 0
    info: 2
    warn: 6
  slug: mesh-rules
score:
  band: developing
  composite: 54.1
  coverage:
    artifact_dirs: 29
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 73.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 43.4
    contract_governance: 31.8
    contract_quality: 56.9
    developer_ergonomics: 68.5
    discoverability: 73.2
    operational_transparency: 42.1
  previous_composite: 54.1
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/mesh/mesh-2026-08-07T172618.png
security:
- kind: authentication
  name: Mesh Authentication
  slug: mesh-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Mesh Domain Security
  slug: mesh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Mesh Trust Center
  slug: mesh-trust-center
  summary_line: SOC 2 Type II
skill_count: 3
skills:
- name: Connect an account and take a crypto deposit
  slug: mesh-connect-and-deposit
- name: Quote, preview, and execute a managed transfer
  slug: mesh-managed-transfer
- name: Read a connected account's holdings and balances
  slug: mesh-read-holdings-and-balances
slug: mesh
tags:
- Company
- Cryptocurrency
- Payments
- Digital Assets
- Financial Services
- Wallets
- Exchange
- Transfers
- Stablecoins
- Embedded Finance
- Fintech
- On-Ramp
- Blockchain
website: https://meshconnect.com
---

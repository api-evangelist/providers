---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.5
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Debank Agentic Access
  operation_count: 42
  slug: debank-agentic-access
  summary_line: 42 operations · 4 acting
api_count: 2
apis:
- description: 'The DeBank Cloud Pro API — a Swagger 2.0 contract published at the API host root covering chain and protocol metadata, pool and token data, historical token prices, user portfolio reads (token lists, '
  name: DeBank OpenAPI
  slug: debank-openapi
- description: OAuth 2.0 authorization-code sign-in for dApps. After a user authorizes, the dApp exchanges the code at api.connect.debank.com/oauth/token using HTTP Basic client credentials and reads the user's base
  name: DeBank Connect
  slug: debank-connect
artifact_total: 8
common:
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
overview: 'DeBank publishes 1 API on the [APIs.io](https://apis.io/) network: OpenAPI. Tagged areas include web3, defi, blockchain, crypto, and portfolio-tracking.


  DeBank''s developer surface includes authentication, documentation, API reference, getting-started guide, signup flow, support, changelog, and 17 more developer resources.'
plans:
- name: Debank Plans Pricing
  plan_count: 0
  slug: debank-plans-pricing
random_paper: 13
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
  band: developing
  composite: 42.2
  facets:
    commercial_clarity: 23.7
    contract_quality: 38.1
    developer_ergonomics: 56.5
    discoverability: 75.9
    governance: 20.8
    operational_transparency: 42.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 48.4
  schema_version: 0.11.0
  scored_at: '2026-08-12'
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
- web3
- defi
- blockchain
- crypto
- portfolio-tracking
- on-chain-data
- wallet
- token-data
- nft
- ethereum
- oauth
- market-data
website: https://debank.com/
---

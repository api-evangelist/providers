---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.7
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 9
  human_in_the_loop: 3
  name: Coinlist Agentic Access
  operation_count: 22
  slug: coinlist-agentic-access
  summary_line: 22 operations · 9 acting · 3 human-in-the-loop
api_count: 11
apis:
- description: The DocumentSubmissions API from CoinList — 1 operation(s) for documentsubmissions.
  name: CoinList DocumentSubmissions API
  slug: coinlist-documentsubmissions-api
- description: The KYC API from CoinList — 1 operation(s) for kyc.
  name: CoinList KYC API
  slug: coinlist-kyc-api
- description: The OAuth API from CoinList — 3 operation(s) for oauth.
  name: CoinList OAuth API
  slug: coinlist-oauth-api
- description: The Offers API from CoinList — 4 operation(s) for offers.
  name: CoinList Offers API
  slug: coinlist-offers-api
- description: The Participations API from CoinList — 2 operation(s) for participations.
  name: CoinList Participations API
  slug: coinlist-participations-api
- description: The Pii API from CoinList — 1 operation(s) for pii.
  name: CoinList Pii API
  slug: coinlist-pii-api
- description: The Requirements API from CoinList — 2 operation(s) for requirements.
  name: CoinList Requirements API
  slug: coinlist-requirements-api
- description: The Swap API from CoinList — 3 operation(s) for swap.
  name: CoinList Swap API
  slug: coinlist-swap-api
- description: The Token API from CoinList — 2 operation(s) for token.
  name: CoinList Token API
  slug: coinlist-token-api
- description: The Wallet API from CoinList — 1 operation(s) for wallet.
  name: CoinList Wallet API
  slug: coinlist-wallet-api
- description: The Wallet Ownership API from CoinList — 1 operation(s) for wallet ownership.
  name: CoinList Wallet Ownership API
  slug: coinlist-wallet-ownership-api
arazzos:
- description: Load an offer, check on-chain balance/allowance, prove and allow-list the wallet, then create and track a participation.
  name: CoinList Passage - Invest flow
  slug: coinlist-invest-flow
- description: Start a Sumsub KYC session, read stored PII, and create a tax-document signing submission for a Passage user.
  name: CoinList Passage - KYC and document onboarding
  slug: coinlist-kyc-onboarding
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Frontline DocumentSubmissions API
  slug: open-coinlist-documentsubmissions-api
- collection_type: open
  name: Frontline DocumentSubmissions KYC API
  slug: open-coinlist-kyc-api
- collection_type: open
  name: Frontline DocumentSubmissions OAuth API
  slug: open-coinlist-oauth-api
- collection_type: open
  name: Frontline DocumentSubmissions Offers API
  slug: open-coinlist-offers-api
- collection_type: open
  name: Frontline DocumentSubmissions Participations API
  slug: open-coinlist-participations-api
- collection_type: open
  name: Frontline DocumentSubmissions Pii API
  slug: open-coinlist-pii-api
- collection_type: open
  name: Frontline DocumentSubmissions Requirements API
  slug: open-coinlist-requirements-api
- collection_type: open
  name: Frontline DocumentSubmissions Swap API
  slug: open-coinlist-swap-api
- collection_type: open
  name: Frontline DocumentSubmissions Token API
  slug: open-coinlist-token-api
- collection_type: open
  name: Frontline DocumentSubmissions Wallet API
  slug: open-coinlist-wallet-api
- collection_type: open
  name: Frontline DocumentSubmissions Wallet Ownership API
  slug: open-coinlist-wallet-ownership-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/coinlist-passage-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/coinlist-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/coinlist-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/coinlist-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/coinlist-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/coinlist-packages.yml
- group: design
  title: ''
  type: Components
  url: components/coinlist-components.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/coinlist-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/coinlist-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/coinlist-agentic-access.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/coinlist-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/coinlist-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/coinlist-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/coinlist-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/coinlist-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coinlist.co
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/coinlist-changelog.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coinlist-invest-flow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/coinlist-kyc-onboarding.yml
- group: company
  title: ''
  type: Website
  url: https://coinlist.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://passage.coinlist.co/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.passage.coinlist.co/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.passage.coinlist.co/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.passage.coinlist.co/sdk/quickstart
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coinlist
- group: company
  title: ''
  type: Blog
  url: https://blog.coinlist.co
- group: operate
  title: ''
  type: Support
  url: https://support.coinlist.co/
- group: operate
  title: ''
  type: HelpCenter
  url: https://coinlist.co/faq
- group: commercial
  title: ''
  type: TermsOfService
  url: https://coinlist.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coinlist.co/privacy
- group: start
  title: ''
  type: Login
  url: https://coinlist.co/login
created: '2026-07-17'
description: 'CoinList is a fintech platform for the token economy - it runs compliant token sales, tokenized equities, trading, staking, and wallet services for crypto projects and investors. Its developer surface is Passage (the "Frontline API"), a partner API that lets third parties embed CoinList-managed token sales and tokenized equities directly inside their own apps: OAuth 2.0 (PKCE) partner and user authentication, Sumsub KYC token issuance, tax-document signing, offers, eligibility requirements, participations, wallet ownership proof and allow-listing, and on-chain swap/token reads. Passage runs the regulated infrastructure and back office; the partner focuses on the product. Shipped with a React SDK (@coinlist-co/react) of UI components, hooks, and server helpers. Added to the API Evangelist network from the electric-capital and polychain portfolios and enriched from CoinList''s public developer surface.'
image: https://logo.clearbit.com/coinlist.co
layout: provider
mcp_servers:
- description: ''
  name: coinlist-mcp.yml
  slug: coinlist-mcpyml
modified: '2026-07-18'
name: CoinList
nav: Providers
network: true
overview: 'CoinList publishes 11 APIs on the [APIs.io](https://apis.io/) network, including DocumentSubmissions API, KYC API, OAuth API, and 8 more. Tagged areas include Company, Fintech, Cryptocurrency, Token Sales, and Tokenized Equities.


  CoinList''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, engineering blog, support, and 25 more developer resources.'
random_paper: 124
scopes:
- name: Coinlist Scopes
  scope_count: 0
  slug: coinlist-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.3
    developer_ergonomics: 62.5
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 36.8
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 58.3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
security:
- kind: authentication
  name: Coinlist Authentication
  slug: coinlist-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Coinlist Domain Security
  slug: coinlist-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: coinlist
tags:
- Company
- Fintech
- Cryptocurrency
- Token Sales
- Tokenized Equities
- KYC
- OAuth
- Blockchain
- Digital Assets
- Embedded Finance
website: https://coinlist.co/
---

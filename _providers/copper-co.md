---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: near-conformant
    agent_skills: true
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 67.4
  scored_at: '2026-08-11'
api_count: 18
apis:
- description: The Accounts API from Copper.co — 1 operation(s) for accounts.
  name: Copper.co Accounts API
  slug: copper-co-accounts-api
- description: The address-book API from Copper.co — 2 operation(s) for address-book.
  name: Copper.co Address Book API
  slug: copper-co-address-book-api
- description: The blockchain API from Copper.co — 1 operation(s) for blockchain.
  name: Copper.co Blockchain API
  slug: copper-co-blockchain-api
- description: The clearloop API from Copper.co — 9 operation(s) for clearloop.
  name: Copper.co Clearloop API
  slug: copper-co-clearloop-api
- description: The currencies API from Copper.co — 3 operation(s) for currencies.
  name: Copper.co Currencies API
  slug: copper-co-currencies-api
- description: The deposit-targets API from Copper.co — 2 operation(s) for deposit-targets.
  name: Copper.co Deposit Targets API
  slug: copper-co-deposit-targets-api
- description: The Exchange API from Copper.co — 1 operation(s) for exchange.
  name: Copper.co Exchange API
  slug: copper-co-exchange-api
- description: The files API from Copper.co — 1 operation(s) for files.
  name: Copper.co Files API
  slug: copper-co-files-api
- description: The lending API from Copper.co — 34 operation(s) for lending.
  name: Copper.co Lending API
  slug: copper-co-lending-api
- description: The network API from Copper.co — 1 operation(s) for network.
  name: Copper.co Network API
  slug: copper-co-network-api
- description: The orders API from Copper.co — 8 operation(s) for orders.
  name: Copper.co Orders API
  slug: copper-co-orders-api
- description: The organizations API from Copper.co — 3 operation(s) for organizations.
  name: Copper.co Organizations API
  slug: copper-co-organizations-api
- description: The portfolios API from Copper.co — 2 operation(s) for portfolios.
  name: Copper.co Portfolios API
  slug: copper-co-portfolios-api
- description: The reports API from Copper.co — 6 operation(s) for reports.
  name: Copper.co Reports API
  slug: copper-co-reports-api
- description: The Sign Async API from Copper.co — 2 operation(s) for sign async.
  name: Copper.co Sign Async API
  slug: copper-co-sign-async-api
- description: The stake API from Copper.co — 3 operation(s) for stake.
  name: Copper.co Stake API
  slug: copper-co-stake-api
- description: The trades API from Copper.co — 19 operation(s) for trades.
  name: Copper.co Trades API
  slug: copper-co-trades-api
- description: The wallets API from Copper.co — 2 operation(s) for wallets.
  name: Copper.co Wallets API
  slug: copper-co-wallets-api
artifact_total: 25
asyncapis:
- description: ''
  name: Copper Co Webhooks
  slug: copper-co-webhooks
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/copper-co-platform-overlay.yaml
- group: company
  title: ''
  type: Website
  url: https://copper.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.copper.co/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.copper.co/guides/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://developer.copper.co/api-reference/getting-started
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.copper.co/api-reference/getting-started
- group: auth
  title: ''
  type: Authentication
  url: authentication/copper-co-authentication.yml
- group: operate
  title: ''
  type: Support
  url: https://help.copper.co
- group: company
  title: ''
  type: Blog
  url: https://copper.co/en/insights/company-news
- group: commercial
  title: ''
  type: Pricing
  url: https://copper.co/en/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://copper.co/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://copper.co/en/privacy
- group: build
  title: ''
  type: Postman
  url: https://developer.copper.co/api-reference/try-it-out#postman-collection
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/copper-co-changelog.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/copper-co-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://copper.co/en/status
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/copper-co-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/copper-co-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/copper-co-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/copper-co-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/copper-co-rate-limits.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/copper-co-sandbox.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/copper-co-webhooks.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/copper-co-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/copper-co-a2a.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/copper-co-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/copper-co-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/copper-co-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://copper.co/en/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/copper-co-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/copper-co-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/copper-co-packages.yml
created: '2026-08-04'
description: Copper is an institutional digital asset infrastructure provider headquartered in Zug, Switzerland, offering custody, prime services and collateral management to hedge funds, trading firms, exchanges, ETP providers, foundations and miners. Its Copper Platform API is a REST API over portfolios (called "accounts" in the UI), wallets, orders, transfers, withdrawals, staking, agency and bilateral lending, and ClearLoop — Copper's off-exchange settlement and collateral network that lets clients trade on connected exchanges while assets remain in custody. The API authenticates with an API key plus a per-request HMAC-SHA256 signature, publishes OpenAPI 3.1 specifications and a Postman collection, and offers a webhook system for real-time order, deposit, withdrawal, ClearLoop and address-book events.
image: https://cdn.sanity.io/images/ih0ldmk7/production/7362d67a23ba5de367175e92536225788ede190c-2400x1181.jpg
layout: provider
mcp_servers:
- description: ''
  name: copper-co-mcp.yml
  slug: copper-co-mcpyml
modified: '2026-08-04'
name: Copper.co
nav: Providers
network: true
overview: 'Copper.co publishes 18 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Address Book API, Blockchain API, and 15 more. Tagged areas include Company, Digital Asset Custody, Cryptocurrency, Financial Services, and Institutional Finance.


  The Copper.co catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Copper.co''s developer surface includes documentation, API reference, getting-started guide, authentication, support, engineering blog, pricing, and 26 more developer resources.'
random_paper: 92
rate_limits:
- limit_count: 4
  name: Copper Co Rate Limits
  slug: copper-co-rate-limits
score:
  band: strong
  composite: 58.4
  delta: -1.8
  facets:
    commercial_clarity: 47.4
    contract_quality: 59.8
    developer_ergonomics: 78.3
    discoverability: 81.5
    governance: 11.5
    operational_transparency: 78.9
  previous_composite: 60.2
  provenance:
    conformance: derived
    contracts:
      callable: 94.4
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 50.0
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/copper-co/refs/heads/main/screenshots/copper-co-2026-08-07T163810.png
security:
- kind: authentication
  name: Copper Co Authentication
  slug: copper-co-authentication
  summary_line: apiKey/httpSignature · 2 schemes
- kind: domain-security
  name: Copper Co Domain Security
  slug: copper-co-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Copper Co Vulnerability Disclosure
  slug: copper-co-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Copper Co Trust Center
  slug: copper-co-trust-center
  summary_line: SOC 2, ISO 27001, NIST Cybersecurity Framework
slug: copper-co
tags:
- Company
- Digital Asset Custody
- Cryptocurrency
- Financial Services
- Institutional Finance
- Prime Brokerage
- Collateral Management
- Lending
- Settlement
- Staking
- Blockchain
- Treasury Management
website: https://copper.co/
---

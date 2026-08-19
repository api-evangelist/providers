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
  band: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: verified
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.3
  scored_at: '2026-08-19'
api_count: 6
apis:
- description: The Accounts API from Brale — 4 operation(s) for accounts.
  name: Brale Accounts API
  slug: brale-accounts-api
- description: The Addresses API from Brale — 5 operation(s) for addresses.
  name: Brale Addresses API
  slug: brale-addresses-api
- description: The Automations API from Brale — 2 operation(s) for automations.
  name: Brale Automations API
  slug: brale-automations-api
- description: The Financial Institutions API from Brale — 10 operation(s) for financial institutions.
  name: Brale Financial Institutions API
  slug: brale-financial-institutions-api
- description: The Orders API from Brale — 8 operation(s) for orders.
  name: Brale Orders API
  slug: brale-orders-api
- description: The Webhooks API from Brale — 6 operation(s) for webhooks.
  name: Brale Webhooks API
  slug: brale-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Brale Webhooks
  slug: brale-webhooks
collections:
- collection_type: postman
  name: Brale Accounts API
  slug: postman-brale-accounts-api
- collection_type: postman
  name: Brale Accounts Addresses API
  slug: postman-brale-addresses-api
- collection_type: postman
  name: Brale Accounts Automations API
  slug: postman-brale-automations-api
- collection_type: postman
  name: Brale Accounts Financial Institutions API
  slug: postman-brale-financial-institutions-api
- collection_type: postman
  name: Brale Accounts Orders API
  slug: postman-brale-orders-api
- collection_type: postman
  name: Brale Accounts Webhooks API
  slug: postman-brale-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Brale Accounts API
  slug: open-brale-accounts-api
- collection_type: open
  name: Brale Accounts Addresses API
  slug: open-brale-addresses-api
- collection_type: open
  name: Brale Accounts Automations API
  slug: open-brale-automations-api
- collection_type: open
  name: Brale Accounts Financial Institutions API
  slug: open-brale-financial-institutions-api
- collection_type: open
  name: Brale Accounts Orders API
  slug: open-brale-orders-api
- collection_type: open
  name: Brale Accounts Webhooks API
  slug: open-brale-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/brale/overview
- group: other
  title: ''
  type: AgentCard
  url: a2a/brale-a2a.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.brale.xyz/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.brale.xyz/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.brale.xyz/api-reference/brale-introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.brale.xyz/documentation/introduction
- group: company
  title: ''
  type: Blog
  url: https://brale.xyz/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://brale.xyz/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.brale.xyz
- group: start
  title: ''
  type: Login
  url: https://app.brale.xyz
- group: operate
  title: ''
  type: Support
  url: https://brale.xyz/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://brale.xyz/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://brale.xyz/legal/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Brale-xyz
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/brale-xyz/brale-api/overview
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/brale-openapi-original.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/brale-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/brale-scopes.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/brale-domain-security.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/brale-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/brale-well-known.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/brale-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://brale.xyz/security
- group: agent
  title: ''
  type: MCPServer
  url: mcp/brale-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/brale-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/brale-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/brale-cli.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/brale-openapi-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/brale-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/brale-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/brale-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.brale.xyz
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/brale-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/brale-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/brale-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/brale-changelog.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/brale-sandbox.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/brale-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/brale-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Brale is a regulated stablecoin issuance and orchestration platform. Its Issuance and Orchestration API lets businesses create their own fiat-backed stablecoins and move value across fiat rails and blockchains — onramps, offramps, swaps, custody, and payouts — with mint/burn execution, reserves, custody, settlement, and reporting handled by Brale. Developers authenticate with OAuth2 client-credentials and manage customer accounts (KYB/KYC), on-chain and off-chain addresses, transfers, automations (virtual U.S. account/routing numbers that auto-mint stablecoins on fiat deposit), self-attested tokenization (mints, burns, transfers), and webhooks across Stellar, Solana, Base, Ethereum, Polygon, Avalanche, Celo, Optimism, Arbitrum, and Canton.
image: https://brale.xyz/assets/site/global-og-image.png
layout: provider
mcp_servers:
- description: ''
  name: brale-mcp.yml
  slug: brale-mcpyml
modified: '2026-07-18'
name: Brale
nav: Providers
network: true
overview: 'Brale publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Addresses API, Automations API, and 3 more. Tagged areas include Company, Stablecoins, Stablecoin Issuance, Payments, and Blockchain.


  The Brale catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Brale''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 33 more developer resources.'
random_paper: 71
scopes:
- name: Brale Scopes
  scope_count: 20
  slug: brale-scopes
  summary_line: 20 scopes · clientCredentials
score:
  band: strong
  composite: 63.7
  delta: 2.6
  facets:
    access_clarity: 44.7
    commercial_clarity: 44.7
    contract_governance: 16.7
    contract_quality: 65.0
    developer_ergonomics: 73.2
    discoverability: 92.6
    governance: 16.7
    operational_transparency: 60.5
  previous_composite: 61.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 64.1
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/brale/refs/heads/main/screenshots/brale-2026-07-25T203713.png
security:
- kind: authentication
  name: Brale Authentication
  slug: brale-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Brale Domain Security
  slug: brale-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Brale Vulnerability Disclosure
  slug: brale-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: brale
tags:
- Company
- Stablecoins
- Stablecoin Issuance
- Payments
- Blockchain
- Cryptocurrency
- Fintech
- Financial Services
- Custody
- Tokenization
- On-Ramp
- Off-Ramp
website: https://docs.brale.xyz/
---

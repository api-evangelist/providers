---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.1
  scored_at: '2026-08-10'
api_count: 17
apis:
- description: The ABC Accounts API from PolySign — 3 operation(s) for abc accounts.
  name: PolySign ABC Accounts API
  slug: polysign-abc-accounts-api
- description: The ABC Memorials API from PolySign — 2 operation(s) for abc memorials.
  name: PolySign ABC Memorials API
  slug: polysign-abc-memorials-api
- description: The ABC Signing API from PolySign — 1 operation(s) for abc signing.
  name: PolySign ABC Signing API
  slug: polysign-abc-signing-api
- description: The ABC Testnet API from PolySign — 2 operation(s) for abc testnet.
  name: PolySign ABC Testnet API
  slug: polysign-abc-testnet-api
- description: The asset API from PolySign — 5 operation(s) for asset.
  name: PolySign Asset API
  slug: polysign-asset-api
- description: The authentication API from PolySign — 1 operation(s) for authentication.
  name: PolySign Authentication API
  slug: polysign-authentication-api
- description: The beneficiary authorization API from PolySign — 6 operation(s) for beneficiary authorization.
  name: PolySign beneficiary authorization API
  slug: polysign-beneficiary-authorization-api
- description: The book transfer API from PolySign — 5 operation(s) for book transfer.
  name: PolySign book transfer API
  slug: polysign-book-transfer-api
- description: The book transfer confirmation API from PolySign — 4 operation(s) for book transfer confirmation.
  name: PolySign book transfer confirmation API
  slug: polysign-book-transfer-confirmation-api
- description: The escrow authorization API from PolySign — 6 operation(s) for escrow authorization.
  name: PolySign escrow authorization API
  slug: polysign-escrow-authorization-api
- description: The investor API from PolySign — 2 operation(s) for investor.
  name: PolySign Investor API
  slug: polysign-investor-api
- description: The order API from PolySign — 5 operation(s) for order.
  name: PolySign Order API
  slug: polysign-order-api
- description: The partner API from PolySign — 3 operation(s) for partner.
  name: PolySign Partner API
  slug: polysign-partner-api
- description: The settlement API from PolySign — 5 operation(s) for settlement.
  name: PolySign Settlement API
  slug: polysign-settlement-api
- description: The settlement confirmation API from PolySign — 6 operation(s) for settlement confirmation.
  name: PolySign settlement confirmation API
  slug: polysign-settlement-confirmation-api
- description: The system API from PolySign — 4 operation(s) for system.
  name: PolySign System API
  slug: polysign-system-api
- description: The utility API from PolySign — 5 operation(s) for utility.
  name: PolySign Utility API
  slug: polysign-utility-api
artifact_total: 20
common:
- group: company
  title: ''
  type: Website
  url: https://www.polysign.io/
- group: other
  title: ''
  type: SecondaryMarket
  url: https://forgeglobal.com/polysign_stock/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.polynet.sandbox.polysign.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.polynet.sandbox.polysign.io/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/PolySignInc
- group: operate
  title: ''
  type: Support
  url: https://www.polysign.io/contact.html
- group: commercial
  title: ''
  type: LegalNotice
  url: https://www.polysign.io/legal.html
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/polysigninc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/polysign
- group: auth
  title: ''
  type: Authentication
  url: authentication/polysign-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/polysign-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/polysign-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/polysign-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/polysign-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/polysign-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/polysign-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/polysign-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/polysign-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/polysign-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/polysign-sandbox.yml
created: '2026-08-02'
description: PolySign, Inc. is an Oakland / San Francisco / New York financial technology company building blockchain-enabled infrastructure for institutional digital asset capital markets and payments. Founded by Arthur Britto, David Schwartz and Jack McDonald, PolySign operates a third-generation permissioned blockchain and the AtomicNet settlement network, and was the parent of Standard Custody & Trust Company, the NYDFS-regulated digital asset custody, trading and settlement platform acquired by Ripple in 2024. PolySign publishes three OpenAPI 3.0.3 contracts for AtomicNet — the AtomicNet API Server (node interface for assets, orders, escrow and beneficiary authorizations, settlements, settlement confirmations, book transfers, partners and investors), the AtomicNet Merchant Gate Node, and the AtomicNet ABC Proxy Service (account registration, digest memorialization, signing and testnet faucet) — all authenticated with OAuth 2.0 client credentials issued by a PolySign-hosted token endpoint.
image: https://www.polysign.io/images/logo.png
layout: provider
modified: '2026-08-02'
name: PolySign
nav: Providers
network: true
overview: 'PolySign publishes 17 APIs on the [APIs.io](https://apis.io/) network, including ABC Accounts API, ABC Memorials API, ABC Signing API, and 14 more. Tagged areas include digital-assets, blockchain, institutional-custody, settlement, and escrow.


  PolySign''s developer surface includes documentation, API reference, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 73
scopes:
- name: Polysign Scopes
  scope_count: 1
  slug: polysign-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 30.6
  delta: -0.4
  facets:
    commercial_clarity: 0.0
    contract_quality: 41.9
    developer_ergonomics: 38.6
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 5.3
  previous_composite: 31.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 42.2
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Polysign Authentication
  slug: polysign-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Polysign Domain Security
  slug: polysign-domain-security
  summary_line: TLSv1.3 · DMARC
slug: polysign
tags:
- digital-assets
- blockchain
- institutional-custody
- settlement
- escrow
- capital-markets
- payments
- fintech
- distributed-ledger
- atomicnet
website: https://www.polysign.io/
---

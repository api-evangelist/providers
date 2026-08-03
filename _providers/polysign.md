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
  scored_at: '2026-08-03'
api_count: 3
apis:
- description: The node-side REST interface for interacting with an AtomicNet node — registering assets and partners, publishing orders and book transfers, requesting and approving escrow and beneficiary authorizati
  name: AtomicNet API Server
  slug: atomicnet-api-server
- description: 'The merchant-facing gate onto an AtomicNet node: submit an order, submit a book transfer, and register assets to the node, alongside the shared authentication and system health surface. Eight operatio'
  name: AtomicNet Merchant Gate Node
  slug: atomicnet-merchant-gate-node
- description: 'Proxy service for the ABC ledger: register an ABC account against an AtomicNet ID, look up account information, memorialize a digest and verify that a digest was memorialized, sign a digest and verify'
  name: AtomicNet ABC Proxy Service
  slug: atomicnet-abc-proxy-service
artifact_total: 6
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
overview: 'PolySign publishes 3 APIs on the [APIs.io](https://apis.io/) network: AtomicNet API Server, AtomicNet Merchant Gate Node, and AtomicNet ABC Proxy Service. Tagged areas include digital-assets, blockchain, institutional-custody, settlement, and escrow.


  PolySign''s developer surface includes documentation, API reference, support, authentication, sandbox, and 16 more developer resources.'
random_paper: 30
scopes:
- name: Polysign Scopes
  scope_count: 1
  slug: polysign-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: thin
  composite: 31.0
  facets:
    commercial_clarity: 0.0
    contract_quality: 43.7
    developer_ergonomics: 38.6
    discoverability: 83.3
    governance: 11.5
    operational_transparency: 5.3
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
  schema_version: 0.9
  scored_at: '2026-08-03'
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

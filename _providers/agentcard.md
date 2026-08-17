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
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: true
    idempotency: documented
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 71.2
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Agentcard Agentic Access
  operation_count: 21
  slug: agentcard-agentic-access
  summary_line: 21 operations · 15 acting
api_count: 5
apis:
- description: Exchange your client credentials for a platform access token, and introspect what a token acts as.
  name: Agentcard Authentication API
  slug: agentcard-authentication-api
- description: 'Connect a user to your platform: send a one-time code, verify it, record consent, and keep the connection alive.'
  name: Agentcard Connect API
  slug: agentcard-connect-api
- description: 'Verify a connected user''s identity: upload their ID, submit any extra fields we ask for, then show a short face scan.'
  name: Agentcard Identity verification API
  slug: agentcard-identity-verification-api
- description: Fund a connected user's wallet from your own UI — request a payment link, relay the phone verification code, and poll until the funds land.
  name: Agentcard Wallet funding API
  slug: agentcard-wallet-funding-api
- description: Move money out of a connected user's wallet — to a saved bank account or a crypto address on Base. Transfers are processed manually by the Agentcard team, usually within 1-3 business days.
  name: Agentcard Withdrawals API
  slug: agentcard-withdrawals-api
arazzos:
- description: Connect an end user, record consent, and run identity verification (KYC) end to end.
  name: Agentcard — connect a user and verify identity
  slug: agentcard-connect-and-verify.arazzo
- description: Verify a user's phone, create an Apple/Google Pay funding session, and poll it to completion.
  name: Agentcard — verify phone and fund wallet
  slug: agentcard-fund-wallet.arazzo
artifact_total: 19
asyncapis:
- description: Event notifications Agentcard delivers to destinations you register in the dashboard. Every delivery is a POST with a signed envelope { id, type, created, livemode, data }. Verify the AgentCard-Signat
  name: Agentcard Webhooks
  slug: agentcard-webhooks-asyncapi
- description: ''
  name: Agentcard Webhooks
  slug: agentcard-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Agentcard Authentication API
  slug: open-agentcard-authentication-api
- collection_type: open
  name: Agentcard Authentication Connect API
  slug: open-agentcard-connect-api
- collection_type: open
  name: Agentcard Authentication Identity verification API
  slug: open-agentcard-identity-verification-api
- collection_type: open
  name: Agentcard Authentication Wallet funding API
  slug: open-agentcard-wallet-funding-api
- collection_type: open
  name: Agentcard Authentication Withdrawals API
  slug: open-agentcard-withdrawals-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/agentcard-v2-overlay.yaml
- group: other
  title: ''
  type: AgentCard
  url: a2a/agentcard-a2a.yml
- group: company
  title: ''
  type: Website
  url: https://www.agentcard.sh
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.agentcard.sh
- group: docs
  title: ''
  type: Documentation
  url: https://docs.agentcard.sh
- group: docs
  title: ''
  type: APIReference
  url: https://docs.agentcard.sh/companies/api/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.agentcard.sh/companies/getting-started/quickstart
- group: start
  title: ''
  type: Quickstart
  url: https://docs.agentcard.sh/personal/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.agentcard.sh/personal/support
- group: company
  title: ''
  type: Blog
  url: https://www.agentcard.sh/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/agentcard
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.agentcard.sh/personal/plans
- group: start
  title: ''
  type: SignUp
  url: https://app.agentcard.sh
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agentcard.sh/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agentcard.sh/privacy
- group: build
  title: ''
  type: Postman
  url: https://docs.agentcard.sh/companies/api/postman
- group: operate
  title: ''
  type: StatusPage
  url: https://agentcard.checkly-status-page.com
- group: auth
  title: ''
  type: Authentication
  url: authentication/agentcard-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/agentcard-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/agentcard-domain-security.yml
- group: build
  title: ''
  type: Packages
  url: packages/agentcard-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/agentcard-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/agentcard-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/agentcard-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/agentcard-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/agentcard-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: well-known/agentcard-api-catalog.json
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/agentcard-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/agentcard-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/agentcard-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/agentcard-lifecycle.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/agentcard-sandbox.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/agentcard-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/agentcard-data-model.yml
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/agentcard-webhooks-asyncapi.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/agentcard-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/agentcard-connect-and-verify.arazzo.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/agentcard-fund-wallet.arazzo.yml
created: '2026-07-17'
description: 'Agentcard is a Y Combinator (Summer 2026) startup building card-issuing payments infrastructure for AI agents. It issues virtual Visa cards that are funded with a fixed USD amount and close after their first charge, giving agents scoped, single-use spending power with hard budget limits and no overdraft risk. Access is available three ways over one host: a REST v2 API, a hosted Model Context Protocol (MCP) server, and first-party CLIs. There are two products: Personal (an individual gives their own agent a card, funded via Apple Pay / Google Pay) and Companies ("Connect with Agentcard" — a platform issues cards to many users through OAuth 2.1 + PKCE). The platform covers user connect, identity verification (KYC), wallet funding, withdrawals, virtual card creation, transactions, and merchant shopping (buy) with HMAC-signed webhooks and a sandbox mode split from live by credential.'
image: https://www.agentcard.sh/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: agentcard-mcp.yml
  slug: agentcard-mcpyml
modified: '2026-07-17'
name: Agentcard
nav: Providers
network: true
overview: 'Agentcard publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Authentication API, Connect API, Identity verification API, and 2 more. Tagged areas include Company, Payments, Virtual Cards, Card Issuing, and AI Agents.


  The Agentcard catalog on APIs.io includes 2 event-driven AsyncAPI specifications.


  Agentcard''s developer surface includes documentation, API reference, getting-started guide, quickstart, support, engineering blog, pricing, and 32 more developer resources.'
random_paper: 43
score:
  band: strong
  composite: 56.4
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 71.6
    developer_ergonomics: 91.3
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 28.9
  previous_composite: 56.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 39.1
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/agentcard/refs/heads/main/screenshots/agentcard-2026-07-25T181800.png
security:
- kind: authentication
  name: Agentcard Authentication
  slug: agentcard-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Agentcard Domain Security
  slug: agentcard-domain-security
  summary_line: TLSv1.3 · DMARC
slug: agentcard
tags:
- Company
- Payments
- Virtual Cards
- Card Issuing
- AI Agents
- Agentic Commerce
- MCP
- Fintech
- Wallet
- Visa
website: https://www.agentcard.sh
---

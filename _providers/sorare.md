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
    agentic_access: false
    asyncapi_events: true
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 43.9
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Single GraphQL endpoint exposing Sorare cards, users, auctions, offers and real-time subscriptions across football, NBA and MLB, with JWT / OAuth 2.0 / API-key auth.
  name: Sorare GraphQL API
  slug: sorare-graphql-api
artifact_total: 7
asyncapis:
- description: ''
  name: Sorare Graphql Asyncapi
  slug: sorare-graphql-asyncapi
common:
- group: company
  title: ''
  type: Website
  url: https://sorare.com
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/sorare/api
- group: docs
  title: ''
  type: APIReference
  url: https://api.sorare.com/graphql/playground
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sorare
- group: operate
  title: ''
  type: Support
  url: https://help.sorare.com
- group: start
  title: ''
  type: SignUp
  url: https://sorare.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sorare.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sorare.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/sorare-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sorare-scopes.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sorare-rate-limits.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sorare-conventions.yml
- group: build
  title: ''
  type: Packages
  url: packages/sorare-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/sorare-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/sorare-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/sorare-security.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sorare-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://sorare.com/.well-known/security.txt
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/sorare-graphql-asyncapi.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sorare-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sorare-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sorare-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sorare-llms.txt
created: '2026-07-17'
description: Sorare is a global fantasy sports platform for football (soccer), NBA basketball and MLB baseball built on blockchain-based digital collectible player cards stored on Ethereum and a StarkWare rollup. Its public developer surface is a single GraphQL API at https://api.sorare.com/graphql covering cards, users, auctions, offers and real-time subscriptions. The API supports JWT authentication (via the signIn mutation, with TOTP 2FA), OAuth 2.0 (Authorization Code and Client Credentials), and optional API keys for elevated rate limits, plus StarkWare payload signing for on-chain trading actions.
image: https://sorare.com/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: sorare-mcp.yml
  slug: sorare-mcpyml
modified: '2026-07-21'
name: Sorare
nav: Providers
network: true
overview: 'Sorare publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, GraphQL, Fantasy Sports, and NFT.


  The Sorare catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sorare''s developer surface includes documentation, API reference, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 36
rate_limits:
- limit_count: 0
  name: Sorare Rate Limits
  slug: sorare-rate-limits
scopes:
- name: Sorare Scopes
  scope_count: 1
  slug: sorare-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: thin
  composite: 40.1
  delta: 4.8
  facets:
    commercial_clarity: 34.2
    contract_quality: 51.6
    developer_ergonomics: 40.8
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 23.7
  previous_composite: 35.3
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Sorare Authentication
  slug: sorare-authentication
  summary_line: http/oauth2/apiKey · 3 schemes
- kind: vulnerability-disclosure
  name: Sorare Vulnerability Disclosure
  slug: sorare-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: sorare
tags:
- Company
- Crypto
- GraphQL
- Fantasy Sports
- NFT
- Blockchain
- Gaming
- Sports
- Web3
website: https://sorare.com
---

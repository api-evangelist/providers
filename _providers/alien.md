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
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: OpenID Connect / OAuth 2.0 identity provider for proof-of-humanity sign-in. Authorization code + PKCE (S256), refresh tokens, optional DPoP (RFC 9449) sender-constrained tokens, and Agent ID (Ed25519)
  name: Alien SSO
  slug: alien-sso
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alien-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://alien.org/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.alien.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alien.org
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alien.org/sso-api-reference/api-reference-core
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alien.org/sso-guide/introduction
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alien-id
- group: company
  title: ''
  type: Blog
  url: https://alien.org/blog
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/alien
- group: start
  title: ''
  type: SignUp
  url: https://app.alien.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alien.org/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://alien.org/legal/privacy
- group: company
  title: ''
  type: Twitter
  url: https://x.com/alienorg
- group: build
  title: ''
  type: Packages
  url: packages/alien-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/alien-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/alien-cli.yml
- group: design
  title: ''
  type: Components
  url: components/alien-components.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/alien-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alien-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/alien-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/alien-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alien-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/alien-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alien-problem-types.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alien-mcp.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alien-lifecycle.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: 'Alien is a proof-of-humanity protocol with its own Layer 1 blockchain that verifies users are real, unique humans without storing biometrics, documents, or personal data — retaining only cryptographic proofs, hashes, and Merkle roots via its Continuous Human Verification Protocol (CHVP). For developers, Alien ships Alien SSO: a standard OpenID Connect / OAuth 2.0 identity provider (authorization code + PKCE, DPoP-bound tokens) that lets apps offer "Sign in with Alien ID" so users prove personhood without sharing name or email. It also provides Alien Agent ID (Ed25519 cryptographic identity linking AI agents to a verified human owner), a Mini Apps SDK, Solana wallet-linking attestations, and first-party JavaScript/React/Python SDKs plus a CLI. Backed by Initialized Capital.'
image: https://alien.org/favicon.ico
layout: provider
mcp_servers:
- description: ''
  name: alien-mcp.yml
  slug: alien-mcpyml
modified: '2026-07-17'
name: Alien
nav: Providers
network: true
overview: 'Alien publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Identity, Authentication, and OAuth.


  Alien''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 20 more developer resources.'
random_paper: 69
scopes:
- name: Alien Scopes
  scope_count: 1
  slug: alien-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 31.5
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 69.0
    discoverability: 87.0
    governance: 12.5
    operational_transparency: 5.3
  previous_composite: 31.5
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alien/refs/heads/main/screenshots/alien-2026-07-25T195612.png
security:
- kind: authentication
  name: Alien Authentication
  slug: alien-authentication
  summary_line: oauth2/openIdConnect · 2 schemes
- kind: domain-security
  name: Alien Domain Security
  slug: alien-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: alien
tags:
- Company
- Crypto
- Identity
- Authentication
- OAuth
- OpenID Connect
- Proof of Humanity
- Blockchain
- Solana
- Agents
website: https://alien.org/
---

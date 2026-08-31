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
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 14.6
  scored_at: '2026-08-30'
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
  name: Alien MCP Server
  slug: alien-mcp-server
modified: '2026-07-17'
name: Alien
nav: Providers
network: true
overview: 'Alien publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto, Identity, Authentication, and OpenID Connect.


  Alien''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, CLI, and 20 more developer resources.'
random_paper: 17
scopes:
- name: Alien Scopes
  scope_count: 1
  slug: alien-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 16
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 31.6
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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
- OpenID Connect
- Proof of Humanity
- Blockchain
- Solana
- Agents
website: https://alien.org/
---

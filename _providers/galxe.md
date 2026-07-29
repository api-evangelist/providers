---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: documented
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: Galxe's public GraphQL API for building web3 experiences — query credentials and eligibility, quests, spaces, loyalty-points leaderboards, and Starboard social/onchain influence metrics, and push cred
  name: Galxe Integration API
  slug: galxe-integration-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://galxe.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.galxe.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.galxe.com/galxe-integration/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.galxe.com/galxe-integration/api-reference/quest
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.galxe.com/galxe-integration/getting-started/quick-start
- group: operate
  title: ''
  type: Support
  url: https://docs.galxe.com/galxe-integration/resources/support
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.galxe.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Galxe
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.galxe.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.galxe.com/about/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://docs.galxe.com/about/legal/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/galxe-changelog.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/galxe-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/galxe-scopes.yml
- group: build
  title: ''
  type: Packages
  url: packages/galxe-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/galxe-packages.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/galxe-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/galxe-error-codes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/galxe-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/galxe-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/galxe-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/galxe-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/galxe-conformance.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/galxe-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/galxe-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/galxe-domain-security.yml
created: '2026-07-17'
description: Galxe is a decentralized super app and one of web3's largest onchain distribution platforms, serving 14M+ Galxe ID users across a product suite of Quest, Passport, Score, Compass, and the Galxe Identity Protocol. For developers, Galxe exposes a public Integration GraphQL API (https://graphigo-business.prd.galaxy.eco/query) to query credentials, quests, spaces, loyalty-points leaderboards, and Starboard social metrics, plus a Credential API for pushing eligibility data, "Sign in with Galxe" OAuth 2.0 for identity, and a TypeScript SDK for the zero-knowledge Galxe Identity Protocol. API access uses a dashboard-issued access-token header with per-second rate limits and monthly quotas. Originally surfaced as a portfolio company of Multicoin Capital and enriched from Galxe's public developer documentation.
image: https://framerusercontent.com/assets/VIwrglmv5dnewbKhEV0KdBzBSAk.jpg
layout: provider
mcp_servers:
- description: ''
  name: galxe-mcp.yml
  slug: galxe-mcpyml
modified: '2026-07-19'
name: Galxe
nav: Providers
network: true
overview: 'Galxe publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Crypto Web3, Digital Identity, Credentials, and Quests.


  Galxe''s developer surface includes documentation, API reference, getting-started guide, support, signup flow, changelog, authentication, and 20 more developer resources.'
plans:
- name: Galxe Plans
  plan_count: 2
  slug: galxe-plans
random_paper: 67
rate_limits:
- limit_count: 0
  name: Galxe Rate Limits
  slug: galxe-rate-limits
scopes:
- name: Galxe Scopes
  scope_count: 12
  slug: galxe-scopes
  summary_line: 12 scopes · authorizationCode
score:
  band: thin
  composite: 35.0
  delta: -2.4
  facets:
    commercial_clarity: 55.3
    contract_quality: 0.0
    developer_ergonomics: 60.3
    discoverability: 75.9
    governance: 12.5
    operational_transparency: 21.1
  previous_composite: 37.4
  provenance:
    conformance: first-party
    mcp: derived
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/galxe/refs/heads/main/screenshots/galxe-2026-07-25T215406.png
security:
- kind: authentication
  name: Galxe Authentication
  slug: galxe-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Galxe Domain Security
  slug: galxe-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: galxe
tags:
- Company
- Crypto Web3
- Digital Identity
- Credentials
- Quests
- Loyalty
- GraphQL
- OAuth
- Blockchain
website: https://galxe.com
---

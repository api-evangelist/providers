---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Single GraphQL endpoint exposing Sorare cards, users, auctions, offers and real-time subscriptions across football, NBA and MLB, with JWT / OAuth 2.0 / API-key auth.
  name: Sorare GraphQL API
  slug: sorare-graphql-api
artifact_total: 8
asyncapis:
- description: ''
  name: Sorare Graphql Asyncapi
  slug: sorare-graphql-asyncapi
common:
- group: company
  title: ''
  type: Blog
  url: https://sorare.com/blog/
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
  href: https://artifacts.apis.io/sorare/authentication/sorare-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sorare-authentication.yml
- group: auth
  href: https://artifacts.apis.io/sorare/scopes/sorare-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/sorare-scopes.yml
- group: operate
  href: https://artifacts.apis.io/sorare/rate-limits/sorare-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sorare-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/sorare/conventions/sorare-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sorare-conventions.yml
- group: build
  href: https://artifacts.apis.io/sorare/packages/sorare-packages.yml
  title: ''
  type: Packages
  url: packages/sorare-packages.yml
- group: build
  href: https://artifacts.apis.io/sorare/packages/sorare-packages.yml
  title: ''
  type: SDKs
  url: packages/sorare-packages.yml
- group: agent
  href: https://artifacts.apis.io/sorare/well-known/sorare-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/sorare-well-known.yml
- group: auth
  href: https://artifacts.apis.io/sorare/well-known/sorare-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/sorare-security.txt
- group: auth
  href: https://artifacts.apis.io/sorare/security/sorare-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sorare-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://sorare.com/.well-known/security.txt
- group: design
  href: https://artifacts.apis.io/sorare/asyncapi/sorare-graphql-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/sorare-graphql-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/sorare/lifecycle/sorare-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sorare-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/sorare/conformance/sorare-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sorare-conformance.yml
- group: agent
  href: https://artifacts.apis.io/sorare/mcp/sorare-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/sorare-mcp.yml
- group: agent
  href: https://artifacts.apis.io/sorare/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/sorare/llms/sorare-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sorare-llms.txt
created: '2026-07-17'
description: Sorare is a global fantasy sports platform for football (soccer), NBA basketball and MLB baseball built on blockchain-based digital collectible player cards stored on Ethereum and a StarkWare rollup. Its public developer surface is a single GraphQL API at https://api.sorare.com/graphql covering cards, users, auctions, offers and real-time subscriptions. The API supports JWT authentication (via the signIn mutation, with TOTP 2FA), OAuth 2.0 (Authorization Code and Client Credentials), and optional API keys for elevated rate limits, plus StarkWare payload signing for on-chain trading actions.
image: https://sorare.com/favicon.ico
layout: provider
modified: '2026-10-06'
name: Sorare
nav: Providers
network: true
overview: 'Sorare is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cryptocurrency, GraphQL, Fantasy Sports, and NFT.


  The Sorare catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Sorare''s developer surface includes engineering blog, documentation, API reference, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 4
rate_limits:
- limit_count: 4
  name: Sorare Rate Limits
  slug: sorare-rate-limits
scopes:
- name: Sorare Scopes
  scope_count: 1
  slug: sorare-scopes
  summary_line: 1 scope · authorizationCode/clientCredentials
score:
  band: developing
  composite: 40.7
  coverage:
    artifact_dirs: 17
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 21.1
    contract_governance: 4.5
    contract_quality: 39.0
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 47.4
  previous_composite: 40.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/sorare/sorare-2026-08-17T082004.png
security:
- kind: authentication
  name: Sorare Authentication
  slug: sorare-authentication
  summary_line: http/oauth2/apiKey · 3 schemes
- kind: vulnerability-disclosure
  name: Sorare Vulnerability Disclosure
  slug: sorare-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 2
skills:
- name: Bid on an auction or make an offer for a Sorare card
  slug: sorare-buy-a-card
- name: Sign in to the Sorare API and query your account
  slug: sorare-sign-in
slug: sorare
tags:
- Company
- Cryptocurrency
- GraphQL
- Fantasy Sports
- NFT
- Blockchain
- Gaming
- Sports
- Web3
website: https://sorare.com
---

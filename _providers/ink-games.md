---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.9
  scored_at: '2026-09-03'
api_count: 1
apis:
- description: The GraphQL contract served by INK Games' Strapi headless CMS, which supplies the content rendered on www.inkgames.com. Schema introspection is enabled and unauthenticated, so the complete type system
  name: INK Games Web Content GraphQL API
  slug: ink-games-web-content-graphql
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ink-games-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.inkgames.com/
- group: operate
  title: ''
  type: Support
  url: https://www.inkgames.com/support/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.inkgames.com/sign-up
- group: start
  title: ''
  type: Login
  url: https://dashboard.inkgames.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.inkgames.com/terms-and-conditions/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.inkgames.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Ink-Games
- group: docs
  title: ''
  type: GraphQL
  url: graphql/ink-games-graphql.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ink-games-authentication.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/ink-games-data-model.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/ink-games-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/ink-games-conventions.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/ink-games-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/ink-games-lifecycle.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/ink-games-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ink-games-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/ink-games-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/ink-games-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/ink-games-llms.txt
created: '2026-08-23'
description: 'INK Games is an Austin, Texas gaming company building a free-to-earn mobile gaming and social platform under the banner "Play. Win. Earn." Its flagship title is Prize Kingdoms, a mobile kingdom-building game distributed through the Apple App Store and Google Play in which players compete and earn real cash prizes. Two platform services sit behind the games: Ink ID, the single account and passkey-based authentication layer, and InkPay, the payments and earnings system that pays players and influencers ongoing royalties tied to the reach of their personal INK referral code. The team is drawn from EA, Zynga, SciPlay and Buffalo Studios. INK Games operates no public developer program — it publishes no developer portal, API reference, SDK or specification, and its shares trade only on private secondary markets.'
image: https://www.inkgames.com/favicon.ico
layout: provider
mcp_servers:
- description: MCP posture for INK Games. No MCP server exists — not hosted, not packaged, not announced. No candidate tool list is derived because there is no reachable operation to derive one from.
  name: INK Games MCP Server
  slug: ink-games-mcp-server
modified: '2026-08-23'
name: INK Games
nav: Providers
network: true
overview: 'INK Games publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Games, Gaming, Mobile Games, and Entertainment.


  INK Games'' developer surface includes support, signup flow, authentication, and 17 more developer resources.'
plans:
- name: Ink Games Plans Pricing
  plan_count: 0
  slug: ink-games-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Ink Games Rate Limits
  slug: ink-games-rate-limits
score:
  band: emerging
  composite: 19.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 4.5
    contract_quality: 37.2
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 4.5
    operational_transparency: 2.6
  previous_composite: 19.8
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
security:
- kind: authentication
  name: Ink Games Authentication
  slug: ink-games-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Ink Games Domain Security
  slug: ink-games-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ink-games
tags:
- Company
- Games
- Gaming
- Mobile Games
- Entertainment
- Consumer
- Rewards
- Payments
- Loyalty
- Referral
- GraphQL
- Content Management
website: https://www.inkgames.com/
---

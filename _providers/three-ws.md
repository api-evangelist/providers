---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: three.ws API for 3D AI agents.
  name: three.ws API
  slug: main-api
artifact_total: 8
common:
- group: operate
  href: https://artifacts.apis.io/three-ws/rate-limits/three-ws-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/three-ws-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/three-ws/plans/three-ws-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/three-ws-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/three-ws/components/three-ws-components.yml
  title: ''
  type: Components
  url: components/three-ws-components.yml
- group: build
  href: https://artifacts.apis.io/three-ws/cli/three-ws-cli.yml
  title: ''
  type: CLI
  url: cli/three-ws-cli.yml
- group: operate
  href: https://artifacts.apis.io/three-ws/changelog/three-ws-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/three-ws-changelog.yml
- group: auth
  href: https://artifacts.apis.io/three-ws/security/three-ws-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/three-ws-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/three-ws/authentication/three-ws-authentication.yml
  title: ''
  type: Authentication
  url: authentication/three-ws-authentication.yml
- group: design
  href: https://artifacts.apis.io/three-ws/conformance/three-ws-conformance.yml
  title: ''
  type: Conformance
  url: conformance/three-ws-conformance.yml
- group: agent
  href: https://artifacts.apis.io/three-ws/llms/three-ws-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/three-ws-llms.txt
- group: other
  href: https://artifacts.apis.io/three-ws/a2a/three-ws-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/three-ws-a2a.yml
- group: agent
  href: https://artifacts.apis.io/three-ws/mcp/three-ws-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/three-ws-mcp.yml
- group: auth
  href: https://artifacts.apis.io/three-ws/well-known/three-ws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/three-ws-security.txt
- group: agent
  href: https://artifacts.apis.io/three-ws/well-known/three-ws-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/three-ws-well-known.yml
- group: other
  href: https://artifacts.apis.io/three-ws/hosts/three-ws-hosts.yml
  title: ''
  type: Hosts
  url: hosts/three-ws-hosts.yml
- group: build
  href: https://artifacts.apis.io/three-ws/packages/three-ws-packages.yml
  title: ''
  type: SDKs
  url: packages/three-ws-packages.yml
- group: build
  href: https://artifacts.apis.io/three-ws/packages/three-ws-packages.yml
  title: ''
  type: Packages
  url: packages/three-ws-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://three.ws/legal/tos
- group: operate
  title: ''
  type: StatusPage
  url: https://three.ws/status
- group: start
  title: ''
  type: Sandbox
  url: https://three.ws/playground
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://three.ws/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://three.ws/news
- group: start
  title: ''
  type: Login
  url: https://three.ws/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://three.ws/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://three.ws/changelog
- group: auth
  href: https://artifacts.apis.io/three-ws/security/three-ws-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/three-ws-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/three-ws/security/three-ws-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/three-ws-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://three.ws/
- group: docs
  title: ''
  type: Documentation
  url: https://three.ws/docs
- group: docs
  title: ''
  type: APIReference
  url: https://three.ws/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://three.ws/docs
- group: operate
  title: ''
  type: Support
  url: https://three.ws/support
- group: company
  title: ''
  type: Blog
  url: https://three.ws/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nirholas/three.ws
- group: commercial
  title: ''
  type: Pricing
  url: https://three.ws/pricing
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://three.ws/openapi.json
  - status: 401
    url: https://three.ws/api/mcp
  - status: 200
    url: https://three.ws/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: 'three.ws is the AI-agent layer for the open web: build, embed, monetize, and trade autonomous agents with real 3D avatars, on-chain identity (ERC-8004), pay-per-call (x402), and pump.fun token launches. It provides a living map of 3D AI agents, allowing creation from selfies, 3D model forging from prompts, and embedding anywhere via a single HTML tag. The platform integrates blockchain identity and payment, offering a marketplace for agents and wallets.'
image: https://three.ws/og-image.png
layout: provider
mcp_servers:
- description: Remote MCP server at three.ws requiring OAuth.
  name: three-ws MCP Server
  slug: three-ws-mcp-yml
modified: '2026-10-29'
name: three-ws
nav: Providers
network: true
overview: 'three-ws is listed with 1 API on the [APIs.io](https://apis.io/) network: three.ws API. Tagged areas include Company, Artificial Intelligence, 3D, Agents, and Web3.


  three-ws'' developer surface includes CLI, changelog, authentication, sandbox, documentation, API reference, getting-started guide, and 27 more developer resources.'
plans:
- name: Three Ws Plans Pricing
  plan_count: 3
  slug: three-ws-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 3
  name: Three Ws Rate Limits
  slug: three-ws-rate-limits
scopes:
- name: Three Ws Scopes
  scope_count: 0
  slug: three-ws-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.8
  facets:
    access_clarity: 53.9
    contract_governance: 4.5
    contract_quality: 24.0
    developer_ergonomics: 52.4
    discoverability: 75.8
    operational_transparency: 60.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 58.8
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 33.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/three-ws/three-ws-2026-11-03T144714.png
security:
- kind: authentication
  name: Three Ws Authentication
  slug: three-ws-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Three Ws Domain Security
  slug: three-ws-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
- kind: vulnerability-disclosure
  name: Three Ws Vulnerability Disclosure
  slug: three-ws-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: three-ws
tags:
- Company
- Artificial Intelligence
- 3D
- Agents
- Web3
website: https://three.ws/
---

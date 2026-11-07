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
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.3
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: REST API for public Twitter/X data with X-API-Key auth, JSON responses, and 76 documented endpoints across users, tweets, posting, interactions, lists, profiles, communities, Spaces, search, auth, X C
  name: TweetAPI tw-v2 REST API
  slug: tweetapi-tw-v2-rest-api
- description: Hosted remote HTTP MCP server providing current TweetAPI docs and read-only live public-data tools. Uses OAuth via dashboard authorization (tweetapi:read); does not expose posting, engagement, account
  name: TweetAPI Hosted MCP Server
  slug: tweetapi-hosted-mcp-server
artifact_total: 12
common:
- group: other
  href: https://artifacts.apis.io/tweetapi/hosts/tweetapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tweetapi-hosts.yml
- group: other
  href: https://artifacts.apis.io/tweetapi/vendors/tweetapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tweetapi-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://tweetapi.com/
- group: auth
  href: https://artifacts.apis.io/tweetapi/security/tweetapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tweetapi-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://tweetapi.com/docs
- group: docs
  title: ''
  type: Documentation
  url: https://tweetapi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tweetapi.com/ai-docs-v2.txt
- group: start
  title: ''
  type: GettingStarted
  url: https://tweetapi.com/docs/getting-started/overview
- group: company
  title: ''
  type: Blog
  url: https://tweetapi.com/blog
- group: operate
  title: ''
  type: Support
  url: https://t.me/tweetapi
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tweetapi
- group: commercial
  title: ''
  type: Pricing
  url: https://tweetapi.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://tweetapi.com/auth/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tweetapi.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tweetapi.com/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://tweetapi.com/status
- group: auth
  title: ''
  type: Security
  url: https://github.com/tweetapi/agent-skill/blob/main/SECURITY.md
- group: commercial
  href: https://artifacts.apis.io/tweetapi/plans/tweetapi-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tweetapi-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tweetapi/rate-limits/tweetapi-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tweetapi-rate-limits.yml
- group: build
  href: https://artifacts.apis.io/tweetapi/packages/tweetapi-packages.yml
  title: ''
  type: Packages
  url: packages/tweetapi-packages.yml
- group: build
  href: https://artifacts.apis.io/tweetapi/packages/tweetapi-packages.yml
  title: ''
  type: SDKs
  url: packages/tweetapi-packages.yml
- group: agent
  href: https://artifacts.apis.io/tweetapi/well-known/tweetapi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tweetapi-well-known.yml
- group: agent
  href: https://artifacts.apis.io/tweetapi/llms/tweetapi-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/tweetapi-llms.txt
- group: agent
  href: https://artifacts.apis.io/tweetapi/mcp/tweetapi-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tweetapi-mcp.yml
- group: agent
  href: https://artifacts.apis.io/tweetapi/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://artifacts.apis.io/tweetapi/authentication/tweetapi-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tweetapi-authentication.yml
- group: auth
  href: https://artifacts.apis.io/tweetapi/scopes/tweetapi-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/tweetapi-scopes.yml
- group: design
  href: https://artifacts.apis.io/tweetapi/conventions/tweetapi-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tweetapi-conventions.yml
- group: design
  href: https://artifacts.apis.io/tweetapi/errors/tweetapi-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/tweetapi-problem-types.yml
- group: design
  href: https://artifacts.apis.io/tweetapi/data-model/tweetapi-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tweetapi-data-model.yml
- group: design
  href: https://artifacts.apis.io/tweetapi/lifecycle/tweetapi-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/tweetapi-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/tweetapi/conformance/tweetapi-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tweetapi-conformance.yml
- group: auth
  href: https://artifacts.apis.io/tweetapi/security/tweetapi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/tweetapi-vulnerability-disclosure.yml
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://mcp.tweetapi.com/mcp
  reason: partner-login
  state: gated
created: '2026-08-10'
description: Independent third-party REST API for public Twitter/X data, built for developers, researchers, startups, agencies, and analytics teams. Offers user profiles, tweets, search, lists, communities, Spaces, posting/engagement, and DMs, plus a hosted MCP server and llms.txt for agent access. Not affiliated with X Corp.
finops:
- has_sources: true
  method: derived
  name: Tweetapi Finops
  primary_unit: ''
  service_category: ''
  slug: tweetapi-finops
  template: true
image: https://tweetapi.com/api/og?type=landing
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.tweetapi.com over HTTP.
  name: TweetAPI MCP Server
  slug: tweetapi
modified: '2026-08-11'
name: TweetAPI
nav: Providers
network: true
overview: 'TweetAPI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Twitter, X, Social Media, Social Data, and Search.


  TweetAPI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 26 more developer resources.'
plans:
- name: Tweetapi Plans Pricing
  plan_count: 4
  slug: tweetapi-plans-pricing
- name: Tweetapi Price Estimates
  plan_count: 0
  slug: tweetapi-price-estimates
random_paper: 3
rate_limits:
- limit_count: 4
  name: Tweetapi Rate Limits
  slug: tweetapi-rate-limits
scopes:
- name: Tweetapi Scopes
  scope_count: 2
  slug: tweetapi-scopes
  summary_line: 2 scopes · authorizationCode
score:
  band: developing
  composite: 50.9
  coverage:
    artifact_dirs: 23
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.0
    operational_transparency: 60.5
  previous_composite: 50.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
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
screenshot: https://apis.io/screenshots/tweetapi/tweetapi-2026-08-17T082504.png
security:
- kind: authentication
  name: Tweetapi Authentication
  slug: tweetapi-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Tweetapi Domain Security
  slug: tweetapi-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Tweetapi Vulnerability Disclosure
  slug: tweetapi-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: tweetapi
  slug: tweetapi-read-only-twitter-data
slug: tweetapi
tags:
- Twitter
- X
- Social Media
- Social Data
- Search
- Analytics
- Research
- Developer Tools
- MCP
- Agent-Native
- Llms.txt
- REST API
website: https://tweetapi.com/
---

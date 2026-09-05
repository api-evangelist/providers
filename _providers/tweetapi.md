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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: REST API for public Twitter/X data with X-API-Key auth, JSON responses, and 76 documented endpoints across users, tweets, posting, interactions, lists, profiles, communities, Spaces, search, auth, X C
  name: TweetAPI tw-v2 REST API
  slug: tweetapi-tw-v2-rest-api
- description: Hosted remote HTTP MCP server providing current TweetAPI docs and read-only live public-data tools. Uses OAuth via dashboard authorization (tweetapi:read); does not expose posting, engagement, account
  name: TweetAPI Hosted MCP Server
  slug: tweetapi-hosted-mcp-server
artifact_total: 10
common:
- group: auth
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
  title: ''
  type: Plans
  url: plans/tweetapi-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/tweetapi-rate-limits.yml
- group: build
  title: ''
  type: Packages
  url: packages/tweetapi-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/tweetapi-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/tweetapi-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/tweetapi-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/tweetapi-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tweetapi-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/tweetapi-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/tweetapi-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/tweetapi-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/tweetapi-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/tweetapi-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/tweetapi-conformance.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/tweetapi-vulnerability-disclosure.yml
created: '2026-08-10'
description: Independent third-party REST API for public Twitter/X data, built for developers, researchers, startups, agencies, and analytics teams. Offers user profiles, tweets, search, lists, communities, Spaces, posting/engagement, and DMs, plus a hosted MCP server and llms.txt for agent access. Not affiliated with X Corp.
image: https://tweetapi.com/api/og?type=landing
layout: provider
mcp_servers:
- description: ''
  name: TweetAPI MCP Server
  slug: tweetapi-mcp-server
- description: ''
  name: MCP server manifest
  slug: mcp-server-manifest
modified: '2026-08-11'
name: TweetAPI
nav: Providers
network: true
overview: 'TweetAPI publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include twitter, X, Social-Media, Social Data, and Search.


  TweetAPI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 23 more developer resources.'
plans:
- name: Tweetapi Plans Pricing
  plan_count: 4
  slug: tweetapi-plans-pricing
random_paper: 6
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
  composite: 47.2
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 71.4
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 60.5
  previous_composite: 47.2
  provenance:
    conformance: first-party
    mcp: first-party
    skills: first-party
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tweetapi/refs/heads/main/screenshots/tweetapi-2026-08-17T082504.png
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
slug: tweetapi
tags:
- twitter
- X
- Social-Media
- Social Data
- Search
- Analytics
- Research
- Developer Tools
- MCP
- agent-native
- llms-txt
- REST API
website: https://tweetapi.com/docs
---

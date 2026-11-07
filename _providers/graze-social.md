---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 8.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Graze Social API for building custom feeds on Bluesky.
  name: Graze API
  slug: graze-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/graze-social/rate-limits/graze-social-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/graze-social-rate-limits.yml
- group: auth
  href: https://artifacts.apis.io/graze-social/authentication/graze-social-authentication.yml
  title: ''
  type: Authentication
  url: authentication/graze-social-authentication.yml
- group: design
  href: https://artifacts.apis.io/graze-social/conformance/graze-social-conformance.yml
  title: ''
  type: Conformance
  url: conformance/graze-social-conformance.yml
- group: agent
  href: https://artifacts.apis.io/graze-social/mcp/graze-social-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/graze-social-mcp.yml
- group: other
  href: https://artifacts.apis.io/graze-social/hosts/graze-social-hosts.yml
  title: ''
  type: Hosts
  url: hosts/graze-social-hosts.yml
- group: other
  href: https://artifacts.apis.io/graze-social/vendors/graze-social-vendors.yml
  title: ''
  type: Vendors
  url: vendors/graze-social-vendors.yml
- group: build
  href: https://artifacts.apis.io/graze-social/packages/graze-social-packages.yml
  title: ''
  type: SDKs
  url: packages/graze-social-packages.yml
- group: build
  href: https://artifacts.apis.io/graze-social/packages/graze-social-packages.yml
  title: ''
  type: Packages
  url: packages/graze-social-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.graze.social/
- group: start
  title: ''
  type: Login
  url: https://www.graze.social/login
- group: auth
  href: https://artifacts.apis.io/graze-social/security/graze-social-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/graze-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://graze.social
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.graze.social/developers
- group: docs
  title: ''
  type: Documentation
  url: https://www.graze.social/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.graze.social/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://www.graze.social/docs/creating-your-first-feed
- group: operate
  title: ''
  type: Support
  url: https://www.graze.social/docs
- group: company
  title: ''
  type: Blog
  url: https://www.graze.social/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/graze-social
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.graze.social/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.graze.social/privacy-policy
coverage:
  checked: '2026-10-29'
  detail: MCP tools/list endpoint requires authentication, preventing contract discovery.
  evidence:
  - status: 406
    url: https://help.graze.social/mcp/v1
  reason: partner-login
  state: gated
created: '2026-10-29'
description: 'Graze Social is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by true-ventures) and added to the network as a stub for full-pipeline profiling.'
image: https://www.graze.social/index.png
layout: provider
mcp_servers:
- description: Remote MCP server at help.graze.social.
  name: Graze Social MCP Server
  slug: graze-social-mcp-yml
modified: '2026-10-29'
name: Graze Social
nav: Providers
network: true
overview: 'Graze Social is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social, FeedBuilder, Bluesky, and Software-as-a-Service.


  Graze Social''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, and 15 more developer resources.'
random_paper: 17
rate_limits:
- limit_count: 2
  name: Graze Social Rate Limits
  slug: graze-social-rate-limits
scopes:
- name: Graze Social Scopes
  scope_count: 0
  slug: graze-social-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 20
    catalog_earned: 30.0
    catalog_earned_first_party: 8.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 17.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 41.7
    discoverability: 43.3
    operational_transparency: 31.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 35.4
  provenance:
    conformance: first-party
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/graze-social/graze-social-2026-11-03T133035.png
security:
- kind: authentication
  name: Graze Social Authentication
  slug: graze-social-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Graze Social Domain Security
  slug: graze-social-domain-security
  summary_line: TLSv1.3 · HSTS
slug: graze-social
tags:
- Social
- FeedBuilder
- Bluesky
- Software-as-a-Service
website: https://graze.social
---

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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
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
    openapi_examples: documented
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.8
  scored_at: '2026-09-04'
api_count: 1
apis:
- description: 'Archive''s public GraphQL API for programmatic access to creator and UGC workspace data — creators, social profiles, items (posts/reels/stories/videos), engagement history, content views, collections, '
  name: Archive API
  slug: archive-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/archive-technologies-domain-security.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.archive.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.archive.com
- group: docs
  title: ''
  type: APIReference
  url: https://app.archive.com/api/v2/docs
- group: operate
  title: ''
  type: Support
  url: https://help.archive.com/en/
- group: company
  title: ''
  type: Blog
  url: https://archive.com/blog
- group: start
  title: ''
  type: Login
  url: https://app.archive.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://archive.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://archive.com/legal/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://archive.instatus.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://feedback.archive.com/changelog
- group: agent
  title: ''
  type: MCPServer
  url: mcp/archive-technologies-mcp.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/archive-technologies-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/archive-technologies-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/archive-technologies-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/archive-technologies-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/archive-technologies-rate-limits.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/archive-technologies-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/archive-technologies-changelog.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/archive-technologies-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/archive-technologies-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/archive-technologies-data-model.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/archive-technologies-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.archive.com/getting-started
- group: operate
  title: ''
  type: Roadmap
  url: https://api-docs.archive.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://archive.com/pricing
- group: commercial
  title: ''
  type: Plans
  url: plans/archive-technologies-plans-pricing.yml
- group: build
  title: ''
  type: Examples
  url: examples/archive-technologies-graphql-examples.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/archive-technologies-tool-crosswalk.yml
- group: docs
  title: ''
  type: GraphQL
  url: graphql/archive-technologies.graphql
created: '2026-07-17'
description: Archive (Archive Technologies, Inc.) is an AI-powered creator and community marketing platform for e-commerce brands, founded in 2021 and headquartered in Miami, FL. Archive automates social listening across TikTok, Instagram, and YouTube, creator discovery, UGC rights and repurposing, campaign tracking, and reporting. Its public developer surface is the Archive API — a GraphQL API at POST https://app.archive.com/api/v2 that gives teams programmatic access to workspace data (creators, social profiles, UGC items, engagement history, content views, collections, campaigns, and competitor brands) authenticated with a workspace-scoped bearer token plus a WORKSPACE-ID header. The schema is published as a full reference (53 operations — 29 queries and 24 mutations — over 135 types) even though runtime introspection is disabled. Archive also operates an OAuth-protected remote MCP server at https://app.archive.com/api/v2/mcp whose 53 tools map 1:1 to those GraphQL operations, and both
  surfaces draw on the same per-workspace credit budget alongside a flat 5 requests/second ceiling, signalled at runtime with IETF ratelimit headers. Archive is backed by Battery Ventures among others.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archive-technologies.png
layout: provider
mcp_servers:
- description: Archive operates an official hosted remote MCP server at https://app.archive.com/api/v2/mcp, discoverable via RFC 9728 protected-resource metadata (well-known/archive-technologies-oauth-protected-reso
  name: Archive Technologies MCP Server
  slug: archive-technologies-mcp-server
modified: '2026-08-13'
name: Archive Technologies
nav: Providers
network: true
overview: 'Archive Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Marketing, Influencer Marketing, Social Listening, and User Generated Content.


  Archive Technologies'' developer surface includes documentation, API reference, support, engineering blog, changelog, authentication, getting-started guide, and 24 more developer resources.'
plans:
- name: Archive Technologies Plans Pricing
  plan_count: 5
  slug: archive-technologies-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Archive Technologies Rate Limits
  slug: archive-technologies-rate-limits
scopes:
- name: Archive Technologies Scopes
  scope_count: 1
  slug: archive-technologies-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 51.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 57.0
    catalog_earned_first_party: 20.0
    catalog_gap: 58.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 4.5
    contract_quality: 46.8
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 4.5
    operational_transparency: 42.1
  previous_composite: 51.0
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/archive-technologies/refs/heads/main/screenshots/archive-technologies-2026-07-25T201038.png
security:
- kind: authentication
  name: Archive Technologies Authentication
  slug: archive-technologies-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Archive Technologies Domain Security
  slug: archive-technologies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: archive-technologies
tags:
- Company
- Creator Marketing
- Influencer Marketing
- Social Listening
- User Generated Content
- E-Commerce
- GraphQL
- MCP
website: https://api-docs.archive.com
---

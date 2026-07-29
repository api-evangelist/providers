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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: true
  schema_version: 0.2
  score: 31.3
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: 'Archive''s public GraphQL API for programmatic access to creator and UGC workspace data — creators, social profiles, items (posts/reels/stories/videos), engagement history, content views, collections, '
  name: Archive API
  slug: archive-api
artifact_total: 6
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
created: '2026-07-17'
description: Archive (Archive Technologies, Inc.) is an AI-powered creator and community marketing platform for e-commerce brands, founded in 2021 and headquartered in Miami, FL. Archive automates social listening across TikTok, Instagram, and YouTube, creator discovery, UGC rights and repurposing, campaign tracking, and reporting. Its public developer surface is the Archive API — a GraphQL API at POST https://app.archive.com/api/v2 that gives teams programmatic access to workspace data (creators, social profiles, UGC items, engagement history, content views, collections, campaigns, and competitor brands) authenticated with a workspace-scoped bearer token plus a WORKSPACE-ID header. Archive also operates an OAuth-protected remote MCP server at https://app.archive.com/api/v2/mcp for AI agents. Archive is backed by Battery Ventures among others.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/archive-technologies.png
layout: provider
mcp_servers:
- description: ''
  name: archive-technologies-mcp.yml
  slug: archive-technologies-mcpyml
modified: '2026-07-18'
name: Archive Technologies
nav: Providers
network: true
overview: 'Archive Technologies publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Creator Marketing, Influencer Marketing, Social Listening, and User Generated Content.


  Archive Technologies'' developer surface includes documentation, API reference, support, engineering blog, changelog, authentication, and 18 more developer resources.'
random_paper: 67
rate_limits:
- limit_count: 1
  name: Archive Technologies Rate Limits
  slug: archive-technologies-rate-limits
scopes:
- name: Archive Technologies Scopes
  scope_count: 1
  slug: archive-technologies-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: thin
  composite: 33.1
  delta: -1.1
  facets:
    commercial_clarity: 34.2
    contract_quality: 0.0
    developer_ergonomics: 51.6
    discoverability: 87.0
    governance: 3.1
    operational_transparency: 52.6
  previous_composite: 34.2
  provenance:
    conformance: derived
    mcp: first-party
    skills: derived
  schema_version: 0.6
  scored_at: '2026-07-28'
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
- E-commerce
- GraphQL
- MCP
website: https://api-docs.archive.com
---

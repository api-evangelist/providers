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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 41.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Publer Agentic Access
  operation_count: 21
  slug: publer-agentic-access
  summary_line: 21 operations · 6 acting
api_count: 8
apis:
- description: The Accounts API from Publer — 1 operation for listing the social media accounts (Facebook, Instagram, X/Twitter, LinkedIn, TikTok, YouTube, Pinterest, Threads, Bluesky, Mastodon, Google Business, Wor
  name: Publer Accounts API
  slug: publer-accounts-api
- description: 'The Analytics API from Publer — 7 operations for social analytics: available charts and chart data, per-post insights, hashtag insights and top hashtag posts, best times to post as a day/hour heatmap,'
  name: Publer Analytics API
  slug: publer-analytics-api
- description: The Competitors API from Publer — 2 operations for listing the competitor accounts tracked against one of your social accounts and comparing followers, engagement, reach and posting mix against them.
  name: Publer Competitors API
  slug: publer-competitors-api
- description: The Jobs API from Publer — 1 operation for resolving the asynchronous job returned by every write on the Publer API. Scheduling, publishing and media-from-URL uploads all return 202 with a job_id; thi
  name: Publer Jobs API
  slug: publer-jobs-api
- description: 'The Media API from Publer — 3 operations for the workspace media library: list and filter photos, videos and GIFs by type, usage, source and search term, upload a file directly as multipart, or upload'
  name: Publer Media API
  slug: publer-media-api
- description: 'The Posts API from Publer — 5 operations covering the content lifecycle: list posts with state, date, account, member and full-text filters, schedule a bulk payload of per-network content, publish imm'
  name: Publer Posts API
  slug: publer-posts-api
- description: The Users API from Publer — 1 operation returning the profile of the currently authenticated user (id, email, name and picture), used to adapt an integration to the user identity behind an API key.
  name: Publer Users API
  slug: publer-users-api
- description: The Workspaces API from Publer — 1 operation listing every workspace the authenticated user can reach, with owner, members, plan and picture. The workspace id it returns is required as the Publer-Work
  name: Publer Workspaces API
  slug: publer-workspaces-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Publer Accounts API
  slug: open-publer-accounts-api
- collection_type: open
  name: Publer Analytics API
  slug: open-publer-analytics-api
- collection_type: open
  name: Publer Competitors API
  slug: open-publer-competitors-api
- collection_type: open
  name: Publer Jobs API
  slug: open-publer-jobs-api
- collection_type: open
  name: Publer Media API
  slug: open-publer-media-api
- collection_type: open
  name: Publer Posts API
  slug: open-publer-posts-api
- collection_type: open
  name: Publer Users API
  slug: open-publer-users-api
- collection_type: open
  name: Publer Workspaces API
  slug: open-publer-workspaces-api
- collection_type: open
  name: Publer API
  slug: open-publer
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/publer-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/publer-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/publer-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Publer
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/publer
- group: company
  title: ''
  type: Website
  url: https://publer.com/
- group: docs
  title: ''
  type: Documentation
  url: https://publer.com/docs
- group: commercial
  title: ''
  type: Plans
  url: plans/publer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/publer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/publer-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://publer.com/blog/feed/
- group: agent
  title: ''
  type: MCPServer
  url: mcp/publer-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/publer-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/publer-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/publer-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/publer-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/publer-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/publer-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.publer.com
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/publer-scopes.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/publer-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/publer-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://publer.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://publer.com/docs/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://publer.com/docs/getting-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://publer.com/help
- group: operate
  title: ''
  type: HelpCenter
  url: https://publer.com/help
- group: operate
  title: ''
  type: Roadmap
  url: https://publer.com/roadmap
- group: commercial
  title: ''
  type: Pricing
  url: https://publer.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://publer.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://publer.com/privacy
created: '2026-06-25'
description: 'Publer is a social-media scheduling and management platform for planning, creating, publishing and analyzing content across Facebook, Instagram, X/Twitter, LinkedIn, TikTok, YouTube, Pinterest, Threads, Bluesky, Mastodon, Google Business Profiles, WordPress and Telegram. The Publer API (v1) is a RESTful JSON interface at https://app.publer.com/api/v1 covering 21 operations: schedule and publish posts, update and delete them, manage connected social accounts and workspaces, upload and list media, resolve asynchronous jobs, and read analytics including post insights, hashtag performance, best times to post and competitor comparison. Authentication is an API key sent as Authorization: Bearer-API with a Publer-Workspace-Id header, scoped per key. Publer also ships a first-party hosted MCP server in beta. API access is limited to Enterprise plan users, Business plan users in good standing, and Top Ambassadors.'
finops:
- name: Publer Finops
  service_category: Management and Governance
  slug: publer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/publer.png
layout: provider
mcp_servers:
- description: ''
  name: publer-mcp.yml
  slug: publer-mcpyml
modified: '2026-08-13'
name: Publer
nav: Providers
network: true
overview: 'Publer publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, Competitors API, and 5 more. Tagged areas include Social Media, Scheduling, Publishing, Content Management, and Marketing.


  Publer''s developer surface includes authentication, documentation, engineering blog, API reference, getting-started guide, support, pricing, and 25 more developer resources.'
plans:
- name: Publer Plans Pricing
  plan_count: 4
  slug: publer-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 18
  name: Publer Rate Limits
  slug: publer-rate-limits
scopes:
- name: Publer Scopes
  scope_count: 0
  slug: publer-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 43.5
  delta: -18.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 16.7
    contract_quality: 59.3
    developer_ergonomics: 20.8
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 50.0
  previous_composite: 61.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: first-party
    skills: derived
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/publer/refs/heads/main/screenshots/publer-2026-08-17T081403.png
security:
- kind: authentication
  name: Publer Authentication
  slug: publer-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Publer Domain Security
  slug: publer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: publer
tags:
- Social Media
- Scheduling
- Publishing
- Content Management
- Marketing
- Social Media Management
- Analytics
- Agents
- MCP
- Automation
website: https://publer.com/
---

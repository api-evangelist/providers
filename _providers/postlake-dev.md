---
access_model:
  confidence: medium
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
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Postlake Dev Agentic Access
  operation_count: 102
  slug: postlake-dev-agentic-access
  summary_line: 102 operations · 48 acting
api_count: 1
apis:
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: API key identity, permissions, usage and account info
  name: postlake-dev Account API
  slug: postlake-dev-account-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Per-post and cross-platform metrics
  name: postlake-dev Analytics API
  slug: postlake-dev-analytics-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: The Channels API from postlake-dev — 10 operation(s) for channels.
  name: postlake-dev Channels API
  slug: postlake-dev-channels-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Hosted connect/manage page links
  name: postlake-dev Connect API
  slug: postlake-dev-connect-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: BYO platform app credentials (BYOK)
  name: postlake-dev Credentials API
  slug: postlake-dev-credentials-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: The Discovery API from postlake-dev — 5 operation(s) for discovery.
  name: postlake-dev Discovery API
  slug: postlake-dev-discovery-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Like, repost, follow, block and mute
  name: postlake-dev Engaging API
  slug: postlake-dev-engaging-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Create and manage Facebook Page live broadcasts
  name: postlake-dev Live Video API
  slug: postlake-dev-live-video-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Model Context Protocol JSON-RPC endpoint
  name: postlake-dev MCP API
  slug: postlake-dev-mcp-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Upload media for posts
  name: postlake-dev Media API
  slug: postlake-dev-media-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Direct message threads
  name: postlake-dev Messages API
  slug: postlake-dev-messages-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: The Openapi.json API from postlake-dev — 1 operation(s) for openapi.json.
  name: postlake-dev Openapi.json API
  slug: postlake-dev-openapi-json-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: The Platform API from postlake-dev — 1 operation(s) for platform.
  name: postlake-dev Platform API
  slug: postlake-dev-platform-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Machine-readable platform capabilities (public)
  name: postlake-dev Platforms API
  slug: postlake-dev-platforms-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Create, list, edit, cancel, schedule posts
  name: postlake-dev Posts API
  slug: postlake-dev-posts-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Named groupings of social accounts
  name: postlake-dev Profiles API
  slug: postlake-dev-profiles-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Notifications, comments and followers, normalised across networks
  name: postlake-dev Reading API
  slug: postlake-dev-reading-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Connect, list, disconnect social accounts
  name: postlake-dev Social Accounts API
  slug: postlake-dev-social-accounts-api
- baseURL: https://api.postlake.dev
  baseurl_source: declared
  description: Register and manage webhook endpoints
  name: postlake-dev Webhooks API
  slug: postlake-dev-webhooks-api
artifact_total: 32
common:
- group: agent
  href: https://artifacts.apis.io/postlake-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/postlake-dev/agentic-access/postlake-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/postlake-dev-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/postlake-dev/plans/postlake-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/postlake-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/rules/postlake-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/postlake-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/json-ld/postlake-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/postlake-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/postlake-dev/vocabulary/postlake-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/postlake-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/data-model/postlake-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/postlake-dev-data-model.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/conventions/postlake-dev-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/postlake-dev-conventions.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/conventions/postlake-dev-conventions.yml
  title: ''
  type: Conventions
  url: conventions/postlake-dev-conventions.yml
- group: auth
  href: https://artifacts.apis.io/postlake-dev/authentication/postlake-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/postlake-dev-authentication.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/errors/postlake-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/postlake-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/postlake-dev/conformance/postlake-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/postlake-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/postlake-dev/llms/postlake-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/postlake-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/postlake-dev/mcp/postlake-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/postlake-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/postlake-dev/well-known/postlake-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/postlake-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/postlake-dev/hosts/postlake-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/postlake-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/postlake-dev/vendors/postlake-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/postlake-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://postlake.dev/status
- group: operate
  title: ''
  type: ChangeLog
  url: https://postlake.dev/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://postlake.dev/llms.txt
- group: auth
  href: https://artifacts.apis.io/postlake-dev/security/postlake-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/postlake-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://postlake.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postlake.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.postlake.dev/quickstart
- group: operate
  title: ''
  type: Support
  url: https://postlake.dev/support
- group: company
  title: ''
  type: Blog
  url: https://postlake.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/postlake
- group: commercial
  title: ''
  type: Pricing
  url: https://postlake.dev/pricing
- group: start
  title: ''
  type: SignUp
  url: https://postlake.dev/signup
- group: start
  title: ''
  type: Login
  url: https://postlake.dev/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://postlake.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://postlake.dev/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://postlake.dev/openapi.json
  - status: null
    url: https://docs.postlake.dev/openapi.json
  - status: null
    url: https://api.postlake.dev/openapi.json
  - status: 401
    url: https://api.postlake.dev/mcp
  - status: 401
    url: https://api.postlake.dev/v1/graphql
  - status: 200
    url: https://postlake.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: 'PostLake is the social media API and infrastructure for AI agents. It provides a unified REST API and hosted MCP server that lets agents publish, schedule, engage, and measure across nine major social networks through a single interface. Developers can obtain an API key, use bearer token authentication, and leverage features such as idempotent publishing, draft approvals, analytics, and secure credential management. The platform offers a free tier, usage‑based pricing, and enterprise plans, with detailed documentation, pricing, support, and a public OpenAPI specification at https://api.postlake.dev/openapi.json. image: https://postlake.dev/og-image.png?v=2'
image: https://postlake.dev/og-image.png?v=2
json_schemas:
- name: DiscoveredPost
  property_count: 10
  slug: postlake-dev-discovered-post
- name: MediaAsset
  property_count: 9
  slug: postlake-dev-media-asset
- name: Metrics
  property_count: 11
  slug: postlake-dev-metrics
- name: PlatformCapabilities
  property_count: 24
  slug: postlake-dev-platform-capabilities
- name: Post
  property_count: 18
  slug: postlake-dev-post
- name: SocialAccount
  property_count: 10
  slug: postlake-dev-social-account
jsonld:
- class_count: 30
  name: Postlake Dev Context
  property_count: 130
  slug: postlake-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.postlake.dev.
  name: postlake-dev MCP Server
  slug: postlake-dev-mcp-yml
modified: '2026-10-31'
name: postlake-dev
nav: Providers
network: true
overview: 'postlake-dev publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Analytics API, Channels API, and 16 more. Tagged areas include Company, Social Media, AI Agents, MCP, and Software-as-a-Service.


  The postlake-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  postlake-dev''s developer surface includes authentication, changelog, API reference, documentation, getting-started guide, support, engineering blog, and 25 more developer resources.'
plans:
- name: Postlake Dev Plans Pricing
  plan_count: 4
  slug: postlake-dev-plans-pricing
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: postlake-dev API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 2
  slug: postlake-dev-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.0
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 61.5
    developer_ergonomics: 36.2
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 56.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/postlake-dev/postlake-dev-2026-11-03T141420.png
security:
- kind: authentication
  name: Postlake Dev Authentication
  slug: postlake-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Postlake Dev Domain Security
  slug: postlake-dev-domain-security
  summary_line: TLSv1.3 · HSTS
slug: postlake-dev
tags:
- Company
- Social Media
- AI Agents
- MCP
- Software-as-a-Service
- Automation
- Publishing
website: https://postlake.dev/
---

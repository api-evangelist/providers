---
access_model:
  confidence: high
  label: Pay-per-usage credits · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 54.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 86
  human_in_the_loop: 4
  name: X Agentic Access
  operation_count: 190
  slug: x-agentic-access
  summary_line: 190 operations · 86 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: Endpoints relating to retrieving, managing Account Activity subscriptions — 5 operation(s) in the X-published contract.
  name: X Account Activity API
  slug: x-account-activity-api
- description: Endpoints for managing the authenticated user's X Developer Platform account — 2 operation(s) in the X-published contract.
  name: X Account API
  slug: x-account-api
- description: Endpoints relating to retrieving, managing activity subscriptions — 5 operation(s) in the X-published contract.
  name: X Activity API
  slug: x-activity-api
- description: Endpoints related to retrieving, creating & modifying Articles — 2 operation(s) in the X-published contract.
  name: X Articles API
  slug: x-articles-api
- description: The Bots surface of the X API v2. — 6 operation(s) in the X-published contract.
  name: X Bots API
  slug: x-bots-api
- description: Endpoints related to live broadcasts and their chat — 13 operation(s) in the X-published contract.
  name: X Broadcasts API
  slug: x-broadcasts-api
- description: Endpoints related to Chat encrypted messaging — 16 operation(s) in the X-published contract.
  name: X Chat API
  slug: x-chat-api
- description: Endpoints related to retrieving and managing Communities — 2 operation(s) in the X-published contract.
  name: X Communities API
  slug: x-communities-api
- description: Endpoints related to retrieving, searching, and modifying Community Notes — 5 operation(s) in the X-published contract.
  name: X Community Notes API
  slug: x-community-notes-api
- description: Endpoints related to keeping X data in your systems compliant — 6 operation(s) in the X-published contract.
  name: X Compliance API
  slug: x-compliance-api
- description: Endpoints related to streaming connections — 4 operation(s) in the X-published contract.
  name: X Connections API
  slug: x-connections-api
- description: Endpoints related to retrieving, managing Direct Messages — 9 operation(s) in the X-published contract.
  name: X Direct Messages API
  slug: x-direct-messages-api
- description: Miscellaneous endpoints for general API functionality — 1 operation(s) in the X-published contract.
  name: X General API
  slug: x-general-api
- description: Endpoints related to retrieving, managing Lists — 9 operation(s) in the X-published contract.
  name: X Lists API
  slug: x-lists-api
- description: Endpoints related to retrieving and uploading Media — 11 operation(s) in the X-published contract.
  name: X Media API
  slug: x-media-api
- description: Endpoint for retrieving news stories — 2 operation(s) in the X-published contract.
  name: X News API
  slug: x-news-api
- description: Endpoints related to retrieving, searching, and modifying Posts — 14 operation(s) in the X-published contract.
  name: X Posts API
  slug: x-posts-api
- description: Endpoints related to retrieving, managing Spaces — 6 operation(s) in the X-published contract.
  name: X Spaces API
  slug: x-spaces-api
- description: Endpoints related to streaming — 18 operation(s) in the X-published contract.
  name: X Stream API
  slug: x-stream-api
- description: Endpoint for retrieving trends — 2 operation(s) in the X-published contract.
  name: X Trends API
  slug: x-trends-api
- description: Endpoints related to retrieving usage — 2 operation(s) in the X-published contract.
  name: X Usage API
  slug: x-usage-api
- description: Endpoints related to retrieving, managing relationships of Users — 42 operation(s) in the X-published contract.
  name: X Users API
  slug: x-users-api
- description: Endpoints relating to retrieving, managing webhooks and webhook configs — 8 operation(s) in the X-published contract.
  name: X Webhooks API
  slug: x-webhooks-api
artifact_total: 38
asyncapis:
- description: ''
  name: X Webhooks
  slug: x-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: X API v2 Posts API
  slug: open-x-posts-api
- collection_type: open
  name: X API v2 Posts Trends API
  slug: open-x-trends-api
- collection_type: open
  name: X API v2 Posts Users API
  slug: open-x-users-api
- collection_type: open
  name: X API v2
  slug: open-x
common:
- group: agent
  title: ''
  type: AgentSkill
  url: skills/x-x-skill.md
- group: company
  title: ''
  type: Website
  url: https://x.com/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/x-api-v2-openapi.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/x-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/x-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/x-agentic-access.yml
- group: build
  title: ''
  type: Packages
  url: packages/x-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/x-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/x-cli.yml
- group: design
  title: ''
  type: Components
  url: components/x-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/x-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/x-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/x-tool-crosswalk.yml
- group: other
  title: ''
  type: AgentCard
  url: a2a/x-a2a.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/x-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/x-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/x-security.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/x-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/x-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/x-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/x-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/x-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/x-webhooks.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/x-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/x-changelog.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/x-api-v2-overlay.yaml
- group: commercial
  title: ''
  type: Plans
  url: plans/x-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/x-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/x-finops.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/x-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/x-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: security/x-vulnerability-disclosure.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.x.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.x.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.x.com/x-api/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.x.com/x-api/getting-started/make-your-first-request
- group: operate
  title: ''
  type: Support
  url: https://devcommunity.x.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/xdevplatform
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.x.com/x-api/getting-started/pricing
- group: start
  title: ''
  type: SignUp
  url: https://console.x.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.x.com/en/developer-terms/agreement-and-policy
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://x.com/en/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.x.com/status
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.x.com/x-api/fundamentals/versioning
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/xapidevelopers/x-api-public-workspace/collection/34902927-2efc5689-99c6-4ab6-8091-996f35c2fd80
created: '2025-08-14'
description: X (formerly Twitter) operates the X Developer Platform, the programmable interface to the public conversation on X. The X API v2 is a 190-operation REST surface covering Posts, Users, Direct Messages, the encrypted Chat API, Lists, Spaces, Media, Communities, Community Notes, Broadcasts, News, Trends, Articles and Bots, plus a substantial real-time layer — filtered stream, firehose and sample volume streams, compliance streams, Account Activity webhooks and the X Activity API. X publishes a machine-readable OpenAPI at api.x.com/2/openapi.json, an llms.txt family, an AGENTS.md, an agentskills.io skill, an A2A agent card and two hosted MCP servers. Access is sold pay-per-usage in prepaid credits rather than by subscription tier, with an Enterprise agreement for volume above the published cap.
finops:
- name: X Finops
  service_category: API
  slug: x-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/x.png
layout: provider
mcp_servers:
- description: 'X ships TWO hosted MCP servers: an API server at https://api.x.com/mcp that calls X API v2 endpoints, and a documentation-search server at https://docs.x.com/mcp. Both are Streamable HTTP remote endpo'
  name: X MCP Server
  slug: x-mcp-server
modified: '2026-08-28'
name: X
nav: Providers
network: true
overview: 'X publishes 23 APIs on the [APIs.io](https://apis.io/) network, including Account Activity API, Account API, Activity API, and 20 more. Tagged areas include Social, Social-Media, Posts, User, and Direct Messages.


  The X catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  X''s developer surface includes authentication, CLI, sandbox, changelog, documentation, API reference, getting-started guide, and 39 more developer resources.'
plans:
- name: X Plans Pricing
  plan_count: 2
  slug: x-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 17
  name: X Rate Limits
  slug: x-rate-limits
scopes:
- name: X Scopes
  scope_count: 29
  slug: x-scopes
  summary_line: 29 scopes
score:
  band: strong
  composite: 64.3
  coverage:
    artifact_dirs: 27
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 16.0
  facets:
    access_clarity: 73.7
    commercial_clarity: 73.7
    contract_governance: 18.2
    contract_quality: 60.5
    developer_ergonomics: 73.8
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 76.3
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 23
    mcp: first-party
    skills: first-party
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/x/refs/heads/main/screenshots/x-2026-06-20T201653.png
security:
- kind: authentication
  name: X Authentication
  slug: x-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: X Domain Security
  slug: x-domain-security
  summary_line: HSTS
- kind: vulnerability-disclosure
  name: X Vulnerability Disclosure
  slug: x-vulnerability-disclosure
  summary_line: Hackerone
slug: x
tags:
- Social
- Social-Media
- Posts
- User
- Direct Messages
- Streaming
- Webhook
- Real-Time
- Trends
- Media
- Spaces
- Content
- Conversation
- Agents
- MCP
website: https://x.com/
---

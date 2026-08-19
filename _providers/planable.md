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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 51.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 25
  human_in_the_loop: 3
  name: Planable Agentic Access
  operation_count: 51
  slug: planable-agentic-access
  summary_line: 51 operations · 25 acting · 3 human-in-the-loop
api_count: 12
apis:
- description: The Campaigns API from Planable — 5 operation(s). Create, read, update and delete campaigns — named groupings of posts inside a workspace.
  name: Planable Campaigns API
  slug: planable-campaigns-api
- description: The Competitors API from Planable — 6 operation(s). Track up to five competitor social pages per page and pull comparison tables, follower/engagement trends and competitor top posts. Requires the Anal
  name: Planable Competitors API
  slug: planable-competitors-api
- description: The Labels API from Planable — 2 operation(s). List and create the color-coded labels used to organize posts by topic, format or event within a workspace.
  name: Planable Labels API
  slug: planable-labels-api
- description: The Media API from Planable — 3 operation(s). List the workspace media library, upload assets from a public URL (up to 100MB per file) and read an asset’s type, dimensions and processing status.
  name: Planable Media API
  slug: planable-media-api
- description: The Members API from Planable — 1 operation(s). List workspace members with their roles and approval-level assignments.
  name: Planable Members API
  slug: planable-members-api
- description: The Pages API from Planable — 4 operation(s). List the social channels connected to a workspace, pull per-page analytics, and trigger and poll a metrics sync from the source platforms.
  name: Planable Pages API
  slug: planable-pages-api
- description: 'The Posts API from Planable — 18 operation(s). The core content surface — list, create, read, update and delete posts, create synced cross-platform group posts, manage comments and reactions, request '
  name: Planable Posts API
  slug: planable-posts-api
- description: The Social Listening API from Planable — 7 operation(s). Track brand and topic keywords for a workspace, then read matched mentions, daily metrics, aggregated summaries and sync status.
  name: Planable Social Listening API
  slug: planable-social-listening-api
- description: The Stories API from Planable — 1 operation(s). Create single-frame or multi-frame Instagram and Facebook stories.
  name: Planable Stories API
  slug: planable-stories-api
- description: The System API from Planable — 1 operation(s). Health check for the Planable Public API.
  name: Planable System API
  slug: planable-system-api
- description: The Workspaces API from Planable — 3 operation(s). List, create and delete the workspaces that scope every other resource in the API.
  name: Planable Workspaces API
  slug: planable-workspaces-api
- description: Planable’s official remote Model Context Protocol server at https://mcp.planable.io/mcp. An OAuth 2.0 protected resource (authorization code + PKCE, dynamic client registration, six scopes) that gives
  name: Planable MCP Server
  slug: planable-mcp
artifact_total: 181
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Planable Public Campaigns API
  slug: open-planable-campaigns-api
- collection_type: open
  name: Planable Public Campaigns Labels API
  slug: open-planable-labels-api
- collection_type: open
  name: Planable Public Campaigns Media API
  slug: open-planable-media-api
- collection_type: open
  name: Planable Public Campaigns Pages API
  slug: open-planable-pages-api
- collection_type: open
  name: Planable Public Campaigns Posts API
  slug: open-planable-posts-api
- collection_type: open
  name: Planable Public Campaigns Stories API
  slug: open-planable-stories-api
- collection_type: open
  name: Planable Public Campaigns System API
  slug: open-planable-system-api
- collection_type: open
  name: Planable Public Campaigns Workspaces API
  slug: open-planable-workspaces-api
common:
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/planable-openapi.json
- group: agent
  title: ''
  type: MCPServer
  url: mcp/planable-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/planable-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planable-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/planable-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/planable-conventions.yml
- group: design
  title: ''
  type: Idempotency
  url: conventions/planable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/planable-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planable-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/planable-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/planable-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/planable-lifecycle.yml
- group: build
  title: ''
  type: Packages
  url: packages/planable-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/planable-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/planable-llms.txt
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/planable-changelog.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/planable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planable-domain-security.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/planable-vocabulary.json
- group: design
  title: ''
  type: Rules
  url: rules/planable-jsonschema-spectral-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/planable-jsonld.json
- group: commercial
  title: ''
  type: Plans
  url: plans/planable-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/planable-finops.yml
- group: company
  title: ''
  type: Website
  url: https://planable.io/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://planable.io/guides/planable-public-api/
- group: docs
  title: ''
  type: Documentation
  url: https://help.planable.io/hc/en-us/
- group: docs
  title: ''
  type: APIReference
  url: https://api.planable.io/api/v1/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://planable.io/guides/planable-public-api/
- group: operate
  title: ''
  type: Support
  url: https://help.planable.io/hc/en-us/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Planable
- group: company
  title: ''
  type: Blog
  url: https://planable.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://planable.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.planable.io/signup
- group: start
  title: ''
  type: Login
  url: https://app.planable.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://planable.io/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://planable.io/privacy/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.planable.io/
- group: other
  title: ''
  type: AIInstructions
  url: https://planable.io/ai-instructions/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planableapp/about/
- group: other
  title: ''
  type: X
  url: https://x.com/planableapp
created: '2026-06-13'
description: 'Planable is a collaboration-first social media management platform used by agencies, multi-location brands, multi-brand companies and in-house marketing teams to create, plan, collaborate on, approve, schedule, publish and analyze content across Facebook, Instagram, X (Twitter), LinkedIn, TikTok, YouTube, Pinterest, Threads and Google Business Profile. It exposes three programmable surfaces: a REST Public API v1 at https://api.planable.io/api/v1 with 51 operations over workspaces, pages, posts, comments, campaigns, labels, media, members, stories, competitor analytics and social listening; a remote OAuth-protected MCP server at https://mcp.planable.io/mcp for Claude, ChatGPT and Gemini; and twelve MIT-licensed Agent Skills published as a Claude Code plugin. Agent- and API-created content always lands as a draft and passes through Planable''s normal approval workflow.'
finops:
- name: Planable Finops
  service_category: ''
  slug: planable-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/planable.png
json_schemas:
- name: Delete_Campaigns_{Id} Response 401
  property_count: 0
  slug: delete_campaigns_{id}-response-401
- name: Delete_Campaigns_{Id} Response 429
  property_count: 0
  slug: delete_campaigns_{id}-response-429
- name: Delete_Campaigns_{Id} Response 500
  property_count: 0
  slug: delete_campaigns_{id}-response-500
- name: Delete_Posts_{Id} Response 401
  property_count: 0
  slug: delete_posts_{id}-response-401
- name: Delete_Posts_{Id} Response 429
  property_count: 0
  slug: delete_posts_{id}-response-429
- name: Delete_Posts_{Id} Response 500
  property_count: 0
  slug: delete_posts_{id}-response-500
- name: Delete_Workspaces_{Id} Response 401
  property_count: 0
  slug: delete_workspaces_{id}-response-401
- name: Delete_Workspaces_{Id} Response 429
  property_count: 0
  slug: delete_workspaces_{id}-response-429
- name: Delete_Workspaces_{Id} Response 500
  property_count: 0
  slug: delete_workspaces_{id}-response-500
- name: Get_Campaigns Response 200
  property_count: 2
  slug: get_campaigns-response-200
- name: Get_Campaigns Response 401
  property_count: 0
  slug: get_campaigns-response-401
- name: Get_Campaigns Response 403
  property_count: 0
  slug: get_campaigns-response-403
- name: Get_Campaigns Response 429
  property_count: 0
  slug: get_campaigns-response-429
- name: Get_Campaigns Response 500
  property_count: 0
  slug: get_campaigns-response-500
- name: Get_Campaigns_{Id} Response 200
  property_count: 1
  slug: get_campaigns_{id}-response-200
- name: Get_Campaigns_{Id} Response 401
  property_count: 0
  slug: get_campaigns_{id}-response-401
- name: Get_Campaigns_{Id} Response 403
  property_count: 0
  slug: get_campaigns_{id}-response-403
- name: Get_Campaigns_{Id} Response 429
  property_count: 0
  slug: get_campaigns_{id}-response-429
- name: Get_Campaigns_{Id} Response 500
  property_count: 0
  slug: get_campaigns_{id}-response-500
- name: Get_Labels Response 200
  property_count: 1
  slug: get_labels-response-200
- name: Get_Labels Response 401
  property_count: 0
  slug: get_labels-response-401
- name: Get_Labels Response 403
  property_count: 0
  slug: get_labels-response-403
- name: Get_Labels Response 429
  property_count: 0
  slug: get_labels-response-429
- name: Get_Labels Response 500
  property_count: 0
  slug: get_labels-response-500
- name: Get_Media Response 200
  property_count: 2
  slug: get_media-response-200
- name: Get_Media Response 401
  property_count: 0
  slug: get_media-response-401
- name: Get_Media Response 403
  property_count: 0
  slug: get_media-response-403
- name: Get_Media Response 429
  property_count: 0
  slug: get_media-response-429
- name: Get_Media Response 500
  property_count: 0
  slug: get_media-response-500
- name: Get_Media_{Id} Response 200
  property_count: 1
  slug: get_media_{id}-response-200
- name: Get_Media_{Id} Response 401
  property_count: 0
  slug: get_media_{id}-response-401
- name: Get_Media_{Id} Response 403
  property_count: 0
  slug: get_media_{id}-response-403
- name: Get_Media_{Id} Response 429
  property_count: 0
  slug: get_media_{id}-response-429
- name: Get_Media_{Id} Response 500
  property_count: 0
  slug: get_media_{id}-response-500
- name: Get_Pages Response 200
  property_count: 2
  slug: get_pages-response-200
- name: Get_Pages Response 401
  property_count: 0
  slug: get_pages-response-401
- name: Get_Pages Response 403
  property_count: 0
  slug: get_pages-response-403
- name: Get_Pages Response 429
  property_count: 0
  slug: get_pages-response-429
- name: Get_Pages Response 500
  property_count: 0
  slug: get_pages-response-500
- name: Get_Pages_{Id}_Metrics Response 200
  property_count: 2
  slug: get_pages_{id}_metrics-response-200
- name: Get_Pages_{Id}_Metrics Response 401
  property_count: 0
  slug: get_pages_{id}_metrics-response-401
- name: Get_Pages_{Id}_Metrics Response 429
  property_count: 0
  slug: get_pages_{id}_metrics-response-429
- name: Get_Pages_{Id}_Metrics Response 500
  property_count: 0
  slug: get_pages_{id}_metrics-response-500
- name: Get_Pages_{Id}_Sync Status Response 200
  property_count: 1
  slug: get_pages_{id}_sync-status-response-200
- name: Get_Pages_{Id}_Sync Status Response 401
  property_count: 0
  slug: get_pages_{id}_sync-status-response-401
- name: Get_Pages_{Id}_Sync Status Response 429
  property_count: 0
  slug: get_pages_{id}_sync-status-response-429
- name: Get_Pages_{Id}_Sync Status Response 500
  property_count: 0
  slug: get_pages_{id}_sync-status-response-500
- name: Get_Ping Response 200
  property_count: 3
  slug: get_ping-response-200
- name: Get_Ping Response 401
  property_count: 0
  slug: get_ping-response-401
- name: Get_Ping Response 403
  property_count: 0
  slug: get_ping-response-403
- name: Get_Ping Response 429
  property_count: 0
  slug: get_ping-response-429
- name: Get_Ping Response 500
  property_count: 0
  slug: get_ping-response-500
- name: Get_Posts Response 200
  property_count: 2
  slug: get_posts-response-200
- name: Get_Posts Response 401
  property_count: 0
  slug: get_posts-response-401
- name: Get_Posts Response 403
  property_count: 0
  slug: get_posts-response-403
- name: Get_Posts Response 429
  property_count: 0
  slug: get_posts-response-429
- name: Get_Posts Response 500
  property_count: 0
  slug: get_posts-response-500
- name: Get_Posts_Count Response 200
  property_count: 1
  slug: get_posts_count-response-200
- name: Get_Posts_Count Response 401
  property_count: 0
  slug: get_posts_count-response-401
- name: Get_Posts_Count Response 403
  property_count: 0
  slug: get_posts_count-response-403
- name: Get_Posts_Count Response 429
  property_count: 0
  slug: get_posts_count-response-429
- name: Get_Posts_Count Response 500
  property_count: 0
  slug: get_posts_count-response-500
- name: Get_Posts_{Id} Response 200
  property_count: 1
  slug: get_posts_{id}-response-200
- name: Get_Posts_{Id} Response 401
  property_count: 0
  slug: get_posts_{id}-response-401
- name: Get_Posts_{Id} Response 403
  property_count: 0
  slug: get_posts_{id}-response-403
- name: Get_Posts_{Id} Response 429
  property_count: 0
  slug: get_posts_{id}-response-429
- name: Get_Posts_{Id} Response 500
  property_count: 0
  slug: get_posts_{id}-response-500
- name: Get_Posts_{Id}_Comments Response 200
  property_count: 2
  slug: get_posts_{id}_comments-response-200
- name: Get_Posts_{Id}_Comments Response 401
  property_count: 0
  slug: get_posts_{id}_comments-response-401
- name: Get_Posts_{Id}_Comments Response 403
  property_count: 0
  slug: get_posts_{id}_comments-response-403
- name: Get_Posts_{Id}_Comments Response 429
  property_count: 0
  slug: get_posts_{id}_comments-response-429
- name: Get_Posts_{Id}_Comments Response 500
  property_count: 0
  slug: get_posts_{id}_comments-response-500
- name: Get_Posts_{Id}_Metrics Response 200
  property_count: 1
  slug: get_posts_{id}_metrics-response-200
- name: Get_Posts_{Id}_Metrics Response 401
  property_count: 0
  slug: get_posts_{id}_metrics-response-401
- name: Get_Posts_{Id}_Metrics Response 403
  property_count: 0
  slug: get_posts_{id}_metrics-response-403
- name: Get_Posts_{Id}_Metrics Response 429
  property_count: 0
  slug: get_posts_{id}_metrics-response-429
- name: Get_Posts_{Id}_Metrics Response 500
  property_count: 0
  slug: get_posts_{id}_metrics-response-500
- name: Get_Posts_{Id}_Sync Status Response 200
  property_count: 1
  slug: get_posts_{id}_sync-status-response-200
- name: Get_Posts_{Id}_Sync Status Response 401
  property_count: 0
  slug: get_posts_{id}_sync-status-response-401
- name: Get_Posts_{Id}_Sync Status Response 429
  property_count: 0
  slug: get_posts_{id}_sync-status-response-429
- name: Get_Posts_{Id}_Sync Status Response 500
  property_count: 0
  slug: get_posts_{id}_sync-status-response-500
- name: Get_Workspaces Response 200
  property_count: 1
  slug: get_workspaces-response-200
- name: Get_Workspaces Response 401
  property_count: 0
  slug: get_workspaces-response-401
- name: Get_Workspaces Response 403
  property_count: 0
  slug: get_workspaces-response-403
- name: Get_Workspaces Response 429
  property_count: 0
  slug: get_workspaces-response-429
- name: Get_Workspaces Response 500
  property_count: 0
  slug: get_workspaces-response-500
- name: Patch_Campaigns_{Id} Request
  property_count: 8
  slug: patch_campaigns_{id}-request
- name: Patch_Campaigns_{Id} Response 200
  property_count: 1
  slug: patch_campaigns_{id}-response-200
- name: Patch_Campaigns_{Id} Response 401
  property_count: 0
  slug: patch_campaigns_{id}-response-401
- name: Patch_Campaigns_{Id} Response 429
  property_count: 0
  slug: patch_campaigns_{id}-response-429
- name: Patch_Campaigns_{Id} Response 500
  property_count: 0
  slug: patch_campaigns_{id}-response-500
- name: Patch_Posts_Reorder Request
  property_count: 2
  slug: patch_posts_reorder-request
- name: Patch_Posts_Reorder Response 200
  property_count: 1
  slug: patch_posts_reorder-response-200
- name: Patch_Posts_Reorder Response 401
  property_count: 0
  slug: patch_posts_reorder-response-401
- name: Patch_Posts_Reorder Response 403
  property_count: 0
  slug: patch_posts_reorder-response-403
- name: Patch_Posts_Reorder Response 429
  property_count: 0
  slug: patch_posts_reorder-response-429
- name: Patch_Posts_Reorder Response 500
  property_count: 0
  slug: patch_posts_reorder-response-500
- name: Patch_Posts_{Id} Request
  property_count: 13
  slug: patch_posts_{id}-request
- name: Patch_Posts_{Id} Response 200
  property_count: 1
  slug: patch_posts_{id}-response-200
- name: Patch_Posts_{Id} Response 401
  property_count: 0
  slug: patch_posts_{id}-response-401
- name: Patch_Posts_{Id} Response 403
  property_count: 0
  slug: patch_posts_{id}-response-403
- name: Patch_Posts_{Id} Response 429
  property_count: 0
  slug: patch_posts_{id}-response-429
- name: Patch_Posts_{Id} Response 500
  property_count: 0
  slug: patch_posts_{id}-response-500
- name: Post_Campaigns Request
  property_count: 9
  slug: post_campaigns-request
- name: Post_Campaigns Response 201
  property_count: 1
  slug: post_campaigns-response-201
- name: Post_Campaigns Response 401
  property_count: 0
  slug: post_campaigns-response-401
- name: Post_Campaigns Response 429
  property_count: 0
  slug: post_campaigns-response-429
- name: Post_Campaigns Response 500
  property_count: 0
  slug: post_campaigns-response-500
- name: Post_Labels Request
  property_count: 3
  slug: post_labels-request
- name: Post_Labels Response 201
  property_count: 1
  slug: post_labels-response-201
- name: Post_Labels Response 401
  property_count: 0
  slug: post_labels-response-401
- name: Post_Labels Response 403
  property_count: 0
  slug: post_labels-response-403
- name: Post_Labels Response 429
  property_count: 0
  slug: post_labels-response-429
- name: Post_Labels Response 500
  property_count: 0
  slug: post_labels-response-500
- name: Post_Media Request
  property_count: 2
  slug: post_media-request
- name: Post_Media Response 202
  property_count: 1
  slug: post_media-response-202
- name: Post_Media Response 401
  property_count: 0
  slug: post_media-response-401
- name: Post_Media Response 403
  property_count: 0
  slug: post_media-response-403
- name: Post_Media Response 429
  property_count: 0
  slug: post_media-response-429
- name: Post_Media Response 500
  property_count: 0
  slug: post_media-response-500
- name: Post_Pages_{Id}_Sync Response 200
  property_count: 1
  slug: post_pages_{id}_sync-response-200
- name: Post_Pages_{Id}_Sync Response 401
  property_count: 0
  slug: post_pages_{id}_sync-response-401
- name: Post_Pages_{Id}_Sync Response 429
  property_count: 0
  slug: post_pages_{id}_sync-response-429
- name: Post_Pages_{Id}_Sync Response 500
  property_count: 0
  slug: post_pages_{id}_sync-response-500
- name: Post_Posts Request
  property_count: 20
  slug: post_posts-request
- name: Post_Posts Response 201
  property_count: 1
  slug: post_posts-response-201
- name: Post_Posts Response 401
  property_count: 0
  slug: post_posts-response-401
- name: Post_Posts Response 403
  property_count: 0
  slug: post_posts-response-403
- name: Post_Posts Response 429
  property_count: 0
  slug: post_posts-response-429
- name: Post_Posts Response 500
  property_count: 0
  slug: post_posts-response-500
- name: Post_Posts_{Id}_Comments Request
  property_count: 2
  slug: post_posts_{id}_comments-request
- name: Post_Posts_{Id}_Comments Response 201
  property_count: 1
  slug: post_posts_{id}_comments-response-201
- name: Post_Posts_{Id}_Comments Response 401
  property_count: 0
  slug: post_posts_{id}_comments-response-401
- name: Post_Posts_{Id}_Comments Response 403
  property_count: 0
  slug: post_posts_{id}_comments-response-403
- name: Post_Posts_{Id}_Comments Response 429
  property_count: 0
  slug: post_posts_{id}_comments-response-429
- name: Post_Posts_{Id}_Comments Response 500
  property_count: 0
  slug: post_posts_{id}_comments-response-500
- name: Post_Posts_{Id}_Sync Response 200
  property_count: 1
  slug: post_posts_{id}_sync-response-200
- name: Post_Posts_{Id}_Sync Response 401
  property_count: 0
  slug: post_posts_{id}_sync-response-401
- name: Post_Posts_{Id}_Sync Response 429
  property_count: 0
  slug: post_posts_{id}_sync-response-429
- name: Post_Posts_{Id}_Sync Response 500
  property_count: 0
  slug: post_posts_{id}_sync-response-500
- name: Post_Stories Request
  property_count: 12
  slug: post_stories-request
- name: Post_Stories Response 201
  property_count: 1
  slug: post_stories-response-201
- name: Post_Stories Response 401
  property_count: 0
  slug: post_stories-response-401
- name: Post_Stories Response 403
  property_count: 0
  slug: post_stories-response-403
- name: Post_Stories Response 429
  property_count: 0
  slug: post_stories-response-429
- name: Post_Stories Response 500
  property_count: 0
  slug: post_stories-response-500
- name: Post_Workspaces Request
  property_count: 4
  slug: post_workspaces-request
- name: Post_Workspaces Response 201
  property_count: 1
  slug: post_workspaces-response-201
- name: Post_Workspaces Response 401
  property_count: 0
  slug: post_workspaces-response-401
- name: Post_Workspaces Response 429
  property_count: 0
  slug: post_workspaces-response-429
- name: Post_Workspaces Response 500
  property_count: 0
  slug: post_workspaces-response-500
layout: provider
mcp_servers:
- description: ''
  name: planable-mcp.yml
  slug: planable-mcpyml
modified: '2026-08-13'
name: Planable
nav: Providers
network: true
overview: 'Planable publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Competitors API, Labels API, and 8 more. Tagged areas include Social Media, Content Collaboration, Approval Workflows, Social Media Management, and Content Publishing.


  The Planable catalog on APIs.io includes 1 Spectral governance ruleset.


  Planable''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 35 more developer resources.'
plans:
- name: Planable Plans Pricing
  plan_count: 4
  slug: planable-plans-pricing
random_paper: 86
rate_limits:
- limit_count: 2
  name: Planable Rate Limits
  slug: planable-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Planable API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: planable-jsonschema-spectral-rules
scopes:
- name: Planable Scopes
  scope_count: 0
  slug: planable-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 63.4
  delta: -8.6
  facets:
    access_clarity: 77.6
    commercial_clarity: 77.6
    contract_governance: 41.7
    contract_quality: 56.2
    developer_ergonomics: 61.9
    discoverability: 92.6
    governance: 41.7
    operational_transparency: 55.3
  previous_composite: 72.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: first-party
    skills: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/planable/refs/heads/main/screenshots/planable-2026-06-20T191751.png
security:
- kind: authentication
  name: Planable Authentication
  slug: planable-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Planable Domain Security
  slug: planable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: planable
tags:
- Social Media
- Content Collaboration
- Approval Workflows
- Social Media Management
- Content Publishing
- Marketing
- Social Media Analytics
- Social Listening
- MCP
- AI Agents
- Agent Skills
website: https://planable.io/
---

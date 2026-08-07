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
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Planable Agentic Access
  operation_count: 31
  slug: planable-agentic-access
  summary_line: 31 operations · 15 acting
api_count: 8
apis:
- description: The Campaigns API from Planable — 2 operation(s) for campaigns.
  name: Planable Campaigns API
  slug: planable-campaigns-api
- description: The Labels API from Planable — 1 operation(s) for labels.
  name: Planable Labels API
  slug: planable-labels-api
- description: The Media API from Planable — 2 operation(s) for media.
  name: Planable Media API
  slug: planable-media-api
- description: The Pages API from Planable — 4 operation(s) for pages.
  name: Planable Pages API
  slug: planable-pages-api
- description: The Posts API from Planable — 8 operation(s) for posts.
  name: Planable Posts API
  slug: planable-posts-api
- description: The Stories API from Planable — 1 operation(s) for stories.
  name: Planable Stories API
  slug: planable-stories-api
- description: The System API from Planable — 1 operation(s) for system.
  name: Planable System API
  slug: planable-system-api
- description: The Workspaces API from Planable — 2 operation(s) for workspaces.
  name: Planable Workspaces API
  slug: planable-workspaces-api
artifact_total: 166
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/planable-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/planable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/planable-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://planable.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.planable.io/hc/en-us/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Planable
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/planableapp/about/
- group: company
  title: ''
  type: Blog
  url: https://planable.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://planable.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.planable.io/
- group: other
  title: ''
  type: X
  url: https://x.com/planableapp
- group: commercial
  title: ''
  type: Plans
  url: plans/planable-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/planable-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/planable-finops.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://changelog.planable.io/
created: '2026-06-13'
description: Planable is a social media collaboration platform trusted by agencies, freelancers, and marketing teams to plan, create, collaborate, approve, and publish content across multiple social media channels. It provides a REST API for managing workspaces, pages, posts, feedback, approval workflows, and publishing to Facebook, Instagram, LinkedIn, X (Twitter), YouTube, TikTok, Pinterest, Google Business Profile, and Threads.
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
modified: '2026-06-13'
name: Planable
nav: Providers
network: true
overview: 'Planable publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Labels API, Media API, and 5 more. Tagged areas include Social Media, Content Collaboration, Approval Workflows, Social Media Management, and Content Publishing.


  The Planable catalog on APIs.io includes 1 Spectral governance ruleset.


  Planable''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, and 10 more developer resources.'
plans:
- name: Planable Plans Pricing
  plan_count: 4
  slug: planable-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 0
  name: Planable Rate Limits
  slug: planable-rate-limits
rules:
- name: Planable API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: planable-jsonschema-spectral-rules
score:
  band: developing
  composite: 48.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 58.9
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 48.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/planable/refs/heads/main/screenshots/planable-2026-06-20T191751.png
security:
- kind: authentication
  name: Planable Authentication
  slug: planable-authentication
  summary_line: http · 1 scheme
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
website: https://planable.io/
---

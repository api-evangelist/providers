---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 37.8
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Blotato Agentic Access
  operation_count: 10
  slug: blotato-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 2
apis:
- baseURL: https://backend.blotato.com/v2
  baseurl_source: declared
  description: User and connected social account lookup.
  name: Blotato Accounts API
  slug: blotato-accounts-api
- baseURL: https://backend.blotato.com/v2
  baseurl_source: declared
  description: Upload media for use in posts.
  name: Blotato Media API
  slug: blotato-media-api
- baseURL: https://backend.blotato.com/v2
  baseurl_source: declared
  description: Publish, schedule, and track posts.
  name: Blotato Posts API
  slug: blotato-posts-api
- baseURL: https://backend.blotato.com/v2
  baseurl_source: declared
  description: AI video and visual generation from templates.
  name: Blotato Visuals API
  slug: blotato-visuals-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to social media analytics for published posts.
  name: Blotato Analytics API
  slug: blotato-analytics-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to DM automations, which send a direct message in response to a comment or message on a connected social account.
  name: Blotato Automations API
  slug: blotato-automations-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to credits, credit balance, and credit purchases.
  name: Blotato Billing API
  slug: blotato-billing-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to reading and posting comments on social posts.
  name: Blotato Comments API
  slug: blotato-comments-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to reading and sending direct messages on connected social media accounts.
  name: Blotato Messaging API
  slug: blotato-messaging-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to publishing content, such as posts and drafts.
  name: Blotato Publishing API
  slug: blotato-publishing-api
- baseURL: https://backend.blotato.com
  baseurl_source: declared
  description: Endpoints related to video creation and management.
  name: Blotato Video API
  slug: blotato-video-api
artifact_total: 25
collections:
- collection_type: open
  name: Blotato Accounts API
  slug: open-blotato-accounts-api
- collection_type: open
  name: Blotato Accounts Media API
  slug: open-blotato-media-api
- collection_type: open
  name: Blotato Accounts Posts API
  slug: open-blotato-posts-api
- collection_type: open
  name: Blotato Accounts Visuals API
  slug: open-blotato-visuals-api
- collection_type: open
  name: Blotato API
  slug: open-blotato
common:
- group: commercial
  title: ''
  type: Pricing
  url: https://www.blotato.com/pricing
- group: other
  href: https://artifacts.apis.io/blotato/capabilities/blotato-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/blotato-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/blotato/agentic-access/blotato-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/blotato-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/blotato/security/blotato-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blotato-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/blotato/authentication/blotato-authentication.yml
  title: ''
  type: Authentication
  url: authentication/blotato-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Blotato-Inc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blotato
- group: company
  title: ''
  type: Website
  url: https://www.blotato.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.blotato.com/api/start
- group: commercial
  href: https://artifacts.apis.io/blotato/plans/blotato-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/blotato-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/blotato/rate-limits/blotato-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/blotato-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/blotato/finops/blotato-finops.yml
  title: ''
  type: FinOps
  url: finops/blotato-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.blotato.com/blog
created: '2026-06-25'
description: Blotato is an AI content-creation and social-media publishing platform. Its REST API lets automation and AI-agent builders upload media, publish posts to many platforms (TikTok, Instagram, YouTube, X/Twitter, LinkedIn, Facebook, Threads, Bluesky, Pinterest), generate AI videos and visuals from templates, and track publishing status, with an authenticated MCP server for AI agents.
finops:
- has_sources: true
  method: generated
  name: Blotato Finops
  primary_unit: ''
  service_category: Web and Application Services
  slug: blotato-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blotato.png
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.blotato.com over HTTP.
  name: Blotato MCP Server
  slug: blotato
modified: '2026-06-25'
name: Blotato
nav: Providers
network: true
overview: 'Blotato publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Media API, Posts API, and 8 more. Tagged areas include Social Media, Publishing, AI content, Automation, and Content Creation.


  The Blotato catalog on APIs.io includes 1 Spectral governance ruleset.


  Blotato''s developer surface includes pricing, authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Blotato Plans Pricing
  plan_count: 3
  slug: blotato-plans-pricing
- name: Blotato Price Estimates
  plan_count: 0
  slug: blotato-price-estimates
random_paper: 13
rate_limits:
- limit_count: 6
  name: Blotato Rate Limits
  slug: blotato-rate-limits
rules:
- authorship: generated
  effective_rule_count: 107
  extends:
  - spectral:oas
  name: Blotato API Rules
  rule_count: 66
  severity_counts:
    error: 57
    hint: 0
    info: 4
    warn: 5
  slug: blotato-rules
score:
  band: thin
  composite: 37.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 65.5
    catalog_earned_first_party: 24.0
    catalog_gap: 49.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 36.8
    contract_governance: 13.6
    contract_quality: 50.0
    developer_ergonomics: 31.0
    discoverability: 68.3
    operational_transparency: 34.2
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/blotato/blotato-2026-07-25T203418.png
security:
- kind: authentication
  name: Blotato Authentication
  slug: blotato-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blotato Domain Security
  slug: blotato-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blotato
tags:
- Social Media
- Publishing
- AI content
- Automation
- Content Creation
website: https://www.blotato.com/
---

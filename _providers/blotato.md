---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Blotato Agentic Access
  operation_count: 10
  slug: blotato-agentic-access
  summary_line: 10 operations · 3 acting
api_count: 4
apis:
- description: User and connected social account lookup.
  name: Blotato Accounts API
  slug: blotato-accounts-api
- description: Upload media for use in posts.
  name: Blotato Media API
  slug: blotato-media-api
- description: Publish, schedule, and track posts.
  name: Blotato Posts API
  slug: blotato-posts-api
- description: AI video and visual generation from templates.
  name: Blotato Visuals API
  slug: blotato-visuals-api
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blotato-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blotato-domain-security.yml
- group: auth
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
  title: ''
  type: Plans
  url: plans/blotato-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/blotato-rate-limits.yml
- group: commercial
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
- name: Blotato Finops
  service_category: Web and Application Services
  slug: blotato-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blotato.png
layout: provider
modified: '2026-06-25'
name: Blotato
nav: Providers
network: true
overview: 'Blotato publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Media API, Posts API, and 1 more. Tagged areas include Social Media, Publishing, AI Content, Automation, and Content Creation.


  Blotato''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Blotato Plans Pricing
  plan_count: 3
  slug: blotato-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 2
  name: Blotato Rate Limits
  slug: blotato-rate-limits
score:
  band: thin
  composite: 37.6
  delta: -0.8
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 57.9
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 38.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blotato/refs/heads/main/screenshots/blotato-2026-07-25T203418.png
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
- AI Content
- Automation
- Content Creation
website: https://www.blotato.com/
---

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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Upload Post Agentic Access
  operation_count: 15
  slug: upload-post-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 4
apis:
- description: Retrieve impressions and per-post performance metrics.
  name: Upload-Post Analytics API
  slug: upload-post-analytics-api
- description: Publish video, photo, and text content to social platforms.
  name: Upload-Post Upload API
  slug: upload-post-upload-api
- description: Check upload status and retrieve upload history.
  name: Upload-Post Upload Management API
  slug: upload-post-upload-management-api
- description: Manage user profiles and social account linking.
  name: Upload-Post Users API
  slug: upload-post-users-api
artifact_total: 11
collections:
- collection_type: open
  name: Upload-Post API
  slug: open-upload-post
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/upload-post-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/upload-post-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/upload-post-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Upload-Post
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/upload-post
- group: company
  title: ''
  type: Website
  url: https://www.upload-post.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.upload-post.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/upload-post-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/upload-post-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/upload-post-finops.yml
created: '2026-06-25'
description: Upload-Post is a universal social media publishing API that lets developers publish videos, photos, and text posts to TikTok, Instagram, YouTube, LinkedIn, Facebook, X (Twitter), Threads, Pinterest, Bluesky, Reddit, Discord, Telegram, and Google Business Profile through a single REST interface, with managed user profiles, OAuth account linking, scheduling, and cross-platform analytics.
finops:
- name: Upload Post Finops
  service_category: Web and Application Services
  slug: upload-post-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/upload-post.png
layout: provider
modified: '2026-06-25'
name: Upload-Post
nav: Providers
network: true
overview: 'Upload-Post publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Upload API, Upload Management API, and 1 more. Tagged areas include Social Media, Publishing, Video, Content, and Cross Posting.


  Upload-Post''s developer surface includes authentication, documentation, and 8 more developer resources.'
plans:
- name: Upload Post Plans Pricing
  plan_count: 2
  slug: upload-post-plans-pricing
random_paper: 24
rate_limits:
- limit_count: 4
  name: Upload Post Rate Limits
  slug: upload-post-rate-limits
score:
  band: thin
  composite: 36.9
  delta: -2.2
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.2
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Upload Post Authentication
  slug: upload-post-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Upload Post Domain Security
  slug: upload-post-domain-security
  summary_line: TLSv1.3 · DMARC
slug: upload-post
tags:
- Social Media
- Publishing
- Video
- Content
- Cross Posting
website: https://www.upload-post.com/
---

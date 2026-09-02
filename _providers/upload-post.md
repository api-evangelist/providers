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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Upload Post Agentic Access
  operation_count: 15
  slug: upload-post-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
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
artifact_total: 16
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Upload-Post Analytics API
  slug: open-upload-post-analytics-api
- collection_type: open
  name: Post Analytics Upload API
  slug: open-upload-post-upload-api
- collection_type: open
  name: Upload-Post Analytics Upload Management API
  slug: open-upload-post-upload-management-api
- collection_type: open
  name: Upload-Post Analytics Users API
  slug: open-upload-post-users-api
- collection_type: open
  name: Upload-Post API
  slug: open-upload-post
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/upload-post-capability-edges.yml
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
overview: 'Upload-Post publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Upload API, Upload Management API, and 1 more. Tagged areas include Social-Media, Publishing, Video, Content, and Cross Posting.


  Upload-Post''s developer surface includes authentication, documentation, and 9 more developer resources.'
plans:
- name: Upload Post Plans Pricing
  plan_count: 2
  slug: upload-post-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 4
  name: Upload Post Rate Limits
  slug: upload-post-rate-limits
score:
  band: thin
  composite: 37.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.9
    commercial_clarity: 28.9
    contract_governance: 0.0
    contract_quality: 56.8
    developer_ergonomics: 33.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.18.0
  scored_at: '2026-09-01'
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
- Social-Media
- Publishing
- Video
- Content
- Cross Posting
website: https://www.upload-post.com/
---

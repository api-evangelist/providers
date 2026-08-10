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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Publer Agentic Access
  operation_count: 7
  slug: publer-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 5
apis:
- description: The Accounts API from Publer — 1 operation(s) for accounts.
  name: Publer Accounts API
  slug: publer-accounts-api
- description: The Jobs API from Publer — 1 operation(s) for jobs.
  name: Publer Jobs API
  slug: publer-jobs-api
- description: The Media API from Publer — 1 operation(s) for media.
  name: Publer Media API
  slug: publer-media-api
- description: The Posts API from Publer — 3 operation(s) for posts.
  name: Publer Posts API
  slug: publer-posts-api
- description: The Workspaces API from Publer — 1 operation(s) for workspaces.
  name: Publer Workspaces API
  slug: publer-workspaces-api
artifact_total: 12
collections:
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
created: '2026-06-25'
description: Publer is a social-media scheduling and management platform for planning, creating, and publishing content across networks like Facebook, Instagram, X, LinkedIn, TikTok, YouTube, Pinterest, and more. The Publer API (v1) lets Business customers programmatically schedule and publish posts, manage connected social accounts and workspaces, work with media libraries, and track asynchronous jobs.
finops:
- name: Publer Finops
  service_category: Management and Governance
  slug: publer-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/publer.png
layout: provider
modified: '2026-06-25'
name: Publer
nav: Providers
network: true
overview: 'Publer publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Accounts API, Jobs API, Media API, and 2 more. Tagged areas include Social Media, Scheduling, Publishing, Content Management, and Marketing.


  Publer''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Publer Plans Pricing
  plan_count: 3
  slug: publer-plans-pricing
random_paper: 70
rate_limits:
- limit_count: 2
  name: Publer Rate Limits
  slug: publer-rate-limits
score:
  band: thin
  composite: 39.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 63.6
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 39.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
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
website: https://publer.com/
---

---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.4
  scored_at: '2026-08-12'
api_count: 1
apis:
- description: GraphQL API for scheduling and publishing posts, managing social media channels, handling content ideas, and accessing post metrics across 11 major social media platforms.
  name: Buffer API
  slug: buffer-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/buffer-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buffer.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.buffer.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bufferapp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bufferapp
- group: company
  title: ''
  type: Blog
  url: https://buffer.com/resources/
- group: commercial
  title: ''
  type: Pricing
  url: https://buffer.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.buffer.com/
- group: other
  title: ''
  type: X
  url: https://x.com/buffer
- group: commercial
  title: ''
  type: Plans
  url: plans/buffer-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/buffer-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/buffer-finops.yml
created: '2026-06-13'
description: Buffer is a social media scheduling and analytics platform with a GraphQL API for scheduling posts, managing content queues, accessing engagement metrics, and publishing across multiple social channels including Instagram, LinkedIn, X, TikTok, Facebook, Threads, Pinterest, Bluesky, YouTube, Mastodon, and Google Business Profiles.
finops:
- name: Buffer Finops
  service_category: ''
  slug: buffer-finops
graphqls:
- description: Buffer provides a GraphQL API for scheduling and publishing social media posts, managing social media channels, handling content ideas, and accessing post engagement metrics across 11 major social med
  name: Buffer GraphQL API
  slug: buffer-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/buffer.png
layout: provider
modified: '2026-06-13'
name: Buffer
nav: Providers
network: true
overview: 'Buffer publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Scheduling, Analytics, Publishing, and Content Management.


  Buffer''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Buffer Plans Pricing
  plan_count: 3
  slug: buffer-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 0
  name: Buffer Rate Limits
  slug: buffer-rate-limits
score:
  band: thin
  composite: 33.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.8
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: domain-security
  name: Buffer Domain Security
  slug: buffer-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buffer
tags:
- Social Media
- Scheduling
- Analytics
- Publishing
- Content Management
- Social Media Management
- Social Media Marketing
- Marketing
- Content Scheduling
website: https://buffer.com
---

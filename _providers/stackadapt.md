---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-07-28'
api_count: 5
apis:
- description: Read-only REST API for fetching reporting data across dimensions and metrics to analyze campaign performance. Write operations are deprecated; use the GraphQL API for write operations.
  name: StackAdapt REST API
  slug: rest-api
- description: Full-featured GraphQL API for creating and managing programmatic advertising campaigns, ad groups, creatives, targeting segments, pixel tracking, and performance reporting. The primary API for write o
  name: StackAdapt GraphQL API
  slug: graphql-api
- description: Server-to-server API for conversion tracking and audience generation without requiring website pixel installation.
  name: StackAdapt Pixel API
  slug: pixel-api
- description: API for secure data sharing and audience synchronization with third-party platforms and data partners.
  name: StackAdapt Data Taxonomy API
  slug: data-taxonomy-api
- description: Model Context Protocol server enabling AI agents (Claude, ChatGPT) to interact with the StackAdapt platform programmatically via the GraphQL API.
  name: StackAdapt MCP Server
  slug: mcp-server
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/stackadapt-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.stackadapt.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.stackadapt.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/StackAdapt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/stackadapt
- group: company
  title: ''
  type: Blog
  url: https://www.stackadapt.com/resources/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.stackadapt.com/plans-and-packages
- group: other
  title: ''
  type: X
  url: https://x.com/stackadapt
- group: commercial
  title: ''
  type: Plans
  url: plans/stackadapt-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/stackadapt-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/stackadapt-finops.yml
created: '2026-06-13'
description: StackAdapt is an AI-powered programmatic advertising platform with REST and GraphQL APIs for managing campaigns, ad groups, creatives, targeting segments, pixel tracking, and performance reporting across native, display, video, connected TV, audio, and digital out-of-home channels.
finops:
- name: Stackadapt Finops
  service_category: ''
  slug: stackadapt-finops
graphqls:
- description: StackAdapt is an AI-powered programmatic advertising platform (DSP) that provides a full-featured GraphQL API for creating and managing digital advertising campaigns across native, display, video, con
  name: StackAdapt GraphQL API
  slug: stackadapt-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/stackadapt.png
layout: provider
modified: '2026-06-13'
name: StackAdapt
nav: Providers
network: true
overview: 'StackAdapt publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Programmatic Advertising, Digital Advertising, Campaign Management, Ad Tech, and DSP.


  StackAdapt''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Stackadapt Plans Pricing
  plan_count: 5
  slug: stackadapt-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 0
  name: Stackadapt Rate Limits
  slug: stackadapt-rate-limits
score:
  band: thin
  composite: 32.3
  delta: 9.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 22.9
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/stackadapt/refs/heads/main/screenshots/stackadapt-2026-06-20T194444.png
security:
- kind: domain-security
  name: Stackadapt Domain Security
  slug: stackadapt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: stackadapt
tags:
- Programmatic Advertising
- Digital Advertising
- Campaign Management
- Ad Tech
- DSP
- Demand-Side Platform
- Native Advertising
- Display Advertising
- Video Advertising
- Connected TV
- Audience Targeting
- Real-Time Bidding
- Conversion Tracking
- Performance Reporting
website: https://www.stackadapt.com
---

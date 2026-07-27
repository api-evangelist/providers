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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Postiz Agentic Access
  operation_count: 20
  slug: postiz-agentic-access
  summary_line: 20 operations · 9 acting
api_count: 6
apis:
- description: Configure a webhook URL in Postiz to receive an HTTP POST notifying your own systems when a post is published, so you can sync downstream tools such as spreadsheets, Slack, or a CRM. Webhooks are conf
  name: Postiz Webhooks
  slug: webhooks
- description: Platform- and post-level analytics.
  name: Postiz Analytics API
  slug: postiz-analytics-api
- description: Connected social media channels and scheduling slots.
  name: Postiz Integrations API
  slug: postiz-integrations-api
- description: Account notifications.
  name: Postiz Notifications API
  slug: postiz-notifications-api
- description: Create, schedule, list, and delete posts.
  name: Postiz Posts API
  slug: postiz-posts-api
- description: Upload media files referenced by posts.
  name: Postiz Uploads API
  slug: postiz-uploads-api
artifact_total: 13
collections:
- collection_type: open
  name: Postiz Public API
  slug: open-postiz
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/postiz-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postiz-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postiz-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/gitroomhq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postiz
- group: company
  title: ''
  type: Website
  url: https://postiz.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postiz.com
- group: company
  title: ''
  type: Blog
  url: https://postiz.com/blog
- group: commercial
  title: ''
  type: Plans
  url: plans/postiz-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postiz-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/postiz-finops.yml
created: '2026-06-25'
description: Postiz is an open-source social media scheduling and management platform for posting across 30+ social, video, community, and blogging channels from a single calendar. It ships as a free AGPL-licensed self-hosted app and as a paid managed Cloud. The Postiz Public API uses simple API-key auth to list connected channels, upload media, and create, schedule, list, and delete posts.
finops:
- name: Postiz Finops
  service_category: Social Media Management
  slug: postiz-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postiz.png
layout: provider
modified: '2026-06-25'
name: Postiz
nav: Providers
network: true
overview: 'Postiz publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Integrations API, Notifications API, and 2 more. Tagged areas include Social Media, Scheduling, Open Source, Content, and Marketing.


  Postiz''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Postiz Plans Pricing
  plan_count: 5
  slug: postiz-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Postiz Rate Limits
  slug: postiz-rate-limits
score:
  band: thin
  composite: 41.3
  delta: 3.3
  facets:
    commercial_clarity: 39.5
    contract_quality: 57.0
    developer_ergonomics: 21.7
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 38.0
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
security:
- kind: authentication
  name: Postiz Authentication
  slug: postiz-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Postiz Domain Security
  slug: postiz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: postiz
tags:
- Social Media
- Scheduling
- Open Source
- Content
- Marketing
website: https://postiz.com
---

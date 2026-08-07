---
access_model:
  confidence: medium
  label: Freemium (free trial)
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: true
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
  scored_at: '2026-08-06'
api_count: 3
apis:
- description: The UserVoice Admin API v2 provides a fast and easy way of working with your feedback data, enabling you to build client applications and custom integrations for administrative operations including da
  name: UserVoice Admin API
  slug: uservoice-admin-api
- description: The UserVoice Helpdesk API exposes the core end-user and admin functionality of UserVoice, making it easy to build client applications or integrations with your own systems using OAuth 1.0a authentica
  name: UserVoice Helpdesk API
  slug: uservoice-helpdesk-api
- description: The UserVoice Idea Collection API enables developers to create custom experiences for capturing feedback from users across multiple platforms including web and mobile, using OAuth Authorization Code F
  name: UserVoice Idea Collection API
  slug: uservoice-idea-collection-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/uservoice-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.uservoice.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.uservoice.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/uservoice
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/uservoice
- group: other
  title: ''
  type: X
  url: https://twitter.com/uservoice
- group: company
  title: ''
  type: Blog
  url: https://www.uservoice.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.uservoice.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.uservoice.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/uservoice-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/uservoice-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/uservoice-finops.yml
created: '2026-06-13'
description: UserVoice is a product feedback and ideation platform with a REST API for managing ideas, gathering votes, tracking status updates, and syncing user feedback with product roadmaps. It provides an Admin API v2 for administrative operations, a Helpdesk API for end-user and support functionality, and an Idea Collection API for custom feedback capture experiences across web and mobile platforms.
finops:
- name: Uservoice Finops
  service_category: ''
  slug: uservoice-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/uservoice.png
jsonld:
- class_count: 30
  name: Uservoice Context
  property_count: 6
  slug: uservoice-context
layout: provider
modified: '2026-06-13'
name: UserVoice
nav: Providers
network: true
overview: 'UserVoice publishes 1 API on the [APIs.io](https://apis.io/) network: Admin API. Tagged areas include Product Feedback, Idea Management, Customer Feedback, Product Roadmap, and Voting.


  The UserVoice catalog on APIs.io includes 1 JSON-LD context.


  UserVoice''s developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Uservoice Plans Pricing
  plan_count: 4
  slug: uservoice-plans-pricing
random_paper: 77
rate_limits:
- limit_count: 0
  name: Uservoice Rate Limits
  slug: uservoice-rate-limits
score:
  band: thin
  composite: 33.6
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.6
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/uservoice/refs/heads/main/screenshots/uservoice-2026-06-20T200702.png
security:
- kind: domain-security
  name: Uservoice Domain Security
  slug: uservoice-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: uservoice
tags:
- Product Feedback
- Idea Management
- Customer Feedback
- Product Roadmap
- Voting
- Feature Requests
- User Research
- SaaS
website: https://www.uservoice.com/
---

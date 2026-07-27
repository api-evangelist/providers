---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: true
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
  score: 39.4
  scored_at: '2026-07-27'
api_count: 3
apis:
- description: Manage assets, query content with ShowQL, get content recommendations, and handle buyer engagement through shares, sharing themes, and digital shared spaces.
  name: Showpad Content API
  slug: showpad-content-api
- description: Access analytics and insights for coaching and training programs, including learning paths, skill assessments, roleplay AI analysis, and coach analytics data.
  name: Showpad Coach API
  slug: showpad-coach-api
- description: Create and manage users, groups, divisions, and permissions with full SCIM 2.0 support for automated identity provisioning and deprovisioning.
  name: Showpad User Management API
  slug: showpad-user-management-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/showpad-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://developer.showpad.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.showpad.com/docs/apis/
- group: other
  title: ''
  type: Fundamentals
  url: https://developer.showpad.com/docs/apis/concepts/fundamentals
- group: auth
  title: ''
  type: Authentication
  url: https://developer.showpad.com/docs/apis/concepts/authentication
- group: design
  title: ''
  type: Versioning
  url: https://developer.showpad.com/docs/apis/concepts/versions
- group: design
  title: ''
  type: Webhooks
  url: https://developer.showpad.com/docs/webhooks/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.showpad.com/docs/changelog/index
- group: operate
  title: ''
  type: Status
  url: https://status.showpad.com
- group: company
  title: ''
  type: Blog
  url: https://www.showpad.com/blog/
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.showpad.com
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://help.showpad.com/hc/en-us/articles/115003975693-Showpad-Release-Notes
- group: commercial
  title: ''
  type: Plans
  url: plans/showpad-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/showpad-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/showpad-finops.yml
created: '2026-06-13'
description: Showpad is a sales enablement and coaching platform offering a REST API for managing sales content, training programs, meeting analytics, and buyer engagement. The API supports content management with ShowQL query language, buyer engagement through shares and digital sales rooms, seller effectiveness via CRM recommendation rules, user management with SCIM 2.0, and analytics covering content reporting and coaching insights across the sales cycle.
finops:
- name: Showpad Finops
  service_category: ''
  slug: showpad-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/showpad.png
layout: provider
modified: '2026-06-13'
name: Showpad
nav: Providers
network: true
overview: 'Showpad publishes 1 API on the [APIs.io](https://apis.io/) network: Content API. Tagged areas include Sales Enablement, Sales Coaching, Content Management, Buyer Engagement, and Sales Analytics.


  Showpad''s developer surface includes developer portal, documentation, authentication, changelog, status page, engineering blog, release notes, and 8 more developer resources.'
plans:
- name: Showpad Plans Pricing
  plan_count: 3
  slug: showpad-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 0
  name: Showpad Rate Limits
  slug: showpad-rate-limits
score:
  band: thin
  composite: 37.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 37.7
    developer_ergonomics: 34.8
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 37.4
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/showpad/refs/heads/main/screenshots/showpad-2026-06-20T193845.png
security:
- kind: domain-security
  name: Showpad Domain Security
  slug: showpad-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: showpad
tags:
- Sales Enablement
- Sales Coaching
- Content Management
- Buyer Engagement
- Sales Analytics
- Training
- CRM Integration
website: https://developer.showpad.com/
---

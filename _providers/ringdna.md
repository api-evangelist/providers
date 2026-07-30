---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: REST API endpoints for managing Guided Selling participant actions within Revenue.io sales engagement workflows, including completing and skipping participant steps in sales cadences.
  name: RingDNA Guided Selling API
  slug: guided-selling-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/ringdna-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ringdna-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.revenue.io
- group: docs
  title: ''
  type: Documentation
  url: https://support.revenue.io/s/topic/0TO60000000TtSEGA0/ringdna
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/ringdna
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/revenueio
- group: company
  title: ''
  type: Blog
  url: https://www.revenue.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.revenue.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.revenue.io
- group: other
  title: ''
  type: X
  url: https://twitter.com/revenue_io
- group: commercial
  title: ''
  type: Plans
  url: plans/ringdna-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/ringdna-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/ringdna-finops.yml
created: '2026-06-13'
description: RingDNA (now Revenue.io) is an intelligent revenue platform providing REST APIs for sales dialing, call recording, conversation analytics, real-time coaching, and CRM integration. The platform is 100% Salesforce-native and serves revenue teams with AI-driven sales engagement, guided selling cadences, conversation intelligence, and revenue orchestration capabilities including the RingDNA Dialer, Moments real-time guidance, and Guided Selling API endpoints.
finops:
- name: Ringdna Finops
  service_category: ''
  slug: ringdna-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ringdna.png
layout: provider
modified: '2026-06-13'
name: RingDNA
nav: Providers
network: true
overview: 'RingDNA publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sales Engagement, Conversation Intelligence, Sales Dialing, Call Recording, and Revenue Orchestration.


  RingDNA''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Ringdna Plans Pricing
  plan_count: 3
  slug: ringdna-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Ringdna Rate Limits
  slug: ringdna-rate-limits
score:
  band: emerging
  composite: 23.4
  delta: -2.4
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 25.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ringdna/refs/heads/main/screenshots/ringdna-2026-06-20T193122.png
security:
- kind: domain-security
  name: Ringdna Domain Security
  slug: ringdna-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Ringdna Trust Center
  slug: ringdna-trust-center
  summary_line: SOC 2, HIPAA, GDPR
slug: ringdna
tags:
- Sales Engagement
- Conversation Intelligence
- Sales Dialing
- Call Recording
- Revenue Orchestration
- CRM Integration
- Salesforce
- AI Coaching
- Sales Automation
website: https://www.revenue.io
---

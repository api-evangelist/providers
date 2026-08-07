---
access_model:
  confidence: medium
  label: Paid (free trial) · Open access
  onboarding: open
  pricing: paid
  public: true
  source:
  - plans
  trial: true
  try_now: true
agent_readiness:
  band: human-only
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
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: REST API for managing social media clients, scheduling posts, monitoring mentions, and accessing analytics and reports across multiple social networks.
  name: Sendible API
  slug: sendible-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sendible-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sendible.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.sendible.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Sendible
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sendible/
- group: company
  title: ''
  type: Blog
  url: https://www.sendible.com/insights
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sendible.com/pricing
- group: other
  title: ''
  type: X
  url: https://x.com/sendible
- group: commercial
  title: ''
  type: Plans
  url: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/plans/sendible-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/rate-limits/sendible-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/finops/sendible-finops.yml
created: '2026-06-13'
description: Sendible is a social media management platform designed for agencies, marketers, and brand managers. It provides a REST API for managing clients, scheduling posts across multiple networks, monitoring mentions, and accessing social media analytics and reports at scale.
finops:
- name: Sendible Finops
  service_category: ''
  slug: sendible-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sendible.png
layout: provider
modified: '2026-06-13'
name: Sendible
nav: Providers
network: true
overview: 'Sendible publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Social Media Management, Agencies, Scheduling, and Analytics.


  Sendible''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Sendible Plans Pricing
  plan_count: 10
  slug: sendible-plans-pricing
random_paper: 47
rate_limits:
- limit_count: 5
  name: Sendible Rate Limits
  slug: sendible-rate-limits
score:
  band: emerging
  composite: 23.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 23.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sendible/refs/heads/main/screenshots/sendible-2026-06-20T193657.png
security:
- kind: domain-security
  name: Sendible Domain Security
  slug: sendible-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sendible
tags:
- Social Media
- Social Media Management
- Agencies
- Scheduling
- Analytics
- Monitoring
website: https://www.sendible.com/
---

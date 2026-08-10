---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: REST API for the Loomly brand success platform, providing programmatic access to social media calendars, posts, approval workflows, publishing scheduling, and analytics. Authenticated via OAuth 2.0 Be
  name: Loomly API
  slug: loomly-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/loomly-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/loomly-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/loomly-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.loomly.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.loomly.com/integrations
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/loomly
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/loomly
- group: company
  title: ''
  type: Blog
  url: https://www.loomly.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.loomly.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.loomly.com
- group: other
  title: ''
  type: X
  url: https://x.com/LoomlySocial
- group: commercial
  title: ''
  type: Plans
  url: plans/loomly-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/loomly-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/loomly-finops.yml
created: '2026-06-13'
description: Loomly is a brand success platform with a REST API for managing social media content calendars, post ideas, approval workflows, publishing, and audience engagement analytics. It supports 10+ social channels including Facebook, Instagram, LinkedIn, TikTok, YouTube, Pinterest, Google Business Profile, and Threads, enabling marketing teams to collaborate, schedule, and analyze content from a unified platform.
finops:
- name: Loomly Finops
  service_category: ''
  slug: loomly-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/loomly.png
layout: provider
modified: '2026-06-13'
name: Loomly
nav: Providers
network: true
overview: 'Loomly publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Content Calendar, Scheduling, Approval Workflows, and Analytics.


  Loomly''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Loomly Plans Pricing
  plan_count: 3
  slug: loomly-plans-pricing
random_paper: 88
rate_limits:
- limit_count: 2
  name: Loomly Rate Limits
  slug: loomly-rate-limits
score:
  band: emerging
  composite: 26.1
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 26.1
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/loomly/refs/heads/main/screenshots/loomly-2026-06-20T184715.png
security:
- kind: domain-security
  name: Loomly Domain Security
  slug: loomly-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Loomly Vulnerability Disclosure
  slug: loomly-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Loomly Trust Center
  slug: loomly-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS
slug: loomly
tags:
- Social Media
- Content Calendar
- Scheduling
- Approval Workflows
- Analytics
- Brand Management
- Publishing
- Community Management
website: https://www.loomly.com
---

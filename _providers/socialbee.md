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
- description: SocialBee platform API for managing social media posts, content categories, scheduling, recycling evergreen content, and accessing analytics across major social networks. Currently accessible via Zapi
  name: SocialBee API
  slug: socialbee-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/socialbee-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/socialbee-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://socialbee.com
- group: docs
  title: ''
  type: Documentation
  url: https://help.socialbee.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/SocialBee
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/socialbeehq/
- group: company
  title: ''
  type: Blog
  url: https://socialbee.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://socialbee.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.socialbee.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/SocialBeeHQ
- group: commercial
  title: ''
  type: Plans
  url: plans/socialbee-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/socialbee-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/socialbee-finops.yml
created: '2026-06-13'
description: SocialBee is an AI-powered social media management tool providing a REST-based platform API for managing content categories, scheduling and recycling evergreen posts, curating content from RSS sources, and accessing social media analytics across Facebook, Instagram, X (Twitter), LinkedIn, TikTok, Pinterest, YouTube, Threads, Bluesky, and Google Business Profiles. Third-party automation is available via Zapier, Make, and Pabbly connectors; a public REST API is on the long-term roadmap.
finops:
- name: Socialbee Finops
  service_category: ''
  slug: socialbee-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/socialbee.png
layout: provider
modified: '2026-06-13'
name: SocialBee
nav: Providers
network: true
overview: 'SocialBee publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media Management, Content Scheduling, Content Recycling, Social Media Analytics, and AI Caption Generation.


  SocialBee''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Socialbee Plans Pricing
  plan_count: 6
  slug: socialbee-plans-pricing
random_paper: 55
rate_limits:
- limit_count: 6
  name: Socialbee Rate Limits
  slug: socialbee-rate-limits
score:
  band: emerging
  composite: 25.9
  delta: -2.4
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 28.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/socialbee/refs/heads/main/screenshots/socialbee-2026-06-20T194123.png
security:
- kind: domain-security
  name: Socialbee Domain Security
  slug: socialbee-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Socialbee Vulnerability Disclosure
  slug: socialbee-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: socialbee
tags:
- Social Media Management
- Content Scheduling
- Content Recycling
- Social Media Analytics
- AI Caption Generation
website: https://socialbee.com
---

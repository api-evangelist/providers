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
api_count: 1
apis:
- description: The Sprout Social Public API provides programmatic access to publishing, analytics, messaging, listening, and social care case data across major social networks. Requires Advanced plan or higher.
  name: Sprout Social API
  slug: sprout-social-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sprout-social-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sprout-social-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sproutsocial.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.sproutsocial.com/docs/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/sproutsocial
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sprout-social-inc-
- group: company
  title: ''
  type: Blog
  url: https://sproutsocial.com/insights/
- group: commercial
  title: ''
  type: Pricing
  url: https://sproutsocial.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sproutsocialstatus.com
- group: other
  title: ''
  type: X
  url: https://x.com/SproutSocial
- group: commercial
  title: ''
  type: Plans
  url: plans/sprout-social-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sprout-social-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/sprout-social-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
created: '2026-06-13'
description: Sprout Social is a social media management platform with a REST API for publishing posts, monitoring mentions, managing messages, accessing analytics, and reporting across social networks including Instagram, Facebook, LinkedIn, TikTok, YouTube, and X.
finops:
- name: Sprout Social Finops
  service_category: ''
  slug: sprout-social-finops
graphqls:
- description: This GraphQL schema is a conceptual representation of the Sprout Social REST API surface, modeling the core entities, relationships, and operations available through the [Sprout Social Public API](htt
  name: Sprout Social GraphQL Schema
  slug: sprout-social-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sprout-social.png
jsonld:
- class_count: 0
  name: Sprout Social Context
  property_count: 0
  slug: sprout-social
layout: provider
modified: '2026-06-13'
name: Sprout Social
nav: Providers
network: true
overview: 'Sprout Social publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Social Media, Social Media Management, Publishing, Analytics, and Reporting.


  The Sprout Social catalog on APIs.io includes 1 JSON-LD context.


  Sprout Social''s developer surface includes documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Sprout Social Plans Pricing
  plan_count: 5
  slug: sprout-social-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 2
  name: Sprout Social Rate Limits
  slug: sprout-social-rate-limits
score:
  band: thin
  composite: 37.0
  delta: 6.2
  facets:
    commercial_clarity: 57.9
    contract_quality: 54.3
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 30.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 22.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
security:
- kind: domain-security
  name: Sprout Social Domain Security
  slug: sprout-social-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sprout Social Trust Center
  slug: sprout-social-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, GDPR, CSA STAR
slug: sprout-social
tags:
- Social Media
- Social Media Management
- Publishing
- Analytics
- Reporting
- Messaging
- Listening
website: https://sproutsocial.com
---

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
- description: REST API for creating and sending personalized postcards and letters, managing contact lists, tracking delivery, and automating direct mail campaigns with webhook support.
  name: Postalytics API
  slug: postalytics-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postalytics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.postalytics.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.postalytics.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/postalytics
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postalytics
- group: company
  title: ''
  type: Blog
  url: https://www.postalytics.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.postalytics.com/direct-mail-pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.postalytics.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/postalytics
- group: commercial
  title: ''
  type: Plans
  url: plans/postalytics-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/postalytics-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/postalytics-finops.yml
created: 2026-06-13
description: Postalytics is a direct mail automation platform with a REST API for creating and sending personalized postcards and letters with real-time mail tracking and analytics. The API enables programmatic campaign management for triggered drip campaigns and batch smart-send mailings, with supported SDKs in Python, Node.js, Rust, Java, Go, and C#.
finops:
- name: Postalytics Finops
  service_category: ''
  slug: postalytics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postalytics.png
jsonld:
- class_count: 21
  name: Postalytics Context
  property_count: 2
  slug: postalytics-context
layout: provider
modified: 2026-06-13
name: Postalytics
nav: Providers
network: true
overview: 'Postalytics publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Direct Mail, Postcards, Letters, Mail Automation, and Print.


  The Postalytics catalog on APIs.io includes 1 JSON-LD context.


  Postalytics'' developer surface includes documentation, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: Postalytics Plans Pricing
  plan_count: 4
  slug: postalytics-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Postalytics Rate Limits
  slug: postalytics-rate-limits
score:
  band: thin
  composite: 33.1
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 33.1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postalytics/refs/heads/main/screenshots/postalytics-2026-06-20T191950.png
security:
- kind: domain-security
  name: Postalytics Domain Security
  slug: postalytics-domain-security
  summary_line: TLSv1.3 · DMARC
slug: postalytics
tags:
- Direct Mail
- Postcards
- Letters
- Mail Automation
- Print
- Tracking
- Analytics
website: https://www.postalytics.com/
---

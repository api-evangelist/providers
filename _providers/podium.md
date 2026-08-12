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
  scored_at: '2026-08-11'
api_count: 1
apis:
- description: REST API for managing customer communications including messaging, reviews, payments, webchat, contacts, automations, and webhooks for local businesses. Base URL is https://api.podium.com/v4/ and uses
  name: Podium API
  slug: podium-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/podium-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.podium.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.podium.com/reference/introduction
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.podium.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/podium
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/podiumhq/
- group: company
  title: ''
  type: Blog
  url: https://www.podium.com/resource-center
- group: commercial
  title: ''
  type: Pricing
  url: https://www.podium.com/getpricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.podium.com
- group: other
  title: ''
  type: X
  url: https://twitter.com/podiumhq/
- group: commercial
  title: ''
  type: Plans
  url: plans/podium-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/podium-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/podium-finops.yml
created: '2026-06-13'
description: Podium is a customer communication platform providing a REST API for local businesses to manage text-based conversations, reviews, payment requests, lead capture forms, webchat, and AI-driven lead conversion. The API is organized around REST with predictable resource-oriented URLs, JSON-encoded responses, and OAuth 2.0 authentication.
finops:
- name: Podium Finops
  service_category: ''
  slug: podium-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/podium.png
jsonld:
- class_count: 18
  name: Podium Context
  property_count: 3
  slug: podium-context
layout: provider
modified: '2026-06-13'
name: Podium
nav: Providers
network: true
overview: 'Podium publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Customer Communication, Reviews, Messaging, Payments, and Webchat.


  The Podium catalog on APIs.io includes 1 JSON-LD context.


  Podium''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Podium Plans Pricing
  plan_count: 3
  slug: podium-plans-pricing
random_paper: 74
rate_limits:
- limit_count: 1
  name: Podium Rate Limits
  slug: podium-rate-limits
score:
  band: emerging
  composite: 27.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 19.6
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 27.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/podium/refs/heads/main/screenshots/podium-2026-06-20T191840.png
security:
- kind: domain-security
  name: Podium Domain Security
  slug: podium-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: podium
tags:
- Customer Communication
- Reviews
- Messaging
- Payments
- Webchat
- Local Business
- SMS
- Lead Generation
website: https://www.podium.com/
---

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
api_count: 2
apis:
- description: REST API for managing Landbot resources including channels, customers, customer fields, message hooks, webhooks, and WhatsApp templates. Token-based authentication using an agent token from account se
  name: Landbot Platform API
  slug: landbot-platform-api
- description: API for embedding and interacting with Landbot chat sessions programmatically, enabling developers to drive conversational flows from custom applications.
  name: Landbot APIchat
  slug: landbot-apichat
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/landbot-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://landbot.io/
- group: docs
  title: ''
  type: Documentation
  url: https://dev.landbot.io/api-reference/platform
- group: company
  title: ''
  type: Blog
  url: https://landbot.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://landbot.io/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.landbot.io/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/landbot-io
- group: other
  title: ''
  type: X
  url: https://twitter.com/landbot_io
- group: commercial
  title: ''
  type: Plans
  url: plans/landbot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/landbot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/landbot-finops.yml
- group: company
  title: ''
  type: BlogPosts
  url: blogs/blogs.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/landbot-context.jsonld
created: 2026-06-12
description: Landbot is a no-code conversational AI platform that enables businesses to build, deploy, and manage chatbots across web, WhatsApp, and messenger channels without requiring programming skills. The platform provides a REST API at api.landbot.io/v1 for programmatic control of channels, customers, customer fields, message hooks, and webhooks. Developers can use token-based authentication to integrate Landbot bots into external systems and retrieve conversation data in real time. Landbot also offers an APIchat interface for embedding chat interactions directly into custom applications. The platform supports webhooks for event-driven automation and provides SDKs and code samples for Shell, Ruby, Node.js, PHP, and Python.
finops:
- name: Landbot Finops
  service_category: ''
  slug: landbot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/landbot.png
jsonld:
- class_count: 11
  name: Landbot Context
  property_count: 7
  slug: landbot-context
layout: provider
modified: 2026-06-12
name: Landbot
nav: Providers
network: true
overview: 'Landbot publishes 1 API on the [APIs.io](https://apis.io/) network: Platform API. Tagged areas include chatbot, conversational AI, no-code, WhatsApp, and webhooks.


  The Landbot catalog on APIs.io includes 1 JSON-LD context.


  Landbot''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Landbot Plans Pricing
  plan_count: 6
  slug: landbot-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Landbot Rate Limits
  slug: landbot-rate-limits
score:
  band: thin
  composite: 29.8
  delta: -6.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 45.2
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 15.8
  previous_composite: 36.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 15.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/landbot/refs/heads/main/screenshots/landbot-2026-06-20T184258.png
security:
- kind: domain-security
  name: Landbot Domain Security
  slug: landbot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: landbot
tags:
- chatbot
- conversational AI
- no-code
- WhatsApp
- webhooks
- messaging
- automation
website: https://landbot.io/
---

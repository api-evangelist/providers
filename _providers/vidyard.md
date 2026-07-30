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
api_count: 3
apis:
- description: The Vidyard Dashboard API provides full CRUD access to your Vidyard account assets including players, videos, chapters, organizations, teams, users, roles, events, campaigns, tags, webhooks, embeds, a
  name: Vidyard Dashboard API
  slug: vidyard-dashboard-api
- description: The Video Agent API enables integration of Vidyard's AI-powered video generation into any application or custom workflow. It allows triggering personalized video creation of Vidyard campaigns programm
  name: Vidyard Video Agent API
  slug: vidyard-video-agent-api
- description: The Analytics Webhook API allows subscribing to and streaming video view data from Vidyard to an external application. View events are delivered as HTTP POST requests in JSON format to a configured en
  name: Vidyard Analytics Webhook API
  slug: vidyard-analytics-webhook-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/vidyard-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vidyard-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vidyard-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vidyard.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.vidyard.com/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Vidyard
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vidyard
- group: company
  title: ''
  type: Blog
  url: https://www.vidyard.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vidyard.com/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vidyard.com/
- group: other
  title: ''
  type: X
  url: https://x.com/vidyard
- group: commercial
  title: ''
  type: Plans
  url: plans/vidyard-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vidyard-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/vidyard-finops.yml
created: '2026-06-12'
description: Vidyard is a video platform for business that provides REST APIs for managing video libraries, generating sharing links, tracking viewer analytics, and integrating with CRM and marketing tools. The Dashboard API enables programmatic control over players, videos, chapters, organizations, teams, users, events, campaigns, webhooks, and more. The Video Agent API supports AI-powered personalized video creation workflows, and the Analytics Webhook API streams real-time viewer data to external systems.
finops:
- name: Vidyard Finops
  service_category: ''
  slug: vidyard-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vidyard.png
jsonld:
- class_count: 6
  name: Vidyard Context
  property_count: 20
  slug: vidyard-context
layout: provider
modified: '2026-06-12'
name: Vidyard
nav: Providers
network: true
overview: 'Vidyard publishes 1 API on the [APIs.io](https://apis.io/) network: Dashboard API. Tagged areas include Video, Video Platform, Video Analytics, Video Sharing, and Sales Video.


  The Vidyard catalog on APIs.io includes 1 JSON-LD context.


  Vidyard''s developer surface includes documentation, GitHub presence, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Vidyard Plans Pricing
  plan_count: 4
  slug: vidyard-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 3
  name: Vidyard Rate Limits
  slug: vidyard-rate-limits
score:
  band: thin
  composite: 40.5
  delta: -4.7
  facets:
    commercial_clarity: 57.9
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 52.6
  previous_composite: 45.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vidyard/refs/heads/main/screenshots/vidyard-2026-06-20T201023.png
security:
- kind: domain-security
  name: Vidyard Domain Security
  slug: vidyard-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Vidyard Vulnerability Disclosure
  slug: vidyard-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Vidyard Trust Center
  slug: vidyard-trust-center
  summary_line: SOC 2, GDPR
slug: vidyard
tags:
- Video
- Video Platform
- Video Analytics
- Video Sharing
- Sales Video
- CRM Integration
- Marketing
- AI Video
- Webhooks
website: https://www.vidyard.com/
---

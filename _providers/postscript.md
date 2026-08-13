---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Postscript Agentic Access
  operation_count: 9
  slug: postscript-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 4
apis:
- description: The Postscript API enables developers to manage SMS subscribers, send messages, configure keywords, trigger events, and integrate the Postscript platform with external commerce and marketing systems.
  name: Postscript API
  slug: postscript-api
- description: Send custom events for use in flows and triggers.
  name: Postscript Events API
  slug: postscript-events-api
- description: Manage SMS subscribers.
  name: Postscript Subscribers API
  slug: postscript-subscribers-api
- description: Configure webhook subscriptions for Postscript events.
  name: Postscript Webhooks API
  slug: postscript-webhooks-api
artifact_total: 13
collections:
- collection_type: open
  name: Postscript API
  slug: open-postscript
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/postscript-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/postscript-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/postscript-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/postscript-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/postscript-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/postscriptio
- group: company
  title: ''
  type: Website
  url: https://postscript.io
- group: docs
  title: ''
  type: Documentation
  url: https://developers.postscript.io
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.postscript.io/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://developers.postscript.io/docs/api-authentication
- group: operate
  title: ''
  type: RateLimits
  url: https://developers.postscript.io/docs/rate-limits
- group: auth
  title: ''
  type: Compliance
  url: https://developers.postscript.io/docs/compliance
- group: docs
  title: ''
  type: APIReference
  url: https://developers.postscript.io/reference
- group: operate
  title: ''
  type: ChangeLog
  url: https://developers.postscript.io/changelog
- group: build
  title: ''
  type: SDKs
  url: https://developers.postscript.io/docs/javascript-sdk-api-reference
- group: commercial
  title: ''
  type: Pricing
  url: https://postscript.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://postscript.io/blog
- group: operate
  title: ''
  type: Support
  url: https://help.postscript.io
- group: agent
  title: ''
  type: LlmsText
  url: https://developers.postscript.io/llms.txt
created: '2025-01-01'
description: Postscript is an SMS marketing and sales platform built for Shopify brands, providing list growth tools, campaign delivery, RCS messaging, and AI-driven shopping assistants alongside a developer API for building custom SMS experiences.
finops:
- name: Postscript Finops
  service_category: API
  slug: postscript-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/postscript.png
layout: provider
modified: '2026-04-28'
name: Postscript
nav: Providers
network: true
overview: 'Postscript publishes 3 APIs on the [APIs.io](https://apis.io/) network: Events API, Subscribers API, and Webhooks API. Tagged areas include SMS, Marketing, Messaging, E-commerce, and Shopify.


  Postscript''s developer surface includes authentication, documentation, getting-started guide, API reference, changelog, pricing, engineering blog, and 12 more developer resources.'
plans:
- name: Postscript Plans Pricing
  plan_count: 3
  slug: postscript-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Postscript Rate Limits
  slug: postscript-rate-limits
score:
  band: thin
  composite: 41.2
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 56.7
    developer_ergonomics: 50.0
    discoverability: 72.2
    governance: 0.0
    operational_transparency: 23.7
  previous_composite: 41.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.9
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/postscript/refs/heads/main/screenshots/postscript-2026-06-20T192017.png
security:
- kind: authentication
  name: Postscript Authentication
  slug: postscript-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Postscript Domain Security
  slug: postscript-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Postscript Vulnerability Disclosure
  slug: postscript-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Postscript Trust Center
  slug: postscript-trust-center
  summary_line: SOC 2, GDPR
slug: postscript
tags:
- SMS
- Marketing
- Messaging
- E-commerce
- Shopify
- RCS
- Subscribers
website: https://postscript.io
---

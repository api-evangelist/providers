---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
- acting_count: 4
  human_in_the_loop: 0
  name: Gupshup Agentic Access
  operation_count: 6
  slug: gupshup-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 6
apis:
- description: 'Broadcast SMS to a single number or many numbers programmatically via POST /msg on the /sm surface. Note - Gupshup has announced end-of-life for the /sm endpoints and recommends migrating SMS traffic '
  name: Gupshup SMS API
  slug: gupshup-sms-api
- description: Send RCS (Rich Communication Services) business messages - rich cards, carousels, suggested replies, and media. RCS is onboarding-gated (username / password issued by Gupshup) and served through the G
  name: Gupshup RCS API
  slug: gupshup-rcs-api
- description: Token-authenticated Partner surface (partner.gupshup.io) for BSPs and resellers - manage apps, templates, subscriptions/callbacks, and send messages through Meta-format passthrough endpoints (e.g. POS
  name: Gupshup Partner API
  slug: gupshup-partner-api
- description: Send WhatsApp session messages.
  name: Gupshup Messaging API
  slug: gupshup-messaging-api
- description: Manage user opt-in / opt-out and list interacted users.
  name: Gupshup Opt-In API
  slug: gupshup-opt-in-api
- description: Send and list WhatsApp template (HSM) messages.
  name: Gupshup Templates API
  slug: gupshup-templates-api
artifact_total: 13
collections:
- collection_type: open
  name: Gupshup WhatsApp Business API
  slug: open-gupshup
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/gupshup-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/gupshup-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/gupshup-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/gupshup
- group: company
  title: ''
  type: Website
  url: https://www.gupshup.io
- group: docs
  title: ''
  type: Documentation
  url: https://docs.gupshup.io
- group: commercial
  title: ''
  type: Plans
  url: plans/gupshup-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/gupshup-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/gupshup-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.gupshup.io/resources/blog
created: '2026-07-12'
description: Gupshup is a conversational messaging and CPaaS platform (headquartered in India) that lets businesses send and receive messages across WhatsApp, SMS, RCS, and other channels, plus build chatbots and conversational AI journeys. The developer platform exposes REST APIs on api.gupshup.io - most prominently the WhatsApp Business API (send session and template messages, opt-in management, templates, media, and inbound webhooks) - authenticated with an apikey header and scoped to a registered app. Separate SMS, RCS, and Partner API surfaces are also documented.
finops:
- name: Gupshup Finops
  service_category: Conversational Messaging and CPaaS
  slug: gupshup-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/gupshup.png
layout: provider
modified: '2026-07-12'
name: Gupshup
nav: Providers
network: true
overview: 'Gupshup publishes 3 APIs on the [APIs.io](https://apis.io/) network: Messaging API, Opt-In API, and Templates API. Tagged areas include Messaging, WhatsApp, Conversational AI, CPaaS, and SMS.


  Gupshup''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Gupshup Plans Pricing
  plan_count: 4
  slug: gupshup-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 4
  name: Gupshup Rate Limits
  slug: gupshup-rate-limits
score:
  band: thin
  composite: 34.9
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 61.2
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 34.9
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
    score: 16.7
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/gupshup/refs/heads/main/screenshots/gupshup-2026-07-25T220436.png
security:
- kind: authentication
  name: Gupshup Authentication
  slug: gupshup-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Gupshup Domain Security
  slug: gupshup-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gupshup
tags:
- Messaging
- WhatsApp
- Conversational AI
- CPaaS
- SMS
- RCS
- India
- Chatbots
- Business Messaging
- Communications
website: https://www.gupshup.io
---

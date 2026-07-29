---
access_model:
  confidence: high
  label: Paid (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: true
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Simpletexting Agentic Access
  operation_count: 35
  slug: simpletexting-agentic-access
  summary_line: 35 operations · 19 acting
api_count: 10
apis:
- description: Create and retrieve bulk campaigns to lists and segments.
  name: SimpleTexting Campaigns API
  slug: simpletexting-campaigns-api
- description: Manage contact lists and list membership.
  name: SimpleTexting Contact Lists API
  slug: simpletexting-contact-lists-api
- description: Read dynamic contact segments.
  name: SimpleTexting Contact Segments API
  slug: simpletexting-contact-segments-api
- description: Create, read, update, and delete individual contacts.
  name: SimpleTexting Contacts API
  slug: simpletexting-contacts-api
- description: Batch update and delete groups of contacts.
  name: SimpleTexting Contacts - Batch Operations API
  slug: simpletexting-contacts-batch-operations-api
- description: Read account custom fields / merge tags.
  name: SimpleTexting Custom Fields API
  slug: simpletexting-custom-fields-api
- description: Upload and manage MMS media items.
  name: SimpleTexting Media Items API
  slug: simpletexting-media-items-api
- description: Send and retrieve one-to-one SMS / MMS messages.
  name: SimpleTexting Messages API
  slug: simpletexting-messages-api
- description: Account information and sending phone numbers.
  name: SimpleTexting Tenant API
  slug: simpletexting-tenant-api
- description: Subscribe to platform events via HTTP callbacks.
  name: SimpleTexting Webhooks API
  slug: simpletexting-webhooks-api
artifact_total: 17
collections:
- collection_type: open
  name: SimpleTexting API
  slug: open-simpletexting
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/simpletexting-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/simpletexting-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/simpletexting-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://simpletexting.com/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/simpletexting
- group: company
  title: ''
  type: Website
  url: https://simpletexting.com/
- group: docs
  title: ''
  type: Documentation
  url: https://simpletexting.com/api/docs/
- group: commercial
  title: ''
  type: Plans
  url: plans/simpletexting-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/simpletexting-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/simpletexting-finops.yml
created: '2026-06-20'
description: SimpleTexting is a business SMS and MMS marketing platform. Its v2 REST API lets developers send single text messages, run bulk campaigns to lists and segments, manage contacts and contact lists, upload MMS media, provision sending numbers, and subscribe to delivery and incoming-message webhooks, all authenticated with a bearer token.
finops:
- name: Simpletexting Finops
  service_category: Communications
  slug: simpletexting-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simpletexting.png
layout: provider
modified: '2026-06-20'
name: SimpleTexting
nav: Providers
network: true
overview: 'SimpleTexting publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contact Lists API, Contact Segments API, and 7 more. Tagged areas include SMS, MMS, Messaging, Marketing, and Text Messaging.


  SimpleTexting''s developer surface includes authentication, engineering blog, documentation, and 7 more developer resources.'
plans:
- name: Simpletexting Plans Pricing
  plan_count: 2
  slug: simpletexting-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 3
  name: Simpletexting Rate Limits
  slug: simpletexting-rate-limits
score:
  band: thin
  composite: 32.1
  delta: -4.8
  facets:
    commercial_clarity: 28.9
    contract_quality: 52.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 10
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/simpletexting/refs/heads/main/screenshots/simpletexting-2026-06-20T193933.png
security:
- kind: authentication
  name: Simpletexting Authentication
  slug: simpletexting-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Simpletexting Domain Security
  slug: simpletexting-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: simpletexting
tags:
- SMS
- MMS
- Messaging
- Marketing
- Text Messaging
website: https://simpletexting.com/
---

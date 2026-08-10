---
access_model:
  confidence: high
  label: Freemium (free trial) · Open access
  onboarding: open
  pricing: freemium
  public: true
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
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 19
  human_in_the_loop: 0
  name: Spruce Health Agentic Access
  operation_count: 38
  slug: spruce-health-agentic-access
  summary_line: 38 operations · 19 acting
api_count: 4
apis:
- description: Contacts (patients and other parties) in a Spruce organization.
  name: Spruce Health Contacts API
  slug: spruce-health-contacts-api
- description: Conversations (message threads) in a Spruce organization.
  name: Spruce Health Conversations API
  slug: spruce-health-conversations-api
- description: Conversation items, messages, media, endpoints, and scheduled messages.
  name: Spruce Health Messages API
  slug: spruce-health-messages-api
- description: Webhook endpoints for real-time contact / conversation events.
  name: Spruce Health Webhooks API
  slug: spruce-health-webhooks-api
artifact_total: 11
collections:
- collection_type: open
  name: Spruce Public API
  slug: open-spruce-health
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/spruce-health-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/spruce-health-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/spruce-health-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://sprucehealth.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/spruce-health
- group: docs
  title: ''
  type: Documentation
  url: https://developer.sprucehealth.com/docs/overview
- group: start
  title: ''
  type: SignUp
  url: https://sprucehealth.com/plans
- group: commercial
  title: ''
  type: Plans
  url: plans/spruce-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/spruce-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/spruce-health-finops.yml
created: '2026-07-10'
description: Spruce Health is a HIPAA-compliant healthcare communication platform that gives modern clinics secure messaging, voice, video, team chat, e-fax, secure payments, and phone lines in one system. The Spruce Public API is a RESTful, Bearer-token-authenticated interface (base https://api.sprucehealth.com/v1) that lets an organization manage Contacts, Conversations, conversation items and Messages, internal endpoints and phone lines, and register Webhook endpoints for real-time events. API access is gated - it is part of the Communicator plan and organizations must contact Spruce Support to have API access enabled before generating tokens.
finops:
- name: Spruce Health Finops
  service_category: Healthcare Communication
  slug: spruce-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/spruce-health.png
layout: provider
modified: '2026-07-10'
name: Spruce Health
nav: Providers
network: true
overview: 'Spruce Health publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Contacts API, Conversations API, Messages API, and 1 more. Tagged areas include Healthcare, HIPAA, Communication, Secure Messaging, and Telehealth.


  Spruce Health''s developer surface includes authentication, documentation, signup flow, and 7 more developer resources.'
plans:
- name: Spruce Health Plans Pricing
  plan_count: 3
  slug: spruce-health-plans-pricing
random_paper: 57
rate_limits:
- limit_count: 4
  name: Spruce Health Rate Limits
  slug: spruce-health-rate-limits
score:
  band: thin
  composite: 37.2
  delta: 0.0
  facets:
    commercial_clarity: 52.6
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: authentication
  name: Spruce Health Authentication
  slug: spruce-health-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Spruce Health Domain Security
  slug: spruce-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: spruce-health
tags:
- Healthcare
- HIPAA
- Communication
- Secure Messaging
- Telehealth
- Contacts
- Conversations
- Messaging
- Webhooks
- VoIP
website: https://sprucehealth.com
---

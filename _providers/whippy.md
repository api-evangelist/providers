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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Whippy Agentic Access
  operation_count: 33
  slug: whippy-agentic-access
  summary_line: 33 operations · 17 acting
api_count: 1
apis:
- description: Send campaigns and inspect campaign analytics.
  name: Whippy Campaigns API
  slug: whippy-campaigns-api
- description: List and inspect channels and channel membership.
  name: Whippy Channels API
  slug: whippy-channels-api
- description: Manage contacts and communication preferences.
  name: Whippy Contacts API
  slug: whippy-contacts-api
- description: List, search, and update conversations and their messages.
  name: Whippy Conversations API
  slug: whippy-conversations-api
- description: Send SMS / MMS, email, and fax messages.
  name: Whippy Messaging API
  slug: whippy-messaging-api
- description: Manage automated multi-step sequences and their contacts.
  name: Whippy Sequences API
  slug: whippy-sequences-api
- description: Push first-party custom events into Whippy.
  name: Whippy Webhooks API
  slug: whippy-webhooks-api
artifact_total: 22
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Whippy Public Campaigns API
  slug: open-whippy-campaigns-api
- collection_type: open
  name: Whippy Public Campaigns Channels API
  slug: open-whippy-channels-api
- collection_type: open
  name: Whippy Public Campaigns Contacts API
  slug: open-whippy-contacts-api
- collection_type: open
  name: Whippy Public Campaigns Conversations API
  slug: open-whippy-conversations-api
- collection_type: open
  name: Whippy Public Campaigns Messaging API
  slug: open-whippy-messaging-api
- collection_type: open
  name: Whippy Public Campaigns Sequences API
  slug: open-whippy-sequences-api
- collection_type: open
  name: Whippy Public Campaigns Webhooks API
  slug: open-whippy-webhooks-api
- collection_type: open
  name: Whippy Public API
  slug: open-whippy
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/whippy-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/whippy-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/whippy-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/whippy-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/whippy-ai
- group: company
  title: ''
  type: Website
  url: https://www.whippy.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.whippy.ai
- group: commercial
  title: ''
  type: Plans
  url: plans/whippy-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/whippy-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/whippy-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.whippy.ai/blog
created: '2026-06-20'
description: Whippy is an AI-powered customer communication platform unifying SMS, email, voice, and fax into a single omnichannel inbox. Its public REST API (X-WHIPPY-KEY header) lets developers send messages, manage contacts and conversations, run campaigns and automated sequences, configure channels, and subscribe to webhooks.
finops:
- name: Whippy Finops
  service_category: Communication and Messaging
  slug: whippy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/whippy.png
layout: provider
modified: '2026-06-20'
name: Whippy
nav: Providers
network: true
overview: 'Whippy publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Channels API, Contacts API, and 4 more. Tagged areas include Communications, Messaging, SMS, Email, and Voice.


  Whippy''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Whippy Plans Pricing
  plan_count: 6
  slug: whippy-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 4
  name: Whippy Rate Limits
  slug: whippy-rate-limits
score:
  band: thin
  composite: 36.9
  coverage:
    artifact_dirs: 11
    catalog_gap: 51.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 55.2
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 36.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/whippy/refs/heads/main/screenshots/whippy-2026-06-20T201440.png
security:
- kind: authentication
  name: Whippy Authentication
  slug: whippy-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Whippy Domain Security
  slug: whippy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: whippy
tags:
- Communications
- Messaging
- SMS
- Email
- Voice
- Artificial Intelligence
- Campaigns
- Sequences
website: https://www.whippy.ai
---

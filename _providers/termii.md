---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
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
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 16
  human_in_the_loop: 0
  name: Termii Agentic Access
  operation_count: 24
  slug: termii-agentic-access
  summary_line: 24 operations · 16 acting
api_count: 6
apis:
- description: Send, list, and manage SMS campaigns.
  name: Termii Campaigns API
  slug: termii-campaigns-api
- description: Manage phonebooks and the contacts within them.
  name: Termii Contacts API
  slug: termii-contacts-api
- description: Account balance, message history, and number status.
  name: Termii Insights API
  slug: termii-insights-api
- description: Send single, bulk, and number-based messages.
  name: Termii Messaging API
  slug: termii-messaging-api
- description: Fetch and request alphanumeric sender IDs.
  name: Termii Sender IDs API
  slug: termii-sender-ids-api
- description: Generate, deliver, and verify one-time passwords.
  name: Termii Token API
  slug: termii-token-api
artifact_total: 13
collections:
- collection_type: open
  name: Termii API
  slug: open-termii
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/termii-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/termii-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/termii-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/termii
- group: company
  title: ''
  type: Website
  url: https://termii.com
- group: docs
  title: ''
  type: Documentation
  url: https://developers.termii.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/termii-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/termii-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/termii-finops.yml
created: '2026-06-20'
description: Termii is an African multichannel messaging platform whose REST API lets businesses send SMS, voice, WhatsApp, and email; generate and verify one-time passwords (OTP) for customer verification; manage sender IDs, campaigns, and contact phonebooks; and pull insights such as account balance, message reports, and number status. All requests authenticate with an api_key passed in the request body or query string.
finops:
- name: Termii Finops
  service_category: Communications and Messaging
  slug: termii-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/termii.png
layout: provider
modified: '2026-06-20'
name: Termii
nav: Providers
network: true
overview: 'Termii publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Campaigns API, Contacts API, Insights API, and 3 more. Tagged areas include Messaging, SMS, OTP, WhatsApp, and Verification.


  Termii''s developer surface includes authentication, documentation, and 7 more developer resources.'
plans:
- name: Termii Plans Pricing
  plan_count: 2
  slug: termii-plans-pricing
random_paper: 85
rate_limits:
- limit_count: 4
  name: Termii Rate Limits
  slug: termii-rate-limits
score:
  band: thin
  composite: 33.4
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 33.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/termii/refs/heads/main/screenshots/termii-2026-06-20T195127.png
security:
- kind: authentication
  name: Termii Authentication
  slug: termii-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Termii Domain Security
  slug: termii-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: termii
tags:
- Messaging
- SMS
- OTP
- WhatsApp
- Verification
website: https://termii.com
---

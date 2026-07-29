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
- acting_count: 22
  human_in_the_loop: 0
  name: Clicksend Agentic Access
  operation_count: 42
  slug: clicksend-agentic-access
  summary_line: 42 operations · 22 acting
api_count: 10
apis:
- description: Account details, usage, and balance.
  name: ClickSend Account API
  slug: clicksend-account-api
- description: Manage contacts.
  name: ClickSend Contact API
  slug: clicksend-contact-api
- description: Manage contact lists.
  name: ClickSend ContactList API
  slug: clicksend-contactlist-api
- description: Send and view transactional email.
  name: ClickSend Email API
  slug: clicksend-email-api
- description: Send and view MMS messages.
  name: ClickSend MMS API
  slug: clicksend-mms-api
- description: Print and mail physical letters.
  name: ClickSend Post Letter API
  slug: clicksend-post-letter-api
- description: Print and mail physical postcards.
  name: ClickSend Post Postcard API
  slug: clicksend-post-postcard-api
- description: Delivery receipts, inbound messages, and automations.
  name: ClickSend Receipts API
  slug: clicksend-receipts-api
- description: Send and view SMS messages.
  name: ClickSend SMS API
  slug: clicksend-sms-api
- description: Send and view voice (text-to-speech) messages.
  name: ClickSend Voice API
  slug: clicksend-voice-api
artifact_total: 18
collections:
- collection_type: open
  name: ClickSend v3 API
  slug: open-clicksend
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clicksend-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/clicksend-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clicksend-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clicksend-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClickSend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/clicksend
- group: company
  title: ''
  type: Website
  url: https://www.clicksend.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.clicksend.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/clicksend-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/clicksend-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/clicksend-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.clicksend.com/
created: '2026-07-01'
description: ClickSend is a cloud communications company providing a single REST API for business messaging across SMS, MMS, voice / text-to-speech, transactional email, and physical post - letters and postcards printed and mailed globally. The v3 API (rest.clicksend.com/v3) uses HTTP Basic authentication with a username and API key and covers sending, delivery receipts, inbound handling, contacts and lists, and account balance.
finops:
- name: Clicksend Finops
  service_category: Communications
  slug: clicksend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/clicksend.png
layout: provider
modified: '2026-07-01'
name: ClickSend
nav: Providers
network: true
overview: 'ClickSend publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account API, Contact API, ContactList API, and 7 more. Tagged areas include Communications, SMS, MMS, Voice, and Email.


  ClickSend''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Clicksend Plans Pricing
  plan_count: 3
  slug: clicksend-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 3
  name: Clicksend Rate Limits
  slug: clicksend-rate-limits
score:
  band: thin
  composite: 36.6
  delta: -5.3
  facets:
    commercial_clarity: 47.4
    contract_quality: 51.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 41.9
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
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/clicksend/refs/heads/main/screenshots/clicksend-2026-07-25T205619.png
security:
- kind: authentication
  name: Clicksend Authentication
  slug: clicksend-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clicksend Domain Security
  slug: clicksend-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Clicksend Trust Center
  slug: clicksend-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
slug: clicksend
tags:
- Communications
- SMS
- MMS
- Voice
- Email
- Post
- Messaging
- CPaaS
website: https://www.clicksend.com/
---

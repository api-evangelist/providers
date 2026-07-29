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
- acting_count: 17
  human_in_the_loop: 0
  name: Messente Agentic Access
  operation_count: 28
  slug: messente-agentic-access
  summary_line: 28 operations · 17 acting
api_count: 11
apis:
- description: Retrieve the current account balance.
  name: Messente Account Balance API
  slug: messente-account-balance-api
- description: Manage the phone number blacklist.
  name: Messente Blacklist API
  slug: messente-blacklist-api
- description: Send an Omnimessage to many recipients in a single request.
  name: Messente Bulk Messaging API
  slug: messente-bulk-messaging-api
- description: Manage contacts in the Messente Phonebook.
  name: Messente Contacts API
  slug: messente-contacts-api
- description: Retrieve delivery status for a sent Omnimessage.
  name: Messente Delivery Report API
  slug: messente-delivery-report-api
- description: Manage contact groups in the Messente Phonebook.
  name: Messente Groups API
  slug: messente-groups-api
- description: Fetch HLR / network information about phone numbers.
  name: Messente Number Lookup API
  slug: messente-number-lookup-api
- description: PIN-based phone number verification (2FA / one-time passwords).
  name: Messente Number Verification API
  slug: messente-number-verification-api
- description: Send SMS, Viber, WhatsApp, and Telegram messages with an automatic fallback chain.
  name: Messente Omnimessage API
  slug: messente-omnimessage-api
- description: Retrieve account pricelist and per-country prices.
  name: Messente Pricing API
  slug: messente-pricing-api
- description: Request messaging statistics reports by country.
  name: Messente Statistics API
  slug: messente-statistics-api
artifact_total: 19
collections:
- collection_type: open
  name: Messente API
  slug: open-messente
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/messente-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/messente-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/messente-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/messente-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/messente
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/messente
- group: company
  title: ''
  type: Website
  url: https://messente.com/
- group: docs
  title: ''
  type: Documentation
  url: https://messente.com/documentation
- group: commercial
  title: ''
  type: Plans
  url: plans/messente-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/messente-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/messente-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://messente.com/blog
created: '2026-07-01'
description: Messente is an Estonian CPaaS provider of global messaging and user verification services. A single Omnimessage endpoint sends SMS, Viber, WhatsApp, and Telegram with an automatic fallback chain, backed by contacts and groups in the Phonebook, phone number (HLR) lookup, PIN-based number verification / 2FA, delivery reports, and messaging statistics over an HTTP Basic authenticated REST API at api.messente.com/v1.
finops:
- name: Messente Finops
  service_category: Communication and Messaging
  slug: messente-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/messente.png
layout: provider
modified: '2026-07-01'
name: Messente
nav: Providers
network: true
overview: 'Messente publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Account Balance API, Blacklist API, Bulk Messaging API, and 8 more. Tagged areas include CPaaS, Messaging, SMS, Viber, and WhatsApp.


  Messente''s developer surface includes authentication, documentation, engineering blog, and 9 more developer resources.'
plans:
- name: Messente Plans Pricing
  plan_count: 2
  slug: messente-plans-pricing
random_paper: 78
rate_limits:
- limit_count: 3
  name: Messente Rate Limits
  slug: messente-rate-limits
score:
  band: thin
  composite: 35.4
  delta: -4.2
  facets:
    commercial_clarity: 36.8
    contract_quality: 54.3
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 39.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 23.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: authentication
  name: Messente Authentication
  slug: messente-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Messente Domain Security
  slug: messente-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: trust-center
  name: Messente Trust Center
  slug: messente-trust-center
  summary_line: ISO 27001, GDPR
slug: messente
tags:
- CPaaS
- Messaging
- SMS
- Viber
- WhatsApp
- Verification
- 2FA
website: https://messente.com/
---

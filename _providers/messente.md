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
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 17
  human_in_the_loop: 0
  name: Messente Agentic Access
  operation_count: 28
  slug: messente-agentic-access
  summary_line: 28 operations · 17 acting
api_count: 1
apis:
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Retrieve the current account balance.
  name: Messente Account Balance API
  slug: messente-account-balance-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Manage the phone number blacklist.
  name: Messente Blacklist API
  slug: messente-blacklist-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Send an Omnimessage to many recipients in a single request.
  name: Messente Bulk Messaging API
  slug: messente-bulk-messaging-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Manage contacts in the Messente Phonebook.
  name: Messente Contacts API
  slug: messente-contacts-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Retrieve delivery status for a sent Omnimessage.
  name: Messente Delivery Report API
  slug: messente-delivery-report-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Manage contact groups in the Messente Phonebook.
  name: Messente Groups API
  slug: messente-groups-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Fetch HLR / network information about phone numbers.
  name: Messente Number Lookup API
  slug: messente-number-lookup-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: PIN-based phone number verification (2FA / one-time passwords).
  name: Messente Number Verification API
  slug: messente-number-verification-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Send SMS, Viber, WhatsApp, and Telegram messages with an automatic fallback chain.
  name: Messente Omnimessage API
  slug: messente-omnimessage-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Retrieve account pricelist and per-country prices.
  name: Messente Pricing API
  slug: messente-pricing-api
- baseURL: https://api.messente.com/v1
  baseurl_source: declared
  description: Request messaging statistics reports by country.
  name: Messente Statistics API
  slug: messente-statistics-api
artifact_total: 31
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Messente Account Balance API
  slug: open-messente-account-balance-api
- collection_type: open
  name: Messente Account Balance Blacklist API
  slug: open-messente-blacklist-api
- collection_type: open
  name: Messente Account Balance Bulk Messaging API
  slug: open-messente-bulk-messaging-api
- collection_type: open
  name: Messente Account Balance Contacts API
  slug: open-messente-contacts-api
- collection_type: open
  name: Messente Account Balance Delivery Report API
  slug: open-messente-delivery-report-api
- collection_type: open
  name: Messente Account Balance Groups API
  slug: open-messente-groups-api
- collection_type: open
  name: Messente Account Balance Number Lookup API
  slug: open-messente-number-lookup-api
- collection_type: open
  name: Messente Account Balance Number Verification API
  slug: open-messente-number-verification-api
- collection_type: open
  name: Messente Account Balance Omnimessage API
  slug: open-messente-omnimessage-api
- collection_type: open
  name: Messente Account Balance Pricing API
  slug: open-messente-pricing-api
- collection_type: open
  name: Messente Account Balance Statistics API
  slug: open-messente-statistics-api
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
random_paper: 7
rate_limits:
- limit_count: 3
  name: Messente Rate Limits
  slug: messente-rate-limits
score:
  band: thin
  composite: 37.5
  coverage:
    artifact_dirs: 10
    catalog_gap: 55.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 36.8
    commercial_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 54.1
    developer_ergonomics: 31.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 34.2
  previous_composite: 37.5
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
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/messente/refs/heads/main/screenshots/messente-2026-08-07T172635.png
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

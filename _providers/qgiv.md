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
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Qgiv Agentic Access
  operation_count: 34
  slug: qgiv-agentic-access
  summary_line: 34 operations · 23 acting
api_count: 10
apis:
- description: Confirmed. Read and update organization and form settings.
  name: Qgiv Account Settings API
  slug: qgiv-account-settings-api
- description: Confirmed. Manage preset suggested-giving amounts.
  name: Qgiv Custom Amounts API
  slug: qgiv-custom-amounts-api
- description: Confirmed. Manage custom fields on a donation form.
  name: Qgiv Custom Fields API
  slug: qgiv-custom-fields-api
- description: Confirmed. Manage fundraising/ticketed events.
  name: Qgiv Events API
  slug: qgiv-events-api
- description: Confirmed. Manage export/report mappings to external systems.
  name: Qgiv Mappings API
  slug: qgiv-mappings-api
- description: Confirmed. Read-only reporting on recurring donation schedules.
  name: Qgiv Recurring API
  slug: qgiv-recurring-api
- description: Confirmed. Read-only reporting on refunds.
  name: Qgiv Refunds API
  slug: qgiv-refunds-api
- description: Confirmed. Read-only reporting on peer-to-peer registrations.
  name: Qgiv Registrations API
  slug: qgiv-registrations-api
- description: Confirmed. Read-only reporting on monthly processing statements.
  name: Qgiv Statements API
  slug: qgiv-statements-api
- description: Confirmed. Read-only reporting on donation transactions.
  name: Qgiv Transactions API
  slug: qgiv-transactions-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Qgiv Account Settings API
  slug: open-qgiv-account-settings-api
- collection_type: open
  name: Qgiv Account Settings Custom Amounts API
  slug: open-qgiv-custom-amounts-api
- collection_type: open
  name: Qgiv Account Settings Custom Fields API
  slug: open-qgiv-custom-fields-api
- collection_type: open
  name: Qgiv Account Settings Events API
  slug: open-qgiv-events-api
- collection_type: open
  name: Qgiv Account Settings Mappings API
  slug: open-qgiv-mappings-api
- collection_type: open
  name: Qgiv Account Settings Recurring API
  slug: open-qgiv-recurring-api
- collection_type: open
  name: Qgiv Account Settings Refunds API
  slug: open-qgiv-refunds-api
- collection_type: open
  name: Qgiv Account Settings Registrations API
  slug: open-qgiv-registrations-api
- collection_type: open
  name: Qgiv Account Settings Statements API
  slug: open-qgiv-statements-api
- collection_type: open
  name: Qgiv Account Settings Transactions API
  slug: open-qgiv-transactions-api
- collection_type: open
  name: Qgiv API
  slug: open-qgiv
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/qgiv-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/qgiv-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/qgiv-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/qgiv-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/qgiv
- group: company
  title: ''
  type: Website
  url: https://www.qgiv.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.qgiv.com/api/
- group: commercial
  title: ''
  type: Plans
  url: plans/qgiv-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/qgiv-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/qgiv-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.qgiv.com/blog/feed/
created: '2026-07-03'
description: Qgiv (now Bloomerang Fundraising) is an online donation, event registration, peer-to-peer fundraising, and payment processing platform for nonprofits, faith-based organizations, and schools. Qgiv was acquired by Bloomerang in January 2024 and now operates as Bloomerang's giving platform; the legacy Qgiv API documentation lives at qgiv.com/api and remains the documented programmatic surface for existing Qgiv forms and accounts. The API is a token-authenticated, form-scoped REST-style service at secure.qgiv.com/admin/api that accepts XML or JSON input and returns XML or JSON based on the URL extension, covering transactions, recurring donations, refunds, peer-to-peer registrations, events, account settings, custom fields, custom amounts, statements, and report mappings.
finops:
- name: Qgiv Finops
  service_category: Nonprofit Fundraising and Payments
  slug: qgiv-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/qgiv.png
layout: provider
modified: '2026-07-03'
name: Qgiv
nav: Providers
network: true
overview: 'Qgiv publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Account Settings API, Custom Amounts API, Custom Fields API, and 7 more. Tagged areas include Nonprofit, Fundraising, Donations, Payments, and Peer to Peer.


  Qgiv''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Qgiv Plans Pricing
  plan_count: 4
  slug: qgiv-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 3
  name: Qgiv Rate Limits
  slug: qgiv-rate-limits
score:
  band: thin
  composite: 37.6
  delta: 0.5
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 37.1
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
    regime: Payments
    regime_id: payments
    score: 26.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
security:
- kind: authentication
  name: Qgiv Authentication
  slug: qgiv-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Qgiv Domain Security
  slug: qgiv-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Qgiv Trust Center
  slug: qgiv-trust-center
  summary_line: SOC 2, ISO 27001
slug: qgiv
tags:
- Nonprofit
- Fundraising
- Donations
- Payments
- Peer to Peer
- Events
- Bloomerang
website: https://www.qgiv.com/
---

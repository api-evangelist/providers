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
  band: agent-ready
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
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 29
  human_in_the_loop: 0
  name: Provet Cloud Agentic Access
  operation_count: 55
  slug: provet-cloud-agentic-access
  summary_line: 55 operations · 29 acting
api_count: 7
apis:
- description: Appointments and online booking.
  name: Provet Cloud Appointments API
  slug: provet-cloud-appointments-api
- description: Invoices, refunds, and payments.
  name: Provet Cloud Billing API
  slug: provet-cloud-billing-api
- description: Animal owners / bill payers.
  name: Provet Cloud Clients API
  slug: provet-cloud-clients-api
- description: Clinical visits and their items.
  name: Provet Cloud Consultations API
  slug: provet-cloud-consultations-api
- description: The animals under care.
  name: Provet Cloud Patients API
  slug: provet-cloud-patients-api
- description: Items, departments, users, and code lists.
  name: Provet Cloud Reference Data API
  slug: provet-cloud-reference-data-api
- description: Event subscriptions.
  name: Provet Cloud Webhooks API
  slug: provet-cloud-webhooks-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Provet Cloud REST Appointments API
  slug: open-provet-cloud-appointments-api
- collection_type: open
  name: Provet Cloud REST Appointments Billing API
  slug: open-provet-cloud-billing-api
- collection_type: open
  name: Provet Cloud REST Appointments Clients API
  slug: open-provet-cloud-clients-api
- collection_type: open
  name: Provet Cloud REST Appointments Consultations API
  slug: open-provet-cloud-consultations-api
- collection_type: open
  name: Provet Cloud REST Appointments Patients API
  slug: open-provet-cloud-patients-api
- collection_type: open
  name: Provet Cloud REST Appointments Reference Data API
  slug: open-provet-cloud-reference-data-api
- collection_type: open
  name: Provet Cloud REST Appointments Webhooks API
  slug: open-provet-cloud-webhooks-api
- collection_type: open
  name: Provet Cloud REST API
  slug: open-provet-cloud
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/provet-cloud-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/provet-cloud-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/provet-cloud-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/provet-cloud-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/provetcloud
- group: company
  title: ''
  type: Website
  url: https://www.provet.cloud
- group: docs
  title: ''
  type: Documentation
  url: https://developers.provetcloud.com/restapi/
- group: commercial
  title: ''
  type: Plans
  url: plans/provet-cloud-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/provet-cloud-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/provet-cloud-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.provet.com/blog
created: '2026-07-03'
description: Provet Cloud is a cloud-based veterinary practice management system (PIMS) built by Nordhealth for animal clinics, hospitals, and referral practices. It exposes a documented REST API (base https://provetcloud.com/<provet_id>/api/0.1/, regional domains such as us.provetcloud.com) that gives approved integration partners programmatic access to clients, patients (animals), consultations, appointments and online booking, invoicing and payments, items, and reference data, plus a webhook system with 60+ triggers for reacting to changes in a Provet Cloud installation. Access is OAuth 2.0 authorized (Client Credentials for backend services, Authorization Code with PKCE for user-facing apps); integrations are registered and approved by Provet's support team per installation. The documentation at developers.provetcloud.com is freely browsable by any customer or developer.
finops:
- name: Provet Cloud Finops
  service_category: Business Application Software (Veterinary PIMS)
  slug: provet-cloud-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/provet-cloud.png
layout: provider
modified: '2026-07-03'
name: Provet Cloud
nav: Providers
network: true
overview: 'Provet Cloud publishes 7 APIs on the [APIs.io](https://apis.io/) network, including Appointments API, Billing API, Clients API, and 4 more. Tagged areas include Veterinary, Practice Management, PIMS, Healthcare, and Nordhealth.


  Provet Cloud''s developer surface includes authentication, documentation, engineering blog, and 8 more developer resources.'
plans:
- name: Provet Cloud Plans Pricing
  plan_count: 3
  slug: provet-cloud-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 3
  name: Provet Cloud Rate Limits
  slug: provet-cloud-rate-limits
scopes:
- name: Provet Cloud Scopes
  scope_count: 2
  slug: provet-cloud-scopes
  summary_line: 2 scopes · clientCredentials/authorizationCode
score:
  band: developing
  composite: 39.8
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 52.1
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 39.8
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
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
security:
- kind: authentication
  name: Provet Cloud Authentication
  slug: provet-cloud-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Provet Cloud Domain Security
  slug: provet-cloud-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: provet-cloud
tags:
- Veterinary
- Practice Management
- PIMS
- Healthcare
- Nordhealth
- Animal Health
- Appointments
- Billing
website: https://www.provet.cloud
---

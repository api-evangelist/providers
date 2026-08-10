---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
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
  score: 19.4
  scored_at: '2026-08-10'
api_count: 6
apis:
- description: List the studies available to your account and read their configuration - domains, enabled features, reason-for-data-change options, and the reference data a study is built from (sites, roles, groups,
  name: Medrio Studies API
  slug: medrio-studies-api
- description: Create, list, and update clinical trial subjects within a study; manage Medrio and study subject identifiers (including their ePRO variants), activate or deactivate subjects, and list deleted subjects
  name: Medrio Subjects API
  slug: medrio-subjects-api
- description: Read and write electronic case report form (eCRF) data - list a subject's visits, create subject visits from a template, submit and update data entry at the study or form/visit level, and clear a form
  name: Medrio Data Entry API
  slug: medrio-data-entry-api
- description: Administer the account user profile and per-study memberships - read and update your user, change password, list study users, add users to a study, assign or remove roles and site access, and remove a
  name: Medrio Users and Memberships API
  slug: medrio-users-memberships-api
- description: Configure event subscriptions for a study - read the available events configuration, then create, list, update, and delete subscriptions so downstream systems are notified of study events. The push/no
  name: Medrio Subscriptions API
  slug: medrio-subscriptions-api
- description: The V2 REST API behind Medrio's mSource eCOA/ePRO applications (mPRO and mCapture) - read study configuration, files, and users; read and write subject, form, and approval data with an asynchronous ke
  name: Medrio mSource API
  slug: medrio-msource-api
artifact_total: 10
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medrio-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medrio.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/medrio
- group: docs
  title: ''
  type: Documentation
  url: https://community.medrio.com/documentation/home
- group: docs
  title: ''
  type: APIReference
  url: https://connectapi.medrio.com/swagger/index.html
- group: docs
  title: ''
  type: OpenAPI
  url: https://connectapi.medrio.com/swagger/v1/swagger.json
- group: start
  title: ''
  type: SignUp
  url: https://medrio.com/contact/
- group: commercial
  title: ''
  type: Plans
  url: plans/medrio-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/medrio-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/medrio-finops.yml
created: '2026-07-05'
description: Medrio is an eClinical / electronic data capture (EDC) platform built for small and scaling life sciences teams, spanning EDC, ePRO/eCOA, eConsent, and RTSM for clinical trials across pharma, biotech, medtech, and diagnostics. Medrio exposes documented REST APIs for integration and data exchange. Medrio API Connect (connectapi.medrio.com) covers study configuration, subject enrollment and identifiers, eCRF form data entry, user and membership administration, reference data (sites, roles, groups, subject statuses), and event subscriptions; it ships a live OpenAPI 3.0 description and Swagger UI. The mSource API (esource.medrio.com) backs the mPRO and mCapture eCOA/ePRO applications for subject-, form-, and approval-level source data capture, including offline access. Both surfaces are request/response REST over HTTPS secured with OAuth 2.0; actual use is gated to Medrio customers with study credentials, and commercial pricing is per-study / contact-sales.
finops:
- name: Medrio Finops
  service_category: eClinical and Electronic Data Capture
  slug: medrio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medrio.png
layout: provider
modified: '2026-07-05'
name: Medrio
nav: Providers
network: true
overview: 'Medrio publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Studies API, Subjects API, Data Entry API, and 2 more. Tagged areas include Clinical Trials, Electronic Data Capture, EDC, eClinical, and ePRO.


  Medrio''s developer surface includes documentation, API reference, signup flow, and 7 more developer resources.'
plans:
- name: Medrio Plans Pricing
  plan_count: 1
  slug: medrio-plans-pricing
random_paper: 60
rate_limits:
- limit_count: 3
  name: Medrio Rate Limits
  slug: medrio-rate-limits
score:
  band: emerging
  composite: 27.5
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 32.3
    developer_ergonomics: 15.2
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 27.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medrio/refs/heads/main/screenshots/medrio-2026-08-07T172404.png
security:
- kind: domain-security
  name: Medrio Domain Security
  slug: medrio-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medrio
tags:
- Clinical Trials
- Electronic Data Capture
- EDC
- eClinical
- ePRO
- eCOA
- Clinical Data
- Life Sciences
- Healthcare
website: https://medrio.com
---

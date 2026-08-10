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
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rxnt Agentic Access
  operation_count: 3
  slug: rxnt-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 2
apis:
- description: Obtain a time-limited token and signature.
  name: RXNT Authentication API
  slug: rxnt-authentication-api
- description: Retrieve patient CCDS clinical data.
  name: RXNT Clinical Data API
  slug: rxnt-clinical-data-api
artifact_total: 5
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rxnt-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rxnt-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RXNT
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rxnt
- group: company
  title: ''
  type: Website
  url: https://www.rxnt.com/
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/RXNT/RxNTClinicalDataAPI
- group: commercial
  title: ''
  type: Plans
  url: plans/rxnt-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.rxnt.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.rxnt.com/blog/
created: '2026-07-04'
description: RXNT is a cloud-based, integrated healthcare software company offering ONC-certified Electronic Health Records (EHR), EPCS-enabled electronic prescribing (eRx), practice management, medical billing, scheduling, and a patient portal for outpatient practices. Most of the RXNT platform is delivered as SaaS with no broadly published developer API - product integrations (labs, radiology, billing clearinghouses) are arranged privately with partners. The one documented, publicly described API is the RXNT Clinical Data API (CDAPI), an ONC-mandated interface that lets registered third-party applications retrieve a patient's Common Clinical Data Set (CCDS). Access to the CDAPI is gated - third parties must register with RXNT (support@rxnt.com) to receive credentials before calling it.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rxnt.png
layout: provider
modified: '2026-07-04'
name: RXNT
nav: Providers
network: true
overview: 'RXNT publishes 2 APIs on the [APIs.io](https://apis.io/) network: Authentication API and Clinical Data API. Tagged areas include Healthcare, EHR, E-Prescribing, Clinical Data, and ONC Certified.


  RXNT''s developer surface includes documentation, pricing, engineering blog, and 6 more developer resources.'
plans:
- name: Rxnt Plans Pricing
  plan_count: 4
  slug: rxnt-plans-pricing
random_paper: 112
score:
  band: thin
  composite: 28.9
  delta: 0.0
  facets:
    commercial_clarity: 42.1
    contract_quality: 58.1
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 28.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
security:
- kind: domain-security
  name: Rxnt Domain Security
  slug: rxnt-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rxnt
tags:
- Healthcare
- EHR
- E-Prescribing
- Clinical Data
- ONC Certified
- CCDS
- Medical Billing
- Practice Management
website: https://www.rxnt.com/
---

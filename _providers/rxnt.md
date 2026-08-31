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
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 14.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rxnt Agentic Access
  operation_count: 3
  slug: rxnt-agentic-access
  summary_line: 3 operations · 3 acting
api_count: 1
apis:
- description: Obtain a time-limited token and signature.
  name: RXNT Authentication API
  slug: rxnt-authentication-api
- description: Retrieve patient CCDS clinical data.
  name: RXNT Clinical Data API
  slug: rxnt-clinical-data-api
artifact_total: 8
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RXNT Clinical Data Authentication API
  slug: open-rxnt-authentication-api
- collection_type: open
  name: RXNT Authentication Clinical Data API
  slug: open-rxnt-clinical-data-api
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
random_paper: 19
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 6
    catalog_gap: 66.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 42.1
    commercial_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 12.8
    developer_ergonomics: 19.0
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 20.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-08-30'
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

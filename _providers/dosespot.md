---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Dosespot Agentic Access
  operation_count: 17
  slug: dosespot-agentic-access
  summary_line: 17 operations · 6 acting
api_count: 6
apis:
- description: Medi-Span drug search and interaction checks.
  name: DoseSpot Medications API
  slug: dosespot-medications-api
- description: Clinician notification counts and actionable items.
  name: DoseSpot Notifications API
  slug: dosespot-notifications-api
- description: Patient demographics, allergies, and self-reported medications.
  name: DoseSpot Patients API
  slug: dosespot-patients-api
- description: Surescripts pharmacy search and patient pharmacy management.
  name: DoseSpot Pharmacies API
  slug: dosespot-pharmacies-api
- description: Clinician (prescriber) and clinic staff management.
  name: DoseSpot Prescribers API
  slug: dosespot-prescribers-api
- description: Prescription creation, transmission, status, and medication history.
  name: DoseSpot Prescriptions API
  slug: dosespot-prescriptions-api
artifact_total: 13
collections:
- collection_type: open
  name: DoseSpot API
  slug: open-dosespot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/dosespot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dosespot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/dosespot-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dosespot
- group: company
  title: ''
  type: Website
  url: https://www.dosespot.com
- group: docs
  title: ''
  type: Documentation
  url: https://dosespot.com/full-integration/
- group: commercial
  title: ''
  type: Plans
  url: plans/dosespot-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/dosespot-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/dosespot-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://dosespot.com/feed/
created: '2026-06-21'
description: DoseSpot is a Surescripts- and EPCS-certified electronic prescribing (eRx) platform. Its REST API (v2) lets healthcare and EHR/EMR software embed the full prescription lifecycle - patient and clinician management, medication and drug search, pharmacy selection, e-prescribing, medication history, eligibility, and push notifications - using OAuth2 Bearer tokens scoped by clinic and clinician keys.
finops:
- name: Dosespot Finops
  service_category: Healthcare
  slug: dosespot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/dosespot.png
layout: provider
modified: '2026-06-21'
name: DoseSpot
nav: Providers
network: true
overview: 'DoseSpot publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Medications API, Notifications API, Patients API, and 3 more. Tagged areas include e-Prescribing, eRx, Healthcare, EHR, and Pharmacy.


  DoseSpot''s developer surface includes authentication, documentation, engineering blog, and 7 more developer resources.'
plans:
- name: Dosespot Plans Pricing
  plan_count: 2
  slug: dosespot-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 1
  name: Dosespot Rate Limits
  slug: dosespot-rate-limits
score:
  band: thin
  composite: 32.3
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 60.5
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 32.3
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
    regime: Health
    regime_id: health
    score: 15.0
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dosespot/refs/heads/main/screenshots/dosespot-2026-07-25T212312.png
security:
- kind: authentication
  name: Dosespot Authentication
  slug: dosespot-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Dosespot Domain Security
  slug: dosespot-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: dosespot
tags:
- e-Prescribing
- eRx
- Healthcare
- EHR
- Pharmacy
- EPCS
website: https://www.dosespot.com
---

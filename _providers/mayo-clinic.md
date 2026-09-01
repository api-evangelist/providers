---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-01'
api_count: 1
apis:
- description: Review and try the existing APIs in the Mayo Clinic Apigee API catalog portal. Provides programmatic access to healthcare data and clinical services.
  name: Mayo Clinic API
  slug: mayo-clinic-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mayo-clinic-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mayo-clinic
- group: start
  title: ''
  type: Portal
  url: https://apiportal.mcc.mayo.edu/
- group: company
  title: ''
  type: Website
  url: https://www.mayoclinic.org/
created: '2025-02-12'
description: Mayo Clinic provides a developer API portal with access to clinical and healthcare APIs hosted on an Apigee API catalog. Developers can review, test, and integrate with available APIs for healthcare data and services.
finops:
- name: Mayo Clinic Finops
  service_category: API
  slug: mayo-clinic-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mayo-clinic.png
layout: provider
modified: '2026-04-28'
name: Mayo Clinic
nav: Providers
network: true
overview: 'Mayo Clinic publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Clinical Data, Healthcare, Hospital, and Medical.


  Mayo Clinic''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: Mayo Clinic Plans Pricing
  plan_count: 3
  slug: mayo-clinic-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Mayo Clinic Rate Limits
  slug: mayo-clinic-rate-limits
score:
  band: minimal
  composite: 10.4
  coverage:
    artifact_dirs: 5
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 10.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mayo-clinic/refs/heads/main/screenshots/mayo-clinic-2026-06-20T185105.png
security:
- kind: domain-security
  name: Mayo Clinic Domain Security
  slug: mayo-clinic-domain-security
  summary_line: TLSv1.3 · DMARC
slug: mayo-clinic
tags:
- Clinical Data
- Healthcare
- Hospital
- Medical
website: https://www.mayoclinic.org/
---

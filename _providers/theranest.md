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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/theranest-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ensora-health
- group: company
  title: ''
  type: Website
  url: https://theranest.com
- group: docs
  title: ''
  type: Documentation
  url: https://theranest.zendesk.com/hc/en-us
- group: commercial
  title: ''
  type: Plans
  url: plans/theranest-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/theranest-finops.yml
- group: other
  title: ''
  type: ProductPage
  url: https://ensorahealth.com/product/mental-health/
created: '2026-07-10'
description: TheraNest (now marketed as Ensora Mental Health) is a behavioral and mental health practice management and EHR platform for therapists, counselors, psychologists, and social workers. It covers client intake, scheduling, telehealth, clinical documentation and notes, treatment plans, client portals, insurance billing and claims, and reporting. TheraNest is the flagship mental health product of Ensora Health (formerly Therapy Brands). As of this review, Ensora does not publish a documented, self-serve public developer API for TheraNest - integration is via partnerships, HIPAA-gated interoperability, and contact-sales arrangements rather than an open developer portal. The API entries below are logical resource groupings modeled from the product surface; their endpoints are NOT documented public endpoints (endpointsModeled true).
finops:
- name: Theranest Finops
  service_category: Healthcare Practice Management and EHR
  slug: theranest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/theranest.png
layout: provider
modified: '2026-07-25'
name: TheraNest
nav: Providers
network: true
overview: 'TheraNest is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, Mental Health, EHR, Practice Management, and Healthcare.


  TheraNest''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Theranest Plans Pricing
  plan_count: 5
  slug: theranest-plans-pricing
random_paper: 8
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 3
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Theranest Domain Security
  slug: theranest-domain-security
  summary_line: TLSv1.3 · DMARC
slug: theranest
tags:
- Behavioral Health
- Mental Health
- EHR
- Practice Management
- Healthcare
- HIPAA
- Telehealth
- Ensora Health
- Therapy Brands
website: https://theranest.com
---

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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 4
apis:
- description: Logical grouping for client records - demographics, contacts, insurance policies, diagnoses, and client-portal status. Modeled from the TheraNest product surface; no documented public endpoints exist.
  name: TheraNest Clients API
  slug: theranest-clients-api
- description: Logical grouping for scheduling - appointments, recurring sessions, telehealth session settings, service codes, and reminders. Modeled from the TheraNest product surface; no documented public endpoint
  name: TheraNest Appointments API
  slug: theranest-appointments-api
- description: Logical grouping for clinical documentation - progress notes, treatment plans, note templates, and sign-off / locking. Modeled from the TheraNest product surface; no documented public endpoints exist.
  name: TheraNest Clinical Notes API
  slug: theranest-clinical-notes-api
- description: Logical grouping for billing and revenue cycle - invoices, payments, insurance eligibility and authorizations, CMS-1500 / 837P claim assembly, and clearinghouse routing. Modeled from the TheraNest pro
  name: TheraNest Billing and Claims API
  slug: theranest-billing-claims-api
artifact_total: 7
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
created: '2026-07-10'
description: TheraNest (now marketed as Ensora Mental Health) is a behavioral and mental health practice management and EHR platform for therapists, counselors, psychologists, and social workers. It covers client intake, scheduling, telehealth, clinical documentation and notes, treatment plans, client portals, insurance billing and claims, and reporting. TheraNest is the flagship mental health product of Ensora Health (formerly Therapy Brands). As of this review, Ensora does not publish a documented, self-serve public developer API for TheraNest - integration is via partnerships, HIPAA-gated interoperability, and contact-sales arrangements rather than an open developer portal. The API entries below are logical resource groupings modeled from the product surface; their endpoints are NOT documented public endpoints (endpointsModeled true).
finops:
- name: Theranest Finops
  service_category: Healthcare Practice Management and EHR
  slug: theranest-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/theranest.png
layout: provider
modified: '2026-07-10'
name: TheraNest
nav: Providers
network: true
overview: 'TheraNest publishes 4 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Behavioral Health, Mental Health, EHR, Practice Management, and Healthcare.


  TheraNest''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Theranest Plans Pricing
  plan_count: 5
  slug: theranest-plans-pricing
random_paper: 5
score:
  band: emerging
  composite: 17.6
  delta: -0.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 18.4
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 13.0
  schema_version: 0.5
  scored_at: '2026-07-23'
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

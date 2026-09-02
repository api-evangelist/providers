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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-01'
api_count: 3
apis:
- description: 'Modeled product-area API for client/patient records - the people a practice serves, their demographics, contact details, and intake information. endpointsModeled: true. Carepatron does not publish a d'
  name: Carepatron Clients API (Modeled)
  slug: carepatron-clients-api
- description: 'Modeled product-area API for clinical notes, forms, intakes, templates, and AI-assisted documentation (the AI scribe / note taker). endpointsModeled: true. Carepatron does not publish a developer API '
  name: Carepatron Notes and Documentation API (Modeled)
  slug: carepatron-notes-api
- description: 'Modeled product-area API for billing - invoices, payments, and insurance claim management. endpointsModeled: true. Carepatron does not publish a developer API for this surface; there is no documented '
  name: Carepatron Billing API (Modeled)
  slug: carepatron-billing-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/carepatron-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/carepatron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.carepatron.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/carepatron
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Carepatron
- group: docs
  title: ''
  type: Documentation
  url: https://help.carepatron.com/en/
- group: commercial
  title: ''
  type: Plans
  url: plans/carepatron-plans-pricing.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://www.carepatron.com/pricing/
created: '2026-07-10'
description: Carepatron is a cloud-based healthcare practice management and EHR platform for therapists, counselors, psychologists, health coaches, nutritionists, and other practitioners. It brings client records, appointment scheduling and online booking, telehealth, AI-assisted clinical notes and documentation, and billing/invoicing with insurance claims into one workspace, and markets HIPAA/SOC/GDPR compliance across 100,000+ clinicians in 120+ countries. As of this review Carepatron does NOT publish a documented public developer API - its pricing page lists "API (coming soon)" on the Advanced plan, and there is no developer portal, API reference, published base URL, OpenAPI definition, or SDK. Third-party connectivity today is limited to a handful of native integrations (Zoom, accounting software, Google Tag Manager). The APIs listed below are logical/product-area groupings modeled from Carepatron's own feature set; their endpoints are NOT documented and are marked as modeled, not confirmed.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/carepatron.png
layout: provider
modified: '2026-07-25'
name: Carepatron
nav: Providers
network: true
overview: 'Carepatron publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Practice Management, EHR, Therapy, and Telehealth.


  Carepatron''s developer surface includes documentation, pricing, and 6 more developer resources.'
plans:
- name: Carepatron Plans Pricing
  plan_count: 3
  slug: carepatron-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 18.0
  coverage:
    artifact_dirs: 3
    catalog_gap: 68.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 18.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/carepatron/refs/heads/main/screenshots/carepatron-2026-07-25T204552.png
security:
- kind: domain-security
  name: Carepatron Domain Security
  slug: carepatron-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Carepatron Trust Center
  slug: carepatron-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA, GDPR
slug: carepatron
tags:
- Healthcare
- Practice Management
- EHR
- Therapy
- Telehealth
- Scheduling
- Clinical Notes
- Medical Billing
website: https://www.carepatron.com
---

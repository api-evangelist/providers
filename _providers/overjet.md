---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  scored_at: '2026-08-26'
api_count: 5
apis:
- description: Modeled surface for submitting dental radiographs (bitewing, periapical, panoramic, CBCT) to Overjet's FDA-cleared Vision AI for analysis. In production this is fed by connector software and DICOM ima
  name: Overjet Vision AI Image Analysis API
  slug: overjet-image-analysis-api
- description: Modeled surface for retrieving structured AI findings for an analyzed radiograph - detected and outlined caries, calculus, bone level and bone-loss measurements, periapical radiolucencies (PARLs), and
  name: Overjet Detections & Findings API
  slug: overjet-detections-api
- description: Modeled surface for Overjet's automated dental insurance verification - checking patient eligibility and benefits and returning coverage details for a practice. Delivered as a product feature and paye
  name: Overjet Insurance Verification API
  slug: overjet-insurance-verification-api
- description: Modeled payer-side surface for AI-assisted dental claim review - Overjet's ReviewPASS applies Vision AI to attached radiographs to support automated approvals and reduce manual review and downcoding d
  name: Overjet Claims Review (ReviewPASS) API
  slug: overjet-claims-review-api
- description: Modeled surface for Overjet's DSO analytics - clinical and operational insights aggregated across practices and providers (diagnostic consistency, treatment acceptance, and utilization). Provided as a
  name: Overjet DSO Analytics API
  slug: overjet-analytics-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/overjet-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/overjet
- group: company
  title: ''
  type: Website
  url: https://www.overjet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.overjet.com/resources
- group: other
  title: ''
  type: SignIn
  url: https://clinic.overjet.ai/signin
- group: start
  title: ''
  type: Demo
  url: https://info.overjet.com/hp-book-your-demo
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.overjet.com/legal/trust-center
- group: company
  title: ''
  type: Blog
  url: https://www.overjet.com/blog
created: '2026-07-05'
description: Overjet is a dental AI platform that applies FDA-cleared computer vision to dental radiographs (bitewings, periapicals, panoramics, and CBCT) to detect, outline, and quantify oral health conditions - caries, calculus, bone level and bone loss, periapical radiolucencies (PARLs), and anatomical structures - for dental providers, DSOs, and insurance payers. Overjet is not a self-serve public API. Its AI is delivered as OEM/partner integrations embedded into imaging systems and practice management software (Open Dental, Dentrix, Dentrix Ascend/Enterprise, Eaglesoft, Oryx, CareStack, and others) via connector software and DICOM image routing, plus payer-side products for insurance verification and claim review (ReviewPASS). Any programmatic access is arranged privately under a partner or enterprise agreement; there is no public developer portal or published API reference as of this catalog entry. The APIs listed below are logical, honestly-modeled surfaces (endpointsModeled) representing
  the capabilities Overjet exposes to integration partners, not documented public endpoints.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/overjet.png
layout: provider
modified: '2026-07-05'
name: Overjet
nav: Providers
network: true
overview: 'Overjet publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Dental, Dental AI, Healthcare, Radiograph Analysis, and Computer-Vision.


  Overjet''s developer surface includes documentation, engineering blog, and 6 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 9.7
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.7
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/overjet/refs/heads/main/screenshots/overjet-2026-08-07T191136.png
security:
- kind: domain-security
  name: Overjet Domain Security
  slug: overjet-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: overjet
tags:
- Dental
- Dental AI
- Healthcare
- Radiograph Analysis
- Computer-Vision
- Medical Imaging
- Caries Detection
- Insurance
- Partner API
- Gated
website: https://www.overjet.com/
---

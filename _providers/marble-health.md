---
access_model:
  confidence: medium
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source: []
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
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/marble-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://marblehealth.com
- group: start
  title: ''
  type: SignUp
  url: https://app.marblehealth.com/refer
- group: start
  title: ''
  type: Login
  url: https://app.marblehealth.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.marblehealth.com/info-pdfs/Notice_of_Privacy_Practices.pdf
created: '2026-07-17'
description: Marble Health is a virtual mental-health company providing personalized therapy for K-12 students, delivered through partnerships with schools and school districts and directly to families. Licensed therapists meet with students over video, typically within a few days and with no waitlists, and the service accepts most insurance plans including Medicaid. The platform at app.marblehealth.com handles referrals and intake for school counselors and parents, and Marble Health also runs parent workshops and professional-development training for educators. The company is backed by Costanoa Ventures. As of this enrichment pass Marble Health exposes no public API, developer portal, or machine-readable discovery surface (no .well-known documents and no llms.txt); it is a consumer/patient-facing healthtech service rather than an API provider.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/marble-health.png
layout: provider
modified: '2026-07-20'
name: Marble Health
nav: Providers
network: true
overview: 'Marble Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthtech, Mental Health, Telehealth, and Therapy.


  Marble Health''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 27
score:
  band: minimal
  composite: 13.0
  delta: 1.5
  facets:
    commercial_clarity: 23.7
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 67.5
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 11.5
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 21.7
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Marble Health Domain Security
  slug: marble-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marble-health
tags:
- Company
- Healthtech
- Mental Health
- Telehealth
- Therapy
- Education
- Students
website: https://marblehealth.com
---

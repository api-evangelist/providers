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
overview: 'Marble Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Health Tech, Mental Health, Telehealth, and Therapy.


  Marble Health''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 8.4
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 23.7
    commercial_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 18.5
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/marble-health/refs/heads/main/screenshots/marble-health-2026-07-25T230131.png
security:
- kind: domain-security
  name: Marble Health Domain Security
  slug: marble-health-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: marble-health
tags:
- Company
- Health Tech
- Mental Health
- Telehealth
- Therapy
- Education
- Students
website: https://marblehealth.com
---

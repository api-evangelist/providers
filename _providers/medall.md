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
  scored_at: '2026-09-01'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://medall.org
- group: start
  title: ''
  type: SignUp
  url: https://app.medall.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://medall.org/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://medall.org/privacy
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medall-domain-security.yml
created: '2026-07-17'
description: MedAll is a UK-founded healthcare education platform on a mission to make medical education radically accessible. It hosts live and on-demand courses, conferences, workshops, webinars and training sessions for healthcare professionals, students and organisations, and provides event management tooling for registrations, feedback forms, certificates, abstracts, schedules and digital poster halls, alongside CME (continuing medical education), question banks and mobile apps for iOS and Android. The platform is used by clinicians and institutions worldwide. As of this enrichment pass MedAll publishes no public API, developer portal, SDKs or webhooks; this profile captures its public identity and domain-security posture. Backed by Seedcamp.
image: https://medall.org/lib_aHdYKDVyntNTXkuN/0qn5wqfencthnohu.png?w=1200&h=630&fit=crop
layout: provider
modified: '2026-07-20'
name: MedAll
nav: Providers
network: true
overview: 'MedAll is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Medical Education, Education, and Training.


  MedAll''s developer surface includes signup flow and 4 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 2
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/medall/refs/heads/main/screenshots/medall-2026-08-07T172312.png
security:
- kind: domain-security
  name: Medall Domain Security
  slug: medall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: medall
tags:
- Company
- Healthcare
- Medical Education
- Education
- Training
- Event
- Continuing Medical Education
- Health Tech
website: https://medall.org
---

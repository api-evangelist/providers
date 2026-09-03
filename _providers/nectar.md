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
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nectar-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://mynectar.com
- group: company
  title: ''
  type: Blog
  url: https://mynectar.com/blog
- group: operate
  title: ''
  type: Support
  url: https://support.mynectar.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.mynectar.com/booking
- group: commercial
  title: ''
  type: TermsOfService
  url: https://mynectar.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://mynectar.com/privacy
created: '2026-07-17'
description: Nectar (Nectar Life Sciences) is a hybrid, vertically-integrated allergy care platform combining at-home testing with in-person clinical care. Patients can self-test for dozens of indoor and outdoor environmental allergens using mail-in home kits, then receive personalized treatment including sublingual immunotherapy (allergy drops), prescription nasal sprays, rescue inhalers, and allergy shots. Its flagship Nectar Allergy Center in New York City treats adults and children for environmental allergies, asthma, food allergies, and eczema, alongside virtual telehealth appointments. Nectar is a consumer healthcare provider with no public developer API surface; it was backed by Obvious Ventures, Juxtapose, and Harmony Partners.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nectar.png
layout: provider
modified: '2026-07-20'
name: Nectar
nav: Providers
network: true
overview: 'Nectar is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health Technology, Allergy, and Telehealth.


  Nectar''s developer surface includes engineering blog, support, signup flow, and 4 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 13.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nectar/refs/heads/main/screenshots/nectar-2026-08-07T184807.png
security:
- kind: domain-security
  name: Nectar Domain Security
  slug: nectar-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: nectar
tags:
- Company
- Healthcare
- Health Technology
- Allergy
- Telehealth
- Immunotherapy
- Consumer Health
website: https://mynectar.com
---

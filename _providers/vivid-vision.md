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
  scored_at: '2026-08-30'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vivid-vision-domain-security.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/vivid-vision-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: conformance/vivid-vision-conformance.yml
- group: company
  title: ''
  type: Website
  url: https://www.seevividly.com/
created: '2026-07-17'
description: Vivid Vision is a digital vision care company that builds VR- and software-based tools for diagnosing and treating binocular vision disorders. Its products include a vision training system for amblyopia (lazy eye), strabismus, and convergence insufficiency; Vivid Vision Perimetry (VVP), a VR-based visual field test used as an endpoint in ophthalmology clinical trials for geographic atrophy, AMD, and glaucoma; and EYEBAB VT therapeutic exercises for clinical settings. Founded in 2014, the platform has been used by more than 100,000 patients across 50+ countries through eye-care practices and clinics. Vivid Vision is backed by Uncork Capital. The company is a patient- and clinician-facing vision-care provider and does not publish a public developer API, SDK, or webhook surface at this time.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vivid-vision.png
layout: provider
modified: '2026-07-21'
name: Vivid Vision
nav: Providers
network: true
overview: Vivid Vision is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Vision Care, Health, Virtual Reality, and Ophthalmology.
random_paper: 16
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
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 9.0
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Health
    regime_id: health
    score: 20.0
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
security:
- kind: domain-security
  name: Vivid Vision Domain Security
  slug: vivid-vision-domain-security
  summary_line: TLSv1.2 · DMARC
slug: vivid-vision
tags:
- Company
- Vision Care
- Health
- Virtual Reality
- Ophthalmology
- Vision Therapy
- Clinical Trials
- MedTech
website: https://www.seevividly.com/
---

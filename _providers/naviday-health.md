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
  scored_at: '2026-09-05'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/naviday-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://navidayhealth.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://navidayhealth.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://navidayhealth.com/privacy
- group: company
  title: ''
  type: LinkedIn
  url: https://linkedin.com/company/naviday
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/navidayhealth
created: '2026-07-17'
description: Naviday Health is a Boston-based women's health technology company and Techstars portfolio company building clinical decision support that connects the continuous health data women generate every day from consumer wearables and patient-generated sources to the practitioners who need it most. Its LUCI Care platform surfaces actionable insights for clinicians between appointments, and the company partners with device manufacturers on wearable integration services. Naviday Health is HIPAA compliant and has been recognized by the Mayo Clinic Platform, StartUp Health, and MassChallenge. As of this enrichment pass the company publishes no public developer API, documentation, SDK, or well-known discovery surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/naviday-health.png
layout: provider
modified: '2026-07-20'
name: Naviday Health
nav: Providers
network: true
overview: Naviday Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Women's Health, Digital Health, and Wearables.
random_paper: 16
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
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
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 9.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/naviday-health/refs/heads/main/screenshots/naviday-health-2026-08-07T184730.png
security:
- kind: domain-security
  name: Naviday Health Domain Security
  slug: naviday-health-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: naviday-health
tags:
- Company
- Healthcare
- Women's Health
- Digital Health
- Wearables
- Clinical Decision Support
- Health Tech
website: https://navidayhealth.com/
---

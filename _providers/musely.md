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
  url: security/musely-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.musely.com/
- group: operate
  title: ''
  type: Support
  url: https://support.musely.com/hc/en-us
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.musely.com/hc/en-us
- group: start
  title: ''
  type: SignUp
  url: https://www.musely.com/login
- group: start
  title: ''
  type: Login
  url: https://www.musely.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.musely.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.musely.com/privacy
created: '2026-07-17'
description: Musely is a telehealth platform, founded in 2012 by Jack Jia and Carrie Jiao and based in San Jose, California, that connects patients with U.S. board-certified dermatologists for personalized, prescription-strength skincare and related care. Patients share skin concerns online, physicians craft personalized treatment plans, and freshly compounded formulas are shipped to the patient. Since pivoting from a wellness community to prescription skincare in 2019, Musely has expanded into hair loss, hormonal/menopause health, and longevity, serving more than 1.2 million patients. Musely is a consumer/health company in the API Evangelist network; it operates as a direct-to-consumer web and mobile telehealth experience and does not publish a public developer API, SDK, or webhook surface as of this enrichment pass.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/musely.png
layout: provider
modified: '2026-07-20'
name: Musely
nav: Providers
network: true
overview: 'Musely is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Consumer, Telehealth, Skincare, and Dermatology.


  Musely''s developer surface includes support, signup flow, and 6 more developer resources.'
random_paper: 20
score:
  band: emerging
  composite: 12.6
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 12.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 17.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/musely/refs/heads/main/screenshots/musely-2026-08-07T184447.png
security:
- kind: domain-security
  name: Musely Domain Security
  slug: musely-domain-security
  summary_line: TLSv1.3 · DMARC
slug: musely
tags:
- Company
- Consumer
- Telehealth
- Skincare
- Dermatology
- Prescription
- Health
- Longevity
website: https://www.musely.com/
---

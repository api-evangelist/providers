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
  url: security/cova-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cova.care/
- group: operate
  title: ''
  type: Support
  url: mailto:questions@cova.care
- group: other
  title: ''
  type: Company
  url: https://www.ycombinator.com/companies/cova
created: '2026-07-17'
description: Cova is an AI-native home care agency licensed in Michigan and backed by Y Combinator (Summer 2026). The company serves Medicaid, long-term care insurance (LTCI), and private-pay patients, pays caregivers the highest base rate in the state, and helps unpaid family caregivers get paid through programs they may not know they qualify for. Cova operates a home care platform that connects caregivers with families needing in-home assistance, using an AI-driven operational model to reduce traditional agency overhead while maximizing caregiver compensation. Founded in 2026 by Jordan Ibe and Ansh Tandon, the team is based in Detroit, Michigan. Cova also runs MichiganHomeHelp.com as a Medicaid Home Help information resource. As a consumer home-care service, Cova does not currently publish a public API, developer portal, or developer documentation.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cova.png
layout: provider
modified: '2026-07-18'
name: Cova
nav: Providers
network: true
overview: 'Cova is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Care, Healthcare, Caregiving, and Medicaid.


  Cova''s developer surface includes support and 3 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
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
  previous_composite: 4.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cova/refs/heads/main/screenshots/cova-2026-07-25T210524.png
security:
- kind: domain-security
  name: Cova Domain Security
  slug: cova-domain-security
  summary_line: TLSv1.3
slug: cova
tags:
- Company
- Home Care
- Healthcare
- Caregiving
- Medicaid
- Long-Term Care
- Artificial Intelligence
- Marketplace
- Detroit
- Michigan
website: https://cova.care/
---

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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/medwing-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://medwing.com
- group: company
  title: ''
  type: Blog
  url: https://medwing.com/de/de/magazine
- group: commercial
  title: ''
  type: Pricing
  url: https://medwing.com/de/de/arbeitgeber
- group: start
  title: ''
  type: SignUp
  url: https://flow.medwing.com
- group: start
  title: ''
  type: Login
  url: https://my.medwing.com
- group: company
  title: ''
  type: About
  url: https://medwing.com/de/ueber-uns
- group: company
  title: ''
  type: Press
  url: https://medwing.com/de/de/ueber-medwing/presse
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/medwing-llms.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/medwing-well-known.yml
created: '2026-07-17'
description: MEDWING is Germany's largest digital service platform for jobs and staffing in the healthcare sector, founded in 2017 and headquartered in Berlin. It operates a recruitment marketplace that matches hospitals, clinics and care facilities with nurses, caregivers, doctors, midwives, pharmacists and other healthcare professionals across Germany and the United Kingdom. Beyond permanent placement, MEDWING combines career brokerage with temporary-staffing (Zeitarbeit) operations and HR/workforce tooling, offering an end-to-end digital workflow that spans job search, matching, contracts, digital signatures and timesheets. The service is free for candidates, with employers paying on successful placement. MEDWING is backed by Northzone and other investors. This profile was enriched from public web sources; MEDWING does not currently publish a public developer API.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/medwing.png
layout: provider
modified: '2026-07-20'
name: Medwing
nav: Providers
network: true
overview: 'Medwing is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Recruitment, Staffing, and Nursing.


  Medwing''s developer surface includes engineering blog, pricing, signup flow, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 17.1
    commercial_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 8.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
security:
- kind: domain-security
  name: Medwing Domain Security
  slug: medwing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: medwing
tags:
- Company
- Healthcare
- Recruitment
- Staffing
- Nursing
- HR Tech
- Marketplace
- Germany
website: https://medwing.com
---

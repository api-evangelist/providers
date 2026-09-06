---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
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
  url: security/state-employees-credit-union-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.ncsecu.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.ncsecu.org/about-us
- group: docs
  title: ''
  type: Documentation
  url: https://www.ncsecu.org/services/online
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ncsecu.org/pdfs/privacy-and-legal/SECUTermsOfUse.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://onlineaccess.ncsecu.org/O/SECUContent/PDF/SECUPrivacyNotice_English.pdf
created: '2026-07-23'
description: 'State Employees'' Credit Union (SECU / NCSECU) is a member-owned, not-for-profit financial cooperative headquartered in Raleigh, North Carolina. Founded in 1937 with 17 members and $437 in deposits, it is a state-chartered credit union regulated by the Credit Union Division of the North Carolina Department of Commerce and federally insured by the NCUA (NMLS #430055). SECU is the second-largest natural-person credit union in the United States by both assets and membership, serving nearly 2.9 million member-owners with roughly $56 billion in assets across 275 branches in all 100 North Carolina counties. Membership is primarily limited to North Carolina state employees and their families. On the open-finance front, SECU operates no public first-party developer portal and publishes no downloadable OpenAPI/Swagger specifications; its consumer digital banking (Member Access) supports connecting external accounts for aggregation, and outbound consumer-permissioned data sharing is
  handled through data aggregators rather than a documented first-party API. No public FDX-conformant data-access endpoint or CFPB Section 1033 data-rights posture is published as of July 2026.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: State Employees' Credit Union
nav: Providers
network: true
overview: 'State Employees'' Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Credit Union, United States, and North Carolina.


  State Employees'' Credit Union''s developer surface includes documentation and 5 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 6.2
  coverage:
    artifact_dirs: 2
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 10.5
    commercial_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 6.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/state-employees-credit-union/refs/heads/main/screenshots/state-employees-credit-union-2026-09-02T160815.png
security:
- kind: domain-security
  name: State Employees Credit Union Domain Security
  slug: state-employees-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: state-employees-credit-union
tags:
- Financial-Services
- Banking
- Credit Union
- United States
- North Carolina
- Open Finance
- Data Aggregation
website: https://www.ncsecu.org/
---

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
  url: security/santander-us-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.santanderbank.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/santander-bank-na
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.santanderbank.com/online-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.santanderbank.com/terms-and-conditions
- group: operate
  title: ''
  type: Support
  url: https://www.santanderbank.com/personal/security-center
created: '2026-07-23'
description: 'Santander Bank, N.A. (santanderbank.com) is the US retail and commercial banking subsidiary of Spain''s Banco Santander S.A., headquartered in Boston, Massachusetts. It is a nationally chartered bank (National Association, regulated by the OCC) operating a branch network across the Northeast US (Massachusetts, New Hampshire, Rhode Island, Connecticut, New York, New Jersey, Pennsylvania and Delaware), which positions it as a super-regional bank. Unlike UK and Australian institutions bound by mandated open-banking contracts, and unlike US banks such as Capital One or Chase that publish first-party developer portals, Santander Bank N.A. exposes no public, first-party developer API for its US retail franchise: developer.santanderbank.com does not resolve, and the site publishes no developers/API/open-banking pages. Consumer-permissioned data access in the US is available today through aggregators rather than a direct API — Plaid supports "Santander - Personal" (Assets, Auth, Balance
  and Transactions). Santander''s UK developer portal (developer.santander.co.uk) and the group''s Corporate & Investment Banking API marketplace (apimarket.santandercib.com) are operated by separate legal entities and are not the US retail bank''s surface. This record is an honest identity profile of a super-regional bank whose US open-finance posture is aggregator-mediated, with no documented first-party developer program.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Santander US
nav: Providers
network: true
overview: 'Santander US is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Super-Regional Bank, and Retail Banking.


  Santander US''s developer surface includes support and 5 more developer resources.'
random_paper: 19
score:
  band: minimal
  composite: 8.2
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
    developer_ergonomics: 4.8
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
  previous_composite: 8.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 17.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/santander-us/refs/heads/main/screenshots/santander-us-2026-09-02T154403.png
security:
- kind: domain-security
  name: Santander Us Domain Security
  slug: santander-us-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: santander-us
tags:
- Financial-Services
- Banking
- United States
- Super-Regional Bank
- Retail Banking
- Open Finance
- Data Aggregation
website: https://www.santanderbank.com
---

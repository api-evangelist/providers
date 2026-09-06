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
  url: security/prospera-credit-union-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.prospera.ca/
- group: company
  title: ''
  type: About
  url: https://www.prospera.ca/About/Our+Story
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/prospera-credit-union
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/ProsperaCreditUnion
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/prosperacreditunion
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/prosperacreditunion
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.prospera.ca/Policies/Legal
- group: operate
  title: ''
  type: Support
  url: https://www.prospera.ca/contact
created: '2026-07-23'
description: Prospera Credit Union is a member-owned cooperative financial institution headquartered in British Columbia, Canada, formed on January 1, 2020 through the merger of the original Prospera Credit Union and Westminster Savings Credit Union — the largest credit-union merger in Canadian history. With roughly CA$9 billion in assets under management, about 120,000 members, and some 900 employees across branches in Metro Vancouver, the Fraser Valley, and the Okanagan, it is the third largest credit union in British Columbia and among the six largest in Canada. As a provincially regulated cooperative (credit unions in BC are overseen by BC Financial Services Authority and deposits are protected by the Credit Union Deposit Insurance Corporation of BC), Prospera serves personal and business members with chequing and savings accounts, credit cards, mortgages, loans, and Interac e-Transfer. On the open-finance side, Prospera runs NO public first-party developer portal or documented API —
  none of developer/api/developers.prospera.ca resolve — and Canada's federal Consumer-Driven Banking (open-banking) framework, legislated in Budget 2024 and overseen by the FCAC, is not yet operational. Like most Canadian credit unions, Prospera reaches national payment rails and consumer data-sharing through shared credit-union-system infrastructure rather than a proprietary API, and third-party data access today is aggregator/screen-scraping based (e.g. Flinks, Plaid). This is an honest identity-only profile with no public API surface to catalog.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Prospera Credit Union
nav: Providers
network: true
overview: 'Prospera Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, Canada, Credit Union, and Cooperative.


  Prospera Credit Union''s developer surface includes YouTube channel, support, and 7 more developer resources.'
random_paper: 12
score:
  band: minimal
  composite: 5.3
  coverage:
    artifact_dirs: 3
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
    developer_ergonomics: 4.8
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 5.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 12.7
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/prospera-credit-union/refs/heads/main/screenshots/prospera-credit-union-2026-09-02T152217.png
security:
- kind: domain-security
  name: Prospera Credit Union Domain Security
  slug: prospera-credit-union-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: prospera-credit-union
tags:
- Financial-Services
- Banking
- Canada
- Credit Union
- Cooperative
- British Columbia
- Interac
- Open Banking
- Consumer-Driven Banking
- Data Aggregation
website: https://www.prospera.ca/
---

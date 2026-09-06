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
  url: security/digital-federal-credit-union-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.dcu.org
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.dcu.org/dcu-support-center/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.dcu.org/dcu-support-center/privacy-practices.html
- group: operate
  title: ''
  type: Support
  url: https://www.dcu.org/help.html
- group: company
  title: ''
  type: Blog
  url: https://www.dcu.org/about/newsroom.html
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/dcu
created: '2026-07-23'
description: 'Digital Federal Credit Union (DCU) is a not-for-profit, member-owned federal credit union headquartered in Marlborough, Massachusetts and regulated by the National Credit Union Administration (NCUA), with roughly 1.18 million members, 23 branches across Massachusetts and New Hampshire, and nationwide access via the Co-Op shared-branch and surcharge-free ATM networks. It offers consumer and business banking, lending, mortgages, credit cards, and investment services, and has recently merged with First Technology Federal Credit Union. Like most US credit unions, DCU publishes NO public first-party developer API, developer portal, or downloadable OpenAPI/Swagger specifications; consumer-permissioned account data is reached only indirectly through third-party aggregators (Plaid, MX, Finicity, Akoya) and its core banking provider, and there is no publicly documented FDX participation or CFPB Section 1033 data-access program. This is an honest identity-only record: no public API surface
  exists to catalog.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: DCU (Digital Federal Credit Union)
nav: Providers
network: true
overview: 'DCU (Digital Federal Credit Union) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Credit Union, and Consumer Banking.


  DCU (Digital Federal Credit Union)''s developer surface includes support, engineering blog, and 5 more developer resources.'
random_paper: 8
score:
  band: minimal
  composite: 2.2
  coverage:
    artifact_dirs: 5
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
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 2.2
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/digital-federal-credit-union/refs/heads/main/screenshots/digital-federal-credit-union-2026-07-25T212011.png
security:
- kind: domain-security
  name: Digital Federal Credit Union Domain Security
  slug: digital-federal-credit-union-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: digital-federal-credit-union
tags:
- Financial-Services
- Banking
- United States
- Credit Union
- Consumer Banking
- Open Finance
- Data Aggregation
website: https://www.dcu.org
---

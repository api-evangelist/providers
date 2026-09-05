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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mountain-america-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.macu.com/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mountain-america-credit-union
created: '2026-07-23'
description: 'Mountain America Credit Union (MACU) is a federally chartered, member-owned not-for-profit financial cooperative headquartered in Sandy, Utah, founded in 1936 and regulated and insured by the National Credit Union Administration (NCUA). It is one of the largest credit unions in the United States, with roughly $21.9 billion in assets, more than 1.4 million members, and over 100 branches serving Utah, Idaho, Montana, Nevada, and Arizona, offering consumer and business checking, savings, mortgages, auto loans, credit cards, and wealth services. Like the vast majority of US credit unions, Mountain America exposes no public first-party developer API or developer portal: there is no developer.macu.com or api.macu.com host, and every path under macu.com returns the same client-rendered application shell. Consumer-permissioned data access is intermediated through its core banking provider and data aggregators (Plaid, MX, Finicity, Akoya) rather than a directly published API. US open
  finance is voluntary and fragmented, and no public FDX participation or CFPB Section 1033 data-access posture is documented for this institution at the time of review.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
layout: provider
modified: '2026-07-23'
name: Mountain America Credit Union
nav: Providers
network: true
overview: Mountain America Credit Union is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Financial-Services, Banking, United States, Credit Union, and Consumer Banking.
random_paper: 4
score:
  band: minimal
  composite: 1.5
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
    developer_ergonomics: 0.0
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 1.5
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 7.6
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mountain-america/refs/heads/main/screenshots/mountain-america-2026-08-07T184345.png
security:
- kind: domain-security
  name: Mountain America Domain Security
  slug: mountain-america-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mountain-america
tags:
- Financial-Services
- Banking
- United States
- Credit Union
- Consumer Banking
- Open Finance
- Data Aggregation
website: https://www.macu.com/
---

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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/rsi/hosts/rsi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rsi-hosts.yml
- group: other
  href: https://artifacts.apis.io/rsi/vendors/rsi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rsi-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.rsi.com/news/
- group: company
  title: ''
  type: Blog
  url: https://www.rsi.com/blog/courts-today/
- group: auth
  href: https://artifacts.apis.io/rsi/security/rsi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rsi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.rsi.com/
- group: operate
  title: ''
  type: Support
  url: https://www.rsi.com/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rsi.com/terms-use/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://rsi.com/
  reason: no-developer-program
  state: none
created: '2026-10-21'
description: Relational Semantics provides advanced data modeling and relational analytics services, enabling enterprises to integrate, query, and visualize complex relational datasets through robust APIs. Their platform focuses on semantic data linking, schema evolution, and real‑time insights, supporting a wide range of industries from finance to healthcare. By offering comprehensive documentation, SDKs, and developer support, Relational Semantics empowers developers to build data‑driven applications that leverage relational semantics for deeper business intelligence.
layout: provider
modified: '2026-10-21'
name: Relational Semantics
nav: Providers
network: true
overview: 'Relational Semantics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Data Modeling, Analytics, Enterprise, and Semantic-Data.


  Relational Semantics'' developer surface includes engineering blog, support, and 6 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 5.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 5.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 3.6
    discoverability: 45.5
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 7.4
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 7.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/rsi/rsi-2026-11-03T142445.png
security:
- kind: domain-security
  name: Rsi Domain Security
  slug: rsi-domain-security
  summary_line: TLSv1.3
slug: rsi
tags:
- Company
- Data Modeling
- Analytics
- Enterprise
- Semantic-Data
website: https://www.rsi.com/
---

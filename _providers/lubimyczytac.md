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
- group: agent
  href: https://artifacts.apis.io/lubimyczytac/llms/lubimyczytac-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/lubimyczytac-llms.txt
- group: other
  href: https://artifacts.apis.io/lubimyczytac/hosts/lubimyczytac-hosts.yml
  title: ''
  type: Hosts
  url: hosts/lubimyczytac-hosts.yml
- group: other
  href: https://artifacts.apis.io/lubimyczytac/vendors/lubimyczytac-vendors.yml
  title: ''
  type: Vendors
  url: vendors/lubimyczytac-vendors.yml
- group: auth
  href: https://artifacts.apis.io/lubimyczytac/security/lubimyczytac-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/lubimyczytac-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://lubimyczytac.pl/
coverage:
  checked: '2026-10-28'
  detail: The site provides no public developer documentation or API specifications.
  evidence:
  - status: 200
    url: https://lubimyczytac.pl/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: LubimyCzytac is a Polish online platform dedicated to books, offering price comparisons, reviews, recommendations, author interviews, and the latest news in the literary world. It aggregates data from multiple retailers, provides detailed book information, and helps readers discover new titles through curated lists and community insights.
image: https://s.lubimyczytac.pl/rwd/src/assets/images/lc-logo-ksiazeczka.png
layout: provider
modified: '2026-10-28'
name: LubimyCzytac
nav: Providers
network: true
overview: LubimyCzytac is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Books, Price Comparison, Reviews, and Community.
random_paper: 16
score:
  band: minimal
  composite: 4.2
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 55.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - poland
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - cee
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 4.2
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/lubimyczytac/lubimyczytac-2026-11-03T135107.png
security:
- kind: domain-security
  name: Lubimyczytac Domain Security
  slug: lubimyczytac-domain-security
  summary_line: TLSv1.3 · DMARC
slug: lubimyczytac
tags:
- Company
- Books
- Price Comparison
- Reviews
- Community
- Poland
website: https://lubimyczytac.pl/
---

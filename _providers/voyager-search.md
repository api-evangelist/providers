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
- group: auth
  href: https://artifacts.apis.io/voyager-search/well-known/voyager-search-product-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/voyager-search-product-security.txt
- group: agent
  href: https://artifacts.apis.io/voyager-search/well-known/voyager-search-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/voyager-search-well-known.yml
- group: other
  href: https://artifacts.apis.io/voyager-search/hosts/voyager-search-hosts.yml
  title: ''
  type: Hosts
  url: hosts/voyager-search-hosts.yml
- group: build
  href: https://artifacts.apis.io/voyager-search/packages/voyager-search-packages.yml
  title: ''
  type: SDKs
  url: packages/voyager-search-packages.yml
- group: build
  href: https://artifacts.apis.io/voyager-search/packages/voyager-search-packages.yml
  title: ''
  type: Packages
  url: packages/voyager-search-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.voyagersearch.com/terms-of-use
- group: auth
  title: ''
  type: Security
  url: https://www.voyagersearch.com/platform/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.voyagersearch.com/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.voyagersearch.com/newsroom/filters/all
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/voyagersearch
- group: auth
  href: https://artifacts.apis.io/voyager-search/security/voyager-search-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/voyager-search-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.voyagersearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.voyagersearch.com/platform
- group: operate
  title: ''
  type: Support
  url: https://www.voyagersearch.com/contact
coverage:
  checked: '2026-10-23'
  detail: Documentation pages are rendered via Framer and provide no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.voyagersearch.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-23'
description: Voyager is a ready-to-deploy platform that connects, enriches, and operationalizes distributed geospatial, non‑spatial, structured and unstructured data—powering analytics, AI, and mission‑critical decisions for enterprises. It provides an intelligence layer for geospatial and enterprise data, enabling users to ingest, index, and query massive datasets with advanced search, visualization, and integration capabilities.
image: https://framerusercontent.com/images/dU0AaD5P0E3UEps2bbNcgyClyk0.png
layout: provider
modified: '2026-10-23'
name: Voyager Search
nav: Providers
network: true
overview: 'Voyager Search is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Geospatial, Data Intelligence, Enterprise, Search, and Platform.


  Voyager Search''s developer surface includes documentation, support, and 12 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 10.1
  coverage:
    artifact_dirs: 10
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.2
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 49.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/voyager-search/voyager-search-2026-11-03T145928.png
security:
- kind: domain-security
  name: Voyager Search Domain Security
  slug: voyager-search-domain-security
  summary_line: TLSv1.3 · HSTS
slug: voyager-search
tags:
- Geospatial
- Data Intelligence
- Enterprise
- Search
- Platform
- Company
website: https://www.voyagersearch.com
---

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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Smart Europe services as described on the developer portal.
  name: Smart Europe API
  slug: smart-europe-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/smart-com/hosts/smart-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/smart-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/smart-com/vendors/smart-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/smart-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/smart-com/security/smart-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/smart-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://smart.com/
- group: docs
  title: ''
  type: Documentation
  url: https://global.smart.com/developers
- group: company
  title: ''
  type: Blog
  url: https://global.smart.com/blog
coverage:
  checked: '2026-10-28'
  detail: Documentation pages return JavaScript shells and HTML instead of machine‑readable specs.
  evidence:
  - status: 200
    url: https://global.smart.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Smart Europe is a multinational automotive and mobility company offering smart vehicles and connected services across Europe and worldwide. The brand provides a range of electric and hybrid models, advanced driver assistance systems, and a digital platform for vehicle management, market selection, and localized content. Through its global website, users can explore models, compare specifications, and access the latest news and updates tailored to their region and language.
image: https://s7.future.smart.com/is/image/smarteurope/social-media-share-dark-theme:16-9?wid=1200&hei=630&fit=crop,1
layout: provider
modified: '2026-10-28'
name: smart Europe
nav: Providers
network: true
overview: 'smart Europe is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  smart Europe''s developer surface includes documentation, engineering blog, and 4 more developer resources.'
random_paper: 3
score:
  band: minimal
  composite: 4.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 6.0
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 5.8
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
screenshot: https://apis.io/screenshots/smart-com/smart-com-2026-11-03T143334.png
security:
- kind: domain-security
  name: Smart Com Domain Security
  slug: smart-com-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: smart-com
tags:
- Company
website: https://smart.com/
---

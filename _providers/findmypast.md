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
  href: https://artifacts.apis.io/findmypast/hosts/findmypast-hosts.yml
  title: ''
  type: Hosts
  url: hosts/findmypast-hosts.yml
- group: other
  href: https://artifacts.apis.io/findmypast/vendors/findmypast-vendors.yml
  title: ''
  type: Vendors
  url: vendors/findmypast-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.findmypast.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.findmypast.com/blog
- group: auth
  href: https://artifacts.apis.io/findmypast/security/findmypast-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/findmypast-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.findmypast.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.findmypast.com/help
- group: operate
  title: ''
  type: Support
  url: https://www.findmypast.com/help/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.findmypast.com/help/sections/4411074088593-privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.findmypast.com/help/sections/4411058333841-terms-conditions
coverage:
  checked: '2026-10-28'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine-readable contract was found despite public documentation pages.
  evidence:
  - status: 404
    url: https://api.findmypast.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Findmypast WebHints provides access to the largest online collection of UK and Irish genealogy records, newspaper archives, and historical documents. Users can search census data, birth, marriage, death records, military registers, and build family trees, helping them uncover their ancestors and family history across Britain and Ireland.
image: https://www.findmypast.com/image-proxy-signed/V3ecfLw3rB7_eis-xKfZXwWbk928lQ2g-aGrsnje93A/czM6Ly9wYXlsb2FkLWNtcy1wcm9kdWN0aW9uL1BheWxvYWQtIE9wZW4gR3JhcGgucG5n
layout: provider
modified: '2026-10-28'
name: Findmypast WebHints
nav: Providers
network: true
overview: 'Findmypast WebHints is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Genealogy, History, Family Tree, Archives, and United Kingdom.


  Findmypast WebHints'' developer surface includes engineering blog, documentation, support, and 7 more developer resources.'
random_paper: 7
score:
  band: minimal
  composite: 9.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 8.3
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - ireland
    - united-kingdom
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - europe
    - united-kingdom-ireland
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.8
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
screenshot: https://apis.io/screenshots/findmypast/findmypast-2026-11-03T132024.png
security:
- kind: domain-security
  name: Findmypast Domain Security
  slug: findmypast-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: findmypast
tags:
- Genealogy
- History
- Family Tree
- Archives
- United Kingdom
- Ireland
website: https://www.findmypast.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 0
artifact_total: 0
common:
- group: company
  title: ''
  type: Crunchbase
  url: https://www.crunchbase.com/organization/brewster
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/brewster-inc
- group: company
  title: ''
  type: InvestorProfile
  url: https://usv.com/blog/brewster
- group: company
  title: ''
  type: NewsCoverage
  url: https://techcrunch.com/2016/03/23/fullcontact-buys-brewsters-technology-after-team-gets-acqui-hired-by-burger-king-owner-rbi/
- group: company
  title: ''
  type: NewsCoverage
  url: https://techcrunch.com/2015/10/23/brewster-contacts-app-team-gets-acqui-hired-by-burger-king-owner-rbi/
created: '2026-07-17'
description: Brewster was a New York-based mobile contacts startup founded by Steve Greenwood that launched an iOS app in July 2012 offering a "hyperconnected mobile address book" — it merged phone contacts with Google Apps, Facebook, Twitter, Foursquare and LinkedIn profiles, deduplicated them, and kept them self-updating in the cloud while surfacing relationship signals about who a user actually engaged with. The company was backed by Union Square Ventures and Slow Ventures. In October 2015 the founding team was acqui-hired by Restaurant Brands International (owner of Burger King and Tim Hortons) without the app or its data, and in March 2016 FullContact acquired Brewster's self-updating address book technology and shut the consumer product down within 30 days. Brewster never published a public developer API, SDK, OpenAPI definition or developer portal, and no API surface survives today. This profile is retained as a historical record only.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/brewster.png
layout: provider
modified: '2026-07-20'
name: Brewster
nav: Providers
network: true
overview: Brewster is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Defunct, Contacts, Address Book, and Mobile.
random_paper: 20
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 1
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/brewster/refs/heads/main/screenshots/brewster-2026-07-25T203758.png
slug: brewster
tags:
- Company
- Defunct
- Contacts
- Address Book
- Mobile
- Social
- Consumer
- Acquired
---

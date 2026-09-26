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
- group: other
  title: ''
  type: Successor
  url: https://www.amentum.com
- group: other
  title: ''
  type: SEC
  url: https://www.sec.gov/cgi-bin/browse-edgar?action=getcompany&CIK=0001514226&type=10-K&dateb=&owner=include&count=40
- group: other
  title: ''
  type: Notes
  url: https://en.wikipedia.org/wiki/DynCorp
coverage:
  checked: '2026-09-06'
  detail: Delta Tucker Holdings deregistered with the SEC on 2019-10-01 (Form 15-15D, its last filing of any kind) and its operating subsidiary DynCorp International was absorbed into Amentum on 2020-11-23; deltatuckerholdings.com has no DNS at all, dyncorp.com is now a Sedo parking page offering the domain for sale, and the only surviving host, dyn-intl.com, is operated under Amentum and answers a Cloudflare 403 to everything but robots.txt.
  evidence:
  - status: 200
    url: https://data.sec.gov/submissions/CIK0001514226.json
  - status: 200
    url: https://dyncorp.com/
  - status: 403
    url: https://dyn-intl.com/.well-known/security.txt
  - status: 200
    url: https://dyn-intl.com/robots.txt
  reason: defunct
  state: none
created: '2024-12-03'
description: Delta Tucker Holdings was the holding company for DynCorp International, a provider of specialized mission-critical professional and support services to government and commercial customers, including aviation services, logistics, and training. DynCorp's operations were acquired and integrated into Amentum in 2020. Delta Tucker Holdings does not publish public APIs; this profile is preserved as a corporate-history index.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/delta-tucker-holdings.png
layout: provider
modified: '2026-09-15'
name: Delta Tucker Holdings
nav: Providers
network: true
overview: Delta Tucker Holdings is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Defense, Government Services, Holding Company, Logistics, and Mission Support.
press:
- date: ''
  title: Proxy Statement (Form DEF 14A)
  url: https://www.publicnow.com/view/F2243B833D18A724285849E28B6619A4215AE43F?1750452459
- date: ''
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1646972/000114036124030899/ny20019591x1_def14a.htm
- date: ''
  title: HP INC. XEROX HOLDINGS CORPORATION
  url: https://investors.xerox.com/static-files/6b7bc5b3-72cd-4b9f-ba5f-e6fc6570a86a
- date: ''
  title: D - API Evangelist Contracts - Contracts
  url: https://contracts.apievangelist.com/d/
- date: ''
  title: Investors - Governance - Board of Directors
  url: https://www.albertsonscompanies.com/investors/governance/board-of-directors/default.aspx
random_paper: 10
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 5
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
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/delta-tucker-holdings/refs/heads/main/screenshots/delta-tucker-holdings-2026-06-20T175904.png
slug: delta-tucker-holdings
tags:
- Defense
- Government Services
- Holding Company
- Logistics
- Mission Support
- Private Company
- Defunct
---

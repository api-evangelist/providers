---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.hollyfrontier.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.hfsinclair.com/ — a different registrable domain (hollyfrontier.com -> hfsinclair.com) following the 2022 reorganization under HF Sinclair Corporation (probed 2026-09-03 and re-probed 2026-09-13, roadmap#169)''}'
  - '{''url'': ''https://customerportal.hollyfrontier.com/'', ''status'': 200, ''note'': ''DTN-operated bulk-fuel customer portal, member login only; no API, spec or developer documentation behind or beside it (probed 2026-09-13)''}'
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
  scored_at: '2026-09-23'
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.hollyfrontier.com
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/hollyfrontier
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/hollyfrontier/refs/heads/main/security/hollyfrontier-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hollyfrontier-domain-security.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/hollyfrontier/refs/heads/main/llms/hollyfrontier-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hollyfrontier-llms.txt
coverage:
  checked: '2026-09-13'
  detail: HollyFrontier Corporation was reorganized under HF Sinclair Corporation in 2022 and www.hollyfrontier.com/home/default.aspx now returns HTTP 301 to www.hfsinclair.com; the only surviving hollyfrontier.com surfaces are an investor-relations site on the Q4 Inc web farm and a DTN-operated bulk-fuel customer portal behind a member login, neither of which publishes an API, a spec, or a developer page.
  evidence:
  - status: 301
    url: https://www.hollyfrontier.com/home/default.aspx
  - status: 200
    url: https://customerportal.hollyfrontier.com/
  - status: 404
    url: https://customerportal.hollyfrontier.com/openapi.json
  - status: 200
    url: https://www.hfsinclair.com/suppliers/HF/default.aspx
  - status: 404
    url: https://api.github.com/orgs/hollyfrontier
  reason: defunct
  state: none
created: '2026-04-28'
description: 'HollyFrontier Corporation (NYSE: HFC) was an independent petroleum refiner and marketer headquartered in Dallas, Texas, formed by the 2011 merger of Holly Corporation and Frontier Oil. It operated refineries across the mid-continent, southwest and Rocky Mountain regions, producing and marketing gasoline, diesel fuel, jet fuel, asphalt and specialty lubricant products, and held the general partner interest in Holly Energy Partners. In 2022 HollyFrontier completed its transactions with The Sinclair Companies and was reorganized under a new parent, HF Sinclair Corporation (NYSE: DINO); the HollyFrontier brand no longer operates independently and www.hollyfrontier.com now redirects to www.hfsinclair.com.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/hollyfrontier.png
layout: provider
modified: '2026-09-13'
name: HollyFrontier
nav: Providers
network: true
overview: HollyFrontier is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fortune 500, Energy, Oil and Gas, Petroleum Refining, and Fuel.
press:
- date: ''
  title: HollyFrontier Corporation (HFC) CEO George Damiris on ...
  url: https://seekingalpha.com/article/4301168-hollyfrontier-corporation-hfc-ceo-george-damiris-on-q3-2019-results-earnings-call-transcript
- date: ''
  title: HollyFrontier sets 4Q earnings release, conference webcast
  url: https://journalrecord.com/2021/01/08/hollyfrontier-sets-4q-earnings-release-conference-webcast/
- date: ''
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/48039/000119312522077293/d260898d8k.htm
- date: ''
  title: HollyFrontier Corporation Completes Merger
  url: https://www.prnewswire.com/news-releases/hollyfrontier-corporation-completes-merger-124844164.html
- date: ''
  title: HollyFrontier Corporation Third Quarter 2021 Earnings ...
  url: http://markets.chroniclejournal.com/chroniclejournal/article/bizwire-2021-10-4-hollyfrontier-corporation-third-quarter-2021-earnings-release-and-conference-webcast
random_paper: 17
score:
  band: minimal
  composite: 3.3
  coverage:
    artifact_dirs: 8
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
    discoverability: 50.0
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 3.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 8.1
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/hollyfrontier/refs/heads/main/screenshots/hollyfrontier-2026-07-25T221320.png
security:
- kind: domain-security
  name: Hollyfrontier Domain Security
  slug: hollyfrontier-domain-security
  summary_line: TLSv1.3 · HSTS
slug: hollyfrontier
tags:
- Fortune 500
- Energy
- Oil and Gas
- Petroleum Refining
- Fuel
- Lubricants
- Specialty Chemicals
- Dallas
website: https://www.hollyfrontier.com
---

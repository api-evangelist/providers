---
access_model:
  confidence: high
  label: No developer access — no API, portal, or sign-up exists
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - well-known/ep-energy-well-known.yml
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
artifact_total: 0
common:
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ep-energy
coverage:
  checked: '2026-09-06'
  detail: EP Energy Corporation ceased to exist as an operating company when Verdun Oil Company II LLC completed its acquisition on 2022-03-30; its corporate domain epenergy.com now 301s to verdunoilco.com, and the hyphenated ep-energy.com this record previously pointed at is a GoDaddy domain-for-sale lander that answers HTTP 200 with the same 114-byte HTML shell for every path, including /openapi.json and /.well-known/agent-card.json.
  evidence:
  - status: 200
    url: https://epenergy.com/
  - status: 200
    url: https://ep-energy.com/openapi.json
  - status: 200
    url: https://ep-energy.com/llms.txt
  - status: 404
    url: https://epenergy.com/llms.txt
  - status: 404
    url: https://api.github.com/orgs/epenergy
  reason: defunct
  state: none
created: '2024-07-02'
description: EP Energy Corporation was an independent exploration and production company engaged in the acquisition and development of unconventional onshore oil and natural gas properties in the United States, principally in the Eagle Ford shale and the Uinta basin. The company filed for Chapter 11 bankruptcy in October 2019 and emerged in October 2020. Verdun Oil Company II LLC, an EnCap Investments portfolio company, completed its acquisition of EP Energy on 30 March 2022 for approximately $1.45 billion, with the Utah/Uinta assets divested post-closing under an FTC order. EP Energy is no longer an operating company. It never published an API, SDK, or developer program, and its corporate domain epenergy.com now redirects to the acquirer, verdunoilco.com. The unrelated hyphenated domain ep-energy.com is a GoDaddy aftermarket listing offered for sale and is not an EP Energy surface.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ep-energy.png
layout: provider
modified: '2026-09-15'
name: EP Energy
nav: Providers
network: true
overview: EP Energy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Energy, Oil and Gas, Exploration and Production, Defunct, and Acquired.
press:
- date: ''
  title: Buyout firm EnCap Investments agrees $1.5 bln purchase ...
  url: https://www.reuters.com/business/energy/buyout-firm-encap-investments-agrees-15-bln-purchase-ep-energy-sources-2021-08-11/
- date: ''
  title: REPORT
  url: https://www.landman.org/asset/0C73B4AB-EF38-4249-B89204401E9E87BE/
- date: ''
  title: EP Energy Wins Fight With Landowners Over Oil ...
  url: https://news.bloomberglaw.com/bankruptcy-law/ep-energy-wins-fight-with-landowners-over-oil-production-pause
- date: ''
  title: EP Energy Corporation Successfully Completes Financial ...
  url: https://www.prnewswire.com/news-releases/ep-energy-corporation-successfully-completes-financial-restructuring-301144546.html
- date: ''
  title: XBRL Viewer
  url: https://www.sec.gov/ix?doc=/Archives/edgar/data/1866175/000119312522043980/d301514d8k.htm
random_paper: 20
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 6
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
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 0.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 0.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/ep-energy/ep-energy-2026-06-20T180746.png
slug: ep-energy
tags:
- Energy
- Oil and Gas
- Exploration and Production
- Defunct
- Acquired
- Bankruptcy
- Fortune 1000
---

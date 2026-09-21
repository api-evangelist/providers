---
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
  scored_at: '2026-09-20'
api_count: 0
artifact_total: 0
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/airqtel/refs/heads/main/well-known/airqtel-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/airqtel-well-known.yml
coverage:
  checked: '2026-09-19'
  detail: AirQtel sells aerial surveillance flight hours and imagery from its own aircraft and remotely piloted hardware, and its only published domain, airqtel.com, was a three-page Squarespace brochure (Home, About, Partner Portal login) whose archived /.well-known/* and /api/ paths all returned 404 while it was live; the domain is now unregistered (NXDOMAIN at 1.1.1.1, 8.8.8.8 and 9.9.9.9; Verisign RDAP 404), no GitHub org, npm or PyPI package exists, and the only reachable 200 is the Nasdaq Private Market venue listing the harvest stub carried, which is not the company.
  evidence:
  - status: 0
    url: https://www.airqtel.com/
  - status: 404
    url: https://rdap.verisign.com/com/v1/domain/airqtel.com
  - status: 404
    url: https://api.github.com/orgs/airqtel
  - status: 404
    url: https://pypi.org/pypi/airqtel/json
  - status: 200
    url: https://www.nasdaqprivatemarket.com/
  reason: not-a-software-company
  state: none
created: '2026-09-19'
description: AirQtel is a Wellesley, Massachusetts aerial surveillance operator founded in 2021 by Vin Loccisano. It sells ultra-high-resolution real-time aerial imaging as a service, flown from its own fleet of manned aircraft and remotely piloted hardware carrying its proprietary "Looking-Glass" imaging systems, to military, government and commercial customers, and announced a $27M Series A in February 2025 following a prototype launch of the Looking Glass aerial network across four countries. Its only published domain, airqtel.com, hosted a three-page Squarespace brochure site (Home, About, Partner Portal login) with no developer program, API, SDK or machine-readable contract of any kind, and as of 2026-09-19 that domain is no longer registered (NXDOMAIN at every public resolver; Verisign RDAP 404).
layout: provider
modified: '2026-09-19'
name: AirQtel
nav: Providers
network: true
overview: AirQtel is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Aerial Surveillance, Aerospace and Defense, Drones, Imaging, and Geospatial.
random_paper: 6
score:
  band: minimal
  composite: 1.4
  coverage:
    artifact_dirs: 1
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 46.3
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 1.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 0.0
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: airqtel
tags:
- Aerial Surveillance
- Aerospace and Defense
- Drones
- Imaging
- Geospatial
- Government
- Hardware
- Company
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 11.9
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: 'Unauthenticated GTFS Realtime v2.0 feeds, encoded in Protobuf, of trip updates, vehicle positions and service alerts for South East Queensland (whole network and per mode: bus, rail, tram, ferry) and '
  name: Translink GTFS Realtime Feeds
  slug: gtfs-realtime
- description: 'GTFS static schedule datasets (timetables, route paths, stopping patterns) for SEQ bus, train, ferry and tram services and Queensland regional bus services, published as downloadable resources on the '
  name: Translink GTFS Schedule Datasets
  slug: gtfs-schedules
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/translink-queensland/plans/translink-queensland-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/translink-queensland-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/translink-queensland/conventions/translink-queensland-conventions.yml
  title: ''
  type: Conventions
  url: conventions/translink-queensland-conventions.yml
- group: design
  href: https://artifacts.apis.io/translink-queensland/lifecycle/translink-queensland-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/translink-queensland-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/translink-queensland/conformance/translink-queensland-conformance.yml
  title: ''
  type: Conformance
  url: conformance/translink-queensland-conformance.yml
- group: agent
  href: https://artifacts.apis.io/translink-queensland/well-known/translink-queensland-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/translink-queensland-well-known.yml
- group: other
  href: https://artifacts.apis.io/translink-queensland/hosts/translink-queensland-hosts.yml
  title: ''
  type: Hosts
  url: hosts/translink-queensland-hosts.yml
- group: company
  title: ''
  type: Website
  url: https://translink.com.au/
- group: docs
  title: ''
  type: Documentation
  url: https://translink.com.au/about-translink/open-data
- group: commercial
  title: ''
  type: TermsOfService
  url: https://translink.com.au/about-translink/open-data/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://translink.com.au/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://translink.com.au/contact-us
- group: operate
  title: ''
  type: Forum
  url: https://groups.google.com/forum/#!forum/translink-australia-opendata
- group: company
  title: ''
  type: News
  url: https://translink.com.au/news-and-media/releases
- group: company
  title: ''
  type: Twitter
  url: https://x.com/Translink_QLD
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/TransLinkQLD
- group: company
  title: ''
  type: Instagram
  url: https://instagram.com/TransLinkQLD
- group: auth
  href: https://artifacts.apis.io/translink-queensland/security/translink-queensland-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/translink-queensland-domain-security.yml
created: '2026-10-22'
description: 'Translink is the public transport division of the Queensland Government''s Department of Transport and Main Roads, with statewide responsibility for buses, trains, ferries and trams across South East Queensland, regional bus services, demand responsive transit, taxi regulation and long distance rail, coach and regional air services. Through its open data program Translink publishes GTFS schedule datasets and unauthenticated GTFS Realtime v2.0 (Protobuf) feeds of trip updates, vehicle positions and alerts at gtfsrt.api.translink.com.au, licensed CC BY 4.0. (Harvest source: australia-apidays-2026.)'
image: https://framework.transinfo.com.au/v2.5.2.19619/images/logos/MyTL-app-icon@180.png
layout: provider
modified: '2026-10-22'
name: Translink
nav: Providers
network: true
overview: 'Translink is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Public Transport, Transit, GTFS, and GTFS Realtime.


  Translink''s developer surface includes documentation, support, product news, and 14 more developer resources.'
plans:
- name: Translink Queensland Plans Pricing
  plan_count: 1
  slug: translink-queensland-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Translink Queensland Rate Limits
  slug: translink-queensland-rate-limits
score:
  band: emerging
  composite: 21.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 0.0
  previous_composite: 21.0
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 24.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Translink Queensland Authentication
  slug: translink-queensland-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Translink Queensland Domain Security
  slug: translink-queensland-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: translink-queensland
tags:
- Company
- Public Transport
- Transit
- GTFS
- GTFS Realtime
- Open Data
- Government
- Queensland
- Australia
website: https://translink.com.au/
---

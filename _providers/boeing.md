---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
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
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 14.3
  scored_at: '2026-10-31'
api_count: 9
apis:
- description: 'The Boeing Aircraft Models API provides model characteristics of commercial and business aviation aircraft including ICAO/IATA codes, engine specifications, wingspan, weight, and height. Data sourced '
  name: Boeing Aircraft Models API
  slug: boeing-aircraft-models-api
- description: The Boeing Airports and Aerodromes API provides current, worldwide aerodrome data from Jeppesen's aeronautical database, including airport identifiers, location data, and operational information for g
  name: Boeing Airports and Aerodromes API
  slug: boeing-airports-aerodromes-api
- description: The Boeing Airspaces API provides detailed, current information about airspace classifications and boundaries around the globe to support flight planning and air traffic management applications.
  name: Boeing Airspaces API
  slug: boeing-airspaces-api
- description: The Boeing Parts API enables searching and requesting price and availability information for specific Boeing aircraft parts, supporting maintenance, repair, and overhaul operations.
  name: Boeing Parts API
  slug: boeing-parts-api
- description: The Boeing Flight Events API (Beta) provides real-time insights into worldwide flight events, enabling flight tracking applications and operational control systems to monitor global air traffic activi
  name: Boeing Flight Events API
  slug: boeing-flight-events-api
- description: The Boeing NOTAMs API provides access to Jeppesen's global Notices to Air Missions (NOTAMs) database, enabling flight planning systems to retrieve current airspace restrictions and safety information.
  name: Boeing NOTAMs API
  slug: boeing-notams-api
- description: The Boeing Runway Monitor API provides active runway information for arrivals and departures at airports around the world, supporting dispatch and operations control center workflows.
  name: Boeing Runway Monitor API
  slug: boeing-runway-monitor-api
- description: The Boeing Standard Minimums API provides worldwide, detailed, and current information about instrument approach standard minimums for airports globally, supporting flight dispatch and operations plan
  name: Boeing Standard Minimums API
  slug: boeing-standard-minimums-api
- description: The Boeing Taxi Time API provides current taxi time information at airports around the world, enabling airline operations and flight planning systems to optimize departure timing and gate scheduling.
  name: Boeing Taxi Time API
  slug: boeing-taxi-time-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/boeing/well-known/boeing-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/boeing-well-known.yml
- group: other
  href: https://artifacts.apis.io/boeing/hosts/boeing-hosts.yml
  title: ''
  type: Hosts
  url: hosts/boeing-hosts.yml
- group: build
  href: https://artifacts.apis.io/boeing/integrations/boeing-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/boeing-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/boeing/vendors/boeing-vendors.yml
  title: ''
  type: Vendors
  url: vendors/boeing-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boeing.com/privacy-and-cookie-policy
- group: commercial
  href: https://artifacts.apis.io/boeing/plans/boeing-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/boeing-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/boeing/rate-limits/boeing-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/boeing-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/boeing/finops/boeing-finops.yml
  title: ''
  type: FinOps
  url: finops/boeing-finops.yml
- group: auth
  href: https://artifacts.apis.io/boeing/security/boeing-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/boeing-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Boeing
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/boeing
- group: company
  title: ''
  type: Website
  url: https://www.boeing.com
- group: start
  title: ''
  type: Portal
  url: https://developer.boeing.com/
- group: other
  title: ''
  type: APIDirectory
  url: https://developer.boeing.com/apis
- group: company
  title: ''
  type: Blog
  url: https://developer.boeing.com/category/whats-new/
coverage:
  checked: '2026-10-20'
  detail: Boeing Developer Tools (developer.boeing.com, Jeppesen aviation data APIs) publishes no OpenAPI, AsyncAPI or GraphQL contract on any probed host, and the portal stalled every fetch strategy including a headless browser from this run (TLS connects, no response).
  evidence:
  - status: 200
    url: https://www.boeing.com
  - status: 0
    url: https://developer.boeing.com/apis/aircraft-models/
  - status: 404
    url: https://api.boeing.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2025-02-24'
description: Boeing is an American multinational corporation that designs, manufactures, and sells airplanes, rotorcraft, rockets, satellites, and telecommunications equipment. Boeing Developer Tools provides aviation data APIs powered by Jeppesen aeronautical databases, covering aircraft models, airport data, airspace information, NOTAMs, flight events, and runway operations.
finops:
- has_sources: true
  method: generated
  name: Boeing Finops
  primary_unit: ''
  service_category: Aerospace / Aviation Services
  slug: boeing-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/boeing.png
layout: provider
modified: '2026-04-21'
name: Boeing
nav: Providers
network: true
overview: 'Boeing is listed with 9 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Aviation, Airplanes, Aerospace, Flights, and Aeronautical.


  Boeing''s developer surface includes developer portal, engineering blog, and 13 more developer resources.'
plans:
- name: Boeing Plans Pricing
  plan_count: 1
  slug: boeing-plans-pricing
press:
- date: ''
  title: Innovation
  url: https://www.boeing.com/innovation
- date: ''
  title: Boeing HorizonX Invests in Artificial Intelligence Leader ...
  url: https://www.prnewswire.com/news-releases/boeing-horizonx-invests-in-artificial-intelligence-leader-sparkcognition-300479137.html
- date: ''
  title: Boeing Defense, Space & Security Partners with Palantir to ...
  url: https://investors.boeing.com/investors/news/press-release-details/2025/Boeing-Defense-Space--Security-Partners-with-Palantir-to-Accelerate-AI-Adoption-Across-Defense-Classified-Programs/default.aspx
- date: ''
  title: Shaping AI for the Sky
  url: https://www.boeing.com/innovation/innovation-quarterly/2025/12/shaping-ai-for-the-sky
- date: ''
  title: News Releases | Boeing Newsroom
  url: https://boeing.mediaroom.com/news-releases-statements?item=131225
random_paper: 4
rate_limits:
- limit_count: 1
  name: Boeing Rate Limits
  slug: boeing-rate-limits
score:
  band: emerging
  composite: 15.1
  coverage:
    artifact_dirs: 13
    catalog_earned: 39.0
    catalog_earned_first_party: 0.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 62.5
    operational_transparency: 10.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 15.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/boeing/boeing-2026-06-20T173551.png
security:
- kind: domain-security
  name: Boeing Domain Security
  slug: boeing-domain-security
  summary_line: TLSv1.3 · DMARC
slug: boeing
tags:
- Aviation
- Airplanes
- Aerospace
- Flights
- Aeronautical
- Fortune 100
website: https://www.boeing.com
---

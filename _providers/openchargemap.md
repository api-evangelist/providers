---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Openchargemap Agentic Access
  operation_count: 6
  slug: openchargemap-agentic-access
  summary_line: 6 operations · 3 acting
api_count: 9
apis:
- description: Primary REST API for searching and retrieving EV charging station data (Points of Interest) from the Open Charge Map global registry. Supports geographic search by latitude/longitude with distance rad
  name: Open Charge Map POI API
  slug: open-charge-map-poi-api
- description: REST API endpoint returning core reference data used for interpreting POI results, including connection types, charging levels, operators, countries, status types, usage types, supply types (AC/DC), a
  name: Open Charge Map Reference Data API
  slug: open-charge-map-reference-data-api
- description: 'REST API endpoint for contributing new EV charging station data or updating existing POI records in the Open Charge Map global registry. Requires an authenticated API key associated with a registered '
  name: Open Charge Map POI Submit API
  slug: open-charge-map-poi-submit-api
- description: The Comment API from Open Charge Map — 1 operation(s) for comment.
  name: Open Charge Map Comment API
  slug: openchargemap-comment-api
- description: The Mediaitem API from Open Charge Map — 1 operation(s) for mediaitem.
  name: Open Charge Map Mediaitem API
  slug: openchargemap-mediaitem-api
- description: The Openapi API from Open Charge Map — 1 operation(s) for openapi.
  name: Open Charge Map Openapi API
  slug: openchargemap-openapi-api
- description: The Poi API from Open Charge Map — 1 operation(s) for poi.
  name: Open Charge Map Poi API
  slug: openchargemap-poi-api
- description: The Profile API from Open Charge Map — 1 operation(s) for profile.
  name: Open Charge Map Profile API
  slug: openchargemap-profile-api
- description: The Referencedata API from Open Charge Map — 1 operation(s) for referencedata.
  name: Open Charge Map Referencedata API
  slug: openchargemap-referencedata-api
artifact_total: 40
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openchargemap-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openchargemap-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openchargemap-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://openchargemap.org/
- group: docs
  title: ''
  type: Documentation
  url: https://openchargemap.org/site/develop/api
- group: other
  title: ''
  type: Developer
  url: https://openchargemap.org/site/develop
- group: build
  title: ''
  type: GitHub
  url: https://github.com/openchargemap/ocm-system
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/openchargemap
- group: operate
  title: ''
  type: Community
  url: https://community.openchargemap.org/
- group: other
  title: ''
  type: Apps
  url: https://openchargemap.org/site/develop/apps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://openchargemap.org/site/about/terms
- group: company
  title: ''
  type: About
  url: https://openchargemap.org/site/about
- group: commercial
  title: ''
  type: Plans
  url: plans/openchargemap-plans.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openchargemap-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/openchargemap-finops.yml
created: '2026-06-13'
description: Open Charge Map is the global public registry of electric vehicle charging locations, established in 2011 as a non-commercial, community-driven project. The platform maintains a crowdsourced dataset of 300,000+ charging points worldwide, combining manually entered data with imported open data from government registries and charging networks. The REST API enables developers to search and retrieve POI (Points of Interest) data on EV charging stations, including location details, equipment specifications, connection types, operator information, and user-submitted check-ins and photos. Data can be filtered by geographic coordinates, bounding box, country, operator, connection type, charging level, and operational status. The API is free to use with an API key registration and supports both read (GET) and write (POST) operations for contributing new charging location data.
examples:
- key_count: 3
  name: Authenticate
  slug: authenticate
- key_count: 3
  name: Geo Bounding Box Search
  slug: geo-bounding-box-search
- key_count: 3
  name: Poi Search
  slug: poi-search
- key_count: 3
  name: Reference Data
  slug: reference-data
finops:
- name: Openchargemap Finops
  service_category: ''
  slug: openchargemap-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openchargemap.png
json_schemas:
- name: AddressInfo
  property_count: 18
  slug: AddressInfo
- name: AuthenticationResult
  property_count: 2
  slug: AuthenticationResult
- name: CheckinStatusType
  property_count: 4
  slug: CheckinStatusType
- name: ConnectionInfo
  property_count: 15
  slug: ConnectionInfo
- name: ConnectionType
  property_count: 5
  slug: ConnectionType
- name: CoreReferenceData
  property_count: 13
  slug: CoreReferenceData
- name: Country
  property_count: 4
  slug: Country
- name: DataProvider
  property_count: 10
  slug: DataProvider
- name: LevelType
  property_count: 4
  slug: LevelType
- name: MediaItem
  property_count: 11
  slug: MediaItem
- name: OperatorInfo
  property_count: 12
  slug: OperatorInfo
- name: POI
  property_count: 30
  slug: POI
- name: StatusType
  property_count: 4
  slug: StatusType
- name: SubmissionStatusType
  property_count: 3
  slug: SubmissionStatusType
- name: SupplyType
  property_count: 2
  slug: SupplyType
- name: UsageType
  property_count: 5
  slug: UsageType
- name: UserComment
  property_count: 11
  slug: UserComment
- name: UserCommentType
  property_count: 2
  slug: UserCommentType
- name: UserInfo
  property_count: 4
  slug: UserInfo
- name: UserProfile
  property_count: 14
  slug: UserProfile
layout: provider
modified: '2026-06-13'
name: Open Charge Map
nav: Providers
network: true
overview: 'Open Charge Map publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Comment API, Mediaitem API, Openapi API, and 3 more. Tagged areas include Electric Vehicles, EV Charging, Charging Stations, Points of Interest, and Open Data.


  The Open Charge Map catalog on APIs.io includes 1 Spectral governance ruleset.


  Open Charge Map''s developer surface includes authentication, documentation, GitHub presence, and 12 more developer resources.'
plans:
- name: Openchargemap Plans
  plan_count: 2
  slug: openchargemap-plans
random_paper: 94
rate_limits:
- limit_count: 4
  name: Openchargemap Rate Limits
  slug: openchargemap-rate-limits
rules:
- name: Open Charge Map API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: openchargemap-jsonschema-spectral-rules
score:
  band: developing
  composite: 43.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 62.3
    developer_ergonomics: 23.9
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 43.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 21.6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openchargemap/refs/heads/main/screenshots/openchargemap-2026-06-20T190925.png
security:
- kind: authentication
  name: Openchargemap Authentication
  slug: openchargemap-authentication
  summary_line: apiKey/http · 3 schemes
- kind: domain-security
  name: Openchargemap Domain Security
  slug: openchargemap-domain-security
  summary_line: TLSv1.3 · DMARC
slug: openchargemap
tags:
- Electric Vehicles
- EV Charging
- Charging Stations
- Points of Interest
- Open Data
- Geospatial
- Transportation
- Clean Energy
- Crowdsourced
- Registry
website: https://openchargemap.org/
---

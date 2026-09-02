---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Blink Agentic Access
  operation_count: 3
  slug: blink-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Geo-radius search for Blink charging station locations.
  name: Blink Charging Locations API
  slug: blink-locations-api
- description: Name-based search for Blink charging station locations.
  name: Blink Charging Search API
  slug: blink-search-api
- description: Live status lookup for a single Blink charging location.
  name: Blink Charging Status API
  slug: blink-status-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Blink Charging & Status API (BlinkMap API) Locations API
  slug: open-blink-locations-api
- collection_type: open
  name: Blink Charging & Status API (BlinkMap API) Locations Search API
  slug: open-blink-search-api
- collection_type: open
  name: Blink Charging & API (BlinkMap API) Locations Status API
  slug: open-blink-status-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/blink-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/blink-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/blink-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/blinkcharging
- group: company
  title: ''
  type: Website
  url: https://blinkcharging.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blinkcharging
- group: docs
  title: ''
  type: Documentation
  url: https://prod.blinknetwork.com/developer.html
- group: company
  title: ''
  type: News
  url: https://blinkcharging.com/news/blink-and-presto-announce-strategic-collaboration-to-provide-advanced-tools-for-ev-fleet-charging
- group: company
  title: ''
  type: News
  url: https://blinkcharging.com/news/hubject-teams-with-blink-charging-to-further-expand-intercharge-network-across-north-america
created: '2026-07-03'
description: Blink Charging Co. (Nasdaq BLNK) operates the Blink Network of Level 2 and DC Fast electric vehicle chargers across North America and Europe, alongside brands acquired via SemaConnect, Blue Corner, BlueLA, and Envoy. Blink's charger hardware (Series 7/8/9) is OCPP 2.0.1 certified for CSMS interoperability, and in 2025 Blink joined Hubject's Intercharge eRoaming platform as a charge point operator using the OCPI protocol so third-party e-mobility service providers can route drivers and billing to Blink stations. Blink also runs a gated BlinkMap API developer program (station locations, hours, and live network status) and a Blink Fleet platform that partners such as Presto and BetterFleet integrate with via API for fleet charging, sessions, and billing. None of these programs currently publish a full public self-serve API reference; access requires signing up directly with Blink.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/blink.png
layout: provider
modified: '2026-07-25'
name: Blink Charging
nav: Providers
network: true
overview: 'Blink Charging publishes 3 APIs on the [APIs.io](https://apis.io/) network: Locations API, Search API, and Status API. Tagged areas include EV Charging, Electric Vehicle, Charging Stations, OCPI, and OCPP.


  Blink Charging''s developer surface includes authentication, documentation, product news, and 6 more developer resources.'
random_paper: 3
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 6
    catalog_gap: 78.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 13.4
    developer_ergonomics: 16.7
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 12.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 16.7
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/blink/refs/heads/main/screenshots/blink-2026-07-25T203318.png
security:
- kind: authentication
  name: Blink Authentication
  slug: blink-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Blink Domain Security
  slug: blink-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: blink
tags:
- EV Charging
- Electric Vehicle
- Charging Stations
- OCPI
- OCPP
- Fleet Management
- Roaming
- DC Fast Charging
website: https://blinkcharging.com
---

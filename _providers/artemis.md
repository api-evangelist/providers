---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Artemis Agentic Access
  operation_count: 8
  slug: artemis-agentic-access
  summary_line: 8 operations
api_count: 1
apis:
- description: NASA's Open API platform at api.nasa.gov provides programmatic access to NASA data including the Astronomy Picture of the Day (APOD), Near Earth Object Web Service (NeoWs), NASA Image and Video Librar
  name: NASA Open APIs
  slug: nasa-open-api
- description: The NASA Technology Transfer API provides programmatic access to the NASA patent portfolio, software catalog, and spinoff technologies developed through the Artemis program and other NASA missions, en
  name: NASA Technology Transfer API
  slug: nasa-tech-transfer-api
- description: Astronomy Picture of the Day
  name: Artemis APOD API
  slug: artemis-apod-api
- description: Space Weather Database Of Notifications, Knowledge, Information
  name: Artemis DONKI API
  slug: artemis-donki-api
- description: Earth Polychromatic Imaging Camera
  name: Artemis EPIC API
  slug: artemis-epic-api
- description: NASA Image and Video Library
  name: Artemis Images API
  slug: artemis-images-api
- description: Near Earth Object Web Service
  name: Artemis NeoWs API
  slug: artemis-neows-api
artifact_total: 29
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NASA Open APIs (Artemis-relevant subset) APOD API
  slug: open-artemis-apod-api
- collection_type: open
  name: NASA Open APIs (Artemis-relevant subset) APOD DONKI API
  slug: open-artemis-donki-api
- collection_type: open
  name: NASA Open APIs (Artemis-relevant subset) APOD EPIC API
  slug: open-artemis-epic-api
- collection_type: open
  name: NASA Open APIs (Artemis-relevant subset) APOD Images API
  slug: open-artemis-images-api
- collection_type: open
  name: NASA Open APIs (Artemis-relevant subset) APOD NeoWs API
  slug: open-artemis-neows-api
- collection_type: open
  name: NASA Open APIs (Artemis-relevant subset)
  slug: open-artemis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/artemis-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/artemis-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/artemis-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://www.nasa.gov/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/artemisag
- group: start
  title: Artemis Program Website
  type: Portal
  url: https://www.nasa.gov/artemis/
- group: docs
  title: NASA Open APIs
  type: Documentation
  url: https://api.nasa.gov/
- group: build
  title: NASA GitHub Organization
  type: GitHubOrganization
  url: https://github.com/nasa
- group: start
  title: API Key Signup
  type: Signup
  url: https://api.nasa.gov/#signUp
- group: commercial
  title: Privacy Policy
  type: PrivacyPolicy
  url: https://www.nasa.gov/privacy/
created: '2024-01-15'
description: NASA's Artemis program is the next generation of lunar exploration, aiming to return humans to the Moon and establish a sustainable presence for future missions to Mars. The program includes the Space Launch System (SLS) rocket, Orion spacecraft, the Lunar Gateway space station, and commercial lunar landers from SpaceX and Blue Origin. NASA's Open APIs provide programmatic access to Artemis-related data, including mission imagery, space weather, and planetary data through api.nasa.gov. The program operates under NASA's Science Mission Directorate and Exploration Systems Development Mission Directorate.
features:
- description: Daily NASA astronomy images with descriptions and metadata, providing a public showcase of space imagery relevant to Artemis and broader space exploration.
  name: Astronomy Picture of the Day API
- description: NeoWs API provides data on near earth asteroids and their orbital parameters, supporting space situational awareness for lunar missions.
  name: Near Earth Object Web Service
- description: Access to photos captured by Curiosity, Opportunity, and Spirit Mars rovers, providing precursor science data for future crewed Mars missions planned after Artemis establishes lunar presence.
  name: Mars Rover Photos API
- description: Earth Polychromatic Imaging Camera imagery showing full-disc Earth imagery, relevant to climate monitoring that informs long-duration space missions.
  name: EPIC Earth Imagery
- description: DONKI API provides solar flare, geomagnetic storm, and space weather data critical for mission planning and crew safety on Artemis lunar missions.
  name: Space Weather Database Of Notifications, Knowledge, Information
finops:
- name: Artemis Finops
  service_category: API
  slug: artemis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/artemis.png
layout: provider
modified: '2026-04-19'
name: Artemis
nav: Providers
network: true
overview: 'Artemis publishes 5 APIs on the [APIs.io](https://apis.io/) network, including APOD API, DONKI API, EPIC API, and 2 more. Tagged areas include Exploration, Lunar, Moon, NASA, and Space.


  Artemis'' developer surface includes authentication, engineering blog, developer portal, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Artemis Plans Pricing
  plan_count: 3
  slug: artemis-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Artemis Rate Limits
  slug: artemis-rate-limits
score:
  band: thin
  composite: 37.2
  coverage:
    artifact_dirs: 10
    catalog_gap: 69.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 39.3
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 37.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/artemis/refs/heads/main/screenshots/artemis-2026-06-20T172440.png
security:
- kind: authentication
  name: Artemis Authentication
  slug: artemis-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Artemis Domain Security
  slug: artemis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: artemis
tags:
- Exploration
- Lunar
- Moon
- NASA
- Space
- Government
use_cases:
- description: Researchers and mission planners integrate NASA Open APIs to build dashboards and tools that aggregate space weather, trajectory, and imagery data for Artemis mission support.
  name: Mission Data Integration
- description: Educators and developers build Artemis-themed applications using NASA imagery and mission data to engage the public in lunar exploration.
  name: Education and Outreach
- description: Scientists access planetary and space environment data programmatically to support research that informs Artemis crew safety and mission planning.
  name: Research Applications
- description: Companies and universities query the NASA Technology Transfer API to identify Artemis-developed patents and software available for licensing.
  name: Technology Transfer
website: https://www.nasa.gov/artemis/
---

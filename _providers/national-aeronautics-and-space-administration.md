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
  scored_at: '2026-08-26'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: National Aeronautics And Space Administration Agentic Access
  operation_count: 12
  slug: national-aeronautics-and-space-administration-agentic-access
  summary_line: 12 operations
api_count: 20
apis:
- description: One of the most popular websites at NASA is the Astronomy Picture of the Day. This API exposes the same featured image with metadata.
  name: APOD - Astronomy Picture of the Day
  slug: apod
- description: Near Earth Object Web Service is a RESTful web service for near earth Asteroid information including closest approach data and orbital data.
  name: NeoWs - Near Earth Object Web Service
  slug: neows
- description: The Space Weather Database Of Notifications, Knowledge, Information (DONKI) is a comprehensive online tool for space weather forecasters, scientists, and researchers.
  name: DONKI - Space Weather Database Of Notifications, Knowledge, Information
  slug: donki
- description: Earth imagery API providing Landsat 8 imagery and asset metadata for a given lat/lon location and date.
  name: Earth Imagery and Assets
  slug: earth
- description: EONET is a prototype web service that provides a curated source of continuously updated natural event metadata.
  name: EONET - Earth Observatory Natural Event Tracker
  slug: eonet
- description: The EPIC API provides full disc imagery of the Earth captured by the DSCOVR spacecraft, including natural and enhanced color images.
  name: EPIC - Earth Polychromatic Imaging Camera
  slug: epic
- description: Image data gathered by NASA's Curiosity, Opportunity, Perseverance, and Spirit rovers on Mars, accessible through this API.
  name: Mars Rover Photos
  slug: mars-rover-photos
- description: The NASA Image and Video Library API exposes the public NASA media library content including imagery, video, and audio.
  name: NASA Image and Video Library
  slug: nasa-image-library
- description: The TLE API provides up to date two line element set records, the standardized format for distributing earth-orbiting object orbital data.
  name: TLE - Two Line Element Set
  slug: tle
- description: Programmatic access to NASA's Exoplanet Archive database of confirmed exoplanets and planet candidates.
  name: Exoplanet Archive API
  slug: exoplanet
- description: Per-Sol summary data for each of the last seven available Sols (Martian days) from the InSight lander on Mars.
  name: InSight - Mars Weather Service
  slug: insight
- description: RESTful web services to make NASA technology project data available in a machine readable format.
  name: TechPort
  slug: techport
- description: Provides access to a number of resources from the Solar System Dynamics group and the Center for Near-Earth Object Studies.
  name: SSD/CNEOS - Solar System Dynamics and Center for Near-Earth Object Studies
  slug: ssd-cneos
- description: Astronomy Picture of the Day.
  name: The National Aeronautics and Space Administration APOD API
  slug: national-aeronautics-and-space-administration-apod-api
- description: Space Weather Database Of Notifications, Knowledge, Information.
  name: The National Aeronautics and Space Administration DONKI API
  slug: national-aeronautics-and-space-administration-donki-api
- description: Earth imagery and assets.
  name: The National Aeronautics and Space Administration Earth API
  slug: national-aeronautics-and-space-administration-earth-api
- description: Earth Polychromatic Imaging Camera.
  name: The National Aeronautics and Space Administration EPIC API
  slug: national-aeronautics-and-space-administration-epic-api
- description: Mars weather from the InSight lander.
  name: The National Aeronautics and Space Administration InSight API
  slug: national-aeronautics-and-space-administration-insight-api
- description: Photos from Curiosity, Opportunity, Perseverance, and Spirit.
  name: The National Aeronautics and Space Administration Mars Rover Photos API
  slug: national-aeronautics-and-space-administration-mars-rover-photos-api
- description: Near Earth Object Web Service.
  name: The National Aeronautics and Space Administration NeoWs API
  slug: national-aeronautics-and-space-administration-neows-api
artifact_total: 35
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NASA Open APIs APOD API
  slug: open-national-aeronautics-and-space-administration-apod-api
- collection_type: open
  name: NASA Open APIs APOD DONKI API
  slug: open-national-aeronautics-and-space-administration-donki-api
- collection_type: open
  name: NASA Open APIs APOD Earth API
  slug: open-national-aeronautics-and-space-administration-earth-api
- collection_type: open
  name: NASA Open APIs APOD EPIC API
  slug: open-national-aeronautics-and-space-administration-epic-api
- collection_type: open
  name: NASA Open APIs APOD InSight API
  slug: open-national-aeronautics-and-space-administration-insight-api
- collection_type: open
  name: NASA Open APIs APOD Mars Rover Photos API
  slug: open-national-aeronautics-and-space-administration-mars-rover-photos-api
- collection_type: open
  name: NASA Open APIs APOD NeoWs API
  slug: open-national-aeronautics-and-space-administration-neows-api
- collection_type: open
  name: NASA Open APIs
  slug: open-national-aeronautics-and-space-administration
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/nasa/apod-api/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/nasa/apod-api/releases
- group: commercial
  title: ''
  type: License
  url: https://github.com/nasa/apod-api/blob/master/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-aeronautics-and-space-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-aeronautics-and-space-administration-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-aeronautics-and-space-administration-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nasa
- group: start
  title: ''
  type: Portal
  url: https://api.nasa.gov/
- group: company
  title: ''
  type: Website
  url: https://www.nasa.gov/
- group: start
  title: ''
  type: Signup
  url: https://api.nasa.gov/#signUp
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nasa.gov/about/highlights/HP_Privacy.html
- group: company
  title: ''
  type: Blog
  url: https://www.nasa.gov/feed/
created: '2024-01-01'
description: NASA explores the unknown in air and space, innovates for the benefit of humanity, and inspires the world through discovery. The api.nasa.gov portal hosts a federated set of APIs that make NASA imagery, science, and mission data accessible to application developers.
finops:
- name: National Aeronautics And Space Administration Finops
  service_category: API
  slug: national-aeronautics-and-space-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-aeronautics-and-space-administration.png
layout: provider
modified: '2026-04-28'
name: The National Aeronautics and Space Administration
nav: Providers
network: true
overview: 'The National Aeronautics and Space Administration publishes 7 APIs on the [APIs.io](https://apis.io/) network, including APOD API, DONKI API, Earth API, and 4 more. Tagged areas include Government, Science, Space, Imagery, and Earth Observation.


  The National Aeronautics and Space Administration''s developer surface includes authentication, developer portal, signup flow, engineering blog, and 8 more developer resources.'
plans:
- name: National Aeronautics And Space Administration Plans Pricing
  plan_count: 3
  slug: national-aeronautics-and-space-administration-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: National Aeronautics And Space Administration Rate Limits
  slug: national-aeronautics-and-space-administration-rate-limits
score:
  band: thin
  composite: 39.1
  delta: 2.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 45.6
    developer_ergonomics: 33.3
    discoverability: 81.5
    governance: 0.0
    operational_transparency: 28.9
  previous_composite: 36.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 29.6
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-aeronautics-and-space-administration/refs/heads/main/screenshots/national-aeronautics-and-space-administration-2026-06-20T185958.png
security:
- kind: authentication
  name: National Aeronautics And Space Administration Authentication
  slug: national-aeronautics-and-space-administration-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: National Aeronautics And Space Administration Domain Security
  slug: national-aeronautics-and-space-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: national-aeronautics-and-space-administration
tags:
- Government
- Science
- Space
- Imagery
- Earth Observation
website: https://www.nasa.gov/
---

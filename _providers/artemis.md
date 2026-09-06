---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
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
  score: 27.3
  scored_at: '2026-09-05'
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
- baseURL: https://api.nasa.gov
  baseurl_source: declared
  description: Astronomy Picture of the Day
  name: Artemis APOD API
  slug: artemis-apod-api
- baseURL: https://api.nasa.gov
  baseurl_source: declared
  description: Space Weather Database Of Notifications, Knowledge, Information
  name: Artemis DONKI API
  slug: artemis-donki-api
- baseURL: https://api.nasa.gov
  baseurl_source: declared
  description: Earth Polychromatic Imaging Camera
  name: Artemis EPIC API
  slug: artemis-epic-api
- baseURL: https://api.nasa.gov
  baseurl_source: declared
  description: NASA Image and Video Library
  name: Artemis Images API
  slug: artemis-images-api
- baseURL: https://api.nasa.gov
  baseurl_source: declared
  description: Near Earth Object Web Service
  name: Artemis NeoWs API
  slug: artemis-neows-api
- baseURL: https://techport.nasa.gov/api
  baseurl_source: declared
  description: TechPort is NASA's public catalog of its technology development projects, including the technology investments made through the Artemis program. The API returns project records — funding, work locatio
  name: NASA TechPort API
  slug: nasa-techport-api
artifact_total: 31
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
- group: company
  title: ''
  type: Website
  url: https://www.nasa.gov/artemis/
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
- group: operate
  title: NASA API catalog issue tracker
  type: Support
  url: https://github.com/nasa/api-docs/issues
- group: commercial
  title: NASA Media Usage Guidelines
  type: TermsOfService
  url: https://www.nasa.gov/nasa-brand-center/images-and-media/
- group: auth
  title: NASA Vulnerability Disclosure Policy
  type: Security
  url: https://www.nasa.gov/vulnerability-disclosure-policy/
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/artemis-vulnerability-disclosure.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/artemis-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/artemis-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/artemis-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/artemis-plans-pricing.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/artemis-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/artemis-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/artemis-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/artemis-packages.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/artemis-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: Candidate MCP tool list derived from the OpenAPI — NASA ships no MCP server
  type: X-MCPServerCandidate
  url: mcp/artemis-mcp.yml
- group: other
  title: Moon Trek LRO WAC global lunar mosaic — OGC WMTS 1.0.0
  type: GetCapabilities
  url: https://trek.nasa.gov/tiles/Moon/EQ/LRO_WAC_Mosaic_Global_303ppd_v02/1.0.0/WMTSCapabilities.xml
- group: other
  title: api.nasa.gov Mars WMTS catalog — OGC WMTS 1.0.0
  type: GetCapabilities
  url: https://api.nasa.gov/mars-wmts/catalog/Mars_Viking_MDIM21_ClrMosaic_global_232m/1.0.0/WMTSCapabilities.xml
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
modified: '2026-09-04'
name: Artemis
nav: Providers
network: true
overview: 'Artemis publishes 6 APIs on the [APIs.io](https://apis.io/) network, including APOD API, DONKI API, EPIC API, and 3 more. Tagged areas include Exploration, Lunar, Moon, NASA, and Space.


  Artemis'' developer surface includes authentication, engineering blog, developer portal, documentation, signup flow, support, and 21 more developer resources.'
plans:
- name: Artemis Plans Pricing
  plan_count: 2
  slug: artemis-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 3
  name: Artemis Rate Limits
  slug: artemis-rate-limits
score:
  band: developing
  composite: 52.5
  coverage:
    artifact_dirs: 24
    catalog_earned: 60.0
    catalog_earned_first_party: 20.0
    catalog_gap: 55.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.2
  facets:
    access_clarity: 63.2
    commercial_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 46.8
    developer_ergonomics: 36.3
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 44.7
  previous_composite: 53.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 57.4
  schema_version: 0.18.3
  scored_at: '2026-09-05'
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
- kind: vulnerability-disclosure
  name: Artemis Vulnerability Disclosure
  slug: artemis-vulnerability-disclosure
  summary_line: Bugcrowd
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

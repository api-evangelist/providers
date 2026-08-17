---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Nasa Agentic Access
  operation_count: 24
  slug: nasa-agentic-access
  summary_line: 24 operations
api_count: 9
apis:
- description: The Asset API from NASA — 1 operation(s) for asset.
  name: NASA Asset API
  slug: nasa-asset-api
- description: The Captions API from NASA — 1 operation(s) for captions.
  name: NASA Captions API
  slug: nasa-captions-api
- description: The DONKI API from NASA — 8 operation(s) for donki.
  name: NASA DONKI API
  slug: nasa-donki-api
- description: The EPIC API from NASA — 5 operation(s) for epic.
  name: NASA EPIC API
  slug: nasa-epic-api
- description: The Mars Photos API from NASA — 3 operation(s) for mars photos.
  name: NASA Mars Photos API
  slug: nasa-mars-photos-api
- description: The Metadata API from NASA — 1 operation(s) for metadata.
  name: NASA Metadata API
  slug: nasa-metadata-api
- description: The Neo API from NASA — 3 operation(s) for neo.
  name: NASA Neo API
  slug: nasa-neo-api
- description: The Planetary API from NASA — 1 operation(s) for planetary.
  name: NASA Planetary API
  slug: nasa-planetary-api
- description: The Search API from NASA — 1 operation(s) for search.
  name: NASA Search API
  slug: nasa-search-api
arazzos:
- description: Pull the Astronomy Picture of the Day and enrich it with related assets from the NASA Image and Video Library.
  name: NASA APOD Daily Digest
  slug: nasa-apod-daily-digest-workflow
- description: Poll DONKI space weather notifications and branch to the matching event endpoint for the detail the alert omits.
  name: NASA DONKI Notification Triage
  slug: nasa-donki-notification-triage-workflow
- description: Walk one space weather window end to end — solar flare, coronal mass ejection, CME analysis, interplanetary shock, geomagnetic storm.
  name: NASA DONKI Space Weather Event Chain
  slug: nasa-donki-space-weather-event-chain-workflow
- description: List the dates EPIC actually has imagery for, then pull both natural and enhanced color metadata for one of them.
  name: NASA EPIC Earth Imagery Retrieval
  slug: nasa-epic-earth-imagery-workflow
- description: Read a rover's mission manifest to find a sol that actually has photos, then harvest that sol's images.
  name: NASA Mars Rover Photo Harvest
  slug: nasa-mars-rover-photo-harvest-workflow
- description: Search the NASA Image and Video Library, then resolve the downloadable files, metadata, and captions for a match.
  name: NASA Media Asset Retrieval
  slug: nasa-media-asset-retrieval-workflow
- description: Page the asteroid catalog, look up a specific near-Earth object, and pull every other object approaching on the same date.
  name: NASA Near Earth Object Close Approach Analysis
  slug: nasa-neo-close-approach-analysis-workflow
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) API
  slug: open-nasa-apod
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset API
  slug: open-nasa-asset-api
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset Captions API
  slug: open-nasa-captions-api
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset DONKI API
  slug: open-nasa-donki-api
- collection_type: open
  name: NASA DONKI (Space Weather Database Of Notifications, Knowledge, Information) API
  slug: open-nasa-donki
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset EPIC API
  slug: open-nasa-epic-api
- collection_type: open
  name: NASA EPIC (Earth Polychromatic Imaging Camera) API
  slug: open-nasa-epic
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset Mars Photos API
  slug: open-nasa-mars-photos-api
- collection_type: open
  name: NASA Mars Rover Photos API
  slug: open-nasa-mars-rover-photos
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset Metadata API
  slug: open-nasa-metadata-api
- collection_type: open
  name: NASA Image and Video Library API
  slug: open-nasa-nasa-image-and-video-library
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset Neo API
  slug: open-nasa-neo-api
- collection_type: open
  name: NASA NeoWs (Near Earth Object Web Service) API
  slug: open-nasa-neo
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset Planetary API
  slug: open-nasa-planetary-api
- collection_type: open
  name: NASA Astronomy Picture of the Day (APOD) Asset Search API
  slug: open-nasa-search-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nasa-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nasa-domain-security.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nasa-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nasa-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/nasa-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nasa-well-known.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nasa-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nasa-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/nasa-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nasa-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nasa-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nasa-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nasa-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/nasa-sandbox.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/nasa-apod-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nasa-donki-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nasa-epic-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nasa-mars-rover-photos-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nasa-nasa-image-and-video-library-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nasa-neo-overlay.yaml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-apod-daily-digest-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-media-asset-retrieval-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-mars-rover-photo-harvest-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-neo-close-approach-analysis-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-epic-earth-imagery-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-donki-space-weather-event-chain-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/nasa-donki-notification-triage-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/nasa
- group: start
  title: ''
  type: Portal
  url: https://api.nasa.gov
- group: company
  title: ''
  type: Website
  url: https://www.nasa.gov
- group: docs
  title: ''
  type: Documentation
  url: https://data.nasa.gov
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/nasa
- group: company
  title: ''
  type: Blog
  url: https://www.nasa.gov/feed/
created: '2025-01-01'
description: NASA (National Aeronautics and Space Administration) provides a suite of public APIs at api.nasa.gov offering access to space, Earth science, and aeronautics data. Key APIs include Astronomy Picture of the Day (APOD), Mars Rover Photos, Near Earth Object Web Service (NeoWs), DONKI space weather events, EPIC Earth imagery, and the NASA Image and Video Library. All APIs are free and accessible with an API key.
finops:
- name: Nasa Finops
  service_category: Open Data / Public Sector
  slug: nasa-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/nasa.png
json_schemas:
- name: APOD Image
  property_count: 9
  slug: apod-image
- name: Rover Camera
  property_count: 4
  slug: camera
- name: Close Approach
  property_count: 6
  slug: close-approach
- name: Coronal Mass Ejection
  property_count: 8
  slug: coronal-mass-ejection
- name: EPIC Image
  property_count: 10
  slug: epic-image
- name: Geomagnetic Storm
  property_count: 3
  slug: geomagnetic-storm
- name: Near Earth Object
  property_count: 9
  slug: near-earth-object
- name: Mars Rover Photo
  property_count: 6
  slug: rover-photo
- name: Mars Rover
  property_count: 5
  slug: rover
- name: Solar Flare
  property_count: 8
  slug: solar-flare
jsonld:
- class_count: 35
  name: Nasa Context
  property_count: 0
  slug: nasa-context
layout: provider
mcp_servers:
- description: ''
  name: nasa-mcp.yml
  slug: nasa-mcpyml
modified: '2026-06-20'
name: NASA
nav: Providers
network: true
overview: 'NASA publishes 9 APIs on the [APIs.io](https://apis.io/) network, including Asset API, Captions API, DONKI API, and 6 more. Tagged areas include Government, Science, and Space.


  The NASA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  NASA''s developer surface includes authentication, sandbox, developer portal, documentation, engineering blog, and 28 more developer resources.'
plans:
- name: Nasa Plans Pricing
  plan_count: 3
  slug: nasa-plans-pricing
random_paper: 121
rate_limits:
- limit_count: 3
  name: Nasa Rate Limits
  slug: nasa-rate-limits
rules:
- name: NASA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: nasa-jsonschema-spectral-rules
score:
  band: developing
  composite: 42.0
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 58.3
    developer_ergonomics: 39.1
    discoverability: 63.0
    governance: 69.8
    operational_transparency: 13.2
  previous_composite: 42.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/nasa/refs/heads/main/screenshots/nasa-2026-06-20T185945.png
security:
- kind: authentication
  name: Nasa Authentication
  slug: nasa-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nasa Domain Security
  slug: nasa-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Nasa Vulnerability Disclosure
  slug: nasa-vulnerability-disclosure
  summary_line: Bugcrowd · contact published
slug: nasa
tags:
- Government
- Science
- Space
website: https://www.nasa.gov
---

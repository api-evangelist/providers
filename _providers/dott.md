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
  band: agent-ready
  dimensions:
    agent_skills: true
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: true
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 57.7
  scored_at: '2026-07-27'
api_count: 5
apis:
- description: Auto-discovery of available feeds and cities
  name: Dott Discovery API
  slug: dott-discovery-api
- description: Docked station information and status (where applicable)
  name: Dott Stations API
  slug: dott-stations-api
- description: System-level metadata and pricing
  name: Dott System API
  slug: dott-system-api
- description: Free-floating vehicle status and types
  name: Dott Vehicles API
  slug: dott-vehicles-api
- description: Geofencing / operating zones
  name: Dott Zones API
  slug: dott-zones-api
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://ridedott.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://ridedott.dev
- group: docs
  title: ''
  type: Documentation
  url: https://ridedott.dev/docs/services/gbfs/introduction/
- group: docs
  title: ''
  type: APIReference
  url: https://gbfs.documentation.ridedott.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://ridedott.dev/docs/services/gbfs/get-started-gbfs/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ridedott
- group: company
  title: ''
  type: Blog
  url: https://ridedott.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ridedott.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ridedott.com/privacy/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/dott-gbfs-openapi.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/dott-gbfs-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/dott-system_information-espoo.json
- group: auth
  title: ''
  type: Authentication
  url: authentication/dott-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/dott-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/dott-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/dott-data-model.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/dott-conformance.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/dott-lifecycle.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/dott-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/dott-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/dott-domain-security.yml
created: '2026-07-17'
description: 'Dott is a European shared micromobility operator running fleets of electric scooters and e-bikes across 250+ cities in Europe and the Middle East. Formed from the 2024 merger of Dott and TIER (the TIER brand was retired into the Dott app that year), the company is headquartered in Amsterdam, Berlin and Paris. For developers and mobility-data partners, Dott publishes its fleet data through the open GBFS 2.3 standard: real-time vehicle locations, vehicle types, per-city pricing plans, geofencing zones and station data are served from gbfs.api.ridedott.com, with an authenticated partner variant carrying stable (non-rotating) vehicle IDs. Originally added to the API Evangelist network as a SoftBank Vision Fund portfolio lead, enriched from its live public developer surface.'
examples:
- key_count: 5
  name: Dott Gbfs Discovery
  slug: dott-gbfs-discovery
- key_count: 4
  name: Dott Gbfs_Versions
  slug: dott-gbfs_versions
- key_count: 4
  name: Dott System_Information Espoo
  slug: dott-system_information-espoo
- key_count: 4
  name: Dott System_Pricing_Plans Espoo
  slug: dott-system_pricing_plans-espoo
- key_count: 4
  name: Dott Vehicle_Types Espoo
  slug: dott-vehicle_types-espoo
image: https://avatars.githubusercontent.com/u/45282822?v=4
layout: provider
mcp_servers:
- description: ''
  name: dott-mcp.yml
  slug: dott-mcpyml
modified: '2026-07-18'
name: Dott
nav: Providers
network: true
overview: 'Dott publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Stations API, System API, and 2 more. Tagged areas include Company, Transportation, Micromobility, Mobility, and E-Scooter.


  Dott''s developer surface includes documentation, API reference, getting-started guide, engineering blog, code examples, authentication, and 16 more developer resources.'
random_paper: 35
score:
  band: thin
  composite: 39.9
  delta: 0.0
  facets:
    commercial_clarity: 21.1
    contract_quality: 49.7
    developer_ergonomics: 63.0
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 39.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/dott/refs/heads/main/screenshots/dott-2026-07-25T212315.png
security:
- kind: authentication
  name: Dott Authentication
  slug: dott-authentication
  summary_line: none/apiKey · 2 schemes
- kind: domain-security
  name: Dott Domain Security
  slug: dott-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: dott
tags:
- Company
- Transportation
- Micromobility
- Mobility
- E-Scooter
- E-Bike
- GBFS
- Shared Mobility
- Smart City
- Sustainability
website: https://ridedott.com
---

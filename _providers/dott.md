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
    agent_skills: derived
    agentic_access: false
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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.8
  scored_at: '2026-09-01'
api_count: 1
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
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Dott GBFS Discovery API
  slug: open-dott-discovery-api
- collection_type: open
  name: Dott GBFS Discovery Stations API
  slug: open-dott-stations-api
- collection_type: open
  name: Dott GBFS Discovery System API
  slug: open-dott-system-api
- collection_type: open
  name: Dott GBFS Discovery Vehicles API
  slug: open-dott-vehicles-api
- collection_type: open
  name: Dott GBFS Discovery Zones API
  slug: open-dott-zones-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/dott-capability-edges.yml
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
  url: openapi/_original/dott-gbfs-openapi.yml
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
  name: Dott MCP Server
  slug: dott-mcp-server
modified: '2026-07-18'
name: Dott
nav: Providers
network: true
overview: 'Dott publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Discovery API, Stations API, System API, and 2 more. Tagged areas include Company, Transportation, Micromobility, Mobility, and E-Scooter.


  Dott''s developer surface includes documentation, API reference, getting-started guide, engineering blog, code examples, authentication, and 17 more developer resources.'
random_paper: 2
score:
  band: developing
  composite: 43.4
  coverage:
    artifact_dirs: 18
    catalog_gap: 63.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.1
    commercial_clarity: 57.1
    contract_governance: 18.2
    contract_quality: 49.8
    developer_ergonomics: 47.0
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 43.4
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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

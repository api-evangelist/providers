---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
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
    error_semantics: derived
    event_surface_described: false
    idempotency: na
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: documented
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://gbfs.api.ridedott.com/public/v2
  baseurl_source: declared
  description: Auto-discovery of available feeds and cities
  name: Dott Discovery API
  slug: dott-discovery-api
- baseURL: https://gbfs.api.ridedott.com/public/v2
  baseurl_source: declared
  description: Docked station information and status (where applicable)
  name: Dott Stations API
  slug: dott-stations-api
- baseURL: https://gbfs.api.ridedott.com/public/v2
  baseurl_source: declared
  description: System-level metadata and pricing
  name: Dott System API
  slug: dott-system-api
- baseURL: https://gbfs.api.ridedott.com/public/v2
  baseurl_source: declared
  description: Free-floating vehicle status and types
  name: Dott Vehicles API
  slug: dott-vehicles-api
- baseURL: https://gbfs.api.ridedott.com/public/v2
  baseurl_source: declared
  description: Geofencing / operating zones
  name: Dott Zones API
  slug: dott-zones-api
- description: Partner-facing data API from Dott (formerly TIER), providing vehicle and availability data (GBFS-style) to authorized partners. Access requires a per-partner API Key issued through Dott's registration
  name: Dott Partner API
  slug: dott-partner-api
artifact_total: 21
collections:
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
  href: https://artifacts.apis.io/dott/capabilities/dott-capability-edges.yml
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
  href: https://artifacts.apis.io/dott/openapi/_original/dott-gbfs-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/dott-gbfs-openapi.yml
- group: other
  href: https://artifacts.apis.io/dott/overlays/dott-gbfs-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/dott-gbfs-overlay.yaml
- group: build
  href: https://artifacts.apis.io/dott/examples/dott-system_information-espoo.json
  title: ''
  type: Examples
  url: examples/dott-system_information-espoo.json
- group: auth
  href: https://artifacts.apis.io/dott/authentication/dott-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dott-authentication.yml
- group: design
  href: https://artifacts.apis.io/dott/conventions/dott-conventions.yml
  title: ''
  type: Conventions
  url: conventions/dott-conventions.yml
- group: design
  href: https://artifacts.apis.io/dott/errors/dott-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dott-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dott/data-model/dott-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dott-data-model.yml
- group: design
  href: https://artifacts.apis.io/dott/conformance/dott-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dott-conformance.yml
- group: design
  href: https://artifacts.apis.io/dott/lifecycle/dott-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/dott-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/dott/mcp/dott-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/dott-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dott/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/dott/llms/dott-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dott-llms.txt
- group: auth
  href: https://artifacts.apis.io/dott/security/dott-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dott-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://ridedott.com/feed
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
modified: '2026-07-18'
name: Dott
nav: Providers
network: true
overview: 'Dott publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Discovery API, Stations API, System API, and 3 more. Tagged areas include Company, Transportation, Micromobility, Mobility, and E-Scooter.


  The Dott catalog on APIs.io includes 1 Spectral governance ruleset.


  Dott''s developer surface includes documentation, API reference, getting-started guide, engineering blog, code examples, authentication, and 18 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: Dott API Rules
  rule_count: 46
  severity_counts:
    error: 44
    hint: 0
    info: 1
    warn: 1
  slug: dott-rules
score:
  band: developing
  composite: 45.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 41.5
    catalog_earned_first_party: 0.0
    catalog_gap: 58.5
    catalog_max: 100.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 57.1
    contract_governance: 31.8
    contract_quality: 45.1
    developer_ergonomics: 47.0
    discoverability: 73.2
    operational_transparency: 2.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - netherlands
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - benelux
    - europe
  previous_composite: 45.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://apis.io/screenshots/dott/dott-2026-07-25T212315.png
security:
- kind: authentication
  name: Dott Authentication
  slug: dott-authentication
  summary_line: none/apiKey · 2 schemes
- kind: authentication
  name: Tier Mobility Authentication
  slug: tier-mobility-authentication
  summary_line: none/http · 2 schemes
- kind: domain-security
  name: Dott Domain Security
  slug: dott-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: Find available Dott vehicles in a city
  slug: dott-find-available-vehicles
slug: dott
tags:
- Company
- Transportation
- Micromobility
- Mobility
- E-Scooter
- E-Bikes
- GBFS
- Shared Mobility
- Smart City
- Sustainability
website: https://ridedott.com
---

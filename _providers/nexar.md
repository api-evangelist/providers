---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 44.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Nexar Agentic Access
  operation_count: 8
  slug: nexar-agentic-access
  summary_line: 8 operations · 8 acting
api_count: 4
apis:
- description: The CityStream™ Live Feed API V4 API from Nexar — 1 operation(s) for citystream™ live feed api v4.
  name: Nexar CityStream™ Live Feed API V4 API
  slug: nexar-citystream-live-feed-api-v4-api
- description: The Get a collection of road signs API from Nexar — 1 operation(s) for get a collection of road signs.
  name: Nexar Get a collection of road signs API
  slug: nexar-get-a-collection-of-road-signs-api
- description: The Get a collection of work zones API from Nexar — 1 operation(s) for get a collection of work zones.
  name: Nexar Get a collection of work zones API
  slug: nexar-get-a-collection-of-work-zones-api
- description: The Get a specific work zone API from Nexar — 1 operation(s) for get a specific work zone.
  name: Nexar Get a specific work zone API
  slug: nexar-get-a-specific-work-zone-api
- description: The Get the details of a specific road sign API from Nexar — 1 operation(s) for get the details of a specific road sign.
  name: Nexar Get the details of a specific road sign API
  slug: nexar-get-the-details-of-a-specific-road-sign-api
- description: The VirtualCam API API from Nexar — 3 operation(s) for virtualcam api.
  name: Nexar VirtualCam API
  slug: nexar-virtualcam-api-api
artifact_total: 14
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/nexar-virtualcam-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nexar-livefeed-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nexar-workzones-overlay.yaml
- group: other
  title: ''
  type: Overlay
  url: overlays/nexar-roadinventory-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/nexar-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/nexar-vulnerability-disclosure.yml
- group: company
  title: ''
  type: Website
  url: https://www.nexar-ai.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.getnexar.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.getnexar.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://developer.getnexar.com/documentation
- group: start
  title: ''
  type: SignUp
  url: https://developer.getnexar.com/signup
- group: start
  title: ''
  type: Login
  url: https://developer.getnexar.com/login
- group: operate
  title: ''
  type: Support
  url: https://help.getnexar.com/
- group: company
  title: ''
  type: Blog
  url: https://www.nexar-ai.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/getnexar
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nexar-ai.com/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nexar-ai.com/legal/privacy-policy
- group: auth
  title: ''
  type: Security
  url: https://www.getnexar.com/.well-known/security.txt
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/nexar-security.txt
- group: agent
  title: ''
  type: WellKnown
  url: well-known/nexar-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/nexar-llms.txt
- group: agent
  title: ''
  type: MCPServer
  url: mcp/nexar-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/nexar-tool-crosswalk.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/nexar-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/nexar-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/nexar-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/nexar-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/nexar-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: lifecycle/nexar-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/nexar-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/nexar-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/nexar-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/nexar-cli.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/nexar-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/nexar-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/nexar-domain-security.yml
created: '2026-08-26'
description: 'Nexar is a physical-AI infrastructure company that operates one of the largest real-world video driving datasets — over 1.2 billion miles of driving captured each year by more than 350,000 connected dashcams — and turns it into training data, collision-prediction models and real-time road intelligence for autonomous-vehicle, ADAS, mapping and smart-city programs. Its developer-facing surface is the CityStream™ family of REST APIs, published as four OpenAPI 3.0.1 contracts on the Nexar Developers Portal: VirtualCam (anonymized road frames), Live Feed (real-time detections), Work Zones (curated construction-zone detections, served as WZDx and GeoJSON) and Road Inventory (curated traffic-sign and road-asset detections). All four run on a single gRPC-gateway backed host and are authorized with a bearer access token minted through Nexar''s Okta authorization server. Nexar also publishes the open-source BADAS collision-prediction model on PyPI and the `nap` platform CLI through its
  own Homebrew tap.'
image: https://cdn.prod.website-files.com/6714bce7188a12cb895149f5/68f0ac403e8da1fec926cec2_social%20sharing.png
layout: provider
mcp_servers:
- description: ''
  name: Nexar MCP Server
  slug: nexar-mcp-server
modified: '2026-08-26'
name: Nexar
nav: Providers
network: true
overview: 'Nexar publishes 6 APIs on the [APIs.io](https://apis.io/) network, including CityStream™ Live Feed API V4 API, Get a collection of road signs API, Get a collection of work zones API, and 3 more. Tagged areas include Company, Mapping, Geospatial, Transportation, and Computer-Vision.


  Nexar''s developer surface includes documentation, API reference, signup flow, support, engineering blog, authentication, CLI, and 30 more developer resources.'
plans:
- name: Nexar Plans Pricing
  plan_count: 0
  slug: nexar-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 0
  name: Nexar Rate Limits
  slug: nexar-rate-limits
scopes:
- name: Nexar Scopes
  scope_count: 4
  slug: nexar-scopes
  summary_line: 4 scopes · authorizationCode
score:
  band: thin
  composite: 36.2
  coverage:
    artifact_dirs: 21
    catalog_gap: 75.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 4.5
    contract_quality: 57.4
    developer_ergonomics: 28.0
    discoverability: 81.5
    governance: 4.5
    operational_transparency: 15.8
  previous_composite: 36.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: authentication
  name: Nexar Authentication
  slug: nexar-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Nexar Domain Security
  slug: nexar-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Nexar Vulnerability Disclosure
  slug: nexar-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: nexar
tags:
- Company
- Mapping
- Geospatial
- Transportation
- Computer-Vision
- Autonomous Vehicles
- Smart Cities
- Imagery
- Road Data
- Machine-Learning
website: https://www.nexar-ai.com/
---

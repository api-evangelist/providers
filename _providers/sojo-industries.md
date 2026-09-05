---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.2
  scored_at: '2026-09-04'
api_count: 2
apis:
- baseURL: https://victoria-agent.sojoshield.com
  baseurl_source: declared
  description: The HTTP surface for Victoria, the SOJO Planning Assistant — a LangGraph-backed agent over Sojo's production and machine-telemetry data. Publishes a public OpenAPI 3.0.3 describing non-streaming orche
  name: SOJO Planning Assistant (Victoria) API
  slug: sojo-planning-assistant-victoria-api
- description: The Sojo Shield track-and-trace platform API, versioned in-path at /api/v3/ and consumed by the Sojo Shield web application at sojoshield.com. Sojo publishes a Swagger UI for it at api.sojoshield.com/
  name: Sojo Shield Platform API
  slug: sojo-shield-platform-api
artifact_total: 7
common:
- group: company
  title: ''
  type: Website
  url: https://www.sojoindustries.com/
- group: other
  title: ''
  type: Application
  url: https://sojoshield.com/
- group: docs
  title: ''
  type: APIReference
  url: https://api.sojoshield.com/docs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sojoindustries/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@SojoFlight
- group: other
  title: ''
  type: Media
  url: https://www.sojoindustries.com/media
- group: agent
  title: ''
  type: MCPServer
  url: mcp/sojo-industries-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/sojo-industries-tool-crosswalk.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/sojo-industries-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/sojo-industries-victoria-agent-overlay.yaml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sojo-industries-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/sojo-industries-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/sojo-industries-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/sojo-industries-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/sojo-industries-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/sojo-industries-data-model.yml
- group: build
  title: ''
  type: Packages
  url: packages/sojo-industries-packages.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/sojo-industries-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/sojo-industries-rate-limits.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sojo-industries-domain-security.yml
created: '2026-08-28'
description: Sojo Industries is a national industrial-automation and supply-chain technology company founded in 2021 and headquartered in Bristol, Pennsylvania, serving the food and beverage industry with robotics-driven variety packing, multi-packing and assembly. It operates fixed Sojo Hubs across Pennsylvania, New Jersey, California and Texas plus Sojo Flight mobile manufacturing lines that are trucked to a customer's own plant to eliminate freight, labour and packaging cost. Its software arm is Sojo Shield, a blockchain-backed track-and-trace platform — a Built for NetSuite SuiteApp — that captures geolocated critical tracking events from the factory floor through to the retailer so brands can meet the FDA FSMA Rule 204 Food Traceability requirements, and Sojo Seal, GPS-enabled tamper-evident seals. Its API surface is the Sojo Shield platform API at api.sojoshield.com and a production Model Context Protocol server for "Victoria", the SOJO Planning Assistant, which exposes production,
  machine-telemetry, dieline and pallet-pattern planning tools to MCP clients.
image: https://cdn.prod.website-files.com/693c57b3032e47cda78c8224/6980f69ec74fbeaa81cf114e_Website%20Logo.png
layout: provider
mcp_servers:
- description: Sojo Industries operates a production Model Context Protocol server for "Victoria", the SOJO Planning Assistant. It is a remote streamable-HTTP MCP endpoint fronting the Sojo Shield production/plannin
  name: SOJO Planning Assistant MCP Server
  slug: sojo-planning-assistant-mcp-server
modified: '2026-08-28'
name: Sojo Industries
nav: Providers
network: true
overview: 'Sojo Industries publishes 1 API on the [APIs.io](https://apis.io/) network: SOJO Planning Assistant (Victoria) API. Tagged areas include Company, Supply Chain, Traceability, Food and Beverage, and Manufacturing.


  Sojo Industries'' developer surface includes API reference, YouTube channel, authentication, and 18 more developer resources.'
plans:
- name: Sojo Industries Plans Pricing
  plan_count: 0
  slug: sojo-industries-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Sojo Industries Rate Limits
  slug: sojo-industries-rate-limits
score:
  band: emerging
  composite: 24.9
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 46.9
    developer_ergonomics: 20.8
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 0.0
  previous_composite: 24.9
  provenance:
    conformance: first-party
    mcp: first-party
    skills: derived
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/screenshots/sojo-industries-2026-09-02T160103.png
security:
- kind: authentication
  name: Sojo Industries Authentication
  slug: sojo-industries-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sojo Industries Domain Security
  slug: sojo-industries-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sojo-industries
tags:
- Company
- Supply Chain
- Traceability
- Food and Beverage
- Manufacturing
- Logistics
- Packaging
- Industrial Automation
- Blockchain
- Artificial Intelligence
- MCP
website: https://www.sojoindustries.com/
---

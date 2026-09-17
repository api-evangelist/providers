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
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-16'
api_count: 1
apis:
- description: The Sojo Shield track-and-trace platform API, versioned in-path at /api/v3/ and consumed by the Sojo Shield web application at sojoshield.com. Sojo publishes a Swagger UI for it at api.sojoshield.com/
  name: Sojo Shield Platform API
  slug: sojo-shield-platform-api
- baseURL: https://victoria-agent.sojoshield.com
  baseurl_source: declared
  description: Orchestration / streaming chat
  name: Sojo Industries Chat API
  slug: sojo-industries-chat-api
- baseURL: https://victoria-agent.sojoshield.com
  baseurl_source: declared
  description: Chat-history list/read/rename/delete (requires AGENT_PERSISTENCE_ENABLED; 404 when the feature is off)
  name: Sojo Industries Conversations API
  slug: sojo-industries-conversations-api
- baseURL: https://victoria-agent.sojoshield.com
  baseurl_source: declared
  description: Image upload (files are uploaded via Shield, then referenced by S3 key)
  name: Sojo Industries Files API
  slug: sojo-industries-files-api
- baseURL: https://victoria-agent.sojoshield.com
  baseurl_source: declared
  description: Health probe
  name: Sojo Industries Health API
  slug: sojo-industries-health-api
artifact_total: 10
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
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/mcp/sojo-industries-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/sojo-industries-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/mcp/sojo-industries-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/sojo-industries-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/llms/sojo-industries-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/sojo-industries-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/overlays/sojo-industries-victoria-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/sojo-industries-victoria-agent-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/authentication/sojo-industries-authentication.yml
  title: ''
  type: Authentication
  url: authentication/sojo-industries-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/conventions/sojo-industries-conventions.yml
  title: ''
  type: Conventions
  url: conventions/sojo-industries-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/errors/sojo-industries-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/sojo-industries-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/lifecycle/sojo-industries-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/sojo-industries-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/conformance/sojo-industries-conformance.yml
  title: ''
  type: Conformance
  url: conformance/sojo-industries-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/data-model/sojo-industries-data-model.yml
  title: ''
  type: DataModel
  url: data-model/sojo-industries-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/packages/sojo-industries-packages.yml
  title: ''
  type: Packages
  url: packages/sojo-industries-packages.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/plans/sojo-industries-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/sojo-industries-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/rate-limits/sojo-industries-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/sojo-industries-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/sojo-industries/refs/heads/main/security/sojo-industries-domain-security.yml
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
overview: 'Sojo Industries publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Chat API, Conversations API, Files API, and 1 more. Tagged areas include Company, Supply Chain, Traceability, Food and Beverage, and Manufacturing.


  Sojo Industries'' developer surface includes API reference, YouTube channel, authentication, and 18 more developer resources.'
plans:
- name: Sojo Industries Plans Pricing
  plan_count: 0
  slug: sojo-industries-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 0
  name: Sojo Industries Rate Limits
  slug: sojo-industries-rate-limits
score:
  band: emerging
  composite: 25.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.9
  facets:
    access_clarity: 0.0
    contract_governance: 18.2
    contract_quality: 50.3
    developer_ergonomics: 20.8
    discoverability: 68.5
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - north-america
  previous_composite: 24.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 0.0
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

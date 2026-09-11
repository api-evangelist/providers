---
access_model:
  confidence: high
  label: Contract-only · Sales-gated onboarding
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  - docs
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
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
    well_known_catalog: true
  schema_version: 0.2
  score: 29.9
  scored_at: '2026-09-10'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: First Street Agentic Access
  operation_count: 3
  slug: first-street-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: The Climate Risk API provides physical climate risk data globally, delivering property-level insights into hazards including flood, wildfire, heat, wind, and air quality.
  name: First Street Climate Risk API
  slug: climate-risk
- description: The Enterprise API offers aggregated climate risk views for portfolios, enabling enterprise users to assess risk across multiple properties and geographic regions.
  name: First Street Enterprise API
  slug: enterprise
- description: The Raster Map API delivers visual raster layers of climate perils for mapping and visualization use cases.
  name: First Street Raster Map API
  slug: raster-map
- baseURL: https://api.firststreet.org
  baseurl_source: declared
  description: The Enterprise API from First Street — 1 operation(s) for enterprise.
  name: First Street Enterprise API
  slug: first-street-enterprise-api
- baseURL: https://api.firststreet.org
  baseurl_source: declared
  description: The Graphql API from First Street — 1 operation(s) for graphql.
  name: First Street Graphql API
  slug: first-street-graphql-api
- baseURL: https://api.firststreet.org
  baseurl_source: declared
  description: The Maps API from First Street — 1 operation(s) for maps.
  name: First Street Maps API
  slug: first-street-maps-api
- description: 'Hosted, remote Model Context Protocol server exposing the Climate Risk API to agents over Streamable HTTP. Ten tools with real JSON Schema inputs — property lookup by address, coordinate or Place ID, '
  name: First Street MCP Server
  slug: mcp
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: First Street Enterprise API
  slug: open-first-street-enterprise-api
- collection_type: open
  name: First Street Enterprise Graphql API
  slug: open-first-street-graphql-api
- collection_type: open
  name: First Street Enterprise Maps API
  slug: open-first-street-maps-api
- collection_type: open
  name: First Street API
  slug: open-first-street
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/first-street-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/first-street-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/first-street-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/first-street-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/first-street-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FirstStreet
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/first-street
- group: company
  title: ''
  type: Website
  url: https://firststreet.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.firststreet.org/api
- group: agent
  title: ''
  type: MCPServer
  url: mcp/first-street-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/first-street-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/first-street-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/first-street-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/first-street-packages.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/first-street-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/first-street-error-codes.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/first-street-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/first-street-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.firststreet.org/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/first-street-changelog.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/first-street-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.firststreet.org/
- group: auth
  title: ''
  type: Security
  url: https://docs.firststreet.org/api/security
- group: start
  title: ''
  type: Sandbox
  url: sandbox/first-street-sandbox.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/first-street-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/first-street-plans-pricing.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/first-street-finops.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.firststreet.org/api
- group: docs
  title: ''
  type: APIReference
  url: https://docs.firststreet.org/api/available-api/graphql-apis
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.firststreet.org/api/climate-risk-api/getting-started
- group: operate
  title: ''
  type: Support
  url: mailto:api@firststreet.org
- group: company
  title: ''
  type: Blog
  url: https://firststreet.org/insights
- group: commercial
  title: ''
  type: Pricing
  url: https://firststreet.org/pricing
- group: start
  title: ''
  type: Login
  url: https://firststreet.org/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.msci.com/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://firststreet.org/privacy-policy
created: '2025-03-01'
description: 'First Street is the physical climate risk data and analytics company behind the Risk Factor property reports, acquired by MSCI on 2026-08-03. It models flood, wildfire, wind, heat, cold, drought and air quality at property level anywhere on Earth using peer-reviewed, physics-based methods rather than historical claims data, and exposes that model through three APIs: a global Climate Risk GraphQL API, an Enterprise GraphQL API for portfolio-level exposure, scenario analysis and adaptation cost-benefit, and a Raster Map tile API for visualising perils on a map. It also runs a hosted MCP server so agents can query property climate risk directly. Access to every surface, and to individual fields within the GraphQL schemas, is granted by contract.'
finops:
- name: First Street Finops
  service_category: API
  slug: first-street-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/first-street.png
layout: provider
mcp_servers:
- description: 'First Street publishes a hosted, remote MCP server that exposes the Climate Risk API (property-level physical climate risk: flood, wildfire, wind, heat, cold, drought) to agents over Streamable HTTP. '
  name: First Street MCP Server
  slug: first-street-mcp-server
modified: '2026-09-10'
name: First Street
nav: Providers
network: true
overview: 'First Street publishes 3 APIs on the [APIs.io](https://apis.io/) network: Enterprise API, Graphql API, and Maps API. Tagged areas include Climate, Risk, Environment, Modeling, and Geospatial.


  First Street''s developer surface includes authentication, documentation, changelog, sandbox, API reference, getting-started guide, support, and 30 more developer resources.'
plans:
- name: First Street Plans Pricing
  plan_count: 0
  slug: first-street-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 2
  name: First Street Rate Limits
  slug: first-street-rate-limits
score:
  band: strong
  composite: 64.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 36.0
  facets:
    access_clarity: 68.4
    commercial_clarity: 68.4
    contract_governance: 18.2
    contract_quality: 56.6
    developer_ergonomics: 73.2
    discoverability: 75.9
    governance: 18.2
    operational_transparency: 65.8
  previous_composite: 28.2
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 54.5
  schema_version: 0.20.0
  scored_at: '2026-09-10'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/first-street/refs/heads/main/screenshots/first-street-2026-06-20T181242.png
security:
- kind: authentication
  name: First Street Authentication
  slug: first-street-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: First Street Domain Security
  slug: first-street-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: First Street Vulnerability Disclosure
  slug: first-street-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: First Street Trust Center
  slug: first-street-trust-center
  summary_line: SOC 2 Type II
slug: first-street
tags:
- Climate
- Risk
- Environment
- Modeling
- Geospatial
- Insurance
- Real Estate
- Data
- GraphQL
- Mapping
website: https://firststreet.org/
---

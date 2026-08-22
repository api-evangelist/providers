---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: na
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: verified
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 55.9
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Atmospore Pollen Forecasts Agentic Access
  operation_count: 4
  slug: atmospore-pollen-forecasts-agentic-access
  summary_line: 4 operations
api_count: 5
apis:
- description: Hosted Model Context Protocol server exposing the Atmospore pollen forecast capability as four agent tools (get_pollen, get_top_species, get_area_average, list_supported_species) plus an atmospore://h
  name: Atmospore MCP Server
  slug: atmospore-mcp-server
- description: The Pollen API from Atmospore Pollen Forecasts — 1 operation(s) for pollen.
  name: Atmospore Pollen Forecasts Pollen API
  slug: atmospore-pollen-forecasts-pollen-api
- description: The Pollen Area API from Atmospore Pollen Forecasts — 1 operation(s) for pollen area.
  name: Atmospore Pollen Forecasts Pollen Area API
  slug: atmospore-pollen-forecasts-pollen-area-api
- description: The Pollen Top API from Atmospore Pollen Forecasts — 1 operation(s) for pollen top.
  name: Atmospore Pollen Forecasts Pollen Top API
  slug: atmospore-pollen-forecasts-pollen-top-api
- description: The Species API from Atmospore Pollen Forecasts — 1 operation(s) for species.
  name: Atmospore Pollen Forecasts Species API
  slug: atmospore-pollen-forecasts-species-api
arazzos:
- description: 'Resolve the Atmospore species catalogue, rank the worst allergens for the coming week at a coordinate, then pull the day-by-day forecast for the species the user actually reacts to. Every operationId '
  name: Plan an allergy week for a location
  slug: atmospore-pollen-forecasts-allergy-week-plan
- description: Resolve the species catalogue, then read tree/grass/weed aggregates across a radius for a regional dashboard or a smart-home ventilation rule. Every operationId exists verbatim in the referenced OpenA
  name: Build a regional pollen risk board
  slug: atmospore-pollen-forecasts-regional-risk-board
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Atmospore Forecast Pollen API
  slug: open-atmospore-pollen-forecasts-pollen-api
- collection_type: open
  name: Atmospore Pollen Forecast Pollen Area API
  slug: open-atmospore-pollen-forecasts-pollen-area-api
- collection_type: open
  name: Atmospore Pollen Forecast Pollen Top API
  slug: open-atmospore-pollen-forecasts-pollen-top-api
- collection_type: open
  name: Atmospore Pollen Forecast Species API
  slug: open-atmospore-pollen-forecasts-species-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/atmospore/atmospore-mcp/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/atmospore/atmospore-mcp/blob/main/LICENSE
- group: company
  title: ''
  type: Website
  url: https://atmospore.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://atmospore.com/api-docs
- group: docs
  title: ''
  type: Documentation
  url: https://atmospore.com/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://atmospore.com/api-docs
- group: operate
  title: ''
  type: Support
  url: https://atmospore.com/contact
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/atmospore
- group: commercial
  title: ''
  type: Pricing
  url: https://atmospore.com/plans
- group: start
  title: ''
  type: Signup
  url: https://atmospore.com/register
- group: start
  title: ''
  type: Login
  url: https://atmospore.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://atmospore.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://atmospore.com/privacy-policy
- group: auth
  title: ''
  type: Authentication
  url: authentication/atmospore-pollen-forecasts-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/atmospore-pollen-forecasts-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/atmospore-pollen-forecasts-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/atmospore-pollen-forecasts-lifecycle.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/atmospore-pollen-forecasts-rate-limits.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/atmospore-pollen-forecasts-plans.yml
- group: build
  title: ''
  type: Packages
  url: packages/atmospore-pollen-forecasts-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/atmospore-pollen-forecasts-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/atmospore-pollen-forecasts-sandbox.yml
- group: design
  title: ''
  type: Components
  url: components/atmospore-pollen-forecasts-components.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/atmospore-pollen-forecasts-conformance.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/atmospore-pollen-forecasts-domain-security.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/atmospore-pollen-forecasts-mcp.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/atmospore-pollen-forecasts-openapi-overlay.yaml
- group: build
  title: ''
  type: Examples
  url: examples/_index.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/atmospore-pollen-forecasts-data-model.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/atmospore-pollen-forecasts-agentic-access.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/atmospore-pollen-forecasts-llms.txt
- group: design
  title: ''
  type: Arazzo
  url: arazzo/atmospore-pollen-forecasts-allergy-week-plan.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/atmospore-pollen-forecasts-regional-risk-board.yml
created: '2026-08-03'
description: 'Atmospore is an Oslo-based provider of AI-driven global pollen and allergy forecasting. Its model combines GFS weather data with ground-truth observations from professional aerobiology networks to produce species-level forecasts on a ~28 km global grid, covering 25 individual tree, grass and weed species with multilingual metadata (English, Norwegian, Swedish) and published concentration thresholds for low/moderate/high/very-high risk. The surface is delivered three ways: a four-operation REST API at pollenapi.com with a live OpenAPI 3.0.3 contract, a hosted Model Context Protocol server at mcp.atmospore.com exposing the same capability as four agent tools, and a keyless embeddable iframe widget that consumes no API quota. Point forecasts, area averages with min/max across a radius, and severity-ranked top species are all available up to 14 days ahead; species metadata is served unauthenticated.'
examples:
- key_count: 1
  name: Atmospore Pollen Forecasts Pollen 401
  slug: atmospore-pollen-forecasts-pollen-401
- key_count: 1
  name: Atmospore Pollen Forecasts Pollen 403
  slug: atmospore-pollen-forecasts-pollen-403
- key_count: 2
  name: Atmospore Pollen Forecasts Species 200
  slug: atmospore-pollen-forecasts-species-200
image: https://atmospore.com/images/logo-bg.png
layout: provider
mcp_servers:
- description: ''
  name: atmospore-pollen-forecasts-mcp.yml
  slug: atmospore-pollen-forecasts-mcpyml
modified: '2026-08-09'
name: Atmospore Pollen Forecasts
nav: Providers
network: true
overview: 'Atmospore Pollen Forecasts publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Pollen API, Pollen Area API, Pollen Top API, and 1 more. Tagged areas include weather, pollen, allergy, environmental-data, and health.


  Atmospore Pollen Forecasts'' developer surface includes documentation, API reference, support, pricing, signup flow, authentication, sandbox, and 27 more developer resources.'
plans:
- name: Atmospore Pollen Forecasts Plans
  plan_count: 5
  slug: atmospore-pollen-forecasts-plans
random_paper: 8
rate_limits:
- limit_count: 4
  name: Atmospore Pollen Forecasts Rate Limits
  slug: atmospore-pollen-forecasts-rate-limits
score:
  band: strong
  composite: 59.3
  delta: 5.8
  facets:
    access_clarity: 69.7
    commercial_clarity: 69.7
    contract_governance: 16.7
    contract_quality: 57.3
    developer_ergonomics: 58.9
    discoverability: 81.5
    governance: 16.7
    operational_transparency: 34.2
  previous_composite: 53.5
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
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 50.0
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/atmospore-pollen-forecasts/refs/heads/main/screenshots/atmospore-pollen-forecasts-2026-08-17T080606.png
security:
- kind: authentication
  name: Atmospore Pollen Forecasts Authentication
  slug: atmospore-pollen-forecasts-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Atmospore Pollen Forecasts Domain Security
  slug: atmospore-pollen-forecasts-domain-security
  summary_line: TLSv1.3 · DMARC
slug: atmospore-pollen-forecasts
tags:
- weather
- pollen
- allergy
- environmental-data
- health
- geospatial
- forecasting
- smart-home
- mcp
- openapi
- norway
- climate
website: https://atmospore.com/
---

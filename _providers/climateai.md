---
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 23.6
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 49
  human_in_the_loop: 4
  name: Climateai Agentic Access
  operation_count: 89
  slug: climateai-agentic-access
  summary_line: 89 operations · 49 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: ClimateAI authentication and routing gateway for platform services. Covers accounts, account configuration, users, roles, permissions, device API keys, products, platform labels, reports, transactiona
  name: ClimateAI Platform API
  slug: platform
- description: account related operations
  name: ClimateAI Account API
  slug: climateai-account-api
- description: account config related operations
  name: ClimateAI Account Config API
  slug: climateai-account-config-api
- description: authentication related operations
  name: ClimateAI Auth API
  slug: climateai-auth-api
- description: Modern endpoints (recommended). Faster grid-index lookups, blended multi-model forecasts, explicit downscaling control, and a compact, date-keyed response shape. All paths start with `/v2/`.
  name: ClimateAI Current (v2) API
  slug: climateai-current-v2-api
- description: device api key related operations
  name: ClimateAI Device API
  slug: climateai-device-api
- description: email sending operations
  name: ClimateAI Email API
  slug: climateai-email-api
- description: Original endpoints. Stable and supported, but superseded by the Current (v2) endpoints where noted. Default response shape is the `{ meta, data }` envelope, where each `data` entry nests its per-varia
  name: ClimateAI Legacy (v1) API
  slug: climateai-legacy-v1-api
- description: permission related operations
  name: ClimateAI Permission API
  slug: climateai-permission-api
- description: platform label related operations
  name: ClimateAI Platform API
  slug: climateai-platform-api
- description: product listing
  name: ClimateAI Product API
  slug: climateai-product-api
- description: report related operations
  name: ClimateAI Report API
  slug: climateai-report-api
- description: user role related operations
  name: ClimateAI Role API
  slug: climateai-role-api
- description: routing and proxy operations
  name: ClimateAI Routing API
  slug: climateai-routing-api
- description: user related operations
  name: ClimateAI User API
  slug: climateai-user-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: ClimateAI Platform Account API
  slug: open-climateai-account-api
- collection_type: open
  name: ClimateAI Platform Account Config API
  slug: open-climateai-account-config-api
- collection_type: open
  name: ClimateAI Platform Auth API
  slug: open-climateai-auth-api
- collection_type: open
  name: ClimateAI Weather Current (v2) Current (v2) API
  slug: open-climateai-current-v2-api
- collection_type: open
  name: ClimateAI Platform Device API
  slug: open-climateai-device-api
- collection_type: open
  name: ClimateAI Platform Email API
  slug: open-climateai-email-api
- collection_type: open
  name: ClimateAI Weather Legacy (v1) Legacy (v1) API
  slug: open-climateai-legacy-v1-api
- collection_type: open
  name: ClimateAI Platform Permission API
  slug: open-climateai-permission-api
- collection_type: open
  name: ClimateAI Platform API
  slug: open-climateai-platform-api
- collection_type: open
  name: ClimateAI Platform Product API
  slug: open-climateai-product-api
- collection_type: open
  name: ClimateAI Platform Report API
  slug: open-climateai-report-api
- collection_type: open
  name: ClimateAI Platform Role API
  slug: open-climateai-role-api
- collection_type: open
  name: ClimateAI Platform Routing API
  slug: open-climateai-routing-api
- collection_type: open
  name: ClimateAI Platform User API
  slug: open-climateai-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/climateai-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://climate.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.climate.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.climate.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.climate.ai/climateai-weather-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.climate.ai/guide/getting-started
- group: company
  title: ''
  type: Blog
  url: https://climate.ai/blog/
- group: company
  title: ''
  type: BlogRSS
  url: https://climate.ai/feed/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ClimateAI
- group: operate
  title: ''
  type: Support
  url: mailto:customersuccess@climate.ai
- group: start
  title: ''
  type: SignUp
  url: https://climate.ai/get-started/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://climate.ai/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://climate.ai/privacy-policy/
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.climate.ai/guide/migration
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/climateai-llms.txt
- group: auth
  title: ''
  type: Authentication
  url: authentication/climateai-authentication.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/climateai-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/climateai-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/climateai-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/climateai-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/climateai-data-model.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/climateai-weather-variables.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/climateai-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/climateai-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/climateai-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/climateai-domain-security.yml
created: '2026-08-02'
description: ClimateAi (climate.ai) is a climate-intelligence company that turns global weather, climate and extreme-event modeling into decision-grade forecasts for agriculture, food and beverage, manufacturing, energy, finance, retail and federal/defense customers. Its ClimateLens products cover risk screening, monitoring and adaptation, and its developer surface is the LensConnect API — a REST weather and climate data API addressed by latitude and longitude that returns 30+ years of history (1995-present, ERA5-backed), a fixed 30-year climatology baseline, and AI-stitched probabilistic forecasts running from short-term through seasonal (~6 months) in a single continuous timeline, at ~25 km resolution with optional 1 km downscaling for select variables. A separate ClimateAI Platform gateway handles accounts, users, roles, permissions, device API keys and product routing.
image: https://climate.ai/wp-content/uploads/2022/09/Logo_orange_dark.png
layout: provider
mcp_servers:
- description: ''
  name: ClimateAI MCP Server
  slug: climateai-mcp-server
modified: '2026-08-04'
name: ClimateAI
nav: Providers
network: true
overview: 'ClimateAI publishes 15 APIs on the [APIs.io](https://apis.io/) network, including Platform API, Account API, Account Config API, and 12 more. Tagged areas include Company, Weather, Climate, Climate Intelligence, and Forecasting.


  ClimateAI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 20 more developer resources.'
random_paper: 13
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 20
    catalog_gap: 73.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 19.7
    contract_quality: 52.2
    developer_ergonomics: 58.9
    discoverability: 75.9
    governance: 19.7
    operational_transparency: 10.5
  previous_composite: 43.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 14.3
      derived: 0
      marker_coverage: 0.0
      total: 14
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/climateai/refs/heads/main/screenshots/climateai-2026-08-07T163452.png
security:
- kind: authentication
  name: Climateai Authentication
  slug: climateai-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Climateai Domain Security
  slug: climateai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: climateai
tags:
- Company
- Weather
- Climate
- Climate Intelligence
- Forecasting
- Agriculture
- Data
- Supply Chain
- Risk
- Sustainability
website: https://climate.ai/
---

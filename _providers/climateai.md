---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: partial
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 38.1
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 49
  human_in_the_loop: 4
  name: Climateai Agentic Access
  operation_count: 89
  slug: climateai-agentic-access
  summary_line: 89 operations · 49 acting · 4 human-in-the-loop
api_count: 2
apis:
- description: 'The LensConnect weather and climate data API. Forecasts, historical observations and climatology for any point on Earth, addressed by latitude and longitude. Current (v2) endpoints return AI-stitched '
  name: ClimateAi Weather API (LensConnect)
  slug: weather
- description: ClimateAI authentication and routing gateway for platform services. Covers accounts, account configuration, users, roles, permissions, device API keys, products, platform labels, reports, transactiona
  name: ClimateAI Platform API
  slug: platform
artifact_total: 6
common:
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
  name: climateai-mcp.yml
  slug: climateai-mcpyml
modified: '2026-08-04'
name: ClimateAI
nav: Providers
network: true
overview: 'ClimateAI publishes 2 APIs on the [APIs.io](https://apis.io/) network: Weather API (LensConnect) and Platform API. Tagged areas include Company, Weather, Climate, Climate Intelligence, and Forecasting.


  ClimateAI''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, signup flow, authentication, and 19 more developer resources.'
random_paper: 33
score:
  band: developing
  composite: 43.8
  delta: 0.0
  facets:
    commercial_clarity: 34.2
    contract_quality: 50.7
    developer_ergonomics: 56.0
    discoverability: 87.0
    governance: 21.9
    operational_transparency: 13.2
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 50.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: derived
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
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

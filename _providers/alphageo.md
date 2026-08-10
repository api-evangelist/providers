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
    agent_skills: false
    agentic_access: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: derived
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 18.5
  scored_at: '2026-08-10'
api_count: 1
apis:
- description: Public REST API for programmatically accessing AlphaGeo climate risk scoring data for global locations and portfolios. Location-Level Data APIs (Scores/CRRI, Physical Risk, Resilience-adjusted Risk, G
  name: AlphaGeo Data API
  slug: alphageo-data-api
artifact_total: 6
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/alphageo-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://alphageo.ai/security/
- group: auth
  title: ''
  type: Security
  url: https://alphageo.ai/security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.alphageo.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.alphageo.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.alphageo.ai/for-developers/alphageo-data-api
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.alphageo.ai/client-onboarding-guide
- group: company
  title: ''
  type: Blog
  url: https://alphageo.ai/insights
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.alphageo.ai/pricing/pricing-guide
- group: start
  title: ''
  type: SignUp
  url: https://app.alphageo.ai/trial_setup
- group: start
  title: ''
  type: Login
  url: https://app.alphageo.ai/
- group: operate
  title: ''
  type: Support
  url: mailto:support@alphageo.ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://alphageo.ai/service-agreement/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.alphageo-info.com/privacy
- group: company
  title: ''
  type: Website
  url: https://alphageo.ai/
- group: auth
  title: ''
  type: Authentication
  url: authentication/alphageo-authentication.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/alphageo-rate-limits.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/alphageo-problem-types.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/alphageo-conventions.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/alphageo-lifecycle.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/alphageo-data-model.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/alphageo-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/alphageo-llms.txt
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alphageo-domain-security.yml
created: '2026-07-17'
description: AlphaGeo is an AI-powered geospatial predictive analytics company that quantifies climate risk and adaptation for real assets to guide resilient, future-proof investing. Its enterprise SaaS platform (AlphaGeo Explorer) and public REST Data API deliver location-level and portfolio-level climate risk scores, resilience-adjusted risk, physical hazard layers (heat stress, inland and coastal flooding, hurricanes, drought, wildfire), and financial impact metrics across CMIP6 emission scenarios (SSP245, SSP370, SSP585) and time horizons (2025, 2035, 2050, 2100). The Data API returns per-location scores by address, coordinates, or uploaded asset ID, and portfolio aggregates across an institution's assets. Backed by DCVC, AlphaGeo also ships a Snowflake Native App and an agentic AI co-pilot, "Darwin."
image: https://app.alphageo.ai/assets/img/svg/alphaGeo-logo.svg
layout: provider
mcp_servers:
- description: ''
  name: alphageo-mcp.yml
  slug: alphageo-mcpyml
modified: '2026-07-17'
name: Alphageo
nav: Providers
network: true
overview: 'Alphageo publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Climate, Climate Risk, Geospatial, and Analytics.


  Alphageo''s developer surface includes documentation, API reference, getting-started guide, engineering blog, pricing, signup flow, support, and 17 more developer resources.'
random_paper: 21
rate_limits:
- limit_count: 6
  name: Alphageo Rate Limits
  slug: alphageo-rate-limits
score:
  band: thin
  composite: 37.1
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 0.0
    developer_ergonomics: 54.3
    discoverability: 87.0
    governance: 0.0
    operational_transparency: 42.1
  previous_composite: 37.1
  provenance:
    mcp: derived
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alphageo/refs/heads/main/screenshots/alphageo-2026-07-25T195759.png
security:
- kind: authentication
  name: Alphageo Authentication
  slug: alphageo-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Alphageo Domain Security
  slug: alphageo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Alphageo Trust Center
  slug: alphageo-trust-center
  summary_line: SOC 2
slug: alphageo
tags:
- Company
- Climate
- Climate Risk
- Geospatial
- Analytics
- Risk
- Real Estate
- ESG
- Data
- Machine Learning
website: https://alphageo.ai/
---

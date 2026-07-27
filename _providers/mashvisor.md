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
  band: agent-native
  dimensions:
    agent_skills: true
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: true
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 65.4
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Mashvisor Agentic Access
  operation_count: 28
  slug: mashvisor-agentic-access
  summary_line: 28 operations
api_count: 5
apis:
- description: ROI, investment breakdowns, and rental performance
  name: Mashvisor Investment Analysis API
  slug: mashvisor-investment-analysis-api
- description: Property records, images, taxing, transactions, estimates
  name: Mashvisor Property Info API
  slug: mashvisor-property-info-api
- description: Traditional and Airbnb rental-rate estimates
  name: Mashvisor Rental Rates API
  slug: mashvisor-rental-rates-api
- description: City, neighborhood, and listing search
  name: Mashvisor Search API
  slug: mashvisor-search-api
- description: Market trends and heatmaps
  name: Mashvisor Trends API
  slug: mashvisor-trends-api
artifact_total: 9
common:
- group: company
  title: ''
  type: Website
  url: https://mashvisor.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.mashvisor.com/api-doc-v2
- group: docs
  title: ''
  type: APIReference
  url: https://www.mashvisor.com/api-doc-v2
- group: start
  title: ''
  type: GettingStarted
  url: https://www.mashvisor.com/api-doc-v2/authentication
- group: commercial
  title: ''
  type: Pricing
  url: https://www.mashvisor.com/api-plans
- group: start
  title: ''
  type: SignUp
  url: https://www.mashvisor.com/explore/profile/developers?api-trial=true
- group: company
  title: ''
  type: Blog
  url: https://www.mashvisor.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.mashvisor.com/contact-us/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.mashvisor.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.mashvisor.com/privacy-policy/
- group: auth
  title: ''
  type: Authentication
  url: authentication/mashvisor-authentication.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/mashvisor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mashvisor-domain-security.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/mashvisor-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/mashvisor-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/mashvisor-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/mashvisor-conformance.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/mashvisor-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/mashvisor-sandbox.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/mashvisor-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/mashvisor-llms.txt
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Mashvisor is a real estate investment analytics platform for the US housing market. Its Data API gives investors, agents, property managers, and developers programmatic access to short-term (Airbnb) and long-term (traditional) rental performance, MLS listings and property records, neighborhood and city analytics, rental-rate estimates, investment ROI and cash-flow breakdowns, predictive scores, and market trends. All API operations are read-only GET requests authenticated with an x-api-key header and scoped by US state; responses are JSON. Plans range from a free developer trial to Enterprise. Mashvisor was surfaced as a 500 Global portfolio company and enriched by the API Evangelist pipeline from its public developer documentation.
image: https://www.mashvisor.com/favicon-32x32.png
layout: provider
mcp_servers:
- description: ''
  name: mashvisor-mcp.yml
  slug: mashvisor-mcpyml
modified: '2026-07-20'
name: Mashvisor
nav: Providers
network: true
overview: 'Mashvisor publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Investment Analysis API, Property Info API, Rental Rates API, and 2 more. Tagged areas include Company, Real Estate, Property Data, Analytics, and Rental.


  Mashvisor''s developer surface includes documentation, API reference, getting-started guide, pricing, signup flow, engineering blog, support, and 15 more developer resources.'
random_paper: 36
score:
  band: developing
  composite: 47.5
  delta: 0.0
  facets:
    commercial_clarity: 44.7
    contract_quality: 61.9
    developer_ergonomics: 65.2
    discoverability: 100.0
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 47.5
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mashvisor/refs/heads/main/screenshots/mashvisor-2026-07-25T230328.png
security:
- kind: authentication
  name: Mashvisor Authentication
  slug: mashvisor-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Mashvisor Domain Security
  slug: mashvisor-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mashvisor
tags:
- Company
- Real Estate
- Property Data
- Analytics
- Rental
- Airbnb
- Investment
- MLS
- Housing
website: https://mashvisor.com
---

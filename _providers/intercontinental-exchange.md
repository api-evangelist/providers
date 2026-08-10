---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: 0.2
  score: 35.4
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Intercontinental Exchange Agentic Access
  operation_count: 4
  slug: intercontinental-exchange-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: The ICE Consolidated Feed API provides developers with access to ICE Data Services real-time and delayed market data. The API delivers consolidated market data feeds from exchanges operated by Interco
  name: ICE Consolidated Feed API
  slug: consolidated-feed-api
- description: The ICE Data Services API provides access to market data, reference data, and analytics from Intercontinental Exchange. The IDS Portal provides documentation, tools, and software required for integrat
  name: ICE Data Services API
  slug: data-services-api
- description: The ICE Mortgage Technology Developer Portal is a self-service solution providing developers with resources and documentation to build and deploy mortgage lending applications. It includes a comprehen
  name: ICE Mortgage Technology Developer Portal
  slug: mortgage-technology-api
artifact_total: 12
collections:
- collection_type: open
  name: ICE Consolidated Feed API
  slug: open-ice-consolidated-feed-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/intercontinental-exchange-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/intercontinental-exchange-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/intercontinental-exchange-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/intercontinental-exchange-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/intercontinental-exchange-packages.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/intercontinental-exchange-well-known.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/intercontinental-exchange-llms.txt
- group: design
  title: ''
  type: Conformance
  url: conformance/intercontinental-exchange-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.ice.com/privacy-security-center/security
- group: auth
  title: ''
  type: TrustCenter
  url: security/intercontinental-exchange-trust-center.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/intercontinental-exchange-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.ice.com/status
- group: design
  title: ''
  type: Conventions
  url: conventions/intercontinental-exchange-conventions.yml
- group: design
  title: ''
  type: Components
  url: components/intercontinental-exchange-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/intercontinental-exchange-data-model.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/intercontinentalexchange
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.ice.com/privacy-security-center/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.ice.com/privacy-security-center
- group: company
  title: ''
  type: Blog
  url: https://www.ice.com/insights
- group: operate
  title: ''
  type: Support
  url: https://developer.theice.com/hc/en-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/icemarkets
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.theice.com/hc/en-us
- group: start
  title: ''
  type: Portal
  url: https://developer.theice.com/hc/en-us
- group: company
  title: ''
  type: Website
  url: https://www.ice.com/
created: '2026-03-21'
description: Intercontinental Exchange (ICE) operates global exchanges, clearing houses, and data services for financial and commodity markets, including the New York Stock Exchange (NYSE). ICE provides multiple developer portals including the Developer Center at developer.theice.com for market data APIs, the IDS Portal for real-time data integration, and the ICE Mortgage Technology Developer Portal for lending application development.
finops:
- name: Intercontinental Exchange Finops
  service_category: Market Data
  slug: intercontinental-exchange-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/intercontinental-exchange.png
layout: provider
mcp_servers:
- description: ''
  name: intercontinental-exchange-mcp.yml
  slug: intercontinental-exchange-mcpyml
modified: '2026-07-22'
name: Intercontinental Exchange
nav: Providers
network: true
overview: 'Intercontinental Exchange publishes 1 API on the [APIs.io](https://apis.io/) network: ICE Consolidated Feed API. Tagged areas include Commodities, Financial Exchanges, Market Data, NYSE, and Trading.


  Intercontinental Exchange''s developer surface includes authentication, engineering blog, support, developer portal, and 21 more developer resources.'
plans:
- name: Intercontinental Exchange Plans Pricing
  plan_count: 1
  slug: intercontinental-exchange-plans-pricing
press:
- date: '2026-05-25'
  title: 'Intercontinental Exchange''s AI Strategy: Analysis of ...'
  url: https://www.klover.ai/intercontinental-exchange-ai-strategy-analysis-of-dominance-in-global-financial-exchanges-clearinghouses/
- date: '2026-05-25'
  title: How Intercontinental Exchange is Taking AI from ...
  url: https://www.nvidia.com/en-us/on-demand/session/gtc25-s72463/
- date: '2026-05-25'
  title: Insights on AI and Data Management from Intercontinental ...
  url: https://www.linkedin.com/posts/allysonklein_insights-on-ai-and-data-management-from-intercontinental-activity-7328551226986377217-DQnR
- date: '2026-05-25'
  title: ICE Collaborates with Space Intelligence to Launch ICE's ...
  url: https://ir.theice.com/press/news-details/2024/ICE-Collaborates-with-Space-Intelligence-to-Launch-ICEs-Commodity-Traceability-Service/default.aspx
- date: '2026-05-25'
  title: National Housing Conference and ICE host industry ...
  url: https://nhc.org/press-release/national-housing-conference-and-ice-host-industry-leaders-and-experts-to-explore-technologys-transformative-impact-on-housing-finance/
random_paper: 57
rate_limits:
- limit_count: 1
  name: Intercontinental Exchange Rate Limits
  slug: intercontinental-exchange-rate-limits
score:
  band: developing
  composite: 51.7
  delta: 0.0
  facets:
    commercial_clarity: 65.8
    contract_quality: 56.6
    developer_ergonomics: 34.2
    discoverability: 92.6
    governance: 11.5
    operational_transparency: 42.1
  previous_composite: 51.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 60.0
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/intercontinental-exchange/refs/heads/main/screenshots/intercontinental-exchange-2026-06-20T183442.png
security:
- kind: authentication
  name: Intercontinental Exchange Authentication
  slug: intercontinental-exchange-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Intercontinental Exchange Domain Security
  slug: intercontinental-exchange-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Intercontinental Exchange Trust Center
  slug: intercontinental-exchange-trust-center
  summary_line: SOC 1, SOC 2
slug: intercontinental-exchange
tags:
- Commodities
- Financial Exchanges
- Market Data
- NYSE
- Trading
- Fortune 1000
website: https://www.ice.com/
---

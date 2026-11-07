---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  - '{''url'': ''https://prevedere.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.board.com/ — a different registrable domain (prevedere.com -> board.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Alert API from Prevedere — 1 operation(s) for alert.
  name: Prevedere Alert API
  slug: prevedere-alert-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The AlertDefinition API from Prevedere — 2 operation(s) for alertdefinition.
  name: Prevedere AlertDefinition API
  slug: prevedere-alertdefinition-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The AnalysisJob API from Prevedere — 2 operation(s) for analysisjob.
  name: Prevedere AnalysisJob API
  slug: prevedere-analysisjob-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The ComponentContributionOverrideValues API from Prevedere — 2 operation(s) for componentcontributionoverridevalues.
  name: Prevedere ComponentContributionOverrideValues API
  slug: prevedere-componentcontributionoverridevalues-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Context API from Prevedere — 1 operation(s) for context.
  name: Prevedere Context API
  slug: prevedere-context-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The DiscoverJob API from Prevedere — 2 operation(s) for discoverjob.
  name: Prevedere DiscoverJob API
  slug: prevedere-discoverjob-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Enumeration API from Prevedere — 6 operation(s) for enumeration.
  name: Prevedere Enumeration API
  slug: prevedere-enumeration-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Favorites API from Prevedere — 2 operation(s) for favorites.
  name: Prevedere Favorites API
  slug: prevedere-favorites-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The ForecastModel API from Prevedere — 16 operation(s) for forecastmodel.
  name: Prevedere ForecastModel API
  slug: prevedere-forecastmodel-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The ForecastModelHistory API from Prevedere — 1 operation(s) for forecastmodelhistory.
  name: Prevedere ForecastModelHistory API
  slug: prevedere-forecastmodelhistory-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The ForecastSummary API from Prevedere — 2 operation(s) for forecastsummary.
  name: Prevedere ForecastSummary API
  slug: prevedere-forecastsummary-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Indicator API from Prevedere — 9 operation(s) for indicator.
  name: Prevedere Indicator API
  slug: prevedere-indicator-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Provider API from Prevedere — 1 operation(s) for provider.
  name: Prevedere Provider API
  slug: prevedere-provider-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Scenario API from Prevedere — 2 operation(s) for scenario.
  name: Prevedere Scenario API
  slug: prevedere-scenario-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Tag API from Prevedere — 1 operation(s) for tag.
  name: Prevedere Tag API
  slug: prevedere-tag-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Test API from Prevedere — 1 operation(s) for test.
  name: Prevedere Test API
  slug: prevedere-test-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: Workbenches are a powerful feature in the Board Foresight application that allow users to organize and analyze data through indicators. They enable the creation of models by selecting primary and addi
  name: Prevedere Workbench API
  slug: prevedere-workbench-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The Data Integration API from Prevedere — 3 operation(s) for data integration.
  name: Prevedere Data Integration API
  slug: prevedere-data-integration-api
- baseURL: https://api.prevedere.com
  baseurl_source: declared
  description: The User Context API from Prevedere — 2 operation(s) for user context.
  name: Prevedere User Context API
  slug: prevedere-user-context-api
artifact_total: 46
collections:
- collection_type: open
  name: Board Foresight API - V1 Alert API
  slug: open-prevedere-alert-api
- collection_type: open
  name: Board Foresight API - V1 Alert AlertDefinition API
  slug: open-prevedere-alertdefinition-api
- collection_type: open
  name: Board Foresight API - V1 Alert AnalysisJob API
  slug: open-prevedere-analysisjob-api
- collection_type: open
  name: Board Foresight API - V1 Alert ComponentContributionOverrideValues API
  slug: open-prevedere-componentcontributionoverridevalues-api
- collection_type: open
  name: Board Foresight API - V1 Alert Context API
  slug: open-prevedere-context-api
- collection_type: open
  name: Board Foresight API - V1 Alert DataIntegration API
  slug: open-prevedere-dataintegration-api
- collection_type: open
  name: Board Foresight API - V1 Alert DiscoverJob API
  slug: open-prevedere-discoverjob-api
- collection_type: open
  name: Board Foresight API - V1 Alert Enumeration API
  slug: open-prevedere-enumeration-api
- collection_type: open
  name: Board Foresight API - V1 Alert Favorites API
  slug: open-prevedere-favorites-api
- collection_type: open
  name: Board Foresight API - V1 Alert ForecastModel API
  slug: open-prevedere-forecastmodel-api
- collection_type: open
  name: Board Foresight API - V1 Alert ForecastModelHistory API
  slug: open-prevedere-forecastmodelhistory-api
- collection_type: open
  name: Board Foresight API - V1 Alert ForecastSummary API
  slug: open-prevedere-forecastsummary-api
- collection_type: open
  name: Board Foresight API - V1 Alert Indicator API
  slug: open-prevedere-indicator-api
- collection_type: open
  name: Board Foresight API - V1 Alert Provider API
  slug: open-prevedere-provider-api
- collection_type: open
  name: Board Foresight API - V1 Alert Scenario API
  slug: open-prevedere-scenario-api
- collection_type: open
  name: Board Foresight API - V1 Alert Tag API
  slug: open-prevedere-tag-api
- collection_type: open
  name: Board Foresight API - V1 Alert Test API
  slug: open-prevedere-test-api
- collection_type: open
  name: Board Foresight API - V1 Alert UserContext API
  slug: open-prevedere-usercontext-api
- collection_type: open
  name: Board Foresight API - V1 Alert Workbench API
  slug: open-prevedere-workbench-api
common:
- group: commercial
  href: https://artifacts.apis.io/prevedere/plans/prevedere-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/prevedere-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/prevedere/capabilities/prevedere-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/prevedere-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/prevedere/security/prevedere-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/prevedere-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/prevedere/authentication/prevedere-authentication.yml
  title: ''
  type: Authentication
  url: authentication/prevedere-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://prevedere.com
- group: docs
  title: ''
  type: Documentation
  url: https://api.prevedere.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://api.prevedere.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.board.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://community.board.com/categories/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.board.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.board.com/legal-notice
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.board.com/privacy-policy
- group: design
  href: https://artifacts.apis.io/prevedere/errors/prevedere-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/prevedere-problem-types.yml
- group: design
  href: https://artifacts.apis.io/prevedere/conventions/prevedere-conventions.yml
  title: ''
  type: Conventions
  url: conventions/prevedere-conventions.yml
- group: design
  href: https://artifacts.apis.io/prevedere/conformance/prevedere-conformance.yml
  title: ''
  type: Conformance
  url: conformance/prevedere-conformance.yml
- group: design
  href: https://artifacts.apis.io/prevedere/data-model/prevedere-data-model.yml
  title: ''
  type: DataModel
  url: data-model/prevedere-data-model.yml
- group: design
  href: https://artifacts.apis.io/prevedere/lifecycle/prevedere-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/prevedere-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/prevedere/mcp/prevedere-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/prevedere-mcp.yml
- group: agent
  href: https://artifacts.apis.io/prevedere/llms/prevedere-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/prevedere-llms.txt
- group: other
  href: https://artifacts.apis.io/prevedere/overlays/prevedere-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/prevedere-openapi-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/prevedere/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
created: '2026-07-17'
description: Prevedere is an economic forecasting and predictive analytics platform that ingests thousands of external macroeconomic, industry, weather, and market indicators to drive demand planning, financial forecasting, and risk analysis. Its models correlate a company's internal metrics against leading external signals to project revenue, demand, and other business outcomes. Prevedere was acquired by Board International and its capability is now delivered as Board Foresight; the live Board Foresight API (V1), hosted at api.prevedere.com, exposes forecast models, indicators, scenarios, alerts, correlation discovery, and client-data integration. This profile enriches the surviving API surface.
finops:
- has_sources: true
  method: derived
  name: Prevedere Finops
  primary_unit: ''
  service_category: ''
  slug: prevedere-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/prevedere.png
layout: provider
modified: '2026-07-20'
name: Prevedere
nav: Providers
network: true
overview: 'Prevedere publishes 19 API contracts indexed on the [APIs.io](https://apis.io/) network, including Alert API, AlertDefinition API, AnalysisJob API, and 16 more. Tagged areas include Company, Economic Forecasting, Predictive Analytics, Demand Planning, and Financial Planning.


  The Prevedere catalog on APIs.io includes 1 Spectral governance ruleset.


  Prevedere''s developer surface includes authentication, documentation, API reference, pricing, support, and 16 more developer resources.'
plans:
- name: Prevedere Plans Pricing
  plan_count: 8
  slug: prevedere-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: Prevedere API Rules
  rule_count: 49
  severity_counts:
    error: 39
    hint: 0
    info: 4
    warn: 6
  slug: prevedere-rules
score:
  band: developing
  composite: 42.7
  coverage:
    artifact_dirs: 22
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 63.2
    contract_governance: 18.2
    contract_quality: 40.6
    developer_ergonomics: 44.6
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 42.7
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 19
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/prevedere/prevedere-2026-09-02T152020.png
security:
- kind: authentication
  name: Prevedere Authentication
  slug: prevedere-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Prevedere Domain Security
  slug: prevedere-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 3
skills:
- name: Discover leading economic indicators and correlations
  slug: prevedere-discover-indicators
- name: Monitor scenarios and alerts
  slug: prevedere-monitor-scenarios-alerts
- name: Read a Board Foresight forecast model and its projection
  slug: prevedere-read-forecast
slug: prevedere
tags:
- Company
- Economic Forecasting
- Predictive Analytics
- Demand Planning
- Financial Planning
- Macroeconomic Data
- Indicators
- Time Series
- Data Integration
- Machine Learning
website: https://prevedere.com
---

---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
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
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
api_count: 1
apis:
- baseURL: https://api.benchmarkminerals.com/v2
  baseurl_source: declared
  description: The Benchmark Minerals API provides programmatic access to price data, supply chain data, and market intelligence for the lithium-ion battery and critical minerals supply chain. API keys are available
  name: Benchmark Minerals API
  slug: benchmark-minerals-api
artifact_total: 20
common:
- group: auth
  title: ''
  type: Authentication
  url: authentication/benchmark-minerals-authentication.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchmark-minerals-domain-security.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/benchmark-minerals-scopes.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/benchmark-minerals-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/benchmark-minerals-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/benchmark-minerals-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/benchmark-minerals-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/benchmark-minerals-conformance.yml
- group: auth
  title: IOSCO-assured price assessments
  type: Compliance
  url: conformance/benchmark-minerals-conformance.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/benchmark-minerals-well-known.yml
- group: agent
  title: Benchmark MCP Gateway (https://mcp.benchmarkminerals.com/mcp)
  type: MCPServer
  url: mcp/benchmark-minerals-mcp.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/benchmark-minerals-llms.txt
- group: build
  title: ''
  type: Packages
  url: packages/benchmark-minerals-packages.yml
- group: design
  title: ''
  type: Components
  url: components/benchmark-minerals-components.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/benchmark-minerals-sandbox.yml
- group: commercial
  title: ''
  type: Plans
  url: plans/benchmark-minerals-plans-pricing.yml
- group: docs
  title: ''
  type: Documentation
  url: https://www.benchmarkminerals.com/api
- group: docs
  title: ''
  type: APIReference
  url: https://www.benchmarkminerals.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://www.benchmarkminerals.com/contact/a-technical-issue
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.benchmarkminerals.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.benchmarkminerals.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benchmarkminerals
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/benchmark-mineral-intelligence
- group: company
  title: ''
  type: Website
  url: https://www.benchmarkminerals.com
- group: start
  title: Benchmark API
  type: DeveloperPortal
  url: https://www.benchmarkminerals.com/api
- group: company
  title: Benchmark Source
  type: Blog
  url: https://source.benchmarkminerals.com
- group: commercial
  title: Subscription Plans
  type: Pricing
  url: https://www.benchmarkminerals.com/plans
created: '2025-03-01'
description: Benchmark Mineral Intelligence is the world's leading market intelligence and price reporting agency for the lithium-ion battery supply chain and energy transition materials. The company provides mine-to-grid supply chain data, price assessments, forecasts, and databases covering lithium, nickel, cobalt, graphite, batteries, electric vehicles, rare earths, and permanent magnets. Benchmark's proprietary price assessment methodologies are assured to Type 2 IOSCO standards. API access is available to subscribers for programmatic integration of price data, supply chain data, and market intelligence into business systems and analytics platforms.
features:
- description: IOSCO Type 2 assured benchmark price assessments for lithium, nickel, cobalt, graphite, rare earths, permanent magnets, and battery cells, used as reference prices in supply contracts and financial instruments.
  name: Price Assessments
- description: Comprehensive mine-to-grid supply chain databases covering raw material mining, processing, cell manufacturing, and gigafactory capacity across lithium ion and sodium ion battery chemistries.
  name: Supply Chain Data
- description: Long-term supply and demand forecasts for critical battery materials and electric vehicle adoption, tracking policy shifts, capacity expansions, and technology transitions.
  name: Market Forecasts
- description: Global tracking of battery gigafactory capacity, ownership, operating status, production volumes, and technology transitions for lithium ion and next-generation battery chemistries.
  name: Gigafactory Intelligence
- description: Enterprise API access enables subscribers to integrate Benchmark price data and supply chain databases directly into business intelligence platforms, ERP systems, and procurement workflows.
  name: API Data Integration
- description: Interactive price dashboard providing real-time access to benchmark prices, historical price charts, and data visualization for energy transition materials.
  name: Price Dashboard
finops:
- name: Benchmark Minerals Finops
  service_category: API
  slug: benchmark-minerals-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benchmark-minerals.png
integrations:
- description: Benchmark API integrates with BI tools and data analytics platforms to embed price data and supply chain metrics in custom dashboards and reporting workflows.
  name: Business Intelligence Platforms
- description: Enterprise API access enables integration of Benchmark benchmark prices into ERP and procurement systems for automated contract indexing and raw material cost tracking.
  name: ERP Systems
layout: provider
mcp_servers:
- description: A first-party remote MCP server operated by Benchmark Mineral Intelligence on their own subdomain, fronting an AWS Bedrock AgentCore Gateway. It is undocumented on the public website — it was found by
  name: Benchmark MCP Gateway (https://mcp.benchmarkminerals.com/mcp)
  slug: benchmark-mcp-gateway-httpsmcpbenchmarkmineralscommcp
modified: '2026-09-04'
name: Benchmark Minerals
nav: Providers
network: true
overview: 'Benchmark Minerals publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Batteries, Cobalt, Critical Minerals, Electric Vehicles, and Energy Transition.


  Benchmark Minerals'' developer surface includes authentication, sandbox, documentation, API reference, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Benchmark Minerals Plans Pricing
  plan_count: 3
  slug: benchmark-minerals-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Benchmark Minerals Rate Limits
  slug: benchmark-minerals-rate-limits
scopes:
- name: Benchmark Minerals Scopes
  scope_count: 0
  slug: benchmark-minerals-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 54.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.3
  facets:
    access_clarity: 78.9
    commercial_clarity: 78.9
    contract_governance: 18.2
    contract_quality: 49.0
    developer_ergonomics: 54.2
    discoverability: 68.5
    governance: 18.2
    operational_transparency: 2.6
  previous_composite: 55.2
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 63.5
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benchmark-minerals/refs/heads/main/screenshots/benchmark-minerals-2026-06-20T173138.png
security:
- kind: authentication
  name: Benchmark Minerals Authentication
  slug: benchmark-minerals-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Benchmark Minerals Domain Security
  slug: benchmark-minerals-domain-security
  summary_line: TLSv1.3 · DMARC
slug: benchmark-minerals
tags:
- Batteries
- Cobalt
- Critical Minerals
- Electric Vehicles
- Energy Transition
- Graphite
- Lithium
- Lithium-Ion
- Market Intelligence
- Mining
- Nickel
- Price Reporting
- Rare Earths
- Supply Chain
use_cases:
- description: Battery manufacturers and EV OEMs use Benchmark price data as reference benchmarks in raw material supply contracts and procurement negotiations for lithium, nickel, cobalt, and graphite.
  name: Supply Chain Procurement
- description: Investors, banks, and financial institutions use Benchmark forecasts and price data to evaluate mining projects, battery companies, and energy transition investment opportunities.
  name: Investment and Financial Analysis
- description: Corporate strategy teams and policy makers use Benchmark supply chain databases and forecasts to plan capacity investments and assess raw material availability for battery manufacturing programs.
  name: Strategic Planning
- description: Supply chain managers use Benchmark price data and market intelligence to identify supply risks, monitor market conditions, and develop hedging strategies for critical mineral exposure.
  name: Risk Management
website: https://www.benchmarkminerals.com
---

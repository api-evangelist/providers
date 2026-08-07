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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-08-06'
api_count: 1
apis:
- description: The Benchmark Minerals API provides programmatic access to price data, supply chain data, and market intelligence for the lithium-ion battery and critical minerals supply chain. API keys are available
  name: Benchmark Minerals API
  slug: benchmark-minerals-api
artifact_total: 17
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchmark-minerals-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/benchmark-mineral-intelligence
- group: company
  title: ''
  type: Website
  url: https://www.benchmarkminerals.com
- group: start
  title: Benchmark Source Data Platform
  type: Portal
  url: https://source.benchmarkminerals.com
- group: commercial
  title: Price Data Subscriptions
  type: Pricing
  url: https://www.benchmarkminerals.com/all-prices-subscription
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
modified: '2026-04-19'
name: Benchmark Minerals
nav: Providers
network: true
overview: 'Benchmark Minerals publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Batteries, Cobalt, Critical Minerals, Electric Vehicles, and Energy Transition.


  Benchmark Minerals'' developer surface includes developer portal, pricing, and 3 more developer resources.'
plans:
- name: Benchmark Minerals Plans Pricing
  plan_count: 3
  slug: benchmark-minerals-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Benchmark Minerals Rate Limits
  slug: benchmark-minerals-rate-limits
score:
  band: emerging
  composite: 21.8
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 21.8
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benchmark-minerals/refs/heads/main/screenshots/benchmark-minerals-2026-06-20T173138.png
security:
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
- Lithium Ion
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

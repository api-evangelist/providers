---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 2
apis:
- description: Cordant is Baker Hughes' modular AI-enabled industrial enterprise software platform for asset performance management (APM), process optimization, and emissions management. It provides a digital thread
  name: Baker Hughes Cordant Industrial Platform
  slug: cordant-platform
- description: The BHC3 AI Suite is a joint product from Baker Hughes and C3.ai providing pre-built, configurable AI applications for the energy industry. Applications cover predictive maintenance, reliability, prod
  name: Baker Hughes BHC3 AI Suite
  slug: bhc3-ai-suite
artifact_total: 31
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/baker-hughes-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BakerHughes
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bakerhughes
- group: company
  title: ''
  type: Website
  url: https://www.bakerhughes.com
- group: start
  title: ''
  type: Portal
  url: https://www.bakerhughes.com/company/digital
- group: company
  title: ''
  type: Blog
  url: https://www.bakerhughes.com/company/news
- group: operate
  title: ''
  type: Support
  url: https://www.bakerhughes.com/contact-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bakerhughes.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bakerhughes.com/terms-and-conditions
- group: design
  title: ''
  type: SpectralRules
  url: rules/baker-hughes-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/baker-hughes-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/baker-hughes-context.jsonld
created: '2026-03-21'
description: Baker Hughes is an energy technology company providing solutions to energy and industrial customers worldwide. Their digital portfolio includes the Cordant industrial software platform for asset performance management, process optimization, and emissions management, along with the BHC3 AI Suite (in alliance with C3.ai) for enterprise AI applications in oil and gas. Baker Hughes operates across oilfield services, industrial equipment, and digital solutions segments globally.
features:
- description: AI-powered predictive maintenance and reliability for industrial assets.
  name: Asset Performance Management
- description: Real-time process monitoring and optimization for energy and industrial operations.
  name: Process Optimization
- description: Track, measure, and reduce greenhouse gas emissions across operations.
  name: Emissions Management
- description: Pre-built AI applications for oil and gas use cases including production optimization and well integrity.
  name: Enterprise AI Applications
- description: Connectivity between operational technology (OT) sensor data and enterprise IT systems.
  name: OT/IT Integration
- description: Connected data fabric linking assets, processes, and enterprise systems across operations.
  name: Digital Thread
- description: Continuous monitoring of well barrier status and integrity for safe operations.
  name: Well Integrity Monitoring
- description: AI-driven optimization of oil and gas production rates from well and reservoir data.
  name: Production Optimization
finops:
- name: Baker Hughes Finops
  service_category: Industrial / Energy Software
  slug: baker-hughes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/baker-hughes.png
integrations:
- description: BHC3 AI Suite is optimized to run on Microsoft Azure cloud infrastructure.
  name: Microsoft Azure
- description: Strategic AI alliance providing enterprise AI platform capabilities for BHC3.
  name: C3.ai
- description: Integration with SAP ERP for asset and maintenance management data.
  name: SAP
- description: Integration with OSIsoft PI data historian for real-time process data.
  name: OSIsoft PI
- description: Integration with IBM Maximo asset management for work order lifecycle.
  name: Maximo
- description: Integration with Honeywell process control and DCS systems.
  name: Honeywell
json_schemas:
- name: Asset
  property_count: 9
  slug: baker-hughes-asset
- name: Prediction
  property_count: 8
  slug: baker-hughes-prediction
jsonld:
- class_count: 0
  name: Baker Hughes Context
  property_count: 25
  slug: baker-hughes-context
layout: provider
modified: '2026-04-21'
name: Baker Hughes
nav: Providers
network: true
overview: 'Baker Hughes publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Energy Technology, Industrial IoT, Oil And Gas, Asset Performance Management, and Digital Energy.


  The Baker Hughes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Baker Hughes'' developer surface includes developer portal, engineering blog, support, and 9 more developer resources.'
plans:
- name: Baker Hughes Plans Pricing
  plan_count: 1
  slug: baker-hughes-plans-pricing
press:
- date: '2026-05-25'
  title: Baker Hughes launches AI software to optimise oil and gas ...
  url: https://www.oilandgasadvancement.com/press-releases/baker-hughes-launches-ai-software-to-optimise-oil-and-gas-production/
- date: '2026-05-25'
  title: Baker Hughes and C3 AI Deploy Enterprise AI Solutions at ...
  url: https://investors.bakerhughes.com/news/press-releases/news-details/2021/Baker-Hughes-and-C3-AI-Deploy-Enterprise-AI-Solutions-at-MEG-Energy-for-Improved-Efficiency-of-Thermal-Production-Operations-09-14-2021/default.aspx
- date: '2026-05-25'
  title: Baker Hughes, a GE company and C3.ai Announce Joint ...
  url: https://investors.bakerhughes.com/news/press-releases/news-details/2019/Baker-Hughes-a-GE-company-and-C3-ai-Announce-Joint-Venture-to-Deliver-AI-Solutions-Across-the-Oil-and-Gas-Industry-06-24-2019/default.aspx
- date: '2026-05-25'
  title: AI by BakerHughesC3.ai
  url: https://www.bakerhughes.com/ai-bakerhughesc3ai/
- date: '2026-05-25'
  title: Baker Hughes and C3 AI to Provide Joint Enterprise AI ...
  url: https://www.linkedin.com/posts/bakerhughes_baker-hughes-and-c3-ai-to-provide-joint-enterprise-activity-6764960334307495936-z-zl
random_paper: 58
rate_limits:
- limit_count: 1
  name: Baker Hughes Rate Limits
  slug: baker-hughes-rate-limits
rules:
- name: Baker Hughes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: baker-hughes-jsonschema-spectral-rules
- name: Baker Hughes API Rules
  rule_count: 15
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 10
  slug: baker-hughes-spectral-rules
score:
  band: thin
  composite: 33.9
  delta: -4.8
  facets:
    commercial_clarity: 50.0
    contract_quality: 12.9
    developer_ergonomics: 15.2
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 38.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/baker-hughes/refs/heads/main/screenshots/baker-hughes-2026-06-20T172934.png
security:
- kind: domain-security
  name: Baker Hughes Domain Security
  slug: baker-hughes-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: baker-hughes
tags:
- Energy Technology
- Industrial IoT
- Oil And Gas
- Asset Performance Management
- Digital Energy
- Fortune 500
use_cases:
- description: Predict equipment failures before they occur to reduce unplanned downtime and maintenance costs.
  name: Predictive Maintenance
- description: Optimize oil and gas production rates using AI-driven insights from well and reservoir data.
  name: Production Optimization
- description: Monitor and report on emissions, energy consumption, and ESG metrics across facilities.
  name: Sustainability Reporting
- description: Automate and optimize industrial processes using real-time sensor data and AI recommendations.
  name: Industrial Process Control
- description: Monitor and optimize oil and gas well performance across the full production lifecycle.
  name: Well Lifecycle Management
- description: Optimize spare parts inventory for maintenance operations using AI demand forecasting.
  name: Inventory Optimization
website: https://www.bakerhughes.com
---

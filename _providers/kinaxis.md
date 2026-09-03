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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 5.0
  scored_at: '2026-09-03'
api_count: 3
apis:
- description: REST-based interface exposing the Kinaxis Maestro (RapidResponse) supply chain planning platform for data integration, process orchestration, and insight embedding. Enables reading and writing plannin
  name: Kinaxis RapidResponse REST API
  slug: rapidresponse-rest-api
- description: A low-code and code-first development environment embedded in the Kinaxis Maestro platform that enables building custom supply chain applications, algorithms, data models, integration jobs, visualizat
  name: Kinaxis Developer Studio
  slug: developer-studio
- description: A production-ready Model Context Protocol (MCP) server that provides AI agents and LLM-powered applications with standardized OAuth 2.0-secured access to Kinaxis Maestro supply chain planning data and
  name: Kinaxis MCP Server
  slug: mcp-server
artifact_total: 9
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/kinaxis-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/kinaxis-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/kinaxis-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.kinaxis.com/en
- group: docs
  title: ''
  type: Documentation
  url: https://knowledge.kinaxis.com/s/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Kinaxis
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/kinaxis
- group: company
  title: ''
  type: Blog
  url: https://www.kinaxis.com/en/blog/main
- group: commercial
  title: ''
  type: Pricing
  url: https://www.kinaxis.com/en/contact-us
- group: other
  title: ''
  type: X
  url: https://x.com/kinaxis
- group: commercial
  title: ''
  type: Plans
  url: plans/kinaxis-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/kinaxis-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/kinaxis-finops.yml
created: 2026-06-13
description: Kinaxis is a concurrent supply chain planning platform — branded Maestro (formerly RapidResponse) — that provides REST APIs for supply chain orchestration, scenario modeling, demand sensing, and supply planning across global manufacturing and distribution networks. The platform offers an AI-infused intelligence engine, digital twin simulation, and a Developer Studio for building custom applications and algorithms on top of the supply chain data fabric.
finops:
- name: Kinaxis Finops
  service_category: ''
  slug: kinaxis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/kinaxis.png
layout: provider
modified: 2026-06-13
name: Kinaxis
nav: Providers
network: true
overview: 'Kinaxis publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Supply Chain, Supply Chain Planning, Demand Sensing, Scenario Modeling, and Supply Planning.


  Kinaxis'' developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Kinaxis Plans Pricing
  plan_count: 1
  slug: kinaxis-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Kinaxis Rate Limits
  slug: kinaxis-rate-limits
score:
  band: emerging
  composite: 24.7
  coverage:
    artifact_dirs: 7
    catalog_gap: 64.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 24.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/kinaxis/refs/heads/main/screenshots/kinaxis-2026-06-20T184039.png
security:
- kind: domain-security
  name: Kinaxis Domain Security
  slug: kinaxis-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Kinaxis Vulnerability Disclosure
  slug: kinaxis-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Kinaxis Trust Center
  slug: kinaxis-trust-center
  summary_line: SOC 2, ISO 27001, GDPR
slug: kinaxis
tags:
- Supply Chain
- Supply Chain Planning
- Demand Sensing
- Scenario Modeling
- Supply Planning
- Inventory Optimization
- S&OP
- Control Tower
- Enterprise Software
- Artificial Intelligence
website: https://www.kinaxis.com/en
---

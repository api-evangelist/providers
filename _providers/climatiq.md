---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Climatiq Agentic Access
  operation_count: 18
  slug: climatiq-agentic-access
  summary_line: 18 operations · 14 acting
api_count: 11
apis:
- description: AI-driven automated emissions calculation.
  name: Climatiq Autopilot API
  slug: climatiq-autopilot-api
- description: EU Carbon Border Adjustment Mechanism reporting.
  name: Climatiq CBAM API
  slug: climatiq-cbam-api
- description: Industry classification mappings for emission factors.
  name: Climatiq Classifications API
  slug: climatiq-classifications-api
- description: Cloud computing carbon footprint.
  name: Climatiq Computing API
  slug: climatiq-computing-api
- description: Emissions from electricity, heat, and fuel consumption.
  name: Climatiq Energy API
  slug: climatiq-energy-api
- description: Activity-based emission estimation.
  name: Climatiq Estimate API
  slug: climatiq-estimate-api
- description: Multi-modal freight emissions using GLEC factors.
  name: Climatiq Freight API
  slug: climatiq-freight-api
- description: Spend-based emissions for purchased goods and services.
  name: Climatiq Procurement API
  slug: climatiq-procurement-api
- description: Reference data such as regions and unit types.
  name: Climatiq Reference API
  slug: climatiq-reference-api
- description: Discover emission factors in the Climatiq dataset.
  name: Climatiq Search API
  slug: climatiq-search-api
- description: Emissions from passenger travel and accommodation.
  name: Climatiq Travel API
  slug: climatiq-travel-api
artifact_total: 33
collections:
- collection_type: postman
  name: Climatiq Autopilot API
  slug: postman-climatiq-autopilot-api
- collection_type: postman
  name: Climatiq Autopilot CBAM API
  slug: postman-climatiq-cbam-api
- collection_type: postman
  name: Climatiq Autopilot Classifications API
  slug: postman-climatiq-classifications-api
- collection_type: postman
  name: Climatiq Autopilot Computing API
  slug: postman-climatiq-computing-api
- collection_type: postman
  name: Climatiq Autopilot Energy API
  slug: postman-climatiq-energy-api
- collection_type: postman
  name: Climatiq Autopilot Estimate API
  slug: postman-climatiq-estimate-api
- collection_type: postman
  name: Climatiq Autopilot Freight API
  slug: postman-climatiq-freight-api
- collection_type: postman
  name: Climatiq Autopilot Procurement API
  slug: postman-climatiq-procurement-api
- collection_type: postman
  name: Climatiq Autopilot Reference API
  slug: postman-climatiq-reference-api
- collection_type: postman
  name: Climatiq Autopilot Search API
  slug: postman-climatiq-search-api
- collection_type: postman
  name: Climatiq Autopilot Travel API
  slug: postman-climatiq-travel-api
- collection_type: open
  name: Climatiq API
  slug: open-climatiq
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/climatiq/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/climatiq-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/climatiq-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/climatiq-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/climatiq
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/climatiq
- group: company
  title: ''
  type: Website
  url: https://www.climatiq.io/
- group: start
  title: ''
  type: Portal
  url: https://www.climatiq.io/docs
- group: docs
  title: ''
  type: Documentation
  url: https://www.climatiq.io/docs/api-reference
- group: start
  title: ''
  type: GettingStarted
  url: https://www.climatiq.io/docs/guides/tutorials/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://www.climatiq.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.climatiq.io/blog
- group: auth
  title: ''
  type: Trust
  url: https://trust.climatiq.io/
- group: operate
  title: ''
  type: Support
  url: https://www.climatiq.io/support
- group: other
  title: ''
  type: Customers
  url: https://www.climatiq.io/customers
- group: start
  title: ''
  type: Login
  url: https://auth.climatiq.io/login
- group: other
  title: ''
  type: Playground
  url: https://www.climatiq.io/demo
- group: company
  title: ''
  type: Partners
  url: https://www.climatiq.io/partner-with-climatiq
- group: company
  title: ''
  type: Newsletter
  url: https://www.climatiq.io/newsletter
- group: design
  title: ''
  type: Versioning
  url: https://www.climatiq.io/docs/changelogs/api-release
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/climatiq-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/climatiq-emission-estimate-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/climatiq-context.jsonld
- group: design
  title: ''
  type: Spectral
  url: rules/climatiq-rules.yml
created: '2025-02-24'
description: Climatiq provides a developer-first API for carbon accounting and emissions calculations. The platform packages a curated emission-factor database together with calculation endpoints that turn activity or spend data into auditable CO2-equivalent estimates aligned with the GHG Protocol. Capabilities span search across the factor catalog, generic activity-based estimation, and purpose-built endpoints for travel, freight (GLEC), energy, cloud computing, procurement, and the EU Carbon Border Adjustment Mechanism. The API is keyed (Bearer token) and hosted at api.climatiq.io.
finops:
- name: Climatiq Finops
  service_category: API
  slug: climatiq-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/climatiq.png
json_schemas:
- name: Climatiq Emission Estimate
  property_count: 8
  slug: climatiq-emission-estimate
jsonld:
- class_count: 9
  name: Climatiq Context
  property_count: 6
  slug: climatiq-context
layout: provider
modified: '2026-05-19'
name: Climatiq
nav: Providers
network: true
overview: 'Climatiq publishes 11 APIs on the [APIs.io](https://apis.io/) network, including Autopilot API, CBAM API, Classifications API, and 8 more. Tagged areas include Carbon Accounting, Carbon Emissions, Climate, Energy, and Environment.


  The Climatiq catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Climatiq''s developer surface includes authentication, developer portal, documentation, getting-started guide, pricing, engineering blog, support, and 17 more developer resources.'
plans:
- name: Climatiq Plans Pricing
  plan_count: 3
  slug: climatiq-plans-pricing
random_paper: 62
rate_limits:
- limit_count: 5
  name: Climatiq Rate Limits
  slug: climatiq-rate-limits
rules:
- name: Climatiq API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: climatiq-jsonschema-spectral-rules
- name: Climatiq API Rules
  rule_count: 6
  severity_counts:
    error: 4
    hint: 0
    info: 0
    warn: 2
  slug: climatiq-rules
score:
  band: strong
  composite: 58.1
  delta: -8.2
  facets:
    commercial_clarity: 71.1
    contract_quality: 65.3
    developer_ergonomics: 56.5
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 66.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 29.7
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/climatiq/refs/heads/main/screenshots/climatiq-2026-06-20T174523.png
security:
- kind: authentication
  name: Climatiq Authentication
  slug: climatiq-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Climatiq Domain Security
  slug: climatiq-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: climatiq
tags:
- Carbon Accounting
- Carbon Emissions
- Climate
- Energy
- Environment
- GHG Protocol
- Sustainability
website: https://www.climatiq.io/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
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
api_count: 3
apis:
- description: REST API providing access to healthcare pricing data including hospital negotiated rates, payer contracted rates, out-of-pocket cost estimates, and machine-readable file (MRF) data. Supports the Turqu
  name: Turquoise Health REST API
  slug: turquoise-health-rest-api
- description: An MCP (Model Context Protocol) server that connects AI tools to Turquoise Health's healthcare pricing data, enabling developers to query pricing information across multiple care settings and organiza
  name: Turquoise Connector (MCP)
  slug: turquoise-connector-mcp
- description: Free API providing access to Turquoise Health's library of Standard Service Packages (SSPs), which gather all medical services, materials, and fees associated with a healthcare procedure and represent
  name: Standard Service Packages (SSP) API
  slug: standard-service-packages-ssp-api
artifact_total: 8
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/turquoise-health-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://turquoise.health/
- group: docs
  title: ''
  type: Documentation
  url: https://turquoise.health/api/redoc
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/turquoisehealth
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/turquoise-health/
- group: other
  title: ''
  type: X
  url: https://twitter.com/TurquoiseHC
- group: company
  title: ''
  type: Blog
  url: https://turquoise.health/resources/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://turquoise.health/plans/providers
- group: commercial
  title: ''
  type: Plans
  url: plans/turquoise-health-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/turquoise-health-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/turquoise-health-finops.yml
created: '2026-06-13'
description: Turquoise Health is a healthcare price transparency platform that provides REST APIs for accessing hospital and insurer negotiated rates, out-of-pocket cost estimates, and machine-readable files (MRF) data. The platform enables precision pricing and intelligent contracting for finance teams across healthcare, covering providers, payers, and life sciences organizations. Turquoise Health also offers the Turquoise Connector MCP server for AI-tool integration with healthcare pricing data, Standard Service Packages (SSP) APIs, and open-source toolkits for FHIR financial transaction standards.
finops:
- name: Turquoise Health Finops
  service_category: ''
  slug: turquoise-health-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/turquoise-health.png
jsonld:
- class_count: 17
  name: Turquoise Health Context
  property_count: 38
  slug: turquoise-health-context
layout: provider
modified: '2026-06-13'
name: Turquoise Health
nav: Providers
network: true
overview: 'Turquoise Health publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Price Transparency, Hospital Rates, Payer Rates, and Machine-Readable Files.


  The Turquoise Health catalog on APIs.io includes 1 JSON-LD context.


  Turquoise Health''s developer surface includes documentation, engineering blog, pricing, and 8 more developer resources.'
plans:
- name: Turquoise Health Plans Pricing
  plan_count: 3
  slug: turquoise-health-plans-pricing
random_paper: 25
rate_limits:
- limit_count: 0
  name: Turquoise Health Rate Limits
  slug: turquoise-health-rate-limits
score:
  band: emerging
  composite: 23.1
  delta: -4.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 17.7
    developer_ergonomics: 10.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 27.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
security:
- kind: domain-security
  name: Turquoise Health Domain Security
  slug: turquoise-health-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: turquoise-health
tags:
- Healthcare
- Price Transparency
- Hospital Rates
- Payer Rates
- Machine-Readable Files
- FHIR
- Health Insurance
- Negotiated Rates
- Out-of-Pocket Costs
- MRF
website: https://turquoise.health/
---

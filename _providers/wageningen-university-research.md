---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Wageningen University Research Agentic Access
  operation_count: 55
  slug: wageningen-university-research-agentic-access
  summary_line: 55 operations
api_count: 6
apis:
- description: API for scientific data about food products, published by Wageningen Food & Biobased Research (WFBR) through an Azure API Management developer portal. Provides software services and algorithms returni
  name: WFBR Food API
  slug: wfbr-food-api
- description: The Altitude API from Wageningen University & Research — 1 operation(s) for altitude.
  name: Wageningen University & Research Altitude API
  slug: wageningen-university-research-altitude-api
- description: The KPI API from Wageningen University & Research — 2 operation(s) for kpi.
  name: Wageningen University & Research KPI API
  slug: wageningen-university-research-kpi-api
- description: The Raster API from Wageningen University & Research — 4 operation(s) for raster.
  name: Wageningen University & Research Raster API
  slug: wageningen-university-research-raster-api
- description: The Retrieve API from Wageningen University & Research — 19 operation(s) for retrieve.
  name: Wageningen University & Research Retrieve API
  slug: wageningen-university-research-retrieve-api
- description: The Return API from Wageningen University & Research — 10 operation(s) for return.
  name: Wageningen University & Research Return API
  slug: wageningen-university-research-return-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wageningen-university-research-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/wageningen-university-research-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wageningen-university-research-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wageningen-university-research-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.wur.nl/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/WUR-AI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/wageningen-university/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://euw-apim-fism-001-p.developer.azure-api.net/
- group: commercial
  title: ''
  type: Plans
  url: plans/wageningen-university-research-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wageningen-university-research-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/wageningen-university-research-finops.yml
- group: other
  title: ''
  type: Review
  url: review.yml
created: '2026-06-03'
description: 'Wageningen University & Research (WUR) is a Dutch university and research institution based in Wageningen, Netherlands, specializing in the domain of healthy food and living environment, and ranked #100 in the QS World University Rankings 2025. Its public developer footprint centers on the agri-food research domain rather than a single central API platform: the AgroDataCube provides a token-based REST API over a large open data collection for agri-food applications, and Wageningen Food & Biobased Research (WFBR) operates an Azure API Management developer portal publishing a Food API for scientific data about food products. WUR also runs a Pure-powered Research Portal (research.wur.nl) and a public Data Portal, though documented public web-service/OAI endpoints there were not openly reachable at review time.'
examples:
- key_count: 2
  name: Wageningen University Research Cropcodes Example
  slug: wageningen-university-research-cropcodes-example
- key_count: 2
  name: Wageningen University Research Fields Example
  slug: wageningen-university-research-fields-example
finops:
- name: Wageningen University Research Finops
  service_category: Education
  slug: wageningen-university-research-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/wageningen-university-research.png
json_schemas:
- name: AgroDataCube Field FeatureCollection
  property_count: 2
  slug: wageningen-university-research-field
json_structures:
- name: Wageningen University Research Field Structure
  property_count: 7
  slug: wageningen-university-research-field-structure
jsonld:
- class_count: 15
  name: Wageningen University Research Context
  property_count: 2
  slug: wageningen-university-research-context
layout: provider
modified: '2026-06-03'
name: Wageningen University & Research
nav: Providers
network: true
overview: 'Wageningen University & Research publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Altitude API, KPI API, Raster API, and 2 more. Tagged areas include Education, Higher Education, University, Research, and Agriculture.


  The Wageningen University & Research catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Wageningen University & Research''s developer surface includes authentication, GitHub presence, and 10 more developer resources.'
plans:
- name: Wageningen University Research Plans Pricing
  plan_count: 2
  slug: wageningen-university-research-plans-pricing
random_paper: 76
rate_limits:
- limit_count: 1
  name: Wageningen University Research Rate Limits
  slug: wageningen-university-research-rate-limits
rules:
- name: Wageningen University & Research API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wageningen-university-research-jsonschema-spectral-rules
- name: Wageningen University & Research API Rules
  rule_count: 6
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 2
  slug: wageningen-university-research-rules
score:
  band: developing
  composite: 44.8
  delta: -4.4
  facets:
    commercial_clarity: 28.9
    contract_quality: 74.6
    developer_ergonomics: 19.6
    discoverability: 64.8
    governance: 58.3
    operational_transparency: 26.3
  previous_composite: 49.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 42.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wageningen-university-research/refs/heads/main/screenshots/wageningen-university-research-2026-06-20T201159.png
security:
- kind: authentication
  name: Wageningen University Research Authentication
  slug: wageningen-university-research-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Wageningen University Research Domain Security
  slug: wageningen-university-research-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Wageningen University Research Vulnerability Disclosure
  slug: wageningen-university-research-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: wageningen-university-research
tags:
- Education
- Higher Education
- University
- Research
- Agriculture
- Agri-Food
- Open Data
- Netherlands
website: https://www.wur.nl/
---

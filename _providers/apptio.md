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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apptio Agentic Access
  operation_count: 4
  slug: apptio-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: IT budget planning and tracking
  name: Apptio Budgets API
  slug: apptio-budgets-api
- description: Technology cost allocation management
  name: Apptio Cost Allocations API
  slug: apptio-cost-allocations-api
- description: Financial reporting and analytics
  name: Apptio Reports API
  slug: apptio-reports-api
artifact_total: 15
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apptio-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apptio-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apptio-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apptio-an-ibm-company
- group: company
  title: ''
  type: Website
  url: https://www.apptio.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.apptio.com/
- group: company
  title: ''
  type: Blog
  url: https://www.apptio.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://www.apptio.com/request-demo/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apptio
created: '2026-03-16'
description: Apptio is a technology business management platform that helps organizations understand the cost, value, and quality of their technology investments. It provides financial management, planning, and analytics capabilities for IT organizations, enabling data-driven decision-making around technology spending and resource allocation.
examples:
- key_count: 8
  name: Cost Allocation Example
  slug: cost-allocation-example
finops:
- name: Apptio Finops
  service_category: API
  slug: apptio-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apptio.png
json_schemas:
- name: CostAllocation
  property_count: 8
  slug: cost-allocation
json_structures:
- name: Cost Allocation Structure
  property_count: 0
  slug: cost-allocation-structure
jsonld:
- class_count: 15
  name: Apptio Context
  property_count: 0
  slug: apptio-context
layout: provider
modified: '2026-04-19'
name: Apptio
nav: Providers
network: true
overview: 'Apptio publishes 3 APIs on the [APIs.io](https://apis.io/) network: Budgets API, Cost Allocations API, and Reports API. Tagged areas include Analytics, Cost Management, IT Finance, and Technology Business Management.


  The Apptio catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apptio''s developer surface includes authentication, documentation, engineering blog, signup flow, and 5 more developer resources.'
plans:
- name: Apptio Plans Pricing
  plan_count: 3
  slug: apptio-plans-pricing
random_paper: 83
rate_limits:
- limit_count: 5
  name: Apptio Rate Limits
  slug: apptio-rate-limits
rules:
- name: Apptio API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apptio-jsonschema-spectral-rules
- name: Apptio API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 13
  slug: apptio-spectral-rules
score:
  band: developing
  composite: 49.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 77.5
    developer_ergonomics: 21.7
    discoverability: 55.6
    governance: 58.3
    operational_transparency: 36.8
  previous_composite: 49.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apptio/refs/heads/main/screenshots/apptio-2026-06-20T172335.png
security:
- kind: authentication
  name: Apptio Authentication
  slug: apptio-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apptio Domain Security
  slug: apptio-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: apptio
tags:
- Analytics
- Cost Management
- IT Finance
- Technology Business Management
website: https://www.apptio.com/
---

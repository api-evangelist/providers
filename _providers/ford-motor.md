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
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ford Motor Agentic Access
  operation_count: 1
  slug: ford-motor-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: Automotive operations
  name: ford-motor Automotive API
  slug: ford-motor-automotive-api
artifact_total: 8
collections:
- collection_type: open
  name: Ford Developer API
  slug: open-ford-motor-ford-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/ford-motor-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/ford-motor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/ford-motor-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ford
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ford-motor-company
description: Ford Motor Company is a global automotive manufacturer that designs, manufactures, markets, and services a full line of Ford trucks, cars, sport utility vehicles, electrified vehicles, and Lincoln luxury vehicles.
finops:
- name: Ford Motor Finops
  service_category: Connected Vehicle / Mobility
  slug: ford-motor-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/ford-motor.png
layout: provider
modified: '2026-05-19'
name: ford-motor
nav: Providers
network: true
overview: 'ford-motor publishes 1 API on the [APIs.io](https://apis.io/) network: Automotive API. Tagged areas include Fortune 100.


  ford-motor''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Ford Motor Plans Pricing
  plan_count: 2
  slug: ford-motor-plans-pricing
press:
- date: '2026-05-25'
  title: Ford Establishes New Product Creation and ...
  url: https://www.fromtheroad.ford.com/us/en/articles/2026/ford-establishes-product-creation-industrialization-organization
- date: '2026-05-25'
  title: Car shoppers are becoming increasingly reliant on artificial ...
  url: https://www.facebook.com/jalopnik/posts/car-shoppers-are-becoming-increasingly-reliant-on-artificial-intelligence-ford-p/1300015721982247/
- date: '2026-05-25'
  title: Ford launches Pro AI for multibillion-dollar commercial ...
  url: https://www.cnbc.com/2026/03/10/ford-pro-ai.html
- date: '2026-05-25'
  title: Ford to launch eyes-off driving system in 2028, automaker ...
  url: https://www.autonews.com/ford/an-ces-2026-ford-doug-field-panel-0107/
- date: '2026-05-25'
  title: 'Ford''s Simple Vision for Smart Tech: Make It for Everyone'
  url: https://www.fromtheroad.ford.com/us/en/articles/2026/ford-affordable-smart-vehicle-technology-strategy
random_paper: 16
rate_limits:
- limit_count: 2
  name: Ford Motor Rate Limits
  slug: ford-motor-rate-limits
score:
  band: thin
  composite: 33.0
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 65.1
    developer_ergonomics: 10.9
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 33.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/ford-motor/refs/heads/main/screenshots/ford-motor-2026-06-20T181422.png
security:
- kind: authentication
  name: Ford Motor Authentication
  slug: ford-motor-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Ford Motor Domain Security
  slug: ford-motor-domain-security
  summary_line: DMARC
slug: ford-motor
tags:
- Fortune 100
---

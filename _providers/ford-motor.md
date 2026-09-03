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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.9
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Ford Motor Agentic Access
  operation_count: 1
  slug: ford-motor-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- baseURL: https://api.ford.com
  baseurl_source: declared
  description: Automotive operations
  name: ford-motor Automotive API
  slug: ford-motor-automotive-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Ford Developer Automotive API
  slug: open-ford-motor-automotive-api
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
name: Ford Motor Company
nav: Providers
network: true
overview: 'Ford Motor Company publishes 1 API on the [APIs.io](https://apis.io/) network: ford-motor Automotive API. Tagged areas include Fortune 100.


  Ford Motor Company''s developer surface includes authentication and 4 more developer resources.'
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
random_paper: 4
rate_limits:
- limit_count: 2
  name: Ford Motor Rate Limits
  slug: ford-motor-rate-limits
score:
  band: thin
  composite: 26.7
  coverage:
    artifact_dirs: 12
    catalog_gap: 79.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 53.7
    developer_ergonomics: 21.4
    discoverability: 53.7
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 26.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
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

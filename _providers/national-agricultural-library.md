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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: National Agricultural Library Agentic Access
  operation_count: 9
  slug: national-agricultural-library-agentic-access
  summary_line: 9 operations · 3 acting
api_count: 1
apis:
- description: endpoints to retrieve nutrient data
  name: National Agricultural Library FDC API
  slug: national-agricultural-library-fdc-api
artifact_total: 8
collections:
- collection_type: open
  name: Food Data Central API
  slug: open-national-agricultural-library
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/national-agricultural-library-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/national-agricultural-library-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/national-agricultural-library-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/national-agricultural-library
- group: company
  title: ''
  type: Website
  url: https://www.nal.usda.gov/
- group: start
  title: ''
  type: Portal
  url: https://fdc.nal.usda.gov/
created: '2024-11-21'
description: The USDA National Agricultural Library houses one of the world's largest collections devoted to agriculture and its related sciences, and operates FoodData Central, an integrated data system providing nutrient profiles for foods.
finops:
- name: National Agricultural Library Finops
  service_category: API
  slug: national-agricultural-library-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/national-agricultural-library.png
layout: provider
modified: '2026-05-19'
name: National Agricultural Library
nav: Providers
network: true
overview: 'National Agricultural Library publishes 1 API on the [APIs.io](https://apis.io/) network: FDC API. Tagged areas include Agriculture, Federal Government, Library, Food, and Nutrition.


  National Agricultural Library''s developer surface includes authentication, developer portal, and 4 more developer resources.'
plans:
- name: National Agricultural Library Plans Pricing
  plan_count: 3
  slug: national-agricultural-library-plans-pricing
random_paper: 38
rate_limits:
- limit_count: 5
  name: National Agricultural Library Rate Limits
  slug: national-agricultural-library-rate-limits
score:
  band: thin
  composite: 35.4
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 54.0
    developer_ergonomics: 19.6
    discoverability: 60.0
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 35.4
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/national-agricultural-library/refs/heads/main/screenshots/national-agricultural-library-2026-06-20T185959.png
security:
- kind: authentication
  name: National Agricultural Library Authentication
  slug: national-agricultural-library-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: National Agricultural Library Domain Security
  slug: national-agricultural-library-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: national-agricultural-library
tags:
- Agriculture
- Federal Government
- Library
- Food
- Nutrition
website: https://www.nal.usda.gov/
---

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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Foreign Agricultural Service Agentic Access
  operation_count: 35
  slug: foreign-agricultural-service-agentic-access
  summary_line: 35 operations
api_count: 4
apis:
- description: The USDA Foreign Agricultural Service Open Data API provides programmatic access to U.S. agricultural trade data, including the Global Agricultural Trade System (GATS), Export Sales Reporting (ESR), a
  name: USDA FAS Open Data API
  slug: fas-open-data
- description: U.S. Weekly Export Sales of Agricultural Commodity Data
  name: Foreign Agricultural Service ESR API
  slug: foreign-agricultural-service-esr-api
- description: Global Agricultural Trade System
  name: Foreign Agricultural Service GATS API
  slug: foreign-agricultural-service-gats-api
- description: Production, Supply and Distribution
  name: Foreign Agricultural Service PSD API
  slug: foreign-agricultural-service-psd-api
artifact_total: 11
collections:
- collection_type: open
  name: USDA FAS Open Data Services
  slug: open-foreign-agricultural-service
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/foreign-agricultural-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/foreign-agricultural-service-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/foreign-agricultural-service-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-foreign-agricultural-service
- group: company
  title: ''
  type: Website
  url: https://www.fas.usda.gov/
created: '2024-12-25'
description: The Foreign Agricultural Service (FAS) is a branch of the United States Department of Agriculture (USDA) that works to promote U.S. agricultural exports and expand global markets for American agricultural products.
finops:
- name: Foreign Agricultural Service Finops
  service_category: API
  slug: foreign-agricultural-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/foreign-agricultural-service.png
layout: provider
modified: '2026-04-28'
name: Foreign Agricultural Service
nav: Providers
network: true
overview: 'Foreign Agricultural Service publishes 3 APIs on the [APIs.io](https://apis.io/) network: ESR API, GATS API, and PSD API. Tagged areas include Agriculture and Federal Government.


  Foreign Agricultural Service''s developer surface includes authentication and 4 more developer resources.'
plans:
- name: Foreign Agricultural Service Plans Pricing
  plan_count: 3
  slug: foreign-agricultural-service-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Foreign Agricultural Service Rate Limits
  slug: foreign-agricultural-service-rate-limits
score:
  band: emerging
  composite: 24.6
  delta: 0.0
  facets:
    commercial_clarity: 15.8
    contract_quality: 52.2
    developer_ergonomics: 10.9
    discoverability: 55.6
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 24.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 22.2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/foreign-agricultural-service/refs/heads/main/screenshots/foreign-agricultural-service-2026-06-20T181418.png
security:
- kind: authentication
  name: Foreign Agricultural Service Authentication
  slug: foreign-agricultural-service-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Foreign Agricultural Service Domain Security
  slug: foreign-agricultural-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: foreign-agricultural-service
tags:
- Agriculture
- Federal Government
website: https://www.fas.usda.gov/
---

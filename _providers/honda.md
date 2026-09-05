---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Honda's customer satisfaction API includes roadside assistance, maintenance programs, and vehicle-service contracts for customers and dealers.
  name: Honda Customer Satisfaction API
  slug: honda-customer-satisfaction-api
- description: Honda Rating Services Web API for vehicle rating and pricing data.
  name: Honda Rating Service API
  slug: honda-rating-service-api
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/honda-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/honda
- group: company
  title: ''
  type: Website
  url: https://www.honda.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.honda.com/
created: '2025-02-25'
description: Honda Motor Co., Ltd. is a Japanese multinational manufacturer known for automobiles, motorcycles, and power equipment. Honda provides APIs for customer satisfaction programs, roadside assistance, vehicle services, and dealer integration.
finops:
- name: Honda Finops
  service_category: API
  slug: honda-finops
graphqls:
- description: This document describes a conceptual GraphQL schema for Honda Motor Company's connected car and API services. Honda provides vehicle data, remote control, navigation, diagnostics, maintenance, and dea
  name: Honda Motor GraphQL Schema
  slug: honda-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/honda.png
layout: provider
modified: '2026-04-28'
name: Honda
nav: Providers
network: true
overview: Honda publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Automobiles, Automotive, Cars, and Vehicles.
plans:
- name: Honda Plans Pricing
  plan_count: 3
  slug: honda-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Honda Rate Limits
  slug: honda-rate-limits
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 36.0
    catalog_earned_first_party: 0.0
    catalog_gap: 79.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 37.2
    developer_ergonomics: 14.3
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 21.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/honda/refs/heads/main/screenshots/honda-2026-06-20T182819.png
security:
- kind: domain-security
  name: Honda Domain Security
  slug: honda-domain-security
  summary_line: TLSv1.3
slug: honda
tags:
- Automobiles
- Automotive
- Cars
- Vehicles
website: https://www.honda.com/
---

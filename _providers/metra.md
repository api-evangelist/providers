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
  band: human-only
  dimensions:
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 6.7
  scored_at: '2026-07-23'
api_count: 1
apis:
- description: 'The Metra GTFS API provides both raw data and JSON for Metra commuter rail schedules, trips, stops, and real-time transit information. Developers must redistribute data through their own host and not '
  name: Metra GTFS API
  slug: metra-gtfs-api
artifact_total: 5
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/metra-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/metra
- group: start
  title: ''
  type: Portal
  url: https://metra.com/metra-gtfs-api
- group: company
  title: ''
  type: Website
  url: https://www.metrarail.com/
created: '2025-02-06'
description: Metra provides GTFS API data for the Metra commuter rail system in the Chicago metropolitan area. The API is hosted at gtfsapi.metrarail.com and provides both RAW data and JSON for schedules, trips, stops, and real-time updates.
finops:
- name: Metra Finops
  service_category: API
  slug: metra-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/metra.png
layout: provider
modified: '2026-04-28'
name: Metra
nav: Providers
network: true
overview: 'Metra publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Chicago, Commuter Rail, GTFS, Public Transportation, and Transit.


  Metra''s developer surface includes developer portal and 3 more developer resources.'
plans:
- name: Metra Plans Pricing
  plan_count: 3
  slug: metra-plans-pricing
random_paper: 27
rate_limits:
- limit_count: 5
  name: Metra Rate Limits
  slug: metra-rate-limits
score:
  band: emerging
  composite: 23.0
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 92.5
    governance: 0.0
    operational_transparency: 31.6
  previous_composite: 23.0
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
security:
- kind: domain-security
  name: Metra Domain Security
  slug: metra-domain-security
  summary_line: TLSv1.3 · DMARC
slug: metra
tags:
- Chicago
- Commuter Rail
- GTFS
- Public Transportation
- Transit
website: https://www.metrarail.com/
---

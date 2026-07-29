---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Public Apis Agentic Access
  operation_count: 4
  slug: public-apis-agentic-access
  summary_line: 4 operations
api_count: 4
apis:
- description: A collective list of free APIs organized by category including Animals, Finance, Weather, Geocoding, Government, Health, Machine Learning, Sports, and 40+ more categories for developers to discover an
  name: Public APIs Directory
  slug: public-apis-directory
- description: Endpoints for category metadata.
  name: Public APIs Categories API
  slug: public-apis-categories-api
- description: Endpoints for listing API directory entries.
  name: Public APIs Entries API
  slug: public-apis-entries-api
- description: Service health check.
  name: Public APIs Health API
  slug: public-apis-health-api
artifact_total: 9
collections:
- collection_type: open
  name: Public APIs API
  slug: open-public-apis
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/public-apis-agentic-access.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/public-apis/public-apis
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/public-apis
- group: docs
  title: ''
  type: Contributing Guide
  url: https://github.com/public-apis/public-apis/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/public-apis/public-apis/blob/master/LICENSE
created: '2026-03-26'
description: Public APIs is a community-curated collective list of over 1,400 free APIs organized across 50+ categories, maintained by contributors and the team at APILayer. It is one of the most popular open-source projects on GitHub with over 400k stars. A companion REST API (davemachado/public-api) exposes the directory data programmatically over HTTPS with no authentication.
finops:
- name: Public Apis Finops
  service_category: API
  slug: public-apis-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/public-apis.png
layout: provider
modified: '2026-05-19'
name: Public APIs
nav: Providers
network: true
overview: 'Public APIs publishes 3 APIs on the [APIs.io](https://apis.io/) network: Categories API, Entries API, and Health API. Tagged areas include API Aggregation, API Directory, API Discovery, Free APIs, and Open Source.'
plans:
- name: Public Apis Plans Pricing
  plan_count: 3
  slug: public-apis-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Public Apis Rate Limits
  slug: public-apis-rate-limits
score:
  band: thin
  composite: 31.9
  delta: -1.7
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.8
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 33.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/public-apis/refs/heads/main/screenshots/public-apis-2026-06-20T192252.png
slug: public-apis
tags:
- API Aggregation
- API Directory
- API Discovery
- Free APIs
- Open Source
---

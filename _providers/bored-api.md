---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.1
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Bored Api Agentic Access
  operation_count: 3
  slug: bored-api-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- description: Operations for discovering and retrieving activities
  name: Bored API Activities API
  slug: bored-api-activities-api
artifact_total: 10
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/bored-api-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/bored-api-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bored-api.appbrewery.com/
- group: docs
  title: ''
  type: Documentation
  url: https://bored-api.appbrewery.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/drewthoennes/Bored-API
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/school/the-app-brewery/
- group: company
  title: ''
  type: Blog
  url: https://appbrewery.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://bored-api.appbrewery.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://bored-api.appbrewery.com/
- group: other
  title: ''
  type: X
  url: https://x.com/appbrewery
- group: commercial
  title: ''
  type: Plans
  url: plans/bored-api-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/bored-api-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/bored-api-finops.yml
created: '2026-06-13'
description: Free REST API that suggests random activities to do when bored, filterable by type, number of participants, price range, and accessibility. A teaching tool by The App Brewery with no authentication required.
examples:
- key_count: 10
  name: Random Activity Response
  slug: random-activity-response
finops:
- name: Bored Api Finops
  service_category: ''
  slug: bored-api-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bored-api.png
json_schemas:
- name: Activity
  property_count: 10
  slug: activity
jsonld:
- class_count: 1
  name: Bored Api Context
  property_count: 10
  slug: bored-api-context
layout: provider
modified: '2026-06-13'
name: Bored API
nav: Providers
network: true
overview: 'Bored API publishes 1 API on the [APIs.io](https://apis.io/) network: Activities API. Tagged areas include Activities, Boredom, Random, Entertainment, and Lifestyle.


  The Bored API catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Bored API''s developer surface includes documentation, engineering blog, pricing, and 10 more developer resources.'
plans:
- name: Bored Api Plans Pricing
  plan_count: 1
  slug: bored-api-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 1
  name: Bored Api Rate Limits
  slug: bored-api-rate-limits
rules:
- name: Bored API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: bored-api-jsonschema-spectral-rules
score:
  band: developing
  composite: 45.6
  delta: 0.0
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.9
    developer_ergonomics: 10.9
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 42.1
  previous_composite: 45.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/bored-api/refs/heads/main/screenshots/bored-api-2026-06-20T173608.png
security:
- kind: domain-security
  name: Bored Api Domain Security
  slug: bored-api-domain-security
  summary_line: TLSv1.3
slug: bored-api
tags:
- Activities
- Boredom
- Random
- Entertainment
- Lifestyle
- Free
website: https://bored-api.appbrewery.com/
---

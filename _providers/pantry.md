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
- acting_count: 6
  human_in_the_loop: 0
  name: Pantry Agentic Access
  operation_count: 9
  slug: pantry-agentic-access
  summary_line: 9 operations · 6 acting
api_count: 2
apis:
- description: Baskets are containers of JSON data within a pantry
  name: Pantry Basket API
  slug: pantry-basket-api
- description: Pantry account (account-level operations)
  name: Pantry Pantry API
  slug: pantry-pantry-api
artifact_total: 12
collections:
- collection_type: open
  name: Pantry API
  slug: open-pantry
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pantry-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pantry-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pantry-retail-inc
- group: company
  title: ''
  type: Website
  url: https://getpantry.cloud/
- group: docs
  title: ''
  type: Documentation
  url: https://getpantry.cloud/
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/imRohan/Pantry
created: '2025-02-06'
description: Pantry is a free data storage service for developers that focuses on your development time, letting you build awesome things fast. It provides a simple cloud-based JSON data storage API.
finops:
- name: Pantry Finops
  service_category: API
  slug: pantry-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/pantry.png
json_schemas:
- name: Basket
  property_count: 3
  slug: basket
- name: Pantry
  property_count: 6
  slug: pantry
jsonld:
- class_count: 8
  name: Pantry Context
  property_count: 1
  slug: pantry-context
layout: provider
modified: '2026-05-19'
name: Pantry
nav: Providers
network: true
overview: 'Pantry publishes 2 APIs on the [APIs.io](https://apis.io/) network: Basket API and Pantry API. Tagged areas include Data Storage, Developer Tools, and JSON.


  The Pantry catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Pantry''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Pantry Plans Pricing
  plan_count: 3
  slug: pantry-plans-pricing
press:
- date: '2026-05-25'
  title: Training Gets Real with Artificial Intelligence
  url: https://foodbanknews.org/training-gets-real-with-artificial-intelligence/
- date: '2026-05-25'
  title: Artificial Intelligence in Food Bank and Pantry Services
  url: https://www.mdpi.com/2072-6643/17/9/1461
- date: '2026-05-25'
  title: 'Future-Proofing Your Pantry: How AI Synthesizes Food ...'
  url: https://georgefox.cafebonappetit.com/future-proofing-your-pantry/
- date: '2026-05-25'
  title: Montgomery County Launches Advisory Council on ...
  url: https://www.montgomerycountypa.gov/CivicAlerts.asp?AID=4690
- date: '2026-05-25'
  title: Purdue professor uses AI technology to help food pantries
  url: https://www.purdueexponent.org/city_state/purdue-alex-psomas-indianapolis-artificial-intelligence/article_07b6cdae-a219-11ef-866e-17a294dc19fd.html
random_paper: 38
rate_limits:
- limit_count: 5
  name: Pantry Rate Limits
  slug: pantry-rate-limits
rules:
- name: Pantry API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: pantry-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.9
  delta: -2.9
  facets:
    commercial_clarity: 39.5
    contract_quality: 64.4
    developer_ergonomics: 8.7
    discoverability: 40.7
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 43.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pantry/refs/heads/main/screenshots/pantry-2026-06-20T191358.png
security:
- kind: domain-security
  name: Pantry Domain Security
  slug: pantry-domain-security
  summary_line: TLSv1.3 · DMARC
slug: pantry
tags:
- Data Storage
- Developer Tools
- JSON
website: https://getpantry.cloud/
---

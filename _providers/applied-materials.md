---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
  scored_at: '2026-08-12'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Applied Materials Agentic Access
  operation_count: 4
  slug: applied-materials-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 2
apis:
- description: Semiconductor manufacturing equipment management
  name: Applied Materials Equipment API
  slug: applied-materials-equipment-api
- description: Equipment maintenance scheduling and records
  name: Applied Materials Maintenance API
  slug: applied-materials-maintenance-api
artifact_total: 13
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/applied-materials-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/applied-materials-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/applied-materials
- group: company
  title: ''
  type: Website
  url: https://www.applied-materials.com
description: Applied Materials is a global leader in materials engineering solutions used to produce virtually every new chip and advanced display in the world.
examples:
- key_count: 8
  name: Equipment Example
  slug: equipment-example
finops:
- name: Applied Materials Finops
  service_category: Industrial / Manufacturing
  slug: applied-materials-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/applied-materials.png
json_schemas:
- name: Equipment
  property_count: 8
  slug: equipment
json_structures:
- name: Equipment Structure
  property_count: 0
  slug: equipment-structure
jsonld:
- class_count: 12
  name: Applied Materials Context
  property_count: 0
  slug: applied-materials-context
layout: provider
modified: '2026-04-19'
name: Applied Materials
nav: Providers
network: true
overview: 'Applied Materials publishes 2 APIs on the [APIs.io](https://apis.io/) network: Equipment API and Maintenance API. Tagged areas include Semiconductor, Manufacturing, Equipment, Fab Operations, and Materials Engineering.


  The Applied Materials catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Applied Materials'' developer surface includes authentication and 3 more developer resources.'
plans:
- name: Applied Materials Plans Pricing
  plan_count: 1
  slug: applied-materials-plans-pricing
press:
- date: '2026-05-25'
  title: Applied Materials
  url: https://www.facebook.com/AppliedMaterialsInc/posts/today-applied-materials-announced-a-new-innovation-partnership-with-tsmc-to-acce/1407076051453212/
- date: '2026-05-25'
  title: Applied Materials and Micron Partner To Advance U.S. ...
  url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-and-micron-partner-advance-us-innovation-next
- date: '2026-05-25'
  title: Applied Materials
  url: https://www.appliedmaterials.com/us/en.html
- date: '2026-05-25'
  title: Applied Materials and SK hynix Announce Long-Term R&D ...
  url: https://ir.appliedmaterials.com/news-releases/news-release-details/applied-materials-and-sk-hynix-announce-long-term-rd-partnership
- date: '2026-05-25'
  title: Applied Materials Debuts New Gear For Making AI Chips
  url: https://www.investors.com/news/technology/amat-stock-applied-materials-new-gear-ai-chips/
random_paper: 62
rate_limits:
- limit_count: 1
  name: Applied Materials Rate Limits
  slug: applied-materials-rate-limits
rules:
- name: Applied Materials API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: applied-materials-jsonschema-spectral-rules
- name: Applied Materials API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 14
  slug: applied-materials-spectral-rules
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 13.2
    contract_quality: 74.6
    developer_ergonomics: 10.9
    discoverability: 44.4
    governance: 58.3
    operational_transparency: 5.3
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.11.0
  scored_at: '2026-08-12'
  trend: flat
security:
- kind: authentication
  name: Applied Materials Authentication
  slug: applied-materials-authentication
  summary_line: http · 1 scheme
slug: applied-materials
tags:
- Semiconductor
- Manufacturing
- Equipment
- Fab Operations
- Materials Engineering
- Fortune 500
website: https://www.applied-materials.com
---

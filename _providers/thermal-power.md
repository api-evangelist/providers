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
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Thermal Power Agentic Access
  operation_count: 4
  slug: thermal-power-agentic-access
  summary_line: 4 operations
api_count: 3
apis:
- description: Generating capacity and generator-level data.
  name: Thermal Power Capacity API
  slug: thermal-power-capacity-api
- description: Plant-level thermal generation operational data.
  name: Thermal Power Plant Operations API
  slug: thermal-power-plant-operations-api
- description: Electric power operational statistics by fuel type.
  name: Thermal Power Power Operations API
  slug: thermal-power-power-operations-api
artifact_total: 17
collections:
- collection_type: open
  name: Thermal Power API
  slug: open-thermal-power
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/thermal-power-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/thermal-power-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/thermal-power-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.eia.gov/opendata/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/opendata/documentation.php
- group: start
  title: ''
  type: Signup
  url: https://www.eia.gov/opendata/register.php
- group: other
  title: ''
  type: Explorer
  url: https://www.eia.gov/opendata/browser/
- group: docs
  title: ''
  type: Documentation
  url: https://www.eia.gov/developer/
created: '2026-03-16'
description: Thermal power generation data APIs providing access to plant-level operational metrics, fuel consumption, heat rates, and generating capacity for coal, natural gas, petroleum, and nuclear power plants in the United States. Primary data source is the U.S. Energy Information Administration (EIA) Open Data API.
examples:
- key_count: 2
  name: Thermal Power Get Electric Power Operational Data Example
  slug: thermal-power-get-electric-power-operational-data-example
- key_count: 2
  name: Thermal Power Get Facility Fuel Data Example
  slug: thermal-power-get-facility-fuel-data-example
finops:
- name: Thermal Power Finops
  service_category: API
  slug: thermal-power-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/thermal-power.png
json_schemas:
- name: Thermal Power Plant Record
  property_count: 13
  slug: thermal-power-plant
json_structures:
- name: Thermal Power Structure
  property_count: 0
  slug: thermal-power-structure
jsonld:
- class_count: 0
  name: Thermal Power Context
  property_count: 3
  slug: thermal-power-context
layout: provider
modified: '2026-05-19'
name: Thermal Power
nav: Providers
network: true
overview: 'Thermal Power publishes 3 APIs on the [APIs.io](https://apis.io/) network: Capacity API, Plant Operations API, and Power Operations API. Tagged areas include Energy, Thermal Power, Power Generation, Electricity, and Coal.


  The Thermal Power catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Thermal Power''s developer surface includes authentication, documentation, signup flow, and 5 more developer resources.'
plans:
- name: Thermal Power Plans Pricing
  plan_count: 3
  slug: thermal-power-plans-pricing
random_paper: 59
rate_limits:
- limit_count: 5
  name: Thermal Power Rate Limits
  slug: thermal-power-rate-limits
rules:
- name: Thermal Power API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: thermal-power-jsonschema-spectral-rules
- name: Thermal Power API Rules
  rule_count: 8
  severity_counts:
    error: 3
    hint: 0
    info: 1
    warn: 4
  slug: thermal-power-rules
score:
  band: developing
  composite: 52.2
  delta: 4.5
  facets:
    commercial_clarity: 39.5
    contract_quality: 69.9
    developer_ergonomics: 19.6
    discoverability: 100.0
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 47.7
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/thermal-power/refs/heads/main/screenshots/thermal-power-2026-06-20T195251.png
security:
- kind: authentication
  name: Thermal Power Authentication
  slug: thermal-power-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Thermal Power Domain Security
  slug: thermal-power-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: thermal-power
tags:
- Energy
- Thermal Power
- Power Generation
- Electricity
- Coal
- Natural Gas
- Nuclear
website: https://www.eia.gov/opendata/
---

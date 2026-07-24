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
api_count: 2
apis:
- description: The Air Force OPEN Data Program provides public access to Department of the Air Force datasets, covering military installations, personnel data, research findings, and operational information. The pro
  name: US Air Force Open Data
  slug: us-air-force-open-data
- description: The Department of the Air Force API program provides a strategic framework for standardized APIs across the DAF enterprise. The DAF API Roadmap 2.0 and API Reference Architecture 2.0 guide the impleme
  name: US Air Force DAF API Program
  slug: us-air-force-developer-api
artifact_total: 11
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-air-force-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-states-air-force
created: '2024-11-21'
description: The United States Air Force is responsible for providing air and space power to protect the United States and its interests. As part of the Department of the Air Force, the USAF has adopted an API-first architecture strategy to improve data sharing, software interoperability, and integration across military systems. The DAF publishes open datasets through data.af.mil and provides developer resources through software.af.mil.
examples:
- key_count: 16
  name: Us Air Force Open Data Dataset Example
  slug: us-air-force-open-data-dataset-example
finops:
- name: Us Air Force Finops
  service_category: API
  slug: us-air-force-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-air-force.png
json_schemas:
- name: Air Force Open Dataset
  property_count: 15
  slug: us-air-force-dataset
json_structures:
- name: Us Air Force Dataset Structure
  property_count: 0
  slug: us-air-force-dataset-structure
jsonld:
- class_count: 32
  name: Us Air Force Context
  property_count: 2
  slug: us-air-force-context
layout: provider
modified: '2026-05-03'
name: US Air Force
nav: Providers
network: true
overview: 'US Air Force publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Air Force, Federal Government, Military, Defense, and Open Data.


  The US Air Force catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Us Air Force Plans Pricing
  plan_count: 3
  slug: us-air-force-plans-pricing
random_paper: 43
rate_limits:
- limit_count: 5
  name: Us Air Force Rate Limits
  slug: us-air-force-rate-limits
rules:
- name: US Air Force API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-air-force-jsonschema-spectral-rules
score:
  band: thin
  composite: 33.7
  delta: -1.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 26.4
    developer_ergonomics: 0.0
    discoverability: 80.0
    governance: 73.7
    operational_transparency: 31.6
  previous_composite: 35.5
  regulatory:
    applies: true
    regime: Government & Public Sector
    regime_id: government
    score: 23.9
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-air-force/refs/heads/main/screenshots/us-air-force-2026-06-20T200539.png
security:
- kind: domain-security
  name: Us Air Force Domain Security
  slug: us-air-force-domain-security
  summary_line: DNSSEC · DMARC
slug: us-air-force
tags:
- Air Force
- Federal Government
- Military
- Defense
- Open Data
- Government API
---

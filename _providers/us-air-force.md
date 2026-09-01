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
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-01'
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
overview: 'US Air Force publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Air Force, Federal-Government, Military, Defense, and Open Data.


  The US Air Force catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Us Air Force Plans Pricing
  plan_count: 3
  slug: us-air-force-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Us Air Force Rate Limits
  slug: us-air-force-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Air Force API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-air-force-jsonschema-spectral-rules
score:
  band: emerging
  composite: 21.9
  coverage:
    artifact_dirs: 12
    catalog_gap: 56.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 9.8
    contract_quality: 25.3
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 9.8
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: no_resolvable_host
  previous_composite: 21.9
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.17.2
  scored_at: '2026-09-01'
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
- Federal-Government
- Military
- Defense
- Open Data
- Government API
---

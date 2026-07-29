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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 1
apis:
- description: The CSB does not currently offer a formal public API. However, it maintains public databases of investigations, recommendations, and incident reports accessible through its website. The CSB releases p
  name: US Chemical Safety and Hazard Investigation Board
  slug: us-chemical-safety-and-hazard-investigation-board
artifact_total: 9
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-chemical-safety-and-hazard-investigation-board-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-states-chemical-safety-and-hazard-investigation-board
created: '2024-12-03'
description: The US Chemical Safety and Hazard Investigation Board (CSB) is an independent federal agency responsible for investigating chemical accidents and hazards across the United States. The board conducts thorough investigations into incidents involving the release of hazardous chemicals, explosions, fires, and other accidents that pose a threat to public safety and the environment. The CSB publishes investigation reports, safety recommendations, and incident data, and maintains a public database of completed investigations and safety recommendations. While no formal public API is available, the CSB makes incident data available through its website and periodic compiled reports under its Accidental Release Reporting Rule transparency initiative.
finops:
- name: Us Chemical Safety And Hazard Investigation Board Finops
  service_category: API
  slug: us-chemical-safety-and-hazard-investigation-board-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-chemical-safety-and-hazard-investigation-board.png
json_schemas:
- name: CSB Chemical Incident
  property_count: 15
  slug: csb-incident
json_structures:
- name: Csb Incident Structure
  property_count: 0
  slug: csb-incident-structure
jsonld:
- class_count: 2
  name: Us Chemical Safety And Hazard Investigation Board Context
  property_count: 34
  slug: us-chemical-safety-and-hazard-investigation-board-context
layout: provider
modified: '2026-05-03'
name: US Chemical Safety and Hazard Investigation Board
nav: Providers
network: true
overview: 'US Chemical Safety and Hazard Investigation Board publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Federal Government, Chemical Safety, Incident Investigation, Hazardous Materials, and Public Safety.


  The US Chemical Safety and Hazard Investigation Board catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.'
plans:
- name: Us Chemical Safety And Hazard Investigation Board Plans Pricing
  plan_count: 3
  slug: us-chemical-safety-and-hazard-investigation-board-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 5
  name: Us Chemical Safety And Hazard Investigation Board Rate Limits
  slug: us-chemical-safety-and-hazard-investigation-board-rate-limits
rules:
- name: US Chemical Safety and Hazard Investigation Board API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: us-chemical-safety-and-hazard-investigation-board-jsonschema-spectral-rules
score:
  band: thin
  composite: 28.2
  delta: -4.4
  facets:
    commercial_clarity: 39.5
    contract_quality: 12.9
    developer_ergonomics: 0.0
    discoverability: 59.3
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 32.6
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/us-chemical-safety-and-hazard-investigation-board/refs/heads/main/screenshots/us-chemical-safety-and-hazard-investigation-board-2026-06-20T200606.png
security:
- kind: domain-security
  name: Us Chemical Safety And Hazard Investigation Board Domain Security
  slug: us-chemical-safety-and-hazard-investigation-board-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: us-chemical-safety-and-hazard-investigation-board
tags:
- Federal Government
- Chemical Safety
- Incident Investigation
- Hazardous Materials
- Public Safety
- Environmental Safety
---

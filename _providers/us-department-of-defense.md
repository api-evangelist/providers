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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: na
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 24.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Us Department Of Defense Agentic Access
  operation_count: 16
  slug: us-department-of-defense-agentic-access
  summary_line: 16 operations
api_count: 11
apis:
- description: The USACE Lock Performance Monitoring System (LPMS) API provides data on inland waterway lock operations across the US Army Corps of Engineers lock system. Endpoints return XML data for lock queue rep
  name: USACE Lock Performance Monitoring System API
  slug: lpms-api
- description: The Department of Defense Data Portal features APIs enabling access to DoD open data across military branches, agencies, and programs. The portal surfaces selected APIs from the DoD's data strategy in
  name: DoD Data Portal
  slug: defense-data-gov
- description: The Department of Defense Open Data Platform (data.mil) provides access to unclassified DoD datasets and data services supporting defense research, policy analysis, and public accountability.
  name: DoD Open Data Platform
  slug: dod-open-data
- description: Data catalog and discovery
  name: US Department of Defense Catalog API
  slug: us-department-of-defense-catalog-api
- description: Location levels and pool data
  name: US Department of Defense Levels API
  slug: us-department-of-defense-levels-api
- description: CWMS monitoring locations and metadata
  name: US Department of Defense Locations API
  slug: us-department-of-defense-locations-api
- description: Field measurements and observations
  name: US Department of Defense Measurements API
  slug: us-department-of-defense-measurements-api
- description: USACE district offices
  name: US Department of Defense Offices API
  slug: us-department-of-defense-offices-api
- description: USACE projects and reservoirs
  name: US Department of Defense Projects API
  slug: us-department-of-defense-projects-api
- description: Rating curves and tables
  name: US Department of Defense Ratings API
  slug: us-department-of-defense-ratings-api
- description: Time series data retrieval and management
  name: US Department of Defense Time Series API
  slug: us-department-of-defense-time-series-api
artifact_total: 32
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: USACE Corps Water Management System Data Catalog API
  slug: open-us-department-of-defense-catalog-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Levels API
  slug: open-us-department-of-defense-levels-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Locations API
  slug: open-us-department-of-defense-locations-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Measurements API
  slug: open-us-department-of-defense-measurements-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Offices API
  slug: open-us-department-of-defense-offices-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Projects API
  slug: open-us-department-of-defense-projects-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Ratings API
  slug: open-us-department-of-defense-ratings-api
- collection_type: open
  name: USACE Corps Water Management System Data Catalog Time Series API
  slug: open-us-department-of-defense-time-series-api
- collection_type: open
  name: USACE Corps Water Management System Data API
  slug: open-usace-cwms-data-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/us-department-of-defense-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/us-department-of-defense-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/united-states-department-of-defense
created: '2024-12-03'
description: The US Department of Defense is responsible for providing the military forces needed to deter war and protect the security of the United States. This includes overseeing the Army, Navy, Marine Corps, and Air Force, as well as coordinating with other defense agencies and organizations. The Department of Defense also plays a critical role in developing military strategies, acquiring and maintaining weapons and equipment, and ensuring the readiness and effectiveness of the armed forces. The DoD's data strategy initiatives have led to the publication of multiple public APIs including the USACE Corps Water Management System API, Lock Performance Monitoring System, and the DoD open data portal.
examples:
- key_count: 3
  name: Usace Cwms Get Timeseries Example
  slug: usace-cwms-get-timeseries-example
finops:
- name: Us Department Of Defense Finops
  service_category: API
  slug: us-department-of-defense-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/us-department-of-defense.png
json_schemas:
- name: USACE CWMS Time Series Response
  property_count: 10
  slug: usace-cwms-timeseries
json_structures:
- name: Usace Cwms Timeseries Structure
  property_count: 0
  slug: usace-cwms-timeseries-structure
jsonld:
- class_count: 22
  name: Us Department Of Defense Context
  property_count: 2
  slug: us-department-of-defense-context
layout: provider
modified: '2026-05-19'
name: US Department of Defense
nav: Providers
network: true
overview: 'US Department of Defense publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Catalog API, Levels API, Locations API, and 5 more. Tagged areas include Federal Government, Defense, Military, Water Management, and Waterways.


  The US Department of Defense catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Us Department Of Defense Plans Pricing
  plan_count: 3
  slug: us-department-of-defense-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Us Department Of Defense Rate Limits
  slug: us-department-of-defense-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: US Department of Defense API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: us-department-of-defense-jsonschema-spectral-rules
- effective_rule_count: 51
  extends:
  - spectral:oas
  name: US Department of Defense API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 6
  slug: usace-cwms-data-api-rules
score:
  band: emerging
  composite: 22.5
  delta: -8.3
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 9.8
    contract_quality: 55.9
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 9.8
    operational_transparency: 7.9
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/us-department-of-defense/refs/heads/main/screenshots/us-department-of-defense-2026-06-20T200627.png
security:
- kind: domain-security
  name: Us Department Of Defense Domain Security
  slug: us-department-of-defense-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: us-department-of-defense
tags:
- Federal Government
- Defense
- Military
- Water Management
- Waterways
- Open Data
---

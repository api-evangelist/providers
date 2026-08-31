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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Food Safety And Inspection Service Agentic Access
  operation_count: 1
  slug: food-safety-and-inspection-service-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: FSIS recall and public health alert records.
  name: Food Safety and Inspection Service Recalls API
  slug: food-safety-and-inspection-service-recalls-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: FSIS Recall Recalls API
  slug: open-food-safety-and-inspection-service-recalls-api
- collection_type: open
  name: FSIS Recall API
  slug: open-fsis-recall
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/food-safety-and-inspection-service-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/food-safety-and-inspection-service-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usda-fsis
- group: company
  title: ''
  type: Website
  url: https://www.fsis.usda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fsis.usda.gov/science-data/developer-resources/recall-api
- group: other
  title: ''
  type: Recalls
  url: https://www.fsis.usda.gov/recalls
created: '2024-12-03'
description: The Food Safety and Inspection Service (FSIS) is a branch of the United States Department of Agriculture (USDA) responsible for ensuring the safety of the nation's commercial supply of meat, poultry, and egg products. FSIS publishes a Recall API that provides machine-readable access to recall and public health alert records.
finops:
- name: Food Safety And Inspection Service Finops
  service_category: API
  slug: food-safety-and-inspection-service-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/food-safety-and-inspection-service.png
layout: provider
modified: '2026-05-19'
name: Food Safety and Inspection Service
nav: Providers
network: true
overview: 'Food Safety and Inspection Service publishes 1 API on the [APIs.io](https://apis.io/) network: Recalls API. Tagged areas include Federal-Government, Food, Food Safety, Inspections, and Recalls.


  The Food Safety and Inspection Service catalog on APIs.io includes 1 Spectral governance ruleset.


  Food Safety and Inspection Service''s developer surface includes documentation and 5 more developer resources.'
plans:
- name: Food Safety And Inspection Service Plans Pricing
  plan_count: 3
  slug: food-safety-and-inspection-service-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 5
  name: Food Safety And Inspection Service Rate Limits
  slug: food-safety-and-inspection-service-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Food Safety and Inspection Service API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: fsis-recall-rules
score:
  band: emerging
  composite: 20.9
  coverage:
    artifact_dirs: 9
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 51.0
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 7.9
  previous_composite: 20.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/food-safety-and-inspection-service/refs/heads/main/screenshots/food-safety-and-inspection-service-2026-06-20T181357.png
security:
- kind: domain-security
  name: Food Safety And Inspection Service Domain Security
  slug: food-safety-and-inspection-service-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: food-safety-and-inspection-service
tags:
- Federal-Government
- Food
- Food Safety
- Inspections
- Recalls
- Meat
- Poultry
- Eggs
website: https://www.fsis.usda.gov/
---

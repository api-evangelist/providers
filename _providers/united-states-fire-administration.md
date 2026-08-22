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
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 31.6
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: United States Fire Administration Agentic Access
  operation_count: 4
  slug: united-states-fire-administration-agentic-access
  summary_line: 4 operations
api_count: 2
apis:
- description: OpenFEMA dataset metadata
  name: United States Fire Administration Datasets API
  slug: united-states-fire-administration-datasets-api
- description: FEMA disaster declaration data
  name: United States Fire Administration Disaster Declarations API
  slug: united-states-fire-administration-disaster-declarations-api
artifact_total: 19
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFEMA Fire Data API
  slug: open-openfema-fire-data
- collection_type: open
  name: OpenFEMA Fire Data Datasets API
  slug: open-united-states-fire-administration-datasets-api
- collection_type: open
  name: OpenFEMA Fire Data Datasets Disaster Declarations API
  slug: open-united-states-fire-administration-disaster-declarations-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/united-states-fire-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/united-states-fire-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/usfire
created: '2024-12-03'
description: The United States Fire Administration (USFA) is a government agency under the Federal Emergency Management Agency (FEMA) that is responsible for providing leadership and support to fire departments across the country. The USFA works to improve fire prevention and safety by disseminating training and education programs, conducting research on fire-related issues, and developing national fire prevention initiatives. USFA manages the National Fire Incident Reporting System (NFIRS) and the National Fire Academy (NFA). Fire incident data is accessible through the OpenFEMA API platform at www.fema.gov/api/open.
examples:
- key_count: 3
  name: Openfema Get Disaster Declarations Example
  slug: openfema-get-disaster-declarations-example
- key_count: 3
  name: Openfema List Datasets Example
  slug: openfema-list-datasets-example
finops:
- name: United States Fire Administration Finops
  service_category: API
  slug: united-states-fire-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/united-states-fire-administration.png
json_schemas:
- name: FEMA Disaster Declaration
  property_count: 12
  slug: usfa-disaster-declaration
- name: NFIRS Fire Incident
  property_count: 25
  slug: usfa-nfirs-incident
json_structures:
- name: Usfa Disaster Declaration Structure
  property_count: 0
  slug: usfa-disaster-declaration-structure
jsonld:
- class_count: 3
  name: United States Fire Administration Context
  property_count: 13
  slug: united-states-fire-administration-context
layout: provider
modified: '2026-05-19'
name: United States Fire Administration
nav: Providers
network: true
overview: 'United States Fire Administration publishes 2 APIs on the [APIs.io](https://apis.io/) network: Datasets API and Disaster Declarations API. Tagged areas include Federal Government, Fire Safety, Emergency Management, Public Safety, and FEMA.


  The United States Fire Administration catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: United States Fire Administration Plans Pricing
  plan_count: 3
  slug: united-states-fire-administration-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: United States Fire Administration Rate Limits
  slug: united-states-fire-administration-rate-limits
rules:
- effective_rule_count: 7
  extends: []
  name: United States Fire Administration API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: openfema-fire-data-rules
- effective_rule_count: 5
  extends: []
  name: United States Fire Administration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-fire-administration-jsonschema-spectral-rules
score:
  band: emerging
  composite: 25.8
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 30.3
    contract_quality: 58.0
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 30.3
    operational_transparency: 7.9
  previous_composite: 27.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 20.4
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/united-states-fire-administration/refs/heads/main/screenshots/united-states-fire-administration-2026-06-20T200055.png
security:
- kind: domain-security
  name: United States Fire Administration Domain Security
  slug: united-states-fire-administration-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: united-states-fire-administration
tags:
- Federal Government
- Fire Safety
- Emergency Management
- Public Safety
- FEMA
---

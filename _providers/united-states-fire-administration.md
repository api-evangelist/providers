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
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 38.5
  scored_at: '2026-07-27'
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
artifact_total: 16
collections:
- collection_type: open
  name: OpenFEMA Fire Data API
  slug: open-openfema-fire-data
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
random_paper: 44
rate_limits:
- limit_count: 5
  name: United States Fire Administration Rate Limits
  slug: united-states-fire-administration-rate-limits
rules:
- name: United States Fire Administration API Rules
  rule_count: 7
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 5
  slug: openfema-fire-data-rules
- name: United States Fire Administration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: united-states-fire-administration-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.2
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 59.3
    developer_ergonomics: 0.0
    discoverability: 92.5
    governance: 26.3
    operational_transparency: 31.6
  previous_composite: 36.0
  schema_version: 0.5
  scored_at: '2026-07-27'
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

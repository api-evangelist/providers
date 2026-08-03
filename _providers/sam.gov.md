---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Sam.Gov Agentic Access
  operation_count: 3
  slug: sam.gov-agentic-access
  summary_line: 3 operations
api_count: 8
apis:
- description: The Get Opportunities Public API provides all published contract opportunity details based on request parameters. Returns solicitation notices, awards, and pre-solicitations from SAM.gov. Rate limited
  name: SAM.gov Get Opportunities Public API
  slug: get-opportunities-api
- description: 'The Opportunity Management API allows authorized users to programmatically submit, update, and manage contract opportunity notices in SAM.gov. Requires federal government or contractor system account '
  name: SAM.gov Opportunity Management API
  slug: opportunities-management-api
- description: The Entity Management API provides detailed entity (vendor/contractor) information from SAM.gov including registration status, hierarchy, security levels, points of contact, and certifications. Used t
  name: SAM.gov Entity Management API
  slug: entity-management-api
- description: The Federal Hierarchy Public API allows non-federal users to retrieve Federal Organization details down to the office level. Used to look up agency and organizational hierarchy for federal procurement
  name: SAM.gov Federal Hierarchy Public API
  slug: federal-hierarchy-public-api
- description: The Contract Awards API provides access to federal contract award information from SAM.gov, including award details, vendor information, award amounts, and performance period data.
  name: SAM.gov Contract Awards API
  slug: contract-awards-api
- description: City lookup and validation
  name: SAM.gov Cities API
  slug: sam.gov-cities-api
- description: State and province lookup
  name: SAM.gov States API
  slug: sam.gov-states-api
- description: ZIP code validation
  name: SAM.gov ZIP Codes API
  slug: sam.gov-zip-codes-api
artifact_total: 24
collections:
- collection_type: open
  name: SAM.gov Public Location Services API
  slug: open-sam-gov-location-services
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sam.gov-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sam.gov-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sam.gov
- group: start
  title: ''
  type: Portal
  url: https://open.gsa.gov/api/
- group: docs
  title: ''
  type: Documentation
  url: https://open.gsa.gov/api/
- group: auth
  title: ''
  type: APIKey
  url: https://open.gsa.gov/api/get-opportunities-public-api/#getting-started
- group: build
  title: ''
  type: GitHub
  url: https://github.com/GSA
- group: other
  title: ''
  type: DataCatalog
  url: https://catalog.data.gov
- group: operate
  title: ''
  type: StatusPage
  url: https://sam.gov/status
created: '2024-03-29'
description: SAM.gov (System for Award Management) is the official US government system for vendor registration and federal procurement. Operated by the General Services Administration (GSA), SAM.gov consolidates multiple legacy acquisition systems and provides APIs for contract opportunities, entity management, federal hierarchy, and location validation services.
examples:
- key_count: 2
  name: Sam Gov Get Cities Example
  slug: sam-gov-get-cities-example
- key_count: 2
  name: Sam Gov Validate Zip Example
  slug: sam-gov-validate-zip-example
finops:
- name: Sam.Gov Finops
  service_category: Federal Government / Procurement Data
  slug: sam.gov-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sam.gov.png
json_schemas:
- name: SAM.gov City
  property_count: 9
  slug: sam-gov-city
- name: SAM.gov Contract Opportunity
  property_count: 21
  slug: sam-gov-opportunity
json_structures:
- name: Sam Gov City Structure
  property_count: 0
  slug: sam-gov-city-structure
- name: Sam Gov Opportunity Structure
  property_count: 0
  slug: sam-gov-opportunity-structure
- name: Sam.Gov Structure
  property_count: 0
  slug: sam.gov-structure
jsonld:
- class_count: 0
  name: Sam Gov Context
  property_count: 5
  slug: sam-gov-context
layout: provider
modified: '2026-05-19'
name: SAM.gov
nav: Providers
network: true
overview: 'SAM.gov publishes 3 APIs on the [APIs.io](https://apis.io/) network: Cities API, States API, and ZIP Codes API. Tagged areas include Federal Government, Procurement, Contracts, Entity Management, and Location Services.


  The SAM.gov catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAM.gov''s developer surface includes developer portal, documentation, GitHub presence, and 6 more developer resources.'
plans:
- name: Sam.Gov Plans Pricing
  plan_count: 1
  slug: sam.gov-plans-pricing
random_paper: 34
rate_limits:
- limit_count: 1
  name: Sam.Gov Rate Limits
  slug: sam.gov-rate-limits
rules:
- name: SAM.gov API Rules
  rule_count: 10
  severity_counts:
    error: 4
    hint: 2
    info: 0
    warn: 4
  slug: sam-gov-rules
- name: SAM.gov API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sam.gov-jsonschema-spectral-rules
score:
  band: thin
  composite: 39.2
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 62.0
    developer_ergonomics: 17.4
    discoverability: 64.8
    governance: 20.8
    operational_transparency: 42.1
  previous_composite: 39.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sam.gov/refs/heads/main/screenshots/sam.gov-2026-06-20T193356.png
security:
- kind: domain-security
  name: Sam.Gov Domain Security
  slug: sam.gov-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: sam.gov
tags:
- Federal Government
- Procurement
- Contracts
- Entity Management
- Location Services
- GSA
website: https://sam.gov
---

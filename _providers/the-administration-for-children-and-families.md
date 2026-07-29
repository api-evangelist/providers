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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: The Administration For Children And Families Agentic Access
  operation_count: 48
  slug: the-administration-for-children-and-families-agentic-access
  summary_line: 48 operations · 15 acting
api_count: 5
apis:
- description: The TANF Data Portal (TDP) is a secure, web-based data reporting system for state agencies to submit Temporary Assistance for Needy Families (TANF) program data to ACF. It provides data submission wor
  name: TANF Data Portal
  slug: tanf-data-portal
- description: NDACAN is the central repository for datasets related to child abuse, neglect, and child welfare at Cornell University, funded by ACF. Provides access to AFCARS (foster care/adoption), NCANDS (child a
  name: National Data Archive on Child Abuse and Neglect
  slug: ndacan
- description: ACF's primary data and research portal providing access to program data, statistical reports, and research findings across all ACF program offices. Includes TANF caseload data, CCDF data, Head Start p
  name: ACF Data and Research Portal
  slug: acf-data-research
- description: The plg_auth_check API from The Administration for Children and Families — 1 operation(s) for plg_auth_check.
  name: The Administration for Children and Families plg_auth_check API
  slug: the-administration-for-children-and-families-plg-auth-check-api
- description: The v1 API from The Administration for Children and Families — 35 operation(s) for v1.
  name: The Administration for Children and Families v1 API
  slug: the-administration-for-children-and-families-v1-api
artifact_total: 17
collections:
- collection_type: open
  name: TDP API
  slug: open-the-administration-for-children-and-families
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/the-administration-for-children-and-families-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/the-administration-for-children-and-families-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/the-administration-for-children-and-families-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/administration-for-children-and-families
- group: company
  title: ''
  type: Website
  url: https://www.acf.hhs.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://acf.gov/acf-data-research
- group: start
  title: ''
  type: Data Portal
  url: https://tanfdata.acf.hhs.gov/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/HHS
- group: other
  title: ''
  type: Data Catalog
  url: https://catalog.data.gov/organization/hhs-acf
- group: other
  title: ''
  type: Interoperability
  url: https://acf.gov/about/interoperability
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/acf-child-welfare-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/acf-tanf-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/acf-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/acf-vocabulary.yml
created: '2024-11-20T00:00:00.000Z'
description: The Administration for Children and Families (ACF) is a division of the U.S. Department of Health and Human Services dedicated to promoting the economic and social well-being of children, families, and communities. ACF administers programs including TANF (cash assistance), CCDF (child care), Head Start, LIHEAP (energy assistance), child welfare, and refugee assistance. ACF collects administrative data via systems including AFCARS (foster care and adoption), NCANDS (child abuse and neglect), NYTD (youth in transition), TANF data reporting, and CCDF data. ACF is pursuing interoperability standards using HL7 FHIR and USCDI+ for human services data exchange. The TANF Data Portal (tanfdata.acf.hhs.gov) provides state agencies with a data submission and analysis interface.
finops:
- name: The Administration For Children And Families Finops
  service_category: API
  slug: the-administration-for-children-and-families-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/the-administration-for-children-and-families.png
json_schemas:
- name: ACF Child Welfare Data
  property_count: 0
  slug: acf-child-welfare
- name: ACF TANF Data
  property_count: 0
  slug: acf-tanf
json_structures:
- name: Acf Data Structure
  property_count: 0
  slug: acf-data-structure
jsonld:
- class_count: 7
  name: Acf Context
  property_count: 21
  slug: acf-context
layout: provider
modified: '2026-07-25'
name: The Administration for Children and Families
nav: Providers
network: true
overview: 'The Administration for Children and Families publishes 2 APIs on the [APIs.io](https://apis.io/) network: plg_auth_check API and v1 API. Tagged areas include Children, Families, Federal Government, Health And Human Services, and Human Services.


  The The Administration for Children and Families catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  The Administration for Children and Families'' developer surface includes authentication, documentation, and 12 more developer resources.'
plans:
- name: The Administration For Children And Families Plans Pricing
  plan_count: 3
  slug: the-administration-for-children-and-families-plans-pricing
random_paper: 28
rate_limits:
- limit_count: 5
  name: The Administration For Children And Families Rate Limits
  slug: the-administration-for-children-and-families-rate-limits
rules:
- name: The Administration for Children and Families API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: the-administration-for-children-and-families-jsonschema-spectral-rules
score:
  band: developing
  composite: 44.8
  delta: -6.8
  facets:
    commercial_clarity: 39.5
    contract_quality: 50.0
    developer_ergonomics: 19.6
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 51.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/the-administration-for-children-and-families/refs/heads/main/screenshots/the-administration-for-children-and-families-2026-06-20T195211.png
security:
- kind: authentication
  name: The Administration For Children And Families Authentication
  slug: the-administration-for-children-and-families-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: The Administration For Children And Families Domain Security
  slug: the-administration-for-children-and-families-domain-security
  summary_line: TLSv1.2 · HSTS · DNSSEC · DMARC
slug: the-administration-for-children-and-families
tags:
- Children
- Families
- Federal Government
- Health And Human Services
- Human Services
- Social Safety Net
website: https://www.acf.hhs.gov/
---

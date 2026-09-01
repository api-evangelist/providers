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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Social Security Administration Agentic Access
  operation_count: 2
  slug: social-security-administration-agentic-access
  summary_line: 2 operations
api_count: 2
apis:
- description: Provides statistics on Old Age, Survivors, and Disability Insurance (OASDI) beneficiaries including counts by state, total population data, and benefit payment statistics. Available through SSA's open
  name: SSA OASDI Open Data API
  slug: oasdi-data-api
- description: The Electronic Consent Based SSN Verification (eCBSV) Service allows financial institutions to verify that a provided Social Security Number, name, and date of birth match SSA records, with consent fr
  name: SSA eCBSV Verification API
  slug: ecbsv-api
- description: Query SSA Field Office locations and hours
  name: Social Security Administration Field Offices API
  slug: social-security-administration-field-offices-api
- description: Query SSA Resident Station locations and hours
  name: Social Security Administration Resident Stations API
  slug: social-security-administration-resident-stations-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: SSA Field Office Address Field Offices API
  slug: open-social-security-administration-field-offices-api
- collection_type: open
  name: SSA Field Office Address Field Offices Resident Stations API
  slug: open-social-security-administration-resident-stations-api
- collection_type: open
  name: SSA Field Office Address API
  slug: open-ssa-field-office
- collection_type: open
  name: SSA Resident Station Address API
  slug: open-ssa-resident-station
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/social-security-administration-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/social-security-administration-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/ssa
- group: company
  title: ''
  type: Website
  url: https://www.ssa.gov/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.ssa.gov/developer/
- group: start
  title: ''
  type: Open Data Portal
  url: https://www.ssa.gov/data/
- group: other
  title: ''
  type: Open Data Inventory
  url: https://www.ssa.gov/data/Open-Data-Inventory-Information.html
- group: other
  title: ''
  type: Data.gov Organization
  url: https://catalog.data.gov/organization/ssa-gov
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ssa-field-office-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/ssa-resident-station-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/ssa-office-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/ssa-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/ssa-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: examples/ssa-field-office-query-example.json
created: '2024-12-03'
description: The Social Security Administration (SSA) is a U.S. federal agency that administers Social Security programs including retirement, disability (SSDI), and survivor benefits. SSA's Developer Support portal provides APIs for locating field offices and resident stations, accessing open data on OASDI beneficiary statistics, and verifying Social Security Numbers through the eCBSV program.
examples:
- key_count: 4
  name: Ssa Field Office Query Example
  slug: ssa-field-office-query-example
finops:
- name: Social Security Administration Finops
  service_category: API
  slug: social-security-administration-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/social-security-administration.png
json_schemas:
- name: SSA Field Office
  property_count: 23
  slug: ssa-field-office
- name: SSA Resident Station
  property_count: 23
  slug: ssa-resident-station
json_structures:
- name: Ssa Office Structure
  property_count: 0
  slug: ssa-office-structure
jsonld:
- class_count: 20
  name: Ssa Context
  property_count: 6
  slug: ssa-context
layout: provider
modified: '2026-05-19'
name: Social Security Administration
nav: Providers
network: true
overview: 'Social Security Administration publishes 2 APIs on the [APIs.io](https://apis.io/) network: Field Offices API and Resident Stations API. Tagged areas include Federal-Government, Social Security, Government API, Open Data, and OASDI.


  The Social Security Administration catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Social Security Administration''s developer surface includes code examples and 13 more developer resources.'
plans:
- name: Social Security Administration Plans Pricing
  plan_count: 3
  slug: social-security-administration-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Social Security Administration Rate Limits
  slug: social-security-administration-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Social Security Administration API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: social-security-administration-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Social Security Administration API Rules
  rule_count: 8
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 3
  slug: ssa-rules
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 14
    catalog_gap: 47.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 28.8
    contract_quality: 59.2
    developer_ergonomics: 19.0
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 28.8
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
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/social-security-administration/refs/heads/main/screenshots/social-security-administration-2026-06-20T194118.png
security:
- kind: domain-security
  name: Social Security Administration Domain Security
  slug: social-security-administration-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: social-security-administration
tags:
- Federal-Government
- Social Security
- Government API
- Open Data
- OASDI
- Disability Benefits
- Retirement Benefits
website: https://www.ssa.gov/
---

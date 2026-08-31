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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 19.8
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Rsc Agentic Access
  operation_count: 16
  slug: rsc-agentic-access
  summary_line: 16 operations · 9 acting
api_count: 1
apis:
- description: Search and filter chemical compounds by various properties.
  name: RSC Filter API
  slug: rsc-filter-api
- description: Look up reference data such as available data sources.
  name: RSC Lookups API
  slug: rsc-lookups-api
- description: Retrieve compound record details, images, and molecular files.
  name: RSC Records API
  slug: rsc-records-api
- description: Chemical format conversion and validation utilities.
  name: RSC Tools API
  slug: rsc-tools-api
artifact_total: 24
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: RSC ChemSpider Compounds API
  slug: open-rsc-chemspider-compounds
- collection_type: open
  name: RSC ChemSpider Compounds Filter API
  slug: open-rsc-filter-api
- collection_type: open
  name: RSC ChemSpider Compounds Filter Lookups API
  slug: open-rsc-lookups-api
- collection_type: open
  name: RSC ChemSpider Compounds Filter Records API
  slug: open-rsc-records-api
- collection_type: open
  name: RSC ChemSpider Compounds Filter Tools API
  slug: open-rsc-tools-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rsc-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rsc-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rsc-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rsc-equipment-rental
- group: start
  title: ''
  type: Portal
  url: https://developer.rsc.org/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.rsc.org/
- group: start
  title: ''
  type: Signup
  url: https://developer.rsc.org/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.rsc.org/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.rsc.org/help-legal/legal/privacy/
created: '2025-03-01'
description: The Royal Society of Chemistry (RSC) provides developer APIs through its ChemSpider platform, enabling programmatic access to one of the world's largest chemistry databases with over 88 million unique chemical compounds. The APIs support compound search, structure retrieval, format conversion, and data enrichment for cheminformatics applications.
examples:
- key_count: 2
  name: Rsc Convert Chemical Format Example
  slug: rsc-convert-chemical-format-example
- key_count: 2
  name: Rsc Filter By Name Example
  slug: rsc-filter-by-name-example
- key_count: 2
  name: Rsc Get Record Details Example
  slug: rsc-get-record-details-example
finops:
- name: Rsc Finops
  service_category: API
  slug: rsc-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rsc.png
json_schemas:
- name: ChemSpider Compound
  property_count: 14
  slug: rsc-compound
json_structures:
- name: Rsc Compound Structure
  property_count: 0
  slug: rsc-compound-structure
jsonld:
- class_count: 5
  name: Rsc Context
  property_count: 15
  slug: rsc-context
layout: provider
modified: '2026-05-19'
name: RSC
nav: Providers
network: true
overview: 'RSC publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Filter API, Lookups API, Records API, and 1 more. Tagged areas include Chemistry, Cheminformatics, Chemical Data, and Science.


  The RSC catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RSC''s developer surface includes authentication, developer portal, signup flow, and 6 more developer resources.'
plans:
- name: Rsc Plans Pricing
  plan_count: 3
  slug: rsc-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 5
  name: Rsc Rate Limits
  slug: rsc-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: RSC API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: rsc-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: RSC API Rules
  rule_count: 18
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 14
  slug: rsc-spectral-rules
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 15
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 13.6
    contract_quality: 64.6
    developer_ergonomics: 9.5
    discoverability: 59.3
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 35.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rsc/refs/heads/main/screenshots/rsc-2026-08-17T081644.png
security:
- kind: authentication
  name: Rsc Authentication
  slug: rsc-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Rsc Domain Security
  slug: rsc-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: rsc
tags:
- Chemistry
- Cheminformatics
- Chemical Data
- Science
website: https://developer.rsc.org/
---

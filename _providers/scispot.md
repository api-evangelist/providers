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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 32.1
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Scispot Agentic Access
  operation_count: 18
  slug: scispot-agentic-access
  summary_line: 18 operations · 7 acting
api_count: 5
apis:
- description: Electronic Lab Notebook protocols and experimental records
  name: Scispot ELN API
  slug: scispot-eln-api
- description: LIMS-style structured data tables for registries, sample tracking, and assay data
  name: Scispot Labsheets API
  slug: scispot-labsheets-api
- description: Physical container management including plates, boxes, and racks
  name: Scispot Manifests API
  slug: scispot-manifests-api
- description: Sample lifecycle management including barcoding and metadata
  name: Scispot Samples API
  slug: scispot-samples-api
- description: Biological sequence management for DNA, RNA, and protein sequences
  name: Scispot Sequences API
  slug: scispot-sequences-api
artifact_total: 26
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Scispot ELN API
  slug: open-scispot-eln-api
- collection_type: open
  name: Scispot ELN Labsheets API
  slug: open-scispot-labsheets-api
- collection_type: open
  name: Scispot ELN Manifests API
  slug: open-scispot-manifests-api
- collection_type: open
  name: Scispot ELN Samples API
  slug: open-scispot-samples-api
- collection_type: open
  name: Scispot ELN Sequences API
  slug: open-scispot-sequences-api
- collection_type: open
  name: Scispot API
  slug: open-scispot
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/scispot-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/scispot-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/scispot-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/scispot
- group: company
  title: ''
  type: Website
  url: https://www.scispot.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.scispot.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.scispot.com/compbio
- group: company
  title: ''
  type: Blog
  url: https://www.scispot.com/blog
created: '2026-05-02'
description: Scispot is a cloud-native laboratory data platform and operating system for modern life science labs. It provides an API-first architecture combining Electronic Lab Notebook (ELN) and Laboratory Information Management System (LIMS) capabilities with over 250 pre-built instrument connectors and 7,000+ application integrations via its GLUE layer. Labs use Scispot to centralize and activate their data, automate experiment workflows, manage samples, sequences, and chemical structures programmatically, and integrate with clinical data standards including HL7 FHIR, HL7 v2, and ASTM protocols.
examples:
- key_count: 3
  name: Scispot Add Labsheet Row Example
  slug: scispot-add-labsheet-row-example
- key_count: 3
  name: Scispot List Labsheets Example
  slug: scispot-list-labsheets-example
finops:
- name: Scispot Finops
  service_category: API
  slug: scispot-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/scispot.png
json_schemas:
- name: Scispot Labsheet
  property_count: 7
  slug: scispot-labsheet
- name: Scispot Biological Sequence
  property_count: 9
  slug: scispot-sequence
json_structures:
- name: Scispot Labsheet Structure
  property_count: 0
  slug: scispot-labsheet-structure
jsonld:
- class_count: 52
  name: Scispot Context
  property_count: 2
  slug: scispot-context
layout: provider
modified: '2026-05-19'
name: Scispot
nav: Providers
network: true
overview: 'Scispot publishes 5 APIs on the [APIs.io](https://apis.io/) network, including ELN API, Labsheets API, Manifests API, and 2 more. Tagged areas include Laboratory, Life Science, LIMS, ELN, and Biotech.


  The Scispot catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Scispot''s developer surface includes authentication, documentation, engineering blog, and 5 more developer resources.'
plans:
- name: Scispot Plans Pricing
  plan_count: 3
  slug: scispot-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 5
  name: Scispot Rate Limits
  slug: scispot-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Scispot API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: scispot-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Scispot API Rules
  rule_count: 13
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 9
  slug: scispot-rules
score:
  band: thin
  composite: 37.7
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 13.6
    contract_quality: 69.7
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 13.6
    operational_transparency: 7.9
  previous_composite: 37.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/scispot/refs/heads/main/screenshots/scispot-2026-06-20T193537.png
security:
- kind: authentication
  name: Scispot Authentication
  slug: scispot-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Scispot Domain Security
  slug: scispot-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: scispot
tags:
- Laboratory
- Life Science
- LIMS
- ELN
- Biotech
- API-First
- Scientific Data
- Healthcare
website: https://www.scispot.com/
---

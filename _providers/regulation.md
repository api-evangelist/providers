---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 16.7
  scored_at: '2026-10-03'
api_count: 3
apis:
- description: The Regulations.gov API provides access to federal regulatory dockets, documents, and public comments. Enables programmatic access to the full regulatory comment process and rulemaking lifecycle acros
  name: Regulations.gov API
  slug: regulations-gov
- description: The Federal Register API provides programmatic access to documents published in the Federal Register since 1994, including proposed rules, final rules, notices, and presidential documents. Supports ad
  name: Federal Register API
  slug: federal-register
- description: Compliance.ai provides an API for regulatory change management that automatically aggregates data from federal and state agencies, enforcement actions, regulatory publications, white papers, and milli
  name: Compliance.ai Regulatory Change Management API
  slug: compliance-ai
artifact_total: 11
common:
- group: company
  title: ''
  type: Website
  url: https://open.gsa.gov/api/regulationsgov/
- group: company
  title: ''
  type: Website
  url: https://www.federalregister.gov/developers/documentation/api/v1
- group: company
  title: ''
  type: Website
  url: https://catalog.data.gov/dataset/regulations-gov-api
- group: company
  title: ''
  type: Website
  url: https://www.compliance.ai/api/
- group: company
  title: ''
  type: Website
  url: https://developer.finra.org/
- group: docs
  title: ''
  type: Documentation
  url: https://en.wikipedia.org/wiki/Regulation
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-schema/regulation-document-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-schema/regulation-comment-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-structure/regulation-document-structure.json
- group: design
  title: ''
  type: JSONLD
  url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/json-ld/regulation-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/vocabulary/regulation-vocabulary.yml
- group: build
  title: ''
  type: Examples
  url: https://raw.githubusercontent.com/api-evangelist/regulation/refs/heads/main/examples/regulation-document-federal-register-example.json
created: '2025-01-01'
description: Regulation encompasses the rules, laws, and standards established by governments, agencies, and standards bodies that govern how businesses and individuals must operate. In the context of APIs and digital technology, regulation drives compliance requirements for data privacy (GDPR, CCPA), financial services (PSD2, Dodd-Frank), healthcare (HIPAA), and many other sectors. A rich ecosystem of APIs exists to access regulatory data, track regulatory changes, and automate compliance workflows.
examples:
- key_count: 18
  name: Regulation Document Federal Register Example
  slug: regulation-document-federal-register-example
finops:
- name: Regulation Finops
  service_category: API
  slug: regulation-finops
json_schemas:
- name: Public Comment
  property_count: 10
  slug: regulation-comment
- name: Regulatory Document
  property_count: 18
  slug: regulation-document
json_structures:
- name: Regulation Document Structure
  property_count: 0
  slug: regulation-document-structure
jsonld:
- class_count: 6
  name: Regulation Context
  property_count: 7
  slug: regulation-context
layout: provider
modified: '2026-05-02'
name: Regulation
nav: Providers
network: true
overview: 'Regulation publishes 3 APIs on the [APIs.io](https://apis.io/) network, including Regulations.gov API, and 2 more. Tagged areas include Compliance, Governance, Government, Legal, and Policy.


  The Regulation catalog on APIs.io includes 1 JSON-LD context.


  Regulation''s developer surface includes documentation, code examples, and 10 more developer resources.'
plans:
- name: Regulation Plans Pricing
  plan_count: 3
  slug: regulation-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 5
  name: Regulation Rate Limits
  slug: regulation-rate-limits
score:
  band: thin
  composite: 30.3
  coverage:
    artifact_dirs: 12
    catalog_earned: 75.1
    catalog_earned_first_party: 0.0
    catalog_gap: 39.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 36.3
    contract_governance: 13.6
    contract_quality: 41.2
    developer_ergonomics: 9.5
    discoverability: 67.9
    operational_transparency: 28.4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: regulation
tags:
- Compliance
- Governance
- Government
- Legal
- Policy
- Regulations
- Regulatory Change
- Risk Management
website: https://open.gsa.gov/api/regulationsgov/
---

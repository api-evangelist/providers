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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.0
  scored_at: '2026-10-17'
api_count: 2
apis:
- description: API for Crux Data platform providing access to datasets and operations.
  name: Crux Data API
  slug: crux-data-api
- baseURL: https://api.cruxinformatics.com
  baseurl_source: declared
  description: The Ops API from Cruxinformatics — 3 operation(s) for ops.
  name: Cruxinformatics Ops API
  slug: cruxinformatics-ops-api
artifact_total: 8
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/rules/cruxinformatics-rules.yml
  title: ''
  type: Spectral
  url: rules/cruxinformatics-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/json-ld/cruxinformatics-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cruxinformatics-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/vocabulary/cruxinformatics-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cruxinformatics-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/data-model/cruxinformatics-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cruxinformatics-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/conformance/cruxinformatics-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cruxinformatics-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/llms/cruxinformatics-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cruxinformatics-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/hosts/cruxinformatics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cruxinformatics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/vendors/cruxinformatics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cruxinformatics-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/cruxinformatics/refs/heads/main/security/cruxinformatics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cruxinformatics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cruxdata.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.cruxdata.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.cruxdata.com
- group: docs
  title: ''
  type: APIReference
  url: https://developer.cruxdata.com/reference
- group: company
  title: ''
  type: Blog
  url: https://www.cruxdata.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cruxdata.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cruxdata.com/privacy-policy
- group: operate
  title: ''
  type: Support
  url: https://www.cruxdata.com/contact-us
- group: start
  title: ''
  type: SignUp
  url: https://app.cruxdata.com/login
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://developer.cruxdata.com/mcp
  - status: 200
    url: https://www.cruxdata.com
  - status: 403
    url: https://equityzen.com/company/cruxinformatics
  reason: partner-login
  state: gated
created: '2026-10-11'
description: Cruxinformatics, operating under the Cruxdata brand, provides AI‑driven data onboarding, transformation, and monitoring solutions for financial services and other industries. Their platform offers managed services, self‑service tools, and extensive integrations with data providers such as Morningstar, Moody's, and MSCI, enabling clients to ingest, validate, and enrich external data streams in real time.
image: https://cdn.prod.website-files.com/671ad000f127406535cffcbb/67fe0c136dc41bb5eb273386_OG-crux.png
json_schemas:
- name: GetV2OpsHealthDatasetsDatasetidDeliveriesResponse
  property_count: 15
  slug: cruxinformatics-get-v2-ops-health-datasets-datasetid-deliveries-response
- name: GetV2OpsHealthDatasetsDeliveriesResponse
  property_count: 4
  slug: cruxinformatics-get-v2-ops-health-datasets-deliveries-response
- name: GetV2OpsHealthDeliveriesDeliveryidTasksResponse
  property_count: 4
  slug: cruxinformatics-get-v2-ops-health-deliveries-deliveryid-tasks-response
jsonld:
- class_count: 3
  name: Cruxinformatics Context
  property_count: 23
  slug: cruxinformatics-context
layout: provider
modified: '2026-10-11'
name: Cruxinformatics
nav: Providers
network: true
overview: 'Cruxinformatics is listed with 2 APIs on the [APIs.io](https://apis.io/) network, including Ops API, and 1 more. Tagged areas include Data Integration, Artificial Intelligence, Financial Services, Managed Service, and Self-Service.


  The Cruxinformatics catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cruxinformatics'' developer surface includes documentation, API reference, engineering blog, support, signup flow, and 13 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Cruxinformatics API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: cruxinformatics-rules
score:
  band: thin
  composite: 28.5
  coverage:
    artifact_dirs: 13
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 22.0
    contract_quality: 22.3
    developer_ergonomics: 33.3
    discoverability: 64.3
    operational_transparency: 0.0
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
security:
- kind: domain-security
  name: Cruxinformatics Domain Security
  slug: cruxinformatics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cruxinformatics
tags:
- Data Integration
- Artificial Intelligence
- Financial Services
- Managed Service
- Self-Service
website: https://www.cruxdata.com
---

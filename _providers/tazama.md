---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - security
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
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 22.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tazama Agentic Access
  operation_count: 6
  slug: tazama-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 1
apis:
- description: Administrative API for managing and configuring the Tazama platform. Supports configuration of rule processors, typology definitions, network maps, and system administration. Swagger documentation ava
  name: Tazama Admin Service API
  slug: admin-service
- baseURL: http://localhost:5000
  baseurl_source: declared
  description: Service health check operations
  name: Tazama Health API
  slug: tazama-health-api
- baseURL: http://localhost:5000
  baseurl_source: declared
  description: ISO 20022 transaction message evaluation for fraud and AML detection
  name: Tazama Transaction Evaluation API
  slug: tazama-transaction-evaluation-api
artifact_total: 19
collections:
- collection_type: open
  name: Tazama Transaction Monitoring Service Health API
  slug: open-tazama-health-api
- collection_type: open
  name: Tazama Transaction Monitoring Service Health Transaction Evaluation API
  slug: open-tazama-transaction-evaluation-api
- collection_type: open
  name: Tazama Transaction Monitoring Service API
  slug: open-tazama-transaction-monitoring-service
common:
- group: commercial
  href: https://artifacts.apis.io/tazama/plans/tazama-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tazama-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tazama/rate-limits/tazama-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tazama-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tazama/finops/tazama-finops.yml
  title: ''
  type: FinOps
  url: finops/tazama-finops.yml
- group: company
  title: ''
  type: Website
  url: https://tazama.org
- group: other
  href: https://artifacts.apis.io/tazama/capabilities/tazama-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/tazama-capability-edges.yml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/tazama-lf/admin-service/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/tazama-lf/admin-service/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/tazama-lf/.github/blob/main/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/tazama-lf/.github/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/tazama-lf/admin-service/blob/main/LICENSE
- group: agent
  href: https://artifacts.apis.io/tazama/agentic-access/tazama-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/tazama-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/tazama/security/tazama-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tazama-domain-security.yml
- group: company
  title: ''
  type: Blog
  url: https://www.tazama.org/feed/
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tazama-org
- group: docs
  title: ''
  type: Documentation
  url: https://tazama.org/products/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/tazama-lf
- group: company
  title: ''
  type: About
  url: https://tazama.org/about/
- group: other
  title: ''
  type: Licensing
  url: https://www.linuxfoundation.org/press/linux-foundation-launches-tazama-for-real-time-fraud-management
- group: docs
  title: ''
  type: OpenAPI
  url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/openapi/tazama-transaction-monitoring-service-openapi.yml
- group: design
  title: ''
  type: Vocabulary
  url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/vocabulary/tazama-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/json-schema/tazama-transaction-response-schema.json
- group: design
  title: ''
  type: JSONLDContext
  url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/json-ld/tazama-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/rules/tazama-rules.yml
created: '2026-03-16'
description: Tazama is the first open source platform for real-time financial monitoring and fraud detection, launched by Linux Foundation Charities with support from the Bill and Melinda Gates Foundation. It provides real-time fraud management, AML compliance, and cost-effective monitoring of digital financial transactions through a microservices architecture with rule processors, typology scoring, and case management integration. Built to ISO 20022 standards for maximum financial messaging interoperability.
examples:
- key_count: 2
  name: Tazama Evaluate Pacs008 Transaction Example
  slug: tazama-evaluate-pacs008-transaction-example
- key_count: 2
  name: Tazama Evaluate Pain001 Transaction Example
  slug: tazama-evaluate-pain001-transaction-example
finops:
- has_sources: false
  method: generated
  name: Tazama Finops
  primary_unit: request
  service_category: API
  slug: tazama-finops
  template: true
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tazama.png
json_schemas:
- name: ISO 20022 pain.001.001.11 Customer Credit Transfer Initiation
  property_count: 1
  slug: tazama-iso20022-pain001
- name: Tazama Transaction Response
  property_count: 2
  slug: tazama-transaction-response
json_structures:
- name: Tazama Transaction Response Structure
  property_count: 0
  slug: tazama-transaction-response-structure
jsonld:
- class_count: 38
  name: Tazama Context
  property_count: 0
  slug: tazama-context
layout: provider
modified: '2026-09-16'
name: Tazama
nav: Providers
network: true
overview: 'Tazama publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network, including Health API, Transaction Evaluation API, and 1 more. Tagged areas include Financial Technology, Fraud Prevention, AML, Linux Foundation, and Open Source.


  The Tazama catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tazama''s developer surface includes engineering blog, documentation, and 21 more developer resources.'
plans:
- name: Tazama Plans Pricing
  plan_count: 3
  slug: tazama-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Tazama Rate Limits
  slug: tazama-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Tazama — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tazama-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Tazama API Rules
  rule_count: 10
  severity_counts:
    error: 2
    hint: 0
    info: 0
    warn: 8
  slug: tazama-rules
score:
  band: thin
  composite: 30.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.0
    catalog_earned_first_party: 0.0
    catalog_gap: 60.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    contract_governance: 27.3
    contract_quality: 47.4
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 28.9
  open_source:
    applies: true
    score: 65.0
  previous_composite: 30.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/tazama/tazama-2026-06-20T194939.png
security:
- kind: domain-security
  name: Tazama Domain Security
  slug: tazama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tazama
tags:
- Financial Technology
- Fraud Prevention
- AML
- Linux Foundation
- Open Source
- Transaction Monitoring
- ISO 20022
- Real-Time
website: https://tazama.org
---

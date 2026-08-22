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
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 26.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Tazama Agentic Access
  operation_count: 6
  slug: tazama-agentic-access
  summary_line: 6 operations · 4 acting
api_count: 3
apis:
- description: Administrative API for managing and configuring the Tazama platform. Supports configuration of rule processors, typology definitions, network maps, and system administration. Swagger documentation ava
  name: Tazama Admin Service API
  slug: admin-service
- description: Service health check operations
  name: Tazama Health API
  slug: tazama-health-api
- description: ISO 20022 transaction message evaluation for fraud and AML detection
  name: Tazama Transaction Evaluation API
  slug: tazama-transaction-evaluation-api
artifact_total: 21
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
  title: ''
  type: License
  url: https://github.com/tazama-lf/admin-service/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tazama-agentic-access.yml
- group: auth
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
- name: Tazama Finops
  service_category: API
  slug: tazama-finops
graphqls:
- description: ''
  name: Tazama GraphQL API
  slug: tazama-graphql
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
modified: '2026-05-19'
name: Tazama
nav: Providers
network: true
overview: 'Tazama publishes 2 APIs on the [APIs.io](https://apis.io/) network: Health API and Transaction Evaluation API. Tagged areas include Financial Technology, Fraud Detection, Anti-Money Laundering, Linux Foundation, and Open Source.


  The Tazama catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tazama''s developer surface includes engineering blog, documentation, and 12 more developer resources.'
plans:
- name: Tazama Plans Pricing
  plan_count: 3
  slug: tazama-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Tazama Rate Limits
  slug: tazama-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Tazama API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: tazama-jsonschema-spectral-rules
- effective_rule_count: 51
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
  composite: 30.1
  delta: -5.7
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 53.5
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 25.0
    operational_transparency: 13.2
  previous_composite: 35.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/tazama/refs/heads/main/screenshots/tazama-2026-06-20T194939.png
security:
- kind: domain-security
  name: Tazama Domain Security
  slug: tazama-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: tazama
tags:
- Financial Technology
- Fraud Detection
- Anti-Money Laundering
- Linux Foundation
- Open Source
- Transaction Monitoring
- ISO 20022
- Real Time
---

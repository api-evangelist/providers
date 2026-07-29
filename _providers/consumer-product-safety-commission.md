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
    asyncapi_events: false
    auth_clarity: false
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
  score: 21.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Consumer Product Safety Commission Agentic Access
  operation_count: 1
  slug: consumer-product-safety-commission-agentic-access
  summary_line: 1 operation
api_count: 2
apis:
- description: 'OData web service exposing publicly published consumer product incident-report data submitted through SaferProducts.gov. Authenticated with a basic-auth header where the registered application key is '
  name: SaferProducts.gov OData API
  slug: saferproducts
- description: The Recalls API from Consumer Product Safety Commission — 1 operation(s) for recalls.
  name: Consumer Product Safety Commission Recalls API
  slug: consumer-product-safety-commission-recalls-api
artifact_total: 12
collections:
- collection_type: open
  name: CPSC Recalls API
  slug: open-cpsc-recalls
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/consumer-product-safety-commission-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/consumer-product-safety-commission-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.cpsc.gov/
- group: other
  title: ''
  type: Recalls
  url: https://www.cpsc.gov/Recalls
- group: other
  title: ''
  type: Data
  url: https://www.cpsc.gov/Data
- group: other
  title: ''
  type: SaferProducts.gov
  url: https://www.saferproducts.gov/
- group: other
  title: ''
  type: Public Search
  url: https://www.saferproducts.gov/PublicSearch
- group: docs
  title: ''
  type: Programmers Guide
  url: https://cpsc.gov/s3fs-public/RecallRetrievalWebServicesProgrammersGuide20180917.pdf
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.cpsc.gov/Newsroom/Privacy-and-Security-Statement
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.cpsc.gov/Newsroom/Privacy-and-Security-Statement
- group: design
  title: ''
  type: JSONLD
  url: json-ld/consumer-product-safety-commission-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/cpsc-recall-schema.json
- group: design
  title: ''
  type: Spectral
  url: rules/consumer-product-safety-commission-rules.yml
created: '2024-12-25'
description: The U.S. Consumer Product Safety Commission (CPSC) is the federal agency responsible for protecting the public from unreasonable risks of injury or death associated with consumer products such as toys, household items, electronics, and furniture. CPSC publishes a public, unauthenticated Recalls Retrieval Web Service that exposes recall records (with products, hazards, manufacturers, retailers, distributors, importers, and remedies) in JSON or XML, plus the SaferProducts.gov OData service for incident-report data accessed by application key.
finops:
- name: Consumer Product Safety Commission Finops
  service_category: API
  slug: consumer-product-safety-commission-finops
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/apis-json.png
json_schemas:
- name: CPSC Recall
  property_count: 21
  slug: cpsc-recall
jsonld:
- class_count: 0
  name: Consumer Product Safety Commission Context
  property_count: 3
  slug: consumer-product-safety-commission-context
layout: provider
modified: '2026-05-19'
name: Consumer Product Safety Commission
nav: Providers
network: true
overview: 'Consumer Product Safety Commission publishes 1 API on the [APIs.io](https://apis.io/) network: Recalls API. Tagged areas include Consumer Protection, Federal Government, Hazards, Open Data, and Product Safety.


  The Consumer Product Safety Commission catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.'
plans:
- name: Consumer Product Safety Commission Plans Pricing
  plan_count: 3
  slug: consumer-product-safety-commission-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Consumer Product Safety Commission Rate Limits
  slug: consumer-product-safety-commission-rate-limits
rules:
- name: Consumer Product Safety Commission API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: consumer-product-safety-commission-jsonschema-spectral-rules
- name: Consumer Product Safety Commission API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 2
    warn: 2
  slug: consumer-product-safety-commission-rules
score:
  band: developing
  composite: 42.9
  delta: -4.1
  facets:
    commercial_clarity: 60.5
    contract_quality: 56.8
    developer_ergonomics: 0.0
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 31.6
  previous_composite: 47.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 35.2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/consumer-product-safety-commission/refs/heads/main/screenshots/consumer-product-safety-commission-2026-06-20T174919.png
security:
- kind: domain-security
  name: Consumer Product Safety Commission Domain Security
  slug: consumer-product-safety-commission-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: consumer-product-safety-commission
tags:
- Consumer Protection
- Federal Government
- Hazards
- Open Data
- Product Safety
- Recalls
website: https://www.cpsc.gov/
---

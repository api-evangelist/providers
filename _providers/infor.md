---
access_model:
  confidence: high
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Infor Agentic Access
  operation_count: 4
  slug: infor-agentic-access
  summary_line: 4 operations · 1 acting
api_count: 5
apis:
- description: The Infor M3 (CloudSuite Industrial) APIs provide access to production orders, inventory management, supply chain planning, and financial data for discrete and process manufacturing enterprises. The M
  name: Infor M3 / LN CloudSuite Industrial API
  slug: infor-m3-api
- description: 'Infor XtendM3 provides a Java SDK for extending and customizing Infor M3 (CloudSuite Industrial) business logic without modifying core code. Extensions are deployed and executed within the M3 runtime '
  name: Infor XtendM3 API
  slug: infor-xtendm3-api
- description: Infor CloudSuite Financials APIs provide integration with general ledger, accounts payable, accounts receivable, cash management, and financial reporting for enterprise finance operations.
  name: Infor CloudSuite Financials API
  slug: infor-cloudsuite-financials-api
- description: ION document routing and processing
  name: Infor ION Documents API
  slug: infor-ion-documents-api
- description: Infor M3 business API programs
  name: Infor M3 API API
  slug: infor-m3-api-api
artifact_total: 22
asyncapis:
- description: Infor ION event framework AsyncAPI specification for event-driven integrations with Infor CloudSuite applications. The ION Event Hub publishes business events when transactions occur in Infor applicat
  name: Infor ION Events
  slug: infor-ion-events-asyncapi
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Infor ION API Gateway
  slug: open-infor-ion-api-gateway
- collection_type: open
  name: Infor ION API Gateway ION Documents API
  slug: open-infor-ion-documents-api
- collection_type: open
  name: Infor ION API Gateway ION Documents M3 API API
  slug: open-infor-m3-api-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/infor-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/infor-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/infor-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/infor-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/infor-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/infor
description: Infor provides industry-specific cloud ERP platforms including CloudSuite Industrial (M3), CloudSuite Financials, and Infor LN. The Infor ION API Gateway enables OAuth 2.0-based integration across Infor applications and third-party systems. SDKs are available via the infor-cloud GitHub organization for Java, .NET, Go, and HTML5 development.
finops:
- name: Infor Finops
  service_category: Enterprise Software
  slug: infor-finops
image: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/image.png
json_schemas:
- name: Infor M3 Customer
  property_count: 22
  slug: infor-m3-customer
jsonld:
- class_count: 22
  name: Infor Context
  property_count: 6
  slug: infor-context
layout: provider
modified: '2026-04-28'
name: Infor
nav: Providers
network: true
overview: 'Infor publishes 2 APIs on the [APIs.io](https://apis.io/) network: ION Documents API and M3 API API. Tagged areas include ERP, Manufacturing, Supply Chain, Cloud, and Integration.


  The Infor catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Infor''s developer surface includes authentication and 5 more developer resources.'
plans:
- name: Infor Plans Pricing
  plan_count: 1
  slug: infor-plans-pricing
random_paper: 17
rate_limits:
- limit_count: 1
  name: Infor Rate Limits
  slug: infor-rate-limits
rules:
- effective_rule_count: 34
  extends:
  - spectral:asyncapi
  name: Infor API Rules
  rule_count: 7
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 5
  slug: infor-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Infor API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: infor-jsonschema-spectral-rules
scopes:
- name: Infor Scopes
  scope_count: 0
  slug: infor-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.6
  delta: -4.8
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 13.6
    contract_quality: 67.5
    developer_ergonomics: 11.9
    discoverability: 68.5
    governance: 13.6
    operational_transparency: 5.3
  previous_composite: 37.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/infor/refs/heads/main/screenshots/infor-2026-06-20T183339.png
security:
- kind: authentication
  name: Infor Authentication
  slug: infor-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Infor Domain Security
  slug: infor-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Infor Trust Center
  slug: infor-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, GDPR
slug: infor
tags:
- ERP
- Manufacturing
- Supply Chain
- Cloud
- Integration
---

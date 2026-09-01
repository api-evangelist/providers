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
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 22.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sandbox Banking Agentic Access
  operation_count: 15
  slug: sandbox-banking-agentic-access
  summary_line: 15 operations · 7 acting
api_count: 1
apis:
- description: The Mock Bank API provides a sandbox environment for testing and developing banking integrations without connecting to production core banking systems. It simulates standard banking operations includi
  name: Mock Bank API
  slug: mockbank
- description: Core banking and fintech adapter management.
  name: Sandbox Banking Adapters API
  slug: sandbox-banking-adapters-api
- description: Field mapping configuration.
  name: Sandbox Banking Field Mappings API
  slug: sandbox-banking-field-mappings-api
- description: Integration workflow management.
  name: Sandbox Banking Integrations API
  slug: sandbox-banking-integrations-api
- description: Integration run audit log access.
  name: Sandbox Banking Run History API
  slug: sandbox-banking-run-history-api
- description: Service request adapter operations.
  name: Sandbox Banking Service Requests API
  slug: sandbox-banking-service-requests-api
- description: Value mapping table management.
  name: Sandbox Banking Value Mappings API
  slug: sandbox-banking-value-mappings-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway Adapters API
  slug: open-sandbox-banking-adapters-api
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway Adapters Field Mappings API
  slug: open-sandbox-banking-field-mappings-api
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway API
  slug: open-sandbox-banking-glyue
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway Adapters Integrations API
  slug: open-sandbox-banking-integrations-api
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway Adapters Run History API
  slug: open-sandbox-banking-run-history-api
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway Adapters Service Requests API
  slug: open-sandbox-banking-service-requests-api
- collection_type: open
  name: Sandbox Banking Glyue Integration Gateway Adapters Value Mappings API
  slug: open-sandbox-banking-value-mappings-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sandbox-banking-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sandbox-banking-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sandbox-banking-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sandboxbanking
- group: docs
  title: Glyue Integration Gateway Documentation
  type: Documentation
  url: https://glyue.docs.sandboxbanking.com/
- group: docs
  title: nCino Integration Gateway
  type: Documentation
  url: https://www.ncino.com/solutions/integrations
- group: docs
  title: Mock Bank API Documentation
  type: Documentation
  url: https://mockbank.docs.sandboxbanking.com/
- group: company
  title: Sandbox Banking Website
  type: Website
  url: https://sandboxbanking.com/
- group: design
  title: Sandbox Banking API Spectral Rules
  type: SpectralRules
  url: rules/sandbox-banking-rules.yml
- group: docs
  title: Sandbox Banking Integration Schema
  type: JSONSchema
  url: json-schema/sandbox-banking-integration-schema.json
- group: design
  title: Sandbox Banking Integration Structure
  type: JSONStructure
  url: json-structure/sandbox-banking-integration-structure.json
- group: design
  title: Sandbox Banking JSON-LD Context
  type: JSONLDContext
  url: json-ld/sandbox-banking-context.jsonld
- group: build
  title: Sandbox Banking List Integrations Example
  type: Examples
  url: examples/sandbox-banking-list-integrations-example.json
- group: build
  title: Sandbox Banking Run Integration Example
  type: Examples
  url: examples/sandbox-banking-run-integration-example.json
- group: design
  title: Sandbox Banking Vocabulary
  type: Vocabulary
  url: vocabulary/sandbox-banking-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://glyue.docs.sandboxbanking.com/llms.txt
created: '2024-12-25'
description: Sandbox Banking (now nCino Integration Gateway) is an Integration Platform as a Service (iPaaS) purpose-built for financial institutions. The platform enables banks and credit unions to connect core banking systems (Fiserv, Jack Henry, FIS, and 14+ other cores) with fintech applications, loan origination systems, CRMs, KYC/AML providers, and 50+ financial services solutions. Glyue, the core integration framework, provides low-code workflow automation with Python extensibility, audit trails, role-based access control, and regulatory compliance features aligned with CFPB Section 1033, GLBA, and FFIEC guidelines.
examples:
- key_count: 4
  name: Sandbox Banking List Integrations Example
  slug: sandbox-banking-list-integrations-example
- key_count: 4
  name: Sandbox Banking Run Integration Example
  slug: sandbox-banking-run-integration-example
finops:
- name: Sandbox Banking Finops
  service_category: API
  slug: sandbox-banking-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sandbox-banking.png
json_schemas:
- name: Sandbox Banking Integration
  property_count: 13
  slug: sandbox-banking-integration
json_structures:
- name: Sandbox Banking Integration Structure
  property_count: 0
  slug: sandbox-banking-integration-structure
jsonld:
- class_count: 43
  name: Sandbox Banking Context
  property_count: 0
  slug: sandbox-banking-context
layout: provider
modified: '2026-05-19'
name: Sandbox Banking
nav: Providers
network: true
overview: 'Sandbox Banking publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Adapters API, Field Mappings API, Integrations API, and 3 more. Tagged areas include API Integration, Banking, Core Banking, Credit Unions, and Financial-Services.


  The Sandbox Banking catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Sandbox Banking''s developer surface includes authentication, documentation, code examples, and 13 more developer resources.'
plans:
- name: Sandbox Banking Plans Pricing
  plan_count: 3
  slug: sandbox-banking-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Sandbox Banking Rate Limits
  slug: sandbox-banking-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Sandbox Banking API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sandbox-banking-jsonschema-spectral-rules
- effective_rule_count: 54
  extends:
  - spectral:oas
  name: Sandbox Banking API Rules
  rule_count: 13
  severity_counts:
    error: 4
    hint: 0
    info: 2
    warn: 7
  slug: sandbox-banking-rules
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 17
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 68.4
    developer_ergonomics: 21.4
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 7.9
  previous_composite: 35.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 21.5
  schema_version: 0.17.2
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sandbox-banking/refs/heads/main/screenshots/sandbox-banking-2026-06-20T193408.png
security:
- kind: authentication
  name: Sandbox Banking Authentication
  slug: sandbox-banking-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Sandbox Banking Domain Security
  slug: sandbox-banking-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: sandbox-banking
tags:
- API Integration
- Banking
- Core Banking
- Credit Unions
- Financial-Services
- Fintech
- Integration Platform
- iPaaS
- Open Banking
website: https://sandboxbanking.com/
---

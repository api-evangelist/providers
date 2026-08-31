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
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Subex Agentic Access
  operation_count: 8
  slug: subex-agentic-access
  summary_line: 8 operations · 1 acting
api_count: 1
apis:
- description: Risk analytics and reporting
  name: Subex Analytics API
  slug: subex-analytics-api
- description: Fraud detection and case management
  name: Subex Fraud Management API
  slug: subex-fraud-management-api
- description: CDR and billing data reconciliation
  name: Subex Reconciliation API
  slug: subex-reconciliation-api
- description: Revenue leakage detection and reconciliation
  name: Subex Revenue Assurance API
  slug: subex-revenue-assurance-api
artifact_total: 23
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Subex Revenue Assurance & Fraud Management Analytics API
  slug: open-subex-analytics-api
- collection_type: open
  name: Subex Revenue Assurance & Analytics Fraud Management API
  slug: open-subex-fraud-management-api
- collection_type: open
  name: Subex Revenue Assurance & Fraud Management Analytics Reconciliation API
  slug: open-subex-reconciliation-api
- collection_type: open
  name: Subex & Fraud Management Analytics Revenue Assurance API
  slug: open-subex-revenue-assurance-api
- collection_type: open
  name: Subex Revenue Assurance & Fraud Management API
  slug: open-subex-revenue-assurance
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/subex-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/subex-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/subex-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/subex-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/subex
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/subex-ltd
- group: company
  title: ''
  type: Website
  url: https://www.subex.com
- group: start
  title: ''
  type: Portal
  url: https://www.subex.com/roc/
- group: company
  title: ''
  type: Blog
  url: https://www.subex.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.subex.com/contact-us/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.subex.com/privacy-policy/
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.subex.com/newsroom/
- group: design
  title: ''
  type: SpectralRules
  url: rules/subex-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/subex-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/subex-fraud-case-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/subex-leakage-alert-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/subex-context.jsonld
- group: build
  title: ''
  type: Examples
  url: examples/subex-list-fraud-cases-example.json
- group: build
  title: ''
  type: Examples
  url: examples/subex-get-subscriber-risk-score-example.json
created: '2026-03-18'
description: Subex is a telecom analytics company providing revenue assurance, fraud management, and network analytics solutions through its ROC (Revenue Operations Center) platform. Subex helps telecom operators detect and prevent revenue leakage, manage telecom fraud (SIM swap, IRSF, bypass fraud, roaming fraud), reconcile CDR data, and gain analytics insights across their business support systems.
examples:
- key_count: 2
  name: Subex Get Subscriber Risk Score Example
  slug: subex-get-subscriber-risk-score-example
- key_count: 2
  name: Subex List Fraud Cases Example
  slug: subex-list-fraud-cases-example
finops:
- name: Subex Finops
  service_category: API
  slug: subex-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/subex.png
json_schemas:
- name: Subex Fraud Case
  property_count: 15
  slug: subex-fraud-case
json_structures:
- name: Subex Leakage Alert Structure
  property_count: 12
  slug: subex-leakage-alert-structure
jsonld:
- class_count: 30
  name: Subex Context
  property_count: 3
  slug: subex-context
layout: provider
modified: '2026-05-19'
name: Subex
nav: Providers
network: true
overview: 'Subex publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Analytics API, Fraud Management API, Reconciliation API, and 1 more. Tagged areas include Telecom, Revenue Assurance, Fraud Management, Analytics, and BSS/OSS.


  The Subex catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Subex''s developer surface includes authentication, developer portal, engineering blog, support, changelog, code examples, and 13 more developer resources.'
plans:
- name: Subex Plans Pricing
  plan_count: 3
  slug: subex-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Subex Rate Limits
  slug: subex-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Subex API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: subex-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Subex API Rules
  rule_count: 9
  severity_counts:
    error: 3
    hint: 2
    info: 0
    warn: 4
  slug: subex-rules
score:
  band: developing
  composite: 40.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 56.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.6
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 28.8
    contract_quality: 60.8
    developer_ergonomics: 38.1
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 41.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 29.2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/subex/refs/heads/main/screenshots/subex-2026-06-20T194634.png
security:
- kind: authentication
  name: Subex Authentication
  slug: subex-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Subex Domain Security
  slug: subex-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: subex
tags:
- Telecom
- Revenue Assurance
- Fraud Management
- Analytics
- BSS/OSS
website: https://www.subex.com
---

---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
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
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Saasment Agentic Access
  operation_count: 13
  slug: saasment-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.saasment.com/v1
  baseurl_source: spec
  description: Security alert and notification management
  name: Saasment Alerts API
  slug: saasment-alerts-api
- baseURL: https://api.saasment.com/v1
  baseurl_source: spec
  description: Compliance assessment and reporting
  name: Saasment Compliance API
  slug: saasment-compliance-api
- baseURL: https://api.saasment.com/v1
  baseurl_source: spec
  description: Cloud cost analysis and optimization recommendations
  name: Saasment Cost Optimization API
  slug: saasment-cost-optimization-api
- baseURL: https://api.saasment.com/v1
  baseurl_source: spec
  description: SaaS application integration management
  name: Saasment Integrations API
  slug: saasment-integrations-api
- baseURL: https://api.saasment.com/v1
  baseurl_source: spec
  description: Misconfiguration detection and remediation
  name: Saasment Misconfigurations API
  slug: saasment-misconfigurations-api
- baseURL: https://api.saasment.com/v1
  baseurl_source: spec
  description: SaaS security posture assessment and monitoring
  name: Saasment Security Posture API
  slug: saasment-security-posture-api
artifact_total: 30
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Saasment Alerts API
  slug: open-saasment-alerts-api
- collection_type: open
  name: Saasment Alerts Compliance API
  slug: open-saasment-compliance-api
- collection_type: open
  name: Saasment Alerts Cost Optimization API
  slug: open-saasment-cost-optimization-api
- collection_type: open
  name: Saasment Alerts Integrations API
  slug: open-saasment-integrations-api
- collection_type: open
  name: Saasment Alerts Misconfigurations API
  slug: open-saasment-misconfigurations-api
- collection_type: open
  name: Saasment Alerts Security Posture API
  slug: open-saasment-security-posture-api
- collection_type: open
  name: Saasment API
  slug: open-saasment
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/saasment-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/saasment-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/saasment-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/saasment-sspm
- group: company
  title: ''
  type: Website
  url: https://www.saasment.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.saasment.com/resources
- group: company
  title: ''
  type: Blog
  url: https://www.saasment.com/blog
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/saasment-openapi.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/saasment-rules.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/saasment-misconfiguration-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/saasment-application-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/saasment-misconfiguration-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/saasment-application-structure.json
- group: design
  title: ''
  type: JSONLDContext
  url: json-ld/saasment-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/saasment-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://www.saasment.com/llms.txt
created: '2026-03-27'
description: Saasment is an AI-powered SaaS security posture management (SSPM) and cloud cost optimization platform that detects misconfigurations, compliance gaps, and cost inefficiencies across cloud applications. It provides continuous monitoring, automated breach and attack simulation, privileged access management, and seamless integrations with identity management systems and other security tools.
examples:
- key_count: 2
  name: Saasment Get Posture Score Example
  slug: saasment-get-posture-score-example
- key_count: 2
  name: Saasment List Cost Recommendations Example
  slug: saasment-list-cost-recommendations-example
- key_count: 2
  name: Saasment List Misconfigurations Example
  slug: saasment-list-misconfigurations-example
finops:
- name: Saasment Finops
  service_category: API
  slug: saasment-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/saasment.png
json_schemas:
- name: Saasment Monitored Application
  property_count: 8
  slug: saasment-application
- name: Saasment Misconfiguration
  property_count: 11
  slug: saasment-misconfiguration
json_structures:
- name: Saasment Application Structure
  property_count: 0
  slug: saasment-application-structure
- name: Saasment Misconfiguration Structure
  property_count: 0
  slug: saasment-misconfiguration-structure
jsonld:
- class_count: 26
  name: Saasment Context
  property_count: 0
  slug: saasment-context
layout: provider
modified: '2026-05-19'
name: Saasment
nav: Providers
network: true
overview: 'Saasment publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Compliance API, Cost Optimization API, and 3 more. Tagged areas include SaaS Security, SSPM, Cloud Security, Cost Optimization, and Compliance.


  The Saasment catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Saasment''s developer surface includes authentication, documentation, engineering blog, and 13 more developer resources.'
plans:
- name: Saasment Plans Pricing
  plan_count: 3
  slug: saasment-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Saasment Rate Limits
  slug: saasment-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Saasment API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: saasment-jsonschema-spectral-rules
- effective_rule_count: 50
  extends:
  - spectral:oas
  name: Saasment API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: saasment-rules
score:
  band: thin
  composite: 31.3
  coverage:
    artifact_dirs: 17
    catalog_earned: 58.5
    catalog_earned_first_party: 0.0
    catalog_gap: 56.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 28.8
    contract_quality: 56.9
    developer_ergonomics: 11.9
    discoverability: 66.7
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 31.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/saasment/refs/heads/main/screenshots/saasment-2026-06-20T193313.png
security:
- kind: authentication
  name: Saasment Authentication
  slug: saasment-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Saasment Domain Security
  slug: saasment-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: saasment
tags:
- SaaS Security
- SSPM
- Cloud Security
- Cost Optimization
- Compliance
- Misconfigurations
website: https://www.saasment.com
---

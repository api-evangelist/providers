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
    asyncapi_events: false
    auth_clarity: true
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
  score: 30.6
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Saasment Agentic Access
  operation_count: 13
  slug: saasment-agentic-access
  summary_line: 13 operations · 3 acting
api_count: 6
apis:
- description: Security alert and notification management
  name: Saasment Alerts API
  slug: saasment-alerts-api
- description: Compliance assessment and reporting
  name: Saasment Compliance API
  slug: saasment-compliance-api
- description: Cloud cost analysis and optimization recommendations
  name: Saasment Cost Optimization API
  slug: saasment-cost-optimization-api
- description: SaaS application integration management
  name: Saasment Integrations API
  slug: saasment-integrations-api
- description: Misconfiguration detection and remediation
  name: Saasment Misconfigurations API
  slug: saasment-misconfigurations-api
- description: SaaS security posture assessment and monitoring
  name: Saasment Security Posture API
  slug: saasment-security-posture-api
artifact_total: 23
collections:
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
  url: openapi/saasment-openapi.yml
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
- group: other
  title: ''
  type: Capabilities
  url: capabilities/saas-security-posture.yaml
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


  Saasment''s developer surface includes authentication, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Saasment Plans Pricing
  plan_count: 3
  slug: saasment-plans-pricing
random_paper: 40
rate_limits:
- limit_count: 5
  name: Saasment Rate Limits
  slug: saasment-rate-limits
rules:
- name: Saasment API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: saasment-jsonschema-spectral-rules
- name: Saasment API Rules
  rule_count: 9
  severity_counts:
    error: 2
    hint: 0
    info: 2
    warn: 5
  slug: saasment-rules
score:
  band: developing
  composite: 48.2
  delta: -4.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 65.8
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 36.8
  previous_composite: 52.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.6
  scored_at: '2026-07-28'
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

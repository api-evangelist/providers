---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 37.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Vistra Agentic Access
  operation_count: 5
  slug: vistra-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 2
apis:
- description: Document upload URL generation and completion notification
  name: Vistra Documents API
  slug: vistra-documents-api
- description: Company incorporation request submission and management
  name: Vistra Incorporations API
  slug: vistra-incorporations-api
artifact_total: 18
collections:
- collection_type: open
  name: Vistra Incorporations API
  slug: open-vistra-incorporations
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vistra-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vistra-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vistra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vistra-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vistra-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/vistra-energy
- group: company
  title: ''
  type: Website
  url: https://www.vistra.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportal.vistra.com/
- group: operate
  title: ''
  type: Help Center
  url: https://help.vistra.com/en/
- group: start
  title: ''
  type: Client Portals
  url: https://www.vistra.com/client-portals
- group: other
  title: ''
  type: Entity Management
  url: https://www.vistra.com/corporate/entity-management
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.vistra.com/privacy-policy
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/vistra-incorporations-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/vistra-incorporation-schema.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/vistra-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/vistra-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/vistra-rules.yml
- group: company
  title: ''
  type: Blog
  url: https://vistra.com/insights/feed.xml
created: '2026-03-21'
description: Vistra is a global corporate services provider operating in over 45 jurisdictions, offering entity management, incorporation, compliance, payroll, and fund administration services. The Vistra REST API enables developers to programmatically submit company incorporation requests in supported jurisdictions (initially British Virgin Islands), upload supporting documents to pre-signed storage URLs, and integrate Vistra's corporate services into business process workflows. Authentication uses OAuth2 bearer tokens obtained through the Vistra Developer Portal.
examples:
- key_count: 2
  name: Vistra Incorporations Createincorporation Example
  slug: vistra-incorporations-createIncorporation-example
- key_count: 2
  name: Vistra Incorporations Generatedocumentuploadurl Example
  slug: vistra-incorporations-generateDocumentUploadUrl-example
finops:
- name: Vistra Finops
  service_category: Energy / Electricity
  slug: vistra-finops
image: https://www.vistra.com/themes/custom/vistra/logo.svg
json_schemas:
- name: Vistra Incorporation Request
  property_count: 8
  slug: vistra-incorporation
json_structures:
- name: Vistra Incorporation Structure
  property_count: 0
  slug: vistra-incorporation-structure
jsonld:
- class_count: 32
  name: Vistra Context
  property_count: 5
  slug: vistra-context
layout: provider
modified: '2026-05-19'
name: Vistra
nav: Providers
network: true
overview: 'Vistra publishes 2 APIs on the [APIs.io](https://apis.io/) network: Documents API and Incorporations API. Tagged areas include Compliance, Corporate Services, Entity Management, Finance, and Fortune 500.


  The Vistra catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Vistra''s developer surface includes authentication, engineering blog, and 16 more developer resources.'
plans:
- name: Vistra Plans Pricing
  plan_count: 1
  slug: vistra-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 1
  name: Vistra Rate Limits
  slug: vistra-rate-limits
rules:
- name: Vistra API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: vistra-jsonschema-spectral-rules
- name: Vistra API Rules
  rule_count: 11
  severity_counts:
    error: 3
    hint: 1
    info: 0
    warn: 7
  slug: vistra-rules
score:
  band: developing
  composite: 49.7
  delta: -5.1
  facets:
    commercial_clarity: 47.4
    contract_quality: 68.6
    developer_ergonomics: 26.1
    discoverability: 68.5
    governance: 68.8
    operational_transparency: 21.1
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/vistra/refs/heads/main/screenshots/vistra-2026-06-20T201057.png
security:
- kind: authentication
  name: Vistra Authentication
  slug: vistra-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Vistra Domain Security
  slug: vistra-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vistra Vulnerability Disclosure
  slug: vistra-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Vistra Trust Center
  slug: vistra-trust-center
  summary_line: ISO 27001, PCI DSS
slug: vistra
tags:
- Compliance
- Corporate Services
- Entity Management
- Finance
- Fortune 500
- Legal
website: https://www.vistra.com
---

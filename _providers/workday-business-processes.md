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
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.9
  scored_at: '2026-08-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Workday Business Processes Agentic Access
  operation_count: 10
  slug: workday-business-processes-agentic-access
  summary_line: 10 operations · 4 acting
api_count: 4
apis:
- description: Manage approval steps and approval chains
  name: Workday Business Processes Approvals API
  slug: workday-business-processes-approvals-api
- description: Retrieve and manage business process type definitions
  name: Workday Business Processes Business Process Definitions API
  slug: workday-business-processes-business-process-definitions-api
- description: Manage user inbox items requiring action
  name: Workday Business Processes Inbox Items API
  slug: workday-business-processes-inbox-items-api
- description: Manage running business process instances
  name: Workday Business Processes Process Instances API
  slug: workday-business-processes-process-instances-api
artifact_total: 41
collections:
- collection_type: postman
  name: Workday Business Process Approvals API
  slug: postman-workday-business-processes-approvals-api
- collection_type: postman
  name: Workday Business Process Approvals Business Process Definitions API
  slug: postman-workday-business-processes-business-process-definitions-api
- collection_type: postman
  name: Workday Business Process Approvals Inbox Items API
  slug: postman-workday-business-processes-inbox-items-api
- collection_type: postman
  name: Workday Business Process Approvals Process Instances API
  slug: postman-workday-business-processes-process-instances-api
- collection_type: open
  name: Workday Business Process API
  slug: open-workday-business-processes
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/workday-business-processes/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/workday-business-processes-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/workday-business-processes-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/workday-business-processes-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/workday-business-processes-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/workday-business-processes-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://community.workday.com
- group: start
  title: ''
  type: GettingStarted
  url: https://doc.workday.com/admin-guide/en-us/workday-web-services/wws-overview/getting-started-with-workday-web-services.html
- group: other
  title: ''
  type: API Standards
  url: https://doc.workday.com/admin-guide/en-us/workday-rest-api/workday-rest-api-overview.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.workday.com/en-us/privacy.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.workday.com/en-us/terms-of-service.html
- group: auth
  title: ''
  type: Security
  url: https://www.workday.com/en-us/why-workday/our-technology/security.html
- group: design
  title: ''
  type: JSONLD
  url: json-ld/workday-business-processes-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/workday-business-processes-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/workday-business-processes-vocabulary.yml
created: '2024-01-01'
description: APIs for managing and executing business processes within Workday, including initiating, monitoring, and completing various workflow processes.
examples:
- key_count: 2
  name: Workday Business Processes Approval Request Example
  slug: workday-business-processes-approval-request-example
- key_count: 7
  name: Workday Business Processes Business Process Definition Example
  slug: workday-business-processes-business-process-definition-example
- key_count: 2
  name: Workday Business Processes Denial Request Example
  slug: workday-business-processes-denial-request-example
- key_count: 8
  name: Workday Business Processes Inbox Item Example
  slug: workday-business-processes-inbox-item-example
- key_count: 4
  name: Workday Business Processes Initiate Process Request Example
  slug: workday-business-processes-initiate-process-request-example
- key_count: 9
  name: Workday Business Processes Process Instance Example
  slug: workday-business-processes-process-instance-example
- key_count: 7
  name: Workday Business Processes Process Step Example
  slug: workday-business-processes-process-step-example
finops:
- name: Workday Business Processes Finops
  service_category: API
  slug: workday-business-processes-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/workday-business-processes.png
json_schemas:
- name: Approval Request
  property_count: 2
  slug: workday-business-processes-approval-request
- name: Business Process Definition
  property_count: 6
  slug: workday-business-processes-business-process-definition
- name: Denial Request
  property_count: 2
  slug: workday-business-processes-denial-request
- name: Inbox Item
  property_count: 10
  slug: workday-business-processes-inbox-item
- name: Initiate Process Request
  property_count: 4
  slug: workday-business-processes-initiate-process-request
- name: Process Instance
  property_count: 11
  slug: workday-business-processes-process-instance
- name: Process Step
  property_count: 8
  slug: workday-business-processes-process-step
json_structures:
- name: Workday Business Processes Approval Request Structure
  property_count: 2
  slug: workday-business-processes-approval-request-structure
- name: Workday Business Processes Business Process Definition Structure
  property_count: 6
  slug: workday-business-processes-business-process-definition-structure
- name: Workday Business Processes Denial Request Structure
  property_count: 2
  slug: workday-business-processes-denial-request-structure
- name: Workday Business Processes Inbox Item Structure
  property_count: 10
  slug: workday-business-processes-inbox-item-structure
- name: Workday Business Processes Initiate Process Request Structure
  property_count: 4
  slug: workday-business-processes-initiate-process-request-structure
- name: Workday Business Processes Process Instance Structure
  property_count: 11
  slug: workday-business-processes-process-instance-structure
- name: Workday Business Processes Process Step Structure
  property_count: 8
  slug: workday-business-processes-process-step-structure
jsonld:
- class_count: 31
  name: Workday Business Processes Context
  property_count: 11
  slug: workday-business-processes-context
layout: provider
modified: '2026-05-19'
name: Workday Business Processes
nav: Providers
network: true
overview: 'Workday Business Processes publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Approvals API, Business Process Definitions API, Inbox Items API, and 1 more.


  The Workday Business Processes catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Workday Business Processes'' developer surface includes authentication, developer portal, getting-started guide, and 12 more developer resources.'
plans:
- name: Workday Business Processes Plans Pricing
  plan_count: 3
  slug: workday-business-processes-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 5
  name: Workday Business Processes Rate Limits
  slug: workday-business-processes-rate-limits
rules:
- name: Workday Business Processes API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: workday-business-processes-jsonschema-spectral-rules
- name: Workday Business Processes API Rules
  rule_count: 44
  severity_counts:
    error: 8
    hint: 0
    info: 9
    warn: 27
  slug: workday-business-processes-spectral-rules
scopes:
- name: Workday Business Processes Scopes
  scope_count: 1
  slug: workday-business-processes-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 48.2
  delta: 0.0
  facets:
    commercial_clarity: 68.4
    contract_quality: 32.9
    developer_ergonomics: 34.8
    discoverability: 55.6
    governance: 68.8
    operational_transparency: 42.1
  previous_composite: 48.2
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-06'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/workday-business-processes/refs/heads/main/screenshots/workday-business-processes-2026-06-20T201558.png
security:
- kind: authentication
  name: Workday Business Processes Authentication
  slug: workday-business-processes-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Workday Business Processes Domain Security
  slug: workday-business-processes-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Workday Business Processes Trust Center
  slug: workday-business-processes-trust-center
  summary_line: SOC 2, ISO 27001, FedRAMP, GDPR
slug: workday-business-processes
website: https://community.workday.com
---

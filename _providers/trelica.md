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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 29.1
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Trelica Agentic Access
  operation_count: 13
  slug: trelica-agentic-access
  summary_line: 13 operations · 2 acting
api_count: 8
apis:
- description: Manage users associated with specific applications
  name: Trelica Application Users API
  slug: trelica-application-users-api
- description: Manage and query SaaS applications in the Trelica catalog
  name: Trelica Applications API
  slug: trelica-applications-api
- description: Manage software and hardware assets
  name: Trelica Assets API
  slug: trelica-assets-api
- description: Access audit trail of changes and events
  name: Trelica Audit Log API
  slug: trelica-audit-log-api
- description: Manage software contracts and renewals
  name: Trelica Contracts API
  slug: trelica-contracts-api
- description: Manage people/employees within the organization
  name: Trelica People API
  slug: trelica-people-api
- description: User provisioning via SCIM 2.0 protocol
  name: Trelica Users (SCIM) API
  slug: trelica-users-scim-api
- description: Manage automation workflows
  name: Trelica Workflows API
  slug: trelica-workflows-api
artifact_total: 34
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Trelica REST Application Users API
  slug: open-trelica-application-users-api
- collection_type: open
  name: Trelica REST Application Users Applications API
  slug: open-trelica-applications-api
- collection_type: open
  name: Trelica REST Application Users Assets API
  slug: open-trelica-assets-api
- collection_type: open
  name: Trelica REST Application Users Audit Log API
  slug: open-trelica-audit-log-api
- collection_type: open
  name: Trelica REST Application Users Contracts API
  slug: open-trelica-contracts-api
- collection_type: open
  name: Trelica REST Application Users People API
  slug: open-trelica-people-api
- collection_type: open
  name: Trelica REST API
  slug: open-trelica-rest-api
- collection_type: open
  name: Trelica REST Application Users Users (SCIM) API
  slug: open-trelica-users-scim-api
- collection_type: open
  name: Trelica REST Application Users Workflows API
  slug: open-trelica-workflows-api
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/trelica/trelica-api-sdk/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/trelica-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/trelica-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/trelica-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/trelica-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/trelica
- group: company
  title: ''
  type: Website
  url: https://www.trelica.com
- group: docs
  title: ''
  type: Documentation
  url: https://trelica.gitbook.io/trelica-api
- group: operate
  title: ''
  type: HelpCenter
  url: https://help.trelica.com/hc/en-us/sections/7739034184093-API
- group: auth
  title: ''
  type: Authentication
  url: https://help.trelica.com/hc/en-us/articles/7739283478941-Trelica-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/trelica
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trelica/trelica-api-sdk
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trelica/node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/trelica/powershell
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trelica-application-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trelica-person-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/trelica-contract-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/trelica-application-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/trelica-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/trelica-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/trelica-vocabulary.yml
created: '2026-03-27'
description: Trelica is a SaaS management platform (now part of 1Password SaaS Manager) providing application discovery, license optimization, contract management, and workflow automation for IT teams. The platform offers a REST API covering applications, users, people, contracts, workflows, assets, and audit logs with OAuth 2.0 authentication using Client Credentials and Authorization Code flows.
examples:
- key_count: 2
  name: Trelica List Applications Example
  slug: trelica-list-applications-example
- key_count: 2
  name: Trelica List People Example
  slug: trelica-list-people-example
finops:
- name: Trelica Finops
  service_category: API
  slug: trelica-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/trelica.png
json_schemas:
- name: Trelica Application
  property_count: 10
  slug: trelica-application
- name: Trelica Contract
  property_count: 10
  slug: trelica-contract
- name: Trelica Person
  property_count: 10
  slug: trelica-person
json_structures:
- name: Trelica Application Structure
  property_count: 0
  slug: trelica-application-structure
jsonld:
- class_count: 23
  name: Trelica Context
  property_count: 15
  slug: trelica-context
layout: provider
modified: '2026-05-19'
name: Trelica
nav: Providers
network: true
overview: 'Trelica publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Application Users API, Applications API, Assets API, and 5 more. Tagged areas include Contract Management, IT Management, License Management, SaaS Management, and Software Asset Management.


  The Trelica catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Trelica''s developer surface includes authentication, documentation, and 19 more developer resources.'
plans:
- name: Trelica Plans Pricing
  plan_count: 3
  slug: trelica-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 5
  name: Trelica Rate Limits
  slug: trelica-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Trelica API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: trelica-jsonschema-spectral-rules
- effective_rule_count: 62
  extends:
  - spectral:oas
  name: Trelica API Rules
  rule_count: 21
  severity_counts:
    error: 3
    hint: 0
    info: 5
    warn: 13
  slug: trelica-spectral-rules
scopes:
- name: Trelica Scopes
  scope_count: 9
  slug: trelica-scopes
  summary_line: 9 scopes · clientCredentials/authorizationCode
score:
  band: thin
  composite: 39.2
  delta: -6.9
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 25.0
    contract_quality: 66.4
    developer_ergonomics: 38.1
    discoverability: 74.1
    governance: 25.0
    operational_transparency: 10.5
  previous_composite: 46.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/trelica/refs/heads/main/screenshots/trelica-2026-06-20T195649.png
security:
- kind: authentication
  name: Trelica Authentication
  slug: trelica-authentication
  summary_line: oauth2 · 2 schemes
- kind: domain-security
  name: Trelica Domain Security
  slug: trelica-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: trelica
tags:
- Contract Management
- IT Management
- License Management
- SaaS Management
- Software Asset Management
website: https://www.trelica.com
---

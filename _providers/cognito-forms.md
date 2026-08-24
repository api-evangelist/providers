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
  scored_at: '2026-08-24'
agentic_access:
- acting_count: 10
  human_in_the_loop: 0
  name: Cognito Forms Agentic Access
  operation_count: 17
  slug: cognito-forms-agentic-access
  summary_line: 17 operations · 10 acting
api_count: 5
apis:
- description: The Entries API from Cognito Forms — 5 operation(s) for entries.
  name: Cognito Forms Entries API
  slug: cognito-forms-entries-api
- description: The Files API from Cognito Forms — 2 operation(s) for files.
  name: Cognito Forms Files API
  slug: cognito-forms-files-api
- description: The Forms API from Cognito Forms — 3 operation(s) for forms.
  name: Cognito Forms Forms API
  slug: cognito-forms-forms-api
- description: The OData API from Cognito Forms — 1 operation(s) for odata.
  name: Cognito Forms OData API
  slug: cognito-forms-odata-api
- description: The Webhooks API from Cognito Forms — 4 operation(s) for webhooks.
  name: Cognito Forms Webhooks API
  slug: cognito-forms-webhooks-api
artifact_total: 28
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Cognito Forms Entries API
  slug: open-cognito-forms-entries-api
- collection_type: open
  name: Cognito Forms Entries Files API
  slug: open-cognito-forms-files-api
- collection_type: open
  name: Cognito Entries Forms API
  slug: open-cognito-forms-forms-api
- collection_type: open
  name: Cognito Forms Entries OData API
  slug: open-cognito-forms-odata-api
- collection_type: open
  name: Cognito Forms Entries Webhooks API
  slug: open-cognito-forms-webhooks-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/cognito-forms-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/cognito-forms-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/cognito-forms-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/cognito-forms-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.cognitoforms.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.cognitoforms.com/support/475/data-integration/cognito-forms-api
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/cognitoforms
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/cognito-forms
- group: company
  title: ''
  type: Blog
  url: https://www.cognitoforms.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.cognitoforms.com/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://x.com/CognitoStatus
- group: other
  title: ''
  type: X
  url: https://twitter.com/cognitoforms
- group: commercial
  title: ''
  type: Plans
  url: plans/cognito-forms-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/cognito-forms-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/cognito-forms-finops.yml
created: '2026-06-13'
description: Cognito Forms is an online form builder with a REST API for managing forms, retrieving entries, updating submissions, and integrating form data into business applications. The API uses API key bearer token authentication and supports operations for forms, entries, and documents, with OData support for analytics tool integration.
examples:
- key_count: 3
  name: Create Entry Example
  slug: create-entry-example
- key_count: 3
  name: Get Forms Example
  slug: get-forms-example
- key_count: 3
  name: Import Entries Example
  slug: import-entries-example
finops:
- name: Cognito Forms Finops
  service_category: ''
  slug: cognito-forms-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/cognito-forms.png
json_schemas:
- name: Error
  property_count: 4
  slug: error
- name: FileDataRef
  property_count: 6
  slug: file-data-ref
- name: FormAvailability
  property_count: 3
  slug: form-availability
- name: FormReference
  property_count: 2
  slug: form-reference
- name: ImportStatus
  property_count: 7
  slug: import-status
jsonld:
- class_count: 11
  name: Cognito Forms Context
  property_count: 23
  slug: cognito-forms-context
layout: provider
modified: '2026-06-13'
name: Cognito Forms
nav: Providers
network: true
overview: 'Cognito Forms publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Entries API, Files API, Forms API, and 2 more. Tagged areas include Forms, Form Builder, Form Entries, Workflow-Automation, and Data Collection.


  The Cognito Forms catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cognito Forms'' developer surface includes authentication, documentation, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Cognito Forms Plans Pricing
  plan_count: 4
  slug: cognito-forms-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 3
  name: Cognito Forms Rate Limits
  slug: cognito-forms-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Cognito Forms API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: cognito-forms-jsonschema-spectral-rules
scopes:
- name: Cognito Forms Scopes
  scope_count: 1
  slug: cognito-forms-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: developing
  composite: 46.4
  delta: 0.0
  facets:
    access_clarity: 50.0
    commercial_clarity: 50.0
    contract_governance: 9.8
    contract_quality: 65.0
    developer_ergonomics: 23.8
    discoverability: 74.1
    governance: 9.8
    operational_transparency: 52.6
  previous_composite: 46.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/cognito-forms/refs/heads/main/screenshots/cognito-forms-2026-06-20T174716.png
security:
- kind: authentication
  name: Cognito Forms Authentication
  slug: cognito-forms-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Cognito Forms Domain Security
  slug: cognito-forms-domain-security
  summary_line: TLSv1.3 · DMARC
slug: cognito-forms
tags:
- Forms
- Form Builder
- Form Entries
- Workflow-Automation
- Data Collection
- OData
website: https://www.cognitoforms.com
---

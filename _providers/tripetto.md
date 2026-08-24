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
- acting_count: 5
  human_in_the_loop: 0
  name: Tripetto Agentic Access
  operation_count: 10
  slug: tripetto-agentic-access
  summary_line: 10 operations · 5 acting
api_count: 4
apis:
- description: Tripetto supports outbound webhooks that deliver form response data to external services and automation platforms including Make, Zapier, and Pabbly Connect. Custom webhook endpoints receive form subm
  name: Tripetto Webhooks
  slug: tripetto-webhooks
- description: Create and manage form definitions
  name: Tripetto Forms API
  slug: tripetto-forms-api
- description: Access collected form response data
  name: Tripetto Responses API
  slug: tripetto-responses-api
- description: Configure outbound webhook integrations
  name: Tripetto Webhooks API
  slug: tripetto-webhooks-api
artifact_total: 26
collections:
- collection_type: postman
  name: Tripetto FormBuilder SDK Forms API
  slug: postman-tripetto-forms-api
- collection_type: postman
  name: Tripetto FormBuilder SDK Forms Responses API
  slug: postman-tripetto-responses-api
- collection_type: postman
  name: Tripetto FormBuilder SDK Forms Webhooks API
  slug: postman-tripetto-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Tripetto FormBuilder SDK API
  slug: open-tripetto-form-builder
- collection_type: open
  name: Tripetto FormBuilder SDK Forms API
  slug: open-tripetto-forms-api
- collection_type: open
  name: Tripetto FormBuilder SDK Forms Responses API
  slug: open-tripetto-responses-api
- collection_type: open
  name: Tripetto FormBuilder SDK Forms Webhooks API
  slug: open-tripetto-webhooks-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/tripetto/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/tripetto-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/tripetto-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/tripetto-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://tripetto.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/tripetto
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/tripetto
- group: company
  title: ''
  type: Website
  url: https://tripetto.com/
- group: docs
  title: ''
  type: Documentation
  url: https://tripetto.com/sdk/docs/
- group: operate
  title: ''
  type: Help Center
  url: https://tripetto.com/help/
- group: learn
  title: ''
  type: Tutorials
  url: https://tripetto.com/tutorials/
- group: commercial
  title: ''
  type: Pricing
  url: https://tripetto.com/pricing/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://gitlab.com/tripetto
- group: build
  title: ''
  type: npm Organization
  url: https://www.npmjs.com/org/tripetto
- group: start
  title: ''
  type: Login
  url: https://tripetto.com/app/sign-in/
- group: start
  title: ''
  type: Signup
  url: https://tripetto.com/app/sign-up/
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/tripetto-form-builder-openapi.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tripetto-form-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/tripetto-response-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/tripetto-form-structure.json
- group: design
  title: ''
  type: JSONLD
  url: json-ld/tripetto-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/tripetto-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/tripetto-vocabulary.yml
created: '2026-03-16'
description: Tripetto is a powerful form builder platform and SDK that enables developers to create smart, conversational forms and surveys with advanced conditional logic. The platform provides a JavaScript/TypeScript SDK for embedding form builders and runners into web applications, along with webhook capabilities for delivering form responses to external services and automation platforms.
examples:
- key_count: 3
  name: Tripetto List Form Responses Example
  slug: tripetto-list-form-responses-example
- key_count: 3
  name: Tripetto List Forms Example
  slug: tripetto-list-forms-example
finops:
- name: Tripetto Finops
  service_category: API
  slug: tripetto-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/tripetto.png
json_schemas:
- name: Tripetto Form
  property_count: 7
  slug: tripetto-form
- name: Tripetto Form Response
  property_count: 5
  slug: tripetto-response
json_structures:
- name: Tripetto Form Structure
  property_count: 0
  slug: tripetto-form-structure
jsonld:
- class_count: 29
  name: Tripetto Context
  property_count: 0
  slug: tripetto-context
layout: provider
modified: '2026-05-19'
name: Tripetto
nav: Providers
network: true
overview: 'Tripetto publishes 3 APIs on the [APIs.io](https://apis.io/) network: Forms API, Responses API, and Webhooks API. Tagged areas include Forms, Surveys, Form Builder, No-Code, and SDK.


  The Tripetto catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Tripetto''s developer surface includes authentication, engineering blog, documentation, pricing, signup flow, and 18 more developer resources.'
plans:
- name: Tripetto Plans Pricing
  plan_count: 3
  slug: tripetto-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Tripetto Rate Limits
  slug: tripetto-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Tripetto API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: tripetto-jsonschema-spectral-rules
- effective_rule_count: 49
  extends:
  - spectral:oas
  name: Tripetto API Rules
  rule_count: 8
  severity_counts:
    error: 2
    hint: 0
    info: 1
    warn: 5
  slug: tripetto-rules
score:
  band: developing
  composite: 42.7
  delta: 0.0
  facets:
    access_clarity: 27.6
    commercial_clarity: 27.6
    contract_governance: 28.8
    contract_quality: 73.2
    developer_ergonomics: 33.3
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 42.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.12.1
  scored_at: '2026-08-24'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/tripetto/refs/heads/main/screenshots/tripetto-2026-06-20T195723.png
security:
- kind: authentication
  name: Tripetto Authentication
  slug: tripetto-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Tripetto Domain Security
  slug: tripetto-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tripetto
tags:
- Forms
- Surveys
- Form Builder
- No-Code
- SDK
- Webhook
website: https://tripetto.com/
---

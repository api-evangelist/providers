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
    event_surface_described: derived
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.3
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Wufoo Agentic Access
  operation_count: 18
  slug: wufoo-agentic-access
  summary_line: 18 operations · 4 acting
api_count: 10
apis:
- description: Wufoo webhooks POST form-submission payloads to a subscriber URL at the moment an entry is created. Up to 10 webhooks per form, with optional handshake key for verification and optional metadata for r
  name: Wufoo Webhooks
  slug: wufoo-webhooks
- description: Read comments attached to entries.
  name: Wufoo Comments API
  slug: wufoo-comments-api
- description: Read and create form submissions.
  name: Wufoo Entries API
  slug: wufoo-entries-api
- description: Read the field structure of a form or report.
  name: Wufoo Fields API
  slug: wufoo-fields-api
- description: Read forms and their metadata.
  name: Wufoo Forms API
  slug: wufoo-forms-api
- description: Exchange credentials for an API key.
  name: Wufoo Login API
  slug: wufoo-login-api
- description: Read reports built on top of forms.
  name: Wufoo Reports API
  slug: wufoo-reports-api
- description: Read account user information.
  name: Wufoo Users API
  slug: wufoo-users-api
- description: Subscribe to and unsubscribe from form submission webhooks.
  name: Wufoo Webhooks API
  slug: wufoo-webhooks-api
- description: Read widgets inside reports.
  name: Wufoo Widgets API
  slug: wufoo-widgets-api
arazzos:
- description: Confirm a form exists, then subscribe a URL to its submission webhook.
  name: Wufoo Add a Form Webhook
  slug: wufoo-add-form-webhook-workflow
- description: Resolve a form, check its entry count, then page through its entries.
  name: Wufoo Browse Form Entries
  slug: wufoo-browse-form-entries-workflow
- description: Resolve a form, count its comments, then list them when any exist.
  name: Wufoo Moderate Form Comments
  slug: wufoo-moderate-form-comments-workflow
- description: Exchange a user's credentials for their API key, then list that user's forms.
  name: Wufoo Provision Builder User Forms
  slug: wufoo-provision-builder-user-forms-workflow
- description: Resolve a report, read its field structure, then pull its filtered entries.
  name: Wufoo Export Report Entries
  slug: wufoo-report-entries-export-workflow
- description: List reports, count a report's entries, then fetch them when non-empty.
  name: Wufoo Report Entry Stats
  slug: wufoo-report-entry-stats-workflow
- description: Resolve a report, list its widgets, then read its underlying field structure.
  name: Wufoo Report Widget Overview
  slug: wufoo-report-widget-overview-workflow
- description: Add a fresh webhook subscription, then delete the prior one by hash.
  name: Wufoo Rotate a Form Webhook
  slug: wufoo-rotate-form-webhook-workflow
- description: Discover a form, read its field structure, then submit a new entry.
  name: Wufoo Submit a Form Entry
  slug: wufoo-submit-form-entry-workflow
artifact_total: 64
asyncapis:
- description: Wufoo webhooks POST a form-submission payload to a subscriber URL the moment an entry is created. Each form supports up to 10 active webhooks. When the subscription is created with `metadata=true`, th
  name: Wufoo Webhooks
  slug: wufoo-webhooks-asyncapi
collections:
- collection_type: postman
  name: Wufoo REST Comments API
  slug: postman-wufoo-comments-api
- collection_type: postman
  name: Wufoo REST Comments Entries API
  slug: postman-wufoo-entries-api
- collection_type: postman
  name: Wufoo REST Comments Fields API
  slug: postman-wufoo-fields-api
- collection_type: postman
  name: Wufoo REST Comments Forms API
  slug: postman-wufoo-forms-api
- collection_type: postman
  name: Wufoo REST Comments Login API
  slug: postman-wufoo-login-api
- collection_type: postman
  name: Wufoo REST Comments Reports API
  slug: postman-wufoo-reports-api
- collection_type: postman
  name: Wufoo REST Comments Users API
  slug: postman-wufoo-users-api
- collection_type: postman
  name: Wufoo REST Comments Webhooks API
  slug: postman-wufoo-webhooks-api
- collection_type: postman
  name: Wufoo REST Comments Widgets API
  slug: postman-wufoo-widgets-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Wufoo REST Comments API
  slug: open-wufoo-comments-api
- collection_type: open
  name: Wufoo REST Comments Entries API
  slug: open-wufoo-entries-api
- collection_type: open
  name: Wufoo REST Comments Fields API
  slug: open-wufoo-fields-api
- collection_type: open
  name: Wufoo REST Comments Forms API
  slug: open-wufoo-forms-api
- collection_type: open
  name: Wufoo REST Comments Login API
  slug: open-wufoo-login-api
- collection_type: open
  name: Wufoo REST Comments Reports API
  slug: open-wufoo-reports-api
- collection_type: open
  name: Wufoo REST API
  slug: open-wufoo-rest-v3
- collection_type: open
  name: Wufoo REST Comments Users API
  slug: open-wufoo-users-api
- collection_type: open
  name: Wufoo REST Comments Webhooks API
  slug: open-wufoo-webhooks-api
- collection_type: open
  name: Wufoo REST Comments Widgets API
  slug: open-wufoo-widgets-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/wufoo/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/wufoo-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/wufoo-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/wufoo-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-add-form-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-browse-form-entries-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-moderate-form-comments-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-provision-builder-user-forms-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-report-entries-export-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-report-entry-stats-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-report-widget-overview-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-rotate-form-webhook-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/wufoo-submit-form-entry-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://www.wufoo.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://wufoo.github.io/docs/
- group: docs
  title: ''
  type: Documentation
  url: https://wufoo.github.io/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://wufoo.github.io/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://help.surveymonkey.com/en/wufoo/integrations/wufoo-api/
- group: start
  title: ''
  type: Signup
  url: https://www.wufoo.com/signup/
- group: start
  title: ''
  type: Login
  url: https://www.wufoo.com/login/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.wufoo.com/pricing/
- group: commercial
  title: ''
  type: Plans
  url: plans/wufoo-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/wufoo-rate-limits.yml
- group: company
  title: ''
  type: Blog
  url: https://www.wufoo.com/blog/
- group: other
  title: ''
  type: RSS
  url: https://www.wufoo.com/blog/feed/
- group: operate
  title: ''
  type: Support
  url: https://help.surveymonkey.com/wufoo/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.wufoo.com/
- group: operate
  title: ''
  type: StatusRSS
  url: https://status.wufoo.com/history.rss
- group: operate
  title: ''
  type: StatusAtom
  url: https://status.wufoo.com/history.atom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.wufoo.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.wufoo.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/wufoo
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/wufoo-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/wufoo-context.jsonld
- group: commercial
  title: ''
  type: FinOps
  url: finops/wufoo-finops.yml
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wufoo/Wufoo-PHP-API-Wrapper
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wufoo/pyfoo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wufoo/wuparty
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wufoo/j-woo
- group: build
  title: ''
  type: SDKs
  url: https://github.com/wufoo/Wufoo-jQuery-API-Wrapper
created: '2026-05-23'
description: Wufoo is an online form-builder owned by SurveyMonkey Inc. It lets non-developers build registration forms, surveys, contact forms, application forms, and payment forms through a drag-and-drop interface, then collect and report on submissions. Wufoo exposes a v3 REST API (Basic Auth, JSON/XML) over Forms, Entries, Fields, Users, Reports, Widgets, Comments, and Webhooks, plus push webhooks that POST form data to subscriber URLs at submission time.
examples:
- key_count: 2
  name: Wufoo Rest V3 List Entries Example
  slug: wufoo-rest-v3-list-entries-example
- key_count: 2
  name: Wufoo Rest V3 List Form Fields Example
  slug: wufoo-rest-v3-list-form-fields-example
- key_count: 2
  name: Wufoo Rest V3 List Forms Example
  slug: wufoo-rest-v3-list-forms-example
- key_count: 2
  name: Wufoo Rest V3 Put Webhook Example
  slug: wufoo-rest-v3-put-webhook-example
- key_count: 2
  name: Wufoo Rest V3 Submit Entry Example
  slug: wufoo-rest-v3-submit-entry-example
- key_count: 4
  name: Wufoo Webhooks Form Submission Example
  slug: wufoo-webhooks-form-submission-example
finops:
- name: Wufoo Finops
  service_category: ''
  slug: wufoo-finops
image: https://www.wufoo.com/images/wufoo-logo.png
json_schemas:
- name: Wufoo Entry
  property_count: 11
  slug: wufoo-entry
- name: Wufoo Field
  property_count: 11
  slug: wufoo-field
- name: Wufoo Form
  property_count: 16
  slug: wufoo-form
- name: Wufoo Report
  property_count: 11
  slug: wufoo-report
- name: Wufoo User
  property_count: 12
  slug: wufoo-user
- name: Wufoo Webhook Payload
  property_count: 8
  slug: wufoo-webhook-payload
json_structures:
- name: Wufoo Entry Structure
  property_count: 0
  slug: wufoo-entry-structure
- name: Wufoo Form Structure
  property_count: 0
  slug: wufoo-form-structure
jsonld:
- class_count: 43
  name: Wufoo Context
  property_count: 0
  slug: wufoo-context
layout: provider
modified: '2026-05-23'
name: Wufoo
nav: Providers
network: true
overview: 'Wufoo publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Webhooks, Comments API, Entries API, and 7 more. Tagged areas include Forms, Form Builder, Surveys, Data Collection, and Webhooks.


  The Wufoo catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Wufoo''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, signup flow, pricing, and 33 more developer resources.'
plans:
- name: Wufoo Plans Pricing
  plan_count: 5
  slug: wufoo-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 0
  name: Wufoo Rate Limits
  slug: wufoo-rate-limits
rules:
- effective_rule_count: 30
  extends:
  - spectral:asyncapi
  name: Wufoo API Rules
  rule_count: 3
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 1
  slug: wufoo-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Wufoo API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: wufoo-jsonschema-spectral-rules
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Wufoo API Rules
  rule_count: 7
  severity_counts:
    error: 4
    hint: 0
    info: 1
    warn: 2
  slug: wufoo-rest-v3-rules
score:
  band: strong
  composite: 60.5
  delta: -0.6
  facets:
    access_clarity: 67.1
    commercial_clarity: 67.1
    contract_governance: 28.8
    contract_quality: 72.3
    developer_ergonomics: 78.6
    discoverability: 74.1
    governance: 28.8
    operational_transparency: 18.4
  previous_composite: 61.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 32.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/wufoo/refs/heads/main/screenshots/wufoo-2026-06-20T201637.png
security:
- kind: authentication
  name: Wufoo Authentication
  slug: wufoo-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Wufoo Domain Security
  slug: wufoo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: wufoo
tags:
- Forms
- Form Builder
- Surveys
- Data Collection
- Webhooks
- Payments
- SurveyMonkey
website: https://wufoo.github.io/docs/
---

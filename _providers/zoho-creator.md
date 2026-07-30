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
- acting_count: 10
  human_in_the_loop: 0
  name: Zoho Creator Agentic Access
  operation_count: 27
  slug: zoho-creator-agentic-access
  summary_line: 27 operations · 10 acting
api_count: 6
apis:
- description: APIs to insert a large set of data into a form
  name: Zoho Creator Bulk Insert APIs API
  slug: zoho-creator-bulk-insert-apis-api
- description: APIs to fetch a large set of data in a report
  name: Zoho Creator Bulk Read APIs API
  slug: zoho-creator-bulk-read-apis-api
- description: APIs to add, update, delete or get records in a form/report
  name: Zoho Creator Data APIs API
  slug: zoho-creator-data-apis-api
- description: APIs to upload or download files in a report
  name: Zoho Creator File APIs API
  slug: zoho-creator-file-apis-api
- description: Get list of applications, forms, reports and fields
  name: Zoho Creator Meta APIs API
  slug: zoho-creator-meta-apis-api
- description: APIs to add or get records in a published form/report
  name: Zoho Creator Publish APIs API
  slug: zoho-creator-publish-apis-api
artifact_total: 25
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/zoho-creator-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-creator-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-creator-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/zoho-creator-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/zoho-creator-scopes.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/creator/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/creator/help/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/showcase/zohocreator/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/creator
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/creator/pricing.html
- group: operate
  title: ''
  type: StatusPage
  url: https://zohostatus.com/
- group: other
  title: ''
  type: X
  url: https://twitter.com/ZohoCreator
- group: commercial
  title: ''
  type: Plans
  url: plans/zoho-creator-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/zoho-creator-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/zoho-creator-finops.yml
created: '2026-06-13'
description: Zoho Creator is a low-code application development platform with a REST API for managing forms, records, reports, workflows, and custom application data. The API enables developers to perform CRUD operations on application data, upload and download files, retrieve metadata about forms and reports, execute custom server-side functions, and build custom API endpoints. It uses OAuth 2.0 for authentication and supports Data APIs, Publish APIs, File APIs, Meta APIs, Bulk Read APIs, and Custom APIs with an OpenAPI 3.0 specification available for download.
examples:
- key_count: 1
  name: Add Record Request
  slug: add-record-request
- key_count: 3
  name: Add Record Response
  slug: add-record-response
- key_count: 2
  name: Bulk Insert Request
  slug: bulk-insert-request
- key_count: 3
  name: Bulk Job Status Response
  slug: bulk-job-status-response
- key_count: 3
  name: Get Form Fields Response
  slug: get-form-fields-response
- key_count: 3
  name: Get Records Response
  slug: get-records-response
finops:
- name: Zoho Creator Finops
  service_category: ''
  slug: zoho-creator-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-creator.png
json_schemas:
- name: Zoho Creator API Response
  property_count: 3
  slug: zoho-creator-api-response
- name: Zoho Creator Bulk Job
  property_count: 5
  slug: zoho-creator-bulk-job
- name: Zoho Creator Record
  property_count: 5
  slug: zoho-creator-record
jsonld:
- class_count: 0
  name: Zoho Creator Context
  property_count: 25
  slug: zoho-creator-context
layout: provider
modified: '2026-06-13'
name: Zoho Creator
nav: Providers
network: true
overview: 'Zoho Creator publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Bulk Insert APIs API, Bulk Read APIs API, Data APIs API, and 3 more. Tagged areas include Low-Code, Application Development, No-Code, Forms, and Records.


  The Zoho Creator catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zoho Creator''s developer surface includes authentication, documentation, engineering blog, pricing, and 12 more developer resources.'
plans:
- name: Zoho Creator Plans Pricing
  plan_count: 6
  slug: zoho-creator-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Zoho Creator Rate Limits
  slug: zoho-creator-rate-limits
rules:
- name: Zoho Creator API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: zoho-creator-jsonschema-spectral-rules
scopes:
- name: Zoho Creator Scopes
  scope_count: 10
  slug: zoho-creator-scopes
  summary_line: 10 scopes · authorizationCode
score:
  band: developing
  composite: 47.3
  delta: -4.9
  facets:
    commercial_clarity: 50.0
    contract_quality: 63.1
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 58.3
    operational_transparency: 21.1
  previous_composite: 52.2
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
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-creator/refs/heads/main/screenshots/zoho-creator-2026-06-20T201937.png
security:
- kind: authentication
  name: Zoho Creator Authentication
  slug: zoho-creator-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Zoho Creator Domain Security
  slug: zoho-creator-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Creator Vulnerability Disclosure
  slug: zoho-creator-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-creator
tags:
- Low-Code
- Application Development
- No-Code
- Forms
- Records
- Workflows
- Database
- CRUD
- Business Applications
website: https://www.zoho.com/creator/
---

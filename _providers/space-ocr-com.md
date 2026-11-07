---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Space Ocr Com Agentic Access
  operation_count: 23
  slug: space-ocr-com-agentic-access
  summary_line: 23 operations · 14 acting
api_count: 1
apis:
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Amount API from space-ocr-com — 1 operation(s) for amount.
  name: space-ocr-com Amount API
  slug: space-ocr-com-amount-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Create API from space-ocr-com — 1 operation(s) for create.
  name: space-ocr-com Create API
  slug: space-ocr-com-create-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Edit API from space-ocr-com — 1 operation(s) for edit.
  name: space-ocr-com Edit API
  slug: space-ocr-com-edit-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Health API from space-ocr-com — 1 operation(s) for health.
  name: space-ocr-com Health API
  slug: space-ocr-com-health-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Jobs API from space-ocr-com — 2 operation(s) for jobs.
  name: space-ocr-com Jobs API
  slug: space-ocr-com-jobs-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Ocr API from space-ocr-com — 3 operation(s) for ocr.
  name: space-ocr-com Ocr API
  slug: space-ocr-com-ocr-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Remove API from space-ocr-com — 1 operation(s) for remove.
  name: space-ocr-com Remove API
  slug: space-ocr-com-remove-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Space API from space-ocr-com — 1 operation(s) for space.
  name: space-ocr-com Space API
  slug: space-ocr-com-space-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Upload API from space-ocr-com — 3 operation(s) for upload.
  name: space-ocr-com Upload API
  slug: space-ocr-com-upload-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The View API from space-ocr-com — 1 operation(s) for view.
  name: space-ocr-com View API
  slug: space-ocr-com-view-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Webhook API from space-ocr-com — 2 operation(s) for webhook.
  name: space-ocr-com Webhook API
  slug: space-ocr-com-webhook-api
- baseURL: https://api.space-ocr.com
  baseurl_source: declared
  description: The Webhooks API from space-ocr-com — 3 operation(s) for webhooks.
  name: space-ocr-com Webhooks API
  slug: space-ocr-com-webhooks-api
artifact_total: 27
common:
- group: agent
  href: https://artifacts.apis.io/space-ocr-com/agentic-access/space-ocr-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/space-ocr-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/space-ocr-com/rate-limits/space-ocr-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/space-ocr-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/space-ocr-com/plans/space-ocr-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/space-ocr-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/rules/space-ocr-com-rules.yml
  title: ''
  type: Spectral
  url: rules/space-ocr-com-rules.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/json-ld/space-ocr-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/space-ocr-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/space-ocr-com/vocabulary/space-ocr-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/space-ocr-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/data-model/space-ocr-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/space-ocr-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/conventions/space-ocr-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/space-ocr-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/conventions/space-ocr-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/space-ocr-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/space-ocr-com/authentication/space-ocr-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/space-ocr-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/errors/space-ocr-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/space-ocr-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/space-ocr-com/conformance/space-ocr-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/space-ocr-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/space-ocr-com/llms/space-ocr-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/space-ocr-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/space-ocr-com/mcp/space-ocr-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/space-ocr-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/space-ocr-com/hosts/space-ocr-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/space-ocr-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/space-ocr-com/vendors/space-ocr-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/space-ocr-com-vendors.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.space-ocr.com<button
- group: auth
  href: https://artifacts.apis.io/space-ocr-com/security/space-ocr-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/space-ocr-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://space-ocr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://space-ocr.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://space-ocr.com/api/
- group: operate
  title: ''
  type: Support
  url: https://space-ocr.com/support/
- group: company
  title: ''
  type: Blog
  url: https://space-ocr.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://space-ocr.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://space-ocr.com/login/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://space-ocr.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://space-ocr.com/privacy/
created: '2026-10-31'
description: 'A field extraction API with built-in verification. Send a document photo with a list of field names — one POST returns typed JSON. No training, no processor setup, no SDK. Every value carries the box / quad it was read from (coordinates come from the OCR pass, not the language model), and values that fail the cross-check come back on an explicit review list — a work list, not a bare confidence score. Measured side by side against Mistral Document AI on the same photos, same schema, same grading script: field accuracy 91.1% vs 70.0%, and 16 of 463 values moved across three runs vs 100 (8 cases over 7 documents · 463 fields · 3 runs each · August 2026).'
image: https://space-ocr.com/ico.svg
json_schemas:
- name: ColumnSpec
  property_count: 14
  slug: space-ocr-com-column-spec
- name: FieldSpec
  property_count: 13
  slug: space-ocr-com-field-spec
- name: OcrFieldsResponse
  property_count: 3
  slug: space-ocr-com-ocr-fields-response
- name: OcrMarkdownResponse
  property_count: 3
  slug: space-ocr-com-ocr-markdown-response
- name: OcrTextResponse
  property_count: 3
  slug: space-ocr-com-ocr-text-response
- name: UploadForm
  property_count: 3
  slug: space-ocr-com-upload-form
jsonld:
- class_count: 15
  name: Space Ocr Com Context
  property_count: 53
  slug: space-ocr-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.space-ocr.com.
  name: space-ocr-com MCP Server
  slug: space-ocr-com-mcp-yml
modified: '2026-10-31'
name: space-ocr-com
nav: Providers
network: true
overview: 'space-ocr-com publishes 12 API contracts indexed on the [APIs.io](https://apis.io/) network, including Amount API, Create API, Edit API, and 9 more. Tagged areas include OCR, Artificial Intelligence, Document Processing, and Field-Extraction.


  The space-ocr-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  space-ocr-com''s developer surface includes authentication, documentation, API reference, support, engineering blog, pricing, signup flow, and 20 more developer resources.'
plans:
- name: Space Ocr Com Plans Pricing
  plan_count: 3
  slug: space-ocr-com-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 2
  name: Space Ocr Com Rate Limits
  slug: space-ocr-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: space-ocr-com API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 2
    warn: 1
  slug: space-ocr-com-rules
scopes:
- name: Space Ocr Com Scopes
  scope_count: 0
  slug: space-ocr-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.5
  coverage:
    artifact_dirs: 31
    catalog_earned: 77.8
    catalog_earned_first_party: 20.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.1
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 59.8
    developer_ergonomics: 28.6
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 53.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 12
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/space-ocr-com/space-ocr-com-2026-11-03T143600.png
security:
- kind: authentication
  name: Space Ocr Com Authentication
  slug: space-ocr-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Space Ocr Com Domain Security
  slug: space-ocr-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: space-ocr-com
tags:
- OCR
- Artificial Intelligence
- Document Processing
- Field-Extraction
website: https://space-ocr.com/
---

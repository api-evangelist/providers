---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.0
  scored_at: '2026-10-31'
api_count: 3
apis:
- baseURL: https://x402.auteng.ai
  baseurl_source: declared
  description: 'auteng-ai core API as documented publicly: 2 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: auteng-ai core API
  slug: core-api
- baseURL: https://x402.auteng.ai
  baseurl_source: declared
  description: 'auteng-ai 6 pages Guides & Best Practices Cross-domain guides for creating exceptional te API as documented publicly: 4 operations. Contract generated from the documentation by API Evangelist (2026-10'
  name: 'auteng-ai 6 pages

    Guides & Best Practices


    Cross-domain guides for creating exceptional te API'
  slug: guides-api
- baseURL: https://x402.auteng.ai
  baseurl_source: declared
  description: 'auteng-ai 5 pages Software Engineering Authentication, APIs, architecture, diagrams, and API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-10-'
  name: 'auteng-ai 5 pages

    Software Engineering


    Authentication, APIs, architecture, diagrams, and API'
  slug: software-api
artifact_total: 17
common:
- group: commercial
  href: https://artifacts.apis.io/auteng-ai/plans/auteng-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/auteng-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/auteng-ai/rules/auteng-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/auteng-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/auteng-ai/json-ld/auteng-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/auteng-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/auteng-ai/vocabulary/auteng-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/auteng-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/auteng-ai/data-model/auteng-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/auteng-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/auteng-ai/conventions/auteng-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/auteng-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/auteng-ai/authentication/auteng-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/auteng-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/auteng-ai/errors/auteng-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/auteng-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/auteng-ai/conformance/auteng-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/auteng-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/auteng-ai/llms/auteng-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/auteng-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/auteng-ai/hosts/auteng-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/auteng-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/auteng-ai/vendors/auteng-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/auteng-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/auteng-ai/security/auteng-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/auteng-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://auteng.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://auteng.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://auteng.ai/docs/software/api/api-documentation
- group: start
  title: ''
  type: GettingStarted
  url: https://auteng.ai/docs/guides/getting-started
- group: operate
  title: ''
  type: Support
  url: https://auteng.ai/contact
- group: commercial
  title: ''
  type: Pricing
  url: https://auteng.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://auteng.ai/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://auteng.ai/legal/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://auteng.ai/legal/privacy-policy
coverage:
  checked: '2026-10-30'
  detail: API specification URLs return 403 Access Denied, indicating the contract is behind an authentication wall.
  evidence:
  - status: 403
    url: https://auteng.ai/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-29'
description: AutEng provides an AI-native workspace for creating, editing, and sharing technical documentation. It supports Markdown, Mermaid diagrams, and KaTeX math, offering a collaborative platform with AI assistance for generating content, visualizations, and code examples. AutEng targets developers, engineers, and technical writers seeking modern, interactive documentation solutions.
image: https://auteng.ai/favicon.ico
json_schemas:
- name: GetApiUsersIdResponse
  property_count: 4
  slug: auteng-ai-get-api-users-id-response
- name: GetResourceResponse
  property_count: 1
  slug: auteng-ai-get-resource-response
- name: GetWellKnownX402Response
  property_count: 4
  slug: auteng-ai-get-well-known-x402-response
- name: PostApiX402ComputeRequest
  property_count: 3
  slug: auteng-ai-post-api-x402-compute-request
- name: PostApiX402ComputeResponse
  property_count: 3
  slug: auteng-ai-post-api-x402-compute-response
- name: PostTokenRequest
  property_count: 3
  slug: auteng-ai-post-token-request
- name: PostTokenResponse
  property_count: 3
  slug: auteng-ai-post-token-response
jsonld:
- class_count: 7
  name: Auteng Ai Context
  property_count: 14
  slug: auteng-ai-context
layout: provider
modified: '2026-10-29'
name: auteng-ai
nav: Providers
network: true
overview: 'auteng-ai is listed with 3 APIs on the [APIs.io](https://apis.io/) network: core API, 6 pages

  Guides & Best Practices


  Cross-domain guides for creating exceptional te API, and 5 pages

  Software Engineering


  Authentication, APIs, architecture, diagrams, and API. Tagged areas include Company, AI, Documentation, Technical Writing, and Markdown.


  The auteng-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  auteng-ai''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, signup flow, and 15 more developer resources.'
plans:
- name: Auteng Ai Plans Pricing
  plan_count: 2
  slug: auteng-ai-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 0
  name: Auteng Ai Rate Limits
  slug: auteng-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: auteng-ai API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: auteng-ai-rules
scopes:
- name: Auteng Ai Scopes
  scope_count: 0
  slug: auteng-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 25
    catalog_earned: 73.0
    catalog_earned_first_party: 8.0
    catalog_gap: 42.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 33.3
    contract_quality: 25.8
    developer_ergonomics: 45.2
    discoverability: 71.4
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 12
      marker_coverage: 100.0
      total: 12
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Auteng Ai Authentication
  slug: auteng-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Auteng Ai Domain Security
  slug: auteng-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: auteng-ai
tags:
- Company
- AI
- Documentation
- Technical Writing
- Markdown
- Mermaid
- KaTeX
website: https://auteng.ai/
---

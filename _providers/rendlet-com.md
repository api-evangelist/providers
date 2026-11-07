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
  - sandbox
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Rendlet Com Agentic Access
  operation_count: 5
  slug: rendlet-com-agentic-access
  summary_line: 5 operations · 3 acting
api_count: 1
apis:
- baseURL: https://rendlet.com
  baseurl_source: declared
  description: The Checkout API from rendlet-com — 1 operation(s) for checkout.
  name: rendlet-com Checkout API
  slug: rendlet-com-checkout-api
- baseURL: https://rendlet.com
  baseurl_source: declared
  description: The Pdf API from rendlet-com — 1 operation(s) for pdf.
  name: rendlet-com PDF API
  slug: rendlet-com-pdf-api
- baseURL: https://rendlet.com
  baseurl_source: declared
  description: The Signup API from rendlet-com — 1 operation(s) for signup.
  name: rendlet-com Signup API
  slug: rendlet-com-signup-api
- baseURL: https://rendlet.com
  baseurl_source: declared
  description: The Templates API from rendlet-com — 1 operation(s) for templates.
  name: rendlet-com Templates API
  slug: rendlet-com-templates-api
- baseURL: https://rendlet.com
  baseurl_source: declared
  description: The Usage API from rendlet-com — 1 operation(s) for usage.
  name: rendlet-com Usage API
  slug: rendlet-com-usage-api
artifact_total: 21
common:
- group: agent
  href: https://artifacts.apis.io/rendlet-com/agentic-access/rendlet-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/rendlet-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/rendlet-com/rate-limits/rendlet-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/rendlet-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/rendlet-com/plans/rendlet-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/rendlet-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/rendlet-com/rules/rendlet-com-rules.yml
  title: ''
  type: Spectral
  url: rules/rendlet-com-rules.yml
- group: design
  href: https://artifacts.apis.io/rendlet-com/json-ld/rendlet-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/rendlet-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/rendlet-com/vocabulary/rendlet-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/rendlet-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/rendlet-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/rendlet-com/data-model/rendlet-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/rendlet-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/rendlet-com/conventions/rendlet-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/rendlet-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/rendlet-com/sandbox/rendlet-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/rendlet-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/rendlet-com/authentication/rendlet-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/rendlet-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/rendlet-com/errors/rendlet-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/rendlet-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/rendlet-com/conformance/rendlet-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/rendlet-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/rendlet-com/llms/rendlet-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/rendlet-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/rendlet-com/mcp/rendlet-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/rendlet-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/rendlet-com/hosts/rendlet-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/rendlet-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/rendlet-com/vendors/rendlet-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/rendlet-com-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://rendlet.com/sandbox
- group: auth
  href: https://artifacts.apis.io/rendlet-com/security/rendlet-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/rendlet-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://rendlet.com/
- group: docs
  title: ''
  type: Documentation
  url: https://rendlet.com/docs.md
- group: docs
  title: ''
  type: APIReference
  url: https://rendlet.com/openapi.json
- group: commercial
  title: ''
  type: Pricing
  url: https://rendlet.com/#pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rendlet.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rendlet.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://rendlet.com/contact
- group: start
  title: ''
  type: SignUp
  url: https://rendlet.com/#signup
created: '2026-10-31'
description: Rendlet provides a developer‑friendly PDF generation API that converts HTML or JSON with built‑in templates (such as invoice or itinerary) into PDF documents in a single HTTP call. It offers a free tier with 100 documents per month, supports base64 responses for AI agents, and includes a full OpenAPI 3.1 specification. Operated by INTELLIFIN LIMITED, the service includes comprehensive documentation, pricing details, terms of service, privacy policy, and support contact information.
image: https://rendlet.com/samples/invoice-sample-page1.png
json_schemas:
- name: Base64Response
  property_count: 5
  slug: rendlet-com-base64-response
- name: HtmlRequest
  property_count: 4
  slug: rendlet-com-html-request
- name: TemplateRequest
  property_count: 4
  slug: rendlet-com-template-request
jsonld:
- class_count: 4
  name: Rendlet Com Context
  property_count: 13
  slug: rendlet-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at rendlet.com.
  name: rendlet-com MCP Server
  slug: rendlet-com-mcp-yml
modified: '2026-10-31'
name: rendlet-com
nav: Providers
network: true
overview: 'rendlet-com publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Checkout API, PDF API, Signup API, and 2 more. Tagged areas include Company, PDF, Document Generation, Software-as-a-Service, and Artificial Intelligence.


  The rendlet-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  rendlet-com''s developer surface includes sandbox, authentication, documentation, API reference, pricing, support, signup flow, and 20 more developer resources.'
plans:
- name: Rendlet Com Plans Pricing
  plan_count: 4
  slug: rendlet-com-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 5
  name: Rendlet Com Rate Limits
  slug: rendlet-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: rendlet-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 1
  slug: rendlet-com-rules
scopes:
- name: Rendlet Com Scopes
  scope_count: 0
  slug: rendlet-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 46.7
  coverage:
    artifact_dirs: 29
    catalog_earned: 83.8
    catalog_earned_first_party: 24.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 56.9
    developer_ergonomics: 32.6
    discoverability: 65.0
    operational_transparency: 31.6
  previous_composite: 54.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: first-party
    skills: unknown
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
screenshot: https://apis.io/screenshots/rendlet-com/rendlet-com-2026-11-03T142143.png
security:
- kind: authentication
  name: Rendlet Com Authentication
  slug: rendlet-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Rendlet Com Domain Security
  slug: rendlet-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 4
skills:
- name: get-usage
  slug: rendlet-com-get-usage
- name: list-templates
  slug: rendlet-com-list-templates
- name: render-pdf
  slug: rendlet-com-render-pdf
- name: request-key
  slug: rendlet-com-request-key
slug: rendlet-com
tags:
- Company
- PDF
- Document Generation
- Software-as-a-Service
- Artificial Intelligence
website: https://rendlet.com/
---

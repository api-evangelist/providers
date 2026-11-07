---
access_model:
  confidence: medium
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.8
  scored_at: '2026-11-06'
api_count: 4
apis:
- description: API for CMD+K platform
  name: CMD+K API
  slug: cmd-k-api
- description: The Cmdk API from CMD+K — 1 operation(s) for cmdk.
  name: CMD+K Cmdk API
  slug: commandplusk-cmdk-api
- description: The Models API from CMD+K — 1 operation(s) for models.
  name: CMD+K Models API
  slug: commandplusk-models-api
- description: The Public API from CMD+K — 3 operation(s) for public.
  name: CMD+K Public API
  slug: commandplusk-public-api
artifact_total: 18
common:
- group: docs
  title: ''
  type: APIReference
  url: https://commandplusk.com/docs/reference/security
- group: commercial
  href: https://artifacts.apis.io/commandplusk/plans/commandplusk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/commandplusk-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/commandplusk/rules/commandplusk-rules.yml
  title: ''
  type: Spectral
  url: rules/commandplusk-rules.yml
- group: design
  href: https://artifacts.apis.io/commandplusk/json-ld/commandplusk-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/commandplusk-context.jsonld
- group: design
  href: https://artifacts.apis.io/commandplusk/vocabulary/commandplusk-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/commandplusk-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/commandplusk/data-model/commandplusk-data-model.yml
  title: ''
  type: DataModel
  url: data-model/commandplusk-data-model.yml
- group: operate
  href: https://artifacts.apis.io/commandplusk/changelog/commandplusk-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/commandplusk-changelog.yml
- group: auth
  href: https://artifacts.apis.io/commandplusk/authentication/commandplusk-authentication.yml
  title: ''
  type: Authentication
  url: authentication/commandplusk-authentication.yml
- group: design
  href: https://artifacts.apis.io/commandplusk/conformance/commandplusk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/commandplusk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/commandplusk/llms/commandplusk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/commandplusk-llms.txt
- group: agent
  href: https://artifacts.apis.io/commandplusk/mcp/commandplusk-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/commandplusk-mcp.yml
- group: agent
  href: https://artifacts.apis.io/commandplusk/well-known/commandplusk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/commandplusk-well-known.yml
- group: other
  href: https://artifacts.apis.io/commandplusk/hosts/commandplusk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/commandplusk-hosts.yml
- group: other
  href: https://artifacts.apis.io/commandplusk/vendors/commandplusk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/commandplusk-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://commandplusk.com/trust
- group: operate
  title: ''
  type: ChangeLog
  url: https://commandplusk.com/changelog
- group: auth
  href: https://artifacts.apis.io/commandplusk/security/commandplusk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/commandplusk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://commandplusk.com/
- group: docs
  title: ''
  type: Documentation
  url: https://commandplusk.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://commandplusk.com/docs/get-started/quickstart
- group: operate
  title: ''
  type: Support
  url: https://commandplusk.com/status
- group: company
  title: ''
  type: Blog
  url: https://commandplusk.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://commandplusk.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://commandplusk.com/auth?mode=signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://commandplusk.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://commandplusk.com/privacy
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/organization/commandplusk
coverage:
  checked: '2026-10-16'
  detail: No OpenAPI or other machine‑readable contract found on api.commandplusk.com despite probing common spec endpoints.
  evidence:
  - status: 0
    url: https://api.commandplusk.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: CMD+K provides an in‑product AI assistant platform that lets software products embed a conversational agent capable of answering user queries from documentation with citations and performing actions on behalf of the user via hosted MCP (Model‑Control‑Plane) servers. It supports OpenAPI and GraphQL specifications, offers OAuth 2.1 authentication, integrates with tools like GitHub, Slack, and Stripe, and includes features such as whitelabeling, usage attribution, and metered billing. Pricing starts at $29 per month with prepaid credits, and a free trial is available.
finops:
- has_sources: true
  method: derived
  name: Commandplusk Finops
  primary_unit: subscription
  service_category: ''
  slug: commandplusk-finops
  template: false
image: https://commandplusk.com/og-image.png
json_schemas:
- name: PostApiPublicPartnerWidgetWidgetidRequest
  property_count: 2
  slug: commandplusk-post-api-public-partner-widget-widgetid-request
- name: PostApiPublicV1ChatCompletionsRequest
  property_count: 3
  slug: commandplusk-post-api-public-v1-chat-completions-request
- name: PostApiPublicWidgetVerifyRequest
  property_count: 2
  slug: commandplusk-post-api-public-widget-verify-request
- name: PostApiPublicWidgetVerifyResponse
  property_count: 2
  slug: commandplusk-post-api-public-widget-verify-response
- name: PostCmdkVerifyUserRequest
  property_count: 7
  slug: commandplusk-post-cmdk-verify-user-request
- name: PostCmdkVerifyUserResponse
  property_count: 7
  slug: commandplusk-post-cmdk-verify-user-response
jsonld:
- class_count: 6
  name: Commandplusk Context
  property_count: 20
  slug: commandplusk-context
layout: provider
mcp_servers:
- description: Remote MCP server at commandplusk.com requiring OAuth.
  name: CMD+K MCP Server
  slug: commandplusk-mcp-yml
modified: '2026-10-16'
name: CMD+K
nav: Providers
network: true
overview: 'CMD+K is listed with 4 APIs on the [APIs.io](https://apis.io/) network, including Cmdk API, Models API, Public API, and 1 more. Tagged areas include Artificial Intelligence, Assistant, Platform, Software-as-a-Service, and Developers.


  The CMD+K catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CMD+K''s developer surface includes API reference, changelog, authentication, documentation, getting-started guide, support, engineering blog, and 20 more developer resources.'
plans:
- name: Commandplusk Plans Pricing
  plan_count: 3
  slug: commandplusk-plans-pricing
- name: Commandplusk Price Estimates
  plan_count: 0
  slug: commandplusk-price-estimates
random_paper: 22
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: CMD+K API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: commandplusk-rules
score:
  band: thin
  composite: 38.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 75.0
    catalog_earned_first_party: 12.0
    catalog_gap: 40.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.3
  facets:
    access_clarity: 65.8
    contract_governance: 33.3
    contract_quality: 24.9
    developer_ergonomics: 32.1
    discoverability: 71.7
    operational_transparency: 7.9
  previous_composite: 49.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/commandplusk/commandplusk-2026-11-03T124923.png
security:
- kind: authentication
  name: Commandplusk Authentication
  slug: commandplusk-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Commandplusk Domain Security
  slug: commandplusk-domain-security
  summary_line: TLSv1.3 · DMARC
slug: commandplusk
tags:
- Artificial Intelligence
- Assistant
- Platform
- Software-as-a-Service
- Developers
website: https://commandplusk.com/
---

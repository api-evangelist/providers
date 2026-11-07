---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.4
  scored_at: '2026-11-06'
api_count: 6
apis:
- description: Remote, read-only Model Context Protocol server (Streamable HTTP) that lets a customer's own AI assistant - Claude, ChatGPT, Codex or any MCP client - read that customer's VeraDial account - calls wit
  name: VeraDial MCP Server
  slug: mcp
- baseURL: https://api.veradial.com/mcp
  baseurl_source: declared
  description: The Hooks API from VeraDial — 2 operation(s) for hooks.
  name: VeraDial Hooks API
  slug: veradial-hooks-api
- baseURL: https://api.veradial.com/mcp
  baseurl_source: declared
  description: The Keys API from VeraDial — 2 operation(s) for keys.
  name: VeraDial Keys API
  slug: veradial-keys-api
- baseURL: https://api.veradial.com/mcp
  baseurl_source: declared
  description: The Lines API from VeraDial — 1 operation(s) for lines.
  name: VeraDial Lines API
  slug: veradial-lines-api
- baseURL: https://api.veradial.com/mcp
  baseurl_source: declared
  description: The Me API from VeraDial — 1 operation(s) for me.
  name: VeraDial Me API
  slug: veradial-me-api
- baseURL: https://api.veradial.com/mcp
  baseurl_source: declared
  description: The Samples API from VeraDial — 1 operation(s) for samples.
  name: VeraDial Samples API
  slug: veradial-samples-api
artifact_total: 25
asyncapis:
- description: ''
  name: Veradial Webhooks
  slug: veradial-webhooks
common:
- group: operate
  href: https://artifacts.apis.io/veradial/rate-limits/veradial-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/veradial-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/veradial/plans/veradial-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/veradial-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/veradial/rules/veradial-rules.yml
  title: ''
  type: Spectral
  url: rules/veradial-rules.yml
- group: design
  href: https://artifacts.apis.io/veradial/json-ld/veradial-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/veradial-context.jsonld
- group: design
  href: https://artifacts.apis.io/veradial/vocabulary/veradial-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/veradial-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/veradial/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/veradial/asyncapi/veradial-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/veradial-webhooks.yml
- group: design
  href: https://artifacts.apis.io/veradial/data-model/veradial-data-model.yml
  title: ''
  type: DataModel
  url: data-model/veradial-data-model.yml
- group: operate
  href: https://artifacts.apis.io/veradial/changelog/veradial-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/veradial-changelog.yml
- group: design
  href: https://artifacts.apis.io/veradial/conventions/veradial-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/veradial-conventions.yml
- group: design
  href: https://artifacts.apis.io/veradial/conventions/veradial-conventions.yml
  title: ''
  type: Conventions
  url: conventions/veradial-conventions.yml
- group: auth
  href: https://artifacts.apis.io/veradial/authentication/veradial-authentication.yml
  title: ''
  type: Authentication
  url: authentication/veradial-authentication.yml
- group: auth
  href: https://artifacts.apis.io/veradial/scopes/veradial-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/veradial-scopes.yml
- group: design
  href: https://artifacts.apis.io/veradial/lifecycle/veradial-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/veradial-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/veradial/errors/veradial-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/veradial-error-codes.yml
- group: design
  href: https://artifacts.apis.io/veradial/conformance/veradial-conformance.yml
  title: ''
  type: Conformance
  url: conformance/veradial-conformance.yml
- group: other
  href: https://artifacts.apis.io/veradial/overlays/veradial-zapier-integration-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/veradial-zapier-integration-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/veradial/llms/veradial-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/veradial-llms.txt
- group: build
  href: https://artifacts.apis.io/veradial/mcp/veradial-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/veradial-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/veradial/mcp/veradial-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/veradial-mcp.yml
- group: agent
  href: https://artifacts.apis.io/veradial/well-known/veradial-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/veradial-well-known.yml
- group: other
  href: https://artifacts.apis.io/veradial/hosts/veradial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/veradial-hosts.yml
- group: other
  href: https://artifacts.apis.io/veradial/vendors/veradial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/veradial-vendors.yml
- group: auth
  href: https://artifacts.apis.io/veradial/security/veradial-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/veradial-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://veradial.com/
- group: docs
  title: ''
  type: Documentation
  url: https://veradial.com/help
- group: start
  title: ''
  type: DeveloperPortal
  url: https://veradial.com/for-agents
- group: docs
  title: ''
  type: APIReference
  url: https://veradial.com/help/zapier-integration-api
- group: start
  title: ''
  type: GettingStarted
  url: https://veradial.com/help/setup-veradial-first-screened-call
- group: operate
  title: ''
  type: Support
  url: https://veradial.com/faq
- group: company
  title: ''
  type: Blog
  url: https://veradial.com/blog
- group: operate
  title: ''
  type: ChangeLog
  url: https://veradial.com/updates
- group: commercial
  title: ''
  type: Pricing
  url: https://veradial.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.veradial.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.veradial.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://veradial.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://veradial.com/privacy
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/VeraDial
- group: other
  title: ''
  type: X
  url: https://x.com/VeraDialApp
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/112327687/
created: '2026-09-23'
description: VeraDial is an AI receptionist and business phone app for small businesses in the United States and Canada, built by Graham Thomson in Toronto. It gives a business a dedicated US or Canadian number with Vera, an AI receptionist that answers calls and texts 24/7, screens callers, takes messages, books appointments and places outbound AI calls. Developers and agents reach an account three ways - a read-only remote MCP server at api.veradial.com/mcp secured with OAuth 2.1, a Zapier REST Hooks integration API authenticated with vdk_ API keys, and signed HMAC event webhooks for Make, n8n or your own service.
finops:
- has_sources: true
  method: derived
  name: Veradial Finops
  primary_unit: subscription
  service_category: ''
  slug: veradial-finops
  template: false
image: https://veradial.com/opengraph-image
json_schemas:
- name: GetKeysResponse
  property_count: 3
  slug: veradial-get-keys-response
- name: GetLinesResponse
  property_count: 1
  slug: veradial-get-lines-response
- name: GetSamplesResponse
  property_count: 9
  slug: veradial-get-samples-response
- name: PostHooksRequest
  property_count: 3
  slug: veradial-post-hooks-request
- name: PostKeysRequest
  property_count: 1
  slug: veradial-post-keys-request
- name: PostKeysResponse
  property_count: 1
  slug: veradial-post-keys-response
jsonld:
- class_count: 9
  name: Veradial Context
  property_count: 17
  slug: veradial-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.veradial.com over streamable HTTP requiring OAuth; 13 tools listed.
  name: VeraDial MCP Server
  slug: veradial-mcp-server
modified: '2026-09-23'
name: VeraDial
nav: Providers
network: true
overview: 'VeraDial is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Hooks API, Keys API, Lines API, and 3 more. Tagged areas include AI Receptionist, Business Phone, Telephony, Voice AI, and SMS.


  The VeraDial catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  VeraDial''s developer surface includes changelog, authentication, documentation, API reference, getting-started guide, support, engineering blog, and 33 more developer resources.'
plans:
- name: Veradial Plans Pricing
  plan_count: 4
  slug: veradial-plans-pricing
- name: Veradial Price Estimates
  plan_count: 0
  slug: veradial-price-estimates
random_paper: 0
rate_limits:
- limit_count: 2
  name: Veradial Rate Limits
  slug: veradial-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: VeraDial API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: veradial-rules
scopes:
- name: Veradial Scopes
  scope_count: 3
  slug: veradial-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 46.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 88.8
    catalog_earned_first_party: 20.0
    catalog_gap: 26.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -11.4
  facets:
    access_clarity: 61.8
    contract_governance: 35.6
    contract_quality: 33.2
    developer_ergonomics: 41.7
    discoverability: 80.0
    operational_transparency: 35.5
  previous_composite: 58.3
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 31.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/veradial/veradial-2026-10-11T132834.png
security:
- kind: authentication
  name: Veradial Authentication
  slug: veradial-authentication
  summary_line: http-bearer/oauth2 · 4 schemes
- kind: domain-security
  name: Veradial Domain Security
  slug: veradial-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: veradial-receptionist
  slug: veradial-receptionist
- name: veradial-subscribe-to-receptionist-events
  slug: veradial-subscribe-to-receptionist-events
slug: veradial
tags:
- AI Receptionist
- Business Phone
- Telephony
- Voice AI
- SMS
- Webhook
- MCP
- Small Business
website: https://veradial.com/
---

---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: unknown
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.clawcall.dev
  baseurl_source: declared
  description: 'ClawCall API as documented publicly: 20 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: ClawCall API
  slug: clawcall-dev-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/clawcall-dev/plans/clawcall-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clawcall-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clawcall-dev/rules/clawcall-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/clawcall-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/clawcall-dev/json-ld/clawcall-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clawcall-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/clawcall-dev/vocabulary/clawcall-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clawcall-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/clawcall-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/clawcall-dev/data-model/clawcall-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clawcall-dev-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://clawcall.dev/security
- group: design
  href: https://artifacts.apis.io/clawcall-dev/conformance/clawcall-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clawcall-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clawcall-dev/llms/clawcall-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawcall-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/clawcall-dev/well-known/clawcall-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawcall-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/clawcall-dev/hosts/clawcall-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawcall-dev-hosts.yml
- group: design
  title: ''
  type: Webhooks
  url: https://clawcall.dev/dashboard/webhooks
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawcall.dev/terms
- group: operate
  title: ''
  type: Support
  url: https://clawcall.dev/support
- group: start
  title: ''
  type: SignUp
  url: https://clawcall.dev/sign-up?redirect_url=%2Fdashboard%2Fpurchase%3Fpromo%3DDEEPGRAM
- group: auth
  title: ''
  type: Security
  url: https://clawcall.dev/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawcall.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://clawcall.dev/pricing
- group: docs
  title: ''
  type: Documentation
  url: https://clawcall.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://clawcall.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://clawcall.dev/guides
- group: auth
  href: https://artifacts.apis.io/clawcall-dev/security/clawcall-dev-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/clawcall-dev-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/clawcall-dev/security/clawcall-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawcall-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawcall.dev/
coverage:
  checked: '2026-11-04'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, or gRPC contracts were found.
  evidence:
  - status: 404
    url: https://api.clawcall.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-03'
description: ClawCall provides an AI-powered phone calling service that automates outbound calls, navigates IVR menus, waits on hold, and returns transcript evidence. It offers a REST API and packaged agent‑skill, with OAuth‑protected MCP connector for AI hosts. The platform serves US customers and integrates with Telnyx telephony and Meta Muse speech‑to‑text.
image: https://clawcall.dev/og.png
json_schemas:
- name: GetMeCallsResponse
  property_count: 2
  slug: clawcall-dev-get-me-calls-response
- name: GetMeWebhookResponse
  property_count: 4
  slug: clawcall-dev-get-me-webhook-response
- name: GetV1CallsCallidResponse
  property_count: 4
  slug: clawcall-dev-get-v1-calls-callid-response
- name: PostAssistantRequest
  property_count: 3
  slug: clawcall-dev-post-assistant-request
- name: PostCallIdHangupResponse
  property_count: 2
  slug: clawcall-dev-post-call-id-hangup-response
- name: PutMeWebhookResponse
  property_count: 1
  slug: clawcall-dev-put-me-webhook-response
jsonld:
- class_count: 22
  name: Clawcall Dev Context
  property_count: 31
  slug: clawcall-dev-context
layout: provider
modified: '2026-11-03'
name: ClawCall
nav: Providers
network: true
overview: 'ClawCall is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI Phone Calls, Developer Tools, ChatGPT Plugins, and US Phone Numbers.


  The ClawCall catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClawCall''s developer surface includes support, signup flow, pricing, documentation, engineering blog, getting-started guide, and 18 more developer resources.'
plans:
- name: Clawcall Dev Plans Pricing
  plan_count: 2
  slug: clawcall-dev-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: ClawCall API Rules
  rule_count: 46
  severity_counts:
    error: 42
    hint: 0
    info: 1
    warn: 3
  slug: clawcall-dev-rules
score:
  band: thin
  composite: 32.4
  coverage:
    artifact_dirs: 19
    catalog_earned: 65.8
    catalog_earned_first_party: 8.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 25.8
    developer_ergonomics: 20.7
    discoverability: 57.1
    operational_transparency: 9.2
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Clawcall Dev Domain Security
  slug: clawcall-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Clawcall Dev Trust Center
  slug: clawcall-dev-trust-center
  summary_line: SOC 2, HIPAA
slug: clawcall-dev
tags:
- AI Phone Calls
- Developer Tools
- ChatGPT Plugins
- US Phone Numbers
website: https://clawcall.dev/
---

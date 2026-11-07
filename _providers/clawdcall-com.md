---
access_model:
  confidence: medium
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
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 3
  human_in_the_loop: 0
  name: Clawdcall Com Agentic Access
  operation_count: 4
  slug: clawdcall-com-agentic-access
  summary_line: 4 operations · 3 acting
api_count: 1
apis:
- baseURL: https://api.clawdcall.com
  baseurl_source: declared
  description: The Cc API from ClawdCall — 3 operation(s) for cc.
  name: ClawdCall Cc API
  slug: clawdcall-com-cc-api
- baseURL: https://api.clawdcall.com
  baseurl_source: declared
  description: The External API from ClawdCall — 1 operation(s) for external.
  name: ClawdCall External API
  slug: clawdcall-com-external-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/clawdcall-com/agentic-access/clawdcall-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/clawdcall-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/clawdcall-com/plans/clawdcall-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/clawdcall-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/clawdcall-com/rules/clawdcall-com-rules.yml
  title: ''
  type: Spectral
  url: rules/clawdcall-com-rules.yml
- group: design
  href: https://artifacts.apis.io/clawdcall-com/json-ld/clawdcall-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/clawdcall-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/clawdcall-com/vocabulary/clawdcall-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/clawdcall-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/clawdcall-com/data-model/clawdcall-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/clawdcall-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/clawdcall-com/errors/clawdcall-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/clawdcall-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/clawdcall-com/conformance/clawdcall-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/clawdcall-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/clawdcall-com/llms/clawdcall-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/clawdcall-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/clawdcall-com/well-known/clawdcall-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/clawdcall-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/clawdcall-com/hosts/clawdcall-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/clawdcall-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/clawdcall-com/vendors/clawdcall-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/clawdcall-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://clawdcall.com/terms-of-service/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://clawdcall.com/privacy-policy/
- group: commercial
  title: ''
  type: Pricing
  url: https://clawdcall.com/pricing/
- group: start
  title: ''
  type: Login
  url: https://app.clawdcall.com/login/?utm_source=clawdcall&utm_medium=homepage&utm_campaign=homepage_cta&utm_content=top_nav_login
- group: company
  title: ''
  type: Blog
  url: https://clawdcall.com/blog
- group: auth
  href: https://artifacts.apis.io/clawdcall-com/authentication/clawdcall-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/clawdcall-com-authentication.yml
- group: auth
  href: https://artifacts.apis.io/clawdcall-com/security/clawdcall-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/clawdcall-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://clawdcall.com/
created: '2026-11-03'
description: ClawdCall provides AI‑driven voice call execution for agents, enabling automated outbound phone workflows with real‑time transcription and structured outcomes. Built on Dialgood’s voice infrastructure, it offers a free starter tier and pay‑as‑you‑go pricing, supports multiple chat integrations, and includes consent, rate‑limit, and webhook security controls for production use.
image: https://clawdcall.com/site-preview.svg
json_schemas:
- name: OutboundCallRequest
  property_count: 4
  slug: clawdcall-com-outbound-call-request
- name: SignupOtpRequest
  property_count: 2
  slug: clawdcall-com-signup-otp-request
- name: VerifyOtpRequest
  property_count: 3
  slug: clawdcall-com-verify-otp-request
jsonld:
- class_count: 3
  name: Clawdcall Com Context
  property_count: 7
  slug: clawdcall-com-context
layout: provider
modified: '2026-11-03'
name: ClawdCall
nav: Providers
network: true
overview: 'ClawdCall publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Cc API and External API. Tagged areas include Artificial Intelligence, Voice, Automation, Agents, and Telephony.


  The ClawdCall catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ClawdCall''s developer surface includes pricing, engineering blog, authentication, and 17 more developer resources.'
plans:
- name: Clawdcall Com Plans Pricing
  plan_count: 2
  slug: clawdcall-com-plans-pricing
random_paper: 3
rules:
- authorship: generated
  effective_rule_count: 77
  extends:
  - spectral:oas
  name: ClawdCall API Rules
  rule_count: 36
  severity_counts:
    error: 34
    hint: 0
    info: 1
    warn: 1
  slug: clawdcall-com-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 64.8
    catalog_earned_first_party: 8.0
    catalog_gap: 50.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 53.6
    developer_ergonomics: 13.1
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Clawdcall Com Authentication
  slug: clawdcall-com-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clawdcall Com Domain Security
  slug: clawdcall-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: clawdcall-com
tags:
- Artificial Intelligence
- Voice
- Automation
- Agents
- Telephony
website: https://clawdcall.com/
---

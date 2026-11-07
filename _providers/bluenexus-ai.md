---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Paid · Self-serve signup
  onboarding: self-serve
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.bluenexus.ai
  baseurl_source: declared
  description: 'BlueNexus AI API as documented publicly: 51 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: BlueNexus AI API
  slug: bluenexus-ai-api
artifact_total: 12
common:
- group: commercial
  href: https://artifacts.apis.io/bluenexus-ai/plans/bluenexus-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bluenexus-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bluenexus-ai/rules/bluenexus-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/bluenexus-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/bluenexus-ai/json-ld/bluenexus-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bluenexus-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/bluenexus-ai/vocabulary/bluenexus-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bluenexus-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bluenexus-ai/data-model/bluenexus-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bluenexus-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/bluenexus-ai/authentication/bluenexus-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bluenexus-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/bluenexus-ai/conformance/bluenexus-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bluenexus-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bluenexus-ai/well-known/bluenexus-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bluenexus-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/bluenexus-ai/hosts/bluenexus-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bluenexus-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/bluenexus-ai/vendors/bluenexus-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bluenexus-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://bluenexus.ai/security/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bluenexus.ai/blog/privacy-sovereign-data-the-real-platform-shift-for-llms/
- group: start
  title: ''
  type: Login
  url: https://app.bluenexus.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.bluenexus.ai/developer/clients
- group: docs
  title: ''
  type: APIReference
  url: https://docs.bluenexus.ai/reference/changelog/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.bluenexus.ai/getting-started/overview/
- group: auth
  href: https://artifacts.apis.io/bluenexus-ai/security/bluenexus-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bluenexus-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bluenexus.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bluenexus.ai/
- group: commercial
  title: ''
  type: Pricing
  url: https://bluenexus.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://bluenexus.ai/blog/
coverage:
  checked: '2026-11-02'
  detail: Documentation pages are rendered via JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://docs.bluenexus.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-11-02'
description: BlueNexus AI provides an Agent Management Platform that enables teams to build AI agents once and deploy them across apps, portals, email, messaging, and widgets. It supports native connectors for data integration, allowing personalized agents for product teams and domain experts. The platform emphasizes real‑time collaboration between people and AI agents, offering early‑access sign‑up and a focus on privacy‑friendly analytics.
image: https://www.bluenexus.ai/img/og-default.png
json_schemas:
- name: GetAgentsAgentidResponse
  property_count: 11
  slug: bluenexus-ai-get-agents-agentid-response
- name: GetWellKnownOauthAuthorizationServerResponse
  property_count: 11
  slug: bluenexus-ai-get-well-known-oauth-authorization-server-response
- name: PostAuthPatRequest
  property_count: 7
  slug: bluenexus-ai-post-auth-pat-request
- name: PostAuthRegisterRequest
  property_count: 8
  slug: bluenexus-ai-post-auth-register-request
- name: PostAuthTokenRequest
  property_count: 6
  slug: bluenexus-ai-post-auth-token-request
- name: PostChatCompletionsRequest
  property_count: 11
  slug: bluenexus-ai-post-chat-completions-request
jsonld:
- class_count: 40
  name: Bluenexus Ai Context
  property_count: 106
  slug: bluenexus-ai-context
layout: provider
modified: '2026-11-02'
name: BlueNexus AI
nav: Providers
network: true
overview: 'BlueNexus AI is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Platform, Agent Management, Collaboration, and Real-Time.


  The BlueNexus AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  BlueNexus AI''s developer surface includes authentication, API reference, getting-started guide, documentation, pricing, engineering blog, and 15 more developer resources.'
plans:
- name: Bluenexus Ai Plans Pricing
  plan_count: 3
  slug: bluenexus-ai-plans-pricing
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 87
  extends:
  - spectral:oas
  name: BlueNexus AI API Rules
  rule_count: 46
  severity_counts:
    error: 40
    hint: 0
    info: 2
    warn: 4
  slug: bluenexus-ai-rules
score:
  band: thin
  composite: 33.0
  coverage:
    artifact_dirs: 16
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 48.7
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 32.1
    discoverability: 66.1
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Bluenexus Ai Authentication
  slug: bluenexus-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Bluenexus Ai Domain Security
  slug: bluenexus-ai-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bluenexus-ai
tags:
- Artificial Intelligence
- Platform
- Agent Management
- Collaboration
- Real-Time
website: https://bluenexus.ai/
---

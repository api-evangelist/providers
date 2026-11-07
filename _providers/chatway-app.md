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
    event_surface_described: true
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 44.6
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Chatway live chat and AI support REST API as described in the developer documentation.
  name: Chatway REST API
  slug: chatway-rest-api
- description: 'Chatway API as documented publicly: 21 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Chatway API
  slug: chatway-app-api
artifact_total: 14
asyncapis:
- description: ''
  name: Chatway App Webhooks
  slug: chatway-app-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/chatway-app/plans/chatway-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chatway-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chatway-app/rules/chatway-app-rules.yml
  title: ''
  type: Spectral
  url: rules/chatway-app-rules.yml
- group: design
  href: https://artifacts.apis.io/chatway-app/json-ld/chatway-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chatway-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/chatway-app/vocabulary/chatway-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chatway-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chatway-app/asyncapi/chatway-app-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chatway-app-webhooks.yml
- group: design
  href: https://artifacts.apis.io/chatway-app/data-model/chatway-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chatway-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/chatway-app/conventions/chatway-app-conventions.yml
  title: ''
  type: Conventions
  url: conventions/chatway-app-conventions.yml
- group: auth
  href: https://artifacts.apis.io/chatway-app/authentication/chatway-app-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chatway-app-authentication.yml
- group: design
  href: https://artifacts.apis.io/chatway-app/conformance/chatway-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chatway-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chatway-app/llms/chatway-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatway-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/chatway-app/well-known/chatway-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatway-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/chatway-app/hosts/chatway-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatway-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatway-app/vendors/chatway-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatway-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/chatway-app/packages/chatway-app-packages.yml
  title: ''
  type: SDKs
  url: packages/chatway-app-packages.yml
- group: build
  href: https://artifacts.apis.io/chatway-app/packages/chatway-app-packages.yml
  title: ''
  type: Packages
  url: packages/chatway-app-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatway.app/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatway.app/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.chatway.app/operations/guides.quickstart
- group: docs
  title: ''
  type: Documentation
  url: https://developers.chatway.app/
- group: auth
  href: https://artifacts.apis.io/chatway-app/security/chatway-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatway-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatway.app/
- group: docs
  title: ''
  type: APIReference
  url: https://chatway.app/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://chatway.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://chatway.app/blog
- group: operate
  title: ''
  type: HelpCenter
  url: https://chatway.app/help
coverage:
  checked: '2026-11-04'
  detail: Developer documentation is HTML without a published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec.
  evidence:
  - status: 200
    url: https://developers.chatway.app/operations/guides.api_overview
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Chatway is a live chat and AI customer support platform offering an all‑in‑one inbox, automation, and Multi‑Channel Platform (MCP) for AI agents such as ChatGPT and Claude. It provides live chat, AI chatbot, integrations, pricing plans, and developer resources.
image: https://chatway.app/wp-content/themes/chatway-theme/assets/images/preview/chatway-v2-preview.webp
json_schemas:
- name: GetApiV1AgentsIdResponse
  property_count: 11
  slug: chatway-app-get-api-v1-agents-id-response
- name: GetApiV1AgentsResponse
  property_count: 3
  slug: chatway-app-get-api-v1-agents-response
- name: GetWellKnownAgentSkillsIndexJsonResponse
  property_count: 2
  slug: chatway-app-get-well-known-agent-skills-index-json-response
- name: PostAgentsInviteRequest
  property_count: 4
  slug: chatway-app-post-agents-invite-request
- name: PostApiV1WebhooksResponse
  property_count: 3
  slug: chatway-app-post-api-v1-webhooks-response
- name: PostMessagesRequest
  property_count: 3
  slug: chatway-app-post-messages-request
jsonld:
- class_count: 15
  name: Chatway App Context
  property_count: 24
  slug: chatway-app-context
layout: provider
modified: '2026-11-04'
name: Chatway
nav: Providers
network: true
overview: 'Chatway is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Live Chat, Artificial Intelligence, Customer Service, MCP, and Chatbots.


  The Chatway catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Chatway''s developer surface includes authentication, getting-started guide, documentation, API reference, pricing, engineering blog, and 19 more developer resources.'
plans:
- name: Chatway App Plans Pricing
  plan_count: 5
  slug: chatway-app-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Chatway API Rules
  rule_count: 44
  severity_counts:
    error: 38
    hint: 0
    info: 2
    warn: 4
  slug: chatway-app-rules
score:
  band: thin
  composite: 34.6
  coverage:
    artifact_dirs: 21
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 32.6
    developer_ergonomics: 36.9
    discoverability: 57.1
    operational_transparency: 7.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chatway App Authentication
  slug: chatway-app-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chatway App Domain Security
  slug: chatway-app-domain-security
  summary_line: TLSv1.3 · DMARC
slug: chatway-app
tags:
- Live Chat
- Artificial Intelligence
- Customer Service
- MCP
- Chatbots
- Company
website: https://chatway.app/
---

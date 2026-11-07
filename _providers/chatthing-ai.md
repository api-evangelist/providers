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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Chat Thing API provides endpoints for chatbot integration as documented.
  name: Chat Thing API
  slug: chat-thing-api
- baseURL: https://app.chatthing.ai
  baseurl_source: declared
  description: 'Chat Thing API as documented publicly: 26 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Chat Thing API
  slug: chatthing-ai-api
artifact_total: 14
asyncapis:
- description: ''
  name: Chatthing Ai Webhooks
  slug: chatthing-ai-webhooks
common:
- group: commercial
  href: https://artifacts.apis.io/chatthing-ai/plans/chatthing-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/chatthing-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/chatthing-ai/rules/chatthing-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/chatthing-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/chatthing-ai/json-ld/chatthing-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/chatthing-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/chatthing-ai/vocabulary/chatthing-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/chatthing-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/chatthing-ai/asyncapi/chatthing-ai-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/chatthing-ai-webhooks.yml
- group: design
  href: https://artifacts.apis.io/chatthing-ai/data-model/chatthing-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/chatthing-ai-data-model.yml
- group: operate
  href: https://artifacts.apis.io/chatthing-ai/changelog/chatthing-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/chatthing-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/chatthing-ai/authentication/chatthing-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/chatthing-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/chatthing-ai/conformance/chatthing-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/chatthing-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/chatthing-ai/llms/chatthing-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/chatthing-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/chatthing-ai/well-known/chatthing-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/chatthing-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/chatthing-ai/hosts/chatthing-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chatthing-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/chatthing-ai/vendors/chatthing-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chatthing-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://chatthing.ai/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://chatthing.ai/demos/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.chatthing.ai/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://chatthing.ai/legal/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://chatthing.ai/pricing
- group: start
  title: ''
  type: Login
  url: https://app.chatthing.ai/app/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://chatthing.ai/docs
- group: operate
  title: ''
  type: ChangeLog
  url: https://chatthing.ai/docs/help/changelog
- group: company
  title: ''
  type: Blog
  url: https://chatthing.ai/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://chatthing.ai/docs/use-cases/onboarding-and-success
- group: auth
  href: https://artifacts.apis.io/chatthing-ai/security/chatthing-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chatthing-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chatthing.ai/
coverage:
  checked: '2026-11-04'
  detail: Documentation is HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://chatthing.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Chat Thing provides an AI-powered chatbot platform that integrates with websites, chat apps, and phone systems to answer customer queries, capture leads, schedule meetings, and handle calls. It offers flat monthly pricing and supports multiple languages, aiming to enhance customer engagement and automate support for businesses of all sizes.
image: https://chatthing.ai/open-graph.png
json_schemas:
- name: PostApiPublicChannelsChannelid20DataSourcesResponse
  property_count: 2
  slug: chatthing-ai-post-api-public-channels-channelid20-data-sources-response
- name: PostApiPublicChannelsChannelid20DataSourcesRowListResponse
  property_count: 3
  slug: chatthing-ai-post-api-public-channels-channelid20-data-sources-row-list-response
- name: PostDataSourcesRowListRequest
  property_count: 3
  slug: chatthing-ai-post-data-sources-row-list-request
- name: PostDataSourcesRowListResponse
  property_count: 3
  slug: chatthing-ai-post-data-sources-row-list-response
- name: PostDataSourcesRowRequest
  property_count: 4
  slug: chatthing-ai-post-data-sources-row-request
- name: PutDataSourcesRowRequest
  property_count: 5
  slug: chatthing-ai-put-data-sources-row-request
jsonld:
- class_count: 40
  name: Chatthing Ai Context
  property_count: 10
  slug: chatthing-ai-context
layout: provider
modified: '2026-11-04'
name: Chat Thing
nav: Providers
network: true
overview: 'Chat Thing is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Chatbot, Customer Service, Lead Capture, Appointment Booking, and Voice Assistant.


  The Chat Thing catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Chat Thing''s developer surface includes changelog, authentication, support, pricing, documentation, engineering blog, getting-started guide, and 18 more developer resources.'
plans:
- name: Chatthing Ai Plans Pricing
  plan_count: 5
  slug: chatthing-ai-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Chat Thing API Rules
  rule_count: 48
  severity_counts:
    error: 41
    hint: 0
    info: 4
    warn: 3
  slug: chatthing-ai-rules
score:
  band: thin
  composite: 37.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 69.8
    catalog_earned_first_party: 12.0
    catalog_gap: 45.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 36.1
    developer_ergonomics: 26.2
    discoverability: 57.1
    operational_transparency: 23.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Chatthing Ai Authentication
  slug: chatthing-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Chatthing Ai Domain Security
  slug: chatthing-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: chatthing-ai
tags:
- AI Chatbot
- Customer Service
- Lead Capture
- Appointment Booking
- Voice Assistant
- Internal knowledge base
- SDK
website: https://chatthing.ai/
---

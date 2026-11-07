---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Clad Labs API as documented publicly: 23 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Clad Labs API
  slug: useclad-ai-api
artifact_total: 12
common:
- group: operate
  href: https://artifacts.apis.io/useclad-ai/rate-limits/useclad-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/useclad-ai-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/useclad-ai/rules/useclad-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/useclad-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/useclad-ai/json-ld/useclad-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/useclad-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/useclad-ai/vocabulary/useclad-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/useclad-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/useclad-ai/data-model/useclad-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/useclad-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/useclad-ai/conventions/useclad-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/useclad-ai-conventions.yml
- group: auth
  href: https://artifacts.apis.io/useclad-ai/authentication/useclad-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/useclad-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/useclad-ai/lifecycle/useclad-ai-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/useclad-ai-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/useclad-ai/conformance/useclad-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/useclad-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/useclad-ai/llms/useclad-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/useclad-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/useclad-ai/hosts/useclad-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/useclad-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/useclad-ai/vendors/useclad-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/useclad-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/useclad-ai/security/useclad-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/useclad-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.useclad.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.useclad.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useclad.ai
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useclad.ai/api/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://www.useclad.ai/get-started
- group: company
  title: ''
  type: Blog
  url: https://www.useclad.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.useclad.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.useclad.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.useclad.ai/privacy
coverage:
  checked: '2026-10-29'
  detail: Documentation pages are rendered via JavaScript and provide no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.useclad.ai
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Clad Labs builds an AI-powered support platform that triages, investigates, and resolves customer support tickets across Slack, Discord, Teams, and email. The system captures conversation threads, provides evidence‑backed handoffs, and automates ticket creation with root‑cause analysis. By integrating with existing tools and ticketing systems, Clad enables teams to resolve issues faster while preserving knowledge in a centralized knowledge base. The platform offers a widget SDK for embedding support chat, a GraphQL API for workspace data, and customizable AI agents to assist support engineers.
image: https://www.useclad.ai/og-image.png?v=2
json_schemas:
- name: GetGraphqlResponse
  property_count: 1
  slug: useclad-ai-get-graphql-response
- name: PostConversationsIdMessagesRequest
  property_count: 2
  slug: useclad-ai-post-conversations-id-messages-request
- name: PostConversationsRequest
  property_count: 5
  slug: useclad-ai-post-conversations-request
- name: PostGraphqlRequest
  property_count: 1
  slug: useclad-ai-post-graphql-request
- name: PostGraphqlResponse
  property_count: 1
  slug: useclad-ai-post-graphql-response
- name: PostSessionsIdentifyRequest
  property_count: 1
  slug: useclad-ai-post-sessions-identify-request
jsonld:
- class_count: 6
  name: Useclad Ai Context
  property_count: 10
  slug: useclad-ai-context
layout: provider
modified: '2026-10-29'
name: Clad Labs
nav: Providers
network: true
overview: 'Clad Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Support, Software-as-a-Service, and Automation.


  The Clad Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clad Labs'' developer surface includes authentication, documentation, API reference, getting-started guide, engineering blog, pricing, and 16 more developer resources.'
random_paper: 0
rate_limits:
- limit_count: 2
  name: Useclad Ai Rate Limits
  slug: useclad-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Clad Labs API Rules
  rule_count: 11
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 0
  slug: useclad-ai-rules
score:
  band: thin
  composite: 27.2
  coverage:
    artifact_dirs: 24
    catalog_earned: 65.0
    catalog_earned_first_party: 8.0
    catalog_gap: 50.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 15.8
    contract_governance: 19.7
    contract_quality: 24.7
    developer_ergonomics: 32.1
    discoverability: 64.3
    operational_transparency: 21.1
  previous_composite: 34.9
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
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/useclad-ai/useclad-ai-2026-11-03T145523.png
security:
- kind: authentication
  name: Useclad Ai Authentication
  slug: useclad-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Useclad Ai Domain Security
  slug: useclad-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: useclad-ai
tags:
- Company
- Artificial Intelligence
- Support
- Software-as-a-Service
- Automation
website: https://www.useclad.ai
---

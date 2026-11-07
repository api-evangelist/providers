---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- baseURL: https://api.apiko.app
  baseurl_source: declared
  description: 'APIKO API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-02); not the provider''s own document.'
  name: APIKO API
  slug: apiko-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/apiko/rules/apiko-rules.yml
  title: ''
  type: Spectral
  url: rules/apiko-rules.yml
- group: design
  href: https://artifacts.apis.io/apiko/json-ld/apiko-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apiko-context.jsonld
- group: design
  href: https://artifacts.apis.io/apiko/vocabulary/apiko-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apiko-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apiko/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apiko/data-model/apiko-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apiko-data-model.yml
- group: auth
  href: https://artifacts.apis.io/apiko/authentication/apiko-authentication.yml
  title: ''
  type: Authentication
  url: authentication/apiko-authentication.yml
- group: design
  href: https://artifacts.apis.io/apiko/lifecycle/apiko-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apiko-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/apiko/errors/apiko-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apiko-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apiko/conformance/apiko-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apiko-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apiko/llms/apiko-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apiko-llms.txt
- group: other
  href: https://artifacts.apis.io/apiko/hosts/apiko-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apiko-hosts.yml
- group: other
  href: https://artifacts.apis.io/apiko/vendors/apiko-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apiko-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apiko.app/terms-of-service
- group: operate
  title: ''
  type: StatusPage
  url: https://apiko.app/status
- group: start
  title: ''
  type: SignUp
  url: https://apiko.app/sign-up?callbackUrl=%2Fdashboard%2Fapikeys
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apiko.app/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://apiko.app/docs/integration-guide/agent-skills/changelog
- group: auth
  href: https://artifacts.apis.io/apiko/security/apiko-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apiko-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apiko.app
- group: docs
  title: ''
  type: Documentation
  url: https://apiko.app/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apiko.app/docs/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://apiko.app/#pricing
- group: company
  title: ''
  type: Blog
  url: https://apiko.app/blog
coverage:
  checked: '2026-11-02'
  detail: Provider publishes documentation but no public OpenAPI spec; contract generated from docs.
  evidence:
  - status: 200
    url: https://apiko.app/docs/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-02'
description: APIKO provides a unified AI API platform that offers text, image, video, and audio generation models through a single key and balanced billing. Users can compare model prices and availability, access a catalog of models, and only pay for successful requests. The service includes endpoints for chat completions, image generation, video generation, and audio processing, with detailed documentation, quickstart guides, pricing information, and a public blog covering updates and best practices.
image: https://apiko.app/logo.svg
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: apiko-post-v1-chat-completions-request
- name: PostV1ImagesGenerationsRequest
  property_count: 4
  slug: apiko-post-v1-images-generations-request
- name: PostV1VideosRequest
  property_count: 6
  slug: apiko-post-v1-videos-request
- name: PostV1VideosResponse
  property_count: 6
  slug: apiko-post-v1-videos-response
jsonld:
- class_count: 4
  name: Apiko Context
  property_count: 14
  slug: apiko-context
layout: provider
modified: '2026-11-02'
name: APIKO
nav: Providers
network: true
overview: 'APIKO is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Machine Learning, Text Generation, Image Generation, and Video Generation.


  The APIKO catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIKO''s developer surface includes authentication, signup flow, changelog, documentation, getting-started guide, pricing, engineering blog, and 16 more developer resources.'
plans:
- name: Apiko Plans Pricing
  plan_count: 0
  slug: apiko-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 0
  name: Apiko Rate Limits
  slug: apiko-rate-limits
rules:
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: APIKO API Rules
  rule_count: 39
  severity_counts:
    error: 37
    hint: 0
    info: 1
    warn: 1
  slug: apiko-rules
scopes:
- name: Apiko Scopes
  scope_count: 0
  slug: apiko-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.9
  coverage:
    artifact_dirs: 28
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 22.4
    contract_governance: 35.6
    contract_quality: 23.6
    developer_ergonomics: 30.2
    discoverability: 66.1
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apiko Authentication
  slug: apiko-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Apiko Domain Security
  slug: apiko-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: apiko-agents
  slug: apiko-agents-SKILL
- name: apiko-api
  slug: apiko-api-SKILL
slug: apiko
tags:
- Artificial Intelligence
- Machine Learning
- Text Generation
- Image Generation
- Video Generation
- Audio Generation
website: https://apiko.app
---

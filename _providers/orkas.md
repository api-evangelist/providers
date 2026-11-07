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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Orkas Agentic Access
  operation_count: 9
  slug: orkas-agentic-access
  summary_line: 9 operations · 4 acting
api_count: 1
apis:
- baseURL: https://orkas.ai
  baseurl_source: spec
  description: The Audio API from Orkas — 2 operation(s) for audio.
  name: Orkas Audio API
  slug: orkas-audio-api
- baseURL: https://orkas.ai
  baseurl_source: spec
  description: The Images API from Orkas — 2 operation(s) for images.
  name: Orkas Images API
  slug: orkas-images-api
- baseURL: https://orkas.ai
  baseurl_source: spec
  description: The Openapi.json API from Orkas — 1 operation(s) for openapi.json.
  name: Orkas Openapi.json API
  slug: orkas-openapi-json-api
- baseURL: https://orkas.ai
  baseurl_source: spec
  description: The Search API from Orkas — 1 operation(s) for search.
  name: Orkas Search API
  slug: orkas-search-api
- baseURL: https://orkas.ai
  baseurl_source: spec
  description: The Videos API from Orkas — 2 operation(s) for videos.
  name: Orkas Videos API
  slug: orkas-videos-api
- baseURL: https://orkas.ai
  baseurl_source: spec
  description: The Chat Completions API from Orkas — 1 operation(s) for chat completions.
  name: Orkas Chat Completions API
  slug: orkas-chat-completions-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/orkas/agentic-access/orkas-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/orkas-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/orkas/plans/orkas-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/orkas-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/orkas/rules/orkas-rules.yml
  title: ''
  type: Spectral
  url: rules/orkas-rules.yml
- group: design
  href: https://artifacts.apis.io/orkas/json-ld/orkas-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/orkas-context.jsonld
- group: design
  href: https://artifacts.apis.io/orkas/vocabulary/orkas-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/orkas-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/orkas/data-model/orkas-data-model.yml
  title: ''
  type: DataModel
  url: data-model/orkas-data-model.yml
- group: design
  href: https://artifacts.apis.io/orkas/errors/orkas-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/orkas-problem-types.yml
- group: design
  href: https://artifacts.apis.io/orkas/conformance/orkas-conformance.yml
  title: ''
  type: Conformance
  url: conformance/orkas-conformance.yml
- group: agent
  href: https://artifacts.apis.io/orkas/llms/orkas-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/orkas-llms.txt
- group: other
  href: https://artifacts.apis.io/orkas/hosts/orkas-hosts.yml
  title: ''
  type: Hosts
  url: hosts/orkas-hosts.yml
- group: other
  href: https://artifacts.apis.io/orkas/vendors/orkas-vendors.yml
  title: ''
  type: Vendors
  url: vendors/orkas-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://orkas.ai/security/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://orkas.ai/use/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://orkas.ai/llms.txt
- group: auth
  href: https://artifacts.apis.io/orkas/authentication/orkas-authentication.yml
  title: ''
  type: Authentication
  url: authentication/orkas-authentication.yml
- group: auth
  href: https://artifacts.apis.io/orkas/security/orkas-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/orkas-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://orkas.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://orkas.ai/api-docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://orkas.ai/pricing/
- group: company
  title: ''
  type: Blog
  url: https://orkas.ai/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://orkas.ai/views/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://orkas.ai/views/legal/privacy.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Orkas-AI
created: '2026-10-11'
description: Orkas provides a metered OpenAI‑compatible API suite covering chat, search, speech, image and video generation, plus a desktop agent client. The platform enables teams to direct AI agents for research, content creation, product development, and operational workflows, offering scalable, usage‑based pricing and comprehensive documentation.
finops:
- has_sources: true
  method: derived
  name: Orkas Finops
  primary_unit: seat
  service_category: ''
  slug: orkas-finops
  template: false
image: https://orkas.ai/res/og.jpg
jsonld:
- class_count: 2
  name: Orkas Context
  property_count: 6
  slug: orkas-context
layout: provider
modified: '2026-10-11'
name: Orkas
nav: Providers
network: true
overview: 'Orkas publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Audio API, Images API, Openapi.json API, and 3 more. Tagged areas include Company, Artificial Intelligence, Chatbots, and Media.


  The Orkas catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Orkas'' developer surface includes API reference, authentication, documentation, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Orkas Plans Pricing
  plan_count: 4
  slug: orkas-plans-pricing
- name: Orkas Price Estimates
  plan_count: 0
  slug: orkas-price-estimates
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: Orkas API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: orkas-rules
score:
  band: thin
  composite: 37.1
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.8
    catalog_earned_first_party: 12.0
    catalog_gap: 62.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 48.6
    developer_ergonomics: 26.2
    discoverability: 55.4
    operational_transparency: 7.9
  previous_composite: 44.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/orkas/orkas-2026-11-03T140731.png
security:
- kind: authentication
  name: Orkas Authentication
  slug: orkas-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Orkas Domain Security
  slug: orkas-domain-security
  summary_line: TLSv1.3 · HSTS
slug: orkas
tags:
- Company
- Artificial Intelligence
- Chatbots
- Media
website: https://orkas.ai/
---

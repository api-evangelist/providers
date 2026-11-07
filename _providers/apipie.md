---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 7
common:
- group: design
  href: https://artifacts.apis.io/apipie/conformance/apipie-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apipie-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apipie/llms/apipie-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apipie-llms.txt
- group: other
  href: https://artifacts.apis.io/apipie/hosts/apipie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apipie-hosts.yml
- group: other
  href: https://artifacts.apis.io/apipie/vendors/apipie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apipie-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apipie.ai/docs/terms/privacy
- group: start
  title: ''
  type: Login
  url: https://apipie.ai/profile/auth/login
- group: docs
  title: ''
  type: Documentation
  url: https://apipie.ai/docs
- group: company
  title: ''
  type: Blog
  url: https://apipie.ai/blog
- group: auth
  href: https://artifacts.apis.io/apipie/security/apipie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apipie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apipie.ai/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://apipie.ai/mcp
  - status: 200
    url: https://apipie.ai/
  reason: no-developer-program
  state: none
created: '2026-10-26'
description: APIpie offers businesses a single OpenAI‑compatible API that aggregates flagship, premium, and budget models from major AI providers. It provides model aliases, key‑level controls, redundant connections for uptime, and detailed usage and spend visibility, allowing companies to manage AI models without rewriting code.
image: https://apipie.ai/_og/d/c_Apipie,description_~RmxhZ3NoaXAgQUkgbW9kZWxzLCBtYW5hZ2VkIGZvciBidXNpbmVzcw,s_3SD0d65liIULfPUw.png
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 4
  slug: apipie-post-v1-chat-completions-request
- name: PostV1ChatCompletionsResponse
  property_count: 11
  slug: apipie-post-v1-chat-completions-response
- name: PostV1ImagesGenerationsRequest
  property_count: 5
  slug: apipie-post-v1-images-generations-request
- name: PostV1ImagesGenerationsResponse
  property_count: 3
  slug: apipie-post-v1-images-generations-response
jsonld:
- class_count: 4
  name: Apipie Context
  property_count: 18
  slug: apipie-context
layout: provider
modified: '2026-10-26'
name: APIpie
nav: Providers
network: true
overview: 'APIpie is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include OpenAI-compatible API and Redundant routing.


  The APIpie catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  APIpie''s developer surface includes documentation, engineering blog, and 8 more developer resources.'
random_paper: 8
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: APIpie API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: apipie-rules
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 19
    catalog_earned: 34.5
    catalog_earned_first_party: 0.0
    catalog_gap: 80.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.9
  facets:
    access_clarity: 11.8
    contract_governance: 31.8
    contract_quality: 10.7
    developer_ergonomics: 6.0
    discoverability: 46.4
    operational_transparency: 0.0
  previous_composite: 17.5
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/apipie/apipie-2026-11-03T120958.png
security:
- kind: domain-security
  name: Apipie Domain Security
  slug: apipie-domain-security
  summary_line: TLSv1.3 · DMARC
slug: apipie
tags:
- OpenAI-compatible API
- Redundant routing
website: https://apipie.ai/
---

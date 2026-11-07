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
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.5
  scored_at: '2026-11-06'
api_count: 3
apis:
- description: Unified AI API gateway providing OpenAI‑compatible endpoint.
  name: bnrouter API
  slug: bnrouter-api-2
- baseURL: https://YOUR-BASE-URL
  baseurl_source: declared
  description: The Images API from bnrouter — 1 operation(s) for images.
  name: bnrouter Images API
  slug: bnrouter-images-api
- baseURL: https://YOUR-BASE-URL
  baseurl_source: declared
  description: The Chat Completions API from bnrouter — 1 operation(s) for chat completions.
  name: bnrouter Chat Completions API
  slug: bnrouter-chat-completions-api
artifact_total: 9
common:
- group: commercial
  href: https://artifacts.apis.io/bnrouter/plans/bnrouter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bnrouter-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/bnrouter/rules/bnrouter-rules.yml
  title: ''
  type: Spectral
  url: rules/bnrouter-rules.yml
- group: design
  href: https://artifacts.apis.io/bnrouter/json-ld/bnrouter-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/bnrouter-context.jsonld
- group: design
  href: https://artifacts.apis.io/bnrouter/vocabulary/bnrouter-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bnrouter-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/bnrouter/data-model/bnrouter-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bnrouter-data-model.yml
- group: build
  href: https://artifacts.apis.io/bnrouter/cli/bnrouter-cli.yml
  title: ''
  type: CLI
  url: cli/bnrouter-cli.yml
- group: design
  href: https://artifacts.apis.io/bnrouter/conformance/bnrouter-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bnrouter-conformance.yml
- group: agent
  href: https://artifacts.apis.io/bnrouter/llms/bnrouter-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bnrouter-llms.txt
- group: other
  href: https://artifacts.apis.io/bnrouter/hosts/bnrouter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bnrouter-hosts.yml
- group: other
  href: https://artifacts.apis.io/bnrouter/vendors/bnrouter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bnrouter-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.bnrouter.com/app/sign-in
- group: auth
  href: https://artifacts.apis.io/bnrouter/security/bnrouter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bnrouter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bnrouter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.bnrouter.com/en/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.bnrouter.com/en/docs/api-reference/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.bnrouter.com/en/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bnrouter.com/en/pricing/
- group: operate
  title: ''
  type: Support
  url: https://www.bnrouter.com/en/faq/
coverage:
  checked: '2026-09-27'
  detail: API host returns HTML page for /openapi.json instead of a machine‑readable OpenAPI document.
  evidence:
  - status: 200
    url: https://api.bnrouter.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-27'
description: bnrouter provides a unified AI API gateway that consolidates multiple large language model providers such as Claude, GPT, Gemini, Kimi, DeepSeek, Qwen, Grok, Llama, and Flux behind a single OpenAI‑compatible endpoint. Users can create API keys, set usage quotas, monitor consumption, and pay per use, simplifying integration of diverse AI models into applications. The platform offers multilingual support, detailed documentation, pricing plans, and a developer console for managing keys and monitoring traffic.
image: https://www.bnrouter.com/images/og-1200x630.png
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: bnrouter-post-v1-chat-completions-request
- name: PostV1ImagesGenerationsRequest
  property_count: 4
  slug: bnrouter-post-v1-images-generations-request
jsonld:
- class_count: 2
  name: Bnrouter Context
  property_count: 5
  slug: bnrouter-context
layout: provider
modified: '2026-09-27'
name: bnrouter
nav: Providers
network: true
overview: 'bnrouter is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including Images API, Chat Completions API, and 1 more. Tagged areas include Artificial Intelligence, Gateways, Multi-Model, OpenAI-Compatible, and Developer Tools.


  The bnrouter catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  bnrouter''s developer surface includes CLI, documentation, API reference, getting-started guide, pricing, support, and 12 more developer resources.'
plans:
- name: Bnrouter Plans Pricing
  plan_count: 0
  slug: bnrouter-plans-pricing
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: bnrouter API Rules
  rule_count: 13
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 1
  slug: bnrouter-rules
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 17
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.7
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 20.6
    developer_ergonomics: 23.8
    discoverability: 69.6
    operational_transparency: 0.0
  previous_composite: 26.1
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/bnrouter/bnrouter-2026-10-11T102520.png
security:
- kind: domain-security
  name: Bnrouter Domain Security
  slug: bnrouter-domain-security
  summary_line: TLSv1.3
slug: bnrouter
tags:
- Artificial Intelligence
- Gateways
- Multi-Model
- OpenAI-Compatible
- Developer Tools
website: https://www.bnrouter.com/
---

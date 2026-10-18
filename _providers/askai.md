---
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.7
  scored_at: '2026-10-17'
api_count: 3
apis:
- description: API for GPTfy's AI services, offering chat and content generation endpoints.
  name: AskAI API
  slug: askai-api-2
- description: The GPTfy API API from GPTfy — 1 operation(s) for gptfy api.
  name: GPTfy GPTfy API
  slug: askai-gptfy-api-api
- description: The Chat Completions API from GPTfy — 1 operation(s) for chat completions.
  name: GPTfy Chat Completions API
  slug: askai-chat-completions-api
artifact_total: 9
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/plans/askai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/askai-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/rules/askai-rules.yml
  title: ''
  type: Spectral
  url: rules/askai-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/json-ld/askai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/askai-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/vocabulary/askai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/askai-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/data-model/askai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/askai-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/conformance/askai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/askai-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/well-known/askai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/askai-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/hosts/askai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/askai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://askai.free/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://askai.free/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://askai.free/pricing
- group: start
  title: ''
  type: Login
  url: https://askai.free/login
- group: docs
  title: ''
  type: Documentation
  url: https://askai.free/ja/guides/translation
- group: company
  title: ''
  type: Blog
  url: https://askai.free/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://askai.free/faq/getting-started
- group: company
  title: ''
  type: Website
  url: https://askai.free/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/askai/refs/heads/main/security/askai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/askai-domain-security.yml
coverage:
  checked: '2026-10-16'
  detail: Documentation pages exist but no OpenAPI, GraphQL, or other machine-readable contract was found.
  evidence:
  - status: 200
    url: https://askai.free/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-16'
description: GPTfy is an emerging AI-powered platform that offers advanced language model services, including chat, content generation, and specialized AI assistants. The company focuses on providing customizable AI solutions for businesses and developers, emphasizing ease of integration, scalability, and robust performance. While still in early stages, GPTfy aims to differentiate itself through a user-friendly API, transparent pricing, and strong data privacy practices, positioning itself within the competitive generative AI market.
image: https://askai.free/static/og/og-home.png
json_schemas:
- name: GetV1V1IdResponse
  property_count: 1
  slug: askai-get-v1-v1-id-response
- name: PostV1ChatCompletionsRequest
  property_count: 3
  slug: askai-post-v1-chat-completions-request
jsonld:
- class_count: 2
  name: Askai Context
  property_count: 4
  slug: askai-context
layout: provider
modified: '2026-10-16'
name: GPTfy
nav: Providers
network: true
overview: 'GPTfy is listed with 3 APIs on the [APIs.io](https://apis.io/) network, including GPTfy API, Chat Completions API, and 1 more. Tagged areas include Company, Artificial Intelligence, Language-Model, and Platform.


  The GPTfy catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  GPTfy''s developer surface includes pricing, documentation, engineering blog, getting-started guide, and 13 more developer resources.'
plans:
- name: Askai Plans Pricing
  plan_count: 3
  slug: askai-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: GPTfy API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: askai-rules
score:
  band: thin
  composite: 34.7
  coverage:
    artifact_dirs: 14
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 20.1
    developer_ergonomics: 23.8
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 3
      marker_coverage: 100.0
      total: 3
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 22.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 0.0
security:
- kind: domain-security
  name: Askai Domain Security
  slug: askai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: askai
tags:
- Company
- Artificial Intelligence
- Language-Model
- Platform
website: https://askai.free/
---

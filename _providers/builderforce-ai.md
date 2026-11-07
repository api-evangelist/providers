---
access_model:
  confidence: low
  label: Free
  onboarding: unknown
  pricing: free
  public: false
  source:
  - plans
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
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 15.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for Builderforce AI platform, as documented on the developer portal.
  name: Builderforce AI API
  slug: builderforce-ai-api-2
- baseURL: https://api.builderforce.ai
  baseurl_source: declared
  description: 'Builderforce.ai API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-11-03); not the provider''s own document.'
  name: Builderforce.ai API
  slug: builderforce-ai-api
artifact_total: 8
common:
- group: commercial
  href: https://artifacts.apis.io/builderforce-ai/plans/builderforce-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/builderforce-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/builderforce-ai/rules/builderforce-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/builderforce-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/builderforce-ai/json-ld/builderforce-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/builderforce-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/builderforce-ai/vocabulary/builderforce-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/builderforce-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/builderforce-ai/data-model/builderforce-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/builderforce-ai-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://builderforce.ai/legal/compliance
- group: design
  href: https://artifacts.apis.io/builderforce-ai/conformance/builderforce-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/builderforce-ai-conformance.yml
- group: other
  href: https://artifacts.apis.io/builderforce-ai/hosts/builderforce-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/builderforce-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/builderforce-ai/vendors/builderforce-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/builderforce-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://builderforce.ai/legal/terms
- group: operate
  title: ''
  type: Support
  url: https://builderforce.ai/seat/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://builderforce.ai/legal/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://builderforce.ai/media
- group: start
  title: ''
  type: Login
  url: https://builderforce.ai/login
- group: start
  title: ''
  type: DeveloperPortal
  url: https://builderforce.ai/developers
- group: start
  title: ''
  type: GettingStarted
  url: https://builderforce.ai/blog/getting-started-with-ai-agents
- group: auth
  href: https://artifacts.apis.io/builderforce-ai/security/builderforce-ai-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/builderforce-ai-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/builderforce-ai/security/builderforce-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/builderforce-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://builderforce.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://builderforce.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://builderforce.ai/pricing
- group: company
  title: ''
  type: Blog
  url: https://builderforce.ai/blog
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.builderforce.ai/mcp
  - status: 200
    url: https://builderforce.ai/
  reason: partner-login
  state: gated
created: '2026-11-03'
description: Builderforce.ai provides a creative canvas where teams and AI agents collaboratively design, build, review, and deliver websites, workflows, models, data stories, and products in a unified visual workspace. It aims to eliminate tool sprawl by integrating project management, AI-driven coding, and visual AI extensions, supporting human‑in‑the‑loop workflows and agentic cloud capabilities.
image: https://builderforce.ai/og-image.png
json_schemas:
- name: PostV1ChatCompletionsRequest
  property_count: 2
  slug: builderforce-ai-post-v1-chat-completions-request
jsonld:
- class_count: 1
  name: Builderforce Ai Context
  property_count: 2
  slug: builderforce-ai-context
layout: provider
modified: '2026-11-03'
name: Builderforce.ai
nav: Providers
network: true
overview: 'Builderforce.ai is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include AI Agents, Low-Code, Marketplace, and Governance.


  The Builderforce.ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Builderforce.ai''s developer surface includes support, getting-started guide, documentation, pricing, engineering blog, and 17 more developer resources.'
plans:
- name: Builderforce Ai Plans Pricing
  plan_count: 1
  slug: builderforce-ai-plans-pricing
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 79
  extends:
  - spectral:oas
  name: Builderforce.ai API Rules
  rule_count: 38
  severity_counts:
    error: 36
    hint: 0
    info: 1
    warn: 1
  slug: builderforce-ai-rules
score:
  band: thin
  composite: 27.5
  coverage:
    artifact_dirs: 17
    catalog_earned: 51.2
    catalog_earned_first_party: 8.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 22.0
    contract_quality: 19.0
    developer_ergonomics: 19.0
    discoverability: 49.1
    operational_transparency: 0.0
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
    score: 17.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Builderforce Ai Domain Security
  slug: builderforce-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Builderforce Ai Trust Center
  slug: builderforce-ai-trust-center
  summary_line: SOC 2
slug: builderforce-ai
tags:
- AI Agents
- Low-Code
- Marketplace
- Governance
website: https://builderforce.ai/
---

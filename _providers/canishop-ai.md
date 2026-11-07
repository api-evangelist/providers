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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: flavored
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Agent checkout API for CanIShop platform
  name: CanIShop API
  slug: canishop-api
- baseURL: https://canishop.ai
  baseurl_source: declared
  description: Agent checkout reviews. Public, unverified purchase-attempt observations. No reports means unknown compatibility. Never submit personal or payment data. All API reads and writes require an active regi
  name: CanIShop API API
  slug: canishop-api-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/canishop-ai/rules/canishop-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/canishop-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/canishop-ai/json-ld/canishop-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/canishop-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/canishop-ai/vocabulary/canishop-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/canishop-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/canishop-ai/conventions/canishop-ai-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/canishop-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/canishop-ai/conventions/canishop-ai-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canishop-ai-conventions.yml
- group: design
  href: https://artifacts.apis.io/canishop-ai/conformance/canishop-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canishop-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/canishop-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/canishop-ai/data-model/canishop-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canishop-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/canishop-ai/errors/canishop-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canishop-ai-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/canishop-ai/llms/canishop-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canishop-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/canishop-ai/a2a/canishop-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/canishop-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/canishop-ai/well-known/canishop-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canishop-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/canishop-ai/hosts/canishop-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/canishop-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/canishop-ai/vendors/canishop-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/canishop-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://canishop.ai/terms
- group: start
  title: ''
  type: SignUp
  url: https://canishop.ai/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://canishop.ai/privacy
- group: docs
  title: ''
  type: APIReference
  url: https://canishop.ai/developers
- group: auth
  href: https://artifacts.apis.io/canishop-ai/security/canishop-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canishop-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://canishop.ai/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://canishop.ai/openapi.json
  - status: 401
    url: https://canishop.ai/mcp
  - status: 200
    url: https://canishop.ai/
  reason: partner-login
  state: gated
created: '2026-11-04'
description: CanIShop is a platform that aggregates and shares checkout experiences for AI agents. It provides reviews of bot blocks, payment outcomes, and effort required during shopping, helping agents understand and improve their purchasing workflows. Users can read and contribute reports about checkout successes, failures, and the steps needed, fostering a community-driven knowledge base for automated commerce.
json_schemas:
- name: CommentInput
  property_count: 2
  slug: canishop-ai-comment-input
- name: MerchantImport
  property_count: 1
  slug: canishop-ai-merchant-import
- name: MerchantInput
  property_count: 6
  slug: canishop-ai-merchant-input
- name: MerchantPatch
  property_count: 6
  slug: canishop-ai-merchant-patch
- name: Moderation
  property_count: 1
  slug: canishop-ai-moderation
- name: ReviewInput
  property_count: 15
  slug: canishop-ai-review-input
jsonld:
- class_count: 6
  name: Canishop Ai Context
  property_count: 24
  slug: canishop-ai-context
layout: provider
modified: '2026-11-04'
name: CanIShop
nav: Providers
network: true
overview: 'CanIShop publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including API API, and 1 more. Tagged areas include Checkout Reviews, Agent Directory, and AI Agents.


  The CanIShop catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  CanIShop''s developer surface includes signup flow, API reference, and 18 more developer resources.'
random_paper: 20
rules:
- authorship: generated
  effective_rule_count: 100
  extends:
  - spectral:oas
  name: CanIShop API Rules
  rule_count: 59
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 3
  slug: canishop-ai-rules
score:
  band: thin
  composite: 26.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 55.8
    catalog_earned_first_party: 0.0
    catalog_gap: 59.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 57.7
    developer_ergonomics: 5.4
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 18.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Canishop Ai Domain Security
  slug: canishop-ai-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: canishop-ai-agent
  slug: canishop-ai-agent
slug: canishop-ai
tags:
- Checkout Reviews
- Agent Directory
- AI Agents
website: https://canishop.ai/
---

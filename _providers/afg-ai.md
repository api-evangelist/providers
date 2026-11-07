---
access_model:
  confidence: low
  label: Requires approval
  onboarding: approval
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 29.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'AFG (Agent Fulfillment Guarantee) agent API, MVP. **MOCK LEDGER ONLY: test tokens, no real money, no mainnet, no custody.** Agents are identified by wallet address. State-changing calls must carry X-A'
  name: AFG Agent API
  slug: afg-agent-api
- description: AFG (Agent Fulfillment Guarantee) agent API, MVP.
  name: AFG agent API V1 API
  slug: afg-agent-api-v1-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/afg-ai/rules/afg-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/afg-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/afg-ai/json-ld/afg-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/afg-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/afg-ai/vocabulary/afg-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/afg-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/afg-ai/data-model/afg-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/afg-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/afg-ai/errors/afg-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/afg-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/afg-ai/conformance/afg-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/afg-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/afg-ai/llms/afg-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/afg-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/afg-ai/a2a/afg-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/afg-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/afg-ai/well-known/afg-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/afg-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/afg-ai/hosts/afg-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/afg-ai-hosts.yml
- group: auth
  href: https://artifacts.apis.io/afg-ai/security/afg-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/afg-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://afg.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://afg.ai/v1/docs
- group: docs
  title: ''
  type: APIReference
  url: https://afg.ai/v1/openapi.json
- group: operate
  title: ''
  type: Support
  url: https://afg.ai/spec/
created: '2026-10-31'
description: AFG (Agent Fulfillment Guarantee) is an early‑access concept platform that enables agents to hire other agents for outcome‑based work. It provides a non‑custodial escrow and bonded mediation system that guarantees payment only upon successful completion, or refunds otherwise. Currently in concept stage with a draft specification and a waitlist for early adopters.
image: https://afg.ai/pivot/og/afg-pivot-og.png
json_schemas:
- name: ArtifactIn
  property_count: 2
  slug: afg-ai-artifact-in
- name: FundBody
  property_count: 1
  slug: afg-ai-fund-body
- name: JobCreate
  property_count: 1
  slug: afg-ai-job-create
- name: OwnerClaimIn
  property_count: 6
  slug: afg-ai-owner-claim-in
- name: RatingIn
  property_count: 1
  slug: afg-ai-rating-in
- name: SignBody
  property_count: 1
  slug: afg-ai-sign-body
jsonld:
- class_count: 12
  name: Afg Ai Context
  property_count: 25
  slug: afg-ai-context
layout: provider
modified: '2026-10-31'
name: AFG
nav: Providers
network: true
overview: 'AFG publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including agent API V1 API, and 1 more. Tagged areas include Artificial Intelligence, Agents, Marketplace, Escrow, and Early-Access.


  The AFG catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  AFG''s developer surface includes documentation, API reference, support, and 12 more developer resources.'
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: AFG API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: afg-ai-rules
score:
  band: emerging
  composite: 22.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.2
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 51.6
    developer_ergonomics: 10.7
    discoverability: 57.1
    operational_transparency: 0.0
  previous_composite: 24.8
  provenance:
    conformance: derived
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Afg Ai Domain Security
  slug: afg-ai-domain-security
  summary_line: TLSv1.3
slug: afg-ai
tags:
- Artificial Intelligence
- Agents
- Marketplace
- Escrow
- Early-Access
website: https://afg.ai/
---

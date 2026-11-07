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
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
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
  score: 21.4
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: On-chain market data API providing asset, token, and price information across multiple chains.
  name: Serialized Data API
  slug: serialized-data-api
artifact_total: 8
asyncapis:
- description: ''
  name: Serialized Xyz Webhooks
  slug: serialized-xyz-webhooks
common:
- group: design
  href: https://artifacts.apis.io/serialized-xyz/rules/serialized-xyz-rules.yml
  title: ''
  type: Spectral
  url: rules/serialized-xyz-rules.yml
- group: design
  href: https://artifacts.apis.io/serialized-xyz/json-ld/serialized-xyz-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/serialized-xyz-context.jsonld
- group: design
  href: https://artifacts.apis.io/serialized-xyz/vocabulary/serialized-xyz-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/serialized-xyz-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/serialized-xyz/conformance/serialized-xyz-conformance.yml
  title: ''
  type: Conformance
  url: conformance/serialized-xyz-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/serialized-xyz/plans/serialized-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/serialized-xyz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/serialized-xyz/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/serialized-xyz/asyncapi/serialized-xyz-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/serialized-xyz-webhooks.yml
- group: design
  href: https://artifacts.apis.io/serialized-xyz/data-model/serialized-xyz-data-model.yml
  title: ''
  type: DataModel
  url: data-model/serialized-xyz-data-model.yml
- group: auth
  href: https://artifacts.apis.io/serialized-xyz/authentication/serialized-xyz-authentication.yml
  title: ''
  type: Authentication
  url: authentication/serialized-xyz-authentication.yml
- group: design
  href: https://artifacts.apis.io/serialized-xyz/errors/serialized-xyz-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/serialized-xyz-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/serialized-xyz/llms/serialized-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/serialized-xyz-llms.txt
- group: other
  href: https://artifacts.apis.io/serialized-xyz/a2a/serialized-xyz-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/serialized-xyz-a2a.yml
- group: agent
  href: https://artifacts.apis.io/serialized-xyz/well-known/serialized-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/serialized-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/serialized-xyz/hosts/serialized-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/serialized-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/serialized-xyz/vendors/serialized-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/serialized-xyz-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://serialized.xyz/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.serialized.xyz/plans
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.serializedaudit.io
- group: auth
  href: https://artifacts.apis.io/serialized-xyz/security/serialized-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/serialized-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://serialized.xyz
- group: docs
  title: ''
  type: Documentation
  url: https://docs.serialized.xyz
- group: docs
  title: ''
  type: APIReference
  url: https://docs.serialized.xyz
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.serialized.xyz/quickstart
- group: operate
  title: ''
  type: Support
  url: https://docs.serialized.xyz/support
- group: commercial
  title: ''
  type: TermsOfService
  url: https://serialized.xyz/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://serialized.xyz/privacy
created: '2026-10-28'
description: Serialized provides on‑chain market data and token security APIs. It offers real‑time price, metadata, wallet activity, and AI‑driven token code analysis across multiple EVM and Solana chains. The platform serves trading apps, terminals, and wallets with high‑performance REST and WebSocket endpoints, detailed documentation, and flexible pricing plans for developers and enterprises.
image: https://serialized.xyz/assets/img/og.png
jsonld:
- class_count: 20
  name: Serialized Xyz Context
  property_count: 92
  slug: serialized-xyz-context
layout: provider
modified: '2026-10-28'
name: Serialized
nav: Providers
network: true
overview: 'Serialized publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Onchain, Market Data, Token Security, and Data.


  The Serialized catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Serialized''s developer surface includes authentication, signup flow, pricing, documentation, API reference, getting-started guide, support, and 19 more developer resources.'
plans:
- name: Serialized Xyz Plans Pricing
  plan_count: 5
  slug: serialized-xyz-plans-pricing
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Serialized API Rules
  rule_count: 50
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 2
  slug: serialized-xyz-rules
score:
  band: developing
  composite: 42.0
  coverage:
    artifact_dirs: 23
    catalog_earned: 65.8
    catalog_earned_first_party: 12.0
    catalog_gap: 49.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -6.7
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 53.2
    developer_ergonomics: 35.1
    discoverability: 73.2
    operational_transparency: 7.9
  previous_composite: 48.7
  provenance:
    conformance: derived
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Securities & Market Data
    regime_id: securities_market_data
    score: 25.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/serialized-xyz/serialized-xyz-2026-11-03T143041.png
security:
- kind: authentication
  name: Serialized Xyz Authentication
  slug: serialized-xyz-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Serialized Xyz Domain Security
  slug: serialized-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: serialized-xyz-set-webhook
  slug: serialized-xyz-set-webhook
slug: serialized-xyz
tags:
- Company
- Onchain
- Market Data
- Token Security
- Data
website: https://serialized.xyz
---

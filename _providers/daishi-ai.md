---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: derived
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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.4
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: 'How Daishi tests AI agents: the benchmark rubric, evaluation governance, alignment tracks, connecting an agent over MCP, and the Studio and developer APIs.'
  name: Daishi Studio API
  slug: daishi-studio-api
artifact_total: 6
common:
- group: operate
  href: https://artifacts.apis.io/daishi-ai/rate-limits/daishi-ai-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/daishi-ai-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/daishi-ai/plans/daishi-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/daishi-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/daishi-ai/vocabulary/daishi-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/daishi-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/daishi-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/daishi-ai/changelog/daishi-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/daishi-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/daishi-ai/authentication/daishi-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/daishi-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/daishi-ai/conformance/daishi-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/daishi-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/daishi-ai/llms/daishi-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/daishi-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/daishi-ai/well-known/daishi-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/daishi-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/daishi-ai/hosts/daishi-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/daishi-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/daishi-ai/vendors/daishi-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/daishi-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/daishi-ai/packages/daishi-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/daishi-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/daishi-ai/packages/daishi-ai-packages.yml
  title: ''
  type: Packages
  url: packages/daishi-ai-packages.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://daishi.ai/pricing
- group: operate
  title: ''
  type: ChangeLog
  url: https://daishi.ai/docs/developer/changelog
- group: auth
  href: https://artifacts.apis.io/daishi-ai/security/daishi-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/daishi-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://daishi.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://daishi.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://daishi.ai/api/v1/openapi.json
- group: commercial
  title: ''
  type: TermsOfService
  url: https://daishi.ai/docs/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://daishi.ai/docs/privacy
created: '2026-10-29'
description: Daishi AI is an independent platform that provides a persistent virtual world for AI agents to interact, compete, and be evaluated. It offers a shared environment where agents can trade, build, train, and survive a scarcity economy, as well as a Studio for running chess and Connect Four matches. The platform exposes a Model Context Protocol (MCP) server for programmatic access, and includes a benchmark rubric, evaluation governance, and open APIs for developers to integrate and test their agents.
image: https://daishi.ai/favicon.ico
layout: provider
modified: '2026-10-29'
name: daishi-ai
nav: Providers
network: true
overview: 'daishi-ai is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include AI, Agents, Platform, Evaluation, and Simulation.


  daishi-ai''s developer surface includes changelog, authentication, pricing, documentation, API reference, and 16 more developer resources.'
plans:
- name: Daishi Ai Plans Pricing
  plan_count: 4
  slug: daishi-ai-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 4
  name: Daishi Ai Rate Limits
  slug: daishi-ai-rate-limits
score:
  band: thin
  composite: 35.0
  coverage:
    artifact_dirs: 15
    catalog_earned: 62.3
    catalog_earned_first_party: 24.0
    catalog_gap: 52.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 63.2
    contract_governance: 8.3
    contract_quality: 0.0
    developer_ergonomics: 37.5
    discoverability: 66.1
    operational_transparency: 47.4
  provenance:
    conformance: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Daishi Ai Authentication
  slug: daishi-ai-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Daishi Ai Domain Security
  slug: daishi-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: daishi-ai-create-experiment
  slug: daishi-ai-create-experiment
slug: daishi-ai
tags:
- AI
- Agents
- Platform
- Evaluation
- Simulation
- Marketplace
- Benchmark
website: https://daishi.ai/
---

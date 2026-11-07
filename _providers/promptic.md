---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
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
    error_semantics: derived
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
  score: 5.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Promptic Agentic Access
  operation_count: 1
  slug: promptic-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: API for managing AI components, experiments, traces, and evaluations.
  name: Promptic API
  slug: promptic-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/promptic/agentic-access/promptic-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/promptic-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/promptic/plans/promptic-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/promptic-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/promptic/rules/promptic-rules.yml
  title: ''
  type: Spectral
  url: rules/promptic-rules.yml
- group: design
  href: https://artifacts.apis.io/promptic/vocabulary/promptic-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/promptic-vocabulary.yml
- group: build
  href: https://artifacts.apis.io/promptic/cli/promptic-cli.yml
  title: ''
  type: CLI
  url: cli/promptic-cli.yml
- group: design
  href: https://artifacts.apis.io/promptic/conventions/promptic-conventions.yml
  title: ''
  type: Conventions
  url: conventions/promptic-conventions.yml
- group: auth
  href: https://artifacts.apis.io/promptic/authentication/promptic-authentication.yml
  title: ''
  type: Authentication
  url: authentication/promptic-authentication.yml
- group: design
  href: https://artifacts.apis.io/promptic/errors/promptic-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/promptic-problem-types.yml
- group: design
  href: https://artifacts.apis.io/promptic/conformance/promptic-conformance.yml
  title: ''
  type: Conformance
  url: conformance/promptic-conformance.yml
- group: agent
  href: https://artifacts.apis.io/promptic/llms/promptic-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/promptic-llms.txt
- group: agent
  href: https://artifacts.apis.io/promptic/well-known/promptic-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/promptic-well-known.yml
- group: other
  href: https://artifacts.apis.io/promptic/hosts/promptic-hosts.yml
  title: ''
  type: Hosts
  url: hosts/promptic-hosts.yml
- group: other
  href: https://artifacts.apis.io/promptic/vendors/promptic-vendors.yml
  title: ''
  type: Vendors
  url: vendors/promptic-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://promptic.eu/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://promptic.eu/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://promptic.eu/docs/guides/dashboard-quickstart
- group: docs
  title: ''
  type: APIReference
  url: https://promptic.eu/docs/openapi
- group: auth
  href: https://artifacts.apis.io/promptic/security/promptic-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/promptic-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://promptic.eu/
- group: docs
  title: ''
  type: Documentation
  url: https://promptic.eu/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://promptic.eu/pricing
- group: company
  title: ''
  type: Blog
  url: https://promptic.eu/blog
- group: start
  title: ''
  type: SignUp
  url: https://promptic.eu/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://promptic.eu/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://promptic.eu/privacy
created: '2026-10-18'
description: Promptic provides an AI optimization platform that enables one‑click prompt optimization, benchmarking, and tuning for large language models and AI agents. It captures OpenTelemetry data from LLM calls, evaluates performance against custom KPIs such as quality, cost, and latency, and automatically generates configurations to improve prompt and agent performance. The service offers features like model selection, prompt tuning, agent architecture optimization, and tool usage analytics, targeting enterprises seeking to scale generative AI across their organization.
image: https://promptic.eu/promptic-preview-image.png
layout: provider
modified: '2026-10-18'
name: Promptic
nav: Providers
network: true
overview: 'Promptic is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Optimization, Enterprise, and LLM.


  The Promptic catalog on APIs.io includes 1 Spectral governance ruleset.


  Promptic''s developer surface includes CLI, authentication, changelog, getting-started guide, API reference, documentation, pricing, and 18 more developer resources.'
plans:
- name: Promptic Plans Pricing
  plan_count: 4
  slug: promptic-plans-pricing
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Promptic API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: promptic-rules
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 20
    catalog_earned: 54.8
    catalog_earned_first_party: 12.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.8
  facets:
    access_clarity: 53.9
    contract_governance: 22.0
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 73.2
    operational_transparency: 13.2
  previous_composite: 39.8
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/promptic/promptic-2026-11-03T141612.png
security:
- kind: authentication
  name: Promptic Authentication
  slug: promptic-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Promptic Domain Security
  slug: promptic-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: promptic
tags:
- Company
- Artificial Intelligence
- Optimization
- Enterprise
- LLM
website: https://promptic.eu/
---

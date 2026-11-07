---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 32.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public REST API for Pocket Agent providing brain, memory, personas, etc.
  name: Pocket Agent REST API
  slug: pocket-agent-rest-api
- baseURL: https://aipocketagent.com/api/v1
  baseurl_source: declared
  description: PA is your brain. Bring any agent. This API exposes your brain files, memory tiers, personas, and privacy zones to any client that speaks REST. Authenticate with a `pa_live_` API key as a Bearer token
  name: Pocket Agent — Public REST API V1 API
  slug: pocket-agent-public-rest-api-v1-api
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/aipocketagent-com/plans/aipocketagent-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aipocketagent-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/aipocketagent-com/rules/aipocketagent-com-rules.yml
  title: ''
  type: Spectral
  url: rules/aipocketagent-com-rules.yml
- group: design
  href: https://artifacts.apis.io/aipocketagent-com/errors/aipocketagent-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/aipocketagent-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/aipocketagent-com/conformance/aipocketagent-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/aipocketagent-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/aipocketagent-com/llms/aipocketagent-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aipocketagent-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/aipocketagent-com/well-known/aipocketagent-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aipocketagent-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/aipocketagent-com/hosts/aipocketagent-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aipocketagent-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/aipocketagent-com/vendors/aipocketagent-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aipocketagent-com-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://aipocketagent.com/app/login
- group: start
  title: ''
  type: GettingStarted
  url: https://aipocketagent.com/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/aipocketagent-com/security/aipocketagent-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aipocketagent-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aipocketagent.com/
- group: docs
  title: ''
  type: Documentation
  url: https://aipocketagent.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://aipocketagent.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aipocketagent.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aipocketagent.com/privacy
created: '2026-11-01'
description: Pocket Agent provides an AI‑driven workspace that automates business tasks across tools. It offers a suite of agents for lead generation, sales outreach, content creation, research, and operations, targeting coaches, consultants, agencies, and small businesses. The platform integrates with existing workflows, allowing owners to deploy AI agents that remember business specifics, act only with approval, and streamline repetitive work, all for a flat monthly fee.
image: https://aipocketagent.com/og-share.png
layout: provider
modified: '2026-11-01'
name: Pocket Agent
nav: Providers
network: true
overview: 'Pocket Agent publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including — Public REST API V1 API, and 1 more. Tagged areas include Artificial Intelligence, Automation, Business, Software-as-a-Service, and Productivity.


  The Pocket Agent catalog on APIs.io includes 1 Spectral governance ruleset.


  Pocket Agent''s developer surface includes getting-started guide, documentation, pricing, and 13 more developer resources.'
plans:
- name: Aipocketagent Com Plans Pricing
  plan_count: 6
  slug: aipocketagent-com-plans-pricing
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Pocket Agent API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: aipocketagent-com-rules
score:
  band: thin
  composite: 31.6
  coverage:
    artifact_dirs: 13
    catalog_earned: 53.5
    catalog_earned_first_party: 12.0
    catalog_gap: 61.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.2
  facets:
    access_clarity: 53.9
    contract_governance: 18.2
    contract_quality: 37.3
    developer_ergonomics: 10.7
    discoverability: 66.1
    operational_transparency: 0.0
  previous_composite: 38.8
  provenance:
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
security:
- kind: domain-security
  name: Aipocketagent Com Domain Security
  slug: aipocketagent-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: aipocketagent-com
tags:
- Artificial Intelligence
- Automation
- Business
- Software-as-a-Service
- Productivity
website: https://aipocketagent.com/
---

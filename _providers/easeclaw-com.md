---
access_model:
  confidence: medium
  label: Paid · Requires approval
  onboarding: approval
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
    agent_skills: unknown
    agentic_access: derived
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 23.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Easeclaw Com Agentic Access
  operation_count: 1
  slug: easeclaw-com-agentic-access
  summary_line: 1 operation
api_count: 1
apis:
- description: REST API for EaseClaw, providing project, leads, and lead management operations.
  name: EaseClaw API
  slug: easeclaw-api
artifact_total: 6
common:
- group: agent
  href: https://artifacts.apis.io/easeclaw-com/agentic-access/easeclaw-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/easeclaw-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/easeclaw-com/plans/easeclaw-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/easeclaw-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/easeclaw-com/rules/easeclaw-com-rules.yml
  title: ''
  type: Spectral
  url: rules/easeclaw-com-rules.yml
- group: agent
  href: https://artifacts.apis.io/easeclaw-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/easeclaw-com/cli/easeclaw-com-cli.yml
  title: ''
  type: CLI
  url: cli/easeclaw-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/easeclaw-com/authentication/easeclaw-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/easeclaw-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/easeclaw-com/conformance/easeclaw-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/easeclaw-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/easeclaw-com/llms/easeclaw-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/easeclaw-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/easeclaw-com/well-known/easeclaw-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/easeclaw-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/easeclaw-com/hosts/easeclaw-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easeclaw-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easeclaw-com/vendors/easeclaw-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easeclaw-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/easeclaw-com/packages/easeclaw-com-packages.yml
  title: ''
  type: SDKs
  url: packages/easeclaw-com-packages.yml
- group: build
  href: https://artifacts.apis.io/easeclaw-com/packages/easeclaw-com-packages.yml
  title: ''
  type: Packages
  url: packages/easeclaw-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.easeclaw.com/terms
- group: operate
  title: ''
  type: Support
  url: https://www.easeclaw.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.easeclaw.com/privacy
- group: start
  title: ''
  type: Login
  url: https://www.easeclaw.com/leads/login
- group: docs
  title: ''
  type: Documentation
  url: https://www.easeclaw.com/guides
- group: docs
  title: ''
  type: APIReference
  url: https://www.easeclaw.com/llms.txt
- group: auth
  href: https://artifacts.apis.io/easeclaw-com/security/easeclaw-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easeclaw-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.easeclaw.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.easeclaw.com/pricing
- group: start
  title: ''
  type: Trial
  url: https://www.easeclaw.com/trial
- group: agent
  title: ''
  type: MCP
  url: https://www.easeclaw.com/mcp
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://easeclaw.com/openapi.json
  - status: null
    url: https://www.easeclaw.com/openapi.json
  - status: 401
    url: https://www.easeclaw.com/api/mcp
  - status: 200
    url: https://easeclaw.com/
  reason: partner-login
  state: gated
created: '2026-11-06'
description: EaseClaw is an AI‑powered agent that automates LinkedIn outreach for sales teams. It finds warm buyers, writes personalized invites and follow‑ups in the user’s voice, and runs the outreach to book meetings. The platform lets users review every message or let the AI run autonomously, aiming to increase conversion rates and streamline prospecting.
image: https://www.easeclaw.com/og.png
layout: provider
modified: '2026-11-06'
name: EaseClaw
nav: Providers
network: true
overview: 'EaseClaw is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Sales, LinkedIn, Outreach, and Automation.


  The EaseClaw catalog on APIs.io includes 1 Spectral governance ruleset.


  EaseClaw''s developer surface includes CLI, authentication, support, documentation, API reference, pricing, and 18 more developer resources.'
plans:
- name: Easeclaw Com Plans Pricing
  plan_count: 2
  slug: easeclaw-com-plans-pricing
random_paper: 1
rules:
- authorship: generated
  effective_rule_count: 64
  extends:
  - spectral:oas
  name: EaseClaw API Rules
  rule_count: 23
  severity_counts:
    error: 21
    hint: 0
    info: 1
    warn: 1
  slug: easeclaw-com-rules
score:
  band: thin
  composite: 33.9
  coverage:
    artifact_dirs: 16
    catalog_earned: 49.5
    catalog_earned_first_party: 8.0
    catalog_gap: 65.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 54.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Easeclaw Com Authentication
  slug: easeclaw-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Easeclaw Com Domain Security
  slug: easeclaw-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: easeclaw-com
tags:
- Artificial Intelligence
- Sales
- LinkedIn
- Outreach
- Automation
website: https://www.easeclaw.com/
---

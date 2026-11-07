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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
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
  score: 6.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documented at the AccrueDev docs site, but no machine‑readable contract was found.
  name: AccrueDev API
  slug: accruedev-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/accruedev-com/plans/accruedev-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accruedev-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/accruedev-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: operate
  href: https://artifacts.apis.io/accruedev-com/changelog/accruedev-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/accruedev-com-changelog.yml
- group: agent
  href: https://artifacts.apis.io/accruedev-com/llms/accruedev-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accruedev-com-llms.txt
- group: other
  href: https://artifacts.apis.io/accruedev-com/hosts/accruedev-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accruedev-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/accruedev-com/vendors/accruedev-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accruedev-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/accruedev-com/packages/accruedev-com-packages.yml
  title: ''
  type: SDKs
  url: packages/accruedev-com-packages.yml
- group: build
  href: https://artifacts.apis.io/accruedev-com/packages/accruedev-com-packages.yml
  title: ''
  type: Packages
  url: packages/accruedev-com-packages.yml
- group: start
  title: ''
  type: Login
  url: https://accruedev.com/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://accruedev.com/changelog/
- group: auth
  href: https://artifacts.apis.io/accruedev-com/security/accruedev-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accruedev-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accruedev.com/
- group: docs
  title: ''
  type: Documentation
  url: https://accruedev.com/docs/
- group: commercial
  title: ''
  type: Pricing
  url: https://accruedev.com/pricing/
- group: company
  title: ''
  type: About
  url: https://accruedev.com/about/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accruedev.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accruedev.com/privacy/
coverage:
  checked: '2026-10-31'
  detail: Docs are public but no OpenAPI, AsyncAPI, GraphQL, or other contract was discovered despite probing API host and docs pages.
  evidence:
  - status: 404
    url: https://api.accruedev.com/openapi.json
  - status: 200
    url: https://accruedev.com/docs/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AccrueDev provides a hands‑on course and an agent store for building AI assistants that run on Claude Code, Anthropic’s command‑line coding assistant. The platform offers ready‑made agents, skills, and commands, along with a memory system, delegation architecture, quality‑gate checks, and production‑ready deployment tools. Users can purchase the course, subscribe to the agent store, and integrate the tools via the accruedev CLI to create, test, and maintain AI‑driven workflows.
image: https://accruedev.com/og-image.png
layout: provider
modified: '2026-10-31'
name: AccrueDev
nav: Providers
network: true
overview: 'AccrueDev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Education, Tools, Claude, and Platform.


  AccrueDev''s developer surface includes changelog, documentation, pricing, and 14 more developer resources.'
plans:
- name: Accruedev Com Plans Pricing
  plan_count: 2
  slug: accruedev-com-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 12
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 18.3
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 24.7
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Accruedev Com Domain Security
  slug: accruedev-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: accruedev-com
tags:
- Artificial Intelligence
- Education
- Tools
- Claude
- Platform
website: https://accruedev.com/
---

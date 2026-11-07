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
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: true
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
  score: 3.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/simular/plans/simular-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/simular-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/simular/security/simular-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/simular-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://simular.ai
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.simular.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.simular.ai/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.simular.ai/simulang-js/api/latest/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.simular.ai/agent-s/quickstart
- group: company
  title: ''
  type: Blog
  url: https://simular.ai/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/simular-ai
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/E2XfsK9fPV
- group: commercial
  title: ''
  type: Pricing
  url: https://simular.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://sai.simular.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://simular.ai/product-sai/privacy
- group: build
  href: https://artifacts.apis.io/simular/packages/simular-packages.yml
  title: ''
  type: Packages
  url: packages/simular-packages.yml
- group: build
  href: https://artifacts.apis.io/simular/packages/simular-packages.yml
  title: ''
  type: SDKs
  url: packages/simular-packages.yml
- group: build
  href: https://artifacts.apis.io/simular/cli/simular-cli.yml
  title: ''
  type: CLI
  url: cli/simular-cli.yml
- group: agent
  href: https://artifacts.apis.io/simular/llms/simular-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/simular-llms.txt
- group: agent
  href: https://artifacts.apis.io/simular/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://artifacts.apis.io/simular/well-known/simular-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/simular-well-known.yml
created: '2026-07-17'
description: Simular is the autonomous computer company. It builds AI agents that operate computers the way people do — clicking, typing, scrolling, and navigating GUIs, APIs, terminals, and code. Its flagship product Sai is a 24/7 AI co-worker that runs on private cloud desktops, and it maintains the open-source Agent-S agentic framework, the OpenACI agent-computer interface, and Simulang, a desktop-automation scripting language with Python (pysimular), Node.js (@simular-ai/simulang-js), and CLI (@simular-ai/simulang) surfaces. Developers integrate Simular through these SDKs and a Claude Code /simulang skill rather than a hosted HTTP API. Simular is backed by Felicis.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/simular.png
layout: provider
modified: '2026-07-21'
name: Simular
nav: Providers
network: true
overview: 'Simular is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, AI Agents, Computer Use, and Browser Automation.


  Simular''s developer surface includes documentation, API reference, getting-started guide, engineering blog, support, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Simular Plans Pricing
  plan_count: 4
  slug: simular-plans-pricing
random_paper: 21
score:
  band: thin
  composite: 28.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 66.7
    discoverability: 55.4
    operational_transparency: 2.6
  previous_composite: 28.8
  provenance:
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/simular/simular-2026-09-02T155604.png
security:
- kind: domain-security
  name: Simular Domain Security
  slug: simular-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 1
skills:
- name: Simulang for Claude Code
  slug: simular-simulang-claude-code
slug: simular
tags:
- Company
- Artificial Intelligence
- AI Agents
- Computer Use
- Browser Automation
- Desktop Automation
- SDK
- Developer Tools
- Open Source
website: https://simular.ai
---

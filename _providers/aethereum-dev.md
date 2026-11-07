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
    agent_card: near-conformant
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
  score: 9.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for Aethereum platform as documented
  name: Aethereum API
  slug: aethereum-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/aethereum-dev/plans/aethereum-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aethereum-dev-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aethereum-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/aethereum-dev/cli/aethereum-dev-cli.yml
  title: ''
  type: CLI
  url: cli/aethereum-dev-cli.yml
- group: agent
  href: https://artifacts.apis.io/aethereum-dev/llms/aethereum-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aethereum-dev-llms.txt
- group: other
  href: https://artifacts.apis.io/aethereum-dev/a2a/aethereum-dev-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/aethereum-dev-a2a.yml
- group: agent
  href: https://artifacts.apis.io/aethereum-dev/well-known/aethereum-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aethereum-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/aethereum-dev/hosts/aethereum-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aethereum-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/aethereum-dev/vendors/aethereum-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aethereum-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.aethereum.dev/legal/terms
- group: auth
  title: ''
  type: Security
  url: https://www.aethereum.dev/security
- group: operate
  title: ''
  type: Roadmap
  url: https://www.aethereum.dev/roadmap
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.aethereum.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.aethereum.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://www.aethereum.dev/signin
- group: start
  title: ''
  type: GettingStarted
  url: https://www.aethereum.dev/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.aethereum.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://www.aethereum.dev/blog
- group: auth
  href: https://artifacts.apis.io/aethereum-dev/security/aethereum-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aethereum-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aethereum.dev/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.aethereum.dev/api/mcp
  - status: 200
    url: https://aethereum.dev/
  reason: partner-login
  state: gated
created: '2026-10-31'
description: Aethereum provides a coordination layer for AI coding agents, enabling multiple AI models such as Claude, Code, Cursor, and Codex to collaborate in real time on a shared screen. It offers features like live code sharing, conflict resolution, integration with various tools, and a no‑signup free tier for teams and hackathons. The platform includes documentation, FAQs, pricing, and a roadmap, positioning itself as a hub for AI‑driven development workflows.
image: https://www.aethereum.dev/opengraph-image?c4cba8f8bf4d5065
layout: provider
modified: '2026-10-31'
name: Aethereum
nav: Providers
network: true
overview: 'Aethereum is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Collaboration, Coordination, Development, and Platform.


  Aethereum''s developer surface includes CLI, pricing, getting-started guide, documentation, engineering blog, and 14 more developer resources.'
plans:
- name: Aethereum Dev Plans Pricing
  plan_count: 1
  slug: aethereum-dev-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 19.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.4
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 25.5
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 28.0
  provenance:
    mcp: unknown
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
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
  name: Aethereum Dev Domain Security
  slug: aethereum-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aethereum-dev
tags:
- Artificial Intelligence
- Collaboration
- Coordination
- Development
- Platform
website: https://aethereum.dev/
---

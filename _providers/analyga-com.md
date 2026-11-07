---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
  score: 2.5
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 4
common:
- group: build
  href: https://artifacts.apis.io/analyga-com/cli/analyga-com-cli.yml
  title: ''
  type: CLI
  url: cli/analyga-com-cli.yml
- group: auth
  href: https://artifacts.apis.io/analyga-com/authentication/analyga-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/analyga-com-authentication.yml
- group: agent
  href: https://artifacts.apis.io/analyga-com/llms/analyga-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/analyga-com-llms.txt
- group: other
  href: https://artifacts.apis.io/analyga-com/hosts/analyga-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/analyga-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/analyga-com/packages/analyga-com-packages.yml
  title: ''
  type: SDKs
  url: packages/analyga-com-packages.yml
- group: build
  href: https://artifacts.apis.io/analyga-com/packages/analyga-com-packages.yml
  title: ''
  type: Packages
  url: packages/analyga-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://analyga.com/terms.html
- group: operate
  title: ''
  type: StatusPage
  url: https://status.analyga.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://analyga.com/privacy.html
- group: auth
  href: https://artifacts.apis.io/analyga-com/security/analyga-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/analyga-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://analyga.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://analyga.com/#features
- group: operate
  title: ''
  type: Support
  url: https://analyga.com/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/jyswee/analyga
- group: commercial
  title: ''
  type: Pricing
  url: https://analyga.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://analyga.com/signup
coverage:
  checked: '2026-11-01'
  detail: Analyga.com provides a SaaS analytics product but does not publish any public API or developer documentation.
  evidence:
  - status: 200
    url: https://analyga.com/
  reason: no-developer-program
  state: none
created: '2026-11-01'
description: Revenue analytics for AI-native SaaS. Board‑ready numbers your whole team reads, organised around your growth funnel — and the only dashboard that counts agent (MCP/AI) traffic as a channel. Track what pays across human and agent traffic, with the raw evidence one click away. If you own revenue at an AI‑native SaaS, GA4 and umami hand you a wall of data and leave you to ask every question a growth leader actually asks, in plain language. MCP and AI agents are already a channel. analyga is the only analytics that counts them alongside your human traffic — tick the box your board will ask about next year.
image: https://prodmedia.tyga.host/public/tyga.cloud/landing/analyga.com/analyga-black-words.svg
layout: provider
modified: '2026-11-01'
name: analyga
nav: Providers
network: true
overview: 'analyga is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include AI-native, Software-as-a-Service, Revenue Analytics, Dashboards, and MCP.


  analyga''s developer surface includes CLI, authentication, getting-started guide, support, pricing, signup flow, and 10 more developer resources.'
plans:
- name: Analyga Com Plans Pricing
  plan_count: 0
  slug: analyga-com-plans-pricing
random_paper: 17
scopes:
- name: Analyga Com Scopes
  scope_count: 0
  slug: analyga-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 19.1
  coverage:
    artifact_dirs: 20
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.1
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 34.5
    discoverability: 48.2
    operational_transparency: 10.5
  previous_composite: 27.2
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Analyga Com Authentication
  slug: analyga-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Analyga Com Domain Security
  slug: analyga-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: analyga-com
tags:
- AI-native
- Software-as-a-Service
- Revenue Analytics
- Dashboards
- MCP
website: https://analyga.com/
---

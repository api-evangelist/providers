---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - plans
  - scopes
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
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
    mcp_server: documented
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
  score: 9.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Public API documented at DiskDrive app site, but no machine‑readable contract found.
  name: DiskDrive API
  slug: diskdrive-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/diskdrive-ai/plans/diskdrive-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/diskdrive-ai-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/diskdrive-ai/changelog/diskdrive-ai-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/diskdrive-ai-changelog.yml
- group: auth
  href: https://artifacts.apis.io/diskdrive-ai/scopes/diskdrive-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/diskdrive-ai-scopes.yml
- group: agent
  href: https://artifacts.apis.io/diskdrive-ai/llms/diskdrive-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/diskdrive-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/diskdrive-ai/well-known/diskdrive-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/diskdrive-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/diskdrive-ai/hosts/diskdrive-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/diskdrive-ai-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://app.diskdrive.ai/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://app.diskdrive.ai/status
- group: auth
  title: ''
  type: Security
  url: https://app.diskdrive.ai/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://app.diskdrive.ai/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://app.diskdrive.ai/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://app.diskdrive.ai/docs
- group: auth
  href: https://artifacts.apis.io/diskdrive-ai/security/diskdrive-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/diskdrive-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://diskdrive.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://app.diskdrive.ai/what-is-diskdrive
- group: commercial
  title: ''
  type: Pricing
  url: https://app.diskdrive.ai/pricing
- group: company
  title: ''
  type: About
  url: https://app.diskdrive.ai/about
coverage:
  detail: Documentation pages exist but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://app.diskdrive.ai/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-05'
description: DiskDrive provides a private, user‑owned drive and memory store for AI assistants. Users can upload files and AI‑generated memories, control per‑AI permissions, and audit actions. The service connects to ChatGPT, Claude, Gemini and other MCP‑compatible assistants, offering subscription plans for individuals and teams. It emphasizes data ownership, explicit access, and portability across AI platforms.
image: https://app.diskdrive.ai/opengraph-image?4ca5ab1c034316aa
layout: provider
modified: '2026-11-05'
name: DiskDrive
nav: Providers
network: true
overview: 'DiskDrive is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Storage, Privacy, Subscription, and DataOwnership.


  DiskDrive''s developer surface includes changelog, getting-started guide, documentation, pricing, and 13 more developer resources.'
plans:
- name: Diskdrive Ai Plans Pricing
  plan_count: 1
  slug: diskdrive-ai-plans-pricing
random_paper: 12
scopes:
- name: Diskdrive Ai Scopes
  scope_count: 4
  slug: diskdrive-ai-scopes
  summary_line: 4 scopes
score:
  band: thin
  composite: 27.0
  coverage:
    artifact_dirs: 11
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 21.4
    discoverability: 57.1
    operational_transparency: 42.1
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 21.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Diskdrive Ai Domain Security
  slug: diskdrive-ai-domain-security
  summary_line: TLSv1.3
slug: diskdrive-ai
tags:
- Artificial Intelligence
- Storage
- Privacy
- Subscription
- DataOwnership
website: https://diskdrive.ai/
---

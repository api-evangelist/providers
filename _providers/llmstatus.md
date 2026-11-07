---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
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
  score: 0.0
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: LLM Status provides API endpoints for model deprecation data, pricing, and alerts.
  name: LLM Status API
  slug: llm-status-api
artifact_total: 2
common:
- group: operate
  href: https://artifacts.apis.io/llmstatus/changelog/llmstatus-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/llmstatus-changelog.yml
- group: other
  href: https://artifacts.apis.io/llmstatus/hosts/llmstatus-hosts.yml
  title: ''
  type: Hosts
  url: hosts/llmstatus-hosts.yml
- group: other
  href: https://artifacts.apis.io/llmstatus/vendors/llmstatus-vendors.yml
  title: ''
  type: Vendors
  url: vendors/llmstatus-vendors.yml
- group: build
  href: https://artifacts.apis.io/llmstatus/packages/llmstatus-packages.yml
  title: ''
  type: SDKs
  url: packages/llmstatus-packages.yml
- group: build
  href: https://artifacts.apis.io/llmstatus/packages/llmstatus-packages.yml
  title: ''
  type: Packages
  url: packages/llmstatus-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://llmstatus.ai/changelog
- group: auth
  href: https://artifacts.apis.io/llmstatus/security/llmstatus-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/llmstatus-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://llmstatus.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://llmstatus.ai/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://llmstatus.ai/pricing
- group: start
  title: ''
  type: SignUp
  url: https://llmstatus.ai/sign-up
- group: other
  title: ''
  type: SignIn
  url: https://llmstatus.ai/sign-in
- group: commercial
  title: ''
  type: TermsOfService
  url: https://llmstatus.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://llmstatus.ai/privacy
coverage:
  checked: '2026-10-18'
  detail: Documentation pages are JavaScript-rendered SPA with no machine‑readable OpenAPI spec.
  evidence:
  - status: 200
    url: https://docs.llmstatus.ai/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-18'
description: LLM Status provides a service that tracks AI model deprecations and retirements, offering developers timely alerts and migration guidance. It includes a CLI tool to scan codebases for model usage and a web dashboard showing model lifecycle status, pricing plans, and documentation. The platform helps prevent broken integrations by notifying users of upcoming model changes, enabling proactive updates.
image: https://llmstatus.ai/opengraph-image?72cd1c5ab8ea556a
layout: provider
modified: '2026-10-18'
name: LLM Status
nav: Providers
network: true
overview: 'LLM Status is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Model, Monitoring, and CLI.


  LLM Status'' developer surface includes changelog, documentation, pricing, signup flow, and 10 more developer resources.'
random_paper: 17
score:
  band: emerging
  composite: 12.7
  coverage:
    artifact_dirs: 11
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 7.9
  previous_composite: 19.7
  provenance:
    mcp: derived
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
screenshot: https://apis.io/screenshots/llmstatus/llmstatus-2026-11-03T135005.png
security:
- kind: domain-security
  name: Llmstatus Domain Security
  slug: llmstatus-domain-security
  summary_line: TLSv1.3 · HSTS
slug: llmstatus
tags:
- Company
- Artificial Intelligence
- Model
- Monitoring
- CLI
website: https://llmstatus.ai/
---

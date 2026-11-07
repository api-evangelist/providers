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
    agent_skills: false
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
  score: 18.7
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API documented at Yavy developer docs providing search and integration capabilities.
  name: Yavy API
  slug: yavy-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/yavy/plans/yavy-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yavy-plans-pricing.yml
- group: build
  href: https://artifacts.apis.io/yavy/cli/yavy-cli.yml
  title: ''
  type: CLI
  url: cli/yavy-cli.yml
- group: agent
  href: https://artifacts.apis.io/yavy/llms/yavy-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yavy-llms.txt
- group: agent
  href: https://artifacts.apis.io/yavy/well-known/yavy-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yavy-well-known.yml
- group: other
  href: https://artifacts.apis.io/yavy/hosts/yavy-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yavy-hosts.yml
- group: other
  href: https://artifacts.apis.io/yavy/vendors/yavy-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yavy-vendors.yml
- group: build
  href: https://artifacts.apis.io/yavy/packages/yavy-packages.yml
  title: ''
  type: SDKs
  url: packages/yavy-packages.yml
- group: build
  href: https://artifacts.apis.io/yavy/packages/yavy-packages.yml
  title: ''
  type: Packages
  url: packages/yavy-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://yavy.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://yavy.dev/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://yavy.dev/pricing
- group: start
  title: ''
  type: Login
  url: https://yavy.dev/login
- group: docs
  title: ''
  type: Documentation
  url: https://yavy.dev/docs
- group: company
  title: ''
  type: Blog
  url: https://yavy.dev/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://yavy.dev/docs/getting-started
- group: auth
  href: https://artifacts.apis.io/yavy/security/yavy-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yavy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://yavy.dev/
coverage:
  checked: '2026-10-19'
  detail: Documentation pages exist but no machine‑readable OpenAPI, GraphQL, AsyncAPI or other contract was found.
  evidence:
  - status: 200
    url: https://yavy.dev/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-19'
description: Yavy provides an AI‑powered knowledge platform that indexes website content and makes it searchable for large language models. Users can integrate Yavy via a CLI, SDKs, or MCP to embed up‑to‑date documentation, pricing, and feature guides into their AI agents, ensuring accurate, hallucination‑free responses. The service offers real‑time syncing, semantic search, and customizable skill packages for developers.
image: https://yavy.dev/images/og.webp
layout: provider
modified: '2026-10-19'
name: Yavy
nav: Providers
network: true
overview: 'Yavy is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Knowledge Base, Search, Integration, and Platform.


  Yavy''s developer surface includes CLI, pricing, documentation, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Yavy Plans Pricing
  plan_count: 3
  slug: yavy-plans-pricing
random_paper: 1
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 13
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 64.3
    operational_transparency: 0.0
  previous_composite: 29.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/yavy/yavy-2026-11-03T150333.png
security:
- kind: domain-security
  name: Yavy Domain Security
  slug: yavy-domain-security
  summary_line: TLSv1.3 · DMARC
slug: yavy
tags:
- Artificial Intelligence
- Knowledge Base
- Search
- Integration
- Platform
- Company
website: https://yavy.dev/
---

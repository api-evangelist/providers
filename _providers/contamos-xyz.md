---
access_model:
  confidence: low
  label: Freemium
  onboarding: unknown
  pricing: freemium
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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 6.7
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/contamos-xyz/plans/contamos-xyz-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/contamos-xyz-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/contamos-xyz/llms/contamos-xyz-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/contamos-xyz-llms.txt
- group: agent
  href: https://artifacts.apis.io/contamos-xyz/well-known/contamos-xyz-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/contamos-xyz-well-known.yml
- group: other
  href: https://artifacts.apis.io/contamos-xyz/hosts/contamos-xyz-hosts.yml
  title: ''
  type: Hosts
  url: hosts/contamos-xyz-hosts.yml
- group: other
  href: https://artifacts.apis.io/contamos-xyz/vendors/contamos-xyz-vendors.yml
  title: ''
  type: Vendors
  url: vendors/contamos-xyz-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://contamos.xyz/en/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/contamos-xyz/security/contamos-xyz-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/contamos-xyz-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://contamos.xyz/
- group: docs
  title: ''
  type: Documentation
  url: https://contamos.xyz/en/docs
- group: company
  title: ''
  type: Blog
  url: https://contamos.xyz/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://contamos.xyz/en
- group: commercial
  title: ''
  type: TermsOfService
  url: https://contamos.xyz/en/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://contamos.xyz/en/privacy
- group: operate
  title: ''
  type: Support
  url: https://contamos.xyz/login
coverage:
  checked: '2026-11-04'
  detail: Docs are public HTML but no machine‑readable OpenAPI, AsyncAPI, GraphQL or gRPC spec was found.
  evidence:
  - status: 200
    url: https://contamos.xyz/en/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Contamos provides a shared ledger platform for managing money across multiple currencies, both fiat and crypto. Users can track balances, budgets, recurring transactions, and integrate AI assistants like Claude or ChatGPT to automate entry and queries. The service offers free and Pro plans with unlimited accounts, members, and history, emphasizing transparency, data export, and privacy. It includes features such as AI‑driven assistance, detailed activity logs, and support for multi‑currency exchange rates, aiming to replace spreadsheets and simplify group finances.
image: https://contamos.xyz/images/og.png
layout: provider
modified: '2026-11-04'
name: Contamos
nav: Providers
network: true
overview: 'Contamos is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Ledger, Multi-Currency, AI Assistant, and Collaboration.


  Contamos'' developer surface includes getting-started guide, documentation, engineering blog, pricing, support, and 9 more developer resources.'
plans:
- name: Contamos Xyz Plans Pricing
  plan_count: 2
  slug: contamos-xyz-plans-pricing
random_paper: 4
score:
  band: emerging
  composite: 20.4
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 13.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Contamos Xyz Domain Security
  slug: contamos-xyz-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: contamos-xyz
tags:
- Finance
- Ledger
- Multi-Currency
- AI Assistant
- Collaboration
website: https://contamos.xyz/
---

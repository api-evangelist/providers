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
  score: 18.2
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for AccountingQB, documented at the developer portal.
  name: AccountingQB API
  slug: accountingqb-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/accountingqb-com/plans/accountingqb-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/accountingqb-com-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/accountingqb-com/llms/accountingqb-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/accountingqb-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/accountingqb-com/well-known/accountingqb-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/accountingqb-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/accountingqb-com/hosts/accountingqb-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/accountingqb-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/accountingqb-com/vendors/accountingqb-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/accountingqb-com-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://accountingqb.com/security
- group: start
  title: ''
  type: Login
  url: https://accountingqb.com/sign-in
- group: operate
  title: ''
  type: ChangeLog
  url: https://accountingqb.com/changelog
- group: auth
  href: https://artifacts.apis.io/accountingqb-com/security/accountingqb-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/accountingqb-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://accountingqb.com/
- group: docs
  title: ''
  type: APIReference
  url: https://accountingqb.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://accountingqb.com/demo
- group: operate
  title: ''
  type: Support
  url: https://accountingqb.com/contact
- group: company
  title: ''
  type: Blog
  url: https://accountingqb.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://accountingqb.com/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://accountingqb.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://accountingqb.com/privacy
coverage:
  checked: '2026-10-31'
  detail: No OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract found on discovered hosts.
  evidence:
  - status: 404
    url: https://api.accountingqb.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: AccountingQB provides an AI‑powered interface to QuickBooks Online, enabling users to ask natural‑language questions about their finances, generate tax workpapers, and receive actionable insights. Built by founder Ryan Colkitt, the platform offers real‑time reconciliation, expense categorization, and financial forecasting without storing user data. It supports both cloud and desktop QuickBooks, integrates with Claude and other AI assistants, and emphasizes zero‑knowledge security with AES‑256‑GCM encryption.
image: https://accountingqb.com/og-image.png
layout: provider
modified: '2026-10-31'
name: AccountingQB
nav: Providers
network: true
overview: 'AccountingQB is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Accounting, Artificial Intelligence, Bookkeeping, Financial Analysis, and Invoice Reconciliation.


  AccountingQB''s developer surface includes changelog, API reference, getting-started guide, support, engineering blog, pricing, and 11 more developer resources.'
plans:
- name: Accountingqb Com Plans Pricing
  plan_count: 3
  slug: accountingqb-com-plans-pricing
random_paper: 10
score:
  band: emerging
  composite: 20.7
  coverage:
    artifact_dirs: 9
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.4
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 57.1
    operational_transparency: 13.2
  previous_composite: 30.1
  provenance:
    mcp: unknown
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
security:
- kind: domain-security
  name: Accountingqb Com Domain Security
  slug: accountingqb-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: accountingqb-com
tags:
- Accounting
- Artificial Intelligence
- Bookkeeping
- Financial Analysis
- Invoice Reconciliation
- CPA Handoff
website: https://accountingqb.com/
---

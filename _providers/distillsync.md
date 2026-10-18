---
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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 14.4
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/distillsync/refs/heads/main/plans/distillsync-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/distillsync-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/distillsync/refs/heads/main/llms/distillsync-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/distillsync-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/distillsync/refs/heads/main/well-known/distillsync-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/distillsync-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/distillsync/refs/heads/main/hosts/distillsync-hosts.yml
  title: ''
  type: Hosts
  url: hosts/distillsync-hosts.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/distillsync/refs/heads/main/security/distillsync-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/distillsync-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://distillsync.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.distillsync.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.distillsync.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://distillsync.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.distillsync.com/auth/signup
- group: start
  title: ''
  type: Login
  url: https://app.distillsync.com/auth/signin
- group: company
  title: ''
  type: Blog
  url: https://distillsync.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://distillsync.com/privacy/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.distillsync.com/docs/empezar/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://distillsync.com/
  reason: no-developer-program
  state: none
created: '2026-10-16'
description: Distillsync provides a semantic integration platform that connects ERP systems with e‑commerce platforms, enabling real‑time synchronization of orders, customers, products, pricing, and inventory. The solution offers a universal API and DSL to automate data flows, supports both cloud and on‑premise deployments, and includes tools for pricing, stock management, and custom business rules. It targets agencies, SaaS providers, and businesses seeking to streamline operations without building individual connectors for each system.
image: https://distillsync.com/wp-content/uploads/2026/07/distillsync-destila-tus-procesos.png
layout: provider
modified: '2026-10-16'
name: Distillsync
nav: Providers
network: true
overview: 'Distillsync is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Integration, ERP, E-Commerce, and Automation.


  Distillsync''s developer surface includes documentation, pricing, signup flow, engineering blog, getting-started guide, and 9 more developer resources.'
plans:
- name: Distillsync Plans Pricing
  plan_count: 1
  slug: distillsync-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 23.3
  coverage:
    artifact_dirs: 8
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 55.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 55.4
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Distillsync Domain Security
  slug: distillsync-domain-security
  summary_line: TLSv1.3 · DMARC
slug: distillsync
tags:
- Company
- Integration
- ERP
- E-Commerce
- Automation
website: https://distillsync.com/
---

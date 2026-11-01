---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/solver/hosts/solver-hosts.yml
  title: ''
  type: Hosts
  url: hosts/solver-hosts.yml
- group: other
  href: https://artifacts.apis.io/solver/vendors/solver-vendors.yml
  title: ''
  type: Vendors
  url: vendors/solver-vendors.yml
- group: auth
  href: https://artifacts.apis.io/solver/security/solver-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/solver-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://solver.ai
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://solver.ai/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://solver.ai/terms-of-service
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://solver.ai
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Solver AI provides an AI‑powered marketing platform that automates content creation, campaign optimization, and multi‑channel publishing for e‑commerce merchants. The service generates on‑brand product copy, social posts, emails and ads, then optimizes campaigns across ad platforms, all from a single web and mobile app. It integrates with popular e‑commerce stores and social media, offering a continuous content‑to‑campaign workflow that saves merchants time and boosts conversion.
image: https://solver-website-g211znvif-solver-ai-team.vercel.app/hero.avif
layout: provider
modified: '2026-10-29'
name: Solver
nav: Providers
network: true
overview: Solver is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Marketing, E-commerce, and Automation.
random_paper: 19
score:
  band: minimal
  composite: 8.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 12.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Solver Domain Security
  slug: solver-domain-security
  summary_line: TLSv1.3 · HSTS
slug: solver
tags:
- Company
- AI
- Marketing
- E-commerce
- Automation
website: https://solver.ai
---

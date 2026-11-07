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
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/calmloop-in/plans/calmloop-in-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/calmloop-in-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/calmloop-in/hosts/calmloop-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/calmloop-in-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://calmloop.in/terms
- group: operate
  title: ''
  type: Support
  url: https://calmloop.in/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://calmloop.in/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://calmloop.in/pricing
- group: start
  title: ''
  type: Login
  url: https://calmloop.in/login
- group: auth
  href: https://artifacts.apis.io/calmloop-in/security/calmloop-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/calmloop-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://calmloop.in/
coverage:
  checked: '2026-11-04'
  detail: The provider's website offers product pages but no public API documentation or machine‑readable spec.
  evidence:
  - status: 200
    url: https://calmloop.in/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: CalmLoop is a calm task manager offering daily focus, a morning email summary, and MCP access for AI assistants. Built by Algoza Solutions OPC Private Limited, it emphasizes distraction‑free productivity, honest pricing with a free month trial, and clear data practices. The platform provides a simple interface for planning, focus zones, and task tracking without push notifications or hidden fees.
image: https://calmloop.in/calmloop-og.png
layout: provider
modified: '2026-11-04'
name: CalmLoop
nav: Providers
network: true
overview: 'CalmLoop is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Task Management, Productivity, Artificial Intelligence, and MCP.


  CalmLoop''s developer surface includes support, pricing, and 7 more developer resources.'
plans:
- name: Calmloop In Plans Pricing
  plan_count: 2
  slug: calmloop-in-plans-pricing
random_paper: 11
score:
  band: emerging
  composite: 13.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
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
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Calmloop In Domain Security
  slug: calmloop-in-domain-security
  summary_line: TLSv1.3 · DMARC
slug: calmloop-in
tags:
- Company
- Task Management
- Productivity
- Artificial Intelligence
- MCP
website: https://calmloop.in/
---

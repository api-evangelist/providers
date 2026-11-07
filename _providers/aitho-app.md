---
access_model:
  confidence: medium
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 21.2
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/aitho-app/plans/aitho-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/aitho-app-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/aitho-app/llms/aitho-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/aitho-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/aitho-app/well-known/aitho-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/aitho-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/aitho-app/hosts/aitho-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aitho-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/aitho-app/vendors/aitho-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aitho-app-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://aitho.app/press
- group: docs
  title: ''
  type: Documentation
  url: https://aitho.app/guides/
- group: auth
  href: https://artifacts.apis.io/aitho-app/security/aitho-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aitho-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://aitho.app/
- group: commercial
  title: ''
  type: Pricing
  url: https://aitho.app/pricing
- group: operate
  title: ''
  type: Support
  url: https://aitho.app/support
- group: start
  title: ''
  type: GettingStarted
  url: https://aitho.app/start
- group: auth
  title: ''
  type: Security
  url: https://aitho.app/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Aitho-app
coverage:
  checked: '2026-11-01'
  detail: Public website provides only presentation guides and no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://aitho.app/guides/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-01'
description: You know your material. The hard part is delivering it when the room is watching. Aitho keeps your words in front of you as you speak (a voice-following teleprompter), moves your slides with you, keeps your notes private, and gives you a grounded private answer when a question comes.
image: https://aitho.app/og.jpg
layout: provider
modified: '2026-11-01'
name: Aitho
nav: Providers
network: true
overview: 'Aitho is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Teleprompter, Presentation, Voice Control, and Productivity.


  Aitho''s developer surface includes documentation, pricing, support, getting-started guide, and 10 more developer resources.'
plans:
- name: Aitho App Plans Pricing
  plan_count: 3
  slug: aitho-app-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Aitho App Rate Limits
  slug: aitho-app-rate-limits
scopes:
- name: Aitho App Scopes
  scope_count: 0
  slug: aitho-app-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 16.7
  coverage:
    artifact_dirs: 21
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.7
  facets:
    access_clarity: 36.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 49.1
    operational_transparency: 7.9
  previous_composite: 21.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 20.0
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Aitho App Authentication
  slug: aitho-app-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Aitho App Domain Security
  slug: aitho-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aitho-app
tags:
- Artificial Intelligence
- Teleprompter
- Presentation
- Voice Control
- Productivity
website: https://aitho.app/
---

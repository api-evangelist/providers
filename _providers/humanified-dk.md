---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 5.8
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Humanified helps people and organisations understand the patterns that shape trust, energy, cooperation and decision quality.
  name: Humanified API
  slug: humanified-api
artifact_total: 5
common:
- group: agent
  href: https://artifacts.apis.io/humanified-dk/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: other
  href: https://artifacts.apis.io/humanified-dk/hosts/humanified-dk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/humanified-dk-hosts.yml
- group: other
  href: https://artifacts.apis.io/humanified-dk/vendors/humanified-dk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/humanified-dk-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.humanified.dk/
- group: auth
  href: https://artifacts.apis.io/humanified-dk/security/humanified-dk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/humanified-dk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://humanified.dk/
coverage:
  checked: '2026-10-29'
  detail: Docs at https://docs.humanified.dk/ provide only static HTML with no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://docs.humanified.dk/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Humanified is a consultancy and platform that helps people and organisations understand the patterns that shape trust, energy, cooperation and decision quality. By visualising human dynamics, they enable teams to identify friction, improve collaboration, and make better decisions. Their approach combines research, tools, and workshops to bring clarity to complex organisational systems, supporting both internal teams and external clients in navigating change.
layout: provider
modified: '2026-10-29'
name: humanified-dk
nav: Providers
network: true
overview: 'humanified-dk is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Trust, Energy, Cooperation, Decision-Making, and Analytics.


  humanified-dk''s developer surface includes documentation and 5 more developer resources.'
random_paper: 6
rate_limits:
- limit_count: 0
  name: Humanified Dk Rate Limits
  slug: humanified-dk-rate-limits
scopes:
- name: Humanified Dk Scopes
  scope_count: 0
  slug: humanified-dk-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 8.5
  coverage:
    artifact_dirs: 21
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.2
    discoverability: 53.6
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.4
  provenance:
    conformance: unknown
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Energy & Utilities
    regime_id: energy_utilities
    score: 18.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/humanified-dk/humanified-dk-2026-11-03T133528.png
security:
- kind: authentication
  name: Humanified Dk Authentication
  slug: humanified-dk-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Humanified Dk Domain Security
  slug: humanified-dk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: humanified-dk
tags:
- Trust
- Energy
- Cooperation
- Decision-Making
- Analytics
website: https://humanified.dk/
---

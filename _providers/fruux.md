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
api_count: 1
apis:
- description: fruux provides a developer portal at https://fruux.com/developers/ with documentation for integrating its synchronization service.
  name: fruux API
  slug: fruux-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/fruux/plans/fruux-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/fruux-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/fruux/hosts/fruux-hosts.yml
  title: ''
  type: Hosts
  url: hosts/fruux-hosts.yml
- group: build
  href: https://artifacts.apis.io/fruux/packages/fruux-packages.yml
  title: ''
  type: SDKs
  url: packages/fruux-packages.yml
- group: build
  href: https://artifacts.apis.io/fruux/packages/fruux-packages.yml
  title: ''
  type: Packages
  url: packages/fruux-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://fruux.com/terms-of-service/
- group: auth
  title: ''
  type: Security
  url: https://fruux.com/security/
- group: company
  title: ''
  type: Newsroom
  url: https://fruux.com/press/
- group: start
  title: ''
  type: Login
  url: https://fruux.com/account/login/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fruux
- group: auth
  href: https://artifacts.apis.io/fruux/security/fruux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/fruux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://fruux.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://fruux.com/developers/
- group: docs
  title: ''
  type: Documentation
  url: https://fruux.com/developers/
- group: docs
  title: ''
  type: APIReference
  url: https://fruux.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://fruux.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://fruux.com/privacy/
coverage:
  checked: '2026-10-27'
  detail: The developer portal provides HTML docs but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://fruux.com/developers/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: fruux provides a cloud‑based synchronization service that unifies contacts, calendars, tasks and notes across devices and platforms for individuals and teams. It offers secure, real‑time syncing, sharing, and collaboration features, supporting iOS, Android, macOS, Windows, and web clients. The service emphasizes privacy, data ownership, and easy integration with existing productivity tools.
layout: provider
modified: '2026-10-27'
name: fruux
nav: Providers
network: true
overview: 'fruux is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Sync, Contacts, Calendar, Task, and Collaboration.


  fruux''s developer surface includes documentation, API reference, pricing, and 13 more developer resources.'
plans:
- name: Fruux Plans Pricing
  plan_count: 3
  slug: fruux-plans-pricing
random_paper: 18
score:
  band: emerging
  composite: 20.5
  coverage:
    artifact_dirs: 11
    catalog_earned: 42.0
    catalog_earned_first_party: 12.0
    catalog_gap: 73.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.8
  facets:
    access_clarity: 53.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 20.2
    discoverability: 54.5
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 29.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/fruux/fruux-2026-11-03T132350.png
security:
- kind: domain-security
  name: Fruux Domain Security
  slug: fruux-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
slug: fruux
tags:
- Sync
- Contacts
- Calendar
- Task
- Collaboration
- Company
website: https://fruux.com/
---

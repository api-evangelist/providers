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
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://artifacts.apis.io/destro/plans/destro-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/destro-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/destro/conformance/destro-conformance.yml
  title: ''
  type: Conformance
  url: conformance/destro-conformance.yml
- group: agent
  href: https://artifacts.apis.io/destro/well-known/destro-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/destro-well-known.yml
- group: other
  href: https://artifacts.apis.io/destro/hosts/destro-hosts.yml
  title: ''
  type: Hosts
  url: hosts/destro-hosts.yml
- group: auth
  href: https://artifacts.apis.io/destro/security/destro-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/destro-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.destroai.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.destroai.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.destroai.com
- group: docs
  title: ''
  type: APIReference
  url: https://www.destroai.com
- group: company
  title: ''
  type: About
  url: https://www.destroai.com/about
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.destroai.com/privacy-policy/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.destroai.com/terms-and-conditions/terms-and-conditions
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://api.papermark.com/api/mcp
  - status: 401
    url: https://docs.destroai.com/api/mcp
  - status: 200
    url: https://destroai.com
  reason: partner-login
  state: gated
created: '2026-10-21'
description: Destro AI provides a shared intelligence layer for autonomous warehouse and factory operations, enabling fleets of robots to execute complex workflows with intuition. Backed by $8M seed funding, Destro combines on-body and omni-body intelligence to decide what, when, where, why, and how tasks are performed, offering a unified mind for physical agents across logistics and manufacturing environments.
image: https://framerusercontent.com/assets/Uzh1p8UJ7jM5E5W2cl146mFCb0.png
layout: provider
modified: '2026-10-21'
name: Destro
nav: Providers
network: true
overview: 'Destro is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Robotics, Automation, and Warehouse.


  Destro''s developer surface includes documentation, API reference, and 10 more developer resources.'
plans:
- name: Destro Plans Pricing
  plan_count: 4
  slug: destro-plans-pricing
random_paper: 9
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.3
  facets:
    access_clarity: 42.1
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 13.1
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 23.9
  provenance:
    conformance: first-party
    mcp: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 1
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/destro/destro-2026-11-03T130550.png
security:
- kind: domain-security
  name: Destro Domain Security
  slug: destro-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: destro
tags:
- Company
- Artificial Intelligence
- Robotics
- Automation
- Warehouse
website: https://www.destroai.com
---

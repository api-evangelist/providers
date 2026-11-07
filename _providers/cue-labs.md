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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 2.5
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: API for CUE Labs services as described in the documentation.
  name: Cue Labs API
  slug: cue-labs-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/cue-labs/hosts/cue-labs-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cue-labs-hosts.yml
- group: other
  href: https://artifacts.apis.io/cue-labs/vendors/cue-labs-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cue-labs-vendors.yml
- group: auth
  href: https://artifacts.apis.io/cue-labs/security/cue-labs-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cue-labs-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cue.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://cue.dev/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://cue.dev/docs/
- group: company
  title: ''
  type: Blog
  url: https://cue.dev/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cue-lang
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cue.dev/terms-of-service/central-registry/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cue.dev/privacy-policy/
coverage:
  checked: '2026-10-29'
  detail: Cue Labs provides documentation at https://cue.dev/docs/ but no machine‑readable API specification was found.
  evidence:
  - status: 404
    url: https://cue.dev/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: End Configuration-Related Outages CUE Hub stops misconfigurations from reaching production. It connects to your existing architecture to provide automated pre-deployment safety checks and impact analysis for every change. Book Demo Learn more Prevent costly outages Over 50% of major outages are due to misconfigurations, leading to billions of losses and reputational damage yearly. We build tried-and-tested solutions used by industry leaders to effectively prevent them.
image: https://cue.dev/img/cue-logo.svg
layout: provider
modified: '2026-10-28'
name: CUE Labs
nav: Providers
network: true
overview: 'CUE Labs is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Configuration, Automation, DevOps, and Infrastructure.


  CUE Labs'' developer surface includes documentation, getting-started guide, engineering blog, and 7 more developer resources.'
plans:
- name: Cue Labs Plans Pricing
  plan_count: 0
  slug: cue-labs-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 0
  name: Cue Labs Rate Limits
  slug: cue-labs-rate-limits
scopes:
- name: Cue Labs Scopes
  scope_count: 0
  slug: cue-labs-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 16.6
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cue-labs/cue-labs-2026-11-03T125749.png
security:
- kind: authentication
  name: Cue Labs Authentication
  slug: cue-labs-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Cue Labs Domain Security
  slug: cue-labs-domain-security
  summary_line: TLSv1.3 · HSTS
slug: cue-labs
tags:
- Company
- Configuration
- Automation
- DevOps
- Infrastructure
website: https://cue.dev/
---

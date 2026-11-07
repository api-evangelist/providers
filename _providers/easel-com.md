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
- description: The Easel API is currently on hiatus. We are not currently accepting early access applications.
  name: Easel API
  slug: easel-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/easel-com/hosts/easel-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/easel-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/easel-com/vendors/easel-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/easel-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/easel-com/security/easel-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/easel-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://easel.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.easel.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/inventables
- group: start
  title: ''
  type: Login
  url: https://easel.com/users/sign_in?tab=returning
- group: commercial
  title: ''
  type: TermsOfService
  url: https://easel.com/pages/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.easel.com/hc/en-us
coverage:
  checked: '2026-10-29'
  detail: The developer portal states the Easel API is on hiatus and no machine‑readable specification is provided.
  evidence:
  - status: 200
    url: https://developer.easel.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Easel is a web‑based CNC carving and design platform by Inventables, enabling makers to create, edit, and send 2D/3D projects to a CNC router directly from a browser. The service offers a library of designs, cloud‑based toolpaths, and integration with Easel Pro for advanced features, serving hobbyists, educators, and small‑business manufacturers. It provides RESTful APIs for project management, machine control, and user data, documented at developer.easel.com.
image: https://easel.com/cms/images/brand/easel-logo-white.png
layout: provider
modified: '2026-10-29'
name: Easel
nav: Providers
network: true
overview: 'Easel is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include CNC, Manufacturing, Design, Software, and Maker.


  Easel''s developer surface includes support and 8 more developer resources.'
plans:
- name: Easel Com Plans Pricing
  plan_count: 0
  slug: easel-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 0
  name: Easel Com Rate Limits
  slug: easel-com-rate-limits
scopes:
- name: Easel Com Scopes
  scope_count: 0
  slug: easel-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -4.5
  facets:
    access_clarity: 11.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 14.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 17.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/easel-com/easel-com-2026-11-03T131221.png
security:
- kind: authentication
  name: Easel Com Authentication
  slug: easel-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Easel Com Domain Security
  slug: easel-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: easel-com
tags:
- CNC
- Manufacturing
- Design
- Software
- Maker
website: https://easel.com
---

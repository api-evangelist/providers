---
access_model:
  confidence: low
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 5.4
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 5
common:
- group: auth
  href: https://artifacts.apis.io/homeboost/well-known/homeboost-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/homeboost-status-security.txt
- group: agent
  href: https://artifacts.apis.io/homeboost/llms/homeboost-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/homeboost-llms.txt
- group: agent
  href: https://artifacts.apis.io/homeboost/well-known/homeboost-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/homeboost-well-known.yml
- group: other
  href: https://artifacts.apis.io/homeboost/hosts/homeboost-hosts.yml
  title: ''
  type: Hosts
  url: hosts/homeboost-hosts.yml
- group: other
  href: https://artifacts.apis.io/homeboost/vendors/homeboost-vendors.yml
  title: ''
  type: Vendors
  url: vendors/homeboost-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.homeboost.com/
- group: auth
  href: https://artifacts.apis.io/homeboost/security/homeboost-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/homeboost-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://homeboost.com
- group: company
  title: ''
  type: Blog
  url: https://www.homeboost.com/blog
coverage:
  checked: '2026-10-29'
  detail: Docs page at https://www.homeboost.com/docs returns a JavaScript‑rendered SPA that blocks automated GET requests, preventing retrieval of a machine‑readable specification.
  evidence:
  - status: 200
    url: https://www.homeboost.com/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: HomeBoost is a startup focused on home energy optimization, offering a platform that helps homeowners monitor and improve energy efficiency. Backed by True Ventures, the company provides resources such as a blog with articles on energy audits, DIY upgrades, and smart thermostat guidance. Their website homeboost.com presents product information, pricing, and support resources.
image: https://content.homeboost.com/logos/logo_mark.svg
layout: provider
modified: '2026-10-29'
name: HomeBoost
nav: Providers
network: true
overview: 'HomeBoost is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Automation, Energy, IoT, and Startups.


  HomeBoost''s developer surface includes engineering blog and 8 more developer resources.'
plans:
- name: Homeboost Plans Pricing
  plan_count: 0
  slug: homeboost-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 0
  name: Homeboost Rate Limits
  slug: homeboost-rate-limits
scopes:
- name: Homeboost Scopes
  scope_count: 0
  slug: homeboost-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.3
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 1.2
    discoverability: 55.4
    operational_transparency: 18.4
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 10.3
  provenance:
    conformance: unknown
    mcp: derived
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
screenshot: https://apis.io/screenshots/homeboost/homeboost-2026-11-03T133433.png
security:
- kind: authentication
  name: Homeboost Authentication
  slug: homeboost-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Homeboost Domain Security
  slug: homeboost-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: homeboost
tags:
- Company
- Home Automation
- Energy
- IoT
- Startups
- TrueVentures
website: https://homeboost.com
---

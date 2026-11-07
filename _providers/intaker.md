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
api_count: 1
apis:
- description: Intaker offers an API for its intake platform, but no public machine‑readable contract or accessible documentation was found.
  name: Intaker API
  slug: intaker-api
artifact_total: 6
common:
- group: other
  href: https://artifacts.apis.io/intaker/vendors/intaker-vendors.yml
  title: ''
  type: Vendors
  url: vendors/intaker-vendors.yml
- group: other
  href: https://artifacts.apis.io/intaker/hosts/intaker-hosts.yml
  title: ''
  type: Hosts
  url: hosts/intaker-hosts.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://help.intaker.com/status
- group: start
  title: ''
  type: GettingStarted
  url: https://help.intaker.com/lesson/getting-started
- group: docs
  title: ''
  type: Documentation
  url: https://help.intaker.com/
- group: auth
  href: https://artifacts.apis.io/intaker/security/intaker-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/intaker-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://intaker.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://dashboard.intaker.com/
- group: company
  title: ''
  type: Blog
  url: https://intaker.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://intaker.com/contact/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://intaker.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://intaker.com/terms/
- group: commercial
  title: ''
  type: Pricing
  url: https://intaker.com/pricing/
- group: operate
  title: ''
  type: Roadmap
  url: https://intaker.com/roadmap/
- group: start
  title: ''
  type: SignUp
  url: https://dashboard.intaker.com/
coverage:
  checked: '2026-10-28'
  detail: Help Center pages require a password, preventing access to any machine‑readable API specification.
  evidence:
  - status: 200
    url: https://help.intaker.com/lesson/getting-started
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Intaker provides AI‑powered client intake software for law firms and local businesses, converting more leads with chat, texting, and automation so every inquiry is answered in seconds across every channel.
image: https://intaker.com/home/images/og-default.png
layout: provider
modified: '2026-10-28'
name: Intaker
nav: Providers
network: true
overview: 'Intaker is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Legal Tech, Law Firms, Automation, and Lead Generation.


  Intaker''s developer surface includes getting-started guide, documentation, engineering blog, support, pricing, signup flow, and 9 more developer resources.'
plans:
- name: Intaker Plans Pricing
  plan_count: 0
  slug: intaker-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Intaker Rate Limits
  slug: intaker-rate-limits
scopes:
- name: Intaker Scopes
  scope_count: 0
  slug: intaker-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 22
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.2
  facets:
    access_clarity: 22.4
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 57.1
    operational_transparency: 10.5
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 26.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/intaker/intaker-2026-11-03T133919.png
security:
- kind: authentication
  name: Intaker Authentication
  slug: intaker-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Intaker Domain Security
  slug: intaker-domain-security
  summary_line: TLSv1.3 · HSTS
slug: intaker
tags:
- Artificial Intelligence
- Legal Tech
- Law Firms
- Automation
- Lead Generation
- Company
website: https://intaker.com/
---

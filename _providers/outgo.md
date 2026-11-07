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
- group: other
  href: https://artifacts.apis.io/outgo/hosts/outgo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/outgo-hosts.yml
- group: other
  href: https://artifacts.apis.io/outgo/vendors/outgo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/outgo-vendors.yml
- group: auth
  href: https://artifacts.apis.io/outgo/security/outgo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/outgo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://outgo.dat.com/
- group: company
  title: ''
  type: Blog
  url: https://outgo.dat.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://outgo.dat.com/get-started/fleets
- group: start
  title: ''
  type: Login
  url: https://app.outgo.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://outgo.dat.com/legal/privacy
- group: operate
  title: ''
  type: Support
  url: https://outgo.dat.com/help
- group: commercial
  title: ''
  type: TermsOfService
  url: https://outgo.dat.com/legal/tpb-platform-agreement
coverage:
  checked: '2026-10-29'
  detail: Outgo's website provides no public developer documentation or machine‑readable API specification.
  evidence:
  - status: 200
    url: https://api.outgo.com/openapi.json
  reason: no-developer-program
  state: none
created: '2026-10-29'
description: Outgo provides freight factoring services, offering low rates, fast funding speeds, and a next‑generation financial platform that integrates banking, debit cards, and broker payments for the freight industry. It enables owner‑operators and fleets to get instant cash flow, automate invoicing, and access a suite of logistics‑focused financial tools.
image: https://cdn.prod.website-files.com/643470afef9fb377f6bac681/68257991d41770c4069c8445_Outgo_Banner_Copyright2025.png
layout: provider
modified: '2026-10-29'
name: Outgo
nav: Providers
network: true
overview: 'Outgo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Freight, Factoring, Fintech, and Payments.


  Outgo''s developer surface includes engineering blog, getting-started guide, support, and 7 more developer resources.'
plans:
- name: Outgo Plans Pricing
  plan_count: 0
  slug: outgo-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Outgo Rate Limits
  slug: outgo-rate-limits
scopes:
- name: Outgo Scopes
  scope_count: 0
  slug: outgo-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: minimal
  composite: 9.9
  coverage:
    artifact_dirs: 22
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.8
  facets:
    access_clarity: 17.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 15.7
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/outgo/outgo-2026-11-03T140827.png
security:
- kind: authentication
  name: Outgo Authentication
  slug: outgo-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Outgo Domain Security
  slug: outgo-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: outgo
tags:
- Company
- Freight
- Factoring
- Fintech
- Payments
- Logistics
website: https://outgo.dat.com/
---

---
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
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.1
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/meandu/plans/meandu-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/meandu-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/meandu/hosts/meandu-hosts.yml
  title: ''
  type: Hosts
  url: hosts/meandu-hosts.yml
- group: other
  href: https://artifacts.apis.io/meandu/vendors/meandu-vendors.yml
  title: ''
  type: Vendors
  url: vendors/meandu-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.meandu.com/velocity/terms
- group: operate
  title: ''
  type: Support
  url: https://help.meandu.com
- group: operate
  title: ''
  type: StatusPage
  url: https://status.meandu.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.meandu.com/legal/privacy-policy-uk
- group: commercial
  title: ''
  type: Pricing
  url: https://www.meandu.com/grow/pricing
- group: start
  title: ''
  type: Login
  url: https://www.meandu.com/sign-in
- group: company
  title: ''
  type: Blog
  url: https://www.meandu.com/blog
- group: docs
  title: ''
  type: Documentation
  url: https://help.meandu.com/
- group: auth
  href: https://artifacts.apis.io/meandu/security/meandu-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/meandu-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://meandu.com/
coverage:
  checked: '2026-10-27'
  detail: The public documentation at https://help.meandu.com/hc/en-us is readable but provides no machine‑readable API specification.
  evidence:
  - status: 200
    url: https://help.meandu.com/hc/en-us
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: me&u is a hospitality SaaS platform that enables venues to personalize the guest experience through integrated ordering, payment, multi‑vendor support, loyalty programs, and reservations. The solution combines AI‑driven recommendations, staff upsell tools, and analytics to help venues increase revenue and streamline operations across restaurants, bars, cafes, and hotels worldwide.
image: https://cdn.prod.website-files.com/68cb96140013fa535857f2bf/692d1368cfee03cc357a9a46_homeOG.jpg
layout: provider
modified: '2026-10-27'
name: me&u
nav: Providers
network: true
overview: 'me&u is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hospitality, SaaS, Payments, and Reservations.


  me&u''s developer surface includes support, pricing, engineering blog, documentation, and 9 more developer resources.'
plans:
- name: Meandu Plans Pricing
  plan_count: 1
  slug: meandu-plans-pricing
random_paper: 10
scopes:
- name: Meandu Scopes
  scope_count: 0
  slug: meandu-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.7
  coverage:
    artifact_dirs: 19
    catalog_earned: 35.0
    catalog_earned_first_party: 8.0
    catalog_gap: 80.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 21.4
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Meandu Authentication
  slug: meandu-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Meandu Domain Security
  slug: meandu-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: meandu
tags:
- Company
- Hospitality
- SaaS
- Payments
- Reservations
website: https://meandu.com/
---

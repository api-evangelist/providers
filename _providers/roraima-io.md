---
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
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 5
common:
- group: commercial
  href: https://artifacts.apis.io/roraima-io/plans/roraima-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/roraima-io-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/roraima-io/llms/roraima-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roraima-io-llms.txt
- group: agent
  href: https://artifacts.apis.io/roraima-io/well-known/roraima-io-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/roraima-io-well-known.yml
- group: other
  href: https://artifacts.apis.io/roraima-io/hosts/roraima-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roraima-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/roraima-io/vendors/roraima-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roraima-io-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://roraima.io/privacy-policy/
- group: auth
  href: https://artifacts.apis.io/roraima-io/security/roraima-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roraima-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://roraima.io/
- group: company
  title: ''
  type: Blog
  url: https://roraima.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://roraima.io/pricing-en/
- group: operate
  title: ''
  type: Support
  url: https://roraima.io/contacts/
coverage:
  checked: '2026-10-30'
  detail: The site provides booking services but offers no public developer program or API documentation.
  evidence:
  - status: 200
    url: https://roraima.io/
  reason: no-developer-program
  state: none
created: '2026-10-30'
description: Roraima provides commission-free direct bookings, synced calendars and self check‑in for B&Bs, holiday homes and hourly spaces. Hosts can create a free page, manage reservations, and integrate with popular channel managers, offering a seamless guest experience and increasing occupancy without third‑party fees.
image: https://roraima.io/design/themes/responsive/css/addons/iot_core/anteprime/roraima-v1.jpg
layout: provider
modified: '2026-10-30'
name: roraima-io
nav: Providers
network: true
overview: 'roraima-io is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Booking, Hospitality, SelfCheckIn, and SaaS.


  roraima-io''s developer surface includes engineering blog, pricing, support, and 8 more developer resources.'
plans:
- name: Roraima Io Plans Pricing
  plan_count: 3
  slug: roraima-io-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 0
  name: Roraima Io Rate Limits
  slug: roraima-io-rate-limits
scopes:
- name: Roraima Io Scopes
  scope_count: 0
  slug: roraima-io-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 18.3
  coverage:
    artifact_dirs: 20
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 25.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Roraima Io Authentication
  slug: roraima-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Roraima Io Domain Security
  slug: roraima-io-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: roraima-io
tags:
- Company
- Booking
- Hospitality
- SelfCheckIn
- SaaS
- DirectBookings
website: https://roraima.io/
---

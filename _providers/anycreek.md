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
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-04'
api_count: 0
artifact_total: 2
common:
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/anycreek/refs/heads/main/plans/anycreek-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anycreek-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anycreek/refs/heads/main/hosts/anycreek-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anycreek-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/anycreek/refs/heads/main/vendors/anycreek-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anycreek-vendors.yml
- group: commercial
  title: ''
  type: Pricing
  url: https://anycreek.com/pricing
- group: start
  title: ''
  type: Login
  url: https://anycreek.com/auth/sign-in
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/anycreek
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/anycreek/refs/heads/main/security/anycreek-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anycreek-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anycreek.com
- group: docs
  title: ''
  type: Documentation
  url: https://anycreek.com/about
- group: start
  title: ''
  type: DeveloperPortal
  url: https://explore.anycreek.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://anycreek.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://anycreek.com/terms
created: '2026-09-25'
description: AnyCreek provides an all‑in‑one operating system for modern outdoor businesses and guides. Founded in 2022, it streamlines calendar management, payments, marketing, and client information, empowering guides and outfitters to grow their businesses. The platform powers over a million hours of outdoor experiences worldwide, offering tools for bookings, payments, and business analytics.
layout: provider
modified: '2026-09-25'
name: AnyCreek
nav: Providers
network: true
overview: 'AnyCreek is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Calendar Management, Guide Assignments, Marketing, and SEO.


  AnyCreek''s developer surface includes pricing, documentation, and 10 more developer resources.'
plans:
- name: Anycreek Plans Pricing
  plan_count: 5
  slug: anycreek-plans-pricing
random_paper: 14
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 37.0
    catalog_earned_first_party: 12.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 19.0
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anycreek Domain Security
  slug: anycreek-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: anycreek
tags:
- Payments
- Calendar Management
- Guide Assignments
- Marketing
- SEO
- Outdoor Guides
- Outfitters
website: https://anycreek.com
---

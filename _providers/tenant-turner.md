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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Tenant Turner lead scheduling software and rental automation API (documentation gated behind login).
  name: Tenant Turner API
  slug: tenant-turner-api
artifact_total: 6
common:
- group: commercial
  href: https://artifacts.apis.io/tenant-turner/plans/tenant-turner-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tenant-turner-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/tenant-turner/changelog/tenant-turner-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/tenant-turner-changelog.yml
- group: auth
  href: https://artifacts.apis.io/tenant-turner/well-known/tenant-turner-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/tenant-turner-status-security.txt
- group: agent
  href: https://artifacts.apis.io/tenant-turner/well-known/tenant-turner-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/tenant-turner-well-known.yml
- group: other
  href: https://artifacts.apis.io/tenant-turner/hosts/tenant-turner-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tenant-turner-hosts.yml
- group: other
  href: https://artifacts.apis.io/tenant-turner/vendors/tenant-turner-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tenant-turner-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.tenantturner.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://tenantturner.com/release-notes/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TenantTurner
- group: auth
  href: https://artifacts.apis.io/tenant-turner/security/tenant-turner-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tenant-turner-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tenantturner.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.tenantturner.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://tenantturner.com/schedule-a-demo/
- group: operate
  title: ''
  type: Support
  url: https://help.tenantturner.com/
- group: company
  title: ''
  type: Blog
  url: https://tenantturner.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://tenantturner.com/plans-pricing/
- group: start
  title: ''
  type: SignUp
  url: https://app.tenantturner.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tenantturner.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tenantturner.com/privacy/
coverage:
  checked: '2026-10-28'
  detail: API documentation at https://api.tenantturner.com/docs redirects to an authentication flow requiring login.
  evidence:
  - status: 302
    url: https://api.tenantturner.com/docs
  reason: partner-login
  state: gated
created: '2026-10-28'
description: Tenant Turner provides AI‑enhanced leasing automation software for property managers, landlords, and leasing agencies. Its platform streamlines lead capture, scheduling, showings, and lease signing, integrating with major property‑management systems and thousands of apps via Zapier. The solution aims to reduce no‑shows, accelerate lease closures, and improve tenant experience through virtual agents and smart access features.
image: https://tenantturner.com/wp-content/uploads/2026/05/logo.png
layout: provider
modified: '2026-10-28'
name: Tenant Turner
nav: Providers
network: true
overview: 'Tenant Turner is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Leasing, Property-Management, Automation, AI, and SaaS.


  Tenant Turner''s developer surface includes changelog, documentation, getting-started guide, support, engineering blog, pricing, signup flow, and 12 more developer resources.'
plans:
- name: Tenant Turner Plans Pricing
  plan_count: 2
  slug: tenant-turner-plans-pricing
random_paper: 23
rate_limits:
- limit_count: 0
  name: Tenant Turner Rate Limits
  slug: tenant-turner-rate-limits
scopes:
- name: Tenant Turner Scopes
  scope_count: 0
  slug: tenant-turner-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 20
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 47.4
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 27.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Tenant Turner Authentication
  slug: tenant-turner-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Tenant Turner Domain Security
  slug: tenant-turner-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: tenant-turner
tags:
- Leasing
- Property-Management
- Automation
- AI
- SaaS
website: https://tenantturner.com/
---

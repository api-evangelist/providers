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
api_count: 1
apis:
- description: Flat‑rate pricing platform API (no public machine‑readable specification found).
  name: The New Flat Rate API
  slug: the-new-flat-rate-api
artifact_total: 4
common:
- group: commercial
  href: https://artifacts.apis.io/the-new-flat-rate/plans/the-new-flat-rate-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/the-new-flat-rate-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/the-new-flat-rate/hosts/the-new-flat-rate-hosts.yml
  title: ''
  type: Hosts
  url: hosts/the-new-flat-rate-hosts.yml
- group: other
  href: https://artifacts.apis.io/the-new-flat-rate/vendors/the-new-flat-rate-vendors.yml
  title: ''
  type: Vendors
  url: vendors/the-new-flat-rate-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://thenewflatrate.com/press
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TheNewFlatRate
- group: auth
  href: https://artifacts.apis.io/the-new-flat-rate/security/the-new-flat-rate-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/the-new-flat-rate-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://thenewflatrate.com/
- group: docs
  title: ''
  type: Documentation
  url: https://thenewflatrate.com/about-us
- group: operate
  title: ''
  type: Support
  url: https://thenewflatrate.com/help-desk
- group: company
  title: ''
  type: Blog
  url: https://thenewflatrate.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://thenewflatrate.com/contractor-pricing-plans
- group: commercial
  title: ''
  type: TermsOfService
  url: https://thenewflatrate.com/member-user-agreement
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://thenewflatrate.com/privacy-policy
coverage:
  checked: '2026-10-28'
  detail: The provider's website offers documentation but no machine‑readable OpenAPI, AsyncAPI, GraphQL, gRPC or WSDL files were found.
  evidence:
  - status: 200
    url: https://thenewflatrate.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: The New Flat Rate provides flat‑rate pricing software with built‑in menu options for HVAC, plumbing, electrical and chimney contractors. Its platform lets technicians present five service options on each job, enabling customers to choose the level of service while businesses increase ticket value and reduce pricing guesswork. The solution includes training, coaching and a suite of resources to help contractors grow profitably and streamline operations.
layout: provider
modified: '2026-10-28'
name: The New Flat Rate
nav: Providers
network: true
overview: 'The New Flat Rate is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pricing, Software, Contractors, and HVAC.


  The New Flat Rate''s developer surface includes documentation, support, engineering blog, pricing, and 9 more developer resources.'
plans:
- name: The New Flat Rate Plans Pricing
  plan_count: 1
  slug: the-new-flat-rate-plans-pricing
- name: The New Flat Rate Plans
  plan_count: 0
  slug: the-new-flat-rate-plans
random_paper: 5
score:
  band: emerging
  composite: 19.9
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 8.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 55.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: The New Flat Rate Domain Security
  slug: the-new-flat-rate-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: the-new-flat-rate
tags:
- Company
- Pricing
- Software
- Contractors
- HVAC
website: https://thenewflatrate.com/
---

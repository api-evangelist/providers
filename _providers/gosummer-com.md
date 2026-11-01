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
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: agent
  href: https://artifacts.apis.io/gosummer-com/well-known/gosummer-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gosummer-com-well-known.yml
- group: commercial
  href: https://artifacts.apis.io/gosummer-com/plans/gosummer-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/gosummer-com-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/gosummer-com/hosts/gosummer-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gosummer-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/gosummer-com/vendors/gosummer-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/gosummer-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.summeros.com/legal/terms-of-use
- group: start
  title: ''
  type: SignUp
  url: https://login.summeros.com/sign-up
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.summeros.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.summeros.com/pricing
- group: auth
  href: https://artifacts.apis.io/gosummer-com/security/gosummer-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gosummer-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.summeros.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: http://www.gosummer.com
  reason: no-developer-program
  state: none
created: '2026-10-23'
description: Summer OS provides an AI‑driven asset intelligence platform for short‑term rental teams, offering professional‑grade revenue forecasting, market intelligence, and performance analytics. The service is aimed at independent owners, investors and underwriters, and property managers who need real‑time insights to optimize pricing and revenue. Summer OS is now part of The Lifetime Value Co.
image: https://www.summeros.com/og-image.png
layout: provider
modified: '2026-10-23'
name: Summer 2
nav: Providers
network: true
overview: 'Summer 2 is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Short‑Term Rentals, Asset Intelligence, Revenue Forecasting, Market Intelligence, and Property Management.


  Summer 2''s developer surface includes signup flow, pricing, and 8 more developer resources.'
plans:
- name: Gosummer Com Plans Pricing
  plan_count: 4
  slug: gosummer-com-plans-pricing
random_paper: 19
score:
  band: emerging
  composite: 20.8
  coverage:
    artifact_dirs: 10
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Gosummer Com Domain Security
  slug: gosummer-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: gosummer-com
tags:
- Short‑Term Rentals
- Asset Intelligence
- Revenue Forecasting
- Market Intelligence
- Property Management
website: https://www.summeros.com
---

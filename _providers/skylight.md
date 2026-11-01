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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: docs
  title: ''
  type: Documentation
  url: https://docs.skylight.io/
- group: commercial
  href: https://artifacts.apis.io/skylight/plans/skylight-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/skylight-plans-pricing.yml
- group: auth
  href: https://artifacts.apis.io/skylight/well-known/skylight-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/skylight-status-security.txt
- group: agent
  href: https://artifacts.apis.io/skylight/well-known/skylight-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/skylight-well-known.yml
- group: other
  href: https://artifacts.apis.io/skylight/hosts/skylight-hosts.yml
  title: ''
  type: Hosts
  url: hosts/skylight-hosts.yml
- group: build
  href: https://artifacts.apis.io/skylight/packages/skylight-packages.yml
  title: ''
  type: SDKs
  url: packages/skylight-packages.yml
- group: build
  href: https://artifacts.apis.io/skylight/packages/skylight-packages.yml
  title: ''
  type: Packages
  url: packages/skylight-packages.yml
- group: auth
  href: https://artifacts.apis.io/skylight/security/skylight-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/skylight-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.skylight.io/
- group: company
  title: ''
  type: Blog
  url: https://blog.skylight.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.skylight.io/pricing
- group: operate
  title: ''
  type: Support
  url: https://www.skylight.io/support
- group: start
  title: ''
  type: SignUp
  url: https://www.skylight.io/signup
- group: start
  title: ''
  type: Login
  url: https://www.skylight.io/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.skylight.io/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.skylight.io/privacy
- group: operate
  title: ''
  type: StatusPage
  url: http://status.skylight.io
- group: operate
  title: ''
  type: Contact
  url: https://www.skylight.io/contact
coverage:
  checked: '2026-10-27'
  detail: Documentation pages are served as JavaScript shells requiring a browser to render.
  evidence:
  - status: 200
    url: https://www.skylight.io/docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-27'
description: Skylight provides a smart profiling platform for Ruby and Rails applications, turning performance data into actionable insights. It helps developers identify bottlenecks, understand slowdowns, and improve application speed through detailed tracing and analytics. The service offers a free tier with 100,000 traces per month and paid plans starting at $20, catering to teams of all sizes.
layout: provider
modified: '2026-10-27'
name: Skylight
nav: Providers
network: true
overview: 'Skylight is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Performance, Ruby, Rails, Monitoring, and Profiling.


  Skylight''s developer surface includes documentation, engineering blog, pricing, support, signup flow, and 13 more developer resources.'
plans:
- name: Skylight Plans Pricing
  plan_count: 2
  slug: skylight-plans-pricing
random_paper: 15
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 9
    catalog_earned: 33.0
    catalog_earned_first_party: 8.0
    catalog_gap: 82.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 44.6
    operational_transparency: 26.3
  provenance:
    mcp: derived
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
  name: Skylight Domain Security
  slug: skylight-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: skylight
tags:
- Performance
- Ruby
- Rails
- Monitoring
- Profiling
- Company
website: https://www.skylight.io/
---

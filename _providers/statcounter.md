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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: StatCounter API provides web analytics data via a paid API. Documentation is at https://statcounter.com/api/docs/v3/.
  name: StatCounter API
  slug: statcounter-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/statcounter/plans/statcounter-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/statcounter-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/statcounter/well-known/statcounter-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/statcounter-well-known.yml
- group: other
  href: https://artifacts.apis.io/statcounter/hosts/statcounter-hosts.yml
  title: ''
  type: Hosts
  url: hosts/statcounter-hosts.yml
- group: other
  href: https://artifacts.apis.io/statcounter/vendors/statcounter-vendors.yml
  title: ''
  type: Vendors
  url: vendors/statcounter-vendors.yml
- group: build
  href: https://artifacts.apis.io/statcounter/packages/statcounter-packages.yml
  title: ''
  type: SDKs
  url: packages/statcounter-packages.yml
- group: build
  href: https://artifacts.apis.io/statcounter/packages/statcounter-packages.yml
  title: ''
  type: Packages
  url: packages/statcounter-packages.yml
- group: auth
  href: https://artifacts.apis.io/statcounter/security/statcounter-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/statcounter-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://statcounter.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://statcounter.com/
- group: docs
  title: ''
  type: Documentation
  url: https://statcounter.com/api/docs/v3/
- group: docs
  title: ''
  type: APIReference
  url: https://statcounter.com/api/docs/v3/
- group: commercial
  title: ''
  type: Pricing
  url: https://statcounter.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://statcounter.com/blogger/
- group: operate
  title: ''
  type: Support
  url: https://statcounter.com/support/faq/
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 403
    url: https://statcounter.com/mcp
  - status: 401
    url: https://api.statcounter.com/mcp
  - status: 200
    url: https://statcounter.com/
  reason: partner-login
  state: gated
created: '2026-10-27'
description: StatCounter provides web analytics services that help website owners track visitor behavior, traffic sources, and engagement in real time. Their platform offers features such as heatmaps, session replay, click fraud detection, and detailed reporting, catering to both small sites and enterprise customers. With a focus on ease of use, StatCounter delivers actionable insights without requiring extensive setup, supporting integration via a paid API for developers to build custom reports and applications.
image: https://www.statcounter.com/images/og_image.png
layout: provider
modified: '2026-10-27'
name: StatCounter
nav: Providers
network: true
overview: 'StatCounter is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Analytics, Web, Real-time, and Heatmaps.


  StatCounter''s developer surface includes documentation, API reference, pricing, engineering blog, support, and 9 more developer resources.'
plans:
- name: Statcounter Plans Pricing
  plan_count: 6
  slug: statcounter-plans-pricing
random_paper: 12
score:
  band: emerging
  composite: 21.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 42.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 11.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Statcounter Domain Security
  slug: statcounter-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: statcounter
tags:
- Company
- Analytics
- Web
- Real-time
- Heatmaps
website: https://statcounter.com/
---

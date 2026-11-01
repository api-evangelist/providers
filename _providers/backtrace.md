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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 18.0
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Backtrace provides error monitoring and crash reporting APIs for developers.
  name: Backtrace API
  slug: backtrace-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/backtrace/plans/backtrace-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/backtrace-plans-pricing.yml
- group: agent
  href: https://artifacts.apis.io/backtrace/well-known/backtrace-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/backtrace-well-known.yml
- group: other
  href: https://artifacts.apis.io/backtrace/hosts/backtrace-hosts.yml
  title: ''
  type: Hosts
  url: hosts/backtrace-hosts.yml
- group: other
  href: https://artifacts.apis.io/backtrace/vendors/backtrace-vendors.yml
  title: ''
  type: Vendors
  url: vendors/backtrace-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://backtrace.io/terms-of-service
- group: operate
  title: ''
  type: Support
  url: https://support.backtrace.io/s/?language=en_US
- group: commercial
  title: ''
  type: Pricing
  url: https://backtrace.io/pricing
- group: start
  title: ''
  type: Login
  url: https://backtrace.io/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/backtrace-labs
- group: company
  title: ''
  type: Blog
  url: https://backtrace.io/blog
- group: auth
  href: https://artifacts.apis.io/backtrace/security/backtrace-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/backtrace-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://backtrace.io/
created: '2026-10-29'
description: Backtrace provides crash and error reporting solutions for video games, embedded technologies, desktop and mobile software, and SaaS markets. It offers application monitoring, crash analytics, and debugging tools to help developers identify, prioritize, and fix issues quickly, improving software stability and user experience across platforms.
image: https://images.prismic.io/backtrace/64276b0f-3f14-4676-8d97-bfde05e3ef0e_og-image.jpg?auto=compress,format
layout: provider
modified: '2026-10-29'
name: Backtrace
nav: Providers
network: true
overview: 'Backtrace is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CrashReporting, Monitoring, DeveloperTools, and Gaming.


  Backtrace''s developer surface includes support, pricing, engineering blog, and 9 more developer resources.'
plans:
- name: Backtrace Plans Pricing
  plan_count: 5
  slug: backtrace-plans-pricing
random_paper: 16
score:
  band: emerging
  composite: 21.1
  coverage:
    artifact_dirs: 7
    catalog_earned: 44.0
    catalog_earned_first_party: 12.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Backtrace Domain Security
  slug: backtrace-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: backtrace
tags:
- Company
- CrashReporting
- Monitoring
- DeveloperTools
- Gaming
website: https://backtrace.io/
---

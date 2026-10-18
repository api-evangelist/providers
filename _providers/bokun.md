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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-17'
api_count: 1
apis:
- description: Bokun provides a GraphQL API for booking management and related operations.
  name: Bokun GraphQL API
  slug: bokun-graphql-api
artifact_total: 3
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/well-known/bokun-bokun-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/bokun-bokun-security.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/plans/bokun-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bokun-plans-pricing.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/well-known/bokun-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bokun-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/hosts/bokun-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bokun-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/vendors/bokun-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bokun-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/packages/bokun-packages.yml
  title: ''
  type: SDKs
  url: packages/bokun-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/packages/bokun-packages.yml
  title: ''
  type: Packages
  url: packages/bokun-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bokun.io/terms
- group: operate
  title: ''
  type: StatusPage
  url: https://bokun.statuspage.io/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bokun.io/privacy-policy
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.bokun.io/changelog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Bokun
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bokun/refs/heads/main/security/bokun-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bokun-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bokun.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.bokun.io/
- group: company
  title: ''
  type: Blog
  url: https://www.bokun.io/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bokun.io/pricing
- group: start
  title: ''
  type: SignUp
  url: https://new.bokun.io/app/signup
- group: operate
  title: ''
  type: Support
  url: https://docs.bokun.io/docs/bokun-help-center
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.bokun.io/api/graphql
  - status: null
    url: https://new.bokun.io/api/graphql
  - status: null
    url: https://extranet.bokun.io/api/graphql
  - status: 401
    url: https://api.bokun.io/mcp
  - status: 401
    url: https://new.bokun.io/mcp
  - status: 401
    url: https://extranet.bokun.io/mcp
  reason: partner-login
  state: gated
created: '2026-10-12'
description: Bokun provides a comprehensive booking management platform for tour and activity providers, enabling them to manage availability, resources, customer communications, and sales across multiple channels. The SaaS solution integrates with partners, offers pricing tools, and supports both online and in‑person bookings, helping businesses streamline operations and increase revenue.
image: https://www.bokun.io/wp-content/uploads/2024/06/Bokun-homepage-screenshot.png
layout: provider
modified: '2026-10-12'
name: Bokun
nav: Providers
network: true
overview: 'Bokun is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Travel, Software-as-a-Service, Booking, and Tour.


  Bokun''s developer surface includes changelog, documentation, engineering blog, pricing, signup flow, support, and 13 more developer resources.'
plans:
- name: Bokun Plans Pricing
  plan_count: 4
  slug: bokun-plans-pricing
random_paper: 15
score:
  band: thin
  composite: 32.1
  coverage:
    artifact_dirs: 9
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 76.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 66.1
    operational_transparency: 36.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bokun Domain Security
  slug: bokun-domain-security
  summary_line: TLSv1.3 · DMARC
slug: bokun
tags:
- Company
- Travel
- Software-as-a-Service
- Booking
- Tour
website: https://www.bokun.io/
---

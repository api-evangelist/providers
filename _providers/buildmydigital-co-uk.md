---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Free website scan for UK local businesses, usable by people and agents.
  name: Build My Digital API
  slug: build-my-digital-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/buildmydigital-co-uk/plans/buildmydigital-co-uk-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/buildmydigital-co-uk-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/buildmydigital-co-uk/conformance/buildmydigital-co-uk-conformance.yml
  title: ''
  type: Conformance
  url: conformance/buildmydigital-co-uk-conformance.yml
- group: agent
  href: https://artifacts.apis.io/buildmydigital-co-uk/llms/buildmydigital-co-uk-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/buildmydigital-co-uk-llms.txt
- group: agent
  href: https://artifacts.apis.io/buildmydigital-co-uk/well-known/buildmydigital-co-uk-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/buildmydigital-co-uk-well-known.yml
- group: other
  href: https://artifacts.apis.io/buildmydigital-co-uk/hosts/buildmydigital-co-uk-hosts.yml
  title: ''
  type: Hosts
  url: hosts/buildmydigital-co-uk-hosts.yml
- group: other
  href: https://artifacts.apis.io/buildmydigital-co-uk/vendors/buildmydigital-co-uk-vendors.yml
  title: ''
  type: Vendors
  url: vendors/buildmydigital-co-uk-vendors.yml
- group: build
  href: https://artifacts.apis.io/buildmydigital-co-uk/packages/buildmydigital-co-uk-packages.yml
  title: ''
  type: SDKs
  url: packages/buildmydigital-co-uk-packages.yml
- group: build
  href: https://artifacts.apis.io/buildmydigital-co-uk/packages/buildmydigital-co-uk-packages.yml
  title: ''
  type: Packages
  url: packages/buildmydigital-co-uk-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://buildmydigital.co.uk/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://buildmydigital.co.uk/privacy/
- group: company
  title: ''
  type: Blog
  url: https://buildmydigital.co.uk/blog/
- group: start
  title: ''
  type: GettingStarted
  url: https://buildmydigital.co.uk/google-ads-setup/
- group: docs
  title: ''
  type: APIReference
  url: https://buildmydigital.co.uk/developers/
- group: auth
  href: https://artifacts.apis.io/buildmydigital-co-uk/security/buildmydigital-co-uk-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/buildmydigital-co-uk-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://buildmydigital.co.uk/
- group: commercial
  title: ''
  type: Pricing
  url: https://buildmydigital.co.uk/pricing/
created: '2026-11-03'
description: Build My Digital provides hand‑coded websites for local home‑improvement firms and private clinics, offering a pay‑per‑booking model where they are only paid when bookings come in. They manage Google ads, business profiles, missed‑call handling, quote chasing and review requests, ensuring high‑ticket jobs are booked efficiently.
image: https://buildmydigital.co.uk/opengraph-image.png?opengraph-image.1_dgzuuqemh84.png
layout: provider
modified: '2026-11-03'
name: Build My Digital
nav: Providers
network: true
overview: 'Build My Digital is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Home Improvement, Clinics, PayPerBooking, and Digital Marketing.


  Build My Digital''s developer surface includes engineering blog, getting-started guide, API reference, pricing, and 12 more developer resources.'
plans:
- name: Buildmydigital Co Uk Plans Pricing
  plan_count: 10
  slug: buildmydigital-co-uk-plans-pricing
random_paper: 0
score:
  band: emerging
  composite: 20.2
  coverage:
    artifact_dirs: 12
    catalog_earned: 49.0
    catalog_earned_first_party: 12.0
    catalog_gap: 66.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 47.4
    contract_governance: 4.5
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    conformance: derived
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Buildmydigital Co Uk Domain Security
  slug: buildmydigital-co-uk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: buildmydigital-co-uk
tags:
- Company
- Home Improvement
- Clinics
- PayPerBooking
- Digital Marketing
website: https://buildmydigital.co.uk/
---

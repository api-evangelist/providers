---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 27.3
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Autumn provides an open-source billing API built on top of Stripe, offering usage‑based billing, credits, entitlements, and subscription management.
  name: Autumn Billing API
  slug: autumn-billing-api
artifact_total: 2
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.useautumn.com/documentation/getting-started/migration
- group: agent
  href: https://artifacts.apis.io/autumn/llms/autumn-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autumn-llms.txt
- group: other
  href: https://artifacts.apis.io/autumn/a2a/autumn-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/autumn-a2a.yml
- group: auth
  href: https://artifacts.apis.io/autumn/well-known/autumn-vercel-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/autumn-vercel-security.txt
- group: agent
  href: https://artifacts.apis.io/autumn/well-known/autumn-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/autumn-well-known.yml
- group: other
  href: https://artifacts.apis.io/autumn/hosts/autumn-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autumn-hosts.yml
- group: other
  href: https://artifacts.apis.io/autumn/vendors/autumn-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autumn-vendors.yml
- group: build
  href: https://artifacts.apis.io/autumn/packages/autumn-packages.yml
  title: ''
  type: SDKs
  url: packages/autumn-packages.yml
- group: build
  href: https://artifacts.apis.io/autumn/packages/autumn-packages.yml
  title: ''
  type: Packages
  url: packages/autumn-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.useautumn.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://useautumn.com/privacy
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.useautumn.com/changelog/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.useautumn.com`
- group: auth
  href: https://artifacts.apis.io/autumn/security/autumn-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autumn-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://useautumn.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.useautumn.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.useautumn.com/api-reference
- group: company
  title: ''
  type: Blog
  url: https://useautumn.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/useautumn
- group: commercial
  title: ''
  type: Pricing
  url: https://useautumn.com/pricing
coverage:
  checked: '2026-10-26'
  detail: OpenAPI spec at https://api.useautumn.com/openapi.json requires authentication, returning 401.
  evidence:
  - status: 401
    url: https://api.useautumn.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-10-26'
description: Autumn provides an open-source billing infrastructure built on top of Stripe, offering usage‑based billing, credits, entitlements, and subscription state through a simple API. It serves AI startups and other SaaS companies needing a unified system of record for subscriptions, metering, and feature access, while delegating payment processing to Stripe. The platform includes endpoints such as attach, check, and track, and is documented with quickstart guides and API references.
image: https://useautumn.com/images/og-image.png
layout: provider
modified: '2026-10-26'
name: Autumn (autumn-js, billing)
nav: Providers
network: true
overview: 'Autumn (autumn-js, billing) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Billing, Open-Source, Stripe, and AI-Startups.


  Autumn (autumn-js, billing)''s developer surface includes getting-started guide, changelog, documentation, API reference, engineering blog, pricing, and 14 more developer resources.'
random_paper: 18
score:
  band: thin
  composite: 26.6
  coverage:
    artifact_dirs: 8
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 47.6
    discoverability: 66.1
    operational_transparency: 47.4
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
  name: Autumn Domain Security
  slug: autumn-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: autumn
tags:
- Company
- Billing
- Open-Source
- Stripe
- AI-Startups
website: https://useautumn.com/
---

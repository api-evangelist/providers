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
api_count: 1
apis:
- description: Safer, simpler global payments for marketplaces, platforms and banks — compliant by design.
  name: LiquidTrust API
  slug: liquidtrust-api
artifact_total: 3
common:
- group: commercial
  href: https://artifacts.apis.io/goliquid-io/plans/goliquid-io-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/goliquid-io-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/goliquid-io/changelog/goliquid-io-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/goliquid-io-changelog.yml
- group: design
  href: https://artifacts.apis.io/goliquid-io/conformance/goliquid-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/goliquid-io-conformance.yml
- group: other
  href: https://artifacts.apis.io/goliquid-io/hosts/goliquid-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/goliquid-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/goliquid-io/vendors/goliquid-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/goliquid-io-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.liquidtrust.io/terms-of-service
- group: auth
  title: ''
  type: Security
  url: https://www.liquidtrust.io/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.liquidtrust.io/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.liquidtrust.io/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://www.liquidtrust.io/press
- group: start
  title: ''
  type: Login
  url: https://www.liquidtrust.io/login
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.liquidtrust.io/release-notes
- group: company
  title: ''
  type: Blog
  url: https://www.liquidtrust.io/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://liquidtrust.io/blog/hidden-cost-of-poor-onboarding
- group: auth
  href: https://artifacts.apis.io/goliquid-io/security/goliquid-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/goliquid-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://goliquid.io/
created: '2026-10-24'
description: LiquidTrust provides Micro Escrow® solutions that enable platforms to hold and release funds based on predefined conditions. It serves marketplaces, banks, and other platform partners that need compliant, global payment flows with built‑in KYC, AML and dispute reduction. The service is offered as a hosted, white‑label, or API integration with a single 1% fee covering trust, compliance, and payouts.
image: https://liquidtrust.io/lt-social-card.png
layout: provider
modified: '2026-10-24'
name: Liquid
nav: Providers
network: true
overview: 'Liquid is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, Escrow, Marketplace, Platform, and Compliance.


  Liquid''s developer surface includes changelog, pricing, engineering blog, getting-started guide, and 12 more developer resources.'
plans:
- name: Goliquid Io Plans Pricing
  plan_count: 2
  slug: goliquid-io-plans-pricing
random_paper: 19
score:
  band: thin
  composite: 28.2
  coverage:
    artifact_dirs: 8
    catalog_earned: 40.0
    catalog_earned_first_party: 8.0
    catalog_gap: 75.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 58.9
    operational_transparency: 26.3
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 24.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Goliquid Io Domain Security
  slug: goliquid-io-domain-security
  summary_line: TLSv1.3 · DMARC
slug: goliquid-io
tags:
- Payments
- Escrow
- Marketplace
- Platform
- Compliance
- Global Payments
website: https://goliquid.io/
---

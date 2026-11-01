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
- description: Integration API for synchronizing Stripe data with QuickBooks as described in the help documentation.
  name: Sush API
  slug: sush-api
artifact_total: 3
common:
- group: other
  href: https://artifacts.apis.io/sush/hosts/sush-hosts.yml
  title: ''
  type: Hosts
  url: hosts/sush-hosts.yml
- group: other
  href: https://artifacts.apis.io/sush/vendors/sush-vendors.yml
  title: ''
  type: Vendors
  url: vendors/sush-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://sush.io/security
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sush.io/article/62-i-made-a-mistake-during-setup-of-the-automation-can-i-edit-or-change-my-settings
- group: auth
  href: https://artifacts.apis.io/sush/security/sush-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/sush-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/sush/security/sush-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/sush-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://sush.io/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sush.io/
- group: company
  title: ''
  type: Blog
  url: https://sush.io/blog
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://sush.io/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://sush.io/terms
coverage:
  checked: '2026-10-21'
  detail: Help documentation provides guides but no OpenAPI or other machine-readable contract was found.
  evidence:
  - status: 0
    url: https://help.sush.io/swagger.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-21'
description: Sush.io provides a seamless integration platform that synchronizes Stripe transaction data with QuickBooks accounting software. By automating the transfer of payouts, fees, refunds, taxes, and class tracking, it eliminates manual bookkeeping, reduces errors, and saves businesses time and money. The service offers a flat monthly pricing model with unlimited transactions, supporting additional integrations like Etsy and Braintree, and is an official Intuit App Partner listed on the QuickBooks App Store since 2014.
image: https://sush.io/og-image.png
layout: provider
modified: '2026-10-21'
name: Sush.io
nav: Providers
network: true
overview: 'Sush.io is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Finance, Accounting, Integration, Software-as-a-Service, and Automation.


  Sush.io''s developer surface includes getting-started guide, documentation, engineering blog, and 8 more developer resources.'
random_paper: 19
score:
  band: emerging
  composite: 15.8
  coverage:
    artifact_dirs: 6
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 23.8
    discoverability: 57.1
    operational_transparency: 10.5
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 17.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Sush Domain Security
  slug: sush-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sush Vulnerability Disclosure
  slug: sush-vulnerability-disclosure
  summary_line: no policy recorded
slug: sush
tags:
- Finance
- Accounting
- Integration
- Software-as-a-Service
- Automation
- Payments
website: https://sush.io/
---

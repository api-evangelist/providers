---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 10.8
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://bugbounty.zohocorp.com/bb/info
- group: agent
  href: https://artifacts.apis.io/zoho-payments/llms/zoho-payments-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zoho-payments-llms.txt
- group: auth
  href: https://artifacts.apis.io/zoho-payments/well-known/zoho-payments-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/zoho-payments-security.txt
- group: agent
  href: https://artifacts.apis.io/zoho-payments/well-known/zoho-payments-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zoho-payments-well-known.yml
- group: other
  href: https://artifacts.apis.io/zoho-payments/hosts/zoho-payments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zoho-payments-hosts.yml
- group: other
  href: https://artifacts.apis.io/zoho-payments/vendors/zoho-payments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zoho-payments-vendors.yml
- group: build
  href: https://artifacts.apis.io/zoho-payments/packages/zoho-payments-packages.yml
  title: ''
  type: SDKs
  url: packages/zoho-payments-packages.yml
- group: build
  href: https://artifacts.apis.io/zoho-payments/packages/zoho-payments-packages.yml
  title: ''
  type: Packages
  url: packages/zoho-payments-packages.yml
- group: start
  title: ''
  type: SignUp
  url: https://www.zoho.com/us/payments/signup/
- group: build
  title: ''
  type: Postman
  url: https://god.gw.postman.com/run-collection/48166576-fde9a00c-3320-4bfd-9105-0ab5f8be92a2
- group: auth
  href: https://artifacts.apis.io/zoho-payments/security/zoho-payments-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-payments-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/zoho-payments/security/zoho-payments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zoho-payments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/us/payments/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.zoho.com/us/payments/developerdocs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/us/payments/developerdocs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.zoho.com/us/payments/api/v1/introduction/
- group: operate
  title: ''
  type: Support
  url: https://www.zoho.com/us/payments/help/
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/blog/payments/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.zoho.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.zoho.com/privacy.html
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/us/payments/pricing/
created: '2026-10-26'
description: Zoho Payments provides a suite of online payment solutions, enabling businesses to accept payments via payment links, embedded checkout, subscriptions, and online stores. It offers APIs for creating payment links, processing transactions, managing subscriptions, and handling webhooks, with detailed developer documentation and SDKs across multiple languages.
image: https://www.zoho.com/payments/images/link-preview.png
layout: provider
modified: '2026-10-26'
name: Zoho Payments
nav: Providers
network: true
overview: 'Zoho Payments is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Fintech, and Online Payments.


  Zoho Payments'' developer surface includes signup flow, documentation, API reference, support, engineering blog, pricing, and 15 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 18.4
  coverage:
    artifact_dirs: 10
    catalog_earned: 22.0
    catalog_earned_first_party: 0.0
    catalog_gap: 93.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.0
  facets:
    access_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 46.4
    operational_transparency: 10.5
  previous_composite: 25.4
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 23.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/zoho-payments/zoho-payments-2026-11-03T150536.png
security:
- kind: domain-security
  name: Zoho Payments Domain Security
  slug: zoho-payments-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Payments Vulnerability Disclosure
  slug: zoho-payments-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-payments
tags:
- Company
- Payments
- Fintech
- Online Payments
website: https://www.zoho.com/us/payments/
---

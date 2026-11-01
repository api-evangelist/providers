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
- description: API for Vested Finance platform providing access to investment data and operations.
  name: Vested API
  slug: vested-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/vested-co-in/wsdl/vestedfinance_com_?wsdl.wsdl
  title: ''
  type: WSDL
  url: wsdl/vestedfinance_com_?wsdl.wsdl
- group: agent
  href: https://artifacts.apis.io/vested-co-in/llms/vested-co-in-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vested-co-in-llms.txt
- group: other
  href: https://artifacts.apis.io/vested-co-in/hosts/vested-co-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/vested-co-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/vested-co-in/vendors/vested-co-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/vested-co-in-vendors.yml
- group: auth
  href: https://artifacts.apis.io/vested-co-in/security/vested-co-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vested-co-in-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://vested.co.in/
- group: commercial
  title: ''
  type: Pricing
  url: https://vestedfinance.com/in/pricing/
- group: company
  title: ''
  type: Blog
  url: https://vestedfinance.com/blog/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://vestedfinance.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://vestedfinance.com/legal/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.vestedfinance.com/portal/en/home
coverage:
  checked: '2026-10-29'
  detail: Documentation page https://vestedfinance.com/in/ returns HTML rendered by JavaScript with no machine‑readable spec.
  evidence:
  - status: 200
    url: https://vestedfinance.com/in/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-29'
description: Vested Finance is a fintech platform that enables Indian investors to access global equities, ETFs, mutual funds, private market opportunities, and ESOP/RSU liquidity through a regulated, user-friendly interface. The service offers a single account to buy and hold international stocks, diversified portfolios, and manage tax-efficient investments, backed by partnerships with global custodians and compliance with Indian financial regulations. Vested aims to democratize global investing for retail investors, providing educational resources, low fees, and a seamless onboarding experience.
image: https://vested-wordpress-media-prod-in.s3.ap-south-1.amazonaws.com/wp-content/uploads/2025/11/14083935/logo-primary.svg
layout: provider
modified: '2026-10-29'
name: Vested
nav: Providers
network: true
overview: 'Vested is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include FinTech, Investment, GlobalMarkets, India, and Platform.


  Vested''s developer surface includes pricing, engineering blog, support, and 8 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 13.2
  coverage:
    artifact_dirs: 10
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 57.1
    operational_transparency: 0.0
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
  name: Vested Co In Domain Security
  slug: vested-co-in-domain-security
  summary_line: TLSv1.3
slug: vested-co-in
tags:
- FinTech
- Investment
- GlobalMarkets
- India
- Platform
website: https://vested.co.in/
---

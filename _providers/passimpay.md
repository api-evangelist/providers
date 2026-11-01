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
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/passimpay/llms/passimpay-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/passimpay-llms.txt
- group: auth
  href: https://artifacts.apis.io/passimpay/well-known/passimpay-www-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/passimpay-www-security.txt
- group: agent
  href: https://artifacts.apis.io/passimpay/well-known/passimpay-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/passimpay-well-known.yml
- group: other
  href: https://artifacts.apis.io/passimpay/hosts/passimpay-hosts.yml
  title: ''
  type: Hosts
  url: hosts/passimpay-hosts.yml
- group: other
  href: https://artifacts.apis.io/passimpay/vendors/passimpay-vendors.yml
  title: ''
  type: Vendors
  url: vendors/passimpay-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://passimpay.io/en/terms
- group: operate
  title: ''
  type: Support
  url: https://passimpay.io/en/help
- group: auth
  title: ''
  type: Security
  url: https://passimpay.io/en/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://passimpay.io/en/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://passimpay.io/en/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://passimpay.io/en/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Passimpay
- group: operate
  title: ''
  type: ChangeLog
  url: https://passimpay.io/en/changelog
- group: start
  title: ''
  type: GettingStarted
  url: https://passimpay.io/en/help/how-can-i-connect-my-business-to-passimpay
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api.passimpay.io<svg
- group: auth
  href: https://artifacts.apis.io/passimpay/security/passimpay-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/passimpay-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://passimpay.io
- group: docs
  title: ''
  type: Documentation
  url: https://passimpay.gitbook.io/passimpay-api
- group: docs
  title: ''
  type: APIReference
  url: https://passimpay.gitbook.io/passimpay-api
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 200
    url: https://passimpay.io
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-20'
description: PassimPay provides a B2B crypto payment gateway enabling businesses to accept cryptocurrency payments across over 74 coins with no hidden fees. It offers instant conversion to EUR, automated AML checks, low‑cost USDT TRC20 fees, and fast withdrawals to cold wallets. Serving more than 530 merchants, it processes over $4 billion monthly, delivering 99.99% uptime and detailed reporting tools for sectors such as retail, real‑estate, advertising, healthcare, and renewable energy.
image: https://passimpay.io/_next/static/media/url_cover2_480.84511b5b.png
layout: provider
modified: '2026-10-20'
name: PassimPay
nav: Providers
network: true
overview: 'PassimPay is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, Crypto, B2B, and Gateway.


  PassimPay''s developer surface includes support, pricing, changelog, getting-started guide, documentation, API reference, and 13 more developer resources.'
random_paper: 23
score:
  band: emerging
  composite: 23.8
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 50.0
    operational_transparency: 31.6
  provenance:
    mcp: unknown
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
  name: Passimpay Domain Security
  slug: passimpay-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: passimpay
tags:
- Company
- Payments
- Crypto
- B2B
- Gateway
website: https://passimpay.io
---

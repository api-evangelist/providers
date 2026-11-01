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
  score: 3.1
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API for Downpayments platform providing access to real estate financing services.
  name: Downpayments API
  slug: downpayments-api
artifact_total: 2
common:
- group: other
  href: https://artifacts.apis.io/downpayments/hosts/downpayments-hosts.yml
  title: ''
  type: Hosts
  url: hosts/downpayments-hosts.yml
- group: other
  href: https://artifacts.apis.io/downpayments/vendors/downpayments-vendors.yml
  title: ''
  type: Vendors
  url: vendors/downpayments-vendors.yml
- group: auth
  href: https://artifacts.apis.io/downpayments/security/downpayments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/downpayments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://downpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://downpayments.com/about-us
- group: docs
  title: ''
  type: APIReference
  url: https://downpayments.com/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://downpayments.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://downpayments.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://downpayments.com/terms-of-service
- group: other
  title: ''
  type: x-coverage
  url: https://downpayments.com/faq
- group: auth
  href: https://artifacts.apis.io/downpayments/security/downpayments-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/downpayments-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://downpayments.com/
- group: docs
  title: ''
  type: Documentation
  url: https://downpayments.com/about-us
- group: docs
  title: ''
  type: APIReference
  url: https://downpayments.com/faq
- group: start
  title: ''
  type: GettingStarted
  url: https://downpayments.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://downpayments.com/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://downpayments.com/terms-of-service
coverage:
  checked: '2026-10-24'
  detail: The provider's documentation pages are HTML without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://downpayments.com/faq
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-24'
description: Downpayments is a real estate fintech company that enables homeowners to access the equity in their property to finance down payments on new investments. By offering interest‑free or low‑rate financing up to 10% of a home’s value, it helps buyers purchase additional properties without depleting savings, while providing flexible repayment terms and in‑house brokerage services.
image: https://cdn.prod.website-files.com/657ba3b9e307f30e78525a64/657bc2bc630e91535964fc1b_downpayments-opengraph.webp
layout: provider
modified: '2026-10-24'
name: Downpayments
nav: Providers
network: true
overview: 'Downpayments is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Real Estate, Home Equity, Mortgage, and Investment.


  Downpayments'' developer surface includes documentation, API reference, getting-started guide, and 14 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 15.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
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
  name: Downpayments Domain Security
  slug: downpayments-domain-security
  summary_line: TLSv1.3 · DMARC
slug: downpayments
tags:
- Fintech
- Real Estate
- Home Equity
- Mortgage
- Investment
website: https://downpayments.com/
---

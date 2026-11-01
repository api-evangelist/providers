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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: true
  schema_version: '0.2'
  score: 21.6
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/saltpay-co/well-known/saltpay-co-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/saltpay-co-well-known.yml
- group: other
  href: https://artifacts.apis.io/saltpay-co/hosts/saltpay-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/saltpay-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/saltpay-co/vendors/saltpay-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/saltpay-co-vendors.yml
- group: build
  href: https://artifacts.apis.io/saltpay-co/packages/saltpay-co-packages.yml
  title: ''
  type: SDKs
  url: packages/saltpay-co-packages.yml
- group: build
  href: https://artifacts.apis.io/saltpay-co/packages/saltpay-co-packages.yml
  title: ''
  type: Packages
  url: packages/saltpay-co-packages.yml
- group: auth
  href: https://artifacts.apis.io/saltpay-co/security/saltpay-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/saltpay-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.teya.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.teya.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.teya.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.teya.com/pricing
- group: operate
  title: ''
  type: Support
  url: https://help.teya.com/
- group: company
  title: ''
  type: Blog
  url: https://www.teya.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.teya.com/legal/general-terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.teya.com/legal/privacy-policy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://www.teya.com/api/mcp
  - status: 401
    url: https://teya-marketing-site.teya.com/api/mcp
  - status: 200
    url: https://www.saltpay.co/
  reason: partner-login
  state: gated
created: '2026-10-25'
description: Teya provides card‑machine hardware and a business‑account platform that enables merchants to accept payments, manage cash‑flow, and issue tap‑to‑pay solutions via iPhone and Android. The company offers online payment tools such as Pay‑by‑Link, hosted checkout, and embedded components, alongside funding and financial‑services for small businesses. Founded in the UK, Teya serves merchants across Europe with a focus on seamless integration and transparent pricing.
layout: provider
modified: '2026-10-25'
name: Teya
nav: Providers
network: true
overview: 'Teya is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Payments, FinTech, CardMachines, and BusinessAccounts.


  Teya''s developer surface includes documentation, pricing, support, engineering blog, and 10 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 17.2
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 33.3
    discoverability: 44.6
    operational_transparency: 0.0
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
  name: Saltpay Co Domain Security
  slug: saltpay-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: saltpay-co
tags:
- Company
- Payments
- FinTech
- CardMachines
- BusinessAccounts
website: https://www.teya.com/
---

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
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bindo/refs/heads/main/hosts/bindo-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bindo-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bindo/refs/heads/main/vendors/bindo-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bindo-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bindolabs.com/terms-and-conditions
- group: start
  title: ''
  type: SignUp
  url: https://bindolabs.com/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bindolabs.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://bindolabs.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bindo/refs/heads/main/security/bindo-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bindo-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bindolabs.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 403
    url: https://equityzen.com/company/bindo
  reason: no-developer-program
  state: none
created: '2026-09-28'
description: Bindo, operating as Bindo Labs, provides a comprehensive cloud‑based point‑of‑sale (POS) platform for hospitality, food‑and‑beverage, and retail businesses. Their solution includes POS terminals, payment processing, inventory management, customer engagement tools, and a suite of integrations for online ordering, gift cards, and analytics. Bindo aims to streamline front‑of‑house and back‑of‑house operations, helping merchants increase sales and improve operational efficiency.
layout: provider
modified: '2026-09-28'
name: Bindo
nav: Providers
network: true
overview: 'Bindo is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Point-of-Sale, Retail, Hospitality, and Payments.


  Bindo''s developer surface includes signup flow, engineering blog, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 10.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 12.5
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bindo Domain Security
  slug: bindo-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bindo
tags:
- Company
- Point-of-Sale
- Retail
- Hospitality
- Payments
website: https://bindolabs.com
---

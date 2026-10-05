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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: API for merchant portal operations such as account management and billing.
  name: Biller Genie Merchant API
  slug: biller-genie-merchant-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/billergenie/refs/heads/main/well-known/billergenie-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/billergenie-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billergenie/refs/heads/main/hosts/billergenie-hosts.yml
  title: ''
  type: Hosts
  url: hosts/billergenie-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/billergenie/refs/heads/main/vendors/billergenie-vendors.yml
  title: ''
  type: Vendors
  url: vendors/billergenie-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://merchant.billergenie.com/Account/Register/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/billergenie/refs/heads/main/security/billergenie-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/billergenie-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://merchant.billergenie.com
coverage:
  checked: '2026-09-28'
  detail: OpenAPI spec endpoints on api.billergenie.com all return HTTP 530, indicating no machine‑readable contract is published.
  evidence:
  - status: 530
    url: https://api.billergenie.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-28'
description: Billergenie is a SaaS platform that offers merchants a comprehensive billing and payment solution. The service includes account management, invoicing, subscription handling, and integrated payment processing. It provides a web portal for merchants to manage their business, view analytics, and configure licensing. The platform emphasizes security and compliance, offering terms of use and privacy policies directly through its merchant portal.
layout: provider
modified: '2026-09-28'
name: Billergenie
nav: Providers
network: true
overview: 'Billergenie publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Software-as-a-Service, Billing, Payments, and Merchants.


  Billergenie''s developer surface includes signup flow and 5 more developer resources.'
random_paper: 10
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 53.6
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 10.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Billergenie Domain Security
  slug: billergenie-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: billergenie
tags:
- Company
- Software-as-a-Service
- Billing
- Payments
- Merchants
- Platform
website: https://merchant.billergenie.com
---

---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/np-atobarai/hosts/np-atobarai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/np-atobarai-hosts.yml
- group: other
  href: https://artifacts.apis.io/np-atobarai/vendors/np-atobarai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/np-atobarai-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://help.np-atobarai.jp/hc/ja
- group: docs
  title: ''
  type: Documentation
  url: https://help.np-atobarai.jp/
- group: auth
  href: https://artifacts.apis.io/np-atobarai/security/np-atobarai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/np-atobarai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://np-atobarai.jp/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://corp.netprotections.com/privacypolicy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://np-atobarai.jp/terms/terms.html
coverage:
  checked: '2026-10-26'
  detail: The provider's website presents only HTML pages without any published OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL specifications.
  evidence:
  - status: 200
    url: https://np-atobarai.jp
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-26'
description: NP Atobarai (Net Protections) provides a post‑pay service in Japan, allowing consumers to purchase items and settle invoices later. The platform offers features such as NP points for exchanges and prizes, invoice re‑issuance, and a FAQ covering payment methods and member benefits. It targets convenience store shoppers and online buyers seeking flexible payment options, positioning itself as a fintech solution for after‑sale transactions.
layout: provider
modified: '2026-10-26'
name: NP Atobarai (Net Protections)
nav: Providers
network: true
overview: 'NP Atobarai (Net Protections) is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Payments, Japan, Post-pay, and Consumer.


  NP Atobarai (Net Protections)''s developer surface includes support, documentation, and 6 more developer resources.'
random_paper: 22
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
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
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Np Atobarai Domain Security
  slug: np-atobarai-domain-security
  summary_line: TLSv1.3
slug: np-atobarai
tags:
- Fintech
- Payments
- Japan
- Post-pay
- Consumer
website: https://np-atobarai.jp/
---

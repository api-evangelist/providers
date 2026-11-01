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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/functional-finance/hosts/functional-finance-hosts.yml
  title: ''
  type: Hosts
  url: hosts/functional-finance-hosts.yml
- group: other
  href: https://artifacts.apis.io/functional-finance/vendors/functional-finance-vendors.yml
  title: ''
  type: Vendors
  url: vendors/functional-finance-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.functionalfi.com/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.functionalfi.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.functionalfi.com/
- group: auth
  href: https://artifacts.apis.io/functional-finance/security/functional-finance-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/functional-finance-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.functionalfi.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.functionalfi.com/
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Functional Finance provides an automated financial operations platform for insurance companies, MGAs, and wholesalers. It simplifies billing, payments, and reconciliation, offering APIs to integrate insurance money movement, streamline workflows, and improve operational efficiency across the insurance ecosystem.
image: https://cdn.prod.website-files.com/669a8a92a94ec7da3395ad98/66fad81449471d6e337cc047_ff-open%20graph.webp
layout: provider
modified: '2026-10-22'
name: Functional Finance
nav: Providers
network: true
overview: 'Functional Finance is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Insurance, FinTech, Payments, and Billing.


  Functional Finance''s developer surface includes documentation and 6 more developer resources.'
random_paper: 20
score:
  band: minimal
  composite: 10.3
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Functional Finance Domain Security
  slug: functional-finance-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: functional-finance
tags:
- Company
- Insurance
- FinTech
- Payments
- Billing
- API
website: https://www.functionalfi.com/
---

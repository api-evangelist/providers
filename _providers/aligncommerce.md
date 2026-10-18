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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aligncommerce/refs/heads/main/hosts/aligncommerce-hosts.yml
  title: ''
  type: Hosts
  url: hosts/aligncommerce-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/aligncommerce/refs/heads/main/vendors/aligncommerce-vendors.yml
  title: ''
  type: Vendors
  url: vendors/aligncommerce-vendors.yml
- group: company
  title: ''
  type: Blog
  url: https://www.alignecommerce.com/blog
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/aligncommerce/refs/heads/main/security/aligncommerce-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/aligncommerce-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alignecommerce.com
coverage:
  checked: '2026-10-05'
  detail: No OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL spec found at common API endpoints.
  evidence:
  - status: 0
    url: https://api.alignecommerce.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-24'
description: Aligncommerce provides high‑risk ecommerce payment processing solutions, offering direct banking relationships, compliance‑first architecture, and dedicated support. Their platform enables merchants in regulated industries such as firearms, adult entertainment, hemp, and telemedicine to accept payments securely and efficiently, having processed over $1 billion in transactions and recognized for industry excellence.
image: http://static1.squarespace.com/static/69b774465498077dcddf409b/t/69b7adbb1729786981730dbf/1773645243253/Untitled+design+%282%29.png?format=1500w
layout: provider
modified: '2026-09-24'
name: Aligncommerce
nav: Providers
network: true
overview: 'Aligncommerce is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payments, High‑Risk Merchants, Chargeback Management, Fraud Prevention, and E‑commerce Integration.


  Aligncommerce''s developer surface includes engineering blog and 4 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 3.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.9
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  previous_composite: 0.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 5.4
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Aligncommerce Domain Security
  slug: aligncommerce-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: aligncommerce
tags:
- Payments
- High‑Risk Merchants
- Chargeback Management
- Fraud Prevention
- E‑commerce Integration
website: https://www.alignecommerce.com
---

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
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: Bindx provides a suite of financial APIs including eCheqs, crypto trading, FX operations, and BCollect payments as listed in their developer portal.
  name: Bindx API
  slug: bindx-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bindx/refs/heads/main/hosts/bindx-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bindx-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bindx/refs/heads/main/vendors/bindx-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bindx-vendors.yml
- group: docs
  title: ''
  type: Documentation
  url: https://developers.bindx.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bindx/refs/heads/main/security/bindx-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bindx-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bindx.com
coverage:
  checked: '2026-09-28'
  detail: Access to the developers.bindx.com API documentation returns HTTP 403 Access Denied, preventing contract discovery.
  evidence:
  - status: 403
    url: https://developers.bindx.com/openapi.json
  reason: partner-login
  state: gated
created: '2026-09-28'
description: Bindx is an Argentine fintech company offering a modular, integrated financial ecosystem through APIs. It provides services such as digital wallets, payments, lending, insurance, and identity verification, targeting businesses to embed banking and financial functionalities. With a focus on scalability and automation, Bindx serves hundreds of companies and millions of users across Latin America, delivering secure and compliant API solutions for banking, payments, crypto, and more.
image: https://www.bindx.com/images/shares_web/fb.jpg?1782436650
layout: provider
modified: '2026-09-28'
name: Bindx
nav: Providers
network: true
overview: 'Bindx publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Fintech, Banking, Payments, and Argentina.


  Bindx''s developer surface includes documentation and 4 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 4.3
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - argentina
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - latin-america
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Banking & Open Finance
    regime_id: banking_open_finance
    score: 4.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bindx Domain Security
  slug: bindx-domain-security
  summary_line: TLSv1.3 · HSTS
slug: bindx
tags:
- Fintech
- Banking
- Payments
- Argentina
website: https://www.bindx.com
---

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
  href: https://raw.githubusercontent.com/api-evangelist/crmls/refs/heads/main/hosts/crmls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/crmls-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/crmls/refs/heads/main/vendors/crmls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/crmls-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/crmls/refs/heads/main/security/crmls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/crmls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://go.crmls.org/
- group: company
  title: ''
  type: Blog
  url: https://blog.crmls.org/
- group: operate
  title: ''
  type: Support
  url: https://go.crmls.org/support/
- group: other
  title: ''
  type: KnowledgeBase
  url: https://kb.crmls.org/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://go.crmls.org/privacy-policy/
- group: start
  title: ''
  type: Login
  url: https://app.crmls.recore.net/login
coverage:
  checked: '2026-10-14'
  detail: CRMLS IDX Resources offers a "RESO Certified Feed" only through its Data Licensing Request Form and approved IDX vendors; no API reference, endpoint or contract is published on go.crmls.org, kb.crmls.org or api.crmls.org (which does not resolve).
  evidence:
  - status: 200
    url: https://go.crmls.org/idx-resources/
  - status: 200
    url: https://go.crmls.org/crmls-data-licensing-request-form/
  reason: sales-gate
  state: gated
created: '2026-10-13'
description: California Regional MLS (CRMLS) is the largest multiple listing service in the United States, serving REALTORS across California with MLS systems (Flexmls, Matrix, Paragon), compliance and education. Listing data reaches developers as IDX and RESO certified data feeds licensed through a CRMLS data licensing request and approved IDX vendors; CRMLS publishes no public API documentation or machine-readable contract of its own.
image: https://go.crmls.org/wp-content/uploads/2018/11/CRMLS-Logo-Thumbnail.jpg
layout: provider
modified: '2026-10-14'
name: California Regional MLS
nav: Providers
network: true
overview: 'California Regional MLS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Real Estate, MLS, IDX, and RESO.


  California Regional MLS''s developer surface includes engineering blog, support, and 7 more developer resources.'
random_paper: 17
score:
  band: minimal
  composite: 10.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 48.2
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Crmls Domain Security
  slug: crmls-domain-security
  summary_line: TLSv1.3 · DMARC
slug: crmls
tags:
- Company
- Real Estate
- MLS
- IDX
- RESO
- Listings
- California
website: https://go.crmls.org/
---

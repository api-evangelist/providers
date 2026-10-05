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
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bima/refs/heads/main/hosts/bima-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bima-hosts.yml
- group: start
  title: ''
  type: Login
  url: https://bima.om/Customer/SignIn
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bima/refs/heads/main/security/bima-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bima-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bima.om
- group: docs
  title: ''
  type: Documentation
  url: https://bima.om/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://bima.om/docs/V3/Index.html
- group: start
  title: ''
  type: GettingStarted
  url: https://bima.om/Home/AboutUs
- group: operate
  title: ''
  type: Support
  url: https://bima.om/SupportCenter
- group: commercial
  title: ''
  type: TermsOfService
  url: https://bima.om/Home/Terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bima.om/Home/PrivacyPolicy
- group: operate
  title: ''
  type: FAQ
  url: https://bima.om/Home/FAQ
- group: company
  title: ''
  type: Blog
  url: https://bima.om/Contents/Articles
coverage:
  checked: '2026-09-28'
  detail: Documentation pages render only via JavaScript, providing no machine‑readable spec.
  evidence:
  - status: 200
    url: https://api.bima.om/Docs
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-28'
description: BIMA is a leading insurance gateway in Oman, offering a wide range of insurance products including vehicle, travel, health, and credit life. The platform provides a user-friendly digital experience with quick policy issuance, 24/7 support, and compliance with Oman's financial services authority. It aims to simplify insurance access for individuals and businesses across the region.
image: https://bima.om/img/logo/bima-en.png
layout: provider
modified: '2026-09-28'
name: BIMA
nav: Providers
network: true
overview: 'BIMA is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Oman, Digital, Gateways, and Bima.


  BIMA''s developer surface includes documentation, API reference, getting-started guide, support, FAQ, engineering blog, and 6 more developer resources.'
random_paper: 13
score:
  band: emerging
  composite: 18.1
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - middle-east
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 12.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bima Domain Security
  slug: bima-domain-security
  summary_line: TLSv1.2 · HSTS
slug: bima
tags:
- Insurance
- Oman
- Digital
- Gateways
- Bima
website: https://bima.om
---

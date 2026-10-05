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
  href: https://raw.githubusercontent.com/api-evangelist/arincare/refs/heads/main/hosts/arincare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/arincare-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/arincare/refs/heads/main/vendors/arincare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/arincare-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://app.arincare.com/login
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/arincare/refs/heads/main/security/arincare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/arincare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://arincare.com
- group: docs
  title: ''
  type: Documentation
  url: https://arincare.com/index_en.html
- group: company
  title: ''
  type: Blog
  url: https://blog.arincare.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://arincare.com/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://arincare.com/privacy.html
coverage:
  checked: 2026-09-26
  detail: The documentation pages are HTML rendered with JavaScript, preventing machine‑readable spec discovery.
  evidence:
  - status: 200
    url: https://arincare.com/index_en.html
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-26'
description: Arincare provides a digital pharmacy platform for pharmacists and drugstores in Thailand, offering a suite of tools including inventory management, point‑of‑sale, e‑prescription, e‑referral, telepharmacy, and a pharma marketplace. The solution aims to streamline pharmacy operations, improve patient care, and increase sales through an integrated, free‑to‑use system.
image: https://arincare.com/img/logo-in-fbs.png
layout: provider
modified: '2026-09-26'
name: Arincare
nav: Providers
network: true
overview: 'Arincare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Pharmacy, Digital Health, Thailand, and Software-as-a-Service.


  Arincare''s developer surface includes documentation, engineering blog, and 7 more developer resources.'
random_paper: 1
score:
  band: emerging
  composite: 13.8
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
    developer_ergonomics: 11.9
    discoverability: 48.2
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - thailand
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - southeast-asia
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Arincare Domain Security
  slug: arincare-domain-security
  summary_line: TLSv1.3
slug: arincare
tags:
- Company
- Pharmacy
- Digital Health
- Thailand
- Software-as-a-Service
website: https://arincare.com
---

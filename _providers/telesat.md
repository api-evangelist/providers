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
  scored_at: '2026-09-24'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/telesat/refs/heads/main/llms/telesat-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/telesat-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telesat/refs/heads/main/hosts/telesat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/telesat-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/telesat/refs/heads/main/vendors/telesat-vendors.yml
  title: ''
  type: Vendors
  url: vendors/telesat-vendors.yml
- group: operate
  title: ''
  type: Support
  url: https://support.telesat.com/(S(rngxmuiw0bfsd1m4h0mec055))/default.aspx
- group: company
  title: ''
  type: Newsroom
  url: https://www.telesat.com/press/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/telesat/refs/heads/main/security/telesat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/telesat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.telesat.com/
- group: company
  title: ''
  type: Blog
  url: https://www.telesat.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.telesat.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.telesat.com/privacy-policy/
coverage:
  checked: 2026-09-23
  detail: OpenAPI endpoint returned HTML SPA instead of a machine‑readable spec
  evidence:
  - status: 200
    url: https://app.telesat.com/openapi.json
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-23'
description: Telesat is a leading global satellite operator providing advanced communications solutions. With over 55 years of experience, Telesat delivers secure, high‑capacity broadband services via its Lightspeed Low Earth Orbit (LEO) satellite network, serving commercial, governmental, and defense customers worldwide. The company focuses on innovative satellite technology to address complex connectivity challenges across the globe.
image: https://www.telesat.com/wp-content/uploads/2022/01/Telesat-Logo-Twitter.png
layout: provider
modified: '2026-09-23'
name: Telesat
nav: Providers
network: true
overview: 'Telesat is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Satellite, Communications, LEO, and Global.


  Telesat''s developer surface includes support, engineering blog, and 8 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 11.4
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
    developer_ergonomics: 7.1
    discoverability: 57.4
    operational_transparency: 0.0
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - global
  provenance:
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Telesat Domain Security
  slug: telesat-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: telesat
tags:
- Company
- Satellite
- Communications
- LEO
- Global
website: https://www.telesat.com/
---

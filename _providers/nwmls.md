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
  href: https://raw.githubusercontent.com/api-evangelist/nwmls/refs/heads/main/hosts/nwmls-hosts.yml
  title: ''
  type: Hosts
  url: hosts/nwmls-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/nwmls/refs/heads/main/vendors/nwmls-vendors.yml
  title: ''
  type: Vendors
  url: vendors/nwmls-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.nwmls.com/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.nwmls.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.nwmls.com/category/news/
- group: company
  title: ''
  type: Blog
  url: https://www.nwmls.com/category/blog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/nwmls/refs/heads/main/security/nwmls-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/nwmls-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.nwmls.com
coverage:
  checked: '2026-10-14'
  detail: NWMLS publishes no public developer program; listing data is licensed to members and approved vendors, and its IMS system at ims.nwmls.com redirects to an IMS Member Login page.
  evidence:
  - status: 200
    url: https://ims.nwmls.com/
  - status: 404
    url: https://www.nwmls.com/data-licensing/
  - status: 404
    url: https://www.nwmls.com/vendors/
  reason: partner-login
  state: gated
created: '2026-10-13'
description: 'NWMLS is a company surfaced via the API Evangelist harvest backlog (source: market-gap:real-estate) and added to the network as a stub for full-pipeline profiling.'
image: https://www.nwmls.com/wp-content/uploads/2026/09/hero-neighborhood.webp
layout: provider
modified: '2026-10-13'
name: NWMLS
nav: Providers
network: true
overview: 'NWMLS is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company.


  NWMLS''s developer surface includes engineering blog and 7 more developer resources.'
random_paper: 11
score:
  band: minimal
  composite: 7.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 17.0
    catalog_earned_first_party: 0.0
    catalog_gap: 98.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 32.1
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Nwmls Domain Security
  slug: nwmls-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: nwmls
tags:
- Company
website: https://www.nwmls.com
---

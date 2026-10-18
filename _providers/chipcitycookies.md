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
api_count: 1
apis:
- description: Provides information about Chipcitycookies catering services and cookie offerings.
  name: Chipcitycookies API
  slug: chipcitycookies-api
artifact_total: 2
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chipcitycookies/refs/heads/main/hosts/chipcitycookies-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chipcitycookies-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/chipcitycookies/refs/heads/main/vendors/chipcitycookies-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chipcitycookies-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://chipcitycookies.com/sign-up
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/chipcitycookies/refs/heads/main/security/chipcitycookies-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chipcitycookies-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chipcitycookies.com
- group: operate
  title: ''
  type: Support
  url: https://chipcitycookies.com/support
coverage:
  checked: '2026-10-08'
  detail: Chipcitycookies does not offer a developer program or public API documentation.
  evidence:
  - status: 200
    url: https://chipcitycookies.com
  reason: no-developer-program
  state: none
created: '2026-10-08'
description: Chipcitycookies is a bakery and catering company that offers a wide variety of cookie flavors across the United States. After operating for over a decade, the company announced the closure of its physical locations due to macro‑economic challenges but continues to ship cookies nationwide, provide catering services, and sell gift cards online. The site includes information on flavors, catering options, nutritional details, and a support portal for customers.
image: https://chipcitycookies.com/og_image.jpg
layout: provider
modified: '2026-10-08'
name: Chipcitycookies
nav: Providers
network: true
overview: 'Chipcitycookies is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bakery, Catering, Cookies, and E-Commerce.


  Chipcitycookies'' developer surface includes signup flow, support, and 4 more developer resources.'
random_paper: 4
score:
  band: minimal
  composite: 7.9
  coverage:
    artifact_dirs: 7
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 4.8
    discoverability: 57.1
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chipcitycookies Domain Security
  slug: chipcitycookies-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chipcitycookies
tags:
- Company
- Bakery
- Catering
- Cookies
- E-Commerce
website: https://chipcitycookies.com
---

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
  scored_at: '2026-10-03'
api_count: 1
apis:
- description: Automotive data APIs providing vehicle identity, history, valuations, specs and images.
  name: One Auto API
  slug: one-auto-api
artifact_total: 2
common:
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.oneautoapi.com/privacy-policy/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/oneautoapi/refs/heads/main/changelog/oneautoapi-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/oneautoapi-changelog.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oneautoapi/refs/heads/main/hosts/oneautoapi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/oneautoapi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/oneautoapi/refs/heads/main/vendors/oneautoapi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/oneautoapi-vendors.yml
- group: start
  title: ''
  type: Login
  url: https://www.oneautoapi.com/login/
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.oneautoapi.com/changelog/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/oneautoapi/refs/heads/main/security/oneautoapi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/oneautoapi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.oneautoapi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.oneautoapi.com/
- group: docs
  title: ''
  type: APIReference
  url: https://swagger.oneautoapi.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.oneautoapi.com/signup/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.oneautoapi.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://go.oneautoapi.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://www.oneautoapi.com/contact/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.oneautoapi.com/terms/
coverage:
  checked: '2026-10-02'
  detail: Documentation pages redirect to JavaScript‑rendered SPA with no machine‑readable spec.
  evidence:
  - status: 308
    url: https://www.oneautoapi.com/docs/
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-02'
description: One Auto API provides comprehensive automotive data APIs for vehicle lookup, valuations, retail pricing, and more across the US, UK, and Europe. Their platform offers over 100 API methods covering car images, mileage checks, specifications, electric vehicle data, registration lookup, service history, and valuation, all accessible via a single subscription and monthly invoice. Designed for developers, product managers, and dealers, the service includes bulk report building, VRM360 insights, and consultancy services, backed by multiple data providers.
image: https://www.oneautoapi.com/images/og-image.png
layout: provider
modified: '2026-10-02'
name: One Auto API
nav: Providers
network: true
overview: 'One Auto API publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Automotive, Data, Vehicles, and United Kingdom.


  One Auto API''s developer surface includes changelog, documentation, API reference, getting-started guide, pricing, engineering blog, support, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 48.2
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Oneautoapi Domain Security
  slug: oneautoapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: oneautoapi
tags:
- Automotive
- Data
- Vehicles
- United Kingdom
website: https://www.oneautoapi.com/
---

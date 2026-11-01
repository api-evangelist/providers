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
  href: https://artifacts.apis.io/stayukio-com/hosts/stayukio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/stayukio-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/stayukio-com/vendors/stayukio-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/stayukio-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/stayukio-com/security/stayukio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/stayukio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://ukio.com/
- group: company
  title: ''
  type: AboutUs
  url: https://ukio.com/about-us
- group: operate
  title: ''
  type: Contact
  url: https://ukio.com/contact-us
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ukio.com/terms-and-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ukio.com/privacy-policy
- group: other
  title: ''
  type: CookiePolicy
  url: https://ukio.com/cookie-policy
- group: other
  title: ''
  type: Sitemap
  url: https://ukio.com/sitemap
- group: company
  title: ''
  type: Blog
  url: https://medium.com/ukio
- group: company
  title: ''
  type: Careers
  url: https://ukio.com/careers
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.stayukio.com/
  reason: no-developer-program
  state: none
created: '2026-10-28'
description: Ukio is a monthly furnished apartment rental platform operating across major European cities. It offers fully furnished homes for rent, purchase, and property management services, targeting business travelers and long‑term residents. The brand emphasizes design, technology integration, and a comprehensive suite of services, positioning itself as a modern alternative to traditional real‑estate markets.
image: https://cdn.sanity.io/images/v48q37k7/production/11f53c58cd6fd491b40fae982008bfda92690de2-1905x920.jpg
layout: provider
modified: '2026-10-28'
name: Ukio
nav: Providers
network: true
overview: 'Ukio is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, RealEstate, Housing, Rentals, and Europe.


  Ukio''s developer surface includes engineering blog and 11 more developer resources.'
random_paper: 5
score:
  band: minimal
  composite: 9.3
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
    developer_ergonomics: 2.4
    discoverability: 48.2
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Stayukio Com Domain Security
  slug: stayukio-com-domain-security
  summary_line: TLSv1.3 · DMARC
slug: stayukio-com
tags:
- Company
- RealEstate
- Housing
- Rentals
- Europe
website: https://ukio.com/
---

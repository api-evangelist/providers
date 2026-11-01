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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/tessitura/hosts/tessitura-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tessitura-hosts.yml
- group: other
  href: https://artifacts.apis.io/tessitura/vendors/tessitura-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tessitura-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.tessitura.com/About/Terms-of-Use
- group: auth
  title: ''
  type: Security
  url: https://www.tessitura.com/support/security
- group: commercial
  title: ''
  type: Pricing
  url: https://www.tessitura.com/items/support/alerts/2024/pricing-rules-fix
- group: start
  title: ''
  type: Login
  url: https://www.tessitura.com/login
- group: other
  title: ''
  type: Leadership
  url: https://www.tessitura.com/about/team
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.tessitura.com/support/start/developers
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.tessitura.com/files/misc/links/release-notes
- group: auth
  href: https://artifacts.apis.io/tessitura/security/tessitura-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tessitura-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tessitura.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.tessitura.com/about
- group: operate
  title: ''
  type: Support
  url: https://www.tessitura.com/support
- group: company
  title: ''
  type: Blog
  url: https://www.tessitura.com/about/news
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.tessitura.com/about/privacy
coverage:
  checked: '2026-10-27'
  detail: The Tessitura website provides no machine‑readable API specification despite having a corporate site.
  evidence:
  - status: 200
    url: https://www.tessitura.com/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: Tessitura provides a unified platform for arts and cultural organizations, delivering integrated CRM, ticketing, admissions, fundraising, memberships, marketing, education, and e‑commerce solutions. Their cloud‑based system helps nonprofits manage audiences, revenue, and engagement across multiple channels, supporting venues, museums, festivals, orchestras, and other cultural institutions worldwide.
image: https://edge.sitecorecloud.io/tessituraneab9a-tessiturane5642-staging-5396/media/Images/Logos/Tessitura-Logo.png?h=696&iar=0&w=1700
layout: provider
modified: '2026-10-27'
name: Tessitura
nav: Providers
network: true
overview: 'Tessitura is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Arts, Culture, Nonprofit, and CRM.


  Tessitura''s developer surface includes pricing, changelog, documentation, support, engineering blog, and 10 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 22.4
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 50.0
    operational_transparency: 26.3
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
  name: Tessitura Domain Security
  slug: tessitura-domain-security
  summary_line: TLSv1.3 · HSTS
slug: tessitura
tags:
- Company
- Arts
- Culture
- Nonprofit
- CRM
- Ticketing
website: https://tessitura.com/
---

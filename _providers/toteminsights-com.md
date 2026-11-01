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
  href: https://artifacts.apis.io/toteminsights-com/hosts/toteminsights-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/toteminsights-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/toteminsights-com/vendors/toteminsights-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/toteminsights-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.humanitru.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.humanitru.com/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.humanitru.com/blog
- group: auth
  href: https://artifacts.apis.io/toteminsights-com/security/toteminsights-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/toteminsights-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://humanitru.com/
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://toteminsights.com/
  reason: no-developer-program
  state: none
created: '2026-10-24'
description: Humanitru is an integration‑first nonprofit CRM built to consolidate data from fundraising and engagement tools, delivering a complete view of each supporter. It serves nonprofits, museums, zoos, and aquariums, offering a cloud‑based platform for donor management, communications, and analytics.
image: https://cdn.prod.website-files.com/698241a7b516516506d193d8/69bb4b0af688a315ddcae000_website%20open%20graph%20image.png
layout: provider
modified: '2026-10-24'
name: Humanitru
nav: Providers
network: true
overview: 'Humanitru is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, CRM, Nonprofit, Data Integration, and Donor Management.


  Humanitru''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 9.3
  coverage:
    artifact_dirs: 7
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
    mcp: derived
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
  name: Toteminsights Com Domain Security
  slug: toteminsights-com-domain-security
  summary_line: TLSv1.2 · HSTS
slug: toteminsights-com
tags:
- Company
- CRM
- Nonprofit
- Data Integration
- Donor Management
website: https://humanitru.com/
---

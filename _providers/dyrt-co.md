---
agent_readiness:
  band: agent-aware
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 6.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/dyrt-co/hosts/dyrt-co-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dyrt-co-hosts.yml
- group: other
  href: https://artifacts.apis.io/dyrt-co/vendors/dyrt-co-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dyrt-co-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://dyrt.co/press
- group: auth
  href: https://artifacts.apis.io/dyrt-co/security/dyrt-co-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dyrt-co-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dyrt.co/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://app.dyrt.co
- group: company
  title: ''
  type: Blog
  url: https://dyrt.co/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dyrt.co/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dyrt.co/privacy
coverage:
  checked: '2026-10-24'
  detail: The developer portal at https://app.dyrt.co loads a JavaScript SPA and provides no machine‑readable API spec.
  evidence:
  - status: 200
    url: https://app.dyrt.co
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-24'
description: Dyrt provides waste‑savings solutions for enterprises, governments and operators, ingesting invoices, contracts, utility bills and hauler data to identify cost reductions, lower emissions and improve vendor management. Their platform offers analytics, automated waste‑diversion tracking and reporting, helping customers such as hotels, arenas and corporate campuses cut waste spend by up to 30%.
image: https://dyrt.co/og-image.png
layout: provider
modified: '2026-10-24'
name: Dyrt
nav: Providers
network: true
overview: 'Dyrt is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Waste, Sustainability, Analytics, Enterprise, and Government.


  Dyrt''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 10
score:
  band: emerging
  composite: 11.7
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
    developer_ergonomics: 11.9
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Dyrt Co Domain Security
  slug: dyrt-co-domain-security
  summary_line: TLSv1.3 · DMARC
slug: dyrt-co
tags:
- Waste
- Sustainability
- Analytics
- Enterprise
- Government
website: https://dyrt.co/
---

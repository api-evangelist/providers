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
  href: https://artifacts.apis.io/proliant/hosts/proliant-hosts.yml
  title: ''
  type: Hosts
  url: hosts/proliant-hosts.yml
- group: other
  href: https://artifacts.apis.io/proliant/vendors/proliant-vendors.yml
  title: ''
  type: Vendors
  url: vendors/proliant-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://blog.proliant.com/topic/security
- group: auth
  href: https://artifacts.apis.io/proliant/security/proliant-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proliant-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.proliant.com/
- group: operate
  title: ''
  type: Support
  url: https://www.proliant.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://blog.proliant.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proliant.com/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proliant.com/privacy-policy
coverage:
  checked: '2026-10-27'
  detail: The public website provides no machine‑readable API specifications or developer documentation.
  evidence:
  - status: 200
    url: https://www.proliant.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-27'
description: ProLiant provides modern payroll and HR management software for businesses, offering solutions such as payroll processing, tax services, employee onboarding, applicant tracking, time and labor management, and compensation management. Their platform emphasizes a people‑first economy, delivering cloud‑based tools that streamline workforce administration and integrate with various HR ecosystems.
image: https://www.proliant.com/hubfs/01%20-%20Website/4%20-%20Main%20Pages/Home/proliant-home-feature-image.png
layout: provider
modified: '2026-10-27'
name: ProLiant
nav: Providers
network: true
overview: 'ProLiant is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Payroll, HR, SaaS, Cloud, and PeopleFirst.


  ProLiant''s developer surface includes support, engineering blog, and 7 more developer resources.'
random_paper: 9
score:
  band: emerging
  composite: 11.1
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
    discoverability: 48.2
    operational_transparency: 10.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Employment & Payroll
    regime_id: employment_payroll
    score: 13.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Proliant Domain Security
  slug: proliant-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: proliant
tags:
- Payroll
- HR
- SaaS
- Cloud
- PeopleFirst
- Company
website: https://www.proliant.com/
---

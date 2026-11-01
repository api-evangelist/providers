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
  href: https://artifacts.apis.io/chg-healthcare/hosts/chg-healthcare-hosts.yml
  title: ''
  type: Hosts
  url: hosts/chg-healthcare-hosts.yml
- group: other
  href: https://artifacts.apis.io/chg-healthcare/vendors/chg-healthcare-vendors.yml
  title: ''
  type: Vendors
  url: vendors/chg-healthcare-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://chghealthcare.com/newsroom
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/chghealthcare
- group: auth
  href: https://artifacts.apis.io/chg-healthcare/security/chg-healthcare-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/chg-healthcare-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://chghealthcare.com
- group: company
  title: ''
  type: Blog
  url: https://chghealthcare.com/blog
created: '2026-10-26'
description: CHG Healthcare is the nation’s largest physician staffing company, providing comprehensive workforce solutions across healthcare. It offers physician, advanced practice, and allied health staffing, along with technology and advisory services to hospitals and health systems. The company is recognized as a Fortune Best Companies to Work For and serves a broad client base nationwide.
layout: provider
modified: '2026-10-26'
name: CHG Healthcare
nav: Providers
network: true
overview: 'CHG Healthcare is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Staffing, Physician, and Technology.


  CHG Healthcare''s developer surface includes engineering blog and 6 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 4.7
  coverage:
    artifact_dirs: 6
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 46.4
    operational_transparency: 5.3
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 4.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Chg Healthcare Domain Security
  slug: chg-healthcare-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: chg-healthcare
tags:
- Company
- Healthcare
- Staffing
- Physician
- Technology
website: https://chghealthcare.com
---

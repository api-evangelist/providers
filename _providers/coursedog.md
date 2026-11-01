---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 18.7
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/coursedog/well-known/coursedog-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/coursedog-well-known.yml
- group: other
  href: https://artifacts.apis.io/coursedog/hosts/coursedog-hosts.yml
  title: ''
  type: Hosts
  url: hosts/coursedog-hosts.yml
- group: other
  href: https://artifacts.apis.io/coursedog/vendors/coursedog-vendors.yml
  title: ''
  type: Vendors
  url: vendors/coursedog-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.coursedog.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.coursedog.com/privacy-policy
- group: docs
  title: ''
  type: Documentation
  url: https://dev.coursedog.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/coursedog
- group: auth
  href: https://artifacts.apis.io/coursedog/security/coursedog-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/coursedog-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.coursedog.com
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: 200
    url: https://www.coursedog.com
  reason: no-developer-program
  state: none
created: '2026-10-22'
description: Coursedog provides an integrated academic operations platform that empowers higher education administrators with scheduling, curriculum management, online catalogs, and comprehensive academic reporting tools. The solution aims to streamline campus workflows, improve data visibility, and enhance the student experience, positioning Coursedog as a trusted partner in the education technology ecosystem.
image: https://cdn.prod.website-files.com/671f67e74337377deb9a3cb5/67aa2e6258db9538fc9e2246_OG%20-Home.png
layout: provider
modified: '2026-10-22'
name: Coursedog
nav: Providers
network: true
overview: 'Coursedog is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Education, SaaS, AcademicOperations, and Scheduling.


  Coursedog''s developer surface includes documentation and 8 more developer resources.'
random_paper: 11
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 6
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 21.1
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 15.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Coursedog Domain Security
  slug: coursedog-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: coursedog
tags:
- Company
- Education
- SaaS
- AcademicOperations
- Scheduling
website: https://www.coursedog.com
---

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
  score: 18.2
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/joincoded-com/well-known/joincoded-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joincoded-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/joincoded-com/hosts/joincoded-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joincoded-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joincoded-com/vendors/joincoded-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joincoded-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/joincoded-com/packages/joincoded-com-packages.yml
  title: ''
  type: SDKs
  url: packages/joincoded-com-packages.yml
- group: build
  href: https://artifacts.apis.io/joincoded-com/packages/joincoded-com-packages.yml
  title: ''
  type: Packages
  url: packages/joincoded-com-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://coded.kw/privacy-policy
- group: start
  title: ''
  type: DeveloperPortal
  url: https://portal.joincoded.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/JoinCODED
- group: auth
  href: https://artifacts.apis.io/joincoded-com/security/joincoded-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joincoded-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coded.kw
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: 401
    url: https://portal.joincoded.com/api/mcp
  - status: 200
    url: https://joincoded.com
  reason: partner-login
  state: gated
created: '2026-10-25'
description: Join CODED in Kuwait for practical coding bootcamps and tech programs for professionals, youth, and kids. Build real skills through hands‑on projects, view upcoming programs, and become part of a vibrant tech community. CODED offers immersive curricula, mentorship, and industry‑aligned projects that prepare learners for careers in software development, data science, and digital product design.
image: https://coded.kw/img/og/og-default.png
layout: provider
modified: '2026-10-25'
name: Coded
nav: Providers
network: true
overview: Coded is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Bootcamps, Technology, Kuwait, and Coding.
random_paper: 11
score:
  band: minimal
  composite: 10.5
  coverage:
    artifact_dirs: 7
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 48.2
    operational_transparency: 5.3
  provenance:
    mcp: unknown
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
  name: Joincoded Com Domain Security
  slug: joincoded-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: joincoded-com
tags:
- Education
- Bootcamps
- Technology
- Kuwait
- Coding
website: https://coded.kw
---

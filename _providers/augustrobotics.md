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
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://augustrobotics.com/vdp
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustrobotics/refs/heads/main/well-known/augustrobotics-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/augustrobotics-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augustrobotics/refs/heads/main/well-known/augustrobotics-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/augustrobotics-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augustrobotics/refs/heads/main/hosts/augustrobotics-hosts.yml
  title: ''
  type: Hosts
  url: hosts/augustrobotics-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augustrobotics/refs/heads/main/vendors/augustrobotics-vendors.yml
  title: ''
  type: Vendors
  url: vendors/augustrobotics-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://augustrobotics.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/augustrobotics
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustrobotics/refs/heads/main/security/augustrobotics-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/augustrobotics-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augustrobotics/refs/heads/main/security/augustrobotics-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augustrobotics-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://augustrobotics.com
- group: docs
  title: ''
  type: Documentation
  url: https://augustrobotics.com/platform
- group: company
  title: ''
  type: AboutUs
  url: https://augustrobotics.com/about-us
coverage:
  detail: the company publishes developer documentation but serves no machine-readable contract from it
  evidence:
  - status: 403
    url: https://portal.augustrobotics.com/mcp
  - status: 403
    url: https://equityzen.com/company/augustrobotics
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-26'
description: August Robotics provides autonomous robotic fleets for construction, exhibition, and industrial applications. Their AI‑driven platform automates dirty, dangerous and dull jobs, improving productivity and safety across sectors. The company offers modular robot solutions, leasing options, and a comprehensive service ecosystem to accelerate project delivery.
image: https://cdn.prod.website-files.com/68f9b17280b6a3c1d5029c80/6901e2decdaa1113ff158443_Open%20Graph%20Image%201200x630.png
layout: provider
modified: '2026-09-26'
name: Augustrobotics
nav: Providers
network: true
overview: 'Augustrobotics is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Robotics, Construction, Exhibition, Automation, and Artificial Intelligence.


  Augustrobotics'' developer surface includes documentation and 11 more developer resources.'
random_paper: 16
score:
  band: minimal
  composite: 8.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 50.0
    operational_transparency: 15.8
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Augustrobotics Domain Security
  slug: augustrobotics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Augustrobotics Vulnerability Disclosure
  slug: augustrobotics-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: augustrobotics
tags:
- Robotics
- Construction
- Exhibition
- Automation
- Artificial Intelligence
website: https://augustrobotics.com
---

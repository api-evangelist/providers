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
  scored_at: '2026-10-17'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: Security
  url: https://www.raspberrypi.com/security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raspberry-pi/refs/heads/main/well-known/raspberry-pi-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/raspberry-pi-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/raspberry-pi/refs/heads/main/well-known/raspberry-pi-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/raspberry-pi-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/raspberry-pi/refs/heads/main/hosts/raspberry-pi-hosts.yml
  title: ''
  type: Hosts
  url: hosts/raspberry-pi-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/raspberry-pi/refs/heads/main/vendors/raspberry-pi-vendors.yml
  title: ''
  type: Vendors
  url: vendors/raspberry-pi-vendors.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raspberry-pi/refs/heads/main/security/raspberry-pi-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/raspberry-pi-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/raspberry-pi/refs/heads/main/security/raspberry-pi-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/raspberry-pi-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.raspberrypi.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.raspberrypi.com/documentation/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.raspberrypi.com/documentation/computers/getting-started.html
- group: operate
  title: ''
  type: Support
  url: https://www.raspberrypi.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.raspberrypi.com/news/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/raspberrypi
created: '2026-10-13'
description: Raspberry Pi designs and manufactures affordable, low‑cost computers and accessories for education, hobbyists, and industry. Their products include the Raspberry Pi single‑board computers, Compute Modules, and accessories, supported by extensive documentation, software, and a global community. The company is based in the UK and focuses on open‑source hardware and software to enable accessible computing for a wide range of applications.
layout: provider
modified: '2026-10-13'
name: Raspberry Pi
nav: Providers
network: true
overview: 'Raspberry Pi is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Hardware, Education, Open Source, and Community.


  Raspberry Pi''s developer surface includes documentation, getting-started guide, support, engineering blog, and 9 more developer resources.'
random_paper: 16
score:
  band: emerging
  composite: 11.2
  coverage:
    artifact_dirs: 5
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Raspberry Pi Domain Security
  slug: raspberry-pi-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Raspberry Pi Vulnerability Disclosure
  slug: raspberry-pi-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: raspberry-pi
tags:
- Company
- Hardware
- Education
- Open Source
- Community
website: https://www.raspberrypi.com
---

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
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 3.6
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: BMAT provides a music operating system API for usage data aggregation and rights management.
  name: BMAT API
  slug: bmat-api
artifact_total: 3
common:
- group: auth
  title: ''
  type: Compliance
  url: https://trust.bmat.com/
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bmat/refs/heads/main/well-known/bmat-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bmat-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bmat/refs/heads/main/hosts/bmat-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bmat-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bmat/refs/heads/main/packages/bmat-packages.yml
  title: ''
  type: SDKs
  url: packages/bmat-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bmat/refs/heads/main/packages/bmat-packages.yml
  title: ''
  type: Packages
  url: packages/bmat-packages.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bmat.com/privacy-policy/
- group: company
  title: ''
  type: Newsroom
  url: https://www.bmat.com/press/
- group: other
  title: ''
  type: Leadership
  url: https://www.bmat.com/team/
- group: company
  title: ''
  type: Blog
  url: https://www.bmat.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bmat
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bmat/refs/heads/main/security/bmat-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bmat-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bmat/refs/heads/main/security/bmat-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bmat-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.bmat.com
coverage:
  checked: '2026-09-29'
  detail: The main site returns a JavaScript shell and no machine‑readable API spec was found.
  evidence:
  - status: 200
    url: https://www.bmat.com
  reason: js-rendered-docs
  state: unreadable
created: '2026-09-29'
description: BMAT Music Innovators provides a music operating system that aggregates and processes usage data across the music industry. Founded in Barcelona in 2006, BMAT offers solutions for DSP processing, VOD processing, UGC tracking, reporting, and rights management, enabling faster, data‑driven decisions for artists, labels, broadcasters, and AI companies. The platform connects every usage source, from radio to streaming, to deliver comprehensive analytics and revenue insights.
image: https://www.bmat.com/wp-content/uploads/2026/09/bmat-2026.jpg
layout: provider
modified: '2026-09-29'
name: Bmat
nav: Providers
network: true
overview: 'Bmat publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Data, Analytics, Rights Management, and Platform.


  Bmat''s developer surface includes engineering blog and 12 more developer resources.'
random_paper: 2
score:
  band: emerging
  composite: 13.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bmat Domain Security
  slug: bmat-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: trust-center
  name: Bmat Trust Center
  slug: bmat-trust-center
  summary_line: ISO 27001, GDPR
slug: bmat
tags:
- Music
- Data
- Analytics
- Rights Management
- Platform
website: https://www.bmat.com
---

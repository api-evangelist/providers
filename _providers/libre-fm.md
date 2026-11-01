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
    well_known_catalog: true
  schema_version: '0.2'
  score: 2.9
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Developer API providing access to user listening data and music metadata.
  name: Libre.fm API
  slug: libre-fm-api
artifact_total: 3
common:
- group: auth
  href: https://artifacts.apis.io/libre-fm/security/libre-fm-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/libre-fm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/libre-fm/well-known/libre-fm-turtle-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/libre-fm-turtle-security.txt
- group: auth
  href: https://artifacts.apis.io/libre-fm/well-known/libre-fm-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/libre-fm-security.txt
- group: auth
  href: https://artifacts.apis.io/libre-fm/well-known/libre-fm-blog-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/libre-fm-blog-security.txt
- group: agent
  href: https://artifacts.apis.io/libre-fm/well-known/libre-fm-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/libre-fm-well-known.yml
- group: other
  href: https://artifacts.apis.io/libre-fm/hosts/libre-fm-hosts.yml
  title: ''
  type: Hosts
  url: hosts/libre-fm-hosts.yml
- group: other
  href: https://artifacts.apis.io/libre-fm/vendors/libre-fm-vendors.yml
  title: ''
  type: Vendors
  url: vendors/libre-fm-vendors.yml
- group: start
  title: ''
  type: SignUp
  url: https://libre.fm/register.php
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/libre-fm
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.github.com/en/github-cli/github-cli/quickstart
- group: auth
  href: https://artifacts.apis.io/libre-fm/security/libre-fm-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/libre-fm-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/libre-fm/security/libre-fm-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/libre-fm-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://libre.fm/
- group: company
  title: ''
  type: Blog
  url: https://blog.libre.fm/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.libre.fm
- group: operate
  title: ''
  type: Support
  url: https://libre.fm/help/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://libre.fm/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://libre.fm/privacy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.libre.fm/
coverage:
  checked: '2026-10-28'
  detail: Developer documentation redirects to GitHub without providing an OpenAPI or other machine‑readable contract.
  evidence:
  - status: 301
    url: https://developer.libre.fm
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Libre.fm is an open source music community that lets users track their listening habits across various music players and services. Since 2009, it has recorded hundreds of millions of listens from over 390,000 users, offering public profiles, community charts, and the ability to run a self‑hosted instance. The service integrates with many clients via scrobbling and provides APIs for developers to access user listening data and music metadata.
image: https://libre.fm/themes/2024-end-times/social.png
layout: provider
modified: '2026-10-28'
name: Libre.fm
nav: Providers
network: true
overview: 'Libre.fm is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Open-Source, Scrobbling, and Community.


  Libre.fm''s developer surface includes signup flow, getting-started guide, engineering blog, documentation, support, and 14 more developer resources.'
random_paper: 14
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 5
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 34.2
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 28.6
    discoverability: 57.1
    operational_transparency: 31.6
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 19.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Libre Fm Domain Security
  slug: libre-fm-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Libre Fm Vulnerability Disclosure
  slug: libre-fm-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: libre-fm
tags:
- Company
- Music
- Open-Source
- Scrobbling
- Community
website: https://libre.fm/
---

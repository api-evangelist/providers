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
  score: 13.9
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 2
common:
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.amazon.com/frustration-free-setup
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/amazonvrp
- group: design
  href: https://artifacts.apis.io/amazon-music/conformance/amazon-music-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-music-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amazon-music/llms/amazon-music-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-music-llms.txt
- group: auth
  href: https://artifacts.apis.io/amazon-music/well-known/amazon-music-aws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-music-aws-security.txt
- group: auth
  href: https://artifacts.apis.io/amazon-music/well-known/amazon-music-amazon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-music-amazon-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-music/well-known/amazon-music-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-music-well-known.yml
- group: other
  href: https://artifacts.apis.io/amazon-music/hosts/amazon-music-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-music-hosts.yml
- group: other
  href: https://artifacts.apis.io/amazon-music/vendors/amazon-music-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-music-vendors.yml
- group: build
  href: https://artifacts.apis.io/amazon-music/packages/amazon-music-packages.yml
  title: ''
  type: SDKs
  url: packages/amazon-music-packages.yml
- group: build
  href: https://artifacts.apis.io/amazon-music/packages/amazon-music-packages.yml
  title: ''
  type: Packages
  url: packages/amazon-music-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/terms-and-agreements
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmazonAppDev
- group: auth
  href: https://artifacts.apis.io/amazon-music/security/amazon-music-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-music-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-music/security/amazon-music-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-music-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://music.amazon.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.amazon.com/docs/music/landing_home.html
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.amazon.com/en
- group: operate
  title: ''
  type: Support
  url: https://developer.amazon.com/en/support
- group: company
  title: ''
  type: Blog
  url: https://developer.amazon.com/blogs
created: '2026-10-26'
description: Amazon Music is a streaming service offering on-demand music, playlists, and podcasts. It integrates with Amazon devices and provides a catalog of millions of songs, personalized stations, and offline listening. The service is part of Amazon’s ecosystem, available via web, mobile apps, and Alexa-enabled devices, and supports subscription tiers for ad‑free listening and high‑fidelity audio.
layout: provider
modified: '2026-10-26'
name: Amazon Music
nav: Providers
network: true
overview: 'Amazon Music is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Music, Streaming, Audio, and Amazon.


  Amazon Music''s developer surface includes getting-started guide, documentation, support, engineering blog, and 16 more developer resources.'
random_paper: 12
score:
  band: emerging
  composite: 21.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 44.6
    operational_transparency: 15.8
  provenance:
    conformance: first-party
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Amazon Music Domain Security
  slug: amazon-music-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Music Vulnerability Disclosure
  slug: amazon-music-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-music
tags:
- Company
- Music
- Streaming
- Audio
- Amazon
website: https://music.amazon.com/
---

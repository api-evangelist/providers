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
api_count: 1
apis:
- description: Spinitron provides a web-based music playlist management platform for radio stations and music businesses.
  name: Spinitron API
  slug: spinitron-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/spinitron/refs/heads/main/llms/spinitron-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/spinitron-llms.txt
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/spinitron/refs/heads/main/hosts/spinitron-hosts.yml
  title: ''
  type: Hosts
  url: hosts/spinitron-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/spinitron/refs/heads/main/packages/spinitron-packages.yml
  title: ''
  type: SDKs
  url: packages/spinitron-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/spinitron/refs/heads/main/packages/spinitron-packages.yml
  title: ''
  type: Packages
  url: packages/spinitron-packages.yml
- group: start
  title: ''
  type: Login
  url: https://spinitron.com/m/site/login
- group: company
  title: ''
  type: Blog
  url: https://blog.spinitron.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/spinitron
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/spinitron/refs/heads/main/security/spinitron-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/spinitron-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://spinitron.com/
- group: docs
  title: ''
  type: Documentation
  url: https://spinitron.com/m/about
- group: start
  title: ''
  type: GettingStarted
  url: https://spinitron.com/m/about
- group: operate
  title: ''
  type: Support
  url: https://spinitron.com/m/about/contact
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://forum.spinitron.com/t/privacy-policy/6
coverage:
  checked: '2026-10-12'
  detail: Spinitron's website provides no developer program or API documentation.
  evidence:
  - status: 200
    url: https://spinitron.com/
  reason: no-developer-program
  state: none
created: '2026-10-12'
description: Spinitron provides a web-based music playlist management platform for radio stations and music businesses. It offers tools for scheduling, charting, and audience engagement, supporting both community and commercial broadcasters. The service includes features such as automated playlists, detailed analytics, and integration with various streaming services, helping stations curate and manage their music content efficiently.
layout: provider
modified: '2026-10-12'
name: Spinitron
nav: Providers
network: true
overview: 'Spinitron is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Radio, Playlist, Community, and Broadcasting.


  Spinitron''s developer surface includes engineering blog, documentation, getting-started guide, support, and 9 more developer resources.'
random_paper: 8
score:
  band: emerging
  composite: 17.8
  coverage:
    artifact_dirs: 8
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 23.7
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 35.7
    discoverability: 60.7
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Spinitron Domain Security
  slug: spinitron-domain-security
  summary_line: TLSv1.3 · DMARC
slug: spinitron
tags:
- Music
- Radio
- Playlist
- Community
- Broadcasting
website: https://spinitron.com/
---

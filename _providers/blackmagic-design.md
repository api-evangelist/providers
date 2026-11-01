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
api_count: 0
artifact_total: 1
common:
- group: operate
  href: https://artifacts.apis.io/blackmagic-design/changelog/blackmagic-design-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/blackmagic-design-changelog.yml
- group: agent
  href: https://artifacts.apis.io/blackmagic-design/llms/blackmagic-design-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/blackmagic-design-llms.txt
- group: other
  href: https://artifacts.apis.io/blackmagic-design/hosts/blackmagic-design-hosts.yml
  title: ''
  type: Hosts
  url: hosts/blackmagic-design-hosts.yml
- group: operate
  title: ''
  type: Support
  url: https://www.blackmagicdesign.com/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.blackmagicdesign.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://www.blackmagicdesign.com/media
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.blackmagicdesign.com/developer
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/blackmagicdesign
- group: auth
  href: https://artifacts.apis.io/blackmagic-design/security/blackmagic-design-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/blackmagic-design-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://blackmagicdesign.com/
coverage:
  checked: '2026-10-28'
  detail: Developer portal provides SDK information but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.blackmagicdesign.com/developer
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Blackmagic Design is a global leader in professional video, broadcast, and cinema technology, offering a broad range of products including cameras, switchers, routers, and the DaVinci Resolve software suite for editing, color correction, visual effects, and audio post-production. The company provides extensive developer resources, APIs, and SDKs for integrating hardware and software solutions, supporting workflows from live production to post-production. Their website hosts documentation, developer portals, support resources, and product information for creators and engineers worldwide.
layout: provider
modified: '2026-10-28'
name: DaVinci Resolve
nav: Providers
network: true
overview: 'DaVinci Resolve is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Video, Broadcast, Cinema, Software, and Hardware.


  DaVinci Resolve''s developer surface includes changelog, support, and 8 more developer resources.'
random_paper: 21
score:
  band: emerging
  composite: 11.5
  coverage:
    artifact_dirs: 8
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 14.3
    discoverability: 46.4
    operational_transparency: 21.1
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 9.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Blackmagic Design Domain Security
  slug: blackmagic-design-domain-security
  summary_line: TLSv1.3 · DMARC
slug: blackmagic-design
tags:
- Video
- Broadcast
- Cinema
- Software
- Hardware
- Company
website: https://blackmagicdesign.com/
---

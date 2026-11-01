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
  score: 14.4
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 1
common:
- group: agent
  href: https://artifacts.apis.io/guruwalk-com/well-known/guruwalk-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/guruwalk-com-well-known.yml
- group: agent
  href: https://artifacts.apis.io/guruwalk-com/llms/guruwalk-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/guruwalk-com-llms.txt
- group: other
  href: https://artifacts.apis.io/guruwalk-com/hosts/guruwalk-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/guruwalk-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/guruwalk-com/vendors/guruwalk-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/guruwalk-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.guruwalk.com/terms/terms_policy
- group: operate
  title: ''
  type: Support
  url: https://support.guruwalk.com/portal/es/kb
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.guruwalk.com/terms/privacy_policy
- group: company
  title: ''
  type: Newsroom
  url: https://www.guruwalk.com/news/global_travellers_map
- group: company
  title: ''
  type: Blog
  url: https://blog.guruwalk.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/guruwalk
- group: auth
  href: https://artifacts.apis.io/guruwalk-com/security/guruwalk-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/guruwalk-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://guruwalk.com/
coverage:
  checked: '2026-10-30'
  detail: No OpenAPI, GraphQL, AsyncAPI, or gRPC specifications were found after probing the known hosts.
  evidence:
  - status: 404
    url: https://www.guruwalk.com/openapi.json
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: GuruWalk is a platform that lets travelers discover and book free tours and activities guided by locals in hundreds of destinations worldwide. Users can compare options, read reviews, and plan their trips, accessing the world’s best free tours and activities all in one place. The service emphasizes community-driven experiences and aims to make travel more authentic and affordable.
image: https://www.guruwalk.com/_next/static/immutable/media/guruwalk.26vx3czz-zkdw.webp
layout: provider
modified: '2026-10-30'
name: guruwalk-com
nav: Providers
network: true
overview: 'guruwalk-com is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Travel, Tours, Free, Local Guides, and Activities.


  guruwalk-com''s developer surface includes support, engineering blog, and 10 more developer resources.'
random_paper: 22
score:
  band: emerging
  composite: 12.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    operational_transparency: 5.3
  provenance:
    mcp: derived
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
  name: Guruwalk Com Domain Security
  slug: guruwalk-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: guruwalk-com
tags:
- Travel
- Tours
- Free
- Local Guides
- Activities
website: https://guruwalk.com/
---

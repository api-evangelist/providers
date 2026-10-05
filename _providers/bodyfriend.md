---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: platform
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
  score: 4.5
  scored_at: '2026-10-04'
api_count: 1
apis:
- description: GraphQL API providing access to Bodyfriend data and operations.
  name: Bodyfriend GraphQL API
  slug: bodyfriend-graphql-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bodyfriend/refs/heads/main/llms/bodyfriend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bodyfriend-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bodyfriend/refs/heads/main/well-known/bodyfriend-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bodyfriend-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bodyfriend/refs/heads/main/hosts/bodyfriend-hosts.yml
  title: ''
  type: Hosts
  url: hosts/bodyfriend-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bodyfriend/refs/heads/main/vendors/bodyfriend-vendors.yml
  title: ''
  type: Vendors
  url: vendors/bodyfriend-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://bodyfriend.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://bodyfriend.com/blogs/news
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bodyfriend/refs/heads/main/security/bodyfriend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bodyfriend-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://bodyfriend.com
coverage:
  checked: '2026-10-02'
  detail: GraphQL endpoint returned a schema unrelated to Bodyfriend, so no owned machine-readable contract was found.
  evidence:
  - status: 200
    url: https://bodyfriend.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-02'
description: Bodyfriend is a digital technology healthcare company specializing in premium 4D full-body massage chairs and wellness products. Their patented ROVO bipedal technology offers therapeutic stretching, mobility support, and relaxation, aiming to extend users’ lives by ten years through healthy living practices. The brand combines advanced engineering, medical expertise, and elegant design to deliver home wellness solutions.
image: http://bodyfriend.com/cdn/shop/files/1_4a6865c6-dd51-4b8f-95b8-1d7668490e05.png?v=1725418895&width=2048
layout: provider
modified: '2026-10-02'
name: Bodyfriend
nav: Providers
network: true
overview: Bodyfriend publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Massage Chairs, Home Wellness, Rehabilitation, and Health Tech.
random_paper: 6
score:
  band: minimal
  composite: 8.0
  coverage:
    artifact_dirs: 8
    catalog_earned: 32.0
    catalog_earned_first_party: 0.0
    catalog_gap: 83.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 66.1
    operational_transparency: 0.0
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.8
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Bodyfriend Domain Security
  slug: bodyfriend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: bodyfriend
tags:
- Massage Chairs
- Home Wellness
- Rehabilitation
- Health Tech
website: https://bodyfriend.com
---

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
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 4.5
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: API discovered via GraphQL endpoint at https://gimmemetal.com/api/graphql; no machine-readable spec available.
  name: Gimme Media API
  slug: gimme-media-api
artifact_total: 4
common:
- group: agent
  href: https://artifacts.apis.io/gimmeradio-com/llms/gimmeradio-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/gimmeradio-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/gimmeradio-com/well-known/gimmeradio-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/gimmeradio-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/gimmeradio-com/hosts/gimmeradio-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/gimmeradio-com-hosts.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://gimmemetal.com/policies/terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://gimmemetal.com/policies/privacy-policy
- group: company
  title: ''
  type: Newsroom
  url: https://gimmemetal.com/blogs/news/gimme-s-community-lives-on
- group: company
  title: ''
  type: Blog
  url: https://gimmemetal.com/pages/blog
- group: auth
  href: https://artifacts.apis.io/gimmeradio-com/security/gimmeradio-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/gimmeradio-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://gimmeradio.com/
coverage:
  checked: '2026-10-29'
  detail: GraphQL endpoint exists at https://gimmemetal.com/api/graphql but no schema document is published.
  evidence:
  - status: 200
    url: https://gimmemetal.com/api/graphql
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: 'Gimme Media is a company surfaced via the API Evangelist harvest backlog (source: vc-portfolio; backed by techstars) and added to the network as a stub for full-pipeline profiling.'
image: https://cdn.shopify.com/s/files/1/2151/5265/files/GM-LOGO.png?v=1723044054
layout: provider
modified: '2026-10-29'
name: Gimme Media
nav: Providers
network: true
overview: 'Gimme Media is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Vinyl, Metal Music, Collections, Vinyl Club, and Bundles.


  Gimme Media''s developer surface includes engineering blog and 8 more developer resources.'
random_paper: 2
scopes:
- name: Gimmeradio Com Scopes
  scope_count: 0
  slug: gimmeradio-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 11.0
  coverage:
    artifact_dirs: 19
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 2.4
    discoverability: 50.0
    operational_transparency: 0.0
  provenance:
    conformance: unknown
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 23.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Gimmeradio Com Authentication
  slug: gimmeradio-com-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Gimmeradio Com Domain Security
  slug: gimmeradio-com-domain-security
  summary_line: TLSv1.3
slug: gimmeradio-com
tags:
- Vinyl
- Metal Music
- Collections
- Vinyl Club
- Bundles
website: https://gimmeradio.com/
---

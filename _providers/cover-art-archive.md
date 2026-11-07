---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-11-06'
api_count: 0
artifact_total: 1
common:
- group: other
  href: https://artifacts.apis.io/cover-art-archive/hosts/cover-art-archive-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cover-art-archive-hosts.yml
- group: build
  href: https://artifacts.apis.io/cover-art-archive/packages/cover-art-archive-packages.yml
  title: ''
  type: SDKs
  url: packages/cover-art-archive-packages.yml
- group: build
  href: https://artifacts.apis.io/cover-art-archive/packages/cover-art-archive-packages.yml
  title: ''
  type: Packages
  url: packages/cover-art-archive-packages.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://musicbrainz.org/doc/MusicBrainz_Server/Setup
- group: auth
  href: https://artifacts.apis.io/cover-art-archive/security/cover-art-archive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cover-art-archive-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://coverartarchive.org/
- group: docs
  title: ''
  type: Documentation
  url: https://musicbrainz.org/doc/Cover_Art_Archive/API
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/lastfm/coverartarchive-api
coverage:
  checked: '2026-10-28'
  detail: Documentation is provided as HTML without a machine‑readable OpenAPI, GraphQL, or other contract.
  evidence:
  - status: 200
    url: https://musicbrainz.org/doc/Cover_Art_Archive/API
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Cover Art Archive provides a free, open database of cover art images for music releases, sourced from the MusicBrainz community. It offers a public API that allows developers to retrieve cover art by release or release-group identifiers, supporting JSON and image formats. The service is community‑maintained, aims to enrich music metadata applications, and operates under an open‑source license.
layout: provider
modified: '2026-10-28'
name: Cover Art Archive
nav: Providers
network: true
overview: 'Cover Art Archive is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Music, Open Data, Community, and CoverArt.


  Cover Art Archive''s developer surface includes getting-started guide, documentation, and 6 more developer resources.'
random_paper: 18
score:
  band: minimal
  composite: 6.7
  coverage:
    artifact_dirs: 8
    catalog_earned: 20.0
    catalog_earned_first_party: 0.0
    catalog_gap: 95.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -2.8
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 17.9
    discoverability: 35.7
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 9.5
  provenance:
    mcp: unknown
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 5.9
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/cover-art-archive/cover-art-archive-2026-11-03T125444.png
security:
- kind: domain-security
  name: Cover Art Archive Domain Security
  slug: cover-art-archive-domain-security
  summary_line: TLSv1.3
slug: cover-art-archive
tags:
- Music
- Open Data
- Community
- CoverArt
website: https://coverartarchive.org/
---

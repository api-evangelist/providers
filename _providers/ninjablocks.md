---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-09-25'
api_count: 1
apis:
- description: Historical RESTful API for the Ninja Blocks IoT platform, used to read device/sensor data and actuate devices. No longer operational; documented here from surviving first-party client libraries.
  name: Ninja Blocks REST API
  slug: ninja-blocks-rest-api
artifact_total: 1
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/ninjablocks/node-ninja-blocks/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/ninjablocks/node-ninja-blocks/blob/master/LICENSE
- group: company
  title: ''
  type: Website
  url: https://ninjablocks.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ninjablocks
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/ninjablocks
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ninjablocks/refs/heads/main/packages/ninjablocks-packages.yml
  title: ''
  type: SDKs
  url: packages/ninjablocks-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ninjablocks/refs/heads/main/packages/ninjablocks-packages.yml
  title: ''
  type: Packages
  url: packages/ninjablocks-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ninjablocks/refs/heads/main/cli/ninjablocks-cli.yml
  title: ''
  type: CLI
  url: cli/ninjablocks-cli.yml
created: '2026-07-17'
description: Ninja Blocks Inc was an Australian Internet-of-Things startup (founded 2012, backed by 500 Global / 500 Startups) behind the Ninja Block and Ninja Sphere home-automation hubs. It offered a cloud-connected platform with a RESTful API (base https://api.ninja.is/rest/v0/) for reading sensor data and controlling actuators, plus first-party client libraries for Node.js, PHP, Ruby, Lua and Arduino, a `ninja-toolbelt` CLI, and OAuth-based authentication. The company ceased operation and its web and API hosts are no longer online; this profile preserves the surviving first-party open-source client libraries and API tooling published to npm and GitHub. Added to the API Evangelist network from the 500 Global portfolio and enriched from public package registries and the github.com/ninjablocks organization.
image: https://avatars.githubusercontent.com/u/1387630?v=4
layout: provider
modified: '2026-07-20'
name: NinjaBlocks
nav: Providers
network: true
overview: 'NinjaBlocks publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, IoT, Home Automation, Smart Home, and Sensors.


  NinjaBlocks'' developer surface includes CLI and 7 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 0.0
  coverage:
    artifact_dirs: 4
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 0.0
    operational_transparency: 0.0
  lifecycle: defunct
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.23.0
  scored_at: '2026-09-25'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/ninjablocks/refs/heads/main/screenshots/ninjablocks-2026-08-07T185322.png
slug: ninjablocks
tags:
- Company
- IoT
- Home Automation
- Smart Home
- Sensors
- Hardware
- REST API
- Defunct
website: https://ninjablocks.com
---

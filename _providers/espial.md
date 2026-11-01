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
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-31'
api_count: 0
artifact_total: 0
common:
- group: other
  href: https://artifacts.apis.io/espial/hosts/espial-hosts.yml
  title: ''
  type: Hosts
  url: hosts/espial-hosts.yml
- group: other
  href: https://artifacts.apis.io/espial/vendors/espial-vendors.yml
  title: ''
  type: Vendors
  url: vendors/espial-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/jonschoning/espial
- group: docs
  title: ''
  type: Documentation
  url: https://github.com/jonschoning/espial#readme
- group: docs
  title: ''
  type: APIReference
  url: https://github.com/jonschoning/espial/blob/master/README.md
coverage:
  checked: '2026-10-28'
  detail: The provider's website and product pages contain only HTML documentation with no machine‑readable API specifications.
  evidence:
  - status: 200
    url: https://www.espial.com
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Espial is an open-source, web-based bookmarking server that supports multiple user accounts and self‑hosted deployments. Bookmarks are stored in a SQLite database for simple setup and maintenance, and the platform includes internationalization support. The project provides a Docker‑based quick‑start, a CLI, and a REST API for programmatic bookmark management.
layout: provider
modified: '2026-10-28'
name: Espial
nav: Providers
network: true
overview: 'Espial is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Bookmarking, OpenSource, Haskell, and Docker.


  Espial''s developer surface includes documentation, API reference, and 3 more developer resources.'
random_paper: 14
score:
  band: minimal
  composite: 5.5
  coverage:
    artifact_dirs: 4
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 44.6
    operational_transparency: 0.0
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 0.0
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: espial
tags:
- Company
- Bookmarking
- OpenSource
- Haskell
- Docker
---

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
- description: 'Self-hosted HTTP server (python -m kev.serve, default 127.0.0.1:8009). Documented paths in the README: POST /v1/systemone, GET /v1/models, POST /v1/systemone/permute, POST /v1/systemone/separate. Opti'
  name: Kev System One API (self-hosted)
  slug: kev-systemone-api
artifact_total: 1
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kev/refs/heads/main/hosts/kev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/kev-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/kev/refs/heads/main/vendors/kev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/kev-vendors.yml
- group: company
  title: ''
  type: Website
  url: https://github.com/jaredpalmer/kev
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/jaredpalmer/kev
- group: commercial
  title: ''
  type: License
  url: https://github.com/jaredpalmer/kev/blob/main/LICENSE
- group: start
  title: ''
  type: Demo
  url: https://huggingface.co/spaces/jaredpalmer/kev
- group: other
  title: ''
  type: Models
  url: https://huggingface.co/collections/jaredpalmer/kev-6aad9d0ea49f2589665e07cd
- group: other
  title: ''
  type: Datasets
  url: https://huggingface.co/datasets/jaredpalmer/kev-suites
created: '2026-10-13'
description: Kev is an open-source (Apache-2.0) family of small decision models built on Qwen3.5/Qwen3.8 by Jared Palmer, released on GitHub and Hugging Face. Its self-hosted server exposes an HTTP API that, per the README, "matches TypeSafe's System One" (POST /v1/systemone with noul, choice and score questions). Not a Cognition product. No OpenAPI or JSON Schema file is published in the repository.
layout: provider
modified: '2026-10-13'
name: Kev
nav: Providers
network: true
overview: Kev is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Artificial Intelligence, Decision Models, Open Source, and Self-Hosted.
random_paper: 18
score:
  band: minimal
  composite: 5.7
  coverage:
    artifact_dirs: 5
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 9.5
    discoverability: 53.6
    operational_transparency: 5.3
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
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: kev
tags:
- Company
- Artificial Intelligence
- Decision Models
- Open Source
- Self-Hosted
---

---
agent_readiness:
  band: agent-aware
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
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 12.9
  scored_at: '2026-09-21'
api_count: 1
apis:
- description: 'Miniflux API as documented publicly: 42 operations. Contract generated from the documentation by API Evangelist (2026-09-21); not the provider''s own document.'
  name: Miniflux API
  slug: miniflux-api
artifact_total: 2
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/mcp/miniflux-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/miniflux-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/packages/miniflux-packages.yml
  title: ''
  type: SDKs
  url: packages/miniflux-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/packages/miniflux-packages.yml
  title: ''
  type: Packages
  url: packages/miniflux-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/security/miniflux-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/miniflux-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://miniflux.app/
- group: docs
  title: ''
  type: Documentation
  url: https://miniflux.app/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://miniflux.app/docs/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://miniflux.app/docs/installation.html
- group: operate
  title: ''
  type: Support
  url: https://github.com/miniflux/v2/issues
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/miniflux
created: '2026-09-21'
description: Miniflux is an open-source minimalist feed reader focused on simplicity and privacy. It provides a clean web interface, supports self‑hosting via binary, Docker, or packages, and offers a RESTful API for managing feeds, entries, categories, and users. The project emphasizes readability, low resource usage, and no telemetry, making it suitable for personal and small‑team use.
layout: provider
modified: '2026-09-21'
name: Miniflux
nav: Providers
network: true
overview: 'Miniflux publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Feed Reader, Open-Source, Self-Hosted, Minimalist, and Privacy.


  Miniflux''s developer surface includes documentation, API reference, getting-started guide, support, and 6 more developer resources.'
random_paper: 18
score:
  band: emerging
  composite: 18.6
  coverage:
    artifact_dirs: 6
    catalog_earned: 30.0
    catalog_earned_first_party: 0.0
    catalog_gap: 85.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 8.7
    developer_ergonomics: 40.5
    discoverability: 55.6
    operational_transparency: 5.3
  provenance:
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-21'
  upsert:
    applies: true
    score: 27.8
security:
- kind: domain-security
  name: Miniflux Domain Security
  slug: miniflux-domain-security
  summary_line: TLSv1.3 · DMARC
slug: miniflux
tags:
- Feed Reader
- Open-Source
- Self-Hosted
- Minimalist
- Privacy
website: https://miniflux.app/
---

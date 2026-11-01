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
- group: other
  href: https://artifacts.apis.io/triliumnotes/hosts/triliumnotes-hosts.yml
  title: ''
  type: Hosts
  url: hosts/triliumnotes-hosts.yml
- group: other
  href: https://artifacts.apis.io/triliumnotes/vendors/triliumnotes-vendors.yml
  title: ''
  type: Vendors
  url: vendors/triliumnotes-vendors.yml
- group: build
  href: https://artifacts.apis.io/triliumnotes/packages/triliumnotes-packages.yml
  title: ''
  type: SDKs
  url: packages/triliumnotes-packages.yml
- group: build
  href: https://artifacts.apis.io/triliumnotes/packages/triliumnotes-packages.yml
  title: ''
  type: Packages
  url: packages/triliumnotes-packages.yml
- group: auth
  href: https://artifacts.apis.io/triliumnotes/security/triliumnotes-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/triliumnotes-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://triliumnotes.org/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.triliumnotes.org/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.triliumnotes.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://triliumnotes.org/en/get-started
- group: operate
  title: ''
  type: Support
  url: https://triliumnotes.org/en/support-us
- group: company
  title: ''
  type: Blog
  url: https://triliumnotes.org/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://triliumnotes.org/en/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/TriliumNext
coverage:
  checked: '2026-10-28'
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://docs.triliumnotes.org/user-guide/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Trilium Notes is an open-source hierarchical note‑taking application that lets users organize personal knowledge bases with rich text, code, markdown, diagrams, and more. It offers self‑hosted and cloud sync options, supports multi‑language UI, and provides a REST API for automation and integration.
layout: provider
modified: '2026-10-28'
name: Trilium Notes
nav: Providers
network: true
overview: 'Trilium Notes is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Note-taking, Open-source, Knowledge-base, Hierarchical, and REST API.


  Trilium Notes'' developer surface includes documentation, API reference, getting-started guide, support, engineering blog, pricing, and 7 more developer resources.'
random_paper: 7
score:
  band: emerging
  composite: 14.4
  coverage:
    artifact_dirs: 7
    catalog_earned: 25.0
    catalog_earned_first_party: 0.0
    catalog_gap: 90.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 10.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 42.9
    discoverability: 44.6
    operational_transparency: 5.3
  provenance:
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 5.9
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Triliumnotes Domain Security
  slug: triliumnotes-domain-security
  summary_line: TLSv1.3
slug: triliumnotes
tags:
- Note-taking
- Open-source
- Knowledge-base
- Hierarchical
- REST API
website: https://triliumnotes.org/
---

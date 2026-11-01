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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.4
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Betula provides a bookmark management API documented at https://joinbetula.org/installation.html. No machine‑readable contract (OpenAPI, AsyncAPI, GraphQL) was found.
  name: Betula API
  slug: betula-api-2
- baseURL: https://hub.docker.com
  baseurl_source: declared
  description: 'Betula API as documented publicly: 137 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Betula API
  slug: betula-api
artifact_total: 4
common:
- group: design
  href: https://artifacts.apis.io/betula/rules/betula-rules.yml
  title: ''
  type: Spectral
  url: rules/betula-rules.yml
- group: design
  href: https://artifacts.apis.io/betula/vocabulary/betula-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/betula-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/betula/conformance/betula-conformance.yml
  title: ''
  type: Conformance
  url: conformance/betula-conformance.yml
- group: auth
  href: https://artifacts.apis.io/betula/well-known/betula-codeberg-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/betula-codeberg-security.txt
- group: agent
  href: https://artifacts.apis.io/betula/well-known/betula-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/betula-well-known.yml
- group: other
  href: https://artifacts.apis.io/betula/hosts/betula-hosts.yml
  title: ''
  type: Hosts
  url: hosts/betula-hosts.yml
- group: other
  href: https://artifacts.apis.io/betula/vendors/betula-vendors.yml
  title: ''
  type: Vendors
  url: vendors/betula-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://joinbetula.org/media/betula-v1.9.0.png
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.codeberg.org/getting-started/
- group: auth
  href: https://artifacts.apis.io/betula/security/betula-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/betula-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinbetula.org/
- group: docs
  title: ''
  type: Documentation
  url: https://joinbetula.org/installation.html
- group: docs
  title: ''
  type: Documentation
  url: https://joinbetula.org/building.html
- group: docs
  title: ''
  type: Documentation
  url: https://joinbetula.org/https-domain.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bouncepaw/betula
- group: build
  title: ''
  type: CodeRepository
  url: https://codeberg.org/bouncepaw/betula
- group: other
  title: ''
  type: DockerHub
  url: https://hub.docker.com/r/bouncepaw/betula/tags
coverage:
  checked: '2026-10-28'
  detail: The provider's documentation at https://joinbetula.org/ contains only HTML pages with no machine‑readable OpenAPI, AsyncAPI, GraphQL or other contract.
  evidence:
  - status: 200
    url: https://joinbetula.org/
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: Betula is a free self‑hosted single‑user federated bookmark manager for the independent web, offering archival support. It lets users organize bookmarks, maintain a linklog, and create personal web archives with Mycomarkup formatting, tag management, and privacy controls for public or private sharing.
layout: provider
modified: '2026-10-28'
name: Betula
nav: Providers
network: true
overview: 'Betula is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Bookmark Manager, Federated, Open Source, Self-hosted, and Independent Web.


  The Betula catalog on APIs.io includes 1 Spectral governance ruleset.


  Betula''s developer surface includes getting-started guide, documentation, and 15 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Betula API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: betula-rules
score:
  band: emerging
  composite: 17.6
  coverage:
    artifact_dirs: 10
    catalog_earned: 35.8
    catalog_earned_first_party: 0.0
    catalog_gap: 79.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 11.3
    developer_ergonomics: 21.4
    discoverability: 55.4
    operational_transparency: 15.8
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 28
      marker_coverage: 100.0
      total: 28
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Betula Domain Security
  slug: betula-domain-security
  summary_line: TLSv1.3
slug: betula
tags:
- Bookmark Manager
- Federated
- Open Source
- Self-hosted
- Independent Web
- Company
website: https://joinbetula.org/
---

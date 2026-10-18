---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 39.2
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Zincsearch Agentic Access
  operation_count: 48
  slug: zincsearch-agentic-access
  summary_line: 48 operations · 28 acting
api_count: 3
apis:
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Document API from ZincSearch — 7 operation(s) for document.
  name: ZincSearch Document API
  slug: zincsearch-document-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Healthz API from ZincSearch — 1 operation(s) for healthz.
  name: ZincSearch Healthz API
  slug: zincsearch-healthz-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Index API from ZincSearch — 14 operation(s) for index.
  name: ZincSearch Index API
  slug: zincsearch-index-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Permission API from ZincSearch — 1 operation(s) for permission.
  name: ZincSearch Permission API
  slug: zincsearch-permission-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Role API from ZincSearch — 2 operation(s) for role.
  name: ZincSearch Role API
  slug: zincsearch-role-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Search API from ZincSearch — 4 operation(s) for search.
  name: ZincSearch Search API
  slug: zincsearch-search-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The User API from ZincSearch — 4 operation(s) for user.
  name: ZincSearch User API
  slug: zincsearch-user-api
- baseURL: http://localhost:4080
  baseurl_source: declared
  description: The Version API from ZincSearch — 1 operation(s) for version.
  name: ZincSearch Version API
  slug: zincsearch-version-api
artifact_total: 12
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/agentic-access/zincsearch-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/zincsearch-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/rules/zincsearch-rules.yml
  title: ''
  type: Spectral
  url: rules/zincsearch-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/vocabulary/zincsearch-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/zincsearch-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/data-model/zincsearch-data-model.yml
  title: ''
  type: DataModel
  url: data-model/zincsearch-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/errors/zincsearch-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/zincsearch-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/conformance/zincsearch-conformance.yml
  title: ''
  type: Conformance
  url: conformance/zincsearch-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/llms/zincsearch-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/zincsearch-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/well-known/zincsearch-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/zincsearch-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/hosts/zincsearch-hosts.yml
  title: ''
  type: Hosts
  url: hosts/zincsearch-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/vendors/zincsearch-vendors.yml
  title: ''
  type: Vendors
  url: vendors/zincsearch-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/packages/zincsearch-packages.yml
  title: ''
  type: SDKs
  url: packages/zincsearch-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/packages/zincsearch-packages.yml
  title: ''
  type: Packages
  url: packages/zincsearch-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/authentication/zincsearch-authentication.yml
  title: ''
  type: Authentication
  url: authentication/zincsearch-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/zincsearch/refs/heads/main/security/zincsearch-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/zincsearch-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://zincsearch.com
- group: docs
  title: ''
  type: Documentation
  url: https://zincsearch-docs.zinc.dev/
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/zincsearch/zincsearch
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zincsearch
created: '2026-10-13'
description: ZincSearch is an open source, self-hosted, lightweight full-text search engine written in Go (Apache 2.0) with an Elasticsearch-compatible ingestion and search API, built by Zinc Labs. The company now develops OpenObserve as its successor, and zincsearch.com redirects to openobserve.ai.
image: https://openobserve.ai/o2-seo-image.png
layout: provider
modified: '2026-10-14'
name: ZincSearch
nav: Providers
network: true
overview: 'ZincSearch publishes 8 API contracts indexed on the [APIs.io](https://apis.io/) network, including Document API, Healthz API, Index API, and 5 more. Tagged areas include Company, Search, Full-Text Search, Open Source, and Self-Hosted.


  The ZincSearch catalog on APIs.io includes 1 Spectral governance ruleset.


  ZincSearch''s developer surface includes authentication, documentation, and 16 more developer resources.'
random_paper: 10
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: ZincSearch API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: zincsearch-rules
score:
  band: thin
  composite: 29.4
  coverage:
    artifact_dirs: 16
    catalog_earned: 40.8
    catalog_earned_first_party: 0.0
    catalog_gap: 74.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 40.9
    developer_ergonomics: 35.7
    discoverability: 69.6
    operational_transparency: 5.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 8
    mcp: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Zincsearch Authentication
  slug: zincsearch-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Zincsearch Domain Security
  slug: zincsearch-domain-security
  summary_line: TLSv1.3 · HSTS
slug: zincsearch
tags:
- Company
- Search
- Full-Text Search
- Open Source
- Self-Hosted
- Elasticsearch Compatible
website: https://zincsearch.com
---

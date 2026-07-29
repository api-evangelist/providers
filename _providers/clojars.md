---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.8
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Clojars Agentic Access
  operation_count: 9
  slug: clojars-agentic-access
  summary_line: 9 operations
api_count: 5
apis:
- description: Operations related to Clojars artifacts and releases
  name: Clojars Artifacts API
  slug: clojars-artifacts-api
- description: Release feed and bulk data operations
  name: Clojars Feeds API
  slug: clojars-feeds-api
- description: Operations related to Clojars artifact groups
  name: Clojars Groups API
  slug: clojars-groups-api
- description: Search operations across the Clojars artifact index
  name: Clojars Search API
  slug: clojars-search-api
- description: Operations related to Clojars user profiles and group memberships
  name: Clojars Users API
  slug: clojars-users-api
artifact_total: 20
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/clojars-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/clojars-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/clojars-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://clojars.statuspage.io
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/clojars
- group: build
  title: ''
  type: GitHubRepo
  url: https://github.com/clojars/clojars-web
- group: other
  title: ''
  type: Wiki
  url: https://github.com/clojars/clojars-web/wiki
- group: other
  title: ''
  type: MavenRepository
  url: https://repo.clojars.org
- group: other
  title: ''
  type: Sponsor
  url: https://www.clojuriststogether.org/
created: '2026-06-13'
description: Clojars is a community repository for open source Clojure libraries, providing a REST API for searching artifacts, retrieving version information, accessing user and group data, and managing deployment credentials via deploy tokens.
examples:
- key_count: 9
  name: Get Artifact By Group
  slug: get-artifact-by-group
- key_count: 2
  name: Get Release Feed
  slug: get-release-feed
- key_count: 2
  name: Get User
  slug: get-user
- key_count: 2
  name: Search Artifacts
  slug: search-artifacts
finops:
- name: Overview
  service_category: ''
  slug: overview
image: https://clojars.org/images/clojars-logo.png
json_schemas:
- name: Artifact
  property_count: 9
  slug: artifact
- name: ReleaseFeed
  property_count: 2
  slug: release-feed
- name: User
  property_count: 2
  slug: user
jsonld:
- class_count: 0
  name: context Context
  property_count: 17
  slug: context
layout: provider
modified: '2026-06-13'
name: Clojars
nav: Providers
network: true
overview: 'Clojars publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Artifacts API, Feeds API, Groups API, and 2 more. Tagged areas include Clojure, Package Registry, Artifact Repository, and Open Source.


  The Clojars catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Clojars'' developer surface includes authentication and 8 more developer resources.'
plans:
- name: Free
  plan_count: 0
  slug: free
random_paper: 21
rate_limits:
- limit_count: 4
  name: Default
  slug: default
rules:
- name: Clojars API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: clojars-jsonschema-spectral-rules
score:
  band: thin
  composite: 40.3
  delta: -3.4
  facets:
    commercial_clarity: 7.9
    contract_quality: 64.1
    developer_ergonomics: 10.9
    discoverability: 66.7
    governance: 58.3
    operational_transparency: 52.6
  previous_composite: 43.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/clojars/refs/heads/main/screenshots/clojars-2026-06-20T174532.png
security:
- kind: authentication
  name: Clojars Authentication
  slug: clojars-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Clojars Domain Security
  slug: clojars-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: clojars
tags:
- Clojure
- Package Registry
- Artifact Repository
- Open Source
website: https://clojars.org/
---

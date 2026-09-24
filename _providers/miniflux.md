---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
  score: 14.7
  scored_at: '2026-09-24'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Miniflux Agentic Access
  operation_count: 42
  slug: miniflux-agentic-access
  summary_line: 42 operations · 20 acting
api_count: 19
apis:
- description: The Api Keys API from Miniflux — 2 operation(s) for api keys.
  name: Miniflux Api Keys API
  slug: miniflux-api-keys-api
- description: The Categories API from Miniflux — 6 operation(s) for categories.
  name: Miniflux Categories API
  slug: miniflux-categories-api
- description: The Enclosures API from Miniflux — 1 operation(s) for enclosures.
  name: Miniflux Enclosures API
  slug: miniflux-enclosures-api
- description: The Entries API from Miniflux — 7 operation(s) for entries.
  name: Miniflux Entries API
  slug: miniflux-entries-api
- description: The Export API from Miniflux — 1 operation(s) for export.
  name: Miniflux Export API
  slug: miniflux-export-api
- description: The Feeds API from Miniflux — 5 operation(s) for feeds.
  name: Miniflux Feeds API
  slug: miniflux-feeds-api
- description: The Import API from Miniflux — 1 operation(s) for import.
  name: Miniflux Import API
  slug: miniflux-import-api
- description: The Integrations API from Miniflux — 1 operation(s) for integrations.
  name: Miniflux Integrations API
  slug: miniflux-integrations-api
- description: The Liveness API from Miniflux — 1 operation(s) for liveness.
  name: Miniflux Liveness API
  slug: miniflux-liveness-api
- description: The Me API from Miniflux — 1 operation(s) for me.
  name: Miniflux Me API
  slug: miniflux-me-api
- description: The Readiness API from Miniflux — 1 operation(s) for readiness.
  name: Miniflux Readiness API
  slug: miniflux-readiness-api
- description: The Users API from Miniflux — 4 operation(s) for users.
  name: Miniflux Users API
  slug: miniflux-users-api
- description: The Version API from Miniflux — 2 operation(s) for version.
  name: Miniflux Version API
  slug: miniflux-version-api
- description: The Discover API from Miniflux — 1 operation(s) for discover.
  name: Miniflux Discover API
  slug: miniflux-discover-api
- description: The Flush History API from Miniflux — 1 operation(s) for flush history.
  name: Miniflux Flush History API
  slug: miniflux-flush-history-api
- description: The Healthz API from Miniflux — 1 operation(s) for healthz.
  name: Miniflux Healthz API
  slug: miniflux-healthz-api
- description: The Icons API from Miniflux — 1 operation(s) for icons.
  name: Miniflux Icons API
  slug: miniflux-icons-api
- description: The Readyz API from Miniflux — 1 operation(s) for readyz.
  name: Miniflux Readyz API
  slug: miniflux-readyz-api
- description: The Health Check API from Miniflux — 1 operation(s) for health check.
  name: Miniflux Health Check API
  slug: miniflux-health-check-api
artifact_total: 32
common:
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/json-ld/miniflux-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/miniflux-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/vocabulary/miniflux-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/miniflux-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/data-model/miniflux-data-model.yml
  title: ''
  type: DataModel
  url: data-model/miniflux-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/agentic-access/miniflux-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/miniflux-agentic-access.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/rules/miniflux-rules.yml
  title: ''
  type: Spectral
  url: rules/miniflux-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/miniflux/refs/heads/main/conformance/miniflux-conformance.yml
  title: ''
  type: Conformance
  url: conformance/miniflux-conformance.yml
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
json_schemas:
- name: GetV1Categories40FeedsResponse
  property_count: 23
  slug: miniflux-get-v1-categories40-feeds-response
- name: GetV1FeedsFeedidIconResponse
  property_count: 3
  slug: miniflux-get-v1-feeds-feedid-icon-response
- name: GetV1FeedsResponse
  property_count: 23
  slug: miniflux-get-v1-feeds-response
- name: GetV1Feeds42Response
  property_count: 23
  slug: miniflux-get-v1-feeds42-response
- name: GetV1MeResponse
  property_count: 15
  slug: miniflux-get-v1-me-response
- name: PostV1FeedsRequest
  property_count: 13
  slug: miniflux-post-v1-feeds-request
- name: PutV1EntriesEntryidResponse
  property_count: 19
  slug: miniflux-put-v1-entries-entryid-response
- name: PutV1Feeds42Request
  property_count: 15
  slug: miniflux-put-v1-feeds42-request
- name: PutV1Feeds42Response
  property_count: 23
  slug: miniflux-put-v1-feeds42-response
jsonld:
- class_count: 55
  name: Miniflux Context
  property_count: 83
  slug: miniflux-context
layout: provider
modified: '2026-09-21'
name: Miniflux
nav: Providers
network: true
overview: 'Miniflux publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Api Keys API, Categories API, Enclosures API, and 16 more. Tagged areas include Feed Reader, Open Source, Self-Hosted, Minimalist, and Privacy.


  The Miniflux catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Miniflux''s developer surface includes documentation, API reference, getting-started guide, support, and 12 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 48
  extends:
  - spectral:oas
  name: Miniflux API Rules
  rule_count: 7
  severity_counts:
    error: 5
    hint: 0
    info: 1
    warn: 1
  slug: miniflux-rules
score:
  band: emerging
  composite: 25.6
  coverage:
    artifact_dirs: 12
    catalog_earned: 59.8
    catalog_earned_first_party: 0.0
    catalog_gap: 55.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 23.9
    developer_ergonomics: 40.5
    discoverability: 61.1
    operational_transparency: 5.3
  previous_composite: 25.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 20
      marker_coverage: 100.0
      total: 20
    mcp: unknown
  schema_version: 0.22.0
  scored_at: '2026-09-24'
  trend: flat
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
- Open Source
- Self-Hosted
- Minimalist
- Privacy
website: https://miniflux.app/
---

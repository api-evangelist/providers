---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 40.5
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 122
  human_in_the_loop: 1
  name: Autobrr Agentic Access
  operation_count: 214
  slug: autobrr-agentic-access
  summary_line: 214 operations · 122 acting · 1 human-in-the-loop
api_count: 1
apis:
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: API key management
  name: autobrr API Keys API
  slug: autobrr-api-keys-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Sonarr/Radarr instance management for external ID lookups
  name: autobrr ARR Integrations API
  slug: autobrr-arr-integrations-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: User authentication and session management
  name: autobrr Authentication API
  slug: autobrr-authentication-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The Backups API from autobrr — 5 operation(s) for backups.
  name: autobrr Backups API
  slug: autobrr-backups-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Category management
  name: autobrr Categories API
  slug: autobrr-categories-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Client API key management for external applications
  name: autobrr Client API Keys API
  slug: autobrr-client-api-keys-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The Client Settings API from autobrr — 1 operation(s) for client settings.
  name: autobrr Client Settings API
  slug: autobrr-client-settings-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Cross-seeding operations for finding and adding duplicate torrents
  name: autobrr Cross Seed API
  slug: autobrr-cross-seed-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Directory scanner operations for data-based matching and injection
  name: autobrr Dir Scan API
  slug: autobrr-dir-scan-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: BDInfo scans of Blu-ray Discs (BDMV folders and .iso files) in torrents
  name: autobrr Disc Scans API
  slug: autobrr-disc-scans-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Manage and execute external applications
  name: autobrr External Programs API
  slug: autobrr-external-programs-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: qBittorrent instance management
  name: autobrr Instances API
  slug: autobrr-instances-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The Licenses API from autobrr — 6 operation(s) for licenses.
  name: autobrr Licenses API
  slug: autobrr-licenses-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Notification-related endpoints for targets and events
  name: autobrr Notifications API
  slug: autobrr-notifications-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Orphan file scanning and cleanup (files on disk not associated with any torrent)
  name: autobrr Orphan Scan API
  slug: autobrr-orphan-scan-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: qBittorrent-compatible proxy endpoints authenticated by client API key
  name: autobrr Proxy API
  slug: autobrr-proxy-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: RSS feed and auto-download rule management
  name: autobrr RSS API
  slug: autobrr-rss-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The System API from autobrr — 12 operation(s) for system.
  name: autobrr System API
  slug: autobrr-system-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Tag management
  name: autobrr Tags API
  slug: autobrr-tags-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Sideloaded custom theme listing (premium)
  name: autobrr Themes API
  slug: autobrr-themes-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Individual torrent information
  name: autobrr Torrent Details API
  slug: autobrr-torrent-details-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: Torrent operations
  name: autobrr Torrents API
  slug: autobrr-torrents-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The Torznab API from autobrr — 4 operation(s) for torznab.
  name: autobrr Torznab API
  slug: autobrr-torznab-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The Tracker Icons API from autobrr — 1 operation(s) for tracker icons.
  name: autobrr Tracker Icons API
  slug: autobrr-tracker-icons-api
- baseURL: http://localhost:7476
  baseurl_source: spec
  description: The Trackers API from autobrr — 1 operation(s) for trackers.
  name: autobrr Trackers API
  slug: autobrr-trackers-api
artifact_total: 31
asyncapis:
- description: ''
  name: Autobrr Webhooks
  slug: autobrr-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/autobrr/agentic-access/autobrr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/autobrr-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/autobrr/rules/autobrr-rules.yml
  title: ''
  type: Spectral
  url: rules/autobrr-rules.yml
- group: design
  href: https://artifacts.apis.io/autobrr/json-ld/autobrr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/autobrr-context.jsonld
- group: design
  href: https://artifacts.apis.io/autobrr/vocabulary/autobrr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/autobrr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/autobrr/asyncapi/autobrr-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/autobrr-webhooks.yml
- group: design
  href: https://artifacts.apis.io/autobrr/data-model/autobrr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/autobrr-data-model.yml
- group: build
  href: https://artifacts.apis.io/autobrr/cli/autobrr-cli.yml
  title: ''
  type: CLI
  url: cli/autobrr-cli.yml
- group: auth
  href: https://artifacts.apis.io/autobrr/authentication/autobrr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/autobrr-authentication.yml
- group: design
  href: https://artifacts.apis.io/autobrr/errors/autobrr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/autobrr-problem-types.yml
- group: design
  href: https://artifacts.apis.io/autobrr/conformance/autobrr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/autobrr-conformance.yml
- group: agent
  href: https://artifacts.apis.io/autobrr/llms/autobrr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/autobrr-llms.txt
- group: other
  href: https://artifacts.apis.io/autobrr/hosts/autobrr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/autobrr-hosts.yml
- group: other
  href: https://artifacts.apis.io/autobrr/vendors/autobrr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/autobrr-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://autobrr.com/release-notes
- group: auth
  href: https://artifacts.apis.io/autobrr/security/autobrr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/autobrr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://autobrr.com/
- group: docs
  title: ''
  type: Documentation
  url: https://autobrr.com/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://autobrr.com/api
- group: start
  title: ''
  type: GettingStarted
  url: https://autobrr.com/quick-start
- group: operate
  title: ''
  type: Support
  url: https://autobrr.com/support
- group: operate
  title: ''
  type: Community
  url: https://autobrr.com/community
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/autobrr
coverage:
  checked: '2026-10-28'
  detail: The autobrr REST API reference page provides human‑readable HTML but no published OpenAPI, AsyncAPI, GraphQL, or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://autobrr.com/api
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-28'
description: autobrr is an open‑source, self‑hosted automation tool that bridges IRC announce channels and RSS feeds from torrent indexers to download clients and *arr applications. It listens to real‑time announcements, filters releases based on user‑defined rules, and pushes matching torrents to qBittorrent, Deluge, Transmission, rTorrent, or the Sonarr/Radarr/Lidarr ecosystem. The platform supports Docker, native binaries for Linux, macOS, Windows, and FreeBSD, and integrates with popular notification services like Discord, Telegram, and Pushover. autobrr aims to streamline torrent acquisition, reduce latency between announcement and download, and provide a flexible API for custom extensions.
jsonld:
- class_count: 120
  name: Autobrr Context
  property_count: 464
  slug: autobrr-context
layout: provider
modified: '2026-10-28'
name: autobrr
nav: Providers
network: true
overview: 'autobrr publishes 25 API contracts indexed on the [APIs.io](https://apis.io/) network, including API Keys API, ARR Integrations API, Authentication API, and 22 more. Tagged areas include Torrent, Automation, Open-Source, Self-Hosted, and Media.


  The autobrr catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  autobrr''s developer surface includes CLI, authentication, changelog, documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: autobrr API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 1
  slug: autobrr-rules
score:
  band: thin
  composite: 35.8
  coverage:
    artifact_dirs: 18
    catalog_earned: 41.8
    catalog_earned_first_party: 0.0
    catalog_gap: 73.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.0
    developer_ergonomics: 52.4
    discoverability: 44.6
    operational_transparency: 28.9
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 25
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
- kind: authentication
  name: Autobrr Authentication
  slug: autobrr-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Autobrr Domain Security
  slug: autobrr-domain-security
  summary_line: TLSv1.3 · HSTS
slug: autobrr
tags:
- Torrent
- Automation
- Open-Source
- Self-Hosted
- Media
website: https://autobrr.com/
---

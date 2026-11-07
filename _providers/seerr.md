---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.3
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: 'Seerr (Overseerr + Jellyseerr) API as documented publicly: 39 operations. Contract generated from the documentation by API Evangelist (2026-10-28); not the provider''s own document.'
  name: Seerr (Overseerr + Jellyseerr) API
  slug: seerr-api
artifact_total: 11
common:
- group: design
  href: https://artifacts.apis.io/seerr/rules/seerr-rules.yml
  title: ''
  type: Spectral
  url: rules/seerr-rules.yml
- group: design
  href: https://artifacts.apis.io/seerr/json-ld/seerr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/seerr-context.jsonld
- group: design
  href: https://artifacts.apis.io/seerr/vocabulary/seerr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/seerr-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/seerr/data-model/seerr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/seerr-data-model.yml
- group: operate
  href: https://artifacts.apis.io/seerr/changelog/seerr-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/seerr-changelog.yml
- group: auth
  href: https://artifacts.apis.io/seerr/authentication/seerr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/seerr-authentication.yml
- group: design
  href: https://artifacts.apis.io/seerr/conformance/seerr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/seerr-conformance.yml
- group: other
  href: https://artifacts.apis.io/seerr/hosts/seerr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/seerr-hosts.yml
- group: other
  href: https://artifacts.apis.io/seerr/vendors/seerr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/seerr-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/seerr-team/seerr/releases
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.seerr.dev/getting-started/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.seerr.dev/
- group: auth
  href: https://artifacts.apis.io/seerr/security/seerr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/seerr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://seerr.dev/
coverage:
  checked: '2026-10-28'
  detail: Documentation is served as Docusaurus HTML without a machine‑readable OpenAPI or other contract.
  evidence:
  - status: 200
    url: https://docs.seerr.dev
  reason: js-rendered-docs
  state: unreadable
created: '2026-10-28'
description: Seerr is a free, open‑source request‑management and media discovery platform that unifies the capabilities of Overseerr and Jellyseerr. It enables users of Jellyfin, Plex and Emby to request, discover and organize media content through a modern web interface, supporting integrations with Radarr, Sonarr and other automation tools.
image: https://seerr.dev/os_logo_filled.svg
json_schemas:
- name: GetAuthMeResponse
  property_count: 1
  slug: seerr-get-auth-me-response
- name: GetSettingsPlexUsersResponse
  property_count: 1
  slug: seerr-get-settings-plex-users-response
- name: GetUserResponse
  property_count: 1
  slug: seerr-get-user-response
- name: GetUserUseridResponse
  property_count: 1
  slug: seerr-get-user-userid-response
- name: PostSettingsDiscoverAddResponse
  property_count: 1
  slug: seerr-post-settings-discover-add-response
- name: PostUserResponse
  property_count: 1
  slug: seerr-post-user-response
jsonld:
- class_count: 8
  name: Seerr Context
  property_count: 0
  slug: seerr-context
layout: provider
modified: '2026-10-28'
name: Seerr (Overseerr + Jellyseerr)
nav: Providers
network: true
overview: 'Seerr (Overseerr + Jellyseerr) is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Media Discovery, Request Management, Open Source, Media Server Integration, and Automation Integration.


  The Seerr (Overseerr + Jellyseerr) catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Seerr (Overseerr + Jellyseerr)''s developer surface includes changelog, authentication, getting-started guide, documentation, and 10 more developer resources.'
random_paper: 17
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Seerr (Overseerr + Jellyseerr) API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: seerr-rules
score:
  band: emerging
  composite: 18.8
  coverage:
    artifact_dirs: 16
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.1
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 21.4
    developer_ergonomics: 22.6
    discoverability: 57.1
    operational_transparency: 7.9
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 21.9
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 16.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/seerr/seerr-2026-11-03T142953.png
security:
- kind: authentication
  name: Seerr Authentication
  slug: seerr-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Seerr Domain Security
  slug: seerr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: seerr
tags:
- Media Discovery
- Request Management
- Open Source
- Media Server Integration
- Automation Integration
- Permissions
- Notification
website: https://seerr.dev/
---

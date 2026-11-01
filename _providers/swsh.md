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
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Swsh Agentic Access
  operation_count: 3
  slug: swsh-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- baseURL: https://public-api.joinswsh.com
  baseurl_source: declared
  description: The album API from swsh — 2 operation(s) for album.
  name: swsh Album API
  slug: swsh-album-api
- baseURL: https://public-api.joinswsh.com
  baseurl_source: declared
  description: The ping API from swsh — 1 operation(s) for ping.
  name: swsh Ping API
  slug: swsh-ping-api
artifact_total: 12
asyncapis:
- description: ''
  name: Swsh Webhooks
  slug: swsh-webhooks
common:
- group: design
  href: https://artifacts.apis.io/swsh/data-model/swsh-data-model.yml
  title: ''
  type: DataModel
  url: data-model/swsh-data-model.yml
- group: agent
  href: https://artifacts.apis.io/swsh/agentic-access/swsh-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/swsh-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/swsh/rules/swsh-rules.yml
  title: ''
  type: Spectral
  url: rules/swsh-rules.yml
- group: design
  href: https://artifacts.apis.io/swsh/vocabulary/swsh-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/swsh-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/swsh/errors/swsh-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/swsh-problem-types.yml
- group: design
  href: https://artifacts.apis.io/swsh/conformance/swsh-conformance.yml
  title: ''
  type: Conformance
  url: conformance/swsh-conformance.yml
- group: agent
  href: https://artifacts.apis.io/swsh/mcp/swsh-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/swsh-mcp.yml
- group: other
  href: https://artifacts.apis.io/swsh/hosts/swsh-hosts.yml
  title: ''
  type: Hosts
  url: hosts/swsh-hosts.yml
- group: other
  href: https://artifacts.apis.io/swsh/vendors/swsh-vendors.yml
  title: ''
  type: Vendors
  url: vendors/swsh-vendors.yml
- group: auth
  href: https://artifacts.apis.io/swsh/security/swsh-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/swsh-domain-security.yml
created: '2026-10-21'
description: SWSH is a fan‑engagement platform for live events that lets organizers collect, share, and monetize photo and video content from attendees. The service provides albums, real‑time photo labeling, webhook subscriptions, and a TypeScript SDK with an OpenAPI spec. Backed by a $4M seed round, SWSH serves major festivals, sports teams, and artists, offering both free consumer plans and paid business tiers with advanced moderation and branding features.
json_schemas:
- name: AlbumName
  property_count: 0
  slug: swsh-album-name
- name: CreateAlbumSupertitle
  property_count: 0
  slug: swsh-create-album-supertitle
- name: ResponsePing
  property_count: 0
  slug: swsh-response-ping
- name: ResponseSingleAlbum
  property_count: 0
  slug: swsh-response-single-album
layout: provider
mcp_servers:
- description: Remote MCP server at public-api.joinswsh.com.
  name: swsh MCP Server
  slug: swsh-mcp-yml
modified: '2026-10-21'
name: swsh
nav: Providers
network: true
overview: 'swsh publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Album API and Ping API. Tagged areas include Company, Fan Engagement, Live Events, Photo Sharing, and Software-as-a-Service.


  The swsh catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.'
plans:
- name: Swsh Plans Pricing
  plan_count: 4
  slug: swsh-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: swsh API Rules
  rule_count: 10
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 1
  slug: swsh-rules
score:
  band: thin
  composite: 27.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 61.8
    catalog_earned_first_party: 12.0
    catalog_gap: 53.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 53.7
    developer_ergonomics: 0.0
    discoverability: 61.7
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 10.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Swsh Domain Security
  slug: swsh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: swsh
tags:
- Company
- Fan Engagement
- Live Events
- Photo Sharing
- Software-as-a-Service
---

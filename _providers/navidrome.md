---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
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
  score: 22.9
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Navidrome Agentic Access
  operation_count: 3
  slug: navidrome-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://navidrome.org/api/v1
  baseurl_source: declared
  description: Server discovery and the published OpenAPI document.
  name: Navidrome Server API
  slug: navidrome-server-api
artifact_total: 9
common:
- group: agent
  href: https://artifacts.apis.io/navidrome/agentic-access/navidrome-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/navidrome-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/navidrome/rules/navidrome-rules.yml
  title: ''
  type: Spectral
  url: rules/navidrome-rules.yml
- group: design
  href: https://artifacts.apis.io/navidrome/json-ld/navidrome-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/navidrome-context.jsonld
- group: design
  href: https://artifacts.apis.io/navidrome/vocabulary/navidrome-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/navidrome-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/navidrome/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/navidrome/data-model/navidrome-data-model.yml
  title: ''
  type: DataModel
  url: data-model/navidrome-data-model.yml
- group: auth
  href: https://artifacts.apis.io/navidrome/authentication/navidrome-authentication.yml
  title: ''
  type: Authentication
  url: authentication/navidrome-authentication.yml
- group: design
  href: https://artifacts.apis.io/navidrome/errors/navidrome-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/navidrome-problem-types.yml
- group: design
  href: https://artifacts.apis.io/navidrome/conformance/navidrome-conformance.yml
  title: ''
  type: Conformance
  url: conformance/navidrome-conformance.yml
- group: other
  href: https://artifacts.apis.io/navidrome/overlays/navidrome-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/navidrome-openapi-overlay.yaml
- group: other
  href: https://artifacts.apis.io/navidrome/hosts/navidrome-hosts.yml
  title: ''
  type: Hosts
  url: hosts/navidrome-hosts.yml
- group: other
  href: https://artifacts.apis.io/navidrome/vendors/navidrome-vendors.yml
  title: ''
  type: Vendors
  url: vendors/navidrome-vendors.yml
- group: auth
  href: https://artifacts.apis.io/navidrome/security/navidrome-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/navidrome-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://navidrome.org/
- group: docs
  title: ''
  type: Documentation
  url: https://navidrome.org/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://navidrome.org/docs/developers/subsonic-api/
- group: start
  title: ''
  type: GettingStarted
  url: https://navidrome.org/docs/getting-started/
- group: operate
  title: ''
  type: Support
  url: https://navidrome.org/about/
- group: operate
  title: ''
  type: Roadmap
  url: https://navidrome.org/docs/overview/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/navidrome
created: '2026-10-28'
description: Welcome to Navidrome! Learn More Download Your Personal Streaming Service. Navidrome allows you to enjoy your music collection from anywhere, by making it available through a modern Web UI and through a wide range of third-party compatible mobile apps, for both iOS and Android devices.
image: https://www.navidrome.org/featured-background.jpg
json_schemas:
- name: ServerInfo
  property_count: 5
  slug: navidrome-server-info
jsonld:
- class_count: 1
  name: Navidrome Context
  property_count: 5
  slug: navidrome-context
layout: provider
modified: '2026-10-28'
name: Navidrome
nav: Providers
network: true
overview: 'Navidrome publishes 1 API contract indexed on the [APIs.io](https://apis.io/) network: Server API. Tagged areas include Company, Music, Streaming, Self-Hosted, and Open-Source.


  The Navidrome catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Navidrome''s developer surface includes authentication, documentation, API reference, getting-started guide, support, and 15 more developer resources.'
random_paper: 5
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Navidrome API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: navidrome-rules
scopes:
- name: Navidrome Scopes
  scope_count: 0
  slug: navidrome-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 34.5
  coverage:
    artifact_dirs: 25
    catalog_earned: 53.2
    catalog_earned_first_party: 0.0
    catalog_gap: 61.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 47.5
    developer_ergonomics: 51.7
    discoverability: 66.1
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Navidrome Authentication
  slug: navidrome-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Navidrome Domain Security
  slug: navidrome-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: get-server-info
  slug: navidrome-get-server-info
slug: navidrome
tags:
- Company
- Music
- Streaming
- Self-Hosted
- Open-Source
- Media-Server
website: https://navidrome.org/
---

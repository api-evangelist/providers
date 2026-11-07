---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
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
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Infranode Dev Agentic Access
  operation_count: 122
  slug: infranode-dev-agentic-access
  summary_line: 122 operations
api_count: 1
apis:
- baseURL: https://infranode.dev
  baseurl_source: declared
  description: Stadt-Register und normalisierte Stadt-Stammdaten
  name: infranode-dev Cities API
  slug: infranode-dev-cities-api
- baseURL: https://infranode.dev
  baseurl_source: declared
  description: Multi-City-Vergleich einer Ressource über mehrere Städte
  name: infranode-dev Compare API
  slug: infranode-dev-compare-api
- baseURL: https://infranode.dev
  baseurl_source: declared
  description: 'Getrennte Live-Kategorie unter /api/v1/live. Minutenfrische bzw. quasi-live Quellen mit eigenem Envelope-Kennzeichen: meta.as_of (Datenstand) und meta.refresh_seconds (Kadenz). Re-exponiert zusätzlich'
  name: infranode-dev Live API
  slug: infranode-dev-live-api
- baseURL: https://infranode.dev
  baseurl_source: declared
  description: Meta- und Diagnose-Routen (Health, Ping, Source-Status, Spec)
  name: infranode-dev Meta API
  slug: infranode-dev-meta-api
- baseURL: https://infranode.dev
  baseurl_source: declared
  description: Per-Bahnhof-Live-Boards unter /api/v1/stations/{eva}. Abfahrten/Ankünfte JEDES DB-Bahnhofs über seine EVA-Nummer (aus dem Katalog /cities/{slug}/stations), alle Gattungen inkl. Nahverkehr, mit Echtzei
  name: infranode-dev Stations API
  slug: infranode-dev-stations-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/infranode-dev/agentic-access/infranode-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/infranode-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/infranode-dev/rules/infranode-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/infranode-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/infranode-dev/json-ld/infranode-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/infranode-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/infranode-dev/vocabulary/infranode-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/infranode-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/infranode-dev/data-model/infranode-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/infranode-dev-data-model.yml
- group: operate
  href: https://artifacts.apis.io/infranode-dev/changelog/infranode-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/infranode-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/infranode-dev/errors/infranode-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/infranode-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/infranode-dev/conformance/infranode-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/infranode-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/infranode-dev/llms/infranode-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/infranode-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/infranode-dev/mcp/infranode-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/infranode-dev-mcp.yml
- group: other
  href: https://artifacts.apis.io/infranode-dev/hosts/infranode-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/infranode-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/infranode-dev/vendors/infranode-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/infranode-dev-vendors.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.infranode.dev/status/infranode
- group: operate
  title: ''
  type: Roadmap
  url: https://infranode.dev/roadmap/
- group: operate
  title: ''
  type: ChangeLog
  url: https://infranode.dev/changelog/
- group: auth
  href: https://artifacts.apis.io/infranode-dev/security/infranode-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/infranode-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://infranode.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://infranode.dev/api/
- group: start
  title: ''
  type: GettingStarted
  url: https://infranode.dev/quickstart/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://infranode.dev/mcp/
- group: operate
  title: ''
  type: Support
  url: https://infranode.dev/tutorials/
created: '2026-10-31'
description: InfraNode provides a free, public open-data REST API covering 84 German cities with 116 endpoints across domains such as environment, weather, public transport, energy, and social statistics. All data is accessible without authentication via a uniform JSON envelope, with clear licensing and source status. The service also offers an MCP server for AI assistants like Claude and ChatGPT, enabling seamless integration for developers and researchers.
image: https://infranode.dev/og-cover.png
json_schemas:
- name: CanonicalRecord
  property_count: 14
  slug: infranode-dev-canonical-record
- name: Health
  property_count: 3
  slug: infranode-dev-health
- name: Meta
  property_count: 5
  slug: infranode-dev-meta
- name: SourceStatus
  property_count: 3
  slug: infranode-dev-source-status
jsonld:
- class_count: 66
  name: Infranode Dev Context
  property_count: 272
  slug: infranode-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.infranode.dev.
  name: infranode-dev MCP Server
  slug: infranode-dev-mcp-yml
modified: '2026-10-31'
name: infranode-dev
nav: Providers
network: true
overview: 'infranode-dev publishes 5 API contracts indexed on the [APIs.io](https://apis.io/) network, including Cities API, Compare API, Live API, and 2 more. Tagged areas include Company, Open Data, Germany, Cities, and Public APIs.


  The infranode-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  infranode-dev''s developer surface includes changelog, API reference, getting-started guide, support, and 17 more developer resources.'
random_paper: 18
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: infranode-dev API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: infranode-dev-rules
score:
  band: thin
  composite: 28.9
  coverage:
    artifact_dirs: 19
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.4
  facets:
    access_clarity: 0.0
    contract_governance: 22.0
    contract_quality: 57.6
    developer_ergonomics: 16.7
    discoverability: 65.0
    operational_transparency: 18.4
  previous_composite: 34.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
    mcp: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 10.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/infranode-dev/infranode-dev-2026-11-03T133805.png
security:
- kind: domain-security
  name: Infranode Dev Domain Security
  slug: infranode-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: infranode-dev
tags:
- Company
- Open Data
- Germany
- Cities
- Public APIs
website: https://infranode.dev/
---

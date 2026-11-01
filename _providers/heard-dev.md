---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 38.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Heard is a macOS voice layer for coding agents.
  name: Heard API
  slug: heard-api
- baseURL: https://heard.dev
  baseurl_source: declared
  description: 'heard-dev API as documented publicly: 1 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: heard-dev API
  slug: heard-dev-api
artifact_total: 10
common:
- group: commercial
  href: https://artifacts.apis.io/heard-dev/plans/heard-dev-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/heard-dev-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/heard-dev/rules/heard-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/heard-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/heard-dev/json-ld/heard-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/heard-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/heard-dev/vocabulary/heard-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/heard-dev-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/heard-dev/data-model/heard-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/heard-dev-data-model.yml
- group: build
  href: https://artifacts.apis.io/heard-dev/cli/heard-dev-cli.yml
  title: ''
  type: CLI
  url: cli/heard-dev-cli.yml
- group: operate
  href: https://artifacts.apis.io/heard-dev/changelog/heard-dev-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/heard-dev-changelog.yml
- group: design
  href: https://artifacts.apis.io/heard-dev/conformance/heard-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/heard-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/heard-dev/llms/heard-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/heard-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/heard-dev/mcp/heard-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/heard-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/heard-dev/well-known/heard-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/heard-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/heard-dev/hosts/heard-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/heard-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/heard-dev/vendors/heard-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/heard-dev-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://heard.dev/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.heard.dev/docs/product-updates/changelog
- group: auth
  href: https://artifacts.apis.io/heard-dev/security/heard-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/heard-dev-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://heard.dev/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.heard.dev/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.heard.dev/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.heard.dev/quickstart.md
- group: operate
  title: ''
  type: Support
  url: https://discord.gg/gdC36fpeDw
- group: company
  title: ''
  type: Blog
  url: https://heard.dev/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/heardlabs
- group: commercial
  title: ''
  type: Pricing
  url: https://heard.dev/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://heard.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://heard.dev/privacy
coverage:
  checked: '2026-10-30'
  detail: Heard provides public markdown documentation but no OpenAPI, AsyncAPI, GraphQL, or other machine-readable spec.
  evidence:
  - status: 200
    url: https://docs.heard.dev/overview.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Heard is a macOS voice layer for coding agents, turning agent activity into concise spoken updates. It integrates with Claude Code, Codex, and other AI coding assistants, providing real-time narration of progress, decisions, failures, and completed work. Users can download the app, connect agents, and customize listening modes such as Co-pilot, Companion, and Focus. The platform offers free and paid plans, with pricing details, and maintains open-source components on GitHub. It emphasizes privacy, with data processed locally unless optional hosted services are enabled.
image: https://heard.dev/social/heard-social-preview-2026-10-29-1200x630.jpg
json_schemas:
- name: GetDownloadCcResponse
  property_count: 1
  slug: heard-dev-get-download-cc-response
jsonld:
- class_count: 1
  name: Heard Dev Context
  property_count: 1
  slug: heard-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.heard.dev.
  name: heard-dev MCP Server
  slug: heard-dev-mcp-yml
modified: '2026-10-30'
name: heard-dev
nav: Providers
network: true
overview: 'heard-dev is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Voice, macOS, and DeveloperTools.


  The heard-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  heard-dev''s developer surface includes CLI, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Heard Dev Plans Pricing
  plan_count: 2
  slug: heard-dev-plans-pricing
random_paper: 16
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: heard-dev API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: heard-dev-rules
scopes:
- name: Heard Dev Scopes
  scope_count: 0
  slug: heard-dev-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.5
  coverage:
    artifact_dirs: 27
    catalog_earned: 56.2
    catalog_earned_first_party: 8.0
    catalog_gap: 58.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 17.8
    developer_ergonomics: 42.9
    discoverability: 56.7
    operational_transparency: 31.6
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 2
      marker_coverage: 100.0
      total: 2
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 31.8
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Heard Dev Authentication
  slug: heard-dev-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Heard Dev Domain Security
  slug: heard-dev-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: heard-dev
tags:
- Company
- AI
- Voice
- macOS
- DeveloperTools
website: https://heard.dev/
---

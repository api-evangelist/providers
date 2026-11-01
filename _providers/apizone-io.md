---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: unknown
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.0
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apizone Io Agentic Access
  operation_count: 3
  slug: apizone-io-agentic-access
  summary_line: 3 operations
api_count: 1
apis:
- baseURL: https://apizone.io
  baseurl_source: declared
  description: The Status API from apizone-io — 2 operation(s) for status.
  name: apizone-io Status API
  slug: apizone-io-status-api
- baseURL: https://apizone.io
  baseurl_source: declared
  description: The Uptime API from apizone-io — 1 operation(s) for uptime.
  name: apizone-io Uptime API
  slug: apizone-io-uptime-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/apizone-io/agentic-access/apizone-io-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/apizone-io-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/apizone-io/rules/apizone-io-rules.yml
  title: ''
  type: Spectral
  url: rules/apizone-io-rules.yml
- group: design
  href: https://artifacts.apis.io/apizone-io/json-ld/apizone-io-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/apizone-io-context.jsonld
- group: design
  href: https://artifacts.apis.io/apizone-io/vocabulary/apizone-io-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/apizone-io-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/apizone-io/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/apizone-io/data-model/apizone-io-data-model.yml
  title: ''
  type: DataModel
  url: data-model/apizone-io-data-model.yml
- group: design
  href: https://artifacts.apis.io/apizone-io/lifecycle/apizone-io-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/apizone-io-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/apizone-io/errors/apizone-io-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apizone-io-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apizone-io/conformance/apizone-io-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apizone-io-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apizone-io/llms/apizone-io-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apizone-io-llms.txt
- group: build
  href: https://artifacts.apis.io/apizone-io/mcp/apizone-io-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/apizone-io-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/apizone-io/mcp/apizone-io-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apizone-io-mcp.yml
- group: other
  href: https://artifacts.apis.io/apizone-io/hosts/apizone-io-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apizone-io-hosts.yml
- group: other
  href: https://artifacts.apis.io/apizone-io/vendors/apizone-io-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apizone-io-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://apizone.io/category/media
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/APIZone
- group: auth
  href: https://artifacts.apis.io/apizone-io/security/apizone-io-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apizone-io-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apizone.io/
- group: docs
  title: ''
  type: Documentation
  url: https://apizone.io/api-docs
- group: docs
  title: ''
  type: APIReference
  url: https://apizone.io/api-docs
- group: start
  title: ''
  type: GettingStarted
  url: https://apizone.io/how-it-works
- group: commercial
  title: ''
  type: Pricing
  url: https://apizone.io/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apizone.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apizone.io/privacy
created: '2026-10-30'
description: APIzone provides independent, real-time status monitoring for hundreds of popular public APIs. It continuously probes API endpoints, records uptime, latency, and incidents, and presents the data on a public status board. Users can view live status, browse historical outage history, and subscribe to email alerts for selected APIs. The service also offers embeddable badges and widgets for developers to display API health on their own sites. Paid plans add customizable alert notifications via email, Slack, Discord, or Microsoft Teams, with billing handled through Stripe. APIzone operates without storing personal data for status checks and respects privacy, as detailed in its privacy policy.
image: https://apizone.io/opengraph-image?a4acc150de076a45
json_schemas:
- name: ServiceStatus
  property_count: 7
  slug: apizone-io-service-status
- name: UptimeWindow
  property_count: 4
  slug: apizone-io-uptime-window
jsonld:
- class_count: 2
  name: Apizone Io Context
  property_count: 11
  slug: apizone-io-context
layout: provider
mcp_servers:
- description: Remote MCP server at apizone.io.
  name: apizone-io MCP Server
  slug: apizone-io-mcp-yml
modified: '2026-10-30'
name: apizone-io
nav: Providers
network: true
overview: 'apizone-io publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Status API and Uptime API. Tagged areas include API Monitoring, Status, Uptime, Developer Tools, and MCP.


  The apizone-io catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  apizone-io''s developer surface includes documentation, API reference, getting-started guide, pricing, and 20 more developer resources.'
random_paper: 11
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: apizone-io API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: apizone-io-rules
score:
  band: developing
  composite: 45.1
  coverage:
    artifact_dirs: 25
    catalog_earned: 74.7
    catalog_earned_first_party: 0.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 79.1
    contract_quality: 57.5
    developer_ergonomics: 35.0
    discoverability: 66.7
    operational_transparency: 5.3
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 18.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Apizone Io Authentication
  slug: apizone-io-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Apizone Io Domain Security
  slug: apizone-io-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: apizone-io-status
  slug: apizone-io-status
slug: apizone-io
tags:
- API Monitoring
- Status
- Uptime
- Developer Tools
- MCP
website: https://apizone.io/
---

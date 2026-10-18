---
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 60.5
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 12
  human_in_the_loop: 2
  name: Ploid Agentic Access
  operation_count: 31
  slug: ploid-agentic-access
  summary_line: 31 operations · 12 acting · 2 human-in-the-loop
api_count: 2
apis:
- description: 'Ploid''s hosted Streamable HTTP MCP server at https://api.ploid.com/mcp, protected by OAuth 2.1 (RFC 9728 protected-resource metadata, dynamic client registration, PKCE S256) and scoped to an approved '
  name: Ploid MCP Server
  slug: ploid-mcp-server
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Account API from Ploid — 4 operation(s) for account.
  name: Ploid Account API
  slug: ploid-account-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Discovery API from Ploid — 1 operation(s) for discovery.
  name: Ploid Discovery API
  slug: ploid-discovery-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Enrichment API from Ploid — 1 operation(s) for enrichment.
  name: Ploid Enrichment API
  slug: ploid-enrichment-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Harness API from Ploid — 2 operation(s) for harness.
  name: Ploid Harness API
  slug: ploid-harness-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Monitors API from Ploid — 7 operation(s) for monitors.
  name: Ploid Monitors API
  slug: ploid-monitors-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The People API from Ploid — 2 operation(s) for people.
  name: Ploid People API
  slug: ploid-people-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Search API from Ploid — 2 operation(s) for search.
  name: Ploid Search API
  slug: ploid-search-api
- baseURL: https://api.ploid.com
  baseurl_source: declared
  description: The Social API from Ploid — 1 operation(s) for social.
  name: Ploid Social API
  slug: ploid-social-api
- baseURL: https://api.ploid.com/mcp
  baseurl_source: declared
  description: The Linked In API from Ploid — 6 operation(s) for linked in.
  name: Ploid Linked In API
  slug: ploid-linked-in-api
artifact_total: 26
asyncapis:
- description: ''
  name: Ploid Webhooks
  slug: ploid-webhooks
common:
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/agentic-access/ploid-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/ploid-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/rate-limits/ploid-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/ploid-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/plans/ploid-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/ploid-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/rules/ploid-rules.yml
  title: ''
  type: Spectral
  url: rules/ploid-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/json-ld/ploid-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/ploid-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/vocabulary/ploid-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/ploid-vocabulary.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/asyncapi/ploid-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/ploid-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/data-model/ploid-data-model.yml
  title: ''
  type: DataModel
  url: data-model/ploid-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/cli/ploid-cli.yml
  title: ''
  type: CLI
  url: cli/ploid-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/conventions/ploid-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/ploid-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/conventions/ploid-conventions.yml
  title: ''
  type: Conventions
  url: conventions/ploid-conventions.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/scopes/ploid-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/ploid-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/lifecycle/ploid-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/ploid-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/errors/ploid-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/ploid-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/conformance/ploid-conformance.yml
  title: ''
  type: Conformance
  url: conformance/ploid-conformance.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/overlays/ploid-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/ploid-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/llms/ploid-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/ploid-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/mcp/ploid-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/ploid-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/mcp/ploid-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/ploid-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/well-known/ploid-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/ploid-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/hosts/ploid-hosts.yml
  title: ''
  type: Hosts
  url: hosts/ploid-hosts.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/vendors/ploid-vendors.yml
  title: ''
  type: Vendors
  url: vendors/ploid-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/packages/ploid-packages.yml
  title: ''
  type: SDKs
  url: packages/ploid-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/packages/ploid-packages.yml
  title: ''
  type: Packages
  url: packages/ploid-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/authentication/ploid-authentication.yml
  title: ''
  type: Authentication
  url: authentication/ploid-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://ploid.com
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/security/ploid-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/ploid-domain-security.yml
- group: docs
  title: ''
  type: Documentation
  url: https://ploid.com/documentation
- group: docs
  title: ''
  type: APIReference
  url: https://ploid.com/documentation/api
- group: start
  title: ''
  type: GettingStarted
  url: https://ploid.com/documentation/getting-started
- group: commercial
  title: ''
  type: Pricing
  url: https://ploid.com/pricing
- group: start
  title: ''
  type: Login
  url: https://app.ploid.com/login
- group: start
  title: ''
  type: SignUp
  url: https://app.ploid.com/login?mode=signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/ploidcom
- group: commercial
  title: ''
  type: TermsOfService
  url: https://ploid.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://ploid.com/privacy
- group: other
  title: ''
  type: DataSubjectRequest
  url: https://ploid.com/data-rights
- group: company
  title: ''
  type: About
  url: https://ploid.com/company
- group: other
  title: ''
  type: Subprocessors
  url: https://ploid.com/privacy
created: '2026-10-07'
description: 'Ploid is an applied AI lab building a people search and intelligence platform: a living index of more than two billion people available through a web app, a REST API, a CLI, and a hosted MCP server. The Ploid Public API (OpenAPI 3.1, 31 operations on api.ploid.com) covers synchronous people search, person resolution and evidence-backed person research runs, contact and social enrichment, public LinkedIn reads, monitors, and account usage and credit budgets, metered in ACU credits.'
image: https://ploid.com/favicon.ico
json_schemas:
- name: HarnessChatCompletionRequest
  property_count: 14
  slug: ploid-harness-chat-completion-request
- name: PersonResponse
  property_count: 0
  slug: ploid-person-response
- name: ResolveResponse
  property_count: 2
  slug: ploid-resolve-response
- name: SearchHandoffResponse
  property_count: 2
  slug: ploid-search-handoff-response
- name: SyncSearchRequest
  property_count: 9
  slug: ploid-sync-search-request
- name: SyncSearchResponse
  property_count: 2
  slug: ploid-sync-search-response
jsonld:
- class_count: 56
  name: Ploid Context
  property_count: 169
  slug: ploid-context
layout: provider
mcp_servers:
- description: Ploid's hosted Streamable HTTP MCP server for people research inside ChatGPT, Claude and other remote MCP clients. Connections are scoped to an approved Ploid workspace and consume that workspace's AC
  name: Ploid MCP Server
  slug: ploid
modified: '2026-10-07'
name: Ploid
nav: Providers
network: true
overview: 'Ploid publishes 10 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Discovery API, Enrichment API, and 7 more. Tagged areas include Company, People Data, People Search, Contact Enrichment, and Sales Intelligence.


  The Ploid catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Ploid''s developer surface includes CLI, authentication, documentation, API reference, getting-started guide, pricing, signup flow, and 33 more developer resources.'
plans:
- name: Ploid Plans Pricing
  plan_count: 3
  slug: ploid-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 6
  name: Ploid Rate Limits
  slug: ploid-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: Ploid API Rules
  rule_count: 14
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 2
  slug: ploid-rules
scopes:
- name: Ploid Scopes
  scope_count: 6
  slug: ploid-scopes
  summary_line: 6 scopes
score:
  band: strong
  composite: 65.2
  coverage:
    artifact_dirs: 29
    catalog_earned: 86.8
    catalog_earned_first_party: 24.0
    catalog_gap: 28.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 76.3
    contract_governance: 35.6
    contract_quality: 70.7
    developer_ergonomics: 56.5
    discoverability: 75.0
    operational_transparency: 44.7
  previous_composite: 64.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 42.2
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/ploid/refs/heads/main/screenshots/ploid-2026-10-11T112630.png
security:
- kind: authentication
  name: Ploid Authentication
  slug: ploid-authentication
  summary_line: apiKey/http/oauth2 · 4 schemes
- kind: domain-security
  name: Ploid Domain Security
  slug: ploid-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: ploid
tags:
- Company
- People Data
- People Search
- Contact Enrichment
- Sales Intelligence
- Recruiting
- LinkedIn
- MCP
- Agents
- Data Enrichment
website: https://ploid.com
---

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
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: derived
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 51.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 54
  human_in_the_loop: 2
  name: Dystro Dev Agentic Access
  operation_count: 113
  slug: dystro-dev-agentic-access
  summary_line: 113 operations · 54 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The accounts API from dystro-dev — 17 operation(s) for accounts.
  name: dystro-dev Accounts API
  slug: dystro-dev-accounts-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The analytics API from dystro-dev — 14 operation(s) for analytics.
  name: dystro-dev Analytics API
  slug: dystro-dev-analytics-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The api-keys API from dystro-dev — 2 operation(s) for api-keys.
  name: dystro-dev API Keys API
  slug: dystro-dev-api-keys-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The campaigns API from dystro-dev — 3 operation(s) for campaigns.
  name: dystro-dev Campaigns API
  slug: dystro-dev-campaigns-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The connect API from dystro-dev — 4 operation(s) for connect.
  name: dystro-dev Connect API
  slug: dystro-dev-connect-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The inbox API from dystro-dev — 15 operation(s) for inbox.
  name: dystro-dev Inbox API
  slug: dystro-dev-inbox-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The media API from dystro-dev — 5 operation(s) for media.
  name: dystro-dev Media API
  slug: dystro-dev-media-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The meta API from dystro-dev — 11 operation(s) for meta.
  name: dystro-dev Meta API
  slug: dystro-dev-meta-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The posts API from dystro-dev — 13 operation(s) for posts.
  name: dystro-dev Posts API
  slug: dystro-dev-posts-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The queue API from dystro-dev — 3 operation(s) for queue.
  name: dystro-dev Queue API
  slug: dystro-dev-queue-api
- baseURL: https://lovable-anaconda-804.convex.site
  baseurl_source: declared
  description: The webhooks API from dystro-dev — 7 operation(s) for webhooks.
  name: dystro-dev Webhooks API
  slug: dystro-dev-webhooks-api
artifact_total: 22
common:
- group: agent
  href: https://artifacts.apis.io/dystro-dev/llms/dystro-dev-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dystro-dev-llms.txt
- group: agent
  href: https://artifacts.apis.io/dystro-dev/agentic-access/dystro-dev-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/dystro-dev-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/dystro-dev/rules/dystro-dev-rules.yml
  title: ''
  type: Spectral
  url: rules/dystro-dev-rules.yml
- group: design
  href: https://artifacts.apis.io/dystro-dev/json-ld/dystro-dev-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dystro-dev-context.jsonld
- group: design
  href: https://artifacts.apis.io/dystro-dev/vocabulary/dystro-dev-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dystro-dev-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/dystro-dev/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/dystro-dev/data-model/dystro-dev-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dystro-dev-data-model.yml
- group: auth
  href: https://artifacts.apis.io/dystro-dev/authentication/dystro-dev-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dystro-dev-authentication.yml
- group: auth
  href: https://artifacts.apis.io/dystro-dev/scopes/dystro-dev-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/dystro-dev-scopes.yml
- group: design
  href: https://artifacts.apis.io/dystro-dev/errors/dystro-dev-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/dystro-dev-problem-types.yml
- group: design
  href: https://artifacts.apis.io/dystro-dev/conformance/dystro-dev-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dystro-dev-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dystro-dev/mcp/dystro-dev-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dystro-dev-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dystro-dev/well-known/dystro-dev-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dystro-dev-well-known.yml
- group: other
  href: https://artifacts.apis.io/dystro-dev/hosts/dystro-dev-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dystro-dev-hosts.yml
- group: other
  href: https://artifacts.apis.io/dystro-dev/vendors/dystro-dev-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dystro-dev-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dystro.dev/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dystro.dev/privacy
- group: company
  title: ''
  type: Website
  url: https://dystro.dev/
- group: auth
  href: https://artifacts.apis.io/dystro-dev/security/dystro-dev-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dystro-dev-domain-security.yml
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://app.dystro.dev/openapi.json
  - status: 401
    url: https://app.dystro.dev/api/mcp
  - status: 200
    url: https://dystro.dev/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: dystro-dev is a company that appeared in the API Evangelist harvest backlog, sourced from the mcp-registry. It currently exists in the network as a stub awaiting full profiling. Public information about dystro-dev is minimal; the company does not expose a functional website at the listed domain, and no additional documentation, developer portal, or API specifications have been discovered. The entry serves as a placeholder for future enrichment once authoritative resources become available.
image: https://artifacts.apis.io/dystro-dev/logo.png
json_schemas:
- name: CreatePostBody
  property_count: 9
  slug: dystro-dev-create-post-body
jsonld:
- class_count: 4
  name: Dystro Dev Context
  property_count: 36
  slug: dystro-dev-context
layout: provider
mcp_servers:
- description: Remote MCP server at app.dystro.dev.
  name: dystro-dev MCP Server
  slug: dystro-dev-mcp-yml
modified: '2026-10-30'
name: dystro-dev
nav: Providers
network: true
overview: 'dystro-dev publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Accounts API, Analytics API, API Keys API, and 8 more. Tagged areas include Company, Developers, Technology, and Integration.


  The dystro-dev catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dystro-dev''s developer surface includes authentication and 18 more developer resources.'
plans:
- name: Dystro Dev Plans Pricing
  plan_count: 0
  slug: dystro-dev-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 0
  name: Dystro Dev Rate Limits
  slug: dystro-dev-rate-limits
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: dystro-dev API Rules
  rule_count: 14
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 3
  slug: dystro-dev-rules
scopes:
- name: Dystro Dev Scopes
  scope_count: 6
  slug: dystro-dev-scopes
  summary_line: 6 scopes
score:
  band: thin
  composite: 30.0
  coverage:
    artifact_dirs: 30
    catalog_earned: 51.2
    catalog_earned_first_party: 0.0
    catalog_gap: 63.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -3.5
  facets:
    access_clarity: 10.5
    contract_governance: 22.0
    contract_quality: 54.4
    developer_ergonomics: 18.3
    discoverability: 56.7
    operational_transparency: 0.0
  previous_composite: 33.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 11
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/dystro-dev/dystro-dev-2026-11-03T131149.png
security:
- kind: authentication
  name: Dystro Dev Authentication
  slug: dystro-dev-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dystro Dev Domain Security
  slug: dystro-dev-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: create-post
  slug: dystro-dev-create-post
slug: dystro-dev
tags:
- Company
- Developers
- Technology
- Integration
website: https://dystro.dev/
---

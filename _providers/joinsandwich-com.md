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
  - sandbox
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
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 52.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 5
  human_in_the_loop: 0
  name: Joinsandwich Com Agentic Access
  operation_count: 17
  slug: joinsandwich-com-agentic-access
  summary_line: 17 operations · 5 acting
api_count: 1
apis:
- baseURL: https://www.joinsandwich.com
  baseurl_source: declared
  description: Firebase session helpers used by the website.
  name: joinsandwich-com Auth API
  slug: joinsandwich-com-auth-api
- baseURL: https://www.joinsandwich.com
  baseurl_source: declared
  description: Channel community threads (authenticated writes).
  name: joinsandwich-com Community API
  slug: joinsandwich-com-community-api
- baseURL: https://www.joinsandwich.com
  baseurl_source: declared
  description: Markdown representations of directory pages.
  name: joinsandwich-com Content API
  slug: joinsandwich-com-content-api
- baseURL: https://www.joinsandwich.com
  baseurl_source: declared
  description: Machine-readable indexes and catalogs.
  name: joinsandwich-com Discovery API
  slug: joinsandwich-com-discovery-api
- baseURL: https://www.joinsandwich.com
  baseurl_source: declared
  description: Public Model Context Protocol endpoint.
  name: joinsandwich-com MCP API
  slug: joinsandwich-com-mcp-api
- baseURL: https://www.joinsandwich.com
  baseurl_source: declared
  description: Public newsletter signup.
  name: joinsandwich-com Newsletter API
  slug: joinsandwich-com-newsletter-api
artifact_total: 17
common:
- group: agent
  href: https://artifacts.apis.io/joinsandwich-com/agentic-access/joinsandwich-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/joinsandwich-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/rules/joinsandwich-com-rules.yml
  title: ''
  type: Spectral
  url: rules/joinsandwich-com-rules.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/json-ld/joinsandwich-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/joinsandwich-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/vocabulary/joinsandwich-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/joinsandwich-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/joinsandwich-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/data-model/joinsandwich-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/joinsandwich-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/conventions/joinsandwich-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/joinsandwich-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/conventions/joinsandwich-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/joinsandwich-com-conventions.yml
- group: start
  href: https://artifacts.apis.io/joinsandwich-com/sandbox/joinsandwich-com-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/joinsandwich-com-sandbox.yml
- group: auth
  href: https://artifacts.apis.io/joinsandwich-com/authentication/joinsandwich-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/joinsandwich-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/errors/joinsandwich-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/joinsandwich-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/joinsandwich-com/conformance/joinsandwich-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/joinsandwich-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/joinsandwich-com/llms/joinsandwich-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/joinsandwich-com-llms.txt
- group: build
  href: https://artifacts.apis.io/joinsandwich-com/mcp/joinsandwich-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/joinsandwich-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/joinsandwich-com/mcp/joinsandwich-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/joinsandwich-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/joinsandwich-com/well-known/joinsandwich-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/joinsandwich-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/joinsandwich-com/hosts/joinsandwich-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/joinsandwich-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/joinsandwich-com/vendors/joinsandwich-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/joinsandwich-com-vendors.yml
- group: start
  title: ''
  type: GettingStarted
  url: https://inbox.lovedone.app/onboarding?utm_source=llms.txt&utm_medium=agent&utm_campaign=care_handoff
- group: docs
  title: ''
  type: Documentation
  url: https://dev.joinsandwich.com/
- group: auth
  href: https://artifacts.apis.io/joinsandwich-com/security/joinsandwich-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/joinsandwich-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://joinsandwich.com/
- group: docs
  title: ''
  type: APIReference
  url: https://www.joinsandwich.com/openapi.json
- group: company
  title: ''
  type: Blog
  url: https://www.joinsandwich.com/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.joinsandwich.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.joinsandwich.com/privacy
- group: start
  title: ''
  type: SignUp
  url: https://www.joinsandwich.com/login
created: '2026-10-30'
description: The Sandwich Generation directory (joinsandwich.com) helps individuals navigating the challenges of caring for aging parents or being part of the sandwich generation. It provides a searchable catalog of technology solutions, financial resources, employment options, and local assistance organized by category, state, and city. Users can explore tools, services, and community support to manage caregiving, finances, and work-life balance.
image: https://www.joinsandwich.com/icon.png
json_schemas:
- name: JsonRpcRequest
  property_count: 4
  slug: joinsandwich-com-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: joinsandwich-com-json-rpc-response
- name: OAuthAuthorizationServer
  property_count: 4
  slug: joinsandwich-com-oauth-authorization-server
jsonld:
- class_count: 4
  name: Joinsandwich Com Context
  property_count: 13
  slug: joinsandwich-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.joinsandwich.com.
  name: joinsandwich-com MCP Server
  slug: joinsandwich-com-mcp-yml
modified: '2026-10-30'
name: joinsandwich-com
nav: Providers
network: true
overview: 'joinsandwich-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Auth API, Community API, Content API, and 3 more. Tagged areas include Company, Directory, Caregiving, and Technology.


  The joinsandwich-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  joinsandwich-com''s developer surface includes sandbox, authentication, getting-started guide, documentation, API reference, engineering blog, signup flow, and 20 more developer resources.'
random_paper: 13
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: joinsandwich-com API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: joinsandwich-com-rules
scopes:
- name: Joinsandwich Com Scopes
  scope_count: 0
  slug: joinsandwich-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 36.7
  coverage:
    artifact_dirs: 28
    catalog_earned: 54.8
    catalog_earned_first_party: 0.0
    catalog_gap: 60.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 17.1
    contract_governance: 22.0
    contract_quality: 56.6
    developer_ergonomics: 41.0
    discoverability: 66.7
    operational_transparency: 0.0
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 30.4
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/joinsandwich-com/joinsandwich-com-2026-11-03T134228.png
security:
- kind: authentication
  name: Joinsandwich Com Authentication
  slug: joinsandwich-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Joinsandwich Com Domain Security
  slug: joinsandwich-com-domain-security
  summary_line: TLSv1.3 · HSTS
skill_count: 1
skills:
- name: search-care-resources
  slug: joinsandwich-com-search-care-resources
slug: joinsandwich-com
tags:
- Company
- Directory
- Caregiving
- Technology
website: https://joinsandwich.com/
---

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
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
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
    well_known_catalog: true
  schema_version: '0.2'
  score: 29.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 26
  human_in_the_loop: 0
  name: Hasmcp Agentic Access
  operation_count: 41
  slug: hasmcp-agentic-access
  summary_line: 41 operations · 26 acting
api_count: 1
apis:
- baseURL: https://api.hasmcp.com
  baseurl_source: declared
  description: The Providers API from HasMCP — 8 operation(s) for providers.
  name: HasMCP Providers API
  slug: hasmcp-providers-api
- baseURL: https://api.hasmcp.com
  baseurl_source: declared
  description: The Servers API from HasMCP — 11 operation(s) for servers.
  name: HasMCP Servers API
  slug: hasmcp-servers-api
- baseURL: https://api.hasmcp.com
  baseurl_source: declared
  description: The Variables API from HasMCP — 2 operation(s) for variables.
  name: HasMCP Variables API
  slug: hasmcp-variables-api
artifact_total: 17
asyncapis:
- description: ''
  name: Hasmcp Webhooks
  slug: hasmcp-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/hasmcp/agentic-access/hasmcp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/hasmcp-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/rules/hasmcp-rules.yml
  title: ''
  type: Spectral
  url: rules/hasmcp-rules.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/json-ld/hasmcp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/hasmcp-context.jsonld
- group: design
  href: https://artifacts.apis.io/hasmcp/vocabulary/hasmcp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/hasmcp-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/hasmcp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/asyncapi/hasmcp-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/hasmcp-webhooks.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/data-model/hasmcp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/hasmcp-data-model.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/conventions/hasmcp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/hasmcp-conventions.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/lifecycle/hasmcp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/hasmcp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/hasmcp/conformance/hasmcp-conformance.yml
  title: ''
  type: Conformance
  url: conformance/hasmcp-conformance.yml
- group: agent
  href: https://artifacts.apis.io/hasmcp/llms/hasmcp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/hasmcp-llms.txt
- group: other
  href: https://artifacts.apis.io/hasmcp/a2a/hasmcp-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/hasmcp-a2a.yml
- group: agent
  href: https://artifacts.apis.io/hasmcp/well-known/hasmcp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/hasmcp-well-known.yml
- group: other
  href: https://artifacts.apis.io/hasmcp/hosts/hasmcp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/hasmcp-hosts.yml
- group: other
  href: https://artifacts.apis.io/hasmcp/vendors/hasmcp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/hasmcp-vendors.yml
- group: auth
  href: https://artifacts.apis.io/hasmcp/scopes/hasmcp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/hasmcp-scopes.yml
- group: auth
  href: https://artifacts.apis.io/hasmcp/authentication/hasmcp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/hasmcp-authentication.yml
- group: auth
  href: https://artifacts.apis.io/hasmcp/security/hasmcp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/hasmcp-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://hasmcp.com/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.hasmcp.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.hasmcp.com/api-reference/providers/list-providers
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.hasmcp.com/quickstart
- group: commercial
  title: ''
  type: Pricing
  url: https://hasmcp.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://accounts.hasmcp.com/signup
- group: commercial
  title: ''
  type: TermsOfService
  url: https://hasmcp.com/tos
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://hasmcp.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://hasmcp.com/contact
- group: company
  title: ''
  type: Blog
  url: https://hasmcp.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/hasmcp
created: '2026-10-17'
description: HasMCP provides a no-code/low-code Model Context Protocol (MCP) server framework and gateway that lets developers quickly turn OpenAPI specifications into LLM‑ready API services. The platform offers a visual GUI for importing specs, managing secrets, OAuth2, and request/response interceptors without writing code or configuration files. It supports integration with popular AI IDEs and agents, includes observability, pricing tiers, and a sandbox for rapid prototyping, aiming to bridge the LLM‑to‑API gap for developers and enterprises.
image: https://hasmcp.com/assets/og-image.png
json_schemas:
- name: ListProviderPromptsResponse
  property_count: 1
  slug: hasmcp-list-provider-prompts-response
- name: ListProviderResourcesResponse
  property_count: 1
  slug: hasmcp-list-provider-resources-response
- name: ListProviderToolsResponse
  property_count: 1
  slug: hasmcp-list-provider-tools-response
- name: ListProvidersResponse
  property_count: 3
  slug: hasmcp-list-providers-response
- name: ListServerPromptsResponse
  property_count: 1
  slug: hasmcp-list-server-prompts-response
- name: ListServerResourcesResponse
  property_count: 1
  slug: hasmcp-list-server-resources-response
jsonld:
- class_count: 65
  name: Hasmcp Context
  property_count: 60
  slug: hasmcp-context
layout: provider
modified: '2026-10-17'
name: HasMCP
nav: Providers
network: true
overview: 'HasMCP publishes 3 API contracts indexed on the [APIs.io](https://apis.io/) network: Providers API, Servers API, and Variables API. Tagged areas include Company, No-Code, Low-Code, MCP, and API Gateway.


  The HasMCP catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  HasMCP''s developer surface includes authentication, documentation, API reference, getting-started guide, pricing, signup flow, support, and 22 more developer resources.'
random_paper: 12
rules:
- authorship: generated
  effective_rule_count: 90
  extends:
  - spectral:oas
  name: HasMCP API Rules
  rule_count: 49
  severity_counts:
    error: 46
    hint: 0
    info: 2
    warn: 1
  slug: hasmcp-rules
scopes:
- name: Hasmcp Scopes
  scope_count: 17
  slug: hasmcp-scopes
  summary_line: 17 scopes · authorizationCode
score:
  band: developing
  composite: 39.4
  coverage:
    artifact_dirs: 27
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.0
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 62.9
    developer_ergonomics: 31.5
    discoverability: 73.2
    operational_transparency: 10.5
  previous_composite: 48.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
    mcp: derived
    skills: derived
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
screenshot: https://apis.io/screenshots/hasmcp/hasmcp-2026-11-03T133234.png
security:
- kind: authentication
  name: Hasmcp Authentication
  slug: hasmcp-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Hasmcp Domain Security
  slug: hasmcp-domain-security
  summary_line: TLSv1.3
skill_count: 1
skills:
- name: hasmcp-create-provider-with-tool
  slug: hasmcp-create-provider-with-tool
slug: hasmcp
tags:
- Company
- No-Code
- Low-Code
- MCP
- API Gateway
website: https://hasmcp.com/
---

---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
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
    idempotency: false
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 41.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Appdeploy Ai Agentic Access
  operation_count: 3
  slug: appdeploy-ai-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://api-v2.appdeploy.ai
  baseurl_source: declared
  description: Streamable HTTP transport for MCP JSON-RPC messages
  name: appdeploy-ai MCP API
  slug: appdeploy-ai-mcp-api
- baseURL: https://api-v2.appdeploy.ai
  baseurl_source: declared
  description: RFC 8414 authorization-server metadata and RFC 9728 protected-resource metadata
  name: appdeploy-ai OAuth discovery API
  slug: appdeploy-ai-oauth-discovery-api
artifact_total: 14
common:
- group: agent
  href: https://artifacts.apis.io/appdeploy-ai/agentic-access/appdeploy-ai-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/appdeploy-ai-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/appdeploy-ai/plans/appdeploy-ai-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/appdeploy-ai-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/appdeploy-ai/rules/appdeploy-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/appdeploy-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/appdeploy-ai/json-ld/appdeploy-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/appdeploy-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/appdeploy-ai/vocabulary/appdeploy-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/appdeploy-ai-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/appdeploy-ai/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/appdeploy-ai/data-model/appdeploy-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/appdeploy-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/appdeploy-ai/errors/appdeploy-ai-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/appdeploy-ai-problem-types.yml
- group: design
  href: https://artifacts.apis.io/appdeploy-ai/conformance/appdeploy-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/appdeploy-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/appdeploy-ai/llms/appdeploy-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/appdeploy-ai-llms.txt
- group: agent
  href: https://artifacts.apis.io/appdeploy-ai/well-known/appdeploy-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/appdeploy-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/appdeploy-ai/hosts/appdeploy-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/appdeploy-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/appdeploy-ai/vendors/appdeploy-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/appdeploy-ai-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://appdeploy.ai/security
- group: operate
  title: ''
  type: ChangeLog
  url: https://appdeploy.ai/changelog
- group: auth
  href: https://artifacts.apis.io/appdeploy-ai/scopes/appdeploy-ai-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/appdeploy-ai-scopes.yml
- group: auth
  href: https://artifacts.apis.io/appdeploy-ai/authentication/appdeploy-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/appdeploy-ai-authentication.yml
- group: auth
  href: https://artifacts.apis.io/appdeploy-ai/security/appdeploy-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/appdeploy-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://appdeploy.ai/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://appdeploy.ai/developers
- group: docs
  title: ''
  type: Documentation
  url: https://appdeploy.ai/mcp-docs
- group: company
  title: ''
  type: Blog
  url: https://appdeploy.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://appdeploy.ai/pricing
- group: commercial
  title: ''
  type: TermsOfService
  url: https://appdeploy.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://appdeploy.ai/privacy
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://appdeploy.ai/openapi.json
  - status: 401
    url: https://api-v2.appdeploy.ai/mcp
  - status: 401
    url: https://api.appdeploy.ai/mcp
  - status: 403
    url: https://19a0236f8309489e80.v2.appdeploy.ai/mcp
  - status: 200
    url: https://appdeploy.ai/
  reason: partner-login
  state: gated
created: '2026-10-29'
description: AppDeploy AI provides a platform that enables developers to deploy applications directly from AI assistants like ChatGPT and Claude. Users can create, configure, and launch apps without traditional setup or hosting decisions, leveraging AI-generated code and instant deployment URLs. The service offers features such as an AI App Builder, a gallery of example apps, pricing plans, security controls, and extensive documentation to guide developers of all skill levels.
image: https://appdeploy.ai/assets/og-image.BZMnj8tZ.png
json_schemas:
- name: AuthorizationServerMetadata
  property_count: 8
  slug: appdeploy-ai-authorization-server-metadata
- name: JsonRpcRequest
  property_count: 4
  slug: appdeploy-ai-json-rpc-request
- name: JsonRpcResponse
  property_count: 4
  slug: appdeploy-ai-json-rpc-response
- name: ProtectedResourceMetadata
  property_count: 4
  slug: appdeploy-ai-protected-resource-metadata
jsonld:
- class_count: 6
  name: Appdeploy Ai Context
  property_count: 21
  slug: appdeploy-ai-context
layout: provider
modified: '2026-10-29'
name: appdeploy-ai
nav: Providers
network: true
overview: 'appdeploy-ai publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: MCP API and OAuth discovery API. Tagged areas include Company, Artificial Intelligence, Deployment, Platform, and Low-Code.


  The appdeploy-ai catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  appdeploy-ai''s developer surface includes changelog, authentication, documentation, engineering blog, pricing, and 20 more developer resources.'
plans:
- name: Appdeploy Ai Plans Pricing
  plan_count: 3
  slug: appdeploy-ai-plans-pricing
random_paper: 21
rules:
- authorship: generated
  effective_rule_count: 55
  extends:
  - spectral:oas
  name: appdeploy-ai API Rules
  rule_count: 14
  severity_counts:
    error: 12
    hint: 0
    info: 1
    warn: 1
  slug: appdeploy-ai-rules
scopes:
- name: Appdeploy Ai Scopes
  scope_count: 3
  slug: appdeploy-ai-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: developing
  composite: 44.2
  coverage:
    artifact_dirs: 23
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 47.4
    contract_governance: 22.0
    contract_quality: 64.1
    developer_ergonomics: 29.0
    discoverability: 73.2
    operational_transparency: 13.2
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 51.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
    mcp: derived
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 28.2
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/appdeploy-ai/appdeploy-ai-2026-11-03T121023.png
security:
- kind: authentication
  name: Appdeploy Ai Authentication
  slug: appdeploy-ai-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Appdeploy Ai Domain Security
  slug: appdeploy-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: mcp
  slug: appdeploy-ai-mcp
slug: appdeploy-ai
tags:
- Company
- Artificial Intelligence
- Deployment
- Platform
- Low-Code
- Automation
website: https://appdeploy.ai/
---

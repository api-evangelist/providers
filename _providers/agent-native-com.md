---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
    well_known_catalog: false
  schema_version: '0.2'
  score: 38.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Agent Native Com Agentic Access
  operation_count: 3
  slug: agent-native-com-agentic-access
  summary_line: 3 operations · 1 acting
api_count: 1
apis:
- baseURL: https://www.agent-native.com
  baseurl_source: declared
  description: The Desktop API from agent-native-com — 2 operation(s) for desktop.
  name: agent-native-com Desktop API
  slug: agent-native-com-desktop-api
- baseURL: https://www.agent-native.com
  baseurl_source: declared
  description: The MCP API from agent-native-com — 1 operation(s) for mcp.
  name: agent-native-com MCP API
  slug: agent-native-com-mcp-api
artifact_total: 13
common:
- group: agent
  href: https://artifacts.apis.io/agent-native-com/agentic-access/agent-native-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/agent-native-com-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/agent-native-com/rules/agent-native-com-rules.yml
  title: ''
  type: Spectral
  url: rules/agent-native-com-rules.yml
- group: design
  href: https://artifacts.apis.io/agent-native-com/json-ld/agent-native-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agent-native-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/agent-native-com/vocabulary/agent-native-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agent-native-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/agent-native-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/agent-native-com/data-model/agent-native-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agent-native-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/agent-native-com/authentication/agent-native-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/agent-native-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/agent-native-com/errors/agent-native-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/agent-native-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/agent-native-com/conformance/agent-native-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agent-native-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agent-native-com/llms/agent-native-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agent-native-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/agent-native-com/well-known/agent-native-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agent-native-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/agent-native-com/hosts/agent-native-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agent-native-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/agent-native-com/vendors/agent-native-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agent-native-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agent-native-com/security/agent-native-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agent-native-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agent-native.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agent-native.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agent-native.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.agent-native.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agent-native.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://www.agent-native.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agent-native.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agent-native.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agent-native.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BuilderIO/agent-native
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.agent-native.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.agent-native.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://www.agent-native.com/openapi.json
- group: start
  title: ''
  type: GettingStarted
  url: https://www.agent-native.com/docs/
- group: operate
  title: ''
  type: Support
  url: https://www.agent-native.com/contact/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.agent-native.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.agent-native.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.agent-native.com/privacy/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/BuilderIO/agent-native
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://api.agent-native.com/openapi.json
  - status: null
    url: https://agent-native.com/openapi.json
  - status: null
    url: https://ws.agent-native.com/openapi.json
  - status: null
    url: https://apidocs.agent-native.com/openapi.json
  - status: null
    url: https://api-docs.agent-native.com/openapi.json
  - status: 401
    url: https://api.agent-native.com/mcp
  reason: partner-login
  state: gated
created: '2026-10-29'
description: Agent-Native is an open-source framework for building applications where AI agents and user interfaces share a single state model. It provides a developer-friendly platform with built-in authentication, MCP protocol support, and a rich set of example apps. The framework is maintained by Builder.io and enables developers to create agentic apps, expose actions via a typed OpenAPI, and integrate with external AI services. Documentation, pricing, and support resources are publicly available.
image: https://cdn.builder.io/api/v1/image/assets%2FYJIGb4i01jvw0SRdL5Bt%2F9ff332b274a147229544c2bf5877a10d
json_schemas:
- name: DesktopDownloadManifest
  property_count: 5
  slug: agent-native-com-desktop-download-manifest
- name: McpJsonRpcRequest
  property_count: 4
  slug: agent-native-com-mcp-json-rpc-request
- name: McpJsonRpcResponse
  property_count: 4
  slug: agent-native-com-mcp-json-rpc-response
jsonld:
- class_count: 6
  name: Agent Native Com Context
  property_count: 18
  slug: agent-native-com-context
layout: provider
modified: '2026-10-29'
name: agent-native-com
nav: Providers
network: true
overview: 'agent-native-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network: Desktop API and MCP API. Tagged areas include Company, Artificial Intelligence, AI Agents, Framework, and Open Source.


  The agent-native-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  agent-native-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, pricing, and 27 more developer resources.'
plans:
- name: Agent Native Com Plans Pricing
  plan_count: 0
  slug: agent-native-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: agent-native-com API Rules
  rule_count: 12
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 0
  slug: agent-native-com-rules
score:
  band: thin
  composite: 38.3
  coverage:
    artifact_dirs: 23
    catalog_earned: 62.0
    catalog_earned_first_party: 0.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -8.3
  facets:
    access_clarity: 15.8
    contract_governance: 33.3
    contract_quality: 62.6
    developer_ergonomics: 39.8
    discoverability: 73.2
    operational_transparency: 2.6
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 46.6
  provenance:
    agentic_access: derived
    conformance: first-party
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
    score: 19.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/agent-native-com/agent-native-com-2026-11-03T120345.png
security:
- kind: authentication
  name: Agent Native Com Authentication
  slug: agent-native-com-authentication
  summary_line: 3 schemes
- kind: domain-security
  name: Agent Native Com Domain Security
  slug: agent-native-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 2
skills:
- name: get-desktop-download-manifest
  slug: agent-native-com-get-desktop-download-manifest
- name: resolve-desktop-updater-asset
  slug: agent-native-com-resolve-desktop-updater-asset
slug: agent-native-com
tags:
- Company
- Artificial Intelligence
- AI Agents
- Framework
- Open Source
- Developer Tools
website: https://agent-native.com/
---

---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: conformant
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 27.2
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Manage your unstructured data with Roe API
  name: Roe API
  slug: roe-api
- baseURL: https://api.roe-ai.com
  baseurl_source: declared
  description: 'Roe AI API as documented publicly: 45 operations. Contract generated from the documentation by API Evangelist (2026-10-29); not the provider''s own document.'
  name: Roe AI API
  slug: roe-ai-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/roe-ai/rules/roe-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/roe-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/roe-ai/json-ld/roe-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/roe-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/roe-ai/vocabulary/roe-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/roe-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/roe-ai/data-model/roe-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/roe-ai-data-model.yml
- group: auth
  href: https://artifacts.apis.io/roe-ai/authentication/roe-ai-authentication.yml
  title: ''
  type: Authentication
  url: authentication/roe-ai-authentication.yml
- group: design
  href: https://artifacts.apis.io/roe-ai/conformance/roe-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/roe-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/roe-ai/llms/roe-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/roe-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/roe-ai/a2a/roe-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/roe-ai-a2a.yml
- group: build
  href: https://artifacts.apis.io/roe-ai/mcp/roe-ai-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/roe-ai-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/roe-ai/mcp/roe-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/roe-ai-mcp.yml
- group: other
  href: https://artifacts.apis.io/roe-ai/hosts/roe-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/roe-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/roe-ai/vendors/roe-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/roe-ai-vendors.yml
- group: build
  href: https://artifacts.apis.io/roe-ai/packages/roe-ai-packages.yml
  title: ''
  type: SDKs
  url: packages/roe-ai-packages.yml
- group: build
  href: https://artifacts.apis.io/roe-ai/packages/roe-ai-packages.yml
  title: ''
  type: Packages
  url: packages/roe-ai-packages.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.roe-ai.com/changelog
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.roe-ai.com
- group: auth
  href: https://artifacts.apis.io/roe-ai/security/roe-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/roe-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.roe-ai.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.roe-ai.com
- group: docs
  title: ''
  type: APIReference
  url: https://docs.roe-ai.com/api-reference/introduction
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.roe-ai.com/quickstart
- group: operate
  title: ''
  type: Support
  url: https://www.roe-ai.com/support
- group: company
  title: ''
  type: Blog
  url: https://roeai.substack.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/roe-ai
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.roe-ai.com/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.roe-ai.com/privacy
coverage:
  checked: '2026-10-29'
  detail: The provider's documentation is markdown but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contract is published.
  evidence:
  - status: 200
    url: https://docs.roe-ai.com/api-reference/introduction.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-29'
description: Roe AI provides an agentic fraud and AML investigation platform that leverages artificial intelligence to automate data collection, analysis, and risk scoring across multiple data sources. Its product suite includes the Rori Agent OS for real‑time transaction monitoring, Atlas Knowledge Base for contextual data enrichment, and Prism Risk Score for comprehensive risk assessment. Designed for financial institutions, fintechs, and compliance teams, Roe AI enables faster, more accurate investigations while reducing manual effort and operational costs.
image: https://www.roe-ai.com/og-image.png
json_schemas:
- name: GetV1AgentsAgentidJobsResponse
  property_count: 14
  slug: roe-ai-get-v1-agents-agentid-jobs-response
- name: GetV1AgentsResponse
  property_count: 4
  slug: roe-ai-get-v1-agents-response
- name: GetV1DatabaseQueryQueryidResultResponse
  property_count: 4
  slug: roe-ai-get-v1-database-query-queryid-result-response
- name: PostV1AgentsAgentidDuplicateResponse
  property_count: 15
  slug: roe-ai-post-v1-agents-agentid-duplicate-response
- name: PostV1AgentsResponse
  property_count: 15
  slug: roe-ai-post-v1-agents-response
- name: PutV1AgentsAgentidResponse
  property_count: 15
  slug: roe-ai-put-v1-agents-agentid-response
jsonld:
- class_count: 60
  name: Roe Ai Context
  property_count: 85
  slug: roe-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.roe-ai.com.
  name: Roe AI MCP Server
  slug: roe-ai-mcp-yml
modified: '2026-10-29'
name: Roe AI
nav: Providers
network: true
overview: 'Roe AI is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, FraudDetection, AML, and FinTech.


  The Roe AI catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Roe AI''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, engineering blog, and 19 more developer resources.'
plans:
- name: Roe Ai Plans Pricing
  plan_count: 0
  slug: roe-ai-plans-pricing
random_paper: 21
rate_limits:
- limit_count: 0
  name: Roe Ai Rate Limits
  slug: roe-ai-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Roe AI API Rules
  rule_count: 12
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 2
  slug: roe-ai-rules
scopes:
- name: Roe Ai Scopes
  scope_count: 0
  slug: roe-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 38.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 21.1
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 64.3
    discoverability: 65.0
    operational_transparency: 21.1
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
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
  name: Roe Ai Authentication
  slug: roe-ai-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Roe Ai Domain Security
  slug: roe-ai-domain-security
  summary_line: TLSv1.3
slug: roe-ai
tags:
- Company
- AI
- FraudDetection
- AML
- FinTech
- DataAnalytics
website: https://www.roe-ai.com
---

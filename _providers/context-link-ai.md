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
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 35.1
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Complete reference for the Context Link API.
  name: Context Link API
  slug: context-link-api
- baseURL: https://context-link.ai
  baseurl_source: declared
  description: 'Context Link API as documented publicly: 34 operations. Contract generated from the documentation by API Evangelist (2026-11-04); not the provider''s own document.'
  name: Context Link API
  slug: context-link-ai-api
artifact_total: 12
common:
- group: design
  href: https://artifacts.apis.io/context-link-ai/rules/context-link-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/context-link-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/context-link-ai/json-ld/context-link-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/context-link-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/context-link-ai/vocabulary/context-link-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/context-link-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/context-link-ai/data-model/context-link-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/context-link-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/context-link-ai/conformance/context-link-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/context-link-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/context-link-ai/mcp/context-link-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/context-link-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/context-link-ai/well-known/context-link-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/context-link-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/context-link-ai/hosts/context-link-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/context-link-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/context-link-ai/vendors/context-link-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/context-link-ai-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.context-link.ai/terms_of_service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.context-link.ai/privacy_policy
- group: start
  title: ''
  type: GettingStarted
  url: https://www.context-link.ai/docs?tag=getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Context-Link
- group: auth
  href: https://artifacts.apis.io/context-link-ai/security/context-link-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/context-link-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.context-link.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://www.context-link.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://www.context-link.ai/docs/api-reference
- group: company
  title: ''
  type: Blog
  url: https://www.context-link.ai/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.context-link.ai/#pricing
- group: company
  title: ''
  type: About
  url: https://www.context-link.ai/about
coverage:
  checked: '2026-11-04'
  detail: The API reference provides only markdown documentation with base URL but no OpenAPI or other machine‑readable contract.
  evidence:
  - status: 200
    url: https://www.context-link.ai/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-11-04'
description: Context Link provides a platform that connects a business’s disparate data sources, enabling AI models like ChatGPT and Claude to query across systems and deliver source‑backed answers. By unifying data silos, it helps enterprises unlock AI‑driven insights and automate interactions, positioning AI as a conversational interface for business operations.
image: https://www.context-link.ai/assets/logo-0ab0c075.png
json_schemas:
- name: GetApiAccountsResponse
  property_count: 15
  slug: context-link-ai-get-api-accounts-response
- name: GetApiAccountsUidResponse
  property_count: 13
  slug: context-link-ai-get-api-accounts-uid-response
- name: GetApiV1ApiAccountsUidConnectionsConnectionuidResponse
  property_count: 9
  slug: context-link-ai-get-api-v1-api-accounts-uid-connections-connectionuid-response
- name: GetContextResponse
  property_count: 16
  slug: context-link-ai-get-context-response
- name: GetQuestionResponse
  property_count: 16
  slug: context-link-ai-get-question-response
- name: GetQWhatIsPricingResponse
  property_count: 6
  slug: context-link-ai-get-qwhat-is-pricing-response
jsonld:
- class_count: 24
  name: Link Ai Context
  property_count: 53
  slug: context-link-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at api.context-link.ai.
  name: Context Link MCP Server
  slug: context-link-ai-mcp-yml
modified: '2026-11-04'
name: Context Link
nav: Providers
network: true
overview: 'Context Link is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Data Integration, Enterprise, Platform, and Automation.


  The Context Link catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Context Link''s developer surface includes getting-started guide, documentation, API reference, engineering blog, pricing, and 15 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 85
  extends:
  - spectral:oas
  name: Context Link API Rules
  rule_count: 44
  severity_counts:
    error: 39
    hint: 0
    info: 4
    warn: 1
  slug: context-link-ai-rules
score:
  band: thin
  composite: 30.1
  coverage:
    artifact_dirs: 14
    catalog_earned: 62.8
    catalog_earned_first_party: 0.0
    catalog_gap: 52.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 31.6
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 31.0
    discoverability: 65.0
    operational_transparency: 5.3
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 1
      marker_coverage: 100.0
      total: 1
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Context Link Ai Domain Security
  slug: context-link-ai-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: context-link-ai
tags:
- Artificial Intelligence
- Data Integration
- Enterprise
- Platform
- Automation
- Company
website: https://www.context-link.ai/
---

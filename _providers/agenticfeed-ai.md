---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Open access
  onboarding: open
  pricing: unknown
  public: true
  source:
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: flavored
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
  score: 24.9
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: Query ecommerce product data by natural language buyer intent.
  name: Agent Query API
  slug: agent-query-api
- description: 'Agenticfeed API as documented publicly: 6 operations. Contract generated from the documentation by API Evangelist (2026-11-01); not the provider''s own document.'
  name: Agenticfeed API
  slug: agenticfeed-ai-api
artifact_total: 14
common:
- group: design
  href: https://artifacts.apis.io/agenticfeed-ai/rules/agenticfeed-ai-rules.yml
  title: ''
  type: Spectral
  url: rules/agenticfeed-ai-rules.yml
- group: design
  href: https://artifacts.apis.io/agenticfeed-ai/json-ld/agenticfeed-ai-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/agenticfeed-ai-context.jsonld
- group: design
  href: https://artifacts.apis.io/agenticfeed-ai/vocabulary/agenticfeed-ai-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/agenticfeed-ai-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/agenticfeed-ai/data-model/agenticfeed-ai-data-model.yml
  title: ''
  type: DataModel
  url: data-model/agenticfeed-ai-data-model.yml
- group: design
  href: https://artifacts.apis.io/agenticfeed-ai/conformance/agenticfeed-ai-conformance.yml
  title: ''
  type: Conformance
  url: conformance/agenticfeed-ai-conformance.yml
- group: agent
  href: https://artifacts.apis.io/agenticfeed-ai/llms/agenticfeed-ai-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/agenticfeed-ai-llms.txt
- group: other
  href: https://artifacts.apis.io/agenticfeed-ai/a2a/agenticfeed-ai-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/agenticfeed-ai-a2a.yml
- group: agent
  href: https://artifacts.apis.io/agenticfeed-ai/mcp/agenticfeed-ai-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/agenticfeed-ai-mcp.yml
- group: agent
  href: https://artifacts.apis.io/agenticfeed-ai/well-known/agenticfeed-ai-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/agenticfeed-ai-well-known.yml
- group: other
  href: https://artifacts.apis.io/agenticfeed-ai/hosts/agenticfeed-ai-hosts.yml
  title: ''
  type: Hosts
  url: hosts/agenticfeed-ai-hosts.yml
- group: other
  href: https://artifacts.apis.io/agenticfeed-ai/vendors/agenticfeed-ai-vendors.yml
  title: ''
  type: Vendors
  url: vendors/agenticfeed-ai-vendors.yml
- group: auth
  href: https://artifacts.apis.io/agenticfeed-ai/security/agenticfeed-ai-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/agenticfeed-ai-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://agenticfeed.ai/
- group: docs
  title: ''
  type: Documentation
  url: https://agenticfeed.ai/docs
- group: docs
  title: ''
  type: APIReference
  url: https://agenticfeed.ai/api.html
- group: operate
  title: ''
  type: Support
  url: https://agenticfeed.ai/faq.html
- group: company
  title: ''
  type: Blog
  url: https://agenticfeed.ai/blog.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/bluestratus
- group: commercial
  title: ''
  type: Pricing
  url: https://agenticfeed.ai/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://agenticfeed.ai/login.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://agenticfeed.ai/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://agenticfeed.ai/privacy
created: '2026-11-01'
description: Agenticfeed.ai helps brands and retailers expose structured, machine-readable product feeds for AI agents to discover, compare and buy products. It offers starter, growth, scale, and enterprise plans, providing AI intent packs and product listings to make commerce AI-ready.
image: https://agenticfeed.ai/og.png
json_schemas:
- name: GetFeedCustomerGuidJsonResponse
  property_count: 7
  slug: agenticfeed-ai-get-feed-customer-guid-json-response
- name: GetProductCustomerguidProductGuidJsonResponse
  property_count: 12
  slug: agenticfeed-ai-get-product-customerguid-product-guid-json-response
- name: GetQuestionsCustomerGuidJsonResponse
  property_count: 4
  slug: agenticfeed-ai-get-questions-customer-guid-json-response
- name: GetQuestionsCustomerguidCategoryJsonResponse
  property_count: 6
  slug: agenticfeed-ai-get-questions-customerguid-category-json-response
- name: PostAgentQueryRequest
  property_count: 3
  slug: agenticfeed-ai-post-agent-query-request
- name: PostAgentQueryResponse
  property_count: 5
  slug: agenticfeed-ai-post-agent-query-response
jsonld:
- class_count: 6
  name: Agenticfeed Ai Context
  property_count: 22
  slug: agenticfeed-ai-context
layout: provider
mcp_servers:
- description: Remote MCP server at agenticfeed.ai.
  name: Agenticfeed MCP Server
  slug: agenticfeed-ai-mcp-yml
modified: '2026-11-01'
name: Agenticfeed
nav: Providers
network: true
overview: 'Agenticfeed is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Artificial Intelligence, Commerce, Product Feeds, Retail, and Software-as-a-Service.


  The Agenticfeed catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Agenticfeed''s developer surface includes documentation, API reference, support, engineering blog, pricing, signup flow, and 16 more developer resources.'
random_paper: 14
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: Agenticfeed API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: agenticfeed-ai-rules
scopes:
- name: Agenticfeed Ai Scopes
  scope_count: 0
  slug: agenticfeed-ai-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 26
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 25.7
    developer_ergonomics: 11.9
    discoverability: 56.7
    operational_transparency: 2.6
  previous_composite: 30.8
  provenance:
    conformance: derived
    contracts:
      callable: 0.0
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
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Agenticfeed Ai Authentication
  slug: agenticfeed-ai-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Agenticfeed Ai Domain Security
  slug: agenticfeed-ai-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: agenticfeed-ai
tags:
- Artificial Intelligence
- Commerce
- Product Feeds
- Retail
- Software-as-a-Service
website: https://agenticfeed.ai/
---

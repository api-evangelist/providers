---
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: near-conformant
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 32.4
  scored_at: '2026-10-31'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Anthonyhunts Com Agentic Access
  operation_count: 7
  slug: anthonyhunts-com-agentic-access
  summary_line: 7 operations · 2 acting
api_count: 1
apis:
- baseURL: https://www.anthonyhunts.com
  baseurl_source: declared
  description: The batch API from anthonyhunts-com — 1 operation(s) for batch.
  name: anthonyhunts-com Batch API
  slug: anthonyhunts-com-batch-api
- baseURL: https://www.anthonyhunts.com
  baseurl_source: declared
  description: The contact API from anthonyhunts-com — 1 operation(s) for contact.
  name: anthonyhunts-com Contact API
  slug: anthonyhunts-com-contact-api
- baseURL: https://www.anthonyhunts.com
  baseurl_source: declared
  description: The content API from anthonyhunts-com — 2 operation(s) for content.
  name: anthonyhunts-com Content API
  slug: anthonyhunts-com-content-api
- baseURL: https://www.anthonyhunts.com
  baseurl_source: declared
  description: The pricing API from anthonyhunts-com — 1 operation(s) for pricing.
  name: anthonyhunts-com Pricing API
  slug: anthonyhunts-com-pricing-api
- baseURL: https://www.anthonyhunts.com
  baseurl_source: declared
  description: The search API from anthonyhunts-com — 1 operation(s) for search.
  name: anthonyhunts-com Search API
  slug: anthonyhunts-com-search-api
- baseURL: https://www.anthonyhunts.com
  baseurl_source: declared
  description: The services API from anthonyhunts-com — 1 operation(s) for services.
  name: anthonyhunts-com Services API
  slug: anthonyhunts-com-services-api
artifact_total: 18
common:
- group: agent
  href: https://artifacts.apis.io/anthonyhunts-com/agentic-access/anthonyhunts-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/anthonyhunts-com-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/anthonyhunts-com/plans/anthonyhunts-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/anthonyhunts-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/anthonyhunts-com/rules/anthonyhunts-com-rules.yml
  title: ''
  type: Spectral
  url: rules/anthonyhunts-com-rules.yml
- group: design
  href: https://artifacts.apis.io/anthonyhunts-com/json-ld/anthonyhunts-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/anthonyhunts-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/anthonyhunts-com/vocabulary/anthonyhunts-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/anthonyhunts-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/anthonyhunts-com/data-model/anthonyhunts-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/anthonyhunts-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/anthonyhunts-com/errors/anthonyhunts-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/anthonyhunts-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/anthonyhunts-com/conformance/anthonyhunts-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/anthonyhunts-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/anthonyhunts-com/llms/anthonyhunts-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/anthonyhunts-com-llms.txt
- group: other
  href: https://artifacts.apis.io/anthonyhunts-com/a2a/anthonyhunts-com-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/anthonyhunts-com-a2a.yml
- group: build
  href: https://artifacts.apis.io/anthonyhunts-com/mcp/anthonyhunts-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/anthonyhunts-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/anthonyhunts-com/mcp/anthonyhunts-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/anthonyhunts-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/anthonyhunts-com/well-known/anthonyhunts-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/anthonyhunts-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/anthonyhunts-com/hosts/anthonyhunts-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/anthonyhunts-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/anthonyhunts-com/vendors/anthonyhunts-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/anthonyhunts-com-vendors.yml
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.anthonyhunts.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://www.anthonyhunts.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.anthonyhunts.com/blog
- group: docs
  title: ''
  type: APIReference
  url: https://www.anthonyhunts.com/developers
- group: auth
  href: https://artifacts.apis.io/anthonyhunts-com/security/anthonyhunts-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/anthonyhunts-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://anthonyhunts.com/
created: '2026-10-29'
description: Anthony Hunt runs SHAART Agency, offering marketing and AI automation services in Puerto Rico and Texas. The company provides AI-driven sales pipelines, chatbot agents, automated workflows, and digital advertising solutions for Latin American businesses in the US. It maintains a blog with case studies, guides, and industry insights, and offers consulting, CRM integration, and custom AI agent development to improve lead generation and customer engagement.
image: https://www.anthonyhunts.com/anthony.png
json_schemas:
- name: AskRequest
  property_count: 4
  slug: anthonyhunts-com-ask-request
- name: AskResponse
  property_count: 4
  slug: anthonyhunts-com-ask-response
- name: BatchRequest
  property_count: 1
  slug: anthonyhunts-com-batch-request
- name: BatchResponse
  property_count: 1
  slug: anthonyhunts-com-batch-response
- name: Contact
  property_count: 10
  slug: anthonyhunts-com-contact
- name: PricingResponse
  property_count: 4
  slug: anthonyhunts-com-pricing-response
jsonld:
- class_count: 12
  name: Anthonyhunts Com Context
  property_count: 47
  slug: anthonyhunts-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at www.anthonyhunts.com.
  name: anthonyhunts-com MCP Server
  slug: anthonyhunts-com-mcp-yml
modified: '2026-10-29'
name: anthonyhunts-com
nav: Providers
network: true
overview: 'anthonyhunts-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Batch API, Contact API, Content API, and 3 more. Tagged areas include Company, Marketing, AI, Automation, and LatinAmerica.


  The anthonyhunts-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  anthonyhunts-com''s developer surface includes pricing, engineering blog, API reference, and 18 more developer resources.'
plans:
- name: Anthonyhunts Com Plans Pricing
  plan_count: 7
  slug: anthonyhunts-com-plans-pricing
random_paper: 15
rules:
- authorship: generated
  effective_rule_count: 56
  extends:
  - spectral:oas
  name: anthonyhunts-com API Rules
  rule_count: 15
  severity_counts:
    error: 13
    hint: 0
    info: 1
    warn: 1
  slug: anthonyhunts-com-rules
score:
  band: thin
  composite: 36.5
  coverage:
    artifact_dirs: 18
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 52.6
    contract_governance: 22.0
    contract_quality: 60.7
    developer_ergonomics: 9.5
    discoverability: 65.0
    operational_transparency: 0.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Anthonyhunts Com Domain Security
  slug: anthonyhunts-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: anthonyhunts-com
tags:
- Company
- Marketing
- AI
- Automation
- LatinAmerica
- US
website: https://anthonyhunts.com/
---

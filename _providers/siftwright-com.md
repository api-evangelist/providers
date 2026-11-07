---
access_model:
  confidence: low
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 17.1
  scored_at: '2026-11-06'
api_count: 1
apis:
- description: Web data endpoints for developers and AI agents.
  name: Siftwright API
  slug: siftwright-api
- baseURL: https://siftwright.com
  baseurl_source: declared
  description: 'Plans: Starter $29/month (10,000 results), Pro $99/month (50,000 results), Business $299/month (250,000 results), Enterprise $999/month (1,500,000 results). Rate limit 60 requests per minute per key. '
  name: Siftwright API API
  slug: siftwright-api-api
artifact_total: 8
common:
- group: design
  href: https://artifacts.apis.io/siftwright-com/rules/siftwright-com-rules.yml
  title: ''
  type: Spectral
  url: rules/siftwright-com-rules.yml
- group: design
  href: https://artifacts.apis.io/siftwright-com/json-ld/siftwright-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/siftwright-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/siftwright-com/vocabulary/siftwright-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/siftwright-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/siftwright-com/conformance/siftwright-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/siftwright-com-conformance.yml
- group: commercial
  href: https://artifacts.apis.io/siftwright-com/plans/siftwright-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/siftwright-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/siftwright-com/data-model/siftwright-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/siftwright-com-data-model.yml
- group: operate
  href: https://artifacts.apis.io/siftwright-com/changelog/siftwright-com-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/siftwright-com-changelog.yml
- group: design
  href: https://artifacts.apis.io/siftwright-com/errors/siftwright-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/siftwright-com-problem-types.yml
- group: agent
  href: https://artifacts.apis.io/siftwright-com/llms/siftwright-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/siftwright-com-llms.txt
- group: build
  href: https://artifacts.apis.io/siftwright-com/mcp/siftwright-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/siftwright-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/siftwright-com/mcp/siftwright-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/siftwright-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/siftwright-com/hosts/siftwright-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/siftwright-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/siftwright-com/vendors/siftwright-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/siftwright-com-vendors.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://siftwright.com/changelog/
- group: auth
  href: https://artifacts.apis.io/siftwright-com/security/siftwright-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/siftwright-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://siftwright.com/
- group: docs
  title: ''
  type: Documentation
  url: https://siftwright.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://siftwright.com/api/
- group: commercial
  title: ''
  type: Pricing
  url: https://siftwright.com/pricing/
- group: company
  title: ''
  type: Blog
  url: https://siftwright.com/blog/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://siftwright.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://siftwright.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://siftwright.com/about/
created: '2026-10-31'
description: Siftwright provides a suite of web data APIs for developers and AI agents, offering tools such as YouTube transcript extraction, website screenshots, Google News search, PDF rendering, contact detail extraction, app store reviews, tech stack detection, job listings, WHOIS/DNS lookup, and post‑quantum TLS scans. All services are accessible via a single REST API key with pay‑per‑result pricing, and include robust error handling and free failed‑request credits. The platform emphasizes clean JSON responses, easy integration, and supports both direct REST calls and MCP (Managed Cloud Proxy) for AI agent workflows.
image: https://siftwright.com/og/home.png
json_schemas:
- name: Result
  property_count: 5
  slug: siftwright-com-result
jsonld:
- class_count: 3
  name: Siftwright Com Context
  property_count: 11
  slug: siftwright-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at siftwright.com requiring an API key.
  name: siftwright-com MCP Server
  slug: siftwright-com-mcp-yml
modified: '2026-10-31'
name: siftwright-com
nav: Providers
network: true
overview: 'siftwright-com publishes 2 API contracts indexed on the [APIs.io](https://apis.io/) network, including Siftwright API API, and 1 more. Tagged areas include Company, Data, Artificial Intelligence, and Web Data.


  The siftwright-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  siftwright-com''s developer surface includes changelog, documentation, API reference, pricing, engineering blog, support, and 17 more developer resources.'
plans:
- name: Siftwright Com Plans Pricing
  plan_count: 4
  slug: siftwright-com-plans-pricing
random_paper: 23
rules:
- authorship: generated
  effective_rule_count: 59
  extends:
  - spectral:oas
  name: siftwright-com API Rules
  rule_count: 18
  severity_counts:
    error: 17
    hint: 0
    info: 1
    warn: 0
  slug: siftwright-com-rules
score:
  band: thin
  composite: 31.2
  coverage:
    artifact_dirs: 21
    catalog_earned: 62.4
    catalog_earned_first_party: 12.0
    catalog_gap: 52.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.9
  facets:
    access_clarity: 47.4
    contract_governance: 19.7
    contract_quality: 41.9
    developer_ergonomics: 11.9
    discoverability: 56.7
    operational_transparency: 7.9
  previous_composite: 39.1
  provenance:
    conformance: derived
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 13.6
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/siftwright-com/siftwright-com-2026-11-03T143150.png
security:
- kind: domain-security
  name: Siftwright Com Domain Security
  slug: siftwright-com-domain-security
  summary_line: TLSv1.3 · HSTS
slug: siftwright-com
tags:
- Company
- Data
- Artificial Intelligence
- Web Data
website: https://siftwright.com/
---

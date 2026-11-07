---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: derived
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.3
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Traceable Agentic Access
  operation_count: 3
  slug: traceable-agentic-access
  summary_line: 3 operations · 2 acting
api_count: 1
apis:
- description: Traceable provides an intelligent API security platform offering API discovery, threat detection and protection, and API security testing. It uses distributed tracing and context-aware AI to understan
  name: Traceable API Security Platform
  slug: traceable-platform
- description: Traceable Active Security Testing (AST) provides automated API security testing with GraphQL-based configuration for scan creation, suite management, and CI/CD pipeline integration. Supports GitHub Ac
  name: Traceable Active Security Testing
  slug: traceable-ast
- baseURL: https://api.traceable.ai
  baseurl_source: declared
  description: Download OpenAPI, WSDL, and other API specification files generated from discovered traffic.
  name: Traceable Specifications API
  slug: traceable-specifications-api
- baseURL: https://api.traceable.ai
  baseurl_source: declared
  description: Execute GraphQL queries against the Traceable platform for advanced analytics, entity queries, and bulk data retrieval.
  name: Traceable Graph QL API
  slug: traceable-graph-ql-api
artifact_total: 23
collections:
- collection_type: open
  name: Traceable Platform GraphQL API
  slug: open-traceable-graphql-api
- collection_type: open
  name: Traceable Platform API
  slug: open-traceable-platform
- collection_type: open
  name: Traceable Platform GraphQL Specifications API
  slug: open-traceable-specifications-api
common:
- group: commercial
  href: https://artifacts.apis.io/traceable/plans/traceable-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/traceable-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/traceable/rate-limits/traceable-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/traceable-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/traceable/finops/traceable-finops.yml
  title: ''
  type: FinOps
  url: finops/traceable-finops.yml
- group: agent
  href: https://artifacts.apis.io/traceable/agentic-access/traceable-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/traceable-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/traceable/security/traceable-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/traceable-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/traceable/security/traceable-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/traceable-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/traceable/authentication/traceable-authentication.yml
  title: ''
  type: Authentication
  url: authentication/traceable-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.traceable.ai
- group: docs
  title: ''
  type: Documentation
  url: https://docs.traceable.ai
- group: company
  title: ''
  type: Blog
  url: https://www.traceable.ai/blog
- group: company
  title: ''
  type: About
  url: https://www.traceable.ai/company
- group: operate
  title: ''
  type: Contact
  url: https://www.traceable.ai/contact
- group: start
  title: ''
  type: Demo
  url: https://www.traceable.ai/request-demo
- group: company
  title: ''
  type: Partners
  url: https://www.traceable.ai/partners
- group: other
  title: ''
  type: Resources
  url: https://www.traceable.ai/resources
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/traboraceable/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/ATraceableAI
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Traceableai
- group: agent
  title: ''
  type: MCPServer
  url: https://docs.traceable.ai/docs/traceable-mcp-server
created: '2025-01-08'
description: Traceable is an API security and observability platform that provides API discovery, threat detection, and protection across the full application lifecycle. It uses context-aware AI to detect and block API-based attacks while providing deep visibility into API behavior and risk. Traceable exposes public GraphQL APIs for configuration, analytics, and operational data access, as well as an MCP server with 12 tools for AI-assisted security workflows.
examples:
- key_count: 2
  name: Traceable Download Api Spec Example
  slug: traceable-download-api-spec-example
- key_count: 2
  name: Traceable Execute Graphql Query Example
  slug: traceable-execute-graphql-query-example
finops:
- has_sources: true
  method: generated
  name: Traceable Finops
  primary_unit: ''
  service_category: API Security
  slug: traceable-finops
  template: false
graphqls:
- description: The Traceable Platform GraphQL API provides programmatic access to API security configuration and operational data. Supports queries for API discovery analytics, vulnerability data, threat activity, e
  name: Traceable GraphQL API
  slug: traceable-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/traceable.png
json_schemas:
- name: Traceable API Entity
  property_count: 17
  slug: traceable-api-entity
json_structures:
- name: Traceable Api Entity Structure
  property_count: 0
  slug: traceable-api-entity-structure
jsonld:
- class_count: 33
  name: Traceable Context
  property_count: 0
  slug: traceable-context
layout: provider
mcp_servers:
- description: ''
  name: Traceable MCP Server
  slug: traceable-mcp-server
modified: '2026-05-19'
name: Traceable
nav: Providers
network: true
overview: 'Traceable publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Specifications API, Graph QL API, and 2 more. Tagged areas include API Discovery, API Protection, API Security, API Testing, and Developer Tools.


  The Traceable catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Traceable''s developer surface includes authentication, documentation, engineering blog, GitHub presence, and 15 more developer resources.'
plans:
- name: Traceable Plans Pricing
  plan_count: 1
  slug: traceable-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 1
  name: Traceable Rate Limits
  slug: traceable-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Traceable — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: traceable-jsonschema-spectral-rules
- authorship: unmarked
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Traceable API Rules
  rule_count: 10
  severity_counts:
    error: 5
    hint: 0
    info: 0
    warn: 5
  slug: traceable-rules
score:
  band: thin
  composite: 33.3
  coverage:
    artifact_dirs: 21
    catalog_earned: 58.4
    catalog_earned_first_party: 0.0
    catalog_gap: 56.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 5.3
    contract_governance: 27.3
    contract_quality: 61.5
    developer_ergonomics: 23.8
    discoverability: 56.7
    operational_transparency: 21.1
  previous_composite: 33.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/traceable/traceable-2026-06-20T195515.png
security:
- kind: authentication
  name: Traceable Authentication
  slug: traceable-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Traceable Domain Security
  slug: traceable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Traceable Vulnerability Disclosure
  slug: traceable-vulnerability-disclosure
  summary_line: no policy recorded
slug: traceable
tags:
- API Discovery
- API Protection
- API Security
- API Testing
- Developer Tools
- Observability
- Security
- Threat Detection
website: https://www.traceable.ai
---

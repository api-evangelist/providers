---
access_model:
  confidence: high
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
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
    mcp_tool_quality: full
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 29.4
  scored_at: '2026-11-06'
api_count: 3
apis:
- baseURL: https://astral.sh
  baseurl_source: declared
  description: The Humanizations API from ToHuman — 3 operation(s) for humanizations.
  name: ToHuman Humanizations API
  slug: tohuman-humanizations-api
- baseURL: https://astral.sh
  baseurl_source: declared
  description: The Humanize API from ToHuman — 2 operation(s) for humanize.
  name: ToHuman Humanize API
  slug: tohuman-humanize-api
- baseURL: https://astral.sh
  baseurl_source: declared
  description: The Submit API from ToHuman — 1 operation(s) for submit.
  name: ToHuman Submit API
  slug: tohuman-submit-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/tohuman/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/tohuman/conventions/tohuman-conventions.yml
  title: ''
  type: Conventions
  url: conventions/tohuman-conventions.yml
- group: operate
  href: https://artifacts.apis.io/tohuman/rate-limits/tohuman-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/tohuman-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/tohuman/plans/tohuman-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/tohuman-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/tohuman/rules/tohuman-rules.yml
  title: ''
  type: Spectral
  url: rules/tohuman-rules.yml
- group: design
  href: https://artifacts.apis.io/tohuman/json-ld/tohuman-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/tohuman-context.jsonld
- group: design
  href: https://artifacts.apis.io/tohuman/vocabulary/tohuman-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/tohuman-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/tohuman/data-model/tohuman-data-model.yml
  title: ''
  type: DataModel
  url: data-model/tohuman-data-model.yml
- group: auth
  href: https://artifacts.apis.io/tohuman/authentication/tohuman-authentication.yml
  title: ''
  type: Authentication
  url: authentication/tohuman-authentication.yml
- group: design
  href: https://artifacts.apis.io/tohuman/conformance/tohuman-conformance.yml
  title: ''
  type: Conformance
  url: conformance/tohuman-conformance.yml
- group: agent
  href: https://artifacts.apis.io/tohuman/mcp/tohuman-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/tohuman-mcp.yml
- group: other
  href: https://artifacts.apis.io/tohuman/hosts/tohuman-hosts.yml
  title: ''
  type: Hosts
  url: hosts/tohuman-hosts.yml
- group: other
  href: https://artifacts.apis.io/tohuman/vendors/tohuman-vendors.yml
  title: ''
  type: Vendors
  url: vendors/tohuman-vendors.yml
- group: start
  title: ''
  type: Sandbox
  url: https://tohuman.io/playground
- group: start
  title: ''
  type: GettingStarted
  url: https://tohuman.io/docs/quickstart
- group: auth
  href: https://artifacts.apis.io/tohuman/security/tohuman-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/tohuman-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://tohuman.io/
- group: docs
  title: ''
  type: Documentation
  url: https://tohuman.io/docs
- group: docs
  title: ''
  type: APIReference
  url: https://tohuman.io/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://tohuman.io/pricing
- group: company
  title: ''
  type: Blog
  url: https://tohuman.io/blog
- group: operate
  title: ''
  type: Support
  url: https://tohuman.io/contact
- group: commercial
  title: ''
  type: TermsOfService
  url: https://tohuman.io/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://tohuman.io/privacy
- group: start
  title: ''
  type: SignUp
  url: https://tohuman.io/users/sign_up
coverage:
  checked: 2026-09-25
  detail: Documentation pages exist but no OpenAPI, AsyncAPI, GraphQL, gRPC, or WSDL contracts were found.
  evidence:
  - status: 200
    url: https://tohuman.io/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-09-25'
description: ToHuman provides AI text humanization services, enabling developers to make AI‑generated content undetectable and natural‑sounding. Their platform offers APIs for transforming articles, emails, ads, and other marketing copy, with integrations for n8n, Make, Zapier, LangChain, and more. Use cases span education, SaaS, chatbots, and content creation, supported by detailed documentation, pricing plans, and a playground for testing. The company aims to help users bypass AI detection tools while maintaining high‑quality, human‑like output.
finops:
- has_sources: true
  method: derived
  name: Tohuman Finops
  primary_unit: seat
  service_category: ''
  slug: tohuman-finops
  template: false
image: https://tohuman.io/og-default.png
json_schemas:
- name: GetApiV1HumanizationsHumanizationidResponse
  property_count: 10
  slug: tohuman-get-api-v1-humanizations-humanizationid-response
- name: PostApiV1HumanizationsRequest
  property_count: 3
  slug: tohuman-post-api-v1-humanizations-request
- name: PostSubmitRequest
  property_count: 1
  slug: tohuman-post-submit-request
- name: PostSubmitResponse
  property_count: 1
  slug: tohuman-post-submit-response
- name: PostV1HumanizeRequest
  property_count: 2
  slug: tohuman-post-v1-humanize-request
- name: PostV1HumanizeResponse
  property_count: 2
  slug: tohuman-post-v1-humanize-response
jsonld:
- class_count: 8
  name: Tohuman Context
  property_count: 14
  slug: tohuman-context
layout: provider
mcp_servers:
- description: Remote MCP server at tohuman.io; 1 tool listed.
  name: ToHuman MCP Server
  slug: tohuman-mcp-yml
modified: '2026-09-25'
name: ToHuman
nav: Providers
network: true
overview: 'ToHuman is listed with 3 APIs on the [APIs.io](https://apis.io/) network: Humanizations API, Humanize API, and Submit API. Tagged areas include Artificial Intelligence, Text-Humanization, Content Generation, Marketing, and Software-as-a-Service.


  The ToHuman catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  ToHuman''s developer surface includes authentication, sandbox, getting-started guide, documentation, API reference, pricing, engineering blog, and 18 more developer resources.'
plans:
- name: Tohuman Plans Pricing
  plan_count: 2
  slug: tohuman-plans-pricing
- name: Tohuman Price Estimates
  plan_count: 0
  slug: tohuman-price-estimates
random_paper: 20
rate_limits:
- limit_count: 2
  name: Tohuman Rate Limits
  slug: tohuman-rate-limits
rules:
- authorship: generated
  effective_rule_count: 53
  extends:
  - spectral:oas
  name: ToHuman API Rules
  rule_count: 12
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 1
  slug: tohuman-rules
score:
  band: thin
  composite: 36.4
  coverage:
    artifact_dirs: 26
    catalog_earned: 84.8
    catalog_earned_first_party: 16.0
    catalog_gap: 30.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.3
  facets:
    access_clarity: 51.3
    contract_governance: 22.0
    contract_quality: 25.9
    developer_ergonomics: 35.1
    discoverability: 73.3
    operational_transparency: 21.1
  previous_composite: 45.7
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 4
      marker_coverage: 100.0
      total: 4
    mcp: first-party
    skills: derived
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
screenshot: https://apis.io/screenshots/tohuman/tohuman-2026-10-11T131206.png
security:
- kind: authentication
  name: Tohuman Authentication
  slug: tohuman-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Tohuman Domain Security
  slug: tohuman-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
skill_count: 1
skills:
- name: tohuman-submit-humanization
  slug: tohuman-submit-humanization
slug: tohuman
tags:
- Artificial Intelligence
- Text-Humanization
- Content Generation
- Marketing
- Software-as-a-Service
website: https://tohuman.io/
---

---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
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
    agent_skills: unknown
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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 33.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Themassprint Com Agentic Access
  operation_count: 12
  slug: themassprint-com-agentic-access
  summary_line: 12 operations · 7 acting
api_count: 1
apis:
- baseURL: https://themassprint.com
  baseurl_source: declared
  description: The Catalog API from themassprint-com — 1 operation(s) for catalog.
  name: themassprint-com Catalog API
  slug: themassprint-com-catalog-api
- baseURL: https://themassprint.com
  baseurl_source: declared
  description: The Enterprise API from themassprint-com — 1 operation(s) for enterprise.
  name: themassprint-com Enterprise API
  slug: themassprint-com-enterprise-api
- baseURL: https://themassprint.com
  baseurl_source: declared
  description: The Health API from themassprint-com — 1 operation(s) for health.
  name: themassprint-com Health API
  slug: themassprint-com-health-api
- baseURL: https://themassprint.com
  baseurl_source: declared
  description: The Orders API from themassprint-com — 3 operation(s) for orders.
  name: themassprint-com Orders API
  slug: themassprint-com-orders-api
- baseURL: https://themassprint.com
  baseurl_source: declared
  description: The Uploads API from themassprint-com — 3 operation(s) for uploads.
  name: themassprint-com Uploads API
  slug: themassprint-com-uploads-api
- baseURL: https://themassprint.com
  baseurl_source: declared
  description: The Webhook Endpoints API from themassprint-com — 2 operation(s) for webhook endpoints.
  name: themassprint-com Webhook Endpoints API
  slug: themassprint-com-webhook-endpoints-api
artifact_total: 19
common:
- group: agent
  href: https://artifacts.apis.io/themassprint-com/agentic-access/themassprint-com-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/themassprint-com-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/themassprint-com/rate-limits/themassprint-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/themassprint-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/themassprint-com/plans/themassprint-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/themassprint-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/themassprint-com/rules/themassprint-com-rules.yml
  title: ''
  type: Spectral
  url: rules/themassprint-com-rules.yml
- group: design
  href: https://artifacts.apis.io/themassprint-com/json-ld/themassprint-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/themassprint-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/themassprint-com/vocabulary/themassprint-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/themassprint-com-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/themassprint-com/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/themassprint-com/data-model/themassprint-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/themassprint-com-data-model.yml
- group: auth
  href: https://artifacts.apis.io/themassprint-com/authentication/themassprint-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/themassprint-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/themassprint-com/errors/themassprint-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/themassprint-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/themassprint-com/conformance/themassprint-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/themassprint-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/themassprint-com/llms/themassprint-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/themassprint-com-llms.txt
- group: build
  href: https://artifacts.apis.io/themassprint-com/mcp/themassprint-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/themassprint-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/themassprint-com/mcp/themassprint-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/themassprint-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/themassprint-com/hosts/themassprint-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/themassprint-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/themassprint-com/vendors/themassprint-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/themassprint-com-vendors.yml
- group: auth
  href: https://artifacts.apis.io/themassprint-com/security/themassprint-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/themassprint-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://themassprint.com/
- group: docs
  title: ''
  type: Documentation
  url: https://themassprint.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://themassprint.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://themassprint.com/docs
- group: operate
  title: ''
  type: Support
  url: https://themassprint.com/login
- group: start
  title: ''
  type: SignUp
  url: https://themassprint.com/order
created: '2026-10-31'
description: massprint provides a print‑on‑demand API that lets developers upload a PDF and receive a printed storybook delivered to a door in India. Built for AI agents, the service offers an MCP endpoint and a REST API, with optional Razorpay payment links. It supports multiple SKUs such as paperback, hardcover, stickers and greeting cards, and includes tracking, order status, and enterprise options.
image: https://themassprint.com/favicon.svg
json_schemas:
- name: Address
  property_count: 7
  slug: themassprint-com-address
- name: Order
  property_count: 16
  slug: themassprint-com-order
- name: UploadValidation
  property_count: 2
  slug: themassprint-com-upload-validation
jsonld:
- class_count: 6
  name: Themassprint Com Context
  property_count: 35
  slug: themassprint-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at themassprint.com.
  name: themassprint-com MCP Server
  slug: themassprint-com-mcp-yml
modified: '2026-10-31'
name: themassprint-com
nav: Providers
network: true
overview: 'themassprint-com publishes 6 API contracts indexed on the [APIs.io](https://apis.io/) network, including Catalog API, Enterprise API, Health API, and 3 more. Tagged areas include Print on Demand, AI Agents, E-Commerce, and India.


  The themassprint-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  themassprint-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, signup flow, and 17 more developer resources.'
plans:
- name: Themassprint Com Plans Pricing
  plan_count: 3
  slug: themassprint-com-plans-pricing
random_paper: 22
rate_limits:
- limit_count: 2
  name: Themassprint Com Rate Limits
  slug: themassprint-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 50
  extends:
  - spectral:oas
  name: themassprint-com API Rules
  rule_count: 9
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 0
  slug: themassprint-com-rules
scopes:
- name: Themassprint Com Scopes
  scope_count: 0
  slug: themassprint-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 42.3
  coverage:
    artifact_dirs: 33
    catalog_earned: 77.0
    catalog_earned_first_party: 20.0
    catalog_gap: 38.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -5.5
  facets:
    access_clarity: 38.2
    contract_governance: 19.7
    contract_quality: 60.7
    developer_ergonomics: 35.0
    discoverability: 56.7
    operational_transparency: 21.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - india
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - india-south-asia
  previous_composite: 47.8
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 26.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/themassprint-com/themassprint-com-2026-11-03T144622.png
security:
- kind: authentication
  name: Themassprint Com Authentication
  slug: themassprint-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Themassprint Com Domain Security
  slug: themassprint-com-domain-security
  summary_line: TLSv1.3 · DMARC
skill_count: 1
skills:
- name: print-book
  slug: themassprint-com-print-book
slug: themassprint-com
tags:
- Print on Demand
- AI Agents
- E-Commerce
- India
website: https://themassprint.com/
---

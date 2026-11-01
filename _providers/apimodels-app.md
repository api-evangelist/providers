---
agent_readiness:
  band: agent-aware
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 24.7
  scored_at: '2026-10-31'
api_count: 1
apis:
- description: Complete API reference for all available models. Get started with our unified API interface.
  name: Unified API
  slug: unified-api
artifact_total: 3
common:
- group: design
  href: https://artifacts.apis.io/apimodels-app/errors/apimodels-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/apimodels-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/apimodels-app/conformance/apimodels-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/apimodels-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/apimodels-app/llms/apimodels-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/apimodels-app-llms.txt
- group: agent
  href: https://artifacts.apis.io/apimodels-app/mcp/apimodels-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/apimodels-app-mcp.yml
- group: agent
  href: https://artifacts.apis.io/apimodels-app/well-known/apimodels-app-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/apimodels-app-well-known.yml
- group: other
  href: https://artifacts.apis.io/apimodels-app/hosts/apimodels-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/apimodels-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/apimodels-app/vendors/apimodels-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/apimodels-app-vendors.yml
- group: build
  href: https://artifacts.apis.io/apimodels-app/packages/apimodels-app-packages.yml
  title: ''
  type: SDKs
  url: packages/apimodels-app-packages.yml
- group: build
  href: https://artifacts.apis.io/apimodels-app/packages/apimodels-app-packages.yml
  title: ''
  type: Packages
  url: packages/apimodels-app-packages.yml
- group: start
  title: ''
  type: Sandbox
  url: https://apimodels.app/console
- group: start
  title: ''
  type: Login
  url: https://apimodels.app/login
- group: docs
  title: ''
  type: APIReference
  url: https://apimodels.app/minimax-h3-prompts/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://apimodels.app/docs/mcp
- group: auth
  href: https://artifacts.apis.io/apimodels-app/security/apimodels-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/apimodels-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://apimodels.app/
- group: docs
  title: ''
  type: Documentation
  url: https://apimodels.app/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://apimodels.app/pricing
- group: company
  title: ''
  type: Blog
  url: https://apimodels.app/blog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://apimodels.app/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://apimodels.app/privacy
coverage:
  checked: '2026-10-30'
  detail: Docs provide base URLs but no machine‑readable OpenAPI/GraphQL/AsyncAPI spec.
  evidence:
  - status: 200
    url: https://apimodels.app/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: APIMODELS is a multi‑model AI API platform that aggregates over 150 models from providers such as Claude, GPT, Gemini, and more, offering developers a single unified endpoint. It delivers stable, affordable access with automatic failover, extensive pricing discounts up to 95% below official rates, and supports image, video, audio, and language models. The service includes a developer console, API keys, and comprehensive documentation, aiming to simplify AI integration for applications across various domains.
image: https://apimodels.app/icon.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.apimodels.app.
  name: apimodels-app MCP Server
  slug: apimodels-app-mcp-yml
modified: '2026-10-30'
name: apimodels-app
nav: Providers
network: true
overview: 'apimodels-app is listed with 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Company, AI, Machine Learning, API, and Aggregation.


  apimodels-app''s developer surface includes sandbox, API reference, getting-started guide, documentation, pricing, engineering blog, and 14 more developer resources.'
random_paper: 4
score:
  band: thin
  composite: 27.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 16.4
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 65.0
    operational_transparency: 0.0
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 22.7
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Apimodels App Domain Security
  slug: apimodels-app-domain-security
  summary_line: TLSv1.3 · HSTS
slug: apimodels-app
tags:
- Company
- AI
- Machine Learning
- API
- Aggregation
- Multi-Model
website: https://apimodels.app/
---

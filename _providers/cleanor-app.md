---
access_model:
  confidence: low
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Open access
  onboarding: open
  pricing: freemium
  public: true
  source:
  - plans
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
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
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 20.6
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 21
  human_in_the_loop: 0
  name: Cleanor App Agentic Access
  operation_count: 25
  slug: cleanor-app-agentic-access
  summary_line: 25 operations · 21 acting
api_count: 1
apis:
- baseURL: https://mcp.cleanor.app
  baseurl_source: declared
  description: The Optimize API from Cleanor Research Labs — 1 operation(s) for optimize.
  name: Cleanor Research Labs Optimize API
  slug: cleanor-app-optimize-api
- baseURL: https://mcp.cleanor.app
  baseurl_source: declared
  description: The Placeholder API from Cleanor Research Labs — 1 operation(s) for placeholder.
  name: Cleanor Research Labs Placeholder API
  slug: cleanor-app-placeholder-api
- baseURL: https://mcp.cleanor.app
  baseurl_source: declared
  description: The Qr.svg API from Cleanor Research Labs — 1 operation(s) for qr.svg.
  name: Cleanor Research Labs Qr.svg API
  slug: cleanor-app-qr-svg-api
- baseURL: https://mcp.cleanor.app
  baseurl_source: declared
  description: The Tools API from Cleanor Research Labs — 22 operation(s) for tools.
  name: Cleanor Research Labs Tools API
  slug: cleanor-app-tools-api
artifact_total: 11
common:
- group: agent
  href: https://artifacts.apis.io/cleanor-app/agentic-access/cleanor-app-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/cleanor-app-agentic-access.yml
- group: commercial
  href: https://artifacts.apis.io/cleanor-app/plans/cleanor-app-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/cleanor-app-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/cleanor-app/rules/cleanor-app-rules.yml
  title: ''
  type: Spectral
  url: rules/cleanor-app-rules.yml
- group: design
  href: https://artifacts.apis.io/cleanor-app/json-ld/cleanor-app-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/cleanor-app-context.jsonld
- group: design
  href: https://artifacts.apis.io/cleanor-app/vocabulary/cleanor-app-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/cleanor-app-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/cleanor-app/data-model/cleanor-app-data-model.yml
  title: ''
  type: DataModel
  url: data-model/cleanor-app-data-model.yml
- group: design
  href: https://artifacts.apis.io/cleanor-app/errors/cleanor-app-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/cleanor-app-problem-types.yml
- group: design
  href: https://artifacts.apis.io/cleanor-app/conformance/cleanor-app-conformance.yml
  title: ''
  type: Conformance
  url: conformance/cleanor-app-conformance.yml
- group: agent
  href: https://artifacts.apis.io/cleanor-app/llms/cleanor-app-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/cleanor-app-llms.txt
- group: build
  href: https://artifacts.apis.io/cleanor-app/mcp/cleanor-app-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/cleanor-app-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/cleanor-app/mcp/cleanor-app-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/cleanor-app-mcp.yml
- group: other
  href: https://artifacts.apis.io/cleanor-app/hosts/cleanor-app-hosts.yml
  title: ''
  type: Hosts
  url: hosts/cleanor-app-hosts.yml
- group: other
  href: https://artifacts.apis.io/cleanor-app/vendors/cleanor-app-vendors.yml
  title: ''
  type: Vendors
  url: vendors/cleanor-app-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://cleanor.app/terms
- group: operate
  title: ''
  type: Support
  url: https://cleanor.app/support
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://cleanor.app/privacy-policy
- group: commercial
  title: ''
  type: Pricing
  url: https://cleanor.app/pricing
- group: company
  title: ''
  type: Newsroom
  url: https://cleanor.app/news
- group: start
  title: ''
  type: Login
  url: https://cleanor.app/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/cleanor-app
- group: operate
  title: ''
  type: ChangeLog
  url: https://cleanor.app/release-notes
- group: company
  title: ''
  type: Blog
  url: https://cleanor.app/blog
- group: docs
  title: ''
  type: APIReference
  url: https://cleanor.app/developers
- group: auth
  href: https://artifacts.apis.io/cleanor-app/security/cleanor-app-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/cleanor-app-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://cleanor.app/
created: '2026-11-03'
description: Cleanor Research Labs offers free, browser‑first tools to convert, compress, and edit images, videos, audio, PDFs and other files directly in the user’s browser. No signup, no upload limits, and files never leave the device. The platform also provides mobile apps, a marketplace of image‑workflow utilities, and support resources for faster document and media processing.
image: https://cleanor.app/og/home.jpg
json_schemas:
- name: ToolResult
  property_count: 5
  slug: cleanor-app-tool-result
jsonld:
- class_count: 1
  name: Cleanor App Context
  property_count: 5
  slug: cleanor-app-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.cleanor.app.
  name: Cleanor Research Labs MCP Server
  slug: cleanor-app-mcp-yml
modified: '2026-11-03'
name: Cleanor Research Labs
nav: Providers
network: true
overview: 'Cleanor Research Labs publishes 4 API contracts indexed on the [APIs.io](https://apis.io/) network, including Optimize API, Placeholder API, Qr.svg API, and 1 more. Tagged areas include Company, Tools, Image Processing, Browser, and Free.


  The Cleanor Research Labs catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Cleanor Research Labs'' developer surface includes support, pricing, changelog, engineering blog, API reference, and 20 more developer resources.'
plans:
- name: Cleanor App Plans Pricing
  plan_count: 2
  slug: cleanor-app-plans-pricing
random_paper: 2
rules:
- authorship: generated
  effective_rule_count: 89
  extends:
  - spectral:oas
  name: Cleanor Research Labs API Rules
  rule_count: 48
  severity_counts:
    error: 34
    hint: 0
    info: 7
    warn: 7
  slug: cleanor-app-rules
score:
  band: thin
  composite: 33.4
  coverage:
    artifact_dirs: 20
    catalog_earned: 61.2
    catalog_earned_first_party: 8.0
    catalog_gap: 53.9
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 43.4
    contract_governance: 22.0
    contract_quality: 51.2
    developer_ergonomics: 7.1
    discoverability: 65.8
    operational_transparency: 10.5
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 14.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: domain-security
  name: Cleanor App Domain Security
  slug: cleanor-app-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: cleanor-app
tags:
- Company
- Tools
- Image Processing
- Browser
- Free
website: https://cleanor.app/
---

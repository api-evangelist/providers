---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.0
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Capture screenshots via POST or GET to the /v1/capture endpoint.
  name: Screenshot Capture API
  slug: screenshot-capture-api
- baseURL: https://api.screenshotscout.com
  baseurl_source: declared
  description: 'screenshotscout-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-31); not the provider''s own document.'
  name: screenshotscout-com API
  slug: screenshotscout-com-api
artifact_total: 13
common:
- group: operate
  href: https://artifacts.apis.io/screenshotscout-com/rate-limits/screenshotscout-com-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/screenshotscout-com-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/screenshotscout-com/plans/screenshotscout-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/screenshotscout-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/rules/screenshotscout-com-rules.yml
  title: ''
  type: Spectral
  url: rules/screenshotscout-com-rules.yml
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/json-ld/screenshotscout-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/screenshotscout-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/vocabulary/screenshotscout-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/screenshotscout-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/data-model/screenshotscout-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/screenshotscout-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/conventions/screenshotscout-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/screenshotscout-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/screenshotscout-com/authentication/screenshotscout-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/screenshotscout-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/errors/screenshotscout-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/screenshotscout-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/screenshotscout-com/conformance/screenshotscout-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/screenshotscout-com-conformance.yml
- group: build
  href: https://artifacts.apis.io/screenshotscout-com/mcp/screenshotscout-com-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/screenshotscout-com-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/screenshotscout-com/mcp/screenshotscout-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/screenshotscout-com-mcp.yml
- group: other
  href: https://artifacts.apis.io/screenshotscout-com/hosts/screenshotscout-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/screenshotscout-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/screenshotscout-com/vendors/screenshotscout-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/screenshotscout-com-vendors.yml
- group: build
  href: https://artifacts.apis.io/screenshotscout-com/packages/screenshotscout-com-packages.yml
  title: ''
  type: Packages
  url: packages/screenshotscout-com-packages.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://screenshotscout.com/terms-of-service
- group: build
  title: ''
  type: SDKs
  url: https://www.npmjs.com/package/@screenshotscout/sdk
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://screenshotscout.com/privacy-policy
- group: auth
  href: https://artifacts.apis.io/screenshotscout-com/security/screenshotscout-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/screenshotscout-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://screenshotscout.com/
- group: docs
  title: ''
  type: Documentation
  url: https://screenshotscout.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://screenshotscout.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://screenshotscout.com/docs
- group: operate
  title: ''
  type: Support
  url: https://screenshotscout.com/contact
- group: company
  title: ''
  type: Blog
  url: https://screenshotscout.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/screenshotscout
- group: commercial
  title: ''
  type: Pricing
  url: https://screenshotscout.com/#pricing
- group: start
  title: ''
  type: SignUp
  url: https://screenshotscout.com/auth/signup
coverage:
  checked: '2026-10-31'
  detail: Docs provide API details but no OpenAPI/AsyncAPI/GraphQL spec is published.
  evidence:
  - status: 200
    url: https://screenshotscout.com/docs/api-reference
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-31'
description: Screenshot Scout provides a powerful API that enables developers to capture high‑resolution screenshots of web pages, generate PDFs, and extract visual data programmatically. The service offers customizable viewport sizes, device emulation, and advanced rendering options, making it suitable for testing, monitoring, and content archiving. With a simple RESTful interface, developers can integrate screenshot capabilities into applications, CI pipelines, and monitoring tools, supporting authentication via API keys and rate‑limited usage plans.
image: https://screenshotscout.com/images/logo.svg
json_schemas:
- name: GetV1CaptureResponse
  property_count: 4
  slug: screenshotscout-com-get-v1-capture-response
- name: PostV1CaptureRequest
  property_count: 3
  slug: screenshotscout-com-post-v1-capture-request
- name: PostV1CaptureResponse
  property_count: 1
  slug: screenshotscout-com-post-v1-capture-response
jsonld:
- class_count: 3
  name: Screenshotscout Com Context
  property_count: 7
  slug: screenshotscout-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.screenshotscout.com.
  name: screenshotscout-com MCP Server
  slug: screenshotscout-com-mcp-yml
modified: '2026-10-31'
name: screenshotscout-com
nav: Providers
network: true
overview: 'screenshotscout-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Screenshots, API, WebAutomation, DeveloperTools, and SaaS.


  The screenshotscout-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  screenshotscout-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 21 more developer resources.'
plans:
- name: Screenshotscout Com Plans Pricing
  plan_count: 4
  slug: screenshotscout-com-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 8
  name: Screenshotscout Com Rate Limits
  slug: screenshotscout-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: screenshotscout-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: screenshotscout-com-rules
scopes:
- name: Screenshotscout Com Scopes
  scope_count: 0
  slug: screenshotscout-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.4
  coverage:
    artifact_dirs: 24
    catalog_earned: 93.3
    catalog_earned_first_party: 0.0
    catalog_gap: 21.7
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 73.2
    contract_governance: 79.1
    contract_quality: 50.1
    developer_ergonomics: 54.8
    discoverability: 65.0
    operational_transparency: 33.7
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 34.3
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Screenshotscout Com Authentication
  slug: screenshotscout-com-authentication
  summary_line: 2 schemes
- kind: domain-security
  name: Screenshotscout Com Domain Security
  slug: screenshotscout-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: screenshotscout-com
tags:
- Screenshots
- API
- WebAutomation
- DeveloperTools
- SaaS
website: https://screenshotscout.com/
---

---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
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
    idempotency: documented
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 43.0
  scored_at: '2026-11-06'
api_count: 2
apis:
- description: API for managing contractors, coverage, and compliance.
  name: 1099Policy API
  slug: 1099policy-api
- baseURL: https://api.1099policy.com
  baseurl_source: declared
  description: '1099policy-com API as documented publicly: 40 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: 1099policy-com API
  slug: 1099policy-com-api
artifact_total: 16
common:
- group: design
  href: https://artifacts.apis.io/1099policy-com/rules/1099policy-com-rules.yml
  title: ''
  type: Spectral
  url: rules/1099policy-com-rules.yml
- group: design
  href: https://artifacts.apis.io/1099policy-com/json-ld/1099policy-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/1099policy-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/1099policy-com/vocabulary/1099policy-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/1099policy-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/1099policy-com/data-model/1099policy-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/1099policy-com-data-model.yml
- group: design
  href: https://artifacts.apis.io/1099policy-com/conventions/1099policy-com-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/1099policy-com-conventions.yml
- group: design
  href: https://artifacts.apis.io/1099policy-com/conventions/1099policy-com-conventions.yml
  title: ''
  type: Conventions
  url: conventions/1099policy-com-conventions.yml
- group: auth
  href: https://artifacts.apis.io/1099policy-com/authentication/1099policy-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/1099policy-com-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.1099policy.com
- group: design
  href: https://artifacts.apis.io/1099policy-com/lifecycle/1099policy-com-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/1099policy-com-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/1099policy-com/errors/1099policy-com-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/1099policy-com-problem-types.yml
- group: design
  href: https://artifacts.apis.io/1099policy-com/conformance/1099policy-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/1099policy-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/1099policy-com/llms/1099policy-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/1099policy-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/1099policy-com/mcp/1099policy-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/1099policy-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/1099policy-com/well-known/1099policy-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/1099policy-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/1099policy-com/hosts/1099policy-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/1099policy-com-hosts.yml
- group: build
  href: https://artifacts.apis.io/1099policy-com/packages/1099policy-com-packages.yml
  title: ''
  type: SDKs
  url: packages/1099policy-com-packages.yml
- group: build
  href: https://artifacts.apis.io/1099policy-com/packages/1099policy-com-packages.yml
  title: ''
  type: Packages
  url: packages/1099policy-com-packages.yml
- group: operate
  title: ''
  type: Support
  url: https://www.1099policy.com/help
- group: auth
  title: ''
  type: Security
  url: https://www.1099policy.com/security
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/1099policy
- group: auth
  href: https://artifacts.apis.io/1099policy-com/security/1099policy-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/1099policy-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://1099policy.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.1099policy.com/docs
- group: commercial
  title: ''
  type: Pricing
  url: https://www.1099policy.com/pricing
- group: company
  title: ''
  type: Blog
  url: https://www.1099policy.com/blog
- group: start
  title: ''
  type: GettingStarted
  url: https://www.1099policy.com/demo
- group: start
  title: ''
  type: Login
  url: https://dashboard.1099policy.com/signin
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.1099policy.com/terms/licensee
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.1099policy.com/legal/privacy
coverage:
  checked: '2026-10-30'
  detail: Docs provide usage examples but no OpenAPI or other machine‑readable spec.
  evidence:
  - status: 200
    url: https://docs.1099policy.com/authentication.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: 1099Policy provides an insurance and compliance platform for 1099 contractors, offering per‑engagement workers’ compensation, liability coverage, and automated certificate of insurance (COI) management. The service enables companies to onboard independent workers quickly, verify coverage, and reduce compliance risk without the overhead of an employer of record. By integrating with payroll and contractor management tools, 1099Policy helps businesses close coverage gaps, lower costs, and maintain audit‑ready records.
image: https://framerusercontent.com/images/NxL4p4IpSD3TeXmMRk03IsMVk0.png
json_schemas:
- name: GetApiV1InvoicesInvoiceResponse
  property_count: 9
  slug: 1099policy-com-get-api-v1-invoices-invoice-response
- name: GetApiV1QuotesQuoteResponse
  property_count: 12
  slug: 1099policy-com-get-api-v1-quotes-quote-response
- name: PostApiV1AssignmentsCancelResponse
  property_count: 12
  slug: 1099policy-com-post-api-v1-assignments-cancel-response
- name: PostApiV1AssignmentsResponse
  property_count: 12
  slug: 1099policy-com-post-api-v1-assignments-response
- name: PostApiV1QuotesResponse
  property_count: 12
  slug: 1099policy-com-post-api-v1-quotes-response
- name: PutApiV1QuotesQuoteResponse
  property_count: 12
  slug: 1099policy-com-put-api-v1-quotes-quote-response
jsonld:
- class_count: 58
  name: 1099Policy Com Context
  property_count: 75
  slug: 1099policy-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at docs.1099policy.com.
  name: 1099policy-com MCP Server
  slug: 1099policy-com-mcp-yml
modified: '2026-10-30'
name: 1099policy-com
nav: Providers
network: true
overview: '1099policy-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Insurance, Compliance, Contractors, and Workers Comp.


  The 1099policy-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  1099policy-com''s developer surface includes authentication, support, documentation, pricing, engineering blog, getting-started guide, and 23 more developer resources.'
plans:
- name: 1099Policy Com Plans Pricing
  plan_count: 0
  slug: 1099policy-com-plans-pricing
random_paper: 7
rate_limits:
- limit_count: 0
  name: 1099Policy Com Rate Limits
  slug: 1099policy-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 54
  extends:
  - spectral:oas
  name: 1099policy-com API Rules
  rule_count: 13
  severity_counts:
    error: 10
    hint: 0
    info: 1
    warn: 2
  slug: 1099policy-com-rules
scopes:
- name: 1099Policy Com Scopes
  scope_count: 0
  slug: 1099policy-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -10.7
  facets:
    access_clarity: 22.4
    contract_governance: 22.0
    contract_quality: 26.3
    developer_ergonomics: 33.3
    discoverability: 56.7
    operational_transparency: 15.8
  previous_composite: 41.3
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
    matched_via: tags
    regime: Insurance
    regime_id: insurance
    score: 33.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://apis.io/screenshots/1099policy-com/1099policy-com-2026-11-03T120054.png
security:
- kind: authentication
  name: 1099Policy Com Authentication
  slug: 1099policy-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: 1099Policy Com Domain Security
  slug: 1099policy-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: 1099policy-com
tags:
- Insurance
- Compliance
- Contractors
- Workers Comp
website: https://1099policy.com/
---

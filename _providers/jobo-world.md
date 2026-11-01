---
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
    event_surface_described: unknown
    idempotency: documented
    mcp_server: documented
    openapi_examples: false
    operation_distinctiveness: na
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 47.3
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Jobo API provides job search, feed, and company data endpoints.
  name: Jobo API
  slug: jobo-api
- baseURL: https://connect.jobo.world
  baseurl_source: declared
  description: 'jobo-world API as documented publicly: 29 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: jobo-world API
  slug: jobo-world-api
artifact_total: 16
common:
- group: operate
  href: https://artifacts.apis.io/jobo-world/rate-limits/jobo-world-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/jobo-world-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/rules/jobo-world-rules.yml
  title: ''
  type: Spectral
  url: rules/jobo-world-rules.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/json-ld/jobo-world-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/jobo-world-context.jsonld
- group: design
  href: https://artifacts.apis.io/jobo-world/vocabulary/jobo-world-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/jobo-world-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/data-model/jobo-world-data-model.yml
  title: ''
  type: DataModel
  url: data-model/jobo-world-data-model.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/conventions/jobo-world-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/jobo-world-conventions.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/conventions/jobo-world-conventions.yml
  title: ''
  type: Conventions
  url: conventions/jobo-world-conventions.yml
- group: auth
  href: https://artifacts.apis.io/jobo-world/authentication/jobo-world-authentication.yml
  title: ''
  type: Authentication
  url: authentication/jobo-world-authentication.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://jobo.world/status
- group: design
  href: https://artifacts.apis.io/jobo-world/lifecycle/jobo-world-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/jobo-world-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/errors/jobo-world-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/jobo-world-problem-types.yml
- group: design
  href: https://artifacts.apis.io/jobo-world/conformance/jobo-world-conformance.yml
  title: ''
  type: Conformance
  url: conformance/jobo-world-conformance.yml
- group: agent
  href: https://artifacts.apis.io/jobo-world/llms/jobo-world-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/jobo-world-llms.txt
- group: agent
  href: https://artifacts.apis.io/jobo-world/mcp/jobo-world-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/jobo-world-mcp.yml
- group: agent
  href: https://artifacts.apis.io/jobo-world/well-known/jobo-world-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/jobo-world-well-known.yml
- group: other
  href: https://artifacts.apis.io/jobo-world/hosts/jobo-world-hosts.yml
  title: ''
  type: Hosts
  url: hosts/jobo-world-hosts.yml
- group: other
  href: https://artifacts.apis.io/jobo-world/vendors/jobo-world-vendors.yml
  title: ''
  type: Vendors
  url: vendors/jobo-world-vendors.yml
- group: build
  href: https://artifacts.apis.io/jobo-world/packages/jobo-world-packages.yml
  title: ''
  type: SDKs
  url: packages/jobo-world-packages.yml
- group: build
  href: https://artifacts.apis.io/jobo-world/packages/jobo-world-packages.yml
  title: ''
  type: Packages
  url: packages/jobo-world-packages.yml
- group: design
  title: ''
  type: Webhooks
  url: https://jobo.world/outbound-feed/webhook
- group: operate
  title: ''
  type: ChangeLog
  url: https://jobo.world/docs/changelog
- group: auth
  href: https://artifacts.apis.io/jobo-world/security/jobo-world-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/jobo-world-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://jobo.world/
- group: docs
  title: ''
  type: Documentation
  url: https://jobo.world/docs
- group: docs
  title: ''
  type: APIReference
  url: https://jobo.world/docs/api-reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://jobo.world/docs/quickstart
- group: operate
  title: ''
  type: Support
  url: https://jobo.world/status
- group: commercial
  title: ''
  type: Pricing
  url: https://jobo.world/pricing
- group: start
  title: ''
  type: SignUp
  url: https://enterprise.jobo.world/register
- group: commercial
  title: ''
  type: TermsOfService
  url: https://jobo.world/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://jobo.world/privacy
coverage:
  checked: '2026-10-31'
  detail: The provider's documentation is publicly available in markdown but no OpenAPI, AsyncAPI, GraphQL, or other machine‑readable spec is published.
  evidence:
  - status: 200
    url: https://jobo.world/docs/api-reference/overview.md
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Jobo provides a comprehensive job data infrastructure platform that aggregates millions of live job listings from over 150,000 career sites and 200+ applicant tracking systems. Their APIs enable developers to search, filter, and retrieve structured job data, enrich listings with AI‑extracted skills, salaries, and seniority, and even automate applications across supported ATS platforms. The service offers real‑time feeds, export options, and integration tools for databases, search engines, and analytics pipelines, targeting job boards, recruitment platforms, and data‑driven HR products.
image: https://jobo.world/favicon.ico
json_schemas:
- name: GetApiAutoApplyApplicationsIdCancelResponse
  property_count: 16
  slug: jobo-world-get-api-auto-apply-applications-id-cancel-response
- name: GetApiAutoApplyMailboxesIdCheckResponse
  property_count: 15
  slug: jobo-world-get-api-auto-apply-mailboxes-id-check-response
- name: GetApiAutoApplyMailboxesIdResponse
  property_count: 15
  slug: jobo-world-get-api-auto-apply-mailboxes-id-response
- name: GetApiAutoApplyMailboxesIdVerificationResponse
  property_count: 9
  slug: jobo-world-get-api-auto-apply-mailboxes-id-verification-response
- name: PostApiJobsFeedRequest
  property_count: 8
  slug: jobo-world-post-api-jobs-feed-request
- name: PostApiJobsSearchRequest
  property_count: 11
  slug: jobo-world-post-api-jobs-search-request
jsonld:
- class_count: 23
  name: Jobo World Context
  property_count: 69
  slug: jobo-world-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.jobo.world requiring OAuth.
  name: jobo-world MCP Server
  slug: jobo-world-mcp-yml
modified: '2026-10-30'
name: jobo-world
nav: Providers
network: true
overview: 'jobo-world is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Job Data, API, Recruitment, Platform, and Data Infrastructure.


  The jobo-world catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  jobo-world''s developer surface includes authentication, changelog, documentation, API reference, getting-started guide, support, pricing, and 24 more developer resources.'
plans:
- name: Jobo World Plans Pricing
  plan_count: 0
  slug: jobo-world-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Jobo World Rate Limits
  slug: jobo-world-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: jobo-world API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: jobo-world-rules
scopes:
- name: Jobo World Scopes
  scope_count: 0
  slug: jobo-world-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 58.3
  coverage:
    artifact_dirs: 24
    catalog_earned: 88.5
    catalog_earned_first_party: 0.0
    catalog_gap: 26.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 79.1
    contract_quality: 44.8
    developer_ergonomics: 52.4
    discoverability: 65.0
    operational_transparency: 67.9
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
  name: Jobo World Authentication
  slug: jobo-world-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Jobo World Domain Security
  slug: jobo-world-domain-security
  summary_line: TLSv1.3 · DMARC
slug: jobo-world
tags:
- Job Data
- API
- Recruitment
- Platform
- Data Infrastructure
website: https://jobo.world/
---

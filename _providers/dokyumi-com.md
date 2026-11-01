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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 43.5
  scored_at: '2026-10-31'
api_count: 2
apis:
- description: Extract structured JSON from PDFs, scanned images and other business documents via a shared endpoint.
  name: Document Extraction API
  slug: document-extraction-api
- description: 'dokyumi-com API as documented publicly: 3 operations. Contract generated from the documentation by API Evangelist (2026-10-30); not the provider''s own document.'
  name: dokyumi-com API
  slug: dokyumi-com-api
artifact_total: 16
common:
- group: commercial
  href: https://artifacts.apis.io/dokyumi-com/plans/dokyumi-com-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/dokyumi-com-plans-pricing.yml
- group: design
  href: https://artifacts.apis.io/dokyumi-com/rules/dokyumi-com-rules.yml
  title: ''
  type: Spectral
  url: rules/dokyumi-com-rules.yml
- group: design
  href: https://artifacts.apis.io/dokyumi-com/json-ld/dokyumi-com-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/dokyumi-com-context.jsonld
- group: design
  href: https://artifacts.apis.io/dokyumi-com/vocabulary/dokyumi-com-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/dokyumi-com-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/dokyumi-com/data-model/dokyumi-com-data-model.yml
  title: ''
  type: DataModel
  url: data-model/dokyumi-com-data-model.yml
- group: auth
  title: ''
  type: Compliance
  url: https://dokyumi.com/security
- group: auth
  href: https://artifacts.apis.io/dokyumi-com/authentication/dokyumi-com-authentication.yml
  title: ''
  type: Authentication
  url: authentication/dokyumi-com-authentication.yml
- group: design
  href: https://artifacts.apis.io/dokyumi-com/conformance/dokyumi-com-conformance.yml
  title: ''
  type: Conformance
  url: conformance/dokyumi-com-conformance.yml
- group: agent
  href: https://artifacts.apis.io/dokyumi-com/llms/dokyumi-com-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/dokyumi-com-llms.txt
- group: agent
  href: https://artifacts.apis.io/dokyumi-com/mcp/dokyumi-com-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/dokyumi-com-mcp.yml
- group: agent
  href: https://artifacts.apis.io/dokyumi-com/well-known/dokyumi-com-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/dokyumi-com-well-known.yml
- group: other
  href: https://artifacts.apis.io/dokyumi-com/hosts/dokyumi-com-hosts.yml
  title: ''
  type: Hosts
  url: hosts/dokyumi-com-hosts.yml
- group: other
  href: https://artifacts.apis.io/dokyumi-com/vendors/dokyumi-com-vendors.yml
  title: ''
  type: Vendors
  url: vendors/dokyumi-com-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://dokyumi.com/terms
- group: auth
  title: ''
  type: Security
  url: https://dokyumi.com/security
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://dokyumi.com/privacy
- group: company
  title: ''
  type: Newsroom
  url: https://dokyumi.com/newsroom
- group: start
  title: ''
  type: Login
  url: https://dokyumi.com/auth/login
- group: auth
  href: https://artifacts.apis.io/dokyumi-com/security/dokyumi-com-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/dokyumi-com-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/dokyumi-com/security/dokyumi-com-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/dokyumi-com-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/dokyumi-com/security/dokyumi-com-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/dokyumi-com-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://dokyumi.com/
- group: docs
  title: ''
  type: Documentation
  url: https://dokyumi.com/docs
- group: docs
  title: ''
  type: APIReference
  url: https://dokyumi.com/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://dokyumi.com/docs#quickstart
- group: operate
  title: ''
  type: Support
  url: https://dokyumi.com/questions
- group: company
  title: ''
  type: Blog
  url: https://dokyumi.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://dokyumi.com/pricing
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/johnarndt
coverage:
  checked: '2026-10-30'
  detail: Documentation is public HTML but provides no machine‑readable OpenAPI, GraphQL, AsyncAPI, or other contract.
  evidence:
  - status: 200
    url: https://dokyumi.com/docs
  reason: no-machine-readable-spec
  state: unreadable
created: '2026-10-30'
description: Dokyumi provides a no‑code document extraction API that turns PDFs, scanned images and other business documents into structured JSON shaped to a user‑defined schema. Founded in 2026 by John Arndt and operated by Soxoa LLC, it offers flat‑rate pricing (free tier, Starter $99/mo, Growth $499/mo) and supports invoices, bank statements, tax forms and more. The service runs on Cloudflare R2 storage, requires only an API key, and includes webhook delivery, schema management and a public API reference.
image: https://dokyumi.com/dokyumi-logo.svg
json_schemas:
- name: GetApiV1SchemasResponse
  property_count: 1
  slug: dokyumi-com-get-api-v1-schemas-response
- name: PostApiSicClassifyRequest
  property_count: 1
  slug: dokyumi-com-post-api-sic-classify-request
- name: PostApiSicClassifyResponse
  property_count: 7
  slug: dokyumi-com-post-api-sic-classify-response
- name: PostApiV1ExtractResponse
  property_count: 8
  slug: dokyumi-com-post-api-v1-extract-response
jsonld:
- class_count: 4
  name: Dokyumi Com Context
  property_count: 15
  slug: dokyumi-com-context
layout: provider
mcp_servers:
- description: Remote MCP server at dokyumi.com requiring OAuth.
  name: dokyumi-com MCP Server
  slug: dokyumi-com-mcp-yml
modified: '2026-10-30'
name: dokyumi-com
nav: Providers
network: true
overview: 'dokyumi-com is listed with 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Document-Parsing, API, OCR, SaaS, and Finance.


  The dokyumi-com catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  dokyumi-com''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 22 more developer resources.'
plans:
- name: Dokyumi Com Plans Pricing
  plan_count: 4
  slug: dokyumi-com-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Dokyumi Com Rate Limits
  slug: dokyumi-com-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: dokyumi-com API Rules
  rule_count: 11
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 1
  slug: dokyumi-com-rules
scopes:
- name: Dokyumi Com Scopes
  scope_count: 0
  slug: dokyumi-com-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 26
    catalog_earned: 80.5
    catalog_earned_first_party: 0.0
    catalog_gap: 34.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 88.9
    contract_governance: 79.1
    contract_quality: 51.2
    developer_ergonomics: 47.6
    discoverability: 58.3
    operational_transparency: 15.8
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.25.0
  scored_at: '2026-10-31'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Dokyumi Com Authentication
  slug: dokyumi-com-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Dokyumi Com Domain Security
  slug: dokyumi-com-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Dokyumi Com Vulnerability Disclosure
  slug: dokyumi-com-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Dokyumi Com Trust Center
  slug: dokyumi-com-trust-center
  summary_line: SOC 2, PCI DSS, HIPAA
slug: dokyumi-com
tags:
- Document-Parsing
- API
- OCR
- SaaS
- Finance
website: https://dokyumi.com/
---

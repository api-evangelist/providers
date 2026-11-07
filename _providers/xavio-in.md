---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - authentication
  - scopes
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: conformant
    agent_skills: unknown
    agentic_access: derived
    agentic_commerce: self
    auth_clarity: served
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: derived
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: paginated
    protected_resource_metadata: verified
    rate_limit_signal: false
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 65.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 27
  human_in_the_loop: 0
  name: Xavio In Agentic Access
  operation_count: 50
  slug: xavio-in-agentic-access
  summary_line: 50 operations · 27 acting
api_count: 1
apis:
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Bookable services (listings), open slots, and the bookings on them. Customer contact only with customers:pii.
  name: xavio-in Bookings API
  slug: xavio-in-bookings-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Public endpoints — no auth. Discover components, categories, audiences.
  name: xavio-in Discovery API
  slug: xavio-in-discovery-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Lead inbox + ingestion.
  name: xavio-in Leads API
  slug: xavio-in-leads-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Model Context Protocol — JSON-RPC 2.0 over HTTP.
  name: xavio-in MCP API
  slug: xavio-in-mcp-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: List and read orders, move them through fulfilment, add tracking, confirm cash-on-delivery and issue refunds (refunds:write). Contact details only with customers:pii.
  name: xavio-in Orders API
  slug: xavio-in-orders-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Catalog management.
  name: xavio-in Products API
  slug: xavio-in-products-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Publish + manage stories.
  name: xavio-in Stories API
  slug: xavio-in-stories-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: Presigned URLs for direct media upload.
  name: xavio-in Uploads API
  slug: xavio-in-uploads-api
- baseURL: https://nafafy.com
  baseurl_source: declared
  description: 'Signed (X-Nafafy-Signature) event deliveries. Event names: components.schemas.WebhookEvent; payloads: GET /api/v1/public/webhook-events.'
  name: xavio-in Webhooks API
  slug: xavio-in-webhooks-api
artifact_total: 25
asyncapis:
- description: ''
  name: Xavio In Webhooks
  slug: xavio-in-webhooks
common:
- group: auth
  href: https://artifacts.apis.io/xavio-in/well-known/xavio-in-nafafy-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xavio-in-nafafy-security.txt
- group: agent
  href: https://artifacts.apis.io/xavio-in/agentic-access/xavio-in-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/xavio-in-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/xavio-in/rules/xavio-in-rules.yml
  title: ''
  type: Spectral
  url: rules/xavio-in-rules.yml
- group: design
  href: https://artifacts.apis.io/xavio-in/json-ld/xavio-in-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/xavio-in-context.jsonld
- group: design
  href: https://artifacts.apis.io/xavio-in/vocabulary/xavio-in-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/xavio-in-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/xavio-in/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/xavio-in/asyncapi/xavio-in-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/xavio-in-webhooks.yml
- group: design
  href: https://artifacts.apis.io/xavio-in/data-model/xavio-in-data-model.yml
  title: ''
  type: DataModel
  url: data-model/xavio-in-data-model.yml
- group: auth
  title: ''
  type: Security
  url: https://nafafy.com/guide/developers
- group: auth
  href: https://artifacts.apis.io/xavio-in/authentication/xavio-in-authentication.yml
  title: ''
  type: Authentication
  url: authentication/xavio-in-authentication.yml
- group: auth
  href: https://artifacts.apis.io/xavio-in/scopes/xavio-in-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/xavio-in-scopes.yml
- group: design
  href: https://artifacts.apis.io/xavio-in/errors/xavio-in-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/xavio-in-problem-types.yml
- group: design
  href: https://artifacts.apis.io/xavio-in/conformance/xavio-in-conformance.yml
  title: ''
  type: Conformance
  url: conformance/xavio-in-conformance.yml
- group: agent
  href: https://artifacts.apis.io/xavio-in/llms/xavio-in-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/xavio-in-llms.txt
- group: other
  href: https://artifacts.apis.io/xavio-in/a2a/xavio-in-a2a.yml
  title: ''
  type: AgentCard
  url: a2a/xavio-in-a2a.yml
- group: agent
  href: https://artifacts.apis.io/xavio-in/mcp/xavio-in-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/xavio-in-mcp.yml
- group: auth
  href: https://artifacts.apis.io/xavio-in/well-known/xavio-in-xavio-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xavio-in-xavio-security.txt
- group: auth
  href: https://artifacts.apis.io/xavio-in/well-known/xavio-in-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/xavio-in-security.txt
- group: agent
  href: https://artifacts.apis.io/xavio-in/well-known/xavio-in-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/xavio-in-well-known.yml
- group: other
  href: https://artifacts.apis.io/xavio-in/hosts/xavio-in-hosts.yml
  title: ''
  type: Hosts
  url: hosts/xavio-in-hosts.yml
- group: other
  href: https://artifacts.apis.io/xavio-in/vendors/xavio-in-vendors.yml
  title: ''
  type: Vendors
  url: vendors/xavio-in-vendors.yml
- group: auth
  title: ''
  type: TrustCenter
  url: https://nafafy.com/trust
- group: commercial
  title: ''
  type: TermsOfService
  url: https://nafafy.com/terms
- group: operate
  title: ''
  type: Support
  url: https://nafafy.com/help
- group: start
  title: ''
  type: SignUp
  url: https://nafafy.com/auth/signup
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://nafafy.com/privacy
- group: commercial
  title: ''
  type: Pricing
  url: https://nafafy.com/plans
- group: operate
  title: ''
  type: ChangeLog
  url: https://nafafy.com/developers/changelog
- group: docs
  title: ''
  type: APIReference
  url: https://nafafy.com/developers
- group: company
  title: ''
  type: Website
  url: https://xavio.in/
- group: auth
  href: https://artifacts.apis.io/xavio-in/security/xavio-in-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/xavio-in-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/xavio-in/security/xavio-in-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/xavio-in-domain-security.yml
coverage:
  detail: the company serves an API surface but requires credentials before any description of it can be read
  evidence:
  - status: null
    url: https://xavio.in/openapi.json
  - status: null
    url: https://nafafy.com/openapi.json
  - status: 401
    url: https://xavio.in/api/mcp
  - status: 401
    url: https://nafafy.com/api/mcp
  - status: 200
    url: https://xavio.in/
  reason: partner-login
  state: gated
created: '2026-10-30'
description: Xavio-in is currently listed as a stub company in the API Evangelist catalog. No verifiable corporate website or official documentation could be located despite attempts to resolve the listed domain (xavio.in) which redirects to an unrelated commercial site. Consequently, the company's public identity, branding, and API offerings remain unknown. This entry reflects the lack of publicly available information and serves as a placeholder for future enrichment when reliable sources become available.
image: https://nafafy.com/og/default.png
json_schemas:
- name: OrderListItem
  property_count: 17
  slug: xavio-in-order-list-item
- name: Order
  property_count: 29
  slug: xavio-in-order
- name: ProductCreateRequest
  property_count: 54
  slug: xavio-in-product-create-request
- name: ProductUpdateRequest
  property_count: 52
  slug: xavio-in-product-update-request
- name: ProductVariantsWriteRequest
  property_count: 2
  slug: xavio-in-product-variants-write-request
- name: WebhookEvent
  property_count: 0
  slug: xavio-in-webhook-event
jsonld:
- class_count: 63
  name: Xavio In Context
  property_count: 266
  slug: xavio-in-context
layout: provider
mcp_servers:
- description: Remote MCP server at xavio.in requiring an API key.
  name: xavio-in MCP Server
  slug: xavio-in-mcp-yml
modified: '2026-10-30'
name: xavio-in
nav: Providers
network: true
overview: 'xavio-in publishes 9 API contracts indexed on the [APIs.io](https://apis.io/) network, including Bookings API, Discovery API, Leads API, and 6 more. Tagged areas include Company and Placeholder.


  The xavio-in catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  xavio-in''s developer surface includes authentication, support, signup flow, pricing, changelog, API reference, and 26 more developer resources.'
random_paper: 19
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: xavio-in API Rules
  rule_count: 11
  severity_counts:
    error: 7
    hint: 0
    info: 3
    warn: 1
  slug: xavio-in-rules
scopes:
- name: Xavio In Scopes
  scope_count: 0
  slug: xavio-in-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 47.8
  coverage:
    artifact_dirs: 30
    catalog_earned: 57.8
    catalog_earned_first_party: 0.0
    catalog_gap: 57.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -9.9
  facets:
    access_clarity: 26.3
    contract_governance: 22.0
    contract_quality: 71.2
    developer_ergonomics: 24.3
    discoverability: 66.7
    operational_transparency: 21.1
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 57.7
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
    mcp: first-party
    skills: unknown
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 38.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/xavio-in/xavio-in-2026-11-03T150301.png
security:
- kind: authentication
  name: Xavio In Authentication
  slug: xavio-in-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Xavio In Domain Security
  slug: xavio-in-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Xavio In Vulnerability Disclosure
  slug: xavio-in-vulnerability-disclosure
  summary_line: security.txt · contact published
skill_count: 1
skills:
- name: agents
  slug: xavio-in-agents
slug: xavio-in
tags:
- Company
- Placeholder
website: https://xavio.in/
---

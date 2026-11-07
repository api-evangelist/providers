---
access_model:
  confidence: medium
  gated: none
  gated_source:
  - onboarding
  label: Self-serve signup
  onboarding: self-serve
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
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: quarter
    openapi_examples: false
    operation_distinctiveness: false
    pagination_ratio: na
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 35.0
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Business Agentic Access
  operation_count: 19
  slug: amazon-business-agentic-access
  summary_line: 19 operations · 6 acting
api_count: 6
apis:
- baseURL: https://na.business-api.amazon.com
  baseurl_source: spec
  description: APIs for Amazon Business platform
  name: Amazon Business API
  slug: amazon-business-api
- baseURL: https://na.business-api.amazon.com
  baseurl_source: declared
  description: The Ab Invoice API from Amazon Business — 3 operation(s) for ab invoice.
  name: Amazon Business Ab Invoice API
  slug: amazon-business-ab-invoice-api
- baseURL: https://na.business-api.amazon.com
  baseurl_source: declared
  description: The Cart API from Amazon Business — 4 operation(s) for cart.
  name: Amazon Business Cart API
  slug: amazon-business-cart-api
- baseURL: https://na.business-api.amazon.com
  baseurl_source: declared
  description: The Ordering API from Amazon Business — 2 operation(s) for ordering.
  name: Amazon Business Ordering API
  slug: amazon-business-ordering-api
- baseURL: https://na.business-api.amazon.com
  baseurl_source: declared
  description: The Products API from Amazon Business — 3 operation(s) for products.
  name: Amazon Business Products API
  slug: amazon-business-products-api
- baseURL: https://na.business-api.amazon.com
  baseurl_source: declared
  description: The Reports API from Amazon Business — 3 operation(s) for reports.
  name: Amazon Business Reports API
  slug: amazon-business-reports-api
artifact_total: 20
asyncapis:
- description: ''
  name: Amazon Business Webhooks
  slug: amazon-business-webhooks
common:
- group: agent
  href: https://artifacts.apis.io/amazon-business/agentic-access/amazon-business-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-business-agentic-access.yml
- group: design
  href: https://artifacts.apis.io/amazon-business/rules/amazon-business-rules.yml
  title: ''
  type: Spectral
  url: rules/amazon-business-rules.yml
- group: design
  href: https://artifacts.apis.io/amazon-business/json-ld/amazon-business-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/amazon-business-context.jsonld
- group: design
  href: https://artifacts.apis.io/amazon-business/vocabulary/amazon-business-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-business-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/amazon-business/asyncapi/amazon-business-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/amazon-business-webhooks.yml
- group: design
  href: https://artifacts.apis.io/amazon-business/data-model/amazon-business-data-model.yml
  title: ''
  type: DataModel
  url: data-model/amazon-business-data-model.yml
- group: operate
  href: https://artifacts.apis.io/amazon-business/changelog/amazon-business-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/amazon-business-changelog.yml
- group: start
  href: https://artifacts.apis.io/amazon-business/sandbox/amazon-business-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/amazon-business-sandbox.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/amazonvrp
- group: auth
  href: https://artifacts.apis.io/amazon-business/authentication/amazon-business-authentication.yml
  title: ''
  type: Authentication
  url: authentication/amazon-business-authentication.yml
- group: design
  href: https://artifacts.apis.io/amazon-business/conformance/amazon-business-conformance.yml
  title: ''
  type: Conformance
  url: conformance/amazon-business-conformance.yml
- group: agent
  href: https://artifacts.apis.io/amazon-business/llms/amazon-business-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/amazon-business-llms.txt
- group: agent
  href: https://artifacts.apis.io/amazon-business/mcp/amazon-business-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/amazon-business-mcp.yml
- group: auth
  href: https://artifacts.apis.io/amazon-business/well-known/amazon-business-aws-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-business-aws-security.txt
- group: auth
  href: https://artifacts.apis.io/amazon-business/well-known/amazon-business-amazon-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/amazon-business-amazon-security.txt
- group: agent
  href: https://artifacts.apis.io/amazon-business/well-known/amazon-business-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/amazon-business-well-known.yml
- group: other
  href: https://artifacts.apis.io/amazon-business/hosts/amazon-business-hosts.yml
  title: ''
  type: Hosts
  url: hosts/amazon-business-hosts.yml
- group: other
  href: https://artifacts.apis.io/amazon-business/vendors/amazon-business-vendors.yml
  title: ''
  type: Vendors
  url: vendors/amazon-business-vendors.yml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.amazon.com/terms-and-agreements
- group: start
  title: ''
  type: Login
  url: https://business.amazon.com/en/login
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AmazonAppDev
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.amazon.com/
- group: operate
  title: ''
  type: ChangeLog
  url: https://business.amazon.com/en/release-notes
- group: auth
  href: https://artifacts.apis.io/amazon-business/security/amazon-business-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-business-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/amazon-business/security/amazon-business-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/amazon-business-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://business.amazon.com
- group: docs
  title: ''
  type: Documentation
  url: https://business.amazon.com/en/solutions
- group: start
  title: ''
  type: GettingStarted
  url: https://business.amazon.com/en/register
- group: operate
  title: ''
  type: Support
  url: https://business.amazon.com/en/contact-us
- group: company
  title: ''
  type: Blog
  url: https://business.amazon.com/en/blog
coverage:
  detail: the company publishes no developer documentation host and no machine-readable contract on its own domain
  evidence:
  - status: null
    url: https://developer.amazon.com/mcp
  - status: 403
    url: https://api.amazon.com/mcp
  - status: 403
    url: https://business.amazon.com/mcp
  - status: 200
    url: https://business.amazon.com
  reason: no-developer-program
  state: none
created: '2026-10-13'
description: Amazon Business provides a B2B marketplace offering procurement solutions, bulk purchasing, spend management, and compliance tools for businesses of all sizes. It enables organizations to create business-only storefronts, access exclusive pricing, manage approvals, and integrate purchasing workflows with existing systems, supporting a wide range of industries and use cases.
image: https://static-assets.business.amazon.com/assets/global/polaris/images/ab_1200x627.png.transform/1450x664/image.jpg
json_schemas:
- name: DeleteCart20250430CartsCartidItemsResponse
  property_count: 3
  slug: amazon-business-delete-cart20250430-carts-cartid-items-response
- name: GetAbInvoice20260201InvoicesInvoicenumberLineitemsResponse
  property_count: 8
  slug: amazon-business-get-ab-invoice20260201-invoices-invoicenumber-lineitems-response
- name: GetAbInvoice20260201InvoicesInvoicenumberResponse
  property_count: 8
  slug: amazon-business-get-ab-invoice20260201-invoices-invoicenumber-response
- name: GetAbInvoice20260201InvoicesResponse
  property_count: 8
  slug: amazon-business-get-ab-invoice20260201-invoices-response
- name: GetCart20250430CartsResponse
  property_count: 3
  slug: amazon-business-get-cart20250430-carts-response
- name: PostProducts20200826ProductsGetproductsbyasinsRequest
  property_count: 4
  slug: amazon-business-post-products20200826-products-getproductsbyasins-request
jsonld:
- class_count: 12
  name: Amazon Business Context
  property_count: 13
  slug: amazon-business-context
layout: provider
mcp_servers:
- description: Remote MCP server at developer.amazon.com.
  name: Amazon Business MCP Server
  slug: amazon-business-mcp-yml
modified: '2026-10-13'
name: Amazon Business
nav: Providers
network: true
overview: 'Amazon Business is listed with 6 APIs on the [APIs.io](https://apis.io/) network, including Ab Invoice API, Cart API, and 4 more. Tagged areas include Company, B2B, Procurement, Marketplace, and BulkPurchasing.


  The Amazon Business catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Amazon Business'' developer surface includes changelog, sandbox, authentication, documentation, getting-started guide, support, engineering blog, and 23 more developer resources.'
random_paper: 7
rules:
- authorship: generated
  effective_rule_count: 83
  extends:
  - spectral:oas
  name: Amazon Business API Rules
  rule_count: 42
  severity_counts:
    error: 35
    hint: 0
    info: 3
    warn: 4
  slug: amazon-business-rules
score:
  band: thin
  composite: 32.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 60.8
    catalog_earned_first_party: 0.0
    catalog_gap: 54.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -7.6
  facets:
    access_clarity: 11.8
    contract_governance: 22.0
    contract_quality: 32.4
    developer_ergonomics: 42.9
    discoverability: 71.7
    operational_transparency: 23.7
  previous_composite: 40.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 6
      marker_coverage: 100.0
      total: 6
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/amazon-business/amazon-business-2026-11-03T120757.png
security:
- kind: authentication
  name: Amazon Business Authentication
  slug: amazon-business-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Amazon Business Domain Security
  slug: amazon-business-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Amazon Business Vulnerability Disclosure
  slug: amazon-business-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: amazon-business
tags:
- Company
- B2B
- Procurement
- Marketplace
- BulkPurchasing
website: https://business.amazon.com
---

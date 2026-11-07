---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium (free trial) · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - rate-limits
  - security
  - sandbox
  trial: true
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: false
    operation_distinctiveness: distinct
    pagination_ratio: na
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 36.1
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Microsoft Dynamics 365 Business Central Agentic Access
  operation_count: 26
  slug: microsoft-dynamics-365-business-central-agentic-access
  summary_line: 26 operations · 14 acting
api_count: 1
apis:
- description: OData v4 endpoints exposing published Business Central pages and queries as web services for custom integrations, reporting, and Power Platform connectors when standard API v2.0 entities are insuffici
  name: Business Central OData Web Services
  slug: odata-web-services
- description: Administration Center REST API for managing Business Central environments, tenants, telemetry, update settings, and notifications programmatically for ISVs and delegated administrators.
  name: Business Central Administration Center API
  slug: admin-center-api
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0
  baseurl_source: declared
  description: Business Central company entities
  name: Microsoft Dynamics 365 Business Central Companies API
  slug: microsoft-dynamics-365-business-central-companies-api
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0
  baseurl_source: declared
  description: Customer master data
  name: Microsoft Dynamics 365 Business Central Customers API
  slug: microsoft-dynamics-365-business-central-customers-api
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0
  baseurl_source: declared
  description: Item master data
  name: Microsoft Dynamics 365 Business Central Items API
  slug: microsoft-dynamics-365-business-central-items-api
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{environment}/api/v2.0
  baseurl_source: declared
  description: Vendor master data
  name: Microsoft Dynamics 365 Business Central Vendors API
  slug: microsoft-dynamics-365-business-central-vendors-api
- description: Remote Model Context Protocol server for Business Central, reached at https://mcp.businesscentral.dynamics.com with Microsoft Entra ID OAuth; exposes configured API tools plus dynamic tools (list_comp
  name: Business Central MCP Server
  slug: mcp-server
- description: 'Webhook subscriptions on API v2.0 entities: register with POST /api/v2.0/subscriptions, complete a validationToken handshake, and renew with PATCH before the three-day expiry.'
  name: Business Central Webhooks (Subscriptions API)
  slug: webhooks
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{tenant}/{environment}/ODataV4
  baseurl_source: declared
  description: Purchase order documents
  name: Microsoft Dynamics 365 Business Central Purchase Orders API
  slug: microsoft-dynamics-365-business-central-purchase-orders-api
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{tenant}/{environment}/ODataV4
  baseurl_source: declared
  description: Sales invoice documents
  name: Microsoft Dynamics 365 Business Central Sales Invoices API
  slug: microsoft-dynamics-365-business-central-sales-invoices-api
- baseURL: https://api.businesscentral.dynamics.com/v2.0/{tenant}/{environment}/ODataV4
  baseurl_source: declared
  description: Sales order documents
  name: Microsoft Dynamics 365 Business Central Sales Orders API
  slug: microsoft-dynamics-365-business-central-sales-orders-api
artifact_total: 35
collections:
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies API
  slug: open-microsoft-dynamics-365-business-central-companies-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies Customers API
  slug: open-microsoft-dynamics-365-business-central-customers-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies Items API
  slug: open-microsoft-dynamics-365-business-central-items-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies PurchaseOrders API
  slug: open-microsoft-dynamics-365-business-central-purchaseorders-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies SalesInvoices API
  slug: open-microsoft-dynamics-365-business-central-salesinvoices-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies SalesOrders API
  slug: open-microsoft-dynamics-365-business-central-salesorders-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0 Companies Vendors API
  slug: open-microsoft-dynamics-365-business-central-vendors-api
- collection_type: open
  name: Microsoft Dynamics 365 Business Central API v2.0
  slug: open-microsoft-dynamics-365-business-central
common:
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/rules/microsoft-dynamics-365-business-central-rules.yml
  title: ''
  type: Spectral
  url: rules/microsoft-dynamics-365-business-central-rules.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/json-ld/microsoft-dynamics-365-business-central-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/microsoft-dynamics-365-business-central-context.jsonld
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/vocabulary/microsoft-dynamics-365-business-central-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/microsoft-dynamics-365-business-central-vocabulary.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/data-model/microsoft-dynamics-365-business-central-data-model.yml
  title: ''
  type: DataModel
  url: data-model/microsoft-dynamics-365-business-central-data-model.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/conventions/microsoft-dynamics-365-business-central-conventions.yml
  title: ''
  type: Conventions
  url: conventions/microsoft-dynamics-365-business-central-conventions.yml
- group: start
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/sandbox/microsoft-dynamics-365-business-central-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/microsoft-dynamics-365-business-central-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.microsoft.com/en-us/trust-center
- group: operate
  title: ''
  type: Deprecation
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/upgrade/deprecated-features-platform
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.microsoft/
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/lifecycle/microsoft-dynamics-365-business-central-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/microsoft-dynamics-365-business-central-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/errors/microsoft-dynamics-365-business-central-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/microsoft-dynamics-365-business-central-error-codes.yml
- group: design
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/conformance/microsoft-dynamics-365-business-central-conformance.yml
  title: ''
  type: Conformance
  url: conformance/microsoft-dynamics-365-business-central-conformance.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/llms/microsoft-dynamics-365-business-central-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/microsoft-dynamics-365-business-central-llms.txt
- group: build
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/mcp/microsoft-dynamics-365-business-central-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/microsoft-dynamics-365-business-central-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/mcp/microsoft-dynamics-365-business-central-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/microsoft-dynamics-365-business-central-mcp.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/well-known/microsoft-dynamics-365-business-central-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/microsoft-dynamics-365-business-central-security.txt
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/well-known/microsoft-dynamics-365-business-central-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/microsoft-dynamics-365-business-central-well-known.yml
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/hosts/microsoft-dynamics-365-business-central-hosts.yml
  title: ''
  type: Hosts
  url: hosts/microsoft-dynamics-365-business-central-hosts.yml
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/vendors/microsoft-dynamics-365-business-central-vendors.yml
  title: ''
  type: Vendors
  url: vendors/microsoft-dynamics-365-business-central-vendors.yml
- group: auth
  title: ''
  type: Security
  url: https://www.microsoft.com/security
- group: other
  title: ''
  type: Leadership
  url: https://news.microsoft.com/leadership
- group: start
  title: ''
  type: GettingStarted
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/developer/devenv-get-started
- group: operate
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/rate-limits/microsoft-dynamics-365-business-central-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/microsoft-dynamics-365-business-central-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/plans/microsoft-dynamics-365-business-central-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/microsoft-dynamics-365-business-central-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/capabilities/microsoft-dynamics-365-business-central-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/microsoft-dynamics-365-business-central-capability-edges.yml
- group: agent
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/agentic-access/microsoft-dynamics-365-business-central-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/microsoft-dynamics-365-business-central-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/security/microsoft-dynamics-365-business-central-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/microsoft-dynamics-365-business-central-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/security/microsoft-dynamics-365-business-central-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/microsoft-dynamics-365-business-central-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/security/microsoft-dynamics-365-business-central-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/microsoft-dynamics-365-business-central-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/authentication/microsoft-dynamics-365-business-central-authentication.yml
  title: ''
  type: Authentication
  url: authentication/microsoft-dynamics-365-business-central-authentication.yml
- group: auth
  href: https://artifacts.apis.io/microsoft-dynamics-365-business-central/scopes/microsoft-dynamics-365-business-central-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/microsoft-dynamics-365-business-central-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/microsoft
- group: company
  title: ''
  type: Website
  url: https://www.microsoft.com/en-us/dynamics-365/products/business-central
- group: docs
  title: ''
  type: Documentation
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.microsoft.com/en-us/dynamics-365/products/business-central/pricing
- group: start
  title: ''
  type: Signup
  url: https://signup.microsoft.com/get-started/signup?products=22b1949b-c5dd-4b06-9c19-1d2fa17e7a9d
- group: company
  title: ''
  type: Blog
  url: https://www.microsoft.com/en-us/dynamics-365/blog/feed/
- group: docs
  title: ''
  type: APIReference
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/api-reference/v2.0/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/
- group: operate
  title: ''
  type: ChangeLog
  url: https://learn.microsoft.com/en-us/dynamics365/business-central/dev-itpro/whatsnew/overview
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.microsoft.com/en-us/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.microsoft.com/privacy
- group: operate
  title: ''
  type: Support
  url: https://support.microsoft.com/en-us
created: '2026-05-11'
description: Microsoft Dynamics 365 Business Central is an all-in-one cloud ERP solution for small and mid-sized businesses that brings together finance, sales, service, project management, supply chain, manufacturing, and operations on the Microsoft Cloud. Business Central exposes a standard REST API (v2.0) plus custom and OData web services so partners can build Connect apps, automate processes, and integrate Business Central with Power Platform and third-party systems using OAuth 2.0 authentication via Microsoft Entra ID.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/microsoft-dynamics-365-business-central.png
json_schemas:
- name: CompanyCollection
  property_count: 1
  slug: microsoft-dynamics-365-business-central-company-collection
- name: Company
  property_count: 7
  slug: microsoft-dynamics-365-business-central-company
- name: CustomerCollection
  property_count: 1
  slug: microsoft-dynamics-365-business-central-customer-collection
- name: Customer
  property_count: 22
  slug: microsoft-dynamics-365-business-central-customer
jsonld:
- class_count: 4
  name: Microsoft Dynamics 365 Business Central Context
  property_count: 28
  slug: microsoft-dynamics-365-business-central-context
layout: provider
mcp_servers:
- description: Remote MCP server at mcp.businesscentral.dynamics.com requiring OAuth; 5 tools listed.
  name: Business Central MCP Server
  slug: business-central-mcp-server
modified: '2026-11-04'
name: Microsoft Dynamics 365 Business Central
nav: Providers
network: true
overview: 'Microsoft Dynamics 365 Business Central publishes 11 API contracts indexed on the [APIs.io](https://apis.io/) network, including Companies API, Customers API, Items API, and 8 more. Tagged areas include ERP, Cloud ERP, Finance, Accounting, and Supply Chain.


  The Microsoft Dynamics 365 Business Central catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Microsoft Dynamics 365 Business Central''s developer surface includes sandbox, getting-started guide, authentication, documentation, pricing, signup flow, engineering blog, and 36 more developer resources.'
plans:
- name: Microsoft Dynamics 365 Business Central Plans Pricing
  plan_count: 6
  slug: microsoft-dynamics-365-business-central-plans-pricing
- name: Microsoft Dynamics 365 Business Central Price Estimates
  plan_count: 0
  slug: microsoft-dynamics-365-business-central-price-estimates
random_paper: 5
rate_limits:
- limit_count: 9
  name: Microsoft Dynamics 365 Business Central Rate Limits
  slug: microsoft-dynamics-365-business-central-rate-limits
rules:
- authorship: generated
  effective_rule_count: 98
  extends:
  - spectral:oas
  name: Microsoft Dynamics 365 Business Central API Rules
  rule_count: 57
  severity_counts:
    error: 55
    hint: 0
    info: 1
    warn: 1
  slug: microsoft-dynamics-365-business-central-rules
scopes:
- name: Microsoft Dynamics 365 Business Central Scopes
  scope_count: 1
  slug: microsoft-dynamics-365-business-central-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 70.2
  coverage:
    artifact_dirs: 30
    catalog_earned: 83.8
    catalog_earned_first_party: 24.0
    catalog_gap: 31.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 28.9
  facets:
    access_clarity: 92.1
    contract_governance: 22.0
    contract_quality: 56.9
    developer_ergonomics: 64.3
    discoverability: 73.3
    operational_transparency: 84.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 7
    mcp: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/microsoft-dynamics-365-business-central/microsoft-dynamics-365-business-central-2026-06-20T185459.png
security:
- kind: authentication
  name: Microsoft Dynamics 365 Business Central Authentication
  slug: microsoft-dynamics-365-business-central-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Microsoft Dynamics 365 Business Central Domain Security
  slug: microsoft-dynamics-365-business-central-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Microsoft Dynamics 365 Business Central Vulnerability Disclosure
  slug: microsoft-dynamics-365-business-central-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Microsoft Dynamics 365 Business Central Trust Center
  slug: microsoft-dynamics-365-business-central-trust-center
  summary_line: GDPR
slug: microsoft-dynamics-365-business-central
tags:
- ERP
- Cloud ERP
- Finance
- Accounting
- Supply Chain
- Small Business
- Mid-Market
- Microsoft Dynamics 365
website: https://www.microsoft.com/en-us/dynamics-365/products/business-central
---

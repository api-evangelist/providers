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
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: verified
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: verified
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 45.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 312
  human_in_the_loop: 3
  name: Keap Agentic Access
  operation_count: 540
  slug: keap-agentic-access
  summary_line: 540 operations · 312 acting · 3 human-in-the-loop
api_count: 8
apis:
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Affiliate API — 48 operations across 28 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Affiliate API
  slug: keap-affiliate-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Automation API — 10 operations across 9 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Automation API
  slug: keap-automation-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Campaign API — 6 operations across 6 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Campaigns API
  slug: keap-campaigns-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Category Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Category Discounts API
  slug: keap-category-discounts-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Company API — 22 operations across 11 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Companies API
  slug: keap-companies-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Contact API — 27 operations across 16 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Contacts API
  slug: keap-contacts-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Email API — 10 operations across 8 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Email API
  slug: keap-email-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Files API — 6 operations across 3 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Files API
  slug: keap-files-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Free Trial Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Free Trial Discounts API
  slug: keap-free-trial-discounts-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Lead Source Categories API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Source Categories API
  slug: keap-lead-source-categories-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Lead Source Expenses API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Source Expenses API
  slug: keap-lead-source-expenses-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Lead Source Recurring Expenses API — 6 operations across 3 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Source Recurring Expenses API
  slug: keap-lead-source-recurring-expenses-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Lead Sources API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Lead Sources API
  slug: keap-lead-sources-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Note API — 21 operations across 11 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Note API
  slug: keap-note-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Opportunity API — 26 operations across 13 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Opportunities API
  slug: keap-opportunities-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Order Total Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Order Total Discounts API
  slug: keap-order-total-discounts-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Orders API — 29 operations across 16 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Orders API
  slug: keap-orders-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Product Categories API — 9 operations across 5 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product Categories API
  slug: keap-product-categories-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Product Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product Discounts API
  slug: keap-product-discounts-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Product Interest Bundles API — 8 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Product Interest Bundles API
  slug: keap-product-interest-bundles-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Products API — 17 operations across 9 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Products API
  slug: keap-products-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Shipping Discounts API — 7 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Shipping Discounts API
  slug: keap-shipping-discounts-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Subscription Plans API — 5 operations across 2 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Subscription Plans API
  slug: keap-subscription-plans-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Subscriptions API — 20 operations across 11 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Subscriptions API
  slug: keap-subscriptions-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Tags API — 14 operations across 8 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Tags API
  slug: keap-tags-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Task API — 19 operations across 9 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Tasks API
  slug: keap-tasks-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Keap Users API — 5 operations across 4 paths on the Keap REST v2 contract, read from Keap's own published OpenAPI 3.1 document.
  name: Keap Users API
  slug: keap-users-api
- baseURL: https://api.infusionsoft.com/crm/rest/v1
  baseurl_source: declared
  description: The Appointment API from Keap — 4 operation(s) for appointment.
  name: Keap Appointment API
  slug: keap-appointment-api
- baseURL: https://api.infusionsoft.com/crm/rest/v1
  baseurl_source: declared
  description: The File API from Keap — 2 operation(s) for file.
  name: Keap File API
  slug: keap-file-api
- baseURL: https://api.infusionsoft.com/crm/rest/v1
  baseurl_source: declared
  description: The Product API from Keap — 6 operation(s) for product.
  name: Keap Product API
  slug: keap-product-api
- baseURL: https://api.infusionsoft.com/crm/rest/v1
  baseurl_source: declared
  description: The REST Hooks API from Keap — 5 operation(s) for rest hooks.
  name: Keap REST Hooks API
  slug: keap-rest-hooks-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Account Info-Endpoint
  name: Keap Account Info API
  slug: keap-account-info-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The AutomationCategory API from Keap — 2 operation(s) for automationcategory.
  name: Keap Automation Category API
  slug: keap-automationcategory-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Business Profile API from Keap — 1 operation(s) for business profile.
  name: Keap Business Profile API
  slug: keap-business-profile-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Email-Addresses-Endpoint
  name: Keap Email Address API
  slug: keap-email-address-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Integrations API from Keap — 3 operation(s) for integrations.
  name: Keap Integrations API
  slug: keap-integrations-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The LeadScore API from Keap — 1 operation(s) for leadscore.
  name: Keap Lead Score API
  slug: keap-leadscore-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Locale-Endpoint
  name: Keap Locale API
  slug: keap-locale-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Merchant-Endpoint
  name: Keap Merchant API
  slug: keap-merchant-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Merchants API from Keap — 1 operation(s) for merchants.
  name: Keap Merchants API
  slug: keap-merchants-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Payment Method Configs API from Keap — 1 operation(s) for payment method configs.
  name: Keap Payment Method Configs API
  slug: keap-payment-method-configs-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Payment Methods API from Keap — 4 operation(s) for payment methods.
  name: Keap Payment Methods API
  slug: keap-payment-methods-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Referral API from Keap — 1 operation(s) for referral.
  name: Keap Referral API
  slug: keap-referral-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Reporting API from Keap — 4 operation(s) for reporting.
  name: Keap Reporting API
  slug: keap-reporting-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Sales API from Keap — 3 operation(s) for sales.
  name: Keap Sales API
  slug: keap-sales-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: Setting-Endpoint
  name: Keap Setting API
  slug: keap-setting-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Settings API from Keap — 3 operation(s) for settings.
  name: Keap Settings API
  slug: keap-settings-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Shipping API from Keap — 1 operation(s) for shipping.
  name: Keap Shipping API
  slug: keap-shipping-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The User Groups API from Keap — 2 operation(s) for user groups.
  name: Keap User Groups API
  slug: keap-user-groups-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Webforms API from Keap — 2 operation(s) for webforms.
  name: Keap Webforms API
  slug: keap-webforms-api
- description: The legacy Infusionsoft XML-RPC API, explicitly labelled Deprecated in the Keap developer guide. It remains documented, with a published table schema reference, but Keap publishes no sunset date for i
  name: Keap XML-RPC API (legacy Infusionsoft)
  slug: keap-xml-rpc-api
- baseURL: https://api.infusionsoft.com/crm/xmlrpc/v1
  baseurl_source: declared
  description: UserInfo-Endpoint
  name: Keap User Info API
  slug: keap-user-info-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Custom Fields API from Keap — 2 operation(s) for custom fields.
  name: Keap Custom Fields API
  slug: keap-custom-fields-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The DateExpression API from Keap — 1 operation(s) for dateexpression.
  name: Keap Date Expression API
  slug: keap-dateexpression-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Deals API from Keap — 12 operation(s) for deals.
  name: Keap Deals API
  slug: keap-deals-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Display Forms API from Keap — 1 operation(s) for display forms.
  name: Keap Display Forms API
  slug: keap-display-forms-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Pipelines API from Keap — 8 operation(s) for pipelines.
  name: Keap Pipelines API
  slug: keap-pipelines-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: The Stages API from Keap — 4 operation(s) for stages.
  name: Keap Stages API
  slug: keap-stages-api
- baseURL: https://api.infusionsoft.com/crm/rest/v2
  baseurl_source: declared
  description: E-Commerce-Endpoint
  name: Keap Ecommerce API
  slug: keap-ecommerce-api
artifact_total: 83
asyncapis:
- description: AsyncAPI 2.6 description of the Keap (formerly Infusionsoft) REST Hooks webhook surface. Keap REST Hooks are subscriptions that are created and managed via the v1 REST API (`POST /rest/v1/hooks`). Onc
  name: Keap REST Hooks
  slug: keap-resthooks-asyncapi
collections:
- collection_type: open
  name: Keap REST Campaigns API
  slug: open-keap-campaigns-api
- collection_type: open
  name: Keap REST Campaigns Companies API
  slug: open-keap-companies-api
- collection_type: open
  name: Keap REST Campaigns Contacts API
  slug: open-keap-contacts-api
- collection_type: open
  name: Keap REST Campaigns Opportunities API
  slug: open-keap-opportunities-api
- collection_type: open
  name: Keap REST Campaigns Orders API
  slug: open-keap-orders-api
- collection_type: open
  name: Keap REST Campaigns Products API
  slug: open-keap-products-api
- collection_type: open
  name: Keap REST Campaigns Tags API
  slug: open-keap-tags-api
- collection_type: open
  name: Keap REST Campaigns Tasks API
  slug: open-keap-tasks-api
- collection_type: open
  name: Keap REST API
  slug: open-keap
common:
- group: commercial
  title: ''
  type: License
  url: https://github.com/infusionsoft/keap-sdk/blob/main/LICENSE
- group: other
  href: https://artifacts.apis.io/keap/capabilities/keap-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/keap-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/keap/overlays/keap-appointment-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keap-appointment-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/keap/overlays/keap-e-commerce-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keap-e-commerce-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/keap/overlays/keap-file-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keap-file-v1-overlay.yaml
- group: other
  href: https://artifacts.apis.io/keap/overlays/keap-product-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/keap-product-v1-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/keap/agentic-access/keap-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/keap-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/keap/security/keap-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/keap-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/keap/authentication/keap-authentication.yml
  title: ''
  type: Authentication
  url: authentication/keap-authentication.yml
- group: auth
  href: https://artifacts.apis.io/keap/scopes/keap-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/keap-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/keap-growing
- group: company
  title: ''
  type: Website
  url: https://keap.com
- group: docs
  title: ''
  type: Documentation
  url: https://developer.infusionsoft.com/
- group: start
  title: ''
  type: Signup
  url: https://keap.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://keap.com/pricing
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.infusionsoft.com/
- group: auth
  title: ''
  type: OAuth
  url: https://developer.infusionsoft.com/getting-started-oauth-keys/
- group: company
  title: ''
  type: Blog
  url: https://keap.com/small-business-automation-blog
- group: agent
  href: https://artifacts.apis.io/keap/well-known/keap-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/keap-well-known.yml
- group: agent
  href: https://artifacts.apis.io/keap/mcp/keap-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/keap-mcp.yml
- group: build
  href: https://artifacts.apis.io/keap/mcp/keap-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/keap-tool-crosswalk.yml
- group: build
  href: https://artifacts.apis.io/keap/packages/keap-packages.yml
  title: ''
  type: Packages
  url: packages/keap-packages.yml
- group: build
  href: https://artifacts.apis.io/keap/packages/keap-packages.yml
  title: ''
  type: SDKs
  url: packages/keap-packages.yml
- group: agent
  href: https://artifacts.apis.io/keap/llms/keap-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/keap-llms.txt
- group: design
  href: https://artifacts.apis.io/keap/conformance/keap-conformance.yml
  title: ''
  type: Conformance
  url: conformance/keap-conformance.yml
- group: auth
  href: https://artifacts.apis.io/keap/conformance/keap-conformance.yml
  title: ''
  type: Compliance
  url: conformance/keap-conformance.yml
- group: design
  href: https://artifacts.apis.io/keap/errors/keap-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/keap-problem-types.yml
- group: design
  href: https://artifacts.apis.io/keap/lifecycle/keap-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/keap-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.thryv.com/
- group: operate
  href: https://artifacts.apis.io/keap/lifecycle/keap-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/keap-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/keap/conventions/keap-conventions.yml
  title: ''
  type: Conventions
  url: conventions/keap-conventions.yml
- group: start
  href: https://artifacts.apis.io/keap/sandbox/keap-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/keap-sandbox.yml
- group: design
  href: https://artifacts.apis.io/keap/components/keap-components.yml
  title: ''
  type: Components
  url: components/keap-components.yml
- group: design
  href: https://artifacts.apis.io/keap/data-model/keap-data-model.yml
  title: ''
  type: DataModel
  url: data-model/keap-data-model.yml
- group: commercial
  href: https://artifacts.apis.io/keap/plans/keap-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/keap-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/keap/rate-limits/keap-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/keap-rate-limits.yml
- group: agent
  href: https://artifacts.apis.io/keap/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: docs
  href: https://artifacts.apis.io/keap/asyncapi/keap-resthooks-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/keap-resthooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/keap/asyncapi/keap-resthooks-asyncapi.yml
  title: ''
  type: Webhooks
  url: asyncapi/keap-resthooks-asyncapi.yml
- group: design
  href: https://artifacts.apis.io/keap/rules/keap-asyncapi-spectral-rules.yml
  title: ''
  type: Rules
  url: rules/keap-asyncapi-spectral-rules.yml
- group: docs
  title: ''
  type: APIReference
  url: https://developer.infusionsoft.com/docs/restv2/
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.infusionsoft.com/getting-started-oauth-keys/
- group: operate
  title: ''
  type: Support
  url: https://developer.infusionsoft.com/get-support/
- group: operate
  title: ''
  type: HelpCenter
  url: https://developer.infusionsoft.com/faqs/
- group: operate
  title: ''
  type: Community
  url: https://community.keap.com/c/api/5
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/infusionsoft
- group: build
  title: ''
  type: Postman
  url: https://documenter.getpostman.com/view/2915979/UVByKWEZ
- group: start
  title: ''
  type: SignUp
  url: https://keys.developer.keap.com/accounts/create
- group: start
  title: ''
  type: Login
  url: https://keys.developer.keap.com/my-apps
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.thryv.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.thryv.com/privacy/
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.keap.com/apps
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/infusionsoft/keap-sdk
- group: operate
  title: ''
  type: KnownIssues
  url: https://developer.infusionsoft.com/support/known-issues/
- group: docs
  title: ''
  type: DeveloperGuide
  url: https://developer.infusionsoft.com/developer-guide/
- group: other
  title: ''
  type: X
  url: https://twitter.com/keapgrowing
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Keap
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.keap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.keap.com/docs/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.keap.com/docs/restv2/
created: '2026-05-11'
description: Keap (formerly Infusionsoft, now part of Thryv) is a CRM, sales and marketing automation platform for small businesses that combines contact management, email and text marketing, e-commerce, affiliate management and pipeline automation. Keap publishes two live OpenAPI 3.1 contracts covering 540 operations — REST v2 (399 operations, the Default version) and REST v1 (141 operations, still the only home of REST Hooks webhooks and Appointments) — plus a deprecated XML-RPC surface. Authentication is OAuth 2.0 authorization code with rotating refresh tokens, or Personal Access Tokens and Service Account Keys, all with a single `full` scope. Keap also operates an undocumented but live remote MCP server at https://api.keap.com/mcp secured with OAuth 2.1, PKCE and dynamic client registration, and ships first-party SDKs for six languages generated in lock-step from its own spec.
finops:
- has_sources: true
  method: derived
  name: Keap Finops
  primary_unit: tier
  service_category: ''
  slug: keap-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/keap.png
layout: provider
mcp_servers:
- description: 'Keap operates a real, first-party REMOTE MCP server. It is undocumented — the string "MCP" does not appear anywhere on developer.keap.com / developer.infusionsoft.com — but it is unambiguously theirs '
  name: Keap MCP Server
  slug: keap-mcp-server
modified: '2026-08-13'
name: Keap
nav: Providers
network: true
overview: 'Keap publishes 59 API contracts indexed on the [APIs.io](https://apis.io/) network, including Affiliate API, Automation API, Campaigns API, and 56 more. Tagged areas include CRM, Sales, Marketing Automation, Small Business, and E-Commerce.


  The Keap catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Keap''s developer surface includes authentication, documentation, signup flow, pricing, engineering blog, sandbox, API reference, and 53 more developer resources.'
plans:
- name: Keap Plans Pricing
  plan_count: 11
  slug: keap-plans-pricing
- name: Keap Price Estimates
  plan_count: 0
  slug: keap-price-estimates
random_paper: 9
rate_limits:
- limit_count: 0
  name: Keap Rate Limits
  slug: keap-rate-limits
rules:
- authorship: generated
  effective_rule_count: 33
  extends:
  - spectral:asyncapi
  name: Keap — asyncapi rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: keap-asyncapi-spectral-rules
scopes:
- name: Keap Scopes
  scope_count: 1
  slug: keap-scopes
  summary_line: 1 scope · authorizationCode
score:
  band: exemplar
  composite: 68.1
  coverage:
    artifact_dirs: 32
    catalog_earned: 58.8
    catalog_earned_first_party: 12.0
    catalog_gap: 56.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 92.1
    contract_governance: 15.9
    contract_quality: 61.4
    developer_ergonomics: 78.0
    discoverability: 73.3
    operational_transparency: 34.2
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 68.1
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 58
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Payments
    regime_id: payments
    score: 35.7
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/keap/keap-2026-06-20T183931.png
security:
- kind: authentication
  name: Keap Authentication
  slug: keap-authentication
  summary_line: 4 schemes
- kind: domain-security
  name: Keap Domain Security
  slug: keap-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
skill_count: 4
skills:
- name: keap-lead-capture-and-tagging
  slug: keap-lead-capture-and-tagging
- name: keap-order-and-subscription-billing
  slug: keap-order-and-subscription-billing
- name: keap-rest-hooks-subscription
  slug: keap-rest-hooks-subscription
- name: keap-sales-pipeline-management
  slug: keap-sales-pipeline-management
slug: keap
tags:
- CRM
- Sales
- Marketing Automation
- Small Business
- E-Commerce
- Contacts
- Email Marketing
- Subscription
- Affiliate Management
- Webhook
- MCP
- Payments
- Sales Automation
website: https://keap.com
---

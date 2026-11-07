---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
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
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: templated
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 54.7
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 400
  human_in_the_loop: 4
  name: Emporix Agentic Access
  operation_count: 670
  slug: emporix-agentic-access
  summary_line: 670 operations · 400 acting · 4 human-in-the-loop
api_count: 44
apis:
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Access Control Templates API from Emporix — 1 operation(s) for access control templates.
  name: Emporix Access Control Templates API
  slug: emporix-access-control-templates-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Access Controls API from Emporix — 2 operation(s) for access controls.
  name: Emporix Access Controls API
  slug: emporix-access-controls-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage customer account details.
  name: Emporix Account and profile API
  slug: emporix-account-and-profile-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage customer address information.
  name: Emporix Addresses API
  slug: emporix-addresses-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Agent analytics and execution metrics
  name: Emporix Agent Analytics API
  slug: emporix-agent-analytics-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Agents
  name: Emporix Agent API
  slug: emporix-agent-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Chat With Agents
  name: Emporix Agent Chat API
  slug: emporix-agent-chat-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read Agent Logs
  name: Emporix Agent Logs API
  slug: emporix-agent-logs-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Agent Templates
  name: Emporix Agent Template API
  slug: emporix-agent-template-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: AI Completions
  name: Emporix AI Completions API
  slug: emporix-ai-completions-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read aggregated import statistics, health, and the settings behind them.
  name: Emporix Analytics API
  slug: emporix-analytics-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Approval API from Emporix — 1 operation(s) for approval.
  name: Emporix Approval API
  slug: emporix-approval-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Approvals API from Emporix — 2 operation(s) for approvals.
  name: Emporix Approvals API
  slug: emporix-approvals-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Assets
  name: Emporix Assets API
  slug: emporix-assets-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Assignments
  name: Emporix Assignment Resources API
  slug: emporix-assignment-resources-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Create and manage customer access tokens.
  name: Emporix Authentication and authorization API
  slug: emporix-authentication-and-authorization-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Availabilities API from Emporix — 4 operation(s) for availabilities.
  name: Emporix Availabilities API
  slug: emporix-availabilities-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage brands
  name: Emporix Brands API
  slug: emporix-brands-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Cart items
  name: Emporix Cart items API
  slug: emporix-cart-items-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Carts
  name: Emporix Carts API
  slug: emporix-carts-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Retrieve lists of catalogs and manage catalog details.
  name: Emporix Catalog management API
  slug: emporix-catalog-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Category Assignments
  name: Emporix Category Assignment Resources API
  slug: emporix-category-assignment-resources-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Categories
  name: Emporix Category Resources API
  slug: emporix-category-resources-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read Category Trees
  name: Emporix Category Tree Resources API
  slug: emporix-category-tree-resources-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Query tenant change history.
  name: Emporix Changelogs API
  slug: emporix-changelogs-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Checkouts API from Emporix — 1 operation(s) for checkouts.
  name: Emporix Checkouts API
  slug: emporix-checkouts-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Client Configurations
  name: Emporix Client configurations API
  slug: emporix-client-configurations-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read Commerce Events
  name: Emporix Commerce Events API
  slug: emporix-commerce-events-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Config API from Emporix — 2 operation(s) for config.
  name: Emporix Config API
  slug: emporix-config-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Configuration API from Emporix — 2 operation(s) for configuration.
  name: Emporix Configuration API
  slug: emporix-configuration-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read import configurations.
  name: Emporix Configurations API
  slug: emporix-configurations-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Contact Assignments API from Emporix — 2 operation(s) for contact assignments.
  name: Emporix Contact Assignments API
  slug: emporix-contact-assignments-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Agent Conversations
  name: Emporix Conversation API
  slug: emporix-conversation-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Countries API from Emporix — 2 operation(s) for countries.
  name: Emporix Countries API
  slug: emporix-countries-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Coupon Management API from Emporix — 2 operation(s) for coupon management.
  name: Emporix Coupon Management API
  slug: emporix-coupon-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Coupon Redemption API from Emporix — 2 operation(s) for coupon redemption.
  name: Emporix Coupon Redemption API
  slug: emporix-coupon-redemption-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Coupon Validation API from Emporix — 1 operation(s) for coupon validation.
  name: Emporix Coupon Validation API
  slug: emporix-coupon-validation-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage customer credentials.
  name: Emporix Credentials API
  slug: emporix-credentials-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Currencies API from Emporix — 2 operation(s) for currencies.
  name: Emporix Currencies API
  slug: emporix-currencies-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Currency exchange API from Emporix — 2 operation(s) for currency exchange.
  name: Emporix Currency exchange API
  slug: emporix-currency-exchange-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Custom Instance API from Emporix — 4 operation(s) for custom instance.
  name: Emporix Custom Instance API
  slug: emporix-custom-instance-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Custom Schema Type API from Emporix — 2 operation(s) for custom schema type.
  name: Emporix Custom Schema Type API
  slug: emporix-custom-schema-type-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage shipping customer groups
  name: Emporix Customer Group Relations API
  slug: emporix-customer-group-relations-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage customer assignments to segments
  name: Emporix Customers Assignments API
  slug: emporix-customers-assignments-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read imported records.
  name: Emporix Data API
  slug: emporix-data-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Generate delivery cycles
  name: Emporix Delivery Cycles API
  slug: emporix-delivery-cycles-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage delivery times
  name: Emporix Delivery Times Management API
  slug: emporix-delivery-times-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage delivery time slots
  name: Emporix Delivery Times Slots Management API
  slug: emporix-delivery-times-slots-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage delivery windows
  name: Emporix Delivery Windows API
  slug: emporix-delivery-windows-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Discounts
  name: Emporix Discounts API
  slug: emporix-discounts-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Allow option for double opt-in.
  name: Emporix Double opt-in API
  slug: emporix-double-opt-in-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Events API from Emporix — 1 operation(s) for events.
  name: Emporix Events API
  slug: emporix-events-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Run a chain of existing cart operations in one request.
  name: Emporix Execute API
  slug: emporix-execute-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Export / Import API from Emporix — 4 operation(s) for export / import.
  name: Emporix Export / Import API
  slug: emporix-export-import-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Fee management API from Emporix — 2 operation(s) for fee management.
  name: Emporix Fee management API
  slug: emporix-fee-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read Global Configurations
  name: Emporix Global configurations API
  slug: emporix-global-configurations-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Group Assignments API from Emporix — 4 operation(s) for group assignments.
  name: Emporix Group Assignments API
  slug: emporix-group-assignments-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Groups API from Emporix — 4 operation(s) for groups.
  name: Emporix Groups API
  slug: emporix-groups-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage IAM group assignments to segments
  name: Emporix Groups Assignments API
  slug: emporix-groups-assignments-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Import and migration API from Emporix — 2 operation(s) for import and migration.
  name: Emporix Import and migration API
  slug: emporix-import-and-migration-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Import & Export Agents
  name: Emporix Import/Export API
  slug: emporix-import-export-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Index Jobs API from Emporix — 2 operation(s) for index jobs.
  name: Emporix Index Jobs API
  slug: emporix-index-jobs-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Invoice Jobs API from Emporix — 2 operation(s) for invoice jobs.
  name: Emporix Invoice Jobs API
  slug: emporix-invoice-jobs-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Item fee management API from Emporix — 3 operation(s) for item fee management.
  name: Emporix Item fee management API
  slug: emporix-item-fee-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Item fee search API from Emporix — 3 operation(s) for item fee search.
  name: Emporix Item fee search API
  slug: emporix-item-fee-search-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage item assignments to segments
  name: Emporix Items Assignments API
  slug: emporix-items-assignments-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Jobs
  name: Emporix Job API
  slug: emporix-job-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Label API from Emporix — 2 operation(s) for label.
  name: Emporix Label API
  slug: emporix-label-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Legal Entities API from Emporix — 4 operation(s) for legal entities.
  name: Emporix Legal Entities API
  slug: emporix-legal-entities-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read the tenant's import limits.
  name: Emporix License API
  slug: emporix-license-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Locations API from Emporix — 7 operation(s) for locations.
  name: Emporix Locations API
  slug: emporix-locations-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Management Dashboard Users API from Emporix — 4 operation(s) for management dashboard users.
  name: Emporix Management Dashboard Users API
  slug: emporix-management-dashboard-users-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage MCP Servers
  name: Emporix MCP Server API
  slug: emporix-mcp-server-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Metadata
  name: Emporix Metadata API
  slug: emporix-metadata-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Mixins API from Emporix — 2 operation(s) for mixins.
  name: Emporix Mixins API
  slug: emporix-mixins-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read LLM models from supported providers
  name: Emporix Model API
  slug: emporix-model-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage OAuth configurations (Preview)
  name: Emporix OAuth API
  slug: emporix-oauth-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage customer orders. **Authentication:** Standard is customer token (Bearer). Alternatively, use access token (client credentials) together with the `saas-token` header.
  name: Emporix Orders (Customer-managed) API
  slug: emporix-orders-customer-managed-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage tenant orders.
  name: Emporix Orders (Tenant-managed) API
  slug: emporix-orders-tenant-managed-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Own session context modification API from Emporix — 2 operation(s) for own session context modification.
  name: Emporix Own session context modification API
  slug: emporix-own-session-context-modification-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Own session management API from Emporix — 1 operation(s) for own session management.
  name: Emporix Own session management API
  slug: emporix-own-session-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Payment API from Emporix — 4 operation(s) for payment.
  name: Emporix Payment API
  slug: emporix-payment-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Payment - frontend API from Emporix — 2 operation(s) for payment - frontend.
  name: Emporix Payment - frontend API
  slug: emporix-payment-frontend-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Payment mode API from Emporix — 2 operation(s) for payment mode.
  name: Emporix Payment mode API
  slug: emporix-payment-mode-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Payment mode - frontend API from Emporix — 2 operation(s) for payment mode - frontend.
  name: Emporix Payment mode - frontend API
  slug: emporix-payment-mode-frontend-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Permissions API from Emporix — 2 operation(s) for permissions.
  name: Emporix Permissions API
  slug: emporix-permissions-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Price lists API from Emporix — 3 operation(s) for price lists.
  name: Emporix Price lists API
  slug: emporix-price-lists-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Price matching API from Emporix — 2 operation(s) for price matching.
  name: Emporix Price matching API
  slug: emporix-price-matching-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Price models API from Emporix — 2 operation(s) for price models.
  name: Emporix Price models API
  slug: emporix-price-models-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Prices API from Emporix — 4 operation(s) for prices.
  name: Emporix Prices API
  slug: emporix-prices-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Prices assigned to price lists API from Emporix — 4 operation(s) for prices assigned to price lists.
  name: Emporix Prices assigned to price lists API
  slug: emporix-prices-assigned-to-price-lists-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Product fees management API from Emporix — 2 operation(s) for product fees management.
  name: Emporix Product fees management API
  slug: emporix-product-fees-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage product templates. Product templates define a set of attributes which are common for all product instances based on that template.
  name: Emporix Product Templates API
  slug: emporix-product-templates-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: 'Manage products. Supported product types include: - `BASIC` — standalone products - `BUNDLE` — groups of products sold together - `PARENT_VARIANT` — products with automatically generated variants defi'
  name: Emporix Products API
  slug: emporix-products-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Public Configuration API from Emporix — 2 operation(s) for public configuration.
  name: Emporix Public Configuration API
  slug: emporix-public-configuration-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Quote history API from Emporix — 1 operation(s) for quote history.
  name: Emporix Quote history API
  slug: emporix-quote-history-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Quote management API from Emporix — 2 operation(s) for quote management.
  name: Emporix Quote management API
  slug: emporix-quote-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Quote pdf API from Emporix — 1 operation(s) for quote pdf.
  name: Emporix Quote pdf API
  slug: emporix-quote-pdf-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Quote reason API from Emporix — 2 operation(s) for quote reason.
  name: Emporix Quote reason API
  slug: emporix-quote-reason-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Redeem Options Management API from Emporix — 2 operation(s) for redeem options management.
  name: Emporix Redeem Options Management API
  slug: emporix-redeem-options-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Reference API from Emporix — 2 operation(s) for reference.
  name: Emporix Reference API
  slug: emporix-reference-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Referral Coupon Management API from Emporix — 1 operation(s) for referral coupon management.
  name: Emporix Referral Coupon Management API
  slug: emporix-referral-coupon-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Regions API from Emporix — 2 operation(s) for regions.
  name: Emporix Regions API
  slug: emporix-regions-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Invoke Reindex
  name: Emporix Reindex API
  slug: emporix-reindex-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Resources API from Emporix — 2 operation(s) for resources.
  name: Emporix Resources API
  slug: emporix-resources-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Returns API from Emporix — 2 operation(s) for returns.
  name: Emporix Returns API
  slug: emporix-returns-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Reward Points Management API from Emporix — 5 operation(s) for reward points management.
  name: Emporix Reward Points Management API
  slug: emporix-reward-points-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Roles API from Emporix — 2 operation(s) for roles.
  name: Emporix Roles API
  slug: emporix-roles-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Trigger, monitor, and cancel import runs.
  name: Emporix Runs API
  slug: emporix-runs-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Saved Searches API from Emporix — 3 operation(s) for saved searches.
  name: Emporix Saved Searches API
  slug: emporix-saved-searches-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read and set a configuration's run schedule.
  name: Emporix Schedules API
  slug: emporix-schedules-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Schema API from Emporix — 3 operation(s) for schema.
  name: Emporix Schema API
  slug: emporix-schema-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Scopes API from Emporix — 2 operation(s) for scopes.
  name: Emporix Scopes API
  slug: emporix-scopes-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Search API from Emporix — 2 operation(s) for search.
  name: Emporix Search API
  slug: emporix-search-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Search Indexes API from Emporix — 3 operation(s) for search indexes.
  name: Emporix Search Indexes API
  slug: emporix-search-indexes-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage segments
  name: Emporix Segments API
  slug: emporix-segments-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Sequential IDs management API from Emporix — 6 operation(s) for sequential ids management.
  name: Emporix Sequential IDs management API
  slug: emporix-sequential-ids-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Service Access Token API from Emporix — 1 operation(s) for service access token.
  name: Emporix Service Access Token API
  slug: emporix-service-access-token-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Session context modification API from Emporix — 2 operation(s) for session context modification.
  name: Emporix Session context modification API
  slug: emporix-session-context-modification-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Session management API from Emporix — 1 operation(s) for session management.
  name: Emporix Session management API
  slug: emporix-session-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage shipping costs
  name: Emporix Shipping Cost API
  slug: emporix-shipping-cost-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage shipping groups
  name: Emporix Shipping Groups API
  slug: emporix-shipping-groups-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage shipping methods
  name: Emporix Shipping Methods API
  slug: emporix-shipping-methods-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage shipping zones
  name: Emporix Shipping Zones API
  slug: emporix-shipping-zones-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Shopping Lists API from Emporix — 2 operation(s) for shopping lists.
  name: Emporix Shopping Lists API
  slug: emporix-shopping-lists-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Signed-In Customer Reward Points API from Emporix — 3 operation(s) for signed-in customer reward points.
  name: Emporix Signed-In Customer Reward Points API
  slug: emporix-signed-in-customer-reward-points-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Site settings API from Emporix — 3 operation(s) for site settings.
  name: Emporix Site settings API
  slug: emporix-site-settings-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Find shipping related sites
  name: Emporix Sites API
  slug: emporix-sites-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read the streams of a configuration.
  name: Emporix Streams API
  slug: emporix-streams-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Svix Emporix Shared Account API from Emporix — 2 operation(s) for svix emporix shared account.
  name: Emporix Svix Emporix Shared Account API
  slug: emporix-svix-emporix-shared-account-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Tax calculation API from Emporix — 1 operation(s) for tax calculation.
  name: Emporix Tax calculation API
  slug: emporix-tax-calculation-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Taxes API from Emporix — 2 operation(s) for taxes.
  name: Emporix Taxes API
  slug: emporix-taxes-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Tenant Configurations
  name: Emporix Tenant configurations API
  slug: emporix-tenant-configurations-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: AI Text Generation
  name: Emporix Text Generation API
  slug: emporix-text-generation-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Tokens
  name: Emporix Token API
  slug: emporix-token-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Tools
  name: Emporix Tool API
  slug: emporix-tool-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Transaction API from Emporix — 2 operation(s) for transaction.
  name: Emporix Transaction API
  slug: emporix-transaction-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Type API from Emporix — 2 operation(s) for type.
  name: Emporix Type API
  slug: emporix-type-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Read Units
  name: Emporix Type management API
  slug: emporix-type-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Convert Units
  name: Emporix Unit conversion API
  slug: emporix-unit-conversion-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: Manage Units
  name: Emporix Unit management API
  slug: emporix-unit-management-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Users API from Emporix — 8 operation(s) for users.
  name: Emporix Users API
  slug: emporix-users-api
- baseURL: https://api.emporix.io
  baseurl_source: declared
  description: The Vendors API from Emporix — 3 operation(s) for vendors.
  name: Emporix Vendors API
  slug: emporix-vendors-api
artifact_total: 342
asyncapis:
- description: ''
  name: Emporix Webhooks
  slug: emporix-webhooks
common:
- group: other
  href: https://artifacts.apis.io/emporix/capabilities/emporix-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/emporix-capability-edges.yml
- group: operate
  href: https://artifacts.apis.io/emporix/changelog/emporix-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/emporix-changelog.yml
- group: build
  href: https://artifacts.apis.io/emporix/integrations/emporix-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/emporix-integration-edges.yml
- group: agent
  href: https://artifacts.apis.io/emporix/agentic-access/emporix-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/emporix-agentic-access.yml
- group: operate
  href: https://artifacts.apis.io/emporix/rate-limits/emporix-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/emporix-rate-limits.yml
- group: design
  href: https://artifacts.apis.io/emporix/rules/emporix-rules.yml
  title: ''
  type: Spectral
  url: rules/emporix-rules.yml
- group: design
  href: https://artifacts.apis.io/emporix/json-ld/emporix-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/emporix-context.jsonld
- group: design
  href: https://artifacts.apis.io/emporix/vocabulary/emporix-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/emporix-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/emporix/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/emporix/asyncapi/emporix-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/emporix-webhooks.yml
- group: design
  href: https://artifacts.apis.io/emporix/data-model/emporix-data-model.yml
  title: ''
  type: DataModel
  url: data-model/emporix-data-model.yml
- group: design
  href: https://artifacts.apis.io/emporix/components/emporix-components.yml
  title: ''
  type: Components
  url: components/emporix-components.yml
- group: design
  href: https://artifacts.apis.io/emporix/conventions/emporix-conventions.yml
  title: ''
  type: Conventions
  url: conventions/emporix-conventions.yml
- group: start
  href: https://artifacts.apis.io/emporix/sandbox/emporix-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/emporix-sandbox.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.emporix.com/
- group: operate
  href: https://artifacts.apis.io/emporix/lifecycle/emporix-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/emporix-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.emporix.io
- group: design
  href: https://artifacts.apis.io/emporix/lifecycle/emporix-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/emporix-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/emporix/errors/emporix-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/emporix-problem-types.yml
- group: design
  href: https://artifacts.apis.io/emporix/conformance/emporix-conformance.yml
  title: ''
  type: Conformance
  url: conformance/emporix-conformance.yml
- group: other
  href: https://artifacts.apis.io/emporix/overlays/emporix-ai-rag-indexer-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/emporix-ai-rag-indexer-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/emporix/llms/emporix-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/emporix-llms.txt
- group: build
  href: https://artifacts.apis.io/emporix/mcp/emporix-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/emporix-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/emporix/mcp/emporix-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/emporix-mcp.yml
- group: agent
  href: https://artifacts.apis.io/emporix/well-known/emporix-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/emporix-well-known.yml
- group: other
  href: https://artifacts.apis.io/emporix/hosts/emporix-hosts.yml
  title: ''
  type: Hosts
  url: hosts/emporix-hosts.yml
- group: other
  href: https://artifacts.apis.io/emporix/vendors/emporix-vendors.yml
  title: ''
  type: Vendors
  url: vendors/emporix-vendors.yml
- group: build
  href: https://artifacts.apis.io/emporix/packages/emporix-packages.yml
  title: ''
  type: Packages
  url: packages/emporix-packages.yml
- group: auth
  href: https://artifacts.apis.io/emporix/authentication/emporix-authentication.yml
  title: ''
  type: Authentication
  url: authentication/emporix-authentication.yml
- group: auth
  href: https://artifacts.apis.io/emporix/scopes/emporix-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/emporix-scopes.yml
- group: auth
  href: https://artifacts.apis.io/emporix/security/emporix-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/emporix-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/emporix/security/emporix-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/emporix-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.emporix.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.emporix.io/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.emporix.io/user-guides
- group: docs
  title: ''
  type: APIReference
  url: https://developer.emporix.io/api-references
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.emporix.io/user-guides/getting-started/generalconcepts
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.emporix.io/changelog
- group: build
  title: ''
  type: SDKs
  url: https://developer.emporix.io/api-documentation/quickstart/emporix-java-sdk
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/emporix/emporix-commerce-orchestration-platform/overview
- group: agent
  title: ''
  type: LLMsTxt
  url: https://developer.emporix.io/llms.txt
- group: operate
  title: ''
  type: Support
  url: https://support.emporix.com/
- group: operate
  title: ''
  type: Community
  url: https://community.emporix.io/
- group: company
  title: ''
  type: Blog
  url: https://www.emporix.com/blog
- group: company
  title: ''
  type: Newsroom
  url: https://www.emporix.com/company/newsroom
- group: company
  title: ''
  type: AboutUs
  url: https://www.emporix.com/company/about-us
- group: operate
  title: ''
  type: Contact
  url: https://www.emporix.com/get-in-touch
- group: company
  title: ''
  type: Partners
  url: https://www.emporix.com/partners
- group: start
  title: ''
  type: Login
  url: https://app.emporix.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.emporix.io/policies/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.emporix.com/privacy-policy
- group: other
  title: ''
  type: Imprint
  url: https://www.emporix.com/imprint
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/emporix
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/emporix
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@emporixcommerce
created: '2026-10-18'
description: Emporix (Emporix AG) is a German commerce software company offering the Autonomous Commerce Execution (ACE) platform, a composable, API-first digital commerce platform for B2B and B2C that combines core commerce services, commerce orchestration with a no-code value stream modeler, agentic commerce intelligence (AI agents for commerce processes), a headless frontend and an embedded iPaaS. It targets manufacturing, wholesale and distribution, electronics, healthcare and automotive aftermarket businesses, and publishes REST API references, user guides, a changelog, a Java SDK and a Postman collection on its developer portal.
image: https://www.emporix.com/hubfs/EMPORIX%20SQUARE.jpg
json_schemas:
- name: AccessControlQueryDocument
  property_count: 13
  slug: emporix-access-control-query-document
- name: AccessControlUpsertRequest
  property_count: 6
  slug: emporix-access-control-upsert-request
- name: AccessTokenRequest
  property_count: 4
  slug: emporix-access-token-request
- name: AccessToken
  property_count: 7
  slug: emporix-access-token
- name: addedPoints
  property_count: 9
  slug: emporix-added-points
- name: Address_2
  property_count: 19
  slug: emporix-address-2
- name: AddressCommonDto
  property_count: 17
  slug: emporix-address-create-dto
- name: Address
  property_count: 19
  slug: emporix-address
- name: AgentAnalyticsResponse
  property_count: 5
  slug: emporix-agent-analytics-response
- name: AgentResponse
  property_count: 21
  slug: emporix-agent-response
- name: AgentTemplateResponse
  property_count: 12
  slug: emporix-agent-template-response
- name: approvalId
  property_count: 1
  slug: emporix-approval-id
- name: Asset Create Link Payload
  property_count: 7
  slug: emporix-asset-create-link
- name: Asset Update Link Payload
  property_count: 6
  slug: emporix-asset-update-link
- name: authorizeFrontendPaymentRequest
  property_count: 6
  slug: emporix-authorize-frontend-payment-request
- name: authorizePaymentRequest
  property_count: 8
  slug: emporix-authorize-payment-request
- name: AvailabilityBulkDto
  property_count: 8
  slug: emporix-availability-bulk-dto
- name: AvailabilityDto
  property_count: 6
  slug: emporix-availability-dto
- name: AvailabilityWithBundle
  property_count: 11
  slug: emporix-availability-with-bundle
- name: Coupon response/update payload
  property_count: 16
  slug: emporix-base-coupon
- name: BaseUnit
  property_count: 6
  slug: emporix-base-unit
- name: Delivery Time
  property_count: 10
  slug: emporix-basic-delivery-time
- name: Brand Response
  property_count: 9
  slug: emporix-brand-response
- name: Brand
  property_count: 5
  slug: emporix-brand
- name: Collection of Brands
  property_count: 0
  slug: emporix-brands
- name: BulkAssignmentResponse
  property_count: 4
  slug: emporix-bulk-assignment-response
- name: BulkResponse
  property_count: 5
  slug: emporix-bulk-response
- name: bundleProductWithId
  property_count: 22
  slug: emporix-bundle-product-with-id
- name: cartItemRequest
  property_count: 16
  slug: emporix-cart-item-request
- name: cartItemResponse
  property_count: 25
  slug: emporix-cart-item-response
- name: cart
  property_count: 38
  slug: emporix-cart
- name: Catalog
  property_count: 8
  slug: emporix-catalog
- name: CategoryCreateRequest
  property_count: 14
  slug: emporix-category-create-request
- name: CategoryDeprecated
  property_count: 11
  slug: emporix-category-deprecated
- name: CategoryPartialUpdateRequest
  property_count: 11
  slug: emporix-category-partial-update-request
- name: Category
  property_count: 18
  slug: emporix-category
- name: CategoryTreeResponse
  property_count: 0
  slug: emporix-category-tree-response
- name: CategoryTree
  property_count: 12
  slug: emporix-category-tree
- name: CategoryUpdateRequest
  property_count: 11
  slug: emporix-category-update-request
- name: ChangelogHistoryResponse
  property_count: 5
  slug: emporix-changelog-history-response
- name: ClientConfiguration
  property_count: 10
  slug: emporix-client-configuration
- name: Configuration
  property_count: 8
  slug: emporix-configuration
- name: Contact Assignment create payload
  property_count: 7
  slug: emporix-contact-assignment-create
- name: Contact Assignment update payload
  property_count: 6
  slug: emporix-contact-assignment-update
- name: ConversationResponse
  property_count: 7
  slug: emporix-conversation-response
- name: ConversionFactorPayload
  property_count: 2
  slug: emporix-conversion-factor-payload
- name: ConversionFactorResponse
  property_count: 3
  slug: emporix-conversion-factor-response
- name: ConversionPayload
  property_count: 2
  slug: emporix-conversion-payload
- name: ConversionResponse
  property_count: 3
  slug: emporix-conversion-response
- name: Country update
  property_count: 2
  slug: emporix-country-update
- name: Coupon creation payload
  property_count: 17
  slug: emporix-coupon-creation
- name: coupon
  property_count: 20
  slug: emporix-coupon
- name: createCart
  property_count: 13
  slug: emporix-create-cart
- name: CreateCatalogResponse
  property_count: 1
  slug: emporix-create-catalog-response
- name: CreateCatalog
  property_count: 6
  slug: emporix-create-catalog
- name: Price
  property_count: 11
  slug: emporix-create-price
- name: currencyCreation
  property_count: 2
  slug: emporix-currency-creation
- name: currencyRetrieval
  property_count: 3
  slug: emporix-currency-retrieval
- name: currencyUpdate
  property_count: 2
  slug: emporix-currency-update
- name: CustomerAssignmentB2CResponse
  property_count: 4
  slug: emporix-customer-assignment-b2-cresponse
- name: CustomerBulkItemResponse
  property_count: 6
  slug: emporix-customer-bulk-item-response
- name: CustomerForSellerDto
  property_count: 26
  slug: emporix-customer-for-seller-dto
- name: Customer
  property_count: 20
  slug: emporix-customer
- name: CustomerSignup
  property_count: 5
  slug: emporix-customer-signup
- name: discountResponse
  property_count: 16
  slug: emporix-discount-response
- name: Download URL
  property_count: 3
  slug: emporix-download-url
- name: dynamicVariantProductWithId
  property_count: 27
  slug: emporix-dynamic-variant-product-with-id
- name: dynamicVariantRecalculationJobResponse
  property_count: 9
  slug: emporix-dynamic-variant-recalculation-job-response
- name: dynamicVariantRecalculationRequest
  property_count: 1
  slug: emporix-dynamic-variant-recalculation-request
- name: dynamicVariantRecalculationResponse
  property_count: 2
  slug: emporix-dynamic-variant-recalculation-response
- name: employeeShoppingListCreateRequest
  property_count: 5
  slug: emporix-employee-shopping-list-create-request
- name: ExchangeAuthTokenResponse
  property_count: 10
  slug: emporix-exchange-auth-token-response
- name: exchangeRate
  property_count: 3
  slug: emporix-exchange-rate-creation-request
- name: exchangeRateRetrieval
  property_count: 5
  slug: emporix-exchange-rate-retrieval
- name: exchangeRateUpdateRequest
  property_count: 2
  slug: emporix-exchange-rate-update-request
- name: Fee
  property_count: 14
  slug: emporix-fee
- name: getShoppingList
  property_count: 2
  slug: emporix-get-shopping-list
- name: getShoppingLists
  property_count: 0
  slug: emporix-get-shopping-lists
- name: GroupAssignmentResponse
  property_count: 4
  slug: emporix-group-assignment-response
- name: GroupCreateRequest
  property_count: 10
  slug: emporix-group-create-request
- name: GroupUpdateRequest
  property_count: 9
  slug: emporix-group-update-request
- name: GroupsQueryDocument
  property_count: 12
  slug: emporix-groups-query-document
- name: Historical Transitions Response
  property_count: 2
  slug: emporix-historical-transitions-response
- name: Run
  property_count: 31
  slug: emporix-import-run
- name: Stream
  property_count: 20
  slug: emporix-import-stream
- name: IndexConfiguration
  property_count: 8
  slug: emporix-index-configuration
- name: IndexCreationResponse
  property_count: 1
  slug: emporix-index-creation-response
- name: IndexPublicConfiguration
  property_count: 5
  slug: emporix-index-public-configuration
- name: initializePaymentRequest
  property_count: 3
  slug: emporix-initialize-payment-request
- name: ItemAssignmentResponse
  property_count: 5
  slug: emporix-item-assignment-response
- name: ItemFeeCreationResponse
  property_count: 2
  slug: emporix-item-fee-creation-response
- name: ItemFee
  property_count: 4
  slug: emporix-item-fee
- name: ItemYRNs
  property_count: 2
  slug: emporix-item-yrns
- name: JobRequest
  property_count: 2
  slug: emporix-job-request
- name: Job
  property_count: 11
  slug: emporix-job
- name: JobStatusResponse
  property_count: 3
  slug: emporix-job-status-response
- name: labelCreation
  property_count: 4
  slug: emporix-label-creation
- name: label
  property_count: 8
  slug: emporix-label
- name: labelUpdate
  property_count: 3
  slug: emporix-label-update
- name: Legal Entity create payload
  property_count: 12
  slug: emporix-legal-entity-create
- name: Legal Entity update payload
  property_count: 11
  slug: emporix-legal-entity-update
- name: Location create payload
  property_count: 6
  slug: emporix-location-create
- name: Location
  property_count: 5
  slug: emporix-location
- name: LocationSearch
  property_count: 2
  slug: emporix-location-search
- name: Location update payload
  property_count: 5
  slug: emporix-location-update
- name: matchResponse
  property_count: 17
  slug: emporix-match-response
- name: Price matching (by criteria) request body
  property_count: 7
  slug: emporix-match
- name: MetadataFilter
  property_count: 4
  slug: emporix-metadata-filter
- name: Shipping method
  property_count: 7
  slug: emporix-method
- name: Mixin
  property_count: 0
  slug: emporix-mixin
- name: Mixins
  property_count: 0
  slug: emporix-mixins
- name: newCustomerIn
  property_count: 2
  slug: emporix-new-customer-in
- name: Object
  property_count: 0
  slug: emporix-object
- name: orderEntriesDto
  property_count: 1
  slug: emporix-order-entries-dto
- name: Order
  property_count: 35
  slug: emporix-order
- name: Order Update DTO
  property_count: 35
  slug: emporix-order-update-dto
- name: ownShoppingListCreateRequest
  property_count: 4
  slug: emporix-own-shopping-list-create-request
- name: ownShoppingListUpdateRequest
  property_count: 4
  slug: emporix-own-shopping-list-update-request
- name: parentVariantProductWithId
  property_count: 22
  slug: emporix-parent-variant-product-with-id
- name: PasswordMigrationRetentionConfigRequest
  property_count: 3
  slug: emporix-password-migration-retention-config-request
- name: PasswordMigrationRetentionConfigResponse
  property_count: 3
  slug: emporix-password-migration-retention-config-response
- name: PatchOperation
  property_count: 3
  slug: emporix-patch-operation
- name: Patch
  property_count: 0
  slug: emporix-patch
- name: paymentMethodUpdateRequest
  property_count: 2
  slug: emporix-payment-method-update-request
- name: paymentModeRequest
  property_count: 4
  slug: emporix-payment-mode-request
- name: pointsSummaryOut
  property_count: 3
  slug: emporix-points-summary-out
- name: priceModelDefinitionCreation
  property_count: 8
  slug: emporix-price-model-definition-creation
- name: priceModelDefinitionRetrieval
  property_count: 8
  slug: emporix-price-model-definition-retrieval
- name: QuoteCreateFromCartRequest
  property_count: 7
  slug: emporix-quote-create-from-cart-request
- name: QuoteCreateRequest
  property_count: 16
  slug: emporix-quote-create-request
- name: QuoteHistory
  property_count: 0
  slug: emporix-quote-history
- name: Quote request payload
  property_count: 4
  slug: emporix-quote-payload
- name: QuoteReasonResponse
  property_count: 5
  slug: emporix-quote-reason-response
- name: QuoteResponse
  property_count: 25
  slug: emporix-quote-response
- name: Quote slot request schema
  property_count: 6
  slug: emporix-quote-slot
- name: QuoteUpdateRequest
  property_count: 0
  slug: emporix-quote-update-request
- name: RagEmporixNativeToolResponse
  property_count: 6
  slug: emporix-rag-emporix-native-tool-response
- name: CouponCode
  property_count: 1
  slug: emporix-redeem-coupon-out
- name: redeemOption
  property_count: 8
  slug: emporix-redeem-option
- name: redeemedPoints
  property_count: 5
  slug: emporix-redeemed-points
- name: Coupon Redemption Request
  property_count: 5
  slug: emporix-redemption-creation
- name: Coupon Redemption
  property_count: 7
  slug: emporix-redemption
- name: Coupon
  property_count: 17
  slug: emporix-referral-coupon
- name: RefreshCustomerToken
  property_count: 10
  slug: emporix-refresh-customer-token
- name: refundRequest
  property_count: 3
  slug: emporix-refund-request
- name: ReindexJob
  property_count: 7
  slug: emporix-reindex-job
- name: ReindexRequest
  property_count: 2
  slug: emporix-reindex-request
- name: Reindex
  property_count: 1
  slug: emporix-reindex
- name: requestCheckout
  property_count: 6
  slug: emporix-request-checkout
- name: requestFromQuoteCheckout
  property_count: 3
  slug: emporix-request-from-quote-checkout
- name: ResourceLocation
  property_count: 1
  slug: emporix-resource-location
- name: responseCheckout
  property_count: 3
  slug: emporix-response-checkout
- name: returnId
  property_count: 1
  slug: emporix-return-id
- name: Order Creation DTO
  property_count: 33
  slug: emporix-sales-order-creation-dto
- name: salesOrder
  property_count: 40
  slug: emporix-sales-order
- name: SearchItemFee
  property_count: 4
  slug: emporix-search-item-fee
- name: SearchItemsFee
  property_count: 4
  slug: emporix-search-items-fee
- name: searchPrices
  property_count: 9
  slug: emporix-search-prices
- name: Site
  property_count: 19
  slug: emporix-site-dto
- name: Slot
  property_count: 5
  slug: emporix-slot-creation
- name: taxCalculationRequest
  property_count: 2
  slug: emporix-tax-calculation-request
- name: taxCalculationResponse
  property_count: 3
  slug: emporix-tax-calculation-response
- name: taxCreationResponse
  property_count: 1
  slug: emporix-tax-creation-response
- name: taxCreation
  property_count: 2
  slug: emporix-tax-creation
- name: taxRetrieval
  property_count: 4
  slug: emporix-tax-retrieval
- name: taxUpdate
  property_count: 3
  slug: emporix-tax-update
- name: Brand
  property_count: 5
  slug: emporix-update-brand
- name: updateCart
  property_count: 17
  slug: emporix-update-cart
- name: UpdateCatalogProperties
  property_count: 6
  slug: emporix-update-catalog-properties
- name: UpdateCatalog
  property_count: 6
  slug: emporix-update-catalog
- name: UpdateUnit
  property_count: 7
  slug: emporix-update-unit
- name: Upload Session Request
  property_count: 8
  slug: emporix-upload-session-request
- name: Upload Session
  property_count: 5
  slug: emporix-upload-session
- name: UserResponse
  property_count: 14
  slug: emporix-user-response
- name: ValidateTokenResponse
  property_count: 6
  slug: emporix-validate-token-response
- name: Vendor create payload
  property_count: 8
  slug: emporix-vendor-create
- name: Vendor update payload
  property_count: 8
  slug: emporix-vendor-update
jsonld:
- class_count: 120
  name: Emporix Context
  property_count: 176
  slug: emporix-context
layout: provider
mcp_servers:
- description: Emporix offers a fully managed, cloud-hosted MCP Server (Streamable HTTP) with dedicated predefined servers per business domain (product, order, customer, extensibility, frontend, importtool), plus te
  name: Emporix MCP Server
  slug: emporix-mcp-server
modified: '2026-10-18'
name: Emporix
nav: Providers
network: true
overview: 'Emporix publishes 143 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Control Templates API, Access Controls API, Account and profile API, and 140 more. Tagged areas include Company, Commerce, E-Commerce, B2B Commerce, and Headless Commerce.


  The Emporix catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Emporix''s developer surface includes changelog, sandbox, authentication, documentation, API reference, getting-started guide, support, and 48 more developer resources.'
plans:
- name: Emporix Plans Pricing
  plan_count: 0
  slug: emporix-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 1
  name: Emporix Rate Limits
  slug: emporix-rate-limits
rules:
- authorship: generated
  effective_rule_count: 57
  extends:
  - spectral:oas
  name: Emporix API Rules
  rule_count: 16
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 6
  slug: emporix-rules
scopes:
- name: Emporix Scopes
  scope_count: 170
  slug: emporix-scopes
  summary_line: 170 scopes · clientCredentials
score:
  band: strong
  composite: 59.3
  coverage:
    artifact_dirs: 36
    catalog_earned: 73.8
    catalog_earned_first_party: 8.0
    catalog_gap: 41.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -12.7
  facets:
    access_clarity: 28.9
    contract_governance: 35.6
    contract_quality: 75.1
    developer_ergonomics: 53.0
    discoverability: 74.2
    operational_transparency: 55.3
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - germany
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: not_a_repo
  previous_composite: 72.0
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 143
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.8
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: falling
  upsert:
    applies: true
    score: 33.3
screenshot: https://apis.io/screenshots/emporix/emporix-2026-11-03T131505.png
security:
- kind: authentication
  name: Emporix Authentication
  slug: emporix-authentication
  summary_line: 1 scheme
- kind: domain-security
  name: Emporix Domain Security
  slug: emporix-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Emporix Trust Center
  slug: emporix-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, HIPAA, GDPR
skill_count: 11
skills:
- name: emporix-authenticate
  slug: emporix-authenticate
- name: emporix-create-and-manage-order
  slug: emporix-create-and-manage-order
- name: emporix-create-update-customer-profile
  slug: emporix-create-update-customer-profile
- name: emporix-custom-entities
  slug: emporix-custom-entities
- name: emporix-import-run
  slug: emporix-import-run
- name: emporix-manage-customer-address
  slug: emporix-manage-customer-address
- name: emporix-manage-customer-segment-assignments
  slug: emporix-manage-customer-segment-assignments
- name: emporix-product-onboarding
  slug: emporix-product-onboarding
- name: emporix-retrieve-and-update-order-status
  slug: emporix-retrieve-and-update-order-status
- name: emporix-returns
  slug: emporix-returns
- name: emporix-storefront-checkout
  slug: emporix-storefront-checkout
slug: emporix
tags:
- Company
- Commerce
- E-Commerce
- B2B Commerce
- Headless Commerce
- Composable Commerce
- Commerce Orchestration
- Agentic Commerce
- iPaaS
- Software-as-a-Service
website: https://www.emporix.com
---

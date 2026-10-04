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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 63.7
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Bloomreach Agentic Access
  operation_count: 42
  slug: bloomreach-agentic-access
  summary_line: 42 operations · 6 acting
api_count: 8
apis:
- description: REST API for the Bloomreach Engagement marketing automation and CDP platform, enabling customer tracking, segmentation, campaign management, email/SMS sends, recommendations, and analytics.
  name: Bloomreach Engagement API
  slug: bloomreach-engagement-api
- description: REST APIs for managing headless CMS content, including site channels, content types, documents, folders, batch import/export, projects, integrations, webhooks, and delivery API settings.
  name: Bloomreach Content Management API
  slug: bloomreach-content-management-api
- description: REST endpoints for SPAs and front-end applications to retrieve JSON representations of available channels, pages, and documents from the Bloomreach headless CMS.
  name: Bloomreach Content Delivery API
  slug: bloomreach-content-delivery-api
- baseURL: https://suggest.dxpapi.com/api/v2/suggest
  baseurl_source: declared
  description: The Autosuggest API v2 API from Bloomreach — 1 operation(s) for autosuggest api v2.
  name: Bloomreach Autosuggest API v2 API
  phrasing_intents:
  - id: autosuggest-api
    intent: Suggest searches and products as a shopper types
    question: How do I show search suggestions while a shopper is still typing?
  phrasing_ops: 1
  slug: bloomreach-autosuggest-api-v2-api
- baseURL: https://discovery.bloomreach.com/dataconnect/api/v3
  baseurl_source: declared
  description: The Catalog configuration API from Bloomreach — 3 operation(s) for catalog configuration.
  name: Bloomreach Catalog configuration API
  phrasing_intents:
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameConfigsLATEST
    intent: View the current catalog configuration
    question: How can I see the catalog settings that are live in the Bloomreach dashboard right now?
  - id: postAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameConfigsLATEST
    intent: Change the current catalog configuration
    question: How do I update catalog settings programmatically instead of clicking through the dashboard?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameConfigsByConfigId
    intent: View a past catalog configuration
    question: What did my catalog configuration look like when a particular index was built?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameReservedAttributes
    intent: List a catalog's reserved attributes
    question: Which attribute names are reserved in my catalog and can't be used for custom fields?
  phrasing_ops: 4
  slug: bloomreach-catalog-configuration-api
- baseURL: https://pathways.dxpapi.com/api/v2/widgets
  baseurl_source: declared
  description: The Category-based widget API from Bloomreach — 1 operation(s) for category-based widget.
  name: Bloomreach Category-based widget API
  phrasing_intents:
  - id: category-based-widget-api
    intent: Get recommendations for a category page
    question: How do I show recommended products on a category landing page?
  phrasing_ops: 1
  slug: bloomreach-category-based-widget-api
- baseURL: https://pathways-email.dxpapi.com
  baseurl_source: declared
  description: The Category-based Widget Products API from Bloomreach — 2 operation(s) for category-based widget products.
  name: Bloomreach Category-based Widget Products API
  phrasing_intents:
  - id: getApiV2WidgetsImageCategoryByWidgetId
    intent: Get product images for a category widget
    question: How do I get enriched product images for a category recommendation widget?
  - id: getApiV2WidgetsProxyCategoryByWidgetId
    intent: Get product pages for a category widget
    question: How can I fetch the product detail pages behind a category-based widget?
  phrasing_ops: 2
  slug: bloomreach-category-based-widget-products-api
- baseURL: https://discovery.bloomreach.com/dataconnect/api/v3
  baseurl_source: declared
  description: The Feed indexing API from Bloomreach — 1 operation(s) for feed indexing.
  name: Bloomreach Feed indexing API
  phrasing_intents:
  - id: postAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameIndexes
    intent: Run a catalog indexing job
    question: How do I trigger a reindex after updating my product feed?
  phrasing_ops: 1
  slug: bloomreach-feed-indexing-api
- baseURL: https://pathways-email.dxpapi.com
  baseurl_source: declared
  description: The Global Recommendation Widget Products API from Bloomreach — 2 operation(s) for global recommendation widget products.
  name: Bloomreach Global Recommendation Widget Products API
  phrasing_intents:
  - id: getApiV2WidgetsImageGlobalByWidgetId
    intent: Get product images for a global widget
    question: How do I get enriched images for trending products on my homepage?
  - id: getApiV2WidgetsProxyGlobalByWidgetId
    intent: Get product pages for a global widget
    question: How can I fetch product description pages for a trending products widget?
  phrasing_ops: 2
  slug: bloomreach-global-recommendation-widget-products-api
- baseURL: https://pathways.dxpapi.com/api/v2/widgets
  baseurl_source: declared
  description: The Global recommendations widget API from Bloomreach — 1 operation(s) for global recommendations widget.
  name: Bloomreach Global recommendations widget API
  phrasing_intents:
  - id: global-recommendation-widget-api
    intent: Get site-wide product recommendations
    question: How do I show site-wide recommendations, like best sellers, on my homepage?
  phrasing_ops: 1
  slug: bloomreach-global-recommendations-widget-api
- baseURL: https://api.bloomreach.com
  baseurl_source: declared
  description: Operations for working with existing imports.
  name: Bloomreach Imports API
  phrasing_intents:
  - id: startWorkspaceImport
    intent: Start an existing data import
    question: How do I kick off a configured data import in my Bloomreach Engagement workspace from code?
  phrasing_ops: 1
  slug: bloomreach-imports-api
- baseURL: https://pathways.dxpapi.com/api/v2/widgets
  baseurl_source: declared
  description: The Item-based recommendation widget API from Bloomreach — 1 operation(s) for item-based recommendation widget.
  name: Bloomreach Item-based recommendation widget API
  phrasing_intents:
  - id: item-based-recommendation-widget-api
    intent: Recommend products related to a given item
    question: How do I show similar or frequently bought together products on a product detail page?
  phrasing_ops: 1
  slug: bloomreach-item-based-recommendation-widget-api
- baseURL: https://pathways-email.dxpapi.com
  baseurl_source: declared
  description: The Item-based Recommendation Widget Products API from Bloomreach — 2 operation(s) for item-based recommendation widget products.
  name: Bloomreach Item-based Recommendation Widget Products API
  phrasing_intents:
  - id: getApiV2WidgetsImageItemByWidgetId
    intent: Get product images for an item-based widget
    question: How do I get images for frequently-bought-together recommendations on a product page?
  - id: getApiV2WidgetsProxyItemByWidgetId
    intent: Get product pages for an item-based widget
    question: How can I fetch product description pages for bestseller or frequently-viewed recommendations?
  phrasing_ops: 2
  slug: bloomreach-item-based-recommendation-widget-products-api
- baseURL: https://discovery.bloomreach.com/dataconnect/api/v3
  baseurl_source: declared
  description: The Job processing API from Bloomreach — 2 operation(s) for job processing.
  name: Bloomreach Job processing API
  phrasing_intents:
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameJobsByJobId
    intent: Check the status of a catalog job
    question: How do I check whether my feed upload or indexing job has finished?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameJobs
    intent: List a catalog's jobs
    question: Which jobs have run against my catalog recently?
  phrasing_ops: 2
  slug: bloomreach-job-processing-api
- baseURL: https://pathways.dxpapi.com/api/v2/widgets
  baseurl_source: declared
  description: The Keyword-based widget API from Bloomreach — 1 operation(s) for keyword-based widget.
  name: Bloomreach Keyword-based widget API
  phrasing_intents:
  - id: keyword-based-widget-api
    intent: Get recommendations for a search keyword
    question: How do I show recommended products on a search results page for what the shopper typed?
  phrasing_ops: 1
  slug: bloomreach-keyword-based-widget-api
- baseURL: https://pathways-email.dxpapi.com
  baseurl_source: declared
  description: The Keyword-based Widget Products API from Bloomreach — 2 operation(s) for keyword-based widget products.
  name: Bloomreach Keyword-based Widget Products API
  phrasing_intents:
  - id: getApiV2WidgetsImageKeywordByWidgetId
    intent: Get product images for a keyword widget
    question: How do I get enriched product images for keyword search widget results?
  - id: getApiV2WidgetsProxyKeywordByWidgetId
    intent: Get product pages for a keyword widget
    question: How can I fetch product description pages for products in keyword search widget results?
  phrasing_ops: 2
  slug: bloomreach-keyword-based-widget-products-api
- baseURL: https://discovery.bloomreach.com/dataconnect/api/v3
  baseurl_source: declared
  description: The Manage feed records API from Bloomreach — 8 operation(s) for manage feed records.
  name: Bloomreach Manage feed records API
  phrasing_intents:
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecords
    intent: List the current feed records in a catalog
    question: How do I see what product records are currently in my catalog feed?
  - id: putAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecords
    intent: Replace the catalog with a full feed upload
    question: How do I upload my entire product feed at once and replace what's there?
  - id: patchAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecords
    intent: Add or change specific feed records
    question: How can I change a few product records without re-uploading the whole feed?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecordsByRecordId
    intent: View one feed record
    question: How do I look up a single product record in my feed by its ID?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecordsByRecordIdVariants
    intent: List the variants of a feed record
    question: Which variants, like sizes or colors, belong to a product record?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecordsByRecordIdVariantsByVariantId
    intent: View one variant of a feed record
    question: How do I get the details of one specific variant of a product?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecordsByRecordIdViews
    intent: List the views of a feed record
    question: Which views, such as store or region overrides, exist for a product record?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentNameRecordsByRecordIdViewsByViewId
    intent: View one view of a feed record
    question: How do I see how a product record looks in one particular view?
  phrasing_ops: 10
  slug: bloomreach-manage-feed-records-api
- baseURL: https://pathways-email.dxpapi.com
  baseurl_source: declared
  description: The Personalization-based Widget Products API from Bloomreach — 2 operation(s) for personalization-based widget products.
  name: Bloomreach Personalization-based Widget Products API
  phrasing_intents:
  - id: getApiV2WidgetsImagePersonalizedByWidgetId
    intent: Get product images for a personalized widget
    question: How do I get images for a shopper's past-purchase recommendations?
  - id: getApiV2WidgetsProxyPersonalizedByWidgetId
    intent: Get product pages for a personalized widget
    question: How can I fetch product description pages for a user's personalized recommendations?
  phrasing_ops: 2
  slug: bloomreach-personalization-based-widget-products-api
- baseURL: https://pathways.dxpapi.com/api/v2/widgets
  baseurl_source: declared
  description: The Personalization-based widgets API from Bloomreach — 2 operation(s) for personalization-based widgets.
  name: Bloomreach Personalization-based widgets API
  phrasing_intents:
  - id: personalization-based-widget-api
    intent: Get personalized product picks for a shopper
    question: How do I show a shopper product recommendations tailored to their own behavior?
  - id: recently-viewed-widget-api
    intent: Show a visitor's recently viewed products
    question: Can I display the products a visitor looked at recently on my storefront?
  phrasing_ops: 2
  slug: bloomreach-personalization-based-widgets-api
- baseURL: https://discovery.bloomreach.com/dataconnect/api/v3
  baseurl_source: declared
  description: The View Catalogs data API from Bloomreach — 2 operation(s) for view catalogs data.
  name: Bloomreach View Catalogs data API
  phrasing_intents:
  - id: getAccountsByAccountNameCatalogs
    intent: List an account's catalogs
    question: Which catalogs exist under my Bloomreach account?
  - id: getAccountsByAccountNameCatalogsByCatalogNameEnvironmentsByEnvironmentName
    intent: View a catalog with all its records
    question: How can I get the whole catalog, including its product and item records, in one call?
  phrasing_ops: 2
  slug: bloomreach-view-catalogs-data-api
- baseURL: https://pathways.dxpapi.com/api/v2/widgets
  baseurl_source: declared
  description: The Visual search API from Bloomreach — 2 operation(s) for visual search.
  name: Bloomreach Visual search API
  phrasing_intents:
  - id: upload-api
    intent: Upload an image for visual search
    question: How do I upload a shopper's photo so I can find visually similar products?
  - id: visual-search-response-api
    intent: Find products that look like an image
    question: Can I get products that look similar to a picture a shopper already uploaded?
  phrasing_ops: 2
  slug: bloomreach-visual-search-api
artifact_total: 62
asyncapis:
- description: ''
  name: Bloomreach Webhooks
  slug: bloomreach-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Workspace Imports Autosuggest API v2 API
  slug: open-bloomreach-autosuggest-api-v2-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Bestseller API v1 API
  slug: open-bloomreach-bestseller-api-v1-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Catalog configuration API
  slug: open-bloomreach-catalog-configuration-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Category-based widget API
  slug: open-bloomreach-category-based-widget-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Category-based Widget Products API
  slug: open-bloomreach-category-based-widget-products-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Content Search API v1 API
  slug: open-bloomreach-content-search-api-v1-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Feed indexing API
  slug: open-bloomreach-feed-indexing-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Global Recommendation Widget Products API
  slug: open-bloomreach-global-recommendation-widget-products-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Global recommendations widget API
  slug: open-bloomreach-global-recommendations-widget-api
- collection_type: open
  name: Workspace Autosuggest API v2 Imports API
  slug: open-bloomreach-imports-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Item-based recommendation widget API
  slug: open-bloomreach-item-based-recommendation-widget-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Item-based Recommendation Widget Products API
  slug: open-bloomreach-item-based-recommendation-widget-products-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Job processing API
  slug: open-bloomreach-job-processing-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Keyword-based widget API
  slug: open-bloomreach-keyword-based-widget-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Keyword-based Widget Products API
  slug: open-bloomreach-keyword-based-widget-products-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Manage feed records API
  slug: open-bloomreach-manage-feed-records-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Personalization-based Widget Products API
  slug: open-bloomreach-personalization-based-widget-products-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Personalization-based widgets API
  slug: open-bloomreach-personalization-based-widgets-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Product & Category Search API v1 API
  slug: open-bloomreach-product-category-search-api-v1-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 View Catalogs data API
  slug: open-bloomreach-view-catalogs-data-api
- collection_type: open
  name: Workspace Imports Autosuggest API v2 Visual search API
  slug: open-bloomreach-visual-search-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/overlays/bloomreach-bestseller-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bloomreach-bestseller-api-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/overlays/bloomreach-content-search-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bloomreach-content-search-api-v1-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/overlays/bloomreach-product-category-search-api-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/bloomreach-product-category-search-api-v1-overlay.yaml
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/bloomreach/api-specs/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/bloomreach/api-specs/blob/main/LICENSE
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/agentic-access/bloomreach-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/bloomreach-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/security/bloomreach-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/bloomreach-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/authentication/bloomreach-authentication.yml
  title: ''
  type: Authentication
  url: authentication/bloomreach-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://www.bloomreach.com
- group: docs
  title: ''
  type: Documentation
  url: https://documentation.bloomreach.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/bloomreach
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/bloomreach/api-specs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/bloomreach
- group: company
  title: ''
  type: Blog
  url: https://www.bloomreach.com/en/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.bloomreach.com/en/pricing
- group: operate
  title: ''
  type: StatusPage
  url: https://status.bloomreach.com
- group: other
  title: ''
  type: X
  url: https://x.com/bloomreach_tm
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/vocabulary/bloomreach-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/bloomreach-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/json-ld/bloomreach-context.jsonld
  title: ''
  type: JSONLDContext
  url: json-ld/bloomreach-context.jsonld
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/plans/bloomreach-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/bloomreach-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/rate-limits/bloomreach-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/bloomreach-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/finops/bloomreach-finops.yml
  title: ''
  type: FinOps
  url: finops/bloomreach-finops.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/mcp/bloomreach-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/bloomreach-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/mcp/bloomreach-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/bloomreach-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/llms/bloomreach-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/bloomreach-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/well-known/bloomreach-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/bloomreach-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/well-known/bloomreach-api-catalog.json
  title: ''
  type: APICatalog
  url: well-known/bloomreach-api-catalog.json
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/packages/bloomreach-packages.yml
  title: ''
  type: Packages
  url: packages/bloomreach-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/packages/bloomreach-packages.yml
  title: ''
  type: SDKs
  url: packages/bloomreach-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/conventions/bloomreach-conventions.yml
  title: ''
  type: Conventions
  url: conventions/bloomreach-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/errors/bloomreach-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/bloomreach-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/lifecycle/bloomreach-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/bloomreach-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/changelog/bloomreach-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/bloomreach-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/conformance/bloomreach-conformance.yml
  title: ''
  type: Conformance
  url: conformance/bloomreach-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.bloomreach.com/en/legal/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/security/bloomreach-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/bloomreach-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/scopes/bloomreach-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/bloomreach-scopes.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/sandbox/bloomreach-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/bloomreach-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/components/bloomreach-components.yml
  title: ''
  type: Components
  url: components/bloomreach-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/data-model/bloomreach-data-model.yml
  title: ''
  type: DataModel
  url: data-model/bloomreach-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/asyncapi/bloomreach-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/bloomreach-webhooks.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.bloomreach.com/en/roadmap
- group: build
  title: ''
  type: Postman
  url: https://documentation.bloomreach.com/content/reference/postman
- group: start
  title: ''
  type: DeveloperPortal
  url: https://documentation.bloomreach.com/
- group: docs
  title: ''
  type: APIReference
  url: https://documentation.bloomreach.com/discovery/reference/welcome
- group: start
  title: ''
  type: GettingStarted
  url: https://documentation.bloomreach.com/engagement/reference/get-started-101
- group: operate
  title: ''
  type: Support
  url: https://support.bloomreach.com
- group: start
  title: ''
  type: SignUp
  url: https://us.login.bloomreach.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.bloomreach.com/en/legal/terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.bloomreach.com/en/legal/privacy-policy
- group: learn
  title: ''
  type: Academy
  url: https://academy.bloomreach.com
created: '2026-06-13'
description: Bloomreach is a commerce experience cloud combining an e-commerce search and merchandising engine (Discovery), a marketing automation platform and customer data platform (Engagement, formerly Exponea), and a headless content management system (Content, formerly Hippo/brXM). It publishes REST APIs for product and category search, autosuggest, recommendation widgets, catalog management and indexing, customer tracking and segmentation, email and SMS campaigns, and headless content delivery and management. Its Loomi AI layer adds agentic capabilities, and Loomi Connect exposes the estate to AI agents as an OAuth-protected remote MCP server carrying more than 160 tools across marketing, analytics, search and data hub.
examples:
- key_count: 3
  name: Bloomreach Autosuggest Response Example
  slug: bloomreach-autosuggest-response-example
- key_count: 4
  name: Bloomreach Catalog Product Put Example
  slug: bloomreach-catalog-product-put-example
- key_count: 16
  name: Bloomreach Product Search Request Example
  slug: bloomreach-product-search-request-example
- key_count: 4
  name: Bloomreach Product Search Response Example
  slug: bloomreach-product-search-response-example
finops:
- name: Bloomreach Finops
  service_category: ''
  slug: bloomreach-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/bloomreach.png
json_schemas:
- name: BloomreachProduct
  property_count: 4
  slug: bloomreach-product
- name: BloomreachSearchResponse
  property_count: 5
  slug: bloomreach-search-response
- name: BloomreachSuggestResponse
  property_count: 2
  slug: bloomreach-suggest-response
jsonld:
- class_count: 6
  name: Bloomreach Context
  property_count: 59
  slug: bloomreach-context
layout: provider
mcp_servers:
- description: 'Bloomreach ships MCP as a first-class agent surface under the Loomi Connect brand. Three distinct remote MCP servers were found and probed: (1) the regional Loomi Connect production servers, OAuth-gat'
  name: Loomi Connect MCP
  slug: loomi-connect-mcp
modified: 2026-08-13
name: Bloomreach
nav: Providers
network: true
overview: 'Bloomreach publishes 21 APIs on the [APIs.io](https://apis.io/) network, including Autosuggest API v2 API, Catalog configuration API, Category-based widget API, and 18 more. Tagged areas include Digital Commerce, Search, Merchandising, Recommendations, and Customer Data Platform.


  The Bloomreach catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Bloomreach''s developer surface includes authentication, documentation, engineering blog, pricing, changelog, sandbox, API reference, and 45 more developer resources.'
plans:
- name: Bloomreach Plans Pricing
  plan_count: 5
  slug: bloomreach-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 8
  name: Bloomreach Rate Limits
  slug: bloomreach-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Bloomreach API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: bloomreach-jsonschema-spectral-rules
scopes:
- name: Bloomreach Scopes
  scope_count: 3
  slug: bloomreach-scopes
  summary_line: 3 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.8
  coverage:
    artifact_dirs: 32
    catalog_earned: 94.8
    catalog_earned_first_party: 24.0
    catalog_gap: 20.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 86.8
    contract_governance: 41.7
    contract_quality: 69.3
    developer_ergonomics: 58.3
    discoverability: 80.0
    operational_transparency: 81.6
  previous_composite: 72.3
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 94.4
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 39.2
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/bloomreach/refs/heads/main/screenshots/bloomreach-2026-08-17T083224.png
security:
- kind: authentication
  name: Bloomreach Authentication
  slug: bloomreach-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Bloomreach Domain Security
  slug: bloomreach-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Bloomreach Trust Center
  slug: bloomreach-trust-center
  summary_line: SOC 2 Type II, ISO/IEC 27001, ISO/IEC 27017, ISO/IEC 27018, ISO 9001, ISO 22301, GDPR
slug: bloomreach
tags:
- Digital Commerce
- Search
- Merchandising
- Recommendations
- Customer Data Platform
- CDP
- Email Marketing
- SMS Marketing
- Marketing Automation
- Headless CMS
- Personalization
- E-Commerce
website: https://www.bloomreach.com
---

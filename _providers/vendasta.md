---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 34.3
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 203
  human_in_the_loop: 2
  name: Vendasta Agentic Access
  operation_count: 347
  slug: vendasta-agentic-access
  summary_line: 347 operations · 203 acting · 2 human-in-the-loop
api_count: 31
apis:
- description: The Account APIs allow you to perform actions against a single account that your application has been added to.
  name: Vendasta account API
  slug: vendasta-account-api
- description: 'The Activity API lets you inform us of new activity from your Marketplace App. It will be displayed in the user''s activity stream and used for notifications. Note: This endpoint has duplicate detectio'
  name: Vendasta activity API
  slug: vendasta-activity-api
- description: The Change Spend APIs allow interact with change spend requests, like resolving them by approving or rejecting
  name: Vendasta change_spend API
  slug: vendasta-change-spend-api
- description: The Customer APIs allow you to perform actions against customers of the account that your application has been added to.
  name: Vendasta customer API
  slug: vendasta-customer-api
- description: The executive report APIs are used to submit data to the executive report for a single app on an account.
  name: Vendasta executive_report API
  slug: vendasta-executive-report-api
- description: The Marketplace App APIs allow you to perform actions against your applications, as well as certain operations against all marketplace apps.
  name: Vendasta marketplace_app API
  slug: vendasta-marketplace-app-api
- description: The OAuth APIs allow applications to retrieve a bearer token that must be supplied with all API calls. See the Authentication documentation for more details.
  name: Vendasta oauth API
  slug: vendasta-oauth-api
- description: The User APIs allow you to perform operations against Vendasta Users. Each user has a unique identifier in the format UID-{}. This ID is guaranteed to stay the same, while the email associated to a us
  name: Vendasta user API
  slug: vendasta-user-api
- description: The Account Stats API from Vendasta — 2 operation(s) for account stats.
  name: Vendasta Account Stats API
  slug: vendasta-account-stats-api
- description: The AnalyticsService API from Vendasta — 2 operation(s) for analyticsservice.
  name: Vendasta Analytics Service API
  slug: vendasta-analyticsservice-api
- description: The Assistants API from Vendasta — 1 operation(s) for assistants.
  name: Vendasta Assistants API
  slug: vendasta-assistants-api
- description: The Automation Runs API from Vendasta — 1 operation(s) for automation runs.
  name: Vendasta Automation Runs API
  slug: vendasta-automation-runs-api
- description: The Automations API from Vendasta — 2 operation(s) for automations.
  name: Vendasta Automations API
  slug: vendasta-automations-api
- description: The BlogPostsService API from Vendasta — 2 operation(s) for blogpostsservice.
  name: Vendasta Blog Posts Service API
  slug: vendasta-blogpostsservice-api
- description: The Business Categories API from Vendasta — 1 operation(s) for business categories.
  name: Vendasta Business Categories API
  slug: vendasta-business-categories-api
- description: The Business Location Reviews API from Vendasta — 2 operation(s) for business location reviews.
  name: Vendasta Business Location Reviews API
  slug: vendasta-business-location-reviews-api
- description: The Business Locations API from Vendasta — 2 operation(s) for business locations.
  name: Vendasta Business Locations API
  slug: vendasta-business-locations-api
- description: The Cache API from Vendasta — 1 operation(s) for cache.
  name: Vendasta Cache API
  slug: vendasta-cache-api
- description: The Campaign Info API from Vendasta — 2 operation(s) for campaign info.
  name: Vendasta Campaign Info API
  slug: vendasta-campaign-info-api
- description: The Campaign Stats API from Vendasta — 2 operation(s) for campaign stats.
  name: Vendasta Campaign Stats API
  slug: vendasta-campaign-stats-api
- description: The Citations API from Vendasta — 2 operation(s) for citations.
  name: Vendasta Citations API
  slug: vendasta-citations-api
- description: The Composer API from Vendasta — 1 operation(s) for composer.
  name: Vendasta Composer API
  slug: vendasta-composer-api
- description: The Connected Accounts API from Vendasta — 2 operation(s) for connected accounts.
  name: Vendasta Connected Accounts API
  slug: vendasta-connected-accounts-api
- description: The ConversationService API from Vendasta — 2 operation(s) for conversationservice.
  name: Vendasta Conversation Service API
  slug: vendasta-conversationservice-api
- description: The Countries API from Vendasta — 4 operation(s) for countries.
  name: Vendasta Countries API
  slug: vendasta-countries-api
- description: The CRMAssociationService API from Vendasta — 6 operation(s) for crmassociationservice.
  name: Vendasta CRM Association Service API
  slug: vendasta-crmassociationservice-api
- description: The CRMCompanyService API from Vendasta — 6 operation(s) for crmcompanyservice.
  name: Vendasta CRM Company Service API
  slug: vendasta-crmcompanyservice-api
- description: The CRMCustomObjectService API from Vendasta — 9 operation(s) for crmcustomobjectservice.
  name: Vendasta CRM Custom Object Service API
  slug: vendasta-crmcustomobjectservice-api
- description: The CRMCustomObjectTypeService API from Vendasta — 5 operation(s) for crmcustomobjecttypeservice.
  name: Vendasta CRM Custom Object Type Service API
  slug: vendasta-crmcustomobjecttypeservice-api
- description: The CRMFieldSchemaCustomizationService API from Vendasta — 5 operation(s) for crmfieldschemacustomizationservice.
  name: Vendasta CRM Field Schema Customization Service API
  slug: vendasta-crmfieldschemacustomizationservice-api
- description: The CRMFieldSchemaService API from Vendasta — 5 operation(s) for crmfieldschemaservice.
  name: Vendasta CRM Field Schema Service API
  slug: vendasta-crmfieldschemaservice-api
- description: The CRMOpportunityService API from Vendasta — 6 operation(s) for crmopportunityservice.
  name: Vendasta CRM Opportunity Service API
  slug: vendasta-crmopportunityservice-api
- description: The CRMService API from Vendasta — 6 operation(s) for crmservice.
  name: Vendasta CRM Service API
  slug: vendasta-crmservice-api
- description: The Customers API from Vendasta — 2 operation(s) for customers.
  name: Vendasta Customers API
  slug: vendasta-customers-api
- description: The Drafts API from Vendasta — 8 operation(s) for drafts.
  name: Vendasta Drafts API
  slug: vendasta-drafts-api
- description: The Forms API from Vendasta — 9 operation(s) for forms.
  name: Vendasta Forms API
  slug: vendasta-forms-api
- description: The Glossary-Contexts API from Vendasta — 3 operation(s) for glossary-contexts.
  name: Vendasta Glossary Contexts API
  slug: vendasta-glossary-contexts-api
- description: The Glossary-Terms API from Vendasta — 3 operation(s) for glossary-terms.
  name: Vendasta Glossary Terms API
  slug: vendasta-glossary-terms-api
- description: Group resource
  name: Vendasta Group API
  slug: vendasta-group-api
- description: The Knowledge API from Vendasta — 5 operation(s) for knowledge.
  name: Vendasta Knowledge API
  slug: vendasta-knowledge-api
- description: The Listing Profiles API from Vendasta — 1 operation(s) for listing profiles.
  name: Vendasta Listing Profiles API
  slug: vendasta-listing-profiles-api
- description: The Listing Scores API from Vendasta — 1 operation(s) for listing scores.
  name: Vendasta Listing Scores API
  slug: vendasta-listing-scores-api
- description: The Listing Sync Listings API from Vendasta — 1 operation(s) for listing sync listings.
  name: Vendasta Listing Sync Listings API
  slug: vendasta-listing-sync-listings-api
- description: The ListingProductsService API from Vendasta — 1 operation(s) for listingproductsservice.
  name: Vendasta Listing Products Service API
  slug: vendasta-listingproductsservice-api
- description: The ListingProfileService API from Vendasta — 1 operation(s) for listingprofileservice.
  name: Vendasta Listing Profile Service API
  slug: vendasta-listingprofileservice-api
- description: The ListingService API from Vendasta — 3 operation(s) for listingservice.
  name: Vendasta Listing Service API
  slug: vendasta-listingservice-api
- description: The ListingSourceService API from Vendasta — 2 operation(s) for listingsourceservice.
  name: Vendasta Listing Source Service API
  slug: vendasta-listingsourceservice-api
- description: The MeetingExternal API from Vendasta — 9 operation(s) for meetingexternal.
  name: Vendasta Meeting External API
  slug: vendasta-meetingexternal-api
- description: The Messages API from Vendasta — 1 operation(s) for messages.
  name: Vendasta Messages API
  slug: vendasta-messages-api
- description: The Monitor API from Vendasta — 2 operation(s) for monitor.
  name: Vendasta Monitor API
  slug: vendasta-monitor-api
- description: The NetPromoterScoreService API from Vendasta — 4 operation(s) for netpromoterscoreservice.
  name: Vendasta Net Promoter Score Service API
  slug: vendasta-netpromoterscoreservice-api
- description: The Options API from Vendasta — 55 operation(s) for options.
  name: Vendasta Options API
  slug: vendasta-options-api
- description: The Order Custom Fields API from Vendasta — 1 operation(s) for order custom fields.
  name: Vendasta Order Custom Fields API
  slug: vendasta-order-custom-fields-api
- description: The Order Fulfillment Forms API from Vendasta — 3 operation(s) for order fulfillment forms.
  name: Vendasta Order Fulfillment Forms API
  slug: vendasta-order-fulfillment-forms-api
- description: The Orders API from Vendasta — 4 operation(s) for orders.
  name: Vendasta Orders API
  slug: vendasta-orders-api
- description: The PageSpeedService API from Vendasta — 1 operation(s) for pagespeedservice.
  name: Vendasta Page Speed Service API
  slug: vendasta-pagespeedservice-api
- description: The Partner Activatable Products API from Vendasta — 2 operation(s) for partner activatable products.
  name: Vendasta Partner Activatable Products API
  slug: vendasta-partner-activatable-products-api
- description: The Pipelines API from Vendasta — 5 operation(s) for pipelines.
  name: Vendasta Pipelines API
  slug: vendasta-pipelines-api
- description: The Product Custom Fields API from Vendasta — 1 operation(s) for product custom fields.
  name: Vendasta Product Custom Fields API
  slug: vendasta-product-custom-fields-api
- description: The Purchases API from Vendasta — 1 operation(s) for purchases.
  name: Vendasta Purchases API
  slug: vendasta-purchases-api
- description: Endpoints related to Resource Operations
  name: Vendasta Resource Operations API
  slug: vendasta-resource-operations-api
- description: The Review Requests API from Vendasta — 1 operation(s) for review requests.
  name: Vendasta Review Requests API
  slug: vendasta-review-requests-api
- description: The ReviewService API from Vendasta — 10 operation(s) for reviewservice.
  name: Vendasta Review Service API
  slug: vendasta-reviewservice-api
- description: The Sales Account Custom Fields API from Vendasta — 1 operation(s) for sales account custom fields.
  name: Vendasta Sales Account Custom Fields API
  slug: vendasta-sales-account-custom-fields-api
- description: The Sales Accounts API from Vendasta — 4 operation(s) for sales accounts.
  name: Vendasta Sales Accounts API
  slug: vendasta-sales-accounts-api
- description: The SalesOrders API from Vendasta — 3 operation(s) for salesorders.
  name: Vendasta Sales Orders API
  slug: vendasta-salesorders-api
- description: The SalesOrdersAuxiliaryFieldSchema API from Vendasta — 2 operation(s) for salesordersauxiliaryfieldschema.
  name: Vendasta Sales Orders Auxiliary Field Schema API
  slug: vendasta-salesordersauxiliaryfieldschema-api
- description: The SearchService API from Vendasta — 2 operation(s) for searchservice.
  name: Vendasta Search Service API
  slug: vendasta-searchservice-api
- description: The Send Welcome Email API from Vendasta — 1 operation(s) for send welcome email.
  name: Vendasta Send Welcome Email API
  slug: vendasta-send-welcome-email-api
- description: The SEOService API from Vendasta — 2 operation(s) for seoservice.
  name: Vendasta SEO Service API
  slug: vendasta-seoservice-api
- description: Partner-facing endpoints for WordPress site information.
  name: Vendasta SiteDetail Service API
  slug: vendasta-sitedetail-service-api
- description: The SiteInfo API from Vendasta — 1 operation(s) for siteinfo.
  name: Vendasta Site Info API
  slug: vendasta-siteinfo-api
- description: The SiteManager API from Vendasta — 5 operation(s) for sitemanager.
  name: Vendasta Site Manager API
  slug: vendasta-sitemanager-api
- description: The SiteOptionsService API from Vendasta — 1 operation(s) for siteoptionsservice.
  name: Vendasta Site Options Service API
  slug: vendasta-siteoptionsservice-api
- description: The Social Profiles API from Vendasta — 1 operation(s) for social profiles.
  name: Vendasta Social Profiles API
  slug: vendasta-social-profiles-api
- description: The SocialPosts API from Vendasta — 3 operation(s) for socialposts.
  name: Vendasta Social Posts API
  slug: vendasta-socialposts-api
- description: The SocialPostsV2 API from Vendasta — 2 operation(s) for socialpostsv2.
  name: Vendasta Social Posts V2 API
  slug: vendasta-socialpostsv2-api
- description: The Subscription Assignments API from Vendasta — 4 operation(s) for subscription assignments.
  name: Vendasta Subscription Assignments API
  slug: vendasta-subscription-assignments-api
- description: The Subscriptions API from Vendasta — 1 operation(s) for subscriptions.
  name: Vendasta Subscriptions API
  slug: vendasta-subscriptions-api
- description: System Operations
  name: Vendasta System Operations API
  slug: vendasta-system-operations-api
- description: The Templates API from Vendasta — 2 operation(s) for templates.
  name: Vendasta Templates API
  slug: vendasta-templates-api
- description: The Terms API from Vendasta — 2 operation(s) for terms.
  name: Vendasta Terms API
  slug: vendasta-terms-api
- description: The User Custom Fields API from Vendasta — 2 operation(s) for user custom fields.
  name: Vendasta User Custom Fields API
  slug: vendasta-user-custom-fields-api
- description: The Users API from Vendasta — 5 operation(s) for users.
  name: Vendasta Users API
  slug: vendasta-users-api
- description: The VAnalytics API from Vendasta — 5 operation(s) for vanalytics.
  name: Vendasta V Analytics API
  slug: vendasta-vanalytics-api
- description: The WordpressPluginService API from Vendasta — 1 operation(s) for wordpresspluginservice.
  name: Vendasta Wordpress Plugin Service API
  slug: vendasta-wordpresspluginservice-api
- description: The WordpressService API from Vendasta — 3 operation(s) for wordpressservice.
  name: Vendasta Wordpress Service API
  slug: vendasta-wordpressservice-api
artifact_total: 106
asyncapis:
- description: ''
  name: Vendasta Webhooks
  slug: vendasta-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account API
  slug: open-vendasta-account-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account activity API
  slug: open-vendasta-activity-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account change_spend API
  slug: open-vendasta-change-spend-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account customer API
  slug: open-vendasta-customer-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account executive_report API
  slug: open-vendasta-executive-report-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account marketplace_app API
  slug: open-vendasta-marketplace-app-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account oauth API
  slug: open-vendasta-oauth-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account user API
  slug: open-vendasta-user-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/vendasta-capability-edges.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/vendasta-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vendasta-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vendasta-domain-security.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/vendasta-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/vendasta-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/vendasta-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/vendasta-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/vendasta-mcp.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vendasta-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/vendasta-marketplace-overlay.yaml
- group: design
  title: ''
  type: Conformance
  url: conformance/vendasta-conformance.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/vendasta-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/vendasta-lifecycle.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/vendasta-conventions.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/vendasta-data-model.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/vendasta-sandbox.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.vendasta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.vendasta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vendasta.com/vendor
- group: docs
  title: ''
  type: APIReference
  url: https://developers.vendasta.com/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.vendasta.com/vendor
- group: auth
  title: ''
  type: Security
  url: https://www.vendasta.com/developers/vulnerability-disclosure-program/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vendasta.com/
- group: operate
  title: ''
  type: Support
  url: https://support.vendasta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vendasta.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendasta.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.vendasta.com/resources?name=terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.vendasta.com/resources?name=customer-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vendasta.com/
- group: commercial
  title: ''
  type: Plans
  url: plans/vendasta-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/vendasta-rate-limits.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vendasta-changelog.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/vendasta-scopes.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/vendasta-webhooks.yml
- group: build
  title: ''
  type: CLI
  url: cli/vendasta-cli.yml
- group: design
  title: ''
  type: ErrorCodes
  url: errors/vendasta-error-codes.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/vendasta-platform-overlay.yaml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/vendasta/api-gateway-docs/blob/master/docs/Overview/Versioning.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendasta
- group: start
  title: ''
  type: SignUp
  url: https://signup.vendasta.com/
- group: start
  title: ''
  type: Login
  url: https://login-prod.apigateway.co/account-selector/login?serviceProviderId=AA
- group: other
  title: ''
  type: SCIM
  url: openapi/vendasta-scim-openapi.yml
created: '2026-07-17'
description: 'Vendasta is an end-to-end commerce and operating platform that lets agencies, media companies, banks, telcos and other channel partners sell digital products and services to small and medium-sized businesses under their own brand. The platform bundles a white-label Marketplace of resellable products, a Business App client dashboard, CRM and sales pipeline, marketing automation, billing, managed WordPress hosting and a family of AI Employees. Vendasta exposes two distinct API surfaces. The API Gateway at prod.apigateway.co is the current one: 30 first-party OpenAPI documents covering Platform (business locations, users, orders, subscriptions, automations), CRM, SCIM 2.0 user provisioning, Local SEO, Reputation, Social, Customer Voice, Advertising Intelligence, AI Employees, AI Knowledge, Meetings, Forms and Website Pro — JSON:API over application/vnd.api+json, secured by OAuth2 with 73 published scopes, deliberately unversioned with per-operation x-lifecycle maturity. The legacy
  Marketplace API V1 at developers.vendasta.com/api/v1 remains for vendor apps: accounts, users, customers, add-ons, activities, executive reports and file groups, plus eight JWT-signed Marketplace webhooks. Headquartered in Saskatoon, Canada, Vendasta was founded in 2008.'
image: https://www.vendasta.com/wp-content/uploads/2021/03/vendasta-logo.png
layout: provider
mcp_servers:
- description: ''
  name: Vendasta MCP Server
  slug: vendasta-mcp-server
modified: '2026-08-13'
name: Vendasta
nav: Providers
network: true
overview: 'Vendasta publishes 87 APIs on the [APIs.io](https://apis.io/) network, including account API, activity API, change_spend API, and 84 more. Tagged areas include Company, Software-as-a-Service, Marketplace, SMB, and White Label.


  The Vendasta catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Vendasta''s developer surface includes authentication, sandbox, documentation, API reference, getting-started guide, support, engineering blog, and 37 more developer resources.'
plans:
- name: Vendasta Plans Pricing
  plan_count: 4
  slug: vendasta-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 2
  name: Vendasta Rate Limits
  slug: vendasta-rate-limits
scopes:
- name: Vendasta Scopes
  scope_count: 73
  slug: vendasta-scopes
  summary_line: 73 scopes
score:
  band: strong
  composite: 60.9
  coverage:
    artifact_dirs: 26
    catalog_gap: 65.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -1.8
  facets:
    access_clarity: 85.5
    commercial_clarity: 85.5
    contract_governance: 18.2
    contract_quality: 63.0
    developer_ergonomics: 44.6
    discoverability: 63.0
    governance: 18.2
    operational_transparency: 81.6
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
    mcp: derived
    skills: derived
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/vendasta/refs/heads/main/screenshots/vendasta-2026-08-17T080435.png
security:
- kind: authentication
  name: Vendasta Authentication
  slug: vendasta-authentication
  summary_line: oauth2/http/openIdConnect · 6 schemes
- kind: domain-security
  name: Vendasta Domain Security
  slug: vendasta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vendasta Vulnerability Disclosure
  slug: vendasta-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Vendasta Trust Center
  slug: vendasta-trust-center
  summary_line: SOC 2
slug: vendasta
tags:
- Company
- Software-as-a-Service
- Marketplace
- SMB
- White Label
- Reseller
- Marketing
- CRM
- Digital Agency
- Platform
website: https://www.vendasta.com
---

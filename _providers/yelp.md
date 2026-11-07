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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: documented
    mcp_tool_quality: na
    openapi_examples: verified
    operation_distinctiveness: mostly
    pagination_ratio: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 53.4
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1
  human_in_the_loop: 0
  name: Yelp Agentic Access
  operation_count: 11
  slug: yelp-agentic-access
  summary_line: 11 operations · 1 acting
api_count: 25
apis:
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: Conversational Yelp Fusion AI search and chat
  name: Yelp AI API
  slug: yelp-ai-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: Search, match, and retrieve local business data
  name: Yelp Businesses API
  slug: yelp-businesses-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: Yelp business category taxonomy
  name: Yelp Categories API
  slug: yelp-categories-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: Local event search and details
  name: Yelp Events API
  slug: yelp-events-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: Business review excerpts and ratings
  name: Yelp Reviews API
  slug: yelp-reviews-api
- baseURL: https://partner-api.yelp.com
  baseurl_source: declared
  description: 'Advertising operations documented in the Yelp developer reference: Pause Program; Resume Program; Create Program; Modify Program; Terminate Program; Program Status.'
  name: Yelp Advertising API
  slug: yelp-advertising-api
- baseURL: https://api.yelp.com/v3/businesses
  baseurl_source: declared
  description: 'Business Subscriptions operations documented in the Yelp developer reference: Get Business Subscriptions; Subscribe to businesses; Unsubscribe from businesses; Get Quota.'
  name: Yelp Business Subscriptions API
  slug: yelp-business-subscriptions-api
- baseURL: https://partner-api.yelp.com
  baseurl_source: declared
  description: 'Claim Business operations documented in the Yelp developer reference: Claim Business; Claim Status.'
  name: Yelp Claim Business API
  slug: yelp-claim-business-api
- baseURL: https://partner-api.yelp.com/v1
  baseurl_source: declared
  description: 'Data Ingestion operations documented in the Yelp developer reference: Business Update; Job Status.'
  name: Yelp Data Ingestion API
  slug: yelp-data-ingestion-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: 'Home Services operations documented in the Yelp developer reference: Get Jobs; Get Survey; Request a Quote.'
  name: Yelp Home Services API
  slug: yelp-home-services-api
- baseURL: https://api.yelp.com/v3
  baseurl_source: declared
  description: 'Leads operations documented in the Yelp developer reference: Get Lead IDs for a Business; Get Lead; Get Lead Events; Write Event; Mark Lead Event as read; Mark Lead as replied.'
  name: Yelp Leads API
  slug: yelp-leads-api
- baseURL: https://partner-api.yelp.com/listing_management
  baseurl_source: declared
  description: 'Listing Management operations documented in the Yelp developer reference: Add subscriptions; Delete subscriptions; Retrieve subscriptions.'
  name: Yelp Listing Management API
  slug: yelp-listing-management-api
- baseURL: https://api.yelp.com/oauth2
  baseurl_source: declared
  description: 'OAuth Authorization v2 operations documented in the Yelp developer reference: Revoke Access Token; Get Access Token v2; Get Access Token v3.'
  name: Yelp OAuth Authorization v2 API
  slug: yelp-oauth-authorization-v2-api
- baseURL: https://partner-api.yelp.com
  baseurl_source: declared
  description: 'Partner Support operations documented in the Yelp developer reference: Program List All; Business Info; Business Migration Info; Program Info; Program List.'
  name: Yelp Partner Support API
  slug: yelp-partner-support-api
- baseURL: https://partner-api.yelp.com/program
  baseurl_source: declared
  description: 'Program Feature operations documented in the Yelp developer reference: Create a portfolio project draft; Retrieve Program Feature; Add Program Feature; Delete Program Feature; Get Portfolio Photos; Up'
  name: Yelp Program Feature API
  slug: yelp-program-feature-api
- baseURL: https://partner-api.yelp.com
  baseurl_source: declared
  description: 'Respond to Reviews API operations documented in the Yelp developer reference: Respond to Review; Get Access Token; Get Businesses Associated with Access Token; Retrieve Business Owner Information.'
  name: Yelp Respond to Reviews API
  slug: yelp-respond-to-reviews-api
- baseURL: https://api.yelp.com/v3/webhooks
  baseurl_source: declared
  description: 'Webhooks operations documented in the Yelp developer reference: Subscribe to Webhooks; Linkout Attribution; Get Webhook Signing Keys; Add Business IDs to Allow List; Remove Business IDs from Allow Lis'
  name: Yelp Webhooks API
  slug: yelp-webhooks-api
- baseURL: https://partner-api.yelp.com/
  baseurl_source: declared
  description: The Access Token API from Yelp — 1 operation(s) for access token.
  name: Yelp Access Token API
  slug: yelp-access-token-api
- baseURL: https://partner-api.yelp.com/syndication/feed
  baseurl_source: declared
  description: The Add API from Yelp — 1 operation(s) for add.
  name: Yelp Add API
  slug: yelp-add-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: The Bookings API from Yelp — 6 operation(s) for bookings.
  name: Yelp Bookings API
  slug: yelp-bookings-api
- baseURL: https://partner-api.yelp.com/checkout
  baseurl_source: declared
  description: The Checkout API API from Yelp — 8 operation(s) for checkout api.
  name: Yelp Checkout API
  slug: yelp-checkout-api-api
- baseURL: https://partner-api.yelp.com/analytics
  baseurl_source: declared
  description: The Daily Reports API from Yelp — 4 operation(s) for daily reports.
  name: Yelp Daily Reports API
  slug: yelp-daily-reports-api
- baseURL: https://partner_base_url
  baseurl_source: declared
  description: The Fulfillment API API from Yelp — 1 operation(s) for fulfillment api.
  name: Yelp Fulfillment API
  slug: yelp-fulfillment-api-api
- baseURL: https://partner-api.yelp.com/syndication/feed
  baseurl_source: declared
  description: The List API from Yelp — 1 operation(s) for list.
  name: Yelp List API
  slug: yelp-list-api
- baseURL: https://partner-api.yelp.com/analytics
  baseurl_source: declared
  description: The Monthly Reports API from Yelp — 4 operation(s) for monthly reports.
  name: Yelp Monthly Reports API
  slug: yelp-monthly-reports-api
- baseURL: https://api.yelp.com/oauth2
  baseurl_source: declared
  description: The OAuth Authorization v3 API from Yelp — 1 operation(s) for oauth authorization v3.
  name: Yelp OAuth Authorization v3 API
  slug: yelp-oauth-authorization-v3-api
- baseURL: https://partner-api.yelp.com/program
  baseurl_source: declared
  description: The Portfolio Photo API from Yelp — 2 operation(s) for portfolio photo.
  name: Yelp Portfolio Photo API
  slug: yelp-portfolio-photo-api
- baseURL: https://partner-api.yelp.com/program
  baseurl_source: declared
  description: The Portfolio Project API from Yelp — 2 operation(s) for portfolio project.
  name: Yelp Portfolio Project API
  slug: yelp-portfolio-project-api
- baseURL: https://partner-api.yelp.com/syndication/feed
  baseurl_source: declared
  description: The Quota API from Yelp — 2 operation(s) for quota.
  name: Yelp Quota API
  slug: yelp-quota-api
- baseURL: https://partner-api.yelp.com/syndication/feed
  baseurl_source: declared
  description: The Remove API from Yelp — 1 operation(s) for remove.
  name: Yelp Remove API
  slug: yelp-remove-api
- baseURL: https://partner-api.yelp.com/
  baseurl_source: declared
  description: The Token API from Yelp — 1 operation(s) for token.
  name: Yelp Token API
  slug: yelp-token-api
- baseURL: https://api.yelp.com
  baseurl_source: declared
  description: The Waitlist API from Yelp — 7 operation(s) for waitlist.
  name: Yelp Waitlist API
  slug: yelp-waitlist-api
artifact_total: 136
collections:
- collection_type: postman
  name: Yelp Fusion AI API
  slug: postman-yelp-ai-api
- collection_type: postman
  name: Yelp Fusion AI Businesses API
  slug: postman-yelp-businesses-api
- collection_type: postman
  name: Yelp Fusion AI Categories API
  slug: postman-yelp-categories-api
- collection_type: postman
  name: Yelp Fusion AI Events API
  slug: postman-yelp-events-api
- collection_type: postman
  name: Yelp Fusion AI Reviews API
  slug: postman-yelp-reviews-api
- collection_type: open
  name: Yelp Fusion AI API
  slug: open-yelp-ai-api
- collection_type: open
  name: Yelp Fusion AI Businesses API
  slug: open-yelp-businesses-api
- collection_type: open
  name: Yelp Fusion AI Categories API
  slug: open-yelp-categories-api
- collection_type: open
  name: Yelp Fusion AI Events API
  slug: open-yelp-events-api
- collection_type: open
  name: Yelp Fusion API
  slug: open-yelp
common:
- group: design
  href: https://artifacts.apis.io/yelp/rules/yelp-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/yelp-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/yelp/rules/yelp-rules.yml
  title: ''
  type: Spectral
  url: rules/yelp-rules.yml
- group: design
  href: https://artifacts.apis.io/yelp/rules/yelp-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/yelp-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/yelp/json-ld/yelp-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yelp-context.jsonld
- group: design
  href: https://artifacts.apis.io/yelp/vocabulary/yelp-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/yelp-vocabulary.yml
- group: agent
  href: https://artifacts.apis.io/yelp/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/yelp/data-model/yelp-data-model.yml
  title: ''
  type: DataModel
  url: data-model/yelp-data-model.yml
- group: operate
  href: https://artifacts.apis.io/yelp/changelog/yelp-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/yelp-changelog.yml
- group: design
  href: https://artifacts.apis.io/yelp/conventions/yelp-conventions.yml
  title: ''
  type: Conventions
  url: conventions/yelp-conventions.yml
- group: auth
  title: ''
  type: Security
  url: https://hackerone.com/yelp?view_policy=true
- group: operate
  href: https://artifacts.apis.io/yelp/lifecycle/yelp-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/yelp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yelp/lifecycle/yelp-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/yelp-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/yelp/errors/yelp-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/yelp-error-codes.yml
- group: design
  href: https://artifacts.apis.io/yelp/errors/yelp-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/yelp-problem-types.yml
- group: other
  href: https://artifacts.apis.io/yelp/overlays/yelp-advertising-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/yelp-advertising-api-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/yelp/llms/yelp-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/yelp-llms.txt
- group: build
  href: https://artifacts.apis.io/yelp/mcp/yelp-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/yelp-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/yelp/mcp/yelp-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/yelp-mcp.yml
- group: auth
  href: https://artifacts.apis.io/yelp/well-known/yelp-yelp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yelp-yelp-security.txt
- group: auth
  href: https://artifacts.apis.io/yelp/well-known/yelp-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/yelp-security.txt
- group: agent
  href: https://artifacts.apis.io/yelp/well-known/yelp-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/yelp-well-known.yml
- group: other
  href: https://artifacts.apis.io/yelp/hosts/yelp-hosts.yml
  title: ''
  type: Hosts
  url: hosts/yelp-hosts.yml
- group: build
  href: https://artifacts.apis.io/yelp/integrations/yelp-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/yelp-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/yelp/vendors/yelp-vendors.yml
  title: ''
  type: Vendors
  url: vendors/yelp-vendors.yml
- group: build
  href: https://artifacts.apis.io/yelp/packages/yelp-packages.yml
  title: ''
  type: Packages
  url: packages/yelp-packages.yml
- group: auth
  href: https://artifacts.apis.io/yelp/scopes/yelp-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/yelp-scopes.yml
- group: other
  href: https://artifacts.apis.io/yelp/capabilities/yelp-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/yelp-capability-edges.yml
- group: company
  title: ''
  type: Website
  url: https://yelp.com
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/Yelp/yelp-fusion/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/Yelp/yelp-fusion/blob/master/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/yelp/overview
- group: agent
  href: https://artifacts.apis.io/yelp/agentic-access/yelp-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/yelp-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/yelp/security/yelp-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/yelp-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/yelp/security/yelp-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/yelp-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/yelp/authentication/yelp-authentication.yml
  title: ''
  type: Authentication
  url: authentication/yelp-authentication.yml
- group: company
  title: ''
  type: Blog
  url: https://blog.yelp.com/feed/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developer.yelp.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developer.yelp.com/docs/getting-started
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developer.yelp.com/reference/v3_business_search
- group: auth
  title: ''
  type: Authentication
  url: https://docs.developer.yelp.com/docs/oauth-authorization
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.yelp.com/developers
- group: start
  title: ''
  type: Signup
  url: https://www.yelp.com/developers/v3/manage_app
- group: start
  title: ''
  type: Console
  url: https://www.yelp.com/developers/fusion-ai/chat
- group: commercial
  title: ''
  type: Pricing
  url: https://docs.developer.yelp.com/docs/plans
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.developer.yelp.com/docs/places-rate-limiting
- group: design
  title: ''
  type: ErrorCodes
  url: https://docs.developer.yelp.com/docs/api-errors
- group: operate
  title: ''
  type: FAQ
  url: https://docs.developer.yelp.com/docs/places-faq
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.developer.yelp.com/changelog
- group: commercial
  title: ''
  type: TermsOfService
  url: https://docs.developer.yelp.com/docs/policies
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Yelp
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/Yelp/yelp-fusion
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/yelp-com
- group: operate
  title: ''
  type: Support
  url: https://www.yelp-support.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.yelp.com/tos/privacy_policy
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.developer.yelp.com/llms.txt
- group: build
  title: Yelp Fusion Code Samples
  type: SDKs
  url: https://github.com/Yelp/yelp-fusion
- group: build
  title: Python (yelp-python)
  type: SDKs
  url: https://github.com/Yelp/yelp-python
- group: build
  title: Ruby (yelp-ruby)
  type: SDKs
  url: https://github.com/Yelp/yelp-ruby
- group: build
  title: Android (yelp-android)
  type: SDKs
  url: https://github.com/Yelp/yelp-android
- group: build
  title: iOS (yelp-ios)
  type: SDKs
  url: https://github.com/Yelp/yelp-ios
- group: build
  title: MCP Server (Fusion AI)
  type: Tools
  url: https://github.com/Yelp/yelp-mcp
- group: design
  href: https://artifacts.apis.io/yelp/rules/yelp-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/yelp-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/yelp/vocabulary/yelp-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/yelp-vocabulary.yaml
- group: design
  href: https://artifacts.apis.io/yelp/json-ld/yelp-fusion-api-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/yelp-fusion-api-context.jsonld
- group: commercial
  href: https://artifacts.apis.io/yelp/plans/yelp-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/yelp-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/yelp/rate-limits/yelp-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/yelp-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/yelp/finops/yelp-finops.yml
  title: ''
  type: FinOps
  url: finops/yelp-finops.yml
created: '2025-02-08'
description: Yelp connects people with great local businesses. The Yelp Fusion API gives developers programmatic access to Yelp's database of millions of local businesses, ratings, reviews, photos, events, and category taxonomy, plus the Yelp Fusion AI conversational search endpoint. Core public capabilities include business search and discovery, business details, review excerpts, autocomplete, phone and address matching, and local event search. Partner-tier APIs add reviews response, leads, advertising, reservations, waitlist, checkout, and reporting. Authentication uses a Yelp API key passed as a bearer token.
examples:
- key_count: 4
  name: Yelp Ai Chat Request Example
  slug: yelp-ai-chat-request-example
- key_count: 5
  name: Yelp Ai Chat Response Example
  slug: yelp-ai-chat-response-example
- key_count: 3
  name: Yelp Autocomplete Response Example
  slug: yelp-autocomplete-response-example
- key_count: 23
  name: Yelp Business Detail Example
  slug: yelp-business-detail-example
- key_count: 17
  name: Yelp Business Example
  slug: yelp-business-example
- key_count: 3
  name: Yelp Business Hours Example
  slug: yelp-business-hours-example
- key_count: 3
  name: Yelp Business Search Response Example
  slug: yelp-business-search-response-example
- key_count: 5
  name: Yelp Category Example
  slug: yelp-category-example
- key_count: 2
  name: Yelp Coordinates Example
  slug: yelp-coordinates-example
- key_count: 20
  name: Yelp Event Example
  slug: yelp-event-example
- key_count: 2
  name: Yelp Event Search Response Example
  slug: yelp-event-search-response-example
- key_count: 9
  name: Yelp Location Example
  slug: yelp-location-example
- key_count: 6
  name: Yelp Review Example
  slug: yelp-review-example
- key_count: 3
  name: Yelp Reviews Response Example
  slug: yelp-reviews-response-example
features:
- description: Search up to 240 businesses by location, term, category, price, and attributes.
  name: Business Search
- description: Retrieve rich detail for a business by id or alias, including hours, photos, and attributes.
  name: Business Details
- description: Retrieve review excerpts, ratings, and reviewer details for a business.
  name: Reviews
- description: Return search-term, business, and category suggestions as the user types.
  name: Autocomplete
- description: Resolve a phone number or postal address to Yelp businesses.
  name: Phone and Address Match
- description: Search and retrieve local events with timing, location, cost, and ticketing.
  name: Events
- description: Access the full Yelp business category list and per-category details.
  name: Category Taxonomy
- description: Natural language, multi-turn conversational search and business questions.
  name: Fusion AI
finops:
- has_sources: true
  method: derived
  name: Yelp Finops
  primary_unit: ''
  service_category: ''
  slug: yelp-finops
  template: true
graphqls:
- description: Yelp exposes a GraphQL endpoint alongside its REST Fusion API, available at `https://api.yelp.com/v3/graphql`. The same bearer-token authentication used for the REST API applies here. The GraphQL surf
  name: Yelp GraphQL API
  slug: yelp-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/yelp.png
integrations:
- description: Yelp Leads and Conversions APIs offer Zapier integrations for no-code workflows.
  name: Zapier
- description: Official Yelp MCP server exposes Fusion AI as an agent tool over MCP.
  name: Model Context Protocol
- description: Reviews and Leads webhooks push real-time events to partner endpoints.
  name: Webhooks
json_schemas:
- name: AddRemoveBusinessesToAllowListResponse
  property_count: 1
  slug: yelp-add-remove-businesses-to-allow-list-response
- name: AiChatRequest
  property_count: 4
  slug: yelp-ai-chat-request
- name: AiChatResponse
  property_count: 5
  slug: yelp-ai-chat-response
- name: AutocompleteResponse
  property_count: 3
  slug: yelp-autocomplete-response
- name: BusinessDetail
  property_count: 6
  slug: yelp-business-detail
- name: BusinessHours
  property_count: 3
  slug: yelp-business-hours
- name: Business
  property_count: 17
  slug: yelp-business
- name: BusinessSearchResponse
  property_count: 3
  slug: yelp-business-search-response
- name: Category
  property_count: 5
  slug: yelp-category
- name: client_id
  property_count: 0
  slug: yelp-client-id
- name: client_secret
  property_count: 0
  slug: yelp-client-secret
- name: Coordinates
  property_count: 2
  slug: yelp-coordinates
- name: Event
  property_count: 20
  slug: yelp-event
- name: EventSearchResponse
  property_count: 2
  slug: yelp-event-search-response
- name: GenericAttributionWebhookRequest
  property_count: 9
  slug: yelp-generic-attribution-webhook-request
- name: GetEventsResponse
  property_count: 1
  slug: yelp-get-events-response
- name: LeadObject
  property_count: 13
  slug: yelp-lead-object
- name: Location
  property_count: 9
  slug: yelp-location
- name: MarkLeadAsRepliedRequest
  property_count: 1
  slug: yelp-mark-lead-as-replied-request
- name: MarkLeadEventAsReadRequest
  property_count: 2
  slug: yelp-mark-lead-event-as-read-request
- name: MatchingCriteria
  property_count: 12
  slug: yelp-matching-criteria
- name: Review
  property_count: 6
  slug: yelp-review
- name: ReviewsResponse
  property_count: 3
  slug: yelp-reviews-response
- name: Access Token Request
  property_count: 7
  slug: yelp-token-authorization-code-request
- name: Response when calling this endpoint using an authorization code.
  property_count: 8
  slug: yelp-token-authorization-code-response
- name: Refresh Access Token Request
  property_count: 5
  slug: yelp-token-refresh-token-request
- name: Response when calling this endpoint using a refresh token.
  property_count: 4
  slug: yelp-token-refresh-token-response
- name: Update
  property_count: 2
  slug: yelp-update
- name: WebhookKeySet
  property_count: 1
  slug: yelp-webhook-key-set
- name: WriteLeadEventRequest
  property_count: 2
  slug: yelp-write-lead-event-request
json_structures:
- name: Yelp Ai Chat Request Structure
  property_count: 4
  slug: yelp-ai-chat-request-structure
- name: Yelp Ai Chat Response Structure
  property_count: 5
  slug: yelp-ai-chat-response-structure
- name: Yelp Autocomplete Response Structure
  property_count: 3
  slug: yelp-autocomplete-response-structure
- name: Yelp Business Detail Structure
  property_count: 0
  slug: yelp-business-detail-structure
- name: Yelp Business Hours Structure
  property_count: 3
  slug: yelp-business-hours-structure
- name: Yelp Business Search Response Structure
  property_count: 3
  slug: yelp-business-search-response-structure
- name: Yelp Business Structure
  property_count: 17
  slug: yelp-business-structure
- name: Yelp Category Structure
  property_count: 5
  slug: yelp-category-structure
- name: Yelp Coordinates Structure
  property_count: 2
  slug: yelp-coordinates-structure
- name: Yelp Event Search Response Structure
  property_count: 2
  slug: yelp-event-search-response-structure
- name: Yelp Event Structure
  property_count: 20
  slug: yelp-event-structure
- name: Yelp Location Structure
  property_count: 9
  slug: yelp-location-structure
- name: Yelp Review Structure
  property_count: 6
  slug: yelp-review-structure
- name: Yelp Reviews Response Structure
  property_count: 3
  slug: yelp-reviews-response-structure
jsonld:
- class_count: 25
  name: Yelp Context
  property_count: 86
  slug: yelp-context
- class_count: 13
  name: Yelp Fusion Api Context
  property_count: 80
  slug: yelp-fusion-api-context
layout: provider
mcp_servers:
- description: MCP server requiring an API key; 1 tool listed.
  name: Yelp MCP Server
  slug: yelp-agent
modified: '2026-11-05'
name: Yelp
nav: Providers
network: true
overview: 'Yelp publishes 32 API contracts indexed on the [APIs.io](https://apis.io/) network, including AI API, Businesses API, Categories API, and 29 more. Tagged areas include Restaurant, Local Search, Reviews, Business Data, and Location.


  The Yelp catalog on APIs.io includes 2 JSON-LD contexts and 3 Spectral governance rulesets.


  Yelp''s developer surface includes changelog, authentication, engineering blog, documentation, getting-started guide, API reference, signup flow, and 60 more developer resources.'
plans:
- name: Yelp Plans Pricing
  plan_count: 3
  slug: yelp-plans-pricing
random_paper: 10
rate_limits:
- limit_count: 2
  name: Yelp Rate Limits
  slug: yelp-rate-limits
rules:
- authorship: generated
  effective_rule_count: 5
  extends: []
  name: Yelp — jsonschema rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: yelp-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 102
  extends:
  - spectral:oas
  name: Yelp API Rules
  rule_count: 61
  severity_counts:
    error: 40
    hint: 0
    info: 7
    warn: 14
  slug: yelp-rules
- authorship: generated
  effective_rule_count: 80
  extends:
  - spectral:oas
  name: Yelp API Rules
  rule_count: 39
  severity_counts:
    error: 6
    hint: 0
    info: 9
    warn: 24
  slug: yelp-spectral-rules
scopes:
- name: Yelp Scopes
  scope_count: 3
  slug: yelp-scopes
  summary_line: 3 scopes · authorizationCode/clientCredentials
score:
  band: strong
  composite: 64.1
  coverage:
    artifact_dirs: 40
    catalog_earned: 89.0
    catalog_earned_first_party: 20.0
    catalog_gap: 26.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 12.1
  facets:
    access_clarity: 76.3
    contract_governance: 27.3
    contract_quality: 73.0
    developer_ergonomics: 83.9
    discoverability: 76.7
    operational_transparency: 57.9
  open_source:
    applies: true
    score: 0.0
  previous_composite: 52.0
  provenance:
    agentic_access: derived
    contracts:
      callable: 97.0
      derived: 0
      marker_coverage: 72.7
      total: 33
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: residual_tags
    regime: AI & Biometrics
    regime_id: ai_biometrics
    score: 37.3
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 0.0
screenshot: https://apis.io/screenshots/yelp/yelp-2026-06-20T201740.png
security:
- kind: authentication
  name: Yelp Authentication
  slug: yelp-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Yelp Domain Security
  slug: yelp-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Yelp Vulnerability Disclosure
  slug: yelp-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
skill_count: 5
skills:
- name: yelp-ask-yelp-ai
  slug: yelp-ask-yelp-ai
- name: yelp-book-a-reservation
  slug: yelp-book-a-reservation
- name: yelp-find-and-vet-a-business
  slug: yelp-find-and-vet-a-business
- name: yelp-respond-to-a-review
  slug: yelp-respond-to-a-review
- name: yelp-work-a-lead
  slug: yelp-work-a-lead
slug: yelp
tags:
- Restaurant
- Local Search
- Reviews
- Business Data
- Location
- Places
- Generative AI
use_cases:
- description: Power restaurant and food discovery experiences with search, ratings, and photos.
  name: Restaurant Discovery
- description: Surface nearby, open, and highly-rated businesses based on user coordinates.
  name: Location-Aware Recommendations
- description: Track ratings and review excerpts for a portfolio of businesses.
  name: Reputation Monitoring
- description: Build AI agents that answer natural language questions about local businesses.
  name: Conversational Concierge
- description: Embed curated local event listings into apps and sites.
  name: Local Events Listings
website: https://yelp.com
---

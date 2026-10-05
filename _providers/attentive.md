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
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: derived
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 28.6
  scored_at: '2026-10-04'
api_count: 2
apis:
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Public applications must authenticate using the OAuth 2.0 specification to use Attentive’s API resources. Attentive uses OAuth 2.0’s authorization code grant flow to issue access tokens on behalf of u
  name: Attentive Access Token API
  phrasing_intents:
  - id: createTokenViaAuthorizationCode
    intent: Exchange an authorization code for an access token
    question: How do I turn an authorization code into an access token for my Attentive app?
  phrasing_ops: 1
  slug: attentive-access-token-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: The Bulk Segment Operations API from Attentive — 1 operation(s) for bulk segment operations.
  name: Attentive Bulk Segment Operations API
  phrasing_intents:
  - id: postBulkSegmentMembers
    intent: Add members to a segment in bulk
    question: How do I add thousands of subscribers to an Attentive segment in one request?
  - id: deleteBulkSegmentMembers
    intent: Remove members from a segment in bulk
    question: How do I remove a large batch of people from an Attentive segment?
  phrasing_ops: 2
  slug: attentive-bulk-segment-operations-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Endpoints for managing bulk data ingestion jobs. Use these endpoints to monitor the processing status asynchronously.
  name: Attentive Bulk Status API
  phrasing_intents:
  - id: getBulkJobStatus
    intent: Check the status of a bulk ingestion job
    question: How do I check whether my bulk upload job has finished?
  phrasing_ops: 1
  slug: attentive-bulk-status-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: The Bulk User Operations API from Attentive — 1 operation(s) for bulk user operations.
  name: Attentive Bulk User Operations API
  phrasing_intents:
  - id: postBulkUserAttributes
    intent: Update attributes for many users in bulk
    question: How do I update attributes for hundreds of users in one Attentive request?
  phrasing_ops: 1
  slug: attentive-bulk-user-operations-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the Custom Attributes API to apply customizable data or characteristics to each of your subscribers. This API will either create a new custom attribute if it doesn't already exist or update an exi
  name: Attentive Custom Attributes API
  phrasing_intents:
  - id: postCustomAttributes
    intent: Set custom attributes on a user
    question: How do I save custom properties like favorite category on a user in Attentive?
  - id: getCustomAttributes
    intent: Get a user's custom attributes
    question: How do I see all the custom attributes stored for one subscriber?
  phrasing_ops: 2
  slug: attentive-custom-attributes-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the Custom Events API to send user actions to use in the Attentive Segment Builder and Journey Builder for both email and text messages. This data cannot contain any sensitive or special categorie
  name: Attentive Custom Events API
  phrasing_intents:
  - id: postCustomEvents
    intent: Send a custom event for a user action
    question: How do I send a custom event like order shipped to Attentive?
  phrasing_ops: 1
  slug: attentive-custom-events-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the eCommerce API to trigger an event when a user views a product, adds a product to their shopping cart, or makes a purchase.
  name: Attentive eCommerce API
  phrasing_intents:
  - id: postProductViewEvents
    intent: Record a product view event
    question: How do I tell Attentive that a shopper viewed a product?
  - id: postAddToCartEvents
    intent: Record an add-to-cart event
    question: How can I track when a customer adds an item to their cart?
  - id: postPurchaseEvents
    intent: Record a purchase event
    question: How do I send completed orders to Attentive as purchase events?
  phrasing_ops: 3
  slug: attentive-ecommerce-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the Identity API to manage user identifiers. With this API, you can programmatically add a client user identifier or custom identifier(s) to a user. You should only use clientUserId and customIden
  name: Attentive Identity API
  phrasing_intents:
  - id: identify
    intent: Link a client user ID or custom identifiers to a user
    question: How do I connect my own customer ID to a subscriber's phone or email?
  phrasing_ops: 1
  slug: attentive-identity-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: 'You can use the Offers API to add discount codes to an existing offer. <br> <h2> Create an offer </h2> <ol> <li> Navigate to the [Offers](https://ui.attentivemobile.com/offers) page. </li> <li> Click '
  name: Attentive Offers API
  phrasing_intents:
  - id: createCoupons
    intent: Add discount codes to an offer
    question: How do I upload my own discount codes into an Attentive offer?
  phrasing_ops: 1
  slug: attentive-offers-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: You can use the Privacy Request API in order to comply with [California Consumer Privacy Act](https://epic.org/california-consumer-privacy-act-ccpa/) deletion requests through Attentive. For more info
  name: Attentive Privacy Request API
  phrasing_intents:
  - id: addDeleteRequest
    intent: Request deletion of a subscriber's data
    question: How do I submit a privacy request to delete a subscriber from Attentive?
  - id: getDeleteRequest
    intent: Check a CCPA deletion request
    question: How can I confirm a privacy deletion request I submitted has gone through?
  phrasing_ops: 2
  slug: attentive-privacy-request-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Our product catalog API unlocks the ability to send high-performing journeys such as back in stock, low inventory, and price drop. It also lets you segment your customers and branch journeys using pro
  name: Attentive Product Catalog API
  phrasing_intents:
  - id: postUpload
    intent: Start a product catalog upload
    question: How do I send my product catalog to Attentive?
  - id: getUploads
    intent: List recent product catalog uploads
    question: How do I see my recent product catalog uploads and their statuses?
  - id: lookupUpload
    intent: Look up one product catalog ingestion
    question: How do I check the ingestion result of a specific catalog upload?
  phrasing_ops: 3
  slug: attentive-product-catalog-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: 'Endpoints for submitting bulk segment member additions and removals. Use these endpoints to manage segment memberships in bulk and monitor the processing status asynchronously. ## Processing Times The'
  name: Attentive Segments API
  phrasing_intents:
  - id: postBulkSegmentMembers
    intent: Add members to a segment in bulk
    question: How can I load up to 10,000 people into an existing segment at once?
  - id: deleteBulkSegmentMembers
    intent: Remove members from a segment in bulk
    question: How can I pull a list of subscribers out of a segment all at once?
  - id: createSegment
    intent: Create a segment
    question: How do I create a new empty segment for a manual audience upload?
  - id: listSegments
    intent: List segments
    question: How do I list all my Attentive segments?
  - id: getSegmentByExternalId
    intent: Get a segment by external ID
    question: How do I fetch the details of one segment using its external ID?
  - id: patchSegmentByExternalId
    intent: Rename or redescribe a segment
    question: How do I rename an existing segment?
  - id: deleteSegmentByExternalId
    intent: Archive a segment
    question: How do I archive a segment I no longer need?
  phrasing_ops: 7
  slug: attentive-segments-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the Subscribers API to manage subscriptions. With this API, you can programmatically subscribe and unsubscribe users from subscriptions.
  name: Attentive Subscribers API
  phrasing_intents:
  - id: addSubscriptions
    intent: Subscribe a user
    question: How do I opt a user into Attentive text messages through the API?
  - id: getSubscriptions
    intent: Check a user's subscription eligibility
    question: How do I check whether someone is subscribed to SMS or email?
  - id: unsubscribeSubscriptions
    intent: Unsubscribe a user
    question: How do I unsubscribe someone from all messages?
  phrasing_ops: 3
  slug: attentive-subscribers-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the Test Authentication endpoint to test your unique token that you received from Attentive. Make sure to save your token because all API requests are authenticated using bearer tokens. The respon
  name: Attentive Test Authentication API
  phrasing_intents:
  - id: getMe
    intent: Test an API token
    question: How do I check that my Attentive API token works?
  phrasing_ops: 1
  slug: attentive-test-authentication-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Use the V2 Test Authentication endpoint to test your unique token that you received from Attentive. Make sure to save your token because all API requests are authenticated using bearer tokens. The res
  name: Attentive Test Authentication V2 API
  phrasing_intents:
  - id: getMeV2
    intent: Test an API token on v2
    question: How do I check that my token works against the v2 API?
  phrasing_ops: 1
  slug: attentive-test-authentication-v2-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: 'Endpoints for submitting bulk user attribute updates. Use these endpoints to upload large datasets of user data in a single request and monitor the processing status asynchronously. Typical use cases '
  name: Attentive User Attributes API
  phrasing_intents:
  - id: postBulkUserAttributes
    intent: Update attributes for many users in bulk
    question: Can I push attribute changes for up to 256 users at once?
  phrasing_ops: 1
  slug: attentive-user-attributes-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: 'This API will either create a new user if it doesn''t already exist or update an existing one with the attributes provided. You can then use these attributes as macros in messages or build segments to '
  name: Attentive User Properties API
  phrasing_intents:
  - id: postUserAttributes
    intent: Create or update one user's profile
    question: How do I create or update a single user with attributes and subscriptions in one call?
  phrasing_ops: 1
  slug: attentive-user-properties-api
- baseURL: https://api.attentivemobile.com/v1
  baseurl_source: declared
  description: Create and manage webhooks
  name: Attentive Webhooks API
  phrasing_intents:
  - id: getWebhooks
    intent: List webhooks
    question: How do I see which webhooks I have set up?
  - id: createWebhook
    intent: Create a webhook
    question: How do I get notified when someone subscribes via SMS?
  - id: deleteWebhook
    intent: Delete a webhook
    question: How do I permanently remove a webhook?
  - id: updateWebhook
    intent: Update a webhook
    question: How do I change the destination URL of an existing webhook?
  phrasing_ops: 4
  slug: attentive-webhooks-api
- description: 'Attentive''s GraphQL API (beta) at POST https://api.attentivemobile.com/v1/graphql, authenticated with the same application token as the REST API and gated by the same app scopes. The graph covers the '
  name: Attentive GraphQL API
  slug: attentive-graphql-api
artifact_total: 65
asyncapis:
- description: ''
  name: Attentive Webhooks
  slug: attentive-webhooks
collections:
- collection_type: postman
  name: Attentive Access Token API
  slug: postman-attentive-access-token-api
- collection_type: postman
  name: Attentive Access Token Bulk Segment Operations API
  slug: postman-attentive-bulk-segment-operations-api
- collection_type: postman
  name: Attentive Access Token Bulk Status API
  slug: postman-attentive-bulk-status-api
- collection_type: postman
  name: Attentive Access Token Bulk User Operations API
  slug: postman-attentive-bulk-user-operations-api
- collection_type: postman
  name: Attentive Access Token Custom Attributes API
  slug: postman-attentive-custom-attributes-api
- collection_type: postman
  name: Attentive Access Token Custom Events API
  slug: postman-attentive-custom-events-api
- collection_type: postman
  name: Attentive Access Token eCommerce API
  slug: postman-attentive-ecommerce-api
- collection_type: postman
  name: Attentive Access Token Identity API
  slug: postman-attentive-identity-api
- collection_type: postman
  name: Attentive Access Token Offers API
  slug: postman-attentive-offers-api
- collection_type: postman
  name: Attentive Access Token Privacy Request API
  slug: postman-attentive-privacy-request-api
- collection_type: postman
  name: Attentive Access Token Product Catalog API
  slug: postman-attentive-product-catalog-api
- collection_type: postman
  name: Attentive Access Token Segments API
  slug: postman-attentive-segments-api
- collection_type: postman
  name: Attentive Access Token Subscribers API
  slug: postman-attentive-subscribers-api
- collection_type: postman
  name: Attentive Access Token Test Authentication API
  slug: postman-attentive-test-authentication-api
- collection_type: postman
  name: Attentive Access Token Test Authentication V2 API
  slug: postman-attentive-test-authentication-v2-api
- collection_type: postman
  name: Attentive Access Token User Attributes API
  slug: postman-attentive-user-attributes-api
- collection_type: postman
  name: Attentive Access Token User Properties API
  slug: postman-attentive-user-properties-api
- collection_type: postman
  name: Attentive Access Token Webhooks API
  slug: postman-attentive-webhooks-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Attentive Access Token API
  slug: open-attentive-access-token-api
- collection_type: open
  name: Attentive Access Token Bulk Segment Operations API
  slug: open-attentive-bulk-segment-operations-api
- collection_type: open
  name: Attentive Access Token Bulk Status API
  slug: open-attentive-bulk-status-api
- collection_type: open
  name: Attentive Access Token Bulk User Operations API
  slug: open-attentive-bulk-user-operations-api
- collection_type: open
  name: Attentive Access Token Custom Attributes API
  slug: open-attentive-custom-attributes-api
- collection_type: open
  name: Attentive Access Token Custom Events API
  slug: open-attentive-custom-events-api
- collection_type: open
  name: Attentive Access Token eCommerce API
  slug: open-attentive-ecommerce-api
- collection_type: open
  name: Attentive Access Token Identity API
  slug: open-attentive-identity-api
- collection_type: open
  name: Attentive Access Token Offers API
  slug: open-attentive-offers-api
- collection_type: open
  name: Attentive Access Token Privacy Request API
  slug: open-attentive-privacy-request-api
- collection_type: open
  name: Attentive Access Token Product Catalog API
  slug: open-attentive-product-catalog-api
- collection_type: open
  name: Attentive Access Token Segments API
  slug: open-attentive-segments-api
- collection_type: open
  name: Attentive Access Token Subscribers API
  slug: open-attentive-subscribers-api
- collection_type: open
  name: Attentive Access Token Test Authentication API
  slug: open-attentive-test-authentication-api
- collection_type: open
  name: Attentive Access Token Test Authentication V2 API
  slug: open-attentive-test-authentication-v2-api
- collection_type: open
  name: Attentive Access Token User Attributes API
  slug: open-attentive-user-attributes-api
- collection_type: open
  name: Attentive Access Token User Properties API
  slug: open-attentive-user-properties-api
- collection_type: open
  name: Attentive Access Token Webhooks API
  slug: open-attentive-webhooks-api
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/capabilities/attentive-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/attentive-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/overlays/attentive-v1-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/attentive-v1-overlay.yaml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/attentive/overview
- group: company
  title: ''
  type: Website
  url: https://www.attentive.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.attentive.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.attentive.com/docs/introduction
- group: docs
  title: ''
  type: APIReference
  url: https://docs.attentive.com/openapi/reference/overview/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.attentive.com/docs/introduction
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/authentication/attentive-authentication.yml
  title: ''
  type: Authentication
  url: authentication/attentive-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/scopes/attentive-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/attentive-scopes.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/packages/attentive-packages.yml
  title: ''
  type: SDKs
  url: packages/attentive-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/packages/attentive-packages.yml
  title: ''
  type: Packages
  url: packages/attentive-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/mcp/attentive-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/attentive-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/llms/attentive-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/attentive-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/conformance/attentive-conformance.yml
  title: ''
  type: Conformance
  url: conformance/attentive-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://security.attentive.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/errors/attentive-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/attentive-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/lifecycle/attentive-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/attentive-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.attentivemobile.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/conventions/attentive-conventions.yml
  title: ''
  type: Conventions
  url: conventions/attentive-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/changelog/attentive-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/attentive-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/components/attentive-components.yml
  title: ''
  type: Components
  url: components/attentive-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/data-model/attentive-data-model.yml
  title: ''
  type: DataModel
  url: data-model/attentive-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/asyncapi/attentive-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/attentive-webhooks.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/rate-limits/attentive-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/attentive-rate-limits.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/sandbox/attentive-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/attentive-sandbox.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/security/attentive-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/attentive-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/security/attentive-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/attentive-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.attentive.com/legal/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/security/attentive-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/attentive-trust-center.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/attentive-mobile
- group: company
  title: ''
  type: Blog
  url: https://www.attentive.com/blog
- group: operate
  title: ''
  type: Support
  url: https://help.attentivemobile.com
- group: commercial
  title: ''
  type: Pricing
  url: https://www.attentive.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://www.attentive.com/demo
- group: start
  title: ''
  type: Login
  url: https://ui.attentivemobile.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.attentive.com/legal/terms
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.attentive.com/legal/privacy
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/graphql/attentive.graphql
  title: ''
  type: GraphQL
  url: graphql/attentive.graphql
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/mcp/attentive-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/attentive-tool-crosswalk.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/plans/attentive-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/attentive-plans-pricing.yml
created: '2026-07-17'
description: Attentive is a martech SMS and email marketing platform for e-commerce and retail brands. Its developer platform exposes REST APIs (v1 and v2) plus a GraphQL API for managing subscribers and subscriptions, sending SMS/email and ecommerce events (product view, add-to-cart, purchase), setting custom attributes and custom events, uploading product catalogs, distributing offers/coupon codes, resolving identity across phone/email/Shopify/Klaviyo/custom identifiers, handling CCPA privacy deletion requests, and subscribing to webhooks. It also ships iOS, Android, and React Native SDKs and an on-site JavaScript Tag for creative rendering and event collection. Authentication is OAuth 2.0 (authorization code grant) or a bearer API token.
image: https://cdn.prod.website-files.com/684306b795a2c402456e92ba/6a037c0d3dadcc6de287311a_Rebrand-OpenGraphImage_5005x2622.png
layout: provider
mcp_servers:
- description: Remote MCP server at docs.attentive.com over HTTP; 32 tools listed.
  name: Attentive MCP Server
  slug: attentive
modified: '2026-08-13'
name: Attentive
nav: Providers
network: true
overview: 'Attentive publishes 19 APIs on the [APIs.io](https://apis.io/) network, including Access Token API, Bulk Segment Operations API, Bulk Status API, and 16 more. Tagged areas include Company, MarTech, SMS Marketing, Email Marketing, and E-Commerce.


  The Attentive catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Attentive''s developer surface includes documentation, API reference, getting-started guide, authentication, changelog, sandbox, engineering blog, and 35 more developer resources.'
plans:
- name: Attentive Plans Pricing
  plan_count: 3
  slug: attentive-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 7
  name: Attentive Rate Limits
  slug: attentive-rate-limits
scopes:
- name: Attentive Scopes
  scope_count: 14
  slug: attentive-scopes
  summary_line: 14 scopes · authorizationCode
score:
  band: exemplar
  composite: 72.0
  coverage:
    artifact_dirs: 28
    catalog_earned: 61.0
    catalog_earned_first_party: 24.0
    catalog_gap: 57.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.6
  facets:
    access_clarity: 92.1
    contract_governance: 4.5
    contract_quality: 58.6
    developer_ergonomics: 55.4
    discoverability: 73.2
    operational_transparency: 84.2
  previous_composite: 71.4
  provenance:
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 18
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: ccpa
    jurisdictions_satisfied: 2
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 44.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 61.1
screenshot: https://raw.githubusercontent.com/api-evangelist/attentive/refs/heads/main/screenshots/attentive-2026-07-25T201630.png
security:
- kind: authentication
  name: Attentive Authentication
  slug: attentive-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Attentive Domain Security
  slug: attentive-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Attentive Vulnerability Disclosure
  slug: attentive-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Attentive Trust Center
  slug: attentive-trust-center
  summary_line: SOC 2, GDPR
slug: attentive
tags:
- Company
- MarTech
- SMS Marketing
- Email Marketing
- E-Commerce
- Marketing Automation
- Subscribers
- Webhook
- Customer Engagement
- SMS
website: https://www.attentive.com
---

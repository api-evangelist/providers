---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: true
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 9
  human_in_the_loop: 0
  name: Apple Agentic Access
  operation_count: 22
  slug: apple-agentic-access
  summary_line: 22 operations · 9 acting
api_count: 21
apis:
- description: Access Apple Music catalog, user library, and playback controls.
  name: Apple Music API
  slug: apple-music-api
- description: Access weather forecasts, current conditions, and historical weather data.
  name: WeatherKit REST API
  slug: weatherkit-rest-api
- description: Embed interactive Apple Maps on websites.
  name: MapKit JS
  slug: mapkit-js
- description: Integrate Sign in with Apple authentication.
  name: Sign in with Apple REST API
  slug: sign-in-with-apple-rest-api
- description: Send push notifications to iOS, macOS, watchOS, and tvOS devices.
  name: Apple Push Notification Service (APNs)
  slug: apple-push-notification-service-apns
- description: Manage customer App Store transactions from your server, including in-app purchases and subscriptions.
  name: App Store Server API
  slug: app-store-server-api
- description: Receive real-time notifications about in-app purchase events and subscription lifecycle changes.
  name: App Store Server Notifications V2
  slug: app-store-server-notifications-v2
- description: Server-side geocoding, reverse geocoding, search, and estimated time of arrival using Apple Maps.
  name: Apple Maps Server API
  slug: apple-maps-server-api
- description: Publish, manage, update, and delete Apple News Format articles.
  name: Apple News API
  slug: apple-news-api
- description: Reduce fraudulent use of your services by managing device state and asserting app integrity.
  name: DeviceCheck API
  slug: devicecheck-api
- description: Create, manage, and report on Apple Search Ads campaigns programmatically.
  name: Apple Ads Campaign Management API
  slug: apple-ads-campaign-management-api
- description: Create, distribute, and update passes for the Apple Wallet app via a web service.
  name: Wallet Passes Web Service
  slug: wallet-passes-web-service
- description: Automate management of users, roles, provisioning profiles, and bundle identifiers for enterprise apps.
  name: Enterprise Program API
  slug: enterprise-program-api
- description: Automate device management actions and access data about devices enrolled via Automated Device Enrollment.
  name: Apple School and Business Manager API
  slug: apple-school-and-business-manager-api
- description: Accept Apple Pay payments on your website using JavaScript-based APIs.
  name: Apple Pay on the Web
  slug: apple-pay-on-the-web
- description: Create, distribute, and update orders in Apple Wallet for order tracking.
  name: Wallet Orders
  slug: wallet-orders
- description: Declare educational activities supported by your app for use with Apple Schoolwork.
  name: ClassKit Catalog API
  slug: classkit-catalog-api
- description: Access the Apple Music catalog metadata in bulk for albums, songs, and artists.
  name: Apple Music Feed API
  slug: apple-music-feed-api
- description: Manage your apps in App Store Connect, including app metadata, pricing, availability, and app information.
  name: Apple Apps API
  slug: apple-apps-api
- description: Manage TestFlight beta testers, including inviting testers, managing tester groups, and controlling access to beta builds.
  name: Apple Beta Testers API
  slug: apple-beta-testers-api
- description: Manage builds uploaded to App Store Connect, including build metadata, processing state, and build relationships.
  name: Apple Builds API
  slug: apple-builds-api
artifact_total: 162
collections:
- collection_type: postman
  name: Apple App Store Connect Apps API
  slug: postman-apple-apps-api
- collection_type: postman
  name: Apple App Store Connect Apps Beta Testers API
  slug: postman-apple-beta-testers-api
- collection_type: postman
  name: Apple App Store Connect Apps Builds API
  slug: postman-apple-builds-api
- collection_type: open
  name: Apple App Store Connect API
  slug: open-app-store-connect-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/apple/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apple-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apple-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apple-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apple-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apple
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.apple.com
- group: commercial
  title: ''
  type: TermsOfService
  url: https://developer.apple.com/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.apple.com/legal/privacy/
- group: operate
  title: ''
  type: Support
  url: https://developer.apple.com/support/
- group: company
  title: ''
  type: Blog
  url: https://developer.apple.com/news/
- group: operate
  title: ''
  type: StatusPage
  url: https://developer.apple.com/system-status/
- group: start
  title: ''
  type: Signup
  url: https://developer.apple.com/programs/enroll/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.apple.com/support/compare-memberships/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apple
- group: learn
  title: ''
  type: YouTube
  url: https://developer.apple.com/videos/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.apple.com/documentation/updates
- group: auth
  title: ''
  type: Authentication
  url: https://developer.apple.com/documentation/appstoreconnectapi/generating-tokens-for-api-requests
- group: learn
  title: ''
  type: Tutorials
  url: https://developer.apple.com/tutorials/
- group: build
  title: ''
  type: CodeExamples
  url: https://developer.apple.com/sample-code/
- group: build
  title: ''
  type: SDKs
  url: https://developer.apple.com/download/
- group: operate
  title: ''
  type: Contact
  url: https://developer.apple.com/contact/
- group: design
  title: ''
  type: JSONLD
  url: json-ld/apple-context.jsonld
- group: design
  title: ''
  type: SpectralRules
  url: rules/apple-spectral-rules.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/apple/ml-mcp-repo-level-coding
created: '2024-01-15'
description: Collection of Apple's public APIs and developer resources.
examples:
- key_count: 11
  name: App Store Connect App Attributes Example
  slug: app-store-connect-app-attributes-example
- key_count: 2
  name: App Store Connect App Example
  slug: app-store-connect-app-example
- key_count: 6
  name: App Store Connect App Relationships Example
  slug: app-store-connect-app-relationships-example
- key_count: 1
  name: App Store Connect App Response Example
  slug: app-store-connect-app-response-example
- key_count: 1
  name: App Store Connect App Update Request Example
  slug: app-store-connect-app-update-request-example
- key_count: 2
  name: App Store Connect Apps Response Example
  slug: app-store-connect-apps-response-example
- key_count: 11
  name: App Store Connect Beta Group Attributes Example
  slug: app-store-connect-beta-group-attributes-example
- key_count: 1
  name: App Store Connect Beta Group Beta Testers Linkages Request Example
  slug: app-store-connect-beta-group-beta-testers-linkages-request-example
- key_count: 1
  name: App Store Connect Beta Group Create Request Example
  slug: app-store-connect-beta-group-create-request-example
- key_count: 2
  name: App Store Connect Beta Group Example
  slug: app-store-connect-beta-group-example
- key_count: 3
  name: App Store Connect Beta Group Relationships Example
  slug: app-store-connect-beta-group-relationships-example
- key_count: 1
  name: App Store Connect Beta Group Response Example
  slug: app-store-connect-beta-group-response-example
- key_count: 1
  name: App Store Connect Beta Group Update Request Example
  slug: app-store-connect-beta-group-update-request-example
- key_count: 2
  name: App Store Connect Beta Groups Response Example
  slug: app-store-connect-beta-groups-response-example
- key_count: 5
  name: App Store Connect Beta Tester Attributes Example
  slug: app-store-connect-beta-tester-attributes-example
- key_count: 1
  name: App Store Connect Beta Tester Create Request Example
  slug: app-store-connect-beta-tester-create-request-example
- key_count: 2
  name: App Store Connect Beta Tester Example
  slug: app-store-connect-beta-tester-example
- key_count: 3
  name: App Store Connect Beta Tester Relationships Example
  slug: app-store-connect-beta-tester-relationships-example
- key_count: 1
  name: App Store Connect Beta Tester Response Example
  slug: app-store-connect-beta-tester-response-example
- key_count: 2
  name: App Store Connect Beta Testers Response Example
  slug: app-store-connect-beta-testers-response-example
- key_count: 11
  name: App Store Connect Build Attributes Example
  slug: app-store-connect-build-attributes-example
- key_count: 2
  name: App Store Connect Build Example
  slug: app-store-connect-build-example
- key_count: 9
  name: App Store Connect Build Relationships Example
  slug: app-store-connect-build-relationships-example
- key_count: 1
  name: App Store Connect Build Response Example
  slug: app-store-connect-build-response-example
- key_count: 1
  name: App Store Connect Build Update Request Example
  slug: app-store-connect-build-update-request-example
- key_count: 2
  name: App Store Connect Builds Response Example
  slug: app-store-connect-builds-response-example
- key_count: 1
  name: App Store Connect Document Links Example
  slug: app-store-connect-document-links-example
- key_count: 6
  name: App Store Connect Error Detail Example
  slug: app-store-connect-error-detail-example
- key_count: 1
  name: App Store Connect Error Response Example
  slug: app-store-connect-error-response-example
- key_count: 3
  name: App Store Connect Paged Document Links Example
  slug: app-store-connect-paged-document-links-example
- key_count: 1
  name: App Store Connect Paging Information Example
  slug: app-store-connect-paging-information-example
- key_count: 2
  name: App Store Connect Relationship Data Example
  slug: app-store-connect-relationship-data-example
- key_count: 2
  name: App Store Connect Relationship Links Example
  slug: app-store-connect-relationship-links-example
- key_count: 1
  name: App Store Connect Resource Link Example
  slug: app-store-connect-resource-link-example
features:
- 'Apple (App Store + iCloud + Apple Music + Maps): hundreds of services across Consumer Cloud + Developer'
- 'Detailed pricing: see https://developer.apple.com/programs/'
- 'Service: App Store Connect API'
- 'Service: Apple Music API'
- 'Service: MapKit JS / Apple Maps Server API'
- 'Service: Sign in with Apple'
- 'Service: Push Notifications (APNs)'
- 'Service: iCloud Web Services'
- 'Service: WeatherKit REST API'
- 'Service: Apple Pay Web'
- 'Service: Wallet API'
- 'Service: Apple Search Ads API'
finops:
- name: Apple Finops
  service_category: Consumer Cloud + Developer
  slug: apple-finops
graphqls:
- description: 'This conceptual GraphQL schema represents the Apple App Store Connect API and related Apple developer APIs. Apple''s public APIs are REST-based (App Store Connect API, Apple Music API, MapKit, Sign in '
  name: Apple GraphQL Schema
  slug: apple-graphql
image: https://www.apple.com/ac/structured-data/images/knowledge_graph_logo.png
integrations:
- description: Full IDE integration for building, testing, and deploying apps across all Apple platforms.
  name: Xcode
- description: Beta testing platform for distributing pre-release builds to internal and external testers.
  name: TestFlight
- description: View app performance metrics, downloads, and user engagement data.
  name: App Analytics
- description: Store and sync app data across devices using Apple's cloud infrastructure.
  name: CloudKit
json_schemas:
- name: AppAttributes
  property_count: 11
  slug: app-store-connect-app-attributes
- name: AppRelationships
  property_count: 6
  slug: app-store-connect-app-relationships
- name: AppResponse
  property_count: 1
  slug: app-store-connect-app-response
- name: App
  property_count: 2
  slug: app-store-connect-app
- name: AppUpdateRequest
  property_count: 1
  slug: app-store-connect-app-update-request
- name: AppsResponse
  property_count: 2
  slug: app-store-connect-apps-response
- name: BetaGroupAttributes
  property_count: 11
  slug: app-store-connect-beta-group-attributes
- name: BetaGroupBetaTestersLinkagesRequest
  property_count: 1
  slug: app-store-connect-beta-group-beta-testers-linkages-request
- name: BetaGroupCreateRequest
  property_count: 1
  slug: app-store-connect-beta-group-create-request
- name: BetaGroupRelationships
  property_count: 3
  slug: app-store-connect-beta-group-relationships
- name: BetaGroupResponse
  property_count: 1
  slug: app-store-connect-beta-group-response
- name: BetaGroup
  property_count: 2
  slug: app-store-connect-beta-group
- name: BetaGroupUpdateRequest
  property_count: 1
  slug: app-store-connect-beta-group-update-request
- name: BetaGroupsResponse
  property_count: 2
  slug: app-store-connect-beta-groups-response
- name: BetaTesterAttributes
  property_count: 5
  slug: app-store-connect-beta-tester-attributes
- name: BetaTesterCreateRequest
  property_count: 1
  slug: app-store-connect-beta-tester-create-request
- name: BetaTesterRelationships
  property_count: 3
  slug: app-store-connect-beta-tester-relationships
- name: BetaTesterResponse
  property_count: 1
  slug: app-store-connect-beta-tester-response
- name: BetaTester
  property_count: 2
  slug: app-store-connect-beta-tester
- name: BetaTestersResponse
  property_count: 2
  slug: app-store-connect-beta-testers-response
- name: BuildAttributes
  property_count: 11
  slug: app-store-connect-build-attributes
- name: BuildRelationships
  property_count: 9
  slug: app-store-connect-build-relationships
- name: BuildResponse
  property_count: 1
  slug: app-store-connect-build-response
- name: Build
  property_count: 2
  slug: app-store-connect-build
- name: BuildUpdateRequest
  property_count: 1
  slug: app-store-connect-build-update-request
- name: BuildsResponse
  property_count: 2
  slug: app-store-connect-builds-response
- name: DocumentLinks
  property_count: 1
  slug: app-store-connect-document-links
- name: ErrorDetail
  property_count: 6
  slug: app-store-connect-error-detail
- name: ErrorResponse
  property_count: 1
  slug: app-store-connect-error-response
- name: PagedDocumentLinks
  property_count: 3
  slug: app-store-connect-paged-document-links
- name: PagingInformation
  property_count: 1
  slug: app-store-connect-paging-information
- name: RelationshipData
  property_count: 2
  slug: app-store-connect-relationship-data
- name: RelationshipLinks
  property_count: 2
  slug: app-store-connect-relationship-links
- name: ResourceLink
  property_count: 1
  slug: app-store-connect-resource-link
- name: Apple App Store Connect Core Models
  property_count: 0
  slug: apple-app
json_structures:
- name: App Store Connect App Attributes Structure
  property_count: 11
  slug: app-store-connect-app-attributes-structure
- name: App Store Connect App Relationships Structure
  property_count: 6
  slug: app-store-connect-app-relationships-structure
- name: App Store Connect App Response Structure
  property_count: 1
  slug: app-store-connect-app-response-structure
- name: App Store Connect App Structure
  property_count: 2
  slug: app-store-connect-app-structure
- name: App Store Connect App Update Request Structure
  property_count: 1
  slug: app-store-connect-app-update-request-structure
- name: App Store Connect Apps Response Structure
  property_count: 2
  slug: app-store-connect-apps-response-structure
- name: App Store Connect Beta Group Attributes Structure
  property_count: 11
  slug: app-store-connect-beta-group-attributes-structure
- name: App Store Connect Beta Group Beta Testers Linkages Request Structure
  property_count: 1
  slug: app-store-connect-beta-group-beta-testers-linkages-request-structure
- name: App Store Connect Beta Group Create Request Structure
  property_count: 1
  slug: app-store-connect-beta-group-create-request-structure
- name: App Store Connect Beta Group Relationships Structure
  property_count: 3
  slug: app-store-connect-beta-group-relationships-structure
- name: App Store Connect Beta Group Response Structure
  property_count: 1
  slug: app-store-connect-beta-group-response-structure
- name: App Store Connect Beta Group Structure
  property_count: 2
  slug: app-store-connect-beta-group-structure
- name: App Store Connect Beta Group Update Request Structure
  property_count: 1
  slug: app-store-connect-beta-group-update-request-structure
- name: App Store Connect Beta Groups Response Structure
  property_count: 2
  slug: app-store-connect-beta-groups-response-structure
- name: App Store Connect Beta Tester Attributes Structure
  property_count: 5
  slug: app-store-connect-beta-tester-attributes-structure
- name: App Store Connect Beta Tester Create Request Structure
  property_count: 1
  slug: app-store-connect-beta-tester-create-request-structure
- name: App Store Connect Beta Tester Relationships Structure
  property_count: 3
  slug: app-store-connect-beta-tester-relationships-structure
- name: App Store Connect Beta Tester Response Structure
  property_count: 1
  slug: app-store-connect-beta-tester-response-structure
- name: App Store Connect Beta Tester Structure
  property_count: 2
  slug: app-store-connect-beta-tester-structure
- name: App Store Connect Beta Testers Response Structure
  property_count: 2
  slug: app-store-connect-beta-testers-response-structure
- name: App Store Connect Build Attributes Structure
  property_count: 11
  slug: app-store-connect-build-attributes-structure
- name: App Store Connect Build Relationships Structure
  property_count: 9
  slug: app-store-connect-build-relationships-structure
- name: App Store Connect Build Response Structure
  property_count: 1
  slug: app-store-connect-build-response-structure
- name: App Store Connect Build Structure
  property_count: 2
  slug: app-store-connect-build-structure
- name: App Store Connect Build Update Request Structure
  property_count: 1
  slug: app-store-connect-build-update-request-structure
- name: App Store Connect Builds Response Structure
  property_count: 2
  slug: app-store-connect-builds-response-structure
- name: App Store Connect Document Links Structure
  property_count: 1
  slug: app-store-connect-document-links-structure
- name: App Store Connect Error Detail Structure
  property_count: 6
  slug: app-store-connect-error-detail-structure
- name: App Store Connect Error Response Structure
  property_count: 1
  slug: app-store-connect-error-response-structure
- name: App Store Connect Paged Document Links Structure
  property_count: 3
  slug: app-store-connect-paged-document-links-structure
- name: App Store Connect Paging Information Structure
  property_count: 1
  slug: app-store-connect-paging-information-structure
- name: App Store Connect Relationship Data Structure
  property_count: 2
  slug: app-store-connect-relationship-data-structure
- name: App Store Connect Relationship Links Structure
  property_count: 2
  slug: app-store-connect-relationship-links-structure
- name: App Store Connect Resource Link Structure
  property_count: 1
  slug: app-store-connect-resource-link-structure
jsonld:
- class_count: 0
  name: App Store Connect Context
  property_count: 0
  slug: app-store-connect-context
- class_count: 2
  name: Apple Context
  property_count: 9
  slug: apple-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-19'
name: Apple
nav: Providers
network: true
overview: 'Apple publishes 3 APIs on the [APIs.io](https://apis.io/) network: Apps API, Beta Testers API, and Builds API. Tagged areas include Developer, iOS, macOS, Mobile, and Technology.


  The Apple catalog on APIs.io includes 2 JSON-LD contexts and 2 Spectral governance rulesets.


  Apple''s developer surface includes authentication, support, engineering blog, signup flow, pricing, YouTube channel, changelog, and 18 more developer resources.'
plans:
- name: Apple Plans Pricing
  plan_count: 3
  slug: apple-plans-pricing
press:
- date: '2026-05-25'
  title: Apple Intelligence gets even more powerful with new ...
  url: https://www.apple.com/newsroom/2025/06/apple-intelligence-gets-even-more-powerful-with-new-capabilities-across-apple-devices/
- date: '2026-05-25'
  title: Introducing Apple Intelligence for iPhone, iPad, and Mac
  url: https://www.apple.com/newsroom/2024/06/introducing-apple-intelligence-for-iphone-ipad-and-mac/
- date: '2026-05-25'
  title: Apple Intelligence is available today on iPhone, iPad, and ...
  url: https://www.apple.com/newsroom/2024/10/apple-intelligence-is-available-today-on-iphone-ipad-and-mac/
- date: '2026-05-25'
  title: Use Apple Intelligence on your iPhone
  url: https://support.apple.com/guide/iphone/intro-to-apple-intelligence-iphc28624b81/ios
- date: '2026-05-25'
  title: Joint statement from Google and Apple
  url: https://blog.google/company-news/inside-google/company-announcements/joint-statement-google-apple/
random_paper: 38
rate_limits:
- limit_count: 2
  name: Apple Rate Limits
  slug: apple-rate-limits
rules:
- name: Apple API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: apple-jsonschema-spectral-rules
- name: Apple API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: apple-spectral-rules
score:
  band: strong
  composite: 63.7
  delta: -1.9
  facets:
    commercial_clarity: 71.1
    contract_quality: 78.1
    developer_ergonomics: 45.7
    discoverability: 63.0
    governance: 58.3
    operational_transparency: 57.9
  previous_composite: 65.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apple/refs/heads/main/screenshots/apple-2026-06-20T172317.png
security:
- kind: authentication
  name: Apple Authentication
  slug: apple-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Apple Domain Security
  slug: apple-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apple Vulnerability Disclosure
  slug: apple-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apple
tags:
- Developer
- iOS
- macOS
- Mobile
- Technology
- Fortune 100
use_cases:
- description: Automate app submissions, manage TestFlight beta testing, and handle app metadata at scale.
  name: App Distribution
- description: Manage subscriptions, consumables, and transaction history with server-side verification.
  name: In-App Purchases
- description: Automate device enrollment and management for schools and businesses at scale.
  name: Enterprise Device Management
- description: Publish and manage articles in Apple News with rich media and analytics.
  name: Content Publishing
- description: Build location-aware applications with geocoding, routing, and interactive maps.
  name: Location Services
website: https://developer.apple.com
---

---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: derived
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 33.7
  scored_at: '2026-09-02'
agentic_access:
- acting_count: 25
  human_in_the_loop: 0
  name: Iterable Agentic Access
  operation_count: 48
  slug: iterable-agentic-access
  summary_line: 48 operations · 25 acting
api_count: 2
apis:
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Iterable Export API enables developers to extract data from Iterable projects for analytics, reporting, and data warehousing purposes. It provides asynchronous export endpoints that allow bulk ret
  name: Iterable Export API
  slug: export-api
- description: The Iterable Web SDK enables developers to integrate Iterable's marketing automation capabilities directly into JavaScript and Node.js applications. It provides functions for tracking user events, man
  name: Iterable Web SDK
  slug: web-sdk
- description: The Iterable iOS SDK allows developers to integrate Iterable's marketing automation features into native iOS applications built with Swift or Objective-C. It supports push notifications, in-app messag
  name: Iterable iOS SDK
  slug: ios-sdk
- description: The Iterable Android SDK provides native integration between Android applications and the Iterable marketing automation platform. It supports push notifications, in-app messages, deep links, and Mobil
  name: Iterable Android SDK
  slug: android-sdk
- description: The Iterable React Native SDK enables developers to integrate Iterable's marketing automation capabilities into cross-platform mobile applications built with React Native. It wraps Iterable's native i
  name: Iterable React Native SDK
  slug: react-native-sdk
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Create, retrieve, and manage marketing campaigns. Access campaign metrics and trigger campaign sends.
  name: Iterable Campaigns API
  slug: iterable-campaigns-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage product catalogs and catalog items used for personalization and recommendation in campaigns.
  name: Iterable Catalogs API
  slug: iterable-catalogs-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Retrieve and manage messaging channels and message types used for organizing campaigns and templates.
  name: Iterable Channels API
  slug: iterable-channels-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Track purchase events, update cart data, and manage commerce-related user activity for revenue attribution.
  name: Iterable Commerce API
  slug: iterable-commerce-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send transactional emails and manage email-specific delivery settings.
  name: Iterable Email API
  slug: iterable-email-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Track custom events, retrieve event data for users, and manage event metadata used for segmentation and campaign triggering.
  name: Iterable Events API
  slug: iterable-events-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Retrieve experiment configurations and metrics for A/B tests running across campaigns.
  name: Iterable Experiments API
  slug: iterable-experiments-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage in-app messages and retrieve in-app message content for mobile and web clients.
  name: Iterable InApp API
  slug: iterable-inapp-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Create and manage subscriber lists. Subscribe and unsubscribe users from lists. Retrieve list metadata and membership.
  name: Iterable Lists API
  slug: iterable-lists-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage message types that categorize the kinds of messages sent through channels.
  name: Iterable MessageTypes API
  slug: iterable-messagetypes-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Store and retrieve key-value metadata tables for use in personalization and campaign logic.
  name: Iterable Metadata API
  slug: iterable-metadata-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send push notifications and manage push notification delivery settings and tokens.
  name: Iterable Push API
  slug: iterable-push-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send SMS messages and manage SMS-specific delivery settings.
  name: Iterable SMS API
  slug: iterable-sms-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage email, push, SMS, and in-app message templates. Retrieve template content and metadata.
  name: Iterable Templates API
  slug: iterable-templates-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Manage user profiles, update user fields, bulk update users, get user data by email or userId, and delete users.
  name: Iterable Users API
  slug: iterable-users-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Send web push notifications and manage web push subscription tokens.
  name: Iterable WebPush API
  slug: iterable-webpush-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: Trigger workflow enrollments and manage journey-based automation workflows.
  name: Iterable Workflows API
  slug: iterable-workflows-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Embedded Messaging API from Iterable — 1 operation(s) for embedded messaging.
  name: Iterable Embedded Messaging API
  slug: iterable-embedded-messaging-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The In-app API from Iterable — 4 operation(s) for in-app.
  name: Iterable In App API
  slug: iterable-in-app-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The In-app-web API from Iterable — 1 operation(s) for in-app-web.
  name: Iterable In App Web API
  slug: iterable-in-app-web-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The snippets API from Iterable — 2 operation(s) for snippets.
  name: Iterable Snippets API
  slug: iterable-snippets-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The subscriptions API from Iterable — 4 operation(s) for subscriptions.
  name: Iterable Subscriptions API
  slug: iterable-subscriptions-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The Verify API from Iterable — 2 operation(s) for verify.
  name: Iterable Verify API
  slug: iterable-verify-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The webhooks API from Iterable — 1 operation(s) for webhooks.
  name: Iterable Webhooks API
  slug: iterable-webhooks-api
- baseURL: https://api.iterable.com
  baseurl_source: declared
  description: The WhatsApp API from Iterable — 2 operation(s) for whatsapp.
  name: Iterable Whats App API
  slug: iterable-whatsapp-api
artifact_total: 117
asyncapis:
- description: Iterable system webhooks send real-time event data from an Iterable project to external systems via HTTP POST requests whenever specified events occur. System webhooks can be configured to fire on ema
  name: Iterable System Webhooks
  slug: iterable-system-webhooks-asyncapi
collections:
- collection_type: postman
  name: Iterable Export Campaigns API
  slug: postman-iterable-campaigns-api
- collection_type: postman
  name: Iterable Export Campaigns Catalogs API
  slug: postman-iterable-catalogs-api
- collection_type: postman
  name: Iterable Export Campaigns Channels API
  slug: postman-iterable-channels-api
- collection_type: postman
  name: Iterable Export Campaigns Commerce API
  slug: postman-iterable-commerce-api
- collection_type: postman
  name: Iterable Export Campaigns Email API
  slug: postman-iterable-email-api
- collection_type: postman
  name: Iterable Export Campaigns Events API
  slug: postman-iterable-events-api
- collection_type: postman
  name: Iterable Export Campaigns ExperimentMetrics API
  slug: postman-iterable-experimentmetrics-api
- collection_type: postman
  name: Iterable Export Campaigns Experiments API
  slug: postman-iterable-experiments-api
- collection_type: postman
  name: Iterable Campaigns Export API
  slug: postman-iterable-export-api
- collection_type: postman
  name: Iterable Export Campaigns InApp API
  slug: postman-iterable-inapp-api
- collection_type: postman
  name: Iterable Export Campaigns Lists API
  slug: postman-iterable-lists-api
- collection_type: postman
  name: Iterable Export Campaigns MessageTypes API
  slug: postman-iterable-messagetypes-api
- collection_type: postman
  name: Iterable Export Campaigns Metadata API
  slug: postman-iterable-metadata-api
- collection_type: postman
  name: Iterable Export Campaigns Push API
  slug: postman-iterable-push-api
- collection_type: postman
  name: Iterable Export Campaigns SMS API
  slug: postman-iterable-sms-api
- collection_type: postman
  name: Iterable Export Campaigns Templates API
  slug: postman-iterable-templates-api
- collection_type: postman
  name: Iterable Export Campaigns Users API
  slug: postman-iterable-users-api
- collection_type: postman
  name: Iterable Export Campaigns WebPush API
  slug: postman-iterable-webpush-api
- collection_type: postman
  name: Iterable Export Campaigns Workflows API
  slug: postman-iterable-workflows-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Iterable Export Campaigns API
  slug: open-iterable-campaigns-api
- collection_type: open
  name: Iterable Export Campaigns Catalogs API
  slug: open-iterable-catalogs-api
- collection_type: open
  name: Iterable Export Campaigns Channels API
  slug: open-iterable-channels-api
- collection_type: open
  name: Iterable Export Campaigns Commerce API
  slug: open-iterable-commerce-api
- collection_type: open
  name: Iterable Export Campaigns Email API
  slug: open-iterable-email-api
- collection_type: open
  name: Iterable Export Campaigns Events API
  slug: open-iterable-events-api
- collection_type: open
  name: Iterable Export Campaigns ExperimentMetrics API
  slug: open-iterable-experimentmetrics-api
- collection_type: open
  name: Iterable Export Campaigns Experiments API
  slug: open-iterable-experiments-api
- collection_type: open
  name: Iterable Campaigns Export API
  slug: open-iterable-export-api
- collection_type: open
  name: Iterable Export Campaigns InApp API
  slug: open-iterable-inapp-api
- collection_type: open
  name: Iterable Export Campaigns Lists API
  slug: open-iterable-lists-api
- collection_type: open
  name: Iterable Export Campaigns MessageTypes API
  slug: open-iterable-messagetypes-api
- collection_type: open
  name: Iterable Export Campaigns Metadata API
  slug: open-iterable-metadata-api
- collection_type: open
  name: Iterable Export Campaigns Push API
  slug: open-iterable-push-api
- collection_type: open
  name: Iterable REST API
  slug: open-iterable-rest-api
- collection_type: open
  name: Iterable Export Campaigns SMS API
  slug: open-iterable-sms-api
- collection_type: open
  name: Iterable Export Campaigns Templates API
  slug: open-iterable-templates-api
- collection_type: open
  name: Iterable Export Campaigns Users API
  slug: open-iterable-users-api
- collection_type: open
  name: Iterable Export Campaigns WebPush API
  slug: open-iterable-webpush-api
- collection_type: open
  name: Iterable Export Campaigns Workflows API
  slug: open-iterable-workflows-api
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/iterable-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/iterable-experimentmetrics-api-overlay.yaml
- group: docs
  title: ''
  type: OpenAPI
  url: openapi/_original/iterable-api-openapi.json
- group: build
  title: ''
  type: Packages
  url: packages/iterable-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/iterable-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/iterable-cli.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/iterable-mcp.yml
- group: build
  title: ''
  type: ToolCrosswalk
  url: mcp/iterable-tool-crosswalk.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/iterable-llms.txt
- group: design
  title: ''
  type: Conventions
  url: conventions/iterable-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iterable-error-codes.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/iterable-problem-types.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/iterable-rate-limits.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/iterable-data-model.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/iterable-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.iterable.com/
- group: operate
  title: ''
  type: Deprecation
  url: https://support.iterable.com/hc/en-us/articles/360046136171-SDK-Support-Policy
- group: design
  title: ''
  type: Conformance
  url: conformance/iterable-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://trust.iterable.com/
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/iterable-changelog.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://support.iterable.com/hc/en-us/articles/44900665796628-2026-Release-Notes
- group: design
  title: ''
  type: Webhooks
  url: https://support.iterable.com/hc/en-us/articles/208013936-System-Webhooks
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/iterable-vocabulary.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.iterable.com/hc/en-us/categories/360002288712
- group: docs
  title: ''
  type: APIReference
  url: https://api.iterable.com/api/docs
- group: start
  title: ''
  type: GettingStarted
  url: https://support.iterable.com/hc/en-us/articles/41044692130196-Getting-Started-with-Iterable-s-API
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Iterable
- group: operate
  title: ''
  type: Community
  url: https://community.iterable.com/
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/iterable/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/iterable-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/iterable-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/iterable-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/iterable-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/iterable
- group: docs
  title: ''
  type: AsyncAPI
  url: asyncapi/iterable-system-webhooks-asyncapi.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/iterable-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-user-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-campaign-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-event-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/iterable-commerce-item-schema.json
- group: company
  title: ''
  type: Website
  url: https://iterable.com/
- group: docs
  title: ''
  type: Documentation
  url: https://api.iterable.com/api/docs
- group: operate
  title: ''
  type: Support
  url: https://support.iterable.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://iterable.com/blog/
- group: start
  title: ''
  type: Login
  url: https://app.iterable.com/login
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://iterable.com/trust/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://iterable.com/legal/terms/
created: '2026-03-20'
description: Iterable is an AI customer engagement platform that powers unified cross-channel marketing experiences and empowers marketers to create, optimize, and measure relevant interactions across email, push, SMS, in-app, and web channels. Their developer platform provides REST APIs, export APIs, AsyncAPI webhooks, and native SDKs for web, iOS, Android, and React Native.
features:
- 'Growth: $3K-$5K/mo for 10K-50K MAUs'
- 'Premier: $6K-$15K/mo for 50K-200K MAUs'
- 'Enterprise: $20K+/mo for 200K+ MAUs'
- Multi-year + volume discounts
- Email + Push + SMS + In-App + Web Push + Direct Mail channels
- Workflow Studio for journey orchestration
- AI Optimization for send-time and channel selection (Premier+)
- REST API at api.iterable.com
- Default 30 req/sec; bulk endpoints up to 1K events/req
- OAuth + API keys (project-scoped)
- Webhooks for events and campaign data
- User profile and event tracking
- Cross-channel campaigns
- Smart Ingest for data lake/warehouse loading
- Real-time event triggers
- Iterable AI for content suggestions
finops:
- name: Iterable Finops
  service_category: Marketing Automation
  slug: iterable-finops
graphqls:
- description: Iterable is a cross-channel marketing automation platform. The API covers user management, event tracking, email/SMS/push campaigns, workflows, A/B testing, audience segmentation, catalog items, and e
  name: Iterable GraphQL API
  slug: iterable-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/iterable.png
json_schemas:
- name: Iterable Campaign
  property_count: 15
  slug: iterable-campaign
- name: CampaignCreateRequest
  property_count: 6
  slug: iterable-campaigncreaterequest
- name: Channel
  property_count: 4
  slug: iterable-channel
- name: Iterable Commerce Item
  property_count: 10
  slug: iterable-commerce-item
- name: CommerceItem
  property_count: 10
  slug: iterable-commerceitem
- name: EmailTemplate
  property_count: 11
  slug: iterable-emailtemplate
- name: EmailTemplateUpdate
  property_count: 8
  slug: iterable-emailtemplateupdate
- name: ErrorResponse
  property_count: 2
  slug: iterable-errorresponse
- name: Iterable Event
  property_count: 7
  slug: iterable-event
- name: ExportedEvent
  property_count: 15
  slug: iterable-exportedevent
- name: IterableResponse
  property_count: 3
  slug: iterable-iterableresponse
- name: List
  property_count: 5
  slug: iterable-list
- name: PurchaseRequest
  property_count: 7
  slug: iterable-purchaserequest
- name: TrackEventRequest
  property_count: 7
  slug: iterable-trackeventrequest
- name: Iterable User
  property_count: 10
  slug: iterable-user
- name: UserResponse
  property_count: 1
  slug: iterable-userresponse
- name: UserUpdateRequest
  property_count: 5
  slug: iterable-userupdaterequest
json_structures:
- name: Iterable Structure
  property_count: 0
  slug: iterable-structure
jsonld:
- class_count: 0
  name: Iterable Context
  property_count: 8
  slug: iterable-context
layout: provider
mcp_servers:
- description: 'Iterable publishes a first-party MCP server as the npm package @iterable/mcp (repo github.com/Iterable/mcp-server). It is a LOCAL STDIO server: a developer installs and runs it with npx, and it calls '
  name: Iterable MCP Server (@iterable/mcp, local stdio)
  slug: iterable-mcp-server-iterablemcp-local-stdio
modified: '2026-08-13'
name: Iterable
nav: Providers
network: true
overview: 'Iterable publishes 26 APIs on the [APIs.io](https://apis.io/) network, including Export API, Campaigns API, Catalogs API, and 23 more. Tagged areas include Cross-Channel Messaging, Customer Engagement, Email, Marketing Automation, and Push Notifications.


  The Iterable catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 2 Spectral governance rulesets.


  Iterable''s developer surface includes CLI, changelog, API reference, getting-started guide, authentication, documentation, support, and 41 more developer resources.'
plans:
- name: Iterable Plans Pricing
  plan_count: 3
  slug: iterable-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 54
  name: Iterable Rate Limits
  slug: iterable-rate-limits
rules:
- effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Iterable API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 1
    warn: 6
  slug: iterable-asyncapi-spectral-rules
- effective_rule_count: 5
  extends: []
  name: Iterable API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: iterable-jsonschema-spectral-rules
score:
  band: exemplar
  composite: 71.1
  coverage:
    artifact_dirs: 33
    catalog_gap: 45.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.1
  facets:
    access_clarity: 65.8
    commercial_clarity: 65.8
    contract_governance: 33.3
    contract_quality: 68.9
    developer_ergonomics: 83.3
    discoverability: 75.9
    governance: 33.3
    operational_transparency: 81.6
  previous_composite: 71.0
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 27
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 41.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/iterable/refs/heads/main/screenshots/iterable-2026-06-20T183630.png
security:
- kind: authentication
  name: Iterable Authentication
  slug: iterable-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Iterable Domain Security
  slug: iterable-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Iterable Trust Center
  slug: iterable-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: iterable
tags:
- Cross-Channel Messaging
- Customer Engagement
- Email
- Marketing Automation
- Push Notifications
- SMS
website: https://iterable.com/
---

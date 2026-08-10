---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 48
  human_in_the_loop: 0
  name: Rapidapi Agentic Access
  operation_count: 93
  slug: rapidapi-agentic-access
  summary_line: 93 operations · 48 acting
api_count: 29
apis:
- description: Endpoints for configuring alert notifications when tests fail, including integrations with PagerDuty, Slack, and Twilio.
  name: RapidAPI Alerts API
  slug: rapidapi-alerts-api
- description: Endpoints for retrieving gateway traffic analytics, including request counts, response times, error rates, and usage patterns.
  name: RapidAPI Analytics API
  slug: rapidapi-analytics-api
- description: The Apis API from RapidAPI — 6 operation(s) for apis.
  name: RapidAPI Apis API
  slug: rapidapi-apis-api
- description: Endpoints for creating, updating, and deleting applications and their associated authorizations within the Enterprise Hub.
  name: RapidAPI Applications API
  slug: rapidapi-applications-api
- description: Endpoints for configuring authentication schemes on gateways, including OAuth2, API key, header-based, and basic authentication.
  name: RapidAPI Authentication API
  slug: rapidapi-authentication-api
- description: Endpoints for browsing API categories available on the marketplace, including Data, Sports, Finance, Travel, and Entertainment.
  name: RapidAPI Categories API
  slug: rapidapi-categories-api
- description: Endpoints for browsing curated API collections organized around themes such as Top Meme APIs, Top Geocoding APIs, and other groupings.
  name: RapidAPI Collections API
  slug: rapidapi-collections-api
- description: Endpoints for importing, exporting, and managing API definitions such as OpenAPI specifications and Postman Collections.
  name: RapidAPI Definitions API
  slug: rapidapi-definitions-api
- description: Endpoints for generating and managing API documentation from project definitions and endpoint configurations.
  name: RapidAPI Documentation API
  slug: rapidapi-documentation-api
- description: Endpoints for managing API endpoint configurations within a project, including creating, updating, and organizing endpoint groups.
  name: RapidAPI Endpoints API
  slug: rapidapi-endpoints-api
- description: Endpoints for managing test environments with variable sets that can be used across tests for different deployment stages.
  name: RapidAPI Environments API
  slug: rapidapi-environments-api
- description: Endpoints for viewing test execution results, including pass/fail statuses, response times, and detailed assertion outcomes.
  name: RapidAPI Executions API
  slug: rapidapi-executions-api
- description: Endpoints for managing gateway instances, including creating, configuring, and monitoring custom API gateways.
  name: RapidAPI Gateways API
  slug: rapidapi-gateways-api
- description: The single GraphQL endpoint that accepts all queries and mutations for managing the Enterprise Hub, including APIs, collections, organizations, users, and hub configuration.
  name: RapidAPI GraphQL API
  slug: rapidapi-graphql-api
- description: Endpoints for listing available monitoring locations across global AWS regions where tests can be executed.
  name: RapidAPI Locations API
  slug: rapidapi-locations-api
- description: Endpoints for managing organizations within the Enterprise Hub, including listing, creating, and updating organization configurations.
  name: RapidAPI Organizations API
  slug: rapidapi-organizations-api
- description: Endpoints for managing API projects within Studio, including creating, listing, updating, and deleting projects.
  name: RapidAPI Projects API
  slug: rapidapi-projects-api
- description: Endpoints for configuring rate limiting policies to protect APIs from overuse, including request limits, quota management, and request size limits.
  name: RapidAPI Rate Limiting API
  slug: rapidapi-rate-limiting-api
- description: Endpoints for managing saved API requests within a project, including importing from spec files and organizing into groups.
  name: RapidAPI Requests API
  slug: rapidapi-requests-api
- description: Endpoints for configuring request routing rules that determine how incoming API requests are forwarded to backend services.
  name: RapidAPI Routes API
  slug: rapidapi-routes-api
- description: Endpoints for managing test schedules, including frequency, environment, and location settings for automated monitoring.
  name: RapidAPI Schedules API
  slug: rapidapi-schedules-api
- description: Endpoints for searching and discovering APIs by keyword, category, collection, or advanced filters across the RapidAPI marketplace.
  name: RapidAPI Search API
  slug: rapidapi-search-api
- description: Endpoints for configuring security policies such as IP allow and deny lists, CORS settings, and proxy secret validation.
  name: RapidAPI Security API
  slug: rapidapi-security-api
- description: Endpoints for generating code snippets for API calls in multiple programming languages and libraries.
  name: RapidAPI Snippets API
  slug: rapidapi-snippets-api
- description: Endpoints for managing API subscriptions, including subscribing to API plans, viewing active subscriptions, and usage analytics.
  name: RapidAPI Subscriptions API
  slug: rapidapi-subscriptions-api
- description: The Tags API from RapidAPI — 2 operation(s) for tags.
  name: RapidAPI Tags API
  slug: rapidapi-tags-api
- description: Endpoints for creating, reading, updating, deleting, and executing API tests, including functional and performance test flows.
  name: RapidAPI Tests API
  slug: rapidapi-tests-api
- description: Endpoints for viewing and managing API transaction records, including usage data and billing information.
  name: RapidAPI Transactions API
  slug: rapidapi-transactions-api
- description: Endpoints for managing users within the Enterprise Hub, including user roles, permissions, and account configurations.
  name: RapidAPI Users API
  slug: rapidapi-users-api
artifact_total: 118
collections:
- collection_type: open
  name: RapidAPI Gateway API
  slug: open-rapidapi-gateway-api
- collection_type: open
  name: RapidAPI GraphQL Platform API
  slug: open-rapidapi-graphql-platform-api
- collection_type: open
  name: RapidAPI Hub API
  slug: open-rapidapi-hub-api
- collection_type: open
  name: RapidAPI REST Platform API
  slug: open-rapidapi-rest-platform-api
- collection_type: open
  name: RapidAPI Studio API
  slug: open-rapidapi-studio-api
- collection_type: open
  name: RapidAPI Testing API
  slug: open-rapidapi-testing-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/rapidapi-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/rapidapi-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/rapidapi-authentication.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/RapidAPI
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/rapidapi
- group: start
  title: ''
  type: Portal
  url: https://rapidapi.com/hub
- group: docs
  title: ''
  type: Documentation
  url: https://docs.rapidapi.com/
- group: company
  title: ''
  type: Website
  url: https://rapidapi.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://rapidapi.com/privacy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://rapidapi.com/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://rapidapi.com/support/
- group: company
  title: ''
  type: Blog
  url: https://rapidapi.com/blog/
- group: start
  title: ''
  type: Signup
  url: https://rapidapi.com/auth/sign-up
- group: design
  title: ''
  type: JSONLD
  url: json-ld/rapidapi-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/rapidapi-vocabulary.yml
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.rapidapi.com/llms.txt
created: '2026-03-20'
description: RapidAPI operates the world's largest API marketplace, connecting developers to thousands of APIs through a single platform. Their developer platform provides tools for API discovery, testing, management, design, and gateway configuration, enabling both individual developers and enterprises to build, consume, and manage APIs at scale.
examples:
- key_count: 2
  name: Rapidapi List Apis Example
  slug: rapidapi-list-apis-example
- key_count: 2
  name: Rapidapi List Subscriptions Example
  slug: rapidapi-list-subscriptions-example
- key_count: 2
  name: Rapidapi List Tests Example
  slug: rapidapi-list-tests-example
finops:
- name: Rapidapi Finops
  service_category: API Management
  slug: rapidapi-finops
graphqls:
- description: The RapidAPI GraphQL Platform API exposes the same queries and mutations that RapidAPI uses internally, providing enterprise users with a powerful interface for managing their API hub. It supports cre
  name: RapidAPI GraphQL API
  slug: rapidapi-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/rapidapi.png
json_schemas:
- name: Alert
  property_count: 6
  slug: rapidapi-alert
- name: AlertInput
  property_count: 4
  slug: rapidapi-alertinput
- name: RapidAPI API Listing
  property_count: 19
  slug: rapidapi-api-listing
- name: Api
  property_count: 10
  slug: rapidapi-api
- name: ApiCreateInput
  property_count: 6
  slug: rapidapi-apicreateinput
- name: ApiDetails
  property_count: 15
  slug: rapidapi-apidetails
- name: ApiEndpoint
  property_count: 7
  slug: rapidapi-apiendpoint
- name: ApiSummary
  property_count: 10
  slug: rapidapi-apisummary
- name: ApiUpdateInput
  property_count: 6
  slug: rapidapi-apiupdateinput
- name: ApiVersion
  property_count: 5
  slug: rapidapi-apiversion
- name: ApiVersionUpdateInput
  property_count: 3
  slug: rapidapi-apiversionupdateinput
- name: Application
  property_count: 6
  slug: rapidapi-application
- name: ApplicationInput
  property_count: 2
  slug: rapidapi-applicationinput
- name: Assertion
  property_count: 4
  slug: rapidapi-assertion
- name: AssertionInput
  property_count: 3
  slug: rapidapi-assertioninput
- name: AuthenticationConfig
  property_count: 5
  slug: rapidapi-authenticationconfig
- name: AuthenticationConfigInput
  property_count: 4
  slug: rapidapi-authenticationconfiginput
- name: Category
  property_count: 3
  slug: rapidapi-category
- name: CategoryInput
  property_count: 1
  slug: rapidapi-categoryinput
- name: CodeSnippet
  property_count: 3
  slug: rapidapi-codesnippet
- name: Collection
  property_count: 5
  slug: rapidapi-collection
- name: CollectionInput
  property_count: 3
  slug: rapidapi-collectioninput
- name: Definition
  property_count: 6
  slug: rapidapi-definition
- name: Endpoint
  property_count: 7
  slug: rapidapi-endpoint
- name: EndpointInput
  property_count: 5
  slug: rapidapi-endpointinput
- name: EndpointParameter
  property_count: 6
  slug: rapidapi-endpointparameter
- name: Environment
  property_count: 4
  slug: rapidapi-environment
- name: EnvironmentInput
  property_count: 2
  slug: rapidapi-environmentinput
- name: Execution
  property_count: 7
  slug: rapidapi-execution
- name: ExecutionDetail
  property_count: 9
  slug: rapidapi-executiondetail
- name: RapidAPI Gateway Configuration
  property_count: 13
  slug: rapidapi-gateway-config
- name: Gateway
  property_count: 9
  slug: rapidapi-gateway
- name: GatewayAnalytics
  property_count: 7
  slug: rapidapi-gatewayanalytics
- name: GatewayInput
  property_count: 4
  slug: rapidapi-gatewayinput
- name: GraphQLError
  property_count: 4
  slug: rapidapi-graphqlerror
- name: GraphQLRequest
  property_count: 3
  slug: rapidapi-graphqlrequest
- name: GraphQLResponse
  property_count: 2
  slug: rapidapi-graphqlresponse
- name: HubCategory
  property_count: 4
  slug: rapidapi-hubcategory
- name: HubCollection
  property_count: 5
  slug: rapidapi-hubcollection
- name: HubSubscription
  property_count: 8
  slug: rapidapi-hubsubscription
- name: Location
  property_count: 4
  slug: rapidapi-location
- name: Organization
  property_count: 5
  slug: rapidapi-organization
- name: OrganizationUpdateInput
  property_count: 2
  slug: rapidapi-organizationupdateinput
- name: PricingPlan
  property_count: 5
  slug: rapidapi-pricingplan
- name: Project
  property_count: 7
  slug: rapidapi-project
- name: ProjectInput
  property_count: 3
  slug: rapidapi-projectinput
- name: RateLimitConfig
  property_count: 6
  slug: rapidapi-ratelimitconfig
- name: RateLimitConfigInput
  property_count: 5
  slug: rapidapi-ratelimitconfiginput
- name: Route
  property_count: 8
  slug: rapidapi-route
- name: RouteInput
  property_count: 6
  slug: rapidapi-routeinput
- name: SavedRequest
  property_count: 7
  slug: rapidapi-savedrequest
- name: Schedule
  property_count: 7
  slug: rapidapi-schedule
- name: ScheduleInput
  property_count: 5
  slug: rapidapi-scheduleinput
- name: SecurityConfig
  property_count: 6
  slug: rapidapi-securityconfig
- name: SecurityConfigInput
  property_count: 5
  slug: rapidapi-securityconfiginput
- name: StepResult
  property_count: 6
  slug: rapidapi-stepresult
- name: Subscription
  property_count: 6
  slug: rapidapi-subscription
- name: Tag
  property_count: 3
  slug: rapidapi-tag
- name: TagInput
  property_count: 1
  slug: rapidapi-taginput
- name: RapidAPI Test
  property_count: 12
  slug: rapidapi-test
- name: TestCreateInput
  property_count: 5
  slug: rapidapi-testcreateinput
- name: TestStep
  property_count: 7
  slug: rapidapi-teststep
- name: TestStepInput
  property_count: 6
  slug: rapidapi-teststepinput
- name: TestUpdateInput
  property_count: 3
  slug: rapidapi-testupdateinput
- name: Transaction
  property_count: 7
  slug: rapidapi-transaction
- name: User
  property_count: 6
  slug: rapidapi-user
json_structures:
- name: Rapidapi Api Listing Structure
  property_count: 0
  slug: rapidapi-api-listing-structure
- name: Rapidapi Structure
  property_count: 0
  slug: rapidapi-structure
- name: Rapidapi Subscription Structure
  property_count: 0
  slug: rapidapi-subscription-structure
- name: Rapidapi Test Structure
  property_count: 0
  slug: rapidapi-test-structure
jsonld:
- class_count: 0
  name: Rapidapi Context
  property_count: 11
  slug: rapidapi-context
layout: provider
modified: '2026-05-19'
name: RapidAPI
nav: Providers
network: true
overview: 'RapidAPI publishes 29 APIs on the [APIs.io](https://apis.io/) network, including Alerts API, Analytics API, Apis API, and 26 more. Tagged areas include API Marketplace, API Management, API Testing, API Gateway, and API Design.


  The RapidAPI catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  RapidAPI''s developer surface includes authentication, developer portal, documentation, support, engineering blog, signup flow, and 10 more developer resources.'
plans:
- name: Rapidapi Plans Pricing
  plan_count: 1
  slug: rapidapi-plans-pricing
random_paper: 30
rate_limits:
- limit_count: 2
  name: Rapidapi Rate Limits
  slug: rapidapi-rate-limits
rules:
- name: RapidAPI API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: rapidapi-jsonschema-spectral-rules
- name: RapidAPI API Rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 1
    info: 0
    warn: 6
  slug: rapidapi-rules
score:
  band: developing
  composite: 54.3
  delta: 0.0
  facets:
    commercial_clarity: 50.0
    contract_quality: 79.1
    developer_ergonomics: 34.8
    discoverability: 59.3
    governance: 68.8
    operational_transparency: 26.3
  previous_composite: 54.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 29
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/rapidapi/refs/heads/main/screenshots/rapidapi-2026-06-20T192601.png
security:
- kind: authentication
  name: Rapidapi Authentication
  slug: rapidapi-authentication
  summary_line: apiKey · 2 schemes
- kind: domain-security
  name: Rapidapi Domain Security
  slug: rapidapi-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC
slug: rapidapi
tags:
- API Marketplace
- API Management
- API Testing
- API Gateway
- API Design
- Enterprise
website: https://rapidapi.com/
---

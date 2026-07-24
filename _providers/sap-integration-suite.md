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
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 48.1
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 7
  human_in_the_loop: 0
  name: Sap Integration Suite Agentic Access
  operation_count: 26
  slug: sap-integration-suite-agentic-access
  summary_line: 26 operations · 7 acting
api_count: 16
apis:
- description: The SAP Integration Advisor API provides access to the library of message implementation guidelines (MIGs) and mapping guidelines (MAGs) used to simplify B2B and A2A integration scenarios. It supports
  name: SAP Integration Advisor API
  slug: sap-integration-advisor
- description: The SAP Open Connectors API (formerly Cloud Elements) provides a unified REST interface to connect to over 160 third-party cloud applications using pre-built connectors. It normalizes disparate API en
  name: SAP Open Connectors API
  slug: sap-open-connectors
- description: The SAP Trading Partner Management API supports setup and management of B2B trading partner relationships, agreements, and communication channels within SAP Integration Suite. It enables automation of
  name: SAP Trading Partner Management API
  slug: sap-trading-partner-management
- description: The SAP Event Mesh API provides access to the event brokering service within SAP Business Technology Platform that enables applications to communicate through asynchronous events. It supports publishi
  name: SAP Event Mesh API
  slug: sap-event-mesh
- description: The SAP Integration Suite Advanced Event Mesh (AEM) REST API provides management capabilities for event brokers, message queues, topic subscriptions, and event broker services. It enables programmatic
  name: SAP Integration Suite Advanced Event Mesh API
  slug: sap-integration-suite-advanced-event-mesh
- description: Manage API products bundling multiple APIs
  name: SAP Integration Suite API Products API
  slug: sap-integration-suite-api-products-api
- description: Manage API proxy configurations
  name: SAP Integration Suite API Proxies API
  slug: sap-integration-suite-api-proxies-api
- description: Manage developer applications and credentials
  name: SAP Integration Suite Applications API
  slug: sap-integration-suite-applications-api
- description: Manage developer accounts
  name: SAP Integration Suite Developers API
  slug: sap-integration-suite-developers-api
- description: Deploy and manage integration flow artifacts
  name: SAP Integration Suite Integration Flows API
  slug: sap-integration-suite-integration-flows-api
- description: Manage integration packages and their content
  name: SAP Integration Suite Integration Packages API
  slug: sap-integration-suite-integration-packages-api
- description: Manage key-value map configurations
  name: SAP Integration Suite Key Value Maps API
  slug: sap-integration-suite-key-value-maps-api
- description: Retrieve message processing logs and audit information
  name: SAP Integration Suite Message Processing Logs API
  slug: sap-integration-suite-message-processing-logs-api
- description: Manage deployed runtime artifacts
  name: SAP Integration Suite Runtime Artifacts API
  slug: sap-integration-suite-runtime-artifacts-api
- description: Discover and manage service endpoints
  name: SAP Integration Suite Service Endpoints API
  slug: sap-integration-suite-service-endpoints-api
- description: Manage global and local variables
  name: SAP Integration Suite Variables API
  slug: sap-integration-suite-variables-api
arazzos:
- description: Inventory deployed runtime artifacts, inspect a chosen one, and list its service endpoints.
  name: SAP Integration Suite Catalog Runtime Endpoints
  slug: sap-integration-suite-catalog-runtime-endpoints-workflow
- description: Deploy an integration flow, wait for it to start, then verify recent message processing succeeded.
  name: SAP Integration Suite Deploy And Verify Flow
  slug: sap-integration-suite-deploy-and-verify-flow-workflow
- description: Discover an integration flow inside a package, deploy it, and poll the runtime until it starts.
  name: SAP Integration Suite Deploy Flow From Package
  slug: sap-integration-suite-deploy-flow-from-package-workflow
- description: Find failed message processing logs, read the worst offender in detail, and pull its adapter attributes.
  name: SAP Integration Suite Monitor Failed Messages
  slug: sap-integration-suite-monitor-failed-messages-workflow
- description: Compare a package's design-time artifacts against what is deployed in the runtime to surface drift.
  name: SAP Integration Suite Package Deployment Drift
  slug: sap-integration-suite-package-deployment-drift-workflow
- description: List existing key-value maps, and create a new one only if it does not already exist.
  name: SAP Integration Suite Provision Key Value Map
  slug: sap-integration-suite-provision-key-value-map-workflow
- description: Create an API proxy, confirm it, then bundle it into a published API product with a quota.
  name: SAP Integration Suite Publish API Product
  slug: sap-integration-suite-publish-api-product-workflow
- description: Confirm an API proxy exists, list products to check for dependents, then delete the proxy.
  name: SAP Integration Suite Retire API Proxy
  slug: sap-integration-suite-retire-api-proxy-workflow
- description: Verify a developer exists, read their application, and confirm the API product it subscribes to.
  name: SAP Integration Suite Review Application Access
  slug: sap-integration-suite-review-application-access-workflow
- description: Read a single message processing log by GUID, pull its adapter attributes, and find correlated messages.
  name: SAP Integration Suite Trace Message By GUID
  slug: sap-integration-suite-trace-message-by-guid-workflow
- description: Confirm a runtime artifact is deployed, undeploy it, and verify it is gone.
  name: SAP Integration Suite Undeploy Runtime Artifact
  slug: sap-integration-suite-undeploy-runtime-artifact-workflow
- description: Look up an API proxy by name and update it if it exists, otherwise create it.
  name: SAP Integration Suite Upsert API Proxy
  slug: sap-integration-suite-upsert-api-proxy-workflow
artifact_total: 62
collections:
- collection_type: postman
  name: SAP API Management API
  slug: postman-sap-integration-suite-api-management
- collection_type: postman
  name: SAP Cloud Integration API
  slug: postman-sap-integration-suite-cloud-integration
- collection_type: open
  name: SAP API Management API
  slug: open-sap-integration-suite-api-management
- collection_type: open
  name: SAP Cloud Integration API
  slug: open-sap-integration-suite-cloud-integration
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sap-integration-suite-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sap-integration-suite-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sap-integration-suite-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sap-integration-suite-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/sap-integration-suite-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sap-integration-suite/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-catalog-runtime-endpoints-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-deploy-and-verify-flow-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-deploy-flow-from-package-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-monitor-failed-messages-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-package-deployment-drift-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-provision-key-value-map-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-publish-api-product-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-retire-api-proxy-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-review-application-access-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-trace-message-by-guid-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-undeploy-runtime-artifact-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sap-integration-suite-upsert-api-proxy-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://api.sap.com/
- group: docs
  title: ''
  type: Documentation
  url: https://help.sap.com/docs/integration-suite
- group: company
  title: ''
  type: Website
  url: https://www.sap.com/products/technology-platform/integration-suite.html
- group: start
  title: ''
  type: GettingStarted
  url: https://help.sap.com/docs/integration-suite/sap-integration-suite/what-is-sap-integration-suite
- group: auth
  title: ''
  type: Authentication
  url: https://help.sap.com/docs/integration-suite/sap-integration-suite/setting-up-oauth-inbound-authentication
- group: company
  title: ''
  type: Blog
  url: https://blogs.sap.com/tags/73554900100700002542/
- group: operate
  title: ''
  type: Community
  url: https://community.sap.com/topics/integration-suite
- group: operate
  title: ''
  type: Support
  url: https://support.sap.com/en/product/support-by-product/73554900100700002542.html
- group: operate
  title: ''
  type: StatusPage
  url: https://www.sap.com/about/trust-center/cloud-service-status.html
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/SAP-samples
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sap.com/about/agreements/policies/cloud-platform.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sap.com/about/legal/privacy.html
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@SAPTechnology
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sap.com/products/technology-platform/integration-suite/pricing.html
- group: learn
  title: ''
  type: Tutorials
  url: https://developers.sap.com/tutorial-navigator.html?tag=software-product%3Atechnology-platform%2Fsap-integration-suite
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sap-integration-suite-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/integration-lifecycle.yaml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sap-integration-suite-rules.yml
created: '2026-03-16'
description: SAP Integration Suite is an enterprise integration platform as a service (iPaaS) that connects applications, processes, and people across cloud and on-premises environments. It includes capabilities for Cloud Integration, API Management, Integration Advisor, Open Connectors, Trading Partner Management, and Event Mesh as part of SAP Business Technology Platform (BTP). It enables seamless connectivity between SAP and non-SAP systems.
examples:
- key_count: 2
  name: Sap Integration Suite List Integration Packages Example
  slug: sap-integration-suite-list-integration-packages-example
- key_count: 2
  name: Sap Integration Suite List Message Processing Logs Example
  slug: sap-integration-suite-list-message-processing-logs-example
finops:
- name: Sap Integration Suite Finops
  service_category: Integration Platform
  slug: sap-integration-suite-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sap-integration-suite.png
json_schemas:
- name: APIProduct
  property_count: 8
  slug: sap-integration-suite-apiproduct
- name: APIProductRequest
  property_count: 4
  slug: sap-integration-suite-apiproductrequest
- name: APIProxy
  property_count: 10
  slug: sap-integration-suite-apiproxy
- name: APIProxyRequest
  property_count: 6
  slug: sap-integration-suite-apiproxyrequest
- name: Application
  property_count: 8
  slug: sap-integration-suite-application
- name: Developer
  property_count: 6
  slug: sap-integration-suite-developer
- name: SAP Integration Package
  property_count: 10
  slug: sap-integration-suite-integration-package
- name: IntegrationArtifact
  property_count: 8
  slug: sap-integration-suite-integrationartifact
- name: IntegrationPackage
  property_count: 10
  slug: sap-integration-suite-integrationpackage
- name: KeyValueMap
  property_count: 4
  slug: sap-integration-suite-keyvaluemap
- name: SAP Message Processing Log
  property_count: 11
  slug: sap-integration-suite-message-processing-log
- name: MessageProcessingLog
  property_count: 11
  slug: sap-integration-suite-messageprocessinglog
- name: RuntimeArtifact
  property_count: 8
  slug: sap-integration-suite-runtimeartifact
- name: ServiceEndpoint
  property_count: 5
  slug: sap-integration-suite-serviceendpoint
- name: Variable
  property_count: 5
  slug: sap-integration-suite-variable
json_structures:
- name: Sap Integration Suite Integration Package Structure
  property_count: 0
  slug: sap-integration-suite-integration-package-structure
- name: Sap Integration Suite Structure
  property_count: 0
  slug: sap-integration-suite-structure
jsonld:
- class_count: 20
  name: Sap Integration Suite Context
  property_count: 6
  slug: sap-integration-suite-context
layout: provider
modified: '2026-05-19'
name: SAP Integration Suite
nav: Providers
network: true
overview: 'SAP Integration Suite publishes 11 APIs on the [APIs.io](https://apis.io/) network, including API Products API, API Proxies API, Applications API, and 8 more. Tagged areas include API Management, Cloud Integration, Enterprise Integration, Event Mesh, and iPaaS.


  The SAP Integration Suite catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  SAP Integration Suite''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, support, YouTube channel, and 29 more developer resources.'
plans:
- name: Sap Integration Suite Plans Pricing
  plan_count: 1
  slug: sap-integration-suite-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 1
  name: Sap Integration Suite Rate Limits
  slug: sap-integration-suite-rate-limits
rules:
- name: SAP Integration Suite API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sap-integration-suite-jsonschema-spectral-rules
- name: SAP Integration Suite API Rules
  rule_count: 11
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 10
  slug: sap-integration-suite-rules
scopes:
- name: Sap Integration Suite Scopes
  scope_count: 0
  slug: sap-integration-suite-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: strong
  composite: 61.6
  delta: 0.0
  facets:
    commercial_clarity: 60.5
    contract_quality: 67.3
    developer_ergonomics: 50.0
    discoverability: 67.5
    governance: 86.8
    operational_transparency: 42.1
  previous_composite: 61.6
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sap-integration-suite/refs/heads/main/screenshots/sap-integration-suite-2026-06-20T193428.png
security:
- kind: authentication
  name: Sap Integration Suite Authentication
  slug: sap-integration-suite-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Sap Integration Suite Domain Security
  slug: sap-integration-suite-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sap Integration Suite Vulnerability Disclosure
  slug: sap-integration-suite-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: sap-integration-suite
tags:
- API Management
- Cloud Integration
- Enterprise Integration
- Event Mesh
- iPaaS
- SAP
- SAP BTP
website: https://www.sap.com/products/technology-platform/integration-suite.html
---

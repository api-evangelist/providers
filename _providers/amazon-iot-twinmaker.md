---
access_model:
  confidence: medium
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - security
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.1
  scored_at: '2026-09-05'
agentic_access:
- acting_count: 28
  human_in_the_loop: 0
  name: Amazon Iot Twinmaker Agentic Access
  operation_count: 34
  slug: amazon-iot-twinmaker-agentic-access
  summary_line: 34 operations · 28 acting
api_count: 1
apis:
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Pricingplan API from Amazon IoT TwinMaker — 1 operation(s) for pricingplan.
  name: Amazon IoT TwinMaker Pricingplan API
  slug: amazon-iot-twinmaker-pricingplan-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Queries API from Amazon IoT TwinMaker — 1 operation(s) for queries.
  name: Amazon IoT TwinMaker Queries API
  slug: amazon-iot-twinmaker-queries-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Sync Jobs API from Amazon IoT TwinMaker — 1 operation(s) for sync jobs.
  name: Amazon IoT TwinMaker Sync Jobs API
  slug: amazon-iot-twinmaker-sync-jobs-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Tags API from Amazon IoT TwinMaker — 1 operation(s) for tags.
  name: Amazon IoT TwinMaker Tags API
  slug: amazon-iot-twinmaker-tags-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Tags List API from Amazon IoT TwinMaker — 1 operation(s) for tags list.
  name: Amazon IoT TwinMaker Tags List API
  slug: amazon-iot-twinmaker-tags-list-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Tags#resourceARN&tagKeys API from Amazon IoT TwinMaker — 1 operation(s) for tags#resourcearn&tagkeys.
  name: Amazon IoT TwinMaker Tags#resourceARN&tagKeys API
  slug: amazon-iot-twinmaker-tags-resourcearn-tagkeys-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Workspaces API from Amazon IoT TwinMaker — 15 operation(s) for workspaces.
  name: Amazon IoT TwinMaker Workspaces API
  slug: amazon-iot-twinmaker-workspaces-api
- baseURL: https://iottwinmaker.amazonaws.com
  baseurl_source: declared
  description: The Workspaces List API from Amazon IoT TwinMaker — 1 operation(s) for workspaces list.
  name: Amazon IoT TwinMaker Workspaces List API
  slug: amazon-iot-twinmaker-workspaces-list-api
artifact_total: 590
collections:
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan API
  slug: postman-amazon-iot-twinmaker-pricingplan-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Queries API
  slug: postman-amazon-iot-twinmaker-queries-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Sync Jobs API
  slug: postman-amazon-iot-twinmaker-sync-jobs-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Tags API
  slug: postman-amazon-iot-twinmaker-tags-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Tags List API
  slug: postman-amazon-iot-twinmaker-tags-list-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Tags#resourceARN&tagKeys API
  slug: postman-amazon-iot-twinmaker-tags-resourcearn-tagkeys-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Workspaces API
  slug: postman-amazon-iot-twinmaker-workspaces-api
- collection_type: postman
  name: AWS IoT TwinMaker Pricingplan Workspaces List API
  slug: postman-amazon-iot-twinmaker-workspaces-list-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan API
  slug: open-amazon-iot-twinmaker-pricingplan-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Queries API
  slug: open-amazon-iot-twinmaker-queries-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Sync Jobs API
  slug: open-amazon-iot-twinmaker-sync-jobs-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Tags API
  slug: open-amazon-iot-twinmaker-tags-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Tags List API
  slug: open-amazon-iot-twinmaker-tags-list-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Tags#resourceARN&tagKeys API
  slug: open-amazon-iot-twinmaker-tags-resourcearn-tagkeys-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Workspaces API
  slug: open-amazon-iot-twinmaker-workspaces-api
- collection_type: open
  name: AWS IoT TwinMaker Pricingplan Workspaces List API
  slug: open-amazon-iot-twinmaker-workspaces-list-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-iot-twinmaker/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-iot-twinmaker-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-iot-twinmaker-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-iot-twinmaker-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-iot-twinmaker-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-iot-twinmaker-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/iot-twinmaker/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/iot-twinmaker/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/iot-twinmaker/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-twinmaker/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/iottwinmaker/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: start
  title: ''
  type: Login
  url: https://signin.aws.amazon.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-iot-twinmaker-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-twinmaker-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-iot-twinmaker-context.jsonld
created: '2026-03-16'
description: AWS IoT TwinMaker makes it easier for developers to create digital twins of real-world systems such as buildings, factories, and industrial equipment. You can use AWS IoT TwinMaker to build operational digital twin applications to visualize, monitor, and diagnose complex operational systems.
examples:
- key_count: 1
  name: Iot Twinmaker Batch Put Property Error Entry Example
  slug: iot-twinmaker-batch-put-property-error-entry-example
- key_count: 3
  name: Iot Twinmaker Batch Put Property Error Example
  slug: iot-twinmaker-batch-put-property-error-example
- key_count: 1
  name: Iot Twinmaker Batch Put Property Values Request Example
  slug: iot-twinmaker-batch-put-property-values-request-example
- key_count: 1
  name: Iot Twinmaker Batch Put Property Values Response Example
  slug: iot-twinmaker-batch-put-property-values-response-example
- key_count: 2
  name: Iot Twinmaker Bundle Information Example
  slug: iot-twinmaker-bundle-information-example
- key_count: 2
  name: Iot Twinmaker Column Description Example
  slug: iot-twinmaker-column-description-example
- key_count: 0
  name: Iot Twinmaker Column Descriptions Example
  slug: iot-twinmaker-column-descriptions-example
- key_count: 3
  name: Iot Twinmaker Component Property Group Request Example
  slug: iot-twinmaker-component-property-group-request-example
- key_count: 0
  name: Iot Twinmaker Component Property Group Requests Example
  slug: iot-twinmaker-component-property-group-requests-example
- key_count: 3
  name: Iot Twinmaker Component Property Group Response Example
  slug: iot-twinmaker-component-property-group-response-example
- key_count: 0
  name: Iot Twinmaker Component Property Group Responses Example
  slug: iot-twinmaker-component-property-group-responses-example
- key_count: 4
  name: Iot Twinmaker Component Request Example
  slug: iot-twinmaker-component-request-example
- key_count: 8
  name: Iot Twinmaker Component Response Example
  slug: iot-twinmaker-component-response-example
- key_count: 0
  name: Iot Twinmaker Component Type Summaries Example
  slug: iot-twinmaker-component-type-summaries-example
- key_count: 7
  name: Iot Twinmaker Component Type Summary Example
  slug: iot-twinmaker-component-type-summary-example
- key_count: 5
  name: Iot Twinmaker Component Update Request Example
  slug: iot-twinmaker-component-update-request-example
- key_count: 0
  name: Iot Twinmaker Component Updates Map Request Example
  slug: iot-twinmaker-component-updates-map-request-example
- key_count: 0
  name: Iot Twinmaker Components Map Example
  slug: iot-twinmaker-components-map-example
- key_count: 0
  name: Iot Twinmaker Components Map Request Example
  slug: iot-twinmaker-components-map-request-example
- key_count: 0
  name: Iot Twinmaker Configuration Example
  slug: iot-twinmaker-configuration-example
- key_count: 8
  name: Iot Twinmaker Create Component Type Request Example
  slug: iot-twinmaker-create-component-type-request-example
- key_count: 3
  name: Iot Twinmaker Create Component Type Response Example
  slug: iot-twinmaker-create-component-type-response-example
- key_count: 6
  name: Iot Twinmaker Create Entity Request Example
  slug: iot-twinmaker-create-entity-request-example
- key_count: 4
  name: Iot Twinmaker Create Entity Response Example
  slug: iot-twinmaker-create-entity-response-example
- key_count: 6
  name: Iot Twinmaker Create Scene Request Example
  slug: iot-twinmaker-create-scene-request-example
- key_count: 2
  name: Iot Twinmaker Create Scene Response Example
  slug: iot-twinmaker-create-scene-response-example
- key_count: 2
  name: Iot Twinmaker Create Sync Job Request Example
  slug: iot-twinmaker-create-sync-job-request-example
- key_count: 3
  name: Iot Twinmaker Create Sync Job Response Example
  slug: iot-twinmaker-create-sync-job-response-example
- key_count: 4
  name: Iot Twinmaker Create Workspace Request Example
  slug: iot-twinmaker-create-workspace-request-example
- key_count: 2
  name: Iot Twinmaker Create Workspace Response Example
  slug: iot-twinmaker-create-workspace-response-example
- key_count: 2
  name: Iot Twinmaker Data Connector Example
  slug: iot-twinmaker-data-connector-example
- key_count: 5
  name: Iot Twinmaker Data Type Example
  slug: iot-twinmaker-data-type-example
- key_count: 9
  name: Iot Twinmaker Data Value Example
  slug: iot-twinmaker-data-value-example
- key_count: 0
  name: Iot Twinmaker Data Value List Example
  slug: iot-twinmaker-data-value-list-example
- key_count: 0
  name: Iot Twinmaker Data Value Map Example
  slug: iot-twinmaker-data-value-map-example
- key_count: 0
  name: Iot Twinmaker Delete Component Type Request Example
  slug: iot-twinmaker-delete-component-type-request-example
- key_count: 1
  name: Iot Twinmaker Delete Component Type Response Example
  slug: iot-twinmaker-delete-component-type-response-example
- key_count: 0
  name: Iot Twinmaker Delete Entity Request Example
  slug: iot-twinmaker-delete-entity-request-example
- key_count: 1
  name: Iot Twinmaker Delete Entity Response Example
  slug: iot-twinmaker-delete-entity-response-example
- key_count: 0
  name: Iot Twinmaker Delete Scene Request Example
  slug: iot-twinmaker-delete-scene-request-example
- key_count: 0
  name: Iot Twinmaker Delete Scene Response Example
  slug: iot-twinmaker-delete-scene-response-example
- key_count: 0
  name: Iot Twinmaker Delete Sync Job Request Example
  slug: iot-twinmaker-delete-sync-job-request-example
- key_count: 1
  name: Iot Twinmaker Delete Sync Job Response Example
  slug: iot-twinmaker-delete-sync-job-response-example
- key_count: 0
  name: Iot Twinmaker Delete Workspace Request Example
  slug: iot-twinmaker-delete-workspace-request-example
- key_count: 0
  name: Iot Twinmaker Delete Workspace Response Example
  slug: iot-twinmaker-delete-workspace-response-example
- key_count: 4
  name: Iot Twinmaker Entity Property Reference Example
  slug: iot-twinmaker-entity-property-reference-example
- key_count: 0
  name: Iot Twinmaker Entity Summaries Example
  slug: iot-twinmaker-entity-summaries-example
- key_count: 9
  name: Iot Twinmaker Entity Summary Example
  slug: iot-twinmaker-entity-summary-example
- key_count: 0
  name: Iot Twinmaker Entries Example
  slug: iot-twinmaker-entries-example
- key_count: 2
  name: Iot Twinmaker Error Details Example
  slug: iot-twinmaker-error-details-example
- key_count: 0
  name: Iot Twinmaker Error Entries Example
  slug: iot-twinmaker-error-entries-example
- key_count: 0
  name: Iot Twinmaker Errors Example
  slug: iot-twinmaker-errors-example
- key_count: 4
  name: Iot Twinmaker Execute Query Request Example
  slug: iot-twinmaker-execute-query-request-example
- key_count: 3
  name: Iot Twinmaker Execute Query Response Example
  slug: iot-twinmaker-execute-query-response-example
- key_count: 0
  name: Iot Twinmaker Extends From Example
  slug: iot-twinmaker-extends-from-example
- key_count: 0
  name: Iot Twinmaker External Id Property Example
  slug: iot-twinmaker-external-id-property-example
- key_count: 3
  name: Iot Twinmaker Function Request Example
  slug: iot-twinmaker-function-request-example
- key_count: 4
  name: Iot Twinmaker Function Response Example
  slug: iot-twinmaker-function-response-example
- key_count: 0
  name: Iot Twinmaker Functions Request Example
  slug: iot-twinmaker-functions-request-example
- key_count: 0
  name: Iot Twinmaker Functions Response Example
  slug: iot-twinmaker-functions-response-example
- key_count: 0
  name: Iot Twinmaker Generated Scene Metadata Map Example
  slug: iot-twinmaker-generated-scene-metadata-map-example
- key_count: 0
  name: Iot Twinmaker Get Component Type Request Example
  slug: iot-twinmaker-get-component-type-request-example
- key_count: 16
  name: Iot Twinmaker Get Component Type Response Example
  slug: iot-twinmaker-get-component-type-response-example
- key_count: 0
  name: Iot Twinmaker Get Entity Request Example
  slug: iot-twinmaker-get-entity-request-example
- key_count: 12
  name: Iot Twinmaker Get Entity Response Example
  slug: iot-twinmaker-get-entity-response-example
- key_count: 0
  name: Iot Twinmaker Get Pricing Plan Request Example
  slug: iot-twinmaker-get-pricing-plan-request-example
- key_count: 2
  name: Iot Twinmaker Get Pricing Plan Response Example
  slug: iot-twinmaker-get-pricing-plan-response-example
- key_count: 13
  name: Iot Twinmaker Get Property Value History Request Example
  slug: iot-twinmaker-get-property-value-history-request-example
- key_count: 2
  name: Iot Twinmaker Get Property Value History Response Example
  slug: iot-twinmaker-get-property-value-history-response-example
- key_count: 8
  name: Iot Twinmaker Get Property Value Request Example
  slug: iot-twinmaker-get-property-value-request-example
- key_count: 3
  name: Iot Twinmaker Get Property Value Response Example
  slug: iot-twinmaker-get-property-value-response-example
- key_count: 0
  name: Iot Twinmaker Get Scene Request Example
  slug: iot-twinmaker-get-scene-request-example
- key_count: 11
  name: Iot Twinmaker Get Scene Response Example
  slug: iot-twinmaker-get-scene-response-example
- key_count: 0
  name: Iot Twinmaker Get Sync Job Request Example
  slug: iot-twinmaker-get-sync-job-request-example
- key_count: 7
  name: Iot Twinmaker Get Sync Job Response Example
  slug: iot-twinmaker-get-sync-job-response-example
- key_count: 0
  name: Iot Twinmaker Get Workspace Request Example
  slug: iot-twinmaker-get-workspace-request-example
- key_count: 7
  name: Iot Twinmaker Get Workspace Response Example
  slug: iot-twinmaker-get-workspace-response-example
- key_count: 2
  name: Iot Twinmaker Interpolation Parameters Example
  slug: iot-twinmaker-interpolation-parameters-example
- key_count: 1
  name: Iot Twinmaker Lambda Function Example
  slug: iot-twinmaker-lambda-function-example
- key_count: 3
  name: Iot Twinmaker List Component Types Filter Example
  slug: iot-twinmaker-list-component-types-filter-example
- key_count: 0
  name: Iot Twinmaker List Component Types Filters Example
  slug: iot-twinmaker-list-component-types-filters-example
- key_count: 3
  name: Iot Twinmaker List Component Types Request Example
  slug: iot-twinmaker-list-component-types-request-example
- key_count: 4
  name: Iot Twinmaker List Component Types Response Example
  slug: iot-twinmaker-list-component-types-response-example
- key_count: 3
  name: Iot Twinmaker List Entities Filter Example
  slug: iot-twinmaker-list-entities-filter-example
- key_count: 0
  name: Iot Twinmaker List Entities Filters Example
  slug: iot-twinmaker-list-entities-filters-example
- key_count: 3
  name: Iot Twinmaker List Entities Request Example
  slug: iot-twinmaker-list-entities-request-example
- key_count: 2
  name: Iot Twinmaker List Entities Response Example
  slug: iot-twinmaker-list-entities-response-example
- key_count: 2
  name: Iot Twinmaker List Scenes Request Example
  slug: iot-twinmaker-list-scenes-request-example
- key_count: 2
  name: Iot Twinmaker List Scenes Response Example
  slug: iot-twinmaker-list-scenes-response-example
- key_count: 2
  name: Iot Twinmaker List Sync Jobs Request Example
  slug: iot-twinmaker-list-sync-jobs-request-example
- key_count: 2
  name: Iot Twinmaker List Sync Jobs Response Example
  slug: iot-twinmaker-list-sync-jobs-response-example
- key_count: 3
  name: Iot Twinmaker List Sync Resources Request Example
  slug: iot-twinmaker-list-sync-resources-request-example
- key_count: 2
  name: Iot Twinmaker List Sync Resources Response Example
  slug: iot-twinmaker-list-sync-resources-response-example
- key_count: 3
  name: Iot Twinmaker List Tags For Resource Request Example
  slug: iot-twinmaker-list-tags-for-resource-request-example
- key_count: 2
  name: Iot Twinmaker List Tags For Resource Response Example
  slug: iot-twinmaker-list-tags-for-resource-response-example
- key_count: 2
  name: Iot Twinmaker List Workspaces Request Example
  slug: iot-twinmaker-list-workspaces-request-example
- key_count: 2
  name: Iot Twinmaker List Workspaces Response Example
  slug: iot-twinmaker-list-workspaces-response-example
- key_count: 2
  name: Iot Twinmaker Order By Example
  slug: iot-twinmaker-order-by-example
- key_count: 0
  name: Iot Twinmaker Order By List Example
  slug: iot-twinmaker-order-by-list-example
- key_count: 2
  name: Iot Twinmaker Parent Entity Update Request Example
  slug: iot-twinmaker-parent-entity-update-request-example
- key_count: 0
  name: Iot Twinmaker Pricing Bundles Example
  slug: iot-twinmaker-pricing-bundles-example
- key_count: 6
  name: Iot Twinmaker Pricing Plan Example
  slug: iot-twinmaker-pricing-plan-example
- key_count: 8
  name: Iot Twinmaker Property Definition Request Example
  slug: iot-twinmaker-property-definition-request-example
- key_count: 11
  name: Iot Twinmaker Property Definition Response Example
  slug: iot-twinmaker-property-definition-response-example
- key_count: 0
  name: Iot Twinmaker Property Definitions Request Example
  slug: iot-twinmaker-property-definitions-request-example
- key_count: 0
  name: Iot Twinmaker Property Definitions Response Example
  slug: iot-twinmaker-property-definitions-response-example
- key_count: 3
  name: Iot Twinmaker Property Filter Example
  slug: iot-twinmaker-property-filter-example
- key_count: 0
  name: Iot Twinmaker Property Filters Example
  slug: iot-twinmaker-property-filters-example
- key_count: 2
  name: Iot Twinmaker Property Group Request Example
  slug: iot-twinmaker-property-group-request-example
- key_count: 3
  name: Iot Twinmaker Property Group Response Example
  slug: iot-twinmaker-property-group-response-example
- key_count: 0
  name: Iot Twinmaker Property Groups Request Example
  slug: iot-twinmaker-property-groups-request-example
- key_count: 0
  name: Iot Twinmaker Property Groups Response Example
  slug: iot-twinmaker-property-groups-response-example
- key_count: 2
  name: Iot Twinmaker Property Latest Value Example
  slug: iot-twinmaker-property-latest-value-example
- key_count: 0
  name: Iot Twinmaker Property Latest Value Map Example
  slug: iot-twinmaker-property-latest-value-map-example
- key_count: 0
  name: Iot Twinmaker Property Names Example
  slug: iot-twinmaker-property-names-example
- key_count: 3
  name: Iot Twinmaker Property Request Example
  slug: iot-twinmaker-property-request-example
- key_count: 0
  name: Iot Twinmaker Property Requests Example
  slug: iot-twinmaker-property-requests-example
- key_count: 2
  name: Iot Twinmaker Property Response Example
  slug: iot-twinmaker-property-response-example
- key_count: 0
  name: Iot Twinmaker Property Responses Example
  slug: iot-twinmaker-property-responses-example
- key_count: 0
  name: Iot Twinmaker Property Table Value Example
  slug: iot-twinmaker-property-table-value-example
- key_count: 2
  name: Iot Twinmaker Property Value Entry Example
  slug: iot-twinmaker-property-value-entry-example
- key_count: 3
  name: Iot Twinmaker Property Value Example
  slug: iot-twinmaker-property-value-example
- key_count: 2
  name: Iot Twinmaker Property Value History Example
  slug: iot-twinmaker-property-value-history-example
- key_count: 0
  name: Iot Twinmaker Property Value List Example
  slug: iot-twinmaker-property-value-list-example
- key_count: 0
  name: Iot Twinmaker Property Values Example
  slug: iot-twinmaker-property-values-example
- key_count: 0
  name: Iot Twinmaker Query Result Value Example
  slug: iot-twinmaker-query-result-value-example
- key_count: 2
  name: Iot Twinmaker Relationship Example
  slug: iot-twinmaker-relationship-example
- key_count: 2
  name: Iot Twinmaker Relationship Value Example
  slug: iot-twinmaker-relationship-value-example
- key_count: 0
  name: Iot Twinmaker Required Properties Example
  slug: iot-twinmaker-required-properties-example
- key_count: 0
  name: Iot Twinmaker Row Data Example
  slug: iot-twinmaker-row-data-example
- key_count: 1
  name: Iot Twinmaker Row Example
  slug: iot-twinmaker-row-example
- key_count: 0
  name: Iot Twinmaker Rows Example
  slug: iot-twinmaker-rows-example
- key_count: 0
  name: Iot Twinmaker Scene Capabilities Example
  slug: iot-twinmaker-scene-capabilities-example
- key_count: 2
  name: Iot Twinmaker Scene Error Example
  slug: iot-twinmaker-scene-error-example
- key_count: 0
  name: Iot Twinmaker Scene Metadata Map Example
  slug: iot-twinmaker-scene-metadata-map-example
- key_count: 0
  name: Iot Twinmaker Scene Summaries Example
  slug: iot-twinmaker-scene-summaries-example
- key_count: 6
  name: Iot Twinmaker Scene Summary Example
  slug: iot-twinmaker-scene-summary-example
- key_count: 0
  name: Iot Twinmaker Selected Property List Example
  slug: iot-twinmaker-selected-property-list-example
- key_count: 2
  name: Iot Twinmaker Status Example
  slug: iot-twinmaker-status-example
- key_count: 2
  name: Iot Twinmaker Sync Job Status Example
  slug: iot-twinmaker-sync-job-status-example
- key_count: 0
  name: Iot Twinmaker Sync Job Summaries Example
  slug: iot-twinmaker-sync-job-summaries-example
- key_count: 6
  name: Iot Twinmaker Sync Job Summary Example
  slug: iot-twinmaker-sync-job-summary-example
- key_count: 4
  name: Iot Twinmaker Sync Resource Filter Example
  slug: iot-twinmaker-sync-resource-filter-example
- key_count: 0
  name: Iot Twinmaker Sync Resource Filters Example
  slug: iot-twinmaker-sync-resource-filters-example
- key_count: 2
  name: Iot Twinmaker Sync Resource Status Example
  slug: iot-twinmaker-sync-resource-status-example
- key_count: 0
  name: Iot Twinmaker Sync Resource Summaries Example
  slug: iot-twinmaker-sync-resource-summaries-example
- key_count: 5
  name: Iot Twinmaker Sync Resource Summary Example
  slug: iot-twinmaker-sync-resource-summary-example
- key_count: 2
  name: Iot Twinmaker Tabular Conditions Example
  slug: iot-twinmaker-tabular-conditions-example
- key_count: 0
  name: Iot Twinmaker Tabular Property Value Example
  slug: iot-twinmaker-tabular-property-value-example
- key_count: 0
  name: Iot Twinmaker Tabular Property Values Example
  slug: iot-twinmaker-tabular-property-values-example
- key_count: 0
  name: Iot Twinmaker Tag Key List Example
  slug: iot-twinmaker-tag-key-list-example
- key_count: 0
  name: Iot Twinmaker Tag Map Example
  slug: iot-twinmaker-tag-map-example
- key_count: 2
  name: Iot Twinmaker Tag Resource Request Example
  slug: iot-twinmaker-tag-resource-request-example
- key_count: 0
  name: Iot Twinmaker Tag Resource Response Example
  slug: iot-twinmaker-tag-resource-response-example
- key_count: 0
  name: Iot Twinmaker Untag Resource Request Example
  slug: iot-twinmaker-untag-resource-request-example
- key_count: 0
  name: Iot Twinmaker Untag Resource Response Example
  slug: iot-twinmaker-untag-resource-response-example
- key_count: 7
  name: Iot Twinmaker Update Component Type Request Example
  slug: iot-twinmaker-update-component-type-request-example
- key_count: 4
  name: Iot Twinmaker Update Component Type Response Example
  slug: iot-twinmaker-update-component-type-response-example
- key_count: 4
  name: Iot Twinmaker Update Entity Request Example
  slug: iot-twinmaker-update-entity-request-example
- key_count: 2
  name: Iot Twinmaker Update Entity Response Example
  slug: iot-twinmaker-update-entity-response-example
- key_count: 2
  name: Iot Twinmaker Update Pricing Plan Request Example
  slug: iot-twinmaker-update-pricing-plan-request-example
- key_count: 2
  name: Iot Twinmaker Update Pricing Plan Response Example
  slug: iot-twinmaker-update-pricing-plan-response-example
- key_count: 4
  name: Iot Twinmaker Update Scene Request Example
  slug: iot-twinmaker-update-scene-request-example
- key_count: 1
  name: Iot Twinmaker Update Scene Response Example
  slug: iot-twinmaker-update-scene-response-example
- key_count: 2
  name: Iot Twinmaker Update Workspace Request Example
  slug: iot-twinmaker-update-workspace-request-example
- key_count: 1
  name: Iot Twinmaker Update Workspace Response Example
  slug: iot-twinmaker-update-workspace-response-example
- key_count: 0
  name: Iot Twinmaker Values Example
  slug: iot-twinmaker-values-example
- key_count: 0
  name: Iot Twinmaker Workspace Summaries Example
  slug: iot-twinmaker-workspace-summaries-example
- key_count: 5
  name: Iot Twinmaker Workspace Summary Example
  slug: iot-twinmaker-workspace-summary-example
features:
- description: Model physical systems as entities with components and property relationships.
  name: Digital Twin Modeling
- description: Build interactive 3D visualization scenes connected to live IoT data.
  name: 3D Scene Integration
- description: Connect to existing data sources with built-in and custom data connectors.
  name: Data Connectors
- description: Explore entity relationships and property graphs for complex systems.
  name: Knowledge Graph
finops:
- name: Amazon Iot Twinmaker Finops
  service_category: API
  slug: amazon-iot-twinmaker-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-iot-twinmaker.png
json_schemas:
- name: BatchPutPropertyErrorEntry
  property_count: 1
  slug: iot-twinmaker-batch-put-property-error-entry
- name: BatchPutPropertyError
  property_count: 3
  slug: iot-twinmaker-batch-put-property-error
- name: BatchPutPropertyValuesRequest
  property_count: 1
  slug: iot-twinmaker-batch-put-property-values-request
- name: BatchPutPropertyValuesResponse
  property_count: 1
  slug: iot-twinmaker-batch-put-property-values-response
- name: BundleInformation
  property_count: 2
  slug: iot-twinmaker-bundle-information
- name: ColumnDescription
  property_count: 2
  slug: iot-twinmaker-column-description
- name: ColumnDescriptions
  property_count: 0
  slug: iot-twinmaker-column-descriptions
- name: ColumnType
  property_count: 0
  slug: iot-twinmaker-column-type
- name: ComponentPropertyGroupRequest
  property_count: 3
  slug: iot-twinmaker-component-property-group-request
- name: ComponentPropertyGroupRequests
  property_count: 0
  slug: iot-twinmaker-component-property-group-requests
- name: ComponentPropertyGroupResponse
  property_count: 3
  slug: iot-twinmaker-component-property-group-response
- name: ComponentPropertyGroupResponses
  property_count: 0
  slug: iot-twinmaker-component-property-group-responses
- name: ComponentRequest
  property_count: 4
  slug: iot-twinmaker-component-request
- name: ComponentResponse
  property_count: 8
  slug: iot-twinmaker-component-response
- name: ComponentTypeSummaries
  property_count: 0
  slug: iot-twinmaker-component-type-summaries
- name: ComponentTypeSummary
  property_count: 7
  slug: iot-twinmaker-component-type-summary
- name: ComponentUpdateRequest
  property_count: 5
  slug: iot-twinmaker-component-update-request
- name: ComponentUpdateType
  property_count: 0
  slug: iot-twinmaker-component-update-type
- name: ComponentUpdatesMapRequest
  property_count: 0
  slug: iot-twinmaker-component-updates-map-request
- name: ComponentsMapRequest
  property_count: 0
  slug: iot-twinmaker-components-map-request
- name: ComponentsMap
  property_count: 0
  slug: iot-twinmaker-components-map
- name: Configuration
  property_count: 0
  slug: iot-twinmaker-configuration
- name: CreateComponentTypeRequest
  property_count: 8
  slug: iot-twinmaker-create-component-type-request
- name: CreateComponentTypeResponse
  property_count: 3
  slug: iot-twinmaker-create-component-type-response
- name: CreateEntityRequest
  property_count: 6
  slug: iot-twinmaker-create-entity-request
- name: CreateEntityResponse
  property_count: 4
  slug: iot-twinmaker-create-entity-response
- name: CreateSceneRequest
  property_count: 6
  slug: iot-twinmaker-create-scene-request
- name: CreateSceneResponse
  property_count: 2
  slug: iot-twinmaker-create-scene-response
- name: CreateSyncJobRequest
  property_count: 2
  slug: iot-twinmaker-create-sync-job-request
- name: CreateSyncJobResponse
  property_count: 3
  slug: iot-twinmaker-create-sync-job-response
- name: CreateWorkspaceRequest
  property_count: 4
  slug: iot-twinmaker-create-workspace-request
- name: CreateWorkspaceResponse
  property_count: 2
  slug: iot-twinmaker-create-workspace-response
- name: DataConnector
  property_count: 2
  slug: iot-twinmaker-data-connector
- name: DataType
  property_count: 5
  slug: iot-twinmaker-data-type
- name: DataValueList
  property_count: 0
  slug: iot-twinmaker-data-value-list
- name: DataValueMap
  property_count: 0
  slug: iot-twinmaker-data-value-map
- name: DataValue
  property_count: 9
  slug: iot-twinmaker-data-value
- name: DeleteComponentTypeRequest
  property_count: 0
  slug: iot-twinmaker-delete-component-type-request
- name: DeleteComponentTypeResponse
  property_count: 1
  slug: iot-twinmaker-delete-component-type-response
- name: DeleteEntityRequest
  property_count: 0
  slug: iot-twinmaker-delete-entity-request
- name: DeleteEntityResponse
  property_count: 1
  slug: iot-twinmaker-delete-entity-response
- name: DeleteSceneRequest
  property_count: 0
  slug: iot-twinmaker-delete-scene-request
- name: DeleteSceneResponse
  property_count: 0
  slug: iot-twinmaker-delete-scene-response
- name: DeleteSyncJobRequest
  property_count: 0
  slug: iot-twinmaker-delete-sync-job-request
- name: DeleteSyncJobResponse
  property_count: 1
  slug: iot-twinmaker-delete-sync-job-response
- name: DeleteWorkspaceRequest
  property_count: 0
  slug: iot-twinmaker-delete-workspace-request
- name: DeleteWorkspaceResponse
  property_count: 0
  slug: iot-twinmaker-delete-workspace-response
- name: EntityPropertyReference
  property_count: 4
  slug: iot-twinmaker-entity-property-reference
- name: EntitySummaries
  property_count: 0
  slug: iot-twinmaker-entity-summaries
- name: EntitySummary
  property_count: 9
  slug: iot-twinmaker-entity-summary
- name: Entries
  property_count: 0
  slug: iot-twinmaker-entries
- name: ErrorCode
  property_count: 0
  slug: iot-twinmaker-error-code
- name: ErrorDetails
  property_count: 2
  slug: iot-twinmaker-error-details
- name: ErrorEntries
  property_count: 0
  slug: iot-twinmaker-error-entries
- name: Errors
  property_count: 0
  slug: iot-twinmaker-errors
- name: ExecuteQueryRequest
  property_count: 4
  slug: iot-twinmaker-execute-query-request
- name: ExecuteQueryResponse
  property_count: 3
  slug: iot-twinmaker-execute-query-response
- name: ExtendsFrom
  property_count: 0
  slug: iot-twinmaker-extends-from
- name: ExternalIdProperty
  property_count: 0
  slug: iot-twinmaker-external-id-property
- name: FunctionRequest
  property_count: 3
  slug: iot-twinmaker-function-request
- name: FunctionResponse
  property_count: 4
  slug: iot-twinmaker-function-response
- name: FunctionsRequest
  property_count: 0
  slug: iot-twinmaker-functions-request
- name: FunctionsResponse
  property_count: 0
  slug: iot-twinmaker-functions-response
- name: GeneratedSceneMetadataMap
  property_count: 0
  slug: iot-twinmaker-generated-scene-metadata-map
- name: GetComponentTypeRequest
  property_count: 0
  slug: iot-twinmaker-get-component-type-request
- name: GetComponentTypeResponse
  property_count: 16
  slug: iot-twinmaker-get-component-type-response
- name: GetEntityRequest
  property_count: 0
  slug: iot-twinmaker-get-entity-request
- name: GetEntityResponse
  property_count: 12
  slug: iot-twinmaker-get-entity-response
- name: GetPricingPlanRequest
  property_count: 0
  slug: iot-twinmaker-get-pricing-plan-request
- name: GetPricingPlanResponse
  property_count: 2
  slug: iot-twinmaker-get-pricing-plan-response
- name: GetPropertyValueHistoryRequest
  property_count: 13
  slug: iot-twinmaker-get-property-value-history-request
- name: GetPropertyValueHistoryResponse
  property_count: 2
  slug: iot-twinmaker-get-property-value-history-response
- name: GetPropertyValueRequest
  property_count: 8
  slug: iot-twinmaker-get-property-value-request
- name: GetPropertyValueResponse
  property_count: 3
  slug: iot-twinmaker-get-property-value-response
- name: GetSceneRequest
  property_count: 0
  slug: iot-twinmaker-get-scene-request
- name: GetSceneResponse
  property_count: 11
  slug: iot-twinmaker-get-scene-response
- name: GetSyncJobRequest
  property_count: 0
  slug: iot-twinmaker-get-sync-job-request
- name: GetSyncJobResponse
  property_count: 7
  slug: iot-twinmaker-get-sync-job-response
- name: GetWorkspaceRequest
  property_count: 0
  slug: iot-twinmaker-get-workspace-request
- name: GetWorkspaceResponse
  property_count: 7
  slug: iot-twinmaker-get-workspace-response
- name: GroupType
  property_count: 0
  slug: iot-twinmaker-group-type
- name: InterpolationParameters
  property_count: 2
  slug: iot-twinmaker-interpolation-parameters
- name: InterpolationType
  property_count: 0
  slug: iot-twinmaker-interpolation-type
- name: LambdaFunction
  property_count: 1
  slug: iot-twinmaker-lambda-function
- name: ListComponentTypesFilter
  property_count: 3
  slug: iot-twinmaker-list-component-types-filter
- name: ListComponentTypesFilters
  property_count: 0
  slug: iot-twinmaker-list-component-types-filters
- name: ListComponentTypesRequest
  property_count: 3
  slug: iot-twinmaker-list-component-types-request
- name: ListComponentTypesResponse
  property_count: 4
  slug: iot-twinmaker-list-component-types-response
- name: ListEntitiesFilter
  property_count: 3
  slug: iot-twinmaker-list-entities-filter
- name: ListEntitiesFilters
  property_count: 0
  slug: iot-twinmaker-list-entities-filters
- name: ListEntitiesRequest
  property_count: 3
  slug: iot-twinmaker-list-entities-request
- name: ListEntitiesResponse
  property_count: 2
  slug: iot-twinmaker-list-entities-response
- name: ListScenesRequest
  property_count: 2
  slug: iot-twinmaker-list-scenes-request
- name: ListScenesResponse
  property_count: 2
  slug: iot-twinmaker-list-scenes-response
- name: ListSyncJobsRequest
  property_count: 2
  slug: iot-twinmaker-list-sync-jobs-request
- name: ListSyncJobsResponse
  property_count: 2
  slug: iot-twinmaker-list-sync-jobs-response
- name: ListSyncResourcesRequest
  property_count: 3
  slug: iot-twinmaker-list-sync-resources-request
- name: ListSyncResourcesResponse
  property_count: 2
  slug: iot-twinmaker-list-sync-resources-response
- name: ListTagsForResourceRequest
  property_count: 3
  slug: iot-twinmaker-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 2
  slug: iot-twinmaker-list-tags-for-resource-response
- name: ListWorkspacesRequest
  property_count: 2
  slug: iot-twinmaker-list-workspaces-request
- name: ListWorkspacesResponse
  property_count: 2
  slug: iot-twinmaker-list-workspaces-response
- name: OrderByList
  property_count: 0
  slug: iot-twinmaker-order-by-list
- name: OrderBy
  property_count: 2
  slug: iot-twinmaker-order-by
- name: OrderByTime
  property_count: 0
  slug: iot-twinmaker-order-by-time
- name: Order
  property_count: 0
  slug: iot-twinmaker-order
- name: ParentEntityUpdateRequest
  property_count: 2
  slug: iot-twinmaker-parent-entity-update-request
- name: ParentEntityUpdateType
  property_count: 0
  slug: iot-twinmaker-parent-entity-update-type
- name: PricingBundles
  property_count: 0
  slug: iot-twinmaker-pricing-bundles
- name: PricingMode
  property_count: 0
  slug: iot-twinmaker-pricing-mode
- name: PricingPlan
  property_count: 6
  slug: iot-twinmaker-pricing-plan
- name: PricingTier
  property_count: 0
  slug: iot-twinmaker-pricing-tier
- name: PropertyDefinitionRequest
  property_count: 8
  slug: iot-twinmaker-property-definition-request
- name: PropertyDefinitionResponse
  property_count: 11
  slug: iot-twinmaker-property-definition-response
- name: PropertyDefinitionsRequest
  property_count: 0
  slug: iot-twinmaker-property-definitions-request
- name: PropertyDefinitionsResponse
  property_count: 0
  slug: iot-twinmaker-property-definitions-response
- name: PropertyFilter
  property_count: 3
  slug: iot-twinmaker-property-filter
- name: PropertyFilters
  property_count: 0
  slug: iot-twinmaker-property-filters
- name: PropertyGroupRequest
  property_count: 2
  slug: iot-twinmaker-property-group-request
- name: PropertyGroupResponse
  property_count: 3
  slug: iot-twinmaker-property-group-response
- name: PropertyGroupUpdateType
  property_count: 0
  slug: iot-twinmaker-property-group-update-type
- name: PropertyGroupsRequest
  property_count: 0
  slug: iot-twinmaker-property-groups-request
- name: PropertyGroupsResponse
  property_count: 0
  slug: iot-twinmaker-property-groups-response
- name: PropertyLatestValueMap
  property_count: 0
  slug: iot-twinmaker-property-latest-value-map
- name: PropertyLatestValue
  property_count: 2
  slug: iot-twinmaker-property-latest-value
- name: PropertyNames
  property_count: 0
  slug: iot-twinmaker-property-names
- name: PropertyRequest
  property_count: 3
  slug: iot-twinmaker-property-request
- name: PropertyRequests
  property_count: 0
  slug: iot-twinmaker-property-requests
- name: PropertyResponse
  property_count: 2
  slug: iot-twinmaker-property-response
- name: PropertyResponses
  property_count: 0
  slug: iot-twinmaker-property-responses
- name: PropertyTableValue
  property_count: 0
  slug: iot-twinmaker-property-table-value
- name: PropertyUpdateType
  property_count: 0
  slug: iot-twinmaker-property-update-type
- name: PropertyValueEntry
  property_count: 2
  slug: iot-twinmaker-property-value-entry
- name: PropertyValueHistory
  property_count: 2
  slug: iot-twinmaker-property-value-history
- name: PropertyValueList
  property_count: 0
  slug: iot-twinmaker-property-value-list
- name: PropertyValue
  property_count: 3
  slug: iot-twinmaker-property-value
- name: PropertyValues
  property_count: 0
  slug: iot-twinmaker-property-values
- name: QueryResultValue
  property_count: 0
  slug: iot-twinmaker-query-result-value
- name: Relationship
  property_count: 2
  slug: iot-twinmaker-relationship
- name: RelationshipValue
  property_count: 2
  slug: iot-twinmaker-relationship-value
- name: RequiredProperties
  property_count: 0
  slug: iot-twinmaker-required-properties
- name: RowData
  property_count: 0
  slug: iot-twinmaker-row-data
- name: Row
  property_count: 1
  slug: iot-twinmaker-row
- name: Rows
  property_count: 0
  slug: iot-twinmaker-rows
- name: SceneCapabilities
  property_count: 0
  slug: iot-twinmaker-scene-capabilities
- name: SceneErrorCode
  property_count: 0
  slug: iot-twinmaker-scene-error-code
- name: SceneError
  property_count: 2
  slug: iot-twinmaker-scene-error
- name: SceneMetadataMap
  property_count: 0
  slug: iot-twinmaker-scene-metadata-map
- name: SceneSummaries
  property_count: 0
  slug: iot-twinmaker-scene-summaries
- name: SceneSummary
  property_count: 6
  slug: iot-twinmaker-scene-summary
- name: Scope
  property_count: 0
  slug: iot-twinmaker-scope
- name: SelectedPropertyList
  property_count: 0
  slug: iot-twinmaker-selected-property-list
- name: State
  property_count: 0
  slug: iot-twinmaker-state
- name: Status
  property_count: 2
  slug: iot-twinmaker-status
- name: SyncJobState
  property_count: 0
  slug: iot-twinmaker-sync-job-state
- name: SyncJobStatus
  property_count: 2
  slug: iot-twinmaker-sync-job-status
- name: SyncJobSummaries
  property_count: 0
  slug: iot-twinmaker-sync-job-summaries
- name: SyncJobSummary
  property_count: 6
  slug: iot-twinmaker-sync-job-summary
- name: SyncResourceFilter
  property_count: 4
  slug: iot-twinmaker-sync-resource-filter
- name: SyncResourceFilters
  property_count: 0
  slug: iot-twinmaker-sync-resource-filters
- name: SyncResourceState
  property_count: 0
  slug: iot-twinmaker-sync-resource-state
- name: SyncResourceStatus
  property_count: 2
  slug: iot-twinmaker-sync-resource-status
- name: SyncResourceSummaries
  property_count: 0
  slug: iot-twinmaker-sync-resource-summaries
- name: SyncResourceSummary
  property_count: 5
  slug: iot-twinmaker-sync-resource-summary
- name: SyncResourceType
  property_count: 0
  slug: iot-twinmaker-sync-resource-type
- name: TabularConditions
  property_count: 2
  slug: iot-twinmaker-tabular-conditions
- name: TabularPropertyValue
  property_count: 0
  slug: iot-twinmaker-tabular-property-value
- name: TabularPropertyValues
  property_count: 0
  slug: iot-twinmaker-tabular-property-values
- name: TagKeyList
  property_count: 0
  slug: iot-twinmaker-tag-key-list
- name: TagMap
  property_count: 0
  slug: iot-twinmaker-tag-map
- name: TagResourceRequest
  property_count: 2
  slug: iot-twinmaker-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: iot-twinmaker-tag-resource-response
- name: Type
  property_count: 0
  slug: iot-twinmaker-type
- name: UntagResourceRequest
  property_count: 0
  slug: iot-twinmaker-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: iot-twinmaker-untag-resource-response
- name: UpdateComponentTypeRequest
  property_count: 7
  slug: iot-twinmaker-update-component-type-request
- name: UpdateComponentTypeResponse
  property_count: 4
  slug: iot-twinmaker-update-component-type-response
- name: UpdateEntityRequest
  property_count: 4
  slug: iot-twinmaker-update-entity-request
- name: UpdateEntityResponse
  property_count: 2
  slug: iot-twinmaker-update-entity-response
- name: UpdatePricingPlanRequest
  property_count: 2
  slug: iot-twinmaker-update-pricing-plan-request
- name: UpdatePricingPlanResponse
  property_count: 2
  slug: iot-twinmaker-update-pricing-plan-response
- name: UpdateReason
  property_count: 0
  slug: iot-twinmaker-update-reason
- name: UpdateSceneRequest
  property_count: 4
  slug: iot-twinmaker-update-scene-request
- name: UpdateSceneResponse
  property_count: 1
  slug: iot-twinmaker-update-scene-response
- name: UpdateWorkspaceRequest
  property_count: 2
  slug: iot-twinmaker-update-workspace-request
- name: UpdateWorkspaceResponse
  property_count: 1
  slug: iot-twinmaker-update-workspace-response
- name: Values
  property_count: 0
  slug: iot-twinmaker-values
- name: WorkspaceSummaries
  property_count: 0
  slug: iot-twinmaker-workspace-summaries
- name: WorkspaceSummary
  property_count: 5
  slug: iot-twinmaker-workspace-summary
json_structures:
- name: Iot Twinmaker Batch Put Property Error Entry Structure
  property_count: 1
  slug: iot-twinmaker-batch-put-property-error-entry-structure
- name: Iot Twinmaker Batch Put Property Error Structure
  property_count: 3
  slug: iot-twinmaker-batch-put-property-error-structure
- name: Iot Twinmaker Batch Put Property Values Request Structure
  property_count: 1
  slug: iot-twinmaker-batch-put-property-values-request-structure
- name: Iot Twinmaker Batch Put Property Values Response Structure
  property_count: 1
  slug: iot-twinmaker-batch-put-property-values-response-structure
- name: Iot Twinmaker Bundle Information Structure
  property_count: 2
  slug: iot-twinmaker-bundle-information-structure
- name: Iot Twinmaker Column Description Structure
  property_count: 2
  slug: iot-twinmaker-column-description-structure
- name: Iot Twinmaker Column Descriptions Structure
  property_count: 0
  slug: iot-twinmaker-column-descriptions-structure
- name: Iot Twinmaker Column Type Structure
  property_count: 0
  slug: iot-twinmaker-column-type-structure
- name: Iot Twinmaker Component Property Group Request Structure
  property_count: 3
  slug: iot-twinmaker-component-property-group-request-structure
- name: Iot Twinmaker Component Property Group Requests Structure
  property_count: 0
  slug: iot-twinmaker-component-property-group-requests-structure
- name: Iot Twinmaker Component Property Group Response Structure
  property_count: 3
  slug: iot-twinmaker-component-property-group-response-structure
- name: Iot Twinmaker Component Property Group Responses Structure
  property_count: 0
  slug: iot-twinmaker-component-property-group-responses-structure
- name: Iot Twinmaker Component Request Structure
  property_count: 4
  slug: iot-twinmaker-component-request-structure
- name: Iot Twinmaker Component Response Structure
  property_count: 8
  slug: iot-twinmaker-component-response-structure
- name: Iot Twinmaker Component Type Summaries Structure
  property_count: 0
  slug: iot-twinmaker-component-type-summaries-structure
- name: Iot Twinmaker Component Type Summary Structure
  property_count: 7
  slug: iot-twinmaker-component-type-summary-structure
- name: Iot Twinmaker Component Update Request Structure
  property_count: 5
  slug: iot-twinmaker-component-update-request-structure
- name: Iot Twinmaker Component Update Type Structure
  property_count: 0
  slug: iot-twinmaker-component-update-type-structure
- name: Iot Twinmaker Component Updates Map Request Structure
  property_count: 0
  slug: iot-twinmaker-component-updates-map-request-structure
- name: Iot Twinmaker Components Map Request Structure
  property_count: 0
  slug: iot-twinmaker-components-map-request-structure
- name: Iot Twinmaker Components Map Structure
  property_count: 0
  slug: iot-twinmaker-components-map-structure
- name: Iot Twinmaker Configuration Structure
  property_count: 0
  slug: iot-twinmaker-configuration-structure
- name: Iot Twinmaker Create Component Type Request Structure
  property_count: 8
  slug: iot-twinmaker-create-component-type-request-structure
- name: Iot Twinmaker Create Component Type Response Structure
  property_count: 3
  slug: iot-twinmaker-create-component-type-response-structure
- name: Iot Twinmaker Create Entity Request Structure
  property_count: 6
  slug: iot-twinmaker-create-entity-request-structure
- name: Iot Twinmaker Create Entity Response Structure
  property_count: 4
  slug: iot-twinmaker-create-entity-response-structure
- name: Iot Twinmaker Create Scene Request Structure
  property_count: 6
  slug: iot-twinmaker-create-scene-request-structure
- name: Iot Twinmaker Create Scene Response Structure
  property_count: 2
  slug: iot-twinmaker-create-scene-response-structure
- name: Iot Twinmaker Create Sync Job Request Structure
  property_count: 2
  slug: iot-twinmaker-create-sync-job-request-structure
- name: Iot Twinmaker Create Sync Job Response Structure
  property_count: 3
  slug: iot-twinmaker-create-sync-job-response-structure
- name: Iot Twinmaker Create Workspace Request Structure
  property_count: 4
  slug: iot-twinmaker-create-workspace-request-structure
- name: Iot Twinmaker Create Workspace Response Structure
  property_count: 2
  slug: iot-twinmaker-create-workspace-response-structure
- name: Iot Twinmaker Data Connector Structure
  property_count: 2
  slug: iot-twinmaker-data-connector-structure
- name: Iot Twinmaker Data Type Structure
  property_count: 5
  slug: iot-twinmaker-data-type-structure
- name: Iot Twinmaker Data Value List Structure
  property_count: 0
  slug: iot-twinmaker-data-value-list-structure
- name: Iot Twinmaker Data Value Map Structure
  property_count: 0
  slug: iot-twinmaker-data-value-map-structure
- name: Iot Twinmaker Data Value Structure
  property_count: 9
  slug: iot-twinmaker-data-value-structure
- name: Iot Twinmaker Delete Component Type Request Structure
  property_count: 0
  slug: iot-twinmaker-delete-component-type-request-structure
- name: Iot Twinmaker Delete Component Type Response Structure
  property_count: 1
  slug: iot-twinmaker-delete-component-type-response-structure
- name: Iot Twinmaker Delete Entity Request Structure
  property_count: 0
  slug: iot-twinmaker-delete-entity-request-structure
- name: Iot Twinmaker Delete Entity Response Structure
  property_count: 1
  slug: iot-twinmaker-delete-entity-response-structure
- name: Iot Twinmaker Delete Scene Request Structure
  property_count: 0
  slug: iot-twinmaker-delete-scene-request-structure
- name: Iot Twinmaker Delete Scene Response Structure
  property_count: 0
  slug: iot-twinmaker-delete-scene-response-structure
- name: Iot Twinmaker Delete Sync Job Request Structure
  property_count: 0
  slug: iot-twinmaker-delete-sync-job-request-structure
- name: Iot Twinmaker Delete Sync Job Response Structure
  property_count: 1
  slug: iot-twinmaker-delete-sync-job-response-structure
- name: Iot Twinmaker Delete Workspace Request Structure
  property_count: 0
  slug: iot-twinmaker-delete-workspace-request-structure
- name: Iot Twinmaker Delete Workspace Response Structure
  property_count: 0
  slug: iot-twinmaker-delete-workspace-response-structure
- name: Iot Twinmaker Entity Property Reference Structure
  property_count: 4
  slug: iot-twinmaker-entity-property-reference-structure
- name: Iot Twinmaker Entity Summaries Structure
  property_count: 0
  slug: iot-twinmaker-entity-summaries-structure
- name: Iot Twinmaker Entity Summary Structure
  property_count: 9
  slug: iot-twinmaker-entity-summary-structure
- name: Iot Twinmaker Entries Structure
  property_count: 0
  slug: iot-twinmaker-entries-structure
- name: Iot Twinmaker Error Code Structure
  property_count: 0
  slug: iot-twinmaker-error-code-structure
- name: Iot Twinmaker Error Details Structure
  property_count: 2
  slug: iot-twinmaker-error-details-structure
- name: Iot Twinmaker Error Entries Structure
  property_count: 0
  slug: iot-twinmaker-error-entries-structure
- name: Iot Twinmaker Errors Structure
  property_count: 0
  slug: iot-twinmaker-errors-structure
- name: Iot Twinmaker Execute Query Request Structure
  property_count: 4
  slug: iot-twinmaker-execute-query-request-structure
- name: Iot Twinmaker Execute Query Response Structure
  property_count: 3
  slug: iot-twinmaker-execute-query-response-structure
- name: Iot Twinmaker Extends From Structure
  property_count: 0
  slug: iot-twinmaker-extends-from-structure
- name: Iot Twinmaker External Id Property Structure
  property_count: 0
  slug: iot-twinmaker-external-id-property-structure
- name: Iot Twinmaker Function Request Structure
  property_count: 3
  slug: iot-twinmaker-function-request-structure
- name: Iot Twinmaker Function Response Structure
  property_count: 4
  slug: iot-twinmaker-function-response-structure
- name: Iot Twinmaker Functions Request Structure
  property_count: 0
  slug: iot-twinmaker-functions-request-structure
- name: Iot Twinmaker Functions Response Structure
  property_count: 0
  slug: iot-twinmaker-functions-response-structure
- name: Iot Twinmaker Generated Scene Metadata Map Structure
  property_count: 0
  slug: iot-twinmaker-generated-scene-metadata-map-structure
- name: Iot Twinmaker Get Component Type Request Structure
  property_count: 0
  slug: iot-twinmaker-get-component-type-request-structure
- name: Iot Twinmaker Get Component Type Response Structure
  property_count: 16
  slug: iot-twinmaker-get-component-type-response-structure
- name: Iot Twinmaker Get Entity Request Structure
  property_count: 0
  slug: iot-twinmaker-get-entity-request-structure
- name: Iot Twinmaker Get Entity Response Structure
  property_count: 12
  slug: iot-twinmaker-get-entity-response-structure
- name: Iot Twinmaker Get Pricing Plan Request Structure
  property_count: 0
  slug: iot-twinmaker-get-pricing-plan-request-structure
- name: Iot Twinmaker Get Pricing Plan Response Structure
  property_count: 2
  slug: iot-twinmaker-get-pricing-plan-response-structure
- name: Iot Twinmaker Get Property Value History Request Structure
  property_count: 13
  slug: iot-twinmaker-get-property-value-history-request-structure
- name: Iot Twinmaker Get Property Value History Response Structure
  property_count: 2
  slug: iot-twinmaker-get-property-value-history-response-structure
- name: Iot Twinmaker Get Property Value Request Structure
  property_count: 8
  slug: iot-twinmaker-get-property-value-request-structure
- name: Iot Twinmaker Get Property Value Response Structure
  property_count: 3
  slug: iot-twinmaker-get-property-value-response-structure
- name: Iot Twinmaker Get Scene Request Structure
  property_count: 0
  slug: iot-twinmaker-get-scene-request-structure
- name: Iot Twinmaker Get Scene Response Structure
  property_count: 11
  slug: iot-twinmaker-get-scene-response-structure
- name: Iot Twinmaker Get Sync Job Request Structure
  property_count: 0
  slug: iot-twinmaker-get-sync-job-request-structure
- name: Iot Twinmaker Get Sync Job Response Structure
  property_count: 7
  slug: iot-twinmaker-get-sync-job-response-structure
- name: Iot Twinmaker Get Workspace Request Structure
  property_count: 0
  slug: iot-twinmaker-get-workspace-request-structure
- name: Iot Twinmaker Get Workspace Response Structure
  property_count: 7
  slug: iot-twinmaker-get-workspace-response-structure
- name: Iot Twinmaker Group Type Structure
  property_count: 0
  slug: iot-twinmaker-group-type-structure
- name: Iot Twinmaker Interpolation Parameters Structure
  property_count: 2
  slug: iot-twinmaker-interpolation-parameters-structure
- name: Iot Twinmaker Interpolation Type Structure
  property_count: 0
  slug: iot-twinmaker-interpolation-type-structure
- name: Iot Twinmaker Lambda Function Structure
  property_count: 1
  slug: iot-twinmaker-lambda-function-structure
- name: Iot Twinmaker List Component Types Filter Structure
  property_count: 3
  slug: iot-twinmaker-list-component-types-filter-structure
- name: Iot Twinmaker List Component Types Filters Structure
  property_count: 0
  slug: iot-twinmaker-list-component-types-filters-structure
- name: Iot Twinmaker List Component Types Request Structure
  property_count: 3
  slug: iot-twinmaker-list-component-types-request-structure
- name: Iot Twinmaker List Component Types Response Structure
  property_count: 4
  slug: iot-twinmaker-list-component-types-response-structure
- name: Iot Twinmaker List Entities Filter Structure
  property_count: 3
  slug: iot-twinmaker-list-entities-filter-structure
- name: Iot Twinmaker List Entities Filters Structure
  property_count: 0
  slug: iot-twinmaker-list-entities-filters-structure
- name: Iot Twinmaker List Entities Request Structure
  property_count: 3
  slug: iot-twinmaker-list-entities-request-structure
- name: Iot Twinmaker List Entities Response Structure
  property_count: 2
  slug: iot-twinmaker-list-entities-response-structure
- name: Iot Twinmaker List Scenes Request Structure
  property_count: 2
  slug: iot-twinmaker-list-scenes-request-structure
- name: Iot Twinmaker List Scenes Response Structure
  property_count: 2
  slug: iot-twinmaker-list-scenes-response-structure
- name: Iot Twinmaker List Sync Jobs Request Structure
  property_count: 2
  slug: iot-twinmaker-list-sync-jobs-request-structure
- name: Iot Twinmaker List Sync Jobs Response Structure
  property_count: 2
  slug: iot-twinmaker-list-sync-jobs-response-structure
- name: Iot Twinmaker List Sync Resources Request Structure
  property_count: 3
  slug: iot-twinmaker-list-sync-resources-request-structure
- name: Iot Twinmaker List Sync Resources Response Structure
  property_count: 2
  slug: iot-twinmaker-list-sync-resources-response-structure
- name: Iot Twinmaker List Tags For Resource Request Structure
  property_count: 3
  slug: iot-twinmaker-list-tags-for-resource-request-structure
- name: Iot Twinmaker List Tags For Resource Response Structure
  property_count: 2
  slug: iot-twinmaker-list-tags-for-resource-response-structure
- name: Iot Twinmaker List Workspaces Request Structure
  property_count: 2
  slug: iot-twinmaker-list-workspaces-request-structure
- name: Iot Twinmaker List Workspaces Response Structure
  property_count: 2
  slug: iot-twinmaker-list-workspaces-response-structure
- name: Iot Twinmaker Order By List Structure
  property_count: 0
  slug: iot-twinmaker-order-by-list-structure
- name: Iot Twinmaker Order By Structure
  property_count: 2
  slug: iot-twinmaker-order-by-structure
- name: Iot Twinmaker Order By Time Structure
  property_count: 0
  slug: iot-twinmaker-order-by-time-structure
- name: Iot Twinmaker Order Structure
  property_count: 0
  slug: iot-twinmaker-order-structure
- name: Iot Twinmaker Parent Entity Update Request Structure
  property_count: 2
  slug: iot-twinmaker-parent-entity-update-request-structure
- name: Iot Twinmaker Parent Entity Update Type Structure
  property_count: 0
  slug: iot-twinmaker-parent-entity-update-type-structure
- name: Iot Twinmaker Pricing Bundles Structure
  property_count: 0
  slug: iot-twinmaker-pricing-bundles-structure
- name: Iot Twinmaker Pricing Mode Structure
  property_count: 0
  slug: iot-twinmaker-pricing-mode-structure
- name: Iot Twinmaker Pricing Plan Structure
  property_count: 6
  slug: iot-twinmaker-pricing-plan-structure
- name: Iot Twinmaker Pricing Tier Structure
  property_count: 0
  slug: iot-twinmaker-pricing-tier-structure
- name: Iot Twinmaker Property Definition Request Structure
  property_count: 8
  slug: iot-twinmaker-property-definition-request-structure
- name: Iot Twinmaker Property Definition Response Structure
  property_count: 11
  slug: iot-twinmaker-property-definition-response-structure
- name: Iot Twinmaker Property Definitions Request Structure
  property_count: 0
  slug: iot-twinmaker-property-definitions-request-structure
- name: Iot Twinmaker Property Definitions Response Structure
  property_count: 0
  slug: iot-twinmaker-property-definitions-response-structure
- name: Iot Twinmaker Property Filter Structure
  property_count: 3
  slug: iot-twinmaker-property-filter-structure
- name: Iot Twinmaker Property Filters Structure
  property_count: 0
  slug: iot-twinmaker-property-filters-structure
- name: Iot Twinmaker Property Group Request Structure
  property_count: 2
  slug: iot-twinmaker-property-group-request-structure
- name: Iot Twinmaker Property Group Response Structure
  property_count: 3
  slug: iot-twinmaker-property-group-response-structure
- name: Iot Twinmaker Property Group Update Type Structure
  property_count: 0
  slug: iot-twinmaker-property-group-update-type-structure
- name: Iot Twinmaker Property Groups Request Structure
  property_count: 0
  slug: iot-twinmaker-property-groups-request-structure
- name: Iot Twinmaker Property Groups Response Structure
  property_count: 0
  slug: iot-twinmaker-property-groups-response-structure
- name: Iot Twinmaker Property Latest Value Map Structure
  property_count: 0
  slug: iot-twinmaker-property-latest-value-map-structure
- name: Iot Twinmaker Property Latest Value Structure
  property_count: 2
  slug: iot-twinmaker-property-latest-value-structure
- name: Iot Twinmaker Property Names Structure
  property_count: 0
  slug: iot-twinmaker-property-names-structure
- name: Iot Twinmaker Property Request Structure
  property_count: 3
  slug: iot-twinmaker-property-request-structure
- name: Iot Twinmaker Property Requests Structure
  property_count: 0
  slug: iot-twinmaker-property-requests-structure
- name: Iot Twinmaker Property Response Structure
  property_count: 2
  slug: iot-twinmaker-property-response-structure
- name: Iot Twinmaker Property Responses Structure
  property_count: 0
  slug: iot-twinmaker-property-responses-structure
- name: Iot Twinmaker Property Table Value Structure
  property_count: 0
  slug: iot-twinmaker-property-table-value-structure
- name: Iot Twinmaker Property Update Type Structure
  property_count: 0
  slug: iot-twinmaker-property-update-type-structure
- name: Iot Twinmaker Property Value Entry Structure
  property_count: 2
  slug: iot-twinmaker-property-value-entry-structure
- name: Iot Twinmaker Property Value History Structure
  property_count: 2
  slug: iot-twinmaker-property-value-history-structure
- name: Iot Twinmaker Property Value List Structure
  property_count: 0
  slug: iot-twinmaker-property-value-list-structure
- name: Iot Twinmaker Property Value Structure
  property_count: 3
  slug: iot-twinmaker-property-value-structure
- name: Iot Twinmaker Property Values Structure
  property_count: 0
  slug: iot-twinmaker-property-values-structure
- name: Iot Twinmaker Query Result Value Structure
  property_count: 0
  slug: iot-twinmaker-query-result-value-structure
- name: Iot Twinmaker Relationship Structure
  property_count: 2
  slug: iot-twinmaker-relationship-structure
- name: Iot Twinmaker Relationship Value Structure
  property_count: 2
  slug: iot-twinmaker-relationship-value-structure
- name: Iot Twinmaker Required Properties Structure
  property_count: 0
  slug: iot-twinmaker-required-properties-structure
- name: Iot Twinmaker Row Data Structure
  property_count: 0
  slug: iot-twinmaker-row-data-structure
- name: Iot Twinmaker Row Structure
  property_count: 1
  slug: iot-twinmaker-row-structure
- name: Iot Twinmaker Rows Structure
  property_count: 0
  slug: iot-twinmaker-rows-structure
- name: Iot Twinmaker Scene Capabilities Structure
  property_count: 0
  slug: iot-twinmaker-scene-capabilities-structure
- name: Iot Twinmaker Scene Error Code Structure
  property_count: 0
  slug: iot-twinmaker-scene-error-code-structure
- name: Iot Twinmaker Scene Error Structure
  property_count: 2
  slug: iot-twinmaker-scene-error-structure
- name: Iot Twinmaker Scene Metadata Map Structure
  property_count: 0
  slug: iot-twinmaker-scene-metadata-map-structure
- name: Iot Twinmaker Scene Summaries Structure
  property_count: 0
  slug: iot-twinmaker-scene-summaries-structure
- name: Iot Twinmaker Scene Summary Structure
  property_count: 6
  slug: iot-twinmaker-scene-summary-structure
- name: Iot Twinmaker Scope Structure
  property_count: 0
  slug: iot-twinmaker-scope-structure
- name: Iot Twinmaker Selected Property List Structure
  property_count: 0
  slug: iot-twinmaker-selected-property-list-structure
- name: Iot Twinmaker State Structure
  property_count: 0
  slug: iot-twinmaker-state-structure
- name: Iot Twinmaker Status Structure
  property_count: 2
  slug: iot-twinmaker-status-structure
- name: Iot Twinmaker Sync Job State Structure
  property_count: 0
  slug: iot-twinmaker-sync-job-state-structure
- name: Iot Twinmaker Sync Job Status Structure
  property_count: 2
  slug: iot-twinmaker-sync-job-status-structure
- name: Iot Twinmaker Sync Job Summaries Structure
  property_count: 0
  slug: iot-twinmaker-sync-job-summaries-structure
- name: Iot Twinmaker Sync Job Summary Structure
  property_count: 6
  slug: iot-twinmaker-sync-job-summary-structure
- name: Iot Twinmaker Sync Resource Filter Structure
  property_count: 4
  slug: iot-twinmaker-sync-resource-filter-structure
- name: Iot Twinmaker Sync Resource Filters Structure
  property_count: 0
  slug: iot-twinmaker-sync-resource-filters-structure
- name: Iot Twinmaker Sync Resource State Structure
  property_count: 0
  slug: iot-twinmaker-sync-resource-state-structure
- name: Iot Twinmaker Sync Resource Status Structure
  property_count: 2
  slug: iot-twinmaker-sync-resource-status-structure
- name: Iot Twinmaker Sync Resource Summaries Structure
  property_count: 0
  slug: iot-twinmaker-sync-resource-summaries-structure
- name: Iot Twinmaker Sync Resource Summary Structure
  property_count: 5
  slug: iot-twinmaker-sync-resource-summary-structure
- name: Iot Twinmaker Sync Resource Type Structure
  property_count: 0
  slug: iot-twinmaker-sync-resource-type-structure
- name: Iot Twinmaker Tabular Conditions Structure
  property_count: 2
  slug: iot-twinmaker-tabular-conditions-structure
- name: Iot Twinmaker Tabular Property Value Structure
  property_count: 0
  slug: iot-twinmaker-tabular-property-value-structure
- name: Iot Twinmaker Tabular Property Values Structure
  property_count: 0
  slug: iot-twinmaker-tabular-property-values-structure
- name: Iot Twinmaker Tag Key List Structure
  property_count: 0
  slug: iot-twinmaker-tag-key-list-structure
- name: Iot Twinmaker Tag Map Structure
  property_count: 0
  slug: iot-twinmaker-tag-map-structure
- name: Iot Twinmaker Tag Resource Request Structure
  property_count: 2
  slug: iot-twinmaker-tag-resource-request-structure
- name: Iot Twinmaker Tag Resource Response Structure
  property_count: 0
  slug: iot-twinmaker-tag-resource-response-structure
- name: Iot Twinmaker Type Structure
  property_count: 0
  slug: iot-twinmaker-type-structure
- name: Iot Twinmaker Untag Resource Request Structure
  property_count: 0
  slug: iot-twinmaker-untag-resource-request-structure
- name: Iot Twinmaker Untag Resource Response Structure
  property_count: 0
  slug: iot-twinmaker-untag-resource-response-structure
- name: Iot Twinmaker Update Component Type Request Structure
  property_count: 7
  slug: iot-twinmaker-update-component-type-request-structure
- name: Iot Twinmaker Update Component Type Response Structure
  property_count: 4
  slug: iot-twinmaker-update-component-type-response-structure
- name: Iot Twinmaker Update Entity Request Structure
  property_count: 4
  slug: iot-twinmaker-update-entity-request-structure
- name: Iot Twinmaker Update Entity Response Structure
  property_count: 2
  slug: iot-twinmaker-update-entity-response-structure
- name: Iot Twinmaker Update Pricing Plan Request Structure
  property_count: 2
  slug: iot-twinmaker-update-pricing-plan-request-structure
- name: Iot Twinmaker Update Pricing Plan Response Structure
  property_count: 2
  slug: iot-twinmaker-update-pricing-plan-response-structure
- name: Iot Twinmaker Update Reason Structure
  property_count: 0
  slug: iot-twinmaker-update-reason-structure
- name: Iot Twinmaker Update Scene Request Structure
  property_count: 4
  slug: iot-twinmaker-update-scene-request-structure
- name: Iot Twinmaker Update Scene Response Structure
  property_count: 1
  slug: iot-twinmaker-update-scene-response-structure
- name: Iot Twinmaker Update Workspace Request Structure
  property_count: 2
  slug: iot-twinmaker-update-workspace-request-structure
- name: Iot Twinmaker Update Workspace Response Structure
  property_count: 1
  slug: iot-twinmaker-update-workspace-response-structure
- name: Iot Twinmaker Values Structure
  property_count: 0
  slug: iot-twinmaker-values-structure
- name: Iot Twinmaker Workspace Summaries Structure
  property_count: 0
  slug: iot-twinmaker-workspace-summaries-structure
- name: Iot Twinmaker Workspace Summary Structure
  property_count: 5
  slug: iot-twinmaker-workspace-summary-structure
jsonld:
- class_count: 102
  name: Amazon Iot Twinmaker Context
  property_count: 137
  slug: amazon-iot-twinmaker-context
layout: provider
modified: '2026-05-19'
name: Amazon IoT TwinMaker
nav: Providers
network: true
overview: 'Amazon IoT TwinMaker publishes 8 APIs on the [APIs.io](https://apis.io/) network, including Pricingplan API, Queries API, Sync Jobs API, and 5 more. Tagged areas include 3D Visualization, Digital Twin, Industrial IoT, and IoT.


  The Amazon IoT TwinMaker catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon IoT TwinMaker''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 15 more developer resources.'
plans:
- name: Amazon Iot Twinmaker Plans Pricing
  plan_count: 3
  slug: amazon-iot-twinmaker-plans-pricing
random_paper: 9
rate_limits:
- limit_count: 5
  name: Amazon Iot Twinmaker Rate Limits
  slug: amazon-iot-twinmaker-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon IoT TwinMaker API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-iot-twinmaker-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Amazon IoT TwinMaker API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 10
  slug: amazon-iot-twinmaker-spectral-rules
score:
  band: developing
  composite: 53.1
  coverage:
    artifact_dirs: 17
    catalog_earned: 61.5
    catalog_earned_first_party: 0.0
    catalog_gap: 53.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 65.1
    developer_ergonomics: 58.3
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 53.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.18.3
  scored_at: '2026-09-05'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-iot-twinmaker/refs/heads/main/screenshots/amazon-iot-twinmaker-2026-06-20T171712.png
security:
- kind: authentication
  name: Amazon Iot Twinmaker Authentication
  slug: amazon-iot-twinmaker-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Iot Twinmaker Domain Security
  slug: amazon-iot-twinmaker-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Iot Twinmaker Vulnerability Disclosure
  slug: amazon-iot-twinmaker-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Iot Twinmaker Trust Center
  slug: amazon-iot-twinmaker-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-iot-twinmaker
tags:
- 3D Visualization
- Digital Twin
- Industrial IoT
- IoT
use_cases:
- description: Create digital twins of buildings for energy optimization and maintenance.
  name: Smart Building Management
- description: Visualize production lines and equipment in 3D for operators.
  name: Factory Digital Twin
- description: Enable remote monitoring and diagnosis of industrial equipment.
  name: Remote Operations
website: https://aws.amazon.com/iot-twinmaker/
---

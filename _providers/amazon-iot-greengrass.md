---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
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
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 36.3
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 14
  human_in_the_loop: 0
  name: Amazon Iot Greengrass Agentic Access
  operation_count: 29
  slug: amazon-iot-greengrass-agentic-access
  summary_line: 29 operations · 14 acting
api_count: 1
apis:
- description: The Greengrass API from Amazon IoT Greengrass — 19 operation(s) for greengrass.
  name: Amazon IoT Greengrass Greengrass API
  slug: amazon-iot-greengrass-greengrass-api
- description: The Tags API from Amazon IoT Greengrass — 2 operation(s) for tags.
  name: Amazon IoT Greengrass Tags API
  slug: amazon-iot-greengrass-tags-api
artifact_total: 445
collections:
- collection_type: postman
  name: AWS IoT V2 Greengrass API
  slug: postman-amazon-iot-greengrass-greengrass-api
- collection_type: postman
  name: AWS IoT V2 Greengrass Tags API
  slug: postman-amazon-iot-greengrass-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: AWS IoT V2 Greengrass API
  slug: open-amazon-iot-greengrass-greengrass-api
- collection_type: open
  name: AWS IoT V2 Greengrass Tags API
  slug: open-amazon-iot-greengrass-tags-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-iot-greengrass/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-iot-greengrass-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-iot-greengrass-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-iot-greengrass-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-iot-greengrass-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-iot-greengrass-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/greengrass/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/greengrass/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/greengrass/v2/developerguide/
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
  url: https://aws.amazon.com/blogs/iot/tag/aws-iot-greengrass/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/greengrass/
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
  url: rules/amazon-iot-greengrass-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-iot-greengrass-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-iot-greengrass-context.jsonld
created: '2026-03-16'
description: AWS IoT Greengrass extends AWS compute, messaging, data management, sync, and ML inference capabilities to edge devices so they can act locally on the data they generate, while still using the cloud for management, analytics, and durable storage.
examples:
- key_count: 1
  name: Iot Greengrass Associate Client Device With Core Device Entry Example
  slug: iot-greengrass-associate-client-device-with-core-device-entry-example
- key_count: 0
  name: Iot Greengrass Associate Client Device With Core Device Entry List Example
  slug: iot-greengrass-associate-client-device-with-core-device-entry-list-example
- key_count: 3
  name: Iot Greengrass Associate Client Device With Core Device Error Entry Example
  slug: iot-greengrass-associate-client-device-with-core-device-error-entry-example
- key_count: 0
  name: Iot Greengrass Associate Client Device With Core Device Error List Example
  slug: iot-greengrass-associate-client-device-with-core-device-error-list-example
- key_count: 1
  name: Iot Greengrass Associate Service Role To Account Request Example
  slug: iot-greengrass-associate-service-role-to-account-request-example
- key_count: 1
  name: Iot Greengrass Associate Service Role To Account Response Example
  slug: iot-greengrass-associate-service-role-to-account-response-example
- key_count: 2
  name: Iot Greengrass Associated Client Device Example
  slug: iot-greengrass-associated-client-device-example
- key_count: 0
  name: Iot Greengrass Associated Client Device List Example
  slug: iot-greengrass-associated-client-device-list-example
- key_count: 1
  name: Iot Greengrass Batch Associate Client Device With Core Device Request Example
  slug: iot-greengrass-batch-associate-client-device-with-core-device-request-example
- key_count: 1
  name: Iot Greengrass Batch Associate Client Device With Core Device Response Example
  slug: iot-greengrass-batch-associate-client-device-with-core-device-response-example
- key_count: 1
  name: Iot Greengrass Batch Disassociate Client Device From Core Device Request Example
  slug: iot-greengrass-batch-disassociate-client-device-from-core-device-request-example
- key_count: 1
  name: Iot Greengrass Batch Disassociate Client Device From Core Device Response Example
  slug: iot-greengrass-batch-disassociate-client-device-from-core-device-response-example
- key_count: 0
  name: Iot Greengrass Cancel Deployment Request Example
  slug: iot-greengrass-cancel-deployment-request-example
- key_count: 1
  name: Iot Greengrass Cancel Deployment Response Example
  slug: iot-greengrass-cancel-deployment-response-example
- key_count: 5
  name: Iot Greengrass Cloud Component Status Example
  slug: iot-greengrass-cloud-component-status-example
- key_count: 3
  name: Iot Greengrass Component Candidate Example
  slug: iot-greengrass-component-candidate-example
- key_count: 0
  name: Iot Greengrass Component Candidate List Example
  slug: iot-greengrass-component-candidate-list-example
- key_count: 0
  name: Iot Greengrass Component Configuration Path List Example
  slug: iot-greengrass-component-configuration-path-list-example
- key_count: 2
  name: Iot Greengrass Component Configuration Update Example
  slug: iot-greengrass-component-configuration-update-example
- key_count: 0
  name: Iot Greengrass Component Dependency Map Example
  slug: iot-greengrass-component-dependency-map-example
- key_count: 2
  name: Iot Greengrass Component Dependency Requirement Example
  slug: iot-greengrass-component-dependency-requirement-example
- key_count: 3
  name: Iot Greengrass Component Deployment Specification Example
  slug: iot-greengrass-component-deployment-specification-example
- key_count: 0
  name: Iot Greengrass Component Deployment Specifications Example
  slug: iot-greengrass-component-deployment-specifications-example
- key_count: 3
  name: Iot Greengrass Component Example
  slug: iot-greengrass-component-example
- key_count: 6
  name: Iot Greengrass Component Latest Version Example
  slug: iot-greengrass-component-latest-version-example
- key_count: 0
  name: Iot Greengrass Component List Example
  slug: iot-greengrass-component-list-example
- key_count: 2
  name: Iot Greengrass Component Platform Example
  slug: iot-greengrass-component-platform-example
- key_count: 0
  name: Iot Greengrass Component Platform List Example
  slug: iot-greengrass-component-platform-list-example
- key_count: 3
  name: Iot Greengrass Component Run With Example
  slug: iot-greengrass-component-run-with-example
- key_count: 0
  name: Iot Greengrass Component Version List Example
  slug: iot-greengrass-component-version-list-example
- key_count: 3
  name: Iot Greengrass Component Version List Item Example
  slug: iot-greengrass-component-version-list-item-example
- key_count: 0
  name: Iot Greengrass Component Version Requirement Map Example
  slug: iot-greengrass-component-version-requirement-map-example
- key_count: 4
  name: Iot Greengrass Connectivity Info Example
  slug: iot-greengrass-connectivity-info-example
- key_count: 0
  name: Iot Greengrass Connectivity Info List Example
  slug: iot-greengrass-connectivity-info-list-example
- key_count: 3
  name: Iot Greengrass Core Device Example
  slug: iot-greengrass-core-device-example
- key_count: 0
  name: Iot Greengrass Core Devices List Example
  slug: iot-greengrass-core-devices-list-example
- key_count: 4
  name: Iot Greengrass Create Component Version Request Example
  slug: iot-greengrass-create-component-version-request-example
- key_count: 5
  name: Iot Greengrass Create Component Version Response Example
  slug: iot-greengrass-create-component-version-response-example
- key_count: 8
  name: Iot Greengrass Create Deployment Request Example
  slug: iot-greengrass-create-deployment-request-example
- key_count: 3
  name: Iot Greengrass Create Deployment Response Example
  slug: iot-greengrass-create-deployment-response-example
- key_count: 0
  name: Iot Greengrass Delete Component Request Example
  slug: iot-greengrass-delete-component-request-example
- key_count: 0
  name: Iot Greengrass Delete Core Device Request Example
  slug: iot-greengrass-delete-core-device-request-example
- key_count: 0
  name: Iot Greengrass Delete Deployment Request Example
  slug: iot-greengrass-delete-deployment-request-example
- key_count: 2
  name: Iot Greengrass Deployment Component Update Policy Example
  slug: iot-greengrass-deployment-component-update-policy-example
- key_count: 1
  name: Iot Greengrass Deployment Configuration Validation Policy Example
  slug: iot-greengrass-deployment-configuration-validation-policy-example
- key_count: 8
  name: Iot Greengrass Deployment Example
  slug: iot-greengrass-deployment-example
- key_count: 3
  name: Iot Greengrass Deployment Io T Job Configuration Example
  slug: iot-greengrass-deployment-io-t-job-configuration-example
- key_count: 0
  name: Iot Greengrass Deployment List Example
  slug: iot-greengrass-deployment-list-example
- key_count: 3
  name: Iot Greengrass Deployment Policies Example
  slug: iot-greengrass-deployment-policies-example
- key_count: 0
  name: Iot Greengrass Describe Component Request Example
  slug: iot-greengrass-describe-component-request-example
- key_count: 9
  name: Iot Greengrass Describe Component Response Example
  slug: iot-greengrass-describe-component-response-example
- key_count: 1
  name: Iot Greengrass Disassociate Client Device From Core Device Entry Example
  slug: iot-greengrass-disassociate-client-device-from-core-device-entry-example
- key_count: 0
  name: Iot Greengrass Disassociate Client Device From Core Device Entry List Example
  slug: iot-greengrass-disassociate-client-device-from-core-device-entry-list-example
- key_count: 3
  name: Iot Greengrass Disassociate Client Device From Core Device Error Entry Example
  slug: iot-greengrass-disassociate-client-device-from-core-device-error-entry-example
- key_count: 0
  name: Iot Greengrass Disassociate Client Device From Core Device Error List Example
  slug: iot-greengrass-disassociate-client-device-from-core-device-error-list-example
- key_count: 0
  name: Iot Greengrass Disassociate Service Role From Account Request Example
  slug: iot-greengrass-disassociate-service-role-from-account-request-example
- key_count: 1
  name: Iot Greengrass Disassociate Service Role From Account Response Example
  slug: iot-greengrass-disassociate-service-role-from-account-response-example
- key_count: 0
  name: Iot Greengrass Effective Deployment Error Stack Example
  slug: iot-greengrass-effective-deployment-error-stack-example
- key_count: 0
  name: Iot Greengrass Effective Deployment Error Type List Example
  slug: iot-greengrass-effective-deployment-error-type-list-example
- key_count: 11
  name: Iot Greengrass Effective Deployment Example
  slug: iot-greengrass-effective-deployment-example
- key_count: 2
  name: Iot Greengrass Effective Deployment Status Details Example
  slug: iot-greengrass-effective-deployment-status-details-example
- key_count: 0
  name: Iot Greengrass Effective Deployments List Example
  slug: iot-greengrass-effective-deployments-list-example
- key_count: 0
  name: Iot Greengrass Get Component Request Example
  slug: iot-greengrass-get-component-request-example
- key_count: 3
  name: Iot Greengrass Get Component Response Example
  slug: iot-greengrass-get-component-response-example
- key_count: 0
  name: Iot Greengrass Get Component Version Artifact Request Example
  slug: iot-greengrass-get-component-version-artifact-request-example
- key_count: 1
  name: Iot Greengrass Get Component Version Artifact Response Example
  slug: iot-greengrass-get-component-version-artifact-response-example
- key_count: 0
  name: Iot Greengrass Get Connectivity Info Request Example
  slug: iot-greengrass-get-connectivity-info-request-example
- key_count: 2
  name: Iot Greengrass Get Connectivity Info Response Example
  slug: iot-greengrass-get-connectivity-info-response-example
- key_count: 0
  name: Iot Greengrass Get Core Device Request Example
  slug: iot-greengrass-get-core-device-request-example
- key_count: 7
  name: Iot Greengrass Get Core Device Response Example
  slug: iot-greengrass-get-core-device-response-example
- key_count: 0
  name: Iot Greengrass Get Deployment Request Example
  slug: iot-greengrass-get-deployment-request-example
- key_count: 14
  name: Iot Greengrass Get Deployment Response Example
  slug: iot-greengrass-get-deployment-response-example
- key_count: 0
  name: Iot Greengrass Get Service Role For Account Request Example
  slug: iot-greengrass-get-service-role-for-account-request-example
- key_count: 2
  name: Iot Greengrass Get Service Role For Account Response Example
  slug: iot-greengrass-get-service-role-for-account-response-example
- key_count: 9
  name: Iot Greengrass Installed Component Example
  slug: iot-greengrass-installed-component-example
- key_count: 0
  name: Iot Greengrass Installed Component Lifecycle Status Code List Example
  slug: iot-greengrass-installed-component-lifecycle-status-code-list-example
- key_count: 0
  name: Iot Greengrass Installed Component List Example
  slug: iot-greengrass-installed-component-list-example
- key_count: 1
  name: Iot Greengrass Io T Job Abort Config Example
  slug: iot-greengrass-io-t-job-abort-config-example
- key_count: 4
  name: Iot Greengrass Io T Job Abort Criteria Example
  slug: iot-greengrass-io-t-job-abort-criteria-example
- key_count: 0
  name: Iot Greengrass Io T Job Abort Criteria List Example
  slug: iot-greengrass-io-t-job-abort-criteria-list-example
- key_count: 2
  name: Iot Greengrass Io T Job Executions Rollout Config Example
  slug: iot-greengrass-io-t-job-executions-rollout-config-example
- key_count: 3
  name: Iot Greengrass Io T Job Exponential Rollout Rate Example
  slug: iot-greengrass-io-t-job-exponential-rollout-rate-example
- key_count: 2
  name: Iot Greengrass Io T Job Rate Increase Criteria Example
  slug: iot-greengrass-io-t-job-rate-increase-criteria-example
- key_count: 1
  name: Iot Greengrass Io T Job Timeout Config Example
  slug: iot-greengrass-io-t-job-timeout-config-example
- key_count: 4
  name: Iot Greengrass Lambda Container Params Example
  slug: iot-greengrass-lambda-container-params-example
- key_count: 0
  name: Iot Greengrass Lambda Device List Example
  slug: iot-greengrass-lambda-device-list-example
- key_count: 3
  name: Iot Greengrass Lambda Device Mount Example
  slug: iot-greengrass-lambda-device-mount-example
- key_count: 0
  name: Iot Greengrass Lambda Environment Variables Example
  slug: iot-greengrass-lambda-environment-variables-example
- key_count: 2
  name: Iot Greengrass Lambda Event Source Example
  slug: iot-greengrass-lambda-event-source-example
- key_count: 0
  name: Iot Greengrass Lambda Event Source List Example
  slug: iot-greengrass-lambda-event-source-list-example
- key_count: 0
  name: Iot Greengrass Lambda Exec Args List Example
  slug: iot-greengrass-lambda-exec-args-list-example
- key_count: 11
  name: Iot Greengrass Lambda Execution Parameters Example
  slug: iot-greengrass-lambda-execution-parameters-example
- key_count: 6
  name: Iot Greengrass Lambda Function Recipe Source Example
  slug: iot-greengrass-lambda-function-recipe-source-example
- key_count: 2
  name: Iot Greengrass Lambda Linux Process Params Example
  slug: iot-greengrass-lambda-linux-process-params-example
- key_count: 0
  name: Iot Greengrass Lambda Volume List Example
  slug: iot-greengrass-lambda-volume-list-example
- key_count: 4
  name: Iot Greengrass Lambda Volume Mount Example
  slug: iot-greengrass-lambda-volume-mount-example
- key_count: 0
  name: Iot Greengrass List Client Devices Associated With Core Device Request Example
  slug: iot-greengrass-list-client-devices-associated-with-core-device-request-example
- key_count: 2
  name: Iot Greengrass List Client Devices Associated With Core Device Response Example
  slug: iot-greengrass-list-client-devices-associated-with-core-device-response-example
- key_count: 0
  name: Iot Greengrass List Component Versions Request Example
  slug: iot-greengrass-list-component-versions-request-example
- key_count: 2
  name: Iot Greengrass List Component Versions Response Example
  slug: iot-greengrass-list-component-versions-response-example
- key_count: 0
  name: Iot Greengrass List Components Request Example
  slug: iot-greengrass-list-components-request-example
- key_count: 2
  name: Iot Greengrass List Components Response Example
  slug: iot-greengrass-list-components-response-example
- key_count: 0
  name: Iot Greengrass List Core Devices Request Example
  slug: iot-greengrass-list-core-devices-request-example
- key_count: 2
  name: Iot Greengrass List Core Devices Response Example
  slug: iot-greengrass-list-core-devices-response-example
- key_count: 0
  name: Iot Greengrass List Deployments Request Example
  slug: iot-greengrass-list-deployments-request-example
- key_count: 2
  name: Iot Greengrass List Deployments Response Example
  slug: iot-greengrass-list-deployments-response-example
- key_count: 0
  name: Iot Greengrass List Effective Deployments Request Example
  slug: iot-greengrass-list-effective-deployments-request-example
- key_count: 2
  name: Iot Greengrass List Effective Deployments Response Example
  slug: iot-greengrass-list-effective-deployments-response-example
- key_count: 0
  name: Iot Greengrass List Installed Components Request Example
  slug: iot-greengrass-list-installed-components-request-example
- key_count: 2
  name: Iot Greengrass List Installed Components Response Example
  slug: iot-greengrass-list-installed-components-response-example
- key_count: 0
  name: Iot Greengrass List Tags For Resource Request Example
  slug: iot-greengrass-list-tags-for-resource-request-example
- key_count: 1
  name: Iot Greengrass List Tags For Resource Response Example
  slug: iot-greengrass-list-tags-for-resource-response-example
- key_count: 0
  name: Iot Greengrass Platform Attributes Map Example
  slug: iot-greengrass-platform-attributes-map-example
- key_count: 2
  name: Iot Greengrass Resolve Component Candidates Request Example
  slug: iot-greengrass-resolve-component-candidates-request-example
- key_count: 1
  name: Iot Greengrass Resolve Component Candidates Response Example
  slug: iot-greengrass-resolve-component-candidates-response-example
- key_count: 6
  name: Iot Greengrass Resolved Component Version Example
  slug: iot-greengrass-resolved-component-version-example
- key_count: 0
  name: Iot Greengrass Resolved Component Versions List Example
  slug: iot-greengrass-resolved-component-versions-list-example
- key_count: 0
  name: Iot Greengrass String Map Example
  slug: iot-greengrass-string-map-example
- key_count: 2
  name: Iot Greengrass System Resource Limits Example
  slug: iot-greengrass-system-resource-limits-example
- key_count: 0
  name: Iot Greengrass Tag Key List Example
  slug: iot-greengrass-tag-key-list-example
- key_count: 0
  name: Iot Greengrass Tag Map Example
  slug: iot-greengrass-tag-map-example
- key_count: 1
  name: Iot Greengrass Tag Resource Request Example
  slug: iot-greengrass-tag-resource-request-example
- key_count: 0
  name: Iot Greengrass Tag Resource Response Example
  slug: iot-greengrass-tag-resource-response-example
- key_count: 0
  name: Iot Greengrass Untag Resource Request Example
  slug: iot-greengrass-untag-resource-request-example
- key_count: 0
  name: Iot Greengrass Untag Resource Response Example
  slug: iot-greengrass-untag-resource-response-example
- key_count: 1
  name: Iot Greengrass Update Connectivity Info Request Example
  slug: iot-greengrass-update-connectivity-info-request-example
- key_count: 2
  name: Iot Greengrass Update Connectivity Info Response Example
  slug: iot-greengrass-update-connectivity-info-response-example
features:
- description: Run Lambda functions and containers on edge devices with local compute.
  name: Edge Computing
- description: Deploy reusable software components to edge devices from a component catalog.
  name: Component System
- description: Run machine learning inference locally with SageMaker model deployment.
  name: Local ML Inference
- description: Deploy and update software components to thousands of edge devices.
  name: Deployment Management
- description: Enable MQTT messaging between local IoT devices without cloud round-trips.
  name: Local Messaging
finops:
- name: Amazon Iot Greengrass Finops
  service_category: API
  slug: amazon-iot-greengrass-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-iot-greengrass.png
json_schemas:
- name: AssociateClientDeviceWithCoreDeviceEntryList
  property_count: 0
  slug: iot-greengrass-associate-client-device-with-core-device-entry-list
- name: AssociateClientDeviceWithCoreDeviceEntry
  property_count: 1
  slug: iot-greengrass-associate-client-device-with-core-device-entry
- name: AssociateClientDeviceWithCoreDeviceErrorEntry
  property_count: 3
  slug: iot-greengrass-associate-client-device-with-core-device-error-entry
- name: AssociateClientDeviceWithCoreDeviceErrorList
  property_count: 0
  slug: iot-greengrass-associate-client-device-with-core-device-error-list
- name: AssociateServiceRoleToAccountRequest
  property_count: 1
  slug: iot-greengrass-associate-service-role-to-account-request
- name: AssociateServiceRoleToAccountResponse
  property_count: 1
  slug: iot-greengrass-associate-service-role-to-account-response
- name: AssociatedClientDeviceList
  property_count: 0
  slug: iot-greengrass-associated-client-device-list
- name: AssociatedClientDevice
  property_count: 2
  slug: iot-greengrass-associated-client-device
- name: BatchAssociateClientDeviceWithCoreDeviceRequest
  property_count: 1
  slug: iot-greengrass-batch-associate-client-device-with-core-device-request
- name: BatchAssociateClientDeviceWithCoreDeviceResponse
  property_count: 1
  slug: iot-greengrass-batch-associate-client-device-with-core-device-response
- name: BatchDisassociateClientDeviceFromCoreDeviceRequest
  property_count: 1
  slug: iot-greengrass-batch-disassociate-client-device-from-core-device-request
- name: BatchDisassociateClientDeviceFromCoreDeviceResponse
  property_count: 1
  slug: iot-greengrass-batch-disassociate-client-device-from-core-device-response
- name: CancelDeploymentRequest
  property_count: 0
  slug: iot-greengrass-cancel-deployment-request
- name: CancelDeploymentResponse
  property_count: 1
  slug: iot-greengrass-cancel-deployment-response
- name: CloudComponentState
  property_count: 0
  slug: iot-greengrass-cloud-component-state
- name: CloudComponentStatus
  property_count: 5
  slug: iot-greengrass-cloud-component-status
- name: ComponentCandidateList
  property_count: 0
  slug: iot-greengrass-component-candidate-list
- name: ComponentCandidate
  property_count: 3
  slug: iot-greengrass-component-candidate
- name: ComponentConfigurationPathList
  property_count: 0
  slug: iot-greengrass-component-configuration-path-list
- name: ComponentConfigurationUpdate
  property_count: 2
  slug: iot-greengrass-component-configuration-update
- name: ComponentDependencyMap
  property_count: 0
  slug: iot-greengrass-component-dependency-map
- name: ComponentDependencyRequirement
  property_count: 2
  slug: iot-greengrass-component-dependency-requirement
- name: ComponentDependencyType
  property_count: 0
  slug: iot-greengrass-component-dependency-type
- name: ComponentDeploymentSpecification
  property_count: 3
  slug: iot-greengrass-component-deployment-specification
- name: ComponentDeploymentSpecifications
  property_count: 0
  slug: iot-greengrass-component-deployment-specifications
- name: ComponentLatestVersion
  property_count: 6
  slug: iot-greengrass-component-latest-version
- name: ComponentList
  property_count: 0
  slug: iot-greengrass-component-list
- name: ComponentPlatformList
  property_count: 0
  slug: iot-greengrass-component-platform-list
- name: ComponentPlatform
  property_count: 2
  slug: iot-greengrass-component-platform
- name: ComponentRunWith
  property_count: 3
  slug: iot-greengrass-component-run-with
- name: Component
  property_count: 3
  slug: iot-greengrass-component
- name: ComponentVersionListItem
  property_count: 3
  slug: iot-greengrass-component-version-list-item
- name: ComponentVersionList
  property_count: 0
  slug: iot-greengrass-component-version-list
- name: ComponentVersionRequirementMap
  property_count: 0
  slug: iot-greengrass-component-version-requirement-map
- name: ComponentVisibilityScope
  property_count: 0
  slug: iot-greengrass-component-visibility-scope
- name: connectivityInfoList
  property_count: 0
  slug: iot-greengrass-connectivity-info-list
- name: ConnectivityInfo
  property_count: 4
  slug: iot-greengrass-connectivity-info
- name: CoreDevice
  property_count: 3
  slug: iot-greengrass-core-device
- name: CoreDeviceStatus
  property_count: 0
  slug: iot-greengrass-core-device-status
- name: CoreDevicesList
  property_count: 0
  slug: iot-greengrass-core-devices-list
- name: CreateComponentVersionRequest
  property_count: 4
  slug: iot-greengrass-create-component-version-request
- name: CreateComponentVersionResponse
  property_count: 5
  slug: iot-greengrass-create-component-version-response
- name: CreateDeploymentRequest
  property_count: 8
  slug: iot-greengrass-create-deployment-request
- name: CreateDeploymentResponse
  property_count: 3
  slug: iot-greengrass-create-deployment-response
- name: DeleteComponentRequest
  property_count: 0
  slug: iot-greengrass-delete-component-request
- name: DeleteCoreDeviceRequest
  property_count: 0
  slug: iot-greengrass-delete-core-device-request
- name: DeleteDeploymentRequest
  property_count: 0
  slug: iot-greengrass-delete-deployment-request
- name: DeploymentComponentUpdatePolicyAction
  property_count: 0
  slug: iot-greengrass-deployment-component-update-policy-action
- name: DeploymentComponentUpdatePolicy
  property_count: 2
  slug: iot-greengrass-deployment-component-update-policy
- name: DeploymentConfigurationValidationPolicy
  property_count: 1
  slug: iot-greengrass-deployment-configuration-validation-policy
- name: DeploymentFailureHandlingPolicy
  property_count: 0
  slug: iot-greengrass-deployment-failure-handling-policy
- name: DeploymentHistoryFilter
  property_count: 0
  slug: iot-greengrass-deployment-history-filter
- name: DeploymentIoTJobConfiguration
  property_count: 3
  slug: iot-greengrass-deployment-io-t-job-configuration
- name: DeploymentList
  property_count: 0
  slug: iot-greengrass-deployment-list
- name: DeploymentPolicies
  property_count: 3
  slug: iot-greengrass-deployment-policies
- name: Deployment
  property_count: 8
  slug: iot-greengrass-deployment
- name: DeploymentStatus
  property_count: 0
  slug: iot-greengrass-deployment-status
- name: DescribeComponentRequest
  property_count: 0
  slug: iot-greengrass-describe-component-request
- name: DescribeComponentResponse
  property_count: 9
  slug: iot-greengrass-describe-component-response
- name: DisassociateClientDeviceFromCoreDeviceEntryList
  property_count: 0
  slug: iot-greengrass-disassociate-client-device-from-core-device-entry-list
- name: DisassociateClientDeviceFromCoreDeviceEntry
  property_count: 1
  slug: iot-greengrass-disassociate-client-device-from-core-device-entry
- name: DisassociateClientDeviceFromCoreDeviceErrorEntry
  property_count: 3
  slug: iot-greengrass-disassociate-client-device-from-core-device-error-entry
- name: DisassociateClientDeviceFromCoreDeviceErrorList
  property_count: 0
  slug: iot-greengrass-disassociate-client-device-from-core-device-error-list
- name: DisassociateServiceRoleFromAccountRequest
  property_count: 0
  slug: iot-greengrass-disassociate-service-role-from-account-request
- name: DisassociateServiceRoleFromAccountResponse
  property_count: 1
  slug: iot-greengrass-disassociate-service-role-from-account-response
- name: EffectiveDeploymentErrorStack
  property_count: 0
  slug: iot-greengrass-effective-deployment-error-stack
- name: EffectiveDeploymentErrorTypeList
  property_count: 0
  slug: iot-greengrass-effective-deployment-error-type-list
- name: EffectiveDeploymentExecutionStatus
  property_count: 0
  slug: iot-greengrass-effective-deployment-execution-status
- name: EffectiveDeployment
  property_count: 11
  slug: iot-greengrass-effective-deployment
- name: EffectiveDeploymentStatusDetails
  property_count: 2
  slug: iot-greengrass-effective-deployment-status-details
- name: EffectiveDeploymentsList
  property_count: 0
  slug: iot-greengrass-effective-deployments-list
- name: GetComponentRequest
  property_count: 0
  slug: iot-greengrass-get-component-request
- name: GetComponentResponse
  property_count: 3
  slug: iot-greengrass-get-component-response
- name: GetComponentVersionArtifactRequest
  property_count: 0
  slug: iot-greengrass-get-component-version-artifact-request
- name: GetComponentVersionArtifactResponse
  property_count: 1
  slug: iot-greengrass-get-component-version-artifact-response
- name: GetConnectivityInfoRequest
  property_count: 0
  slug: iot-greengrass-get-connectivity-info-request
- name: GetConnectivityInfoResponse
  property_count: 2
  slug: iot-greengrass-get-connectivity-info-response
- name: GetCoreDeviceRequest
  property_count: 0
  slug: iot-greengrass-get-core-device-request
- name: GetCoreDeviceResponse
  property_count: 7
  slug: iot-greengrass-get-core-device-response
- name: GetDeploymentRequest
  property_count: 0
  slug: iot-greengrass-get-deployment-request
- name: GetDeploymentResponse
  property_count: 14
  slug: iot-greengrass-get-deployment-response
- name: GetServiceRoleForAccountRequest
  property_count: 0
  slug: iot-greengrass-get-service-role-for-account-request
- name: GetServiceRoleForAccountResponse
  property_count: 2
  slug: iot-greengrass-get-service-role-for-account-response
- name: InstalledComponentLifecycleState
  property_count: 0
  slug: iot-greengrass-installed-component-lifecycle-state
- name: InstalledComponentLifecycleStatusCodeList
  property_count: 0
  slug: iot-greengrass-installed-component-lifecycle-status-code-list
- name: InstalledComponentList
  property_count: 0
  slug: iot-greengrass-installed-component-list
- name: InstalledComponent
  property_count: 9
  slug: iot-greengrass-installed-component
- name: InstalledComponentTopologyFilter
  property_count: 0
  slug: iot-greengrass-installed-component-topology-filter
- name: IoTJobAbortAction
  property_count: 0
  slug: iot-greengrass-io-t-job-abort-action
- name: IoTJobAbortConfig
  property_count: 1
  slug: iot-greengrass-io-t-job-abort-config
- name: IoTJobAbortCriteriaList
  property_count: 0
  slug: iot-greengrass-io-t-job-abort-criteria-list
- name: IoTJobAbortCriteria
  property_count: 4
  slug: iot-greengrass-io-t-job-abort-criteria
- name: IoTJobExecutionFailureType
  property_count: 0
  slug: iot-greengrass-io-t-job-execution-failure-type
- name: IoTJobExecutionsRolloutConfig
  property_count: 2
  slug: iot-greengrass-io-t-job-executions-rollout-config
- name: IoTJobExponentialRolloutRate
  property_count: 3
  slug: iot-greengrass-io-t-job-exponential-rollout-rate
- name: IoTJobRateIncreaseCriteria
  property_count: 2
  slug: iot-greengrass-io-t-job-rate-increase-criteria
- name: IoTJobTimeoutConfig
  property_count: 1
  slug: iot-greengrass-io-t-job-timeout-config
- name: LambdaContainerParams
  property_count: 4
  slug: iot-greengrass-lambda-container-params
- name: LambdaDeviceList
  property_count: 0
  slug: iot-greengrass-lambda-device-list
- name: LambdaDeviceMount
  property_count: 3
  slug: iot-greengrass-lambda-device-mount
- name: LambdaEnvironmentVariables
  property_count: 0
  slug: iot-greengrass-lambda-environment-variables
- name: LambdaEventSourceList
  property_count: 0
  slug: iot-greengrass-lambda-event-source-list
- name: LambdaEventSource
  property_count: 2
  slug: iot-greengrass-lambda-event-source
- name: LambdaEventSourceType
  property_count: 0
  slug: iot-greengrass-lambda-event-source-type
- name: LambdaExecArgsList
  property_count: 0
  slug: iot-greengrass-lambda-exec-args-list
- name: LambdaExecutionParameters
  property_count: 11
  slug: iot-greengrass-lambda-execution-parameters
- name: LambdaFilesystemPermission
  property_count: 0
  slug: iot-greengrass-lambda-filesystem-permission
- name: LambdaFunctionRecipeSource
  property_count: 6
  slug: iot-greengrass-lambda-function-recipe-source
- name: LambdaInputPayloadEncodingType
  property_count: 0
  slug: iot-greengrass-lambda-input-payload-encoding-type
- name: LambdaIsolationMode
  property_count: 0
  slug: iot-greengrass-lambda-isolation-mode
- name: LambdaLinuxProcessParams
  property_count: 2
  slug: iot-greengrass-lambda-linux-process-params
- name: LambdaVolumeList
  property_count: 0
  slug: iot-greengrass-lambda-volume-list
- name: LambdaVolumeMount
  property_count: 4
  slug: iot-greengrass-lambda-volume-mount
- name: ListClientDevicesAssociatedWithCoreDeviceRequest
  property_count: 0
  slug: iot-greengrass-list-client-devices-associated-with-core-device-request
- name: ListClientDevicesAssociatedWithCoreDeviceResponse
  property_count: 2
  slug: iot-greengrass-list-client-devices-associated-with-core-device-response
- name: ListComponentVersionsRequest
  property_count: 0
  slug: iot-greengrass-list-component-versions-request
- name: ListComponentVersionsResponse
  property_count: 2
  slug: iot-greengrass-list-component-versions-response
- name: ListComponentsRequest
  property_count: 0
  slug: iot-greengrass-list-components-request
- name: ListComponentsResponse
  property_count: 2
  slug: iot-greengrass-list-components-response
- name: ListCoreDevicesRequest
  property_count: 0
  slug: iot-greengrass-list-core-devices-request
- name: ListCoreDevicesResponse
  property_count: 2
  slug: iot-greengrass-list-core-devices-response
- name: ListDeploymentsRequest
  property_count: 0
  slug: iot-greengrass-list-deployments-request
- name: ListDeploymentsResponse
  property_count: 2
  slug: iot-greengrass-list-deployments-response
- name: ListEffectiveDeploymentsRequest
  property_count: 0
  slug: iot-greengrass-list-effective-deployments-request
- name: ListEffectiveDeploymentsResponse
  property_count: 2
  slug: iot-greengrass-list-effective-deployments-response
- name: ListInstalledComponentsRequest
  property_count: 0
  slug: iot-greengrass-list-installed-components-request
- name: ListInstalledComponentsResponse
  property_count: 2
  slug: iot-greengrass-list-installed-components-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: iot-greengrass-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: iot-greengrass-list-tags-for-resource-response
- name: PlatformAttributesMap
  property_count: 0
  slug: iot-greengrass-platform-attributes-map
- name: RecipeOutputFormat
  property_count: 0
  slug: iot-greengrass-recipe-output-format
- name: ResolveComponentCandidatesRequest
  property_count: 2
  slug: iot-greengrass-resolve-component-candidates-request
- name: ResolveComponentCandidatesResponse
  property_count: 1
  slug: iot-greengrass-resolve-component-candidates-response
- name: ResolvedComponentVersion
  property_count: 6
  slug: iot-greengrass-resolved-component-version
- name: ResolvedComponentVersionsList
  property_count: 0
  slug: iot-greengrass-resolved-component-versions-list
- name: StringMap
  property_count: 0
  slug: iot-greengrass-string-map
- name: SystemResourceLimits
  property_count: 2
  slug: iot-greengrass-system-resource-limits
- name: TagKeyList
  property_count: 0
  slug: iot-greengrass-tag-key-list
- name: TagMap
  property_count: 0
  slug: iot-greengrass-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: iot-greengrass-tag-resource-request
- name: TagResourceResponse
  property_count: 0
  slug: iot-greengrass-tag-resource-response
- name: UntagResourceRequest
  property_count: 0
  slug: iot-greengrass-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: iot-greengrass-untag-resource-response
- name: UpdateConnectivityInfoRequest
  property_count: 1
  slug: iot-greengrass-update-connectivity-info-request
- name: UpdateConnectivityInfoResponse
  property_count: 2
  slug: iot-greengrass-update-connectivity-info-response
- name: VendorGuidance
  property_count: 0
  slug: iot-greengrass-vendor-guidance
json_structures:
- name: Iot Greengrass Associate Client Device With Core Device Entry List Structure
  property_count: 0
  slug: iot-greengrass-associate-client-device-with-core-device-entry-list-structure
- name: Iot Greengrass Associate Client Device With Core Device Entry Structure
  property_count: 1
  slug: iot-greengrass-associate-client-device-with-core-device-entry-structure
- name: Iot Greengrass Associate Client Device With Core Device Error Entry Structure
  property_count: 3
  slug: iot-greengrass-associate-client-device-with-core-device-error-entry-structure
- name: Iot Greengrass Associate Client Device With Core Device Error List Structure
  property_count: 0
  slug: iot-greengrass-associate-client-device-with-core-device-error-list-structure
- name: Iot Greengrass Associate Service Role To Account Request Structure
  property_count: 1
  slug: iot-greengrass-associate-service-role-to-account-request-structure
- name: Iot Greengrass Associate Service Role To Account Response Structure
  property_count: 1
  slug: iot-greengrass-associate-service-role-to-account-response-structure
- name: Iot Greengrass Associated Client Device List Structure
  property_count: 0
  slug: iot-greengrass-associated-client-device-list-structure
- name: Iot Greengrass Associated Client Device Structure
  property_count: 2
  slug: iot-greengrass-associated-client-device-structure
- name: Iot Greengrass Batch Associate Client Device With Core Device Request Structure
  property_count: 1
  slug: iot-greengrass-batch-associate-client-device-with-core-device-request-structure
- name: Iot Greengrass Batch Associate Client Device With Core Device Response Structure
  property_count: 1
  slug: iot-greengrass-batch-associate-client-device-with-core-device-response-structure
- name: Iot Greengrass Batch Disassociate Client Device From Core Device Request Structure
  property_count: 1
  slug: iot-greengrass-batch-disassociate-client-device-from-core-device-request-structure
- name: Iot Greengrass Batch Disassociate Client Device From Core Device Response Structure
  property_count: 1
  slug: iot-greengrass-batch-disassociate-client-device-from-core-device-response-structure
- name: Iot Greengrass Cancel Deployment Request Structure
  property_count: 0
  slug: iot-greengrass-cancel-deployment-request-structure
- name: Iot Greengrass Cancel Deployment Response Structure
  property_count: 1
  slug: iot-greengrass-cancel-deployment-response-structure
- name: Iot Greengrass Cloud Component State Structure
  property_count: 0
  slug: iot-greengrass-cloud-component-state-structure
- name: Iot Greengrass Cloud Component Status Structure
  property_count: 5
  slug: iot-greengrass-cloud-component-status-structure
- name: Iot Greengrass Component Candidate List Structure
  property_count: 0
  slug: iot-greengrass-component-candidate-list-structure
- name: Iot Greengrass Component Candidate Structure
  property_count: 3
  slug: iot-greengrass-component-candidate-structure
- name: Iot Greengrass Component Configuration Path List Structure
  property_count: 0
  slug: iot-greengrass-component-configuration-path-list-structure
- name: Iot Greengrass Component Configuration Update Structure
  property_count: 2
  slug: iot-greengrass-component-configuration-update-structure
- name: Iot Greengrass Component Dependency Map Structure
  property_count: 0
  slug: iot-greengrass-component-dependency-map-structure
- name: Iot Greengrass Component Dependency Requirement Structure
  property_count: 2
  slug: iot-greengrass-component-dependency-requirement-structure
- name: Iot Greengrass Component Dependency Type Structure
  property_count: 0
  slug: iot-greengrass-component-dependency-type-structure
- name: Iot Greengrass Component Deployment Specification Structure
  property_count: 3
  slug: iot-greengrass-component-deployment-specification-structure
- name: Iot Greengrass Component Deployment Specifications Structure
  property_count: 0
  slug: iot-greengrass-component-deployment-specifications-structure
- name: Iot Greengrass Component Latest Version Structure
  property_count: 6
  slug: iot-greengrass-component-latest-version-structure
- name: Iot Greengrass Component List Structure
  property_count: 0
  slug: iot-greengrass-component-list-structure
- name: Iot Greengrass Component Platform List Structure
  property_count: 0
  slug: iot-greengrass-component-platform-list-structure
- name: Iot Greengrass Component Platform Structure
  property_count: 2
  slug: iot-greengrass-component-platform-structure
- name: Iot Greengrass Component Run With Structure
  property_count: 3
  slug: iot-greengrass-component-run-with-structure
- name: Iot Greengrass Component Structure
  property_count: 3
  slug: iot-greengrass-component-structure
- name: Iot Greengrass Component Version List Item Structure
  property_count: 3
  slug: iot-greengrass-component-version-list-item-structure
- name: Iot Greengrass Component Version List Structure
  property_count: 0
  slug: iot-greengrass-component-version-list-structure
- name: Iot Greengrass Component Version Requirement Map Structure
  property_count: 0
  slug: iot-greengrass-component-version-requirement-map-structure
- name: Iot Greengrass Component Visibility Scope Structure
  property_count: 0
  slug: iot-greengrass-component-visibility-scope-structure
- name: Iot Greengrass Connectivity Info List Structure
  property_count: 0
  slug: iot-greengrass-connectivity-info-list-structure
- name: Iot Greengrass Connectivity Info Structure
  property_count: 4
  slug: iot-greengrass-connectivity-info-structure
- name: Iot Greengrass Core Device Status Structure
  property_count: 0
  slug: iot-greengrass-core-device-status-structure
- name: Iot Greengrass Core Device Structure
  property_count: 3
  slug: iot-greengrass-core-device-structure
- name: Iot Greengrass Core Devices List Structure
  property_count: 0
  slug: iot-greengrass-core-devices-list-structure
- name: Iot Greengrass Create Component Version Request Structure
  property_count: 4
  slug: iot-greengrass-create-component-version-request-structure
- name: Iot Greengrass Create Component Version Response Structure
  property_count: 5
  slug: iot-greengrass-create-component-version-response-structure
- name: Iot Greengrass Create Deployment Request Structure
  property_count: 8
  slug: iot-greengrass-create-deployment-request-structure
- name: Iot Greengrass Create Deployment Response Structure
  property_count: 3
  slug: iot-greengrass-create-deployment-response-structure
- name: Iot Greengrass Delete Component Request Structure
  property_count: 0
  slug: iot-greengrass-delete-component-request-structure
- name: Iot Greengrass Delete Core Device Request Structure
  property_count: 0
  slug: iot-greengrass-delete-core-device-request-structure
- name: Iot Greengrass Delete Deployment Request Structure
  property_count: 0
  slug: iot-greengrass-delete-deployment-request-structure
- name: Iot Greengrass Deployment Component Update Policy Action Structure
  property_count: 0
  slug: iot-greengrass-deployment-component-update-policy-action-structure
- name: Iot Greengrass Deployment Component Update Policy Structure
  property_count: 2
  slug: iot-greengrass-deployment-component-update-policy-structure
- name: Iot Greengrass Deployment Configuration Validation Policy Structure
  property_count: 1
  slug: iot-greengrass-deployment-configuration-validation-policy-structure
- name: Iot Greengrass Deployment Failure Handling Policy Structure
  property_count: 0
  slug: iot-greengrass-deployment-failure-handling-policy-structure
- name: Iot Greengrass Deployment History Filter Structure
  property_count: 0
  slug: iot-greengrass-deployment-history-filter-structure
- name: Iot Greengrass Deployment Io T Job Configuration Structure
  property_count: 3
  slug: iot-greengrass-deployment-io-t-job-configuration-structure
- name: Iot Greengrass Deployment List Structure
  property_count: 0
  slug: iot-greengrass-deployment-list-structure
- name: Iot Greengrass Deployment Policies Structure
  property_count: 3
  slug: iot-greengrass-deployment-policies-structure
- name: Iot Greengrass Deployment Status Structure
  property_count: 0
  slug: iot-greengrass-deployment-status-structure
- name: Iot Greengrass Deployment Structure
  property_count: 8
  slug: iot-greengrass-deployment-structure
- name: Iot Greengrass Describe Component Request Structure
  property_count: 0
  slug: iot-greengrass-describe-component-request-structure
- name: Iot Greengrass Describe Component Response Structure
  property_count: 9
  slug: iot-greengrass-describe-component-response-structure
- name: Iot Greengrass Disassociate Client Device From Core Device Entry List Structure
  property_count: 0
  slug: iot-greengrass-disassociate-client-device-from-core-device-entry-list-structure
- name: Iot Greengrass Disassociate Client Device From Core Device Entry Structure
  property_count: 1
  slug: iot-greengrass-disassociate-client-device-from-core-device-entry-structure
- name: Iot Greengrass Disassociate Client Device From Core Device Error Entry Structure
  property_count: 3
  slug: iot-greengrass-disassociate-client-device-from-core-device-error-entry-structure
- name: Iot Greengrass Disassociate Client Device From Core Device Error List Structure
  property_count: 0
  slug: iot-greengrass-disassociate-client-device-from-core-device-error-list-structure
- name: Iot Greengrass Disassociate Service Role From Account Request Structure
  property_count: 0
  slug: iot-greengrass-disassociate-service-role-from-account-request-structure
- name: Iot Greengrass Disassociate Service Role From Account Response Structure
  property_count: 1
  slug: iot-greengrass-disassociate-service-role-from-account-response-structure
- name: Iot Greengrass Effective Deployment Error Stack Structure
  property_count: 0
  slug: iot-greengrass-effective-deployment-error-stack-structure
- name: Iot Greengrass Effective Deployment Error Type List Structure
  property_count: 0
  slug: iot-greengrass-effective-deployment-error-type-list-structure
- name: Iot Greengrass Effective Deployment Execution Status Structure
  property_count: 0
  slug: iot-greengrass-effective-deployment-execution-status-structure
- name: Iot Greengrass Effective Deployment Status Details Structure
  property_count: 2
  slug: iot-greengrass-effective-deployment-status-details-structure
- name: Iot Greengrass Effective Deployment Structure
  property_count: 11
  slug: iot-greengrass-effective-deployment-structure
- name: Iot Greengrass Effective Deployments List Structure
  property_count: 0
  slug: iot-greengrass-effective-deployments-list-structure
- name: Iot Greengrass Get Component Request Structure
  property_count: 0
  slug: iot-greengrass-get-component-request-structure
- name: Iot Greengrass Get Component Response Structure
  property_count: 3
  slug: iot-greengrass-get-component-response-structure
- name: Iot Greengrass Get Component Version Artifact Request Structure
  property_count: 0
  slug: iot-greengrass-get-component-version-artifact-request-structure
- name: Iot Greengrass Get Component Version Artifact Response Structure
  property_count: 1
  slug: iot-greengrass-get-component-version-artifact-response-structure
- name: Iot Greengrass Get Connectivity Info Request Structure
  property_count: 0
  slug: iot-greengrass-get-connectivity-info-request-structure
- name: Iot Greengrass Get Connectivity Info Response Structure
  property_count: 2
  slug: iot-greengrass-get-connectivity-info-response-structure
- name: Iot Greengrass Get Core Device Request Structure
  property_count: 0
  slug: iot-greengrass-get-core-device-request-structure
- name: Iot Greengrass Get Core Device Response Structure
  property_count: 7
  slug: iot-greengrass-get-core-device-response-structure
- name: Iot Greengrass Get Deployment Request Structure
  property_count: 0
  slug: iot-greengrass-get-deployment-request-structure
- name: Iot Greengrass Get Deployment Response Structure
  property_count: 14
  slug: iot-greengrass-get-deployment-response-structure
- name: Iot Greengrass Get Service Role For Account Request Structure
  property_count: 0
  slug: iot-greengrass-get-service-role-for-account-request-structure
- name: Iot Greengrass Get Service Role For Account Response Structure
  property_count: 2
  slug: iot-greengrass-get-service-role-for-account-response-structure
- name: Iot Greengrass Installed Component Lifecycle State Structure
  property_count: 0
  slug: iot-greengrass-installed-component-lifecycle-state-structure
- name: Iot Greengrass Installed Component Lifecycle Status Code List Structure
  property_count: 0
  slug: iot-greengrass-installed-component-lifecycle-status-code-list-structure
- name: Iot Greengrass Installed Component List Structure
  property_count: 0
  slug: iot-greengrass-installed-component-list-structure
- name: Iot Greengrass Installed Component Structure
  property_count: 9
  slug: iot-greengrass-installed-component-structure
- name: Iot Greengrass Installed Component Topology Filter Structure
  property_count: 0
  slug: iot-greengrass-installed-component-topology-filter-structure
- name: Iot Greengrass Io T Job Abort Action Structure
  property_count: 0
  slug: iot-greengrass-io-t-job-abort-action-structure
- name: Iot Greengrass Io T Job Abort Config Structure
  property_count: 1
  slug: iot-greengrass-io-t-job-abort-config-structure
- name: Iot Greengrass Io T Job Abort Criteria List Structure
  property_count: 0
  slug: iot-greengrass-io-t-job-abort-criteria-list-structure
- name: Iot Greengrass Io T Job Abort Criteria Structure
  property_count: 4
  slug: iot-greengrass-io-t-job-abort-criteria-structure
- name: Iot Greengrass Io T Job Execution Failure Type Structure
  property_count: 0
  slug: iot-greengrass-io-t-job-execution-failure-type-structure
- name: Iot Greengrass Io T Job Executions Rollout Config Structure
  property_count: 2
  slug: iot-greengrass-io-t-job-executions-rollout-config-structure
- name: Iot Greengrass Io T Job Exponential Rollout Rate Structure
  property_count: 3
  slug: iot-greengrass-io-t-job-exponential-rollout-rate-structure
- name: Iot Greengrass Io T Job Rate Increase Criteria Structure
  property_count: 2
  slug: iot-greengrass-io-t-job-rate-increase-criteria-structure
- name: Iot Greengrass Io T Job Timeout Config Structure
  property_count: 1
  slug: iot-greengrass-io-t-job-timeout-config-structure
- name: Iot Greengrass Lambda Container Params Structure
  property_count: 4
  slug: iot-greengrass-lambda-container-params-structure
- name: Iot Greengrass Lambda Device List Structure
  property_count: 0
  slug: iot-greengrass-lambda-device-list-structure
- name: Iot Greengrass Lambda Device Mount Structure
  property_count: 3
  slug: iot-greengrass-lambda-device-mount-structure
- name: Iot Greengrass Lambda Environment Variables Structure
  property_count: 0
  slug: iot-greengrass-lambda-environment-variables-structure
- name: Iot Greengrass Lambda Event Source List Structure
  property_count: 0
  slug: iot-greengrass-lambda-event-source-list-structure
- name: Iot Greengrass Lambda Event Source Structure
  property_count: 2
  slug: iot-greengrass-lambda-event-source-structure
- name: Iot Greengrass Lambda Event Source Type Structure
  property_count: 0
  slug: iot-greengrass-lambda-event-source-type-structure
- name: Iot Greengrass Lambda Exec Args List Structure
  property_count: 0
  slug: iot-greengrass-lambda-exec-args-list-structure
- name: Iot Greengrass Lambda Execution Parameters Structure
  property_count: 11
  slug: iot-greengrass-lambda-execution-parameters-structure
- name: Iot Greengrass Lambda Filesystem Permission Structure
  property_count: 0
  slug: iot-greengrass-lambda-filesystem-permission-structure
- name: Iot Greengrass Lambda Function Recipe Source Structure
  property_count: 6
  slug: iot-greengrass-lambda-function-recipe-source-structure
- name: Iot Greengrass Lambda Input Payload Encoding Type Structure
  property_count: 0
  slug: iot-greengrass-lambda-input-payload-encoding-type-structure
- name: Iot Greengrass Lambda Isolation Mode Structure
  property_count: 0
  slug: iot-greengrass-lambda-isolation-mode-structure
- name: Iot Greengrass Lambda Linux Process Params Structure
  property_count: 2
  slug: iot-greengrass-lambda-linux-process-params-structure
- name: Iot Greengrass Lambda Volume List Structure
  property_count: 0
  slug: iot-greengrass-lambda-volume-list-structure
- name: Iot Greengrass Lambda Volume Mount Structure
  property_count: 4
  slug: iot-greengrass-lambda-volume-mount-structure
- name: Iot Greengrass List Client Devices Associated With Core Device Request Structure
  property_count: 0
  slug: iot-greengrass-list-client-devices-associated-with-core-device-request-structure
- name: Iot Greengrass List Client Devices Associated With Core Device Response Structure
  property_count: 2
  slug: iot-greengrass-list-client-devices-associated-with-core-device-response-structure
- name: Iot Greengrass List Component Versions Request Structure
  property_count: 0
  slug: iot-greengrass-list-component-versions-request-structure
- name: Iot Greengrass List Component Versions Response Structure
  property_count: 2
  slug: iot-greengrass-list-component-versions-response-structure
- name: Iot Greengrass List Components Request Structure
  property_count: 0
  slug: iot-greengrass-list-components-request-structure
- name: Iot Greengrass List Components Response Structure
  property_count: 2
  slug: iot-greengrass-list-components-response-structure
- name: Iot Greengrass List Core Devices Request Structure
  property_count: 0
  slug: iot-greengrass-list-core-devices-request-structure
- name: Iot Greengrass List Core Devices Response Structure
  property_count: 2
  slug: iot-greengrass-list-core-devices-response-structure
- name: Iot Greengrass List Deployments Request Structure
  property_count: 0
  slug: iot-greengrass-list-deployments-request-structure
- name: Iot Greengrass List Deployments Response Structure
  property_count: 2
  slug: iot-greengrass-list-deployments-response-structure
- name: Iot Greengrass List Effective Deployments Request Structure
  property_count: 0
  slug: iot-greengrass-list-effective-deployments-request-structure
- name: Iot Greengrass List Effective Deployments Response Structure
  property_count: 2
  slug: iot-greengrass-list-effective-deployments-response-structure
- name: Iot Greengrass List Installed Components Request Structure
  property_count: 0
  slug: iot-greengrass-list-installed-components-request-structure
- name: Iot Greengrass List Installed Components Response Structure
  property_count: 2
  slug: iot-greengrass-list-installed-components-response-structure
- name: Iot Greengrass List Tags For Resource Request Structure
  property_count: 0
  slug: iot-greengrass-list-tags-for-resource-request-structure
- name: Iot Greengrass List Tags For Resource Response Structure
  property_count: 1
  slug: iot-greengrass-list-tags-for-resource-response-structure
- name: Iot Greengrass Platform Attributes Map Structure
  property_count: 0
  slug: iot-greengrass-platform-attributes-map-structure
- name: Iot Greengrass Recipe Output Format Structure
  property_count: 0
  slug: iot-greengrass-recipe-output-format-structure
- name: Iot Greengrass Resolve Component Candidates Request Structure
  property_count: 2
  slug: iot-greengrass-resolve-component-candidates-request-structure
- name: Iot Greengrass Resolve Component Candidates Response Structure
  property_count: 1
  slug: iot-greengrass-resolve-component-candidates-response-structure
- name: Iot Greengrass Resolved Component Version Structure
  property_count: 6
  slug: iot-greengrass-resolved-component-version-structure
- name: Iot Greengrass Resolved Component Versions List Structure
  property_count: 0
  slug: iot-greengrass-resolved-component-versions-list-structure
- name: Iot Greengrass String Map Structure
  property_count: 0
  slug: iot-greengrass-string-map-structure
- name: Iot Greengrass System Resource Limits Structure
  property_count: 2
  slug: iot-greengrass-system-resource-limits-structure
- name: Iot Greengrass Tag Key List Structure
  property_count: 0
  slug: iot-greengrass-tag-key-list-structure
- name: Iot Greengrass Tag Map Structure
  property_count: 0
  slug: iot-greengrass-tag-map-structure
- name: Iot Greengrass Tag Resource Request Structure
  property_count: 1
  slug: iot-greengrass-tag-resource-request-structure
- name: Iot Greengrass Tag Resource Response Structure
  property_count: 0
  slug: iot-greengrass-tag-resource-response-structure
- name: Iot Greengrass Untag Resource Request Structure
  property_count: 0
  slug: iot-greengrass-untag-resource-request-structure
- name: Iot Greengrass Untag Resource Response Structure
  property_count: 0
  slug: iot-greengrass-untag-resource-response-structure
- name: Iot Greengrass Update Connectivity Info Request Structure
  property_count: 1
  slug: iot-greengrass-update-connectivity-info-request-structure
- name: Iot Greengrass Update Connectivity Info Response Structure
  property_count: 2
  slug: iot-greengrass-update-connectivity-info-response-structure
- name: Iot Greengrass Vendor Guidance Structure
  property_count: 0
  slug: iot-greengrass-vendor-guidance-structure
jsonld:
- class_count: 102
  name: Amazon Iot Greengrass Context
  property_count: 133
  slug: amazon-iot-greengrass-context
layout: provider
modified: '2026-05-19'
name: Amazon IoT Greengrass
nav: Providers
network: true
overview: 'Amazon IoT Greengrass publishes 2 APIs on the [APIs.io](https://apis.io/) network: Greengrass API and Tags API. Tagged areas include Edge Computing, IoT, Lambda, Machine-Learning, and Real-Time Processing.


  The Amazon IoT Greengrass catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon IoT Greengrass'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 15 more developer resources.'
plans:
- name: Amazon Iot Greengrass Plans Pricing
  plan_count: 3
  slug: amazon-iot-greengrass-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Amazon Iot Greengrass Rate Limits
  slug: amazon-iot-greengrass-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon IoT Greengrass API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-iot-greengrass-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Amazon IoT Greengrass API Rules
  rule_count: 20
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 10
  slug: amazon-iot-greengrass-spectral-rules
score:
  band: strong
  composite: 54.8
  coverage:
    artifact_dirs: 17
    catalog_gap: 48.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 61.8
    commercial_clarity: 61.8
    contract_governance: 28.8
    contract_quality: 65.4
    developer_ergonomics: 61.9
    discoverability: 68.5
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 54.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-iot-greengrass/refs/heads/main/screenshots/amazon-iot-greengrass-2026-06-20T171714.png
security:
- kind: authentication
  name: Amazon Iot Greengrass Authentication
  slug: amazon-iot-greengrass-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Iot Greengrass Domain Security
  slug: amazon-iot-greengrass-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Iot Greengrass Vulnerability Disclosure
  slug: amazon-iot-greengrass-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Iot Greengrass Trust Center
  slug: amazon-iot-greengrass-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-iot-greengrass
tags:
- Edge Computing
- IoT
- Lambda
- Machine-Learning
- Real-Time Processing
use_cases:
- description: Process sensor data locally to reduce latency and bandwidth.
  name: Industrial Edge Processing
- description: Run computer vision and anomaly detection models at the edge.
  name: Edge ML Inference
- description: Continue processing and storing data when disconnected from the cloud.
  name: Offline Operation
website: https://aws.amazon.com/greengrass/
---

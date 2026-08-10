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
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: verified
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 52.3
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 23
  human_in_the_loop: 0
  name: Aws App Mesh Agentic Access
  operation_count: 38
  slug: aws-app-mesh-agentic-access
  summary_line: 38 operations · 23 acting
api_count: 4
apis:
- description: The Meshes API from AWS App Mesh — 14 operation(s) for meshes.
  name: AWS App Mesh Meshes API
  slug: aws-app-mesh-meshes-api
- description: The Tag#resourceArn API from AWS App Mesh — 1 operation(s) for tag#resourcearn.
  name: AWS App Mesh Tag#resourceArn API
  slug: aws-app-mesh-tag-resourcearn-api
- description: The Tags#resourceArn API from AWS App Mesh — 1 operation(s) for tags#resourcearn.
  name: AWS App Mesh Tags#resourceArn API
  slug: aws-app-mesh-tags-resourcearn-api
- description: The Untag#resourceArn API from AWS App Mesh — 1 operation(s) for untag#resourcearn.
  name: AWS App Mesh Untag#resourceArn API
  slug: aws-app-mesh-untag-resourcearn-api
artifact_total: 1049
collections:
- collection_type: postman
  name: AWS App Mesh Meshes API
  slug: postman-aws-app-mesh-meshes-api
- collection_type: postman
  name: AWS App Mesh Meshes Tag#resourceArn API
  slug: postman-aws-app-mesh-tag-resourcearn-api
- collection_type: postman
  name: AWS App Mesh Meshes Tags#resourceArn API
  slug: postman-aws-app-mesh-tags-resourcearn-api
- collection_type: postman
  name: AWS App Mesh Meshes Untag#resourceArn API
  slug: postman-aws-app-mesh-untag-resourcearn-api
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/aws-app-mesh/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/aws-app-mesh-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/aws-app-mesh-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/aws-app-mesh-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/aws-app-mesh-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/aws-app-mesh-authentication.yml
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/app-mesh/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/app-mesh/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.aws.amazon.com/app-mesh/latest/userguide/getting_started.html
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/app-mesh/pricing/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/app-mesh/faqs/
- group: auth
  title: ''
  type: Authentication
  url: https://docs.aws.amazon.com/app-mesh/latest/userguide/security-iam.html
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/appmesh/
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
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: design
  title: ''
  type: SpectralRules
  url: rules/aws-app-mesh-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/aws-app-mesh-vocabulary.yaml
created: '2026-03-16'
description: 'AWS App Mesh is a service mesh based on the Envoy proxy that provides application-level networking to make it easy for services to communicate with each other across multiple types of compute infrastructure including Amazon ECS, EKS, EC2, and Fargate. App Mesh standardizes service communication, giving end-to-end visibility and helping ensure high availability. Note: AWS App Mesh is deprecated; Amazon ECS Service Connect is the recommended replacement for new workloads.'
examples:
- key_count: 1
  name: App Mesh Access Log Example
  slug: app-mesh-access-log-example
- key_count: 1
  name: App Mesh Account Id Example
  slug: app-mesh-account-id-example
- key_count: 1
  name: App Mesh Arn Example
  slug: app-mesh-arn-example
- key_count: 2
  name: App Mesh Aws Cloud Map Instance Attribute Example
  slug: app-mesh-aws-cloud-map-instance-attribute-example
- key_count: 1
  name: App Mesh Aws Cloud Map Instance Attribute Key Example
  slug: app-mesh-aws-cloud-map-instance-attribute-key-example
- key_count: 1
  name: App Mesh Aws Cloud Map Instance Attribute Value Example
  slug: app-mesh-aws-cloud-map-instance-attribute-value-example
- key_count: 1
  name: App Mesh Aws Cloud Map Instance Attributes Example
  slug: app-mesh-aws-cloud-map-instance-attributes-example
- key_count: 1
  name: App Mesh Aws Cloud Map Name Example
  slug: app-mesh-aws-cloud-map-name-example
- key_count: 4
  name: App Mesh Aws Cloud Map Service Discovery Example
  slug: app-mesh-aws-cloud-map-service-discovery-example
- key_count: 1
  name: App Mesh Backend Defaults Example
  slug: app-mesh-backend-defaults-example
- key_count: 1
  name: App Mesh Backend Example
  slug: app-mesh-backend-example
- key_count: 1
  name: App Mesh Backends Example
  slug: app-mesh-backends-example
- key_count: 1
  name: App Mesh Bad Request Exception Example
  slug: app-mesh-bad-request-exception-example
- key_count: 1
  name: App Mesh Boolean Example
  slug: app-mesh-boolean-example
- key_count: 1
  name: App Mesh Certificate Authority Arns Example
  slug: app-mesh-certificate-authority-arns-example
- key_count: 1
  name: App Mesh Client Policy Example
  slug: app-mesh-client-policy-example
- key_count: 4
  name: App Mesh Client Policy Tls Example
  slug: app-mesh-client-policy-tls-example
- key_count: 2
  name: App Mesh Client Tls Certificate Example
  slug: app-mesh-client-tls-certificate-example
- key_count: 1
  name: App Mesh Conflict Exception Example
  slug: app-mesh-conflict-exception-example
- key_count: 4
  name: App Mesh Create Gateway Route Input Example
  slug: app-mesh-create-gateway-route-input-example
- key_count: 1
  name: App Mesh Create Gateway Route Output Example
  slug: app-mesh-create-gateway-route-output-example
- key_count: 4
  name: App Mesh Create Mesh Input Example
  slug: app-mesh-create-mesh-input-example
- key_count: 1
  name: App Mesh Create Mesh Output Example
  slug: app-mesh-create-mesh-output-example
- key_count: 4
  name: App Mesh Create Route Input Example
  slug: app-mesh-create-route-input-example
- key_count: 1
  name: App Mesh Create Route Output Example
  slug: app-mesh-create-route-output-example
- key_count: 4
  name: App Mesh Create Virtual Gateway Input Example
  slug: app-mesh-create-virtual-gateway-input-example
- key_count: 1
  name: App Mesh Create Virtual Gateway Output Example
  slug: app-mesh-create-virtual-gateway-output-example
- key_count: 4
  name: App Mesh Create Virtual Node Input Example
  slug: app-mesh-create-virtual-node-input-example
- key_count: 1
  name: App Mesh Create Virtual Node Output Example
  slug: app-mesh-create-virtual-node-output-example
- key_count: 4
  name: App Mesh Create Virtual Router Input Example
  slug: app-mesh-create-virtual-router-input-example
- key_count: 1
  name: App Mesh Create Virtual Router Output Example
  slug: app-mesh-create-virtual-router-output-example
- key_count: 4
  name: App Mesh Create Virtual Service Input Example
  slug: app-mesh-create-virtual-service-input-example
- key_count: 1
  name: App Mesh Create Virtual Service Output Example
  slug: app-mesh-create-virtual-service-output-example
- key_count: 1
  name: App Mesh Default Gateway Route Rewrite Example
  slug: app-mesh-default-gateway-route-rewrite-example
- key_count: 1
  name: App Mesh Delete Gateway Route Input Example
  slug: app-mesh-delete-gateway-route-input-example
- key_count: 1
  name: App Mesh Delete Gateway Route Output Example
  slug: app-mesh-delete-gateway-route-output-example
- key_count: 1
  name: App Mesh Delete Mesh Input Example
  slug: app-mesh-delete-mesh-input-example
- key_count: 1
  name: App Mesh Delete Mesh Output Example
  slug: app-mesh-delete-mesh-output-example
- key_count: 1
  name: App Mesh Delete Route Input Example
  slug: app-mesh-delete-route-input-example
- key_count: 1
  name: App Mesh Delete Route Output Example
  slug: app-mesh-delete-route-output-example
- key_count: 1
  name: App Mesh Delete Virtual Gateway Input Example
  slug: app-mesh-delete-virtual-gateway-input-example
- key_count: 1
  name: App Mesh Delete Virtual Gateway Output Example
  slug: app-mesh-delete-virtual-gateway-output-example
- key_count: 1
  name: App Mesh Delete Virtual Node Input Example
  slug: app-mesh-delete-virtual-node-input-example
- key_count: 1
  name: App Mesh Delete Virtual Node Output Example
  slug: app-mesh-delete-virtual-node-output-example
- key_count: 1
  name: App Mesh Delete Virtual Router Input Example
  slug: app-mesh-delete-virtual-router-input-example
- key_count: 1
  name: App Mesh Delete Virtual Router Output Example
  slug: app-mesh-delete-virtual-router-output-example
- key_count: 1
  name: App Mesh Delete Virtual Service Input Example
  slug: app-mesh-delete-virtual-service-input-example
- key_count: 1
  name: App Mesh Delete Virtual Service Output Example
  slug: app-mesh-delete-virtual-service-output-example
- key_count: 1
  name: App Mesh Describe Gateway Route Input Example
  slug: app-mesh-describe-gateway-route-input-example
- key_count: 1
  name: App Mesh Describe Gateway Route Output Example
  slug: app-mesh-describe-gateway-route-output-example
- key_count: 1
  name: App Mesh Describe Mesh Input Example
  slug: app-mesh-describe-mesh-input-example
- key_count: 1
  name: App Mesh Describe Mesh Output Example
  slug: app-mesh-describe-mesh-output-example
- key_count: 1
  name: App Mesh Describe Route Input Example
  slug: app-mesh-describe-route-input-example
- key_count: 1
  name: App Mesh Describe Route Output Example
  slug: app-mesh-describe-route-output-example
- key_count: 1
  name: App Mesh Describe Virtual Gateway Input Example
  slug: app-mesh-describe-virtual-gateway-input-example
- key_count: 1
  name: App Mesh Describe Virtual Gateway Output Example
  slug: app-mesh-describe-virtual-gateway-output-example
- key_count: 1
  name: App Mesh Describe Virtual Node Input Example
  slug: app-mesh-describe-virtual-node-input-example
- key_count: 1
  name: App Mesh Describe Virtual Node Output Example
  slug: app-mesh-describe-virtual-node-output-example
- key_count: 1
  name: App Mesh Describe Virtual Router Input Example
  slug: app-mesh-describe-virtual-router-input-example
- key_count: 1
  name: App Mesh Describe Virtual Router Output Example
  slug: app-mesh-describe-virtual-router-output-example
- key_count: 1
  name: App Mesh Describe Virtual Service Input Example
  slug: app-mesh-describe-virtual-service-input-example
- key_count: 1
  name: App Mesh Describe Virtual Service Output Example
  slug: app-mesh-describe-virtual-service-output-example
- key_count: 1
  name: App Mesh Dns Response Type Example
  slug: app-mesh-dns-response-type-example
- key_count: 3
  name: App Mesh Dns Service Discovery Example
  slug: app-mesh-dns-service-discovery-example
- key_count: 2
  name: App Mesh Duration Example
  slug: app-mesh-duration-example
- key_count: 1
  name: App Mesh Duration Unit Example
  slug: app-mesh-duration-unit-example
- key_count: 1
  name: App Mesh Duration Value Example
  slug: app-mesh-duration-value-example
- key_count: 1
  name: App Mesh Egress Filter Example
  slug: app-mesh-egress-filter-example
- key_count: 1
  name: App Mesh Egress Filter Type Example
  slug: app-mesh-egress-filter-type-example
- key_count: 1
  name: App Mesh Exact Host Name Example
  slug: app-mesh-exact-host-name-example
- key_count: 2
  name: App Mesh File Access Log Example
  slug: app-mesh-file-access-log-example
- key_count: 1
  name: App Mesh File Path Example
  slug: app-mesh-file-path-example
- key_count: 1
  name: App Mesh Forbidden Exception Example
  slug: app-mesh-forbidden-exception-example
- key_count: 6
  name: App Mesh Gateway Route Data Example
  slug: app-mesh-gateway-route-data-example
- key_count: 2
  name: App Mesh Gateway Route Hostname Match Example
  slug: app-mesh-gateway-route-hostname-match-example
- key_count: 1
  name: App Mesh Gateway Route Hostname Rewrite Example
  slug: app-mesh-gateway-route-hostname-rewrite-example
- key_count: 1
  name: App Mesh Gateway Route List Example
  slug: app-mesh-gateway-route-list-example
- key_count: 1
  name: App Mesh Gateway Route Priority Example
  slug: app-mesh-gateway-route-priority-example
- key_count: 9
  name: App Mesh Gateway Route Ref Example
  slug: app-mesh-gateway-route-ref-example
- key_count: 4
  name: App Mesh Gateway Route Spec Example
  slug: app-mesh-gateway-route-spec-example
- key_count: 1
  name: App Mesh Gateway Route Status Code Example
  slug: app-mesh-gateway-route-status-code-example
- key_count: 1
  name: App Mesh Gateway Route Status Example
  slug: app-mesh-gateway-route-status-example
- key_count: 2
  name: App Mesh Gateway Route Target Example
  slug: app-mesh-gateway-route-target-example
- key_count: 1
  name: App Mesh Gateway Route Virtual Service Example
  slug: app-mesh-gateway-route-virtual-service-example
- key_count: 2
  name: App Mesh Grpc Gateway Route Action Example
  slug: app-mesh-grpc-gateway-route-action-example
- key_count: 2
  name: App Mesh Grpc Gateway Route Example
  slug: app-mesh-grpc-gateway-route-example
- key_count: 4
  name: App Mesh Grpc Gateway Route Match Example
  slug: app-mesh-grpc-gateway-route-match-example
- key_count: 3
  name: App Mesh Grpc Gateway Route Metadata Example
  slug: app-mesh-grpc-gateway-route-metadata-example
- key_count: 1
  name: App Mesh Grpc Gateway Route Metadata List Example
  slug: app-mesh-grpc-gateway-route-metadata-list-example
- key_count: 1
  name: App Mesh Grpc Gateway Route Rewrite Example
  slug: app-mesh-grpc-gateway-route-rewrite-example
- key_count: 5
  name: App Mesh Grpc Metadata Match Method Example
  slug: app-mesh-grpc-metadata-match-method-example
- key_count: 1
  name: App Mesh Grpc Retry Policy Event Example
  slug: app-mesh-grpc-retry-policy-event-example
- key_count: 1
  name: App Mesh Grpc Retry Policy Events Example
  slug: app-mesh-grpc-retry-policy-events-example
- key_count: 5
  name: App Mesh Grpc Retry Policy Example
  slug: app-mesh-grpc-retry-policy-example
- key_count: 1
  name: App Mesh Grpc Route Action Example
  slug: app-mesh-grpc-route-action-example
- key_count: 4
  name: App Mesh Grpc Route Example
  slug: app-mesh-grpc-route-example
- key_count: 4
  name: App Mesh Grpc Route Match Example
  slug: app-mesh-grpc-route-match-example
- key_count: 3
  name: App Mesh Grpc Route Metadata Example
  slug: app-mesh-grpc-route-metadata-example
- key_count: 1
  name: App Mesh Grpc Route Metadata List Example
  slug: app-mesh-grpc-route-metadata-list-example
- key_count: 5
  name: App Mesh Grpc Route Metadata Match Method Example
  slug: app-mesh-grpc-route-metadata-match-method-example
- key_count: 2
  name: App Mesh Grpc Timeout Example
  slug: app-mesh-grpc-timeout-example
- key_count: 1
  name: App Mesh Header Match Example
  slug: app-mesh-header-match-example
- key_count: 5
  name: App Mesh Header Match Method Example
  slug: app-mesh-header-match-method-example
- key_count: 1
  name: App Mesh Header Name Example
  slug: app-mesh-header-name-example
- key_count: 1
  name: App Mesh Health Check Interval Millis Example
  slug: app-mesh-health-check-interval-millis-example
- key_count: 7
  name: App Mesh Health Check Policy Example
  slug: app-mesh-health-check-policy-example
- key_count: 1
  name: App Mesh Health Check Threshold Example
  slug: app-mesh-health-check-threshold-example
- key_count: 1
  name: App Mesh Health Check Timeout Millis Example
  slug: app-mesh-health-check-timeout-millis-example
- key_count: 1
  name: App Mesh Hostname Example
  slug: app-mesh-hostname-example
- key_count: 2
  name: App Mesh Http Gateway Route Action Example
  slug: app-mesh-http-gateway-route-action-example
- key_count: 2
  name: App Mesh Http Gateway Route Example
  slug: app-mesh-http-gateway-route-example
- key_count: 3
  name: App Mesh Http Gateway Route Header Example
  slug: app-mesh-http-gateway-route-header-example
- key_count: 1
  name: App Mesh Http Gateway Route Headers Example
  slug: app-mesh-http-gateway-route-headers-example
- key_count: 7
  name: App Mesh Http Gateway Route Match Example
  slug: app-mesh-http-gateway-route-match-example
- key_count: 1
  name: App Mesh Http Gateway Route Path Rewrite Example
  slug: app-mesh-http-gateway-route-path-rewrite-example
- key_count: 1
  name: App Mesh Http Gateway Route Prefix Example
  slug: app-mesh-http-gateway-route-prefix-example
- key_count: 2
  name: App Mesh Http Gateway Route Prefix Rewrite Example
  slug: app-mesh-http-gateway-route-prefix-rewrite-example
- key_count: 3
  name: App Mesh Http Gateway Route Rewrite Example
  slug: app-mesh-http-gateway-route-rewrite-example
- key_count: 1
  name: App Mesh Http Method Example
  slug: app-mesh-http-method-example
- key_count: 1
  name: App Mesh Http Path Exact Example
  slug: app-mesh-http-path-exact-example
- key_count: 2
  name: App Mesh Http Path Match Example
  slug: app-mesh-http-path-match-example
- key_count: 1
  name: App Mesh Http Path Regex Example
  slug: app-mesh-http-path-regex-example
- key_count: 2
  name: App Mesh Http Query Parameter Example
  slug: app-mesh-http-query-parameter-example
- key_count: 1
  name: App Mesh Http Query Parameters Example
  slug: app-mesh-http-query-parameters-example
- key_count: 1
  name: App Mesh Http Retry Policy Event Example
  slug: app-mesh-http-retry-policy-event-example
- key_count: 1
  name: App Mesh Http Retry Policy Events Example
  slug: app-mesh-http-retry-policy-events-example
- key_count: 4
  name: App Mesh Http Retry Policy Example
  slug: app-mesh-http-retry-policy-example
- key_count: 1
  name: App Mesh Http Route Action Example
  slug: app-mesh-http-route-action-example
- key_count: 4
  name: App Mesh Http Route Example
  slug: app-mesh-http-route-example
- key_count: 3
  name: App Mesh Http Route Header Example
  slug: app-mesh-http-route-header-example
- key_count: 1
  name: App Mesh Http Route Headers Example
  slug: app-mesh-http-route-headers-example
- key_count: 7
  name: App Mesh Http Route Match Example
  slug: app-mesh-http-route-match-example
- key_count: 1
  name: App Mesh Http Scheme Example
  slug: app-mesh-http-scheme-example
- key_count: 2
  name: App Mesh Http Timeout Example
  slug: app-mesh-http-timeout-example
- key_count: 1
  name: App Mesh Internal Server Error Exception Example
  slug: app-mesh-internal-server-error-exception-example
- key_count: 1
  name: App Mesh Ip Preference Example
  slug: app-mesh-ip-preference-example
- key_count: 1
  name: App Mesh Json Format Example
  slug: app-mesh-json-format-example
- key_count: 2
  name: App Mesh Json Format Ref Example
  slug: app-mesh-json-format-ref-example
- key_count: 1
  name: App Mesh Json Key Example
  slug: app-mesh-json-key-example
- key_count: 1
  name: App Mesh Json Value Example
  slug: app-mesh-json-value-example
- key_count: 1
  name: App Mesh Limit Exceeded Exception Example
  slug: app-mesh-limit-exceeded-exception-example
- key_count: 1
  name: App Mesh List Gateway Routes Input Example
  slug: app-mesh-list-gateway-routes-input-example
- key_count: 1
  name: App Mesh List Gateway Routes Limit Example
  slug: app-mesh-list-gateway-routes-limit-example
- key_count: 2
  name: App Mesh List Gateway Routes Output Example
  slug: app-mesh-list-gateway-routes-output-example
- key_count: 1
  name: App Mesh List Meshes Input Example
  slug: app-mesh-list-meshes-input-example
- key_count: 1
  name: App Mesh List Meshes Limit Example
  slug: app-mesh-list-meshes-limit-example
- key_count: 2
  name: App Mesh List Meshes Output Example
  slug: app-mesh-list-meshes-output-example
- key_count: 1
  name: App Mesh List Routes Input Example
  slug: app-mesh-list-routes-input-example
- key_count: 1
  name: App Mesh List Routes Limit Example
  slug: app-mesh-list-routes-limit-example
- key_count: 2
  name: App Mesh List Routes Output Example
  slug: app-mesh-list-routes-output-example
- key_count: 1
  name: App Mesh List Tags For Resource Input Example
  slug: app-mesh-list-tags-for-resource-input-example
- key_count: 2
  name: App Mesh List Tags For Resource Output Example
  slug: app-mesh-list-tags-for-resource-output-example
- key_count: 1
  name: App Mesh List Virtual Gateways Input Example
  slug: app-mesh-list-virtual-gateways-input-example
- key_count: 1
  name: App Mesh List Virtual Gateways Limit Example
  slug: app-mesh-list-virtual-gateways-limit-example
- key_count: 2
  name: App Mesh List Virtual Gateways Output Example
  slug: app-mesh-list-virtual-gateways-output-example
- key_count: 1
  name: App Mesh List Virtual Nodes Input Example
  slug: app-mesh-list-virtual-nodes-input-example
- key_count: 1
  name: App Mesh List Virtual Nodes Limit Example
  slug: app-mesh-list-virtual-nodes-limit-example
- key_count: 2
  name: App Mesh List Virtual Nodes Output Example
  slug: app-mesh-list-virtual-nodes-output-example
- key_count: 1
  name: App Mesh List Virtual Routers Input Example
  slug: app-mesh-list-virtual-routers-input-example
- key_count: 1
  name: App Mesh List Virtual Routers Limit Example
  slug: app-mesh-list-virtual-routers-limit-example
- key_count: 2
  name: App Mesh List Virtual Routers Output Example
  slug: app-mesh-list-virtual-routers-output-example
- key_count: 1
  name: App Mesh List Virtual Services Input Example
  slug: app-mesh-list-virtual-services-input-example
- key_count: 1
  name: App Mesh List Virtual Services Limit Example
  slug: app-mesh-list-virtual-services-limit-example
- key_count: 2
  name: App Mesh List Virtual Services Output Example
  slug: app-mesh-list-virtual-services-output-example
- key_count: 6
  name: App Mesh Listener Example
  slug: app-mesh-listener-example
- key_count: 1
  name: App Mesh Listener Port Example
  slug: app-mesh-listener-port-example
- key_count: 4
  name: App Mesh Listener Timeout Example
  slug: app-mesh-listener-timeout-example
- key_count: 1
  name: App Mesh Listener Tls Acm Certificate Example
  slug: app-mesh-listener-tls-acm-certificate-example
- key_count: 3
  name: App Mesh Listener Tls Certificate Example
  slug: app-mesh-listener-tls-certificate-example
- key_count: 3
  name: App Mesh Listener Tls Example
  slug: app-mesh-listener-tls-example
- key_count: 2
  name: App Mesh Listener Tls File Certificate Example
  slug: app-mesh-listener-tls-file-certificate-example
- key_count: 1
  name: App Mesh Listener Tls Mode Example
  slug: app-mesh-listener-tls-mode-example
- key_count: 1
  name: App Mesh Listener Tls Sds Certificate Example
  slug: app-mesh-listener-tls-sds-certificate-example
- key_count: 2
  name: App Mesh Listener Tls Validation Context Example
  slug: app-mesh-listener-tls-validation-context-example
- key_count: 2
  name: App Mesh Listener Tls Validation Context Trust Example
  slug: app-mesh-listener-tls-validation-context-trust-example
- key_count: 1
  name: App Mesh Listeners Example
  slug: app-mesh-listeners-example
- key_count: 1
  name: App Mesh Logging Example
  slug: app-mesh-logging-example
- key_count: 2
  name: App Mesh Logging Format Example
  slug: app-mesh-logging-format-example
- key_count: 1
  name: App Mesh Long Example
  slug: app-mesh-long-example
- key_count: 2
  name: App Mesh Match Range Example
  slug: app-mesh-match-range-example
- key_count: 1
  name: App Mesh Max Connections Example
  slug: app-mesh-max-connections-example
- key_count: 1
  name: App Mesh Max Pending Requests Example
  slug: app-mesh-max-pending-requests-example
- key_count: 1
  name: App Mesh Max Requests Example
  slug: app-mesh-max-requests-example
- key_count: 1
  name: App Mesh Max Retries Example
  slug: app-mesh-max-retries-example
- key_count: 4
  name: App Mesh Mesh Data Example
  slug: app-mesh-mesh-data-example
- key_count: 1
  name: App Mesh Mesh List Example
  slug: app-mesh-mesh-list-example
- key_count: 7
  name: App Mesh Mesh Ref Example
  slug: app-mesh-mesh-ref-example
- key_count: 1
  name: App Mesh Mesh Service Discovery Example
  slug: app-mesh-mesh-service-discovery-example
- key_count: 2
  name: App Mesh Mesh Spec Example
  slug: app-mesh-mesh-spec-example
- key_count: 1
  name: App Mesh Mesh Status Code Example
  slug: app-mesh-mesh-status-code-example
- key_count: 1
  name: App Mesh Mesh Status Example
  slug: app-mesh-mesh-status-example
- key_count: 1
  name: App Mesh Method Name Example
  slug: app-mesh-method-name-example
- key_count: 1
  name: App Mesh Not Found Exception Example
  slug: app-mesh-not-found-exception-example
- key_count: 4
  name: App Mesh Outlier Detection Example
  slug: app-mesh-outlier-detection-example
- key_count: 1
  name: App Mesh Outlier Detection Max Ejection Percent Example
  slug: app-mesh-outlier-detection-max-ejection-percent-example
- key_count: 1
  name: App Mesh Outlier Detection Max Server Errors Example
  slug: app-mesh-outlier-detection-max-server-errors-example
- key_count: 1
  name: App Mesh Percent Int Example
  slug: app-mesh-percent-int-example
- key_count: 2
  name: App Mesh Port Mapping Example
  slug: app-mesh-port-mapping-example
- key_count: 1
  name: App Mesh Port Number Example
  slug: app-mesh-port-number-example
- key_count: 1
  name: App Mesh Port Protocol Example
  slug: app-mesh-port-protocol-example
- key_count: 1
  name: App Mesh Port Set Example
  slug: app-mesh-port-set-example
- key_count: 1
  name: App Mesh Query Parameter Match Example
  slug: app-mesh-query-parameter-match-example
- key_count: 1
  name: App Mesh Query Parameter Name Example
  slug: app-mesh-query-parameter-name-example
- key_count: 1
  name: App Mesh Resource In Use Exception Example
  slug: app-mesh-resource-in-use-exception-example
- key_count: 7
  name: App Mesh Resource Metadata Example
  slug: app-mesh-resource-metadata-example
- key_count: 1
  name: App Mesh Resource Name Example
  slug: app-mesh-resource-name-example
- key_count: 6
  name: App Mesh Route Data Example
  slug: app-mesh-route-data-example
- key_count: 1
  name: App Mesh Route List Example
  slug: app-mesh-route-list-example
- key_count: 1
  name: App Mesh Route Priority Example
  slug: app-mesh-route-priority-example
- key_count: 9
  name: App Mesh Route Ref Example
  slug: app-mesh-route-ref-example
- key_count: 5
  name: App Mesh Route Spec Example
  slug: app-mesh-route-spec-example
- key_count: 1
  name: App Mesh Route Status Code Example
  slug: app-mesh-route-status-code-example
- key_count: 1
  name: App Mesh Route Status Example
  slug: app-mesh-route-status-example
- key_count: 1
  name: App Mesh Sds Secret Name Example
  slug: app-mesh-sds-secret-name-example
- key_count: 2
  name: App Mesh Service Discovery Example
  slug: app-mesh-service-discovery-example
- key_count: 1
  name: App Mesh Service Name Example
  slug: app-mesh-service-name-example
- key_count: 1
  name: App Mesh Service Unavailable Exception Example
  slug: app-mesh-service-unavailable-exception-example
- key_count: 1
  name: App Mesh String Example
  slug: app-mesh-string-example
- key_count: 1
  name: App Mesh Subject Alternative Name Example
  slug: app-mesh-subject-alternative-name-example
- key_count: 1
  name: App Mesh Subject Alternative Name List Example
  slug: app-mesh-subject-alternative-name-list-example
- key_count: 1
  name: App Mesh Subject Alternative Name Matchers Example
  slug: app-mesh-subject-alternative-name-matchers-example
- key_count: 1
  name: App Mesh Subject Alternative Names Example
  slug: app-mesh-subject-alternative-names-example
- key_count: 1
  name: App Mesh Suffix Hostname Example
  slug: app-mesh-suffix-hostname-example
- key_count: 1
  name: App Mesh Tag Key Example
  slug: app-mesh-tag-key-example
- key_count: 1
  name: App Mesh Tag Key List Example
  slug: app-mesh-tag-key-list-example
- key_count: 1
  name: App Mesh Tag List Example
  slug: app-mesh-tag-list-example
- key_count: 2
  name: App Mesh Tag Ref Example
  slug: app-mesh-tag-ref-example
- key_count: 1
  name: App Mesh Tag Resource Input Example
  slug: app-mesh-tag-resource-input-example
- key_count: 1
  name: App Mesh Tag Resource Output Example
  slug: app-mesh-tag-resource-output-example
- key_count: 1
  name: App Mesh Tag Value Example
  slug: app-mesh-tag-value-example
- key_count: 1
  name: App Mesh Tags Limit Example
  slug: app-mesh-tags-limit-example
- key_count: 1
  name: App Mesh Tcp Retry Policy Event Example
  slug: app-mesh-tcp-retry-policy-event-example
- key_count: 1
  name: App Mesh Tcp Retry Policy Events Example
  slug: app-mesh-tcp-retry-policy-events-example
- key_count: 1
  name: App Mesh Tcp Route Action Example
  slug: app-mesh-tcp-route-action-example
- key_count: 3
  name: App Mesh Tcp Route Example
  slug: app-mesh-tcp-route-example
- key_count: 1
  name: App Mesh Tcp Route Match Example
  slug: app-mesh-tcp-route-match-example
- key_count: 1
  name: App Mesh Tcp Timeout Example
  slug: app-mesh-tcp-timeout-example
- key_count: 1
  name: App Mesh Text Format Example
  slug: app-mesh-text-format-example
- key_count: 1
  name: App Mesh Timestamp Example
  slug: app-mesh-timestamp-example
- key_count: 1
  name: App Mesh Tls Validation Context Acm Trust Example
  slug: app-mesh-tls-validation-context-acm-trust-example
- key_count: 2
  name: App Mesh Tls Validation Context Example
  slug: app-mesh-tls-validation-context-example
- key_count: 1
  name: App Mesh Tls Validation Context File Trust Example
  slug: app-mesh-tls-validation-context-file-trust-example
- key_count: 1
  name: App Mesh Tls Validation Context Sds Trust Example
  slug: app-mesh-tls-validation-context-sds-trust-example
- key_count: 3
  name: App Mesh Tls Validation Context Trust Example
  slug: app-mesh-tls-validation-context-trust-example
- key_count: 1
  name: App Mesh Too Many Requests Exception Example
  slug: app-mesh-too-many-requests-exception-example
- key_count: 1
  name: App Mesh Too Many Tags Exception Example
  slug: app-mesh-too-many-tags-exception-example
- key_count: 1
  name: App Mesh Untag Resource Input Example
  slug: app-mesh-untag-resource-input-example
- key_count: 1
  name: App Mesh Untag Resource Output Example
  slug: app-mesh-untag-resource-output-example
- key_count: 2
  name: App Mesh Update Gateway Route Input Example
  slug: app-mesh-update-gateway-route-input-example
- key_count: 1
  name: App Mesh Update Gateway Route Output Example
  slug: app-mesh-update-gateway-route-output-example
- key_count: 2
  name: App Mesh Update Mesh Input Example
  slug: app-mesh-update-mesh-input-example
- key_count: 1
  name: App Mesh Update Mesh Output Example
  slug: app-mesh-update-mesh-output-example
- key_count: 2
  name: App Mesh Update Route Input Example
  slug: app-mesh-update-route-input-example
- key_count: 1
  name: App Mesh Update Route Output Example
  slug: app-mesh-update-route-output-example
- key_count: 2
  name: App Mesh Update Virtual Gateway Input Example
  slug: app-mesh-update-virtual-gateway-input-example
- key_count: 1
  name: App Mesh Update Virtual Gateway Output Example
  slug: app-mesh-update-virtual-gateway-output-example
- key_count: 2
  name: App Mesh Update Virtual Node Input Example
  slug: app-mesh-update-virtual-node-input-example
- key_count: 1
  name: App Mesh Update Virtual Node Output Example
  slug: app-mesh-update-virtual-node-output-example
- key_count: 2
  name: App Mesh Update Virtual Router Input Example
  slug: app-mesh-update-virtual-router-input-example
- key_count: 1
  name: App Mesh Update Virtual Router Output Example
  slug: app-mesh-update-virtual-router-output-example
- key_count: 2
  name: App Mesh Update Virtual Service Input Example
  slug: app-mesh-update-virtual-service-input-example
- key_count: 1
  name: App Mesh Update Virtual Service Output Example
  slug: app-mesh-update-virtual-service-output-example
- key_count: 1
  name: App Mesh Virtual Gateway Access Log Example
  slug: app-mesh-virtual-gateway-access-log-example
- key_count: 1
  name: App Mesh Virtual Gateway Backend Defaults Example
  slug: app-mesh-virtual-gateway-backend-defaults-example
- key_count: 1
  name: App Mesh Virtual Gateway Certificate Authority Arns Example
  slug: app-mesh-virtual-gateway-certificate-authority-arns-example
- key_count: 1
  name: App Mesh Virtual Gateway Client Policy Example
  slug: app-mesh-virtual-gateway-client-policy-example
- key_count: 4
  name: App Mesh Virtual Gateway Client Policy Tls Example
  slug: app-mesh-virtual-gateway-client-policy-tls-example
- key_count: 2
  name: App Mesh Virtual Gateway Client Tls Certificate Example
  slug: app-mesh-virtual-gateway-client-tls-certificate-example
- key_count: 3
  name: App Mesh Virtual Gateway Connection Pool Example
  slug: app-mesh-virtual-gateway-connection-pool-example
- key_count: 5
  name: App Mesh Virtual Gateway Data Example
  slug: app-mesh-virtual-gateway-data-example
- key_count: 2
  name: App Mesh Virtual Gateway File Access Log Example
  slug: app-mesh-virtual-gateway-file-access-log-example
- key_count: 1
  name: App Mesh Virtual Gateway Grpc Connection Pool Example
  slug: app-mesh-virtual-gateway-grpc-connection-pool-example
- key_count: 1
  name: App Mesh Virtual Gateway Health Check Interval Millis Example
  slug: app-mesh-virtual-gateway-health-check-interval-millis-example
- key_count: 7
  name: App Mesh Virtual Gateway Health Check Policy Example
  slug: app-mesh-virtual-gateway-health-check-policy-example
- key_count: 1
  name: App Mesh Virtual Gateway Health Check Threshold Example
  slug: app-mesh-virtual-gateway-health-check-threshold-example
- key_count: 1
  name: App Mesh Virtual Gateway Health Check Timeout Millis Example
  slug: app-mesh-virtual-gateway-health-check-timeout-millis-example
- key_count: 2
  name: App Mesh Virtual Gateway Http Connection Pool Example
  slug: app-mesh-virtual-gateway-http-connection-pool-example
- key_count: 1
  name: App Mesh Virtual Gateway Http2 Connection Pool Example
  slug: app-mesh-virtual-gateway-http2-connection-pool-example
- key_count: 1
  name: App Mesh Virtual Gateway List Example
  slug: app-mesh-virtual-gateway-list-example
- key_count: 4
  name: App Mesh Virtual Gateway Listener Example
  slug: app-mesh-virtual-gateway-listener-example
- key_count: 1
  name: App Mesh Virtual Gateway Listener Tls Acm Certificate Example
  slug: app-mesh-virtual-gateway-listener-tls-acm-certificate-example
- key_count: 3
  name: App Mesh Virtual Gateway Listener Tls Certificate Example
  slug: app-mesh-virtual-gateway-listener-tls-certificate-example
- key_count: 3
  name: App Mesh Virtual Gateway Listener Tls Example
  slug: app-mesh-virtual-gateway-listener-tls-example
- key_count: 2
  name: App Mesh Virtual Gateway Listener Tls File Certificate Example
  slug: app-mesh-virtual-gateway-listener-tls-file-certificate-example
- key_count: 1
  name: App Mesh Virtual Gateway Listener Tls Mode Example
  slug: app-mesh-virtual-gateway-listener-tls-mode-example
- key_count: 1
  name: App Mesh Virtual Gateway Listener Tls Sds Certificate Example
  slug: app-mesh-virtual-gateway-listener-tls-sds-certificate-example
- key_count: 2
  name: App Mesh Virtual Gateway Listener Tls Validation Context Example
  slug: app-mesh-virtual-gateway-listener-tls-validation-context-example
- key_count: 2
  name: App Mesh Virtual Gateway Listener Tls Validation Context Trust Example
  slug: app-mesh-virtual-gateway-listener-tls-validation-context-trust-example
- key_count: 1
  name: App Mesh Virtual Gateway Listeners Example
  slug: app-mesh-virtual-gateway-listeners-example
- key_count: 1
  name: App Mesh Virtual Gateway Logging Example
  slug: app-mesh-virtual-gateway-logging-example
- key_count: 2
  name: App Mesh Virtual Gateway Port Mapping Example
  slug: app-mesh-virtual-gateway-port-mapping-example
- key_count: 1
  name: App Mesh Virtual Gateway Port Protocol Example
  slug: app-mesh-virtual-gateway-port-protocol-example
- key_count: 8
  name: App Mesh Virtual Gateway Ref Example
  slug: app-mesh-virtual-gateway-ref-example
- key_count: 1
  name: App Mesh Virtual Gateway Sds Secret Name Example
  slug: app-mesh-virtual-gateway-sds-secret-name-example
- key_count: 3
  name: App Mesh Virtual Gateway Spec Example
  slug: app-mesh-virtual-gateway-spec-example
- key_count: 1
  name: App Mesh Virtual Gateway Status Code Example
  slug: app-mesh-virtual-gateway-status-code-example
- key_count: 1
  name: App Mesh Virtual Gateway Status Example
  slug: app-mesh-virtual-gateway-status-example
- key_count: 1
  name: App Mesh Virtual Gateway Tls Validation Context Acm Trust Example
  slug: app-mesh-virtual-gateway-tls-validation-context-acm-trust-example
- key_count: 2
  name: App Mesh Virtual Gateway Tls Validation Context Example
  slug: app-mesh-virtual-gateway-tls-validation-context-example
- key_count: 1
  name: App Mesh Virtual Gateway Tls Validation Context File Trust Example
  slug: app-mesh-virtual-gateway-tls-validation-context-file-trust-example
- key_count: 1
  name: App Mesh Virtual Gateway Tls Validation Context Sds Trust Example
  slug: app-mesh-virtual-gateway-tls-validation-context-sds-trust-example
- key_count: 3
  name: App Mesh Virtual Gateway Tls Validation Context Trust Example
  slug: app-mesh-virtual-gateway-tls-validation-context-trust-example
- key_count: 4
  name: App Mesh Virtual Node Connection Pool Example
  slug: app-mesh-virtual-node-connection-pool-example
- key_count: 5
  name: App Mesh Virtual Node Data Example
  slug: app-mesh-virtual-node-data-example
- key_count: 1
  name: App Mesh Virtual Node Grpc Connection Pool Example
  slug: app-mesh-virtual-node-grpc-connection-pool-example
- key_count: 2
  name: App Mesh Virtual Node Http Connection Pool Example
  slug: app-mesh-virtual-node-http-connection-pool-example
- key_count: 1
  name: App Mesh Virtual Node Http2 Connection Pool Example
  slug: app-mesh-virtual-node-http2-connection-pool-example
- key_count: 1
  name: App Mesh Virtual Node List Example
  slug: app-mesh-virtual-node-list-example
- key_count: 8
  name: App Mesh Virtual Node Ref Example
  slug: app-mesh-virtual-node-ref-example
- key_count: 1
  name: App Mesh Virtual Node Service Provider Example
  slug: app-mesh-virtual-node-service-provider-example
- key_count: 5
  name: App Mesh Virtual Node Spec Example
  slug: app-mesh-virtual-node-spec-example
- key_count: 1
  name: App Mesh Virtual Node Status Code Example
  slug: app-mesh-virtual-node-status-code-example
- key_count: 1
  name: App Mesh Virtual Node Status Example
  slug: app-mesh-virtual-node-status-example
- key_count: 1
  name: App Mesh Virtual Node Tcp Connection Pool Example
  slug: app-mesh-virtual-node-tcp-connection-pool-example
- key_count: 5
  name: App Mesh Virtual Router Data Example
  slug: app-mesh-virtual-router-data-example
- key_count: 1
  name: App Mesh Virtual Router List Example
  slug: app-mesh-virtual-router-list-example
- key_count: 1
  name: App Mesh Virtual Router Listener Example
  slug: app-mesh-virtual-router-listener-example
- key_count: 1
  name: App Mesh Virtual Router Listeners Example
  slug: app-mesh-virtual-router-listeners-example
- key_count: 8
  name: App Mesh Virtual Router Ref Example
  slug: app-mesh-virtual-router-ref-example
- key_count: 1
  name: App Mesh Virtual Router Service Provider Example
  slug: app-mesh-virtual-router-service-provider-example
- key_count: 1
  name: App Mesh Virtual Router Spec Example
  slug: app-mesh-virtual-router-spec-example
- key_count: 1
  name: App Mesh Virtual Router Status Code Example
  slug: app-mesh-virtual-router-status-code-example
- key_count: 1
  name: App Mesh Virtual Router Status Example
  slug: app-mesh-virtual-router-status-example
- key_count: 2
  name: App Mesh Virtual Service Backend Example
  slug: app-mesh-virtual-service-backend-example
- key_count: 5
  name: App Mesh Virtual Service Data Example
  slug: app-mesh-virtual-service-data-example
- key_count: 1
  name: App Mesh Virtual Service List Example
  slug: app-mesh-virtual-service-list-example
- key_count: 2
  name: App Mesh Virtual Service Provider Example
  slug: app-mesh-virtual-service-provider-example
- key_count: 8
  name: App Mesh Virtual Service Ref Example
  slug: app-mesh-virtual-service-ref-example
- key_count: 1
  name: App Mesh Virtual Service Spec Example
  slug: app-mesh-virtual-service-spec-example
- key_count: 1
  name: App Mesh Virtual Service Status Code Example
  slug: app-mesh-virtual-service-status-code-example
- key_count: 1
  name: App Mesh Virtual Service Status Example
  slug: app-mesh-virtual-service-status-example
- key_count: 3
  name: App Mesh Weighted Target Example
  slug: app-mesh-weighted-target-example
- key_count: 1
  name: App Mesh Weighted Targets Example
  slug: app-mesh-weighted-targets-example
features:
- description: Create and manage service meshes spanning Amazon ECS, EKS, EC2, and Fargate compute environments.
  name: Service Mesh Management
- description: Define virtual nodes representing actual services with listener ports, health checks, and service discovery backends.
  name: Virtual Node Configuration
- description: Configure virtual routers and routes for weighted routing, retry policies, and timeout configurations.
  name: Traffic Routing
- description: Automatically injects and manages Envoy sidecar proxies for transparent service-to-service communication.
  name: Envoy Proxy Integration
- description: Export metrics, logs, and traces from Envoy proxies to AWS CloudWatch, X-Ray, and third-party tools.
  name: Observability
- description: Enable mutual TLS encryption between services within the mesh for zero-trust networking.
  name: mTLS Encryption
- description: Configure ingress traffic from outside the mesh to virtual services using gateway routes.
  name: Virtual Gateways
- description: Share service meshes across AWS accounts using AWS Resource Access Manager.
  name: Multi-Account Mesh Sharing
finops:
- name: Aws App Mesh Finops
  service_category: API
  slug: aws-app-mesh-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/aws-app-mesh.png
json_schemas:
- name: AccessLog
  property_count: 1
  slug: app-mesh-access-log
- name: AccountId
  property_count: 0
  slug: app-mesh-account-id
- name: Arn
  property_count: 0
  slug: app-mesh-arn
- name: AwsCloudMapInstanceAttributeKey
  property_count: 0
  slug: app-mesh-aws-cloud-map-instance-attribute-key
- name: AwsCloudMapInstanceAttribute
  property_count: 2
  slug: app-mesh-aws-cloud-map-instance-attribute
- name: AwsCloudMapInstanceAttributeValue
  property_count: 0
  slug: app-mesh-aws-cloud-map-instance-attribute-value
- name: AwsCloudMapInstanceAttributes
  property_count: 0
  slug: app-mesh-aws-cloud-map-instance-attributes
- name: AwsCloudMapName
  property_count: 0
  slug: app-mesh-aws-cloud-map-name
- name: AwsCloudMapServiceDiscovery
  property_count: 4
  slug: app-mesh-aws-cloud-map-service-discovery
- name: BackendDefaults
  property_count: 1
  slug: app-mesh-backend-defaults
- name: Backend
  property_count: 1
  slug: app-mesh-backend
- name: Backends
  property_count: 0
  slug: app-mesh-backends
- name: BadRequestException
  property_count: 0
  slug: app-mesh-bad-request-exception
- name: Boolean
  property_count: 0
  slug: app-mesh-boolean
- name: CertificateAuthorityArns
  property_count: 0
  slug: app-mesh-certificate-authority-arns
- name: ClientPolicy
  property_count: 1
  slug: app-mesh-client-policy
- name: ClientPolicyTls
  property_count: 4
  slug: app-mesh-client-policy-tls
- name: ClientTlsCertificate
  property_count: 2
  slug: app-mesh-client-tls-certificate
- name: ConflictException
  property_count: 0
  slug: app-mesh-conflict-exception
- name: CreateGatewayRouteInput
  property_count: 4
  slug: app-mesh-create-gateway-route-input
- name: CreateGatewayRouteOutput
  property_count: 1
  slug: app-mesh-create-gateway-route-output
- name: CreateMeshInput
  property_count: 4
  slug: app-mesh-create-mesh-input
- name: CreateMeshOutput
  property_count: 1
  slug: app-mesh-create-mesh-output
- name: CreateRouteInput
  property_count: 4
  slug: app-mesh-create-route-input
- name: CreateRouteOutput
  property_count: 1
  slug: app-mesh-create-route-output
- name: CreateVirtualGatewayInput
  property_count: 4
  slug: app-mesh-create-virtual-gateway-input
- name: CreateVirtualGatewayOutput
  property_count: 1
  slug: app-mesh-create-virtual-gateway-output
- name: CreateVirtualNodeInput
  property_count: 4
  slug: app-mesh-create-virtual-node-input
- name: CreateVirtualNodeOutput
  property_count: 1
  slug: app-mesh-create-virtual-node-output
- name: CreateVirtualRouterInput
  property_count: 4
  slug: app-mesh-create-virtual-router-input
- name: CreateVirtualRouterOutput
  property_count: 1
  slug: app-mesh-create-virtual-router-output
- name: CreateVirtualServiceInput
  property_count: 4
  slug: app-mesh-create-virtual-service-input
- name: CreateVirtualServiceOutput
  property_count: 1
  slug: app-mesh-create-virtual-service-output
- name: DefaultGatewayRouteRewrite
  property_count: 0
  slug: app-mesh-default-gateway-route-rewrite
- name: DeleteGatewayRouteInput
  property_count: 0
  slug: app-mesh-delete-gateway-route-input
- name: DeleteGatewayRouteOutput
  property_count: 1
  slug: app-mesh-delete-gateway-route-output
- name: DeleteMeshInput
  property_count: 0
  slug: app-mesh-delete-mesh-input
- name: DeleteMeshOutput
  property_count: 1
  slug: app-mesh-delete-mesh-output
- name: DeleteRouteInput
  property_count: 0
  slug: app-mesh-delete-route-input
- name: DeleteRouteOutput
  property_count: 1
  slug: app-mesh-delete-route-output
- name: DeleteVirtualGatewayInput
  property_count: 0
  slug: app-mesh-delete-virtual-gateway-input
- name: DeleteVirtualGatewayOutput
  property_count: 1
  slug: app-mesh-delete-virtual-gateway-output
- name: DeleteVirtualNodeInput
  property_count: 0
  slug: app-mesh-delete-virtual-node-input
- name: DeleteVirtualNodeOutput
  property_count: 1
  slug: app-mesh-delete-virtual-node-output
- name: DeleteVirtualRouterInput
  property_count: 0
  slug: app-mesh-delete-virtual-router-input
- name: DeleteVirtualRouterOutput
  property_count: 1
  slug: app-mesh-delete-virtual-router-output
- name: DeleteVirtualServiceInput
  property_count: 0
  slug: app-mesh-delete-virtual-service-input
- name: DeleteVirtualServiceOutput
  property_count: 1
  slug: app-mesh-delete-virtual-service-output
- name: DescribeGatewayRouteInput
  property_count: 0
  slug: app-mesh-describe-gateway-route-input
- name: DescribeGatewayRouteOutput
  property_count: 1
  slug: app-mesh-describe-gateway-route-output
- name: DescribeMeshInput
  property_count: 0
  slug: app-mesh-describe-mesh-input
- name: DescribeMeshOutput
  property_count: 1
  slug: app-mesh-describe-mesh-output
- name: DescribeRouteInput
  property_count: 0
  slug: app-mesh-describe-route-input
- name: DescribeRouteOutput
  property_count: 1
  slug: app-mesh-describe-route-output
- name: DescribeVirtualGatewayInput
  property_count: 0
  slug: app-mesh-describe-virtual-gateway-input
- name: DescribeVirtualGatewayOutput
  property_count: 1
  slug: app-mesh-describe-virtual-gateway-output
- name: DescribeVirtualNodeInput
  property_count: 0
  slug: app-mesh-describe-virtual-node-input
- name: DescribeVirtualNodeOutput
  property_count: 1
  slug: app-mesh-describe-virtual-node-output
- name: DescribeVirtualRouterInput
  property_count: 0
  slug: app-mesh-describe-virtual-router-input
- name: DescribeVirtualRouterOutput
  property_count: 1
  slug: app-mesh-describe-virtual-router-output
- name: DescribeVirtualServiceInput
  property_count: 0
  slug: app-mesh-describe-virtual-service-input
- name: DescribeVirtualServiceOutput
  property_count: 1
  slug: app-mesh-describe-virtual-service-output
- name: DnsResponseType
  property_count: 0
  slug: app-mesh-dns-response-type
- name: DnsServiceDiscovery
  property_count: 3
  slug: app-mesh-dns-service-discovery
- name: Duration
  property_count: 2
  slug: app-mesh-duration
- name: DurationUnit
  property_count: 0
  slug: app-mesh-duration-unit
- name: DurationValue
  property_count: 0
  slug: app-mesh-duration-value
- name: EgressFilter
  property_count: 1
  slug: app-mesh-egress-filter
- name: EgressFilterType
  property_count: 0
  slug: app-mesh-egress-filter-type
- name: ExactHostName
  property_count: 0
  slug: app-mesh-exact-host-name
- name: FileAccessLog
  property_count: 2
  slug: app-mesh-file-access-log
- name: FilePath
  property_count: 0
  slug: app-mesh-file-path
- name: ForbiddenException
  property_count: 0
  slug: app-mesh-forbidden-exception
- name: GatewayRouteData
  property_count: 6
  slug: app-mesh-gateway-route-data
- name: GatewayRouteHostnameMatch
  property_count: 2
  slug: app-mesh-gateway-route-hostname-match
- name: GatewayRouteHostnameRewrite
  property_count: 1
  slug: app-mesh-gateway-route-hostname-rewrite
- name: GatewayRouteList
  property_count: 0
  slug: app-mesh-gateway-route-list
- name: GatewayRoutePriority
  property_count: 0
  slug: app-mesh-gateway-route-priority
- name: GatewayRouteRef
  property_count: 9
  slug: app-mesh-gateway-route-ref
- name: GatewayRouteSpec
  property_count: 4
  slug: app-mesh-gateway-route-spec
- name: GatewayRouteStatusCode
  property_count: 0
  slug: app-mesh-gateway-route-status-code
- name: GatewayRouteStatus
  property_count: 1
  slug: app-mesh-gateway-route-status
- name: GatewayRouteTarget
  property_count: 2
  slug: app-mesh-gateway-route-target
- name: GatewayRouteVirtualService
  property_count: 1
  slug: app-mesh-gateway-route-virtual-service
- name: GrpcGatewayRouteAction
  property_count: 2
  slug: app-mesh-grpc-gateway-route-action
- name: GrpcGatewayRouteMatch
  property_count: 4
  slug: app-mesh-grpc-gateway-route-match
- name: GrpcGatewayRouteMetadataList
  property_count: 0
  slug: app-mesh-grpc-gateway-route-metadata-list
- name: GrpcGatewayRouteMetadata
  property_count: 3
  slug: app-mesh-grpc-gateway-route-metadata
- name: GrpcGatewayRouteRewrite
  property_count: 1
  slug: app-mesh-grpc-gateway-route-rewrite
- name: GrpcGatewayRoute
  property_count: 2
  slug: app-mesh-grpc-gateway-route
- name: GrpcMetadataMatchMethod
  property_count: 5
  slug: app-mesh-grpc-metadata-match-method
- name: GrpcRetryPolicyEvent
  property_count: 0
  slug: app-mesh-grpc-retry-policy-event
- name: GrpcRetryPolicyEvents
  property_count: 0
  slug: app-mesh-grpc-retry-policy-events
- name: GrpcRetryPolicy
  property_count: 5
  slug: app-mesh-grpc-retry-policy
- name: GrpcRouteAction
  property_count: 1
  slug: app-mesh-grpc-route-action
- name: GrpcRouteMatch
  property_count: 4
  slug: app-mesh-grpc-route-match
- name: GrpcRouteMetadataList
  property_count: 0
  slug: app-mesh-grpc-route-metadata-list
- name: GrpcRouteMetadataMatchMethod
  property_count: 5
  slug: app-mesh-grpc-route-metadata-match-method
- name: GrpcRouteMetadata
  property_count: 3
  slug: app-mesh-grpc-route-metadata
- name: GrpcRoute
  property_count: 4
  slug: app-mesh-grpc-route
- name: GrpcTimeout
  property_count: 2
  slug: app-mesh-grpc-timeout
- name: HeaderMatchMethod
  property_count: 5
  slug: app-mesh-header-match-method
- name: HeaderMatch
  property_count: 0
  slug: app-mesh-header-match
- name: HeaderName
  property_count: 0
  slug: app-mesh-header-name
- name: HealthCheckIntervalMillis
  property_count: 0
  slug: app-mesh-health-check-interval-millis
- name: HealthCheckPolicy
  property_count: 7
  slug: app-mesh-health-check-policy
- name: HealthCheckThreshold
  property_count: 0
  slug: app-mesh-health-check-threshold
- name: HealthCheckTimeoutMillis
  property_count: 0
  slug: app-mesh-health-check-timeout-millis
- name: Hostname
  property_count: 0
  slug: app-mesh-hostname
- name: HttpGatewayRouteAction
  property_count: 2
  slug: app-mesh-http-gateway-route-action
- name: HttpGatewayRouteHeader
  property_count: 3
  slug: app-mesh-http-gateway-route-header
- name: HttpGatewayRouteHeaders
  property_count: 0
  slug: app-mesh-http-gateway-route-headers
- name: HttpGatewayRouteMatch
  property_count: 7
  slug: app-mesh-http-gateway-route-match
- name: HttpGatewayRoutePathRewrite
  property_count: 1
  slug: app-mesh-http-gateway-route-path-rewrite
- name: HttpGatewayRoutePrefixRewrite
  property_count: 2
  slug: app-mesh-http-gateway-route-prefix-rewrite
- name: HttpGatewayRoutePrefix
  property_count: 0
  slug: app-mesh-http-gateway-route-prefix
- name: HttpGatewayRouteRewrite
  property_count: 3
  slug: app-mesh-http-gateway-route-rewrite
- name: HttpGatewayRoute
  property_count: 2
  slug: app-mesh-http-gateway-route
- name: HttpMethod
  property_count: 0
  slug: app-mesh-http-method
- name: HttpPathExact
  property_count: 0
  slug: app-mesh-http-path-exact
- name: HttpPathMatch
  property_count: 2
  slug: app-mesh-http-path-match
- name: HttpPathRegex
  property_count: 0
  slug: app-mesh-http-path-regex
- name: HttpQueryParameter
  property_count: 2
  slug: app-mesh-http-query-parameter
- name: HttpQueryParameters
  property_count: 0
  slug: app-mesh-http-query-parameters
- name: HttpRetryPolicyEvent
  property_count: 0
  slug: app-mesh-http-retry-policy-event
- name: HttpRetryPolicyEvents
  property_count: 0
  slug: app-mesh-http-retry-policy-events
- name: HttpRetryPolicy
  property_count: 4
  slug: app-mesh-http-retry-policy
- name: HttpRouteAction
  property_count: 1
  slug: app-mesh-http-route-action
- name: HttpRouteHeader
  property_count: 3
  slug: app-mesh-http-route-header
- name: HttpRouteHeaders
  property_count: 0
  slug: app-mesh-http-route-headers
- name: HttpRouteMatch
  property_count: 7
  slug: app-mesh-http-route-match
- name: HttpRoute
  property_count: 4
  slug: app-mesh-http-route
- name: HttpScheme
  property_count: 0
  slug: app-mesh-http-scheme
- name: HttpTimeout
  property_count: 2
  slug: app-mesh-http-timeout
- name: InternalServerErrorException
  property_count: 0
  slug: app-mesh-internal-server-error-exception
- name: IpPreference
  property_count: 0
  slug: app-mesh-ip-preference
- name: JsonFormatRef
  property_count: 2
  slug: app-mesh-json-format-ref
- name: JsonFormat
  property_count: 0
  slug: app-mesh-json-format
- name: JsonKey
  property_count: 0
  slug: app-mesh-json-key
- name: JsonValue
  property_count: 0
  slug: app-mesh-json-value
- name: LimitExceededException
  property_count: 0
  slug: app-mesh-limit-exceeded-exception
- name: ListGatewayRoutesInput
  property_count: 0
  slug: app-mesh-list-gateway-routes-input
- name: ListGatewayRoutesLimit
  property_count: 0
  slug: app-mesh-list-gateway-routes-limit
- name: ListGatewayRoutesOutput
  property_count: 2
  slug: app-mesh-list-gateway-routes-output
- name: ListMeshesInput
  property_count: 0
  slug: app-mesh-list-meshes-input
- name: ListMeshesLimit
  property_count: 0
  slug: app-mesh-list-meshes-limit
- name: ListMeshesOutput
  property_count: 2
  slug: app-mesh-list-meshes-output
- name: ListRoutesInput
  property_count: 0
  slug: app-mesh-list-routes-input
- name: ListRoutesLimit
  property_count: 0
  slug: app-mesh-list-routes-limit
- name: ListRoutesOutput
  property_count: 2
  slug: app-mesh-list-routes-output
- name: ListTagsForResourceInput
  property_count: 0
  slug: app-mesh-list-tags-for-resource-input
- name: ListTagsForResourceOutput
  property_count: 2
  slug: app-mesh-list-tags-for-resource-output
- name: ListVirtualGatewaysInput
  property_count: 0
  slug: app-mesh-list-virtual-gateways-input
- name: ListVirtualGatewaysLimit
  property_count: 0
  slug: app-mesh-list-virtual-gateways-limit
- name: ListVirtualGatewaysOutput
  property_count: 2
  slug: app-mesh-list-virtual-gateways-output
- name: ListVirtualNodesInput
  property_count: 0
  slug: app-mesh-list-virtual-nodes-input
- name: ListVirtualNodesLimit
  property_count: 0
  slug: app-mesh-list-virtual-nodes-limit
- name: ListVirtualNodesOutput
  property_count: 2
  slug: app-mesh-list-virtual-nodes-output
- name: ListVirtualRoutersInput
  property_count: 0
  slug: app-mesh-list-virtual-routers-input
- name: ListVirtualRoutersLimit
  property_count: 0
  slug: app-mesh-list-virtual-routers-limit
- name: ListVirtualRoutersOutput
  property_count: 2
  slug: app-mesh-list-virtual-routers-output
- name: ListVirtualServicesInput
  property_count: 0
  slug: app-mesh-list-virtual-services-input
- name: ListVirtualServicesLimit
  property_count: 0
  slug: app-mesh-list-virtual-services-limit
- name: ListVirtualServicesOutput
  property_count: 2
  slug: app-mesh-list-virtual-services-output
- name: ListenerPort
  property_count: 0
  slug: app-mesh-listener-port
- name: Listener
  property_count: 6
  slug: app-mesh-listener
- name: ListenerTimeout
  property_count: 4
  slug: app-mesh-listener-timeout
- name: ListenerTlsAcmCertificate
  property_count: 1
  slug: app-mesh-listener-tls-acm-certificate
- name: ListenerTlsCertificate
  property_count: 3
  slug: app-mesh-listener-tls-certificate
- name: ListenerTlsFileCertificate
  property_count: 2
  slug: app-mesh-listener-tls-file-certificate
- name: ListenerTlsMode
  property_count: 0
  slug: app-mesh-listener-tls-mode
- name: ListenerTls
  property_count: 3
  slug: app-mesh-listener-tls
- name: ListenerTlsSdsCertificate
  property_count: 1
  slug: app-mesh-listener-tls-sds-certificate
- name: ListenerTlsValidationContext
  property_count: 2
  slug: app-mesh-listener-tls-validation-context
- name: ListenerTlsValidationContextTrust
  property_count: 2
  slug: app-mesh-listener-tls-validation-context-trust
- name: Listeners
  property_count: 0
  slug: app-mesh-listeners
- name: LoggingFormat
  property_count: 2
  slug: app-mesh-logging-format
- name: Logging
  property_count: 1
  slug: app-mesh-logging
- name: Long
  property_count: 0
  slug: app-mesh-long
- name: MatchRange
  property_count: 2
  slug: app-mesh-match-range
- name: MaxConnections
  property_count: 0
  slug: app-mesh-max-connections
- name: MaxPendingRequests
  property_count: 0
  slug: app-mesh-max-pending-requests
- name: MaxRequests
  property_count: 0
  slug: app-mesh-max-requests
- name: MaxRetries
  property_count: 0
  slug: app-mesh-max-retries
- name: MeshData
  property_count: 4
  slug: app-mesh-mesh-data
- name: MeshList
  property_count: 0
  slug: app-mesh-mesh-list
- name: MeshRef
  property_count: 7
  slug: app-mesh-mesh-ref
- name: MeshServiceDiscovery
  property_count: 1
  slug: app-mesh-mesh-service-discovery
- name: MeshSpec
  property_count: 2
  slug: app-mesh-mesh-spec
- name: MeshStatusCode
  property_count: 0
  slug: app-mesh-mesh-status-code
- name: MeshStatus
  property_count: 1
  slug: app-mesh-mesh-status
- name: MethodName
  property_count: 0
  slug: app-mesh-method-name
- name: NotFoundException
  property_count: 0
  slug: app-mesh-not-found-exception
- name: OutlierDetectionMaxEjectionPercent
  property_count: 0
  slug: app-mesh-outlier-detection-max-ejection-percent
- name: OutlierDetectionMaxServerErrors
  property_count: 0
  slug: app-mesh-outlier-detection-max-server-errors
- name: OutlierDetection
  property_count: 4
  slug: app-mesh-outlier-detection
- name: PercentInt
  property_count: 0
  slug: app-mesh-percent-int
- name: PortMapping
  property_count: 2
  slug: app-mesh-port-mapping
- name: PortNumber
  property_count: 0
  slug: app-mesh-port-number
- name: PortProtocol
  property_count: 0
  slug: app-mesh-port-protocol
- name: PortSet
  property_count: 0
  slug: app-mesh-port-set
- name: QueryParameterMatch
  property_count: 1
  slug: app-mesh-query-parameter-match
- name: QueryParameterName
  property_count: 0
  slug: app-mesh-query-parameter-name
- name: ResourceInUseException
  property_count: 0
  slug: app-mesh-resource-in-use-exception
- name: ResourceMetadata
  property_count: 7
  slug: app-mesh-resource-metadata
- name: ResourceName
  property_count: 0
  slug: app-mesh-resource-name
- name: RouteData
  property_count: 6
  slug: app-mesh-route-data
- name: RouteList
  property_count: 0
  slug: app-mesh-route-list
- name: RoutePriority
  property_count: 0
  slug: app-mesh-route-priority
- name: RouteRef
  property_count: 9
  slug: app-mesh-route-ref
- name: RouteSpec
  property_count: 5
  slug: app-mesh-route-spec
- name: RouteStatusCode
  property_count: 0
  slug: app-mesh-route-status-code
- name: RouteStatus
  property_count: 1
  slug: app-mesh-route-status
- name: SdsSecretName
  property_count: 0
  slug: app-mesh-sds-secret-name
- name: ServiceDiscovery
  property_count: 2
  slug: app-mesh-service-discovery
- name: ServiceName
  property_count: 0
  slug: app-mesh-service-name
- name: ServiceUnavailableException
  property_count: 0
  slug: app-mesh-service-unavailable-exception
- name: String
  property_count: 0
  slug: app-mesh-string
- name: SubjectAlternativeNameList
  property_count: 0
  slug: app-mesh-subject-alternative-name-list
- name: SubjectAlternativeNameMatchers
  property_count: 1
  slug: app-mesh-subject-alternative-name-matchers
- name: SubjectAlternativeName
  property_count: 0
  slug: app-mesh-subject-alternative-name
- name: SubjectAlternativeNames
  property_count: 1
  slug: app-mesh-subject-alternative-names
- name: SuffixHostname
  property_count: 0
  slug: app-mesh-suffix-hostname
- name: TagKeyList
  property_count: 0
  slug: app-mesh-tag-key-list
- name: TagKey
  property_count: 0
  slug: app-mesh-tag-key
- name: TagList
  property_count: 0
  slug: app-mesh-tag-list
- name: TagRef
  property_count: 2
  slug: app-mesh-tag-ref
- name: TagResourceInput
  property_count: 1
  slug: app-mesh-tag-resource-input
- name: TagResourceOutput
  property_count: 0
  slug: app-mesh-tag-resource-output
- name: TagValue
  property_count: 0
  slug: app-mesh-tag-value
- name: TagsLimit
  property_count: 0
  slug: app-mesh-tags-limit
- name: TcpRetryPolicyEvent
  property_count: 0
  slug: app-mesh-tcp-retry-policy-event
- name: TcpRetryPolicyEvents
  property_count: 0
  slug: app-mesh-tcp-retry-policy-events
- name: TcpRouteAction
  property_count: 1
  slug: app-mesh-tcp-route-action
- name: TcpRouteMatch
  property_count: 1
  slug: app-mesh-tcp-route-match
- name: TcpRoute
  property_count: 3
  slug: app-mesh-tcp-route
- name: TcpTimeout
  property_count: 1
  slug: app-mesh-tcp-timeout
- name: TextFormat
  property_count: 0
  slug: app-mesh-text-format
- name: Timestamp
  property_count: 0
  slug: app-mesh-timestamp
- name: TlsValidationContextAcmTrust
  property_count: 1
  slug: app-mesh-tls-validation-context-acm-trust
- name: TlsValidationContextFileTrust
  property_count: 1
  slug: app-mesh-tls-validation-context-file-trust
- name: TlsValidationContext
  property_count: 2
  slug: app-mesh-tls-validation-context
- name: TlsValidationContextSdsTrust
  property_count: 1
  slug: app-mesh-tls-validation-context-sds-trust
- name: TlsValidationContextTrust
  property_count: 3
  slug: app-mesh-tls-validation-context-trust
- name: TooManyRequestsException
  property_count: 0
  slug: app-mesh-too-many-requests-exception
- name: TooManyTagsException
  property_count: 0
  slug: app-mesh-too-many-tags-exception
- name: UntagResourceInput
  property_count: 1
  slug: app-mesh-untag-resource-input
- name: UntagResourceOutput
  property_count: 0
  slug: app-mesh-untag-resource-output
- name: UpdateGatewayRouteInput
  property_count: 2
  slug: app-mesh-update-gateway-route-input
- name: UpdateGatewayRouteOutput
  property_count: 1
  slug: app-mesh-update-gateway-route-output
- name: UpdateMeshInput
  property_count: 2
  slug: app-mesh-update-mesh-input
- name: UpdateMeshOutput
  property_count: 1
  slug: app-mesh-update-mesh-output
- name: UpdateRouteInput
  property_count: 2
  slug: app-mesh-update-route-input
- name: UpdateRouteOutput
  property_count: 1
  slug: app-mesh-update-route-output
- name: UpdateVirtualGatewayInput
  property_count: 2
  slug: app-mesh-update-virtual-gateway-input
- name: UpdateVirtualGatewayOutput
  property_count: 1
  slug: app-mesh-update-virtual-gateway-output
- name: UpdateVirtualNodeInput
  property_count: 2
  slug: app-mesh-update-virtual-node-input
- name: UpdateVirtualNodeOutput
  property_count: 1
  slug: app-mesh-update-virtual-node-output
- name: UpdateVirtualRouterInput
  property_count: 2
  slug: app-mesh-update-virtual-router-input
- name: UpdateVirtualRouterOutput
  property_count: 1
  slug: app-mesh-update-virtual-router-output
- name: UpdateVirtualServiceInput
  property_count: 2
  slug: app-mesh-update-virtual-service-input
- name: UpdateVirtualServiceOutput
  property_count: 1
  slug: app-mesh-update-virtual-service-output
- name: VirtualGatewayAccessLog
  property_count: 1
  slug: app-mesh-virtual-gateway-access-log
- name: VirtualGatewayBackendDefaults
  property_count: 1
  slug: app-mesh-virtual-gateway-backend-defaults
- name: VirtualGatewayCertificateAuthorityArns
  property_count: 0
  slug: app-mesh-virtual-gateway-certificate-authority-arns
- name: VirtualGatewayClientPolicy
  property_count: 1
  slug: app-mesh-virtual-gateway-client-policy
- name: VirtualGatewayClientPolicyTls
  property_count: 4
  slug: app-mesh-virtual-gateway-client-policy-tls
- name: VirtualGatewayClientTlsCertificate
  property_count: 2
  slug: app-mesh-virtual-gateway-client-tls-certificate
- name: VirtualGatewayConnectionPool
  property_count: 3
  slug: app-mesh-virtual-gateway-connection-pool
- name: VirtualGatewayData
  property_count: 5
  slug: app-mesh-virtual-gateway-data
- name: VirtualGatewayFileAccessLog
  property_count: 2
  slug: app-mesh-virtual-gateway-file-access-log
- name: VirtualGatewayGrpcConnectionPool
  property_count: 1
  slug: app-mesh-virtual-gateway-grpc-connection-pool
- name: VirtualGatewayHealthCheckIntervalMillis
  property_count: 0
  slug: app-mesh-virtual-gateway-health-check-interval-millis
- name: VirtualGatewayHealthCheckPolicy
  property_count: 7
  slug: app-mesh-virtual-gateway-health-check-policy
- name: VirtualGatewayHealthCheckThreshold
  property_count: 0
  slug: app-mesh-virtual-gateway-health-check-threshold
- name: VirtualGatewayHealthCheckTimeoutMillis
  property_count: 0
  slug: app-mesh-virtual-gateway-health-check-timeout-millis
- name: VirtualGatewayHttpConnectionPool
  property_count: 2
  slug: app-mesh-virtual-gateway-http-connection-pool
- name: VirtualGatewayHttp2ConnectionPool
  property_count: 1
  slug: app-mesh-virtual-gateway-http2-connection-pool
- name: VirtualGatewayList
  property_count: 0
  slug: app-mesh-virtual-gateway-list
- name: VirtualGatewayListener
  property_count: 4
  slug: app-mesh-virtual-gateway-listener
- name: VirtualGatewayListenerTlsAcmCertificate
  property_count: 1
  slug: app-mesh-virtual-gateway-listener-tls-acm-certificate
- name: VirtualGatewayListenerTlsCertificate
  property_count: 3
  slug: app-mesh-virtual-gateway-listener-tls-certificate
- name: VirtualGatewayListenerTlsFileCertificate
  property_count: 2
  slug: app-mesh-virtual-gateway-listener-tls-file-certificate
- name: VirtualGatewayListenerTlsMode
  property_count: 0
  slug: app-mesh-virtual-gateway-listener-tls-mode
- name: VirtualGatewayListenerTls
  property_count: 3
  slug: app-mesh-virtual-gateway-listener-tls
- name: VirtualGatewayListenerTlsSdsCertificate
  property_count: 1
  slug: app-mesh-virtual-gateway-listener-tls-sds-certificate
- name: VirtualGatewayListenerTlsValidationContext
  property_count: 2
  slug: app-mesh-virtual-gateway-listener-tls-validation-context
- name: VirtualGatewayListenerTlsValidationContextTrust
  property_count: 2
  slug: app-mesh-virtual-gateway-listener-tls-validation-context-trust
- name: VirtualGatewayListeners
  property_count: 0
  slug: app-mesh-virtual-gateway-listeners
- name: VirtualGatewayLogging
  property_count: 1
  slug: app-mesh-virtual-gateway-logging
- name: VirtualGatewayPortMapping
  property_count: 2
  slug: app-mesh-virtual-gateway-port-mapping
- name: VirtualGatewayPortProtocol
  property_count: 0
  slug: app-mesh-virtual-gateway-port-protocol
- name: VirtualGatewayRef
  property_count: 8
  slug: app-mesh-virtual-gateway-ref
- name: VirtualGatewaySdsSecretName
  property_count: 0
  slug: app-mesh-virtual-gateway-sds-secret-name
- name: VirtualGatewaySpec
  property_count: 3
  slug: app-mesh-virtual-gateway-spec
- name: VirtualGatewayStatusCode
  property_count: 0
  slug: app-mesh-virtual-gateway-status-code
- name: VirtualGatewayStatus
  property_count: 1
  slug: app-mesh-virtual-gateway-status
- name: VirtualGatewayTlsValidationContextAcmTrust
  property_count: 1
  slug: app-mesh-virtual-gateway-tls-validation-context-acm-trust
- name: VirtualGatewayTlsValidationContextFileTrust
  property_count: 1
  slug: app-mesh-virtual-gateway-tls-validation-context-file-trust
- name: VirtualGatewayTlsValidationContext
  property_count: 2
  slug: app-mesh-virtual-gateway-tls-validation-context
- name: VirtualGatewayTlsValidationContextSdsTrust
  property_count: 1
  slug: app-mesh-virtual-gateway-tls-validation-context-sds-trust
- name: VirtualGatewayTlsValidationContextTrust
  property_count: 3
  slug: app-mesh-virtual-gateway-tls-validation-context-trust
- name: VirtualNodeConnectionPool
  property_count: 4
  slug: app-mesh-virtual-node-connection-pool
- name: VirtualNodeData
  property_count: 5
  slug: app-mesh-virtual-node-data
- name: VirtualNodeGrpcConnectionPool
  property_count: 1
  slug: app-mesh-virtual-node-grpc-connection-pool
- name: VirtualNodeHttpConnectionPool
  property_count: 2
  slug: app-mesh-virtual-node-http-connection-pool
- name: VirtualNodeHttp2ConnectionPool
  property_count: 1
  slug: app-mesh-virtual-node-http2-connection-pool
- name: VirtualNodeList
  property_count: 0
  slug: app-mesh-virtual-node-list
- name: VirtualNodeRef
  property_count: 8
  slug: app-mesh-virtual-node-ref
- name: VirtualNodeServiceProvider
  property_count: 1
  slug: app-mesh-virtual-node-service-provider
- name: VirtualNodeSpec
  property_count: 5
  slug: app-mesh-virtual-node-spec
- name: VirtualNodeStatusCode
  property_count: 0
  slug: app-mesh-virtual-node-status-code
- name: VirtualNodeStatus
  property_count: 1
  slug: app-mesh-virtual-node-status
- name: VirtualNodeTcpConnectionPool
  property_count: 1
  slug: app-mesh-virtual-node-tcp-connection-pool
- name: VirtualRouterData
  property_count: 5
  slug: app-mesh-virtual-router-data
- name: VirtualRouterList
  property_count: 0
  slug: app-mesh-virtual-router-list
- name: VirtualRouterListener
  property_count: 1
  slug: app-mesh-virtual-router-listener
- name: VirtualRouterListeners
  property_count: 0
  slug: app-mesh-virtual-router-listeners
- name: VirtualRouterRef
  property_count: 8
  slug: app-mesh-virtual-router-ref
- name: VirtualRouterServiceProvider
  property_count: 1
  slug: app-mesh-virtual-router-service-provider
- name: VirtualRouterSpec
  property_count: 1
  slug: app-mesh-virtual-router-spec
- name: VirtualRouterStatusCode
  property_count: 0
  slug: app-mesh-virtual-router-status-code
- name: VirtualRouterStatus
  property_count: 1
  slug: app-mesh-virtual-router-status
- name: VirtualServiceBackend
  property_count: 2
  slug: app-mesh-virtual-service-backend
- name: VirtualServiceData
  property_count: 5
  slug: app-mesh-virtual-service-data
- name: VirtualServiceList
  property_count: 0
  slug: app-mesh-virtual-service-list
- name: VirtualServiceProvider
  property_count: 2
  slug: app-mesh-virtual-service-provider
- name: VirtualServiceRef
  property_count: 8
  slug: app-mesh-virtual-service-ref
- name: VirtualServiceSpec
  property_count: 1
  slug: app-mesh-virtual-service-spec
- name: VirtualServiceStatusCode
  property_count: 0
  slug: app-mesh-virtual-service-status-code
- name: VirtualServiceStatus
  property_count: 1
  slug: app-mesh-virtual-service-status
- name: WeightedTarget
  property_count: 3
  slug: app-mesh-weighted-target
- name: WeightedTargets
  property_count: 0
  slug: app-mesh-weighted-targets
json_structures:
- name: App Mesh Access Log Structure
  property_count: 1
  slug: app-mesh-access-log-structure
- name: App Mesh Account Id Structure
  property_count: 0
  slug: app-mesh-account-id-structure
- name: App Mesh Arn Structure
  property_count: 0
  slug: app-mesh-arn-structure
- name: App Mesh Aws Cloud Map Instance Attribute Key Structure
  property_count: 0
  slug: app-mesh-aws-cloud-map-instance-attribute-key-structure
- name: App Mesh Aws Cloud Map Instance Attribute Structure
  property_count: 2
  slug: app-mesh-aws-cloud-map-instance-attribute-structure
- name: App Mesh Aws Cloud Map Instance Attribute Value Structure
  property_count: 0
  slug: app-mesh-aws-cloud-map-instance-attribute-value-structure
- name: App Mesh Aws Cloud Map Instance Attributes Structure
  property_count: 0
  slug: app-mesh-aws-cloud-map-instance-attributes-structure
- name: App Mesh Aws Cloud Map Name Structure
  property_count: 0
  slug: app-mesh-aws-cloud-map-name-structure
- name: App Mesh Aws Cloud Map Service Discovery Structure
  property_count: 4
  slug: app-mesh-aws-cloud-map-service-discovery-structure
- name: App Mesh Backend Defaults Structure
  property_count: 1
  slug: app-mesh-backend-defaults-structure
- name: App Mesh Backend Structure
  property_count: 1
  slug: app-mesh-backend-structure
- name: App Mesh Backends Structure
  property_count: 0
  slug: app-mesh-backends-structure
- name: App Mesh Bad Request Exception Structure
  property_count: 0
  slug: app-mesh-bad-request-exception-structure
- name: App Mesh Boolean Structure
  property_count: 0
  slug: app-mesh-boolean-structure
- name: App Mesh Certificate Authority Arns Structure
  property_count: 0
  slug: app-mesh-certificate-authority-arns-structure
- name: App Mesh Client Policy Structure
  property_count: 1
  slug: app-mesh-client-policy-structure
- name: App Mesh Client Policy Tls Structure
  property_count: 4
  slug: app-mesh-client-policy-tls-structure
- name: App Mesh Client Tls Certificate Structure
  property_count: 2
  slug: app-mesh-client-tls-certificate-structure
- name: App Mesh Conflict Exception Structure
  property_count: 0
  slug: app-mesh-conflict-exception-structure
- name: App Mesh Create Gateway Route Input Structure
  property_count: 4
  slug: app-mesh-create-gateway-route-input-structure
- name: App Mesh Create Gateway Route Output Structure
  property_count: 1
  slug: app-mesh-create-gateway-route-output-structure
- name: App Mesh Create Mesh Input Structure
  property_count: 4
  slug: app-mesh-create-mesh-input-structure
- name: App Mesh Create Mesh Output Structure
  property_count: 1
  slug: app-mesh-create-mesh-output-structure
- name: App Mesh Create Route Input Structure
  property_count: 4
  slug: app-mesh-create-route-input-structure
- name: App Mesh Create Route Output Structure
  property_count: 1
  slug: app-mesh-create-route-output-structure
- name: App Mesh Create Virtual Gateway Input Structure
  property_count: 4
  slug: app-mesh-create-virtual-gateway-input-structure
- name: App Mesh Create Virtual Gateway Output Structure
  property_count: 1
  slug: app-mesh-create-virtual-gateway-output-structure
- name: App Mesh Create Virtual Node Input Structure
  property_count: 4
  slug: app-mesh-create-virtual-node-input-structure
- name: App Mesh Create Virtual Node Output Structure
  property_count: 1
  slug: app-mesh-create-virtual-node-output-structure
- name: App Mesh Create Virtual Router Input Structure
  property_count: 4
  slug: app-mesh-create-virtual-router-input-structure
- name: App Mesh Create Virtual Router Output Structure
  property_count: 1
  slug: app-mesh-create-virtual-router-output-structure
- name: App Mesh Create Virtual Service Input Structure
  property_count: 4
  slug: app-mesh-create-virtual-service-input-structure
- name: App Mesh Create Virtual Service Output Structure
  property_count: 1
  slug: app-mesh-create-virtual-service-output-structure
- name: App Mesh Default Gateway Route Rewrite Structure
  property_count: 0
  slug: app-mesh-default-gateway-route-rewrite-structure
- name: App Mesh Delete Gateway Route Input Structure
  property_count: 0
  slug: app-mesh-delete-gateway-route-input-structure
- name: App Mesh Delete Gateway Route Output Structure
  property_count: 1
  slug: app-mesh-delete-gateway-route-output-structure
- name: App Mesh Delete Mesh Input Structure
  property_count: 0
  slug: app-mesh-delete-mesh-input-structure
- name: App Mesh Delete Mesh Output Structure
  property_count: 1
  slug: app-mesh-delete-mesh-output-structure
- name: App Mesh Delete Route Input Structure
  property_count: 0
  slug: app-mesh-delete-route-input-structure
- name: App Mesh Delete Route Output Structure
  property_count: 1
  slug: app-mesh-delete-route-output-structure
- name: App Mesh Delete Virtual Gateway Input Structure
  property_count: 0
  slug: app-mesh-delete-virtual-gateway-input-structure
- name: App Mesh Delete Virtual Gateway Output Structure
  property_count: 1
  slug: app-mesh-delete-virtual-gateway-output-structure
- name: App Mesh Delete Virtual Node Input Structure
  property_count: 0
  slug: app-mesh-delete-virtual-node-input-structure
- name: App Mesh Delete Virtual Node Output Structure
  property_count: 1
  slug: app-mesh-delete-virtual-node-output-structure
- name: App Mesh Delete Virtual Router Input Structure
  property_count: 0
  slug: app-mesh-delete-virtual-router-input-structure
- name: App Mesh Delete Virtual Router Output Structure
  property_count: 1
  slug: app-mesh-delete-virtual-router-output-structure
- name: App Mesh Delete Virtual Service Input Structure
  property_count: 0
  slug: app-mesh-delete-virtual-service-input-structure
- name: App Mesh Delete Virtual Service Output Structure
  property_count: 1
  slug: app-mesh-delete-virtual-service-output-structure
- name: App Mesh Describe Gateway Route Input Structure
  property_count: 0
  slug: app-mesh-describe-gateway-route-input-structure
- name: App Mesh Describe Gateway Route Output Structure
  property_count: 1
  slug: app-mesh-describe-gateway-route-output-structure
- name: App Mesh Describe Mesh Input Structure
  property_count: 0
  slug: app-mesh-describe-mesh-input-structure
- name: App Mesh Describe Mesh Output Structure
  property_count: 1
  slug: app-mesh-describe-mesh-output-structure
- name: App Mesh Describe Route Input Structure
  property_count: 0
  slug: app-mesh-describe-route-input-structure
- name: App Mesh Describe Route Output Structure
  property_count: 1
  slug: app-mesh-describe-route-output-structure
- name: App Mesh Describe Virtual Gateway Input Structure
  property_count: 0
  slug: app-mesh-describe-virtual-gateway-input-structure
- name: App Mesh Describe Virtual Gateway Output Structure
  property_count: 1
  slug: app-mesh-describe-virtual-gateway-output-structure
- name: App Mesh Describe Virtual Node Input Structure
  property_count: 0
  slug: app-mesh-describe-virtual-node-input-structure
- name: App Mesh Describe Virtual Node Output Structure
  property_count: 1
  slug: app-mesh-describe-virtual-node-output-structure
- name: App Mesh Describe Virtual Router Input Structure
  property_count: 0
  slug: app-mesh-describe-virtual-router-input-structure
- name: App Mesh Describe Virtual Router Output Structure
  property_count: 1
  slug: app-mesh-describe-virtual-router-output-structure
- name: App Mesh Describe Virtual Service Input Structure
  property_count: 0
  slug: app-mesh-describe-virtual-service-input-structure
- name: App Mesh Describe Virtual Service Output Structure
  property_count: 1
  slug: app-mesh-describe-virtual-service-output-structure
- name: App Mesh Dns Response Type Structure
  property_count: 0
  slug: app-mesh-dns-response-type-structure
- name: App Mesh Dns Service Discovery Structure
  property_count: 3
  slug: app-mesh-dns-service-discovery-structure
- name: App Mesh Duration Structure
  property_count: 2
  slug: app-mesh-duration-structure
- name: App Mesh Duration Unit Structure
  property_count: 0
  slug: app-mesh-duration-unit-structure
- name: App Mesh Duration Value Structure
  property_count: 0
  slug: app-mesh-duration-value-structure
- name: App Mesh Egress Filter Structure
  property_count: 1
  slug: app-mesh-egress-filter-structure
- name: App Mesh Egress Filter Type Structure
  property_count: 0
  slug: app-mesh-egress-filter-type-structure
- name: App Mesh Exact Host Name Structure
  property_count: 0
  slug: app-mesh-exact-host-name-structure
- name: App Mesh File Access Log Structure
  property_count: 2
  slug: app-mesh-file-access-log-structure
- name: App Mesh File Path Structure
  property_count: 0
  slug: app-mesh-file-path-structure
- name: App Mesh Forbidden Exception Structure
  property_count: 0
  slug: app-mesh-forbidden-exception-structure
- name: App Mesh Gateway Route Data Structure
  property_count: 6
  slug: app-mesh-gateway-route-data-structure
- name: App Mesh Gateway Route Hostname Match Structure
  property_count: 2
  slug: app-mesh-gateway-route-hostname-match-structure
- name: App Mesh Gateway Route Hostname Rewrite Structure
  property_count: 1
  slug: app-mesh-gateway-route-hostname-rewrite-structure
- name: App Mesh Gateway Route List Structure
  property_count: 0
  slug: app-mesh-gateway-route-list-structure
- name: App Mesh Gateway Route Priority Structure
  property_count: 0
  slug: app-mesh-gateway-route-priority-structure
- name: App Mesh Gateway Route Ref Structure
  property_count: 9
  slug: app-mesh-gateway-route-ref-structure
- name: App Mesh Gateway Route Spec Structure
  property_count: 4
  slug: app-mesh-gateway-route-spec-structure
- name: App Mesh Gateway Route Status Code Structure
  property_count: 0
  slug: app-mesh-gateway-route-status-code-structure
- name: App Mesh Gateway Route Status Structure
  property_count: 1
  slug: app-mesh-gateway-route-status-structure
- name: App Mesh Gateway Route Target Structure
  property_count: 2
  slug: app-mesh-gateway-route-target-structure
- name: App Mesh Gateway Route Virtual Service Structure
  property_count: 1
  slug: app-mesh-gateway-route-virtual-service-structure
- name: App Mesh Grpc Gateway Route Action Structure
  property_count: 2
  slug: app-mesh-grpc-gateway-route-action-structure
- name: App Mesh Grpc Gateway Route Match Structure
  property_count: 4
  slug: app-mesh-grpc-gateway-route-match-structure
- name: App Mesh Grpc Gateway Route Metadata List Structure
  property_count: 0
  slug: app-mesh-grpc-gateway-route-metadata-list-structure
- name: App Mesh Grpc Gateway Route Metadata Structure
  property_count: 3
  slug: app-mesh-grpc-gateway-route-metadata-structure
- name: App Mesh Grpc Gateway Route Rewrite Structure
  property_count: 1
  slug: app-mesh-grpc-gateway-route-rewrite-structure
- name: App Mesh Grpc Gateway Route Structure
  property_count: 2
  slug: app-mesh-grpc-gateway-route-structure
- name: App Mesh Grpc Metadata Match Method Structure
  property_count: 5
  slug: app-mesh-grpc-metadata-match-method-structure
- name: App Mesh Grpc Retry Policy Event Structure
  property_count: 0
  slug: app-mesh-grpc-retry-policy-event-structure
- name: App Mesh Grpc Retry Policy Events Structure
  property_count: 0
  slug: app-mesh-grpc-retry-policy-events-structure
- name: App Mesh Grpc Retry Policy Structure
  property_count: 5
  slug: app-mesh-grpc-retry-policy-structure
- name: App Mesh Grpc Route Action Structure
  property_count: 1
  slug: app-mesh-grpc-route-action-structure
- name: App Mesh Grpc Route Match Structure
  property_count: 4
  slug: app-mesh-grpc-route-match-structure
- name: App Mesh Grpc Route Metadata List Structure
  property_count: 0
  slug: app-mesh-grpc-route-metadata-list-structure
- name: App Mesh Grpc Route Metadata Match Method Structure
  property_count: 5
  slug: app-mesh-grpc-route-metadata-match-method-structure
- name: App Mesh Grpc Route Metadata Structure
  property_count: 3
  slug: app-mesh-grpc-route-metadata-structure
- name: App Mesh Grpc Route Structure
  property_count: 4
  slug: app-mesh-grpc-route-structure
- name: App Mesh Grpc Timeout Structure
  property_count: 2
  slug: app-mesh-grpc-timeout-structure
- name: App Mesh Header Match Method Structure
  property_count: 5
  slug: app-mesh-header-match-method-structure
- name: App Mesh Header Match Structure
  property_count: 0
  slug: app-mesh-header-match-structure
- name: App Mesh Header Name Structure
  property_count: 0
  slug: app-mesh-header-name-structure
- name: App Mesh Health Check Interval Millis Structure
  property_count: 0
  slug: app-mesh-health-check-interval-millis-structure
- name: App Mesh Health Check Policy Structure
  property_count: 7
  slug: app-mesh-health-check-policy-structure
- name: App Mesh Health Check Threshold Structure
  property_count: 0
  slug: app-mesh-health-check-threshold-structure
- name: App Mesh Health Check Timeout Millis Structure
  property_count: 0
  slug: app-mesh-health-check-timeout-millis-structure
- name: App Mesh Hostname Structure
  property_count: 0
  slug: app-mesh-hostname-structure
- name: App Mesh Http Gateway Route Action Structure
  property_count: 2
  slug: app-mesh-http-gateway-route-action-structure
- name: App Mesh Http Gateway Route Header Structure
  property_count: 3
  slug: app-mesh-http-gateway-route-header-structure
- name: App Mesh Http Gateway Route Headers Structure
  property_count: 0
  slug: app-mesh-http-gateway-route-headers-structure
- name: App Mesh Http Gateway Route Match Structure
  property_count: 7
  slug: app-mesh-http-gateway-route-match-structure
- name: App Mesh Http Gateway Route Path Rewrite Structure
  property_count: 1
  slug: app-mesh-http-gateway-route-path-rewrite-structure
- name: App Mesh Http Gateway Route Prefix Rewrite Structure
  property_count: 2
  slug: app-mesh-http-gateway-route-prefix-rewrite-structure
- name: App Mesh Http Gateway Route Prefix Structure
  property_count: 0
  slug: app-mesh-http-gateway-route-prefix-structure
- name: App Mesh Http Gateway Route Rewrite Structure
  property_count: 3
  slug: app-mesh-http-gateway-route-rewrite-structure
- name: App Mesh Http Gateway Route Structure
  property_count: 2
  slug: app-mesh-http-gateway-route-structure
- name: App Mesh Http Method Structure
  property_count: 0
  slug: app-mesh-http-method-structure
- name: App Mesh Http Path Exact Structure
  property_count: 0
  slug: app-mesh-http-path-exact-structure
- name: App Mesh Http Path Match Structure
  property_count: 2
  slug: app-mesh-http-path-match-structure
- name: App Mesh Http Path Regex Structure
  property_count: 0
  slug: app-mesh-http-path-regex-structure
- name: App Mesh Http Query Parameter Structure
  property_count: 2
  slug: app-mesh-http-query-parameter-structure
- name: App Mesh Http Query Parameters Structure
  property_count: 0
  slug: app-mesh-http-query-parameters-structure
- name: App Mesh Http Retry Policy Event Structure
  property_count: 0
  slug: app-mesh-http-retry-policy-event-structure
- name: App Mesh Http Retry Policy Events Structure
  property_count: 0
  slug: app-mesh-http-retry-policy-events-structure
- name: App Mesh Http Retry Policy Structure
  property_count: 4
  slug: app-mesh-http-retry-policy-structure
- name: App Mesh Http Route Action Structure
  property_count: 1
  slug: app-mesh-http-route-action-structure
- name: App Mesh Http Route Header Structure
  property_count: 3
  slug: app-mesh-http-route-header-structure
- name: App Mesh Http Route Headers Structure
  property_count: 0
  slug: app-mesh-http-route-headers-structure
- name: App Mesh Http Route Match Structure
  property_count: 7
  slug: app-mesh-http-route-match-structure
- name: App Mesh Http Route Structure
  property_count: 4
  slug: app-mesh-http-route-structure
- name: App Mesh Http Scheme Structure
  property_count: 0
  slug: app-mesh-http-scheme-structure
- name: App Mesh Http Timeout Structure
  property_count: 2
  slug: app-mesh-http-timeout-structure
- name: App Mesh Internal Server Error Exception Structure
  property_count: 0
  slug: app-mesh-internal-server-error-exception-structure
- name: App Mesh Ip Preference Structure
  property_count: 0
  slug: app-mesh-ip-preference-structure
- name: App Mesh Json Format Ref Structure
  property_count: 2
  slug: app-mesh-json-format-ref-structure
- name: App Mesh Json Format Structure
  property_count: 0
  slug: app-mesh-json-format-structure
- name: App Mesh Json Key Structure
  property_count: 0
  slug: app-mesh-json-key-structure
- name: App Mesh Json Value Structure
  property_count: 0
  slug: app-mesh-json-value-structure
- name: App Mesh Limit Exceeded Exception Structure
  property_count: 0
  slug: app-mesh-limit-exceeded-exception-structure
- name: App Mesh List Gateway Routes Input Structure
  property_count: 0
  slug: app-mesh-list-gateway-routes-input-structure
- name: App Mesh List Gateway Routes Limit Structure
  property_count: 0
  slug: app-mesh-list-gateway-routes-limit-structure
- name: App Mesh List Gateway Routes Output Structure
  property_count: 2
  slug: app-mesh-list-gateway-routes-output-structure
- name: App Mesh List Meshes Input Structure
  property_count: 0
  slug: app-mesh-list-meshes-input-structure
- name: App Mesh List Meshes Limit Structure
  property_count: 0
  slug: app-mesh-list-meshes-limit-structure
- name: App Mesh List Meshes Output Structure
  property_count: 2
  slug: app-mesh-list-meshes-output-structure
- name: App Mesh List Routes Input Structure
  property_count: 0
  slug: app-mesh-list-routes-input-structure
- name: App Mesh List Routes Limit Structure
  property_count: 0
  slug: app-mesh-list-routes-limit-structure
- name: App Mesh List Routes Output Structure
  property_count: 2
  slug: app-mesh-list-routes-output-structure
- name: App Mesh List Tags For Resource Input Structure
  property_count: 0
  slug: app-mesh-list-tags-for-resource-input-structure
- name: App Mesh List Tags For Resource Output Structure
  property_count: 2
  slug: app-mesh-list-tags-for-resource-output-structure
- name: App Mesh List Virtual Gateways Input Structure
  property_count: 0
  slug: app-mesh-list-virtual-gateways-input-structure
- name: App Mesh List Virtual Gateways Limit Structure
  property_count: 0
  slug: app-mesh-list-virtual-gateways-limit-structure
- name: App Mesh List Virtual Gateways Output Structure
  property_count: 2
  slug: app-mesh-list-virtual-gateways-output-structure
- name: App Mesh List Virtual Nodes Input Structure
  property_count: 0
  slug: app-mesh-list-virtual-nodes-input-structure
- name: App Mesh List Virtual Nodes Limit Structure
  property_count: 0
  slug: app-mesh-list-virtual-nodes-limit-structure
- name: App Mesh List Virtual Nodes Output Structure
  property_count: 2
  slug: app-mesh-list-virtual-nodes-output-structure
- name: App Mesh List Virtual Routers Input Structure
  property_count: 0
  slug: app-mesh-list-virtual-routers-input-structure
- name: App Mesh List Virtual Routers Limit Structure
  property_count: 0
  slug: app-mesh-list-virtual-routers-limit-structure
- name: App Mesh List Virtual Routers Output Structure
  property_count: 2
  slug: app-mesh-list-virtual-routers-output-structure
- name: App Mesh List Virtual Services Input Structure
  property_count: 0
  slug: app-mesh-list-virtual-services-input-structure
- name: App Mesh List Virtual Services Limit Structure
  property_count: 0
  slug: app-mesh-list-virtual-services-limit-structure
- name: App Mesh List Virtual Services Output Structure
  property_count: 2
  slug: app-mesh-list-virtual-services-output-structure
- name: App Mesh Listener Port Structure
  property_count: 0
  slug: app-mesh-listener-port-structure
- name: App Mesh Listener Structure
  property_count: 6
  slug: app-mesh-listener-structure
- name: App Mesh Listener Timeout Structure
  property_count: 4
  slug: app-mesh-listener-timeout-structure
- name: App Mesh Listener Tls Acm Certificate Structure
  property_count: 1
  slug: app-mesh-listener-tls-acm-certificate-structure
- name: App Mesh Listener Tls Certificate Structure
  property_count: 3
  slug: app-mesh-listener-tls-certificate-structure
- name: App Mesh Listener Tls File Certificate Structure
  property_count: 2
  slug: app-mesh-listener-tls-file-certificate-structure
- name: App Mesh Listener Tls Mode Structure
  property_count: 0
  slug: app-mesh-listener-tls-mode-structure
- name: App Mesh Listener Tls Sds Certificate Structure
  property_count: 1
  slug: app-mesh-listener-tls-sds-certificate-structure
- name: App Mesh Listener Tls Structure
  property_count: 3
  slug: app-mesh-listener-tls-structure
- name: App Mesh Listener Tls Validation Context Structure
  property_count: 2
  slug: app-mesh-listener-tls-validation-context-structure
- name: App Mesh Listener Tls Validation Context Trust Structure
  property_count: 2
  slug: app-mesh-listener-tls-validation-context-trust-structure
- name: App Mesh Listeners Structure
  property_count: 0
  slug: app-mesh-listeners-structure
- name: App Mesh Logging Format Structure
  property_count: 2
  slug: app-mesh-logging-format-structure
- name: App Mesh Logging Structure
  property_count: 1
  slug: app-mesh-logging-structure
- name: App Mesh Long Structure
  property_count: 0
  slug: app-mesh-long-structure
- name: App Mesh Match Range Structure
  property_count: 2
  slug: app-mesh-match-range-structure
- name: App Mesh Max Connections Structure
  property_count: 0
  slug: app-mesh-max-connections-structure
- name: App Mesh Max Pending Requests Structure
  property_count: 0
  slug: app-mesh-max-pending-requests-structure
- name: App Mesh Max Requests Structure
  property_count: 0
  slug: app-mesh-max-requests-structure
- name: App Mesh Max Retries Structure
  property_count: 0
  slug: app-mesh-max-retries-structure
- name: App Mesh Mesh Data Structure
  property_count: 4
  slug: app-mesh-mesh-data-structure
- name: App Mesh Mesh List Structure
  property_count: 0
  slug: app-mesh-mesh-list-structure
- name: App Mesh Mesh Ref Structure
  property_count: 7
  slug: app-mesh-mesh-ref-structure
- name: App Mesh Mesh Service Discovery Structure
  property_count: 1
  slug: app-mesh-mesh-service-discovery-structure
- name: App Mesh Mesh Spec Structure
  property_count: 2
  slug: app-mesh-mesh-spec-structure
- name: App Mesh Mesh Status Code Structure
  property_count: 0
  slug: app-mesh-mesh-status-code-structure
- name: App Mesh Mesh Status Structure
  property_count: 1
  slug: app-mesh-mesh-status-structure
- name: App Mesh Method Name Structure
  property_count: 0
  slug: app-mesh-method-name-structure
- name: App Mesh Not Found Exception Structure
  property_count: 0
  slug: app-mesh-not-found-exception-structure
- name: App Mesh Outlier Detection Max Ejection Percent Structure
  property_count: 0
  slug: app-mesh-outlier-detection-max-ejection-percent-structure
- name: App Mesh Outlier Detection Max Server Errors Structure
  property_count: 0
  slug: app-mesh-outlier-detection-max-server-errors-structure
- name: App Mesh Outlier Detection Structure
  property_count: 4
  slug: app-mesh-outlier-detection-structure
- name: App Mesh Percent Int Structure
  property_count: 0
  slug: app-mesh-percent-int-structure
- name: App Mesh Port Mapping Structure
  property_count: 2
  slug: app-mesh-port-mapping-structure
- name: App Mesh Port Number Structure
  property_count: 0
  slug: app-mesh-port-number-structure
- name: App Mesh Port Protocol Structure
  property_count: 0
  slug: app-mesh-port-protocol-structure
- name: App Mesh Port Set Structure
  property_count: 0
  slug: app-mesh-port-set-structure
- name: App Mesh Query Parameter Match Structure
  property_count: 1
  slug: app-mesh-query-parameter-match-structure
- name: App Mesh Query Parameter Name Structure
  property_count: 0
  slug: app-mesh-query-parameter-name-structure
- name: App Mesh Resource In Use Exception Structure
  property_count: 0
  slug: app-mesh-resource-in-use-exception-structure
- name: App Mesh Resource Metadata Structure
  property_count: 7
  slug: app-mesh-resource-metadata-structure
- name: App Mesh Resource Name Structure
  property_count: 0
  slug: app-mesh-resource-name-structure
- name: App Mesh Route Data Structure
  property_count: 6
  slug: app-mesh-route-data-structure
- name: App Mesh Route List Structure
  property_count: 0
  slug: app-mesh-route-list-structure
- name: App Mesh Route Priority Structure
  property_count: 0
  slug: app-mesh-route-priority-structure
- name: App Mesh Route Ref Structure
  property_count: 9
  slug: app-mesh-route-ref-structure
- name: App Mesh Route Spec Structure
  property_count: 5
  slug: app-mesh-route-spec-structure
- name: App Mesh Route Status Code Structure
  property_count: 0
  slug: app-mesh-route-status-code-structure
- name: App Mesh Route Status Structure
  property_count: 1
  slug: app-mesh-route-status-structure
- name: App Mesh Sds Secret Name Structure
  property_count: 0
  slug: app-mesh-sds-secret-name-structure
- name: App Mesh Service Discovery Structure
  property_count: 2
  slug: app-mesh-service-discovery-structure
- name: App Mesh Service Name Structure
  property_count: 0
  slug: app-mesh-service-name-structure
- name: App Mesh Service Unavailable Exception Structure
  property_count: 0
  slug: app-mesh-service-unavailable-exception-structure
- name: App Mesh String Structure
  property_count: 0
  slug: app-mesh-string-structure
- name: App Mesh Subject Alternative Name List Structure
  property_count: 0
  slug: app-mesh-subject-alternative-name-list-structure
- name: App Mesh Subject Alternative Name Matchers Structure
  property_count: 1
  slug: app-mesh-subject-alternative-name-matchers-structure
- name: App Mesh Subject Alternative Name Structure
  property_count: 0
  slug: app-mesh-subject-alternative-name-structure
- name: App Mesh Subject Alternative Names Structure
  property_count: 1
  slug: app-mesh-subject-alternative-names-structure
- name: App Mesh Suffix Hostname Structure
  property_count: 0
  slug: app-mesh-suffix-hostname-structure
- name: App Mesh Tag Key List Structure
  property_count: 0
  slug: app-mesh-tag-key-list-structure
- name: App Mesh Tag Key Structure
  property_count: 0
  slug: app-mesh-tag-key-structure
- name: App Mesh Tag List Structure
  property_count: 0
  slug: app-mesh-tag-list-structure
- name: App Mesh Tag Ref Structure
  property_count: 2
  slug: app-mesh-tag-ref-structure
- name: App Mesh Tag Resource Input Structure
  property_count: 1
  slug: app-mesh-tag-resource-input-structure
- name: App Mesh Tag Resource Output Structure
  property_count: 0
  slug: app-mesh-tag-resource-output-structure
- name: App Mesh Tag Value Structure
  property_count: 0
  slug: app-mesh-tag-value-structure
- name: App Mesh Tags Limit Structure
  property_count: 0
  slug: app-mesh-tags-limit-structure
- name: App Mesh Tcp Retry Policy Event Structure
  property_count: 0
  slug: app-mesh-tcp-retry-policy-event-structure
- name: App Mesh Tcp Retry Policy Events Structure
  property_count: 0
  slug: app-mesh-tcp-retry-policy-events-structure
- name: App Mesh Tcp Route Action Structure
  property_count: 1
  slug: app-mesh-tcp-route-action-structure
- name: App Mesh Tcp Route Match Structure
  property_count: 1
  slug: app-mesh-tcp-route-match-structure
- name: App Mesh Tcp Route Structure
  property_count: 3
  slug: app-mesh-tcp-route-structure
- name: App Mesh Tcp Timeout Structure
  property_count: 1
  slug: app-mesh-tcp-timeout-structure
- name: App Mesh Text Format Structure
  property_count: 0
  slug: app-mesh-text-format-structure
- name: App Mesh Timestamp Structure
  property_count: 0
  slug: app-mesh-timestamp-structure
- name: App Mesh Tls Validation Context Acm Trust Structure
  property_count: 1
  slug: app-mesh-tls-validation-context-acm-trust-structure
- name: App Mesh Tls Validation Context File Trust Structure
  property_count: 1
  slug: app-mesh-tls-validation-context-file-trust-structure
- name: App Mesh Tls Validation Context Sds Trust Structure
  property_count: 1
  slug: app-mesh-tls-validation-context-sds-trust-structure
- name: App Mesh Tls Validation Context Structure
  property_count: 2
  slug: app-mesh-tls-validation-context-structure
- name: App Mesh Tls Validation Context Trust Structure
  property_count: 3
  slug: app-mesh-tls-validation-context-trust-structure
- name: App Mesh Too Many Requests Exception Structure
  property_count: 0
  slug: app-mesh-too-many-requests-exception-structure
- name: App Mesh Too Many Tags Exception Structure
  property_count: 0
  slug: app-mesh-too-many-tags-exception-structure
- name: App Mesh Untag Resource Input Structure
  property_count: 1
  slug: app-mesh-untag-resource-input-structure
- name: App Mesh Untag Resource Output Structure
  property_count: 0
  slug: app-mesh-untag-resource-output-structure
- name: App Mesh Update Gateway Route Input Structure
  property_count: 2
  slug: app-mesh-update-gateway-route-input-structure
- name: App Mesh Update Gateway Route Output Structure
  property_count: 1
  slug: app-mesh-update-gateway-route-output-structure
- name: App Mesh Update Mesh Input Structure
  property_count: 2
  slug: app-mesh-update-mesh-input-structure
- name: App Mesh Update Mesh Output Structure
  property_count: 1
  slug: app-mesh-update-mesh-output-structure
- name: App Mesh Update Route Input Structure
  property_count: 2
  slug: app-mesh-update-route-input-structure
- name: App Mesh Update Route Output Structure
  property_count: 1
  slug: app-mesh-update-route-output-structure
- name: App Mesh Update Virtual Gateway Input Structure
  property_count: 2
  slug: app-mesh-update-virtual-gateway-input-structure
- name: App Mesh Update Virtual Gateway Output Structure
  property_count: 1
  slug: app-mesh-update-virtual-gateway-output-structure
- name: App Mesh Update Virtual Node Input Structure
  property_count: 2
  slug: app-mesh-update-virtual-node-input-structure
- name: App Mesh Update Virtual Node Output Structure
  property_count: 1
  slug: app-mesh-update-virtual-node-output-structure
- name: App Mesh Update Virtual Router Input Structure
  property_count: 2
  slug: app-mesh-update-virtual-router-input-structure
- name: App Mesh Update Virtual Router Output Structure
  property_count: 1
  slug: app-mesh-update-virtual-router-output-structure
- name: App Mesh Update Virtual Service Input Structure
  property_count: 2
  slug: app-mesh-update-virtual-service-input-structure
- name: App Mesh Update Virtual Service Output Structure
  property_count: 1
  slug: app-mesh-update-virtual-service-output-structure
- name: App Mesh Virtual Gateway Access Log Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-access-log-structure
- name: App Mesh Virtual Gateway Backend Defaults Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-backend-defaults-structure
- name: App Mesh Virtual Gateway Certificate Authority Arns Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-certificate-authority-arns-structure
- name: App Mesh Virtual Gateway Client Policy Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-client-policy-structure
- name: App Mesh Virtual Gateway Client Policy Tls Structure
  property_count: 4
  slug: app-mesh-virtual-gateway-client-policy-tls-structure
- name: App Mesh Virtual Gateway Client Tls Certificate Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-client-tls-certificate-structure
- name: App Mesh Virtual Gateway Connection Pool Structure
  property_count: 3
  slug: app-mesh-virtual-gateway-connection-pool-structure
- name: App Mesh Virtual Gateway Data Structure
  property_count: 5
  slug: app-mesh-virtual-gateway-data-structure
- name: App Mesh Virtual Gateway File Access Log Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-file-access-log-structure
- name: App Mesh Virtual Gateway Grpc Connection Pool Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-grpc-connection-pool-structure
- name: App Mesh Virtual Gateway Health Check Interval Millis Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-health-check-interval-millis-structure
- name: App Mesh Virtual Gateway Health Check Policy Structure
  property_count: 7
  slug: app-mesh-virtual-gateway-health-check-policy-structure
- name: App Mesh Virtual Gateway Health Check Threshold Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-health-check-threshold-structure
- name: App Mesh Virtual Gateway Health Check Timeout Millis Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-health-check-timeout-millis-structure
- name: App Mesh Virtual Gateway Http Connection Pool Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-http-connection-pool-structure
- name: App Mesh Virtual Gateway Http2 Connection Pool Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-http2-connection-pool-structure
- name: App Mesh Virtual Gateway List Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-list-structure
- name: App Mesh Virtual Gateway Listener Structure
  property_count: 4
  slug: app-mesh-virtual-gateway-listener-structure
- name: App Mesh Virtual Gateway Listener Tls Acm Certificate Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-listener-tls-acm-certificate-structure
- name: App Mesh Virtual Gateway Listener Tls Certificate Structure
  property_count: 3
  slug: app-mesh-virtual-gateway-listener-tls-certificate-structure
- name: App Mesh Virtual Gateway Listener Tls File Certificate Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-listener-tls-file-certificate-structure
- name: App Mesh Virtual Gateway Listener Tls Mode Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-listener-tls-mode-structure
- name: App Mesh Virtual Gateway Listener Tls Sds Certificate Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-listener-tls-sds-certificate-structure
- name: App Mesh Virtual Gateway Listener Tls Structure
  property_count: 3
  slug: app-mesh-virtual-gateway-listener-tls-structure
- name: App Mesh Virtual Gateway Listener Tls Validation Context Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-listener-tls-validation-context-structure
- name: App Mesh Virtual Gateway Listener Tls Validation Context Trust Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-listener-tls-validation-context-trust-structure
- name: App Mesh Virtual Gateway Listeners Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-listeners-structure
- name: App Mesh Virtual Gateway Logging Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-logging-structure
- name: App Mesh Virtual Gateway Port Mapping Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-port-mapping-structure
- name: App Mesh Virtual Gateway Port Protocol Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-port-protocol-structure
- name: App Mesh Virtual Gateway Ref Structure
  property_count: 8
  slug: app-mesh-virtual-gateway-ref-structure
- name: App Mesh Virtual Gateway Sds Secret Name Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-sds-secret-name-structure
- name: App Mesh Virtual Gateway Spec Structure
  property_count: 3
  slug: app-mesh-virtual-gateway-spec-structure
- name: App Mesh Virtual Gateway Status Code Structure
  property_count: 0
  slug: app-mesh-virtual-gateway-status-code-structure
- name: App Mesh Virtual Gateway Status Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-status-structure
- name: App Mesh Virtual Gateway Tls Validation Context Acm Trust Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-tls-validation-context-acm-trust-structure
- name: App Mesh Virtual Gateway Tls Validation Context File Trust Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-tls-validation-context-file-trust-structure
- name: App Mesh Virtual Gateway Tls Validation Context Sds Trust Structure
  property_count: 1
  slug: app-mesh-virtual-gateway-tls-validation-context-sds-trust-structure
- name: App Mesh Virtual Gateway Tls Validation Context Structure
  property_count: 2
  slug: app-mesh-virtual-gateway-tls-validation-context-structure
- name: App Mesh Virtual Gateway Tls Validation Context Trust Structure
  property_count: 3
  slug: app-mesh-virtual-gateway-tls-validation-context-trust-structure
- name: App Mesh Virtual Node Connection Pool Structure
  property_count: 4
  slug: app-mesh-virtual-node-connection-pool-structure
- name: App Mesh Virtual Node Data Structure
  property_count: 5
  slug: app-mesh-virtual-node-data-structure
- name: App Mesh Virtual Node Grpc Connection Pool Structure
  property_count: 1
  slug: app-mesh-virtual-node-grpc-connection-pool-structure
- name: App Mesh Virtual Node Http Connection Pool Structure
  property_count: 2
  slug: app-mesh-virtual-node-http-connection-pool-structure
- name: App Mesh Virtual Node Http2 Connection Pool Structure
  property_count: 1
  slug: app-mesh-virtual-node-http2-connection-pool-structure
- name: App Mesh Virtual Node List Structure
  property_count: 0
  slug: app-mesh-virtual-node-list-structure
- name: App Mesh Virtual Node Ref Structure
  property_count: 8
  slug: app-mesh-virtual-node-ref-structure
- name: App Mesh Virtual Node Service Provider Structure
  property_count: 1
  slug: app-mesh-virtual-node-service-provider-structure
- name: App Mesh Virtual Node Spec Structure
  property_count: 5
  slug: app-mesh-virtual-node-spec-structure
- name: App Mesh Virtual Node Status Code Structure
  property_count: 0
  slug: app-mesh-virtual-node-status-code-structure
- name: App Mesh Virtual Node Status Structure
  property_count: 1
  slug: app-mesh-virtual-node-status-structure
- name: App Mesh Virtual Node Tcp Connection Pool Structure
  property_count: 1
  slug: app-mesh-virtual-node-tcp-connection-pool-structure
- name: App Mesh Virtual Router Data Structure
  property_count: 5
  slug: app-mesh-virtual-router-data-structure
- name: App Mesh Virtual Router List Structure
  property_count: 0
  slug: app-mesh-virtual-router-list-structure
- name: App Mesh Virtual Router Listener Structure
  property_count: 1
  slug: app-mesh-virtual-router-listener-structure
- name: App Mesh Virtual Router Listeners Structure
  property_count: 0
  slug: app-mesh-virtual-router-listeners-structure
- name: App Mesh Virtual Router Ref Structure
  property_count: 8
  slug: app-mesh-virtual-router-ref-structure
- name: App Mesh Virtual Router Service Provider Structure
  property_count: 1
  slug: app-mesh-virtual-router-service-provider-structure
- name: App Mesh Virtual Router Spec Structure
  property_count: 1
  slug: app-mesh-virtual-router-spec-structure
- name: App Mesh Virtual Router Status Code Structure
  property_count: 0
  slug: app-mesh-virtual-router-status-code-structure
- name: App Mesh Virtual Router Status Structure
  property_count: 1
  slug: app-mesh-virtual-router-status-structure
- name: App Mesh Virtual Service Backend Structure
  property_count: 2
  slug: app-mesh-virtual-service-backend-structure
- name: App Mesh Virtual Service Data Structure
  property_count: 5
  slug: app-mesh-virtual-service-data-structure
- name: App Mesh Virtual Service List Structure
  property_count: 0
  slug: app-mesh-virtual-service-list-structure
- name: App Mesh Virtual Service Provider Structure
  property_count: 2
  slug: app-mesh-virtual-service-provider-structure
- name: App Mesh Virtual Service Ref Structure
  property_count: 8
  slug: app-mesh-virtual-service-ref-structure
- name: App Mesh Virtual Service Spec Structure
  property_count: 1
  slug: app-mesh-virtual-service-spec-structure
- name: App Mesh Virtual Service Status Code Structure
  property_count: 0
  slug: app-mesh-virtual-service-status-code-structure
- name: App Mesh Virtual Service Status Structure
  property_count: 1
  slug: app-mesh-virtual-service-status-structure
- name: App Mesh Weighted Target Structure
  property_count: 3
  slug: app-mesh-weighted-target-structure
- name: App Mesh Weighted Targets Structure
  property_count: 0
  slug: app-mesh-weighted-targets-structure
jsonld:
- class_count: 2
  name: Aws App Mesh Aws Context
  property_count: 6
  slug: aws-app-mesh-aws-context
- class_count: 14
  name: Aws App Mesh Create Context
  property_count: 17
  slug: aws-app-mesh-create-context
- class_count: 14
  name: Aws App Mesh Describe Context
  property_count: 7
  slug: aws-app-mesh-describe-context
- class_count: 1
  name: Aws App Mesh Egress Context
  property_count: 1
  slug: aws-app-mesh-egress-context
- class_count: 9
  name: Aws App Mesh Gateway Context
  property_count: 21
  slug: aws-app-mesh-gateway-context
- class_count: 14
  name: Aws App Mesh Grpc Context
  property_count: 25
  slug: aws-app-mesh-grpc-context
- class_count: 16
  name: Aws App Mesh Http Context
  property_count: 26
  slug: aws-app-mesh-http-context
- class_count: 16
  name: Aws App Mesh List Context
  property_count: 9
  slug: aws-app-mesh-list-context
- class_count: 9
  name: Aws App Mesh Listener Context
  property_count: 22
  slug: aws-app-mesh-listener-context
- class_count: 2
  name: Aws App Mesh Logging Context
  property_count: 3
  slug: aws-app-mesh-logging-context
- class_count: 6
  name: Aws App Mesh Mesh Context
  property_count: 12
  slug: aws-app-mesh-mesh-context
- class_count: 1
  name: Aws App Mesh Port Context
  property_count: 2
  slug: aws-app-mesh-port-context
- class_count: 5
  name: Aws App Mesh Route Context
  property_count: 16
  slug: aws-app-mesh-route-context
- class_count: 3
  name: Aws App Mesh Tag Context
  property_count: 3
  slug: aws-app-mesh-tag-context
- class_count: 4
  name: Aws App Mesh Tcp Context
  property_count: 6
  slug: aws-app-mesh-tcp-context
- class_count: 5
  name: Aws App Mesh Tls Context
  property_count: 8
  slug: aws-app-mesh-tls-context
- class_count: 2
  name: Aws App Mesh Untag Context
  property_count: 1
  slug: aws-app-mesh-untag-context
- class_count: 14
  name: Aws App Mesh Update Context
  property_count: 9
  slug: aws-app-mesh-update-context
- class_count: 53
  name: Aws App Mesh Virtual Context
  property_count: 57
  slug: aws-app-mesh-virtual-context
- class_count: 1
  name: Aws App Mesh Weighted Context
  property_count: 3
  slug: aws-app-mesh-weighted-context
layout: provider
modified: '2026-05-19'
name: AWS App Mesh
nav: Providers
network: true
overview: 'AWS App Mesh publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Meshes API, Tag#resourceArn API, Tags#resourceArn API, and 1 more. Tagged areas include Deprecated, Envoy, Microservices, Networking, and Service Mesh.


  The AWS App Mesh catalog on APIs.io includes 20 JSON-LD contexts and 2 Spectral governance rulesets.


  AWS App Mesh''s developer surface includes authentication, documentation, getting-started guide, pricing, FAQ, developer console, support, and 12 more developer resources.'
plans:
- name: Aws App Mesh Plans Pricing
  plan_count: 3
  slug: aws-app-mesh-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 5
  name: Aws App Mesh Rate Limits
  slug: aws-app-mesh-rate-limits
rules:
- name: AWS App Mesh API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: aws-app-mesh-jsonschema-spectral-rules
- name: AWS App Mesh API Rules
  rule_count: 24
  severity_counts:
    error: 11
    hint: 0
    info: 1
    warn: 12
  slug: aws-app-mesh-spectral-rules
score:
  band: strong
  composite: 65.5
  delta: 0.0
  facets:
    commercial_clarity: 78.9
    contract_quality: 75.2
    developer_ergonomics: 45.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 47.4
  previous_composite: 65.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/aws-app-mesh/refs/heads/main/screenshots/aws-app-mesh-2026-06-20T172740.png
security:
- kind: authentication
  name: Aws App Mesh Authentication
  slug: aws-app-mesh-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Aws App Mesh Domain Security
  slug: aws-app-mesh-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Aws App Mesh Vulnerability Disclosure
  slug: aws-app-mesh-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Aws App Mesh Trust Center
  slug: aws-app-mesh-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: aws-app-mesh
tags:
- Deprecated
- Envoy
- Microservices
- Networking
- Service Mesh
use_cases:
- description: Standardize and control service-to-service networking for containerized microservices applications.
  name: Microservices Communication
- description: Implement canary deployments, A/B testing, and weighted routing without application code changes.
  name: Traffic Management
- description: Capture end-to-end metrics and traces to identify performance bottlenecks and service failures.
  name: Observability and Debugging
- description: Enforce mTLS encryption between services for internal network security compliance.
  name: Zero-Trust Networking
website: https://aws.amazon.com/app-mesh/
---

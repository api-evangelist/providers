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
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 30
  human_in_the_loop: 1
  name: Amazon Opensearch Agentic Access
  operation_count: 50
  slug: amazon-opensearch-agentic-access
  summary_line: 50 operations · 30 acting · 1 human-in-the-loop
api_count: 5
apis:
- description: The Domain API from Amazon OpenSearch Service API — 2 operation(s) for domain.
  name: Amazon OpenSearch Service API Domain API
  slug: amazon-opensearch-domain-api
- description: The Es API from Amazon OpenSearch Service API — 34 operation(s) for es.
  name: Amazon OpenSearch Service API Es API
  slug: amazon-opensearch-es-api
- description: The Packages API from Amazon OpenSearch Service API — 8 operation(s) for packages.
  name: Amazon OpenSearch Service API Packages API
  slug: amazon-opensearch-packages-api
- description: The Tags API from Amazon OpenSearch Service API — 2 operation(s) for tags.
  name: Amazon OpenSearch Service API Tags API
  slug: amazon-opensearch-tags-api
- description: The Tags Removal API from Amazon OpenSearch Service API — 1 operation(s) for tags removal.
  name: Amazon OpenSearch Service API Tags Removal API
  slug: amazon-opensearch-tags-removal-api
artifact_total: 980
collections:
- collection_type: postman
  name: Amazon Elasticsearch Service Domain API
  slug: postman-amazon-opensearch-domain-api
- collection_type: postman
  name: Amazon Elasticsearch Service Domain Es API
  slug: postman-amazon-opensearch-es-api
- collection_type: postman
  name: Amazon Elasticsearch Service Domain Packages API
  slug: postman-amazon-opensearch-packages-api
- collection_type: postman
  name: Amazon Elasticsearch Service Domain Tags API
  slug: postman-amazon-opensearch-tags-api
- collection_type: postman
  name: Amazon Elasticsearch Service Domain Tags Removal API
  slug: postman-amazon-opensearch-tags-removal-api
- collection_type: open
  name: Amazon Elasticsearch Service
  slug: open-amazon-opensearch
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-opensearch-service-api/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-opensearch-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-opensearch-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-opensearch-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-opensearch-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-opensearch-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: company
  title: ''
  type: Website
  url: https://aws.amazon.com/opensearch-service/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/opensearch-service/
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
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/opensearch/
- group: start
  title: ''
  type: Signup
  url: https://signin.aws.amazon.com/signup?request_type=register
- group: start
  title: ''
  type: Login
  url: https://aws.amazon.com/console/
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
  url: rules/amazon-opensearch-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-opensearch-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-opensearch-openapi-context.jsonld
- group: docs
  title: Openapi Accept Inbound Cross Cluster Search Connection Request
  type: JSONSchema
  url: json-schema/openapi-accept-inbound-cross-cluster-search-connection-request-schema.json
- group: docs
  title: Openapi Accept Inbound Cross Cluster Search Connection Response
  type: JSONSchema
  url: json-schema/openapi-accept-inbound-cross-cluster-search-connection-response-schema.json
- group: docs
  title: Openapi Access Denied Exception
  type: JSONSchema
  url: json-schema/openapi-access-denied-exception-schema.json
- group: docs
  title: Openapi Access Policies Status
  type: JSONSchema
  url: json-schema/openapi-access-policies-status-schema.json
- group: docs
  title: Openapi Add Tags Request
  type: JSONSchema
  url: json-schema/openapi-add-tags-request-schema.json
created: '2024-01-15'
description: Amazon OpenSearch Service is a managed service that makes it easy to deploy, operate, and scale OpenSearch clusters in the AWS Cloud. It offers visualization capabilities powered by OpenSearch Dashboards and Kibana, and provides direct access to the OpenSearch API so that existing code and applications work seamlessly. It supports log analytics, full-text search, application monitoring, and clickstream analytics.
examples:
- key_count: 0
  name: Openapi Accept Inbound Cross Cluster Search Connection Request Example
  slug: openapi-accept-inbound-cross-cluster-search-connection-request-example
- key_count: 1
  name: Openapi Accept Inbound Cross Cluster Search Connection Response Example
  slug: openapi-accept-inbound-cross-cluster-search-connection-response-example
- key_count: 0
  name: Openapi Access Denied Exception Example
  slug: openapi-access-denied-exception-example
- key_count: 2
  name: Openapi Access Policies Status Example
  slug: openapi-access-policies-status-example
- key_count: 2
  name: Openapi Add Tags Request Example
  slug: openapi-add-tags-request-example
- key_count: 2
  name: Openapi Additional Limit Example
  slug: openapi-additional-limit-example
- key_count: 0
  name: Openapi Advanced Options Example
  slug: openapi-advanced-options-example
- key_count: 2
  name: Openapi Advanced Options Status Example
  slug: openapi-advanced-options-status-example
- key_count: 5
  name: Openapi Advanced Security Options Example
  slug: openapi-advanced-security-options-example
- key_count: 5
  name: Openapi Advanced Security Options Input Example
  slug: openapi-advanced-security-options-input-example
- key_count: 2
  name: Openapi Advanced Security Options Status Example
  slug: openapi-advanced-security-options-status-example
- key_count: 0
  name: Openapi Arn Example
  slug: openapi-arn-example
- key_count: 0
  name: Openapi Associate Package Request Example
  slug: openapi-associate-package-request-example
- key_count: 1
  name: Openapi Associate Package Response Example
  slug: openapi-associate-package-response-example
- key_count: 1
  name: Openapi Authorize Vpc Endpoint Access Request Example
  slug: openapi-authorize-vpc-endpoint-access-request-example
- key_count: 1
  name: Openapi Authorize Vpc Endpoint Access Response Example
  slug: openapi-authorize-vpc-endpoint-access-response-example
- key_count: 2
  name: Openapi Authorized Principal Example
  slug: openapi-authorized-principal-example
- key_count: 0
  name: Openapi Auto Tune Date Example
  slug: openapi-auto-tune-date-example
- key_count: 0
  name: Openapi Auto Tune Desired State Example
  slug: openapi-auto-tune-desired-state-example
- key_count: 1
  name: Openapi Auto Tune Details Example
  slug: openapi-auto-tune-details-example
- key_count: 2
  name: Openapi Auto Tune Example
  slug: openapi-auto-tune-example
- key_count: 3
  name: Openapi Auto Tune Maintenance Schedule Example
  slug: openapi-auto-tune-maintenance-schedule-example
- key_count: 3
  name: Openapi Auto Tune Options Example
  slug: openapi-auto-tune-options-example
- key_count: 2
  name: Openapi Auto Tune Options Input Example
  slug: openapi-auto-tune-options-input-example
- key_count: 2
  name: Openapi Auto Tune Options Output Example
  slug: openapi-auto-tune-options-output-example
- key_count: 2
  name: Openapi Auto Tune Options Status Example
  slug: openapi-auto-tune-options-status-example
- key_count: 0
  name: Openapi Auto Tune State Example
  slug: openapi-auto-tune-state-example
- key_count: 6
  name: Openapi Auto Tune Status Example
  slug: openapi-auto-tune-status-example
- key_count: 0
  name: Openapi Auto Tune Type Example
  slug: openapi-auto-tune-type-example
- key_count: 0
  name: Openapi Aws Account Example
  slug: openapi-aws-account-example
- key_count: 0
  name: Openapi Backend Role Example
  slug: openapi-backend-role-example
- key_count: 0
  name: Openapi Base Exception Example
  slug: openapi-base-exception-example
- key_count: 0
  name: Openapi Boolean Example
  slug: openapi-boolean-example
- key_count: 1
  name: Openapi Cancel Elasticsearch Service Software Update Request Example
  slug: openapi-cancel-elasticsearch-service-software-update-request-example
- key_count: 1
  name: Openapi Cancel Elasticsearch Service Software Update Response Example
  slug: openapi-cancel-elasticsearch-service-software-update-response-example
- key_count: 2
  name: Openapi Change Progress Details Example
  slug: openapi-change-progress-details-example
- key_count: 4
  name: Openapi Change Progress Stage Example
  slug: openapi-change-progress-stage-example
- key_count: 0
  name: Openapi Change Progress Stage Name Example
  slug: openapi-change-progress-stage-name-example
- key_count: 0
  name: Openapi Change Progress Stage Status Example
  slug: openapi-change-progress-stage-status-example
- key_count: 7
  name: Openapi Change Progress Status Details Example
  slug: openapi-change-progress-status-details-example
- key_count: 0
  name: Openapi Client Token Example
  slug: openapi-client-token-example
- key_count: 0
  name: Openapi Cloud Watch Logs Log Group Arn Example
  slug: openapi-cloud-watch-logs-log-group-arn-example
- key_count: 4
  name: Openapi Cognito Options Example
  slug: openapi-cognito-options-example
- key_count: 2
  name: Openapi Cognito Options Status Example
  slug: openapi-cognito-options-status-example
- key_count: 1
  name: Openapi Cold Storage Options Example
  slug: openapi-cold-storage-options-example
- key_count: 0
  name: Openapi Commit Message Example
  slug: openapi-commit-message-example
- key_count: 2
  name: Openapi Compatible Versions Map Example
  slug: openapi-compatible-versions-map-example
- key_count: 0
  name: Openapi Conflict Exception Example
  slug: openapi-conflict-exception-example
- key_count: 0
  name: Openapi Connection Alias Example
  slug: openapi-connection-alias-example
- key_count: 15
  name: Openapi Create Elasticsearch Domain Request Example
  slug: openapi-create-elasticsearch-domain-request-example
- key_count: 1
  name: Openapi Create Elasticsearch Domain Response Example
  slug: openapi-create-elasticsearch-domain-response-example
- key_count: 3
  name: Openapi Create Outbound Cross Cluster Search Connection Request Example
  slug: openapi-create-outbound-cross-cluster-search-connection-request-example
- key_count: 5
  name: Openapi Create Outbound Cross Cluster Search Connection Response Example
  slug: openapi-create-outbound-cross-cluster-search-connection-response-example
- key_count: 4
  name: Openapi Create Package Request Example
  slug: openapi-create-package-request-example
- key_count: 1
  name: Openapi Create Package Response Example
  slug: openapi-create-package-response-example
- key_count: 3
  name: Openapi Create Vpc Endpoint Request Example
  slug: openapi-create-vpc-endpoint-request-example
- key_count: 1
  name: Openapi Create Vpc Endpoint Response Example
  slug: openapi-create-vpc-endpoint-response-example
- key_count: 0
  name: Openapi Created At Example
  slug: openapi-created-at-example
- key_count: 0
  name: Openapi Cross Cluster Search Connection Id Example
  slug: openapi-cross-cluster-search-connection-id-example
- key_count: 0
  name: Openapi Cross Cluster Search Connection Status Message Example
  slug: openapi-cross-cluster-search-connection-status-message-example
- key_count: 0
  name: Openapi Delete Elasticsearch Domain Request Example
  slug: openapi-delete-elasticsearch-domain-request-example
- key_count: 1
  name: Openapi Delete Elasticsearch Domain Response Example
  slug: openapi-delete-elasticsearch-domain-response-example
- key_count: 0
  name: Openapi Delete Inbound Cross Cluster Search Connection Request Example
  slug: openapi-delete-inbound-cross-cluster-search-connection-request-example
- key_count: 1
  name: Openapi Delete Inbound Cross Cluster Search Connection Response Example
  slug: openapi-delete-inbound-cross-cluster-search-connection-response-example
- key_count: 0
  name: Openapi Delete Outbound Cross Cluster Search Connection Request Example
  slug: openapi-delete-outbound-cross-cluster-search-connection-request-example
- key_count: 1
  name: Openapi Delete Outbound Cross Cluster Search Connection Response Example
  slug: openapi-delete-outbound-cross-cluster-search-connection-response-example
- key_count: 0
  name: Openapi Delete Package Request Example
  slug: openapi-delete-package-request-example
- key_count: 1
  name: Openapi Delete Package Response Example
  slug: openapi-delete-package-response-example
- key_count: 0
  name: Openapi Delete Vpc Endpoint Request Example
  slug: openapi-delete-vpc-endpoint-request-example
- key_count: 1
  name: Openapi Delete Vpc Endpoint Response Example
  slug: openapi-delete-vpc-endpoint-response-example
- key_count: 0
  name: Openapi Deployment Close Date Time Stamp Example
  slug: openapi-deployment-close-date-time-stamp-example
- key_count: 0
  name: Openapi Deployment Status Example
  slug: openapi-deployment-status-example
- key_count: 0
  name: Openapi Deployment Type Example
  slug: openapi-deployment-type-example
- key_count: 2
  name: Openapi Describe Domain Auto Tunes Request Example
  slug: openapi-describe-domain-auto-tunes-request-example
- key_count: 2
  name: Openapi Describe Domain Auto Tunes Response Example
  slug: openapi-describe-domain-auto-tunes-response-example
- key_count: 0
  name: Openapi Describe Domain Change Progress Request Example
  slug: openapi-describe-domain-change-progress-request-example
- key_count: 1
  name: Openapi Describe Domain Change Progress Response Example
  slug: openapi-describe-domain-change-progress-response-example
- key_count: 0
  name: Openapi Describe Elasticsearch Domain Config Request Example
  slug: openapi-describe-elasticsearch-domain-config-request-example
- key_count: 1
  name: Openapi Describe Elasticsearch Domain Config Response Example
  slug: openapi-describe-elasticsearch-domain-config-response-example
- key_count: 0
  name: Openapi Describe Elasticsearch Domain Request Example
  slug: openapi-describe-elasticsearch-domain-request-example
- key_count: 1
  name: Openapi Describe Elasticsearch Domain Response Example
  slug: openapi-describe-elasticsearch-domain-response-example
- key_count: 1
  name: Openapi Describe Elasticsearch Domains Request Example
  slug: openapi-describe-elasticsearch-domains-request-example
- key_count: 1
  name: Openapi Describe Elasticsearch Domains Response Example
  slug: openapi-describe-elasticsearch-domains-response-example
- key_count: 0
  name: Openapi Describe Elasticsearch Instance Type Limits Request Example
  slug: openapi-describe-elasticsearch-instance-type-limits-request-example
- key_count: 1
  name: Openapi Describe Elasticsearch Instance Type Limits Response Example
  slug: openapi-describe-elasticsearch-instance-type-limits-response-example
- key_count: 3
  name: Openapi Describe Inbound Cross Cluster Search Connections Request Example
  slug: openapi-describe-inbound-cross-cluster-search-connections-request-example
- key_count: 2
  name: Openapi Describe Inbound Cross Cluster Search Connections Response Example
  slug: openapi-describe-inbound-cross-cluster-search-connections-response-example
- key_count: 3
  name: Openapi Describe Outbound Cross Cluster Search Connections Request Example
  slug: openapi-describe-outbound-cross-cluster-search-connections-request-example
- key_count: 2
  name: Openapi Describe Outbound Cross Cluster Search Connections Response Example
  slug: openapi-describe-outbound-cross-cluster-search-connections-response-example
- key_count: 2
  name: Openapi Describe Packages Filter Example
  slug: openapi-describe-packages-filter-example
- key_count: 0
  name: Openapi Describe Packages Filter Name Example
  slug: openapi-describe-packages-filter-name-example
- key_count: 0
  name: Openapi Describe Packages Filter Value Example
  slug: openapi-describe-packages-filter-value-example
- key_count: 3
  name: Openapi Describe Packages Request Example
  slug: openapi-describe-packages-request-example
- key_count: 2
  name: Openapi Describe Packages Response Example
  slug: openapi-describe-packages-response-example
- key_count: 0
  name: Openapi Describe Reserved Elasticsearch Instance Offerings Request Example
  slug: openapi-describe-reserved-elasticsearch-instance-offerings-request-example
- key_count: 2
  name: Openapi Describe Reserved Elasticsearch Instance Offerings Response Example
  slug: openapi-describe-reserved-elasticsearch-instance-offerings-response-example
- key_count: 0
  name: Openapi Describe Reserved Elasticsearch Instances Request Example
  slug: openapi-describe-reserved-elasticsearch-instances-request-example
- key_count: 2
  name: Openapi Describe Reserved Elasticsearch Instances Response Example
  slug: openapi-describe-reserved-elasticsearch-instances-response-example
- key_count: 1
  name: Openapi Describe Vpc Endpoints Request Example
  slug: openapi-describe-vpc-endpoints-request-example
- key_count: 2
  name: Openapi Describe Vpc Endpoints Response Example
  slug: openapi-describe-vpc-endpoints-response-example
- key_count: 0
  name: Openapi Description Example
  slug: openapi-description-example
- key_count: 0
  name: Openapi Disable Timestamp Example
  slug: openapi-disable-timestamp-example
- key_count: 0
  name: Openapi Disabled Operation Exception Example
  slug: openapi-disabled-operation-exception-example
- key_count: 0
  name: Openapi Dissociate Package Request Example
  slug: openapi-dissociate-package-request-example
- key_count: 1
  name: Openapi Dissociate Package Response Example
  slug: openapi-dissociate-package-response-example
- key_count: 0
  name: Openapi Domain Arn Example
  slug: openapi-domain-arn-example
- key_count: 5
  name: Openapi Domain Endpoint Options Example
  slug: openapi-domain-endpoint-options-example
- key_count: 2
  name: Openapi Domain Endpoint Options Status Example
  slug: openapi-domain-endpoint-options-status-example
- key_count: 0
  name: Openapi Domain Id Example
  slug: openapi-domain-id-example
- key_count: 2
  name: Openapi Domain Info Example
  slug: openapi-domain-info-example
- key_count: 3
  name: Openapi Domain Information Example
  slug: openapi-domain-information-example
- key_count: 0
  name: Openapi Domain Name Example
  slug: openapi-domain-name-example
- key_count: 0
  name: Openapi Domain Name Fqdn Example
  slug: openapi-domain-name-fqdn-example
- key_count: 9
  name: Openapi Domain Package Details Example
  slug: openapi-domain-package-details-example
- key_count: 0
  name: Openapi Domain Package Status Example
  slug: openapi-domain-package-status-example
- key_count: 0
  name: Openapi Double Example
  slug: openapi-double-example
- key_count: 0
  name: Openapi Dry Run Example
  slug: openapi-dry-run-example
- key_count: 2
  name: Openapi Dry Run Results Example
  slug: openapi-dry-run-results-example
- key_count: 2
  name: Openapi Duration Example
  slug: openapi-duration-example
- key_count: 0
  name: Openapi Duration Value Example
  slug: openapi-duration-value-example
- key_count: 5
  name: Openapi Ebs Options Example
  slug: openapi-ebs-options-example
- key_count: 2
  name: Openapi Ebs Options Status Example
  slug: openapi-ebs-options-status-example
- key_count: 11
  name: Openapi Elasticsearch Cluster Config Example
  slug: openapi-elasticsearch-cluster-config-example
- key_count: 2
  name: Openapi Elasticsearch Cluster Config Status Example
  slug: openapi-elasticsearch-cluster-config-status-example
- key_count: 15
  name: Openapi Elasticsearch Domain Config Example
  slug: openapi-elasticsearch-domain-config-example
- key_count: 15
  name: Openapi Elasticsearch Domain Status Example
  slug: openapi-elasticsearch-domain-status-example
- key_count: 2
  name: Openapi Elasticsearch Version Status Example
  slug: openapi-elasticsearch-version-status-example
- key_count: 0
  name: Openapi Elasticsearch Version String Example
  slug: openapi-elasticsearch-version-string-example
- key_count: 2
  name: Openapi Encryption At Rest Options Example
  slug: openapi-encryption-at-rest-options-example
- key_count: 2
  name: Openapi Encryption At Rest Options Status Example
  slug: openapi-encryption-at-rest-options-status-example
- key_count: 0
  name: Openapi Endpoint Example
  slug: openapi-endpoint-example
- key_count: 0
  name: Openapi Endpoints Map Example
  slug: openapi-endpoints-map-example
- key_count: 0
  name: Openapi Engine Type Example
  slug: openapi-engine-type-example
- key_count: 2
  name: Openapi Error Details Example
  slug: openapi-error-details-example
- key_count: 0
  name: Openapi Error Message Example
  slug: openapi-error-message-example
- key_count: 0
  name: Openapi Error Type Example
  slug: openapi-error-type-example
- key_count: 0
  name: Openapi Es Partition Instance Type Example
  slug: openapi-es-partition-instance-type-example
- key_count: 0
  name: Openapi Es Warm Partition Instance Type Example
  slug: openapi-es-warm-partition-instance-type-example
- key_count: 2
  name: Openapi Filter Example
  slug: openapi-filter-example
- key_count: 0
  name: Openapi Get Compatible Elasticsearch Versions Request Example
  slug: openapi-get-compatible-elasticsearch-versions-request-example
- key_count: 1
  name: Openapi Get Compatible Elasticsearch Versions Response Example
  slug: openapi-get-compatible-elasticsearch-versions-response-example
- key_count: 0
  name: Openapi Get Package Version History Request Example
  slug: openapi-get-package-version-history-request-example
- key_count: 3
  name: Openapi Get Package Version History Response Example
  slug: openapi-get-package-version-history-response-example
- key_count: 0
  name: Openapi Get Upgrade History Request Example
  slug: openapi-get-upgrade-history-request-example
- key_count: 2
  name: Openapi Get Upgrade History Response Example
  slug: openapi-get-upgrade-history-response-example
- key_count: 0
  name: Openapi Get Upgrade Status Request Example
  slug: openapi-get-upgrade-status-request-example
- key_count: 3
  name: Openapi Get Upgrade Status Response Example
  slug: openapi-get-upgrade-status-response-example
- key_count: 0
  name: Openapi Guid Example
  slug: openapi-guid-example
- key_count: 0
  name: Openapi Identity Pool Id Example
  slug: openapi-identity-pool-id-example
- key_count: 4
  name: Openapi Inbound Cross Cluster Search Connection Example
  slug: openapi-inbound-cross-cluster-search-connection-example
- key_count: 0
  name: Openapi Inbound Cross Cluster Search Connection Status Code Example
  slug: openapi-inbound-cross-cluster-search-connection-status-code-example
- key_count: 2
  name: Openapi Inbound Cross Cluster Search Connection Status Example
  slug: openapi-inbound-cross-cluster-search-connection-status-example
- key_count: 0
  name: Openapi Instance Count Example
  slug: openapi-instance-count-example
- key_count: 2
  name: Openapi Instance Count Limits Example
  slug: openapi-instance-count-limits-example
- key_count: 1
  name: Openapi Instance Limits Example
  slug: openapi-instance-limits-example
- key_count: 0
  name: Openapi Instance Role Example
  slug: openapi-instance-role-example
- key_count: 0
  name: Openapi Integer Class Example
  slug: openapi-integer-class-example
- key_count: 0
  name: Openapi Integer Example
  slug: openapi-integer-example
- key_count: 0
  name: Openapi Internal Exception Example
  slug: openapi-internal-exception-example
- key_count: 0
  name: Openapi Invalid Pagination Token Exception Example
  slug: openapi-invalid-pagination-token-exception-example
- key_count: 0
  name: Openapi Invalid Type Exception Example
  slug: openapi-invalid-type-exception-example
- key_count: 0
  name: Openapi Issue Example
  slug: openapi-issue-example
- key_count: 0
  name: Openapi Kms Key Id Example
  slug: openapi-kms-key-id-example
- key_count: 0
  name: Openapi Last Updated Example
  slug: openapi-last-updated-example
- key_count: 0
  name: Openapi Limit Exceeded Exception Example
  slug: openapi-limit-exceeded-exception-example
- key_count: 0
  name: Openapi Limit Name Example
  slug: openapi-limit-name-example
- key_count: 0
  name: Openapi Limit Value Example
  slug: openapi-limit-value-example
- key_count: 0
  name: Openapi Limits By Role Example
  slug: openapi-limits-by-role-example
- key_count: 3
  name: Openapi Limits Example
  slug: openapi-limits-example
- key_count: 0
  name: Openapi List Domain Names Request Example
  slug: openapi-list-domain-names-request-example
- key_count: 1
  name: Openapi List Domain Names Response Example
  slug: openapi-list-domain-names-response-example
- key_count: 0
  name: Openapi List Domains For Package Request Example
  slug: openapi-list-domains-for-package-request-example
- key_count: 2
  name: Openapi List Domains For Package Response Example
  slug: openapi-list-domains-for-package-response-example
- key_count: 0
  name: Openapi List Elasticsearch Instance Types Request Example
  slug: openapi-list-elasticsearch-instance-types-request-example
- key_count: 2
  name: Openapi List Elasticsearch Instance Types Response Example
  slug: openapi-list-elasticsearch-instance-types-response-example
- key_count: 0
  name: Openapi List Elasticsearch Versions Request Example
  slug: openapi-list-elasticsearch-versions-request-example
- key_count: 2
  name: Openapi List Elasticsearch Versions Response Example
  slug: openapi-list-elasticsearch-versions-response-example
- key_count: 0
  name: Openapi List Packages For Domain Request Example
  slug: openapi-list-packages-for-domain-request-example
- key_count: 2
  name: Openapi List Packages For Domain Response Example
  slug: openapi-list-packages-for-domain-response-example
- key_count: 0
  name: Openapi List Tags Request Example
  slug: openapi-list-tags-request-example
- key_count: 1
  name: Openapi List Tags Response Example
  slug: openapi-list-tags-response-example
- key_count: 0
  name: Openapi List Vpc Endpoint Access Request Example
  slug: openapi-list-vpc-endpoint-access-request-example
- key_count: 2
  name: Openapi List Vpc Endpoint Access Response Example
  slug: openapi-list-vpc-endpoint-access-response-example
- key_count: 0
  name: Openapi List Vpc Endpoints For Domain Request Example
  slug: openapi-list-vpc-endpoints-for-domain-request-example
- key_count: 2
  name: Openapi List Vpc Endpoints For Domain Response Example
  slug: openapi-list-vpc-endpoints-for-domain-response-example
- key_count: 0
  name: Openapi List Vpc Endpoints Request Example
  slug: openapi-list-vpc-endpoints-request-example
- key_count: 2
  name: Openapi List Vpc Endpoints Response Example
  slug: openapi-list-vpc-endpoints-response-example
- key_count: 2
  name: Openapi Log Publishing Option Example
  slug: openapi-log-publishing-option-example
- key_count: 0
  name: Openapi Log Publishing Options Example
  slug: openapi-log-publishing-options-example
- key_count: 2
  name: Openapi Log Publishing Options Status Example
  slug: openapi-log-publishing-options-status-example
- key_count: 0
  name: Openapi Log Type Example
  slug: openapi-log-type-example
- key_count: 3
  name: Openapi Master User Options Example
  slug: openapi-master-user-options-example
- key_count: 0
  name: Openapi Max Results Example
  slug: openapi-max-results-example
- key_count: 0
  name: Openapi Maximum Instance Count Example
  slug: openapi-maximum-instance-count-example
- key_count: 0
  name: Openapi Message Example
  slug: openapi-message-example
- key_count: 0
  name: Openapi Minimum Instance Count Example
  slug: openapi-minimum-instance-count-example
- key_count: 0
  name: Openapi Next Token Example
  slug: openapi-next-token-example
- key_count: 1
  name: Openapi Node To Node Encryption Options Example
  slug: openapi-node-to-node-encryption-options-example
- key_count: 2
  name: Openapi Node To Node Encryption Options Status Example
  slug: openapi-node-to-node-encryption-options-status-example
- key_count: 0
  name: Openapi Non Empty String Example
  slug: openapi-non-empty-string-example
- key_count: 0
  name: Openapi Option State Example
  slug: openapi-option-state-example
- key_count: 5
  name: Openapi Option Status Example
  slug: openapi-option-status-example
- key_count: 5
  name: Openapi Outbound Cross Cluster Search Connection Example
  slug: openapi-outbound-cross-cluster-search-connection-example
- key_count: 0
  name: Openapi Outbound Cross Cluster Search Connection Status Code Example
  slug: openapi-outbound-cross-cluster-search-connection-status-code-example
- key_count: 2
  name: Openapi Outbound Cross Cluster Search Connection Status Example
  slug: openapi-outbound-cross-cluster-search-connection-status-example
- key_count: 0
  name: Openapi Overall Change Status Example
  slug: openapi-overall-change-status-example
- key_count: 0
  name: Openapi Owner Id Example
  slug: openapi-owner-id-example
- key_count: 0
  name: Openapi Package Description Example
  slug: openapi-package-description-example
- key_count: 9
  name: Openapi Package Details Example
  slug: openapi-package-details-example
- key_count: 0
  name: Openapi Package Id Example
  slug: openapi-package-id-example
- key_count: 0
  name: Openapi Package Name Example
  slug: openapi-package-name-example
- key_count: 2
  name: Openapi Package Source Example
  slug: openapi-package-source-example
- key_count: 0
  name: Openapi Package Status Example
  slug: openapi-package-status-example
- key_count: 0
  name: Openapi Package Type Example
  slug: openapi-package-type-example
- key_count: 0
  name: Openapi Package Version Example
  slug: openapi-package-version-example
- key_count: 3
  name: Openapi Package Version History Example
  slug: openapi-package-version-history-example
- key_count: 0
  name: Openapi Password Example
  slug: openapi-password-example
- key_count: 0
  name: Openapi Policy Document Example
  slug: openapi-policy-document-example
- key_count: 0
  name: Openapi Principal Type Example
  slug: openapi-principal-type-example
- key_count: 3
  name: Openapi Purchase Reserved Elasticsearch Instance Offering Request Example
  slug: openapi-purchase-reserved-elasticsearch-instance-offering-request-example
- key_count: 2
  name: Openapi Purchase Reserved Elasticsearch Instance Offering Response Example
  slug: openapi-purchase-reserved-elasticsearch-instance-offering-response-example
- key_count: 2
  name: Openapi Recurring Charge Example
  slug: openapi-recurring-charge-example
- key_count: 0
  name: Openapi Reference Path Example
  slug: openapi-reference-path-example
- key_count: 0
  name: Openapi Region Example
  slug: openapi-region-example
- key_count: 0
  name: Openapi Reject Inbound Cross Cluster Search Connection Request Example
  slug: openapi-reject-inbound-cross-cluster-search-connection-request-example
- key_count: 1
  name: Openapi Reject Inbound Cross Cluster Search Connection Response Example
  slug: openapi-reject-inbound-cross-cluster-search-connection-response-example
- key_count: 2
  name: Openapi Remove Tags Request Example
  slug: openapi-remove-tags-request-example
- key_count: 0
  name: Openapi Reservation Token Example
  slug: openapi-reservation-token-example
- key_count: 13
  name: Openapi Reserved Elasticsearch Instance Example
  slug: openapi-reserved-elasticsearch-instance-example
- key_count: 8
  name: Openapi Reserved Elasticsearch Instance Offering Example
  slug: openapi-reserved-elasticsearch-instance-offering-example
- key_count: 0
  name: Openapi Reserved Elasticsearch Instance Payment Option Example
  slug: openapi-reserved-elasticsearch-instance-payment-option-example
- key_count: 0
  name: Openapi Resource Already Exists Exception Example
  slug: openapi-resource-already-exists-exception-example
- key_count: 0
  name: Openapi Resource Not Found Exception Example
  slug: openapi-resource-not-found-exception-example
- key_count: 1
  name: Openapi Revoke Vpc Endpoint Access Request Example
  slug: openapi-revoke-vpc-endpoint-access-request-example
- key_count: 0
  name: Openapi Revoke Vpc Endpoint Access Response Example
  slug: openapi-revoke-vpc-endpoint-access-response-example
- key_count: 0
  name: Openapi Role Arn Example
  slug: openapi-role-arn-example
- key_count: 0
  name: Openapi Rollback On Disable Example
  slug: openapi-rollback-on-disable-example
- key_count: 0
  name: Openapi S3 Bucket Name Example
  slug: openapi-s3-bucket-name-example
- key_count: 0
  name: Openapi S3 Key Example
  slug: openapi-s3-key-example
- key_count: 0
  name: Openapi Saml Entity Id Example
  slug: openapi-saml-entity-id-example
- key_count: 2
  name: Openapi Saml Idp Example
  slug: openapi-saml-idp-example
- key_count: 0
  name: Openapi Saml Metadata Example
  slug: openapi-saml-metadata-example
- key_count: 7
  name: Openapi Saml Options Input Example
  slug: openapi-saml-options-input-example
- key_count: 5
  name: Openapi Saml Options Output Example
  slug: openapi-saml-options-output-example
- key_count: 0
  name: Openapi Scheduled Auto Tune Action Type Example
  slug: openapi-scheduled-auto-tune-action-type-example
- key_count: 0
  name: Openapi Scheduled Auto Tune Description Example
  slug: openapi-scheduled-auto-tune-description-example
- key_count: 4
  name: Openapi Scheduled Auto Tune Details Example
  slug: openapi-scheduled-auto-tune-details-example
- key_count: 0
  name: Openapi Scheduled Auto Tune Severity Type Example
  slug: openapi-scheduled-auto-tune-severity-type-example
- key_count: 8
  name: Openapi Service Software Options Example
  slug: openapi-service-software-options-example
- key_count: 0
  name: Openapi Service Url Example
  slug: openapi-service-url-example
- key_count: 1
  name: Openapi Snapshot Options Example
  slug: openapi-snapshot-options-example
- key_count: 2
  name: Openapi Snapshot Options Status Example
  slug: openapi-snapshot-options-status-example
- key_count: 0
  name: Openapi Start At Example
  slug: openapi-start-at-example
- key_count: 1
  name: Openapi Start Elasticsearch Service Software Update Request Example
  slug: openapi-start-elasticsearch-service-software-update-request-example
- key_count: 1
  name: Openapi Start Elasticsearch Service Software Update Response Example
  slug: openapi-start-elasticsearch-service-software-update-response-example
- key_count: 0
  name: Openapi Start Timestamp Example
  slug: openapi-start-timestamp-example
- key_count: 0
  name: Openapi Storage Sub Type Name Example
  slug: openapi-storage-sub-type-name-example
- key_count: 3
  name: Openapi Storage Type Example
  slug: openapi-storage-type-example
- key_count: 2
  name: Openapi Storage Type Limit Example
  slug: openapi-storage-type-limit-example
- key_count: 0
  name: Openapi Storage Type Name Example
  slug: openapi-storage-type-name-example
- key_count: 0
  name: Openapi String Example
  slug: openapi-string-example
- key_count: 2
  name: Openapi Tag Example
  slug: openapi-tag-example
- key_count: 0
  name: Openapi Tag Key Example
  slug: openapi-tag-key-example
- key_count: 0
  name: Openapi Tag Value Example
  slug: openapi-tag-value-example
- key_count: 0
  name: Openapi Time Unit Example
  slug: openapi-time-unit-example
- key_count: 0
  name: Openapi Tls Security Policy Example
  slug: openapi-tls-security-policy-example
- key_count: 0
  name: Openapi Total Number Of Stages Example
  slug: openapi-total-number-of-stages-example
- key_count: 0
  name: Openapi U Int Value Example
  slug: openapi-u-int-value-example
- key_count: 14
  name: Openapi Update Elasticsearch Domain Config Request Example
  slug: openapi-update-elasticsearch-domain-config-request-example
- key_count: 2
  name: Openapi Update Elasticsearch Domain Config Response Example
  slug: openapi-update-elasticsearch-domain-config-response-example
- key_count: 4
  name: Openapi Update Package Request Example
  slug: openapi-update-package-request-example
- key_count: 1
  name: Openapi Update Package Response Example
  slug: openapi-update-package-response-example
- key_count: 0
  name: Openapi Update Timestamp Example
  slug: openapi-update-timestamp-example
- key_count: 2
  name: Openapi Update Vpc Endpoint Request Example
  slug: openapi-update-vpc-endpoint-request-example
- key_count: 1
  name: Openapi Update Vpc Endpoint Response Example
  slug: openapi-update-vpc-endpoint-response-example
- key_count: 3
  name: Openapi Upgrade Elasticsearch Domain Request Example
  slug: openapi-upgrade-elasticsearch-domain-request-example
- key_count: 4
  name: Openapi Upgrade Elasticsearch Domain Response Example
  slug: openapi-upgrade-elasticsearch-domain-response-example
- key_count: 4
  name: Openapi Upgrade History Example
  slug: openapi-upgrade-history-example
- key_count: 0
  name: Openapi Upgrade Name Example
  slug: openapi-upgrade-name-example
- key_count: 0
  name: Openapi Upgrade Status Example
  slug: openapi-upgrade-status-example
- key_count: 0
  name: Openapi Upgrade Step Example
  slug: openapi-upgrade-step-example
- key_count: 4
  name: Openapi Upgrade Step Item Example
  slug: openapi-upgrade-step-item-example
- key_count: 0
  name: Openapi User Pool Id Example
  slug: openapi-user-pool-id-example
- key_count: 0
  name: Openapi Username Example
  slug: openapi-username-example
- key_count: 0
  name: Openapi Validation Exception Example
  slug: openapi-validation-exception-example
- key_count: 0
  name: Openapi Volume Type Example
  slug: openapi-volume-type-example
- key_count: 4
  name: Openapi Vpc Derived Info Example
  slug: openapi-vpc-derived-info-example
- key_count: 2
  name: Openapi Vpc Derived Info Status Example
  slug: openapi-vpc-derived-info-status-example
- key_count: 0
  name: Openapi Vpc Endpoint Error Code Example
  slug: openapi-vpc-endpoint-error-code-example
- key_count: 3
  name: Openapi Vpc Endpoint Error Example
  slug: openapi-vpc-endpoint-error-example
- key_count: 6
  name: Openapi Vpc Endpoint Example
  slug: openapi-vpc-endpoint-example
- key_count: 0
  name: Openapi Vpc Endpoint Id Example
  slug: openapi-vpc-endpoint-id-example
- key_count: 0
  name: Openapi Vpc Endpoint Status Example
  slug: openapi-vpc-endpoint-status-example
- key_count: 4
  name: Openapi Vpc Endpoint Summary Example
  slug: openapi-vpc-endpoint-summary-example
- key_count: 2
  name: Openapi Vpc Options Example
  slug: openapi-vpc-options-example
- key_count: 1
  name: Openapi Zone Awareness Config Example
  slug: openapi-zone-awareness-config-example
finops:
- name: Amazon Opensearch Finops
  service_category: API
  slug: amazon-opensearch-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: AcceptInboundCrossClusterSearchConnectionRequest
  property_count: 0
  slug: openapi-accept-inbound-cross-cluster-search-connection-request
- name: AcceptInboundCrossClusterSearchConnectionResponse
  property_count: 1
  slug: openapi-accept-inbound-cross-cluster-search-connection-response
- name: AccessDeniedException
  property_count: 0
  slug: openapi-access-denied-exception
- name: AccessPoliciesStatus
  property_count: 2
  slug: openapi-access-policies-status
- name: AddTagsRequest
  property_count: 2
  slug: openapi-add-tags-request
- name: AdditionalLimitList
  property_count: 0
  slug: openapi-additional-limit-list
- name: AdditionalLimit
  property_count: 2
  slug: openapi-additional-limit
- name: AdvancedOptions
  property_count: 0
  slug: openapi-advanced-options
- name: AdvancedOptionsStatus
  property_count: 2
  slug: openapi-advanced-options-status
- name: AdvancedSecurityOptionsInput
  property_count: 5
  slug: openapi-advanced-security-options-input
- name: AdvancedSecurityOptions
  property_count: 5
  slug: openapi-advanced-security-options
- name: AdvancedSecurityOptionsStatus
  property_count: 2
  slug: openapi-advanced-security-options-status
- name: ARN
  property_count: 0
  slug: openapi-arn
- name: AssociatePackageRequest
  property_count: 0
  slug: openapi-associate-package-request
- name: AssociatePackageResponse
  property_count: 1
  slug: openapi-associate-package-response
- name: AuthorizeVpcEndpointAccessRequest
  property_count: 1
  slug: openapi-authorize-vpc-endpoint-access-request
- name: AuthorizeVpcEndpointAccessResponse
  property_count: 1
  slug: openapi-authorize-vpc-endpoint-access-response
- name: AuthorizedPrincipalList
  property_count: 0
  slug: openapi-authorized-principal-list
- name: AuthorizedPrincipal
  property_count: 2
  slug: openapi-authorized-principal
- name: AutoTuneDate
  property_count: 0
  slug: openapi-auto-tune-date
- name: AutoTuneDesiredState
  property_count: 0
  slug: openapi-auto-tune-desired-state
- name: AutoTuneDetails
  property_count: 1
  slug: openapi-auto-tune-details
- name: AutoTuneList
  property_count: 0
  slug: openapi-auto-tune-list
- name: AutoTuneMaintenanceScheduleList
  property_count: 0
  slug: openapi-auto-tune-maintenance-schedule-list
- name: AutoTuneMaintenanceSchedule
  property_count: 3
  slug: openapi-auto-tune-maintenance-schedule
- name: AutoTuneOptionsInput
  property_count: 2
  slug: openapi-auto-tune-options-input
- name: AutoTuneOptionsOutput
  property_count: 2
  slug: openapi-auto-tune-options-output
- name: AutoTuneOptions
  property_count: 3
  slug: openapi-auto-tune-options
- name: AutoTuneOptionsStatus
  property_count: 2
  slug: openapi-auto-tune-options-status
- name: AutoTune
  property_count: 2
  slug: openapi-auto-tune
- name: AutoTuneState
  property_count: 0
  slug: openapi-auto-tune-state
- name: AutoTuneStatus
  property_count: 6
  slug: openapi-auto-tune-status
- name: AutoTuneType
  property_count: 0
  slug: openapi-auto-tune-type
- name: AWSAccount
  property_count: 0
  slug: openapi-aws-account
- name: BackendRole
  property_count: 0
  slug: openapi-backend-role
- name: BaseException
  property_count: 0
  slug: openapi-base-exception
- name: Boolean
  property_count: 0
  slug: openapi-boolean
- name: CancelElasticsearchServiceSoftwareUpdateRequest
  property_count: 1
  slug: openapi-cancel-elasticsearch-service-software-update-request
- name: CancelElasticsearchServiceSoftwareUpdateResponse
  property_count: 1
  slug: openapi-cancel-elasticsearch-service-software-update-response
- name: ChangeProgressDetails
  property_count: 2
  slug: openapi-change-progress-details
- name: ChangeProgressStageList
  property_count: 0
  slug: openapi-change-progress-stage-list
- name: ChangeProgressStageName
  property_count: 0
  slug: openapi-change-progress-stage-name
- name: ChangeProgressStage
  property_count: 4
  slug: openapi-change-progress-stage
- name: ChangeProgressStageStatus
  property_count: 0
  slug: openapi-change-progress-stage-status
- name: ChangeProgressStatusDetails
  property_count: 7
  slug: openapi-change-progress-status-details
- name: ClientToken
  property_count: 0
  slug: openapi-client-token
- name: CloudWatchLogsLogGroupArn
  property_count: 0
  slug: openapi-cloud-watch-logs-log-group-arn
- name: CognitoOptions
  property_count: 4
  slug: openapi-cognito-options
- name: CognitoOptionsStatus
  property_count: 2
  slug: openapi-cognito-options-status
- name: ColdStorageOptions
  property_count: 1
  slug: openapi-cold-storage-options
- name: CommitMessage
  property_count: 0
  slug: openapi-commit-message
- name: CompatibleElasticsearchVersionsList
  property_count: 0
  slug: openapi-compatible-elasticsearch-versions-list
- name: CompatibleVersionsMap
  property_count: 2
  slug: openapi-compatible-versions-map
- name: ConflictException
  property_count: 0
  slug: openapi-conflict-exception
- name: ConnectionAlias
  property_count: 0
  slug: openapi-connection-alias
- name: CreateElasticsearchDomainRequest
  property_count: 16
  slug: openapi-create-elasticsearch-domain-request
- name: CreateElasticsearchDomainResponse
  property_count: 1
  slug: openapi-create-elasticsearch-domain-response
- name: CreateOutboundCrossClusterSearchConnectionRequest
  property_count: 3
  slug: openapi-create-outbound-cross-cluster-search-connection-request
- name: CreateOutboundCrossClusterSearchConnectionResponse
  property_count: 5
  slug: openapi-create-outbound-cross-cluster-search-connection-response
- name: CreatePackageRequest
  property_count: 4
  slug: openapi-create-package-request
- name: CreatePackageResponse
  property_count: 1
  slug: openapi-create-package-response
- name: CreateVpcEndpointRequest
  property_count: 3
  slug: openapi-create-vpc-endpoint-request
- name: CreateVpcEndpointResponse
  property_count: 1
  slug: openapi-create-vpc-endpoint-response
- name: CreatedAt
  property_count: 0
  slug: openapi-created-at
- name: CrossClusterSearchConnectionId
  property_count: 0
  slug: openapi-cross-cluster-search-connection-id
- name: CrossClusterSearchConnectionStatusMessage
  property_count: 0
  slug: openapi-cross-cluster-search-connection-status-message
- name: DeleteElasticsearchDomainRequest
  property_count: 0
  slug: openapi-delete-elasticsearch-domain-request
- name: DeleteElasticsearchDomainResponse
  property_count: 1
  slug: openapi-delete-elasticsearch-domain-response
- name: DeleteInboundCrossClusterSearchConnectionRequest
  property_count: 0
  slug: openapi-delete-inbound-cross-cluster-search-connection-request
- name: DeleteInboundCrossClusterSearchConnectionResponse
  property_count: 1
  slug: openapi-delete-inbound-cross-cluster-search-connection-response
- name: DeleteOutboundCrossClusterSearchConnectionRequest
  property_count: 0
  slug: openapi-delete-outbound-cross-cluster-search-connection-request
- name: DeleteOutboundCrossClusterSearchConnectionResponse
  property_count: 1
  slug: openapi-delete-outbound-cross-cluster-search-connection-response
- name: DeletePackageRequest
  property_count: 0
  slug: openapi-delete-package-request
- name: DeletePackageResponse
  property_count: 1
  slug: openapi-delete-package-response
- name: DeleteVpcEndpointRequest
  property_count: 0
  slug: openapi-delete-vpc-endpoint-request
- name: DeleteVpcEndpointResponse
  property_count: 1
  slug: openapi-delete-vpc-endpoint-response
- name: DeploymentCloseDateTimeStamp
  property_count: 0
  slug: openapi-deployment-close-date-time-stamp
- name: DeploymentStatus
  property_count: 0
  slug: openapi-deployment-status
- name: DeploymentType
  property_count: 0
  slug: openapi-deployment-type
- name: DescribeDomainAutoTunesRequest
  property_count: 2
  slug: openapi-describe-domain-auto-tunes-request
- name: DescribeDomainAutoTunesResponse
  property_count: 2
  slug: openapi-describe-domain-auto-tunes-response
- name: DescribeDomainChangeProgressRequest
  property_count: 0
  slug: openapi-describe-domain-change-progress-request
- name: DescribeDomainChangeProgressResponse
  property_count: 1
  slug: openapi-describe-domain-change-progress-response
- name: DescribeElasticsearchDomainConfigRequest
  property_count: 0
  slug: openapi-describe-elasticsearch-domain-config-request
- name: DescribeElasticsearchDomainConfigResponse
  property_count: 1
  slug: openapi-describe-elasticsearch-domain-config-response
- name: DescribeElasticsearchDomainRequest
  property_count: 0
  slug: openapi-describe-elasticsearch-domain-request
- name: DescribeElasticsearchDomainResponse
  property_count: 1
  slug: openapi-describe-elasticsearch-domain-response
- name: DescribeElasticsearchDomainsRequest
  property_count: 1
  slug: openapi-describe-elasticsearch-domains-request
- name: DescribeElasticsearchDomainsResponse
  property_count: 1
  slug: openapi-describe-elasticsearch-domains-response
- name: DescribeElasticsearchInstanceTypeLimitsRequest
  property_count: 0
  slug: openapi-describe-elasticsearch-instance-type-limits-request
- name: DescribeElasticsearchInstanceTypeLimitsResponse
  property_count: 1
  slug: openapi-describe-elasticsearch-instance-type-limits-response
- name: DescribeInboundCrossClusterSearchConnectionsRequest
  property_count: 3
  slug: openapi-describe-inbound-cross-cluster-search-connections-request
- name: DescribeInboundCrossClusterSearchConnectionsResponse
  property_count: 2
  slug: openapi-describe-inbound-cross-cluster-search-connections-response
- name: DescribeOutboundCrossClusterSearchConnectionsRequest
  property_count: 3
  slug: openapi-describe-outbound-cross-cluster-search-connections-request
- name: DescribeOutboundCrossClusterSearchConnectionsResponse
  property_count: 2
  slug: openapi-describe-outbound-cross-cluster-search-connections-response
- name: DescribePackagesFilterList
  property_count: 0
  slug: openapi-describe-packages-filter-list
- name: DescribePackagesFilterName
  property_count: 0
  slug: openapi-describe-packages-filter-name
- name: DescribePackagesFilter
  property_count: 2
  slug: openapi-describe-packages-filter
- name: DescribePackagesFilterValue
  property_count: 0
  slug: openapi-describe-packages-filter-value
- name: DescribePackagesFilterValues
  property_count: 0
  slug: openapi-describe-packages-filter-values
- name: DescribePackagesRequest
  property_count: 3
  slug: openapi-describe-packages-request
- name: DescribePackagesResponse
  property_count: 2
  slug: openapi-describe-packages-response
- name: DescribeReservedElasticsearchInstanceOfferingsRequest
  property_count: 0
  slug: openapi-describe-reserved-elasticsearch-instance-offerings-request
- name: DescribeReservedElasticsearchInstanceOfferingsResponse
  property_count: 2
  slug: openapi-describe-reserved-elasticsearch-instance-offerings-response
- name: DescribeReservedElasticsearchInstancesRequest
  property_count: 0
  slug: openapi-describe-reserved-elasticsearch-instances-request
- name: DescribeReservedElasticsearchInstancesResponse
  property_count: 2
  slug: openapi-describe-reserved-elasticsearch-instances-response
- name: DescribeVpcEndpointsRequest
  property_count: 1
  slug: openapi-describe-vpc-endpoints-request
- name: DescribeVpcEndpointsResponse
  property_count: 2
  slug: openapi-describe-vpc-endpoints-response
- name: Description
  property_count: 0
  slug: openapi-description
- name: DisableTimestamp
  property_count: 0
  slug: openapi-disable-timestamp
- name: DisabledOperationException
  property_count: 0
  slug: openapi-disabled-operation-exception
- name: DissociatePackageRequest
  property_count: 0
  slug: openapi-dissociate-package-request
- name: DissociatePackageResponse
  property_count: 1
  slug: openapi-dissociate-package-response
- name: DomainArn
  property_count: 0
  slug: openapi-domain-arn
- name: DomainEndpointOptions
  property_count: 5
  slug: openapi-domain-endpoint-options
- name: DomainEndpointOptionsStatus
  property_count: 2
  slug: openapi-domain-endpoint-options-status
- name: DomainId
  property_count: 0
  slug: openapi-domain-id
- name: DomainInfoList
  property_count: 0
  slug: openapi-domain-info-list
- name: DomainInfo
  property_count: 2
  slug: openapi-domain-info
- name: DomainInformation
  property_count: 3
  slug: openapi-domain-information
- name: DomainNameFqdn
  property_count: 0
  slug: openapi-domain-name-fqdn
- name: DomainNameList
  property_count: 0
  slug: openapi-domain-name-list
- name: DomainName
  property_count: 0
  slug: openapi-domain-name
- name: DomainPackageDetailsList
  property_count: 0
  slug: openapi-domain-package-details-list
- name: DomainPackageDetails
  property_count: 9
  slug: openapi-domain-package-details
- name: DomainPackageStatus
  property_count: 0
  slug: openapi-domain-package-status
- name: Double
  property_count: 0
  slug: openapi-double
- name: DryRunResults
  property_count: 2
  slug: openapi-dry-run-results
- name: DryRun
  property_count: 0
  slug: openapi-dry-run
- name: Duration
  property_count: 2
  slug: openapi-duration
- name: DurationValue
  property_count: 0
  slug: openapi-duration-value
- name: EBSOptions
  property_count: 5
  slug: openapi-ebs-options
- name: EBSOptionsStatus
  property_count: 2
  slug: openapi-ebs-options-status
- name: ElasticsearchClusterConfig
  property_count: 11
  slug: openapi-elasticsearch-cluster-config
- name: ElasticsearchClusterConfigStatus
  property_count: 2
  slug: openapi-elasticsearch-cluster-config-status
- name: ElasticsearchDomainConfig
  property_count: 15
  slug: openapi-elasticsearch-domain-config
- name: ElasticsearchDomainStatusList
  property_count: 0
  slug: openapi-elasticsearch-domain-status-list
- name: ElasticsearchDomainStatus
  property_count: 25
  slug: openapi-elasticsearch-domain-status
- name: ElasticsearchInstanceTypeList
  property_count: 0
  slug: openapi-elasticsearch-instance-type-list
- name: ElasticsearchVersionList
  property_count: 0
  slug: openapi-elasticsearch-version-list
- name: ElasticsearchVersionStatus
  property_count: 2
  slug: openapi-elasticsearch-version-status
- name: ElasticsearchVersionString
  property_count: 0
  slug: openapi-elasticsearch-version-string
- name: EncryptionAtRestOptions
  property_count: 2
  slug: openapi-encryption-at-rest-options
- name: EncryptionAtRestOptionsStatus
  property_count: 2
  slug: openapi-encryption-at-rest-options-status
- name: Endpoint
  property_count: 0
  slug: openapi-endpoint
- name: EndpointsMap
  property_count: 0
  slug: openapi-endpoints-map
- name: EngineType
  property_count: 0
  slug: openapi-engine-type
- name: ErrorDetails
  property_count: 2
  slug: openapi-error-details
- name: ErrorMessage
  property_count: 0
  slug: openapi-error-message
- name: ErrorType
  property_count: 0
  slug: openapi-error-type
- name: ESPartitionInstanceType
  property_count: 0
  slug: openapi-es-partition-instance-type
- name: ESWarmPartitionInstanceType
  property_count: 0
  slug: openapi-es-warm-partition-instance-type
- name: FilterList
  property_count: 0
  slug: openapi-filter-list
- name: Filter
  property_count: 2
  slug: openapi-filter
- name: GetCompatibleElasticsearchVersionsRequest
  property_count: 0
  slug: openapi-get-compatible-elasticsearch-versions-request
- name: GetCompatibleElasticsearchVersionsResponse
  property_count: 1
  slug: openapi-get-compatible-elasticsearch-versions-response
- name: GetPackageVersionHistoryRequest
  property_count: 0
  slug: openapi-get-package-version-history-request
- name: GetPackageVersionHistoryResponse
  property_count: 3
  slug: openapi-get-package-version-history-response
- name: GetUpgradeHistoryRequest
  property_count: 0
  slug: openapi-get-upgrade-history-request
- name: GetUpgradeHistoryResponse
  property_count: 2
  slug: openapi-get-upgrade-history-response
- name: GetUpgradeStatusRequest
  property_count: 0
  slug: openapi-get-upgrade-status-request
- name: GetUpgradeStatusResponse
  property_count: 3
  slug: openapi-get-upgrade-status-response
- name: GUID
  property_count: 0
  slug: openapi-guid
- name: IdentityPoolId
  property_count: 0
  slug: openapi-identity-pool-id
- name: InboundCrossClusterSearchConnection
  property_count: 4
  slug: openapi-inbound-cross-cluster-search-connection
- name: InboundCrossClusterSearchConnectionStatusCode
  property_count: 0
  slug: openapi-inbound-cross-cluster-search-connection-status-code
- name: InboundCrossClusterSearchConnectionStatus
  property_count: 2
  slug: openapi-inbound-cross-cluster-search-connection-status
- name: InboundCrossClusterSearchConnections
  property_count: 0
  slug: openapi-inbound-cross-cluster-search-connections
- name: InstanceCountLimits
  property_count: 2
  slug: openapi-instance-count-limits
- name: InstanceCount
  property_count: 0
  slug: openapi-instance-count
- name: InstanceLimits
  property_count: 1
  slug: openapi-instance-limits
- name: InstanceRole
  property_count: 0
  slug: openapi-instance-role
- name: IntegerClass
  property_count: 0
  slug: openapi-integer-class
- name: Integer
  property_count: 0
  slug: openapi-integer
- name: InternalException
  property_count: 0
  slug: openapi-internal-exception
- name: InvalidPaginationTokenException
  property_count: 0
  slug: openapi-invalid-pagination-token-exception
- name: InvalidTypeException
  property_count: 0
  slug: openapi-invalid-type-exception
- name: Issue
  property_count: 0
  slug: openapi-issue
- name: Issues
  property_count: 0
  slug: openapi-issues
- name: KmsKeyId
  property_count: 0
  slug: openapi-kms-key-id
- name: LastUpdated
  property_count: 0
  slug: openapi-last-updated
- name: LimitExceededException
  property_count: 0
  slug: openapi-limit-exceeded-exception
- name: LimitName
  property_count: 0
  slug: openapi-limit-name
- name: LimitValueList
  property_count: 0
  slug: openapi-limit-value-list
- name: LimitValue
  property_count: 0
  slug: openapi-limit-value
- name: LimitsByRole
  property_count: 0
  slug: openapi-limits-by-role
- name: Limits
  property_count: 3
  slug: openapi-limits
- name: ListDomainNamesRequest
  property_count: 0
  slug: openapi-list-domain-names-request
- name: ListDomainNamesResponse
  property_count: 1
  slug: openapi-list-domain-names-response
- name: ListDomainsForPackageRequest
  property_count: 0
  slug: openapi-list-domains-for-package-request
- name: ListDomainsForPackageResponse
  property_count: 2
  slug: openapi-list-domains-for-package-response
- name: ListElasticsearchInstanceTypesRequest
  property_count: 0
  slug: openapi-list-elasticsearch-instance-types-request
- name: ListElasticsearchInstanceTypesResponse
  property_count: 2
  slug: openapi-list-elasticsearch-instance-types-response
- name: ListElasticsearchVersionsRequest
  property_count: 0
  slug: openapi-list-elasticsearch-versions-request
- name: ListElasticsearchVersionsResponse
  property_count: 2
  slug: openapi-list-elasticsearch-versions-response
- name: ListPackagesForDomainRequest
  property_count: 0
  slug: openapi-list-packages-for-domain-request
- name: ListPackagesForDomainResponse
  property_count: 2
  slug: openapi-list-packages-for-domain-response
- name: ListTagsRequest
  property_count: 0
  slug: openapi-list-tags-request
- name: ListTagsResponse
  property_count: 1
  slug: openapi-list-tags-response
- name: ListVpcEndpointAccessRequest
  property_count: 0
  slug: openapi-list-vpc-endpoint-access-request
- name: ListVpcEndpointAccessResponse
  property_count: 2
  slug: openapi-list-vpc-endpoint-access-response
- name: ListVpcEndpointsForDomainRequest
  property_count: 0
  slug: openapi-list-vpc-endpoints-for-domain-request
- name: ListVpcEndpointsForDomainResponse
  property_count: 2
  slug: openapi-list-vpc-endpoints-for-domain-response
- name: ListVpcEndpointsRequest
  property_count: 0
  slug: openapi-list-vpc-endpoints-request
- name: ListVpcEndpointsResponse
  property_count: 2
  slug: openapi-list-vpc-endpoints-response
- name: LogPublishingOption
  property_count: 2
  slug: openapi-log-publishing-option
- name: LogPublishingOptions
  property_count: 0
  slug: openapi-log-publishing-options
- name: LogPublishingOptionsStatus
  property_count: 2
  slug: openapi-log-publishing-options-status
- name: LogType
  property_count: 0
  slug: openapi-log-type
- name: MasterUserOptions
  property_count: 3
  slug: openapi-master-user-options
- name: MaxResults
  property_count: 0
  slug: openapi-max-results
- name: MaximumInstanceCount
  property_count: 0
  slug: openapi-maximum-instance-count
- name: Message
  property_count: 0
  slug: openapi-message
- name: MinimumInstanceCount
  property_count: 0
  slug: openapi-minimum-instance-count
- name: NextToken
  property_count: 0
  slug: openapi-next-token
- name: NodeToNodeEncryptionOptions
  property_count: 1
  slug: openapi-node-to-node-encryption-options
- name: NodeToNodeEncryptionOptionsStatus
  property_count: 2
  slug: openapi-node-to-node-encryption-options-status
- name: NonEmptyString
  property_count: 0
  slug: openapi-non-empty-string
- name: OptionState
  property_count: 0
  slug: openapi-option-state
- name: OptionStatus
  property_count: 5
  slug: openapi-option-status
- name: OutboundCrossClusterSearchConnection
  property_count: 5
  slug: openapi-outbound-cross-cluster-search-connection
- name: OutboundCrossClusterSearchConnectionStatusCode
  property_count: 0
  slug: openapi-outbound-cross-cluster-search-connection-status-code
- name: OutboundCrossClusterSearchConnectionStatus
  property_count: 2
  slug: openapi-outbound-cross-cluster-search-connection-status
- name: OutboundCrossClusterSearchConnections
  property_count: 0
  slug: openapi-outbound-cross-cluster-search-connections
- name: OverallChangeStatus
  property_count: 0
  slug: openapi-overall-change-status
- name: OwnerId
  property_count: 0
  slug: openapi-owner-id
- name: PackageDescription
  property_count: 0
  slug: openapi-package-description
- name: PackageDetailsList
  property_count: 0
  slug: openapi-package-details-list
- name: PackageDetails
  property_count: 9
  slug: openapi-package-details
- name: PackageID
  property_count: 0
  slug: openapi-package-id
- name: PackageName
  property_count: 0
  slug: openapi-package-name
- name: PackageSource
  property_count: 2
  slug: openapi-package-source
- name: PackageStatus
  property_count: 0
  slug: openapi-package-status
- name: PackageType
  property_count: 0
  slug: openapi-package-type
- name: PackageVersionHistoryList
  property_count: 0
  slug: openapi-package-version-history-list
- name: PackageVersionHistory
  property_count: 3
  slug: openapi-package-version-history
- name: PackageVersion
  property_count: 0
  slug: openapi-package-version
- name: Password
  property_count: 0
  slug: openapi-password
- name: PolicyDocument
  property_count: 0
  slug: openapi-policy-document
- name: PrincipalType
  property_count: 0
  slug: openapi-principal-type
- name: PurchaseReservedElasticsearchInstanceOfferingRequest
  property_count: 3
  slug: openapi-purchase-reserved-elasticsearch-instance-offering-request
- name: PurchaseReservedElasticsearchInstanceOfferingResponse
  property_count: 2
  slug: openapi-purchase-reserved-elasticsearch-instance-offering-response
- name: RecurringChargeList
  property_count: 0
  slug: openapi-recurring-charge-list
- name: RecurringCharge
  property_count: 2
  slug: openapi-recurring-charge
- name: ReferencePath
  property_count: 0
  slug: openapi-reference-path
- name: Region
  property_count: 0
  slug: openapi-region
- name: RejectInboundCrossClusterSearchConnectionRequest
  property_count: 0
  slug: openapi-reject-inbound-cross-cluster-search-connection-request
- name: RejectInboundCrossClusterSearchConnectionResponse
  property_count: 1
  slug: openapi-reject-inbound-cross-cluster-search-connection-response
- name: RemoveTagsRequest
  property_count: 2
  slug: openapi-remove-tags-request
- name: ReservationToken
  property_count: 0
  slug: openapi-reservation-token
- name: ReservedElasticsearchInstanceList
  property_count: 0
  slug: openapi-reserved-elasticsearch-instance-list
- name: ReservedElasticsearchInstanceOfferingList
  property_count: 0
  slug: openapi-reserved-elasticsearch-instance-offering-list
- name: ReservedElasticsearchInstanceOffering
  property_count: 8
  slug: openapi-reserved-elasticsearch-instance-offering
- name: ReservedElasticsearchInstancePaymentOption
  property_count: 0
  slug: openapi-reserved-elasticsearch-instance-payment-option
- name: ReservedElasticsearchInstance
  property_count: 13
  slug: openapi-reserved-elasticsearch-instance
- name: ResourceAlreadyExistsException
  property_count: 0
  slug: openapi-resource-already-exists-exception
- name: ResourceNotFoundException
  property_count: 0
  slug: openapi-resource-not-found-exception
- name: RevokeVpcEndpointAccessRequest
  property_count: 1
  slug: openapi-revoke-vpc-endpoint-access-request
- name: RevokeVpcEndpointAccessResponse
  property_count: 0
  slug: openapi-revoke-vpc-endpoint-access-response
- name: RoleArn
  property_count: 0
  slug: openapi-role-arn
- name: RollbackOnDisable
  property_count: 0
  slug: openapi-rollback-on-disable
- name: S3BucketName
  property_count: 0
  slug: openapi-s3-bucket-name
- name: S3Key
  property_count: 0
  slug: openapi-s3-key
- name: SAMLEntityId
  property_count: 0
  slug: openapi-saml-entity-id
- name: SAMLIdp
  property_count: 2
  slug: openapi-saml-idp
- name: SAMLMetadata
  property_count: 0
  slug: openapi-saml-metadata
- name: SAMLOptionsInput
  property_count: 7
  slug: openapi-saml-options-input
- name: SAMLOptionsOutput
  property_count: 5
  slug: openapi-saml-options-output
- name: ScheduledAutoTuneActionType
  property_count: 0
  slug: openapi-scheduled-auto-tune-action-type
- name: ScheduledAutoTuneDescription
  property_count: 0
  slug: openapi-scheduled-auto-tune-description
- name: ScheduledAutoTuneDetails
  property_count: 4
  slug: openapi-scheduled-auto-tune-details
- name: ScheduledAutoTuneSeverityType
  property_count: 0
  slug: openapi-scheduled-auto-tune-severity-type
- name: ServiceSoftwareOptions
  property_count: 8
  slug: openapi-service-software-options
- name: ServiceUrl
  property_count: 0
  slug: openapi-service-url
- name: SnapshotOptions
  property_count: 1
  slug: openapi-snapshot-options
- name: SnapshotOptionsStatus
  property_count: 2
  slug: openapi-snapshot-options-status
- name: StartAt
  property_count: 0
  slug: openapi-start-at
- name: StartElasticsearchServiceSoftwareUpdateRequest
  property_count: 1
  slug: openapi-start-elasticsearch-service-software-update-request
- name: StartElasticsearchServiceSoftwareUpdateResponse
  property_count: 1
  slug: openapi-start-elasticsearch-service-software-update-response
- name: StartTimestamp
  property_count: 0
  slug: openapi-start-timestamp
- name: StorageSubTypeName
  property_count: 0
  slug: openapi-storage-sub-type-name
- name: StorageTypeLimitList
  property_count: 0
  slug: openapi-storage-type-limit-list
- name: StorageTypeLimit
  property_count: 2
  slug: openapi-storage-type-limit
- name: StorageTypeList
  property_count: 0
  slug: openapi-storage-type-list
- name: StorageTypeName
  property_count: 0
  slug: openapi-storage-type-name
- name: StorageType
  property_count: 3
  slug: openapi-storage-type
- name: StringList
  property_count: 0
  slug: openapi-string-list
- name: String
  property_count: 0
  slug: openapi-string
- name: TagKey
  property_count: 0
  slug: openapi-tag-key
- name: TagList
  property_count: 0
  slug: openapi-tag-list
- name: Tag
  property_count: 2
  slug: openapi-tag
- name: TagValue
  property_count: 0
  slug: openapi-tag-value
- name: TimeUnit
  property_count: 0
  slug: openapi-time-unit
- name: TLSSecurityPolicy
  property_count: 0
  slug: openapi-tls-security-policy
- name: TotalNumberOfStages
  property_count: 0
  slug: openapi-total-number-of-stages
- name: UIntValue
  property_count: 0
  slug: openapi-u-int-value
- name: UpdateElasticsearchDomainConfigRequest
  property_count: 14
  slug: openapi-update-elasticsearch-domain-config-request
- name: UpdateElasticsearchDomainConfigResponse
  property_count: 2
  slug: openapi-update-elasticsearch-domain-config-response
- name: UpdatePackageRequest
  property_count: 4
  slug: openapi-update-package-request
- name: UpdatePackageResponse
  property_count: 1
  slug: openapi-update-package-response
- name: UpdateTimestamp
  property_count: 0
  slug: openapi-update-timestamp
- name: UpdateVpcEndpointRequest
  property_count: 2
  slug: openapi-update-vpc-endpoint-request
- name: UpdateVpcEndpointResponse
  property_count: 1
  slug: openapi-update-vpc-endpoint-response
- name: UpgradeElasticsearchDomainRequest
  property_count: 3
  slug: openapi-upgrade-elasticsearch-domain-request
- name: UpgradeElasticsearchDomainResponse
  property_count: 4
  slug: openapi-upgrade-elasticsearch-domain-response
- name: UpgradeHistoryList
  property_count: 0
  slug: openapi-upgrade-history-list
- name: UpgradeHistory
  property_count: 4
  slug: openapi-upgrade-history
- name: UpgradeName
  property_count: 0
  slug: openapi-upgrade-name
- name: UpgradeStatus
  property_count: 0
  slug: openapi-upgrade-status
- name: UpgradeStepItem
  property_count: 4
  slug: openapi-upgrade-step-item
- name: UpgradeStep
  property_count: 0
  slug: openapi-upgrade-step
- name: UpgradeStepsList
  property_count: 0
  slug: openapi-upgrade-steps-list
- name: UserPoolId
  property_count: 0
  slug: openapi-user-pool-id
- name: Username
  property_count: 0
  slug: openapi-username
- name: ValidationException
  property_count: 0
  slug: openapi-validation-exception
- name: ValueStringList
  property_count: 0
  slug: openapi-value-string-list
- name: VolumeType
  property_count: 0
  slug: openapi-volume-type
- name: VPCDerivedInfo
  property_count: 4
  slug: openapi-vpc-derived-info
- name: VPCDerivedInfoStatus
  property_count: 2
  slug: openapi-vpc-derived-info-status
- name: VpcEndpointErrorCode
  property_count: 0
  slug: openapi-vpc-endpoint-error-code
- name: VpcEndpointErrorList
  property_count: 0
  slug: openapi-vpc-endpoint-error-list
- name: VpcEndpointError
  property_count: 3
  slug: openapi-vpc-endpoint-error
- name: VpcEndpointIdList
  property_count: 0
  slug: openapi-vpc-endpoint-id-list
- name: VpcEndpointId
  property_count: 0
  slug: openapi-vpc-endpoint-id
- name: VpcEndpoint
  property_count: 6
  slug: openapi-vpc-endpoint
- name: VpcEndpointStatus
  property_count: 0
  slug: openapi-vpc-endpoint-status
- name: VpcEndpointSummaryList
  property_count: 0
  slug: openapi-vpc-endpoint-summary-list
- name: VpcEndpointSummary
  property_count: 4
  slug: openapi-vpc-endpoint-summary
- name: VpcEndpoints
  property_count: 0
  slug: openapi-vpc-endpoints
- name: VPCOptions
  property_count: 2
  slug: openapi-vpc-options
- name: ZoneAwarenessConfig
  property_count: 1
  slug: openapi-zone-awareness-config
json_structures:
- name: Openapi Accept Inbound Cross Cluster Search Connection Request Structure
  property_count: 0
  slug: openapi-accept-inbound-cross-cluster-search-connection-request-structure
- name: Openapi Accept Inbound Cross Cluster Search Connection Response Structure
  property_count: 1
  slug: openapi-accept-inbound-cross-cluster-search-connection-response-structure
- name: Openapi Access Denied Exception Structure
  property_count: 0
  slug: openapi-access-denied-exception-structure
- name: Openapi Access Policies Status Structure
  property_count: 2
  slug: openapi-access-policies-status-structure
- name: Openapi Add Tags Request Structure
  property_count: 2
  slug: openapi-add-tags-request-structure
- name: Openapi Additional Limit List Structure
  property_count: 0
  slug: openapi-additional-limit-list-structure
- name: Openapi Additional Limit Structure
  property_count: 2
  slug: openapi-additional-limit-structure
- name: Openapi Advanced Options Status Structure
  property_count: 2
  slug: openapi-advanced-options-status-structure
- name: Openapi Advanced Options Structure
  property_count: 0
  slug: openapi-advanced-options-structure
- name: Openapi Advanced Security Options Input Structure
  property_count: 5
  slug: openapi-advanced-security-options-input-structure
- name: Openapi Advanced Security Options Status Structure
  property_count: 2
  slug: openapi-advanced-security-options-status-structure
- name: Openapi Advanced Security Options Structure
  property_count: 5
  slug: openapi-advanced-security-options-structure
- name: Openapi Arn Structure
  property_count: 0
  slug: openapi-arn-structure
- name: Openapi Associate Package Request Structure
  property_count: 0
  slug: openapi-associate-package-request-structure
- name: Openapi Associate Package Response Structure
  property_count: 1
  slug: openapi-associate-package-response-structure
- name: Openapi Authorize Vpc Endpoint Access Request Structure
  property_count: 1
  slug: openapi-authorize-vpc-endpoint-access-request-structure
- name: Openapi Authorize Vpc Endpoint Access Response Structure
  property_count: 1
  slug: openapi-authorize-vpc-endpoint-access-response-structure
- name: Openapi Authorized Principal List Structure
  property_count: 0
  slug: openapi-authorized-principal-list-structure
- name: Openapi Authorized Principal Structure
  property_count: 2
  slug: openapi-authorized-principal-structure
- name: Openapi Auto Tune Date Structure
  property_count: 0
  slug: openapi-auto-tune-date-structure
- name: Openapi Auto Tune Desired State Structure
  property_count: 0
  slug: openapi-auto-tune-desired-state-structure
- name: Openapi Auto Tune Details Structure
  property_count: 1
  slug: openapi-auto-tune-details-structure
- name: Openapi Auto Tune List Structure
  property_count: 0
  slug: openapi-auto-tune-list-structure
- name: Openapi Auto Tune Maintenance Schedule List Structure
  property_count: 0
  slug: openapi-auto-tune-maintenance-schedule-list-structure
- name: Openapi Auto Tune Maintenance Schedule Structure
  property_count: 3
  slug: openapi-auto-tune-maintenance-schedule-structure
- name: Openapi Auto Tune Options Input Structure
  property_count: 2
  slug: openapi-auto-tune-options-input-structure
- name: Openapi Auto Tune Options Output Structure
  property_count: 2
  slug: openapi-auto-tune-options-output-structure
- name: Openapi Auto Tune Options Status Structure
  property_count: 2
  slug: openapi-auto-tune-options-status-structure
- name: Openapi Auto Tune Options Structure
  property_count: 3
  slug: openapi-auto-tune-options-structure
- name: Openapi Auto Tune State Structure
  property_count: 0
  slug: openapi-auto-tune-state-structure
- name: Openapi Auto Tune Status Structure
  property_count: 6
  slug: openapi-auto-tune-status-structure
- name: Openapi Auto Tune Structure
  property_count: 2
  slug: openapi-auto-tune-structure
- name: Openapi Auto Tune Type Structure
  property_count: 0
  slug: openapi-auto-tune-type-structure
- name: Openapi Aws Account Structure
  property_count: 0
  slug: openapi-aws-account-structure
- name: Openapi Backend Role Structure
  property_count: 0
  slug: openapi-backend-role-structure
- name: Openapi Base Exception Structure
  property_count: 0
  slug: openapi-base-exception-structure
- name: Openapi Boolean Structure
  property_count: 0
  slug: openapi-boolean-structure
- name: Openapi Cancel Elasticsearch Service Software Update Request Structure
  property_count: 1
  slug: openapi-cancel-elasticsearch-service-software-update-request-structure
- name: Openapi Cancel Elasticsearch Service Software Update Response Structure
  property_count: 1
  slug: openapi-cancel-elasticsearch-service-software-update-response-structure
- name: Openapi Change Progress Details Structure
  property_count: 2
  slug: openapi-change-progress-details-structure
- name: Openapi Change Progress Stage List Structure
  property_count: 0
  slug: openapi-change-progress-stage-list-structure
- name: Openapi Change Progress Stage Name Structure
  property_count: 0
  slug: openapi-change-progress-stage-name-structure
- name: Openapi Change Progress Stage Status Structure
  property_count: 0
  slug: openapi-change-progress-stage-status-structure
- name: Openapi Change Progress Stage Structure
  property_count: 4
  slug: openapi-change-progress-stage-structure
- name: Openapi Change Progress Status Details Structure
  property_count: 7
  slug: openapi-change-progress-status-details-structure
- name: Openapi Client Token Structure
  property_count: 0
  slug: openapi-client-token-structure
- name: Openapi Cloud Watch Logs Log Group Arn Structure
  property_count: 0
  slug: openapi-cloud-watch-logs-log-group-arn-structure
- name: Openapi Cognito Options Status Structure
  property_count: 2
  slug: openapi-cognito-options-status-structure
- name: Openapi Cognito Options Structure
  property_count: 4
  slug: openapi-cognito-options-structure
- name: Openapi Cold Storage Options Structure
  property_count: 1
  slug: openapi-cold-storage-options-structure
- name: Openapi Commit Message Structure
  property_count: 0
  slug: openapi-commit-message-structure
- name: Openapi Compatible Elasticsearch Versions List Structure
  property_count: 0
  slug: openapi-compatible-elasticsearch-versions-list-structure
- name: Openapi Compatible Versions Map Structure
  property_count: 2
  slug: openapi-compatible-versions-map-structure
- name: Openapi Conflict Exception Structure
  property_count: 0
  slug: openapi-conflict-exception-structure
- name: Openapi Connection Alias Structure
  property_count: 0
  slug: openapi-connection-alias-structure
- name: Openapi Create Elasticsearch Domain Request Structure
  property_count: 16
  slug: openapi-create-elasticsearch-domain-request-structure
- name: Openapi Create Elasticsearch Domain Response Structure
  property_count: 1
  slug: openapi-create-elasticsearch-domain-response-structure
- name: Openapi Create Outbound Cross Cluster Search Connection Request Structure
  property_count: 3
  slug: openapi-create-outbound-cross-cluster-search-connection-request-structure
- name: Openapi Create Outbound Cross Cluster Search Connection Response Structure
  property_count: 5
  slug: openapi-create-outbound-cross-cluster-search-connection-response-structure
- name: Openapi Create Package Request Structure
  property_count: 4
  slug: openapi-create-package-request-structure
- name: Openapi Create Package Response Structure
  property_count: 1
  slug: openapi-create-package-response-structure
- name: Openapi Create Vpc Endpoint Request Structure
  property_count: 3
  slug: openapi-create-vpc-endpoint-request-structure
- name: Openapi Create Vpc Endpoint Response Structure
  property_count: 1
  slug: openapi-create-vpc-endpoint-response-structure
- name: Openapi Created At Structure
  property_count: 0
  slug: openapi-created-at-structure
- name: Openapi Cross Cluster Search Connection Id Structure
  property_count: 0
  slug: openapi-cross-cluster-search-connection-id-structure
- name: Openapi Cross Cluster Search Connection Status Message Structure
  property_count: 0
  slug: openapi-cross-cluster-search-connection-status-message-structure
- name: Openapi Delete Elasticsearch Domain Request Structure
  property_count: 0
  slug: openapi-delete-elasticsearch-domain-request-structure
- name: Openapi Delete Elasticsearch Domain Response Structure
  property_count: 1
  slug: openapi-delete-elasticsearch-domain-response-structure
- name: Openapi Delete Inbound Cross Cluster Search Connection Request Structure
  property_count: 0
  slug: openapi-delete-inbound-cross-cluster-search-connection-request-structure
- name: Openapi Delete Inbound Cross Cluster Search Connection Response Structure
  property_count: 1
  slug: openapi-delete-inbound-cross-cluster-search-connection-response-structure
- name: Openapi Delete Outbound Cross Cluster Search Connection Request Structure
  property_count: 0
  slug: openapi-delete-outbound-cross-cluster-search-connection-request-structure
- name: Openapi Delete Outbound Cross Cluster Search Connection Response Structure
  property_count: 1
  slug: openapi-delete-outbound-cross-cluster-search-connection-response-structure
- name: Openapi Delete Package Request Structure
  property_count: 0
  slug: openapi-delete-package-request-structure
- name: Openapi Delete Package Response Structure
  property_count: 1
  slug: openapi-delete-package-response-structure
- name: Openapi Delete Vpc Endpoint Request Structure
  property_count: 0
  slug: openapi-delete-vpc-endpoint-request-structure
- name: Openapi Delete Vpc Endpoint Response Structure
  property_count: 1
  slug: openapi-delete-vpc-endpoint-response-structure
- name: Openapi Deployment Close Date Time Stamp Structure
  property_count: 0
  slug: openapi-deployment-close-date-time-stamp-structure
- name: Openapi Deployment Status Structure
  property_count: 0
  slug: openapi-deployment-status-structure
- name: Openapi Deployment Type Structure
  property_count: 0
  slug: openapi-deployment-type-structure
- name: Openapi Describe Domain Auto Tunes Request Structure
  property_count: 2
  slug: openapi-describe-domain-auto-tunes-request-structure
- name: Openapi Describe Domain Auto Tunes Response Structure
  property_count: 2
  slug: openapi-describe-domain-auto-tunes-response-structure
- name: Openapi Describe Domain Change Progress Request Structure
  property_count: 0
  slug: openapi-describe-domain-change-progress-request-structure
- name: Openapi Describe Domain Change Progress Response Structure
  property_count: 1
  slug: openapi-describe-domain-change-progress-response-structure
- name: Openapi Describe Elasticsearch Domain Config Request Structure
  property_count: 0
  slug: openapi-describe-elasticsearch-domain-config-request-structure
- name: Openapi Describe Elasticsearch Domain Config Response Structure
  property_count: 1
  slug: openapi-describe-elasticsearch-domain-config-response-structure
- name: Openapi Describe Elasticsearch Domain Request Structure
  property_count: 0
  slug: openapi-describe-elasticsearch-domain-request-structure
- name: Openapi Describe Elasticsearch Domain Response Structure
  property_count: 1
  slug: openapi-describe-elasticsearch-domain-response-structure
- name: Openapi Describe Elasticsearch Domains Request Structure
  property_count: 1
  slug: openapi-describe-elasticsearch-domains-request-structure
- name: Openapi Describe Elasticsearch Domains Response Structure
  property_count: 1
  slug: openapi-describe-elasticsearch-domains-response-structure
- name: Openapi Describe Elasticsearch Instance Type Limits Request Structure
  property_count: 0
  slug: openapi-describe-elasticsearch-instance-type-limits-request-structure
- name: Openapi Describe Elasticsearch Instance Type Limits Response Structure
  property_count: 1
  slug: openapi-describe-elasticsearch-instance-type-limits-response-structure
- name: Openapi Describe Inbound Cross Cluster Search Connections Request Structure
  property_count: 3
  slug: openapi-describe-inbound-cross-cluster-search-connections-request-structure
- name: Openapi Describe Inbound Cross Cluster Search Connections Response Structure
  property_count: 2
  slug: openapi-describe-inbound-cross-cluster-search-connections-response-structure
- name: Openapi Describe Outbound Cross Cluster Search Connections Request Structure
  property_count: 3
  slug: openapi-describe-outbound-cross-cluster-search-connections-request-structure
- name: Openapi Describe Outbound Cross Cluster Search Connections Response Structure
  property_count: 2
  slug: openapi-describe-outbound-cross-cluster-search-connections-response-structure
- name: Openapi Describe Packages Filter List Structure
  property_count: 0
  slug: openapi-describe-packages-filter-list-structure
- name: Openapi Describe Packages Filter Name Structure
  property_count: 0
  slug: openapi-describe-packages-filter-name-structure
- name: Openapi Describe Packages Filter Structure
  property_count: 2
  slug: openapi-describe-packages-filter-structure
- name: Openapi Describe Packages Filter Value Structure
  property_count: 0
  slug: openapi-describe-packages-filter-value-structure
- name: Openapi Describe Packages Filter Values Structure
  property_count: 0
  slug: openapi-describe-packages-filter-values-structure
- name: Openapi Describe Packages Request Structure
  property_count: 3
  slug: openapi-describe-packages-request-structure
- name: Openapi Describe Packages Response Structure
  property_count: 2
  slug: openapi-describe-packages-response-structure
- name: Openapi Describe Reserved Elasticsearch Instance Offerings Request Structure
  property_count: 0
  slug: openapi-describe-reserved-elasticsearch-instance-offerings-request-structure
- name: Openapi Describe Reserved Elasticsearch Instance Offerings Response Structure
  property_count: 2
  slug: openapi-describe-reserved-elasticsearch-instance-offerings-response-structure
- name: Openapi Describe Reserved Elasticsearch Instances Request Structure
  property_count: 0
  slug: openapi-describe-reserved-elasticsearch-instances-request-structure
- name: Openapi Describe Reserved Elasticsearch Instances Response Structure
  property_count: 2
  slug: openapi-describe-reserved-elasticsearch-instances-response-structure
- name: Openapi Describe Vpc Endpoints Request Structure
  property_count: 1
  slug: openapi-describe-vpc-endpoints-request-structure
- name: Openapi Describe Vpc Endpoints Response Structure
  property_count: 2
  slug: openapi-describe-vpc-endpoints-response-structure
- name: Openapi Description Structure
  property_count: 0
  slug: openapi-description-structure
- name: Openapi Disable Timestamp Structure
  property_count: 0
  slug: openapi-disable-timestamp-structure
- name: Openapi Disabled Operation Exception Structure
  property_count: 0
  slug: openapi-disabled-operation-exception-structure
- name: Openapi Dissociate Package Request Structure
  property_count: 0
  slug: openapi-dissociate-package-request-structure
- name: Openapi Dissociate Package Response Structure
  property_count: 1
  slug: openapi-dissociate-package-response-structure
- name: Openapi Domain Arn Structure
  property_count: 0
  slug: openapi-domain-arn-structure
- name: Openapi Domain Endpoint Options Status Structure
  property_count: 2
  slug: openapi-domain-endpoint-options-status-structure
- name: Openapi Domain Endpoint Options Structure
  property_count: 5
  slug: openapi-domain-endpoint-options-structure
- name: Openapi Domain Id Structure
  property_count: 0
  slug: openapi-domain-id-structure
- name: Openapi Domain Info List Structure
  property_count: 0
  slug: openapi-domain-info-list-structure
- name: Openapi Domain Info Structure
  property_count: 2
  slug: openapi-domain-info-structure
- name: Openapi Domain Information Structure
  property_count: 3
  slug: openapi-domain-information-structure
- name: Openapi Domain Name Fqdn Structure
  property_count: 0
  slug: openapi-domain-name-fqdn-structure
- name: Openapi Domain Name List Structure
  property_count: 0
  slug: openapi-domain-name-list-structure
- name: Openapi Domain Name Structure
  property_count: 0
  slug: openapi-domain-name-structure
- name: Openapi Domain Package Details List Structure
  property_count: 0
  slug: openapi-domain-package-details-list-structure
- name: Openapi Domain Package Details Structure
  property_count: 9
  slug: openapi-domain-package-details-structure
- name: Openapi Domain Package Status Structure
  property_count: 0
  slug: openapi-domain-package-status-structure
- name: Openapi Double Structure
  property_count: 0
  slug: openapi-double-structure
- name: Openapi Dry Run Results Structure
  property_count: 2
  slug: openapi-dry-run-results-structure
- name: Openapi Dry Run Structure
  property_count: 0
  slug: openapi-dry-run-structure
- name: Openapi Duration Structure
  property_count: 2
  slug: openapi-duration-structure
- name: Openapi Duration Value Structure
  property_count: 0
  slug: openapi-duration-value-structure
- name: Openapi Ebs Options Status Structure
  property_count: 2
  slug: openapi-ebs-options-status-structure
- name: Openapi Ebs Options Structure
  property_count: 5
  slug: openapi-ebs-options-structure
- name: Openapi Elasticsearch Cluster Config Status Structure
  property_count: 2
  slug: openapi-elasticsearch-cluster-config-status-structure
- name: Openapi Elasticsearch Cluster Config Structure
  property_count: 11
  slug: openapi-elasticsearch-cluster-config-structure
- name: Openapi Elasticsearch Domain Config Structure
  property_count: 15
  slug: openapi-elasticsearch-domain-config-structure
- name: Openapi Elasticsearch Domain Status List Structure
  property_count: 0
  slug: openapi-elasticsearch-domain-status-list-structure
- name: Openapi Elasticsearch Domain Status Structure
  property_count: 25
  slug: openapi-elasticsearch-domain-status-structure
- name: Openapi Elasticsearch Instance Type List Structure
  property_count: 0
  slug: openapi-elasticsearch-instance-type-list-structure
- name: Openapi Elasticsearch Version List Structure
  property_count: 0
  slug: openapi-elasticsearch-version-list-structure
- name: Openapi Elasticsearch Version Status Structure
  property_count: 2
  slug: openapi-elasticsearch-version-status-structure
- name: Openapi Elasticsearch Version String Structure
  property_count: 0
  slug: openapi-elasticsearch-version-string-structure
- name: Openapi Encryption At Rest Options Status Structure
  property_count: 2
  slug: openapi-encryption-at-rest-options-status-structure
- name: Openapi Encryption At Rest Options Structure
  property_count: 2
  slug: openapi-encryption-at-rest-options-structure
- name: Openapi Endpoint Structure
  property_count: 0
  slug: openapi-endpoint-structure
- name: Openapi Endpoints Map Structure
  property_count: 0
  slug: openapi-endpoints-map-structure
- name: Openapi Engine Type Structure
  property_count: 0
  slug: openapi-engine-type-structure
- name: Openapi Error Details Structure
  property_count: 2
  slug: openapi-error-details-structure
- name: Openapi Error Message Structure
  property_count: 0
  slug: openapi-error-message-structure
- name: Openapi Error Type Structure
  property_count: 0
  slug: openapi-error-type-structure
- name: Openapi Es Partition Instance Type Structure
  property_count: 0
  slug: openapi-es-partition-instance-type-structure
- name: Openapi Es Warm Partition Instance Type Structure
  property_count: 0
  slug: openapi-es-warm-partition-instance-type-structure
- name: Openapi Filter List Structure
  property_count: 0
  slug: openapi-filter-list-structure
- name: Openapi Filter Structure
  property_count: 2
  slug: openapi-filter-structure
- name: Openapi Get Compatible Elasticsearch Versions Request Structure
  property_count: 0
  slug: openapi-get-compatible-elasticsearch-versions-request-structure
- name: Openapi Get Compatible Elasticsearch Versions Response Structure
  property_count: 1
  slug: openapi-get-compatible-elasticsearch-versions-response-structure
- name: Openapi Get Package Version History Request Structure
  property_count: 0
  slug: openapi-get-package-version-history-request-structure
- name: Openapi Get Package Version History Response Structure
  property_count: 3
  slug: openapi-get-package-version-history-response-structure
- name: Openapi Get Upgrade History Request Structure
  property_count: 0
  slug: openapi-get-upgrade-history-request-structure
- name: Openapi Get Upgrade History Response Structure
  property_count: 2
  slug: openapi-get-upgrade-history-response-structure
- name: Openapi Get Upgrade Status Request Structure
  property_count: 0
  slug: openapi-get-upgrade-status-request-structure
- name: Openapi Get Upgrade Status Response Structure
  property_count: 3
  slug: openapi-get-upgrade-status-response-structure
- name: Openapi Guid Structure
  property_count: 0
  slug: openapi-guid-structure
- name: Openapi Identity Pool Id Structure
  property_count: 0
  slug: openapi-identity-pool-id-structure
- name: Openapi Inbound Cross Cluster Search Connection Status Code Structure
  property_count: 0
  slug: openapi-inbound-cross-cluster-search-connection-status-code-structure
- name: Openapi Inbound Cross Cluster Search Connection Status Structure
  property_count: 2
  slug: openapi-inbound-cross-cluster-search-connection-status-structure
- name: Openapi Inbound Cross Cluster Search Connection Structure
  property_count: 4
  slug: openapi-inbound-cross-cluster-search-connection-structure
- name: Openapi Inbound Cross Cluster Search Connections Structure
  property_count: 0
  slug: openapi-inbound-cross-cluster-search-connections-structure
- name: Openapi Instance Count Limits Structure
  property_count: 2
  slug: openapi-instance-count-limits-structure
- name: Openapi Instance Count Structure
  property_count: 0
  slug: openapi-instance-count-structure
- name: Openapi Instance Limits Structure
  property_count: 1
  slug: openapi-instance-limits-structure
- name: Openapi Instance Role Structure
  property_count: 0
  slug: openapi-instance-role-structure
- name: Openapi Integer Class Structure
  property_count: 0
  slug: openapi-integer-class-structure
- name: Openapi Integer Structure
  property_count: 0
  slug: openapi-integer-structure
- name: Openapi Internal Exception Structure
  property_count: 0
  slug: openapi-internal-exception-structure
- name: Openapi Invalid Pagination Token Exception Structure
  property_count: 0
  slug: openapi-invalid-pagination-token-exception-structure
- name: Openapi Invalid Type Exception Structure
  property_count: 0
  slug: openapi-invalid-type-exception-structure
- name: Openapi Issue Structure
  property_count: 0
  slug: openapi-issue-structure
- name: Openapi Issues Structure
  property_count: 0
  slug: openapi-issues-structure
- name: Openapi Kms Key Id Structure
  property_count: 0
  slug: openapi-kms-key-id-structure
- name: Openapi Last Updated Structure
  property_count: 0
  slug: openapi-last-updated-structure
- name: Openapi Limit Exceeded Exception Structure
  property_count: 0
  slug: openapi-limit-exceeded-exception-structure
- name: Openapi Limit Name Structure
  property_count: 0
  slug: openapi-limit-name-structure
- name: Openapi Limit Value List Structure
  property_count: 0
  slug: openapi-limit-value-list-structure
- name: Openapi Limit Value Structure
  property_count: 0
  slug: openapi-limit-value-structure
- name: Openapi Limits By Role Structure
  property_count: 0
  slug: openapi-limits-by-role-structure
- name: Openapi Limits Structure
  property_count: 3
  slug: openapi-limits-structure
- name: Openapi List Domain Names Request Structure
  property_count: 0
  slug: openapi-list-domain-names-request-structure
- name: Openapi List Domain Names Response Structure
  property_count: 1
  slug: openapi-list-domain-names-response-structure
- name: Openapi List Domains For Package Request Structure
  property_count: 0
  slug: openapi-list-domains-for-package-request-structure
- name: Openapi List Domains For Package Response Structure
  property_count: 2
  slug: openapi-list-domains-for-package-response-structure
- name: Openapi List Elasticsearch Instance Types Request Structure
  property_count: 0
  slug: openapi-list-elasticsearch-instance-types-request-structure
- name: Openapi List Elasticsearch Instance Types Response Structure
  property_count: 2
  slug: openapi-list-elasticsearch-instance-types-response-structure
- name: Openapi List Elasticsearch Versions Request Structure
  property_count: 0
  slug: openapi-list-elasticsearch-versions-request-structure
- name: Openapi List Elasticsearch Versions Response Structure
  property_count: 2
  slug: openapi-list-elasticsearch-versions-response-structure
- name: Openapi List Packages For Domain Request Structure
  property_count: 0
  slug: openapi-list-packages-for-domain-request-structure
- name: Openapi List Packages For Domain Response Structure
  property_count: 2
  slug: openapi-list-packages-for-domain-response-structure
- name: Openapi List Tags Request Structure
  property_count: 0
  slug: openapi-list-tags-request-structure
- name: Openapi List Tags Response Structure
  property_count: 1
  slug: openapi-list-tags-response-structure
- name: Openapi List Vpc Endpoint Access Request Structure
  property_count: 0
  slug: openapi-list-vpc-endpoint-access-request-structure
- name: Openapi List Vpc Endpoint Access Response Structure
  property_count: 2
  slug: openapi-list-vpc-endpoint-access-response-structure
- name: Openapi List Vpc Endpoints For Domain Request Structure
  property_count: 0
  slug: openapi-list-vpc-endpoints-for-domain-request-structure
- name: Openapi List Vpc Endpoints For Domain Response Structure
  property_count: 2
  slug: openapi-list-vpc-endpoints-for-domain-response-structure
- name: Openapi List Vpc Endpoints Request Structure
  property_count: 0
  slug: openapi-list-vpc-endpoints-request-structure
- name: Openapi List Vpc Endpoints Response Structure
  property_count: 2
  slug: openapi-list-vpc-endpoints-response-structure
- name: Openapi Log Publishing Option Structure
  property_count: 2
  slug: openapi-log-publishing-option-structure
- name: Openapi Log Publishing Options Status Structure
  property_count: 2
  slug: openapi-log-publishing-options-status-structure
- name: Openapi Log Publishing Options Structure
  property_count: 0
  slug: openapi-log-publishing-options-structure
- name: Openapi Log Type Structure
  property_count: 0
  slug: openapi-log-type-structure
- name: Openapi Master User Options Structure
  property_count: 3
  slug: openapi-master-user-options-structure
- name: Openapi Max Results Structure
  property_count: 0
  slug: openapi-max-results-structure
- name: Openapi Maximum Instance Count Structure
  property_count: 0
  slug: openapi-maximum-instance-count-structure
- name: Openapi Message Structure
  property_count: 0
  slug: openapi-message-structure
- name: Openapi Minimum Instance Count Structure
  property_count: 0
  slug: openapi-minimum-instance-count-structure
- name: Openapi Next Token Structure
  property_count: 0
  slug: openapi-next-token-structure
- name: Openapi Node To Node Encryption Options Status Structure
  property_count: 2
  slug: openapi-node-to-node-encryption-options-status-structure
- name: Openapi Node To Node Encryption Options Structure
  property_count: 1
  slug: openapi-node-to-node-encryption-options-structure
- name: Openapi Non Empty String Structure
  property_count: 0
  slug: openapi-non-empty-string-structure
- name: Openapi Option State Structure
  property_count: 0
  slug: openapi-option-state-structure
- name: Openapi Option Status Structure
  property_count: 5
  slug: openapi-option-status-structure
- name: Openapi Outbound Cross Cluster Search Connection Status Code Structure
  property_count: 0
  slug: openapi-outbound-cross-cluster-search-connection-status-code-structure
- name: Openapi Outbound Cross Cluster Search Connection Status Structure
  property_count: 2
  slug: openapi-outbound-cross-cluster-search-connection-status-structure
- name: Openapi Outbound Cross Cluster Search Connection Structure
  property_count: 5
  slug: openapi-outbound-cross-cluster-search-connection-structure
- name: Openapi Outbound Cross Cluster Search Connections Structure
  property_count: 0
  slug: openapi-outbound-cross-cluster-search-connections-structure
- name: Openapi Overall Change Status Structure
  property_count: 0
  slug: openapi-overall-change-status-structure
- name: Openapi Owner Id Structure
  property_count: 0
  slug: openapi-owner-id-structure
- name: Openapi Package Description Structure
  property_count: 0
  slug: openapi-package-description-structure
- name: Openapi Package Details List Structure
  property_count: 0
  slug: openapi-package-details-list-structure
- name: Openapi Package Details Structure
  property_count: 9
  slug: openapi-package-details-structure
- name: Openapi Package Id Structure
  property_count: 0
  slug: openapi-package-id-structure
- name: Openapi Package Name Structure
  property_count: 0
  slug: openapi-package-name-structure
- name: Openapi Package Source Structure
  property_count: 2
  slug: openapi-package-source-structure
- name: Openapi Package Status Structure
  property_count: 0
  slug: openapi-package-status-structure
- name: Openapi Package Type Structure
  property_count: 0
  slug: openapi-package-type-structure
- name: Openapi Package Version History List Structure
  property_count: 0
  slug: openapi-package-version-history-list-structure
- name: Openapi Package Version History Structure
  property_count: 3
  slug: openapi-package-version-history-structure
- name: Openapi Package Version Structure
  property_count: 0
  slug: openapi-package-version-structure
- name: Openapi Password Structure
  property_count: 0
  slug: openapi-password-structure
- name: Openapi Policy Document Structure
  property_count: 0
  slug: openapi-policy-document-structure
- name: Openapi Principal Type Structure
  property_count: 0
  slug: openapi-principal-type-structure
- name: Openapi Purchase Reserved Elasticsearch Instance Offering Request Structure
  property_count: 3
  slug: openapi-purchase-reserved-elasticsearch-instance-offering-request-structure
- name: Openapi Purchase Reserved Elasticsearch Instance Offering Response Structure
  property_count: 2
  slug: openapi-purchase-reserved-elasticsearch-instance-offering-response-structure
- name: Openapi Recurring Charge List Structure
  property_count: 0
  slug: openapi-recurring-charge-list-structure
- name: Openapi Recurring Charge Structure
  property_count: 2
  slug: openapi-recurring-charge-structure
- name: Openapi Reference Path Structure
  property_count: 0
  slug: openapi-reference-path-structure
- name: Openapi Region Structure
  property_count: 0
  slug: openapi-region-structure
- name: Openapi Reject Inbound Cross Cluster Search Connection Request Structure
  property_count: 0
  slug: openapi-reject-inbound-cross-cluster-search-connection-request-structure
- name: Openapi Reject Inbound Cross Cluster Search Connection Response Structure
  property_count: 1
  slug: openapi-reject-inbound-cross-cluster-search-connection-response-structure
- name: Openapi Remove Tags Request Structure
  property_count: 2
  slug: openapi-remove-tags-request-structure
- name: Openapi Reservation Token Structure
  property_count: 0
  slug: openapi-reservation-token-structure
- name: Openapi Reserved Elasticsearch Instance List Structure
  property_count: 0
  slug: openapi-reserved-elasticsearch-instance-list-structure
- name: Openapi Reserved Elasticsearch Instance Offering List Structure
  property_count: 0
  slug: openapi-reserved-elasticsearch-instance-offering-list-structure
- name: Openapi Reserved Elasticsearch Instance Offering Structure
  property_count: 8
  slug: openapi-reserved-elasticsearch-instance-offering-structure
- name: Openapi Reserved Elasticsearch Instance Payment Option Structure
  property_count: 0
  slug: openapi-reserved-elasticsearch-instance-payment-option-structure
- name: Openapi Reserved Elasticsearch Instance Structure
  property_count: 13
  slug: openapi-reserved-elasticsearch-instance-structure
- name: Openapi Resource Already Exists Exception Structure
  property_count: 0
  slug: openapi-resource-already-exists-exception-structure
- name: Openapi Resource Not Found Exception Structure
  property_count: 0
  slug: openapi-resource-not-found-exception-structure
- name: Openapi Revoke Vpc Endpoint Access Request Structure
  property_count: 1
  slug: openapi-revoke-vpc-endpoint-access-request-structure
- name: Openapi Revoke Vpc Endpoint Access Response Structure
  property_count: 0
  slug: openapi-revoke-vpc-endpoint-access-response-structure
- name: Openapi Role Arn Structure
  property_count: 0
  slug: openapi-role-arn-structure
- name: Openapi Rollback On Disable Structure
  property_count: 0
  slug: openapi-rollback-on-disable-structure
- name: Openapi S3 Bucket Name Structure
  property_count: 0
  slug: openapi-s3-bucket-name-structure
- name: Openapi S3 Key Structure
  property_count: 0
  slug: openapi-s3-key-structure
- name: Openapi Saml Entity Id Structure
  property_count: 0
  slug: openapi-saml-entity-id-structure
- name: Openapi Saml Idp Structure
  property_count: 2
  slug: openapi-saml-idp-structure
- name: Openapi Saml Metadata Structure
  property_count: 0
  slug: openapi-saml-metadata-structure
- name: Openapi Saml Options Input Structure
  property_count: 7
  slug: openapi-saml-options-input-structure
- name: Openapi Saml Options Output Structure
  property_count: 5
  slug: openapi-saml-options-output-structure
- name: Openapi Scheduled Auto Tune Action Type Structure
  property_count: 0
  slug: openapi-scheduled-auto-tune-action-type-structure
- name: Openapi Scheduled Auto Tune Description Structure
  property_count: 0
  slug: openapi-scheduled-auto-tune-description-structure
- name: Openapi Scheduled Auto Tune Details Structure
  property_count: 4
  slug: openapi-scheduled-auto-tune-details-structure
- name: Openapi Scheduled Auto Tune Severity Type Structure
  property_count: 0
  slug: openapi-scheduled-auto-tune-severity-type-structure
- name: Openapi Service Software Options Structure
  property_count: 8
  slug: openapi-service-software-options-structure
- name: Openapi Service Url Structure
  property_count: 0
  slug: openapi-service-url-structure
- name: Openapi Snapshot Options Status Structure
  property_count: 2
  slug: openapi-snapshot-options-status-structure
- name: Openapi Snapshot Options Structure
  property_count: 1
  slug: openapi-snapshot-options-structure
- name: Openapi Start At Structure
  property_count: 0
  slug: openapi-start-at-structure
- name: Openapi Start Elasticsearch Service Software Update Request Structure
  property_count: 1
  slug: openapi-start-elasticsearch-service-software-update-request-structure
- name: Openapi Start Elasticsearch Service Software Update Response Structure
  property_count: 1
  slug: openapi-start-elasticsearch-service-software-update-response-structure
- name: Openapi Start Timestamp Structure
  property_count: 0
  slug: openapi-start-timestamp-structure
- name: Openapi Storage Sub Type Name Structure
  property_count: 0
  slug: openapi-storage-sub-type-name-structure
- name: Openapi Storage Type Limit List Structure
  property_count: 0
  slug: openapi-storage-type-limit-list-structure
- name: Openapi Storage Type Limit Structure
  property_count: 2
  slug: openapi-storage-type-limit-structure
- name: Openapi Storage Type List Structure
  property_count: 0
  slug: openapi-storage-type-list-structure
- name: Openapi Storage Type Name Structure
  property_count: 0
  slug: openapi-storage-type-name-structure
- name: Openapi Storage Type Structure
  property_count: 3
  slug: openapi-storage-type-structure
- name: Openapi String List Structure
  property_count: 0
  slug: openapi-string-list-structure
- name: Openapi String Structure
  property_count: 0
  slug: openapi-string-structure
- name: Openapi Tag Key Structure
  property_count: 0
  slug: openapi-tag-key-structure
- name: Openapi Tag List Structure
  property_count: 0
  slug: openapi-tag-list-structure
- name: Openapi Tag Structure
  property_count: 2
  slug: openapi-tag-structure
- name: Openapi Tag Value Structure
  property_count: 0
  slug: openapi-tag-value-structure
- name: Openapi Time Unit Structure
  property_count: 0
  slug: openapi-time-unit-structure
- name: Openapi Tls Security Policy Structure
  property_count: 0
  slug: openapi-tls-security-policy-structure
- name: Openapi Total Number Of Stages Structure
  property_count: 0
  slug: openapi-total-number-of-stages-structure
- name: Openapi U Int Value Structure
  property_count: 0
  slug: openapi-u-int-value-structure
- name: Openapi Update Elasticsearch Domain Config Request Structure
  property_count: 14
  slug: openapi-update-elasticsearch-domain-config-request-structure
- name: Openapi Update Elasticsearch Domain Config Response Structure
  property_count: 2
  slug: openapi-update-elasticsearch-domain-config-response-structure
- name: Openapi Update Package Request Structure
  property_count: 4
  slug: openapi-update-package-request-structure
- name: Openapi Update Package Response Structure
  property_count: 1
  slug: openapi-update-package-response-structure
- name: Openapi Update Timestamp Structure
  property_count: 0
  slug: openapi-update-timestamp-structure
- name: Openapi Update Vpc Endpoint Request Structure
  property_count: 2
  slug: openapi-update-vpc-endpoint-request-structure
- name: Openapi Update Vpc Endpoint Response Structure
  property_count: 1
  slug: openapi-update-vpc-endpoint-response-structure
- name: Openapi Upgrade Elasticsearch Domain Request Structure
  property_count: 3
  slug: openapi-upgrade-elasticsearch-domain-request-structure
- name: Openapi Upgrade Elasticsearch Domain Response Structure
  property_count: 4
  slug: openapi-upgrade-elasticsearch-domain-response-structure
- name: Openapi Upgrade History List Structure
  property_count: 0
  slug: openapi-upgrade-history-list-structure
- name: Openapi Upgrade History Structure
  property_count: 4
  slug: openapi-upgrade-history-structure
- name: Openapi Upgrade Name Structure
  property_count: 0
  slug: openapi-upgrade-name-structure
- name: Openapi Upgrade Status Structure
  property_count: 0
  slug: openapi-upgrade-status-structure
- name: Openapi Upgrade Step Item Structure
  property_count: 4
  slug: openapi-upgrade-step-item-structure
- name: Openapi Upgrade Step Structure
  property_count: 0
  slug: openapi-upgrade-step-structure
- name: Openapi Upgrade Steps List Structure
  property_count: 0
  slug: openapi-upgrade-steps-list-structure
- name: Openapi User Pool Id Structure
  property_count: 0
  slug: openapi-user-pool-id-structure
- name: Openapi Username Structure
  property_count: 0
  slug: openapi-username-structure
- name: Openapi Validation Exception Structure
  property_count: 0
  slug: openapi-validation-exception-structure
- name: Openapi Value String List Structure
  property_count: 0
  slug: openapi-value-string-list-structure
- name: Openapi Volume Type Structure
  property_count: 0
  slug: openapi-volume-type-structure
- name: Openapi Vpc Derived Info Status Structure
  property_count: 2
  slug: openapi-vpc-derived-info-status-structure
- name: Openapi Vpc Derived Info Structure
  property_count: 4
  slug: openapi-vpc-derived-info-structure
- name: Openapi Vpc Endpoint Error Code Structure
  property_count: 0
  slug: openapi-vpc-endpoint-error-code-structure
- name: Openapi Vpc Endpoint Error List Structure
  property_count: 0
  slug: openapi-vpc-endpoint-error-list-structure
- name: Openapi Vpc Endpoint Error Structure
  property_count: 3
  slug: openapi-vpc-endpoint-error-structure
- name: Openapi Vpc Endpoint Id List Structure
  property_count: 0
  slug: openapi-vpc-endpoint-id-list-structure
- name: Openapi Vpc Endpoint Id Structure
  property_count: 0
  slug: openapi-vpc-endpoint-id-structure
- name: Openapi Vpc Endpoint Status Structure
  property_count: 0
  slug: openapi-vpc-endpoint-status-structure
- name: Openapi Vpc Endpoint Structure
  property_count: 6
  slug: openapi-vpc-endpoint-structure
- name: Openapi Vpc Endpoint Summary List Structure
  property_count: 0
  slug: openapi-vpc-endpoint-summary-list-structure
- name: Openapi Vpc Endpoint Summary Structure
  property_count: 4
  slug: openapi-vpc-endpoint-summary-structure
- name: Openapi Vpc Endpoints Structure
  property_count: 0
  slug: openapi-vpc-endpoints-structure
- name: Openapi Vpc Options Structure
  property_count: 2
  slug: openapi-vpc-options-structure
- name: Openapi Zone Awareness Config Structure
  property_count: 1
  slug: openapi-zone-awareness-config-structure
jsonld:
- class_count: 237
  name: Amazon Opensearch Openapi Context
  property_count: 222
  slug: amazon-opensearch-openapi-context
layout: provider
modified: '2026-05-19'
name: Amazon OpenSearch Service API
nav: Providers
network: true
overview: 'Amazon OpenSearch Service API publishes 5 APIs on the [APIs.io](https://apis.io/) network, including Domain API, Es API, Packages API, and 2 more. Tagged areas include Analytics, Elasticsearch, and Search.


  The Amazon OpenSearch Service API catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon OpenSearch Service API''s developer surface includes authentication, developer portal, documentation, support, developer console, signup flow, and 20 more developer resources.'
plans:
- name: Amazon Opensearch Plans Pricing
  plan_count: 3
  slug: amazon-opensearch-plans-pricing
random_paper: 45
rate_limits:
- limit_count: 5
  name: Amazon Opensearch Rate Limits
  slug: amazon-opensearch-rate-limits
rules:
- name: Amazon OpenSearch Service API API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-opensearch-jsonschema-spectral-rules
- name: Amazon OpenSearch Service API API Rules
  rule_count: 27
  severity_counts:
    error: 10
    hint: 0
    info: 2
    warn: 15
  slug: amazon-opensearch-spectral-rules
score:
  band: strong
  composite: 65.9
  delta: 0.0
  facets:
    commercial_clarity: 81.6
    contract_quality: 74.2
    developer_ergonomics: 43.5
    discoverability: 72.2
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 65.9
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 5
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-opensearch/refs/heads/main/screenshots/amazon-opensearch-2026-06-20T171751.png
security:
- kind: authentication
  name: Amazon Opensearch Authentication
  slug: amazon-opensearch-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Opensearch Domain Security
  slug: amazon-opensearch-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Opensearch Vulnerability Disclosure
  slug: amazon-opensearch-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Opensearch Trust Center
  slug: amazon-opensearch-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-opensearch
tags:
- Analytics
- Elasticsearch
- Search
website: https://aws.amazon.com/opensearch-service/
---

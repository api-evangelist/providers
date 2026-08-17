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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.6
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 1
  name: Amazon Msk Agentic Access
  operation_count: 36
  slug: amazon-msk-agentic-access
  summary_line: 36 operations · 20 acting · 1 human-in-the-loop
api_count: 6
apis:
- description: The Clusters API from Amazon MSK — 18 operation(s) for clusters.
  name: Amazon MSK Clusters API
  slug: amazon-msk-clusters-api
- description: The Compatible Kafka Versions API from Amazon MSK — 1 operation(s) for compatible kafka versions.
  name: Amazon MSK Compatible Kafka Versions API
  slug: amazon-msk-compatible-kafka-versions-api
- description: The Configurations API from Amazon MSK — 4 operation(s) for configurations.
  name: Amazon MSK Configurations API
  slug: amazon-msk-configurations-api
- description: The Kafka Versions API from Amazon MSK — 1 operation(s) for kafka versions.
  name: Amazon MSK Kafka Versions API
  slug: amazon-msk-kafka-versions-api
- description: The Operations API from Amazon MSK — 1 operation(s) for operations.
  name: Amazon MSK Operations API
  slug: amazon-msk-operations-api
- description: The Tags API from Amazon MSK — 2 operation(s) for tags.
  name: Amazon MSK Tags API
  slug: amazon-msk-tags-api
artifact_total: 446
collections:
- collection_type: postman
  name: Managed Streaming for Kafka Clusters API
  slug: postman-amazon-msk-clusters-api
- collection_type: postman
  name: Managed Streaming for Kafka Clusters Compatible Kafka Versions API
  slug: postman-amazon-msk-compatible-kafka-versions-api
- collection_type: postman
  name: Managed Streaming for Kafka Clusters Configurations API
  slug: postman-amazon-msk-configurations-api
- collection_type: postman
  name: Managed Streaming for Kafka Clusters Kafka Versions API
  slug: postman-amazon-msk-kafka-versions-api
- collection_type: postman
  name: Managed Streaming for Kafka Clusters Operations API
  slug: postman-amazon-msk-operations-api
- collection_type: postman
  name: Managed Streaming for Kafka Clusters Tags API
  slug: postman-amazon-msk-tags-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Managed Streaming for Kafka Clusters API
  slug: open-amazon-msk-clusters-api
- collection_type: open
  name: Managed Streaming for Kafka Clusters Compatible Kafka Versions API
  slug: open-amazon-msk-compatible-kafka-versions-api
- collection_type: open
  name: Managed Streaming for Kafka Clusters Configurations API
  slug: open-amazon-msk-configurations-api
- collection_type: open
  name: Managed Streaming for Kafka Clusters Kafka Versions API
  slug: open-amazon-msk-kafka-versions-api
- collection_type: open
  name: Managed Streaming for Kafka Clusters Operations API
  slug: open-amazon-msk-operations-api
- collection_type: open
  name: Managed Streaming for Kafka Clusters Tags API
  slug: open-amazon-msk-tags-api
- collection_type: open
  name: Amazon MSK API
  slug: open-openapi
common:
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/aws/agent-toolkit-for-aws/tree/main/skills/specialized-skills/analytics-skills
- group: docs
  title: ''
  type: MCPDocumentation
  url: https://docs.aws.amazon.com/agent-toolkit/latest/userguide/getting-started-aws-mcp-server.html
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-msk/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-msk-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-msk-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-msk-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-msk-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-msk-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/msk/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/msk/
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
  url: https://aws.amazon.com/blogs/media/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/msk/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
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
  url: rules/amazon-msk-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-msk-vocabulary.yaml
created: '2026-03-16'
description: Amazon Managed Streaming for Apache Kafka (Amazon MSK) is a fully managed service that enables you to build and run applications that use Apache Kafka to process streaming data, with the infrastructure management handled by AWS.
examples:
- key_count: 1
  name: Msk Api Batch Associate Scram Secret Request Example
  slug: msk-api-batch-associate-scram-secret-request-example
- key_count: 2
  name: Msk Api Batch Associate Scram Secret Response Example
  slug: msk-api-batch-associate-scram-secret-response-example
- key_count: 1
  name: Msk Api Batch Disassociate Scram Secret Request Example
  slug: msk-api-batch-disassociate-scram-secret-request-example
- key_count: 2
  name: Msk Api Batch Disassociate Scram Secret Response Example
  slug: msk-api-batch-disassociate-scram-secret-response-example
- key_count: 0
  name: Msk Api Broker Az Distribution Example
  slug: msk-api-broker-az-distribution-example
- key_count: 3
  name: Msk Api Broker Ebs Volume Info Example
  slug: msk-api-broker-ebs-volume-info-example
- key_count: 3
  name: Msk Api Broker Logs Example
  slug: msk-api-broker-logs-example
- key_count: 6
  name: Msk Api Broker Node Group Info Example
  slug: msk-api-broker-node-group-info-example
- key_count: 6
  name: Msk Api Broker Node Info Example
  slug: msk-api-broker-node-info-example
- key_count: 3
  name: Msk Api Broker Software Info Example
  slug: msk-api-broker-software-info-example
- key_count: 3
  name: Msk Api Client Authentication Example
  slug: msk-api-client-authentication-example
- key_count: 0
  name: Msk Api Client Broker Example
  slug: msk-api-client-broker-example
- key_count: 2
  name: Msk Api Cloud Watch Logs Example
  slug: msk-api-cloud-watch-logs-example
- key_count: 11
  name: Msk Api Cluster Example
  slug: msk-api-cluster-example
- key_count: 19
  name: Msk Api Cluster Info Example
  slug: msk-api-cluster-info-example
- key_count: 11
  name: Msk Api Cluster Operation Info Example
  slug: msk-api-cluster-operation-info-example
- key_count: 2
  name: Msk Api Cluster Operation Step Example
  slug: msk-api-cluster-operation-step-example
- key_count: 1
  name: Msk Api Cluster Operation Step Info Example
  slug: msk-api-cluster-operation-step-info-example
- key_count: 0
  name: Msk Api Cluster State Example
  slug: msk-api-cluster-state-example
- key_count: 0
  name: Msk Api Cluster Type Example
  slug: msk-api-cluster-type-example
- key_count: 2
  name: Msk Api Compatible Kafka Version Example
  slug: msk-api-compatible-kafka-version-example
- key_count: 7
  name: Msk Api Configuration Example
  slug: msk-api-configuration-example
- key_count: 2
  name: Msk Api Configuration Info Example
  slug: msk-api-configuration-info-example
- key_count: 3
  name: Msk Api Configuration Revision Example
  slug: msk-api-configuration-revision-example
- key_count: 0
  name: Msk Api Configuration State Example
  slug: msk-api-configuration-state-example
- key_count: 1
  name: Msk Api Connectivity Info Example
  slug: msk-api-connectivity-info-example
- key_count: 12
  name: Msk Api Create Cluster Request Example
  slug: msk-api-create-cluster-request-example
- key_count: 3
  name: Msk Api Create Cluster Response Example
  slug: msk-api-create-cluster-response-example
- key_count: 4
  name: Msk Api Create Cluster V2 Request Example
  slug: msk-api-create-cluster-v2-request-example
- key_count: 4
  name: Msk Api Create Cluster V2 Response Example
  slug: msk-api-create-cluster-v2-response-example
- key_count: 4
  name: Msk Api Create Configuration Request Example
  slug: msk-api-create-configuration-request-example
- key_count: 5
  name: Msk Api Create Configuration Response Example
  slug: msk-api-create-configuration-response-example
- key_count: 0
  name: Msk Api Delete Cluster Request Example
  slug: msk-api-delete-cluster-request-example
- key_count: 2
  name: Msk Api Delete Cluster Response Example
  slug: msk-api-delete-cluster-response-example
- key_count: 0
  name: Msk Api Delete Configuration Request Example
  slug: msk-api-delete-configuration-request-example
- key_count: 2
  name: Msk Api Delete Configuration Response Example
  slug: msk-api-delete-configuration-response-example
- key_count: 0
  name: Msk Api Describe Cluster Operation Request Example
  slug: msk-api-describe-cluster-operation-request-example
- key_count: 1
  name: Msk Api Describe Cluster Operation Response Example
  slug: msk-api-describe-cluster-operation-response-example
- key_count: 0
  name: Msk Api Describe Cluster Request Example
  slug: msk-api-describe-cluster-request-example
- key_count: 1
  name: Msk Api Describe Cluster Response Example
  slug: msk-api-describe-cluster-response-example
- key_count: 0
  name: Msk Api Describe Cluster V2 Request Example
  slug: msk-api-describe-cluster-v2-request-example
- key_count: 1
  name: Msk Api Describe Cluster V2 Response Example
  slug: msk-api-describe-cluster-v2-response-example
- key_count: 0
  name: Msk Api Describe Configuration Request Example
  slug: msk-api-describe-configuration-request-example
- key_count: 7
  name: Msk Api Describe Configuration Response Example
  slug: msk-api-describe-configuration-response-example
- key_count: 0
  name: Msk Api Describe Configuration Revision Request Example
  slug: msk-api-describe-configuration-revision-request-example
- key_count: 5
  name: Msk Api Describe Configuration Revision Response Example
  slug: msk-api-describe-configuration-revision-response-example
- key_count: 2
  name: Msk Api Ebs Storage Info Example
  slug: msk-api-ebs-storage-info-example
- key_count: 1
  name: Msk Api Encryption At Rest Example
  slug: msk-api-encryption-at-rest-example
- key_count: 2
  name: Msk Api Encryption In Transit Example
  slug: msk-api-encryption-in-transit-example
- key_count: 2
  name: Msk Api Encryption Info Example
  slug: msk-api-encryption-info-example
- key_count: 0
  name: Msk Api Enhanced Monitoring Example
  slug: msk-api-enhanced-monitoring-example
- key_count: 2
  name: Msk Api Error Info Example
  slug: msk-api-error-info-example
- key_count: 2
  name: Msk Api Firehose Example
  slug: msk-api-firehose-example
- key_count: 0
  name: Msk Api Get Bootstrap Brokers Request Example
  slug: msk-api-get-bootstrap-brokers-request-example
- key_count: 7
  name: Msk Api Get Bootstrap Brokers Response Example
  slug: msk-api-get-bootstrap-brokers-response-example
- key_count: 0
  name: Msk Api Get Compatible Kafka Versions Request Example
  slug: msk-api-get-compatible-kafka-versions-request-example
- key_count: 1
  name: Msk Api Get Compatible Kafka Versions Response Example
  slug: msk-api-get-compatible-kafka-versions-response-example
- key_count: 1
  name: Msk Api Iam Example
  slug: msk-api-iam-example
- key_count: 1
  name: Msk Api Jmx Exporter Example
  slug: msk-api-jmx-exporter-example
- key_count: 1
  name: Msk Api Jmx Exporter Info Example
  slug: msk-api-jmx-exporter-info-example
- key_count: 2
  name: Msk Api Kafka Version Example
  slug: msk-api-kafka-version-example
- key_count: 0
  name: Msk Api Kafka Version Status Example
  slug: msk-api-kafka-version-status-example
- key_count: 0
  name: Msk Api List Cluster Operations Request Example
  slug: msk-api-list-cluster-operations-request-example
- key_count: 2
  name: Msk Api List Cluster Operations Response Example
  slug: msk-api-list-cluster-operations-response-example
- key_count: 0
  name: Msk Api List Clusters Request Example
  slug: msk-api-list-clusters-request-example
- key_count: 2
  name: Msk Api List Clusters Response Example
  slug: msk-api-list-clusters-response-example
- key_count: 0
  name: Msk Api List Clusters V2 Request Example
  slug: msk-api-list-clusters-v2-request-example
- key_count: 2
  name: Msk Api List Clusters V2 Response Example
  slug: msk-api-list-clusters-v2-response-example
- key_count: 0
  name: Msk Api List Configuration Revisions Request Example
  slug: msk-api-list-configuration-revisions-request-example
- key_count: 2
  name: Msk Api List Configuration Revisions Response Example
  slug: msk-api-list-configuration-revisions-response-example
- key_count: 0
  name: Msk Api List Configurations Request Example
  slug: msk-api-list-configurations-request-example
- key_count: 2
  name: Msk Api List Configurations Response Example
  slug: msk-api-list-configurations-response-example
- key_count: 0
  name: Msk Api List Kafka Versions Request Example
  slug: msk-api-list-kafka-versions-request-example
- key_count: 2
  name: Msk Api List Kafka Versions Response Example
  slug: msk-api-list-kafka-versions-response-example
- key_count: 0
  name: Msk Api List Nodes Request Example
  slug: msk-api-list-nodes-request-example
- key_count: 2
  name: Msk Api List Nodes Response Example
  slug: msk-api-list-nodes-response-example
- key_count: 0
  name: Msk Api List Scram Secrets Request Example
  slug: msk-api-list-scram-secrets-request-example
- key_count: 2
  name: Msk Api List Scram Secrets Response Example
  slug: msk-api-list-scram-secrets-response-example
- key_count: 0
  name: Msk Api List Tags For Resource Request Example
  slug: msk-api-list-tags-for-resource-request-example
- key_count: 1
  name: Msk Api List Tags For Resource Response Example
  slug: msk-api-list-tags-for-resource-response-example
- key_count: 1
  name: Msk Api Logging Info Example
  slug: msk-api-logging-info-example
- key_count: 0
  name: Msk Api Max Results Example
  slug: msk-api-max-results-example
- key_count: 12
  name: Msk Api Mutable Cluster Info Example
  slug: msk-api-mutable-cluster-info-example
- key_count: 1
  name: Msk Api Node Exporter Example
  slug: msk-api-node-exporter-example
- key_count: 1
  name: Msk Api Node Exporter Info Example
  slug: msk-api-node-exporter-info-example
- key_count: 6
  name: Msk Api Node Info Example
  slug: msk-api-node-info-example
- key_count: 0
  name: Msk Api Node Type Example
  slug: msk-api-node-type-example
- key_count: 1
  name: Msk Api Open Monitoring Example
  slug: msk-api-open-monitoring-example
- key_count: 1
  name: Msk Api Open Monitoring Info Example
  slug: msk-api-open-monitoring-info-example
- key_count: 2
  name: Msk Api Prometheus Example
  slug: msk-api-prometheus-example
- key_count: 2
  name: Msk Api Prometheus Info Example
  slug: msk-api-prometheus-info-example
- key_count: 11
  name: Msk Api Provisioned Example
  slug: msk-api-provisioned-example
- key_count: 10
  name: Msk Api Provisioned Request Example
  slug: msk-api-provisioned-request-example
- key_count: 2
  name: Msk Api Provisioned Throughput Example
  slug: msk-api-provisioned-throughput-example
- key_count: 1
  name: Msk Api Public Access Example
  slug: msk-api-public-access-example
- key_count: 1
  name: Msk Api Reboot Broker Request Example
  slug: msk-api-reboot-broker-request-example
- key_count: 2
  name: Msk Api Reboot Broker Response Example
  slug: msk-api-reboot-broker-response-example
- key_count: 3
  name: Msk Api S3 Example
  slug: msk-api-s3-example
- key_count: 2
  name: Msk Api Sasl Example
  slug: msk-api-sasl-example
- key_count: 1
  name: Msk Api Scram Example
  slug: msk-api-scram-example
- key_count: 1
  name: Msk Api Serverless Client Authentication Example
  slug: msk-api-serverless-client-authentication-example
- key_count: 2
  name: Msk Api Serverless Example
  slug: msk-api-serverless-example
- key_count: 2
  name: Msk Api Serverless Request Example
  slug: msk-api-serverless-request-example
- key_count: 1
  name: Msk Api Serverless Sasl Example
  slug: msk-api-serverless-sasl-example
- key_count: 2
  name: Msk Api State Info Example
  slug: msk-api-state-info-example
- key_count: 1
  name: Msk Api Storage Info Example
  slug: msk-api-storage-info-example
- key_count: 0
  name: Msk Api Storage Mode Example
  slug: msk-api-storage-mode-example
- key_count: 1
  name: Msk Api Tag Resource Request Example
  slug: msk-api-tag-resource-request-example
- key_count: 2
  name: Msk Api Tls Example
  slug: msk-api-tls-example
- key_count: 1
  name: Msk Api Unauthenticated Example
  slug: msk-api-unauthenticated-example
- key_count: 0
  name: Msk Api Unauthorized Exception Example
  slug: msk-api-unauthorized-exception-example
- key_count: 3
  name: Msk Api Unprocessed Scram Secret Example
  slug: msk-api-unprocessed-scram-secret-example
- key_count: 0
  name: Msk Api Untag Resource Request Example
  slug: msk-api-untag-resource-request-example
- key_count: 2
  name: Msk Api Update Broker Count Request Example
  slug: msk-api-update-broker-count-request-example
- key_count: 2
  name: Msk Api Update Broker Count Response Example
  slug: msk-api-update-broker-count-response-example
- key_count: 2
  name: Msk Api Update Broker Storage Request Example
  slug: msk-api-update-broker-storage-request-example
- key_count: 2
  name: Msk Api Update Broker Storage Response Example
  slug: msk-api-update-broker-storage-response-example
- key_count: 2
  name: Msk Api Update Broker Type Request Example
  slug: msk-api-update-broker-type-request-example
- key_count: 2
  name: Msk Api Update Broker Type Response Example
  slug: msk-api-update-broker-type-response-example
- key_count: 2
  name: Msk Api Update Cluster Configuration Request Example
  slug: msk-api-update-cluster-configuration-request-example
- key_count: 2
  name: Msk Api Update Cluster Configuration Response Example
  slug: msk-api-update-cluster-configuration-response-example
- key_count: 3
  name: Msk Api Update Cluster Kafka Version Request Example
  slug: msk-api-update-cluster-kafka-version-request-example
- key_count: 2
  name: Msk Api Update Cluster Kafka Version Response Example
  slug: msk-api-update-cluster-kafka-version-response-example
- key_count: 2
  name: Msk Api Update Configuration Request Example
  slug: msk-api-update-configuration-request-example
- key_count: 2
  name: Msk Api Update Configuration Response Example
  slug: msk-api-update-configuration-response-example
- key_count: 2
  name: Msk Api Update Connectivity Request Example
  slug: msk-api-update-connectivity-request-example
- key_count: 2
  name: Msk Api Update Connectivity Response Example
  slug: msk-api-update-connectivity-response-example
- key_count: 4
  name: Msk Api Update Monitoring Request Example
  slug: msk-api-update-monitoring-request-example
- key_count: 2
  name: Msk Api Update Monitoring Response Example
  slug: msk-api-update-monitoring-response-example
- key_count: 3
  name: Msk Api Update Security Request Example
  slug: msk-api-update-security-request-example
- key_count: 2
  name: Msk Api Update Security Response Example
  slug: msk-api-update-security-response-example
- key_count: 4
  name: Msk Api Update Storage Request Example
  slug: msk-api-update-storage-request-example
- key_count: 2
  name: Msk Api Update Storage Response Example
  slug: msk-api-update-storage-response-example
- key_count: 2
  name: Msk Api Vpc Config Example
  slug: msk-api-vpc-config-example
- key_count: 5
  name: Msk Api Zookeeper Node Info Example
  slug: msk-api-zookeeper-node-info-example
features:
- description: Automatically provisions, configures, and maintains Apache Kafka clusters without operational overhead.
  name: Fully Managed Kafka
- description: Multi-AZ deployments with automatic replication and failover for data durability.
  name: High Durability
- description: Serverless cluster mode that automatically scales capacity to match streaming demand.
  name: MSK Serverless
- description: Fully managed Kafka Connect to stream data to and from databases and other services.
  name: MSK Connect
- description: Offload older data to low-cost Amazon S3 storage while keeping recent data on brokers.
  name: Tiered Storage
- description: Manage and enforce schemas for Kafka topics with AWS Glue Schema Registry integration.
  name: Schema Registry
finops:
- name: Amazon Msk Finops
  service_category: API
  slug: amazon-msk-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-msk.png
json_schemas:
- name: BatchAssociateScramSecretRequest
  property_count: 1
  slug: msk-api-batch-associate-scram-secret-request
- name: BatchAssociateScramSecretResponse
  property_count: 2
  slug: msk-api-batch-associate-scram-secret-response
- name: BatchDisassociateScramSecretRequest
  property_count: 1
  slug: msk-api-batch-disassociate-scram-secret-request
- name: BatchDisassociateScramSecretResponse
  property_count: 2
  slug: msk-api-batch-disassociate-scram-secret-response
- name: BrokerAZDistribution
  property_count: 0
  slug: msk-api-broker-az-distribution
- name: BrokerEBSVolumeInfo
  property_count: 3
  slug: msk-api-broker-ebs-volume-info
- name: BrokerLogs
  property_count: 3
  slug: msk-api-broker-logs
- name: BrokerNodeGroupInfo
  property_count: 6
  slug: msk-api-broker-node-group-info
- name: BrokerNodeInfo
  property_count: 6
  slug: msk-api-broker-node-info
- name: BrokerSoftwareInfo
  property_count: 3
  slug: msk-api-broker-software-info
- name: ClientAuthentication
  property_count: 3
  slug: msk-api-client-authentication
- name: ClientBroker
  property_count: 0
  slug: msk-api-client-broker
- name: CloudWatchLogs
  property_count: 2
  slug: msk-api-cloud-watch-logs
- name: ClusterInfo
  property_count: 19
  slug: msk-api-cluster-info
- name: ClusterOperationInfo
  property_count: 11
  slug: msk-api-cluster-operation-info
- name: ClusterOperationStepInfo
  property_count: 1
  slug: msk-api-cluster-operation-step-info
- name: ClusterOperationStep
  property_count: 2
  slug: msk-api-cluster-operation-step
- name: Cluster
  property_count: 11
  slug: msk-api-cluster
- name: ClusterState
  property_count: 0
  slug: msk-api-cluster-state
- name: ClusterType
  property_count: 0
  slug: msk-api-cluster-type
- name: CompatibleKafkaVersion
  property_count: 2
  slug: msk-api-compatible-kafka-version
- name: ConfigurationInfo
  property_count: 2
  slug: msk-api-configuration-info
- name: ConfigurationRevision
  property_count: 3
  slug: msk-api-configuration-revision
- name: Configuration
  property_count: 7
  slug: msk-api-configuration
- name: ConfigurationState
  property_count: 0
  slug: msk-api-configuration-state
- name: ConnectivityInfo
  property_count: 1
  slug: msk-api-connectivity-info
- name: CreateClusterRequest
  property_count: 12
  slug: msk-api-create-cluster-request
- name: CreateClusterResponse
  property_count: 3
  slug: msk-api-create-cluster-response
- name: CreateClusterV2Request
  property_count: 4
  slug: msk-api-create-cluster-v2-request
- name: CreateClusterV2Response
  property_count: 4
  slug: msk-api-create-cluster-v2-response
- name: CreateConfigurationRequest
  property_count: 4
  slug: msk-api-create-configuration-request
- name: CreateConfigurationResponse
  property_count: 5
  slug: msk-api-create-configuration-response
- name: DeleteClusterRequest
  property_count: 0
  slug: msk-api-delete-cluster-request
- name: DeleteClusterResponse
  property_count: 2
  slug: msk-api-delete-cluster-response
- name: DeleteConfigurationRequest
  property_count: 0
  slug: msk-api-delete-configuration-request
- name: DeleteConfigurationResponse
  property_count: 2
  slug: msk-api-delete-configuration-response
- name: DescribeClusterOperationRequest
  property_count: 0
  slug: msk-api-describe-cluster-operation-request
- name: DescribeClusterOperationResponse
  property_count: 1
  slug: msk-api-describe-cluster-operation-response
- name: DescribeClusterRequest
  property_count: 0
  slug: msk-api-describe-cluster-request
- name: DescribeClusterResponse
  property_count: 1
  slug: msk-api-describe-cluster-response
- name: DescribeClusterV2Request
  property_count: 0
  slug: msk-api-describe-cluster-v2-request
- name: DescribeClusterV2Response
  property_count: 1
  slug: msk-api-describe-cluster-v2-response
- name: DescribeConfigurationRequest
  property_count: 0
  slug: msk-api-describe-configuration-request
- name: DescribeConfigurationResponse
  property_count: 7
  slug: msk-api-describe-configuration-response
- name: DescribeConfigurationRevisionRequest
  property_count: 0
  slug: msk-api-describe-configuration-revision-request
- name: DescribeConfigurationRevisionResponse
  property_count: 5
  slug: msk-api-describe-configuration-revision-response
- name: EBSStorageInfo
  property_count: 2
  slug: msk-api-ebs-storage-info
- name: EncryptionAtRest
  property_count: 1
  slug: msk-api-encryption-at-rest
- name: EncryptionInTransit
  property_count: 2
  slug: msk-api-encryption-in-transit
- name: EncryptionInfo
  property_count: 2
  slug: msk-api-encryption-info
- name: EnhancedMonitoring
  property_count: 0
  slug: msk-api-enhanced-monitoring
- name: ErrorInfo
  property_count: 2
  slug: msk-api-error-info
- name: Firehose
  property_count: 2
  slug: msk-api-firehose
- name: GetBootstrapBrokersRequest
  property_count: 0
  slug: msk-api-get-bootstrap-brokers-request
- name: GetBootstrapBrokersResponse
  property_count: 7
  slug: msk-api-get-bootstrap-brokers-response
- name: GetCompatibleKafkaVersionsRequest
  property_count: 0
  slug: msk-api-get-compatible-kafka-versions-request
- name: GetCompatibleKafkaVersionsResponse
  property_count: 1
  slug: msk-api-get-compatible-kafka-versions-response
- name: Iam
  property_count: 1
  slug: msk-api-iam
- name: JmxExporterInfo
  property_count: 1
  slug: msk-api-jmx-exporter-info
- name: JmxExporter
  property_count: 1
  slug: msk-api-jmx-exporter
- name: KafkaVersion
  property_count: 2
  slug: msk-api-kafka-version
- name: KafkaVersionStatus
  property_count: 0
  slug: msk-api-kafka-version-status
- name: ListClusterOperationsRequest
  property_count: 0
  slug: msk-api-list-cluster-operations-request
- name: ListClusterOperationsResponse
  property_count: 2
  slug: msk-api-list-cluster-operations-response
- name: ListClustersRequest
  property_count: 0
  slug: msk-api-list-clusters-request
- name: ListClustersResponse
  property_count: 2
  slug: msk-api-list-clusters-response
- name: ListClustersV2Request
  property_count: 0
  slug: msk-api-list-clusters-v2-request
- name: ListClustersV2Response
  property_count: 2
  slug: msk-api-list-clusters-v2-response
- name: ListConfigurationRevisionsRequest
  property_count: 0
  slug: msk-api-list-configuration-revisions-request
- name: ListConfigurationRevisionsResponse
  property_count: 2
  slug: msk-api-list-configuration-revisions-response
- name: ListConfigurationsRequest
  property_count: 0
  slug: msk-api-list-configurations-request
- name: ListConfigurationsResponse
  property_count: 2
  slug: msk-api-list-configurations-response
- name: ListKafkaVersionsRequest
  property_count: 0
  slug: msk-api-list-kafka-versions-request
- name: ListKafkaVersionsResponse
  property_count: 2
  slug: msk-api-list-kafka-versions-response
- name: ListNodesRequest
  property_count: 0
  slug: msk-api-list-nodes-request
- name: ListNodesResponse
  property_count: 2
  slug: msk-api-list-nodes-response
- name: ListScramSecretsRequest
  property_count: 0
  slug: msk-api-list-scram-secrets-request
- name: ListScramSecretsResponse
  property_count: 2
  slug: msk-api-list-scram-secrets-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: msk-api-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: msk-api-list-tags-for-resource-response
- name: LoggingInfo
  property_count: 1
  slug: msk-api-logging-info
- name: MaxResults
  property_count: 0
  slug: msk-api-max-results
- name: MutableClusterInfo
  property_count: 12
  slug: msk-api-mutable-cluster-info
- name: NodeExporterInfo
  property_count: 1
  slug: msk-api-node-exporter-info
- name: NodeExporter
  property_count: 1
  slug: msk-api-node-exporter
- name: NodeInfo
  property_count: 6
  slug: msk-api-node-info
- name: NodeType
  property_count: 0
  slug: msk-api-node-type
- name: OpenMonitoringInfo
  property_count: 1
  slug: msk-api-open-monitoring-info
- name: OpenMonitoring
  property_count: 1
  slug: msk-api-open-monitoring
- name: PrometheusInfo
  property_count: 2
  slug: msk-api-prometheus-info
- name: Prometheus
  property_count: 2
  slug: msk-api-prometheus
- name: ProvisionedRequest
  property_count: 10
  slug: msk-api-provisioned-request
- name: Provisioned
  property_count: 11
  slug: msk-api-provisioned
- name: ProvisionedThroughput
  property_count: 2
  slug: msk-api-provisioned-throughput
- name: PublicAccess
  property_count: 1
  slug: msk-api-public-access
- name: RebootBrokerRequest
  property_count: 1
  slug: msk-api-reboot-broker-request
- name: RebootBrokerResponse
  property_count: 2
  slug: msk-api-reboot-broker-response
- name: S3
  property_count: 3
  slug: msk-api-s3
- name: Sasl
  property_count: 2
  slug: msk-api-sasl
- name: Scram
  property_count: 1
  slug: msk-api-scram
- name: ServerlessClientAuthentication
  property_count: 1
  slug: msk-api-serverless-client-authentication
- name: ServerlessRequest
  property_count: 2
  slug: msk-api-serverless-request
- name: ServerlessSasl
  property_count: 1
  slug: msk-api-serverless-sasl
- name: Serverless
  property_count: 2
  slug: msk-api-serverless
- name: StateInfo
  property_count: 2
  slug: msk-api-state-info
- name: StorageInfo
  property_count: 1
  slug: msk-api-storage-info
- name: StorageMode
  property_count: 0
  slug: msk-api-storage-mode
- name: TagResourceRequest
  property_count: 1
  slug: msk-api-tag-resource-request
- name: Tls
  property_count: 2
  slug: msk-api-tls
- name: Unauthenticated
  property_count: 1
  slug: msk-api-unauthenticated
- name: UnauthorizedException
  property_count: 0
  slug: msk-api-unauthorized-exception
- name: UnprocessedScramSecret
  property_count: 3
  slug: msk-api-unprocessed-scram-secret
- name: UntagResourceRequest
  property_count: 0
  slug: msk-api-untag-resource-request
- name: UpdateBrokerCountRequest
  property_count: 2
  slug: msk-api-update-broker-count-request
- name: UpdateBrokerCountResponse
  property_count: 2
  slug: msk-api-update-broker-count-response
- name: UpdateBrokerStorageRequest
  property_count: 2
  slug: msk-api-update-broker-storage-request
- name: UpdateBrokerStorageResponse
  property_count: 2
  slug: msk-api-update-broker-storage-response
- name: UpdateBrokerTypeRequest
  property_count: 2
  slug: msk-api-update-broker-type-request
- name: UpdateBrokerTypeResponse
  property_count: 2
  slug: msk-api-update-broker-type-response
- name: UpdateClusterConfigurationRequest
  property_count: 2
  slug: msk-api-update-cluster-configuration-request
- name: UpdateClusterConfigurationResponse
  property_count: 2
  slug: msk-api-update-cluster-configuration-response
- name: UpdateClusterKafkaVersionRequest
  property_count: 3
  slug: msk-api-update-cluster-kafka-version-request
- name: UpdateClusterKafkaVersionResponse
  property_count: 2
  slug: msk-api-update-cluster-kafka-version-response
- name: UpdateConfigurationRequest
  property_count: 2
  slug: msk-api-update-configuration-request
- name: UpdateConfigurationResponse
  property_count: 2
  slug: msk-api-update-configuration-response
- name: UpdateConnectivityRequest
  property_count: 2
  slug: msk-api-update-connectivity-request
- name: UpdateConnectivityResponse
  property_count: 2
  slug: msk-api-update-connectivity-response
- name: UpdateMonitoringRequest
  property_count: 4
  slug: msk-api-update-monitoring-request
- name: UpdateMonitoringResponse
  property_count: 2
  slug: msk-api-update-monitoring-response
- name: UpdateSecurityRequest
  property_count: 3
  slug: msk-api-update-security-request
- name: UpdateSecurityResponse
  property_count: 2
  slug: msk-api-update-security-response
- name: UpdateStorageRequest
  property_count: 4
  slug: msk-api-update-storage-request
- name: UpdateStorageResponse
  property_count: 2
  slug: msk-api-update-storage-response
- name: VpcConfig
  property_count: 2
  slug: msk-api-vpc-config
- name: ZookeeperNodeInfo
  property_count: 5
  slug: msk-api-zookeeper-node-info
json_structures:
- name: Msk Api Batch Associate Scram Secret Request Structure
  property_count: 1
  slug: msk-api-batch-associate-scram-secret-request-structure
- name: Msk Api Batch Associate Scram Secret Response Structure
  property_count: 2
  slug: msk-api-batch-associate-scram-secret-response-structure
- name: Msk Api Batch Disassociate Scram Secret Request Structure
  property_count: 1
  slug: msk-api-batch-disassociate-scram-secret-request-structure
- name: Msk Api Batch Disassociate Scram Secret Response Structure
  property_count: 2
  slug: msk-api-batch-disassociate-scram-secret-response-structure
- name: Msk Api Broker Az Distribution Structure
  property_count: 0
  slug: msk-api-broker-az-distribution-structure
- name: Msk Api Broker Ebs Volume Info Structure
  property_count: 3
  slug: msk-api-broker-ebs-volume-info-structure
- name: Msk Api Broker Logs Structure
  property_count: 3
  slug: msk-api-broker-logs-structure
- name: Msk Api Broker Node Group Info Structure
  property_count: 6
  slug: msk-api-broker-node-group-info-structure
- name: Msk Api Broker Node Info Structure
  property_count: 6
  slug: msk-api-broker-node-info-structure
- name: Msk Api Broker Software Info Structure
  property_count: 3
  slug: msk-api-broker-software-info-structure
- name: Msk Api Client Authentication Structure
  property_count: 3
  slug: msk-api-client-authentication-structure
- name: Msk Api Client Broker Structure
  property_count: 0
  slug: msk-api-client-broker-structure
- name: Msk Api Cloud Watch Logs Structure
  property_count: 2
  slug: msk-api-cloud-watch-logs-structure
- name: Msk Api Cluster Info Structure
  property_count: 19
  slug: msk-api-cluster-info-structure
- name: Msk Api Cluster Operation Info Structure
  property_count: 11
  slug: msk-api-cluster-operation-info-structure
- name: Msk Api Cluster Operation Step Info Structure
  property_count: 1
  slug: msk-api-cluster-operation-step-info-structure
- name: Msk Api Cluster Operation Step Structure
  property_count: 2
  slug: msk-api-cluster-operation-step-structure
- name: Msk Api Cluster State Structure
  property_count: 0
  slug: msk-api-cluster-state-structure
- name: Msk Api Cluster Structure
  property_count: 11
  slug: msk-api-cluster-structure
- name: Msk Api Cluster Type Structure
  property_count: 0
  slug: msk-api-cluster-type-structure
- name: Msk Api Compatible Kafka Version Structure
  property_count: 2
  slug: msk-api-compatible-kafka-version-structure
- name: Msk Api Configuration Info Structure
  property_count: 2
  slug: msk-api-configuration-info-structure
- name: Msk Api Configuration Revision Structure
  property_count: 3
  slug: msk-api-configuration-revision-structure
- name: Msk Api Configuration State Structure
  property_count: 0
  slug: msk-api-configuration-state-structure
- name: Msk Api Configuration Structure
  property_count: 7
  slug: msk-api-configuration-structure
- name: Msk Api Connectivity Info Structure
  property_count: 1
  slug: msk-api-connectivity-info-structure
- name: Msk Api Create Cluster Request Structure
  property_count: 12
  slug: msk-api-create-cluster-request-structure
- name: Msk Api Create Cluster Response Structure
  property_count: 3
  slug: msk-api-create-cluster-response-structure
- name: Msk Api Create Cluster V2 Request Structure
  property_count: 4
  slug: msk-api-create-cluster-v2-request-structure
- name: Msk Api Create Cluster V2 Response Structure
  property_count: 4
  slug: msk-api-create-cluster-v2-response-structure
- name: Msk Api Create Configuration Request Structure
  property_count: 4
  slug: msk-api-create-configuration-request-structure
- name: Msk Api Create Configuration Response Structure
  property_count: 5
  slug: msk-api-create-configuration-response-structure
- name: Msk Api Delete Cluster Request Structure
  property_count: 0
  slug: msk-api-delete-cluster-request-structure
- name: Msk Api Delete Cluster Response Structure
  property_count: 2
  slug: msk-api-delete-cluster-response-structure
- name: Msk Api Delete Configuration Request Structure
  property_count: 0
  slug: msk-api-delete-configuration-request-structure
- name: Msk Api Delete Configuration Response Structure
  property_count: 2
  slug: msk-api-delete-configuration-response-structure
- name: Msk Api Describe Cluster Operation Request Structure
  property_count: 0
  slug: msk-api-describe-cluster-operation-request-structure
- name: Msk Api Describe Cluster Operation Response Structure
  property_count: 1
  slug: msk-api-describe-cluster-operation-response-structure
- name: Msk Api Describe Cluster Request Structure
  property_count: 0
  slug: msk-api-describe-cluster-request-structure
- name: Msk Api Describe Cluster Response Structure
  property_count: 1
  slug: msk-api-describe-cluster-response-structure
- name: Msk Api Describe Cluster V2 Request Structure
  property_count: 0
  slug: msk-api-describe-cluster-v2-request-structure
- name: Msk Api Describe Cluster V2 Response Structure
  property_count: 1
  slug: msk-api-describe-cluster-v2-response-structure
- name: Msk Api Describe Configuration Request Structure
  property_count: 0
  slug: msk-api-describe-configuration-request-structure
- name: Msk Api Describe Configuration Response Structure
  property_count: 7
  slug: msk-api-describe-configuration-response-structure
- name: Msk Api Describe Configuration Revision Request Structure
  property_count: 0
  slug: msk-api-describe-configuration-revision-request-structure
- name: Msk Api Describe Configuration Revision Response Structure
  property_count: 5
  slug: msk-api-describe-configuration-revision-response-structure
- name: Msk Api Ebs Storage Info Structure
  property_count: 2
  slug: msk-api-ebs-storage-info-structure
- name: Msk Api Encryption At Rest Structure
  property_count: 1
  slug: msk-api-encryption-at-rest-structure
- name: Msk Api Encryption In Transit Structure
  property_count: 2
  slug: msk-api-encryption-in-transit-structure
- name: Msk Api Encryption Info Structure
  property_count: 2
  slug: msk-api-encryption-info-structure
- name: Msk Api Enhanced Monitoring Structure
  property_count: 0
  slug: msk-api-enhanced-monitoring-structure
- name: Msk Api Error Info Structure
  property_count: 2
  slug: msk-api-error-info-structure
- name: Msk Api Firehose Structure
  property_count: 2
  slug: msk-api-firehose-structure
- name: Msk Api Get Bootstrap Brokers Request Structure
  property_count: 0
  slug: msk-api-get-bootstrap-brokers-request-structure
- name: Msk Api Get Bootstrap Brokers Response Structure
  property_count: 7
  slug: msk-api-get-bootstrap-brokers-response-structure
- name: Msk Api Get Compatible Kafka Versions Request Structure
  property_count: 0
  slug: msk-api-get-compatible-kafka-versions-request-structure
- name: Msk Api Get Compatible Kafka Versions Response Structure
  property_count: 1
  slug: msk-api-get-compatible-kafka-versions-response-structure
- name: Msk Api Iam Structure
  property_count: 1
  slug: msk-api-iam-structure
- name: Msk Api Jmx Exporter Info Structure
  property_count: 1
  slug: msk-api-jmx-exporter-info-structure
- name: Msk Api Jmx Exporter Structure
  property_count: 1
  slug: msk-api-jmx-exporter-structure
- name: Msk Api Kafka Version Status Structure
  property_count: 0
  slug: msk-api-kafka-version-status-structure
- name: Msk Api Kafka Version Structure
  property_count: 2
  slug: msk-api-kafka-version-structure
- name: Msk Api List Cluster Operations Request Structure
  property_count: 0
  slug: msk-api-list-cluster-operations-request-structure
- name: Msk Api List Cluster Operations Response Structure
  property_count: 2
  slug: msk-api-list-cluster-operations-response-structure
- name: Msk Api List Clusters Request Structure
  property_count: 0
  slug: msk-api-list-clusters-request-structure
- name: Msk Api List Clusters Response Structure
  property_count: 2
  slug: msk-api-list-clusters-response-structure
- name: Msk Api List Clusters V2 Request Structure
  property_count: 0
  slug: msk-api-list-clusters-v2-request-structure
- name: Msk Api List Clusters V2 Response Structure
  property_count: 2
  slug: msk-api-list-clusters-v2-response-structure
- name: Msk Api List Configuration Revisions Request Structure
  property_count: 0
  slug: msk-api-list-configuration-revisions-request-structure
- name: Msk Api List Configuration Revisions Response Structure
  property_count: 2
  slug: msk-api-list-configuration-revisions-response-structure
- name: Msk Api List Configurations Request Structure
  property_count: 0
  slug: msk-api-list-configurations-request-structure
- name: Msk Api List Configurations Response Structure
  property_count: 2
  slug: msk-api-list-configurations-response-structure
- name: Msk Api List Kafka Versions Request Structure
  property_count: 0
  slug: msk-api-list-kafka-versions-request-structure
- name: Msk Api List Kafka Versions Response Structure
  property_count: 2
  slug: msk-api-list-kafka-versions-response-structure
- name: Msk Api List Nodes Request Structure
  property_count: 0
  slug: msk-api-list-nodes-request-structure
- name: Msk Api List Nodes Response Structure
  property_count: 2
  slug: msk-api-list-nodes-response-structure
- name: Msk Api List Scram Secrets Request Structure
  property_count: 0
  slug: msk-api-list-scram-secrets-request-structure
- name: Msk Api List Scram Secrets Response Structure
  property_count: 2
  slug: msk-api-list-scram-secrets-response-structure
- name: Msk Api List Tags For Resource Request Structure
  property_count: 0
  slug: msk-api-list-tags-for-resource-request-structure
- name: Msk Api List Tags For Resource Response Structure
  property_count: 1
  slug: msk-api-list-tags-for-resource-response-structure
- name: Msk Api Logging Info Structure
  property_count: 1
  slug: msk-api-logging-info-structure
- name: Msk Api Max Results Structure
  property_count: 0
  slug: msk-api-max-results-structure
- name: Msk Api Mutable Cluster Info Structure
  property_count: 12
  slug: msk-api-mutable-cluster-info-structure
- name: Msk Api Node Exporter Info Structure
  property_count: 1
  slug: msk-api-node-exporter-info-structure
- name: Msk Api Node Exporter Structure
  property_count: 1
  slug: msk-api-node-exporter-structure
- name: Msk Api Node Info Structure
  property_count: 6
  slug: msk-api-node-info-structure
- name: Msk Api Node Type Structure
  property_count: 0
  slug: msk-api-node-type-structure
- name: Msk Api Open Monitoring Info Structure
  property_count: 1
  slug: msk-api-open-monitoring-info-structure
- name: Msk Api Open Monitoring Structure
  property_count: 1
  slug: msk-api-open-monitoring-structure
- name: Msk Api Prometheus Info Structure
  property_count: 2
  slug: msk-api-prometheus-info-structure
- name: Msk Api Prometheus Structure
  property_count: 2
  slug: msk-api-prometheus-structure
- name: Msk Api Provisioned Request Structure
  property_count: 10
  slug: msk-api-provisioned-request-structure
- name: Msk Api Provisioned Structure
  property_count: 11
  slug: msk-api-provisioned-structure
- name: Msk Api Provisioned Throughput Structure
  property_count: 2
  slug: msk-api-provisioned-throughput-structure
- name: Msk Api Public Access Structure
  property_count: 1
  slug: msk-api-public-access-structure
- name: Msk Api Reboot Broker Request Structure
  property_count: 1
  slug: msk-api-reboot-broker-request-structure
- name: Msk Api Reboot Broker Response Structure
  property_count: 2
  slug: msk-api-reboot-broker-response-structure
- name: Msk Api S3 Structure
  property_count: 3
  slug: msk-api-s3-structure
- name: Msk Api Sasl Structure
  property_count: 2
  slug: msk-api-sasl-structure
- name: Msk Api Scram Structure
  property_count: 1
  slug: msk-api-scram-structure
- name: Msk Api Serverless Client Authentication Structure
  property_count: 1
  slug: msk-api-serverless-client-authentication-structure
- name: Msk Api Serverless Request Structure
  property_count: 2
  slug: msk-api-serverless-request-structure
- name: Msk Api Serverless Sasl Structure
  property_count: 1
  slug: msk-api-serverless-sasl-structure
- name: Msk Api Serverless Structure
  property_count: 2
  slug: msk-api-serverless-structure
- name: Msk Api State Info Structure
  property_count: 2
  slug: msk-api-state-info-structure
- name: Msk Api Storage Info Structure
  property_count: 1
  slug: msk-api-storage-info-structure
- name: Msk Api Storage Mode Structure
  property_count: 0
  slug: msk-api-storage-mode-structure
- name: Msk Api Tag Resource Request Structure
  property_count: 1
  slug: msk-api-tag-resource-request-structure
- name: Msk Api Tls Structure
  property_count: 2
  slug: msk-api-tls-structure
- name: Msk Api Unauthenticated Structure
  property_count: 1
  slug: msk-api-unauthenticated-structure
- name: Msk Api Unauthorized Exception Structure
  property_count: 0
  slug: msk-api-unauthorized-exception-structure
- name: Msk Api Unprocessed Scram Secret Structure
  property_count: 3
  slug: msk-api-unprocessed-scram-secret-structure
- name: Msk Api Untag Resource Request Structure
  property_count: 0
  slug: msk-api-untag-resource-request-structure
- name: Msk Api Update Broker Count Request Structure
  property_count: 2
  slug: msk-api-update-broker-count-request-structure
- name: Msk Api Update Broker Count Response Structure
  property_count: 2
  slug: msk-api-update-broker-count-response-structure
- name: Msk Api Update Broker Storage Request Structure
  property_count: 2
  slug: msk-api-update-broker-storage-request-structure
- name: Msk Api Update Broker Storage Response Structure
  property_count: 2
  slug: msk-api-update-broker-storage-response-structure
- name: Msk Api Update Broker Type Request Structure
  property_count: 2
  slug: msk-api-update-broker-type-request-structure
- name: Msk Api Update Broker Type Response Structure
  property_count: 2
  slug: msk-api-update-broker-type-response-structure
- name: Msk Api Update Cluster Configuration Request Structure
  property_count: 2
  slug: msk-api-update-cluster-configuration-request-structure
- name: Msk Api Update Cluster Configuration Response Structure
  property_count: 2
  slug: msk-api-update-cluster-configuration-response-structure
- name: Msk Api Update Cluster Kafka Version Request Structure
  property_count: 3
  slug: msk-api-update-cluster-kafka-version-request-structure
- name: Msk Api Update Cluster Kafka Version Response Structure
  property_count: 2
  slug: msk-api-update-cluster-kafka-version-response-structure
- name: Msk Api Update Configuration Request Structure
  property_count: 2
  slug: msk-api-update-configuration-request-structure
- name: Msk Api Update Configuration Response Structure
  property_count: 2
  slug: msk-api-update-configuration-response-structure
- name: Msk Api Update Connectivity Request Structure
  property_count: 2
  slug: msk-api-update-connectivity-request-structure
- name: Msk Api Update Connectivity Response Structure
  property_count: 2
  slug: msk-api-update-connectivity-response-structure
- name: Msk Api Update Monitoring Request Structure
  property_count: 4
  slug: msk-api-update-monitoring-request-structure
- name: Msk Api Update Monitoring Response Structure
  property_count: 2
  slug: msk-api-update-monitoring-response-structure
- name: Msk Api Update Security Request Structure
  property_count: 3
  slug: msk-api-update-security-request-structure
- name: Msk Api Update Security Response Structure
  property_count: 2
  slug: msk-api-update-security-response-structure
- name: Msk Api Update Storage Request Structure
  property_count: 4
  slug: msk-api-update-storage-request-structure
- name: Msk Api Update Storage Response Structure
  property_count: 2
  slug: msk-api-update-storage-response-structure
- name: Msk Api Vpc Config Structure
  property_count: 2
  slug: msk-api-vpc-config-structure
- name: Msk Api Zookeeper Node Info Structure
  property_count: 5
  slug: msk-api-zookeeper-node-info-structure
jsonld:
- class_count: 139
  name: Amazon Msk Msk Api Context
  property_count: 129
  slug: amazon-msk-msk-api-context
layout: provider
modified: '2026-08-06'
name: Amazon MSK
nav: Providers
network: true
overview: 'Amazon MSK publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Clusters API, Compatible Kafka Versions API, Configurations API, and 3 more. Tagged areas include Broadcasting, Media Processing, and Media.


  The Amazon MSK catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon MSK''s developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 14 more developer resources.'
plans:
- name: Amazon Msk Plans Pricing
  plan_count: 3
  slug: amazon-msk-plans-pricing
random_paper: 128
rate_limits:
- limit_count: 5
  name: Amazon Msk Rate Limits
  slug: amazon-msk-rate-limits
rules:
- name: Amazon MSK API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-msk-jsonschema-spectral-rules
- name: Amazon MSK API Rules
  rule_count: 26
  severity_counts:
    error: 9
    hint: 0
    info: 5
    warn: 12
  slug: amazon-msk-spectral-rules
score:
  band: strong
  composite: 58.6
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 72.4
    developer_ergonomics: 52.2
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 58.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-msk/refs/heads/main/screenshots/amazon-msk-2026-06-20T171749.png
security:
- kind: authentication
  name: Amazon Msk Authentication
  slug: amazon-msk-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Msk Domain Security
  slug: amazon-msk-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Msk Vulnerability Disclosure
  slug: amazon-msk-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Msk Trust Center
  slug: amazon-msk-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-msk
tags:
- Broadcasting
- Media Processing
- Media
use_cases:
- description: Build real-time data pipelines for clickstream analytics, log aggregation, and metrics.
  name: Real-Time Data Streaming
- description: Implement event sourcing patterns with durable, ordered Kafka topics.
  name: Event Sourcing
- description: Process streaming data with Apache Flink, Spark Streaming, or custom consumers.
  name: Stream Processing
- description: Stream database changes to downstream systems using Debezium and MSK Connect.
  name: Database Change Data Capture
website: https://aws.amazon.com/msk/
---

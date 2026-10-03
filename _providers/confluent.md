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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: true
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 49.4
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 265
  human_in_the_loop: 5
  name: Confluent Agentic Access
  operation_count: 528
  slug: confluent-agentic-access
  summary_line: 528 operations · 265 acting · 5 human-in-the-loop
api_count: 3
apis:
- description: Stream, connect, process, and govern your data with an all-in-one, real-time platform from the pioneer in data streaming. Build faster, scale smarter, and turn data chaos into instantly accessible and
  name: Confluent
  slug: confluent
- description: Confluent's managed remote Model Context Protocol servers. The global server at https://api.confluent.cloud/mcp/v1 provides tools for discovering environments and clusters, inspecting and debugging co
  name: Confluent Managed MCP Servers
  slug: confluent-mcp
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The API Keys API from Confluent — 1 operation(s) for api keys.
  name: Confluent API Keys API
  phrasing_intents:
  - id: listApiKeys
    intent: List API keys (subset spec)
    question: What API keys does my Confluent Cloud account have?
  - id: createApiKey
    intent: Create an API key (subset spec)
    question: How do I generate a new API key for Kafka REST access?
  phrasing_ops: 2
  slug: confluent-api-keys-api
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The Clusters API from Confluent — 2 operation(s) for clusters.
  name: Confluent Clusters API
  phrasing_intents:
  - id: listKafkaClusters
    intent: List Kafka clusters
    question: Which Kafka clusters can I reach through this REST endpoint?
  - id: getKafkaCluster
    intent: Get a Kafka cluster
    question: What are the details of one Kafka cluster?
  phrasing_ops: 2
  slug: confluent-clusters-api
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The Consumer Groups API from Confluent — 2 operation(s) for consumer groups.
  name: Confluent Consumer Groups API
  phrasing_intents:
  - id: listConsumerGroups
    intent: List consumer groups
    question: Which consumer groups are reading from my Kafka cluster?
  - id: getConsumerGroup
    intent: Get a consumer group
    question: What state and coordinator does a particular consumer group have?
  phrasing_ops: 2
  slug: confluent-consumer-groups-api
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The Environments API from Confluent — 1 operation(s) for environments.
  name: Confluent Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List Confluent Cloud environments
    question: Which environments exist in my Confluent Cloud organization?
  - id: createEnvironment
    intent: Create an environment
    question: How do I create a new environment to group my clusters?
  phrasing_ops: 2
  slug: confluent-environments-api
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The Partitions API from Confluent — 2 operation(s) for partitions.
  name: Confluent Partitions API
  phrasing_intents:
  - id: listPartitions
    intent: List partitions for a topic
    question: How many partitions does a topic have?
  - id: getPartition
    intent: Get a single partition
    question: What are the details of one specific partition of a topic?
  phrasing_ops: 2
  slug: confluent-partitions-api
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The Service Accounts API from Confluent — 1 operation(s) for service accounts.
  name: Confluent Service Accounts API
  phrasing_intents:
  - id: listServiceAccounts
    intent: List service accounts
    question: Which service accounts exist in my organization?
  - id: createServiceAccount
    intent: Create a service account
    question: How do I create a service account for an application?
  phrasing_ops: 2
  slug: confluent-service-accounts-api
- baseURL: https://api.confluent.cloud
  baseurl_source: spec
  description: The Topics API from Confluent — 2 operation(s) for topics.
  name: Confluent Topics API
  phrasing_intents:
  - id: listTopics
    intent: List topics in a cluster
    question: Which topics are in my Kafka cluster?
  - id: createTopic
    intent: Create a topic
    question: How do I create a topic with a chosen replication factor?
  - id: getTopic
    intent: Get topic metadata
    question: What metadata does a topic have, like partitions and replication?
  - id: deleteTopic
    intent: Delete a topic
    question: How do I delete a topic from my cluster?
  phrasing_ops: 4
  slug: confluent-topics-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AccessPoint objects represent network connections i'
  name: Confluent Access Points (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1AccessPoints
    intent: List access points in an environment
    question: Which network access points exist in an environment?
  - id: createNetworkingV1AccessPoint
    intent: Create an access point
    question: How do I create a new access point for private networking?
  - id: getNetworkingV1AccessPoint
    intent: Get an access point
    question: What is the status of one of my access points?
  - id: updateNetworkingV1AccessPoint
    intent: Update an access point
    question: Can I rename or change the spec of an existing access point?
  - id: deleteNetworkingV1AccessPoint
    intent: Delete an access point
    question: How do I tear down an access point I no longer need?
  phrasing_ops: 5
  slug: confluent-access-points-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent ACL (v3) API
  phrasing_intents:
  - id: batchCreateKafkaAcls
    intent: Create many Kafka ACLs in one request
    question: Can I create several ACLs in a single call instead of one at a time?
  - id: getKafkaAcls
    intent: List Kafka ACLs matching a filter
    question: Which ACLs grant access to a given topic?
  - id: createKafkaAcls
    intent: Create a single Kafka ACL
    question: How do I give a service account read access to one topic?
  - id: deleteKafkaAcls
    intent: Delete Kafka ACLs matching a filter
    question: How do I revoke ACLs that match certain criteria?
  phrasing_ops: 4
  slug: confluent-acl-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Agent` models an AI agent that uses a specified model, prompt, and set of tool'
  name: Confluent Agents (sql/v1) API
  phrasing_intents:
  - id: listSqlv1Agents
    intent: List Flink SQL agents in an environment
    question: Which AI agents are defined in my Flink SQL environment?
  - id: createSqlv1Agent
    intent: Create a Flink SQL agent
    question: How do I create an AI agent in a Confluent Flink SQL database?
  - id: getSqlv1Agent
    intent: Get a Flink SQL agent by name
    question: What model and prompt is a specific agent configured with?
  - id: updateSqlv1Agent
    intent: Alter a Flink SQL agent's prompt or model
    question: Can I change an agent's prompt, model or description after it is created?
  - id: deleteSqlv1Agent
    intent: Delete a Flink SQL agent
    question: How do I remove an agent I no longer need from a Flink database?
  phrasing_ops: 5
  slug: confluent-agents-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ApiKey` objects represent access to different part'
  name: Confluent API Keys (iam/v2) API
  phrasing_intents:
  - id: listIamV2ApiKeys
    intent: List API keys in the organization
    question: Which API keys exist in my Confluent Cloud organization?
  - id: createIamV2ApiKey
    intent: Create an API key
    question: How do I create an API key for a service account to use against a Kafka cluster?
  - id: getIamV2ApiKey
    intent: Get one API key
    question: Who owns a given API key and what resource is it for?
  - id: updateIamV2ApiKey
    intent: Update an API key's details
    question: Can I rename or change the description on an existing API key?
  - id: deleteIamV2ApiKey
    intent: Delete an API key
    question: How do I revoke an API key that may have leaked?
  phrasing_ops: 5
  slug: confluent-api-keys-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A `quota` object represents a quota configuration f'
  name: Confluent Applied Quotas (service-quota/v1) API
  phrasing_intents:
  - id: listServiceQuotaV1AppliedQuotas
    intent: List applied service quotas
    question: What service quotas apply to my organization or a cluster?
  - id: getServiceQuotaV1AppliedQuota
    intent: Read one applied quota
    question: What is the limit for a specific quota code?
  phrasing_ops: 2
  slug: confluent-applied-quotas-service-quota-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Catalog Integration represents configuration rela'
  name: Confluent Catalog Integrations (tableflow/v1) API
  phrasing_intents:
  - id: listTableflowV1CatalogIntegrations
    intent: List Tableflow catalog integrations
    question: Which catalog integrations are set up for Tableflow on my Kafka cluster?
  - id: createTableflowV1CatalogIntegration
    intent: Create a Tableflow catalog integration
    question: How do I connect Tableflow tables to an external catalog?
  - id: getTableflowV1CatalogIntegration
    intent: Read a Tableflow catalog integration
    question: What are the settings and status of a specific catalog integration?
  - id: updateTableflowV1CatalogIntegration
    intent: Update a Tableflow catalog integration
    question: Can I change the configuration of an existing catalog integration?
  - id: deleteTableflowV1CatalogIntegration
    intent: Delete a Tableflow catalog integration
    question: How do I remove a Tableflow catalog integration?
  phrasing_ops: 5
  slug: confluent-catalog-integrations-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `CertificateAuthority` objects represent signing ce'
  name: Confluent Certificate Authorities (iam/v2) API
  phrasing_intents:
  - id: listIamV2CertificateAuthorities
    intent: List certificate authorities
    question: Which certificate authorities are registered for mTLS in my organization?
  - id: createIamV2CertificateAuthority
    intent: Register a certificate authority
    question: How do I upload a CA certificate chain so clients can authenticate with mTLS?
  - id: getIamV2CertificateAuthority
    intent: Get a certificate authority
    question: What certificate chain and CRL settings does one of my CAs have?
  - id: updateIamV2CertificateAuthority
    intent: Update a certificate authority
    question: How do I rotate the certificate chain on an existing certificate authority?
  - id: deleteIamV2CertificateAuthority
    intent: Delete a certificate authority
    question: What removes a certificate authority from my organization?
  phrasing_ops: 5
  slug: confluent-certificate-authorities-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Identitypool` objects represent workload identitie'
  name: Confluent Certificate Identity Pools (iam/v2) API
  phrasing_intents:
  - id: listIamV2CertificateIdentityPools
    intent: List identity pools for a certificate authority
    question: Which certificate identity pools are attached to my certificate authority?
  - id: createIamV2CertificateIdentityPool
    intent: Create a certificate identity pool
    question: How do I map mTLS client certificates to an identity in Confluent Cloud?
  - id: getIamV2CertificateIdentityPool
    intent: Get a certificate identity pool
    question: What filter and external identifier does a certificate identity pool use?
  - id: updateIamV2CertificateIdentityPool
    intent: Update a certificate identity pool
    question: Can I change the certificate filter on an existing identity pool?
  - id: deleteIamV2CertificateIdentityPool
    intent: Delete a certificate identity pool
    question: How do I remove a certificate identity pool from a CA?
  phrasing_ops: 5
  slug: confluent-certificate-identity-pools-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ClientQuota` objects represent Client Quotas you c'
  name: Confluent Client Quotas (kafka-quotas/v1) API
  phrasing_intents:
  - id: listKafkaQuotasV1ClientQuotas
    intent: List client quotas on a cluster
    question: Which client throughput quotas are set on my Dedicated Kafka cluster?
  - id: createKafkaQuotasV1ClientQuota
    intent: Create a client quota
    question: How do I throttle a noisy client application with a new client quota?
  - id: getKafkaQuotasV1ClientQuota
    intent: Get one client quota
    question: What throughput limits does a particular client quota enforce?
  - id: updateKafkaQuotasV1ClientQuota
    intent: Update a client quota
    question: Can I raise or lower the throughput limit on an existing client quota?
  - id: deleteKafkaQuotasV1ClientQuota
    intent: Delete a client quota
    question: Can I remove a client quota so those clients are no longer throttled?
  phrasing_ops: 5
  slug: confluent-client-quotas-kafka-quotas-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Cluster Linking (v3) API
  phrasing_intents:
  - id: listKafkaLinks
    intent: List cluster links on a destination cluster
    question: Which cluster links exist on my destination Kafka cluster?
  - id: createKafkaLink
    intent: Create a cluster link between Kafka clusters
    question: How do I set up a cluster link to replicate data from a source Kafka cluster in Confluent?
  - id: getKafkaLink
    intent: Describe a cluster link
    question: What is the current state of a particular cluster link?
  - id: deleteKafkaLink
    intent: Delete a cluster link
    question: How do I remove a cluster link I no longer need?
  - id: listKafkaLinkConfigs
    intent: List all configs of a cluster link
    question: What configuration settings are applied to my cluster link?
  - id: getKafkaLinkConfigs
    intent: Get one config value on a cluster link
    question: What value is a single named config set to on my cluster link?
  - id: updateKafkaLinkConfig
    intent: Change one config on a cluster link
    question: How do I change a single setting on an existing cluster link?
  - id: deleteKafkaLinkConfig
    intent: Reset a cluster link config to its default
    question: How do I revert a cluster link setting back to its default value?
  phrasing_ops: 20
  slug: confluent-cluster-linking-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Cluster (v3) API
  phrasing_intents:
  - id: getKafkaCluster
    intent: Get a Kafka cluster
    question: What are the details of a Kafka cluster by ID?
  phrasing_ops: 1
  slug: confluent-cluster-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Apache Kafka Clusters '
  name: Confluent Clusters (cmk/v2) API
  phrasing_intents:
  - id: listCmkV2Clusters
    intent: List Kafka clusters
    question: Which Kafka clusters are running in my environment?
  - id: createCmkV2Cluster
    intent: Create a Kafka cluster
    question: How do I provision a new Kafka cluster in Confluent Cloud?
  - id: getCmkV2Cluster
    intent: Read a Kafka cluster
    question: What is the status and bootstrap endpoint of a specific Kafka cluster?
  - id: updateCmkV2Cluster
    intent: Update a Kafka cluster
    question: Can I rename or resize an existing Kafka cluster?
  - id: deleteCmkV2Cluster
    intent: Delete a Kafka cluster
    question: How do I tear down a Kafka cluster I no longer use?
  phrasing_ops: 5
  slug: confluent-clusters-cmk-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cluster` represents a ksqlDB runtime that you can '
  name: Confluent Clusters (ksqldbcm/v2) API
  phrasing_intents:
  - id: listKsqldbcmV2Clusters
    intent: List ksqlDB clusters
    question: Which ksqlDB clusters are running in my environment?
  - id: createKsqldbcmV2Cluster
    intent: Create a ksqlDB cluster
    question: How do I spin up a new ksqlDB cluster attached to a Kafka cluster?
  - id: getKsqldbcmV2Cluster
    intent: Get one ksqlDB cluster
    question: Is a specific ksqlDB cluster provisioned, and what is its endpoint?
  - id: deleteKsqldbcmV2Cluster
    intent: Delete a ksqlDB cluster
    question: What is the way to decommission a ksqlDB cluster I no longer need?
  phrasing_ops: 4
  slug: confluent-clusters-ksqldbcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Clusters on Confluent Cloud.'
  name: Confluent Clusters (srcm/v2) API
  phrasing_intents:
  - id: listSrcmV2Clusters
    intent: List Schema Registry clusters (deprecated v2)
    question: Which Schema Registry clusters does an environment have, using the older v2 API?
  - id: createSrcmV2Cluster
    intent: Create a Schema Registry cluster (deprecated)
    question: Can I still enable a Schema Registry cluster through the deprecated v2 API?
  - id: getSrcmV2Cluster
    intent: Get a Schema Registry cluster (deprecated v2)
    question: How do I read one Schema Registry cluster using the older v2 endpoint?
  - id: updateSrcmV2Cluster
    intent: Update a Schema Registry cluster (deprecated)
    question: Can I change a Schema Registry cluster's package through the v2 API?
  - id: deleteSrcmV2Cluster
    intent: Delete a Schema Registry cluster (deprecated)
    question: Can I remove a Schema Registry cluster through the v2 API?
  phrasing_ops: 5
  slug: confluent-clusters-srcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Cluste'
  name: Confluent Clusters (srcm/v3) API
  phrasing_intents:
  - id: listSrcmV3Clusters
    intent: List Schema Registry clusters
    question: Which Schema Registry cluster does my environment have?
  - id: getSrcmV3Cluster
    intent: Get a Schema Registry cluster
    question: What is the endpoint URL of my Schema Registry cluster?
  phrasing_ops: 2
  slug: confluent-clusters-srcm-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to test schema compatibility. Rela'
  name: Confluent Compatibility (v1) API
  phrasing_intents:
  - id: testCompatibilityBySubjectName
    intent: Test a schema against one subject version
    question: Is my new schema compatible with one specific version of a subject?
  - id: testCompatibilityForSubject
    intent: Test a schema against all versions of a subject
    question: Would this schema pass the same compatibility check as registering it under the subject?
  phrasing_ops: 2
  slug: confluent-compatibility-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Compute Pool represents a set of compute resource'
  name: Confluent Compute Pools (fcpm/v2) API
  phrasing_intents:
  - id: listFcpmV2ComputePools
    intent: List Flink compute pools in an environment
    question: Which Flink compute pools exist in my environment?
  - id: createFcpmV2ComputePool
    intent: Create a Flink compute pool
    question: How do I provision a compute pool to run Flink SQL statements in Confluent Cloud?
  - id: getFcpmV2ComputePool
    intent: Get a Flink compute pool
    question: What is the status and size of a specific compute pool?
  - id: updateFcpmV2ComputePool
    intent: Update a Flink compute pool
    question: Can I resize a compute pool or rename it after creation?
  - id: deleteFcpmV2ComputePool
    intent: Delete a Flink compute pool
    question: How do I tear down a compute pool I'm not using anymore?
  phrasing_ops: 5
  slug: confluent-compute-pools-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to manage and query schema compati'
  name: Confluent Config (v1) API
  phrasing_intents:
  - id: getClusterConfig
    intent: Get Schema Registry cluster config
    question: What cluster-wide configuration is my Schema Registry running with?
  - id: getSubjectLevelConfig
    intent: Get a subject's compatibility settings
    question: What compatibility level is set on a particular subject?
  - id: updateSubjectLevelConfig
    intent: Set a subject's compatibility level
    question: How do I change the compatibility level of just one subject?
  - id: deleteSubjectConfig
    intent: Revert a subject to the global compatibility
    question: How do I drop a subject's own compatibility setting so it follows the global default?
  - id: getTopLevelConfig
    intent: Get the global compatibility level
    question: What is the global compatibility level for my Schema Registry?
  - id: updateTopLevelConfig
    intent: Set the global compatibility level
    question: How can I change the default compatibility level for every subject?
  - id: deleteTopLevelConfig
    intent: Reset the global compatibility level
    question: Can I remove my custom global compatibility level and go back to the default?
  phrasing_ops: 7
  slug: confluent-config-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Configs (v3) API
  phrasing_intents:
  - id: listKafkaClusterConfigs
    intent: List a cluster's dynamic broker configs
    question: Which broker settings have been overridden dynamically across my whole Kafka cluster?
  - id: updateKafkaClusterConfigs
    intent: Batch alter dynamic broker configs
    question: Can I change several cluster-wide broker settings in one request?
  - id: getKafkaClusterConfig
    intent: Get one dynamic broker config
    question: What is the current cluster-wide value of a single broker setting?
  - id: updateKafkaClusterConfig
    intent: Update one dynamic broker config
    question: Can I set a single cluster-wide broker setting without sending a whole batch?
  - id: deleteKafkaClusterConfig
    intent: Reset a broker config to its default
    question: How do I undo a dynamic broker override and go back to the default?
  - id: listKafkaTopicConfigs
    intent: List a topic's configs
    question: What configuration settings does one particular topic have?
  - id: updateKafkaTopicConfigBatch
    intent: Batch alter a topic's configs
    question: Can I update or delete several settings on one topic at once?
  - id: getKafkaTopicConfig
    intent: Get one topic config value
    question: What is a topic's current value for one specific setting like retention.ms?
  phrasing_ops: 17
  slug: confluent-configs-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connect Artifact` objects represent collection of '
  name: Confluent Connect Artifacts (cam/v1) API
  phrasing_intents:
  - id: listCamV1ConnectArtifacts
    intent: List Connect artifacts
    question: Which Connect artifacts are uploaded for a cloud in my environment?
  - id: createCamV1ConnectArtifact
    intent: Create a Connect artifact
    question: How do I register a new Connect artifact?
  - id: getCamV1ConnectArtifact
    intent: Read a Connect artifact
    question: What is the status of a Connect artifact I uploaded?
  - id: deleteCamV1ConnectArtifact
    intent: Delete a Connect artifact
    question: Why can't I delete a Connect artifact that workloads still use?
  phrasing_ops: 4
  slug: confluent-connect-artifacts-cam-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `ConnectCluster` object represent Confluent Platform Connect clusters registere'
  name: Confluent Connect Clusters (usm/v1) API
  phrasing_intents:
  - id: listUsmV1ConnectClusters
    intent: List registered Connect clusters
    question: Which Confluent Platform Connect clusters are registered for unified stream manager?
  - id: createUsmV1ConnectCluster
    intent: Register a Connect cluster
    question: How do I register a self-managed Connect cluster with Confluent Cloud?
  - id: getUsmV1ConnectCluster
    intent: Get a registered Connect cluster
    question: What are the details of one registered Connect cluster?
  - id: deleteUsmV1ConnectCluster
    intent: Unregister a Connect cluster
    question: How do I unregister a Connect cluster?
  phrasing_ops: 4
  slug: confluent-connect-clusters-usm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connection` represents a core resource used to mod'
  name: Confluent Connections (sql/v1) API
  phrasing_intents:
  - id: listSqlv1Connections
    intent: List Flink SQL connections
    question: Which Flink SQL connections are defined in my environment?
  - id: createSqlv1Connection
    intent: Create a Flink SQL connection
    question: How do I create a connection so Flink SQL can reach an external endpoint?
  - id: getSqlv1Connection
    intent: Get one Flink SQL connection
    question: What endpoint and type does a specific Flink connection use?
  - id: deleteSqlv1Connection
    intent: Delete a Flink SQL connection
    question: How do I delete a Flink SQL connection I no longer use?
  - id: updateSqlv1Connection
    intent: Update a Flink SQL connection
    question: Can I rotate the secret on an existing Flink SQL connection?
  phrasing_ops: 5
  slug: confluent-connections-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed Connectors or Custom Connectors in '
  name: Confluent Connectors (connect/v1) API
  phrasing_intents:
  - id: listConnectv1Connectors
    intent: List connector names on a cluster
    question: Which managed connectors are active on my Kafka cluster?
  - id: createConnectv1Connector
    intent: Create a managed connector
    question: How do I create a new fully managed connector on Confluent Cloud?
  - id: listConnectv1ConnectorsWithExpansions
    intent: List connectors with status and details
    question: Can I list connectors together with their status, info and IDs in one call?
  - id: getConnectv1ConnectorConfig
    intent: Read a connector's configuration
    question: What configuration is a connector currently running with?
  - id: createOrUpdateConnectv1ConnectorConfig
    intent: Create or update a connector's configuration
    question: Can I change the settings of an existing connector without deleting it?
  - id: readConnectv1Connector
    intent: Get information about one connector
    question: What type and tasks does a specific connector have?
  - id: deleteConnectv1Connector
    intent: Delete a connector
    question: How do I delete a connector and stop all its tasks?
  phrasing_ops: 7
  slug: confluent-connectors-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Consumer Group (v3) API
  phrasing_intents:
  - id: listKafkaConsumerGroups
    intent: List consumer groups in a cluster
    question: Which consumer groups are reading from my Kafka cluster?
  - id: getKafkaConsumerGroup
    intent: Get a consumer group
    question: What state is a particular consumer group in?
  - id: listKafkaConsumers
    intent: List consumers in a group
    question: Which consumer instances are members of a consumer group?
  - id: getKafkaConsumerGroupLagSummary
    intent: Get a consumer group's lag summary
    question: What is the maximum and total lag for a consumer group?
  - id: listKafkaConsumerLags
    intent: List per-partition lags for a group
    question: Which partitions are my group's consumers falling behind on?
  - id: getKafkaConsumerLag
    intent: Get consumer lag on one partition
    question: How far behind is my consumer group on one specific topic partition?
  - id: getKafkaConsumer
    intent: Get one consumer in a group
    question: What client and assignments does a specific consumer in a group have?
  phrasing_ops: 7
  slug: confluent-consumer-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerSharedResource` object contains details of'
  name: Confluent Consumer Shared Resources (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ConsumerSharedResources
    intent: List resources shared with me
    question: Which topics have other organizations shared with me through Stream Sharing?
  - id: getCdxV1ConsumerSharedResource
    intent: Get a resource shared with me
    question: What details are available for a resource someone shared with me?
  - id: imageCdxV1ConsumerSharedResource
    intent: Get the image of a resource shared with me
    question: How do I fetch the logo of a resource another organization shared with me?
  - id: networkCdxV1ConsumerSharedResource
    intent: Get network config of a shared resource
    question: What networking do I need to reach a topic shared with me privately?
  phrasing_ops: 4
  slug: confluent-consumer-shared-resources-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerShare` object respresents the share that y'
  name: Confluent Consumer Shares (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ConsumerShares
    intent: List shares I've received
    question: Which stream shares have I accepted as a consumer?
  - id: getCdxV1ConsumerShare
    intent: Get a consumer share
    question: What is the status of a share I received?
  - id: deleteCdxV1ConsumerShare
    intent: Delete a consumer share
    question: How do I stop consuming a stream share I accepted?
  phrasing_ops: 3
  slug: confluent-consumer-shares-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to retrieve information about sche'
  name: Confluent Contexts (v1) API
  phrasing_intents:
  - id: listContexts
    intent: List Schema Registry contexts
    question: Which schema contexts exist in my Schema Registry?
  phrasing_ops: 1
  slug: confluent-contexts-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cost` objects represent the aggregated billing cos'
  name: Confluent Costs (billing/v1) API
  phrasing_intents:
  - id: listBillingV1Costs
    intent: List costs for a date range
    question: How much did I spend on Confluent Cloud last month?
  phrasing_ops: 1
  slug: confluent-costs-billing-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Custom Code Logging API EA](https://img.shield'
  name: Confluent Custom Code Loggings (ccl/v1) API
  phrasing_intents:
  - id: listCclV1CustomCodeLoggings
    intent: List custom code logging configs
    question: Where are my custom code logs being sent in this environment?
  - id: createCclV1CustomCodeLogging
    intent: Create a custom code logging config
    question: How do I send logs from custom code to a destination in my cloud?
  - id: getCclV1CustomCodeLogging
    intent: Read a custom code logging config
    question: What destination is a particular custom code logging config using?
  - id: updateCclV1CustomCodeLogging
    intent: Update a custom code logging config
    question: Can I change where an existing custom code logging config sends its logs?
  - id: deleteCclV1CustomCodeLogging
    intent: Delete a custom code logging config
    question: How do I stop sending custom code logs to a destination?
  phrasing_ops: 5
  slug: confluent-custom-code-loggings-ccl-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPluginVersion objects represent Custom'
  name: Confluent Custom Connect Plugin Versions (ccpm/v1) API
  phrasing_intents:
  - id: listCcpmV1CustomConnectPluginVersions
    intent: List versions of a custom connect plugin
    question: Which versions of my custom connector plugin have been uploaded?
  - id: createCcpmV1CustomConnectPluginVersion
    intent: Add a version to a custom connect plugin
    question: How do I publish a new version of my custom connector plugin?
  - id: getCcpmV1CustomConnectPluginVersion
    intent: Get one custom plugin version
    question: What connector classes and status does a specific plugin version have?
  - id: deleteCcpmV1CustomConnectPluginVersion
    intent: Delete a custom plugin version
    question: How do I delete an old version of my custom connector plugin?
  phrasing_ops: 4
  slug: confluent-custom-connect-plugin-versions-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPlugins objects represent Custom Conne'
  name: Confluent Custom Connect Plugins (ccpm/v1) API
  phrasing_intents:
  - id: listCcpmV1CustomConnectPlugins
    intent: List custom Connect plugins
    question: Which custom connector plugins have I uploaded to an environment?
  - id: createCcpmV1CustomConnectPlugin
    intent: Create a custom Connect plugin
    question: How do I register my own connector plugin in Confluent Cloud?
  - id: getCcpmV1CustomConnectPlugin
    intent: Get a custom Connect plugin
    question: What versions and cloud does one of my custom plugins have?
  - id: updateCcpmV1CustomConnectPlugin
    intent: Update a custom Connect plugin
    question: Can I rename or change the description of a custom Connect plugin?
  - id: deleteCcpmV1CustomConnectPlugin
    intent: Delete a custom Connect plugin
    question: How do I remove a custom connector plugin I uploaded?
  phrasing_ops: 5
  slug: confluent-custom-connect-plugins-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectorPlugins objects represent Custom Con'
  name: Confluent Custom Connector Plugins (connect/v1) API
  phrasing_intents:
  - id: listConnectV1CustomConnectorPlugins
    intent: List custom connector plugins
    question: Which custom connector plugins have I uploaded?
  - id: createConnectV1CustomConnectorPlugin
    intent: Create a custom connector plugin
    question: How do I upload my own Kafka Connect plugin to Confluent Cloud?
  - id: getConnectV1CustomConnectorPlugin
    intent: Get a custom connector plugin
    question: What connector class and type does one of my custom plugins use?
  - id: updateConnectV1CustomConnectorPlugin
    intent: Update a custom connector plugin
    question: Can I change the documentation link or description of a custom plugin?
  - id: deleteConnectV1CustomConnectorPlugin
    intent: Delete a custom connector plugin
    question: How do I remove a custom connector plugin I uploaded?
  phrasing_ops: 5
  slug: confluent-custom-connector-plugins-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of supported runtime languages for Custom Conn'
  name: Confluent Custom Connector Runtimes (connect/v1) API
  phrasing_intents:
  - id: listConnectV1CustomConnectorRuntimes
    intent: List custom connector runtimes
    question: Which runtimes are available for running custom connectors?
  phrasing_ops: 1
  slug: confluent-custom-connector-runtimes-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Data Encryption Keys (v1) API
  phrasing_intents:
  - id: getDekSubjects
    intent: List DEK subjects under a KEK
    question: Which subjects have data encryption keys under a given key encryption key?
  - id: createDek
    intent: Create a data encryption key
    question: How do I register a new data encryption key for a subject in Schema Registry?
  - id: deleteDekVersions
    intent: Delete all versions of a DEK
    question: How do I delete every version of a subject's data encryption key?
  - id: getDek
    intent: Get the latest DEK for a subject
    question: What data encryption key is currently used for a subject?
  - id: deleteDekVersion
    intent: Delete one DEK version
    question: How do I delete just one version of a DEK and keep the rest?
  - id: getDekByVersion
    intent: Get a specific DEK version
    question: Can I retrieve an older version of a subject's DEK?
  - id: getDekVersions
    intent: List versions of a DEK
    question: What versions exist for a subject's data encryption key?
  - id: undeleteDekVersion
    intent: Restore a soft-deleted DEK version
    question: Can I recover a DEK version I soft-deleted by mistake?
  phrasing_ops: 9
  slug: confluent-data-encryption-keys-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add, remove, and update DNS forwarder for your gate'
  name: Confluent DNS Forwarders (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1DnsForwarders
    intent: List DNS forwarders
    question: Which DNS forwarders are set up in my Confluent environment?
  - id: createNetworkingV1DnsForwarder
    intent: Create a DNS forwarder
    question: How do I forward DNS queries for my private domains from Confluent Cloud to my own resolvers?
  - id: getNetworkingV1DnsForwarder
    intent: Get one DNS forwarder
    question: What domains and DNS server IPs does a specific forwarder use?
  - id: updateNetworkingV1DnsForwarder
    intent: Update a DNS forwarder
    question: Can I rename a DNS forwarder or change its forwarded domains?
  - id: deleteNetworkingV1DnsForwarder
    intent: Delete a DNS forwarder
    question: How do I remove a DNS forwarder from my environment?
  phrasing_ops: 5
  slug: confluent-dns-forwarders-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) DNS record objects are associated with Confluent Cl'
  name: Confluent DNS Records (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1DnsRecords
    intent: List DNS records
    question: Which private DNS records exist in my environment?
  - id: createNetworkingV1DnsRecord
    intent: Create a DNS record
    question: How do I add a DNS record for a private endpoint in Confluent Cloud?
  - id: getNetworkingV1DnsRecord
    intent: Read a DNS record
    question: What domain and status does a specific DNS record have?
  - id: updateNetworkingV1DnsRecord
    intent: Update a DNS record
    question: Can I change the name or target of an existing DNS record?
  - id: deleteNetworkingV1DnsRecord
    intent: Delete a DNS record
    question: How do I remove a DNS record I created?
  phrasing_ops: 5
  slug: confluent-dns-records-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An Endpoint object represents a Fully Qualified Dom'
  name: Confluent Endpoints (endpoint/v1) API
  phrasing_intents:
  - id: listEndpointV1Endpoints
    intent: List service endpoints
    question: What endpoints can I use to reach a service in my environment?
  phrasing_ops: 1
  slug: confluent-endpoints-endpoint-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent Entitlements (partner/v2) API
  phrasing_intents:
  - id: listPartnerV2Entitlements
    intent: List partner entitlements
    question: Which entitlements have I created as a Confluent partner?
  - id: createPartnerV2Entitlement
    intent: Create a partner entitlement
    question: How do I entitle a customer to a Confluent plan through the partner program?
  - id: getPartnerV2Entitlement
    intent: Get one partner entitlement
    question: What plan and organization does a specific entitlement belong to?
  phrasing_ops: 3
  slug: confluent-entitlements-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Entity (v1) API
  phrasing_intents:
  - id: createBusinessMetadata
    intent: Bulk attach business metadata to entities
    question: How do I attach business metadata to several topics or schemas at once?
  - id: updateBusinessMetadata
    intent: Bulk update business metadata on entities
    question: Can I change business metadata values on many catalog entities in one call?
  - id: getBusinessMetadata
    intent: Read business metadata on an entity
    question: What business metadata is attached to a particular topic in the catalog?
  - id: deleteBusinessMetadata
    intent: Remove business metadata from an entity
    question: Can I detach a single business metadata from one catalog entity?
  - id: updateTags
    intent: Bulk update tags on entities
    question: Can I update tags that are already applied to many entities in one go?
  - id: createTags
    intent: Bulk tag entities
    question: How do I tag many topics or schemas with a classification at once?
  - id: getByUniqueAttributes
    intent: Read a catalog entity
    question: What is the full catalog definition of a topic or schema entity?
  - id: getTags
    intent: List tags on an entity
    question: Which tags are applied to a specific topic in the catalog?
  phrasing_ops: 10
  slug: confluent-entity-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Environment` objects represent an isolated namespa'
  name: Confluent Environments (org/v2) API
  phrasing_intents:
  - id: listOrgV2Environments
    intent: List environments
    question: What environments exist in my Confluent Cloud organization?
  - id: createOrgV2Environment
    intent: Create an environment
    question: How do I create a new environment for my Kafka clusters?
  - id: getOrgV2Environment
    intent: Get an environment
    question: What Stream Governance package is an environment on?
  - id: updateOrgV2Environment
    intent: Update an environment
    question: Can I rename an existing environment?
  - id: deleteOrgV2Environment
    intent: Delete an environment and its resources
    question: Does deleting an environment also delete the clusters inside it?
  phrasing_ops: 5
  slug: confluent-environments-org-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Exporters (v1) API
  phrasing_intents:
  - id: listExporters
    intent: List schema exporters
    question: Which schema exporters have been set up in my Schema Registry?
  - id: registerExporter
    intent: Create a schema exporter
    question: How do I set up a new schema exporter to copy schemas to another cluster?
  - id: getExporterInfoByName
    intent: Get a schema exporter's details
    question: What subjects and context does a given schema exporter cover?
  - id: updateExporterInfo
    intent: Update a schema exporter's settings
    question: Can I change which subjects an existing schema exporter copies?
  - id: deleteExporter
    intent: Delete a schema exporter
    question: How do I remove a schema exporter I no longer need?
  - id: getExporterStatusByName
    intent: Check a schema exporter's status
    question: Is my schema exporter currently running, paused or in an error state?
  - id: getExporterConfigByName
    intent: Get a schema exporter's config
    question: What destination Schema Registry URL is a given exporter configured with?
  - id: updateExporterConfigByName
    intent: Update a schema exporter's config
    question: Can I point an existing exporter at a different destination Schema Registry URL?
  phrasing_ops: 11
  slug: confluent-exporters-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) FlinkArtifact objects represent Flink Artifacts on '
  name: Confluent Flink Artifacts (artifact/v1) API
  phrasing_intents:
  - id: listArtifactV1FlinkArtifacts
    intent: List Flink artifacts in a region
    question: Which Flink UDF artifacts have been uploaded to my environment?
  - id: createArtifactV1FlinkArtifact
    intent: Create a Flink artifact
    question: How do I register a Flink user-defined function JAR as an artifact?
  - id: getArtifactV1FlinkArtifact
    intent: Get a Flink artifact
    question: What versions and class name does a Flink artifact have?
  - id: updateArtifactV1FlinkArtifact
    intent: Update a Flink artifact
    question: Can I change the description or documentation link of a Flink artifact?
  - id: deleteArtifactV1FlinkArtifact
    intent: Delete a Flink artifact
    question: How do I remove a Flink artifact I no longer need?
  phrasing_ops: 5
  slug: confluent-flink-artifacts-artifact-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Gateway represents a slice of traffic capacity in'
  name: Confluent Gateways (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1Gateways
    intent: List network gateways
    question: Which network gateways exist in my Confluent environment?
  - id: createNetworkingV1Gateway
    intent: Create a network gateway
    question: How do I create a gateway for private networking to Confluent Cloud?
  - id: getNetworkingV1Gateway
    intent: Get one network gateway
    question: Is a specific gateway ready, and what endpoints does it expose?
  - id: updateNetworkingV1Gateway
    intent: Update a network gateway
    question: Can I rename an existing gateway?
  - id: deleteNetworkingV1Gateway
    intent: Delete a network gateway
    question: How do I delete a gateway I no longer need?
  phrasing_ops: 5
  slug: confluent-gateways-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `GroupMapping` objects establish relationships betw'
  name: Confluent Group Mappings (iam/v2/sso) API
  phrasing_intents:
  - id: listIamV2SsoGroupMappings
    intent: List SSO group mappings
    question: Which SSO group mappings are configured for my organization?
  - id: createIamV2SsoGroupMapping
    intent: Create an SSO group mapping
    question: How do I map an identity provider group to Confluent Cloud permissions?
  - id: getIamV2SsoGroupMapping
    intent: Read an SSO group mapping
    question: What filter and principal does a given group mapping use?
  - id: updateIamV2SsoGroupMapping
    intent: Update an SSO group mapping
    question: Can I change the group filter of an existing mapping?
  - id: deleteIamV2SsoGroupMapping
    intent: Delete an SSO group mapping
    question: How do I remove an SSO group mapping?
  phrasing_ops: 5
  slug: confluent-group-mappings-iam-v2-sso-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityPool` objects represent groups of identiti'
  name: Confluent Identity Pools (iam/v2) API
  phrasing_intents:
  - id: listIamV2IdentityPools
    intent: List identity pools for an identity provider
    question: Which identity pools are set up under one of my OAuth identity providers?
  - id: createIamV2IdentityPool
    intent: Create an identity pool
    question: How do I map OAuth tokens from my identity provider to a Confluent principal?
  - id: getIamV2IdentityPool
    intent: Get an identity pool
    question: What claim and filter does a particular identity pool use?
  - id: updateIamV2IdentityPool
    intent: Update an identity pool
    question: Can I change the CEL filter on an existing identity pool?
  - id: deleteIamV2IdentityPool
    intent: Delete an identity pool
    question: How do I remove an identity pool I no longer need?
  phrasing_ops: 5
  slug: confluent-identity-pools-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityProvider` objects represent external OAuth'
  name: Confluent Identity Providers (iam/v2) API
  phrasing_intents:
  - id: listIamV2IdentityProviders
    intent: List OAuth identity providers
    question: Which OAuth identity providers are configured for my organization?
  - id: createIamV2IdentityProvider
    intent: Add an OAuth identity provider
    question: How do I let OAuth/OIDC tokens from my identity provider authenticate to Confluent Cloud?
  - id: getIamV2IdentityProvider
    intent: Get an identity provider
    question: What issuer and identity claim does a configured identity provider use?
  - id: updateIamV2IdentityProvider
    intent: Update an identity provider
    question: Can I change the identity claim or JWKS URI of an existing identity provider?
  - id: deleteIamV2IdentityProvider
    intent: Delete an identity provider
    question: How do I stop trusting tokens from an identity provider?
  phrasing_ops: 5
  slug: confluent-identity-providers-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) You can create an `Integration` to specify how we c'
  name: Confluent Integrations (notifications/v1) API
  phrasing_intents:
  - id: createNotificationsV1Integration
    intent: Create a notification integration
    question: How do I send Confluent Cloud notifications to a webhook or Slack channel?
  - id: listNotificationsV1Integrations
    intent: List notification integrations
    question: Which notification integrations are set up for my organization?
  - id: getNotificationsV1Integration
    intent: Get a notification integration
    question: What target is a specific notification integration pointing to?
  - id: updateNotificationsV1Integration
    intent: Update a notification integration
    question: Can I change the webhook target of an existing notification integration?
  - id: deleteNotificationsV1Integration
    intent: Delete a notification integration
    question: How do I stop sending notifications to an integration I no longer use?
  - id: testNotificationsV1Integration
    intent: Send a test notification to an integration
    question: Is there a way to check my webhook, Slack or Teams integration works before relying on it?
  phrasing_ops: 6
  slug: confluent-integrations-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Provider Integration` objects represent access to '
  name: Confluent Integrations (pim/v1) API
  phrasing_intents:
  - id: listPimV1Integrations
    intent: List cloud provider integrations
    question: Which cloud provider integrations exist in my environment?
  - id: createPimV1Integration
    intent: Create a cloud provider integration
    question: How do I give Confluent Cloud access to my cloud account through a provider integration?
  - id: getPimV1Integration
    intent: Read a cloud provider integration
    question: Which resources are using a particular provider integration?
  - id: deletePimV1Integration
    intent: Delete a cloud provider integration
    question: Why does deleting a provider integration fail while workloads still use it?
  phrasing_ops: 4
  slug: confluent-integrations-pim-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/b'
  name: Confluent Integrations (pim/v2) API
  phrasing_intents:
  - id: listPimV2Integrations
    intent: List cloud provider integrations
    question: Which cloud provider integrations exist in my Confluent environment?
  - id: createPimV2Integration
    intent: Create a cloud provider integration
    question: How do I set up a new provider integration so Confluent can access my cloud account?
  - id: getPimV2Integration
    intent: Get one cloud provider integration
    question: What is the current status and config of a specific provider integration?
  - id: updatePimV2Integration
    intent: Update a cloud provider integration
    question: Can I rename or change the configuration of an existing provider integration?
  - id: deletePimV2Integration
    intent: Delete a cloud provider integration
    question: Can I remove a provider integration I no longer use?
  - id: validatePimV2Integration
    intent: Validate a cloud provider integration
    question: Is my provider integration configured correctly before I rely on it?
  phrasing_ops: 6
  slug: confluent-integrations-pim-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Invitation` objects represent invitations to invit'
  name: Confluent Invitations (iam/v2) API
  phrasing_intents:
  - id: listIamV2Invitations
    intent: List user invitations
    question: Which user invitations are still pending in my organization?
  - id: createIamV2Invitation
    intent: Invite a user to the organization
    question: How do I invite a new teammate to Confluent Cloud by email?
  - id: getIamV2Invitation
    intent: Get an invitation
    question: Has a particular invitation been accepted yet?
  - id: deleteIamV2Invitation
    intent: Revoke an invitation
    question: How do I cancel an invitation I sent by mistake?
  phrasing_ops: 4
  slug: confluent-invitations-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) IP Addresses Related guide: [Use Public Egress IP a'
  name: Confluent IP Addresses (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1IpAddresses
    intent: List public egress IP addresses
    question: Which public egress IP addresses does Confluent Cloud use, so I can allowlist them?
  phrasing_ops: 1
  slug: confluent-ip-addresses-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The IP Filter Summary endpoint returns an aggregati'
  name: Confluent IP Filter Summaries (iam/v2) API
  phrasing_intents:
  - id: getIamV2IpFilterSummary
    intent: Get an IP filter summary
    question: Which IP filters are in effect for my organization?
  phrasing_ops: 1
  slug: confluent-ip-filter-summaries-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IP Filter` objects are bindings between IP Groups '
  name: Confluent IP Filters (iam/v2) API
  phrasing_intents:
  - id: listIamV2IpFilters
    intent: List IP filters
    question: Which IP filters restrict access to my Confluent Cloud organization?
  - id: createIamV2IpFilter
    intent: Create an IP filter
    question: How do I allow access only from my corporate IP ranges?
  - id: getIamV2IpFilter
    intent: Get one IP filter
    question: Which IP groups and operations does a particular IP filter cover?
  - id: updateIamV2IpFilter
    intent: Update an IP filter
    question: Can I add another IP group to an existing filter?
  - id: deleteIamV2IpFilter
    intent: Delete an IP filter
    question: How do I remove an IP filter that is blocking legitimate traffic?
  phrasing_ops: 5
  slug: confluent-ip-filters-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Definitions of networks which can be named and refe'
  name: Confluent IP Groups (iam/v2) API
  phrasing_intents:
  - id: listIamV2IpGroups
    intent: List IP groups
    question: Which IP groups are defined for IP filtering in my organization?
  - id: createIamV2IpGroup
    intent: Create an IP group
    question: How do I define a set of CIDR ranges as an IP group?
  - id: getIamV2IpGroup
    intent: Read an IP group
    question: Which CIDR blocks does a specific IP group contain?
  - id: updateIamV2IpGroup
    intent: Update an IP group
    question: Can I add or change CIDR ranges in an existing IP group?
  - id: deleteIamV2IpGroup
    intent: Delete an IP group
    question: How do I remove an IP group I no longer use?
  phrasing_ops: 5
  slug: confluent-ip-groups-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `JWKS` objects represent public key sets for a spec'
  name: Confluent Jwks (iam/v2) API
  phrasing_intents:
  - id: refreshIamV2JsonWebKeySet
    intent: Refresh an identity provider's JWKS
    question: How do I force Confluent Cloud to pick up rotated signing keys from my identity provider?
  phrasing_ops: 1
  slug: confluent-jwks-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `KafkaCluster` object represent Confluent Platform Kafka clusters registered wi'
  name: Confluent Kafka Clusters (usm/v1) API
  phrasing_intents:
  - id: listUsmV1KafkaClusters
    intent: List registered Confluent Platform Kafka clusters
    question: Which self-managed Confluent Platform clusters are registered in an environment?
  - id: createUsmV1KafkaCluster
    intent: Register a Confluent Platform Kafka cluster
    question: Can I register a self-managed Kafka cluster with Confluent Cloud?
  - id: getUsmV1KafkaCluster
    intent: Get a registered Confluent Platform cluster
    question: What details are stored for a self-managed cluster I registered?
  - id: deleteUsmV1KafkaCluster
    intent: Unregister a Confluent Platform cluster
    question: How do I unregister a self-managed Kafka cluster?
  phrasing_ops: 4
  slug: confluent-kafka-clusters-usm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Key Encryption Keys (v1) API
  phrasing_intents:
  - id: getKekNames
    intent: List key encryption key names
    question: Which key encryption keys are registered for client-side field encryption?
  - id: createKek
    intent: Register a key encryption key
    question: How do I register a KMS key as a KEK in the DEK registry?
  - id: deleteKek
    intent: Delete a key encryption key
    question: Can I soft-delete a KEK and still bring it back later?
  - id: getKek
    intent: Get a key encryption key
    question: What KMS type and key ID back a given KEK?
  - id: putKek
    intent: Alter a key encryption key
    question: Can I change the KMS properties or description of an existing KEK?
  - id: undeleteKek
    intent: Restore a deleted key encryption key
    question: Can I restore a KEK that I soft-deleted?
  - id: testKek
    intent: Test a key encryption key
    question: Can I check that a KEK actually works against its KMS?
  phrasing_ops: 7
  slug: confluent-key-encryption-keys-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Key` objects represent customer managed keys on de'
  name: Confluent Keys (byok/v1) API
  phrasing_intents:
  - id: listByokV1Keys
    intent: List bring-your-own-keys
    question: Which customer-managed encryption keys have I registered?
  - id: createByokV1Key
    intent: Register a bring-your-own-key
    question: How do I register my own KMS key to encrypt a dedicated Kafka cluster?
  - id: getByokV1Key
    intent: Get a bring-your-own-key
    question: Is my registered encryption key available for cluster provisioning?
  - id: updateByokV1Key
    intent: Update a bring-your-own-key
    question: Can I rename a registered encryption key?
  - id: deleteByokV1Key
    intent: Delete a bring-your-own-key
    question: Can I remove a customer-managed key I no longer use?
  phrasing_ops: 5
  slug: confluent-keys-byok-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the lifecycle for a Managed Connec'
  name: Confluent Lifecycle (connect/v1) API
  phrasing_intents:
  - id: pauseConnectv1Connector
    intent: Pause a connector
    question: How do I temporarily stop a connector from processing messages?
  - id: resumeConnectv1Connector
    intent: Resume a paused connector
    question: Can I restart message flow on a connector I paused?
  - id: restartConnectv1Connector
    intent: Restart a connector and its tasks
    question: Is there a way to restart a connector and all its tasks?
  phrasing_ops: 3
  slug: confluent-lifecycle-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed connectors in Confluent Cloud.'
  name: Confluent Managed Connector Plugins (connect/v1) API
  phrasing_intents:
  - id: listConnectv1ConnectorPlugins
    intent: List managed connector plugins
    question: Which fully managed connectors can I run on my Kafka cluster?
  - id: validateConnectv1ConnectorPlugin
    intent: Validate a managed connector config
    question: Can I check a connector configuration for errors before creating the connector?
  - id: translateConnectv1ConnectorPlugin
    intent: Translate self-managed connector config
    question: How do I convert a self-managed connector config into a fully managed one?
  phrasing_ops: 3
  slug: confluent-managed-connector-plugins-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTableVersion` represents a specific ve'
  name: Confluent Materialized Table Versions (sql/v1) API
  phrasing_intents:
  - id: listSqlv1MaterializedTableVersions
    intent: List versions of a materialized table
    question: What versions exist for one of my Flink materialized tables?
  - id: getSqlv1MaterializedTableVersion
    intent: Get a materialized table version
    question: What did a specific earlier version of a materialized table look like?
  phrasing_ops: 2
  slug: confluent-materialized-table-versions-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTable` represents a core resource used'
  name: Confluent Materialized Tables (sql/v1) API
  phrasing_intents:
  - id: listSqlv1MaterializedTables
    intent: List materialized tables in an environment
    question: Which Flink materialized tables exist in my environment?
  - id: createSqlv1MaterializedTable
    intent: Create a materialized table
    question: How do I create a continuously maintained materialized table with Flink SQL in Confluent?
  - id: getSqlv1MaterializedTable
    intent: Get a materialized table
    question: What query and status does one materialized table have?
  - id: updateSqlv1MaterializedTable
    intent: Update or evolve a materialized table
    question: Can I change a materialized table's query, compute pool or columns?
  - id: deleteSqlv1MaterializedTable
    intent: Delete a materialized table
    question: How do I drop a materialized table I no longer need?
  phrasing_ops: 5
  slug: confluent-materialized-tables-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Modes (v1) API
  phrasing_intents:
  - id: getMode
    intent: Get a subject's Schema Registry mode
    question: Is a particular subject in READONLY, READWRITE or IMPORT mode?
  - id: updateMode
    intent: Set a subject's Schema Registry mode
    question: How do I make one subject read-only?
  - id: deleteSubjectMode
    intent: Reset a subject's mode to the global default
    question: How do I clear a subject-level mode so it inherits the global mode again?
  - id: getTopLevelMode
    intent: Get the global Schema Registry mode
    question: What mode is my Schema Registry running in globally?
  - id: updateTopLevelMode
    intent: Set the global Schema Registry mode
    question: How do I put the whole Schema Registry into read-only mode?
  phrasing_ops: 5
  slug: confluent-modes-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Network Link Enpoint is associated with a Private'
  name: Confluent Network Link Endpoints (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1NetworkLinkEndpoints
    intent: List network link endpoints
    question: Which network link endpoints exist in my environment?
  - id: createNetworkingV1NetworkLinkEndpoint
    intent: Create a network link endpoint
    question: How do I connect my network to a network link service?
  - id: getNetworkingV1NetworkLinkEndpoint
    intent: Read a network link endpoint
    question: What phase is a particular network link endpoint in?
  - id: updateNetworkingV1NetworkLinkEndpoint
    intent: Update a network link endpoint
    question: Can I rename or edit an existing network link endpoint?
  - id: deleteNetworkingV1NetworkLinkEndpoint
    intent: Delete a network link endpoint
    question: How do I remove a network link endpoint?
  phrasing_ops: 5
  slug: confluent-network-link-endpoints-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of incoming Network Link Enpoints associated w'
  name: Confluent Network Link Service Associations (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1NetworkLinkServiceAssociations
    intent: List associations of a network link service
    question: Which network link endpoints are associated with my network link service?
  - id: getNetworkingV1NetworkLinkServiceAssociation
    intent: Get one network link service association
    question: What is the status of a single association on my network link service?
  phrasing_ops: 2
  slug: confluent-network-link-service-associations-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Network Link Service is associated with a Private L'
  name: Confluent Network Link Services (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1NetworkLinkServices
    intent: List network link services
    question: Which network link services exist in an environment?
  - id: createNetworkingV1NetworkLinkService
    intent: Create a network link service
    question: How do I expose my network so other Confluent networks can link to it for cluster linking?
  - id: getNetworkingV1NetworkLinkService
    intent: Get a network link service
    question: Is my network link service ready yet?
  - id: updateNetworkingV1NetworkLinkService
    intent: Update a network link service
    question: Can I change which environments or networks may connect to my network link service?
  - id: deleteNetworkingV1NetworkLinkService
    intent: Delete a network link service
    question: What removes a network link service from my network?
  phrasing_ops: 5
  slug: confluent-network-link-services-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Network` represents a network (VPC) in Confluent C'
  name: Confluent Networks (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1Networks
    intent: List networks in an environment
    question: Which Confluent Cloud networks exist in my environment?
  - id: createNetworkingV1Network
    intent: Create a network
    question: How do I create a private network for my Kafka clusters?
  - id: getNetworkingV1Network
    intent: Get a network
    question: What is the status and CIDR of a specific network?
  - id: updateNetworkingV1Network
    intent: Update a network
    question: Can I rename a network or change its DNS settings after creation?
  - id: deleteNetworkingV1Network
    intent: Delete a network
    question: How do I delete a network I no longer use?
  phrasing_ops: 5
  slug: confluent-networks-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The type of notifications (and their corresponding '
  name: Confluent Notification Types (notifications/v1) API
  phrasing_intents:
  - id: getNotificationsV1NotificationType
    intent: Read a notification type
    question: What does a particular notification type cover?
  - id: listNotificationsV1NotificationTypes
    intent: List notification types
    question: Which notification types can I subscribe to?
  phrasing_ops: 2
  slug: confluent-notification-types-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) OAuth Token is a [JSON Web Token (JWT)](https://www'
  name: Confluent OAuth Tokens (sts/v1) API
  phrasing_intents:
  - id: exchangeStsV1OauthToken
    intent: Exchange an external token for a Confluent token
    question: How do I trade a JWT from my identity provider for a Confluent Cloud access token?
  phrasing_ops: 1
  slug: confluent-oauth-tokens-sts-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the offsets for a Managed Connecto'
  name: Confluent Offsets (connect/v1) API
  phrasing_intents:
  - id: getConnectv1ConnectorOffsets
    intent: Get a connector's current offsets
    question: Where in the source system is my connector currently reading from?
  - id: alterConnectv1ConnectorOffsetsRequest
    intent: Change or reset a connector's offsets
    question: How do I rewind a connector to reprocess data from an earlier offset?
  - id: getConnectv1ConnectorOffsetsRequestStatus
    intent: Check status of an offset change request
    question: Did my request to alter a connector's offsets finish successfully?
  phrasing_ops: 3
  slug: confluent-offsets-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Stream sharing opt in options ## The Opt Ins Model '
  name: Confluent Opt Ins (cdx/v1) API
  phrasing_intents:
  - id: getCdxV1OptIn
    intent: Check stream sharing opt-in settings
    question: Is stream sharing enabled for my organization?
  - id: updateCdxV1OptIn
    intent: Turn stream sharing on or off
    question: How do I enable stream sharing for my organization?
  phrasing_ops: 2
  slug: confluent-opt-ins-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `OrgComputePoolConfig` manages compute pool configu'
  name: Confluent Org Compute Pool Configs (fcpm/v2) API
  phrasing_intents:
  - id: getFcpmV2OrgComputePoolConfig
    intent: Get organization Flink compute pool settings
    question: What are my organization-wide Flink compute pool settings?
  - id: updateFcpmV2OrgComputePoolConfig
    intent: Update organization Flink compute pool settings
    question: Can I change the organization-wide defaults for Flink compute pools?
  phrasing_ops: 2
  slug: confluent-org-compute-pool-configs-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Organization` objects represent a customer organiz'
  name: Confluent Organizations (org/v2) API
  phrasing_intents:
  - id: listOrgV2Organizations
    intent: List organizations
    question: Which Confluent Cloud organizations can I access?
  - id: getOrgV2Organization
    intent: Read an organization
    question: What is the display name and JIT setting of a given organization?
  - id: updateOrgV2Organization
    intent: Update an organization
    question: How do I rename my organization?
  phrasing_ops: 3
  slug: confluent-organizations-org-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent Organizations (partner/v2) API
  phrasing_intents:
  - id: getPartnerV2Organization
    intent: Get one customer organization as a partner
    question: What details can I see about one customer organization I manage as a partner?
  - id: listPartnerV2Organizations
    intent: List customer organizations as a partner
    question: Which customer organizations do I manage through the Confluent partner program?
  phrasing_ops: 2
  slug: confluent-organizations-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Partition (v3) API
  phrasing_intents:
  - id: listKafkaPartitions
    intent: List a topic's partitions
    question: How many partitions does a topic have?
  - id: getKafkaPartition
    intent: Get one partition of a topic
    question: Who is the leader of a specific partition?
  phrasing_ops: 2
  slug: confluent-partition-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove VPC/VNet peering connections between '
  name: Confluent Peerings (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1Peerings
    intent: List VPC/VNet peerings
    question: Which VPC or VNet peerings are connected to my Confluent networks?
  - id: createNetworkingV1Peering
    intent: Create a VPC/VNet peering
    question: How do I peer my cloud VPC with a Confluent Cloud network?
  - id: getNetworkingV1Peering
    intent: Get one peering
    question: Is a specific peering connection ready or still pending?
  - id: updateNetworkingV1Peering
    intent: Update a peering
    question: Can I rename an existing peering connection?
  - id: deleteNetworkingV1Peering
    intent: Delete a peering
    question: How do I disconnect a VPC peering from Confluent Cloud?
  phrasing_ops: 5
  slug: confluent-peerings-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Flink Artifa'
  name: Confluent Presigned Urls (artifact/v1) API
  phrasing_intents:
  - id: presigned-upload-urlArtifactV1PresignedUrl
    intent: Get a presigned URL to upload a Flink artifact
    question: How do I upload a Flink artifact archive before registering it?
  phrasing_ops: 1
  slug: confluent-presigned-urls-artifact-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Connect Arti'
  name: Confluent Presigned Urls (cam/v1) API
  phrasing_intents:
  - id: presigned-upload-urlCamV1PresignedUrl
    intent: Get an upload URL for a Connect artifact
    question: How do I upload a custom connector archive to Confluent Cloud?
  phrasing_ops: 1
  slug: confluent-presigned-urls-cam-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent Presigned Urls (ccpm/v1) API
  phrasing_intents:
  - id: createCcpmV1PresignedUrl
    intent: Get an upload URL for a custom plugin archive
    question: How do I upload a custom connector plugin archive to Confluent Cloud?
  phrasing_ops: 1
  slug: confluent-presigned-urls-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent Presigned Urls (connect/v1) API
  phrasing_intents:
  - id: presigned-upload-urlConnectV1PresignedUrl
    intent: Get an upload URL for a custom connector plugin
    question: How do I upload a custom connector plugin archive?
  phrasing_ops: 1
  slug: confluent-presigned-urls-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove access to PrivateLink endpoints by AW'
  name: Confluent Private Link Accesses (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1PrivateLinkAccesses
    intent: List private link accesses
    question: Which cloud accounts have private link access to my network?
  - id: createNetworkingV1PrivateLinkAccess
    intent: Grant private link access
    question: How do I allow a cloud account to reach my Confluent network over private link?
  - id: getNetworkingV1PrivateLinkAccess
    intent: Read a private link access
    question: What account and status does a given private link access have?
  - id: updateNetworkingV1PrivateLinkAccess
    intent: Update a private link access
    question: Can I rename an existing private link access?
  - id: deleteNetworkingV1PrivateLinkAccess
    intent: Revoke a private link access
    question: How do I revoke a cloud account's private link access?
  phrasing_ops: 5
  slug: confluent-private-link-accesses-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment connection objects represent'
  name: Confluent Private Link Attachment Connections (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1PrivateLinkAttachmentConnections
    intent: List private link attachment connections
    question: Which private endpoint connections are attached in an environment?
  - id: createNetworkingV1PrivateLinkAttachmentConnection
    intent: Create a private link attachment connection
    question: How do I register my VPC private endpoint against a private link attachment?
  - id: getNetworkingV1PrivateLinkAttachmentConnection
    intent: Get a private link attachment connection
    question: Is my private endpoint connection ready?
  - id: updateNetworkingV1PrivateLinkAttachmentConnection
    intent: Update a private link attachment connection
    question: Can I rename a private link attachment connection?
  - id: deleteNetworkingV1PrivateLinkAttachmentConnection
    intent: Delete a private link attachment connection
    question: What disconnects a private endpoint from a private link attachment?
  phrasing_ops: 5
  slug: confluent-private-link-attachment-connections-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment objects represent reservatio'
  name: Confluent Private Link Attachments (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1PrivateLinkAttachments
    intent: List private link attachments
    question: Which private link attachments exist in my environment?
  - id: createNetworkingV1PrivateLinkAttachment
    intent: Create a private link attachment
    question: How do I set up a private link attachment for serverless Kafka clusters?
  - id: getNetworkingV1PrivateLinkAttachment
    intent: Get a private link attachment
    question: Is my private link attachment ready?
  - id: updateNetworkingV1PrivateLinkAttachment
    intent: Update a private link attachment
    question: Can I rename a private link attachment?
  - id: deleteNetworkingV1PrivateLinkAttachment
    intent: Delete a private link attachment
    question: How do I remove a private link attachment?
  phrasing_ops: 5
  slug: confluent-private-link-attachments-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderSharedResource` object contains details of'
  name: Confluent Provider Shared Resources (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ProviderSharedResources
    intent: List resources I share as a provider
    question: Which topics and clusters am I sharing out through Stream Sharing?
  - id: getCdxV1ProviderSharedResource
    intent: Get a provider shared resource
    question: What details are stored for a resource I'm sharing as a provider?
  - id: updateCdxV1ProviderSharedResource
    intent: Update a provider shared resource's listing
    question: Can I change the display name, description and tags on a resource I share?
  - id: upload_imageCdxV1ProviderSharedResource
    intent: Upload an image for a shared resource
    question: Can I upload a logo image for a resource I share with consumers?
  - id: view_imageCdxV1ProviderSharedResource
    intent: Download a provider shared resource image
    question: How do I fetch the logo image attached to a resource I'm sharing?
  - id: delete_imageCdxV1ProviderSharedResource
    intent: Delete a shared resource's image
    question: How do I remove an outdated logo from a shared resource?
  phrasing_ops: 6
  slug: confluent-provider-shared-resources-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderShare` object respresents the share that y'
  name: Confluent Provider Shares (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ProviderShares
    intent: List Stream Shares I have provided
    question: Which topics have I shared with other organizations through Stream Sharing?
  - id: createCdxV1ProviderShare
    intent: Share a resource with a consumer
    question: How do I share a topic with a partner who is outside my organization?
  - id: getCdxV1ProviderShare
    intent: Get one provider share
    question: Has the consumer accepted a share I sent?
  - id: deleteCdxV1ProviderShare
    intent: Revoke a provider share
    question: How do I stop sharing a topic with a consumer?
  - id: resendCdxV1ProviderShare
    intent: Resend a share invitation
    question: Can I resend a share invite the recipient never received?
  phrasing_ops: 5
  slug: confluent-provider-shares-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Records (v3) API
  phrasing_intents:
  - id: produceRecord
    intent: Produce records to a Kafka topic
    question: How do I send a message to a Kafka topic over REST?
  phrasing_ops: 1
  slug: confluent-records-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions a'
  name: Confluent Regions (fcpm/v2) API
  phrasing_intents:
  - id: listFcpmV2Regions
    intent: List Flink regions
    question: Which cloud regions can I run Flink compute pools in?
  phrasing_ops: 1
  slug: confluent-regions-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent Regions (rtce/v1) API
  phrasing_intents:
  - id: listRtceV1Regions
    intent: List available RTCE regions
    question: Which cloud regions are available for RTCE in Confluent Cloud?
  phrasing_ops: 1
  slug: confluent-regions-rtce-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions available when placing '
  name: Confluent Regions (srcm/v2) API
  phrasing_intents:
  - id: listSrcmV2Regions
    intent: List Schema Registry regions (deprecated)
    question: Which cloud regions can host a Schema Registry cluster?
  - id: getSrcmV2Region
    intent: Get a Schema Registry region (deprecated)
    question: What packages does a specific Schema Registry region support?
  phrasing_ops: 2
  slug: confluent-regions-srcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent Regions (tableflow/v1) API
  phrasing_intents:
  - id: listTableflowV1Regions
    intent: List Tableflow regions
    question: In which regions is Tableflow available?
  phrasing_ops: 1
  slug: confluent-regions-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourcePreference` objects represent the intent o'
  name: Confluent Resource Preferences (notifications/v1) API
  phrasing_intents:
  - id: createNotificationsV1ResourcePreference
    intent: Create a notification preference for a resource
    question: How do I turn notifications on or off for one specific cluster?
  - id: getNotificationsV1ResourcePreference
    intent: Read a resource preference
    question: What state is a given resource preference in?
  - id: updateNotificationsV1ResourcePreference
    intent: Update a resource preference
    question: Can I re-enable notifications for a resource I previously silenced?
  - id: deleteNotificationsV1ResourcePreference
    intent: Delete a resource preference
    question: How do I remove a notification preference I set on a resource?
  - id: getNotificationsV1ResourcePreferenceByFilter
    intent: Find a resource's notification preference
    question: Is there already a notification preference for a given resource?
  phrasing_ops: 5
  slug: confluent-resource-preferences-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourceSubscription` objects represent the intent'
  name: Confluent Resource Subscriptions (notifications/v1) API
  phrasing_intents:
  - id: createNotificationsV1ResourceSubscription
    intent: Subscribe a resource to notifications
    question: How do I get notified about events on one specific cluster or resource?
  - id: getNotificationsV1ResourceSubscription
    intent: Get a resource subscription
    question: What notification type and integrations does a resource subscription use?
  - id: updateNotificationsV1ResourceSubscription
    intent: Update a resource subscription
    question: Can I disable a resource subscription without deleting it?
  - id: deleteNotificationsV1ResourceSubscription
    intent: Delete a resource subscription
    question: How do I stop notifications for a resource I subscribed to?
  - id: listNotificationsV1ResourceSubscriptionsByFilter
    intent: Look up subscriptions for a resource
    question: Which notification subscriptions exist for a given cluster or resource?
  phrasing_ops: 5
  slug: confluent-resource-subscriptions-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A role binding grants a Principal a role on resourc'
  name: Confluent Role Bindings (iam/v2) API
  phrasing_intents:
  - id: listIamV2RoleBindings
    intent: List role bindings on a resource
    question: Who has which roles on a given Confluent resource?
  - id: createIamV2RoleBinding
    intent: Grant a role to a principal
    question: How do I give a service account the CloudClusterAdmin role on a cluster?
  - id: getIamV2RoleBinding
    intent: Get one role binding
    question: What principal, role and resource does a specific role binding cover?
  - id: deleteIamV2RoleBinding
    intent: Revoke a role binding
    question: How do I take a role away from a user or service account?
  phrasing_ops: 4
  slug: confluent-role-bindings-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An RtceTopic represents a customer''s Kafka topic en'
  name: Confluent Rtce Topics (rtce/v1) API
  phrasing_intents:
  - id: listRtceV1RtceTopics
    intent: List RTCE topics for a Kafka cluster
    question: Which real-time context engine topics are set up on my Kafka cluster?
  - id: createRtceV1RtceTopic
    intent: Create an RTCE topic
    question: How do I enable a topic for the real-time context engine?
  - id: getRtceV1RtceTopic
    intent: Get an RTCE topic
    question: What is the status of one RTCE topic?
  - id: updateRtceV1RtceTopic
    intent: Update an RTCE topic
    question: Can I change the spec of an existing RTCE topic?
  - id: deleteRtceV1RtceTopic
    intent: Delete an RTCE topic
    question: How do I remove a topic from the real-time context engine?
  phrasing_ops: 5
  slug: confluent-rtce-topics-rtce-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Schemas (v1) API
  phrasing_intents:
  - id: getSchema
    intent: Get a schema string by ID
    question: How do I fetch the schema for a given schema ID in Schema Registry?
  - id: getSchemaOnly
    intent: Get only the raw schema by ID
    question: Can I get just the raw schema text for an ID without the wrapper object?
  - id: getSchemaTypes
    intent: List supported schema types
    question: Which schema formats does the registry support, like Avro, Protobuf or JSON Schema?
  - id: getSchemas
    intent: Search schemas by subject prefix
    question: How do I find all schemas whose subject starts with a prefix?
  - id: getSubjects
    intent: List subjects using a schema ID
    question: Which subjects reference a particular schema ID?
  - id: getVersions
    intent: List subject-version pairs for a schema ID
    question: What subject and version combinations point at one schema ID?
  phrasing_ops: 6
  slug: confluent-schemas-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets a list of all available scopes for applied quo'
  name: Confluent Scopes (service-quota/v1) API
  phrasing_intents:
  - id: listServiceQuotaV1Scopes
    intent: List service quota scopes
    question: At which levels, like organization or environment, are service quotas applied?
  - id: getServiceQuotaV1Scope
    intent: Get one service quota scope
    question: What does a particular service quota scope represent?
  phrasing_ops: 2
  slug: confluent-scopes-service-quota-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to search for entities. Related gu'
  name: Confluent Search (v1) API
  phrasing_intents:
  - id: searchUsingAttribute
    intent: Search the catalog by attribute
    question: Can I find catalog entities whose attribute value starts with a prefix?
  - id: searchUsingBasic
    intent: Search the catalog by full text
    question: How do I search the Stream Catalog with a free-text query?
  phrasing_ops: 2
  slug: confluent-search-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ServiceAccount` objects are typically used to repr'
  name: Confluent Service Accounts (iam/v2) API
  phrasing_intents:
  - id: listIamV2ServiceAccounts
    intent: List service accounts
    question: Which service accounts exist in my Confluent Cloud organization?
  - id: createIamV2ServiceAccount
    intent: Create a service account
    question: How do I create a service account for an application to authenticate with?
  - id: getIamV2ServiceAccount
    intent: Get one service account
    question: What is the name and description of a given service account?
  - id: updateIamV2ServiceAccount
    intent: Update a service account's description
    question: Can I change the description of an existing service account?
  - id: deleteIamV2ServiceAccount
    intent: Delete a service account
    question: How do I delete a service account an application no longer uses?
  phrasing_ops: 5
  slug: confluent-service-accounts-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Share Group (v3) API
  phrasing_intents:
  - id: listKafkaShareGroups
    intent: List share groups on a cluster
    question: Which share groups exist on my Kafka cluster?
  - id: getKafkaShareGroup
    intent: Get one share group
    question: What state is a particular share group in?
  - id: deleteKafkaShareGroup
    intent: Delete a share group
    question: Can I delete a share group I no longer need?
  - id: listKafkaShareGroupConsumers
    intent: List consumers in a share group
    question: Which consumers are currently part of a share group?
  - id: getKafkaShareGroupConsumer
    intent: Get one consumer in a share group
    question: What do I know about one consumer in a share group, like its client ID?
  - id: listKafkaShareGroupConsumerAssignments
    intent: List a share consumer's partition assignments
    question: Which topic partitions is a share group consumer assigned to?
  phrasing_ops: 6
  slug: confluent-share-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Encrypted Token shared with consumer ## The Shared '
  name: Confluent Shared Tokens (cdx/v1) API
  phrasing_intents:
  - id: resourcesCdxV1SharedToken
    intent: Preview resources in a share token
    question: What topics would I get access to from a stream share invite token?
  - id: redeemCdxV1SharedToken
    intent: Redeem a stream share token
    question: How do I accept a stream share and get the topic and cluster access details?
  phrasing_ops: 2
  slug: confluent-shared-tokens-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent Signup (partner/v2) API
  phrasing_intents:
  - id: signup
    intent: Sign up a new organization for a customer
    question: How do I create a Confluent Cloud organization on behalf of a customer as a partner?
  - id: activateSignup
    intent: Activate an incomplete signup
    question: How do I finish a customer signup that was left incomplete?
  - id: signupPartnerV2Link
    intent: Link a customer to an existing organization
    question: Can I sign up a customer by linking them to an organization they already have?
  phrasing_ops: 3
  slug: confluent-signup-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementException` represents an exception of a `'
  name: Confluent Statement Exceptions (sql/v1) API
  phrasing_intents:
  - id: getSqlv1StatementExceptions
    intent: List recent exceptions for a Flink statement
    question: Why did my Flink SQL statement fail?
  phrasing_ops: 1
  slug: confluent-statement-exceptions-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementResult` represents a result of a `Stateme'
  name: Confluent Statement Results (sql/v1) API
  phrasing_intents:
  - id: getSqlv1StatementResult
    intent: Read a Flink SQL statement's results
    question: How do I fetch the rows returned by a Flink SQL query I ran?
  phrasing_ops: 1
  slug: confluent-statement-results-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: Execute SQL statements against queryable topics and read their results. A statement that resolves quickly returns its results inline; a long-running one is assigned a background job that can be polled
  name: Confluent Statements (query/v1alpha1) API
  phrasing_intents:
  - id: executeQueryV1alpha1Statement
    intent: Run a SQL query against a Kafka cluster
    question: How do I run a SQL query over my Kafka topics and get rows back?
  - id: getQueryV1alpha1JobStatus
    intent: Check status of a background query
    question: Is my long-running background SQL query still running or finished?
  phrasing_ops: 2
  slug: confluent-statements-query-v1alpha1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Statement` represents a core resource used to mode'
  name: Confluent Statements (sql/v1) API
  phrasing_intents:
  - id: listSqlv1Statements
    intent: List Flink SQL statements
    question: Which Flink SQL statements are running in my environment?
  - id: createSqlv1Statement
    intent: Submit a Flink SQL statement
    question: How do I run a new Flink SQL statement through the API?
  - id: getSqlv1Statement
    intent: Read a Flink SQL statement
    question: What is the current status and result of one of my SQL statements?
  - id: deleteSqlv1Statement
    intent: Delete a Flink SQL statement
    question: How do I remove a SQL statement I no longer need?
  - id: updateSqlv1Statement
    intent: Replace a Flink SQL statement
    question: Why does updating a statement fail with a 409 Conflict?
  - id: patchSqlv1Statement
    intent: Patch a Flink SQL statement
    question: Is there an early-access way to change only part of a SQL statement?
  phrasing_ops: 6
  slug: confluent-statements-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for requesting the status or the tasks for a Ma'
  name: Confluent Status (connect/v1) API
  phrasing_intents:
  - id: readConnectv1ConnectorStatus
    intent: Check a connector's status
    question: Is my connector running, paused or failed?
  - id: listConnectv1ConnectorTasks
    intent: List a connector's tasks
    question: Which tasks are currently running for a connector?
  phrasing_ops: 2
  slug: confluent-status-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Streams Group (v3) API
  phrasing_intents:
  - id: listKafkaStreamsGroups
    intent: List Kafka Streams groups on a cluster
    question: Which Kafka Streams applications are registered as streams groups on my Confluent cluster?
  - id: getKafkaStreamsGroup
    intent: Get details of one streams group
    question: What state is a particular Kafka Streams group in right now?
  - id: listKafkaStreamsGroupSubtopologies
    intent: List subtopologies of a streams group
    question: What subtopologies make up my Kafka Streams group's topology?
  - id: getKafkaStreamsGroupSubtopology
    intent: Get one subtopology of a streams group
    question: Which source topics feed a specific subtopology in my streams group?
  - id: listKafkaStreamsGroupMembers
    intent: List members of a streams group
    question: Which Kafka Streams instances are currently members of my streams group?
  - id: getKafkaStreamsGroupMember
    intent: Get one member of a streams group
    question: What do I know about a single member of a Kafka Streams group?
  - id: getKafkaStreamsGroupMemberAssignments
    intent: Get a streams member's current assignments
    question: Which tasks is a Kafka Streams member currently assigned?
  - id: getKafkaStreamsGroupMemberTargetAssignments
    intent: Get a streams member's target assignments
    question: What is the target assignment a streams member is being rebalanced toward?
  phrasing_ops: 12
  slug: confluent-streams-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Subjects (v1) API
  phrasing_intents:
  - id: getSchemaByVersion
    intent: Get a schema version under a subject
    question: How do I fetch a specific version of a schema registered under a subject?
  - id: deleteSchemaVersion
    intent: Delete a schema version from a subject
    question: Can I remove one version of a schema without deleting the whole subject?
  - id: getReferencedBy
    intent: List schemas that reference a schema version
    question: Which other schemas reference this schema version?
  - id: getSchemaOnly_1
    intent: Get only the raw schema string for a version
    question: How do I get just the unescaped schema text for a subject version, without metadata?
  - id: listVersions
    intent: List versions registered under a subject
    question: What versions exist for a subject in Schema Registry?
  - id: register
    intent: Register a new schema under a subject
    question: How do I register a new Avro or Protobuf schema under a subject?
  - id: lookUpSchemaUnderSubject
    intent: Check if a schema is already registered
    question: Has this exact schema already been registered under my subject?
  - id: deleteSubject
    intent: Delete a subject and all its versions
    question: How do I delete a whole subject from Schema Registry when recycling a topic?
  phrasing_ops: 10
  slug: confluent-subjects-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Subscription` objects represent the intent of the '
  name: Confluent Subscriptions (notifications/v1) API
  phrasing_intents:
  - id: listNotificationsV1Subscriptions
    intent: List notification subscriptions
    question: Which notification types am I subscribed to?
  - id: createNotificationsV1Subscription
    intent: Subscribe to a notification type
    question: How do I subscribe to a notification type and send it to an integration?
  - id: getNotificationsV1Subscription
    intent: Read a notification subscription
    question: Which integrations does a given subscription deliver to?
  - id: updateNotificationsV1Subscription
    intent: Update a notification subscription
    question: Can I pause a subscription without deleting it?
  - id: deleteNotificationsV1Subscription
    intent: Delete a notification subscription
    question: How do I unsubscribe from a notification type entirely?
  phrasing_ops: 5
  slug: confluent-subscriptions-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Tableflow Topic represents configuration related '
  name: Confluent Tableflow Topics (tableflow/v1) API
  phrasing_intents:
  - id: listTableflowV1TableflowTopics
    intent: List Tableflow-enabled topics
    question: Which Kafka topics have Tableflow turned on in a cluster?
  - id: createTableflowV1TableflowTopic
    intent: Enable Tableflow on a topic
    question: How do I turn a Kafka topic into an Iceberg or Delta table?
  - id: getTableflowV1TableflowTopic
    intent: Get a Tableflow topic
    question: What is the Tableflow status of one of my topics?
  - id: updateTableflowV1TableflowTopic
    intent: Update a Tableflow topic
    question: Can I change the table formats or retention of a Tableflow topic?
  - id: deleteTableflowV1TableflowTopic
    intent: Disable Tableflow on a topic
    question: How do I stop materializing a topic as a table?
  phrasing_ops: 5
  slug: confluent-tableflow-topics-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Tool` models a reusable tool resource backed by a connection that can be refer'
  name: Confluent Tools (sql/v1) API
  phrasing_intents:
  - id: createSqlv1Tool
    intent: Create a Flink SQL tool
    question: How do I define a tool backed by an MCP connection in a Flink database?
  - id: listSqlv1Tools
    intent: List Flink SQL tools in a database
    question: Which tools are defined in one of my Flink SQL databases?
  - id: getSqlv1Tool
    intent: Read a Flink SQL tool
    question: What connection or function does a specific tool reference?
  - id: deleteSqlv1Tool
    intent: Delete a Flink SQL tool
    question: How do I remove a tool from a Flink database?
  phrasing_ops: 4
  slug: confluent-tools-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Topic (v3) API
  phrasing_intents:
  - id: listKafkaTopics
    intent: List topics in a Kafka cluster
    question: Which topics exist in my Kafka cluster?
  - id: createKafkaTopic
    intent: Create a Kafka topic
    question: How do I create a new Kafka topic with a set number of partitions?
  - id: getKafkaTopic
    intent: Get a Kafka topic
    question: What partition count and replication factor does a topic have?
  - id: updatePartitionCountKafkaTopic
    intent: Increase a topic's partition count
    question: How do I add partitions to an existing Kafka topic?
  - id: deleteKafkaTopic
    intent: Delete a Kafka topic
    question: How do I delete a Kafka topic and its data?
  phrasing_ops: 5
  slug: confluent-topic-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AWS Transit Gateway Attachments Related guide: [API'
  name: Confluent Transit Gateway Attachments (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1TransitGatewayAttachments
    intent: List AWS Transit Gateway attachments
    question: Which Transit Gateway attachments connect my AWS networks to Confluent?
  - id: createNetworkingV1TransitGatewayAttachment
    intent: Attach a network to a Transit Gateway
    question: How do I connect a Confluent network to my AWS Transit Gateway?
  - id: getNetworkingV1TransitGatewayAttachment
    intent: Get one Transit Gateway attachment
    question: Is my Transit Gateway attachment ready yet?
  - id: updateNetworkingV1TransitGatewayAttachment
    intent: Update a Transit Gateway attachment
    question: Can I rename an existing Transit Gateway attachment?
  - id: deleteNetworkingV1TransitGatewayAttachment
    intent: Delete a Transit Gateway attachment
    question: How do I detach a Confluent network from my Transit Gateway?
  phrasing_ops: 5
  slug: confluent-transit-gateway-attachments-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Types (v1) API
  phrasing_intents:
  - id: getAllBusinessMetadataDefs
    intent: List business metadata definitions
    question: What business metadata definitions exist in my Stream Catalog?
  - id: createBusinessMetadataDefs
    intent: Bulk create business metadata definitions
    question: How do I define new business metadata like owner or team for catalog entities?
  - id: updateBusinessMetadataDefs
    intent: Bulk update business metadata definitions
    question: Can I edit several business metadata definitions in one request?
  - id: deleteBusinessMetadataDef
    intent: Delete a business metadata definition
    question: Can I remove a business metadata definition I no longer use?
  - id: getBusinessMetadataDefByName
    intent: Get a business metadata definition
    question: What attributes does a specific business metadata definition have?
  - id: getAllTagDefs
    intent: List tag definitions
    question: Which tag definitions like PII or sensitive exist in my catalog?
  - id: updateTagDefs
    intent: Bulk update tag definitions
    question: Can I update several catalog tag definitions in one call?
  - id: createTagDefs
    intent: Bulk create tag definitions
    question: How do I create a new tag like PII to label schemas and topics?
  phrasing_ops: 10
  slug: confluent-types-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To User Notifications API v1](https://img.shields'
  name: Confluent User Notifications (notifications/v1) API
  phrasing_intents:
  - id: listNotificationsV1UserNotifications
    intent: List my notifications
    question: What unread critical notifications do I have?
  - id: getNotificationsV1UserNotification
    intent: Read a notification
    question: What recommended actions come with a particular notification?
  - id: updateNotificationsV1UserNotification
    intent: Mark a notification read or unread
    question: How do I mark a single notification as read?
  - id: markAllNotificationsV1UserNotifications
    intent: Mark many notifications read or unread
    question: Can I mark all my notifications as read at once?
  - id: getNotificationsV1UserNotificationsSummary
    intent: Get a summary of my notifications
    question: How many notifications do I have overall?
  phrasing_ops: 5
  slug: confluent-user-notifications-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `User` objects represent individuals who may access'
  name: Confluent Users (iam/v2) API
  phrasing_intents:
  - id: listIamV2Users
    intent: List users in the organization
    question: Who are all the users in my Confluent Cloud organization?
  - id: getIamV2User
    intent: Get a user
    question: What email and auth method does a particular user have?
  - id: updateIamV2User
    intent: Update a user's profile
    question: Can I change a user's full name?
  - id: deleteIamV2User
    intent: Delete a user and their resources
    question: Does deleting a user also remove their cloud API keys?
  - id: update_auth_typeIamV2User
    intent: Change a user's authentication method
    question: How do I switch a user between SSO and password login?
  phrasing_ops: 5
  slug: confluent-users-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '![generally-available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%230074A2) Version 2 of the Metrics API adds the ability to query metrics for Kafka Connect, ksqlDB, and Sch'
  name: Confluent Version 2 API
  phrasing_intents:
  - id: getV2MetricsByDatasetDescriptorsMetrics
    intent: List the metrics available in a dataset
    question: Which metrics can I query in the Confluent Cloud metrics dataset?
  - id: getV2MetricsByDatasetDescriptorsResources
    intent: List the resource types a dataset has metrics for
    question: What kinds of resources does a metrics dataset report on?
  - id: postV2MetricsByDatasetQuery
    intent: Query time-series metric values
    question: How do I get hourly bytes received for my Kafka cluster over the last day?
  - id: getV2MetricsByDatasetExport
    intent: Export current metrics for Prometheus scraping
    question: How can I scrape Confluent Cloud metrics into Prometheus or another OpenMetrics tool?
  - id: postV2MetricsByDatasetAttributes
    intent: Enumerate the label values for a metric
    question: Which topic names currently show up as label values for a metric?
  - id: getV2MetricsByDatasetDiscovery
    intent: Discover Prometheus scrape targets
    question: Can Prometheus automatically discover which of my Confluent Cloud resources to scrape?
  phrasing_ops: 6
  slug: confluent-version-2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: The ACLs API from Confluent — 1 operation(s) for acls.
  name: Confluent AC Ls API
  phrasing_intents:
  - id: listAcls
    intent: List ACLs on a Kafka cluster
    question: Which access control rules are set on my Kafka cluster?
  - id: createAcl
    intent: Create an ACL on a Kafka cluster
    question: Can I grant a service account permission to read a topic?
  phrasing_ops: 2
  slug: confluent-acls-api
artifact_total: 160
asyncapis:
- description: ''
  name: Confluent Webhooks
  slug: confluent-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs API
  slug: open-confluent-acls-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs API Keys API
  slug: open-confluent-api-keys-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs Clusters API
  slug: open-confluent-clusters-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs Consumer Groups API
  slug: open-confluent-consumer-groups-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs Environments API
  slug: open-confluent-environments-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs Partitions API
  slug: open-confluent-partitions-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs Service Accounts API
  slug: open-confluent-service-accounts-api
- collection_type: open
  name: Confluent Cloud Kafka REST ACLs Topics API
  slug: open-confluent-topics-api
- collection_type: open
  name: Confluent Cloud Kafka REST API
  slug: open-confluent
common:
- group: company
  title: ''
  type: Website
  url: https://www.confluent.io/
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/capabilities/confluent-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/confluent-capability-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/overlays/confluent-cloud-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluent-cloud-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/overlays/confluent-metrics-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluent-metrics-overlay.yaml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.confluent.io/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.confluent.io/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.confluent.io/cloud/current/api.html
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.confluent.io/cloud/current/get-started/index.html
- group: operate
  title: ''
  type: Support
  url: https://developer.confluent.io/community/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confluent.io/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.confluent.io/confluent-cloud/tryfree/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confluent.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confluent.io/legal/confluent-privacy-notice/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.confluent.cloud/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/lifecycle/confluent-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/confluent-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/lifecycle/confluent-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/confluent-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/changelog/confluent-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/confluent-changelog.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/security/confluent-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/confluent-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/security/confluent-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/confluent-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.confluent.io/trust-and-security/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/conformance/confluent-conformance.yml
  title: ''
  type: Conformance
  url: conformance/confluent-conformance.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/packages/confluent-packages.yml
  title: ''
  type: Packages
  url: packages/confluent-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/packages/confluent-packages.yml
  title: ''
  type: SDKs
  url: packages/confluent-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/cli/confluent-cli.yml
  title: ''
  type: CLI
  url: cli/confluent-cli.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/sandbox/confluent-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/confluent-sandbox.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/conventions/confluent-conventions.yml
  title: ''
  type: Conventions
  url: conventions/confluent-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/errors/confluent-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/confluent-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/data-model/confluent-data-model.yml
  title: ''
  type: DataModel
  url: data-model/confluent-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/asyncapi/confluent-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/confluent-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/well-known/confluent-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/confluent-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/well-known/confluent-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/confluent-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/llms/confluent-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/confluent-llms.txt
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/plans/confluent-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/confluent-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/rate-limits/confluent-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/confluent-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/finops/confluent-finops.yml
  title: ''
  type: FinOps
  url: finops/confluent-finops.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/scopes/confluent-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/confluent-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/agentic-access/confluent-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/security/confluent-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/security/confluent-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/confluent-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/authentication/confluent-authentication.yml
  title: ''
  type: Authentication
  url: authentication/confluent-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/confluentinc/agent-skills
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/confluentinc
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/confluent
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.confluent.io/llms.txt
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/feed/
created: '2025-08-19'
description: Stream, connect, process, and govern your data with an all-in-one, real-time platform from the pioneer in data streaming. Build faster, scale smarter, and turn data chaos into instantly accessible and usable data products with the market leading Data Streaming Platform.
finops:
- name: Confluent Finops
  service_category: API
  slug: confluent-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent.png
layout: provider
mcp_servers:
- description: 'Confluent ships TWO distinct MCP products. The managed servers are remote HTTPS endpoints an agent can POST to today, governed by the caller''s existing Confluent Cloud RBAC. The open-source server is '
  name: Confluent MCP Server
  slug: confluent-mcp-server
modified: '2026-08-27'
name: Confluent
nav: Providers
network: true
overview: 'Confluent publishes 127 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Clusters API, Consumer Groups API, and 124 more. Tagged areas include Data Streaming, Apache Kafka, Event Streaming, Stream Processing, and Schema Registry.


  The Confluent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Confluent''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 39 more developer resources.'
plans:
- name: Confluent Plans Pricing
  plan_count: 5
  slug: confluent-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 6
  name: Confluent Rate Limits
  slug: confluent-rate-limits
scopes:
- name: Confluent Scopes
  scope_count: 5
  slug: confluent-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: exemplar
  composite: 82.6
  coverage:
    artifact_dirs: 28
    catalog_earned: 62.0
    catalog_earned_first_party: 24.0
    catalog_gap: 53.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 61.6
    developer_ergonomics: 85.7
    discoverability: 71.7
    operational_transparency: 92.1
  previous_composite: 82.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 125
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/confluent/refs/heads/main/screenshots/confluent-2026-06-20T174900.png
security:
- kind: authentication
  name: Confluent Authentication
  slug: confluent-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Confluent Domain Security
  slug: confluent-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Confluent Vulnerability Disclosure
  slug: confluent-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Confluent Trust Center
  slug: confluent-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO 27001, ISO 27701, PCI DSS, CSA STAR Level 2, TISAX
skill_count: 12
skills:
- name: Bad_Frontmatter
  slug: bad-frontmatter
- name: confluent-cloud-cdc-tableflow
  slug: confluent-cloud-cdc-tableflow
- name: confluent-skill-creator
  slug: confluent-skill-creator
- name: confluent-skill-reviewer
  slug: confluent-skill-reviewer
- name: developing-kafka-python-client
  slug: developing-kafka-python-client
- name: flink-udf
  slug: flink-udf
- name: good-skill
  slug: good-skill
- name: inlined-refs
  slug: inlined-refs
- name: kafka-schema-registry
  slug: kafka-schema-registry
- name: kafka-streams-programming
  slug: kafka-streams-programming
- name: stale-expectations
  slug: stale-expectations
- name: trigger-overlap
  slug: trigger-overlap
slug: confluent
tags:
- Data Streaming
- Apache Kafka
- Event Streaming
- Stream Processing
- Schema Registry
- Apache Flink
- Data Integration
- Connectors
- Data Governance
- Real-Time Data
- Messaging
- Cloud Infrastructure
website: https://www.confluent.io/
---

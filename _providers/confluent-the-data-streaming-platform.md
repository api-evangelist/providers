---
access_model:
  confidence: high
  gated: none
  gated_source:
  - onboarding
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 50.5
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 259
  human_in_the_loop: 5
  name: Confluent The Data Streaming Platform Agentic Access
  operation_count: 504
  slug: confluent-the-data-streaming-platform-agentic-access
  summary_line: 504 operations · 259 acting · 5 human-in-the-loop
api_count: 2
apis:
- description: The Kafka REST API (Confluent REST Proxy in self-managed deployments, Kafka REST in Cloud) provides HTTP access to Apache Kafka topics, consumers, partitions, brokers, and ACLs. Clients without a nati
  name: Confluent Kafka REST API
  slug: kafka-rest-api
- description: The Schema Registry REST API stores and serves Avro, JSON Schema, and Protobuf schemas with versioning and compatibility enforcement. It is available both as a managed Confluent Cloud service and as a
  name: Confluent Schema Registry REST API
  slug: schema-registry-api
- description: The Kafka Connect REST API manages connectors, tasks, and worker configuration. Operators use it to deploy, configure, pause, resume, and delete source and sink connectors, inspect task status, and re
  name: Kafka Connect REST API
  slug: connect-rest-api
- description: The ksqlDB REST API exposes ksqlDB, Confluent's streaming SQL engine, over HTTP. Clients submit streaming SQL statements, query streams and tables (push and pull queries), and inspect server status.
  name: ksqlDB REST API
  slug: ksqldb-rest-api
- description: The Confluent Cloud for Apache Flink REST API manages Flink compute pools, statements, and workspaces for stateful stream processing on Confluent Cloud. It is part of the Confluent Cloud REST surface.
  name: Confluent Cloud for Apache Flink REST API
  slug: flink-rest-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AccessPoint objects represent network connections i'
  name: Confluent | the Data Streaming Platform Access Points (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1AccessPoints
    intent: List access points in an environment
    question: Which network access points exist in my environment?
  - id: createNetworkingV1AccessPoint
    intent: Create a network access point
    question: How do I create an access point on a gateway in Confluent Cloud?
  - id: getNetworkingV1AccessPoint
    intent: Get an access point
    question: What is the status of one of my access points?
  - id: updateNetworkingV1AccessPoint
    intent: Update an access point
    question: How do I rename or change the configuration of an access point?
  - id: deleteNetworkingV1AccessPoint
    intent: Delete an access point
    question: How do I remove an access point I no longer need?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-access-points-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform ACL (v3) API
  phrasing_intents:
  - id: batchCreateKafkaAcls
    intent: Create several Kafka ACLs at once
    question: Can I create many Kafka ACLs in a single request?
  - id: getKafkaAcls
    intent: Search Kafka ACLs
    question: Which ACLs grant a given principal access in my cluster?
  - id: createKafkaAcls
    intent: Create a Kafka ACL
    question: How do I grant a principal read access to a topic with an ACL?
  - id: deleteKafkaAcls
    intent: Delete matching Kafka ACLs
    question: Can I revoke every ACL matching a resource and operation in one call?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-acl-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Agent` models an AI agent that uses a specified model, prompt, and set of tool'
  name: Confluent | the Data Streaming Platform Agents (sql/v1) API
  phrasing_intents:
  - id: listSqlv1Agents
    intent: List Flink SQL agents in an environment
    question: Which AI agents are defined in my Flink SQL environment?
  - id: createSqlv1Agent
    intent: Create a Flink SQL agent
    question: How do I create an agent in a Flink SQL database backed by a Kafka cluster?
  - id: getSqlv1Agent
    intent: Get a Flink SQL agent
    question: What model and prompt is a specific Flink SQL agent using?
  - id: updateSqlv1Agent
    intent: Alter a Flink SQL agent
    question: Can I change an existing agent's model or prompt?
  - id: deleteSqlv1Agent
    intent: Delete a Flink SQL agent
    question: How do I remove an agent from a Flink SQL database?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-agents-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ApiKey` objects represent access to different part'
  name: Confluent | the Data Streaming Platform API Keys (iam/v2) API
  phrasing_intents:
  - id: listIamV2ApiKeys
    intent: List API keys
    question: Which API keys exist in my Confluent Cloud organization?
  - id: createIamV2ApiKey
    intent: Create an API key
    question: How do I create an API key for a service account?
  - id: getIamV2ApiKey
    intent: Read an API key
    question: Who owns a given API key and what resource is it for?
  - id: updateIamV2ApiKey
    intent: Update an API key
    question: Can I change the display name or description of an API key?
  - id: deleteIamV2ApiKey
    intent: Delete an API key
    question: How do I revoke an API key that leaked?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-api-keys-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A `quota` object represents a quota configuration f'
  name: Confluent | the Data Streaming Platform Applied Quotas (service-quota/v1) API
  phrasing_intents:
  - id: listServiceQuotaV1AppliedQuotas
    intent: List applied service quotas
    question: What service quotas apply to my organization or environment?
  - id: getServiceQuotaV1AppliedQuota
    intent: Get one applied quota
    question: What is the current limit for a particular quota code?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-applied-quotas-service-quota-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Catalog Integration represents configuration rela'
  name: Confluent | the Data Streaming Platform Catalog Integrations (tableflow/v1) API
  phrasing_intents:
  - id: listTableflowV1CatalogIntegrations
    intent: List Tableflow catalog integrations
    question: Which external catalogs is Tableflow publishing tables to for my cluster?
  - id: createTableflowV1CatalogIntegration
    intent: Create a Tableflow catalog integration
    question: How do I connect Tableflow to an external data catalog?
  - id: getTableflowV1CatalogIntegration
    intent: Get a Tableflow catalog integration
    question: What is the status of a particular Tableflow catalog integration?
  - id: updateTableflowV1CatalogIntegration
    intent: Update a Tableflow catalog integration
    question: Can I change the settings of an existing Tableflow catalog integration?
  - id: deleteTableflowV1CatalogIntegration
    intent: Delete a Tableflow catalog integration
    question: How do I stop Tableflow from publishing to an external catalog?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-catalog-integrations-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `CertificateAuthority` objects represent signing ce'
  name: Confluent | the Data Streaming Platform Certificate Authorities (iam/v2) API
  phrasing_intents:
  - id: listIamV2CertificateAuthorities
    intent: List certificate authorities for mTLS
    question: Which certificate authorities are registered for mTLS in my organization?
  - id: createIamV2CertificateAuthority
    intent: Register a certificate authority
    question: How do I add a certificate authority so clients can authenticate with mTLS?
  - id: getIamV2CertificateAuthority
    intent: Get a certificate authority
    question: What certificate chain and CRL settings does one of my CAs have?
  - id: updateIamV2CertificateAuthority
    intent: Update a certificate authority
    question: How do I rotate the certificate chain on an existing certificate authority?
  - id: deleteIamV2CertificateAuthority
    intent: Delete a certificate authority
    question: How do I remove a certificate authority I no longer trust?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-certificate-authorities-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Identitypool` objects represent workload identitie'
  name: Confluent | the Data Streaming Platform Certificate Identity Pools (iam/v2) API
  phrasing_intents:
  - id: listIamV2CertificateIdentityPools
    intent: List certificate identity pools
    question: Which certificate identity pools belong to my certificate authority?
  - id: createIamV2CertificateIdentityPool
    intent: Create a certificate identity pool
    question: How do I map mTLS client certificates to a principal with an identity pool?
  - id: getIamV2CertificateIdentityPool
    intent: Get a certificate identity pool
    question: What filter and principal does a certificate identity pool use?
  - id: updateIamV2CertificateIdentityPool
    intent: Update a certificate identity pool
    question: Can I change the certificate filter on an existing identity pool?
  - id: deleteIamV2CertificateIdentityPool
    intent: Delete a certificate identity pool
    question: How do I remove a certificate identity pool from a certificate authority?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-certificate-identity-pools-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ClientQuota` objects represent Client Quotas you c'
  name: Confluent | the Data Streaming Platform Client Quotas (kafka-quotas/v1) API
  phrasing_intents:
  - id: listKafkaQuotasV1ClientQuotas
    intent: List client quotas on a cluster
    question: Which client throughput quotas are set on my Kafka cluster?
  - id: createKafkaQuotasV1ClientQuota
    intent: Create a client quota
    question: How do I limit the throughput of a specific client application?
  - id: getKafkaQuotasV1ClientQuota
    intent: Read a client quota
    question: What throughput limits does one client quota enforce?
  - id: updateKafkaQuotasV1ClientQuota
    intent: Update a client quota
    question: Can I raise the throughput limit on an existing client quota?
  - id: deleteKafkaQuotasV1ClientQuota
    intent: Delete a client quota
    question: Can I remove a quota so a client is no longer throttled?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-client-quotas-kafka-quotas-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Cluster Linking (v3) API
  phrasing_intents:
  - id: listKafkaLinks
    intent: List cluster links on a destination cluster
    question: Which cluster links are set up on my destination Kafka cluster?
  - id: createKafkaLink
    intent: Create a cluster link
    question: How do I set up a cluster link to replicate topics from another Kafka cluster?
  - id: getKafkaLink
    intent: Describe a cluster link
    question: What are the details of a specific cluster link, including its link ID?
  - id: deleteKafkaLink
    intent: Delete a cluster link
    question: How do I remove a cluster link I no longer need?
  - id: listKafkaLinkConfigs
    intent: List a cluster link's configs
    question: What configuration settings does my cluster link currently have?
  - id: getKafkaLinkConfigs
    intent: Get one cluster link config value
    question: What is the current value of a single setting on my cluster link?
  - id: updateKafkaLinkConfig
    intent: Change one cluster link config
    question: How do I change a single setting on an existing cluster link?
  - id: deleteKafkaLinkConfig
    intent: Reset a cluster link config to default
    question: How do I put a cluster link setting back to its default value?
  phrasing_ops: 20
  slug: confluent-the-data-streaming-platform-cluster-linking-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Cluster (v3) API
  phrasing_intents:
  - id: getKafkaCluster
    intent: Get a Kafka cluster
    question: What are the details of my Kafka cluster, like its controller and brokers?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-cluster-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Apache Kafka Clusters '
  name: Confluent | the Data Streaming Platform Clusters (cmk/v2) API
  phrasing_intents:
  - id: listCmkV2Clusters
    intent: List Kafka clusters
    question: Which Kafka clusters exist in my Confluent Cloud environment?
  - id: createCmkV2Cluster
    intent: Create a Kafka cluster
    question: How do I provision a new Kafka cluster through the API?
  - id: getCmkV2Cluster
    intent: Get a Kafka cluster
    question: What is the bootstrap endpoint and status of one of my Kafka clusters?
  - id: updateCmkV2Cluster
    intent: Update a Kafka cluster
    question: Can I rename a Kafka cluster or change its capacity after creation?
  - id: deleteCmkV2Cluster
    intent: Delete a Kafka cluster
    question: How do I tear down a Kafka cluster I no longer use?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-clusters-cmk-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cluster` represents a ksqlDB runtime that you can '
  name: Confluent | the Data Streaming Platform Clusters (ksqldbcm/v2) API
  phrasing_intents:
  - id: listKsqldbcmV2Clusters
    intent: List ksqlDB clusters
    question: Which ksqlDB clusters are running in my environment?
  - id: createKsqldbcmV2Cluster
    intent: Create a ksqlDB cluster
    question: How do I spin up a new ksqlDB cluster?
  - id: getKsqldbcmV2Cluster
    intent: Read a ksqlDB cluster
    question: Is my ksqlDB cluster provisioned yet?
  - id: deleteKsqldbcmV2Cluster
    intent: Delete a ksqlDB cluster
    question: Can I delete a ksqlDB cluster I no longer use?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-clusters-ksqldbcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Clusters on Confluent Cloud.'
  name: Confluent | the Data Streaming Platform Clusters (srcm/v2) API
  phrasing_intents:
  - id: listSrcmV2Clusters
    intent: List Schema Registry clusters
    question: Which Schema Registry clusters exist in my environment?
  - id: createSrcmV2Cluster
    intent: Create a Schema Registry cluster
    question: How do I enable Schema Registry for an environment?
  - id: getSrcmV2Cluster
    intent: Get a Schema Registry cluster
    question: What is the endpoint of my Schema Registry cluster?
  - id: updateSrcmV2Cluster
    intent: Update a Schema Registry cluster
    question: How do I change the package on my Schema Registry cluster?
  - id: deleteSrcmV2Cluster
    intent: Delete a Schema Registry cluster
    question: How do I remove the Schema Registry cluster from an environment?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-clusters-srcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Cluste'
  name: Confluent | the Data Streaming Platform Clusters (srcm/v3) API
  phrasing_intents:
  - id: listSrcmV3Clusters
    intent: List Schema Registry clusters
    question: Which Schema Registry clusters are in my environment?
  - id: getSrcmV3Cluster
    intent: Get a Schema Registry cluster
    question: What is the endpoint and package of a Schema Registry cluster?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-clusters-srcm-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to test schema compatibility. Rela'
  name: Confluent | the Data Streaming Platform Compatibility (v1) API
  phrasing_intents:
  - id: testCompatibilityBySubjectName
    intent: Test a schema against one subject version
    question: Is my new schema compatible with a specific version of a subject?
  - id: testCompatibilityForSubject
    intent: Test a schema against all versions of a subject
    question: Would registering this schema break compatibility with the subject's existing versions?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-compatibility-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Compute Pool represents a set of compute resource'
  name: Confluent | the Data Streaming Platform Compute Pools (fcpm/v2) API
  phrasing_intents:
  - id: listFcpmV2ComputePools
    intent: List Flink compute pools
    question: Which Flink compute pools exist in my environment?
  - id: createFcpmV2ComputePool
    intent: Create a Flink compute pool
    question: How do I provision a new compute pool for running Flink statements?
  - id: getFcpmV2ComputePool
    intent: Get a Flink compute pool
    question: What is the status and size of a particular compute pool?
  - id: updateFcpmV2ComputePool
    intent: Update a Flink compute pool
    question: Can I resize an existing compute pool or change its name?
  - id: deleteFcpmV2ComputePool
    intent: Delete a Flink compute pool
    question: How do I tear down a compute pool I no longer need?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-compute-pools-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to manage and query schema compati'
  name: Confluent | the Data Streaming Platform Config (v1) API
  phrasing_intents:
  - id: getClusterConfig
    intent: Get Schema Registry cluster config
    question: Where can I see the Schema Registry cluster-level config information?
  - id: getSubjectLevelConfig
    intent: Get a subject's compatibility settings
    question: What compatibility level is set for a specific schema subject?
  - id: updateSubjectLevelConfig
    intent: Set a subject's compatibility level
    question: How do I change the compatibility level for just one subject?
  - id: deleteSubjectConfig
    intent: Revert a subject to the global compatibility
    question: How do I remove a subject-level compatibility override?
  - id: getTopLevelConfig
    intent: Get the global compatibility level
    question: What is the global compatibility level for my Schema Registry?
  - id: updateTopLevelConfig
    intent: Set the global compatibility level
    question: How do I change the default compatibility level for every subject?
  - id: deleteTopLevelConfig
    intent: Reset the global compatibility level
    question: Can I clear the global compatibility setting and go back to the default?
  phrasing_ops: 7
  slug: confluent-the-data-streaming-platform-config-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Configs (v3) API
  phrasing_intents:
  - id: listKafkaClusterConfigs
    intent: List a cluster's dynamic broker configs
    question: Which broker settings have been dynamically overridden on my Kafka cluster?
  - id: updateKafkaClusterConfigs
    intent: Change several broker configs at once
    question: How do I update multiple cluster-wide broker settings in one request?
  - id: getKafkaClusterConfig
    intent: Get one dynamic broker config
    question: What is the current value of a specific broker setting on my cluster?
  - id: updateKafkaClusterConfig
    intent: Set a single broker config value
    question: How do I change just one cluster-wide broker setting?
  - id: deleteKafkaClusterConfig
    intent: Reset a broker config to its default
    question: How do I put a broker setting back to its default value?
  - id: listKafkaTopicConfigs
    intent: List a topic's configs
    question: What configuration settings does one of my Kafka topics have?
  - id: updateKafkaTopicConfigBatch
    intent: Change several topic configs at once
    question: How do I update multiple settings on a topic in one call?
  - id: getKafkaTopicConfig
    intent: Get one topic config value
    question: What is a single config value, like retention.ms, set to on my topic?
  phrasing_ops: 17
  slug: confluent-the-data-streaming-platform-configs-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connect Artifact` objects represent collection of '
  name: Confluent | the Data Streaming Platform Connect Artifacts (cam/v1) API
  phrasing_intents:
  - id: listCamV1ConnectArtifacts
    intent: List Connect artifacts
    question: Which custom Connect artifacts have I uploaded to an environment?
  - id: createCamV1ConnectArtifact
    intent: Register a Connect artifact
    question: How do I register a connector archive I uploaded as a Connect artifact?
  - id: getCamV1ConnectArtifact
    intent: Get a Connect artifact
    question: What is the status of a Connect artifact I uploaded?
  - id: deleteCamV1ConnectArtifact
    intent: Delete a Connect artifact
    question: How do I delete a Connect artifact I no longer need?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-connect-artifacts-cam-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `ConnectCluster` object represent Confluent Platform Connect clusters registere'
  name: Confluent | the Data Streaming Platform Connect Clusters (usm/v1) API
  phrasing_intents:
  - id: listUsmV1ConnectClusters
    intent: List registered Connect clusters
    question: Which self-managed Connect clusters are registered with Unified Stream Manager?
  - id: createUsmV1ConnectCluster
    intent: Register a Connect cluster
    question: How do I register a Confluent Platform Connect cluster with Confluent Cloud?
  - id: getUsmV1ConnectCluster
    intent: Get a registered Connect cluster
    question: What Kafka cluster and region is a registered Connect cluster tied to?
  - id: deleteUsmV1ConnectCluster
    intent: Deregister a Connect cluster
    question: How do I deregister a Connect cluster from Unified Stream Manager?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-connect-clusters-usm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connection` represents a core resource used to mod'
  name: Confluent | the Data Streaming Platform Connections (sql/v1) API
  phrasing_intents:
  - id: listSqlv1Connections
    intent: List Flink SQL connections
    question: Which Flink SQL connections are set up in my environment?
  - id: createSqlv1Connection
    intent: Create a Flink SQL connection
    question: How do I create a connection so Flink SQL can reach an external service?
  - id: getSqlv1Connection
    intent: Read a Flink SQL connection
    question: What endpoint and type does one Flink connection use?
  - id: deleteSqlv1Connection
    intent: Delete a Flink SQL connection
    question: Can I remove a Flink SQL connection I no longer use?
  - id: updateSqlv1Connection
    intent: Update a Flink SQL connection
    question: Can I change the endpoint or credentials of an existing Flink connection?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-connections-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed Connectors or Custom Connectors in '
  name: Confluent | the Data Streaming Platform Connectors (connect/v1) API
  phrasing_intents:
  - id: listConnectv1Connectors
    intent: List connector names in a Kafka cluster
    question: Which managed connectors are active on my Kafka cluster?
  - id: createConnectv1Connector
    intent: Create a managed connector
    question: How do I create a fully managed connector on Confluent Cloud?
  - id: listConnectv1ConnectorsWithExpansions
    intent: List connectors with status and details
    question: Can I get the status and config of every connector in one call?
  - id: getConnectv1ConnectorConfig
    intent: Read a connector's configuration
    question: What configuration settings is a connector currently running with?
  - id: createOrUpdateConnectv1ConnectorConfig
    intent: Create or update a connector's configuration
    question: Can I change a connector's configuration in place without deleting it?
  - id: readConnectv1Connector
    intent: Read a connector's details
    question: What type and tasks does a specific connector have?
  - id: deleteConnectv1Connector
    intent: Delete a connector
    question: What happens to running tasks when I delete a connector?
  phrasing_ops: 7
  slug: confluent-the-data-streaming-platform-connectors-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Consumer Group (v3) API
  phrasing_intents:
  - id: listKafkaConsumerGroups
    intent: List consumer groups on a cluster
    question: Which consumer groups are reading from my Kafka cluster?
  - id: getKafkaConsumerGroup
    intent: Get a consumer group
    question: What state is a particular consumer group in?
  - id: listKafkaConsumers
    intent: List consumers in a group
    question: Which consumers are members of a consumer group right now?
  - id: getKafkaConsumerGroupLagSummary
    intent: Summarize a consumer group's lag
    question: How far behind is my consumer group overall?
  - id: listKafkaConsumerLags
    intent: List per-partition lag for a group
    question: Which partitions is my consumer group lagging on?
  - id: getKafkaConsumerLag
    intent: Get lag on one partition
    question: How far behind is my consumer group on one specific topic partition?
  - id: getKafkaConsumer
    intent: Get one consumer in a group
    question: What client ID and host is a specific consumer running on?
  phrasing_ops: 7
  slug: confluent-the-data-streaming-platform-consumer-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerSharedResource` object contains details of'
  name: Confluent | the Data Streaming Platform Consumer Shared Resources (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ConsumerSharedResources
    intent: List resources shared with me
    question: Which topics have other organizations shared with me through Stream Sharing?
  - id: getCdxV1ConsumerSharedResource
    intent: Get a resource shared with me
    question: What details did the provider publish about a resource shared with me?
  - id: imageCdxV1ConsumerSharedResource
    intent: Get the image on a resource shared with me
    question: Can I download the provider's logo for a resource shared with me?
  - id: networkCdxV1ConsumerSharedResource
    intent: Get network config for a shared resource
    question: What network settings do I need to reach a resource shared with me?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-consumer-shared-resources-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerShare` object respresents the share that y'
  name: Confluent | the Data Streaming Platform Consumer Shares (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ConsumerShares
    intent: List stream shares I've received
    question: Which stream shares have been shared with me as a consumer?
  - id: getCdxV1ConsumerShare
    intent: Get a consumer share
    question: What resource and provider details does one consumer share have?
  - id: deleteCdxV1ConsumerShare
    intent: Delete a consumer share
    question: How do I stop consuming a stream share someone gave me?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-consumer-shares-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to retrieve information about sche'
  name: Confluent | the Data Streaming Platform Contexts (v1) API
  phrasing_intents:
  - id: listContexts
    intent: List Schema Registry contexts
    question: Which schema contexts exist in my registry?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-contexts-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cost` objects represent the aggregated billing cos'
  name: Confluent | the Data Streaming Platform Costs (billing/v1) API
  phrasing_intents:
  - id: listBillingV1Costs
    intent: List costs for a date range
    question: How much did I spend on Confluent Cloud last month?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-costs-billing-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Custom Code Logging API EA](https://img.shield'
  name: Confluent | the Data Streaming Platform Custom Code Loggings (ccl/v1) API
  phrasing_intents:
  - id: listCclV1CustomCodeLoggings
    intent: List custom code logging configs
    question: Which custom code logging destinations exist in my environment?
  - id: createCclV1CustomCodeLogging
    intent: Create a custom code logging config
    question: How do I send logs from my custom code to a Kafka topic?
  - id: getCclV1CustomCodeLogging
    intent: Get a custom code logging config
    question: What destination is a given custom code logging config using?
  - id: updateCclV1CustomCodeLogging
    intent: Update a custom code logging config
    question: Can I change where an existing custom code logging config sends logs?
  - id: deleteCclV1CustomCodeLogging
    intent: Delete a custom code logging config
    question: How do I stop collecting custom code logs?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-custom-code-loggings-ccl-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPluginVersion objects represent Custom'
  name: Confluent | the Data Streaming Platform Custom Connect Plugin Versions (ccpm/v1) API
  phrasing_intents:
  - id: listCcpmV1CustomConnectPluginVersions
    intent: List versions of a custom connector plugin
    question: Which versions of my custom connector plugin have been uploaded?
  - id: createCcpmV1CustomConnectPluginVersion
    intent: Add a version to a custom connector plugin
    question: How do I upload a new version of my custom connector plugin?
  - id: getCcpmV1CustomConnectPluginVersion
    intent: Read a custom connector plugin version
    question: What's the status of a particular plugin version?
  - id: deleteCcpmV1CustomConnectPluginVersion
    intent: Delete a custom connector plugin version
    question: Can I delete an old version of my custom plugin?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-custom-connect-plugin-versions-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPlugins objects represent Custom Conne'
  name: Confluent | the Data Streaming Platform Custom Connect Plugins (ccpm/v1) API
  phrasing_intents:
  - id: listCcpmV1CustomConnectPlugins
    intent: List custom connector plugins
    question: Which custom connector plugins have I uploaded to an environment?
  - id: createCcpmV1CustomConnectPlugin
    intent: Create a custom connector plugin
    question: How do I register a custom connector plugin after uploading its archive?
  - id: getCcpmV1CustomConnectPlugin
    intent: Get a custom connector plugin
    question: What versions and cloud does one of my custom plugins have?
  - id: updateCcpmV1CustomConnectPlugin
    intent: Update a custom connector plugin
    question: How do I rename or re-describe a custom connector plugin?
  - id: deleteCcpmV1CustomConnectPlugin
    intent: Delete a custom connector plugin
    question: How do I remove a custom connector plugin I no longer need?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-custom-connect-plugins-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectorPlugins objects represent Custom Con'
  name: Confluent | the Data Streaming Platform Custom Connector Plugins (connect/v1) API
  phrasing_intents:
  - id: listConnectV1CustomConnectorPlugins
    intent: List custom connector plugins
    question: Which custom connector plugins have I uploaded to Confluent Cloud?
  - id: createConnectV1CustomConnectorPlugin
    intent: Register a custom connector plugin
    question: How do I register my own connector plugin after uploading its archive?
  - id: getConnectV1CustomConnectorPlugin
    intent: Get a custom connector plugin
    question: What connector class and sensitive properties does one custom plugin declare?
  - id: updateConnectV1CustomConnectorPlugin
    intent: Update a custom connector plugin
    question: Can I change the name or documentation link of an existing custom plugin?
  - id: deleteConnectV1CustomConnectorPlugin
    intent: Delete a custom connector plugin
    question: How do I remove a custom connector plugin I uploaded?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-custom-connector-plugins-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of supported runtime languages for Custom Conn'
  name: Confluent | the Data Streaming Platform Custom Connector Runtimes (connect/v1) API
  phrasing_intents:
  - id: listConnectV1CustomConnectorRuntimes
    intent: List custom connector runtimes
    question: Which runtimes are available for running custom connectors?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-custom-connector-runtimes-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Data Encryption Keys (v1) API
  phrasing_intents:
  - id: getDekSubjects
    intent: List DEK subjects under a KEK
    question: Which subjects have data encryption keys under a given key encryption key?
  - id: createDek
    intent: Create a data encryption key
    question: How do I create a data encryption key for a subject under my KEK?
  - id: deleteDekVersions
    intent: Delete all versions of a DEK
    question: How do I delete every version of a subject's data encryption key?
  - id: getDek
    intent: Get the latest DEK for a subject
    question: What is the current data encryption key for a subject?
  - id: deleteDekVersion
    intent: Delete one DEK version
    question: Can I delete a single version of a DEK and keep the others?
  - id: getDekByVersion
    intent: Get a specific DEK version
    question: How can I retrieve an older version of a subject's data encryption key?
  - id: getDekVersions
    intent: List versions of a DEK
    question: What versions exist for a subject's data encryption key?
  - id: undeleteDekVersion
    intent: Restore one deleted DEK version
    question: How do I bring back a single DEK version I soft-deleted?
  phrasing_ops: 9
  slug: confluent-the-data-streaming-platform-data-encryption-keys-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add, remove, and update DNS forwarder for your gate'
  name: Confluent | the Data Streaming Platform DNS Forwarders (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1DnsForwarders
    intent: List DNS forwarders in an environment
    question: Which DNS forwarders are configured in my Confluent Cloud environment?
  - id: createNetworkingV1DnsForwarder
    intent: Create a DNS forwarder
    question: How do I forward DNS queries for my private domains from a Confluent network?
  - id: getNetworkingV1DnsForwarder
    intent: Read a DNS forwarder
    question: Is my DNS forwarder provisioned and ready?
  - id: updateNetworkingV1DnsForwarder
    intent: Update a DNS forwarder
    question: Can I change the forwarded domains on an existing DNS forwarder?
  - id: deleteNetworkingV1DnsForwarder
    intent: Delete a DNS forwarder
    question: Can I remove a DNS forwarder I no longer need?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-dns-forwarders-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) DNS record objects are associated with Confluent Cl'
  name: Confluent | the Data Streaming Platform DNS Records (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1DnsRecords
    intent: List DNS records
    question: Which private DNS records are configured in my environment?
  - id: createNetworkingV1DnsRecord
    intent: Create a DNS record
    question: How do I add a DNS record that points to a private access point?
  - id: getNetworkingV1DnsRecord
    intent: Get a DNS record
    question: What domain and target does a specific DNS record have?
  - id: updateNetworkingV1DnsRecord
    intent: Update a DNS record
    question: Can I rename or repoint an existing DNS record?
  - id: deleteNetworkingV1DnsRecord
    intent: Delete a DNS record
    question: How do I remove a private DNS record?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-dns-records-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An Endpoint object represents a Fully Qualified Dom'
  name: Confluent | the Data Streaming Platform Endpoints (endpoint/v1) API
  phrasing_intents:
  - id: listEndpointV1Endpoints
    intent: List service endpoints in an environment
    question: What connection endpoints does a service in my environment expose?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-endpoints-endpoint-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent | the Data Streaming Platform Entitlements (partner/v2) API
  phrasing_intents:
  - id: listPartnerV2Entitlements
    intent: List partner entitlements
    question: Which marketplace entitlements have I created as a partner?
  - id: createPartnerV2Entitlement
    intent: Create a partner entitlement
    question: How do I provision an entitlement for a customer as a partner?
  - id: getPartnerV2Entitlement
    intent: Get a partner entitlement
    question: What plan and product is one entitlement on?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-entitlements-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Entity (v1) API
  phrasing_intents:
  - id: createBusinessMetadata
    intent: Bulk attach business metadata to entities
    question: How do I attach business metadata to several topics or schemas in one request?
  - id: updateBusinessMetadata
    intent: Bulk update business metadata on entities
    question: Can I change business metadata values on many catalog entities at once?
  - id: getBusinessMetadata
    intent: List business metadata on an entity
    question: What business metadata is attached to a particular topic or schema?
  - id: deleteBusinessMetadata
    intent: Remove business metadata from an entity
    question: How do I detach one business metadata from a topic in the catalog?
  - id: updateTags
    intent: Bulk update tags on entities
    question: Can I change the attributes of tags already applied to many entities?
  - id: createTags
    intent: Bulk tag entities
    question: How do I tag several topics as PII in one request?
  - id: getByUniqueAttributes
    intent: Get a catalog entity
    question: Can I fetch the full catalog definition of a topic by its qualified name?
  - id: getTags
    intent: List tags on an entity
    question: Which tags are attached to a particular topic?
  phrasing_ops: 10
  slug: confluent-the-data-streaming-platform-entity-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Environment` objects represent an isolated namespa'
  name: Confluent | the Data Streaming Platform Environments (org/v2) API
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
    question: How do I rename an environment?
  - id: deleteOrgV2Environment
    intent: Delete an environment and everything in it
    question: What gets deleted along with an environment?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-environments-org-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Exporters (v1) API
  phrasing_intents:
  - id: listExporters
    intent: List schema exporters
    question: Which schema exporters have been set up in my Schema Registry?
  - id: registerExporter
    intent: Create a schema exporter
    question: How do I start exporting schemas from one Schema Registry to another?
  - id: getExporterInfoByName
    intent: Get a schema exporter's details
    question: What subjects and context does a given schema exporter export?
  - id: updateExporterInfo
    intent: Update a schema exporter's settings
    question: Can I change which subjects an existing schema exporter sends?
  - id: deleteExporter
    intent: Delete a schema exporter
    question: How do I remove a schema exporter I no longer need?
  - id: getExporterStatusByName
    intent: Check a schema exporter's status
    question: Is my schema exporter running, paused or in an error state?
  - id: getExporterConfigByName
    intent: Get a schema exporter's destination config
    question: Which destination Schema Registry URL is my exporter pointing at?
  - id: updateExporterConfigByName
    intent: Change a schema exporter's destination config
    question: Can I point an existing schema exporter at a different destination registry URL?
  phrasing_ops: 11
  slug: confluent-the-data-streaming-platform-exporters-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) FlinkArtifact objects represent Flink Artifacts on '
  name: Confluent | the Data Streaming Platform Flink Artifacts (artifact/v1) API
  phrasing_intents:
  - id: listArtifactV1FlinkArtifacts
    intent: List Flink artifacts
    question: Which Flink UDF artifacts have I uploaded to an environment?
  - id: createArtifactV1FlinkArtifact
    intent: Create a Flink artifact
    question: How do I register a JAR of Flink user-defined functions as an artifact?
  - id: getArtifactV1FlinkArtifact
    intent: Get a Flink artifact
    question: What versions and class does a specific Flink artifact have?
  - id: updateArtifactV1FlinkArtifact
    intent: Update a Flink artifact
    question: Can I change the description or documentation link of a Flink artifact?
  - id: deleteArtifactV1FlinkArtifact
    intent: Delete a Flink artifact
    question: How do I delete a Flink UDF artifact I no longer need?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-flink-artifacts-artifact-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Gateway represents a slice of traffic capacity in'
  name: Confluent | the Data Streaming Platform Gateways (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1Gateways
    intent: List network gateways
    question: Which networking gateways exist in my environment?
  - id: createNetworkingV1Gateway
    intent: Create a network gateway
    question: How do I create an egress or ingress gateway for private networking?
  - id: getNetworkingV1Gateway
    intent: Read a network gateway
    question: Has my gateway finished provisioning?
  - id: updateNetworkingV1Gateway
    intent: Update a network gateway
    question: Can I rename an existing gateway?
  - id: deleteNetworkingV1Gateway
    intent: Delete a network gateway
    question: Can I delete a gateway I'm no longer routing through?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-gateways-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `GroupMapping` objects establish relationships betw'
  name: Confluent | the Data Streaming Platform Group Mappings (iam/v2/sso) API
  phrasing_intents:
  - id: listIamV2SsoGroupMappings
    intent: List SSO group mappings
    question: Which SSO groups are mapped to Confluent Cloud roles?
  - id: createIamV2SsoGroupMapping
    intent: Map an SSO group
    question: How do I map an identity provider group so its members get access?
  - id: getIamV2SsoGroupMapping
    intent: Get an SSO group mapping
    question: What filter does a particular SSO group mapping use?
  - id: updateIamV2SsoGroupMapping
    intent: Update an SSO group mapping
    question: Can I change the filter on an existing SSO group mapping?
  - id: deleteIamV2SsoGroupMapping
    intent: Delete an SSO group mapping
    question: How do I stop an identity provider group from getting access?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-group-mappings-iam-v2-sso-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityPool` objects represent groups of identiti'
  name: Confluent | the Data Streaming Platform Identity Pools (iam/v2) API
  phrasing_intents:
  - id: listIamV2IdentityPools
    intent: List identity pools for an identity provider
    question: Which identity pools are set up under my OAuth identity provider?
  - id: createIamV2IdentityPool
    intent: Create an identity pool
    question: How do I map tokens from my external identity provider to Confluent Cloud access?
  - id: getIamV2IdentityPool
    intent: Get an identity pool
    question: What filter and identity claim does one of my identity pools use?
  - id: updateIamV2IdentityPool
    intent: Update an identity pool
    question: How do I change the claim filter on an existing identity pool?
  - id: deleteIamV2IdentityPool
    intent: Delete an identity pool
    question: How do I remove an identity pool so those external identities lose access?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-identity-pools-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityProvider` objects represent external OAuth'
  name: Confluent | the Data Streaming Platform Identity Providers (iam/v2) API
  phrasing_intents:
  - id: listIamV2IdentityProviders
    intent: List OAuth identity providers
    question: Which OAuth/OIDC identity providers are registered for my organization?
  - id: createIamV2IdentityProvider
    intent: Register an OAuth identity provider
    question: How do I add my OIDC provider so clients can authenticate with OAuth tokens?
  - id: getIamV2IdentityProvider
    intent: Get an OAuth identity provider
    question: What issuer and JWKS URI is a specific identity provider using?
  - id: updateIamV2IdentityProvider
    intent: Update an OAuth identity provider
    question: Can I change the identity claim or description of an existing identity provider?
  - id: deleteIamV2IdentityProvider
    intent: Delete an OAuth identity provider
    question: How do I remove an OAuth identity provider from my org?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-identity-providers-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) You can create an `Integration` to specify how we c'
  name: Confluent | the Data Streaming Platform Integrations (notifications/v1) API
  phrasing_intents:
  - id: createNotificationsV1Integration
    intent: Create a notification integration
    question: How do I send platform notifications to a webhook, Slack or Teams channel?
  - id: listNotificationsV1Integrations
    intent: List notification integrations
    question: Which notification integrations are configured in my Confluent Cloud org?
  - id: getNotificationsV1Integration
    intent: Get a notification integration
    question: What target and settings does one notification integration have?
  - id: updateNotificationsV1Integration
    intent: Update a notification integration
    question: Can I change where an existing notification integration sends alerts?
  - id: deleteNotificationsV1Integration
    intent: Delete a notification integration
    question: How do I stop notifications going to an integration by removing it?
  - id: testNotificationsV1Integration
    intent: Send a test notification
    question: Can I send a test notification to check my webhook or Slack integration works?
  phrasing_ops: 6
  slug: confluent-the-data-streaming-platform-integrations-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Provider Integration` objects represent access to '
  name: Confluent | the Data Streaming Platform Integrations (pim/v1) API
  phrasing_intents:
  - id: listPimV1Integrations
    intent: List provider integrations
    question: Which cloud provider integrations exist in my environment?
  - id: createPimV1Integration
    intent: Create a provider integration
    question: How do I set up a cloud provider integration so connectors can access my account?
  - id: getPimV1Integration
    intent: Get a provider integration
    question: What config and usages does one provider integration have?
  - id: deletePimV1Integration
    intent: Delete a provider integration
    question: How do I remove a cloud provider integration?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-integrations-pim-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/b'
  name: Confluent | the Data Streaming Platform Integrations (pim/v2) API
  phrasing_intents:
  - id: listPimV2Integrations
    intent: List cloud provider integrations
    question: Which cloud provider integrations exist in my environment?
  - id: createPimV2Integration
    intent: Create a cloud provider integration
    question: How do I set up a provider integration so Confluent can access my cloud account?
  - id: getPimV2Integration
    intent: Read a provider integration
    question: What is the current status of one provider integration?
  - id: updatePimV2Integration
    intent: Update a provider integration
    question: Can I rename or reconfigure an existing provider integration?
  - id: deletePimV2Integration
    intent: Delete a provider integration
    question: Can I remove a cloud provider integration I no longer use?
  - id: validatePimV2Integration
    intent: Validate a provider integration setup
    question: Can I test that a provider integration's cloud access is set up correctly before relying on it?
  phrasing_ops: 6
  slug: confluent-the-data-streaming-platform-integrations-pim-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Invitation` objects represent invitations to invit'
  name: Confluent | the Data Streaming Platform Invitations (iam/v2) API
  phrasing_intents:
  - id: listIamV2Invitations
    intent: List user invitations
    question: Which user invitations to my organization are still pending?
  - id: createIamV2Invitation
    intent: Invite a user to the organization
    question: How do I invite a new user to my Confluent Cloud organization?
  - id: getIamV2Invitation
    intent: Get an invitation
    question: Has a specific invitation been accepted or has it expired?
  - id: deleteIamV2Invitation
    intent: Revoke an invitation
    question: How do I cancel an invitation I sent by mistake?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-invitations-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) IP Addresses Related guide: [Use Public Egress IP a'
  name: Confluent | the Data Streaming Platform IP Addresses (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1IpAddresses
    intent: List Confluent Cloud IP addresses
    question: Which public egress IP addresses does Confluent Cloud use so I can allowlist them?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-ip-addresses-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The IP Filter Summary endpoint returns an aggregati'
  name: Confluent | the Data Streaming Platform IP Filter Summaries (iam/v2) API
  phrasing_intents:
  - id: getIamV2IpFilterSummary
    intent: Get an IP filter summary
    question: Which IP filters apply at a given scope?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-ip-filter-summaries-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IP Filter` objects are bindings between IP Groups '
  name: Confluent | the Data Streaming Platform IP Filters (iam/v2) API
  phrasing_intents:
  - id: listIamV2IpFilters
    intent: List IP filters
    question: Which IP filters restrict access to my Confluent Cloud organization?
  - id: createIamV2IpFilter
    intent: Create an IP filter
    question: How do I allow access only from certain IP ranges?
  - id: getIamV2IpFilter
    intent: Read an IP filter
    question: Which IP groups does a given IP filter allow?
  - id: updateIamV2IpFilter
    intent: Update an IP filter
    question: Can I add another IP group to an existing filter?
  - id: deleteIamV2IpFilter
    intent: Delete an IP filter
    question: Can I remove an IP filter to reopen access?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-ip-filters-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Definitions of networks which can be named and refe'
  name: Confluent | the Data Streaming Platform IP Groups (iam/v2) API
  phrasing_intents:
  - id: listIamV2IpGroups
    intent: List IP groups
    question: Which IP groups have I defined for IP filtering?
  - id: createIamV2IpGroup
    intent: Create an IP group
    question: How do I define a set of allowed CIDR blocks for IP filtering?
  - id: getIamV2IpGroup
    intent: Get an IP group
    question: Which CIDR ranges are in a specific IP group?
  - id: updateIamV2IpGroup
    intent: Update an IP group
    question: Can I add or change the CIDR blocks in an existing IP group?
  - id: deleteIamV2IpGroup
    intent: Delete an IP group
    question: How do I remove an IP group I no longer use?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-ip-groups-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `JWKS` objects represent public key sets for a spec'
  name: Confluent | the Data Streaming Platform Jwks (iam/v2) API
  phrasing_intents:
  - id: refreshIamV2JsonWebKeySet
    intent: Refresh an identity provider's JWKS
    question: Is there a way to force Confluent to re-fetch my identity provider's signing keys?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-jwks-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `KafkaCluster` object represent Confluent Platform Kafka clusters registered wi'
  name: Confluent | the Data Streaming Platform Kafka Clusters (usm/v1) API
  phrasing_intents:
  - id: listUsmV1KafkaClusters
    intent: List registered Confluent Platform clusters
    question: Which self-managed Confluent Platform clusters are registered with Unified Stream Manager?
  - id: createUsmV1KafkaCluster
    intent: Register a Confluent Platform cluster
    question: How do I register my self-managed Confluent Platform Kafka cluster with the cloud?
  - id: getUsmV1KafkaCluster
    intent: Get a registered Confluent Platform cluster
    question: What cloud and region hold the metadata for my registered cluster?
  - id: deleteUsmV1KafkaCluster
    intent: Unregister a Confluent Platform cluster
    question: How do I unregister a self-managed cluster from Unified Stream Manager?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-kafka-clusters-usm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Key Encryption Keys (v1) API
  phrasing_intents:
  - id: getKekNames
    intent: List key encryption keys
    question: Which key encryption keys are registered for client-side field encryption?
  - id: createKek
    intent: Register a key encryption key
    question: How do I register a KMS key as a KEK for field-level encryption?
  - id: deleteKek
    intent: Delete a key encryption key
    question: How do I delete a KEK, and can I delete it permanently?
  - id: getKek
    intent: Get a key encryption key
    question: Which KMS key backs a given KEK?
  - id: putKek
    intent: Update a key encryption key
    question: Can I change the KMS properties or documentation on an existing KEK?
  - id: undeleteKek
    intent: Restore a deleted key encryption key
    question: Can I bring back a KEK I soft-deleted?
  - id: testKek
    intent: Test a key encryption key
    question: How can I verify a KEK can actually reach its KMS key?
  phrasing_ops: 7
  slug: confluent-the-data-streaming-platform-key-encryption-keys-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Key` objects represent customer managed keys on de'
  name: Confluent | the Data Streaming Platform Keys (byok/v1) API
  phrasing_intents:
  - id: listByokV1Keys
    intent: List bring-your-own encryption keys
    question: Which self-managed encryption keys have I registered for my clusters?
  - id: createByokV1Key
    intent: Register a bring-your-own encryption key
    question: How do I register my own KMS key to encrypt a dedicated cluster?
  - id: getByokV1Key
    intent: Get a bring-your-own key
    question: Has my self-managed encryption key passed validation?
  - id: updateByokV1Key
    intent: Rename a bring-your-own key
    question: How do I change the display name of a BYOK key?
  - id: deleteByokV1Key
    intent: Delete a bring-your-own key
    question: How do I remove a self-managed encryption key I registered?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-keys-byok-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the lifecycle for a Managed Connec'
  name: Confluent | the Data Streaming Platform Lifecycle (connect/v1) API
  phrasing_intents:
  - id: pauseConnectv1Connector
    intent: Pause a connector
    question: How do I temporarily stop a connector from processing messages?
  - id: resumeConnectv1Connector
    intent: Resume a paused connector
    question: Can I restart message processing on a paused connector?
  - id: restartConnectv1Connector
    intent: Restart a connector and its tasks
    question: Can I restart a failed connector and its tasks?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-lifecycle-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed connectors in Confluent Cloud.'
  name: Confluent | the Data Streaming Platform Managed Connector Plugins (connect/v1) API
  phrasing_intents:
  - id: listConnectv1ConnectorPlugins
    intent: List managed connector plugins
    question: Which fully managed connector plugins can I use on my Kafka cluster?
  - id: validateConnectv1ConnectorPlugin
    intent: Validate a managed connector config
    question: Can I check a connector configuration for errors before creating the connector?
  - id: translateConnectv1ConnectorPlugin
    intent: Translate a self-managed connector config
    question: How do I convert a self-managed connector config into a fully managed one?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-managed-connector-plugins-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTableVersion` represents a specific ve'
  name: Confluent | the Data Streaming Platform Materialized Table Versions (sql/v1) API
  phrasing_intents:
  - id: listSqlv1MaterializedTableVersions
    intent: List versions of a materialized table
    question: What versions exist for one of my Flink materialized tables?
  - id: getSqlv1MaterializedTableVersion
    intent: Get one version of a materialized table
    question: What did a materialized table's definition look like at a specific version?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-materialized-table-versions-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTable` represents a core resource used'
  name: Confluent | the Data Streaming Platform Materialized Tables (sql/v1) API
  phrasing_intents:
  - id: listSqlv1MaterializedTables
    intent: List materialized tables in an environment
    question: Which materialized tables exist in my Flink SQL environment?
  - id: createSqlv1MaterializedTable
    intent: Create a materialized table
    question: How do I create a materialized table from a Flink SQL query?
  - id: getSqlv1MaterializedTable
    intent: Get a materialized table
    question: What query and columns define a specific materialized table?
  - id: updateSqlv1MaterializedTable
    intent: Evolve a materialized table
    question: Can I change the query or compute pool behind an existing materialized table?
  - id: deleteSqlv1MaterializedTable
    intent: Delete a materialized table
    question: How do I drop a materialized table I no longer need?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-materialized-tables-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Modes (v1) API
  phrasing_intents:
  - id: getMode
    intent: Get a subject's Schema Registry mode
    question: Is a subject in READWRITE, READONLY or IMPORT mode?
  - id: updateMode
    intent: Set a subject's Schema Registry mode
    question: How do I make one subject read-only?
  - id: deleteSubjectMode
    intent: Remove a subject's mode override
    question: Can I clear a subject-level mode so it goes back to the global default?
  - id: getTopLevelMode
    intent: Get the global Schema Registry mode
    question: What is the registry-wide mode right now?
  - id: updateTopLevelMode
    intent: Set the global Schema Registry mode
    question: Can I put the entire registry into read-only mode for maintenance?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-modes-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Network Link Enpoint is associated with a Private'
  name: Confluent | the Data Streaming Platform Network Link Endpoints (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1NetworkLinkEndpoints
    intent: List network link endpoints
    question: Which network link endpoints exist in my environment?
  - id: createNetworkingV1NetworkLinkEndpoint
    intent: Create a network link endpoint
    question: How do I connect my network to another network's link service?
  - id: getNetworkingV1NetworkLinkEndpoint
    intent: Get a network link endpoint
    question: Is my network link endpoint ready or still pending?
  - id: updateNetworkingV1NetworkLinkEndpoint
    intent: Update a network link endpoint
    question: Can I rename or redescribe an existing network link endpoint?
  - id: deleteNetworkingV1NetworkLinkEndpoint
    intent: Delete a network link endpoint
    question: How do I remove a network link endpoint?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-network-link-endpoints-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of incoming Network Link Enpoints associated w'
  name: Confluent | the Data Streaming Platform Network Link Service Associations (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1NetworkLinkServiceAssociations
    intent: List network link service associations
    question: Which network link endpoints are associated with my network link service?
  - id: getNetworkingV1NetworkLinkServiceAssociation
    intent: Read a network link service association
    question: What's the state of one network link service association?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-network-link-service-associations-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Network Link Service is associated with a Private L'
  name: Confluent | the Data Streaming Platform Network Link Services (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1NetworkLinkServices
    intent: List network link services
    question: Which network link services exist in my environment?
  - id: createNetworkingV1NetworkLinkService
    intent: Create a network link service
    question: How do I let other networks connect to my network with a network link service?
  - id: getNetworkingV1NetworkLinkService
    intent: Get a network link service
    question: What is the status of my network link service?
  - id: updateNetworkingV1NetworkLinkService
    intent: Update a network link service
    question: How do I change which networks can connect through a link service?
  - id: deleteNetworkingV1NetworkLinkService
    intent: Delete a network link service
    question: How do I remove a network link service?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-network-link-services-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Network` represents a network (VPC) in Confluent C'
  name: Confluent | the Data Streaming Platform Networks (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1Networks
    intent: List networks in an environment
    question: Which Confluent Cloud networks exist in my environment?
  - id: createNetworkingV1Network
    intent: Create a network
    question: How do I create a dedicated network for private connectivity to my clusters?
  - id: getNetworkingV1Network
    intent: Get a network
    question: What is the provisioning phase of a specific network?
  - id: updateNetworkingV1Network
    intent: Update a network
    question: Can I rename an existing network?
  - id: deleteNetworkingV1Network
    intent: Delete a network
    question: How do I delete a network I no longer use?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-networks-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The type of notifications (and their corresponding '
  name: Confluent | the Data Streaming Platform Notification Types (notifications/v1) API
  phrasing_intents:
  - id: getNotificationsV1NotificationType
    intent: Get a notification type
    question: What does a specific notification type cover?
  - id: listNotificationsV1NotificationTypes
    intent: List notification types
    question: Which notification types can I subscribe to?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-notification-types-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) OAuth Token is a [JSON Web Token (JWT)](https://www'
  name: Confluent | the Data Streaming Platform OAuth Tokens (sts/v1) API
  phrasing_intents:
  - id: exchangeStsV1OauthToken
    intent: Exchange an external token for a Confluent token
    question: How do I use a JWT from my own identity provider to call Confluent Cloud APIs?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-oauth-tokens-sts-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the offsets for a Managed Connecto'
  name: Confluent | the Data Streaming Platform Offsets (connect/v1) API
  phrasing_intents:
  - id: getConnectv1ConnectorOffsets
    intent: Get a connector's current offsets
    question: Where in the source system is my connector currently reading from?
  - id: alterConnectv1ConnectorOffsetsRequest
    intent: Alter or reset a connector's offsets
    question: How do I reset or change the offsets of a connector?
  - id: getConnectv1ConnectorOffsetsRequestStatus
    intent: Check an offset change request's status
    question: Did my last request to alter connector offsets finish?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-offsets-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Stream sharing opt in options ## The Opt Ins Model '
  name: Confluent | the Data Streaming Platform Opt Ins (cdx/v1) API
  phrasing_intents:
  - id: getCdxV1OptIn
    intent: Check stream sharing opt-in
    question: Is stream sharing enabled for my organization?
  - id: updateCdxV1OptIn
    intent: Turn stream sharing on or off
    question: How do I enable stream sharing for my organization?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-opt-ins-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `OrgComputePoolConfig` manages compute pool configu'
  name: Confluent | the Data Streaming Platform Org Compute Pool Configs (fcpm/v2) API
  phrasing_intents:
  - id: getFcpmV2OrgComputePoolConfig
    intent: Get the org-wide Flink compute pool config
    question: What is my organization's default Flink compute pool configuration?
  - id: updateFcpmV2OrgComputePoolConfig
    intent: Update the org-wide Flink compute pool config
    question: How do I change the organization-level Flink compute pool configuration?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-org-compute-pool-configs-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Organization` objects represent a customer organiz'
  name: Confluent | the Data Streaming Platform Organizations (org/v2) API
  phrasing_intents:
  - id: listOrgV2Organizations
    intent: List organizations
    question: Which Confluent Cloud organizations can I access?
  - id: getOrgV2Organization
    intent: Get an organization
    question: Is just-in-time user provisioning turned on for my organization?
  - id: updateOrgV2Organization
    intent: Update an organization
    question: How do I rename my organization?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-organizations-org-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent | the Data Streaming Platform Organizations (partner/v2) API
  phrasing_intents:
  - id: getPartnerV2Organization
    intent: Read a customer organization
    question: As a partner, can I view details of one customer organization?
  - id: listPartnerV2Organizations
    intent: List customer organizations
    question: Which customer organizations are under my partner account?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-organizations-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Partition (v3) API
  phrasing_intents:
  - id: listKafkaPartitions
    intent: List a topic's partitions
    question: How many partitions does my Kafka topic have?
  - id: getKafkaPartition
    intent: Get a topic partition
    question: Which broker leads a specific partition of my topic?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-partition-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove VPC/VNet peering connections between '
  name: Confluent | the Data Streaming Platform Peerings (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1Peerings
    intent: List VPC/VNet peerings
    question: Which VPC peerings are connected to my Confluent networks?
  - id: createNetworkingV1Peering
    intent: Create a network peering
    question: How do I peer my cloud VPC with a Confluent Cloud network?
  - id: getNetworkingV1Peering
    intent: Read a network peering
    question: Is my VPC peering active yet?
  - id: updateNetworkingV1Peering
    intent: Update a network peering
    question: Can I rename an existing peering?
  - id: deleteNetworkingV1Peering
    intent: Delete a network peering
    question: Can I disconnect a VPC peering from my Confluent network?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-peerings-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Flink Artifa'
  name: Confluent | the Data Streaming Platform Presigned Urls (artifact/v1) API
  phrasing_intents:
  - id: presigned-upload-urlArtifactV1PresignedUrl
    intent: Get an upload URL for a Flink artifact
    question: How do I upload a Flink UDF JAR to Confluent Cloud?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-presigned-urls-artifact-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Connect Arti'
  name: Confluent | the Data Streaming Platform Presigned Urls (cam/v1) API
  phrasing_intents:
  - id: presigned-upload-urlCamV1PresignedUrl
    intent: Get an upload URL for a Connect artifact
    question: How do I upload a custom connector archive before registering it?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-presigned-urls-cam-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent | the Data Streaming Platform Presigned Urls (ccpm/v1) API
  phrasing_intents:
  - id: createCcpmV1PresignedUrl
    intent: Get an upload URL for a custom plugin archive
    question: Where do I upload my custom Connect plugin archive before registering it?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-presigned-urls-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent | the Data Streaming Platform Presigned Urls (connect/v1) API
  phrasing_intents:
  - id: presigned-upload-urlConnectV1PresignedUrl
    intent: Get an upload URL for a connector plugin archive
    question: How do I upload a custom connector plugin archive?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-presigned-urls-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove access to PrivateLink endpoints by AW'
  name: Confluent | the Data Streaming Platform Private Link Accesses (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1PrivateLinkAccesses
    intent: List private link accesses
    question: Which cloud accounts have private link access to my networks?
  - id: createNetworkingV1PrivateLinkAccess
    intent: Grant private link access
    question: How do I allow my cloud account to connect over PrivateLink?
  - id: getNetworkingV1PrivateLinkAccess
    intent: Get a private link access
    question: Is a private link access I granted ready to use?
  - id: updateNetworkingV1PrivateLinkAccess
    intent: Update a private link access
    question: Can I rename a private link access after creating it?
  - id: deleteNetworkingV1PrivateLinkAccess
    intent: Revoke a private link access
    question: How do I revoke a cloud account's private link access?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-private-link-accesses-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment connection objects represent'
  name: Confluent | the Data Streaming Platform Private Link Attachment Connections (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1PrivateLinkAttachmentConnections
    intent: List private link attachment connections
    question: Which private endpoint connections are attached to my private link attachment?
  - id: createNetworkingV1PrivateLinkAttachmentConnection
    intent: Connect a private endpoint to an attachment
    question: How do I register my VPC endpoint with a private link attachment?
  - id: getNetworkingV1PrivateLinkAttachmentConnection
    intent: Get a private link attachment connection
    question: Is my private link attachment connection ready?
  - id: updateNetworkingV1PrivateLinkAttachmentConnection
    intent: Rename a private link attachment connection
    question: How do I rename a private link attachment connection?
  - id: deleteNetworkingV1PrivateLinkAttachmentConnection
    intent: Delete a private link attachment connection
    question: How do I disconnect a private endpoint from a private link attachment?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-private-link-attachment-connections-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment objects represent reservatio'
  name: Confluent | the Data Streaming Platform Private Link Attachments (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1PrivateLinkAttachments
    intent: List private link attachments
    question: Which private link attachments exist in my environment?
  - id: createNetworkingV1PrivateLinkAttachment
    intent: Create a private link attachment
    question: How do I create a private link attachment for serverless cluster access?
  - id: getNetworkingV1PrivateLinkAttachment
    intent: Get a private link attachment
    question: What is the status of a specific private link attachment?
  - id: updateNetworkingV1PrivateLinkAttachment
    intent: Update a private link attachment
    question: Can I rename an existing private link attachment?
  - id: deleteNetworkingV1PrivateLinkAttachment
    intent: Delete a private link attachment
    question: How do I remove a private link attachment?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-private-link-attachments-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderSharedResource` object contains details of'
  name: Confluent | the Data Streaming Platform Provider Shared Resources (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ProviderSharedResources
    intent: List resources I'm sharing as a provider
    question: Which resources have I shared with other organizations through Stream Sharing?
  - id: getCdxV1ProviderSharedResource
    intent: Get a resource I'm sharing
    question: What details are on a resource I share with consumers?
  - id: updateCdxV1ProviderSharedResource
    intent: Update a resource I'm sharing
    question: How do I change the display name or description on a resource I share?
  - id: upload_imageCdxV1ProviderSharedResource
    intent: Upload an image for a resource I share
    question: How do I add a logo image to a resource I'm sharing?
  - id: view_imageCdxV1ProviderSharedResource
    intent: Get the image on a resource I share
    question: Can I download the logo image attached to a resource I'm sharing?
  - id: delete_imageCdxV1ProviderSharedResource
    intent: Delete the image on a resource I share
    question: How do I remove the image from a resource I share?
  phrasing_ops: 6
  slug: confluent-the-data-streaming-platform-provider-shared-resources-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderShare` object respresents the share that y'
  name: Confluent | the Data Streaming Platform Provider Shares (cdx/v1) API
  phrasing_intents:
  - id: listCdxV1ProviderShares
    intent: List stream shares I've provided
    question: Which topics have I shared with other organizations through Stream Sharing?
  - id: createCdxV1ProviderShare
    intent: Share a stream with a consumer
    question: How do I share a Kafka topic with someone outside my organization?
  - id: getCdxV1ProviderShare
    intent: Read a provider share
    question: Has the consumer accepted a share I sent?
  - id: deleteCdxV1ProviderShare
    intent: Revoke a provider share
    question: Can I stop sharing a topic with a consumer?
  - id: resendCdxV1ProviderShare
    intent: Resend a provider share invitation
    question: Can I resend a share invite the recipient never got?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-provider-shares-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Records (v3) API
  phrasing_intents:
  - id: produceRecord
    intent: Produce records to a Kafka topic
    question: How do I send a message to a Kafka topic over REST?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-records-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions a'
  name: Confluent | the Data Streaming Platform Regions (fcpm/v2) API
  phrasing_intents:
  - id: listFcpmV2Regions
    intent: List Flink regions
    question: Which cloud regions support Flink compute pools?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-regions-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent | the Data Streaming Platform Regions (rtce/v1) API
  phrasing_intents:
  - id: listRtceV1Regions
    intent: List real-time context engine regions
    question: In which regions is the real-time context engine available?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-regions-rtce-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions available when placing '
  name: Confluent | the Data Streaming Platform Regions (srcm/v2) API
  phrasing_intents:
  - id: listSrcmV2Regions
    intent: List Schema Registry regions
    question: Which cloud regions can host a Schema Registry cluster?
  - id: getSrcmV2Region
    intent: Get a Schema Registry region
    question: What cloud and packages does one Schema Registry region offer?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-regions-srcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent | the Data Streaming Platform Regions (tableflow/v1) API
  phrasing_intents:
  - id: listTableflowV1Regions
    intent: List regions where Tableflow is available
    question: Which cloud regions support Tableflow?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-regions-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourcePreference` objects represent the intent o'
  name: Confluent | the Data Streaming Platform Resource Preferences (notifications/v1) API
  phrasing_intents:
  - id: createNotificationsV1ResourcePreference
    intent: Set notification preference for a resource
    question: How do I turn notifications on or off for one specific resource?
  - id: getNotificationsV1ResourcePreference
    intent: Get a resource notification preference
    question: What notification setting applies to a resource preference I created?
  - id: updateNotificationsV1ResourcePreference
    intent: Update a resource notification preference
    question: Can I flip an existing resource preference from muted to enabled?
  - id: deleteNotificationsV1ResourcePreference
    intent: Delete a resource notification preference
    question: How do I remove a per-resource notification override?
  - id: getNotificationsV1ResourcePreferenceByFilter
    intent: Look up a resource's notification preference
    question: What notification preference is set for a given resource and resource type?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-resource-preferences-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourceSubscription` objects represent the intent'
  name: Confluent | the Data Streaming Platform Resource Subscriptions (notifications/v1) API
  phrasing_intents:
  - id: createNotificationsV1ResourceSubscription
    intent: Subscribe to notifications for a resource
    question: How do I get notified about events on a specific cluster or resource?
  - id: getNotificationsV1ResourceSubscription
    intent: Get a resource subscription
    question: What notification type and integrations does one of my subscriptions use?
  - id: updateNotificationsV1ResourceSubscription
    intent: Update a resource subscription
    question: How do I change where notifications for a resource are delivered?
  - id: deleteNotificationsV1ResourceSubscription
    intent: Unsubscribe from a resource's notifications
    question: How do I stop getting notifications for a resource?
  - id: listNotificationsV1ResourceSubscriptionsByFilter
    intent: Look up subscriptions for a resource
    question: Which notification subscriptions exist for a particular resource?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-resource-subscriptions-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A role binding grants a Principal a role on resourc'
  name: Confluent | the Data Streaming Platform Role Bindings (iam/v2) API
  phrasing_intents:
  - id: listIamV2RoleBindings
    intent: List role bindings
    question: Who has which roles on a given resource?
  - id: createIamV2RoleBinding
    intent: Grant a role to a principal
    question: How do I give a user or service account a role on a cluster?
  - id: getIamV2RoleBinding
    intent: Read a role binding
    question: What role and resource does a specific role binding cover?
  - id: deleteIamV2RoleBinding
    intent: Revoke a role binding
    question: How do I take away a role from a user?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-role-bindings-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An RtceTopic represents a customer''s Kafka topic en'
  name: Confluent | the Data Streaming Platform Rtce Topics (rtce/v1) API
  phrasing_intents:
  - id: listRtceV1RtceTopics
    intent: List real-time context engine topics
    question: Which topics are enabled for the real-time context engine on my Kafka cluster?
  - id: createRtceV1RtceTopic
    intent: Enable a topic for the real-time context engine
    question: How do I enable a Kafka topic for the real-time context engine?
  - id: getRtceV1RtceTopic
    intent: Get a real-time context engine topic
    question: What is the status of one RTCE topic?
  - id: updateRtceV1RtceTopic
    intent: Update a real-time context engine topic
    question: Can I change the settings of an existing RTCE topic?
  - id: deleteRtceV1RtceTopic
    intent: Delete a real-time context engine topic
    question: How do I stop serving a topic through the real-time context engine?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-rtce-topics-rtce-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Schemas (v1) API
  phrasing_intents:
  - id: getSchema
    intent: Get a schema record by ID
    question: How do I look up a registered schema and its type from a schema ID?
  - id: getSchemaOnly
    intent: Get only the raw schema text by ID
    question: Can I get just the raw schema body for an ID without the wrapper fields?
  - id: getSchemaTypes
    intent: List supported schema types
    question: Which schema formats does this Schema Registry support?
  - id: getSchemas
    intent: Search registered schemas
    question: How can I find all schemas whose subject starts with a given prefix?
  - id: getSubjects
    intent: List subjects that use a schema ID
    question: Which subjects are using a particular schema ID?
  - id: getVersions
    intent: List subject-versions for a schema ID
    question: What subject and version pairs point to a given schema ID?
  phrasing_ops: 6
  slug: confluent-the-data-streaming-platform-schemas-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets a list of all available scopes for applied quo'
  name: Confluent | the Data Streaming Platform Scopes (service-quota/v1) API
  phrasing_intents:
  - id: listServiceQuotaV1Scopes
    intent: List service quota scopes
    question: At which levels are service quotas applied in Confluent Cloud?
  - id: getServiceQuotaV1Scope
    intent: Get a service quota scope
    question: What does a particular service quota scope cover?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-scopes-service-quota-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to search for entities. Related gu'
  name: Confluent | the Data Streaming Platform Search (v1) API
  phrasing_intents:
  - id: searchUsingAttribute
    intent: Search the catalog by attribute
    question: Can I find topics or schemas whose attribute matches a given value?
  - id: searchUsingBasic
    intent: Full-text search the Stream Catalog
    question: Can I do a free-text search across topics, schemas and connectors?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-search-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ServiceAccount` objects are typically used to repr'
  name: Confluent | the Data Streaming Platform Service Accounts (iam/v2) API
  phrasing_intents:
  - id: listIamV2ServiceAccounts
    intent: List service accounts
    question: Which service accounts exist in my organization?
  - id: createIamV2ServiceAccount
    intent: Create a service account
    question: How do I create a service account for an application?
  - id: getIamV2ServiceAccount
    intent: Read a service account
    question: What are the details of a given service account?
  - id: updateIamV2ServiceAccount
    intent: Update a service account
    question: Can I change a service account's description?
  - id: deleteIamV2ServiceAccount
    intent: Delete a service account
    question: Does deleting a service account also remove its API keys?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-service-accounts-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Share Group (v3) API
  phrasing_intents:
  - id: listKafkaShareGroups
    intent: List share groups on a Kafka cluster
    question: Which share groups (queues for Kafka) exist on my cluster?
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
    question: What do I know about one consumer in a share group?
  - id: listKafkaShareGroupConsumerAssignments
    intent: List a share group consumer's assignments
    question: Which topic partitions is a share group consumer assigned?
  phrasing_ops: 6
  slug: confluent-the-data-streaming-platform-share-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Encrypted Token shared with consumer ## The Shared '
  name: Confluent | the Data Streaming Platform Shared Tokens (cdx/v1) API
  phrasing_intents:
  - id: resourcesCdxV1SharedToken
    intent: Preview resources in a shared token
    question: What topics were shared with me in a Stream Sharing token?
  - id: redeemCdxV1SharedToken
    intent: Redeem a shared token
    question: How do I redeem a Stream Sharing token to get topic access?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-shared-tokens-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent | the Data Streaming Platform Signup (partner/v2) API
  phrasing_intents:
  - id: signup
    intent: Sign up a new organization for a customer
    question: As a partner, how do I create a Confluent Cloud organization for my customer?
  - id: activateSignup
    intent: Activate an incomplete customer signup
    question: How do I finish a signup that was created without a user?
  - id: signupPartnerV2Link
    intent: Link a customer's existing organization
    question: Can I bring a customer's existing organization under my partner account?
  phrasing_ops: 3
  slug: confluent-the-data-streaming-platform-signup-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementException` represents an exception of a `'
  name: Confluent | the Data Streaming Platform Statement Exceptions (sql/v1) API
  phrasing_intents:
  - id: getSqlv1StatementExceptions
    intent: List recent exceptions of a Flink statement
    question: Why is my Flink SQL statement failing?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-statement-exceptions-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementResult` represents a result of a `Stateme'
  name: Confluent | the Data Streaming Platform Statement Results (sql/v1) API
  phrasing_intents:
  - id: getSqlv1StatementResult
    intent: Read a Flink SQL statement's results
    question: How do I fetch the rows returned by a Flink SQL query?
  phrasing_ops: 1
  slug: confluent-the-data-streaming-platform-statement-results-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: Execute SQL statements against queryable topics and read their results. A statement that resolves quickly returns its results inline; a long-running one is assigned a background job that can be polled
  name: Confluent | the Data Streaming Platform Statements (query/v1alpha1) API
  phrasing_intents:
  - id: executeQueryV1alpha1Statement
    intent: Run a SQL query
    question: How do I run a SQL query and get results back over HTTP?
  - id: getQueryV1alpha1JobStatus
    intent: Check a background query's status
    question: Is my long-running SQL query still running or finished?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-statements-query-v1alpha1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Statement` represents a core resource used to mode'
  name: Confluent | the Data Streaming Platform Statements (sql/v1) API
  phrasing_intents:
  - id: listSqlv1Statements
    intent: List Flink SQL statements
    question: Which Flink SQL statements are running in my environment?
  - id: createSqlv1Statement
    intent: Submit a Flink SQL statement
    question: How do I run a Flink SQL query through the API?
  - id: getSqlv1Statement
    intent: Get a Flink SQL statement
    question: What is the current phase of a Flink SQL statement I submitted?
  - id: deleteSqlv1Statement
    intent: Delete a Flink SQL statement
    question: How do I delete a Flink SQL statement I no longer need?
  - id: updateSqlv1Statement
    intent: Replace a Flink SQL statement's spec
    question: Can I stop a running statement or move it to another compute pool with a full update?
  - id: patchSqlv1Statement
    intent: Patch a Flink SQL statement
    question: Can I change just part of a statement without sending its whole definition?
  phrasing_ops: 6
  slug: confluent-the-data-streaming-platform-statements-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for requesting the status or the tasks for a Ma'
  name: Confluent | the Data Streaming Platform Status (connect/v1) API
  phrasing_intents:
  - id: readConnectv1ConnectorStatus
    intent: Check a connector's status
    question: Is my connector running, paused or failed?
  - id: listConnectv1ConnectorTasks
    intent: List a connector's running tasks
    question: What tasks are currently running for my connector?
  phrasing_ops: 2
  slug: confluent-the-data-streaming-platform-status-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Streams Group (v3) API
  phrasing_intents:
  - id: listKafkaStreamsGroups
    intent: List Kafka Streams groups on a cluster
    question: Which Kafka Streams applications are registered as streams groups on my cluster?
  - id: getKafkaStreamsGroup
    intent: Get details of one streams group
    question: What state is a particular Kafka Streams group in right now?
  - id: listKafkaStreamsGroupSubtopologies
    intent: List subtopologies of a streams group
    question: What subtopologies make up my Kafka Streams application's topology?
  - id: getKafkaStreamsGroupSubtopology
    intent: Get one subtopology of a streams group
    question: Which source topics and partitions does one specific subtopology use?
  - id: listKafkaStreamsGroupMembers
    intent: List members of a streams group
    question: Which instances are currently members of my Kafka Streams group?
  - id: getKafkaStreamsGroupMember
    intent: Get one member of a streams group
    question: What do we know about one particular member of a streams group?
  - id: getKafkaStreamsGroupMemberAssignments
    intent: Get a streams member's current assignments
    question: What tasks is a streams group member currently assigned?
  - id: getKafkaStreamsGroupMemberTargetAssignments
    intent: Get a streams member's target assignments
    question: What is the target assignment a streams member is being moved toward during a rebalance?
  phrasing_ops: 12
  slug: confluent-the-data-streaming-platform-streams-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Subjects (v1) API
  phrasing_intents:
  - id: getSchemaByVersion
    intent: Get a schema by subject and version
    question: How do I fetch a specific version of a schema from Schema Registry?
  - id: deleteSchemaVersion
    intent: Delete a schema version from a subject
    question: Can I remove one version of a schema without deleting the whole subject?
  - id: getReferencedBy
    intent: List schemas that reference a schema
    question: Which other schemas depend on this schema version through references?
  - id: getSchemaOnly_1
    intent: Get only the raw schema string for a version
    question: Can I get just the unescaped schema text for a version, without the wrapper fields?
  - id: listVersions
    intent: List versions registered under a subject
    question: How many schema versions have been registered for a subject?
  - id: register
    intent: Register a new schema version under a subject
    question: How do I register a new schema with Confluent Schema Registry?
  - id: lookUpSchemaUnderSubject
    intent: Check whether a schema is already registered
    question: Has this exact schema already been registered under a subject?
  - id: deleteSubject
    intent: Delete a subject and all its versions
    question: Can I delete an entire subject along with its compatibility level?
  phrasing_ops: 10
  slug: confluent-the-data-streaming-platform-subjects-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Subscription` objects represent the intent of the '
  name: Confluent | the Data Streaming Platform Subscriptions (notifications/v1) API
  phrasing_intents:
  - id: listNotificationsV1Subscriptions
    intent: List notification subscriptions
    question: Which notification types am I subscribed to?
  - id: createNotificationsV1Subscription
    intent: Subscribe to a notification type
    question: How do I start receiving alerts for a particular notification type?
  - id: getNotificationsV1Subscription
    intent: Get a notification subscription
    question: Which integrations does a given subscription deliver to?
  - id: updateNotificationsV1Subscription
    intent: Update a notification subscription
    question: Can I change which integrations an existing subscription uses?
  - id: deleteNotificationsV1Subscription
    intent: Unsubscribe from a notification type
    question: How do I stop receiving a type of notification?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-subscriptions-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Tableflow Topic represents configuration related '
  name: Confluent | the Data Streaming Platform Tableflow Topics (tableflow/v1) API
  phrasing_intents:
  - id: listTableflowV1TableflowTopics
    intent: List topics with Tableflow enabled
    question: Which Kafka topics have Tableflow turned on in a cluster?
  - id: createTableflowV1TableflowTopic
    intent: Enable Tableflow on a topic
    question: How do I materialize a Kafka topic as an Iceberg table with Tableflow?
  - id: getTableflowV1TableflowTopic
    intent: Get a Tableflow topic
    question: Is Tableflow running for one of my topics?
  - id: updateTableflowV1TableflowTopic
    intent: Update a Tableflow topic
    question: How do I change the settings on a topic that already has Tableflow?
  - id: deleteTableflowV1TableflowTopic
    intent: Disable Tableflow on a topic
    question: How do I turn off Tableflow for a topic?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-tableflow-topics-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Tool` models a reusable tool resource backed by a connection that can be refer'
  name: Confluent | the Data Streaming Platform Tools (sql/v1) API
  phrasing_intents:
  - id: createSqlv1Tool
    intent: Create a Flink SQL tool
    question: How do I define a new tool in a Flink SQL database?
  - id: listSqlv1Tools
    intent: List Flink SQL tools in a database
    question: Which tools are defined in a Flink SQL database?
  - id: getSqlv1Tool
    intent: Get a Flink SQL tool
    question: What is the definition of a particular SQL tool?
  - id: deleteSqlv1Tool
    intent: Delete a Flink SQL tool
    question: How do I remove a tool from a Flink SQL database?
  phrasing_ops: 4
  slug: confluent-the-data-streaming-platform-tools-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Topic (v3) API
  phrasing_intents:
  - id: listKafkaTopics
    intent: List Kafka topics in a cluster
    question: What topics exist in my Kafka cluster?
  - id: createKafkaTopic
    intent: Create a Kafka topic
    question: How do I create a Kafka topic with a set number of partitions?
  - id: getKafkaTopic
    intent: Get a Kafka topic
    question: How many partitions and what replication factor does a topic have?
  - id: updatePartitionCountKafkaTopic
    intent: Increase a topic's partition count
    question: How do I add more partitions to an existing topic?
  - id: deleteKafkaTopic
    intent: Delete a Kafka topic
    question: What happens to the data when I delete a Kafka topic?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-topic-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AWS Transit Gateway Attachments Related guide: [API'
  name: Confluent | the Data Streaming Platform Transit Gateway Attachments (networking/v1) API
  phrasing_intents:
  - id: listNetworkingV1TransitGatewayAttachments
    intent: List transit gateway attachments
    question: Which AWS Transit Gateway attachments are connected to my networks?
  - id: createNetworkingV1TransitGatewayAttachment
    intent: Create a transit gateway attachment
    question: How do I attach my Confluent network to an AWS Transit Gateway?
  - id: getNetworkingV1TransitGatewayAttachment
    intent: Read a transit gateway attachment
    question: Is my transit gateway attachment ready?
  - id: updateNetworkingV1TransitGatewayAttachment
    intent: Update a transit gateway attachment
    question: Can I rename a transit gateway attachment?
  - id: deleteNetworkingV1TransitGatewayAttachment
    intent: Delete a transit gateway attachment
    question: Can I detach a network from a transit gateway?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-transit-gateway-attachments-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Types (v1) API
  phrasing_intents:
  - id: getAllBusinessMetadataDefs
    intent: List business metadata definitions
    question: Which business metadata definitions exist in my Stream Catalog?
  - id: createBusinessMetadataDefs
    intent: Create business metadata definitions in bulk
    question: How do I define new business metadata to attach to topics and schemas?
  - id: updateBusinessMetadataDefs
    intent: Update business metadata definitions in bulk
    question: How do I change several existing business metadata definitions at once?
  - id: deleteBusinessMetadataDef
    intent: Delete a business metadata definition
    question: How do I remove a business metadata definition I no longer use?
  - id: getBusinessMetadataDefByName
    intent: Get a business metadata definition
    question: What attributes does a particular business metadata definition have?
  - id: getAllTagDefs
    intent: List tag definitions
    question: Which tag definitions like PII are available in the Stream Catalog?
  - id: updateTagDefs
    intent: Update tag definitions in bulk
    question: How do I edit several existing tag definitions at once?
  - id: createTagDefs
    intent: Create tag definitions in bulk
    question: How do I create a new tag like Sensitive to label topics and schemas?
  phrasing_ops: 10
  slug: confluent-the-data-streaming-platform-types-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To User Notifications API v1](https://img.shields'
  name: Confluent | the Data Streaming Platform User Notifications (notifications/v1) API
  phrasing_intents:
  - id: listNotificationsV1UserNotifications
    intent: List my notifications
    question: Which critical notifications did I get in the last 7 days?
  - id: getNotificationsV1UserNotification
    intent: Get a notification
    question: What are the details and recommended actions of one notification?
  - id: updateNotificationsV1UserNotification
    intent: Mark a notification read or unread
    question: How do I mark one notification as read?
  - id: markAllNotificationsV1UserNotifications
    intent: Mark many notifications read or unread
    question: Can I mark all my notifications as read at once?
  - id: getNotificationsV1UserNotificationsSummary
    intent: Get a notification summary
    question: How many notifications do I have waiting?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-user-notifications-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `User` objects represent individuals who may access'
  name: Confluent | the Data Streaming Platform Users (iam/v2) API
  phrasing_intents:
  - id: listIamV2Users
    intent: List users in the organization
    question: Who are the users in my Confluent Cloud organization?
  - id: getIamV2User
    intent: Get a user
    question: What email and auth type does a particular user have?
  - id: updateIamV2User
    intent: Update a user's name
    question: How do I change a user's full name?
  - id: deleteIamV2User
    intent: Delete a user and their API keys
    question: What happens to a user's API keys when I remove them?
  - id: update_auth_typeIamV2User
    intent: Change a user's authentication type
    question: How do I switch a user between SSO and password login?
  phrasing_ops: 5
  slug: confluent-the-data-streaming-platform-users-iam-v2-api
artifact_total: 152
asyncapis:
- description: ''
  name: Confluent The Data Streaming Platform Webhooks
  slug: confluent-the-data-streaming-platform-webhooks
collections:
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys API
  slug: open-confluent-the-data-streaming-platform-api-keys-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Clusters API
  slug: open-confluent-the-data-streaming-platform-clusters-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Environments API
  slug: open-confluent-the-data-streaming-platform-environments-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Organizations API
  slug: open-confluent-the-data-streaming-platform-organizations-api
- collection_type: open
  name: Confluent Cloud REST API (selected) API Keys Service Accounts API
  slug: open-confluent-the-data-streaming-platform-service-accounts-api
- collection_type: open
  name: Confluent Cloud REST API (selected)
  slug: open-confluent-the-data-streaming-platform
common:
- group: commercial
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/finops/confluent-the-data-streaming-platform-finops.yml
  title: ''
  type: FinOps
  url: finops/confluent-the-data-streaming-platform-finops.yml
- group: other
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/capabilities/confluent-the-data-streaming-platform-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/confluent-the-data-streaming-platform-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/overlays/confluent-the-data-streaming-platform-cloud-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluent-the-data-streaming-platform-cloud-apis-overlay.yaml
- group: auth
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/scopes/confluent-the-data-streaming-platform-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/confluent-the-data-streaming-platform-scopes.yml
- group: agent
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/agentic-access/confluent-the-data-streaming-platform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-the-data-streaming-platform-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/security/confluent-the-data-streaming-platform-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-the-data-streaming-platform-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/security/confluent-the-data-streaming-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/confluent-the-data-streaming-platform-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/authentication/confluent-the-data-streaming-platform-authentication.yml
  title: ''
  type: Authentication
  url: authentication/confluent-the-data-streaming-platform-authentication.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/confluentinc/agent-skills
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/confluent
- group: company
  title: ''
  type: Website
  url: https://www.confluent.io/
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
  type: Cloud API Reference
  url: https://docs.confluent.io/cloud/current/api.html
- group: build
  title: ''
  type: GitHub
  url: https://github.com/confluentinc
- group: company
  title: ''
  type: Blog
  url: https://www.confluent.io/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.confluent.io/pricing/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.confluent.cloud/
- group: start
  title: ''
  type: Login
  url: https://confluent.cloud/login
- group: other
  title: ''
  type: Marketplace
  url: https://www.confluent.io/hub/
- group: learn
  title: ''
  type: Training
  url: https://training.confluent.io/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.confluent.io/terms-of-use/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.confluent.io/legal/confluent-privacy-notice/
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.confluent.io/llms.txt
- group: agent
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/llms/confluent-the-data-streaming-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/confluent-the-data-streaming-platform-llms.txt
- group: build
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/packages/confluent-the-data-streaming-platform-packages.yml
  title: ''
  type: Packages
  url: packages/confluent-the-data-streaming-platform-packages.yml
- group: build
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/packages/confluent-the-data-streaming-platform-packages.yml
  title: ''
  type: SDKs
  url: packages/confluent-the-data-streaming-platform-packages.yml
- group: build
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/cli/confluent-the-data-streaming-platform-cli.yml
  title: ''
  type: CLI
  url: cli/confluent-the-data-streaming-platform-cli.yml
- group: agent
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/mcp/confluent-the-data-streaming-platform-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/confluent-the-data-streaming-platform-mcp.yml
- group: agent
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/conventions/confluent-the-data-streaming-platform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/confluent-the-data-streaming-platform-conventions.yml
- group: design
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/errors/confluent-the-data-streaming-platform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/confluent-the-data-streaming-platform-problem-types.yml
- group: design
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/lifecycle/confluent-the-data-streaming-platform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/confluent-the-data-streaming-platform-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.confluent.io/cloud/current/api.html#deprecation-policy
- group: operate
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/changelog/confluent-the-data-streaming-platform-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/confluent-the-data-streaming-platform-changelog.yml
- group: design
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/conformance/confluent-the-data-streaming-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/confluent-the-data-streaming-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.confluent.io/trust-and-security/
- group: auth
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/security/confluent-the-data-streaming-platform-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/confluent-the-data-streaming-platform-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.confluent.io/trust-and-security/
- group: auth
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/well-known/confluent-the-data-streaming-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/confluent-the-data-streaming-platform-security.txt
- group: agent
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/well-known/confluent-the-data-streaming-platform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/confluent-the-data-streaming-platform-well-known.yml
- group: design
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/asyncapi/confluent-the-data-streaming-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/confluent-the-data-streaming-platform-webhooks.yml
- group: start
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/sandbox/confluent-the-data-streaming-platform-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/confluent-the-data-streaming-platform-sandbox.yml
- group: commercial
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/plans/confluent-the-data-streaming-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/confluent-the-data-streaming-platform-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/confluent-the-data-streaming-platform/rate-limits/confluent-the-data-streaming-platform-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/confluent-the-data-streaming-platform-rate-limits.yml
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
  url: https://support.confluent.io/
- group: operate
  title: ''
  type: Community
  url: https://developer.confluent.io/community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/confluentinc
- group: start
  title: ''
  type: SignUp
  url: https://www.confluent.io/confluent-cloud/tryfree/
created: '2025-08-19'
description: Confluent is a fully managed data streaming platform built by the original creators of Apache Kafka. It lets organizations stream, connect, process, and govern data in motion through a cloud-native service (Confluent Cloud) and the on-prem/self-managed Confluent Platform. Confluent's developer surface includes the Confluent Cloud REST API for managing clusters, environments, and access; the Kafka REST Proxy for producing and consuming events over HTTP; the Schema Registry REST API for governance of Avro, JSON Schema, and Protobuf schemas; the Kafka Connect REST API for managing connectors; the ksqlDB REST API for stream processing; and managed Apache Flink. Authentication is API-key based (Cloud) or HTTP/mTLS/OAuth (Platform).
finops:
- has_sources: true
  method: derived
  name: Confluent The Data Streaming Platform Finops
  primary_unit: cluster
  service_category: ''
  slug: confluent-the-data-streaming-platform-finops
  template: false
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent-the-data-streaming-platform.png
layout: provider
mcp_servers:
- description: Remote MCP server at api.confluent.cloud requiring an API key.
  name: Confluent managed MCP server
  slug: confluent-managed-mcp-server
modified: '2026-09-05'
name: Confluent | the Data Streaming Platform
nav: Providers
network: true
overview: 'Confluent | the Data Streaming Platform publishes 121 API contracts indexed on the [APIs.io](https://apis.io/) network, including Access Points (networking/v1) API, ACL (v3) API, Agents (sql/v1) API, and 118 more. Tagged areas include Apache Flink, Apache Kafka, Confluent Cloud, Connectors, and Data Streaming.


  The Confluent | the Data Streaming Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Confluent | the Data Streaming Platform''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, training material, CLI, and 44 more developer resources.'
plans:
- name: Confluent The Data Streaming Platform Plans Pricing
  plan_count: 4
  slug: confluent-the-data-streaming-platform-plans-pricing
- name: Confluent The Data Streaming Platform Price Estimates
  plan_count: 0
  slug: confluent-the-data-streaming-platform-price-estimates
random_paper: 4
rate_limits:
- limit_count: 0
  name: Confluent The Data Streaming Platform Rate Limits
  slug: confluent-the-data-streaming-platform-rate-limits
rules:
- authorship: generated
  effective_rule_count: 105
  extends:
  - spectral:oas
  name: Confluent | the Data Streaming Platform API Rules
  rule_count: 64
  severity_counts:
    error: 38
    hint: 0
    info: 4
    warn: 22
  slug: confluent-the-data-streaming-platform-rules
scopes:
- name: Confluent The Data Streaming Platform Scopes
  scope_count: 5
  slug: confluent-the-data-streaming-platform-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: exemplar
  composite: 82.0
  coverage:
    artifact_dirs: 31
    catalog_earned: 56.5
    catalog_earned_first_party: 12.0
    catalog_gap: 58.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 2.5
  facets:
    access_clarity: 100.0
    contract_governance: 31.8
    contract_quality: 67.4
    developer_ergonomics: 85.7
    discoverability: 75.0
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 79.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 100.0
      total: 116
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://apis.io/screenshots/confluent-the-data-streaming-platform/confluent-the-data-streaming-platform-2026-06-20T174902.png
security:
- kind: authentication
  name: Confluent The Data Streaming Platform Authentication
  slug: confluent-the-data-streaming-platform-authentication
  summary_line: http/oauth2 · 3 schemes
- kind: domain-security
  name: Confluent The Data Streaming Platform Domain Security
  slug: confluent-the-data-streaming-platform-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Confluent The Data Streaming Platform Vulnerability Disclosure
  slug: confluent-the-data-streaming-platform-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Confluent The Data Streaming Platform Trust Center
  slug: confluent-the-data-streaming-platform-trust-center
  summary_line: SOC 1 Type 2, SOC 2 Type 2, SOC 3, ISO 27001, ISO 27701, PCI DSS, CSA STAR Level 2, HITRUST CSF, TISAX
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
slug: confluent-the-data-streaming-platform
tags:
- Apache Flink
- Apache Kafka
- Confluent Cloud
- Connectors
- Data Streaming
- Event Streaming
- Kafka Connect
- ksqlDB
- Real-Time Data
- REST
- Schema Registry
- Stream Processing
website: https://www.confluent.io/
---

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
  scored_at: '2026-09-16'
agentic_access:
- acting_count: 269
  human_in_the_loop: 5
  name: Confluent The Data Streaming Platform Agentic Access
  operation_count: 523
  slug: confluent-the-data-streaming-platform-agentic-access
  summary_line: 523 operations · 269 acting · 5 human-in-the-loop
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
  slug: confluent-the-data-streaming-platform-access-points-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform ACL (v3) API
  slug: confluent-the-data-streaming-platform-acl-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Agent` models an AI agent that uses a specified model, prompt, and set of tool'
  name: Confluent | the Data Streaming Platform Agents (sql/v1) API
  slug: confluent-the-data-streaming-platform-agents-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ApiKey` objects represent access to different part'
  name: Confluent | the Data Streaming Platform API Keys (iam/v2) API
  slug: confluent-the-data-streaming-platform-api-keys-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A `quota` object represents a quota configuration f'
  name: Confluent | the Data Streaming Platform Applied Quotas (service-quota/v1) API
  slug: confluent-the-data-streaming-platform-applied-quotas-service-quota-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Catalog Integration represents configuration rela'
  name: Confluent | the Data Streaming Platform Catalog Integrations (tableflow/v1) API
  slug: confluent-the-data-streaming-platform-catalog-integrations-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `CertificateAuthority` objects represent signing ce'
  name: Confluent | the Data Streaming Platform Certificate Authorities (iam/v2) API
  slug: confluent-the-data-streaming-platform-certificate-authorities-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Identitypool` objects represent workload identitie'
  name: Confluent | the Data Streaming Platform Certificate Identity Pools (iam/v2) API
  slug: confluent-the-data-streaming-platform-certificate-identity-pools-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ClientQuota` objects represent Client Quotas you c'
  name: Confluent | the Data Streaming Platform Client Quotas (kafka-quotas/v1) API
  slug: confluent-the-data-streaming-platform-client-quotas-kafka-quotas-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Cluster Linking (v3) API
  slug: confluent-the-data-streaming-platform-cluster-linking-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Cluster (v3) API
  slug: confluent-the-data-streaming-platform-cluster-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Apache Kafka Clusters '
  name: Confluent | the Data Streaming Platform Clusters (cmk/v2) API
  slug: confluent-the-data-streaming-platform-clusters-cmk-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cluster` represents a ksqlDB runtime that you can '
  name: Confluent | the Data Streaming Platform Clusters (ksqldbcm/v2) API
  slug: confluent-the-data-streaming-platform-clusters-ksqldbcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Clusters on Confluent Cloud.'
  name: Confluent | the Data Streaming Platform Clusters (srcm/v2) API
  slug: confluent-the-data-streaming-platform-clusters-srcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Cluste'
  name: Confluent | the Data Streaming Platform Clusters (srcm/v3) API
  slug: confluent-the-data-streaming-platform-clusters-srcm-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to test schema compatibility. Rela'
  name: Confluent | the Data Streaming Platform Compatibility (v1) API
  slug: confluent-the-data-streaming-platform-compatibility-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Compute Pool represents a set of compute resource'
  name: Confluent | the Data Streaming Platform Compute Pools (fcpm/v2) API
  slug: confluent-the-data-streaming-platform-compute-pools-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to manage and query schema compati'
  name: Confluent | the Data Streaming Platform Config (v1) API
  slug: confluent-the-data-streaming-platform-config-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Configs (v3) API
  slug: confluent-the-data-streaming-platform-configs-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connect Artifact` objects represent collection of '
  name: Confluent | the Data Streaming Platform Connect Artifacts (cam/v1) API
  slug: confluent-the-data-streaming-platform-connect-artifacts-cam-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `ConnectCluster` object represent Confluent Platform Connect clusters registere'
  name: Confluent | the Data Streaming Platform Connect Clusters (usm/v1) API
  slug: confluent-the-data-streaming-platform-connect-clusters-usm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connection` represents a core resource used to mod'
  name: Confluent | the Data Streaming Platform Connections (sql/v1) API
  slug: confluent-the-data-streaming-platform-connections-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed Connectors or Custom Connectors in '
  name: Confluent | the Data Streaming Platform Connectors (connect/v1) API
  slug: confluent-the-data-streaming-platform-connectors-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Consumer Group (v3) API
  slug: confluent-the-data-streaming-platform-consumer-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerSharedResource` object contains details of'
  name: Confluent | the Data Streaming Platform Consumer Shared Resources (cdx/v1) API
  slug: confluent-the-data-streaming-platform-consumer-shared-resources-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerShare` object respresents the share that y'
  name: Confluent | the Data Streaming Platform Consumer Shares (cdx/v1) API
  slug: confluent-the-data-streaming-platform-consumer-shares-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to retrieve information about sche'
  name: Confluent | the Data Streaming Platform Contexts (v1) API
  slug: confluent-the-data-streaming-platform-contexts-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cost` objects represent the aggregated billing cos'
  name: Confluent | the Data Streaming Platform Costs (billing/v1) API
  slug: confluent-the-data-streaming-platform-costs-billing-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Custom Code Logging API EA](https://img.shield'
  name: Confluent | the Data Streaming Platform Custom Code Loggings (ccl/v1) API
  slug: confluent-the-data-streaming-platform-custom-code-loggings-ccl-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPluginVersion objects represent Custom'
  name: Confluent | the Data Streaming Platform Custom Connect Plugin Versions (ccpm/v1) API
  slug: confluent-the-data-streaming-platform-custom-connect-plugin-versions-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPlugins objects represent Custom Conne'
  name: Confluent | the Data Streaming Platform Custom Connect Plugins (ccpm/v1) API
  slug: confluent-the-data-streaming-platform-custom-connect-plugins-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectorPlugins objects represent Custom Con'
  name: Confluent | the Data Streaming Platform Custom Connector Plugins (connect/v1) API
  slug: confluent-the-data-streaming-platform-custom-connector-plugins-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of supported runtime languages for Custom Conn'
  name: Confluent | the Data Streaming Platform Custom Connector Runtimes (connect/v1) API
  slug: confluent-the-data-streaming-platform-custom-connector-runtimes-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Data Encryption Keys (v1) API
  slug: confluent-the-data-streaming-platform-data-encryption-keys-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add, remove, and update DNS forwarder for your gate'
  name: Confluent | the Data Streaming Platform DNS Forwarders (networking/v1) API
  slug: confluent-the-data-streaming-platform-dns-forwarders-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) DNS record objects are associated with Confluent Cl'
  name: Confluent | the Data Streaming Platform DNS Records (networking/v1) API
  slug: confluent-the-data-streaming-platform-dns-records-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An Endpoint object represents a Fully Qualified Dom'
  name: Confluent | the Data Streaming Platform Endpoints (endpoint/v1) API
  slug: confluent-the-data-streaming-platform-endpoints-endpoint-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent | the Data Streaming Platform Entitlements (partner/v2) API
  slug: confluent-the-data-streaming-platform-entitlements-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Entity (v1) API
  slug: confluent-the-data-streaming-platform-entity-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Environment` objects represent an isolated namespa'
  name: Confluent | the Data Streaming Platform Environments (org/v2) API
  slug: confluent-the-data-streaming-platform-environments-org-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Exporters (v1) API
  slug: confluent-the-data-streaming-platform-exporters-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) FlinkArtifact objects represent Flink Artifacts on '
  name: Confluent | the Data Streaming Platform Flink Artifacts (artifact/v1) API
  slug: confluent-the-data-streaming-platform-flink-artifacts-artifact-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Gateway represents a slice of traffic capacity in'
  name: Confluent | the Data Streaming Platform Gateways (networking/v1) API
  slug: confluent-the-data-streaming-platform-gateways-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `GroupMapping` objects establish relationships betw'
  name: Confluent | the Data Streaming Platform Group Mappings (iam/v2/sso) API
  slug: confluent-the-data-streaming-platform-group-mappings-iam-v2-sso-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityPool` objects represent groups of identiti'
  name: Confluent | the Data Streaming Platform Identity Pools (iam/v2) API
  slug: confluent-the-data-streaming-platform-identity-pools-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityProvider` objects represent external OAuth'
  name: Confluent | the Data Streaming Platform Identity Providers (iam/v2) API
  slug: confluent-the-data-streaming-platform-identity-providers-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) You can create an `Integration` to specify how we c'
  name: Confluent | the Data Streaming Platform Integrations (notifications/v1) API
  slug: confluent-the-data-streaming-platform-integrations-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Provider Integration` objects represent access to '
  name: Confluent | the Data Streaming Platform Integrations (pim/v1) API
  slug: confluent-the-data-streaming-platform-integrations-pim-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/b'
  name: Confluent | the Data Streaming Platform Integrations (pim/v2) API
  slug: confluent-the-data-streaming-platform-integrations-pim-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Invitation` objects represent invitations to invit'
  name: Confluent | the Data Streaming Platform Invitations (iam/v2) API
  slug: confluent-the-data-streaming-platform-invitations-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) IP Addresses Related guide: [Use Public Egress IP a'
  name: Confluent | the Data Streaming Platform IP Addresses (networking/v1) API
  slug: confluent-the-data-streaming-platform-ip-addresses-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The IP Filter Summary endpoint returns an aggregati'
  name: Confluent | the Data Streaming Platform IP Filter Summaries (iam/v2) API
  slug: confluent-the-data-streaming-platform-ip-filter-summaries-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IP Filter` objects are bindings between IP Groups '
  name: Confluent | the Data Streaming Platform IP Filters (iam/v2) API
  slug: confluent-the-data-streaming-platform-ip-filters-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Definitions of networks which can be named and refe'
  name: Confluent | the Data Streaming Platform IP Groups (iam/v2) API
  slug: confluent-the-data-streaming-platform-ip-groups-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `JWKS` objects represent public key sets for a spec'
  name: Confluent | the Data Streaming Platform Jwks (iam/v2) API
  slug: confluent-the-data-streaming-platform-jwks-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `KafkaCluster` object represent Confluent Platform Kafka clusters registered wi'
  name: Confluent | the Data Streaming Platform Kafka Clusters (usm/v1) API
  slug: confluent-the-data-streaming-platform-kafka-clusters-usm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Key Encryption Keys (v1) API
  slug: confluent-the-data-streaming-platform-key-encryption-keys-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Key` objects represent customer managed keys on de'
  name: Confluent | the Data Streaming Platform Keys (byok/v1) API
  slug: confluent-the-data-streaming-platform-keys-byok-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the lifecycle for a Managed Connec'
  name: Confluent | the Data Streaming Platform Lifecycle (connect/v1) API
  slug: confluent-the-data-streaming-platform-lifecycle-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed connectors in Confluent Cloud.'
  name: Confluent | the Data Streaming Platform Managed Connector Plugins (connect/v1) API
  slug: confluent-the-data-streaming-platform-managed-connector-plugins-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTableVersion` represents a specific ve'
  name: Confluent | the Data Streaming Platform Materialized Table Versions (sql/v1) API
  slug: confluent-the-data-streaming-platform-materialized-table-versions-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTable` represents a core resource used'
  name: Confluent | the Data Streaming Platform Materialized Tables (sql/v1) API
  slug: confluent-the-data-streaming-platform-materialized-tables-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Modes (v1) API
  slug: confluent-the-data-streaming-platform-modes-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Network Link Enpoint is associated with a Private'
  name: Confluent | the Data Streaming Platform Network Link Endpoints (networking/v1) API
  slug: confluent-the-data-streaming-platform-network-link-endpoints-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of incoming Network Link Enpoints associated w'
  name: Confluent | the Data Streaming Platform Network Link Service Associations (networking/v1) API
  slug: confluent-the-data-streaming-platform-network-link-service-associations-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Network Link Service is associated with a Private L'
  name: Confluent | the Data Streaming Platform Network Link Services (networking/v1) API
  slug: confluent-the-data-streaming-platform-network-link-services-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Network` represents a network (VPC) in Confluent C'
  name: Confluent | the Data Streaming Platform Networks (networking/v1) API
  slug: confluent-the-data-streaming-platform-networks-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The type of notifications (and their corresponding '
  name: Confluent | the Data Streaming Platform Notification Types (notifications/v1) API
  slug: confluent-the-data-streaming-platform-notification-types-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) OAuth Token is a [JSON Web Token (JWT)](https://www'
  name: Confluent | the Data Streaming Platform OAuth Tokens (sts/v1) API
  slug: confluent-the-data-streaming-platform-oauth-tokens-sts-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the offsets for a Managed Connecto'
  name: Confluent | the Data Streaming Platform Offsets (connect/v1) API
  slug: confluent-the-data-streaming-platform-offsets-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Stream sharing opt in options ## The Opt Ins Model '
  name: Confluent | the Data Streaming Platform Opt Ins (cdx/v1) API
  slug: confluent-the-data-streaming-platform-opt-ins-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `OrgComputePoolConfig` manages compute pool configu'
  name: Confluent | the Data Streaming Platform Org Compute Pool Configs (fcpm/v2) API
  slug: confluent-the-data-streaming-platform-org-compute-pool-configs-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Organization` objects represent a customer organiz'
  name: Confluent | the Data Streaming Platform Organizations (org/v2) API
  slug: confluent-the-data-streaming-platform-organizations-org-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent | the Data Streaming Platform Organizations (partner/v2) API
  slug: confluent-the-data-streaming-platform-organizations-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Partition (v3) API
  slug: confluent-the-data-streaming-platform-partition-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove VPC/VNet peering connections between '
  name: Confluent | the Data Streaming Platform Peerings (networking/v1) API
  slug: confluent-the-data-streaming-platform-peerings-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Flink Artifa'
  name: Confluent | the Data Streaming Platform Presigned Urls (artifact/v1) API
  slug: confluent-the-data-streaming-platform-presigned-urls-artifact-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Connect Arti'
  name: Confluent | the Data Streaming Platform Presigned Urls (cam/v1) API
  slug: confluent-the-data-streaming-platform-presigned-urls-cam-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent | the Data Streaming Platform Presigned Urls (ccpm/v1) API
  slug: confluent-the-data-streaming-platform-presigned-urls-ccpm-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent | the Data Streaming Platform Presigned Urls (connect/v1) API
  slug: confluent-the-data-streaming-platform-presigned-urls-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove access to PrivateLink endpoints by AW'
  name: Confluent | the Data Streaming Platform Private Link Accesses (networking/v1) API
  slug: confluent-the-data-streaming-platform-private-link-accesses-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment connection objects represent'
  name: Confluent | the Data Streaming Platform Private Link Attachment Connections (networking/v1) API
  slug: confluent-the-data-streaming-platform-private-link-attachment-connections-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment objects represent reservatio'
  name: Confluent | the Data Streaming Platform Private Link Attachments (networking/v1) API
  slug: confluent-the-data-streaming-platform-private-link-attachments-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderSharedResource` object contains details of'
  name: Confluent | the Data Streaming Platform Provider Shared Resources (cdx/v1) API
  slug: confluent-the-data-streaming-platform-provider-shared-resources-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderShare` object respresents the share that y'
  name: Confluent | the Data Streaming Platform Provider Shares (cdx/v1) API
  slug: confluent-the-data-streaming-platform-provider-shares-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Records (v3) API
  slug: confluent-the-data-streaming-platform-records-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions a'
  name: Confluent | the Data Streaming Platform Regions (fcpm/v2) API
  slug: confluent-the-data-streaming-platform-regions-fcpm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent | the Data Streaming Platform Regions (rtce/v1) API
  slug: confluent-the-data-streaming-platform-regions-rtce-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions available when placing '
  name: Confluent | the Data Streaming Platform Regions (srcm/v2) API
  slug: confluent-the-data-streaming-platform-regions-srcm-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent | the Data Streaming Platform Regions (tableflow/v1) API
  slug: confluent-the-data-streaming-platform-regions-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourcePreference` objects represent the intent o'
  name: Confluent | the Data Streaming Platform Resource Preferences (notifications/v1) API
  slug: confluent-the-data-streaming-platform-resource-preferences-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourceSubscription` objects represent the intent'
  name: Confluent | the Data Streaming Platform Resource Subscriptions (notifications/v1) API
  slug: confluent-the-data-streaming-platform-resource-subscriptions-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A role binding grants a Principal a role on resourc'
  name: Confluent | the Data Streaming Platform Role Bindings (iam/v2) API
  slug: confluent-the-data-streaming-platform-role-bindings-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An RtceTopic represents a customer''s Kafka topic en'
  name: Confluent | the Data Streaming Platform Rtce Topics (rtce/v1) API
  slug: confluent-the-data-streaming-platform-rtce-topics-rtce-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Schemas (v1) API
  slug: confluent-the-data-streaming-platform-schemas-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets a list of all available scopes for applied quo'
  name: Confluent | the Data Streaming Platform Scopes (service-quota/v1) API
  slug: confluent-the-data-streaming-platform-scopes-service-quota-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to search for entities. Related gu'
  name: Confluent | the Data Streaming Platform Search (v1) API
  slug: confluent-the-data-streaming-platform-search-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ServiceAccount` objects are typically used to repr'
  name: Confluent | the Data Streaming Platform Service Accounts (iam/v2) API
  slug: confluent-the-data-streaming-platform-service-accounts-iam-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Share Group (v3) API
  slug: confluent-the-data-streaming-platform-share-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Encrypted Token shared with consumer ## The Shared '
  name: Confluent | the Data Streaming Platform Shared Tokens (cdx/v1) API
  slug: confluent-the-data-streaming-platform-shared-tokens-cdx-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent | the Data Streaming Platform Signup (partner/v2) API
  slug: confluent-the-data-streaming-platform-signup-partner-v2-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementException` represents an exception of a `'
  name: Confluent | the Data Streaming Platform Statement Exceptions (sql/v1) API
  slug: confluent-the-data-streaming-platform-statement-exceptions-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementResult` represents a result of a `Stateme'
  name: Confluent | the Data Streaming Platform Statement Results (sql/v1) API
  slug: confluent-the-data-streaming-platform-statement-results-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: Execute SQL statements against queryable topics and read their results. A statement that resolves quickly returns its results inline; a long-running one is assigned a background job that can be polled
  name: Confluent | the Data Streaming Platform Statements (query/v1alpha1) API
  slug: confluent-the-data-streaming-platform-statements-query-v1alpha1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Statement` represents a core resource used to mode'
  name: Confluent | the Data Streaming Platform Statements (sql/v1) API
  slug: confluent-the-data-streaming-platform-statements-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for requesting the status or the tasks for a Ma'
  name: Confluent | the Data Streaming Platform Status (connect/v1) API
  slug: confluent-the-data-streaming-platform-status-connect-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Streams Group (v3) API
  slug: confluent-the-data-streaming-platform-streams-group-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Subjects (v1) API
  slug: confluent-the-data-streaming-platform-subjects-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Subscription` objects represent the intent of the '
  name: Confluent | the Data Streaming Platform Subscriptions (notifications/v1) API
  slug: confluent-the-data-streaming-platform-subscriptions-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Tableflow Topic represents configuration related '
  name: Confluent | the Data Streaming Platform Tableflow Topics (tableflow/v1) API
  slug: confluent-the-data-streaming-platform-tableflow-topics-tableflow-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Tool` models a reusable tool resource backed by a connection that can be refer'
  name: Confluent | the Data Streaming Platform Tools (sql/v1) API
  slug: confluent-the-data-streaming-platform-tools-sql-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent | the Data Streaming Platform Topic (v3) API
  slug: confluent-the-data-streaming-platform-topic-v3-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AWS Transit Gateway Attachments Related guide: [API'
  name: Confluent | the Data Streaming Platform Transit Gateway Attachments (networking/v1) API
  slug: confluent-the-data-streaming-platform-transit-gateway-attachments-networking-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent | the Data Streaming Platform Types (v1) API
  slug: confluent-the-data-streaming-platform-types-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To User Notifications API v1](https://img.shields'
  name: Confluent | the Data Streaming Platform User Notifications (notifications/v1) API
  slug: confluent-the-data-streaming-platform-user-notifications-notifications-v1-api
- baseURL: https://api.confluent.cloud
  baseurl_source: declared
  description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `User` objects represent individuals who may access'
  name: Confluent | the Data Streaming Platform Users (iam/v2) API
  slug: confluent-the-data-streaming-platform-users-iam-v2-api
artifact_total: 151
asyncapis:
- description: ''
  name: Confluent The Data Streaming Platform Webhooks
  slug: confluent-the-data-streaming-platform-webhooks
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
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
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/overlays/confluent-the-data-streaming-platform-cloud-apis-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/confluent-the-data-streaming-platform-cloud-apis-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/scopes/confluent-the-data-streaming-platform-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/confluent-the-data-streaming-platform-scopes.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/agentic-access/confluent-the-data-streaming-platform-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-the-data-streaming-platform-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/security/confluent-the-data-streaming-platform-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-the-data-streaming-platform-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/security/confluent-the-data-streaming-platform-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/confluent-the-data-streaming-platform-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/authentication/confluent-the-data-streaming-platform-authentication.yml
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
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/llms/confluent-the-data-streaming-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/confluent-the-data-streaming-platform-llms.txt
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/packages/confluent-the-data-streaming-platform-packages.yml
  title: ''
  type: Packages
  url: packages/confluent-the-data-streaming-platform-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/packages/confluent-the-data-streaming-platform-packages.yml
  title: ''
  type: SDKs
  url: packages/confluent-the-data-streaming-platform-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/cli/confluent-the-data-streaming-platform-cli.yml
  title: ''
  type: CLI
  url: cli/confluent-the-data-streaming-platform-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/mcp/confluent-the-data-streaming-platform-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/confluent-the-data-streaming-platform-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/conventions/confluent-the-data-streaming-platform-conventions.yml
  title: ''
  type: Conventions
  url: conventions/confluent-the-data-streaming-platform-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/errors/confluent-the-data-streaming-platform-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/confluent-the-data-streaming-platform-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/lifecycle/confluent-the-data-streaming-platform-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/confluent-the-data-streaming-platform-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://docs.confluent.io/cloud/current/api.html#deprecation-policy
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/changelog/confluent-the-data-streaming-platform-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/confluent-the-data-streaming-platform-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/conformance/confluent-the-data-streaming-platform-conformance.yml
  title: ''
  type: Conformance
  url: conformance/confluent-the-data-streaming-platform-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.confluent.io/trust-and-security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/security/confluent-the-data-streaming-platform-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/confluent-the-data-streaming-platform-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://www.confluent.io/trust-and-security/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/well-known/confluent-the-data-streaming-platform-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/confluent-the-data-streaming-platform-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/well-known/confluent-the-data-streaming-platform-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/confluent-the-data-streaming-platform-well-known.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/asyncapi/confluent-the-data-streaming-platform-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/confluent-the-data-streaming-platform-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/sandbox/confluent-the-data-streaming-platform-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/confluent-the-data-streaming-platform-sandbox.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/plans/confluent-the-data-streaming-platform-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/confluent-the-data-streaming-platform-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/rate-limits/confluent-the-data-streaming-platform-rate-limits.yml
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
- name: Confluent The Data Streaming Platform Finops
  service_category: API
  slug: confluent-the-data-streaming-platform-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/confluent-the-data-streaming-platform.png
layout: provider
mcp_servers:
- description: ''
  name: Confluent managed MCP server
  slug: confluent-managed-mcp-server
modified: '2026-09-05'
name: Confluent | the Data Streaming Platform
nav: Providers
network: true
overview: 'Confluent | the Data Streaming Platform publishes 116 APIs on the [APIs.io](https://apis.io/) network, including Access Points (networking/v1) API, ACL (v3) API, Agents (sql/v1) API, and 113 more. Tagged areas include Apache Flink, Apache Kafka, Confluent Cloud, Connectors, and Data Streaming.


  The Confluent | the Data Streaming Platform catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Confluent | the Data Streaming Platform''s developer surface includes authentication, documentation, GitHub presence, engineering blog, pricing, training material, CLI, and 42 more developer resources.'
plans:
- name: Confluent The Data Streaming Platform Plans Pricing
  plan_count: 5
  slug: confluent-the-data-streaming-platform-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 0
  name: Confluent The Data Streaming Platform Rate Limits
  slug: confluent-the-data-streaming-platform-rate-limits
scopes:
- name: Confluent The Data Streaming Platform Scopes
  scope_count: 5
  slug: confluent-the-data-streaming-platform-scopes
  summary_line: 5 scopes · clientCredentials
score:
  band: exemplar
  composite: 72.5
  coverage:
    artifact_dirs: 26
    catalog_earned: 39.0
    catalog_earned_first_party: 12.0
    catalog_gap: 76.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.4
  facets:
    access_clarity: 100.0
    contract_governance: 18.2
    contract_quality: 67.4
    developer_ergonomics: 85.7
    discoverability: 51.9
    operational_transparency: 52.6
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 116
    mcp: first-party
    skills: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-16'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/confluent-the-data-streaming-platform/refs/heads/main/screenshots/confluent-the-data-streaming-platform-2026-06-20T174902.png
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

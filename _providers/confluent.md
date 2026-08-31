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
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 47.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Confluent Agentic Access
  operation_count: 18
  slug: confluent-agentic-access
  summary_line: 18 operations · 6 acting
api_count: 3
apis:
- description: Stream, connect, process, and govern your data with an all-in-one, real-time platform from the pioneer in data streaming. Build faster, scale smarter, and turn data chaos into instantly accessible and
  name: Confluent
  slug: confluent
- description: Confluent's managed remote Model Context Protocol servers. The global server at https://api.confluent.cloud/mcp/v1 provides tools for discovering environments and clusters, inspecting and debugging co
  name: Confluent Managed MCP Servers
  slug: confluent-mcp
- description: The ACLs API from Confluent — 1 operation(s) for acls.
  name: Confluent ACLs API
  slug: confluent-acls-api
- description: The API Keys API from Confluent — 1 operation(s) for api keys.
  name: Confluent API Keys API
  slug: confluent-api-keys-api
- description: The Clusters API from Confluent — 2 operation(s) for clusters.
  name: Confluent Clusters API
  slug: confluent-clusters-api
- description: The Consumer Groups API from Confluent — 2 operation(s) for consumer groups.
  name: Confluent Consumer Groups API
  slug: confluent-consumer-groups-api
- description: The Environments API from Confluent — 1 operation(s) for environments.
  name: Confluent Environments API
  slug: confluent-environments-api
- description: The Partitions API from Confluent — 2 operation(s) for partitions.
  name: Confluent Partitions API
  slug: confluent-partitions-api
- description: The Service Accounts API from Confluent — 1 operation(s) for service accounts.
  name: Confluent Service Accounts API
  slug: confluent-service-accounts-api
- description: The Topics API from Confluent — 2 operation(s) for topics.
  name: Confluent Topics API
  slug: confluent-topics-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AccessPoint objects represent network connections i'
  name: Confluent Access Points (networking/v1) API
  slug: confluent-access-points-networking-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent ACL (v3) API
  slug: confluent-acl-v3-api
- description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Agent` models an AI agent that uses a specified model, prompt, and set of tool'
  name: Confluent Agents (sql/v1) API
  slug: confluent-agents-sql-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ApiKey` objects represent access to different part'
  name: Confluent API Keys (iam/v2) API
  slug: confluent-api-keys-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A `quota` object represents a quota configuration f'
  name: Confluent Applied Quotas (service-quota/v1) API
  slug: confluent-applied-quotas-service-quota-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Catalog Integration represents configuration rela'
  name: Confluent Catalog Integrations (tableflow/v1) API
  slug: confluent-catalog-integrations-tableflow-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `CertificateAuthority` objects represent signing ce'
  name: Confluent Certificate Authorities (iam/v2) API
  slug: confluent-certificate-authorities-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Identitypool` objects represent workload identitie'
  name: Confluent Certificate Identity Pools (iam/v2) API
  slug: confluent-certificate-identity-pools-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ClientQuota` objects represent Client Quotas you c'
  name: Confluent Client Quotas (kafka-quotas/v1) API
  slug: confluent-client-quotas-kafka-quotas-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Cluster Linking (v3) API
  slug: confluent-cluster-linking-v3-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Cluster (v3) API
  slug: confluent-cluster-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Apache Kafka Clusters '
  name: Confluent Clusters (cmk/v2) API
  slug: confluent-clusters-cmk-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cluster` represents a ksqlDB runtime that you can '
  name: Confluent Clusters (ksqldbcm/v2) API
  slug: confluent-clusters-ksqldbcm-v2-api
- description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Clusters on Confluent Cloud.'
  name: Confluent Clusters (srcm/v2) API
  slug: confluent-clusters-srcm-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Clusters` objects represent Schema Registry Cluste'
  name: Confluent Clusters (srcm/v3) API
  slug: confluent-clusters-srcm-v3-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to test schema compatibility. Rela'
  name: Confluent Compatibility (v1) API
  slug: confluent-compatibility-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Compute Pool represents a set of compute resource'
  name: Confluent Compute Pools (fcpm/v2) API
  slug: confluent-compute-pools-fcpm-v2-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to manage and query schema compati'
  name: Confluent Config (v1) API
  slug: confluent-config-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Configs (v3) API
  slug: confluent-configs-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connect Artifact` objects represent collection of '
  name: Confluent Connect Artifacts (cam/v1) API
  slug: confluent-connect-artifacts-cam-v1-api
- description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `ConnectCluster` object represent Confluent Platform Connect clusters registere'
  name: Confluent Connect Clusters (usm/v1) API
  slug: confluent-connect-clusters-usm-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Connection` represents a core resource used to mod'
  name: Confluent Connections (sql/v1) API
  slug: confluent-connections-sql-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed Connectors or Custom Connectors in '
  name: Confluent Connectors (connect/v1) API
  slug: confluent-connectors-connect-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Consumer Group (v3) API
  slug: confluent-consumer-group-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerSharedResource` object contains details of'
  name: Confluent Consumer Shared Resources (cdx/v1) API
  slug: confluent-consumer-shared-resources-cdx-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ConsumerShare` object respresents the share that y'
  name: Confluent Consumer Shares (cdx/v1) API
  slug: confluent-consumer-shares-cdx-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to retrieve information about sche'
  name: Confluent Contexts (v1) API
  slug: confluent-contexts-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Cost` objects represent the aggregated billing cos'
  name: Confluent Costs (billing/v1) API
  slug: confluent-costs-billing-v1-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Custom Code Logging API EA](https://img.shield'
  name: Confluent Custom Code Loggings (ccl/v1) API
  slug: confluent-custom-code-loggings-ccl-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPluginVersion objects represent Custom'
  name: Confluent Custom Connect Plugin Versions (ccpm/v1) API
  slug: confluent-custom-connect-plugin-versions-ccpm-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectPlugins objects represent Custom Conne'
  name: Confluent Custom Connect Plugins (ccpm/v1) API
  slug: confluent-custom-connect-plugins-ccpm-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) CustomConnectorPlugins objects represent Custom Con'
  name: Confluent Custom Connector Plugins (connect/v1) API
  slug: confluent-custom-connector-plugins-connect-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of supported runtime languages for Custom Conn'
  name: Confluent Custom Connector Runtimes (connect/v1) API
  slug: confluent-custom-connector-runtimes-connect-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Data Encryption Keys (v1) API
  slug: confluent-data-encryption-keys-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add, remove, and update DNS forwarder for your gate'
  name: Confluent DNS Forwarders (networking/v1) API
  slug: confluent-dns-forwarders-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) DNS record objects are associated with Confluent Cl'
  name: Confluent DNS Records (networking/v1) API
  slug: confluent-dns-records-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An Endpoint object represents a Fully Qualified Dom'
  name: Confluent Endpoints (endpoint/v1) API
  slug: confluent-endpoints-endpoint-v1-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent Entitlements (partner/v2) API
  slug: confluent-entitlements-partner-v2-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Entity (v1) API
  slug: confluent-entity-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Environment` objects represent an isolated namespa'
  name: Confluent Environments (org/v2) API
  slug: confluent-environments-org-v2-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Exporters (v1) API
  slug: confluent-exporters-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) FlinkArtifact objects represent Flink Artifacts on '
  name: Confluent Flink Artifacts (artifact/v1) API
  slug: confluent-flink-artifacts-artifact-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Gateway represents a slice of traffic capacity in'
  name: Confluent Gateways (networking/v1) API
  slug: confluent-gateways-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `GroupMapping` objects establish relationships betw'
  name: Confluent Group Mappings (iam/v2/sso) API
  slug: confluent-group-mappings-iam-v2-sso-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityPool` objects represent groups of identiti'
  name: Confluent Identity Pools (iam/v2) API
  slug: confluent-identity-pools-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IdentityProvider` objects represent external OAuth'
  name: Confluent Identity Providers (iam/v2) API
  slug: confluent-identity-providers-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) You can create an `Integration` to specify how we c'
  name: Confluent Integrations (notifications/v1) API
  slug: confluent-integrations-notifications-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Provider Integration` objects represent access to '
  name: Confluent Integrations (pim/v1) API
  slug: confluent-integrations-pim-v1-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Provider Integration](https://img.shields.io/b'
  name: Confluent Integrations (pim/v2) API
  slug: confluent-integrations-pim-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Invitation` objects represent invitations to invit'
  name: Confluent Invitations (iam/v2) API
  slug: confluent-invitations-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) IP Addresses Related guide: [Use Public Egress IP a'
  name: Confluent IP Addresses (networking/v1) API
  slug: confluent-ip-addresses-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The IP Filter Summary endpoint returns an aggregati'
  name: Confluent IP Filter Summaries (iam/v2) API
  slug: confluent-ip-filter-summaries-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `IP Filter` objects are bindings between IP Groups '
  name: Confluent IP Filters (iam/v2) API
  slug: confluent-ip-filters-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Definitions of networks which can be named and refe'
  name: Confluent IP Groups (iam/v2) API
  slug: confluent-ip-groups-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `JWKS` objects represent public key sets for a spec'
  name: Confluent Jwks (iam/v2) API
  slug: confluent-jwks-iam-v2-api
- description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `KafkaCluster` object represent Confluent Platform Kafka clusters registered wi'
  name: Confluent Kafka Clusters (usm/v1) API
  slug: confluent-kafka-clusters-usm-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Key Encryption Keys (v1) API
  slug: confluent-key-encryption-keys-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Key` objects represent customer managed keys on de'
  name: Confluent Keys (byok/v1) API
  slug: confluent-keys-byok-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the lifecycle for a Managed Connec'
  name: Confluent Lifecycle (connect/v1) API
  slug: confluent-lifecycle-connect-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for Managed connectors in Confluent Cloud.'
  name: Confluent Managed Connector Plugins (connect/v1) API
  slug: confluent-managed-connector-plugins-connect-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTableVersion` represents a specific ve'
  name: Confluent Materialized Table Versions (sql/v1) API
  slug: confluent-materialized-table-versions-sql-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `MaterializedTable` represents a core resource used'
  name: Confluent Materialized Tables (sql/v1) API
  slug: confluent-materialized-tables-sql-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Modes (v1) API
  slug: confluent-modes-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Network Link Enpoint is associated with a Private'
  name: Confluent Network Link Endpoints (networking/v1) API
  slug: confluent-network-link-endpoints-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) List of incoming Network Link Enpoints associated w'
  name: Confluent Network Link Service Associations (networking/v1) API
  slug: confluent-network-link-service-associations-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Network Link Service is associated with a Private L'
  name: Confluent Network Link Services (networking/v1) API
  slug: confluent-network-link-services-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Network` represents a network (VPC) in Confluent C'
  name: Confluent Networks (networking/v1) API
  slug: confluent-networks-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The type of notifications (and their corresponding '
  name: Confluent Notification Types (notifications/v1) API
  slug: confluent-notification-types-notifications-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) OAuth Token is a [JSON Web Token (JWT)](https://www'
  name: Confluent OAuth Tokens (sts/v1) API
  slug: confluent-oauth-tokens-sts-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for managing the offsets for a Managed Connecto'
  name: Confluent Offsets (connect/v1) API
  slug: confluent-offsets-connect-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Stream sharing opt in options ## The Opt Ins Model '
  name: Confluent Opt Ins (cdx/v1) API
  slug: confluent-opt-ins-cdx-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `OrgComputePoolConfig` manages compute pool configu'
  name: Confluent Org Compute Pool Configs (fcpm/v2) API
  slug: confluent-org-compute-pool-configs-fcpm-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Organization` objects represent a customer organiz'
  name: Confluent Organizations (org/v2) API
  slug: confluent-organizations-org-v2-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent Organizations (partner/v2) API
  slug: confluent-organizations-partner-v2-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Partition (v3) API
  slug: confluent-partition-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove VPC/VNet peering connections between '
  name: Confluent Peerings (networking/v1) API
  slug: confluent-peerings-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Flink Artifa'
  name: Confluent Presigned Urls (artifact/v1) API
  slug: confluent-presigned-urls-artifact-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Connect Arti'
  name: Confluent Presigned Urls (cam/v1) API
  slug: confluent-presigned-urls-cam-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent Presigned Urls (ccpm/v1) API
  slug: confluent-presigned-urls-ccpm-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Request a presigned upload URL for new Custom Conne'
  name: Confluent Presigned Urls (connect/v1) API
  slug: confluent-presigned-urls-connect-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Add or remove access to PrivateLink endpoints by AW'
  name: Confluent Private Link Accesses (networking/v1) API
  slug: confluent-private-link-accesses-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment connection objects represent'
  name: Confluent Private Link Attachment Connections (networking/v1) API
  slug: confluent-private-link-attachment-connections-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) PrivateLink attachment objects represent reservatio'
  name: Confluent Private Link Attachments (networking/v1) API
  slug: confluent-private-link-attachments-networking-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderSharedResource` object contains details of'
  name: Confluent Provider Shared Resources (cdx/v1) API
  slug: confluent-provider-shared-resources-cdx-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ProviderShare` object respresents the share that y'
  name: Confluent Provider Shares (cdx/v1) API
  slug: confluent-provider-shares-cdx-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Records (v3) API
  slug: confluent-records-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions a'
  name: Confluent Regions (fcpm/v2) API
  slug: confluent-regions-fcpm-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent Regions (rtce/v1) API
  slug: confluent-regions-rtce-v1-api
- description: '[![Deprecated](https://img.shields.io/badge/Lifecycle%20Stage-Deprecated-%23ff005c)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions available when placing '
  name: Confluent Regions (srcm/v2) API
  slug: confluent-regions-srcm-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Region` objects represent cloud provider regions w'
  name: Confluent Regions (tableflow/v1) API
  slug: confluent-regions-tableflow-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourcePreference` objects represent the intent o'
  name: Confluent Resource Preferences (notifications/v1) API
  slug: confluent-resource-preferences-notifications-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ResourceSubscription` objects represent the intent'
  name: Confluent Resource Subscriptions (notifications/v1) API
  slug: confluent-resource-subscriptions-notifications-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A role binding grants a Principal a role on resourc'
  name: Confluent Role Bindings (iam/v2) API
  slug: confluent-role-bindings-iam-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) An RtceTopic represents a customer''s Kafka topic en'
  name: Confluent Rtce Topics (rtce/v1) API
  slug: confluent-rtce-topics-rtce-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Schemas (v1) API
  slug: confluent-schemas-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Gets a list of all available scopes for applied quo'
  name: Confluent Scopes (service-quota/v1) API
  slug: confluent-scopes-service-quota-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to search for entities. Related gu'
  name: Confluent Search (v1) API
  slug: confluent-search-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `ServiceAccount` objects are typically used to repr'
  name: Confluent Service Accounts (iam/v2) API
  slug: confluent-service-accounts-iam-v2-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Share Group (v3) API
  slug: confluent-share-group-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) Encrypted Token shared with consumer ## The Shared '
  name: Confluent Shared Tokens (cdx/v1) API
  slug: confluent-shared-tokens-cdx-v1-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To Partner v2](https://img.shields.io/badge/-Requ'
  name: Confluent Signup (partner/v2) API
  slug: confluent-signup-partner-v2-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementException` represents an exception of a `'
  name: Confluent Statement Exceptions (sql/v1) API
  slug: confluent-statement-exceptions-sql-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `StatementResult` represents a result of a `Stateme'
  name: Confluent Statement Results (sql/v1) API
  slug: confluent-statement-results-sql-v1-api
- description: Execute SQL statements against queryable topics and read their results. A statement that resolves quickly returns its results inline; a long-running one is assigned a background job that can be polled
  name: Confluent Statements (query/v1alpha1) API
  slug: confluent-statements-query-v1alpha1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Statement` represents a core resource used to mode'
  name: Confluent Statements (sql/v1) API
  slug: confluent-statements-sql-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) API for requesting the status or the tasks for a Ma'
  name: Confluent Status (connect/v1) API
  slug: confluent-status-connect-v1-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Streams Group (v3) API
  slug: confluent-streams-group-v3-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Subjects (v1) API
  slug: confluent-subjects-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `Subscription` objects represent the intent of the '
  name: Confluent Subscriptions (notifications/v1) API
  slug: confluent-subscriptions-notifications-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) A Tableflow Topic represents configuration related '
  name: Confluent Tableflow Topics (tableflow/v1) API
  slug: confluent-tableflow-topics-tableflow-v1-api
- description: '[![Preview](https://img.shields.io/badge/Lifecycle%20Stage-Preview-%2300afba)](#section/Versioning/API-Lifecycle-Policy) `Tool` models a reusable tool resource backed by a connection that can be refer'
  name: Confluent Tools (sql/v1) API
  slug: confluent-tools-sql-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy)'
  name: Confluent Topic (v3) API
  slug: confluent-topic-v3-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) AWS Transit Gateway Attachments Related guide: [API'
  name: Confluent Transit Gateway Attachments (networking/v1) API
  slug: confluent-transit-gateway-attachments-networking-v1-api
- description: '[![Generally Available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) The API allows you to create, retrieve, update, and d'
  name: Confluent Types (v1) API
  slug: confluent-types-v1-api
- description: '[![Early Access](https://img.shields.io/badge/Lifecycle%20Stage-Early%20Access-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) [![Request Access To User Notifications API v1](https://img.shields'
  name: Confluent User Notifications (notifications/v1) API
  slug: confluent-user-notifications-notifications-v1-api
- description: '[![General Availability](https://img.shields.io/badge/Lifecycle%20Stage-General%20Availability-%2345c6e8)](#section/Versioning/API-Lifecycle-Policy) `User` objects represent individuals who may access'
  name: Confluent Users (iam/v2) API
  slug: confluent-users-iam-v2-api
- description: '![generally-available](https://img.shields.io/badge/Lifecycle%20Stage-Generally%20Available-%230074A2) Version 2 of the Metrics API adds the ability to query metrics for Kafka Connect, ksqlDB, and Sch'
  name: Confluent Version 2 API
  slug: confluent-version-2-api
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
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/confluent-capability-edges.yml
- group: other
  title: ''
  type: Overlay
  url: overlays/confluent-cloud-overlay.yaml
- group: other
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
  title: ''
  type: Deprecation
  url: lifecycle/confluent-lifecycle.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/confluent-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/confluent-changelog.yml
- group: auth
  title: ''
  type: Security
  url: security/confluent-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/confluent-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.confluent.io/trust-and-security/
- group: design
  title: ''
  type: Conformance
  url: conformance/confluent-conformance.yml
- group: build
  title: ''
  type: Packages
  url: packages/confluent-packages.yml
- group: build
  title: ''
  type: SDKs
  url: packages/confluent-packages.yml
- group: build
  title: ''
  type: CLI
  url: cli/confluent-cli.yml
- group: start
  title: ''
  type: Sandbox
  url: sandbox/confluent-sandbox.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/confluent-conventions.yml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/confluent-problem-types.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/confluent-data-model.yml
- group: design
  title: ''
  type: Webhooks
  url: asyncapi/confluent-webhooks.yml
- group: agent
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/confluent-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/confluent-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/confluent-llms.txt
- group: commercial
  title: ''
  type: Plans
  url: plans/confluent-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/confluent-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/confluent-finops.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/confluent-scopes.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/confluent-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/confluent-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/confluent-domain-security.yml
- group: auth
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
overview: 'Confluent publishes 125 APIs on the [APIs.io](https://apis.io/) network, including ACLs API, API Keys API, Clusters API, and 122 more. Tagged areas include Data Streaming, Apache Kafka, Event Streaming, Stream Processing, and Schema Registry.


  The Confluent catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Confluent''s developer surface includes documentation, API reference, getting-started guide, support, pricing, signup flow, changelog, and 38 more developer resources.'
plans:
- name: Confluent Plans Pricing
  plan_count: 5
  slug: confluent-plans-pricing
random_paper: 8
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
  band: strong
  composite: 66.3
  coverage:
    artifact_dirs: 27
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 18.2
    contract_quality: 64.7
    developer_ergonomics: 85.7
    discoverability: 66.7
    governance: 18.2
    operational_transparency: 68.4
  previous_composite: 66.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 8
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
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
website: https://developer.confluent.io/
---

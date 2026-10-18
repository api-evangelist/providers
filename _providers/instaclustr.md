---
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 42.6
  scored_at: '2026-10-17'
agentic_access:
- acting_count: 272
  human_in_the_loop: 9
  name: Instaclustr Agentic Access
  operation_count: 539
  slug: instaclustr-agentic-access
  summary_line: 539 operations · 272 acting · 9 human-in-the-loop
api_count: 4
apis:
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Account Cluster List V2 API from Instaclustr — 1 operation(s) for account cluster list v2.
  name: Instaclustr Account Cluster List V2 API
  slug: instaclustr-account-cluster-list-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Cassandra Provisioning V2 API from Instaclustr — 10 operation(s) for apache cassandra provisioning v2.
  name: Instaclustr Apache Cassandra Provisioning V2 API
  slug: instaclustr-apache-cassandra-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka ACL V2 API from Instaclustr — 4 operation(s) for apache kafka acl v2.
  name: Instaclustr Apache Kafka ACL V2 API
  slug: instaclustr-apache-kafka-acl-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka ACL V3 API from Instaclustr — 2 operation(s) for apache kafka acl v3.
  name: Instaclustr Apache Kafka ACL V3 API
  slug: instaclustr-apache-kafka-acl-v3-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Apache Kafka Connect Mirror.
  name: Instaclustr Apache Kafka Connect Mirror V2 API
  slug: instaclustr-apache-kafka-connect-mirror-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka Connect Provisioning V2 API from Instaclustr — 6 operation(s) for apache kafka connect provisioning v2.
  name: Instaclustr Apache Kafka Connect Provisioning V2 API
  slug: instaclustr-apache-kafka-connect-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka Provisioning V2 API from Instaclustr — 6 operation(s) for apache kafka provisioning v2.
  name: Instaclustr Apache Kafka Provisioning V2 API
  slug: instaclustr-apache-kafka-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations relating to the Apache Kafka Rest Proxy user.
  name: Instaclustr Apache Kafka Provisioning V3 API
  slug: instaclustr-apache-kafka-provisioning-v3-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations relating to the Apache Kafka Rest Proxy user.
  name: Instaclustr Apache Kafka Rest Proxy User API
  slug: instaclustr-apache-kafka-rest-proxy-user-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations relating to the Apache Schema Registry user.
  name: Instaclustr Apache Kafka Schema Registry User API
  slug: instaclustr-apache-kafka-schema-registry-user-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka Tiered Storage API from Instaclustr — 4 operation(s) for apache kafka tiered storage.
  name: Instaclustr Apache Kafka Tiered Storage API
  slug: instaclustr-apache-kafka-tiered-storage-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka Topic V2 API from Instaclustr — 4 operation(s) for apache kafka topic v2.
  name: Instaclustr Apache Kafka Topic V2 API
  slug: instaclustr-apache-kafka-topic-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka Topic V3 API from Instaclustr — 2 operation(s) for apache kafka topic v3.
  name: Instaclustr Apache Kafka Topic V3 API
  slug: instaclustr-apache-kafka-topic-v3-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Kafka User API from Instaclustr — 14 operation(s) for apache kafka user.
  name: Instaclustr Apache Kafka User API
  slug: instaclustr-apache-kafka-user-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Apache Zookeeper Provisioning V2 API from Instaclustr — 5 operation(s) for apache zookeeper provisioning v2.
  name: Instaclustr Apache Zookeeper Provisioning V2 API
  slug: instaclustr-apache-zookeeper-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The AWS Encryption Key V2 API from Instaclustr — 4 operation(s) for aws encryption key v2.
  name: Instaclustr AWS Encryption Key V2 API
  slug: instaclustr-aws-encryption-key-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS endpoint dns names.
  name: Instaclustr AWS Endpoint DNS Names V2 API
  slug: instaclustr-aws-endpoint-dns-names-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS endpoint service names.
  name: Instaclustr AWS Endpoint Service Names V2 API
  slug: instaclustr-aws-endpoint-service-names-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS endpoint service principals.
  name: Instaclustr AWS Endpoint Service Principals API
  slug: instaclustr-aws-endpoint-service-principals-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS endpoint service principals.
  name: Instaclustr AWS Endpoint Service Principals V2 API
  slug: instaclustr-aws-endpoint-service-principals-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS FSx ONTAP file system provisioning
  name: Instaclustr AWS FSx ONTAP File Systems API
  slug: instaclustr-aws-fsx-ontap-file-systems-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to BYO AWS FSx ONTAP filesystem credentials
  name: Instaclustr AWS FSx ONTAP Filesystem Credentials V2 API
  slug: instaclustr-aws-fsx-ontap-filesystem-credentials-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS prefix list firewall rule
  name: Instaclustr AWS Prefix List Firewall Rule V1 API
  slug: instaclustr-aws-prefix-list-firewall-rule-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to bulk AWS prefix list firewall rule operations for a cluster data centre
  name: Instaclustr AWS Prefix List Firewall Rules V1 API
  slug: instaclustr-aws-prefix-list-firewall-rules-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS security group firewall rule
  name: Instaclustr AWS Security Group Firewall Rule V2 API
  slug: instaclustr-aws-security-group-firewall-rule-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to perform bulk operation on Cluster AWS security group firewall rules
  name: Instaclustr AWS Security Group Firewall Rules V2 API
  slug: instaclustr-aws-security-group-firewall-rules-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to AWS VPC Peering with Cluster Data Centers.
  name: Instaclustr AWS VPC Peer V2 API
  slug: instaclustr-aws-vpc-peer-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Azure Private Link Service allowed subscriptions
  name: Instaclustr Azure Private Link Service Subscriptions API
  slug: instaclustr-azure-private-link-service-subscriptions-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Azure Vnet Peering with Cluster Data Centers.
  name: Instaclustr Azure Vnet Peer V2 API
  slug: instaclustr-azure-vnet-peer-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to retrieving information on bundles.
  name: Instaclustr Bundle Information API
  slug: instaclustr-bundle-information-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to users in a bundle.
  name: Instaclustr Bundle User API
  slug: instaclustr-bundle-user-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Bring-Your-Own-Cloud (BYOC) AWS CloudFormation template.
  name: Instaclustr BYOC AWS CloudFormation API
  slug: instaclustr-byoc-aws-cloudformation-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to BYOC provider account setup records.
  name: Instaclustr BYOC AWS Provider Account Setup V1 API
  slug: instaclustr-byoc-aws-provider-account-setup-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Cadence per-frontend-instance domain request-rate limits.
  name: Instaclustr Cadence Domain Rate Limits V2 API
  slug: instaclustr-cadence-domain-rate-limits-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Cadence cluster-wide domain request-rate limits.
  name: Instaclustr Cadence Global Domain Rate Limits V2 API
  slug: instaclustr-cadence-global-domain-rate-limits-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Cadence Provisioning V2 API from Instaclustr — 5 operation(s) for cadence provisioning v2.
  name: Instaclustr Cadence Provisioning V2 API
  slug: instaclustr-cadence-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to ClickHouse configuration properties.
  name: Instaclustr ClickHouse Configurations API
  slug: instaclustr-clickhouse-configurations-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to ClickHouse integrations.
  name: Instaclustr ClickHouse Integrations API
  slug: instaclustr-clickhouse-integrations-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to ClickHouse provisioning.
  name: Instaclustr ClickHouse Provisioning API
  slug: instaclustr-clickhouse-provisioning-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Cloud provider information.
  name: Instaclustr Cloud Provider Details V2 API
  slug: instaclustr-cloud-provider-details-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to configurations of a cluster.
  name: Instaclustr Cluster Config API
  slug: instaclustr-cluster-config-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Cluster exclusion window
  name: Instaclustr Cluster Exclusion Window V2 API
  slug: instaclustr-cluster-exclusion-window-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to cluster maintenance events
  name: Instaclustr Cluster Maintenance Events V2 API
  slug: instaclustr-cluster-maintenance-events-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to cluster network firewall rule, not supported for on-premises clusters
  name: Instaclustr Cluster Network Firewall Rule V2 API
  slug: instaclustr-cluster-network-firewall-rule-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to perform bulk operation on Cluster network firewall rules, not supported for on-premises clusters
  name: Instaclustr Cluster Network Firewall Rules V2 API
  slug: instaclustr-cluster-network-firewall-rules-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Cluster non-recurring exclusion window
  name: Instaclustr Cluster Non Recurring Exclusion Window V2 API
  slug: instaclustr-cluster-non-recurring-exclusion-window-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to provisioning clusters.
  name: Instaclustr Cluster Resource API
  slug: instaclustr-cluster-resource-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Cluster Settings V2 API from Instaclustr — 1 operation(s) for cluster settings v2.
  name: Instaclustr Cluster Settings V2 API
  slug: instaclustr-cluster-settings-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to suspending and resuming clusters.
  name: Instaclustr Cluster Suspend Resume V2 API
  slug: instaclustr-cluster-suspend-resume-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to managing custom tags
  name: Instaclustr Custom Tags V2 API
  slug: instaclustr-custom-tags-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to firewall rules of a cluster.
  name: Instaclustr Firewall Rule API
  slug: instaclustr-firewall-rule-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to GCP PSC Service Attachments Accept List
  name: Instaclustr GCP PSC Service Attachments Accept List V2 API
  slug: instaclustr-gcp-psc-service-attachments-accept-list-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to GCP VPC Peering with Cluster Data Centers.
  name: Instaclustr GCP VPC Peer V2 API
  slug: instaclustr-gcp-vpc-peer-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to horizontal scaling of Cluster Data Centres.
  name: Instaclustr Horizontal Scaling Operations API
  slug: instaclustr-horizontal-scaling-operations-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Kafka Access Control Lists.
  name: Instaclustr Kafka ACL API
  slug: instaclustr-kafka-acl-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to managing mirroring setups between Kafka and Kafka Connect clusters.
  name: Instaclustr Kafka Mirroring API
  slug: instaclustr-kafka-mirroring-api-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Kafka topics.
  name: Instaclustr Kafka Topic API
  slug: instaclustr-kafka-topic-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations relating to the Karapace Rest Proxy user.
  name: Instaclustr Karapace Rest Proxy User API
  slug: instaclustr-karapace-rest-proxy-user-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations relating to the Karapace Schema Registry user.
  name: Instaclustr Karapace Schema Registry User API
  slug: instaclustr-karapace-schema-registry-user-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to managing maintenance events on Instaclustr clusters.
  name: Instaclustr Maintenance Events API
  slug: instaclustr-maintenance-events-api-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Account Management Units Usage Information
  name: Instaclustr Management Units Usage API
  slug: instaclustr-management-units-usage-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to MCP Gateway backends.
  name: Instaclustr MCP Gateway Backend V1 API
  slug: instaclustr-mcp-gateway-backend-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to MCP Gateway persona access control.
  name: Instaclustr MCP Gateway Persona Access Control V1 API
  slug: instaclustr-mcp-gateway-persona-access-control-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to MCP Gateway provisioning
  name: Instaclustr MCP Gateway Provisioning V1 API
  slug: instaclustr-mcp-gateway-provisioning-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to MCP Gateway tools
  name: Instaclustr MCP Gateway Tool V1 API
  slug: instaclustr-mcp-gateway-tool-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to MCP Gateway virtual servers.
  name: Instaclustr MCP Gateway Virtual Server V1 API
  slug: instaclustr-mcp-gateway-virtual-server-v1-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operation to retrieve metric definitions.
  name: Instaclustr Monitoring API
  slug: instaclustr-monitoring-api-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to monitoring provisioned clusters
  name: Instaclustr Monitoring API - Cluster API
  slug: instaclustr-monitoring-api-cluster-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to monitoring data centres of provisioned clusters
  name: Instaclustr Monitoring API - Data Centre API
  slug: instaclustr-monitoring-api-data-centre-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to monitoring nodes of provisioned clusters
  name: Instaclustr Monitoring API - Node API
  slug: instaclustr-monitoring-api-node-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operation related to reloading nodes.
  name: Instaclustr Node Reload API
  slug: instaclustr-node-reload-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The OpenSearch Egress Rules V2 API from Instaclustr — 3 operation(s) for opensearch egress rules v2.
  name: Instaclustr OpenSearch Egress Rules V2 API
  slug: instaclustr-opensearch-egress-rules-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to managing external S3 buckets with read-only access for OpenSearch clusters.
  name: Instaclustr OpenSearch External S3 Bucket V2 API
  slug: instaclustr-opensearch-external-s3-bucket-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The OpenSearch Provisioning V2 API from Instaclustr — 10 operation(s) for opensearch provisioning v2.
  name: Instaclustr OpenSearch Provisioning V2 API
  slug: instaclustr-opensearch-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Organization Management.<br><br>These endpoints require an Organization Management API key. Organization API keys can be retrieved any time from the <a href='https://console2.ins
  name: Instaclustr Organization Management API
  slug: instaclustr-organization-management-api-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to PostgreSQL configuration properties.
  name: Instaclustr PostgreSQL Configuration V2 API
  slug: instaclustr-postgresql-configuration-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to PostgreSQL.
  name: Instaclustr PostgreSQL Operations API
  slug: instaclustr-postgresql-operations-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to managing a Postgresql cluster
  name: Instaclustr PostgreSQL Provisioning V2 API
  slug: instaclustr-postgresql-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operation to fetch pricing information. These endpoints do not require any API keys to access. These are publicly available information.
  name: Instaclustr Pricing information - Node sizes API
  slug: instaclustr-pricing-information-node-sizes-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to Private Link / Private Service Connect Endpoint addresses
  name: Instaclustr Private Link Private Service Connect Endpoint Addresses V2 API
  slug: instaclustr-private-link-private-service-connect-endpoint-addresses-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Redis Provisioning V2 API from Instaclustr — 8 operation(s) for redis provisioning v2.
  name: Instaclustr Redis Provisioning V2 API
  slug: instaclustr-redis-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Redis User V2 API from Instaclustr — 3 operation(s) for redis user v2.
  name: Instaclustr Redis User V2 API
  slug: instaclustr-redis-user-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations and information related to resizing clusters.
  name: Instaclustr Resize Operations V2 API
  slug: instaclustr-resize-operations-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to scaling a cluster. Includes adding a new data centre and resizing a cluster.
  name: Instaclustr Scale Cluster API
  slug: instaclustr-scale-cluster-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: 'Operations related to service user management.<br>Service Users are API-only users. Service Users are created in, and have access to, a single account. This account is the account associated with the '
  name: Instaclustr Service User Management API
  slug: instaclustr-service-user-management-api-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Terraform Import V2 API from Instaclustr — 1 operation(s) for terraform import v2.
  name: Instaclustr Terraform Import V2 API
  slug: instaclustr-terraform-import-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to the user actions
  name: Instaclustr User Actions V3 API
  slug: instaclustr-user-actions-v3-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to user management. Several operations implement the <a href='http://www.simplecloud.info/#Specification' target='_blank'>SCIM 2.0 protocol</a>.<br><br>
  name: Instaclustr User Management and SCIM 2.0 API
  slug: instaclustr-user-management-and-scim-2-0-api-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Valkey Provisioning V2 API from Instaclustr — 8 operation(s) for valkey provisioning v2.
  name: Instaclustr Valkey Provisioning V2 API
  slug: instaclustr-valkey-provisioning-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: The Valkey User V2 API from Instaclustr — 3 operation(s) for valkey user v2.
  name: Instaclustr Valkey User V2 API
  slug: instaclustr-valkey-user-v2-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to VPC Peering.
  name: Instaclustr VPC Peering API
  slug: instaclustr-vpc-peering-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to backing up and restoring a cluster
  name: Instaclustr Backup And Restore API
  slug: instaclustr-backup-and-restore-api
- baseURL: https://api.instaclustr.com
  baseurl_source: declared
  description: Operations related to encryption keys.
  name: Instaclustr Encryptionkey API
  slug: instaclustr-encryptionkey-api
artifact_total: 112
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/capabilities/instaclustr-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/instaclustr-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/agentic-access/instaclustr-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/instaclustr-agentic-access.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/rate-limits/instaclustr-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/instaclustr-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/rules/instaclustr-rules.yml
  title: ''
  type: Spectral
  url: rules/instaclustr-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/json-ld/instaclustr-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/instaclustr-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/vocabulary/instaclustr-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/instaclustr-vocabulary.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/data-model/instaclustr-data-model.yml
  title: ''
  type: DataModel
  url: data-model/instaclustr-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/conventions/instaclustr-conventions.yml
  title: ''
  type: Conventions
  url: conventions/instaclustr-conventions.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://instaclustr.redoc.ly/Deprecated/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/lifecycle/instaclustr-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/instaclustr-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/errors/instaclustr-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/instaclustr-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/conformance/instaclustr-conformance.yml
  title: ''
  type: Conformance
  url: conformance/instaclustr-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/llms/instaclustr-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/instaclustr-llms.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/well-known/instaclustr-status-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/instaclustr-status-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/well-known/instaclustr-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/instaclustr-well-known.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/hosts/instaclustr-hosts.yml
  title: ''
  type: Hosts
  url: hosts/instaclustr-hosts.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/integrations/instaclustr-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/instaclustr-integration-edges.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/vendors/instaclustr-vendors.yml
  title: ''
  type: Vendors
  url: vendors/instaclustr-vendors.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/packages/instaclustr-packages.yml
  title: ''
  type: SDKs
  url: packages/instaclustr-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/packages/instaclustr-packages.yml
  title: ''
  type: Packages
  url: packages/instaclustr-packages.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.instaclustr.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/authentication/instaclustr-authentication.yml
  title: ''
  type: Authentication
  url: authentication/instaclustr-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/instaclustr/refs/heads/main/security/instaclustr-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/instaclustr-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.instaclustr.com
- group: docs
  title: ''
  type: Documentation
  url: https://www.instaclustr.com/support/documentation/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.api.instaclustr.com/
- group: company
  title: ''
  type: Blog
  url: https://www.instaclustr.com/blog/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/instaclustr
- group: start
  title: ''
  type: Login
  url: https://console2.instaclustr.com/login
- group: start
  title: ''
  type: SignUp
  url: https://console2.instaclustr.com/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://www.instaclustr.com/pricing/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.instaclustr.com/policies/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.instaclustr.com/policies/terms-of-service/
- group: operate
  title: ''
  type: Support
  url: https://support.instaclustr.com/hc/en-us
created: '2026-10-13'
description: NetApp Instaclustr is a managed platform for open source data infrastructure, running and supporting Apache Kafka, Kafka Connect, Apache Cassandra, PostgreSQL, OpenSearch, ClickHouse, Valkey and Cadence clusters in its own cloud accounts or in a customer's cloud (Bring Your Own Cloud). Its public Instaclustr API at api.instaclustr.com provides cluster management (provisioning, firewall rules, peering, users, backups, maintenance events), monitoring metrics, user/organization management with SCIM 2.0, and an MCP Gateway product for AI agents. Instaclustr is part of NetApp.
image: https://www.instaclustr.com/wp-content/uploads/Insta_Website_Social-Share-Thumbnail_rebrand.png
json_schemas:
- name: BundleCompatibilityResponseSchema
  property_count: 17
  slug: instaclustr-bundle-compatibility-response-schema
- name: CadenceClusterV2
  property_count: 19
  slug: instaclustr-cadence-cluster-v2
- name: CassandraClusterV2
  property_count: 16
  slug: instaclustr-cassandra-cluster-v2
- name: ClickHouseIntegrationS3Fsxn
  property_count: 5
  slug: instaclustr-click-house-integration-s3-fsxn
- name: ClusterDetailsResponseForTerraformImport
  property_count: 17
  slug: instaclustr-cluster-details-response-for-terraform-import
- name: ClusterProvisioningRequest
  property_count: 18
  slug: instaclustr-cluster-provisioning-request
- name: DataCentreRequest
  property_count: 8
  slug: instaclustr-data-centre-request
- name: KafkaClusterV2
  property_count: 30
  slug: instaclustr-kafka-cluster-v2
- name: KafkaClusterV3
  property_count: 30
  slug: instaclustr-kafka-cluster-v3
- name: KafkaTopicV2
  property_count: 6
  slug: instaclustr-kafka-topic-v2
- name: OpenSearchClusterV2
  property_count: 47
  slug: instaclustr-open-search-cluster-v2
- name: PostgresqlClusterV2
  property_count: 16
  slug: instaclustr-postgresql-cluster-v2
jsonld:
- class_count: 120
  name: Instaclustr Context
  property_count: 277
  slug: instaclustr-context
layout: provider
modified: '2026-10-13'
name: Instaclustr
nav: Providers
network: true
overview: 'Instaclustr publishes 93 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account Cluster List V2 API, Apache Cassandra Provisioning V2 API, Apache Kafka ACL V2 API, and 90 more. Tagged areas include Company, Apache Kafka, Apache Cassandra, PostgreSQL, and OpenSearch.


  The Instaclustr catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Instaclustr''s developer surface includes authentication, documentation, API reference, engineering blog, signup flow, pricing, support, and 28 more developer resources.'
plans:
- name: Instaclustr Plans Pricing
  plan_count: 0
  slug: instaclustr-plans-pricing
random_paper: 2
rate_limits:
- limit_count: 3
  name: Instaclustr Rate Limits
  slug: instaclustr-rate-limits
rules:
- authorship: generated
  effective_rule_count: 52
  extends:
  - spectral:oas
  name: Instaclustr API Rules
  rule_count: 11
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 4
  slug: instaclustr-rules
score:
  band: strong
  composite: 56.8
  coverage:
    artifact_dirs: 24
    catalog_earned: 77.8
    catalog_earned_first_party: 12.0
    catalog_gap: 37.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 44.7
    contract_governance: 35.6
    contract_quality: 64.0
    developer_ergonomics: 44.6
    discoverability: 78.6
    operational_transparency: 60.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 93
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 24.5
  schema_version: 0.24.0
  scored_at: '2026-10-17'
  upsert:
    applies: true
    score: 22.2
security:
- kind: authentication
  name: Instaclustr Authentication
  slug: instaclustr-authentication
  summary_line: http · 2 schemes
- kind: domain-security
  name: Instaclustr Domain Security
  slug: instaclustr-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: instaclustr
tags:
- Company
- Apache Kafka
- Apache Cassandra
- PostgreSQL
- OpenSearch
- ClickHouse
- Managed Database
- Data Streaming
- MCP
website: https://www.instaclustr.com
---

---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 28.6
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 21
  human_in_the_loop: 2
  name: Amazon Aurora Agentic Access
  operation_count: 21
  slug: amazon-aurora-agentic-access
  summary_line: 21 operations · 21 acting · 2 human-in-the-loop
api_count: 1
apis:
- baseURL: https://rds.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Aurora cluster endpoints
  name: Amazon Aurora DB Cluster Endpoints API
  slug: amazon-aurora-db-cluster-endpoints-api
- baseURL: https://rds.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Aurora cluster parameter groups
  name: Amazon Aurora DB Cluster Parameter Groups API
  slug: amazon-aurora-db-cluster-parameter-groups-api
- baseURL: https://rds.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Aurora cluster snapshots
  name: Amazon Aurora DB Cluster Snapshots API
  slug: amazon-aurora-db-cluster-snapshots-api
- baseURL: https://rds.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Aurora DB clusters
  name: Amazon Aurora DB Clusters API
  slug: amazon-aurora-db-clusters-api
- baseURL: https://rds.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Aurora DB instances within clusters
  name: Amazon Aurora DB Instances API
  slug: amazon-aurora-db-instances-api
- baseURL: https://rds.us-east-1.amazonaws.com
  baseurl_source: declared
  description: Operations for managing Aurora Global Databases
  name: Amazon Aurora Global Clusters API
  slug: amazon-aurora-global-clusters-api
artifact_total: 210
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Aurora DB Cluster Endpoints API
  slug: open-amazon-aurora-db-cluster-endpoints-api
- collection_type: open
  name: Amazon Aurora DB Cluster Endpoints DB Cluster Parameter Groups API
  slug: open-amazon-aurora-db-cluster-parameter-groups-api
- collection_type: open
  name: Amazon Aurora DB Cluster Endpoints DB Cluster Snapshots API
  slug: open-amazon-aurora-db-cluster-snapshots-api
- collection_type: open
  name: Amazon Aurora DB Cluster Endpoints DB Clusters API
  slug: open-amazon-aurora-db-clusters-api
- collection_type: open
  name: Amazon Aurora DB Cluster Endpoints DB Instances API
  slug: open-amazon-aurora-db-instances-api
- collection_type: open
  name: Amazon Aurora DB Cluster Endpoints Global Clusters API
  slug: open-amazon-aurora-global-clusters-api
common:
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-aurora-openapi-overlay.yaml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-aurora-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-aurora-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-aurora-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-aurora-authentication.yml
- group: build
  title: ''
  type: Packages
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/packages/amazon-aurora-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/mcp/amazon-aurora-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/well-known/amazon-aurora-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/well-known/amazon-aurora-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/llms/amazon-aurora-llms.txt
- group: design
  title: ''
  type: Lifecycle
  url: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/lifecycle/amazon-aurora-lifecycle.yml
created: '2024-01-15'
description: Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.
examples:
- key_count: 3
  name: Aurora Create Db Cluster Endpoint Input Example
  slug: aurora-create-db-cluster-endpoint-input-example
- key_count: 3
  name: Aurora Create Db Cluster Endpoint Output Example
  slug: aurora-create-db-cluster-endpoint-output-example
- key_count: 3
  name: Aurora Create Db Cluster Input Example
  slug: aurora-create-db-cluster-input-example
- key_count: 3
  name: Aurora Create Db Cluster Output Example
  slug: aurora-create-db-cluster-output-example
- key_count: 3
  name: Aurora Create Db Cluster Parameter Group Input Example
  slug: aurora-create-db-cluster-parameter-group-input-example
- key_count: 3
  name: Aurora Create Db Cluster Parameter Group Output Example
  slug: aurora-create-db-cluster-parameter-group-output-example
- key_count: 3
  name: Aurora Create Db Cluster Snapshot Input Example
  slug: aurora-create-db-cluster-snapshot-input-example
- key_count: 3
  name: Aurora Create Db Cluster Snapshot Output Example
  slug: aurora-create-db-cluster-snapshot-output-example
- key_count: 3
  name: Aurora Create Db Instance Input Example
  slug: aurora-create-db-instance-input-example
- key_count: 3
  name: Aurora Create Db Instance Output Example
  slug: aurora-create-db-instance-output-example
- key_count: 3
  name: Aurora Create Global Cluster Input Example
  slug: aurora-create-global-cluster-input-example
- key_count: 3
  name: Aurora Create Global Cluster Output Example
  slug: aurora-create-global-cluster-output-example
- key_count: 3
  name: Aurora Db Cluster Endpoint Example
  slug: aurora-db-cluster-endpoint-example
- key_count: 3
  name: Aurora Db Cluster Example
  slug: aurora-db-cluster-example
- key_count: 3
  name: Aurora Db Cluster Member Example
  slug: aurora-db-cluster-member-example
- key_count: 3
  name: Aurora Db Cluster Parameter Group Example
  slug: aurora-db-cluster-parameter-group-example
- key_count: 3
  name: Aurora Db Cluster Snapshot Example
  slug: aurora-db-cluster-snapshot-example
- key_count: 3
  name: Aurora Db Instance Example
  slug: aurora-db-instance-example
- key_count: 3
  name: Aurora Delete Db Cluster Input Example
  slug: aurora-delete-db-cluster-input-example
- key_count: 3
  name: Aurora Delete Db Cluster Output Example
  slug: aurora-delete-db-cluster-output-example
- key_count: 3
  name: Aurora Delete Db Cluster Snapshot Input Example
  slug: aurora-delete-db-cluster-snapshot-input-example
- key_count: 3
  name: Aurora Delete Db Cluster Snapshot Output Example
  slug: aurora-delete-db-cluster-snapshot-output-example
- key_count: 3
  name: Aurora Delete Db Instance Input Example
  slug: aurora-delete-db-instance-input-example
- key_count: 3
  name: Aurora Delete Db Instance Output Example
  slug: aurora-delete-db-instance-output-example
- key_count: 3
  name: Aurora Delete Global Cluster Input Example
  slug: aurora-delete-global-cluster-input-example
- key_count: 3
  name: Aurora Delete Global Cluster Output Example
  slug: aurora-delete-global-cluster-output-example
- key_count: 3
  name: Aurora Describe Db Cluster Endpoints Input Example
  slug: aurora-describe-db-cluster-endpoints-input-example
- key_count: 3
  name: Aurora Describe Db Cluster Endpoints Output Example
  slug: aurora-describe-db-cluster-endpoints-output-example
- key_count: 3
  name: Aurora Describe Db Cluster Parameter Groups Input Example
  slug: aurora-describe-db-cluster-parameter-groups-input-example
- key_count: 3
  name: Aurora Describe Db Cluster Parameter Groups Output Example
  slug: aurora-describe-db-cluster-parameter-groups-output-example
- key_count: 3
  name: Aurora Describe Db Cluster Snapshots Input Example
  slug: aurora-describe-db-cluster-snapshots-input-example
- key_count: 3
  name: Aurora Describe Db Cluster Snapshots Output Example
  slug: aurora-describe-db-cluster-snapshots-output-example
- key_count: 3
  name: Aurora Describe Db Clusters Input Example
  slug: aurora-describe-db-clusters-input-example
- key_count: 3
  name: Aurora Describe Db Clusters Output Example
  slug: aurora-describe-db-clusters-output-example
- key_count: 3
  name: Aurora Describe Db Instances Input Example
  slug: aurora-describe-db-instances-input-example
- key_count: 3
  name: Aurora Describe Db Instances Output Example
  slug: aurora-describe-db-instances-output-example
- key_count: 3
  name: Aurora Describe Global Clusters Input Example
  slug: aurora-describe-global-clusters-input-example
- key_count: 3
  name: Aurora Describe Global Clusters Output Example
  slug: aurora-describe-global-clusters-output-example
- key_count: 3
  name: Aurora Endpoint Example
  slug: aurora-endpoint-example
- key_count: 3
  name: Aurora Filter Example
  slug: aurora-filter-example
- key_count: 3
  name: Aurora Global Cluster Example
  slug: aurora-global-cluster-example
- key_count: 3
  name: Aurora Global Cluster Member Example
  slug: aurora-global-cluster-member-example
- key_count: 3
  name: Aurora Modify Db Cluster Input Example
  slug: aurora-modify-db-cluster-input-example
- key_count: 3
  name: Aurora Modify Db Cluster Output Example
  slug: aurora-modify-db-cluster-output-example
- key_count: 3
  name: Aurora Reboot Db Cluster Input Example
  slug: aurora-reboot-db-cluster-input-example
- key_count: 3
  name: Aurora Reboot Db Cluster Output Example
  slug: aurora-reboot-db-cluster-output-example
- key_count: 3
  name: Aurora Restore Db Cluster From Snapshot Input Example
  slug: aurora-restore-db-cluster-from-snapshot-input-example
- key_count: 3
  name: Aurora Restore Db Cluster From Snapshot Output Example
  slug: aurora-restore-db-cluster-from-snapshot-output-example
- key_count: 3
  name: Aurora Start Db Cluster Input Example
  slug: aurora-start-db-cluster-input-example
- key_count: 3
  name: Aurora Start Db Cluster Output Example
  slug: aurora-start-db-cluster-output-example
- key_count: 3
  name: Aurora Stop Db Cluster Input Example
  slug: aurora-stop-db-cluster-input-example
- key_count: 3
  name: Aurora Stop Db Cluster Output Example
  slug: aurora-stop-db-cluster-output-example
- key_count: 3
  name: Aurora Tag Example
  slug: aurora-tag-example
- key_count: 3
  name: Aurora Vpc Security Group Membership Example
  slug: aurora-vpc-security-group-membership-example
features:
- MySQL and PostgreSQL compatible relational database engine
- Up to 5x throughput of standard MySQL and 3x of standard PostgreSQL
- Auto-scaling storage from 10GB to 128TB
- Up to 15 low-latency read replicas
- Aurora Serverless for intermittent and unpredictable workloads
- Aurora Global Database for multi-region deployments
- Continuous backup to Amazon S3 with point-in-time recovery
- Fast database cloning for testing and development
- Parallel query for faster analytical queries
- Machine learning integration through Aurora ML
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-aurora.png
integrations:
- Amazon RDS
- Amazon S3
- AWS Lambda
- Amazon CloudWatch
- AWS IAM
- Amazon VPC
- AWS KMS
- AWS Secrets Manager
- Amazon SageMaker
- AWS DMS
json_schemas:
- name: Amazon Aurora DB Cluster
  property_count: 22
  slug: amazon-aurora
- name: CreateDBClusterEndpointInput
  property_count: 0
  slug: aurora-create-db-cluster-endpoint-input
- name: CreateDBClusterEndpointOutput
  property_count: 0
  slug: aurora-create-db-cluster-endpoint-output
- name: CreateDBClusterInput
  property_count: 0
  slug: aurora-create-db-cluster-input
- name: CreateDBClusterOutput
  property_count: 0
  slug: aurora-create-db-cluster-output
- name: CreateDBClusterParameterGroupInput
  property_count: 0
  slug: aurora-create-db-cluster-parameter-group-input
- name: CreateDBClusterParameterGroupOutput
  property_count: 0
  slug: aurora-create-db-cluster-parameter-group-output
- name: CreateDBClusterSnapshotInput
  property_count: 0
  slug: aurora-create-db-cluster-snapshot-input
- name: CreateDBClusterSnapshotOutput
  property_count: 0
  slug: aurora-create-db-cluster-snapshot-output
- name: CreateDBInstanceInput
  property_count: 0
  slug: aurora-create-db-instance-input
- name: CreateDBInstanceOutput
  property_count: 0
  slug: aurora-create-db-instance-output
- name: CreateGlobalClusterInput
  property_count: 0
  slug: aurora-create-global-cluster-input
- name: CreateGlobalClusterOutput
  property_count: 0
  slug: aurora-create-global-cluster-output
- name: DBClusterEndpoint
  property_count: 0
  slug: aurora-db-cluster-endpoint
- name: DBClusterMember
  property_count: 0
  slug: aurora-db-cluster-member
- name: DBClusterParameterGroup
  property_count: 0
  slug: aurora-db-cluster-parameter-group
- name: DBCluster
  property_count: 0
  slug: aurora-db-cluster
- name: DBClusterSnapshot
  property_count: 0
  slug: aurora-db-cluster-snapshot
- name: DBInstance
  property_count: 0
  slug: aurora-db-instance
- name: DeleteDBClusterInput
  property_count: 0
  slug: aurora-delete-db-cluster-input
- name: DeleteDBClusterOutput
  property_count: 0
  slug: aurora-delete-db-cluster-output
- name: DeleteDBClusterSnapshotInput
  property_count: 0
  slug: aurora-delete-db-cluster-snapshot-input
- name: DeleteDBClusterSnapshotOutput
  property_count: 0
  slug: aurora-delete-db-cluster-snapshot-output
- name: DeleteDBInstanceInput
  property_count: 0
  slug: aurora-delete-db-instance-input
- name: DeleteDBInstanceOutput
  property_count: 0
  slug: aurora-delete-db-instance-output
- name: DeleteGlobalClusterInput
  property_count: 0
  slug: aurora-delete-global-cluster-input
- name: DeleteGlobalClusterOutput
  property_count: 0
  slug: aurora-delete-global-cluster-output
- name: DescribeDBClusterEndpointsInput
  property_count: 0
  slug: aurora-describe-db-cluster-endpoints-input
- name: DescribeDBClusterEndpointsOutput
  property_count: 0
  slug: aurora-describe-db-cluster-endpoints-output
- name: DescribeDBClusterParameterGroupsInput
  property_count: 0
  slug: aurora-describe-db-cluster-parameter-groups-input
- name: DescribeDBClusterParameterGroupsOutput
  property_count: 0
  slug: aurora-describe-db-cluster-parameter-groups-output
- name: DescribeDBClusterSnapshotsInput
  property_count: 0
  slug: aurora-describe-db-cluster-snapshots-input
- name: DescribeDBClusterSnapshotsOutput
  property_count: 0
  slug: aurora-describe-db-cluster-snapshots-output
- name: DescribeDBClustersInput
  property_count: 0
  slug: aurora-describe-db-clusters-input
- name: DescribeDBClustersOutput
  property_count: 0
  slug: aurora-describe-db-clusters-output
- name: DescribeDBInstancesInput
  property_count: 0
  slug: aurora-describe-db-instances-input
- name: DescribeDBInstancesOutput
  property_count: 0
  slug: aurora-describe-db-instances-output
- name: DescribeGlobalClustersInput
  property_count: 0
  slug: aurora-describe-global-clusters-input
- name: DescribeGlobalClustersOutput
  property_count: 0
  slug: aurora-describe-global-clusters-output
- name: Endpoint
  property_count: 0
  slug: aurora-endpoint
- name: Filter
  property_count: 0
  slug: aurora-filter
- name: GlobalClusterMember
  property_count: 0
  slug: aurora-global-cluster-member
- name: GlobalCluster
  property_count: 0
  slug: aurora-global-cluster
- name: ModifyDBClusterInput
  property_count: 0
  slug: aurora-modify-db-cluster-input
- name: ModifyDBClusterOutput
  property_count: 0
  slug: aurora-modify-db-cluster-output
- name: RebootDBClusterInput
  property_count: 0
  slug: aurora-reboot-db-cluster-input
- name: RebootDBClusterOutput
  property_count: 0
  slug: aurora-reboot-db-cluster-output
- name: RestoreDBClusterFromSnapshotInput
  property_count: 0
  slug: aurora-restore-db-cluster-from-snapshot-input
- name: RestoreDBClusterFromSnapshotOutput
  property_count: 0
  slug: aurora-restore-db-cluster-from-snapshot-output
- name: StartDBClusterInput
  property_count: 0
  slug: aurora-start-db-cluster-input
- name: StartDBClusterOutput
  property_count: 0
  slug: aurora-start-db-cluster-output
- name: StopDBClusterInput
  property_count: 0
  slug: aurora-stop-db-cluster-input
- name: StopDBClusterOutput
  property_count: 0
  slug: aurora-stop-db-cluster-output
- name: Tag
  property_count: 0
  slug: aurora-tag
- name: VpcSecurityGroupMembership
  property_count: 0
  slug: aurora-vpc-security-group-membership
json_structures:
- name: Aurora Create Db Cluster Endpoint Input Structure
  property_count: 0
  slug: aurora-create-db-cluster-endpoint-input-structure
- name: Aurora Create Db Cluster Endpoint Output Structure
  property_count: 0
  slug: aurora-create-db-cluster-endpoint-output-structure
- name: Aurora Create Db Cluster Input Structure
  property_count: 0
  slug: aurora-create-db-cluster-input-structure
- name: Aurora Create Db Cluster Output Structure
  property_count: 0
  slug: aurora-create-db-cluster-output-structure
- name: Aurora Create Db Cluster Parameter Group Input Structure
  property_count: 0
  slug: aurora-create-db-cluster-parameter-group-input-structure
- name: Aurora Create Db Cluster Parameter Group Output Structure
  property_count: 0
  slug: aurora-create-db-cluster-parameter-group-output-structure
- name: Aurora Create Db Cluster Snapshot Input Structure
  property_count: 0
  slug: aurora-create-db-cluster-snapshot-input-structure
- name: Aurora Create Db Cluster Snapshot Output Structure
  property_count: 0
  slug: aurora-create-db-cluster-snapshot-output-structure
- name: Aurora Create Db Instance Input Structure
  property_count: 0
  slug: aurora-create-db-instance-input-structure
- name: Aurora Create Db Instance Output Structure
  property_count: 0
  slug: aurora-create-db-instance-output-structure
- name: Aurora Create Global Cluster Input Structure
  property_count: 0
  slug: aurora-create-global-cluster-input-structure
- name: Aurora Create Global Cluster Output Structure
  property_count: 0
  slug: aurora-create-global-cluster-output-structure
- name: Aurora Db Cluster Endpoint Structure
  property_count: 0
  slug: aurora-db-cluster-endpoint-structure
- name: Aurora Db Cluster Member Structure
  property_count: 0
  slug: aurora-db-cluster-member-structure
- name: Aurora Db Cluster Parameter Group Structure
  property_count: 0
  slug: aurora-db-cluster-parameter-group-structure
- name: Aurora Db Cluster Snapshot Structure
  property_count: 0
  slug: aurora-db-cluster-snapshot-structure
- name: Aurora Db Cluster Structure
  property_count: 0
  slug: aurora-db-cluster-structure
- name: Aurora Db Instance Structure
  property_count: 0
  slug: aurora-db-instance-structure
- name: Aurora Delete Db Cluster Input Structure
  property_count: 0
  slug: aurora-delete-db-cluster-input-structure
- name: Aurora Delete Db Cluster Output Structure
  property_count: 0
  slug: aurora-delete-db-cluster-output-structure
- name: Aurora Delete Db Cluster Snapshot Input Structure
  property_count: 0
  slug: aurora-delete-db-cluster-snapshot-input-structure
- name: Aurora Delete Db Cluster Snapshot Output Structure
  property_count: 0
  slug: aurora-delete-db-cluster-snapshot-output-structure
- name: Aurora Delete Db Instance Input Structure
  property_count: 0
  slug: aurora-delete-db-instance-input-structure
- name: Aurora Delete Db Instance Output Structure
  property_count: 0
  slug: aurora-delete-db-instance-output-structure
- name: Aurora Delete Global Cluster Input Structure
  property_count: 0
  slug: aurora-delete-global-cluster-input-structure
- name: Aurora Delete Global Cluster Output Structure
  property_count: 0
  slug: aurora-delete-global-cluster-output-structure
- name: Aurora Describe Db Cluster Endpoints Input Structure
  property_count: 0
  slug: aurora-describe-db-cluster-endpoints-input-structure
- name: Aurora Describe Db Cluster Endpoints Output Structure
  property_count: 0
  slug: aurora-describe-db-cluster-endpoints-output-structure
- name: Aurora Describe Db Cluster Parameter Groups Input Structure
  property_count: 0
  slug: aurora-describe-db-cluster-parameter-groups-input-structure
- name: Aurora Describe Db Cluster Parameter Groups Output Structure
  property_count: 0
  slug: aurora-describe-db-cluster-parameter-groups-output-structure
- name: Aurora Describe Db Cluster Snapshots Input Structure
  property_count: 0
  slug: aurora-describe-db-cluster-snapshots-input-structure
- name: Aurora Describe Db Cluster Snapshots Output Structure
  property_count: 0
  slug: aurora-describe-db-cluster-snapshots-output-structure
- name: Aurora Describe Db Clusters Input Structure
  property_count: 0
  slug: aurora-describe-db-clusters-input-structure
- name: Aurora Describe Db Clusters Output Structure
  property_count: 0
  slug: aurora-describe-db-clusters-output-structure
- name: Aurora Describe Db Instances Input Structure
  property_count: 0
  slug: aurora-describe-db-instances-input-structure
- name: Aurora Describe Db Instances Output Structure
  property_count: 0
  slug: aurora-describe-db-instances-output-structure
- name: Aurora Describe Global Clusters Input Structure
  property_count: 0
  slug: aurora-describe-global-clusters-input-structure
- name: Aurora Describe Global Clusters Output Structure
  property_count: 0
  slug: aurora-describe-global-clusters-output-structure
- name: Aurora Endpoint Structure
  property_count: 0
  slug: aurora-endpoint-structure
- name: Aurora Filter Structure
  property_count: 0
  slug: aurora-filter-structure
- name: Aurora Global Cluster Member Structure
  property_count: 0
  slug: aurora-global-cluster-member-structure
- name: Aurora Global Cluster Structure
  property_count: 0
  slug: aurora-global-cluster-structure
- name: Aurora Modify Db Cluster Input Structure
  property_count: 0
  slug: aurora-modify-db-cluster-input-structure
- name: Aurora Modify Db Cluster Output Structure
  property_count: 0
  slug: aurora-modify-db-cluster-output-structure
- name: Aurora Reboot Db Cluster Input Structure
  property_count: 0
  slug: aurora-reboot-db-cluster-input-structure
- name: Aurora Reboot Db Cluster Output Structure
  property_count: 0
  slug: aurora-reboot-db-cluster-output-structure
- name: Aurora Restore Db Cluster From Snapshot Input Structure
  property_count: 0
  slug: aurora-restore-db-cluster-from-snapshot-input-structure
- name: Aurora Restore Db Cluster From Snapshot Output Structure
  property_count: 0
  slug: aurora-restore-db-cluster-from-snapshot-output-structure
- name: Aurora Start Db Cluster Input Structure
  property_count: 0
  slug: aurora-start-db-cluster-input-structure
- name: Aurora Start Db Cluster Output Structure
  property_count: 0
  slug: aurora-start-db-cluster-output-structure
- name: Aurora Stop Db Cluster Input Structure
  property_count: 0
  slug: aurora-stop-db-cluster-input-structure
- name: Aurora Stop Db Cluster Output Structure
  property_count: 0
  slug: aurora-stop-db-cluster-output-structure
- name: Aurora Tag Structure
  property_count: 0
  slug: aurora-tag-structure
- name: Aurora Vpc Security Group Membership Structure
  property_count: 0
  slug: aurora-vpc-security-group-membership-structure
jsonld:
- class_count: 0
  name: Amazon Aurora Context
  property_count: 4
  slug: amazon-aurora-context
layout: provider
mcp_servers:
- description: ''
  name: Amazon Aurora MCP Server
  slug: amazon-aurora-mcp-server
modified: '2026-06-20'
name: Amazon Aurora
nav: Providers
network: true
overview: 'Amazon Aurora publishes 6 APIs on the [APIs.io](https://apis.io/) network, including DB Cluster Endpoints API, DB Cluster Parameter Groups API, DB Cluster Snapshots API, and 3 more. Tagged areas include Amazon Aurora, MySQL, PostgreSQL, and Relational Database.


  The Amazon Aurora catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Aurora''s developer surface includes authentication and 10 more developer resources.'
random_paper: 18
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Aurora API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-aurora-jsonschema-spectral-rules
- effective_rule_count: 61
  extends:
  - spectral:oas
  name: Amazon Aurora API Rules
  rule_count: 20
  severity_counts:
    error: 9
    hint: 0
    info: 0
    warn: 11
  slug: amazon-aurora-spectral-rules
score:
  band: thin
  composite: 32.2
  coverage:
    artifact_dirs: 20
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 33.3
    contract_quality: 72.1
    developer_ergonomics: 11.9
    discoverability: 77.8
    governance: 33.3
    operational_transparency: 0.0
  previous_composite: 32.2
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
    mcp: first-party
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-aurora/refs/heads/main/screenshots/amazon-aurora-2026-07-25T195929.png
security:
- kind: authentication
  name: Amazon Aurora Authentication
  slug: amazon-aurora-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Aurora Domain Security
  slug: amazon-aurora-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Aurora Vulnerability Disclosure
  slug: amazon-aurora-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: amazon-aurora
tags:
- Amazon Aurora
- MySQL
- PostgreSQL
- Relational Database
use_cases:
- Enterprise applications requiring high availability and durability
- SaaS applications needing scalable multi-tenant databases
- E-commerce platforms with variable traffic patterns
- Financial applications requiring ACID compliance
- Global applications needing low-latency multi-region access
- Development and testing with fast database cloning
---

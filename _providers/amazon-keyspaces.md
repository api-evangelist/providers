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
  band: agent-aware
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
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 21.5
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 6
  human_in_the_loop: 0
  name: Amazon Keyspaces Agentic Access
  operation_count: 10
  slug: amazon-keyspaces-agentic-access
  summary_line: 10 operations · 6 acting
api_count: 1
apis:
- baseURL: https://cassandra.amazonaws.com
  baseurl_source: declared
  description: Cassandra keyspace management
  name: Amazon Keyspaces Keyspaces API
  slug: amazon-keyspaces-keyspaces-api
- baseURL: https://cassandra.amazonaws.com
  baseurl_source: declared
  description: Cassandra table management
  name: Amazon Keyspaces Tables API
  slug: amazon-keyspaces-tables-api
arazzos:
- description: Read a source table's schema and create a new table from it in a target keyspace.
  name: Amazon Keyspaces Clone Table Schema
  slug: amazon-keyspaces-clone-table-workflow
- description: Delete a table, wait for it to drain, then delete its keyspace.
  name: Amazon Keyspaces Decommission Keyspace
  slug: amazon-keyspaces-decommission-keyspace-workflow
- description: Confirm a keyspace, add a table, then list its tables to verify the table appears.
  name: Amazon Keyspaces Keyspace Inventory
  slug: amazon-keyspaces-keyspace-inventory-workflow
- description: Create a keyspace, add a table to it, and wait until the table is ACTIVE.
  name: Amazon Keyspaces Provision Table
  slug: amazon-keyspaces-provision-table-workflow
- description: Restore a table to a point in time and wait for the restored copy to be ACTIVE.
  name: Amazon Keyspaces Restore Table
  slug: amazon-keyspaces-restore-table-workflow
- description: Add columns to an existing table and wait for it to return to ACTIVE.
  name: Amazon Keyspaces Update Table Schema
  slug: amazon-keyspaces-update-table-schema-workflow
artifact_total: 40
collections:
- collection_type: postman
  name: Amazon Keyspaces API
  slug: postman-amazon-keyspaces
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Keyspaces API
  slug: open-amazon-keyspaces-keyspaces-api
- collection_type: open
  name: Amazon Keyspaces Tables API
  slug: open-amazon-keyspaces-tables-api
- collection_type: open
  name: Amazon Keyspaces API
  slug: open-amazon-keyspaces
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-keyspaces-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-keyspaces-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-keyspaces-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-keyspaces-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-keyspaces-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-keyspaces/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-keyspaces-clone-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-keyspaces-decommission-keyspace-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-keyspaces-keyspace-inventory-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-keyspaces-provision-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-keyspaces-restore-table-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-keyspaces-update-table-schema-workflow.yml
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/database/category/database/amazon-keyspaces/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/keyspaces/home
- group: build
  title: ''
  type: CLI
  url: https://docs.aws.amazon.com/cli/latest/reference/keyspaces/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/tools/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.aws.amazon.com/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/keyspaces/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/keyspaces/
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/keyspaces/pricing/
- group: start
  title: ''
  type: GettingStarted
  url: https://aws.amazon.com/keyspaces/getting-started/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/keyspaces/faqs/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-keyspaces-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-keyspaces-vocabulary.yaml
created: '2024-01-15'
description: Amazon Keyspaces (for Apache Cassandra) is a scalable, highly available, and managed Apache Cassandra-compatible database service that lets you run Cassandra workloads on AWS without managing servers or software.
examples:
- key_count: 3
  name: Amazon Keyspaces Keyspace Example
  slug: amazon-keyspaces-keyspace-example
- key_count: 5
  name: Amazon Keyspaces Table Example
  slug: amazon-keyspaces-table-example
features:
- description: Fully compatible with Apache Cassandra drivers, tools, and applications with no code changes required.
  name: Cassandra Compatibility
- description: Automatically scales table throughput and storage up and down based on application traffic.
  name: Serverless Scaling
- description: Continuous backup with PITR enables restoration of tables to any second within the last 35 days.
  name: Point-in-Time Recovery
- description: Data is encrypted at rest by default using AWS managed keys or customer-managed keys via AWS KMS.
  name: Encryption at Rest
- description: Access Amazon Keyspaces from within VPCs using VPC endpoints for enhanced network security.
  name: Virtual Private Cloud (VPC) Support
- description: Choose on-demand or provisioned capacity mode with auto scaling for predictable workloads.
  name: Capacity Modes
finops:
- name: Amazon Keyspaces Finops
  service_category: API
  slug: amazon-keyspaces-finops
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: Keyspace
  property_count: 3
  slug: amazon-keyspaces-keyspace
- name: Table
  property_count: 5
  slug: amazon-keyspaces-table
json_structures:
- name: Amazon Keyspaces Keyspace Structure
  property_count: 3
  slug: amazon-keyspaces-keyspace-structure
- name: Amazon Keyspaces Table Structure
  property_count: 5
  slug: amazon-keyspaces-table-structure
jsonld:
- class_count: 2
  name: Amazon Keyspaces Context
  property_count: 7
  slug: amazon-keyspaces-context
layout: provider
modified: '2026-05-19'
name: Amazon Keyspaces
nav: Providers
network: true
overview: 'Amazon Keyspaces publishes 2 APIs on the [APIs.io](https://apis.io/) network: Keyspaces API and Tables API. Tagged areas include Cassandra, Database, Managed Database, NoSQL, and Wide Column.


  The Amazon Keyspaces catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Keyspaces'' developer surface includes authentication, engineering blog, support, developer console, CLI, developer portal, documentation, and 23 more developer resources.'
plans:
- name: Amazon Keyspaces Plans Pricing
  plan_count: 3
  slug: amazon-keyspaces-plans-pricing
random_paper: 0
rate_limits:
- limit_count: 5
  name: Amazon Keyspaces Rate Limits
  slug: amazon-keyspaces-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Keyspaces API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-keyspaces-jsonschema-spectral-rules
- effective_rule_count: 65
  extends:
  - spectral:oas
  name: Amazon Keyspaces API Rules
  rule_count: 24
  severity_counts:
    error: 9
    hint: 0
    info: 1
    warn: 14
  slug: amazon-keyspaces-spectral-rules
score:
  band: strong
  composite: 62.0
  coverage:
    artifact_dirs: 18
    catalog_earned: 70.5
    catalog_earned_first_party: 0.0
    catalog_gap: 44.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 28.8
    contract_quality: 67.3
    developer_ergonomics: 77.4
    discoverability: 75.9
    governance: 28.8
    operational_transparency: 26.3
  previous_composite: 62.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-keyspaces/refs/heads/main/screenshots/amazon-keyspaces-2026-06-20T171716.png
security:
- kind: authentication
  name: Amazon Keyspaces Authentication
  slug: amazon-keyspaces-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Keyspaces Domain Security
  slug: amazon-keyspaces-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Keyspaces Vulnerability Disclosure
  slug: amazon-keyspaces-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Keyspaces Trust Center
  slug: amazon-keyspaces-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-keyspaces
tags:
- Cassandra
- Database
- Managed Database
- NoSQL
- Wide Column
use_cases:
- description: Store high-volume sensor data and telemetry from IoT devices with wide-column schema.
  name: IoT Data Storage
- description: Track user events, clickstreams, and behavioral data at massive scale.
  name: User Activity Tracking
- description: Manage time-series data for monitoring, metrics, and log aggregation.
  name: Time-Series Data
- description: Lift and shift existing Cassandra applications to a fully managed cloud service.
  name: Migrate Cassandra Workloads
website: https://aws.amazon.com/keyspaces/
---

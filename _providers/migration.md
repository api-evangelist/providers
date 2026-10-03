---
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 0.0
  scored_at: '2026-10-03'
api_count: 0
artifact_total: 30
common:
- group: start
  title: ''
  type: Portal
  url: https://apievangelist.com
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/api-evangelist
created: '2026-05-19'
description: An index and topic collection covering data migration, cloud migration, database migration, and API migration platforms and services. Migration platforms help organizations move workloads, databases, files, accounts, and applications between environments, providers, or schemas while preserving integrity, minimizing downtime, and tracking cutover progress. This collection includes cloud migration services like AWS Application Migration Service, Azure Migrate, and Google Cloud Migration Center; database migration and replication tools like AWS DMS, Oracle GoldenGate, and Google Cloud Datastream; modern data movement platforms like Airbyte, Fivetran, and Hotglue; and code, content, and tenant migration tooling used during platform changeovers.
examples:
- key_count: 11
  name: Migration Cutover Plan Example
  slug: migration-cutover-plan-example
- key_count: 13
  name: Migration Migration Project Example
  slug: migration-migration-project-example
features:
- description: Services like AWS Application Migration Service, Azure Migrate, and Google Cloud Migration Center lift and shift servers, VMs, and applications between data centers and cloud providers with assessment, replication, and cutover tooling.
  name: Cloud Workload Migration
- description: Database migration services like AWS DMS, Oracle GoldenGate, and Google Cloud Datastream replicate transactional data between heterogeneous database engines with change data capture and minimal downtime cutover.
  name: Database Migration and Replication
- description: Tooling like dbt, Liquibase, and Flyway version, diff, and apply schema and transformation changes through migration files checked into source control alongside application code.
  name: Schema Migration and Versioning
- description: Platforms like Airbyte, Fivetran, Hotglue, and Stitch extract data from SaaS sources, APIs, and databases and load it into warehouses and lakes with managed connectors and incremental sync.
  name: ETL and Data Movement
- description: Tools like Debezium and Kafka Connect stream row-level database changes as events, enabling near-real-time replication, audit trails, and downstream system synchronization during long-running migrations.
  name: Change Data Capture
- description: Migration assessment tools inventory existing servers, applications, dependencies, and licenses to plan target architecture, sizing, and migration waves before cutover begins.
  name: Assessment and Discovery
- description: Migration platforms coordinate rehearsals, dependency ordering, cutover windows, validation gates, and rollback procedures to reduce blast radius during go-live.
  name: Cutover Planning and Rollback
- description: SDK and API migration tooling like Liblab and OpenRewrite regenerate client libraries and rewrite consumer code when APIs change versions, providers, or specification standards.
  name: API and Code Migration
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/apis-json-logo.jpg
integrations:
- description: Managed database migration and replication service supporting homogeneous and heterogeneous migrations between Oracle, SQL Server, MySQL, Postgres, Aurora, and analytics targets.
  name: AWS Database Migration Service
- description: Unified hub for discovery, assessment, and migration of servers, databases, web apps, and virtual desktops to Microsoft Azure.
  name: Azure Migrate
- description: Serverless change data capture and replication service streaming changes from Oracle, MySQL, and Postgres into BigQuery, Cloud SQL, and Cloud Storage.
  name: Google Cloud Datastream
- description: Open-source data integration platform with 350+ connectors for moving data from SaaS and database sources into warehouses and lakes.
  name: Airbyte
- description: Managed ELT platform with automated schema migration, normalization, and incremental replication from operational sources to cloud data warehouses.
  name: Fivetran
- description: Real-time data replication and integration platform for heterogeneous database migration, high availability, and zero-downtime cutover.
  name: Oracle GoldenGate
- description: Open-source distributed change data capture platform built on Kafka Connect for streaming row-level changes from MySQL, Postgres, MongoDB, and more.
  name: Debezium
- description: Data transformation and modeling tool that versions schema and transformation migrations as SQL and YAML alongside warehouse pipelines.
  name: dbt
json_schemas:
- name: CutoverPlan
  property_count: 11
  slug: migration-cutover-plan
- name: MigrationProject
  property_count: 14
  slug: migration-migration-project
json_structures:
- name: Migration Cutover Plan Structure
  property_count: 11
  slug: migration-cutover-plan-structure
- name: Migration Migration Project Structure
  property_count: 14
  slug: migration-migration-project-structure
jsonld:
- class_count: 7
  name: Migration Context
  property_count: 28
  slug: migration-context
layout: provider
modified: '2026-05-19'
name: Migration
nav: Providers
network: true
overview: 'Migration is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Migration, Data Migration, Database Migration, Cloud Migration, and API Migration.


  The Migration catalog on APIs.io includes 1 JSON-LD context.


  Migration''s developer surface includes developer portal and 1 more developer resources.'
random_paper: 2
score:
  band: minimal
  composite: 9.5
  coverage:
    artifact_dirs: 9
    catalog_earned: 38.0
    catalog_earned_first_party: 0.0
    catalog_gap: 77.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  facets:
    access_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 14.7
    developer_ergonomics: 9.5
    discoverability: 48.2
    operational_transparency: 5.3
  needs_work:
    note: Recorded so this provider's gaps can be attributed. Does not affect the composite above.
    owner: catalog
    reasons:
    - owner: catalog
      reason: never_enriched
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 4.9
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
slug: migration
tags:
- Migration
- Data Migration
- Database Migration
- Cloud Migration
- API Migration
- Replication
- Cutover
use_cases:
- description: Enterprises use AWS Application Migration Service, Azure Migrate, or Google Cloud Migration Center to inventory on-premise workloads and replicate them to the cloud with minimal application changes.
  name: Data Center to Cloud Lift and Shift
- description: Teams use AWS DMS or Oracle GoldenGate to migrate from legacy commercial databases like Oracle and SQL Server to open-source or cloud-native engines such as Postgres, Aurora, or BigQuery.
  name: Heterogeneous Database Migration
- description: Data teams use Airbyte, Fivetran, or Stitch to backfill historical data from SaaS sources like Salesforce, HubSpot, and Stripe into a warehouse and keep it incrementally in sync.
  name: SaaS Data Onboarding
- description: Engineering teams stand up Debezium and Kafka Connect to stream change data capture events from operational databases into analytical systems, search indexes, and microservices.
  name: Real-Time Replication and CDC
- description: IT teams migrate mailboxes, files, and identities between Microsoft 365, Google Workspace, and Slack tenants during mergers, acquisitions, or restructurings using dedicated tenant migration tooling.
  name: Cross-Tenant SaaS Migration
- description: Application teams version SQL migrations alongside code using tools like dbt, Liquibase, and Flyway so that schema changes deploy and roll back atomically with releases.
  name: Schema Evolution at Deploy Time
- description: API providers use migration tooling and codegen platforms like Liblab to help consumers move between major versions of an API with regenerated SDKs and rewritten call sites.
  name: API Version Cutover
website: https://apievangelist.com
---

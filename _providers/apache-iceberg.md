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
  dimensions:
    agent_card: false
    agent_skills: false
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
  score: 44.1
  scored_at: '2026-08-17'
agentic_access:
- acting_count: 20
  human_in_the_loop: 0
  name: Apache Iceberg Agentic Access
  operation_count: 32
  slug: apache-iceberg-agentic-access
  summary_line: 32 operations · 20 acting
api_count: 5
apis:
- description: The Iceberg Java API provides programmatic access to table operations, schema management, partition management, and catalog implementations. It is the primary library for integrating Iceberg with JVM-
  name: Apache Iceberg Java API
  slug: java-api
- description: PyIceberg is the official Python implementation of the Apache Iceberg table specification. It provides programmatic access to Iceberg table metadata and data, with integrations for PyArrow, Pandas, Du
  name: PyIceberg Python API
  slug: python-api
- description: The Catalog API API from Apache Iceberg — 18 operation(s) for catalog api.
  name: Apache Iceberg Catalog API API
  slug: apache-iceberg-catalog-api-api
- description: The Configuration API API from Apache Iceberg — 1 operation(s) for configuration api.
  name: Apache Iceberg Configuration API API
  slug: apache-iceberg-configuration-api-api
- description: The OAuth2 API API from Apache Iceberg — 1 operation(s) for oauth2 api.
  name: Apache Iceberg OAuth2 API API
  slug: apache-iceberg-oauth2-api-api
artifact_total: 513
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Iceberg REST Catalog Catalog API API
  slug: open-apache-iceberg-catalog-api-api
- collection_type: open
  name: Apache Iceberg REST Catalog Catalog API Configuration API API
  slug: open-apache-iceberg-configuration-api-api
- collection_type: open
  name: Apache Iceberg REST Catalog Catalog API OAuth2 API API
  slug: open-apache-iceberg-oauth2-api-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/iceberg-python/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/iceberg-python/releases
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/iceberg-python/blob/main/LICENSE
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-iceberg-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-iceberg-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-iceberg-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/apache-iceberg-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/apache-iceberg-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/apacheiceberg
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/iceberg
- group: docs
  title: ''
  type: Documentation
  url: https://iceberg.apache.org/docs/latest/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: company
  title: ''
  type: Blog
  url: https://iceberg.apache.org/blogs/
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@ApacheIceberg
- group: design
  title: ''
  type: Versioning
  url: https://iceberg.apache.org/releases/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://iceberg.apache.org/releases/
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-iceberg-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-iceberg-vocabulary.yaml
created: '2026-03-16'
description: Apache Iceberg is an open table format for large analytic datasets that provides ACID transactions, schema evolution, hidden partitioning, and time travel. It works with Spark, Flink, Hive, Presto, Trino, DuckDB, ClickHouse, and many more compute engines. Governed by the Apache Software Foundation under the Apache 2.0 license.
examples:
- key_count: 1
  name: Rest Catalog Open Api Add Encryption Key Update Example
  slug: rest-catalog-open-api-add-encryption-key-update-example
- key_count: 1
  name: Rest Catalog Open Api Add Partition Spec Update Example
  slug: rest-catalog-open-api-add-partition-spec-update-example
- key_count: 2
  name: Rest Catalog Open Api Add Schema Update Example
  slug: rest-catalog-open-api-add-schema-update-example
- key_count: 1
  name: Rest Catalog Open Api Add Snapshot Update Example
  slug: rest-catalog-open-api-add-snapshot-update-example
- key_count: 1
  name: Rest Catalog Open Api Add Sort Order Update Example
  slug: rest-catalog-open-api-add-sort-order-update-example
- key_count: 1
  name: Rest Catalog Open Api Add View Version Update Example
  slug: rest-catalog-open-api-add-view-version-update-example
- key_count: 0
  name: Rest Catalog Open Api And Or Expression Example
  slug: rest-catalog-open-api-and-or-expression-example
- key_count: 1
  name: Rest Catalog Open Api Assert Create Example
  slug: rest-catalog-open-api-assert-create-example
- key_count: 2
  name: Rest Catalog Open Api Assert Current Schema Id Example
  slug: rest-catalog-open-api-assert-current-schema-id-example
- key_count: 2
  name: Rest Catalog Open Api Assert Default Sort Order Id Example
  slug: rest-catalog-open-api-assert-default-sort-order-id-example
- key_count: 2
  name: Rest Catalog Open Api Assert Default Spec Id Example
  slug: rest-catalog-open-api-assert-default-spec-id-example
- key_count: 2
  name: Rest Catalog Open Api Assert Last Assigned Field Id Example
  slug: rest-catalog-open-api-assert-last-assigned-field-id-example
- key_count: 2
  name: Rest Catalog Open Api Assert Last Assigned Partition Id Example
  slug: rest-catalog-open-api-assert-last-assigned-partition-id-example
- key_count: 3
  name: Rest Catalog Open Api Assert Ref Snapshot Id Example
  slug: rest-catalog-open-api-assert-ref-snapshot-id-example
- key_count: 2
  name: Rest Catalog Open Api Assert Table Uuid Example
  slug: rest-catalog-open-api-assert-table-uuid-example
- key_count: 2
  name: Rest Catalog Open Api Assert View Uuid Example
  slug: rest-catalog-open-api-assert-view-uuid-example
- key_count: 2
  name: Rest Catalog Open Api Assign Uuid Update Example
  slug: rest-catalog-open-api-assign-uuid-update-example
- key_count: 1
  name: Rest Catalog Open Api Async Planning Result Example
  slug: rest-catalog-open-api-async-planning-result-example
- key_count: 1
  name: Rest Catalog Open Api Base Update Example
  slug: rest-catalog-open-api-base-update-example
- key_count: 0
  name: Rest Catalog Open Api Binary Type Value Example
  slug: rest-catalog-open-api-binary-type-value-example
- key_count: 5
  name: Rest Catalog Open Api Blob Metadata Example
  slug: rest-catalog-open-api-blob-metadata-example
- key_count: 0
  name: Rest Catalog Open Api Boolean Type Value Example
  slug: rest-catalog-open-api-boolean-type-value-example
- key_count: 4
  name: Rest Catalog Open Api Catalog Config Example
  slug: rest-catalog-open-api-catalog-config-example
- key_count: 5
  name: Rest Catalog Open Api Commit Report Example
  slug: rest-catalog-open-api-commit-report-example
- key_count: 2
  name: Rest Catalog Open Api Commit Table Request Example
  slug: rest-catalog-open-api-commit-table-request-example
- key_count: 1
  name: Rest Catalog Open Api Commit Table Response Example
  slug: rest-catalog-open-api-commit-table-response-example
- key_count: 1
  name: Rest Catalog Open Api Commit Transaction Request Example
  slug: rest-catalog-open-api-commit-transaction-request-example
- key_count: 2
  name: Rest Catalog Open Api Commit View Request Example
  slug: rest-catalog-open-api-commit-view-request-example
- key_count: 0
  name: Rest Catalog Open Api Completed Planning Result Example
  slug: rest-catalog-open-api-completed-planning-result-example
- key_count: 0
  name: Rest Catalog Open Api Completed Planning With Id Result Example
  slug: rest-catalog-open-api-completed-planning-with-id-result-example
- key_count: 9
  name: Rest Catalog Open Api Content File Example
  slug: rest-catalog-open-api-content-file-example
- key_count: 2
  name: Rest Catalog Open Api Count Map Example
  slug: rest-catalog-open-api-count-map-example
- key_count: 2
  name: Rest Catalog Open Api Counter Result Example
  slug: rest-catalog-open-api-counter-result-example
- key_count: 1
  name: Rest Catalog Open Api Create Namespace Request Example
  slug: rest-catalog-open-api-create-namespace-request-example
- key_count: 1
  name: Rest Catalog Open Api Create Namespace Response Example
  slug: rest-catalog-open-api-create-namespace-response-example
- key_count: 4
  name: Rest Catalog Open Api Create Table Request Example
  slug: rest-catalog-open-api-create-table-request-example
- key_count: 3
  name: Rest Catalog Open Api Create View Request Example
  slug: rest-catalog-open-api-create-view-request-example
- key_count: 8
  name: Rest Catalog Open Api Data File Example
  slug: rest-catalog-open-api-data-file-example
- key_count: 0
  name: Rest Catalog Open Api Date Type Value Example
  slug: rest-catalog-open-api-date-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Decimal Type Value Example
  slug: rest-catalog-open-api-decimal-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Delete File Example
  slug: rest-catalog-open-api-delete-file-example
- key_count: 0
  name: Rest Catalog Open Api Double Type Value Example
  slug: rest-catalog-open-api-double-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Empty Planning Result Example
  slug: rest-catalog-open-api-empty-planning-result-example
- key_count: 4
  name: Rest Catalog Open Api Encrypted Key Example
  slug: rest-catalog-open-api-encrypted-key-example
- key_count: 2
  name: Rest Catalog Open Api Equality Delete File Example
  slug: rest-catalog-open-api-equality-delete-file-example
- key_count: 0
  name: Rest Catalog Open Api Expression Example
  slug: rest-catalog-open-api-expression-example
- key_count: 0
  name: Rest Catalog Open Api Expression Type Example
  slug: rest-catalog-open-api-expression-type-example
- key_count: 0
  name: Rest Catalog Open Api Failed Planning Result Example
  slug: rest-catalog-open-api-failed-planning-result-example
- key_count: 0
  name: Rest Catalog Open Api False Expression Example
  slug: rest-catalog-open-api-false-expression-example
- key_count: 0
  name: Rest Catalog Open Api Fetch Planning Result Example
  slug: rest-catalog-open-api-fetch-planning-result-example
- key_count: 0
  name: Rest Catalog Open Api Fetch Scan Tasks Request Example
  slug: rest-catalog-open-api-fetch-scan-tasks-request-example
- key_count: 0
  name: Rest Catalog Open Api Fetch Scan Tasks Result Example
  slug: rest-catalog-open-api-fetch-scan-tasks-result-example
- key_count: 0
  name: Rest Catalog Open Api Field Name Example
  slug: rest-catalog-open-api-field-name-example
- key_count: 0
  name: Rest Catalog Open Api File Format Example
  slug: rest-catalog-open-api-file-format-example
- key_count: 2
  name: Rest Catalog Open Api File Scan Task Example
  slug: rest-catalog-open-api-file-scan-task-example
- key_count: 0
  name: Rest Catalog Open Api Fixed Type Value Example
  slug: rest-catalog-open-api-fixed-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Float Type Value Example
  slug: rest-catalog-open-api-float-type-value-example
- key_count: 1
  name: Rest Catalog Open Api Get Namespace Response Example
  slug: rest-catalog-open-api-get-namespace-response-example
- key_count: 0
  name: Rest Catalog Open Api Integer Type Value Example
  slug: rest-catalog-open-api-integer-type-value-example
- key_count: 1
  name: Rest Catalog Open Api List Namespaces Response Example
  slug: rest-catalog-open-api-list-namespaces-response-example
- key_count: 1
  name: Rest Catalog Open Api List Tables Response Example
  slug: rest-catalog-open-api-list-tables-response-example
- key_count: 3
  name: Rest Catalog Open Api List Type Example
  slug: rest-catalog-open-api-list-type-example
- key_count: 0
  name: Rest Catalog Open Api Literal Expression Example
  slug: rest-catalog-open-api-literal-expression-example
- key_count: 1
  name: Rest Catalog Open Api Load Credentials Response Example
  slug: rest-catalog-open-api-load-credentials-response-example
- key_count: 3
  name: Rest Catalog Open Api Load Table Result Example
  slug: rest-catalog-open-api-load-table-result-example
- key_count: 2
  name: Rest Catalog Open Api Load View Result Example
  slug: rest-catalog-open-api-load-view-result-example
- key_count: 0
  name: Rest Catalog Open Api Long Type Value Example
  slug: rest-catalog-open-api-long-type-value-example
- key_count: 4
  name: Rest Catalog Open Api Map Type Example
  slug: rest-catalog-open-api-map-type-example
- key_count: 0
  name: Rest Catalog Open Api Metadata Log Example
  slug: rest-catalog-open-api-metadata-log-example
- key_count: 0
  name: Rest Catalog Open Api Metric Result Example
  slug: rest-catalog-open-api-metric-result-example
- key_count: 0
  name: Rest Catalog Open Api Metrics Example
  slug: rest-catalog-open-api-metrics-example
- key_count: 0
  name: Rest Catalog Open Api Multi Valued Map Example
  slug: rest-catalog-open-api-multi-valued-map-example
- key_count: 0
  name: Rest Catalog Open Api Namespace Example
  slug: rest-catalog-open-api-namespace-example
- key_count: 0
  name: Rest Catalog Open Api Not Expression Example
  slug: rest-catalog-open-api-not-expression-example
- key_count: 0
  name: Rest Catalog Open Api Null Order Example
  slug: rest-catalog-open-api-null-order-example
- key_count: 4
  name: Rest Catalog Open Api O Auth Client Credentials Request Example
  slug: rest-catalog-open-api-o-auth-client-credentials-request-example
- key_count: 3
  name: Rest Catalog Open Api O Auth Error Example
  slug: rest-catalog-open-api-o-auth-error-example
- key_count: 4
  name: Rest Catalog Open Api O Auth Token Exchange Request Example
  slug: rest-catalog-open-api-o-auth-token-exchange-request-example
- key_count: 0
  name: Rest Catalog Open Api O Auth Token Request Example
  slug: rest-catalog-open-api-o-auth-token-request-example
- key_count: 5
  name: Rest Catalog Open Api O Auth Token Response Example
  slug: rest-catalog-open-api-o-auth-token-response-example
- key_count: 0
  name: Rest Catalog Open Api Page Token Example
  slug: rest-catalog-open-api-page-token-example
- key_count: 3
  name: Rest Catalog Open Api Partition Field Example
  slug: rest-catalog-open-api-partition-field-example
- key_count: 2
  name: Rest Catalog Open Api Partition Spec Example
  slug: rest-catalog-open-api-partition-spec-example
- key_count: 3
  name: Rest Catalog Open Api Partition Statistics File Example
  slug: rest-catalog-open-api-partition-statistics-file-example
- key_count: 0
  name: Rest Catalog Open Api Plan Status Example
  slug: rest-catalog-open-api-plan-status-example
- key_count: 8
  name: Rest Catalog Open Api Plan Table Scan Request Example
  slug: rest-catalog-open-api-plan-table-scan-request-example
- key_count: 0
  name: Rest Catalog Open Api Plan Table Scan Result Example
  slug: rest-catalog-open-api-plan-table-scan-result-example
- key_count: 0
  name: Rest Catalog Open Api Plan Task Example
  slug: rest-catalog-open-api-plan-task-example
- key_count: 3
  name: Rest Catalog Open Api Position Delete File Example
  slug: rest-catalog-open-api-position-delete-file-example
- key_count: 0
  name: Rest Catalog Open Api Primitive Type Example
  slug: rest-catalog-open-api-primitive-type-example
- key_count: 0
  name: Rest Catalog Open Api Primitive Type Value Example
  slug: rest-catalog-open-api-primitive-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Reference Example
  slug: rest-catalog-open-api-reference-example
- key_count: 3
  name: Rest Catalog Open Api Register Table Request Example
  slug: rest-catalog-open-api-register-table-request-example
- key_count: 2
  name: Rest Catalog Open Api Register View Request Example
  slug: rest-catalog-open-api-register-view-request-example
- key_count: 6
  name: Rest Catalog Open Api Remote Sign Request Example
  slug: rest-catalog-open-api-remote-sign-request-example
- key_count: 1
  name: Rest Catalog Open Api Remote Sign Result Example
  slug: rest-catalog-open-api-remote-sign-result-example
- key_count: 2
  name: Rest Catalog Open Api Remove Encryption Key Update Example
  slug: rest-catalog-open-api-remove-encryption-key-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Partition Specs Update Example
  slug: rest-catalog-open-api-remove-partition-specs-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Partition Statistics Update Example
  slug: rest-catalog-open-api-remove-partition-statistics-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Properties Update Example
  slug: rest-catalog-open-api-remove-properties-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Schemas Update Example
  slug: rest-catalog-open-api-remove-schemas-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Snapshot Ref Update Example
  slug: rest-catalog-open-api-remove-snapshot-ref-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Snapshots Update Example
  slug: rest-catalog-open-api-remove-snapshots-update-example
- key_count: 2
  name: Rest Catalog Open Api Remove Statistics Update Example
  slug: rest-catalog-open-api-remove-statistics-update-example
- key_count: 0
  name: Rest Catalog Open Api Rename Table Request Example
  slug: rest-catalog-open-api-rename-table-request-example
- key_count: 1
  name: Rest Catalog Open Api Report Metrics Request Example
  slug: rest-catalog-open-api-report-metrics-request-example
- key_count: 6
  name: Rest Catalog Open Api Scan Report Example
  slug: rest-catalog-open-api-scan-report-example
- key_count: 3
  name: Rest Catalog Open Api Scan Tasks Example
  slug: rest-catalog-open-api-scan-tasks-example
- key_count: 0
  name: Rest Catalog Open Api Schema Example
  slug: rest-catalog-open-api-schema-example
- key_count: 2
  name: Rest Catalog Open Api Set Current Schema Update Example
  slug: rest-catalog-open-api-set-current-schema-update-example
- key_count: 2
  name: Rest Catalog Open Api Set Current View Version Update Example
  slug: rest-catalog-open-api-set-current-view-version-update-example
- key_count: 2
  name: Rest Catalog Open Api Set Default Sort Order Update Example
  slug: rest-catalog-open-api-set-default-sort-order-update-example
- key_count: 2
  name: Rest Catalog Open Api Set Default Spec Update Example
  slug: rest-catalog-open-api-set-default-spec-update-example
- key_count: 1
  name: Rest Catalog Open Api Set Expression Example
  slug: rest-catalog-open-api-set-expression-example
- key_count: 2
  name: Rest Catalog Open Api Set Location Update Example
  slug: rest-catalog-open-api-set-location-update-example
- key_count: 1
  name: Rest Catalog Open Api Set Partition Statistics Update Example
  slug: rest-catalog-open-api-set-partition-statistics-update-example
- key_count: 2
  name: Rest Catalog Open Api Set Properties Update Example
  slug: rest-catalog-open-api-set-properties-update-example
- key_count: 2
  name: Rest Catalog Open Api Set Snapshot Ref Update Example
  slug: rest-catalog-open-api-set-snapshot-ref-update-example
- key_count: 2
  name: Rest Catalog Open Api Set Statistics Update Example
  slug: rest-catalog-open-api-set-statistics-update-example
- key_count: 9
  name: Rest Catalog Open Api Snapshot Example
  slug: rest-catalog-open-api-snapshot-example
- key_count: 0
  name: Rest Catalog Open Api Snapshot Log Example
  slug: rest-catalog-open-api-snapshot-log-example
- key_count: 5
  name: Rest Catalog Open Api Snapshot Reference Example
  slug: rest-catalog-open-api-snapshot-reference-example
- key_count: 0
  name: Rest Catalog Open Api Snapshot References Example
  slug: rest-catalog-open-api-snapshot-references-example
- key_count: 0
  name: Rest Catalog Open Api Sort Direction Example
  slug: rest-catalog-open-api-sort-direction-example
- key_count: 1
  name: Rest Catalog Open Api Sort Field Example
  slug: rest-catalog-open-api-sort-field-example
- key_count: 2
  name: Rest Catalog Open Api Sort Order Example
  slug: rest-catalog-open-api-sort-order-example
- key_count: 3
  name: Rest Catalog Open Api Sql View Representation Example
  slug: rest-catalog-open-api-sql-view-representation-example
- key_count: 5
  name: Rest Catalog Open Api Statistics File Example
  slug: rest-catalog-open-api-statistics-file-example
- key_count: 2
  name: Rest Catalog Open Api Storage Credential Example
  slug: rest-catalog-open-api-storage-credential-example
- key_count: 0
  name: Rest Catalog Open Api String Type Value Example
  slug: rest-catalog-open-api-string-type-value-example
- key_count: 4
  name: Rest Catalog Open Api Struct Field Example
  slug: rest-catalog-open-api-struct-field-example
- key_count: 2
  name: Rest Catalog Open Api Struct Type Example
  slug: rest-catalog-open-api-struct-type-example
- key_count: 1
  name: Rest Catalog Open Api Table Identifier Example
  slug: rest-catalog-open-api-table-identifier-example
- key_count: 20
  name: Rest Catalog Open Api Table Metadata Example
  slug: rest-catalog-open-api-table-metadata-example
- key_count: 1
  name: Rest Catalog Open Api Table Requirement Example
  slug: rest-catalog-open-api-table-requirement-example
- key_count: 0
  name: Rest Catalog Open Api Table Update Example
  slug: rest-catalog-open-api-table-update-example
- key_count: 0
  name: Rest Catalog Open Api Term Example
  slug: rest-catalog-open-api-term-example
- key_count: 0
  name: Rest Catalog Open Api Time Type Value Example
  slug: rest-catalog-open-api-time-type-value-example
- key_count: 3
  name: Rest Catalog Open Api Timer Result Example
  slug: rest-catalog-open-api-timer-result-example
- key_count: 0
  name: Rest Catalog Open Api Timestamp Nano Type Value Example
  slug: rest-catalog-open-api-timestamp-nano-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Timestamp Type Value Example
  slug: rest-catalog-open-api-timestamp-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Timestamp Tz Nano Type Value Example
  slug: rest-catalog-open-api-timestamp-tz-nano-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Timestamp Tz Type Value Example
  slug: rest-catalog-open-api-timestamp-tz-type-value-example
- key_count: 0
  name: Rest Catalog Open Api Token Type Example
  slug: rest-catalog-open-api-token-type-example
- key_count: 0
  name: Rest Catalog Open Api Transform Example
  slug: rest-catalog-open-api-transform-example
- key_count: 1
  name: Rest Catalog Open Api Transform Term Example
  slug: rest-catalog-open-api-transform-term-example
- key_count: 0
  name: Rest Catalog Open Api True Expression Example
  slug: rest-catalog-open-api-true-expression-example
- key_count: 0
  name: Rest Catalog Open Api Type Example
  slug: rest-catalog-open-api-type-example
- key_count: 0
  name: Rest Catalog Open Api Unary Expression Example
  slug: rest-catalog-open-api-unary-expression-example
- key_count: 2
  name: Rest Catalog Open Api Update Namespace Properties Request Example
  slug: rest-catalog-open-api-update-namespace-properties-request-example
- key_count: 3
  name: Rest Catalog Open Api Update Namespace Properties Response Example
  slug: rest-catalog-open-api-update-namespace-properties-response-example
- key_count: 2
  name: Rest Catalog Open Api Upgrade Format Version Update Example
  slug: rest-catalog-open-api-upgrade-format-version-update-example
- key_count: 0
  name: Rest Catalog Open Api Uuid Type Value Example
  slug: rest-catalog-open-api-uuid-type-value-example
- key_count: 2
  name: Rest Catalog Open Api Value Map Example
  slug: rest-catalog-open-api-value-map-example
- key_count: 2
  name: Rest Catalog Open Api View History Entry Example
  slug: rest-catalog-open-api-view-history-entry-example
- key_count: 8
  name: Rest Catalog Open Api View Metadata Example
  slug: rest-catalog-open-api-view-metadata-example
- key_count: 0
  name: Rest Catalog Open Api View Representation Example
  slug: rest-catalog-open-api-view-representation-example
- key_count: 0
  name: Rest Catalog Open Api View Requirement Example
  slug: rest-catalog-open-api-view-requirement-example
- key_count: 0
  name: Rest Catalog Open Api View Update Example
  slug: rest-catalog-open-api-view-update-example
- key_count: 6
  name: Rest Catalog Open Api View Version Example
  slug: rest-catalog-open-api-view-version-example
features:
- description: Full ACID transaction support with serializable isolation for concurrent readers and writers.
  name: ACID Transactions
- description: Add, drop, update, or rename columns without rewriting existing data files.
  name: Schema Evolution
- description: Automatic partition management that prevents common user mistakes and silently incorrect results.
  name: Hidden Partitioning
- description: Change partition layout over time without rewriting existing data.
  name: Partition Evolution
- description: Query historical snapshots of tables and roll back to any prior version.
  name: Time Travel
- description: Supports upserts, deletes, and updates at the row level via merge-on-read and copy-on-write modes.
  name: Row-Level Updates
- description: Works with Spark, Flink, Hive, Trino, Presto, Impala, DuckDB, ClickHouse, and more.
  name: Multi-Engine Support
- description: Native support for S3, ADLS, GCS, and HDFS with no filesystem dependencies.
  name: Cloud-Native Storage
finops:
- name: Apache Iceberg Finops
  service_category: API
  slug: apache-iceberg-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-iceberg.png
json_schemas:
- name: AddEncryptionKeyUpdate
  property_count: 2
  slug: rest-catalog-open-api-add-encryption-key-update
- name: AddPartitionSpecUpdate
  property_count: 2
  slug: rest-catalog-open-api-add-partition-spec-update
- name: AddSchemaUpdate
  property_count: 3
  slug: rest-catalog-open-api-add-schema-update
- name: AddSnapshotUpdate
  property_count: 2
  slug: rest-catalog-open-api-add-snapshot-update
- name: AddSortOrderUpdate
  property_count: 2
  slug: rest-catalog-open-api-add-sort-order-update
- name: AddViewVersionUpdate
  property_count: 2
  slug: rest-catalog-open-api-add-view-version-update
- name: AndOrExpression
  property_count: 3
  slug: rest-catalog-open-api-and-or-expression
- name: AssertCreate
  property_count: 1
  slug: rest-catalog-open-api-assert-create
- name: AssertCurrentSchemaId
  property_count: 2
  slug: rest-catalog-open-api-assert-current-schema-id
- name: AssertDefaultSortOrderId
  property_count: 2
  slug: rest-catalog-open-api-assert-default-sort-order-id
- name: AssertDefaultSpecId
  property_count: 2
  slug: rest-catalog-open-api-assert-default-spec-id
- name: AssertLastAssignedFieldId
  property_count: 2
  slug: rest-catalog-open-api-assert-last-assigned-field-id
- name: AssertLastAssignedPartitionId
  property_count: 2
  slug: rest-catalog-open-api-assert-last-assigned-partition-id
- name: AssertRefSnapshotId
  property_count: 3
  slug: rest-catalog-open-api-assert-ref-snapshot-id
- name: AssertTableUUID
  property_count: 2
  slug: rest-catalog-open-api-assert-table-uuid
- name: AssertViewUUID
  property_count: 2
  slug: rest-catalog-open-api-assert-view-uuid
- name: AssignUUIDUpdate
  property_count: 2
  slug: rest-catalog-open-api-assign-uuid-update
- name: AsyncPlanningResult
  property_count: 2
  slug: rest-catalog-open-api-async-planning-result
- name: BaseUpdate
  property_count: 1
  slug: rest-catalog-open-api-base-update
- name: BinaryTypeValue
  property_count: 0
  slug: rest-catalog-open-api-binary-type-value
- name: BlobMetadata
  property_count: 5
  slug: rest-catalog-open-api-blob-metadata
- name: BooleanTypeValue
  property_count: 0
  slug: rest-catalog-open-api-boolean-type-value
- name: CatalogConfig
  property_count: 4
  slug: rest-catalog-open-api-catalog-config
- name: CommitReport
  property_count: 6
  slug: rest-catalog-open-api-commit-report
- name: CommitTableRequest
  property_count: 3
  slug: rest-catalog-open-api-commit-table-request
- name: CommitTableResponse
  property_count: 2
  slug: rest-catalog-open-api-commit-table-response
- name: CommitTransactionRequest
  property_count: 1
  slug: rest-catalog-open-api-commit-transaction-request
- name: CommitViewRequest
  property_count: 3
  slug: rest-catalog-open-api-commit-view-request
- name: CompletedPlanningResult
  property_count: 0
  slug: rest-catalog-open-api-completed-planning-result
- name: CompletedPlanningWithIDResult
  property_count: 0
  slug: rest-catalog-open-api-completed-planning-with-id-result
- name: ContentFile
  property_count: 10
  slug: rest-catalog-open-api-content-file
- name: CountMap
  property_count: 2
  slug: rest-catalog-open-api-count-map
- name: CounterResult
  property_count: 2
  slug: rest-catalog-open-api-counter-result
- name: CreateNamespaceRequest
  property_count: 2
  slug: rest-catalog-open-api-create-namespace-request
- name: CreateNamespaceResponse
  property_count: 2
  slug: rest-catalog-open-api-create-namespace-response
- name: CreateTableRequest
  property_count: 7
  slug: rest-catalog-open-api-create-table-request
- name: CreateViewRequest
  property_count: 5
  slug: rest-catalog-open-api-create-view-request
- name: DataFile
  property_count: 8
  slug: rest-catalog-open-api-data-file
- name: DateTypeValue
  property_count: 0
  slug: rest-catalog-open-api-date-type-value
- name: DecimalTypeValue
  property_count: 0
  slug: rest-catalog-open-api-decimal-type-value
- name: DeleteFile
  property_count: 0
  slug: rest-catalog-open-api-delete-file
- name: DoubleTypeValue
  property_count: 0
  slug: rest-catalog-open-api-double-type-value
- name: EmptyPlanningResult
  property_count: 1
  slug: rest-catalog-open-api-empty-planning-result
- name: EncryptedKey
  property_count: 4
  slug: rest-catalog-open-api-encrypted-key
- name: EqualityDeleteFile
  property_count: 2
  slug: rest-catalog-open-api-equality-delete-file
- name: Expression
  property_count: 0
  slug: rest-catalog-open-api-expression
- name: ExpressionType
  property_count: 0
  slug: rest-catalog-open-api-expression-type
- name: FailedPlanningResult
  property_count: 0
  slug: rest-catalog-open-api-failed-planning-result
- name: FalseExpression
  property_count: 1
  slug: rest-catalog-open-api-false-expression
- name: FetchPlanningResult
  property_count: 0
  slug: rest-catalog-open-api-fetch-planning-result
- name: FetchScanTasksRequest
  property_count: 1
  slug: rest-catalog-open-api-fetch-scan-tasks-request
- name: FetchScanTasksResult
  property_count: 0
  slug: rest-catalog-open-api-fetch-scan-tasks-result
- name: FieldName
  property_count: 0
  slug: rest-catalog-open-api-field-name
- name: FileFormat
  property_count: 0
  slug: rest-catalog-open-api-file-format
- name: FileScanTask
  property_count: 3
  slug: rest-catalog-open-api-file-scan-task
- name: FixedTypeValue
  property_count: 0
  slug: rest-catalog-open-api-fixed-type-value
- name: FloatTypeValue
  property_count: 0
  slug: rest-catalog-open-api-float-type-value
- name: GetNamespaceResponse
  property_count: 2
  slug: rest-catalog-open-api-get-namespace-response
- name: IntegerTypeValue
  property_count: 0
  slug: rest-catalog-open-api-integer-type-value
- name: ListNamespacesResponse
  property_count: 2
  slug: rest-catalog-open-api-list-namespaces-response
- name: ListTablesResponse
  property_count: 2
  slug: rest-catalog-open-api-list-tables-response
- name: ListType
  property_count: 4
  slug: rest-catalog-open-api-list-type
- name: LiteralExpression
  property_count: 3
  slug: rest-catalog-open-api-literal-expression
- name: LoadCredentialsResponse
  property_count: 1
  slug: rest-catalog-open-api-load-credentials-response
- name: LoadTableResult
  property_count: 4
  slug: rest-catalog-open-api-load-table-result
- name: LoadViewResult
  property_count: 3
  slug: rest-catalog-open-api-load-view-result
- name: LongTypeValue
  property_count: 0
  slug: rest-catalog-open-api-long-type-value
- name: MapType
  property_count: 6
  slug: rest-catalog-open-api-map-type
- name: MetadataLog
  property_count: 0
  slug: rest-catalog-open-api-metadata-log
- name: MetricResult
  property_count: 0
  slug: rest-catalog-open-api-metric-result
- name: Metrics
  property_count: 0
  slug: rest-catalog-open-api-metrics
- name: MultiValuedMap
  property_count: 0
  slug: rest-catalog-open-api-multi-valued-map
- name: Namespace
  property_count: 0
  slug: rest-catalog-open-api-namespace
- name: NotExpression
  property_count: 2
  slug: rest-catalog-open-api-not-expression
- name: NullOrder
  property_count: 0
  slug: rest-catalog-open-api-null-order
- name: OAuthClientCredentialsRequest
  property_count: 4
  slug: rest-catalog-open-api-o-auth-client-credentials-request
- name: OAuthError
  property_count: 3
  slug: rest-catalog-open-api-o-auth-error
- name: OAuthTokenExchangeRequest
  property_count: 7
  slug: rest-catalog-open-api-o-auth-token-exchange-request
- name: OAuthTokenRequest
  property_count: 0
  slug: rest-catalog-open-api-o-auth-token-request
- name: OAuthTokenResponse
  property_count: 6
  slug: rest-catalog-open-api-o-auth-token-response
- name: PageToken
  property_count: 0
  slug: rest-catalog-open-api-page-token
- name: PartitionField
  property_count: 4
  slug: rest-catalog-open-api-partition-field
- name: PartitionSpec
  property_count: 2
  slug: rest-catalog-open-api-partition-spec
- name: PartitionStatisticsFile
  property_count: 3
  slug: rest-catalog-open-api-partition-statistics-file
- name: PlanStatus
  property_count: 0
  slug: rest-catalog-open-api-plan-status
- name: PlanTableScanRequest
  property_count: 9
  slug: rest-catalog-open-api-plan-table-scan-request
- name: PlanTableScanResult
  property_count: 0
  slug: rest-catalog-open-api-plan-table-scan-result
- name: PlanTask
  property_count: 0
  slug: rest-catalog-open-api-plan-task
- name: PositionDeleteFile
  property_count: 3
  slug: rest-catalog-open-api-position-delete-file
- name: PrimitiveType
  property_count: 0
  slug: rest-catalog-open-api-primitive-type
- name: PrimitiveTypeValue
  property_count: 0
  slug: rest-catalog-open-api-primitive-type-value
- name: Reference
  property_count: 0
  slug: rest-catalog-open-api-reference
- name: RegisterTableRequest
  property_count: 3
  slug: rest-catalog-open-api-register-table-request
- name: RegisterViewRequest
  property_count: 2
  slug: rest-catalog-open-api-register-view-request
- name: RemoteSignRequest
  property_count: 7
  slug: rest-catalog-open-api-remote-sign-request
- name: RemoteSignResult
  property_count: 2
  slug: rest-catalog-open-api-remote-sign-result
- name: RemoveEncryptionKeyUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-encryption-key-update
- name: RemovePartitionSpecsUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-partition-specs-update
- name: RemovePartitionStatisticsUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-partition-statistics-update
- name: RemovePropertiesUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-properties-update
- name: RemoveSchemasUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-schemas-update
- name: RemoveSnapshotRefUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-snapshot-ref-update
- name: RemoveSnapshotsUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-snapshots-update
- name: RemoveStatisticsUpdate
  property_count: 2
  slug: rest-catalog-open-api-remove-statistics-update
- name: RenameTableRequest
  property_count: 2
  slug: rest-catalog-open-api-rename-table-request
- name: ReportMetricsRequest
  property_count: 1
  slug: rest-catalog-open-api-report-metrics-request
- name: ScanReport
  property_count: 8
  slug: rest-catalog-open-api-scan-report
- name: ScanTasks
  property_count: 3
  slug: rest-catalog-open-api-scan-tasks
- name: Schema
  property_count: 0
  slug: rest-catalog-open-api-schema
- name: SetCurrentSchemaUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-current-schema-update
- name: SetCurrentViewVersionUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-current-view-version-update
- name: SetDefaultSortOrderUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-default-sort-order-update
- name: SetDefaultSpecUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-default-spec-update
- name: SetExpression
  property_count: 3
  slug: rest-catalog-open-api-set-expression
- name: SetLocationUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-location-update
- name: SetPartitionStatisticsUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-partition-statistics-update
- name: SetPropertiesUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-properties-update
- name: SetSnapshotRefUpdate
  property_count: 2
  slug: rest-catalog-open-api-set-snapshot-ref-update
- name: SetStatisticsUpdate
  property_count: 3
  slug: rest-catalog-open-api-set-statistics-update
- name: SnapshotLog
  property_count: 0
  slug: rest-catalog-open-api-snapshot-log
- name: SnapshotReference
  property_count: 5
  slug: rest-catalog-open-api-snapshot-reference
- name: SnapshotReferences
  property_count: 0
  slug: rest-catalog-open-api-snapshot-references
- name: Snapshot
  property_count: 9
  slug: rest-catalog-open-api-snapshot
- name: SortDirection
  property_count: 0
  slug: rest-catalog-open-api-sort-direction
- name: SortField
  property_count: 4
  slug: rest-catalog-open-api-sort-field
- name: SortOrder
  property_count: 2
  slug: rest-catalog-open-api-sort-order
- name: SQLViewRepresentation
  property_count: 3
  slug: rest-catalog-open-api-sql-view-representation
- name: StatisticsFile
  property_count: 5
  slug: rest-catalog-open-api-statistics-file
- name: StorageCredential
  property_count: 2
  slug: rest-catalog-open-api-storage-credential
- name: StringTypeValue
  property_count: 0
  slug: rest-catalog-open-api-string-type-value
- name: StructField
  property_count: 7
  slug: rest-catalog-open-api-struct-field
- name: StructType
  property_count: 2
  slug: rest-catalog-open-api-struct-type
- name: TableIdentifier
  property_count: 2
  slug: rest-catalog-open-api-table-identifier
- name: TableMetadata
  property_count: 23
  slug: rest-catalog-open-api-table-metadata
- name: TableRequirement
  property_count: 1
  slug: rest-catalog-open-api-table-requirement
- name: TableUpdate
  property_count: 0
  slug: rest-catalog-open-api-table-update
- name: Term
  property_count: 0
  slug: rest-catalog-open-api-term
- name: TimeTypeValue
  property_count: 0
  slug: rest-catalog-open-api-time-type-value
- name: TimerResult
  property_count: 3
  slug: rest-catalog-open-api-timer-result
- name: TimestampNanoTypeValue
  property_count: 0
  slug: rest-catalog-open-api-timestamp-nano-type-value
- name: TimestampTypeValue
  property_count: 0
  slug: rest-catalog-open-api-timestamp-type-value
- name: TimestampTzNanoTypeValue
  property_count: 0
  slug: rest-catalog-open-api-timestamp-tz-nano-type-value
- name: TimestampTzTypeValue
  property_count: 0
  slug: rest-catalog-open-api-timestamp-tz-type-value
- name: TokenType
  property_count: 0
  slug: rest-catalog-open-api-token-type
- name: Transform
  property_count: 0
  slug: rest-catalog-open-api-transform
- name: TransformTerm
  property_count: 3
  slug: rest-catalog-open-api-transform-term
- name: TrueExpression
  property_count: 1
  slug: rest-catalog-open-api-true-expression
- name: Type
  property_count: 0
  slug: rest-catalog-open-api-type
- name: UnaryExpression
  property_count: 2
  slug: rest-catalog-open-api-unary-expression
- name: UpdateNamespacePropertiesRequest
  property_count: 2
  slug: rest-catalog-open-api-update-namespace-properties-request
- name: UpdateNamespacePropertiesResponse
  property_count: 3
  slug: rest-catalog-open-api-update-namespace-properties-response
- name: UpgradeFormatVersionUpdate
  property_count: 2
  slug: rest-catalog-open-api-upgrade-format-version-update
- name: UUIDTypeValue
  property_count: 0
  slug: rest-catalog-open-api-uuid-type-value
- name: ValueMap
  property_count: 2
  slug: rest-catalog-open-api-value-map
- name: ViewHistoryEntry
  property_count: 2
  slug: rest-catalog-open-api-view-history-entry
- name: ViewMetadata
  property_count: 8
  slug: rest-catalog-open-api-view-metadata
- name: ViewRepresentation
  property_count: 0
  slug: rest-catalog-open-api-view-representation
- name: ViewRequirement
  property_count: 0
  slug: rest-catalog-open-api-view-requirement
- name: ViewUpdate
  property_count: 0
  slug: rest-catalog-open-api-view-update
- name: ViewVersion
  property_count: 7
  slug: rest-catalog-open-api-view-version
json_structures:
- name: Rest Catalog Open Api Add Encryption Key Update Structure
  property_count: 2
  slug: rest-catalog-open-api-add-encryption-key-update-structure
- name: Rest Catalog Open Api Add Partition Spec Update Structure
  property_count: 2
  slug: rest-catalog-open-api-add-partition-spec-update-structure
- name: Rest Catalog Open Api Add Schema Update Structure
  property_count: 3
  slug: rest-catalog-open-api-add-schema-update-structure
- name: Rest Catalog Open Api Add Snapshot Update Structure
  property_count: 2
  slug: rest-catalog-open-api-add-snapshot-update-structure
- name: Rest Catalog Open Api Add Sort Order Update Structure
  property_count: 2
  slug: rest-catalog-open-api-add-sort-order-update-structure
- name: Rest Catalog Open Api Add View Version Update Structure
  property_count: 2
  slug: rest-catalog-open-api-add-view-version-update-structure
- name: Rest Catalog Open Api And Or Expression Structure
  property_count: 3
  slug: rest-catalog-open-api-and-or-expression-structure
- name: Rest Catalog Open Api Assert Create Structure
  property_count: 1
  slug: rest-catalog-open-api-assert-create-structure
- name: Rest Catalog Open Api Assert Current Schema Id Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-current-schema-id-structure
- name: Rest Catalog Open Api Assert Default Sort Order Id Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-default-sort-order-id-structure
- name: Rest Catalog Open Api Assert Default Spec Id Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-default-spec-id-structure
- name: Rest Catalog Open Api Assert Last Assigned Field Id Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-last-assigned-field-id-structure
- name: Rest Catalog Open Api Assert Last Assigned Partition Id Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-last-assigned-partition-id-structure
- name: Rest Catalog Open Api Assert Ref Snapshot Id Structure
  property_count: 3
  slug: rest-catalog-open-api-assert-ref-snapshot-id-structure
- name: Rest Catalog Open Api Assert Table Uuid Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-table-uuid-structure
- name: Rest Catalog Open Api Assert View Uuid Structure
  property_count: 2
  slug: rest-catalog-open-api-assert-view-uuid-structure
- name: Rest Catalog Open Api Assign Uuid Update Structure
  property_count: 2
  slug: rest-catalog-open-api-assign-uuid-update-structure
- name: Rest Catalog Open Api Async Planning Result Structure
  property_count: 2
  slug: rest-catalog-open-api-async-planning-result-structure
- name: Rest Catalog Open Api Base Update Structure
  property_count: 1
  slug: rest-catalog-open-api-base-update-structure
- name: Rest Catalog Open Api Binary Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-binary-type-value-structure
- name: Rest Catalog Open Api Blob Metadata Structure
  property_count: 5
  slug: rest-catalog-open-api-blob-metadata-structure
- name: Rest Catalog Open Api Boolean Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-boolean-type-value-structure
- name: Rest Catalog Open Api Catalog Config Structure
  property_count: 4
  slug: rest-catalog-open-api-catalog-config-structure
- name: Rest Catalog Open Api Commit Report Structure
  property_count: 6
  slug: rest-catalog-open-api-commit-report-structure
- name: Rest Catalog Open Api Commit Table Request Structure
  property_count: 3
  slug: rest-catalog-open-api-commit-table-request-structure
- name: Rest Catalog Open Api Commit Table Response Structure
  property_count: 2
  slug: rest-catalog-open-api-commit-table-response-structure
- name: Rest Catalog Open Api Commit Transaction Request Structure
  property_count: 1
  slug: rest-catalog-open-api-commit-transaction-request-structure
- name: Rest Catalog Open Api Commit View Request Structure
  property_count: 3
  slug: rest-catalog-open-api-commit-view-request-structure
- name: Rest Catalog Open Api Completed Planning Result Structure
  property_count: 0
  slug: rest-catalog-open-api-completed-planning-result-structure
- name: Rest Catalog Open Api Completed Planning With Id Result Structure
  property_count: 0
  slug: rest-catalog-open-api-completed-planning-with-id-result-structure
- name: Rest Catalog Open Api Content File Structure
  property_count: 10
  slug: rest-catalog-open-api-content-file-structure
- name: Rest Catalog Open Api Count Map Structure
  property_count: 2
  slug: rest-catalog-open-api-count-map-structure
- name: Rest Catalog Open Api Counter Result Structure
  property_count: 2
  slug: rest-catalog-open-api-counter-result-structure
- name: Rest Catalog Open Api Create Namespace Request Structure
  property_count: 2
  slug: rest-catalog-open-api-create-namespace-request-structure
- name: Rest Catalog Open Api Create Namespace Response Structure
  property_count: 2
  slug: rest-catalog-open-api-create-namespace-response-structure
- name: Rest Catalog Open Api Create Table Request Structure
  property_count: 7
  slug: rest-catalog-open-api-create-table-request-structure
- name: Rest Catalog Open Api Create View Request Structure
  property_count: 5
  slug: rest-catalog-open-api-create-view-request-structure
- name: Rest Catalog Open Api Data File Structure
  property_count: 8
  slug: rest-catalog-open-api-data-file-structure
- name: Rest Catalog Open Api Date Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-date-type-value-structure
- name: Rest Catalog Open Api Decimal Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-decimal-type-value-structure
- name: Rest Catalog Open Api Delete File Structure
  property_count: 0
  slug: rest-catalog-open-api-delete-file-structure
- name: Rest Catalog Open Api Double Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-double-type-value-structure
- name: Rest Catalog Open Api Empty Planning Result Structure
  property_count: 1
  slug: rest-catalog-open-api-empty-planning-result-structure
- name: Rest Catalog Open Api Encrypted Key Structure
  property_count: 4
  slug: rest-catalog-open-api-encrypted-key-structure
- name: Rest Catalog Open Api Equality Delete File Structure
  property_count: 2
  slug: rest-catalog-open-api-equality-delete-file-structure
- name: Rest Catalog Open Api Expression Structure
  property_count: 0
  slug: rest-catalog-open-api-expression-structure
- name: Rest Catalog Open Api Expression Type Structure
  property_count: 0
  slug: rest-catalog-open-api-expression-type-structure
- name: Rest Catalog Open Api Failed Planning Result Structure
  property_count: 0
  slug: rest-catalog-open-api-failed-planning-result-structure
- name: Rest Catalog Open Api False Expression Structure
  property_count: 1
  slug: rest-catalog-open-api-false-expression-structure
- name: Rest Catalog Open Api Fetch Planning Result Structure
  property_count: 0
  slug: rest-catalog-open-api-fetch-planning-result-structure
- name: Rest Catalog Open Api Fetch Scan Tasks Request Structure
  property_count: 1
  slug: rest-catalog-open-api-fetch-scan-tasks-request-structure
- name: Rest Catalog Open Api Fetch Scan Tasks Result Structure
  property_count: 0
  slug: rest-catalog-open-api-fetch-scan-tasks-result-structure
- name: Rest Catalog Open Api Field Name Structure
  property_count: 0
  slug: rest-catalog-open-api-field-name-structure
- name: Rest Catalog Open Api File Format Structure
  property_count: 0
  slug: rest-catalog-open-api-file-format-structure
- name: Rest Catalog Open Api File Scan Task Structure
  property_count: 3
  slug: rest-catalog-open-api-file-scan-task-structure
- name: Rest Catalog Open Api Fixed Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-fixed-type-value-structure
- name: Rest Catalog Open Api Float Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-float-type-value-structure
- name: Rest Catalog Open Api Get Namespace Response Structure
  property_count: 2
  slug: rest-catalog-open-api-get-namespace-response-structure
- name: Rest Catalog Open Api Integer Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-integer-type-value-structure
- name: Rest Catalog Open Api List Namespaces Response Structure
  property_count: 2
  slug: rest-catalog-open-api-list-namespaces-response-structure
- name: Rest Catalog Open Api List Tables Response Structure
  property_count: 2
  slug: rest-catalog-open-api-list-tables-response-structure
- name: Rest Catalog Open Api List Type Structure
  property_count: 4
  slug: rest-catalog-open-api-list-type-structure
- name: Rest Catalog Open Api Literal Expression Structure
  property_count: 3
  slug: rest-catalog-open-api-literal-expression-structure
- name: Rest Catalog Open Api Load Credentials Response Structure
  property_count: 1
  slug: rest-catalog-open-api-load-credentials-response-structure
- name: Rest Catalog Open Api Load Table Result Structure
  property_count: 4
  slug: rest-catalog-open-api-load-table-result-structure
- name: Rest Catalog Open Api Load View Result Structure
  property_count: 3
  slug: rest-catalog-open-api-load-view-result-structure
- name: Rest Catalog Open Api Long Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-long-type-value-structure
- name: Rest Catalog Open Api Map Type Structure
  property_count: 6
  slug: rest-catalog-open-api-map-type-structure
- name: Rest Catalog Open Api Metadata Log Structure
  property_count: 0
  slug: rest-catalog-open-api-metadata-log-structure
- name: Rest Catalog Open Api Metric Result Structure
  property_count: 0
  slug: rest-catalog-open-api-metric-result-structure
- name: Rest Catalog Open Api Metrics Structure
  property_count: 0
  slug: rest-catalog-open-api-metrics-structure
- name: Rest Catalog Open Api Multi Valued Map Structure
  property_count: 0
  slug: rest-catalog-open-api-multi-valued-map-structure
- name: Rest Catalog Open Api Namespace Structure
  property_count: 0
  slug: rest-catalog-open-api-namespace-structure
- name: Rest Catalog Open Api Not Expression Structure
  property_count: 2
  slug: rest-catalog-open-api-not-expression-structure
- name: Rest Catalog Open Api Null Order Structure
  property_count: 0
  slug: rest-catalog-open-api-null-order-structure
- name: Rest Catalog Open Api O Auth Client Credentials Request Structure
  property_count: 4
  slug: rest-catalog-open-api-o-auth-client-credentials-request-structure
- name: Rest Catalog Open Api O Auth Error Structure
  property_count: 3
  slug: rest-catalog-open-api-o-auth-error-structure
- name: Rest Catalog Open Api O Auth Token Exchange Request Structure
  property_count: 7
  slug: rest-catalog-open-api-o-auth-token-exchange-request-structure
- name: Rest Catalog Open Api O Auth Token Request Structure
  property_count: 0
  slug: rest-catalog-open-api-o-auth-token-request-structure
- name: Rest Catalog Open Api O Auth Token Response Structure
  property_count: 6
  slug: rest-catalog-open-api-o-auth-token-response-structure
- name: Rest Catalog Open Api Page Token Structure
  property_count: 0
  slug: rest-catalog-open-api-page-token-structure
- name: Rest Catalog Open Api Partition Field Structure
  property_count: 4
  slug: rest-catalog-open-api-partition-field-structure
- name: Rest Catalog Open Api Partition Spec Structure
  property_count: 2
  slug: rest-catalog-open-api-partition-spec-structure
- name: Rest Catalog Open Api Partition Statistics File Structure
  property_count: 3
  slug: rest-catalog-open-api-partition-statistics-file-structure
- name: Rest Catalog Open Api Plan Status Structure
  property_count: 0
  slug: rest-catalog-open-api-plan-status-structure
- name: Rest Catalog Open Api Plan Table Scan Request Structure
  property_count: 9
  slug: rest-catalog-open-api-plan-table-scan-request-structure
- name: Rest Catalog Open Api Plan Table Scan Result Structure
  property_count: 0
  slug: rest-catalog-open-api-plan-table-scan-result-structure
- name: Rest Catalog Open Api Plan Task Structure
  property_count: 0
  slug: rest-catalog-open-api-plan-task-structure
- name: Rest Catalog Open Api Position Delete File Structure
  property_count: 3
  slug: rest-catalog-open-api-position-delete-file-structure
- name: Rest Catalog Open Api Primitive Type Structure
  property_count: 0
  slug: rest-catalog-open-api-primitive-type-structure
- name: Rest Catalog Open Api Primitive Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-primitive-type-value-structure
- name: Rest Catalog Open Api Reference Structure
  property_count: 0
  slug: rest-catalog-open-api-reference-structure
- name: Rest Catalog Open Api Register Table Request Structure
  property_count: 3
  slug: rest-catalog-open-api-register-table-request-structure
- name: Rest Catalog Open Api Register View Request Structure
  property_count: 2
  slug: rest-catalog-open-api-register-view-request-structure
- name: Rest Catalog Open Api Remote Sign Request Structure
  property_count: 7
  slug: rest-catalog-open-api-remote-sign-request-structure
- name: Rest Catalog Open Api Remote Sign Result Structure
  property_count: 2
  slug: rest-catalog-open-api-remote-sign-result-structure
- name: Rest Catalog Open Api Remove Encryption Key Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-encryption-key-update-structure
- name: Rest Catalog Open Api Remove Partition Specs Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-partition-specs-update-structure
- name: Rest Catalog Open Api Remove Partition Statistics Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-partition-statistics-update-structure
- name: Rest Catalog Open Api Remove Properties Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-properties-update-structure
- name: Rest Catalog Open Api Remove Schemas Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-schemas-update-structure
- name: Rest Catalog Open Api Remove Snapshot Ref Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-snapshot-ref-update-structure
- name: Rest Catalog Open Api Remove Snapshots Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-snapshots-update-structure
- name: Rest Catalog Open Api Remove Statistics Update Structure
  property_count: 2
  slug: rest-catalog-open-api-remove-statistics-update-structure
- name: Rest Catalog Open Api Rename Table Request Structure
  property_count: 2
  slug: rest-catalog-open-api-rename-table-request-structure
- name: Rest Catalog Open Api Report Metrics Request Structure
  property_count: 1
  slug: rest-catalog-open-api-report-metrics-request-structure
- name: Rest Catalog Open Api Scan Report Structure
  property_count: 8
  slug: rest-catalog-open-api-scan-report-structure
- name: Rest Catalog Open Api Scan Tasks Structure
  property_count: 3
  slug: rest-catalog-open-api-scan-tasks-structure
- name: Rest Catalog Open Api Schema Structure
  property_count: 0
  slug: rest-catalog-open-api-schema-structure
- name: Rest Catalog Open Api Set Current Schema Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-current-schema-update-structure
- name: Rest Catalog Open Api Set Current View Version Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-current-view-version-update-structure
- name: Rest Catalog Open Api Set Default Sort Order Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-default-sort-order-update-structure
- name: Rest Catalog Open Api Set Default Spec Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-default-spec-update-structure
- name: Rest Catalog Open Api Set Expression Structure
  property_count: 3
  slug: rest-catalog-open-api-set-expression-structure
- name: Rest Catalog Open Api Set Location Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-location-update-structure
- name: Rest Catalog Open Api Set Partition Statistics Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-partition-statistics-update-structure
- name: Rest Catalog Open Api Set Properties Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-properties-update-structure
- name: Rest Catalog Open Api Set Snapshot Ref Update Structure
  property_count: 2
  slug: rest-catalog-open-api-set-snapshot-ref-update-structure
- name: Rest Catalog Open Api Set Statistics Update Structure
  property_count: 3
  slug: rest-catalog-open-api-set-statistics-update-structure
- name: Rest Catalog Open Api Snapshot Log Structure
  property_count: 0
  slug: rest-catalog-open-api-snapshot-log-structure
- name: Rest Catalog Open Api Snapshot Reference Structure
  property_count: 5
  slug: rest-catalog-open-api-snapshot-reference-structure
- name: Rest Catalog Open Api Snapshot References Structure
  property_count: 0
  slug: rest-catalog-open-api-snapshot-references-structure
- name: Rest Catalog Open Api Snapshot Structure
  property_count: 9
  slug: rest-catalog-open-api-snapshot-structure
- name: Rest Catalog Open Api Sort Direction Structure
  property_count: 0
  slug: rest-catalog-open-api-sort-direction-structure
- name: Rest Catalog Open Api Sort Field Structure
  property_count: 4
  slug: rest-catalog-open-api-sort-field-structure
- name: Rest Catalog Open Api Sort Order Structure
  property_count: 2
  slug: rest-catalog-open-api-sort-order-structure
- name: Rest Catalog Open Api Sql View Representation Structure
  property_count: 3
  slug: rest-catalog-open-api-sql-view-representation-structure
- name: Rest Catalog Open Api Statistics File Structure
  property_count: 5
  slug: rest-catalog-open-api-statistics-file-structure
- name: Rest Catalog Open Api Storage Credential Structure
  property_count: 2
  slug: rest-catalog-open-api-storage-credential-structure
- name: Rest Catalog Open Api String Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-string-type-value-structure
- name: Rest Catalog Open Api Struct Field Structure
  property_count: 7
  slug: rest-catalog-open-api-struct-field-structure
- name: Rest Catalog Open Api Struct Type Structure
  property_count: 2
  slug: rest-catalog-open-api-struct-type-structure
- name: Rest Catalog Open Api Table Identifier Structure
  property_count: 2
  slug: rest-catalog-open-api-table-identifier-structure
- name: Rest Catalog Open Api Table Metadata Structure
  property_count: 23
  slug: rest-catalog-open-api-table-metadata-structure
- name: Rest Catalog Open Api Table Requirement Structure
  property_count: 1
  slug: rest-catalog-open-api-table-requirement-structure
- name: Rest Catalog Open Api Table Update Structure
  property_count: 0
  slug: rest-catalog-open-api-table-update-structure
- name: Rest Catalog Open Api Term Structure
  property_count: 0
  slug: rest-catalog-open-api-term-structure
- name: Rest Catalog Open Api Time Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-time-type-value-structure
- name: Rest Catalog Open Api Timer Result Structure
  property_count: 3
  slug: rest-catalog-open-api-timer-result-structure
- name: Rest Catalog Open Api Timestamp Nano Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-timestamp-nano-type-value-structure
- name: Rest Catalog Open Api Timestamp Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-timestamp-type-value-structure
- name: Rest Catalog Open Api Timestamp Tz Nano Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-timestamp-tz-nano-type-value-structure
- name: Rest Catalog Open Api Timestamp Tz Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-timestamp-tz-type-value-structure
- name: Rest Catalog Open Api Token Type Structure
  property_count: 0
  slug: rest-catalog-open-api-token-type-structure
- name: Rest Catalog Open Api Transform Structure
  property_count: 0
  slug: rest-catalog-open-api-transform-structure
- name: Rest Catalog Open Api Transform Term Structure
  property_count: 3
  slug: rest-catalog-open-api-transform-term-structure
- name: Rest Catalog Open Api True Expression Structure
  property_count: 1
  slug: rest-catalog-open-api-true-expression-structure
- name: Rest Catalog Open Api Type Structure
  property_count: 0
  slug: rest-catalog-open-api-type-structure
- name: Rest Catalog Open Api Unary Expression Structure
  property_count: 2
  slug: rest-catalog-open-api-unary-expression-structure
- name: Rest Catalog Open Api Update Namespace Properties Request Structure
  property_count: 2
  slug: rest-catalog-open-api-update-namespace-properties-request-structure
- name: Rest Catalog Open Api Update Namespace Properties Response Structure
  property_count: 3
  slug: rest-catalog-open-api-update-namespace-properties-response-structure
- name: Rest Catalog Open Api Upgrade Format Version Update Structure
  property_count: 2
  slug: rest-catalog-open-api-upgrade-format-version-update-structure
- name: Rest Catalog Open Api Uuid Type Value Structure
  property_count: 0
  slug: rest-catalog-open-api-uuid-type-value-structure
- name: Rest Catalog Open Api Value Map Structure
  property_count: 2
  slug: rest-catalog-open-api-value-map-structure
- name: Rest Catalog Open Api View History Entry Structure
  property_count: 2
  slug: rest-catalog-open-api-view-history-entry-structure
- name: Rest Catalog Open Api View Metadata Structure
  property_count: 8
  slug: rest-catalog-open-api-view-metadata-structure
- name: Rest Catalog Open Api View Representation Structure
  property_count: 0
  slug: rest-catalog-open-api-view-representation-structure
- name: Rest Catalog Open Api View Requirement Structure
  property_count: 0
  slug: rest-catalog-open-api-view-requirement-structure
- name: Rest Catalog Open Api View Update Structure
  property_count: 0
  slug: rest-catalog-open-api-view-update-structure
- name: Rest Catalog Open Api View Version Structure
  property_count: 7
  slug: rest-catalog-open-api-view-version-structure
jsonld:
- class_count: 119
  name: Apache Iceberg Rest Catalog Open Api Context
  property_count: 190
  slug: apache-iceberg-rest-catalog-open-api-context
layout: provider
modified: '2026-05-19'
name: Apache Iceberg
nav: Providers
network: true
overview: 'Apache Iceberg publishes 3 APIs on the [APIs.io](https://apis.io/) network: Catalog API API, Configuration API API, and OAuth2 API API. Tagged areas include ACID, Analytics, Apache, Data Lake, and Lakehouse.


  The Apache Iceberg catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Iceberg''s developer surface includes authentication, documentation, engineering blog, YouTube channel, release notes, and 15 more developer resources.'
plans:
- name: Apache Iceberg Plans Pricing
  plan_count: 3
  slug: apache-iceberg-plans-pricing
random_paper: 35
rate_limits:
- limit_count: 5
  name: Apache Iceberg Rate Limits
  slug: apache-iceberg-rate-limits
rules:
- name: Apache Iceberg API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-iceberg-jsonschema-spectral-rules
- name: Apache Iceberg API Rules
  rule_count: 35
  severity_counts:
    error: 11
    hint: 0
    info: 7
    warn: 17
  slug: apache-iceberg-spectral-rules
scopes:
- name: Apache Iceberg Scopes
  scope_count: 1
  slug: apache-iceberg-scopes
  summary_line: 1 scope · clientCredentials
score:
  band: developing
  composite: 44.6
  delta: 0.0
  facets:
    commercial_clarity: 26.3
    contract_quality: 66.1
    developer_ergonomics: 21.7
    discoverability: 64.8
    governance: 68.8
    operational_transparency: 28.9
  previous_composite: 44.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.11.0
  scored_at: '2026-08-17'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-iceberg/refs/heads/main/screenshots/apache-iceberg-2026-06-20T172110.png
security:
- kind: authentication
  name: Apache Iceberg Authentication
  slug: apache-iceberg-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Apache Iceberg Domain Security
  slug: apache-iceberg-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Iceberg Vulnerability Disclosure
  slug: apache-iceberg-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-iceberg
tags:
- ACID
- Analytics
- Apache
- Data Lake
- Lakehouse
- Open Source
- Table Format
use_cases:
- description: Build open lakehouse architectures with ACID guarantees across petabyte-scale datasets.
  name: Lakehouse Analytics
- description: Stream data into Iceberg tables via Flink or Kafka Connect with exactly-once semantics.
  name: Real-Time Data Pipelines
- description: Use time travel to audit historical data states and implement regulatory compliance.
  name: Data Versioning and Auditing
- description: Query the same Iceberg tables from multiple engines (Spark, Trino, DuckDB) without data duplication.
  name: Multi-Engine Query Federation
- description: Migrate on-premises Hive workloads to cloud-native Iceberg tables with full compatibility.
  name: Cloud Data Migration
---

---
access_model:
  confidence: high
  label: Enterprise · Self-serve signup
  onboarding: self-serve
  pricing: enterprise
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_skills: false
    agentic_access: true
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 53.8
  scored_at: '2026-07-27'
agentic_access:
- acting_count: 4
  human_in_the_loop: 0
  name: Datahub Agentic Access
  operation_count: 7
  slug: datahub-agentic-access
  summary_line: 7 operations · 4 acting
api_count: 11
apis:
- description: 'Primary API for querying and mutating metadata in DataHub. The GraphQL API serves as the main public API for the platform and can be used to fetch and update metadata programmatically in the language '
  name: DataHub GraphQL API
  slug: datahub-graphql-api
- description: The Rest.li API represents the underlying persistence layer and exposes the raw PDL models used in storage. It powers the GraphQL API under the hood and is used for system-specific ingestion of metada
  name: DataHub REST API
  slug: datahub-rest-api
- description: 'Python client for interacting with DataHub. The acryl-datahub package provides a CLI and SDK for DataHub, including REST and Kafka emitter APIs for pushing metadata programmatically. It is one of the '
  name: DataHub Python SDK
  slug: datahub-python-sdk
- description: Java client for interacting with DataHub. The io.acryl datahub-client package offers REST emitter APIs that can be used to emit metadata from JVM-based systems. It supports all major DataHub entity ty
  name: DataHub Java SDK
  slug: datahub-java-sdk
- description: Command line tool for interacting with DataHub. The datahub CLI allows you to perform common operations including metadata ingestion, entity management, and system administration from the command line
  name: DataHub CLI
  slug: datahub-cli
- description: Event-driven framework for responding to real-time changes in the DataHub metadata graph. The Actions Framework allows you to configure event sources, transformations, and actions using YAML configura
  name: DataHub Actions Framework
  slug: datahub-actions-framework
- description: Batch operations for fetching multiple entities and their aspects in a single request. Supports version-specific retrieval and conditional writes.
  name: DataHub Batch API
  slug: datahub-batch-api
- description: 'Read, write, and delete metadata entities in the DataHub metadata graph. The entities endpoints support upserting entity-aspect pairs, retrieving the latest aspects for a given entity, and performing '
  name: DataHub Entities API
  slug: datahub-entities-api
- description: Write metadata events using the standard platform format. Provides an alternative ingestion path for emitting metadata change proposals to the DataHub metadata graph.
  name: DataHub Platform API
  slug: datahub-platform-api
- description: Query the relationship graph to navigate connections between entities. Supports filtering by relationship type and traversal direction (incoming or outgoing) from a given entity URN.
  name: DataHub Relationships API
  slug: datahub-relationships-api
- description: Query the versioned history of entity aspects over time. Useful for tracking schema changes, documentation updates, and other temporal metadata modifications for a given entity.
  name: DataHub Timeline API
  slug: datahub-timeline-api
arazzos:
- description: Confirm a dataset, attach glossary terms via its glossaryTerms aspect, then review the change in the entity timeline.
  name: DataHub Add Glossary Terms to a Dataset
  slug: datahub-add-glossary-terms-workflow
- description: Write an ownership aspect onto a dataset, then read it back to verify the owners were recorded.
  name: DataHub Assign Dataset Ownership
  slug: datahub-assign-ownership-workflow
- description: Confirm a dataset, check it has no downstream dependents, then soft delete it from the metadata graph.
  name: DataHub Decommission a Dataset
  slug: datahub-decommission-dataset-workflow
- description: Emit a metadata change proposal through the platform ingestion path, then read the entity back and review its timeline.
  name: DataHub Emit Platform Event and Audit
  slug: datahub-emit-and-audit-workflow
- description: Confirm a dataset exists, then write its globalTags aspect to apply governance tags.
  name: DataHub Tag a Dataset
  slug: datahub-tag-dataset-workflow
- description: Confirm a dataset, query its downstream relationships, then batch fetch the related datasets' aspects.
  name: DataHub Trace Dataset Lineage
  slug: datahub-trace-lineage-workflow
- description: Write a dataset's properties aspect into the metadata graph, then read the entity back to confirm the write landed.
  name: DataHub Upsert Dataset and Verify
  slug: datahub-upsert-dataset-workflow
artifact_total: 47
asyncapis:
- description: Event-driven interface for responding to real-time changes in the DataHub metadata graph. The Actions Framework consumes Metadata Change Log events and Platform Events from Kafka topics, enabling seam
  name: DataHub Actions Framework Events
  slug: datahub-actions-asyncapi
collections:
- collection_type: postman
  name: DataHub OpenAPI
  slug: postman-datahub-openapi
- collection_type: open
  name: DataHub OpenAPI
  slug: open-datahub-openapi
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/datahub-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/datahub-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/datahub-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/datahub/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-add-glossary-terms-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-assign-ownership-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-decommission-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-emit-and-audit-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-tag-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-trace-lineage-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/datahub-upsert-dataset-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://datahub.com
- group: start
  title: ''
  type: Portal
  url: https://docs.datahub.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.datahub.com/docs/
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.datahub.com/docs/quickstart
- group: auth
  title: ''
  type: Authentication
  url: https://docs.datahub.com/docs/authentication
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/datahub-project/datahub
- group: operate
  title: ''
  type: Slack
  url: https://slack.datahubproject.io
- group: company
  title: ''
  type: Blog
  url: https://datahub.com/blog/
- group: start
  title: ''
  type: Demo
  url: https://demo.datahubproject.io/
- group: operate
  title: ''
  type: ChangeLog
  url: https://github.com/datahub-project/datahub/releases
- group: operate
  title: ''
  type: StatusPage
  url: https://status.datahub.com
- group: operate
  title: ''
  type: Community
  url: https://forum.datahubproject.io/
- group: learn
  title: ''
  type: YouTube
  url: https://youtube.com/@datahubproject
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/datahub-cloud
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://datahub.com/privacy-policy/
- group: auth
  title: ''
  type: Security
  url: https://docs.datahub.com/docs/security_stance
- group: design
  title: ''
  type: JSONLD
  url: json-ld/datahub-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/datahub-vocabulary.yml
- group: other
  title: ''
  type: Capabilities
  url: capabilities/datahub-capabilities.yml
- group: design
  title: ''
  type: Rules
  url: rules/datahub-rules.yml
created: '2024-01-15'
description: DataHub is LinkedIn's generalized metadata search and discovery platform, providing a unified data catalog, lineage graph, governance tooling, and event-driven Actions Framework. It exposes GraphQL, OpenAPI, and Rest.li APIs along with Python and Java SDKs and a CLI for metadata ingestion.
finops:
- name: Datahub Finops
  service_category: Data Catalog
  slug: datahub-finops
graphqls:
- description: 'Primary API for querying and mutating metadata in DataHub. The GraphQL API serves as the main public API for the platform and can be used to fetch and update metadata programmatically in the language '
  name: DataHub GraphQL API
  slug: datahub-graphql
image: https://datahubproject.io/img/datahub-logo.svg
json_schemas:
- name: AspectValue
  property_count: 3
  slug: datahub-aspectvalue
- name: AuditStamp
  property_count: 2
  slug: datahub-auditstamp
- name: BatchGetRequest
  property_count: 2
  slug: datahub-batchgetrequest
- name: ChangeEvent
  property_count: 4
  slug: datahub-changeevent
- name: ChangeTransaction
  property_count: 4
  slug: datahub-changetransaction
- name: EntityAspectRequest
  property_count: 4
  slug: datahub-entityaspectrequest
- name: EntityAspectResponse
  property_count: 3
  slug: datahub-entityaspectresponse
- name: Error
  property_count: 3
  slug: datahub-error
- name: DataHub Metadata Change Log Event
  property_count: 8
  slug: datahub-metadata-change-log-event
- name: MetadataChangeProposal
  property_count: 6
  slug: datahub-metadatachangeproposal
- name: Relationship
  property_count: 3
  slug: datahub-relationship
- name: RelationshipsResponse
  property_count: 4
  slug: datahub-relationshipsresponse
- name: SystemMetadata
  property_count: 4
  slug: datahub-systemmetadata
- name: TimelineResponse
  property_count: 1
  slug: datahub-timelineresponse
json_structures:
- name: Datahub Structure
  property_count: 0
  slug: datahub-structure
jsonld:
- class_count: 0
  name: Datahub Context
  property_count: 9
  slug: datahub-context
layout: provider
modified: '2026-05-19'
name: DataHub
nav: Providers
network: true
overview: 'DataHub publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Actions Framework, Batch API, Entities API, and 3 more. Tagged areas include Data Catalog, Data Discovery, Data Governance, Data Lineage, and Metadata.


  The DataHub catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  DataHub''s developer surface includes authentication, developer portal, documentation, getting-started guide, engineering blog, changelog, YouTube channel, and 24 more developer resources.'
plans:
- name: Datahub Plans Pricing
  plan_count: 2
  slug: datahub-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 2
  name: Datahub Rate Limits
  slug: datahub-rate-limits
rules:
- name: DataHub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: datahub-asyncapi-spectral-rules
- name: DataHub API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: datahub-jsonschema-spectral-rules
- name: DataHub API Rules
  rule_count: 5
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 4
  slug: datahub-rules
score:
  band: strong
  composite: 65.0
  delta: 3.2
  facets:
    commercial_clarity: 39.5
    contract_quality: 78.8
    developer_ergonomics: 50.0
    discoverability: 87.5
    governance: 86.8
    operational_transparency: 63.2
  previous_composite: 61.8
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/datahub/refs/heads/main/screenshots/datahub-2026-06-20T175643.png
security:
- kind: authentication
  name: Datahub Authentication
  slug: datahub-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Datahub Domain Security
  slug: datahub-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: datahub
tags:
- Data Catalog
- Data Discovery
- Data Governance
- Data Lineage
- Metadata
website: https://datahub.com
---

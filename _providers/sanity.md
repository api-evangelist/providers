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
    error_semantics: false
    event_surface_described: derived
    idempotency: false
    mcp_server: true
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 42.8
  scored_at: '2026-08-10'
agentic_access:
- acting_count: 8
  human_in_the_loop: 0
  name: Sanity Agentic Access
  operation_count: 15
  slug: sanity-agentic-access
  summary_line: 15 operations · 8 acting
api_count: 14
apis:
- description: The Sanity Mutation API enables creating, updating, patching, and deleting documents in Content Lake. Mutations are submitted as arrays of operations (create, createOrReplace, createIfNotExists, patch
  name: Sanity Mutation API
  slug: sanity-mutation-api
- description: The Sanity Assets API handles uploading, retrieving, and managing file and image assets in Content Lake. Assets are stored as documents and referenced from content documents.
  name: Sanity Assets API
  slug: sanity-assets-api
- description: The Sanity Projects API enables programmatic management of Sanity projects including creating projects, managing datasets, configuring CORS origins, managing access tokens, and checking user permissio
  name: Sanity Projects API
  slug: sanity-projects-api
- description: 'The Sanity Webhooks API enables configuring event-driven notifications for content changes. Webhooks can be created to trigger on document create, update, delete, and publish events with customizable '
  name: Sanity Webhooks API
  slug: sanity-webhooks-api
- description: The Sanity Listen API provides real-time event streaming via Server-Sent Events (SSE) for content changes in a dataset. Clients can subscribe to a GROQ query and receive real-time notifications when m
  name: Sanity Listen API
  slug: sanity-listen-api
- description: The Sanity Roles API provides endpoints for managing user roles and permissions within Sanity projects. Supports predefined roles (Administrator, Read+Write, Read, Viewer) and custom role management.
  name: Sanity Roles API
  slug: sanity-roles-api
- description: The Sanity Scheduling API enables scheduling content for future publication or unpublication at specific times, supporting editorial workflows and content calendars.
  name: Sanity Scheduling API
  slug: sanity-scheduling-api
- description: The Sanity Embeddings Index API enables creating and managing vector embedding indexes for Content Lake documents, supporting semantic search and AI-powered content retrieval workflows.
  name: Sanity Embeddings Index API
  slug: sanity-embeddings-index-api
- description: File and image asset management
  name: Sanity Assets API
  slug: sanity-assets-api
- description: Real-time event streaming
  name: Sanity Listen API
  slug: sanity-listen-api
- description: Create, update, and delete document operations
  name: Sanity Mutations API
  slug: sanity-mutations-api
- description: Project and dataset management
  name: Sanity Projects API
  slug: sanity-projects-api
- description: GROQ query operations against Content Lake
  name: Sanity Query API
  slug: sanity-query-api
- description: Event notification configuration
  name: Sanity Webhooks API
  slug: sanity-webhooks-api
arazzos:
- description: Create a project, add an initial dataset, then list the project datasets.
  name: Sanity Bootstrap Project
  slug: sanity-bootstrap-project-workflow
- description: Count documents matching a GROQ filter, then delete them in one mutation.
  name: Sanity Bulk Delete by Query
  slug: sanity-bulk-delete-by-query-workflow
- description: Read a document's draft and published perspectives to inspect its history.
  name: Sanity Compare Draft and Published
  slug: sanity-compare-draft-and-published-workflow
- description: Create a document with a mutation, then confirm it exists with a GROQ query.
  name: Sanity Create and Verify Document
  slug: sanity-create-and-verify-document-workflow
- description: List accessible projects, then enumerate the datasets of a chosen project.
  name: Sanity Discover Project Datasets
  slug: sanity-discover-project-datasets-workflow
- description: Confirm a project exists, mint an API token on it, then list its tokens.
  name: Sanity Issue Token for Project
  slug: sanity-issue-token-for-project-workflow
- description: Create a dataset in a project, then list datasets to confirm it exists.
  name: Sanity Provision Dataset
  slug: sanity-provision-dataset-workflow
- description: Read a draft, promote it to a published document, then verify the result.
  name: Sanity Publish Draft Document
  slug: sanity-publish-draft-document-workflow
- description: Find a document with GROQ, then patch it when a match is found.
  name: Sanity Query Then Patch Document
  slug: sanity-query-then-patch-document-workflow
- description: Validate a GROQ filter, register a webhook on it, then list webhooks.
  name: Sanity Register Webhook for Query
  slug: sanity-register-webhook-for-query-workflow
- description: Read a project, update its display name and metadata, then re-read it.
  name: Sanity Rename Project
  slug: sanity-rename-project-workflow
- description: Upload a new image, find the target document, then point it at the new asset.
  name: Sanity Replace Document Asset
  slug: sanity-replace-document-asset-workflow
- description: Upload an image asset, then create a document that references it.
  name: Sanity Upload Asset and Reference
  slug: sanity-upload-asset-and-reference-workflow
- description: Find a document by a GROQ key match and patch it, otherwise create it.
  name: Sanity Upsert Document
  slug: sanity-upsert-document-workflow
artifact_total: 65
asyncapis:
- description: AsyncAPI specification for Sanity's GROQ-powered webhook surface. Sanity delivers event-driven HTTP callbacks when documents in a Content Lake dataset are created, updated, or deleted. Subscribers con
  name: Sanity GROQ-Powered Webhooks
  slug: sanity-webhooks-asyncapi
collections:
- collection_type: postman
  name: Sanity HTTP Assets API
  slug: postman-sanity-assets-api
- collection_type: postman
  name: Sanity HTTP Assets Listen API
  slug: postman-sanity-listen-api
- collection_type: postman
  name: Sanity HTTP Assets Mutations API
  slug: postman-sanity-mutations-api
- collection_type: postman
  name: Sanity HTTP Assets Projects API
  slug: postman-sanity-projects-api
- collection_type: postman
  name: Sanity HTTP Assets Query API
  slug: postman-sanity-query-api
- collection_type: postman
  name: Sanity HTTP Assets Webhooks API
  slug: postman-sanity-webhooks-api
- collection_type: open
  name: Sanity HTTP API
  slug: open-sanity
common:
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/sanity/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/sanity-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/sanity-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/sanity-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sanity-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/sanity-authentication.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-bootstrap-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-bulk-delete-by-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-compare-draft-and-published-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-create-and-verify-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-discover-project-datasets-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-issue-token-for-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-provision-dataset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-publish-draft-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-query-then-patch-document-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-register-webhook-for-query-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-rename-project-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-replace-document-asset-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-upload-asset-and-reference-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/sanity-upsert-document-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sanity-io
- group: company
  title: ''
  type: Website
  url: https://www.sanity.io
- group: docs
  title: ''
  type: Documentation
  url: https://www.sanity.io/docs
- group: docs
  title: ''
  type: HTTP API Reference
  url: https://www.sanity.io/docs/http-reference
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.sanity.io/docs
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sanity-io
- group: start
  title: ''
  type: GettingStarted
  url: https://www.sanity.io/docs/getting-started-with-sanity
- group: build
  title: ''
  type: JavaScript SDK
  url: https://www.npmjs.com/package/@sanity/client
- group: commercial
  title: ''
  type: Pricing
  url: https://www.sanity.io/pricing
- group: operate
  title: ''
  type: Community
  url: https://slack.sanity.io
- group: company
  title: ''
  type: Blog
  url: https://www.sanity.io/blog
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sanity.io
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/sanity-vocabulary.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/sanity-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/sanity-context.jsonld
- group: agent
  title: ''
  type: MCPServer
  url: https://github.com/sanity-io/sanity-mcp-server
- group: agent
  title: ''
  type: AgentSkills
  url: https://www.sanity.io/blog/introducing-sanity-agent-skills
created: '2026-05-02'
description: Sanity is a composable content platform providing a headless CMS with a real-time collaborative editor (Sanity Studio) and a powerful HTTP API for managing structured content. The Sanity Content Lake stores content as flexible documents queryable via GROQ (Graph-Relational Object Queries). Key API capabilities include document querying, mutations, real-time listening, asset management, project management, webhooks, scheduling, roles and permissions, vector embeddings, and AI-powered content agents.
examples:
- key_count: 2
  name: Sanity Mutate Documents Example
  slug: sanity-mutate-documents-example
- key_count: 2
  name: Sanity Query Documents Example
  slug: sanity-query-documents-example
finops:
- name: Sanity Finops
  service_category: Developer Tools / Headless CMS
  slug: sanity-finops
graphqls:
- description: 'Sanity provides a project-scoped GraphQL API that exposes Content Lake documents as a typed, queryable schema. The API is deployed per-project and per-dataset: you generate and deploy the schema from '
  name: Sanity GraphQL API
  slug: sanity-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sanity.png
json_schemas:
- name: AssetDocument
  property_count: 1
  slug: sanity-assetdocument
- name: Dataset
  property_count: 3
  slug: sanity-dataset
- name: Sanity Document
  property_count: 5
  slug: sanity-document
- name: MutationResponse
  property_count: 2
  slug: sanity-mutationresponse
- name: MutationsRequest
  property_count: 1
  slug: sanity-mutationsrequest
- name: Project
  property_count: 6
  slug: sanity-project
- name: QueryResponse
  property_count: 4
  slug: sanity-queryresponse
- name: Token
  property_count: 4
  slug: sanity-token
- name: TokenWithKey
  property_count: 0
  slug: sanity-tokenwithkey
- name: Sanity Webhook
  property_count: 10
  slug: sanity-webhook
- name: WebhookInput
  property_count: 7
  slug: sanity-webhookinput
json_structures:
- name: Sanity Document Structure
  property_count: 0
  slug: sanity-document-structure
- name: Sanity Structure
  property_count: 0
  slug: sanity-structure
jsonld:
- class_count: 0
  name: Sanity Context
  property_count: 12
  slug: sanity-context
layout: provider
mcp_servers:
- description: ''
  name: MCP Server
  slug: mcp-server
modified: '2026-05-30'
name: Sanity
nav: Providers
network: true
overview: 'Sanity publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Projects API, Webhooks API, and 7 more. Tagged areas include Headless CMS, Content Management, GROQ, Real-Time, and Structured Content.


  The Sanity catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Sanity''s developer surface includes authentication, documentation, getting-started guide, pricing, engineering blog, and 32 more developer resources.'
plans:
- name: Sanity Plans Pricing
  plan_count: 3
  slug: sanity-plans-pricing
random_paper: 84
rate_limits:
- limit_count: 6
  name: Sanity Rate Limits
  slug: sanity-rate-limits
rules:
- name: Sanity API Rules
  rule_count: 6
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 5
  slug: sanity-asyncapi-spectral-rules
- name: Sanity API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: sanity-jsonschema-spectral-rules
- name: Sanity API Rules
  rule_count: 7
  severity_counts:
    error: 3
    hint: 0
    info: 0
    warn: 4
  slug: sanity-rules
score:
  band: strong
  composite: 65.8
  delta: 0.0
  facets:
    commercial_clarity: 57.9
    contract_quality: 86.3
    developer_ergonomics: 65.2
    discoverability: 64.8
    governance: 52.1
    operational_transparency: 52.6
  previous_composite: 65.8
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  schema_version: 0.9.1
  scored_at: '2026-08-10'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sanity/refs/heads/main/screenshots/sanity-2026-06-20T193435.png
security:
- kind: authentication
  name: Sanity Authentication
  slug: sanity-authentication
  summary_line: http · 1 scheme
- kind: domain-security
  name: Sanity Domain Security
  slug: sanity-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Sanity Vulnerability Disclosure
  slug: sanity-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Sanity Trust Center
  slug: sanity-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, GDPR, CSA STAR
slug: sanity
tags:
- Headless CMS
- Content Management
- GROQ
- Real-Time
- Structured Content
- Developer Platform
website: https://www.sanity.io
---

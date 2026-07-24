---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: true
    rate_limit_signal: true
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.1
  score: 54.8
  scored_at: '2026-07-23'
agentic_access:
- acting_count: 39
  human_in_the_loop: 0
  name: Pinecone Agentic Access
  operation_count: 66
  slug: pinecone-agentic-access
  summary_line: 66 operations · 39 acting
api_count: 9
apis:
- description: Actions that manage API Keys.
  name: Pinecone API Keys API
  slug: pinecone-api-keys-api
- description: The Bulk Operations API from Pinecone — 2 operation(s) for bulk operations.
  name: Pinecone Bulk Operations API
  slug: pinecone-bulk-operations-api
- description: Model inference
  name: Pinecone Inference API
  slug: pinecone-inference-api
- description: Actions that manage Assistants
  name: Pinecone Manage Assistants API
  slug: pinecone-manage-assistants-api
- description: Actions that manage indexes
  name: Pinecone Manage Indexes API
  slug: pinecone-manage-indexes-api
- description: The Namespace Operations API from Pinecone — 2 operation(s) for namespace operations.
  name: Pinecone Namespace Operations API
  slug: pinecone-namespace-operations-api
- description: Actions that manage organizations.
  name: Pinecone Organizations API
  slug: pinecone-organizations-api
- description: Actions that manage projects.
  name: Pinecone Projects API
  slug: pinecone-projects-api
- description: The Vector Operations API from Pinecone — 10 operation(s) for vector operations.
  name: Pinecone Vector Operations API
  slug: pinecone-vector-operations-api
artifact_total: 218
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/pinecone-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/pinecone-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/pinecone-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/pinecone-authentication.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/pinecone-io
- group: company
  title: ''
  type: Website
  url: https://www.pinecone.io/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.pinecone.io/pricing/
- group: company
  title: ''
  type: Blog
  url: https://www.pinecone.io/blog/
- group: company
  title: ''
  type: Newsroom
  url: https://www.pinecone.io/newsroom/news/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.pinecone.io/guides/get-started/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.pinecone.io/guides/get-started/overview
- group: other
  title: ''
  type: Glossary
  url: https://docs.pinecone.io/guides/get-started/glossary
- group: build
  title: ''
  type: Examples
  url: https://docs.pinecone.io/examples/notebooks
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.pinecone.io/release-notes/2024
- group: operate
  title: ''
  type: StatusPage
  url: https://status.pinecone.io/
- group: start
  title: ''
  type: Login
  url: https://app.pinecone.io
- group: auth
  title: ''
  type: Security
  url: https://www.pinecone.io/security/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.pinecone.io/legal/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.pinecone.io/privacy/
- group: build
  title: ''
  type: SDKs
  url: https://docs.pinecone.io/reference/pinecone-sdks
- group: other
  title: ''
  type: Repository
  url: https://github.com/pinecone-io/pinecone-api
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.pinecone.io/llms.txt
created: '2024-07-02'
description: With its vector database at the core, Pinecone is the leading knowledge platform for building accurate, secure, and scalable AI applications. The Pinecone APIs cover Database (vector storage and search), Inference (embeddings and reranking), Assistant (RAG over documents), and Admin (organization and project management).
examples:
- key_count: 6
  name: Pinecone Chat Assistant Example
  slug: pinecone-chat-assistant-example
- key_count: 6
  name: Pinecone Chat Completion Assistant Example
  slug: pinecone-chat-completion-assistant-example
- key_count: 6
  name: Pinecone Configure Index Example
  slug: pinecone-configure-index-example
- key_count: 6
  name: Pinecone Context Assistant Example
  slug: pinecone-context-assistant-example
- key_count: 6
  name: Pinecone Create Api Key Example
  slug: pinecone-create-api-key-example
- key_count: 6
  name: Pinecone Create Assistant Example
  slug: pinecone-create-assistant-example
- key_count: 6
  name: Pinecone Create Backup Example
  slug: pinecone-create-backup-example
- key_count: 6
  name: Pinecone Create Collection Example
  slug: pinecone-create-collection-example
- key_count: 6
  name: Pinecone Create Index Example
  slug: pinecone-create-index-example
- key_count: 6
  name: Pinecone Create Index For Model Example
  slug: pinecone-create-index-for-model-example
- key_count: 6
  name: Pinecone Create Index From Backup Operation Example
  slug: pinecone-create-index-from-backup-operation-example
- key_count: 6
  name: Pinecone Create Project Example
  slug: pinecone-create-project-example
- key_count: 6
  name: Pinecone Delete Api Key Example
  slug: pinecone-delete-api-key-example
- key_count: 6
  name: Pinecone Delete Assistant Example
  slug: pinecone-delete-assistant-example
- key_count: 6
  name: Pinecone Delete Backup Example
  slug: pinecone-delete-backup-example
- key_count: 6
  name: Pinecone Delete Collection Example
  slug: pinecone-delete-collection-example
- key_count: 6
  name: Pinecone Delete File Example
  slug: pinecone-delete-file-example
- key_count: 6
  name: Pinecone Delete Index Example
  slug: pinecone-delete-index-example
- key_count: 6
  name: Pinecone Delete Organization Example
  slug: pinecone-delete-organization-example
- key_count: 6
  name: Pinecone Delete Project Example
  slug: pinecone-delete-project-example
- key_count: 6
  name: Pinecone Describe Backup Example
  slug: pinecone-describe-backup-example
- key_count: 6
  name: Pinecone Describe Collection Example
  slug: pinecone-describe-collection-example
- key_count: 6
  name: Pinecone Describe File Example
  slug: pinecone-describe-file-example
- key_count: 6
  name: Pinecone Describe Index Example
  slug: pinecone-describe-index-example
- key_count: 6
  name: Pinecone Describe Restore Job Example
  slug: pinecone-describe-restore-job-example
- key_count: 6
  name: Pinecone Embed Example
  slug: pinecone-embed-example
- key_count: 6
  name: Pinecone Fetch Api Key Example
  slug: pinecone-fetch-api-key-example
- key_count: 6
  name: Pinecone Fetch Organization Example
  slug: pinecone-fetch-organization-example
- key_count: 6
  name: Pinecone Fetch Project Example
  slug: pinecone-fetch-project-example
- key_count: 6
  name: Pinecone Get Assistant Example
  slug: pinecone-get-assistant-example
- key_count: 6
  name: Pinecone Get Model Example
  slug: pinecone-get-model-example
- key_count: 6
  name: Pinecone List Assistants Example
  slug: pinecone-list-assistants-example
- key_count: 6
  name: Pinecone List Collections Example
  slug: pinecone-list-collections-example
- key_count: 6
  name: Pinecone List Files Example
  slug: pinecone-list-files-example
- key_count: 6
  name: Pinecone List Index Backups Example
  slug: pinecone-list-index-backups-example
- key_count: 6
  name: Pinecone List Indexes Example
  slug: pinecone-list-indexes-example
- key_count: 6
  name: Pinecone List Models Example
  slug: pinecone-list-models-example
- key_count: 6
  name: Pinecone List Organizations Example
  slug: pinecone-list-organizations-example
- key_count: 6
  name: Pinecone List Project Api Keys Example
  slug: pinecone-list-project-api-keys-example
- key_count: 6
  name: Pinecone List Project Backups Example
  slug: pinecone-list-project-backups-example
- key_count: 6
  name: Pinecone List Projects Example
  slug: pinecone-list-projects-example
- key_count: 6
  name: Pinecone List Restore Jobs Example
  slug: pinecone-list-restore-jobs-example
- key_count: 6
  name: Pinecone Rerank Example
  slug: pinecone-rerank-example
- key_count: 6
  name: Pinecone Update Api Key Example
  slug: pinecone-update-api-key-example
- key_count: 6
  name: Pinecone Update Organization Example
  slug: pinecone-update-organization-example
- key_count: 6
  name: Pinecone Update Project Example
  slug: pinecone-update-project-example
- key_count: 6
  name: Pinecone Upload File Example
  slug: pinecone-upload-file-example
features:
- 'Starter free: 2 GB, 2M writes, 1M reads'
- 'Builder at $20/mo flat: 10 GB, 5M writes, 2M reads'
- 'Standard $50/mo min: $0.33/GB, $4-$4.50/M writes, $16-$18/M reads'
- 'Enterprise $500/mo min: $6-$6.75/M writes, $24-$27/M reads, 99.95% SLA'
- Serverless indexes (auto-scaling)
- Pod-based (legacy) for reserved capacity
- REST and gRPC APIs
- OpenAPI spec available
- Hybrid search (dense + sparse vectors)
- Namespaces for multi-tenancy
- Bulk import from S3/GCS/Azure
- Up to 1,000 vectors per upsert request
- Dedicated Read Nodes for QPS isolation
- Backup/restore on Standard+
- SAML SSO and audit logs (Enterprise)
- Inference API for embeddings + reranking
finops:
- name: Pinecone Finops
  service_category: Vector Database
  slug: pinecone-finops
graphqls:
- description: Pinecone is a managed vector database for AI applications. The API covers index management, upsert and query of vector embeddings, metadata filtering, sparse-dense hybrid search, namespaces, and colle
  name: Pinecone GraphQL API
  slug: pinecone-graphql
image: https://kinlane-productions2.s3.amazonaws.com/apis-json-icons/introduction-pinecone-docs.png
json_schemas:
- name: APIKey
  property_count: 4
  slug: pinecone-apikey
- name: APIKeyWithSecret
  property_count: 2
  slug: pinecone-apikeywithsecret
- name: Assistant
  property_count: 7
  slug: pinecone-assistant
- name: AssistantFileModel
  property_count: 10
  slug: pinecone-assistantfilemodel
- name: BackupList
  property_count: 2
  slug: pinecone-backuplist
- name: BackupModel
  property_count: 16
  slug: pinecone-backupmodel
- name: BYOC
  property_count: 3
  slug: pinecone-byocspec
- name: BYOC
  property_count: 3
  slug: pinecone-byocspecresponse
- name: CancelImportResponse
  property_count: 0
  slug: pinecone-cancelimportresponse
- name: ChatCompletionModel
  property_count: 4
  slug: pinecone-chatcompletionmodel
- name: ChatModel
  property_count: 6
  slug: pinecone-chatmodel
- name: ChatRequest
  property_count: 8
  slug: pinecone-chatrequest
- name: ChoiceChunkModel
  property_count: 3
  slug: pinecone-choicechunkmodel
- name: ChoiceModel
  property_count: 3
  slug: pinecone-choicemodel
- name: CitationModel
  property_count: 2
  slug: pinecone-citationmodel
- name: CollectionList
  property_count: 1
  slug: pinecone-collectionlist
- name: CollectionModel
  property_count: 6
  slug: pinecone-collectionmodel
- name: ConfigureIndexRequest
  property_count: 4
  slug: pinecone-configureindexrequest
- name: ContextModel
  property_count: 3
  slug: pinecone-contextmodel
- name: ContextOptionsModel
  property_count: 4
  slug: pinecone-contextoptionsmodel
- name: ContextRequest
  property_count: 7
  slug: pinecone-contextrequest
- name: CreateAPIKeyRequest
  property_count: 2
  slug: pinecone-createapikeyrequest
- name: CreateBackupRequest
  property_count: 2
  slug: pinecone-createbackuprequest
- name: CreateCollectionRequest
  property_count: 2
  slug: pinecone-createcollectionrequest
- name: CreateIndexForModelRequest
  property_count: 8
  slug: pinecone-createindexformodelrequest
- name: CreateIndexFromBackupRequest
  property_count: 3
  slug: pinecone-createindexfrombackuprequest
- name: CreateIndexFromBackupResponse
  property_count: 2
  slug: pinecone-createindexfrombackupresponse
- name: CreateIndexRequest
  property_count: 7
  slug: pinecone-createindexrequest
- name: CreateNamespaceRequest
  property_count: 2
  slug: pinecone-createnamespacerequest
- name: CreateProjectRequest
  property_count: 3
  slug: pinecone-createprojectrequest
- name: DeleteRequest
  property_count: 4
  slug: pinecone-deleterequest
- name: DeleteResponse
  property_count: 0
  slug: pinecone-deleteresponse
- name: DeletionProtection
  property_count: 0
  slug: pinecone-deletionprotection
- name: Dense embedding
  property_count: 2
  slug: pinecone-denseembedding
- name: DescribeIndexStatsRequest
  property_count: 1
  slug: pinecone-describeindexstatsrequest
- name: Document
  property_count: 0
  slug: pinecone-document
- name: DocxReferenceModel
  property_count: 3
  slug: pinecone-docxreferencemodel
- name: Embedding
  property_count: 0
  slug: pinecone-embedding
- name: EmbeddingsList
  property_count: 4
  slug: pinecone-embeddingslist
- name: EmbedInputs
  property_count: 0
  slug: pinecone-embedinputs
- name: EmbedRequest
  property_count: 3
  slug: pinecone-embedrequest
- name: ErrorResponse
  property_count: 2
  slug: pinecone-errorresponse
- name: FetchByMetadataRequest
  property_count: 4
  slug: pinecone-fetchbymetadatarequest
- name: FetchByMetadataResponse
  property_count: 4
  slug: pinecone-fetchbymetadataresponse
- name: FetchResponse
  property_count: 3
  slug: pinecone-fetchresponse
- name: HighlightModel
  property_count: 2
  slug: pinecone-highlightmodel
- name: Hit
  property_count: 3
  slug: pinecone-hit
- name: ImageModel
  property_count: 3
  slug: pinecone-imagemodel
- name: ImportErrorMode
  property_count: 1
  slug: pinecone-importerrormode
- name: ImportModel
  property_count: 8
  slug: pinecone-importmodel
- name: IndexDescription
  property_count: 8
  slug: pinecone-indexdescription
- name: IndexList
  property_count: 1
  slug: pinecone-indexlist
- name: IndexModel
  property_count: 11
  slug: pinecone-indexmodel
- name: IndexSpec
  property_count: 0
  slug: pinecone-indexspec
- name: IndexTags
  property_count: 0
  slug: pinecone-indextags
- name: JsonReferenceModel
  property_count: 2
  slug: pinecone-jsonreferencemodel
- name: ListApiKeysResponse
  property_count: 1
  slug: pinecone-listapikeysresponse
- name: ListImportsResponse
  property_count: 2
  slug: pinecone-listimportsresponse
- name: ListItem
  property_count: 1
  slug: pinecone-listitem
- name: ListNamespacesResponse
  property_count: 3
  slug: pinecone-listnamespacesresponse
- name: ListResponse
  property_count: 4
  slug: pinecone-listresponse
- name: MarkdownReferenceModel
  property_count: 2
  slug: pinecone-markdownreferencemodel
- name: MessageModel
  property_count: 2
  slug: pinecone-messagemodel
- name: MetadataSchema
  property_count: 1
  slug: pinecone-metadataschema
- name: ModelIndexEmbed
  property_count: 7
  slug: pinecone-modelindexembed
- name: ModelInfo
  property_count: 12
  slug: pinecone-modelinfo
- name: ModelInfoList
  property_count: 1
  slug: pinecone-modelinfolist
- name: ModelInfoMetric
  property_count: 0
  slug: pinecone-modelinfometric
- name: ModelInfoSupportedMetrics
  property_count: 0
  slug: pinecone-modelinfosupportedmetrics
- name: ModelInfoSupportedParameter
  property_count: 8
  slug: pinecone-modelinfosupportedparameter
- name: MultiModalContentBlocksModel
  property_count: 0
  slug: pinecone-multimodalcontentblocksmodel
- name: MultiModalContentImageBlockModel
  property_count: 3
  slug: pinecone-multimodalcontentimageblockmodel
- name: MultiModalContentTextBlockModel
  property_count: 2
  slug: pinecone-multimodalcontenttextblockmodel
- name: MultiModalSnippetModel
  property_count: 4
  slug: pinecone-multimodalsnippetmodel
- name: NamespaceDescription
  property_count: 4
  slug: pinecone-namespacedescription
- name: NamespaceSummary
  property_count: 1
  slug: pinecone-namespacesummary
- name: Organization
  property_count: 6
  slug: pinecone-organization
- name: OrganizationList
  property_count: 1
  slug: pinecone-organizationlist
- name: Pagination
  property_count: 1
  slug: pinecone-pagination
- name: PaginationResponse
  property_count: 1
  slug: pinecone-paginationresponse
- name: PdfReferenceModel
  property_count: 3
  slug: pinecone-pdfreferencemodel
- name: Pod-based
  property_count: 7
  slug: pinecone-podspec
- name: Project
  property_count: 6
  slug: pinecone-project
- name: ProjectList
  property_count: 1
  slug: pinecone-projectlist
- name: protobufAny
  property_count: 2
  slug: pinecone-protobufany
- name: QueryRequest
  property_count: 11
  slug: pinecone-queryrequest
- name: QueryResponse
  property_count: 4
  slug: pinecone-queryresponse
- name: QueryVector
  property_count: 5
  slug: pinecone-queryvector
- name: RankedDocument
  property_count: 3
  slug: pinecone-rankeddocument
- name: ReadCapacity
  property_count: 0
  slug: pinecone-readcapacity
- name: ReadCapacityDedicatedConfig
  property_count: 3
  slug: pinecone-readcapacitydedicatedconfig
- name: Dedicated
  property_count: 2
  slug: pinecone-readcapacitydedicatedspec
- name: Dedicated
  property_count: 3
  slug: pinecone-readcapacitydedicatedspecresponse
- name: On-demand
  property_count: 1
  slug: pinecone-readcapacityondemandspec
- name: On-demand
  property_count: 2
  slug: pinecone-readcapacityondemandspecresponse
- name: ReadCapacityResponse
  property_count: 0
  slug: pinecone-readcapacityresponse
- name: ReadCapacityStatus
  property_count: 4
  slug: pinecone-readcapacitystatus
- name: ReferenceModel
  property_count: 3
  slug: pinecone-referencemodel
- name: RerankRequest
  property_count: 7
  slug: pinecone-rerankrequest
- name: RerankResult
  property_count: 3
  slug: pinecone-rerankresult
- name: RestoreJobList
  property_count: 2
  slug: pinecone-restorejoblist
- name: RestoreJobModel
  property_count: 8
  slug: pinecone-restorejobmodel
- name: rpcStatus
  property_count: 3
  slug: pinecone-rpcstatus
- name: ScalingConfigManual
  property_count: 2
  slug: pinecone-scalingconfigmanual
- name: ScoredVector
  property_count: 5
  slug: pinecone-scoredvector
- name: SearchCompletions
  property_count: 5
  slug: pinecone-searchcompletions
- name: SearchMatchTerms
  property_count: 2
  slug: pinecone-searchmatchterms
- name: SearchRecordsRequest
  property_count: 3
  slug: pinecone-searchrecordsrequest
- name: SearchRecordsResponse
  property_count: 2
  slug: pinecone-searchrecordsresponse
- name: SearchRecordsVector
  property_count: 3
  slug: pinecone-searchrecordsvector
- name: SearchUsage
  property_count: 3
  slug: pinecone-searchusage
- name: Serverless
  property_count: 5
  slug: pinecone-serverlessspec
- name: ServerlessSpecResponse
  property_count: 5
  slug: pinecone-serverlessspecresponse
- name: The query results for a single `QueryVector`
  property_count: 2
  slug: pinecone-singlequeryresults
- name: SnippetModel
  property_count: 0
  slug: pinecone-snippetmodel
- name: Sparse embedding
  property_count: 4
  slug: pinecone-sparseembedding
- name: SparseValues
  property_count: 2
  slug: pinecone-sparsevalues
- name: StartImportRequest
  property_count: 3
  slug: pinecone-startimportrequest
- name: StartImportResponse
  property_count: 1
  slug: pinecone-startimportresponse
- name: StreamChatCompletionChunkModel
  property_count: 3
  slug: pinecone-streamchatcompletionchunkmodel
- name: TextReferenceModel
  property_count: 2
  slug: pinecone-textreferencemodel
- name: TextSnippetModel
  property_count: 4
  slug: pinecone-textsnippetmodel
- name: TypedReferenceModel
  property_count: 0
  slug: pinecone-typedreferencemodel
- name: UpdateAPIKeyRequest
  property_count: 2
  slug: pinecone-updateapikeyrequest
- name: UpdateOrganizationRequest
  property_count: 1
  slug: pinecone-updateorganizationrequest
- name: UpdateProjectRequest
  property_count: 3
  slug: pinecone-updateprojectrequest
- name: UpdateRequest
  property_count: 7
  slug: pinecone-updaterequest
- name: UpdateResponse
  property_count: 1
  slug: pinecone-updateresponse
- name: UpsertRecord
  property_count: 1
  slug: pinecone-upsertrecord
- name: UpsertRequest
  property_count: 2
  slug: pinecone-upsertrequest
- name: UpsertResponse
  property_count: 1
  slug: pinecone-upsertresponse
- name: Usage
  property_count: 1
  slug: pinecone-usage
- name: UsageModel
  property_count: 3
  slug: pinecone-usagemodel
- name: Vector
  property_count: 4
  slug: pinecone-vector
- name: VectorType
  property_count: 0
  slug: pinecone-vectortype
- name: VectorValues
  property_count: 0
  slug: pinecone-vectorvalues
json_structures:
- name: Pinecone Structure
  property_count: 0
  slug: pinecone-structure
layout: provider
modified: '2026-05-19'
name: Pinecone
nav: Providers
network: true
overview: 'Pinecone publishes 9 APIs on the [APIs.io](https://apis.io/) network, including API Keys API, Bulk Operations API, Inference API, and 6 more. Tagged areas include Vector Databases, AI, Embeddings, and RAG.


  The Pinecone catalog on APIs.io includes 1 Spectral governance ruleset.


  Pinecone''s developer surface includes authentication, pricing, engineering blog, documentation, getting-started guide, code examples, changelog, and 15 more developer resources.'
plans:
- name: Pinecone Plans Pricing
  plan_count: 4
  slug: pinecone-plans-pricing
random_paper: 33
rate_limits:
- limit_count: 4
  name: Pinecone Rate Limits
  slug: pinecone-rate-limits
rules:
- name: Pinecone API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: pinecone-jsonschema-spectral-rules
score:
  band: strong
  composite: 68.5
  delta: 0.0
  facets:
    commercial_clarity: 92.1
    contract_quality: 60.3
    developer_ergonomics: 39.1
    discoverability: 87.5
    governance: 73.7
    operational_transparency: 73.7
  previous_composite: 68.5
  schema_version: 0.5
  scored_at: '2026-07-23'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/pinecone/refs/heads/main/screenshots/pinecone-2026-06-20T191712.png
security:
- kind: authentication
  name: Pinecone Authentication
  slug: pinecone-authentication
  summary_line: apiKey/http · 2 schemes
- kind: domain-security
  name: Pinecone Domain Security
  slug: pinecone-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: trust-center
  name: Pinecone Trust Center
  slug: pinecone-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, GDPR
slug: pinecone
tags:
- Vector Databases
- AI
- Embeddings
- RAG
website: https://www.pinecone.io/
---

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
    asyncapi_events: true
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: false
    mcp_server: false
    openapi_examples: partial
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 46.4
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 234
  human_in_the_loop: 0
  name: Benchling Agentic Access
  operation_count: 402
  slug: benchling-agentic-access
  summary_line: 402 operations · 234 acting
api_count: 57
apis:
- description: AA Sequences are the working units of cells that make everything run (they help make structures, catalyze reactions and allow for signaling - a kind of internal cell communication). On Benchling, thes
  name: Benchling AA Sequences API
  slug: benchling-aa-sequences-api
- description: Create and manage Benchling apps on your tenant
  name: Benchling Apps API
  slug: benchling-apps-api
- description: Results represent the output of assays that have been performed. You can customize the schemas of results to fit your needs. Results can link to runs, entities, and other types. To learn more about cr
  name: Benchling Assay Results API
  slug: benchling-assay-results-api
- description: Runs capture the details / parameters of a run that was performed. Results are usually nested under a run.
  name: Benchling Assay Runs API
  slug: benchling-assay-runs-api
- description: Export audit log data for Benchling objects.
  name: Benchling Audit API
  slug: benchling-audit-api
- description: Endpoints to help authenticate with the rest of the API resources.
  name: Benchling Authentication API
  slug: benchling-authentication-api
- description: Blobs are opaque files that can be linked to other items in Benchling, like assay runs or results. For example, you can upload a blob, then upload an assay result that links to that blob by ID. The bl
  name: Benchling Blobs API
  slug: benchling-blobs-api
- description: Boxes are a structured inventory type, consisting of a grid of positions that can each hold one container. Unlike locations, there are a maximum number of containers that a box can hold (one per posit
  name: Benchling Boxes API
  slug: benchling-boxes-api
- description: Benchling curates codon usage data for a variety of organisms to support operations such as Codon Optimization and Back Translation.
  name: Benchling Codon Usage Tables API
  slug: benchling-codon-usage-tables-api
- description: Connect endpoints support Benchling Connect actions, like instrument data conversion.
  name: Benchling Connect API
  slug: benchling-connect-api
- description: Containers are the backbone of sample management in Benchling. They represent physical containers, such as tubes or wells, that hold quantities of biological samples (represented by the entities insid
  name: Benchling Containers API
  slug: benchling-containers-api
- description: Benchling supports custom entities for biological entities that are neither DNA, RNA, nor AA sequences. Custom entities must have an entity schema set and can have both schema fields and custom fields
  name: Benchling Custom Entities API
  slug: benchling-custom-entities-api
- description: Benchling allows users to configure their own fully-custom string representation formats for import/export of nucleotide sequences (including chemical modifications).
  name: Benchling Custom Notations API
  slug: benchling-custom-notations-api
- description: Data frames in Benchling represent tabular data that is not schematized. They contain columns with defined types and rows of data. Data frames are primarily used within specific Benchling applications
  name: Benchling Data Frames API
  slug: benchling-data-frames-api
- description: Similar to Data frames, datasets in Benchling represent tabular data that is not schematized. Datasets are saved to folders within Benchling with additional metadata, making them accessible and search
  name: Benchling Datasets API
  slug: benchling-datasets-api
- description: A DNA alignment is a Benchling object representing an alignment of multiple DNA sequences. This endpoint is deprecated, please migrate to the existing [Nucleotide Alignments endpoints.](#/Nucleotide%2
  name: Benchling DNA Alignments API
  slug: benchling-dna-alignments-api
- description: DNA Oligos are short linear DNA sequences that can be attached as primers to full DNA sequences. Just like other entities, they support schemas, tags, and aliases.
  name: Benchling DNA Oligos API
  slug: benchling-dna-oligos-api
- description: DNA sequences are the bread and butter of the Benchling Molecular Biology suite. On Benchling, these are comprised of a string of nucleotides and collections of other attributes, such as annotations a
  name: Benchling DNA Sequences API
  slug: benchling-dna-sequences-api
- description: Dropdowns are registry-wide enums. Use dropdowns to standardize on spelling and naming conventions, especially for important metadata like resistance markers.
  name: Benchling Dropdowns API
  slug: benchling-dropdowns-api
- description: Entities include DNA and AA sequences, oligos, molecules, custom entities, and other biological objects in Benchling. Entities support schemas, tags, and aliases, and can be registered.
  name: Benchling Entities API
  slug: benchling-entities-api
- description: Entries are rich text documents that allow you to capture all of your experimental data in one place.
  name: Benchling Entries API
  slug: benchling-entries-api
- description: Restriction enzymes are curated by Benchling for operations such as Digests and Codon Optimization.
  name: Benchling Enzymes API
  slug: benchling-enzymes-api
- description: The Events system allows external services to subscribe to events that are triggered in Benchling (e.g. plasmid registration, request submission, etc).
  name: Benchling Events API
  slug: benchling-events-api
- description: Export a Notebook Entry or a Legacy Workflow Stage Entry.
  name: Benchling Exports API
  slug: benchling-exports-api
- description: Feature Libraries are collections of shared canonical patterns that can be used to generate annotations on matching regions of DNA Sequences or AA Sequences.
  name: Benchling Feature Libraries API
  slug: benchling-feature-libraries-api
- description: 'Files are Benchling objects that represent files and their metadata. Compared to Blobs, which are used by most Benchling products for attachments, Files are primarily used in the Analysis and Connect '
  name: Benchling Files API
  slug: benchling-files-api
- description: Folders are nested within projects to provide additional organization.
  name: Benchling Folders API
  slug: benchling-folders-api
- description: Instrument Queries are used to query the instrument service.
  name: Benchling Instrument Queries API
  slug: benchling-instrument-queries-api
- description: Manage inventory wide objects.
  name: Benchling Inventory API
  slug: benchling-inventory-api
- description: Lab Automation endpoints support integration with lab instruments, and liquid handlers to create samples or results, and capture transfers between containers at scale.
  name: Benchling Lab Automation API
  slug: benchling-lab-automation-api
- description: List label templates.
  name: Benchling Label Templates API
  slug: benchling-label-templates-api
- description: Legacy Requests allow scientists and teams to collaborate around experimental assays and workflows.
  name: Benchling Legacy Requests API
  slug: benchling-legacy-requests-api
- description: Legacy Workflows allow orchestrating complex experiments.
  name: Benchling Legacy Workflows API
  slug: benchling-legacy-workflows-api
- description: Please use endpoints for Legacy Workflows. These deprecated endpoints will be removed once users are migrated onto Legacy Workflows endpoints.
  name: Benchling Legacy Workflows (deprecated) API
  slug: benchling-legacy-workflows-deprecated-api
- description: Manage locations objects. Like all inventory, every Location has a barcode that is unique across the registry.
  name: Benchling Locations API
  slug: benchling-locations-api
- description: Mixtures are solutions comprised of multiple ingredients where the exact quantities of each ingredient are important to track. Each ingredient is uniquely identified by its component entity.
  name: Benchling Mixtures API
  slug: benchling-mixtures-api
- description: Molecules are groups of atoms held together by bonds, representing entities smaller than DNA Sequences and AA Sequences. Just like other entities, they support schemas, tags, and aliases.
  name: Benchling Molecules API
  slug: benchling-molecules-api
- description: Monomers are chemical building blocks with specified structures used to compose modified nucleotides. Note that monomer write endpoints require tenant admin permissions.
  name: Benchling Monomers API
  slug: benchling-monomers-api
- description: A Nucleotide Alignment is a Benchling object representing an alignment of multiple DNA and/or RNA sequences.
  name: Benchling Nucleotide Alignments API
  slug: benchling-nucleotide-alignments-api
- description: 'Oligos are short linear DNA sequences that can be attached as primers to full DNA sequences. Just like other entities, they support schemas, tags, and aliases. Please migrate to the corresponding DNA '
  name: Benchling Oligos API
  slug: benchling-oligos-api
- description: View organization objects.
  name: Benchling Organizations API
  slug: benchling-organizations-api
- description: 'Plates are a structured inventory type, grids of wells that each function like containers. Plates come in two types: a traditional "fixed" type, where the wells cannot move, and a "matrix" type. A mat'
  name: Benchling Plates API
  slug: benchling-plates-api
- description: List printers.
  name: Benchling Printers API
  slug: benchling-printers-api
- description: Manage project objects.
  name: Benchling Projects API
  slug: benchling-projects-api
- description: Manage registry objects. See our documentation on [how to register entities](https://docs.benchling.com/docs/registering-entities).
  name: Benchling Registry API
  slug: benchling-registry-api
- description: RNA Oligos are short linear RNA sequences that can be attached as primers to full DNA sequences. Just like other entities, they support schemas, tags, and aliases.
  name: Benchling RNA Oligos API
  slug: benchling-rna-oligos-api
- description: Chains of linear, single stranded RNA that support most capabilities and attributes of DNA Sequences.
  name: Benchling RNA Sequences API
  slug: benchling-rna-sequences-api
- description: Schemas represent custom configuration of objects in Benchling. See this [guide in our documentation](https://docs.benchling.com/docs/schemas) on how Schemas impact our developers
  name: Benchling Schemas API
  slug: benchling-schemas-api
- description: Endpoints that perform expensive computations launch long-running tasks. These endpoints return the task ID (a UUID) in the response body. After launching a task, periodically invoke the [Get a task](
  name: Benchling Tasks API
  slug: benchling-tasks-api
- description: View team objects.
  name: Benchling Teams API
  slug: benchling-teams-api
- description: Manage user objects.
  name: Benchling Users API
  slug: benchling-users-api
- description: Manage warehouse credentials.
  name: Benchling Warehouse API
  slug: benchling-warehouse-api
- description: Workflow flowchart config versions are versioned graphs of flowchart configurations.
  name: Benchling Workflow Flowchart Config Versions API
  slug: benchling-workflow-flowchart-config-versions-api
- description: Workflow flowcharts represent the nodes and edges that a flowchart is comprised of.
  name: Benchling Workflow Flowcharts API
  slug: benchling-workflow-flowcharts-api
- description: Workflow outputs are outputs of a workflow task
  name: Benchling Workflow Outputs API
  slug: benchling-workflow-outputs-api
- description: Workflow task groups are groups of workflow tasks of the same schema
  name: Benchling Workflow Task Groups API
  slug: benchling-workflow-task-groups-api
- description: Workflow tasks encapsulate a single unit of work
  name: Benchling Workflow Tasks API
  slug: benchling-workflow-tasks-api
artifact_total: 935
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/benchling-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchling-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/benchling-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/benchling-scopes.yml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.benchling.com/docs/developer-platform-overview
- group: docs
  title: ''
  type: Reference
  url: https://benchling.com/api/reference
- group: auth
  title: ''
  type: Authentication
  url: https://docs.benchling.com/docs/getting-started-benchling-apps
- group: build
  title: ''
  type: SDKs
  url: https://docs.benchling.com/docs/getting-started-with-the-sdk
- group: build
  title: ''
  type: SDKPython
  url: https://pypi.org/project/benchling-sdk/
- group: design
  title: ''
  type: Webhooks
  url: https://docs.benchling.com/docs/getting-started-with-webhooks
- group: docs
  title: ''
  type: WebhookReference
  url: https://benchling.com/webhooks/reference
- group: other
  title: ''
  type: Events
  url: https://docs.benchling.com/docs/events-getting-started
- group: operate
  title: ''
  type: ChangeLog
  url: https://docs.benchling.com/changelog
- group: operate
  title: ''
  type: DeveloperChangelog
  url: https://docs.benchling.com/changelog/benchling-developer-changelog
- group: company
  title: ''
  type: Blog
  url: https://www.benchling.com/blog
- group: operate
  title: ''
  type: Status
  url: https://benchling.betteruptime.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benchling
- group: other
  title: ''
  type: DeveloperPlatform
  url: https://www.benchling.com/developer-platform
- group: operate
  title: ''
  type: RateLimits
  url: https://docs.benchling.com/docs/rate-limiting
- group: commercial
  title: ''
  type: Plans
  url: plans/benchling-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/benchling-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/benchling-finops.yml
created: 2026-06-13
description: Benchling is a life sciences R&D cloud platform offering a comprehensive REST API for programmatically managing molecular biology entities, assay results and runs, electronic lab notebook entries, DNA/RNA/protein sequences, inventory, and experiment workflows. The API enables integrations with lab instruments, ERP systems, LIMS, and external databases, as well as bulk data ingest/export and event-driven automation via webhooks and AWS EventBridge. API access is available to Professional and Enterprise tenants and supports user API keys, OAuth 2.0 client credentials, and OIDC authentication.
examples:
- key_count: 5
  name: Createappconfigurationitem Request
  slug: createAppConfigurationItem-request
- key_count: 6
  name: Createappconfigurationitem Response 201
  slug: createAppConfigurationItem-response-201
- key_count: 5
  name: Createblob Request
  slug: createBlob-request
- key_count: 6
  name: Createdataframe Response 200
  slug: createDataFrame-response-200
- key_count: 6
  name: Createfile Response 200
  slug: createFile-response-200
- key_count: 6
  name: Getappconfigurationitembyid Response 200
  slug: getAppConfigurationItemById-response-200
- key_count: 6
  name: Getdataframe Response 200
  slug: getDataFrame-response-200
- key_count: 6
  name: Gettask Response 200
  slug: getTask-response-200
- key_count: 6
  name: Patchdataframe Response 202
  slug: patchDataFrame-response-202
- key_count: 5
  name: Updateappconfigurationitem Request
  slug: updateAppConfigurationItem-request
finops:
- name: Benchling Finops
  service_category: ''
  slug: benchling-finops
graphqls:
- description: Benchling is a life sciences R&D cloud platform for biotech and pharma. The API covers notebook entries, sequences, molecules, assay results, registration, inventory management, plates, workflows, and
  name: Benchling GraphQL API
  slug: benchling-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benchling.png
json_schemas:
- name: AIGGenerateInputAsyncTask
  property_count: 0
  slug: AIGGenerateInputAsyncTask
- name: AOPProcessOutputAsyncTask
  property_count: 0
  slug: AOPProcessOutputAsyncTask
- name: AaAnnotation
  property_count: 7
  slug: AaAnnotation
- name: AaSequence
  property_count: 21
  slug: AaSequence
- name: AaSequenceBaseRequest
  property_count: 9
  slug: AaSequenceBaseRequest
- name: AaSequenceBaseRequestForCreate
  property_count: 0
  slug: AaSequenceBaseRequestForCreate
- name: AaSequenceBulkCreate
  property_count: 0
  slug: AaSequenceBulkCreate
- name: AaSequenceBulkUpdate
  property_count: 0
  slug: AaSequenceBulkUpdate
- name: AaSequenceBulkUpsertRequest
  property_count: 0
  slug: AaSequenceBulkUpsertRequest
- name: AaSequenceCreate
  property_count: 0
  slug: AaSequenceCreate
- name: AaSequenceRequestRegistryFields
  property_count: 1
  slug: AaSequenceRequestRegistryFields
- name: AaSequenceSummary
  property_count: 3
  slug: AaSequenceSummary
- name: AaSequenceUpdate
  property_count: 0
  slug: AaSequenceUpdate
- name: AaSequenceUpsert
  property_count: 0
  slug: AaSequenceUpsert
- name: AaSequenceWithEntityType
  property_count: 0
  slug: AaSequenceWithEntityType
- name: AaSequencesArchivalChange
  property_count: 2
  slug: AaSequencesArchivalChange
- name: AaSequencesArchive
  property_count: 2
  slug: AaSequencesArchive
- name: AaSequencesBulkCreateRequest
  property_count: 1
  slug: AaSequencesBulkCreateRequest
- name: AaSequencesBulkGet
  property_count: 1
  slug: AaSequencesBulkGet
- name: AaSequencesBulkUpdateRequest
  property_count: 1
  slug: AaSequencesBulkUpdateRequest
- name: AaSequencesBulkUpsertRequest
  property_count: 1
  slug: AaSequencesBulkUpsertRequest
- name: AaSequencesFindMatchingRegion
  property_count: 3
  slug: AaSequencesFindMatchingRegion
- name: AaSequencesMatchBases
  property_count: 6
  slug: AaSequencesMatchBases
- name: AaSequencesPaginatedList
  property_count: 2
  slug: AaSequencesPaginatedList
- name: AaSequencesSearchBases
  property_count: 6
  slug: AaSequencesSearchBases
- name: AaSequencesUnarchive
  property_count: 1
  slug: AaSequencesUnarchive
- name: AlignedNucleotideSequence
  property_count: 7
  slug: AlignedNucleotideSequence
- name: AlignedSequence
  property_count: 7
  slug: AlignedSequence
- name: AppCanvas
  property_count: 0
  slug: AppCanvas
- name: AppCanvasBase
  property_count: 0
  slug: AppCanvasBase
- name: AppCanvasCreate
  property_count: 0
  slug: AppCanvasCreate
- name: AppCanvasCreateBase
  property_count: 0
  slug: AppCanvasCreateBase
- name: AppCanvasCreateUiBlockList
  property_count: 1
  slug: AppCanvasCreateUiBlockList
- name: AppCanvasLeafNodeUiBlockList
  property_count: 1
  slug: AppCanvasLeafNodeUiBlockList
- name: AppCanvasNotePart
  property_count: 0
  slug: AppCanvasNotePart
- name: AppCanvasUiBlockList
  property_count: 1
  slug: AppCanvasUiBlockList
- name: AppCanvasUpdate
  property_count: 0
  slug: AppCanvasUpdate
- name: AppCanvasUpdateBase
  property_count: 0
  slug: AppCanvasUpdateBase
- name: AppCanvasUpdateUiBlockList
  property_count: 1
  slug: AppCanvasUpdateUiBlockList
- name: AppCanvasWriteBase
  property_count: 0
  slug: AppCanvasWriteBase
- name: AppCanvasesArchivalChange
  property_count: 1
  slug: AppCanvasesArchivalChange
- name: AppCanvasesArchive
  property_count: 2
  slug: AppCanvasesArchive
- name: AppCanvasesArchiveReason
  property_count: 0
  slug: AppCanvasesArchiveReason
- name: AppCanvasesUnarchive
  property_count: 1
  slug: AppCanvasesUnarchive
- name: AppConfigItem
  property_count: 0
  slug: AppConfigItem
- name: AppConfigItemApiMixin
  property_count: 7
  slug: AppConfigItemApiMixin
- name: AppConfigItemBooleanBulkUpdate
  property_count: 0
  slug: AppConfigItemBooleanBulkUpdate
- name: AppConfigItemBooleanCreate
  property_count: 0
  slug: AppConfigItemBooleanCreate
- name: AppConfigItemBooleanUpdate
  property_count: 2
  slug: AppConfigItemBooleanUpdate
- name: AppConfigItemBulkUpdate
  property_count: 0
  slug: AppConfigItemBulkUpdate
- name: AppConfigItemBulkUpdateMixin
  property_count: 1
  slug: AppConfigItemBulkUpdateMixin
- name: AppConfigItemCreate
  property_count: 0
  slug: AppConfigItemCreate
- name: AppConfigItemCreateMixin
  property_count: 2
  slug: AppConfigItemCreateMixin
- name: AppConfigItemDateBulkUpdate
  property_count: 0
  slug: AppConfigItemDateBulkUpdate
- name: AppConfigItemDateCreate
  property_count: 0
  slug: AppConfigItemDateCreate
- name: AppConfigItemDateUpdate
  property_count: 2
  slug: AppConfigItemDateUpdate
- name: AppConfigItemDatetimeBulkUpdate
  property_count: 0
  slug: AppConfigItemDatetimeBulkUpdate
- name: AppConfigItemDatetimeCreate
  property_count: 0
  slug: AppConfigItemDatetimeCreate
- name: AppConfigItemDatetimeUpdate
  property_count: 2
  slug: AppConfigItemDatetimeUpdate
- name: AppConfigItemFloatBulkUpdate
  property_count: 0
  slug: AppConfigItemFloatBulkUpdate
- name: AppConfigItemFloatCreate
  property_count: 0
  slug: AppConfigItemFloatCreate
- name: AppConfigItemFloatUpdate
  property_count: 2
  slug: AppConfigItemFloatUpdate
- name: AppConfigItemGenericBulkUpdate
  property_count: 0
  slug: AppConfigItemGenericBulkUpdate
- name: AppConfigItemGenericCreate
  property_count: 0
  slug: AppConfigItemGenericCreate
- name: AppConfigItemGenericUpdate
  property_count: 2
  slug: AppConfigItemGenericUpdate
- name: AppConfigItemIntegerBulkUpdate
  property_count: 0
  slug: AppConfigItemIntegerBulkUpdate
- name: AppConfigItemIntegerCreate
  property_count: 0
  slug: AppConfigItemIntegerCreate
- name: AppConfigItemIntegerUpdate
  property_count: 2
  slug: AppConfigItemIntegerUpdate
- name: AppConfigItemJsonBulkUpdate
  property_count: 0
  slug: AppConfigItemJsonBulkUpdate
- name: AppConfigItemJsonCreate
  property_count: 0
  slug: AppConfigItemJsonCreate
- name: AppConfigItemJsonUpdate
  property_count: 2
  slug: AppConfigItemJsonUpdate
- name: AppConfigItemUpdate
  property_count: 0
  slug: AppConfigItemUpdate
- name: AppConfigItemsBulkCreateRequest
  property_count: 1
  slug: AppConfigItemsBulkCreateRequest
- name: AppConfigItemsBulkUpdateRequest
  property_count: 1
  slug: AppConfigItemsBulkUpdateRequest
- name: AppConfigurationPaginatedList
  property_count: 0
  slug: AppConfigurationPaginatedList
- name: AppSession
  property_count: 8
  slug: AppSession
- name: AppSessionCreate
  property_count: 4
  slug: AppSessionCreate
- name: AppSessionMessage
  property_count: 0
  slug: AppSessionMessage
- name: AppSessionMessageCreate
  property_count: 2
  slug: AppSessionMessageCreate
- name: AppSessionMessageStyle
  property_count: 0
  slug: AppSessionMessageStyle
- name: AppSessionStatus
  property_count: 0
  slug: AppSessionStatus
- name: AppSessionUpdate
  property_count: 3
  slug: AppSessionUpdate
- name: AppSessionUpdateStatus
  property_count: 0
  slug: AppSessionUpdateStatus
- name: AppSummary
  property_count: 1
  slug: AppSummary
- name: ArchiveRecord
  property_count: 1
  slug: ArchiveRecord
- name: ArchiveRecordSet
  property_count: 0
  slug: ArchiveRecordSet
- name: ArrayElementAppConfigItem
  property_count: 0
  slug: ArrayElementAppConfigItem
- name: AssayFieldsCreate
  property_count: 0
  slug: AssayFieldsCreate
- name: AssayResult
  property_count: 14
  slug: AssayResult
- name: AssayResultCreate
  property_count: 5
  slug: AssayResultCreate
- name: AssayResultIdsRequest
  property_count: 1
  slug: AssayResultIdsRequest
- name: AssayResultIdsResponse
  property_count: 1
  slug: AssayResultIdsResponse
- name: AssayResultSchema
  property_count: 0
  slug: AssayResultSchema
- name: AssayResultSchemasPaginatedList
  property_count: 2
  slug: AssayResultSchemasPaginatedList
- name: AssayResultTransactionCreateResponse
  property_count: 1
  slug: AssayResultTransactionCreateResponse
- name: AssayResultsArchive
  property_count: 0
  slug: AssayResultsArchive
- name: AssayResultsBulkCreateInTableRequest
  property_count: 0
  slug: AssayResultsBulkCreateInTableRequest
- name: AssayResultsBulkCreateRequest
  property_count: 1
  slug: AssayResultsBulkCreateRequest
- name: AssayResultsBulkGet
  property_count: 1
  slug: AssayResultsBulkGet
- name: AssayResultsCreateErrorResponse
  property_count: 2
  slug: AssayResultsCreateErrorResponse
- name: AssayResultsCreateResponse
  property_count: 2
  slug: AssayResultsCreateResponse
- name: AssayResultsPaginatedList
  property_count: 2
  slug: AssayResultsPaginatedList
- name: AssayRun
  property_count: 14
  slug: AssayRun
- name: AssayRunCreate
  property_count: 6
  slug: AssayRunCreate
- name: AssayRunCreatedEvent
  property_count: 0
  slug: AssayRunCreatedEvent
- name: AssayRunNotePart
  property_count: 0
  slug: AssayRunNotePart
- name: AssayRunSchema
  property_count: 0
  slug: AssayRunSchema
- name: AssayRunSchemasPaginatedList
  property_count: 2
  slug: AssayRunSchemasPaginatedList
- name: AssayRunUpdate
  property_count: 2
  slug: AssayRunUpdate
- name: AssayRunUpdatedFieldsEvent
  property_count: 0
  slug: AssayRunUpdatedFieldsEvent
- name: AssayRunValidationStatus
  property_count: 0
  slug: AssayRunValidationStatus
- name: AssayRunsArchivalChange
  property_count: 1
  slug: AssayRunsArchivalChange
- name: AssayRunsArchive
  property_count: 2
  slug: AssayRunsArchive
- name: AssayRunsBulkCreateErrorResponse
  property_count: 2
  slug: AssayRunsBulkCreateErrorResponse
- name: AssayRunsBulkCreateRequest
  property_count: 1
  slug: AssayRunsBulkCreateRequest
- name: AssayRunsBulkCreateResponse
  property_count: 2
  slug: AssayRunsBulkCreateResponse
- name: AssayRunsBulkGet
  property_count: 1
  slug: AssayRunsBulkGet
- name: AssayRunsPaginatedList
  property_count: 2
  slug: AssayRunsPaginatedList
- name: AssayRunsUnarchive
  property_count: 1
  slug: AssayRunsUnarchive
- name: AsyncTask
  property_count: 4
  slug: AsyncTask
- name: AsyncTaskLink
  property_count: 1
  slug: AsyncTaskLink
- name: AuditLogExport
  property_count: 1
  slug: AuditLogExport
- name: AutoAnnotateAaSequences
  property_count: 2
  slug: AutoAnnotateAaSequences
- name: AutoAnnotateDnaSequences
  property_count: 2
  slug: AutoAnnotateDnaSequences
- name: AutoAnnotateRnaSequences
  property_count: 2
  slug: AutoAnnotateRnaSequences
- name: AutofillPartsAsyncTask
  property_count: 0
  slug: AutofillPartsAsyncTask
- name: AutofillRnaSequences
  property_count: 1
  slug: AutofillRnaSequences
- name: AutofillSequences
  property_count: 1
  slug: AutofillSequences
- name: AutofillTranscriptionsAsyncTask
  property_count: 0
  slug: AutofillTranscriptionsAsyncTask
- name: AutofillTranslationsAsyncTask
  property_count: 0
  slug: AutofillTranslationsAsyncTask
- name: AutomationFile
  property_count: 5
  slug: AutomationFile
- name: AutomationFileInputsPaginatedList
  property_count: 2
  slug: AutomationFileInputsPaginatedList
- name: AutomationInputGenerator
  property_count: 0
  slug: AutomationInputGenerator
- name: AutomationInputGeneratorCompletedV2BetaEvent
  property_count: 0
  slug: AutomationInputGeneratorCompletedV2BetaEvent
- name: AutomationInputGeneratorCompletedV2Event
  property_count: 0
  slug: AutomationInputGeneratorCompletedV2Event
- name: AutomationInputGeneratorUpdate
  property_count: 1
  slug: AutomationInputGeneratorUpdate
- name: AutomationOutputProcessor
  property_count: 0
  slug: AutomationOutputProcessor
- name: AutomationOutputProcessorArchivalChange
  property_count: 2
  slug: AutomationOutputProcessorArchivalChange
- name: AutomationOutputProcessorCompletedV2BetaEvent
  property_count: 0
  slug: AutomationOutputProcessorCompletedV2BetaEvent
- name: AutomationOutputProcessorCompletedV2Event
  property_count: 0
  slug: AutomationOutputProcessorCompletedV2Event
- name: AutomationOutputProcessorCreate
  property_count: 7
  slug: AutomationOutputProcessorCreate
- name: AutomationOutputProcessorUpdate
  property_count: 1
  slug: AutomationOutputProcessorUpdate
- name: AutomationOutputProcessorUploadedV2BetaEvent
  property_count: 0
  slug: AutomationOutputProcessorUploadedV2BetaEvent
- name: AutomationOutputProcessorUploadedV2Event
  property_count: 0
  slug: AutomationOutputProcessorUploadedV2Event
- name: AutomationOutputProcessorsArchive
  property_count: 2
  slug: AutomationOutputProcessorsArchive
- name: AutomationOutputProcessorsPaginatedList
  property_count: 2
  slug: AutomationOutputProcessorsPaginatedList
- name: AutomationOutputProcessorsUnarchive
  property_count: 1
  slug: AutomationOutputProcessorsUnarchive
- name: AutomationProgressStats
  property_count: 3
  slug: AutomationProgressStats
- name: AutomationTransformStatusFailedEventV2Event
  property_count: 0
  slug: AutomationTransformStatusFailedEventV2Event
- name: AutomationTransformStatusPendingEventV2Event
  property_count: 0
  slug: AutomationTransformStatusPendingEventV2Event
- name: AutomationTransformStatusRunningEventV2Event
  property_count: 0
  slug: AutomationTransformStatusRunningEventV2Event
- name: AutomationTransformStatusSucceededEventV2Event
  property_count: 0
  slug: AutomationTransformStatusSucceededEventV2Event
- name: BackTranslate
  property_count: 11
  slug: BackTranslate
- name: BadRequestError
  property_count: 1
  slug: BadRequestError
- name: BadRequestErrorBulk
  property_count: 0
  slug: BadRequestErrorBulk
- name: BarcodeValidationResult
  property_count: 3
  slug: BarcodeValidationResult
- name: BarcodeValidationResults
  property_count: 1
  slug: BarcodeValidationResults
- name: BarcodesList
  property_count: 1
  slug: BarcodesList
- name: BaseAppConfigItem
  property_count: 0
  slug: BaseAppConfigItem
- name: BaseAssaySchema
  property_count: 0
  slug: BaseAssaySchema
- name: BaseDropdownUIBlock
  property_count: 0
  slug: BaseDropdownUIBlock
- name: BaseError
  property_count: 3
  slug: BaseError
- name: BaseNotePart
  property_count: 2
  slug: BaseNotePart
- name: BaseSearchInputUIBlock
  property_count: 0
  slug: BaseSearchInputUIBlock
- name: BaseSelectorInputUIBlock
  property_count: 0
  slug: BaseSelectorInputUIBlock
- name: Batch
  property_count: 11
  slug: Batch
- name: BatchOrInaccessibleResource
  property_count: 0
  slug: BatchOrInaccessibleResource
- name: BatchSchema
  property_count: 0
  slug: BatchSchema
- name: BatchSchemasList
  property_count: 1
  slug: BatchSchemasList
- name: BatchSchemasPaginatedList
  property_count: 0
  slug: BatchSchemasPaginatedList
- name: BenchlingApp
  property_count: 0
  slug: BenchlingApp
- name: BenchlingAppCreate
  property_count: 2
  slug: BenchlingAppCreate
- name: BenchlingAppUpdate
  property_count: 2
  slug: BenchlingAppUpdate
- name: BenchlingAppsArchivalChange
  property_count: 1
  slug: BenchlingAppsArchivalChange
- name: BenchlingAppsArchive
  property_count: 2
  slug: BenchlingAppsArchive
- name: BenchlingAppsPaginatedList
  property_count: 0
  slug: BenchlingAppsPaginatedList
- name: BenchlingAppsUnarchive
  property_count: 1
  slug: BenchlingAppsUnarchive
- name: Blob
  property_count: 5
  slug: Blob
- name: BlobComplete
  property_count: 1
  slug: BlobComplete
- name: BlobCreate
  property_count: 5
  slug: BlobCreate
- name: BlobMultipartCreate
  property_count: 3
  slug: BlobMultipartCreate
- name: BlobPart
  property_count: 2
  slug: BlobPart
- name: BlobPartCreate
  property_count: 3
  slug: BlobPartCreate
- name: BlobUrl
  property_count: 2
  slug: BlobUrl
- name: BlobsBulkGet
  property_count: 1
  slug: BlobsBulkGet
- name: BooleanAppConfigItem
  property_count: 0
  slug: BooleanAppConfigItem
- name: Box
  property_count: 19
  slug: Box
- name: BoxContentsPaginatedList
  property_count: 2
  slug: BoxContentsPaginatedList
- name: BoxCreate
  property_count: 6
  slug: BoxCreate
- name: BoxCreationTableNotePart
  property_count: 0
  slug: BoxCreationTableNotePart
- name: BoxSchema
  property_count: 0
  slug: BoxSchema
- name: BoxSchemasList
  property_count: 1
  slug: BoxSchemasList
- name: BoxSchemasPaginatedList
  property_count: 0
  slug: BoxSchemasPaginatedList
- name: BoxUpdate
  property_count: 4
  slug: BoxUpdate
- name: BoxesArchivalChange
  property_count: 2
  slug: BoxesArchivalChange
- name: BoxesArchive
  property_count: 3
  slug: BoxesArchive
- name: BoxesBulkGet
  property_count: 1
  slug: BoxesBulkGet
- name: BoxesPaginatedList
  property_count: 2
  slug: BoxesPaginatedList
- name: BoxesUnarchive
  property_count: 1
  slug: BoxesUnarchive
- name: BulkCreateAaSequencesAsyncTask
  property_count: 0
  slug: BulkCreateAaSequencesAsyncTask
- name: BulkCreateContainersAsyncTask
  property_count: 0
  slug: BulkCreateContainersAsyncTask
- name: BulkCreateCustomEntitiesAsyncTask
  property_count: 0
  slug: BulkCreateCustomEntitiesAsyncTask
- name: BulkCreateDnaOligosAsyncTask
  property_count: 0
  slug: BulkCreateDnaOligosAsyncTask
- name: BulkCreateDnaSequencesAsyncTask
  property_count: 0
  slug: BulkCreateDnaSequencesAsyncTask
- name: BulkCreateFeaturesAsyncTask
  property_count: 0
  slug: BulkCreateFeaturesAsyncTask
- name: BulkCreateRnaOligosAsyncTask
  property_count: 0
  slug: BulkCreateRnaOligosAsyncTask
- name: BulkCreateRnaSequencesAsyncTask
  property_count: 0
  slug: BulkCreateRnaSequencesAsyncTask
- name: BulkRegisterEntitiesAsyncTask
  property_count: 0
  slug: BulkRegisterEntitiesAsyncTask
- name: BulkUpdateAaSequencesAsyncTask
  property_count: 0
  slug: BulkUpdateAaSequencesAsyncTask
- name: BulkUpdateContainersAsyncTask
  property_count: 0
  slug: BulkUpdateContainersAsyncTask
- name: BulkUpdateCustomEntitiesAsyncTask
  property_count: 0
  slug: BulkUpdateCustomEntitiesAsyncTask
- name: BulkUpdateDnaOligosAsyncTask
  property_count: 0
  slug: BulkUpdateDnaOligosAsyncTask
- name: BulkUpdateDnaSequencesAsyncTask
  property_count: 0
  slug: BulkUpdateDnaSequencesAsyncTask
- name: BulkUpdateRnaOligosAsyncTask
  property_count: 0
  slug: BulkUpdateRnaOligosAsyncTask
- name: BulkUpdateRnaSequencesAsyncTask
  property_count: 0
  slug: BulkUpdateRnaSequencesAsyncTask
- name: ButtonUiBlock
  property_count: 0
  slug: ButtonUiBlock
- name: ButtonUiBlockCreate
  property_count: 0
  slug: ButtonUiBlockCreate
- name: ButtonUiBlockUpdate
  property_count: 0
  slug: ButtonUiBlockUpdate
- name: ChartNotePart
  property_count: 0
  slug: ChartNotePart
- name: CheckboxNotePart
  property_count: 0
  slug: CheckboxNotePart
- name: CheckoutRecord
  property_count: 4
  slug: CheckoutRecord
- name: ChipUiBlock
  property_count: 0
  slug: ChipUiBlock
- name: ChipUiBlockCreate
  property_count: 0
  slug: ChipUiBlockCreate
- name: ChipUiBlockUpdate
  property_count: 0
  slug: ChipUiBlockUpdate
- name: ClustaloOptions
  property_count: 5
  slug: ClustaloOptions
- name: CodonUsageTable
  property_count: 2
  slug: CodonUsageTable
- name: CodonUsageTablesPaginatedList
  property_count: 0
  slug: CodonUsageTablesPaginatedList
- name: ConflictError
  property_count: 1
  slug: ConflictError
- name: Container
  property_count: 21
  slug: Container
- name: ContainerBulkUpdateItem
  property_count: 0
  slug: ContainerBulkUpdateItem
- name: ContainerContent
  property_count: 3
  slug: ContainerContent
- name: ContainerContentUpdate
  property_count: 1
  slug: ContainerContentUpdate
- name: ContainerContentsList
  property_count: 1
  slug: ContainerContentsList
- name: ContainerCreate
  property_count: 0
  slug: ContainerCreate
- name: ContainerLabels
  property_count: 3
  slug: ContainerLabels
- name: ContainerQuantity
  property_count: 2
  slug: ContainerQuantity
- name: ContainerSchema
  property_count: 0
  slug: ContainerSchema
- name: ContainerSchemasList
  property_count: 1
  slug: ContainerSchemasList
- name: ContainerSchemasPaginatedList
  property_count: 0
  slug: ContainerSchemasPaginatedList
- name: ContainerTransfer
  property_count: 0
  slug: ContainerTransfer
- name: ContainerTransferBase
  property_count: 8
  slug: ContainerTransferBase
- name: ContainerTransferDestinationContentsItem
  property_count: 2
  slug: ContainerTransferDestinationContentsItem
- name: ContainerUpdate
  property_count: 0
  slug: ContainerUpdate
- name: ContainerWithCoordinates
  property_count: 0
  slug: ContainerWithCoordinates
- name: ContainerWriteBase
  property_count: 6
  slug: ContainerWriteBase
- name: ContainersArchivalChange
  property_count: 1
  slug: ContainersArchivalChange
- name: ContainersArchive
  property_count: 3
  slug: ContainersArchive
- name: ContainersBulkCreateRequest
  property_count: 1
  slug: ContainersBulkCreateRequest
- name: ContainersBulkUpdateRequest
  property_count: 1
  slug: ContainersBulkUpdateRequest
- name: ContainersCheckin
  property_count: 2
  slug: ContainersCheckin
- name: ContainersCheckout
  property_count: 3
  slug: ContainersCheckout
- name: ContainersList
  property_count: 1
  slug: ContainersList
- name: ContainersPaginatedList
  property_count: 0
  slug: ContainersPaginatedList
- name: ContainersUnarchive
  property_count: 1
  slug: ContainersUnarchive
- name: ConvertToASM
  property_count: 3
  slug: ConvertToASM
- name: ConvertToCSV
  property_count: 6
  slug: ConvertToCSV
- name: CreateConsensusAlignmentAsyncTask
  property_count: 0
  slug: CreateConsensusAlignmentAsyncTask
- name: CreateEntityIntoRegistry
  property_count: 4
  slug: CreateEntityIntoRegistry
- name: CreateNucleotideConsensusAlignmentAsyncTask
  property_count: 0
  slug: CreateNucleotideConsensusAlignmentAsyncTask
- name: CreateNucleotideTemplateAlignmentAsyncTask
  property_count: 0
  slug: CreateNucleotideTemplateAlignmentAsyncTask
- name: CreateTemplateAlignmentAsyncTask
  property_count: 0
  slug: CreateTemplateAlignmentAsyncTask
- name: CreationOrigin
  property_count: 4
  slug: CreationOrigin
- name: CustomEntitiesArchivalChange
  property_count: 2
  slug: CustomEntitiesArchivalChange
- name: CustomEntitiesArchive
  property_count: 2
  slug: CustomEntitiesArchive
- name: CustomEntitiesBulkCreateRequest
  property_count: 1
  slug: CustomEntitiesBulkCreateRequest
- name: CustomEntitiesBulkUpdateRequest
  property_count: 1
  slug: CustomEntitiesBulkUpdateRequest
- name: CustomEntitiesBulkUpsertRequest
  property_count: 1
  slug: CustomEntitiesBulkUpsertRequest
- name: CustomEntitiesList
  property_count: 1
  slug: CustomEntitiesList
- name: CustomEntitiesPaginatedList
  property_count: 2
  slug: CustomEntitiesPaginatedList
- name: CustomEntitiesUnarchive
  property_count: 1
  slug: CustomEntitiesUnarchive
- name: CustomEntity
  property_count: 18
  slug: CustomEntity
- name: CustomEntityBaseRequest
  property_count: 7
  slug: CustomEntityBaseRequest
- name: CustomEntityBaseRequestForCreate
  property_count: 0
  slug: CustomEntityBaseRequestForCreate
- name: CustomEntityBulkCreate
  property_count: 0
  slug: CustomEntityBulkCreate
- name: CustomEntityBulkUpdate
  property_count: 1
  slug: CustomEntityBulkUpdate
- name: CustomEntityBulkUpsertRequest
  property_count: 0
  slug: CustomEntityBulkUpsertRequest
- name: CustomEntityCreate
  property_count: 0
  slug: CustomEntityCreate
- name: CustomEntityRequestRegistryFields
  property_count: 1
  slug: CustomEntityRequestRegistryFields
- name: CustomEntitySummary
  property_count: 3
  slug: CustomEntitySummary
- name: CustomEntityUpdate
  property_count: 0
  slug: CustomEntityUpdate
- name: CustomEntityUpsertRequest
  property_count: 0
  slug: CustomEntityUpsertRequest
- name: CustomEntityWithEntityType
  property_count: 0
  slug: CustomEntityWithEntityType
- name: CustomField
  property_count: 1
  slug: CustomField
- name: CustomFields
  property_count: 0
  slug: CustomFields
- name: CustomNotation
  property_count: 3
  slug: CustomNotation
- name: CustomNotationAlias
  property_count: 9
  slug: CustomNotationAlias
- name: CustomNotationRequest
  property_count: 2
  slug: CustomNotationRequest
- name: CustomNotationsPaginatedList
  property_count: 0
  slug: CustomNotationsPaginatedList
- name: DataFrame
  property_count: 0
  slug: DataFrame
- name: DataFrameColumnMetadata
  property_count: 2
  slug: DataFrameColumnMetadata
- name: DataFrameColumnTypeMetadata
  property_count: 0
  slug: DataFrameColumnTypeMetadata
- name: DataFrameColumnTypeNameEnum
  property_count: 1
  slug: DataFrameColumnTypeNameEnum
- name: DataFrameCreate
  property_count: 0
  slug: DataFrameCreate
- name: DataFrameCreateManifest
  property_count: 1
  slug: DataFrameCreateManifest
- name: DataFrameManifest
  property_count: 1
  slug: DataFrameManifest
- name: DataFrameUpdate
  property_count: 1
  slug: DataFrameUpdate
- name: Dataset
  property_count: 0
  slug: Dataset
- name: DatasetCreate
  property_count: 5
  slug: DatasetCreate
- name: DatasetUpdate
  property_count: 3
  slug: DatasetUpdate
- name: DatasetsArchivalChange
  property_count: 1
  slug: DatasetsArchivalChange
- name: DatasetsArchive
  property_count: 2
  slug: DatasetsArchive
- name: DatasetsPaginatedList
  property_count: 2
  slug: DatasetsPaginatedList
- name: DatasetsUnarchive
  property_count: 1
  slug: DatasetsUnarchive
- name: DateAppConfigItem
  property_count: 0
  slug: DateAppConfigItem
- name: DatetimeAppConfigItem
  property_count: 0
  slug: DatetimeAppConfigItem
- name: DeprecatedAutomationOutputProcessorsPaginatedList
  property_count: 2
  slug: DeprecatedAutomationOutputProcessorsPaginatedList
- name: DeprecatedContainerVolumeForInput
  property_count: 2
  slug: DeprecatedContainerVolumeForInput
- name: DeprecatedContainerVolumeForResponse
  property_count: 0
  slug: DeprecatedContainerVolumeForResponse
- name: DeprecatedEntitySchema
  property_count: 0
  slug: DeprecatedEntitySchema
- name: DeprecatedEntitySchemasList
  property_count: 1
  slug: DeprecatedEntitySchemasList
- name: DnaAlignment
  property_count: 0
  slug: DnaAlignment
- name: DnaAlignmentBase
  property_count: 5
  slug: DnaAlignmentBase
- name: DnaAlignmentSummary
  property_count: 7
  slug: DnaAlignmentSummary
- name: DnaAlignmentsPaginatedList
  property_count: 0
  slug: DnaAlignmentsPaginatedList
- name: DnaAnnotation
  property_count: 0
  slug: DnaAnnotation
- name: DnaConsensusAlignmentCreate
  property_count: 0
  slug: DnaConsensusAlignmentCreate
- name: DnaOligo
  property_count: 0
  slug: DnaOligo
- name: DnaOligoBulkUpdate
  property_count: 0
  slug: DnaOligoBulkUpdate
- name: DnaOligoCreate
  property_count: 0
  slug: DnaOligoCreate
- name: DnaOligoUpdate
  property_count: 0
  slug: DnaOligoUpdate
- name: DnaOligoWithEntityType
  property_count: 0
  slug: DnaOligoWithEntityType
- name: DnaOligosArchivalChange
  property_count: 2
  slug: DnaOligosArchivalChange
- name: DnaOligosArchive
  property_count: 2
  slug: DnaOligosArchive
- name: DnaOligosBulkCreateRequest
  property_count: 1
  slug: DnaOligosBulkCreateRequest
- name: DnaOligosBulkUpdateRequest
  property_count: 1
  slug: DnaOligosBulkUpdateRequest
- name: DnaOligosBulkUpsertRequest
  property_count: 1
  slug: DnaOligosBulkUpsertRequest
- name: DnaOligosPaginatedList
  property_count: 0
  slug: DnaOligosPaginatedList
- name: DnaOligosUnarchive
  property_count: 1
  slug: DnaOligosUnarchive
- name: DnaSequence
  property_count: 27
  slug: DnaSequence
- name: DnaSequenceBaseRequest
  property_count: 13
  slug: DnaSequenceBaseRequest
- name: DnaSequenceBaseRequestForCreate
  property_count: 0
  slug: DnaSequenceBaseRequestForCreate
- name: DnaSequenceBulkCreate
  property_count: 0
  slug: DnaSequenceBulkCreate
- name: DnaSequenceBulkUpdate
  property_count: 0
  slug: DnaSequenceBulkUpdate
- name: DnaSequenceBulkUpsertRequest
  property_count: 0
  slug: DnaSequenceBulkUpsertRequest
- name: DnaSequenceCreate
  property_count: 0
  slug: DnaSequenceCreate
- name: DnaSequencePart
  property_count: 0
  slug: DnaSequencePart
- name: DnaSequenceRequestRegistryFields
  property_count: 1
  slug: DnaSequenceRequestRegistryFields
- name: DnaSequenceSummary
  property_count: 3
  slug: DnaSequenceSummary
- name: DnaSequenceTranscription
  property_count: 4
  slug: DnaSequenceTranscription
- name: DnaSequenceUpdate
  property_count: 0
  slug: DnaSequenceUpdate
- name: DnaSequenceUpsertRequest
  property_count: 0
  slug: DnaSequenceUpsertRequest
- name: DnaSequenceWithEntityType
  property_count: 0
  slug: DnaSequenceWithEntityType
- name: DnaSequencesArchivalChange
  property_count: 2
  slug: DnaSequencesArchivalChange
- name: DnaSequencesArchive
  property_count: 2
  slug: DnaSequencesArchive
- name: DnaSequencesBulkCreateRequest
  property_count: 1
  slug: DnaSequencesBulkCreateRequest
- name: DnaSequencesBulkGet
  property_count: 1
  slug: DnaSequencesBulkGet
- name: DnaSequencesBulkUpdateRequest
  property_count: 1
  slug: DnaSequencesBulkUpdateRequest
- name: DnaSequencesBulkUpsertRequest
  property_count: 1
  slug: DnaSequencesBulkUpsertRequest
- name: DnaSequencesFindMatchingRegion
  property_count: 3
  slug: DnaSequencesFindMatchingRegion
- name: DnaSequencesPaginatedList
  property_count: 2
  slug: DnaSequencesPaginatedList
- name: DnaSequencesUnarchive
  property_count: 1
  slug: DnaSequencesUnarchive
- name: DnaTemplateAlignmentCreate
  property_count: 0
  slug: DnaTemplateAlignmentCreate
- name: DnaTemplateAlignmentFile
  property_count: 2
  slug: DnaTemplateAlignmentFile
- name: Dropdown
  property_count: 0
  slug: Dropdown
- name: DropdownCreate
  property_count: 3
  slug: DropdownCreate
- name: DropdownFieldDefinition
  property_count: 0
  slug: DropdownFieldDefinition
- name: DropdownMultiValueUiBlock
  property_count: 0
  slug: DropdownMultiValueUiBlock
- name: DropdownMultiValueUiBlockCreate
  property_count: 0
  slug: DropdownMultiValueUiBlockCreate
- name: DropdownMultiValueUiBlockUpdate
  property_count: 0
  slug: DropdownMultiValueUiBlockUpdate
- name: DropdownOption
  property_count: 3
  slug: DropdownOption
- name: DropdownOptionCreate
  property_count: 1
  slug: DropdownOptionCreate
- name: DropdownOptionUpdate
  property_count: 2
  slug: DropdownOptionUpdate
- name: DropdownOptionsArchivalChange
  property_count: 1
  slug: DropdownOptionsArchivalChange
- name: DropdownOptionsArchive
  property_count: 2
  slug: DropdownOptionsArchive
- name: DropdownOptionsUnarchive
  property_count: 1
  slug: DropdownOptionsUnarchive
- name: DropdownSummariesPaginatedList
  property_count: 2
  slug: DropdownSummariesPaginatedList
- name: DropdownSummary
  property_count: 2
  slug: DropdownSummary
- name: DropdownUiBlock
  property_count: 0
  slug: DropdownUiBlock
- name: DropdownUiBlockCreate
  property_count: 0
  slug: DropdownUiBlockCreate
- name: DropdownUiBlockUpdate
  property_count: 0
  slug: DropdownUiBlockUpdate
- name: DropdownUpdate
  property_count: 1
  slug: DropdownUpdate
- name: DropdownsRegistryList
  property_count: 1
  slug: DropdownsRegistryList
- name: EmptyObject
  property_count: 0
  slug: EmptyObject
- name: EntitiesBulkUpsertRequest
  property_count: 6
  slug: EntitiesBulkUpsertRequest
- name: Entity
  property_count: 0
  slug: Entity
- name: EntityArchiveReason
  property_count: 0
  slug: EntityArchiveReason
- name: EntityBulkUpsertBaseRequest
  property_count: 0
  slug: EntityBulkUpsertBaseRequest
- name: EntityLabels
  property_count: 3
  slug: EntityLabels
- name: EntityOrInaccessibleResource
  property_count: 0
  slug: EntityOrInaccessibleResource
- name: EntityRegisteredEvent
  property_count: 0
  slug: EntityRegisteredEvent
- name: EntitySchema
  property_count: 0
  slug: EntitySchema
- name: EntitySchemaAppConfigItem
  property_count: 0
  slug: EntitySchemaAppConfigItem
- name: EntitySchemasPaginatedList
  property_count: 2
  slug: EntitySchemasPaginatedList
- name: EntityUpsertBaseRequest
  property_count: 5
  slug: EntityUpsertBaseRequest
- name: Entries
  property_count: 1
  slug: Entries
- name: EntriesArchivalChange
  property_count: 1
  slug: EntriesArchivalChange
- name: EntriesArchive
  property_count: 2
  slug: EntriesArchive
- name: EntriesPaginatedList
  property_count: 2
  slug: EntriesPaginatedList
- name: EntriesUnarchive
  property_count: 1
  slug: EntriesUnarchive
- name: Entry
  property_count: 18
  slug: Entry
- name: EntryById
  property_count: 1
  slug: EntryById
- name: EntryCreate
  property_count: 8
  slug: EntryCreate
- name: EntryCreatedEvent
  property_count: 0
  slug: EntryCreatedEvent
- name: EntryDay
  property_count: 3
  slug: EntryDay
- name: EntryExternalFile
  property_count: 4
  slug: EntryExternalFile
- name: EntryExternalFileById
  property_count: 1
  slug: EntryExternalFileById
- name: EntryLink
  property_count: 3
  slug: EntryLink
- name: EntryNotePart
  property_count: 0
  slug: EntryNotePart
- name: EntryReviewProcess
  property_count: 5
  slug: EntryReviewProcess
- name: EntrySchema
  property_count: 3
  slug: EntrySchema
- name: EntrySchemaDetailed
  property_count: 0
  slug: EntrySchemaDetailed
- name: EntrySchemasPaginatedList
  property_count: 2
  slug: EntrySchemasPaginatedList
- name: EntryTable
  property_count: 3
  slug: EntryTable
- name: EntryTableCell
  property_count: 2
  slug: EntryTableCell
- name: EntryTableRow
  property_count: 1
  slug: EntryTableRow
- name: EntryTemplate
  property_count: 12
  slug: EntryTemplate
- name: EntryTemplateDay
  property_count: 3
  slug: EntryTemplateDay
- name: EntryTemplateUpdate
  property_count: 5
  slug: EntryTemplateUpdate
- name: EntryTemplatesPaginatedList
  property_count: 2
  slug: EntryTemplatesPaginatedList
- name: EntryUpdate
  property_count: 5
  slug: EntryUpdate
- name: EntryUpdatedAssignedReviewersEvent
  property_count: 0
  slug: EntryUpdatedAssignedReviewersEvent
- name: EntryUpdatedFieldsEvent
  property_count: 0
  slug: EntryUpdatedFieldsEvent
- name: EntryUpdatedReviewRecordEvent
  property_count: 0
  slug: EntryUpdatedReviewRecordEvent
- name: EntryUpdatedReviewSnapshotBetaEvent
  property_count: 0
  slug: EntryUpdatedReviewSnapshotBetaEvent
- name: Enzyme
  property_count: 6
  slug: Enzyme
- name: EnzymesPaginatedList
  property_count: 0
  slug: EnzymesPaginatedList
- name: Event
  property_count: 0
  slug: Event
- name: EventBase
  property_count: 5
  slug: EventBase
- name: EventsPaginatedList
  property_count: 2
  slug: EventsPaginatedList
- name: ExecuteSampleGroups
  property_count: 0
  slug: ExecuteSampleGroups
- name: ExperimentalWellRole
  property_count: 3
  slug: ExperimentalWellRole
- name: ExportAuditLogAsyncTask
  property_count: 0
  slug: ExportAuditLogAsyncTask
- name: ExportItemRequest
  property_count: 2
  slug: ExportItemRequest
- name: ExportsAsyncTask
  property_count: 0
  slug: ExportsAsyncTask
- name: ExternalFileNotePart
  property_count: 0
  slug: ExternalFileNotePart
- name: Feature
  property_count: 0
  slug: Feature
- name: FeatureBase
  property_count: 5
  slug: FeatureBase
- name: FeatureBulkCreate
  property_count: 0
  slug: FeatureBulkCreate
- name: FeatureCreate
  property_count: 0
  slug: FeatureCreate
- name: FeatureLibrariesPaginatedList
  property_count: 0
  slug: FeatureLibrariesPaginatedList
- name: FeatureLibrary
  property_count: 0
  slug: FeatureLibrary
- name: FeatureLibraryBase
  property_count: 2
  slug: FeatureLibraryBase
- name: FeatureLibraryCreate
  property_count: 0
  slug: FeatureLibraryCreate
- name: FeatureLibraryUpdate
  property_count: 0
  slug: FeatureLibraryUpdate
- name: FeatureUpdate
  property_count: 0
  slug: FeatureUpdate
- name: FeaturesBulkCreateRequest
  property_count: 1
  slug: FeaturesBulkCreateRequest
- name: FeaturesPaginatedList
  property_count: 0
  slug: FeaturesPaginatedList
- name: Field
  property_count: 5
  slug: Field
- name: FieldAppConfigItem
  property_count: 0
  slug: FieldAppConfigItem
- name: FieldDefinition
  property_count: 6
  slug: FieldDefinition
- name: FieldType
  property_count: 0
  slug: FieldType
- name: FieldValueWithResolution
  property_count: 0
  slug: FieldValueWithResolution
- name: FieldWithResolution
  property_count: 0
  slug: FieldWithResolution
- name: Fields
  property_count: 0
  slug: Fields
- name: FieldsWithResolution
  property_count: 0
  slug: FieldsWithResolution
- name: File
  property_count: 0
  slug: File
- name: FileCreate
  property_count: 4
  slug: FileCreate
- name: FileStatus
  property_count: 2
  slug: FileStatus
- name: FileUpdate
  property_count: 4
  slug: FileUpdate
- name: FileUploadUiBlock
  property_count: 0
  slug: FileUploadUiBlock
- name: FileUploadUiBlockCreate
  property_count: 0
  slug: FileUploadUiBlockCreate
- name: FileUploadUiBlockUpdate
  property_count: 0
  slug: FileUploadUiBlockUpdate
- name: FilesArchivalChange
  property_count: 1
  slug: FilesArchivalChange
- name: FilesArchive
  property_count: 2
  slug: FilesArchive
- name: FilesPaginatedList
  property_count: 2
  slug: FilesPaginatedList
- name: FilesUnarchive
  property_count: 1
  slug: FilesUnarchive
- name: FindMatchingRegionsAsyncTask
  property_count: 0
  slug: FindMatchingRegionsAsyncTask
- name: FindMatchingRegionsDnaAsyncTask
  property_count: 0
  slug: FindMatchingRegionsDnaAsyncTask
- name: FloatAppConfigItem
  property_count: 0
  slug: FloatAppConfigItem
- name: FloatFieldDefinition
  property_count: 0
  slug: FloatFieldDefinition
- name: Folder
  property_count: 5
  slug: Folder
- name: FolderCreate
  property_count: 2
  slug: FolderCreate
- name: FoldersArchivalChange
  property_count: 8
  slug: FoldersArchivalChange
- name: FoldersArchive
  property_count: 2
  slug: FoldersArchive
- name: FoldersPaginatedList
  property_count: 2
  slug: FoldersPaginatedList
- name: FoldersUnarchive
  property_count: 1
  slug: FoldersUnarchive
- name: ForbiddenError
  property_count: 1
  slug: ForbiddenError
- name: ForbiddenRestrictedSampleError
  property_count: 1
  slug: ForbiddenRestrictedSampleError
- name: GenericApiIdentifiedAppConfigItem
  property_count: 0
  slug: GenericApiIdentifiedAppConfigItem
- name: GenericEntity
  property_count: 17
  slug: GenericEntity
- name: InaccessibleResource
  property_count: 3
  slug: InaccessibleResource
- name: Ingredient
  property_count: 10
  slug: Ingredient
- name: IngredientMeasurementUnits
  property_count: 0
  slug: IngredientMeasurementUnits
- name: IngredientWriteParams
  property_count: 8
  slug: IngredientWriteParams
- name: InitialTable
  property_count: 2
  slug: InitialTable
- name: InstrumentQuery
  property_count: 8
  slug: InstrumentQuery
- name: IntegerAppConfigItem
  property_count: 0
  slug: IntegerAppConfigItem
- name: IntegerFieldDefinition
  property_count: 0
  slug: IntegerFieldDefinition
- name: InteractiveUiBlock
  property_count: 2
  slug: InteractiveUiBlock
- name: InventoryContainerTableNotePart
  property_count: 0
  slug: InventoryContainerTableNotePart
- name: InventoryPlateTableNotePart
  property_count: 0
  slug: InventoryPlateTableNotePart
- name: JsonAppConfigItem
  property_count: 0
  slug: JsonAppConfigItem
- name: LabAutomationBenchlingAppError
  property_count: 1
  slug: LabAutomationBenchlingAppError
- name: LabAutomationBenchlingAppErrors
  property_count: 1
  slug: LabAutomationBenchlingAppErrors
- name: LabAutomationTransform
  property_count: 9
  slug: LabAutomationTransform
- name: LabAutomationTransformUpdate
  property_count: 2
  slug: LabAutomationTransformUpdate
- name: LabelTemplate
  property_count: 3
  slug: LabelTemplate
- name: LabelTemplatesList
  property_count: 1
  slug: LabelTemplatesList
- name: LegacyWorkflow
  property_count: 6
  slug: LegacyWorkflow
- name: LegacyWorkflowList
  property_count: 1
  slug: LegacyWorkflowList
- name: LegacyWorkflowPatch
  property_count: 3
  slug: LegacyWorkflowPatch
- name: LegacyWorkflowSample
  property_count: 5
  slug: LegacyWorkflowSample
- name: LegacyWorkflowSampleList
  property_count: 1
  slug: LegacyWorkflowSampleList
- name: LegacyWorkflowStage
  property_count: 3
  slug: LegacyWorkflowStage
- name: LegacyWorkflowStageList
  property_count: 1
  slug: LegacyWorkflowStageList
- name: LegacyWorkflowStageRun
  property_count: 4
  slug: LegacyWorkflowStageRun
- name: LegacyWorkflowStageRunList
  property_count: 1
  slug: LegacyWorkflowStageRunList
- name: LinkedAppConfigResource
  property_count: 0
  slug: LinkedAppConfigResource
- name: LinkedAppConfigResourceMixin
  property_count: 1
  slug: LinkedAppConfigResourceMixin
- name: LinkedAppConfigResourceSummary
  property_count: 2
  slug: LinkedAppConfigResourceSummary
- name: ListingError
  property_count: 1
  slug: ListingError
- name: Location
  property_count: 14
  slug: Location
- name: LocationCreate
  property_count: 5
  slug: LocationCreate
- name: LocationSchema
  property_count: 0
  slug: LocationSchema
- name: LocationSchemasList
  property_count: 1
  slug: LocationSchemasList
- name: LocationSchemasPaginatedList
  property_count: 0
  slug: LocationSchemasPaginatedList
- name: LocationUpdate
  property_count: 3
  slug: LocationUpdate
- name: LocationsArchivalChange
  property_count: 4
  slug: LocationsArchivalChange
- name: LocationsArchive
  property_count: 3
  slug: LocationsArchive
- name: LocationsBulkGet
  property_count: 1
  slug: LocationsBulkGet
- name: LocationsPaginatedList
  property_count: 2
  slug: LocationsPaginatedList
- name: LocationsUnarchive
  property_count: 1
  slug: LocationsUnarchive
- name: LookupTableNotePart
  property_count: 0
  slug: LookupTableNotePart
- name: MafftOptions
  property_count: 6
  slug: MafftOptions
- name: MarkdownUiBlock
  property_count: 3
  slug: MarkdownUiBlock
- name: MarkdownUiBlockCreate
  property_count: 0
  slug: MarkdownUiBlockCreate
- name: MarkdownUiBlockUpdate
  property_count: 0
  slug: MarkdownUiBlockUpdate
- name: MatchBasesRequest
  property_count: 6
  slug: MatchBasesRequest
- name: Measurement
  property_count: 2
  slug: Measurement
- name: Membership
  property_count: 2
  slug: Membership
- name: MembershipCreate
  property_count: 2
  slug: MembershipCreate
- name: MembershipUpdate
  property_count: 1
  slug: MembershipUpdate
- name: MembershipsPaginatedList
  property_count: 0
  slug: MembershipsPaginatedList
- name: Mixture
  property_count: 21
  slug: Mixture
- name: MixtureBulkUpdate
  property_count: 0
  slug: MixtureBulkUpdate
- name: MixtureCreate
  property_count: 0
  slug: MixtureCreate
- name: MixtureMeasurementUnits
  property_count: 0
  slug: MixtureMeasurementUnits
- name: MixturePrepTableNotePart
  property_count: 0
  slug: MixturePrepTableNotePart
- name: MixtureUpdate
  property_count: 11
  slug: MixtureUpdate
- name: MixtureWithEntityType
  property_count: 0
  slug: MixtureWithEntityType
- name: MixturesArchivalChange
  property_count: 1
  slug: MixturesArchivalChange
- name: MixturesArchive
  property_count: 2
  slug: MixturesArchive
- name: MixturesBulkCreateRequest
  property_count: 1
  slug: MixturesBulkCreateRequest
- name: MixturesBulkUpdateRequest
  property_count: 1
  slug: MixturesBulkUpdateRequest
- name: MixturesPaginatedList
  property_count: 2
  slug: MixturesPaginatedList
- name: MixturesUnarchive
  property_count: 1
  slug: MixturesUnarchive
- name: Molecule
  property_count: 19
  slug: Molecule
- name: MoleculeBaseRequest
  property_count: 8
  slug: MoleculeBaseRequest
- name: MoleculeBaseRequestForCreate
  property_count: 0
  slug: MoleculeBaseRequestForCreate
- name: MoleculeBulkUpdate
  property_count: 0
  slug: MoleculeBulkUpdate
- name: MoleculeBulkUpsertRequest
  property_count: 0
  slug: MoleculeBulkUpsertRequest
- name: MoleculeCreate
  property_count: 0
  slug: MoleculeCreate
- name: MoleculeStructure
  property_count: 2
  slug: MoleculeStructure
- name: MoleculeUpdate
  property_count: 0
  slug: MoleculeUpdate
- name: MoleculeUpsertRequest
  property_count: 0
  slug: MoleculeUpsertRequest
- name: MoleculeWithEntityType
  property_count: 0
  slug: MoleculeWithEntityType
- name: MoleculesArchivalChange
  property_count: 2
  slug: MoleculesArchivalChange
- name: MoleculesArchive
  property_count: 2
  slug: MoleculesArchive
- name: MoleculesBulkCreateRequest
  property_count: 1
  slug: MoleculesBulkCreateRequest
- name: MoleculesBulkUpdateRequest
  property_count: 1
  slug: MoleculesBulkUpdateRequest
- name: MoleculesBulkUpsertRequest
  property_count: 1
  slug: MoleculesBulkUpsertRequest
- name: MoleculesPaginatedList
  property_count: 0
  slug: MoleculesPaginatedList
- name: MoleculesUnarchive
  property_count: 1
  slug: MoleculesUnarchive
- name: Monomer
  property_count: 17
  slug: Monomer
- name: MonomerBaseRequest
  property_count: 6
  slug: MonomerBaseRequest
- name: MonomerCreate
  property_count: 0
  slug: MonomerCreate
- name: MonomerPolymerType
  property_count: 0
  slug: MonomerPolymerType
- name: MonomerType
  property_count: 0
  slug: MonomerType
- name: MonomerUpdate
  property_count: 0
  slug: MonomerUpdate
- name: MonomerVisualSymbol
  property_count: 0
  slug: MonomerVisualSymbol
- name: MonomersArchivalChange
  property_count: 2
  slug: MonomersArchivalChange
- name: MonomersArchive
  property_count: 2
  slug: MonomersArchive
- name: MonomersPaginatedList
  property_count: 0
  slug: MonomersPaginatedList
- name: MonomersUnarchive
  property_count: 1
  slug: MonomersUnarchive
- name: MultipleContainersTransfer
  property_count: 0
  slug: MultipleContainersTransfer
- name: MultipleContainersTransfersList
  property_count: 1
  slug: MultipleContainersTransfersList
- name: NameTemplatePart
  property_count: 4
  slug: NameTemplatePart
- name: NamingStrategy
  property_count: 0
  slug: NamingStrategy
- name: NotFoundError
  property_count: 1
  slug: NotFoundError
- name: NucleotideAlignment
  property_count: 0
  slug: NucleotideAlignment
- name: NucleotideAlignmentBase
  property_count: 5
  slug: NucleotideAlignmentBase
- name: NucleotideAlignmentFile
  property_count: 2
  slug: NucleotideAlignmentFile
- name: NucleotideAlignmentSummary
  property_count: 7
  slug: NucleotideAlignmentSummary
- name: NucleotideAlignmentsPaginatedList
  property_count: 0
  slug: NucleotideAlignmentsPaginatedList
- name: NucleotideConsensusAlignmentCreate
  property_count: 0
  slug: NucleotideConsensusAlignmentCreate
- name: NucleotideSequencePart
  property_count: 3
  slug: NucleotideSequencePart
- name: NucleotideTemplateAlignmentCreate
  property_count: 0
  slug: NucleotideTemplateAlignmentCreate
- name: OAuthBadRequestError
  property_count: 1
  slug: OAuthBadRequestError
- name: OAuthUnauthorizedError
  property_count: 1
  slug: OAuthUnauthorizedError
- name: Oligo
  property_count: 20
  slug: Oligo
- name: OligoBaseRequest
  property_count: 8
  slug: OligoBaseRequest
- name: OligoBaseRequestForCreate
  property_count: 0
  slug: OligoBaseRequestForCreate
- name: OligoBulkUpsertRequest
  property_count: 0
  slug: OligoBulkUpsertRequest
- name: OligoCreate
  property_count: 0
  slug: OligoCreate
- name: OligoUpdate
  property_count: 0
  slug: OligoUpdate
- name: OligoUpsertRequest
  property_count: 0
  slug: OligoUpsertRequest
- name: OligosArchivalChange
  property_count: 2
  slug: OligosArchivalChange
- name: OligosArchive
  property_count: 2
  slug: OligosArchive
- name: OligosBulkCreateRequest
  property_count: 1
  slug: OligosBulkCreateRequest
- name: OligosBulkGet
  property_count: 1
  slug: OligosBulkGet
- name: OligosPaginatedList
  property_count: 0
  slug: OligosPaginatedList
- name: OligosUnarchive
  property_count: 1
  slug: OligosUnarchive
- name: OptimizeCodons
  property_count: 11
  slug: OptimizeCodons
- name: Organization
  property_count: 3
  slug: Organization
- name: OrganizationSummary
  property_count: 3
  slug: OrganizationSummary
- name: OrganizationsPaginatedList
  property_count: 0
  slug: OrganizationsPaginatedList
- name: Pagination
  property_count: 1
  slug: Pagination
- name: PartySummary
  property_count: 3
  slug: PartySummary
- name: Plate
  property_count: 17
  slug: Plate
- name: PlateCreate
  property_count: 8
  slug: PlateCreate
- name: PlateCreationTableNotePart
  property_count: 0
  slug: PlateCreationTableNotePart
- name: PlateSchema
  property_count: 0
  slug: PlateSchema
- name: PlateSchemasList
  property_count: 1
  slug: PlateSchemasList
- name: PlateSchemasPaginatedList
  property_count: 0
  slug: PlateSchemasPaginatedList
- name: PlateUpdate
  property_count: 4
  slug: PlateUpdate
- name: PlatesArchivalChange
  property_count: 2
  slug: PlatesArchivalChange
- name: PlatesArchive
  property_count: 3
  slug: PlatesArchive
- name: PlatesBulkGet
  property_count: 1
  slug: PlatesBulkGet
- name: PlatesPaginatedList
  property_count: 2
  slug: PlatesPaginatedList
- name: PlatesUnarchive
  property_count: 1
  slug: PlatesUnarchive
- name: Primer
  property_count: 9
  slug: Primer
- name: PrintLabels
  property_count: 3
  slug: PrintLabels
- name: Printer
  property_count: 6
  slug: Printer
- name: PrintersList
  property_count: 1
  slug: PrintersList
- name: Project
  property_count: 4
  slug: Project
- name: ProjectsArchivalChange
  property_count: 9
  slug: ProjectsArchivalChange
- name: ProjectsArchive
  property_count: 2
  slug: ProjectsArchive
- name: ProjectsPaginatedList
  property_count: 2
  slug: ProjectsPaginatedList
- name: ProjectsUnarchive
  property_count: 1
  slug: ProjectsUnarchive
- name: ReducedPattern
  property_count: 2
  slug: ReducedPattern
- name: RegisterEntities
  property_count: 2
  slug: RegisterEntities
- name: RegisteredEntitiesList
  property_count: 1
  slug: RegisteredEntitiesList
- name: RegistrationOrigin
  property_count: 2
  slug: RegistrationOrigin
- name: RegistrationTableNotePart
  property_count: 0
  slug: RegistrationTableNotePart
- name: RegistriesList
  property_count: 1
  slug: RegistriesList
- name: Registry
  property_count: 4
  slug: Registry
- name: RegistrySchema
  property_count: 0
  slug: RegistrySchema
- name: Request
  property_count: 0
  slug: Request
- name: RequestBase
  property_count: 0
  slug: RequestBase
- name: RequestCreate
  property_count: 0
  slug: RequestCreate
- name: RequestCreatedEvent
  property_count: 0
  slug: RequestCreatedEvent
- name: RequestFulfillment
  property_count: 7
  slug: RequestFulfillment
- name: RequestFulfillmentsPaginatedList
  property_count: 2
  slug: RequestFulfillmentsPaginatedList
- name: RequestResponse
  property_count: 2
  slug: RequestResponse
- name: RequestResponseSamplesItemBatch
  property_count: 0
  slug: RequestResponseSamplesItemBatch
- name: RequestResponseSamplesItemEntity
  property_count: 0
  slug: RequestResponseSamplesItemEntity
- name: RequestSampleGroup
  property_count: 2
  slug: RequestSampleGroup
- name: RequestSampleGroupCreate
  property_count: 1
  slug: RequestSampleGroupCreate
- name: RequestSampleGroupSamples
  property_count: 0
  slug: RequestSampleGroupSamples
- name: RequestSampleWithBatch
  property_count: 2
  slug: RequestSampleWithBatch
- name: RequestSampleWithEntity
  property_count: 2
  slug: RequestSampleWithEntity
- name: RequestSchema
  property_count: 0
  slug: RequestSchema
- name: RequestSchemasPaginatedList
  property_count: 2
  slug: RequestSchemasPaginatedList
- name: RequestStatus
  property_count: 0
  slug: RequestStatus
- name: RequestTask
  property_count: 1
  slug: RequestTask
- name: RequestTaskBase
  property_count: 1
  slug: RequestTaskBase
- name: RequestTaskBaseFields
  property_count: 2
  slug: RequestTaskBaseFields
- name: RequestTaskSchema
  property_count: 0
  slug: RequestTaskSchema
- name: RequestTaskSchemasPaginatedList
  property_count: 2
  slug: RequestTaskSchemasPaginatedList
- name: RequestTasksBulkCreate
  property_count: 1
  slug: RequestTasksBulkCreate
- name: RequestTasksBulkCreateRequest
  property_count: 1
  slug: RequestTasksBulkCreateRequest
- name: RequestTasksBulkCreateResponse
  property_count: 1
  slug: RequestTasksBulkCreateResponse
- name: RequestTasksBulkUpdateRequest
  property_count: 1
  slug: RequestTasksBulkUpdateRequest
- name: RequestTasksBulkUpdateResponse
  property_count: 1
  slug: RequestTasksBulkUpdateResponse
- name: RequestTeamAssignee
  property_count: 1
  slug: RequestTeamAssignee
- name: RequestUpdate
  property_count: 0
  slug: RequestUpdate
- name: RequestUpdatedFieldsEvent
  property_count: 0
  slug: RequestUpdatedFieldsEvent
- name: RequestUserAssignee
  property_count: 1
  slug: RequestUserAssignee
- name: RequestWriteBase
  property_count: 0
  slug: RequestWriteBase
- name: RequestWriteTeamAssignee
  property_count: 1
  slug: RequestWriteTeamAssignee
- name: RequestWriteUserAssignee
  property_count: 1
  slug: RequestWriteUserAssignee
- name: RequestsBulkGet
  property_count: 1
  slug: RequestsBulkGet
- name: RequestsPaginatedList
  property_count: 0
  slug: RequestsPaginatedList
- name: ResultsTableNotePart
  property_count: 0
  slug: ResultsTableNotePart
- name: ReviewChange
  property_count: 6
  slug: ReviewChange
- name: ReviewSnapshot
  property_count: 5
  slug: ReviewSnapshot
- name: RnaAnnotation
  property_count: 0
  slug: RnaAnnotation
- name: RnaOligo
  property_count: 0
  slug: RnaOligo
- name: RnaOligoBulkUpdate
  property_count: 0
  slug: RnaOligoBulkUpdate
- name: RnaOligoCreate
  property_count: 0
  slug: RnaOligoCreate
- name: RnaOligoUpdate
  property_count: 0
  slug: RnaOligoUpdate
- name: RnaOligoWithEntityType
  property_count: 0
  slug: RnaOligoWithEntityType
- name: RnaOligosArchivalChange
  property_count: 2
  slug: RnaOligosArchivalChange
- name: RnaOligosArchive
  property_count: 2
  slug: RnaOligosArchive
- name: RnaOligosBulkCreateRequest
  property_count: 1
  slug: RnaOligosBulkCreateRequest
- name: RnaOligosBulkUpdateRequest
  property_count: 1
  slug: RnaOligosBulkUpdateRequest
- name: RnaOligosBulkUpsertRequest
  property_count: 1
  slug: RnaOligosBulkUpsertRequest
- name: RnaOligosPaginatedList
  property_count: 0
  slug: RnaOligosPaginatedList
- name: RnaOligosUnarchive
  property_count: 1
  slug: RnaOligosUnarchive
- name: RnaSequence
  property_count: 29
  slug: RnaSequence
- name: RnaSequenceBaseRequest
  property_count: 0
  slug: RnaSequenceBaseRequest
- name: RnaSequenceBaseRequestForCreate
  property_count: 0
  slug: RnaSequenceBaseRequestForCreate
- name: RnaSequenceBulkCreate
  property_count: 0
  slug: RnaSequenceBulkCreate
- name: RnaSequenceBulkUpdate
  property_count: 0
  slug: RnaSequenceBulkUpdate
- name: RnaSequenceCreate
  property_count: 0
  slug: RnaSequenceCreate
- name: RnaSequencePart
  property_count: 0
  slug: RnaSequencePart
- name: RnaSequenceRequestRegistryFields
  property_count: 1
  slug: RnaSequenceRequestRegistryFields
- name: RnaSequenceUpdate
  property_count: 0
  slug: RnaSequenceUpdate
- name: RnaSequenceWithEntityType
  property_count: 0
  slug: RnaSequenceWithEntityType
- name: RnaSequencesArchivalChange
  property_count: 1
  slug: RnaSequencesArchivalChange
- name: RnaSequencesArchive
  property_count: 2
  slug: RnaSequencesArchive
- name: RnaSequencesBulkCreateRequest
  property_count: 1
  slug: RnaSequencesBulkCreateRequest
- name: RnaSequencesBulkGet
  property_count: 1
  slug: RnaSequencesBulkGet
- name: RnaSequencesBulkUpdateRequest
  property_count: 1
  slug: RnaSequencesBulkUpdateRequest
- name: RnaSequencesPaginatedList
  property_count: 2
  slug: RnaSequencesPaginatedList
- name: RnaSequencesUnarchive
  property_count: 1
  slug: RnaSequencesUnarchive
- name: SampleGroup
  property_count: 2
  slug: SampleGroup
- name: SampleGroupStatus
  property_count: 0
  slug: SampleGroupStatus
- name: SampleGroupStatusUpdate
  property_count: 2
  slug: SampleGroupStatusUpdate
- name: SampleGroupsStatusUpdate
  property_count: 1
  slug: SampleGroupsStatusUpdate
- name: SampleRestrictionStatus
  property_count: 0
  slug: SampleRestrictionStatus
- name: Schema
  property_count: 5
  slug: Schema
- name: SchemaDependencySubtypes
  property_count: 0
  slug: SchemaDependencySubtypes
- name: SchemaFieldsQueryParam
  property_count: 0
  slug: SchemaFieldsQueryParam
- name: SchemaLinkFieldDefinition
  property_count: 0
  slug: SchemaLinkFieldDefinition
- name: SchemaSummary
  property_count: 2
  slug: SchemaSummary
- name: SearchBasesRequest
  property_count: 7
  slug: SearchBasesRequest
- name: SearchInputMultiValueUiBlock
  property_count: 0
  slug: SearchInputMultiValueUiBlock
- name: SearchInputMultiValueUiBlockCreate
  property_count: 0
  slug: SearchInputMultiValueUiBlockCreate
- name: SearchInputMultiValueUiBlockUpdate
  property_count: 0
  slug: SearchInputMultiValueUiBlockUpdate
- name: SearchInputUiBlock
  property_count: 0
  slug: SearchInputUiBlock
- name: SearchInputUiBlockCreate
  property_count: 0
  slug: SearchInputUiBlockCreate
- name: SearchInputUiBlockItemType
  property_count: 0
  slug: SearchInputUiBlockItemType
- name: SearchInputUiBlockUpdate
  property_count: 0
  slug: SearchInputUiBlockUpdate
- name: SectionUiBlock
  property_count: 0
  slug: SectionUiBlock
- name: SectionUiBlockCreate
  property_count: 0
  slug: SectionUiBlockCreate
- name: SectionUiBlockUpdate
  property_count: 0
  slug: SectionUiBlockUpdate
- name: SecureTextAppConfigItem
  property_count: 0
  slug: SecureTextAppConfigItem
- name: SelectorInputMultiValueUiBlock
  property_count: 0
  slug: SelectorInputMultiValueUiBlock
- name: SelectorInputMultiValueUiBlockCreate
  property_count: 0
  slug: SelectorInputMultiValueUiBlockCreate
- name: SelectorInputMultiValueUiBlockUpdate
  property_count: 0
  slug: SelectorInputMultiValueUiBlockUpdate
- name: SelectorInputUiBlock
  property_count: 0
  slug: SelectorInputUiBlock
- name: SelectorInputUiBlockCreate
  property_count: 0
  slug: SelectorInputUiBlockCreate
- name: SelectorInputUiBlockUpdate
  property_count: 0
  slug: SelectorInputUiBlockUpdate
- name: SequenceFeatureBase
  property_count: 4
  slug: SequenceFeatureBase
- name: SequenceFeatureCustomField
  property_count: 2
  slug: SequenceFeatureCustomField
- name: SimpleFieldDefinition
  property_count: 0
  slug: SimpleFieldDefinition
- name: SimpleNotePart
  property_count: 0
  slug: SimpleNotePart
- name: StageEntry
  property_count: 16
  slug: StageEntry
- name: StageEntryCreatedEvent
  property_count: 0
  slug: StageEntryCreatedEvent
- name: StageEntryUpdatedAssignedReviewersEvent
  property_count: 0
  slug: StageEntryUpdatedAssignedReviewersEvent
- name: StageEntryUpdatedFieldsEvent
  property_count: 0
  slug: StageEntryUpdatedFieldsEvent
- name: StageEntryUpdatedReviewRecordEvent
  property_count: 0
  slug: StageEntryUpdatedReviewRecordEvent
- name: StructuredTableApiIdentifiers
  property_count: 3
  slug: StructuredTableApiIdentifiers
- name: StructuredTableColumnInfo
  property_count: 3
  slug: StructuredTableColumnInfo
- name: TableNotePart
  property_count: 0
  slug: TableNotePart
- name: TableUiBlock
  property_count: 0
  slug: TableUiBlock
- name: TableUiBlockCreate
  property_count: 0
  slug: TableUiBlockCreate
- name: TableUiBlockDataFrameSource
  property_count: 2
  slug: TableUiBlockDataFrameSource
- name: TableUiBlockDatasetSource
  property_count: 2
  slug: TableUiBlockDatasetSource
- name: TableUiBlockSource
  property_count: 0
  slug: TableUiBlockSource
- name: TableUiBlockUpdate
  property_count: 0
  slug: TableUiBlockUpdate
- name: Team
  property_count: 0
  slug: Team
- name: TeamCreate
  property_count: 3
  slug: TeamCreate
- name: TeamSummary
  property_count: 0
  slug: TeamSummary
- name: TeamUpdate
  property_count: 2
  slug: TeamUpdate
- name: TeamsPaginatedList
  property_count: 0
  slug: TeamsPaginatedList
- name: TextAppConfigItem
  property_count: 0
  slug: TextAppConfigItem
- name: TextBoxNotePart
  property_count: 0
  slug: TextBoxNotePart
- name: TextInputUiBlock
  property_count: 0
  slug: TextInputUiBlock
- name: TextInputUiBlockCreate
  property_count: 0
  slug: TextInputUiBlockCreate
- name: TextInputUiBlockUpdate
  property_count: 0
  slug: TextInputUiBlockUpdate
- name: TokenCreate
  property_count: 3
  slug: TokenCreate
- name: TokenResponse
  property_count: 3
  slug: TokenResponse
- name: TransfersAsyncTask
  property_count: 0
  slug: TransfersAsyncTask
- name: Translation
  property_count: 0
  slug: Translation
- name: UnitSummary
  property_count: 4
  slug: UnitSummary
- name: UnregisterEntities
  property_count: 2
  slug: UnregisterEntities
- name: UpdateEventMixin
  property_count: 1
  slug: UpdateEventMixin
- name: User
  property_count: 0
  slug: User
- name: UserActivity
  property_count: 2
  slug: UserActivity
- name: UserBulkCreateRequest
  property_count: 1
  slug: UserBulkCreateRequest
- name: UserBulkUpdate
  property_count: 0
  slug: UserBulkUpdate
- name: UserBulkUpdateRequest
  property_count: 1
  slug: UserBulkUpdateRequest
- name: UserCreate
  property_count: 3
  slug: UserCreate
- name: UserInputMultiValueUiBlock
  property_count: 0
  slug: UserInputMultiValueUiBlock
- name: UserInputUiBlock
  property_count: 0
  slug: UserInputUiBlock
- name: UserSummary
  property_count: 0
  slug: UserSummary
- name: UserUpdate
  property_count: 4
  slug: UserUpdate
- name: UserValidation
  property_count: 2
  slug: UserValidation
- name: UsersPaginatedList
  property_count: 0
  slug: UsersPaginatedList
- name: WarehouseCredentialSummary
  property_count: 6
  slug: WarehouseCredentialSummary
- name: WarehouseCredentials
  property_count: 3
  slug: WarehouseCredentials
- name: WarehouseCredentialsCreate
  property_count: 1
  slug: WarehouseCredentialsCreate
- name: Well
  property_count: 22
  slug: Well
- name: WellOrInaccessibleResource
  property_count: 0
  slug: WellOrInaccessibleResource
- name: WorkflowEndNodeDetails
  property_count: 3
  slug: WorkflowEndNodeDetails
- name: WorkflowFlowchart
  property_count: 7
  slug: WorkflowFlowchart
- name: WorkflowFlowchartConfigSummary
  property_count: 2
  slug: WorkflowFlowchartConfigSummary
- name: WorkflowFlowchartConfigVersion
  property_count: 4
  slug: WorkflowFlowchartConfigVersion
- name: WorkflowFlowchartEdgeConfig
  property_count: 3
  slug: WorkflowFlowchartEdgeConfig
- name: WorkflowFlowchartNodeConfig
  property_count: 3
  slug: WorkflowFlowchartNodeConfig
- name: WorkflowFlowchartPaginatedList
  property_count: 2
  slug: WorkflowFlowchartPaginatedList
- name: WorkflowList
  property_count: 1
  slug: WorkflowList
- name: WorkflowNodeTaskGroupSummary
  property_count: 0
  slug: WorkflowNodeTaskGroupSummary
- name: WorkflowOutput
  property_count: 0
  slug: WorkflowOutput
- name: WorkflowOutputArchiveReason
  property_count: 0
  slug: WorkflowOutputArchiveReason
- name: WorkflowOutputBulkCreate
  property_count: 0
  slug: WorkflowOutputBulkCreate
- name: WorkflowOutputBulkUpdate
  property_count: 0
  slug: WorkflowOutputBulkUpdate
- name: WorkflowOutputCreate
  property_count: 0
  slug: WorkflowOutputCreate
- name: WorkflowOutputCreatedEvent
  property_count: 0
  slug: WorkflowOutputCreatedEvent
- name: WorkflowOutputNodeDetails
  property_count: 3
  slug: WorkflowOutputNodeDetails
- name: WorkflowOutputSchema
  property_count: 0
  slug: WorkflowOutputSchema
- name: WorkflowOutputSummary
  property_count: 2
  slug: WorkflowOutputSummary
- name: WorkflowOutputUpdate
  property_count: 0
  slug: WorkflowOutputUpdate
- name: WorkflowOutputUpdatedFieldsEvent
  property_count: 0
  slug: WorkflowOutputUpdatedFieldsEvent
- name: WorkflowOutputWriteBase
  property_count: 1
  slug: WorkflowOutputWriteBase
- name: WorkflowOutputsArchivalChange
  property_count: 1
  slug: WorkflowOutputsArchivalChange
- name: WorkflowOutputsArchive
  property_count: 2
  slug: WorkflowOutputsArchive
- name: WorkflowOutputsBulkCreateRequest
  property_count: 1
  slug: WorkflowOutputsBulkCreateRequest
- name: WorkflowOutputsBulkUpdateRequest
  property_count: 1
  slug: WorkflowOutputsBulkUpdateRequest
- name: WorkflowOutputsPaginatedList
  property_count: 2
  slug: WorkflowOutputsPaginatedList
- name: WorkflowOutputsUnarchive
  property_count: 1
  slug: WorkflowOutputsUnarchive
- name: WorkflowPatch
  property_count: 3
  slug: WorkflowPatch
- name: WorkflowRootNodeDetails
  property_count: 3
  slug: WorkflowRootNodeDetails
- name: WorkflowRouterFunction
  property_count: 4
  slug: WorkflowRouterFunction
- name: WorkflowRouterNodeDetails
  property_count: 4
  slug: WorkflowRouterNodeDetails
- name: WorkflowSample
  property_count: 5
  slug: WorkflowSample
- name: WorkflowSampleList
  property_count: 1
  slug: WorkflowSampleList
- name: WorkflowStage
  property_count: 3
  slug: WorkflowStage
- name: WorkflowStageList
  property_count: 1
  slug: WorkflowStageList
- name: WorkflowStageRun
  property_count: 4
  slug: WorkflowStageRun
- name: WorkflowStageRunList
  property_count: 1
  slug: WorkflowStageRunList
- name: WorkflowTask
  property_count: 0
  slug: WorkflowTask
- name: WorkflowTaskArchiveReason
  property_count: 0
  slug: WorkflowTaskArchiveReason
- name: WorkflowTaskBase
  property_count: 0
  slug: WorkflowTaskBase
- name: WorkflowTaskBulkCreate
  property_count: 0
  slug: WorkflowTaskBulkCreate
- name: WorkflowTaskBulkUpdate
  property_count: 0
  slug: WorkflowTaskBulkUpdate
- name: WorkflowTaskCreate
  property_count: 0
  slug: WorkflowTaskCreate
- name: WorkflowTaskCreatedEvent
  property_count: 0
  slug: WorkflowTaskCreatedEvent
- name: WorkflowTaskExecutionOrigin
  property_count: 3
  slug: WorkflowTaskExecutionOrigin
- name: WorkflowTaskGroup
  property_count: 0
  slug: WorkflowTaskGroup
- name: WorkflowTaskGroupArchiveReason
  property_count: 0
  slug: WorkflowTaskGroupArchiveReason
- name: WorkflowTaskGroupBase
  property_count: 0
  slug: WorkflowTaskGroupBase
- name: WorkflowTaskGroupCreate
  property_count: 0
  slug: WorkflowTaskGroupCreate
- name: WorkflowTaskGroupCreatedEvent
  property_count: 0
  slug: WorkflowTaskGroupCreatedEvent
- name: WorkflowTaskGroupMappingCompletedEvent
  property_count: 0
  slug: WorkflowTaskGroupMappingCompletedEvent
- name: WorkflowTaskGroupSummary
  property_count: 3
  slug: WorkflowTaskGroupSummary
- name: WorkflowTaskGroupUpdate
  property_count: 0
  slug: WorkflowTaskGroupUpdate
- name: WorkflowTaskGroupUpdatedWatchersEvent
  property_count: 0
  slug: WorkflowTaskGroupUpdatedWatchersEvent
- name: WorkflowTaskGroupWriteBase
  property_count: 3
  slug: WorkflowTaskGroupWriteBase
- name: WorkflowTaskGroupsArchivalChange
  property_count: 1
  slug: WorkflowTaskGroupsArchivalChange
- name: WorkflowTaskGroupsArchive
  property_count: 2
  slug: WorkflowTaskGroupsArchive
- name: WorkflowTaskGroupsPaginatedList
  property_count: 2
  slug: WorkflowTaskGroupsPaginatedList
- name: WorkflowTaskGroupsUnarchive
  property_count: 1
  slug: WorkflowTaskGroupsUnarchive
- name: WorkflowTaskNodeDetails
  property_count: 3
  slug: WorkflowTaskNodeDetails
- name: WorkflowTaskSchema
  property_count: 0
  slug: WorkflowTaskSchema
- name: WorkflowTaskSchemaBase
  property_count: 0
  slug: WorkflowTaskSchemaBase
- name: WorkflowTaskSchemaSummary
  property_count: 2
  slug: WorkflowTaskSchemaSummary
- name: WorkflowTaskSchemasPaginatedList
  property_count: 2
  slug: WorkflowTaskSchemasPaginatedList
- name: WorkflowTaskStatus
  property_count: 3
  slug: WorkflowTaskStatus
- name: WorkflowTaskStatusLifecycle
  property_count: 5
  slug: WorkflowTaskStatusLifecycle
- name: WorkflowTaskStatusLifecycleTransition
  property_count: 2
  slug: WorkflowTaskStatusLifecycleTransition
- name: WorkflowTaskSummary
  property_count: 2
  slug: WorkflowTaskSummary
- name: WorkflowTaskUpdate
  property_count: 0
  slug: WorkflowTaskUpdate
- name: WorkflowTaskUpdatedAssigneeEvent
  property_count: 0
  slug: WorkflowTaskUpdatedAssigneeEvent
- name: WorkflowTaskUpdatedFieldsEvent
  property_count: 0
  slug: WorkflowTaskUpdatedFieldsEvent
- name: WorkflowTaskUpdatedScheduledOnEvent
  property_count: 0
  slug: WorkflowTaskUpdatedScheduledOnEvent
- name: WorkflowTaskUpdatedStatusEvent
  property_count: 0
  slug: WorkflowTaskUpdatedStatusEvent
- name: WorkflowTaskWriteBase
  property_count: 3
  slug: WorkflowTaskWriteBase
- name: WorkflowTasksArchivalChange
  property_count: 1
  slug: WorkflowTasksArchivalChange
- name: WorkflowTasksArchive
  property_count: 2
  slug: WorkflowTasksArchive
- name: WorkflowTasksBulkCopyRequest
  property_count: 1
  slug: WorkflowTasksBulkCopyRequest
- name: WorkflowTasksBulkCreateRequest
  property_count: 1
  slug: WorkflowTasksBulkCreateRequest
- name: WorkflowTasksBulkUpdateRequest
  property_count: 1
  slug: WorkflowTasksBulkUpdateRequest
- name: WorkflowTasksPaginatedList
  property_count: 2
  slug: WorkflowTasksPaginatedList
- name: WorkflowTasksUnarchive
  property_count: 1
  slug: WorkflowTasksUnarchive
- name: WorksheetReviewChanges
  property_count: 9
  slug: WorksheetReviewChanges
- name: WorksheetUpdatedReviewSnapshotBetaEvent
  property_count: 0
  slug: WorksheetUpdatedReviewSnapshotBetaEvent
layout: provider
modified: 2026-06-13
name: Benchling
nav: Providers
network: true
overview: 'Benchling publishes 57 APIs on the [APIs.io](https://apis.io/) network, including AA Sequences API, Apps API, Assay Results API, and 54 more. Tagged areas include Life Sciences, Biotech, R&D, Molecular Biology, and Laboratory Information Management.


  The Benchling catalog on APIs.io includes 1 Spectral governance ruleset.


  Benchling''s developer surface includes authentication, documentation, changelog, engineering blog, status page, and 17 more developer resources.'
plans:
- name: Benchling Plans Pricing
  plan_count: 3
  slug: benchling-plans-pricing
random_paper: 69
rate_limits:
- limit_count: 0
  name: Benchling Rate Limits
  slug: benchling-rate-limits
rules:
- name: Benchling API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: benchling-jsonschema-spectral-rules
scopes:
- name: Benchling Scopes
  scope_count: 0
  slug: benchling-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 44.9
  delta: -5.6
  facets:
    commercial_clarity: 39.5
    contract_quality: 55.9
    developer_ergonomics: 34.8
    discoverability: 68.5
    governance: 58.3
    operational_transparency: 28.9
  previous_composite: 50.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 57
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 36.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/benchling/refs/heads/main/screenshots/benchling-2026-06-20T173135.png
security:
- kind: authentication
  name: Benchling Authentication
  slug: benchling-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Benchling Domain Security
  slug: benchling-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: benchling
tags:
- Life Sciences
- Biotech
- R&D
- Molecular Biology
- Laboratory Information Management
- Electronic Lab Notebook
- Assay Management
- Inventory Management
- Sequence Management
- Experiment Workflows
- REST
- Webhooks
---

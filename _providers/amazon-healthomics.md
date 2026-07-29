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
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: verified
    idempotency: verified
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 45.9
  scored_at: '2026-07-28'
agentic_access:
- acting_count: 49
  human_in_the_loop: 0
  name: Amazon Healthomics Agentic Access
  operation_count: 72
  slug: amazon-healthomics-agentic-access
  summary_line: 72 operations · 49 acting
api_count: 13
apis:
- description: The AnnotationStore API from Amazon HealthOmics — 2 operation(s) for annotationstore.
  name: Amazon HealthOmics AnnotationStore API
  slug: amazon-healthomics-annotationstore-api
- description: The AnnotationStores API from Amazon HealthOmics — 1 operation(s) for annotationstores.
  name: Amazon HealthOmics AnnotationStores API
  slug: amazon-healthomics-annotationstores-api
- description: The Import API from Amazon HealthOmics — 6 operation(s) for import.
  name: Amazon HealthOmics Import API
  slug: amazon-healthomics-import-api
- description: The Referencestore API from Amazon HealthOmics — 9 operation(s) for referencestore.
  name: Amazon HealthOmics Referencestore API
  slug: amazon-healthomics-referencestore-api
- description: The Referencestores API from Amazon HealthOmics — 1 operation(s) for referencestores.
  name: Amazon HealthOmics Referencestores API
  slug: amazon-healthomics-referencestores-api
- description: The Run API from Amazon HealthOmics — 5 operation(s) for run.
  name: Amazon HealthOmics Run API
  slug: amazon-healthomics-run-api
- description: The RunGroup API from Amazon HealthOmics — 2 operation(s) for rungroup.
  name: Amazon HealthOmics RunGroup API
  slug: amazon-healthomics-rungroup-api
- description: The Sequencestore API from Amazon HealthOmics — 21 operation(s) for sequencestore.
  name: Amazon HealthOmics Sequencestore API
  slug: amazon-healthomics-sequencestore-api
- description: The Sequencestores API from Amazon HealthOmics — 1 operation(s) for sequencestores.
  name: Amazon HealthOmics Sequencestores API
  slug: amazon-healthomics-sequencestores-api
- description: The Tags API from Amazon HealthOmics — 2 operation(s) for tags.
  name: Amazon HealthOmics Tags API
  slug: amazon-healthomics-tags-api
- description: The VariantStore API from Amazon HealthOmics — 2 operation(s) for variantstore.
  name: Amazon HealthOmics VariantStore API
  slug: amazon-healthomics-variantstore-api
- description: The VariantStores API from Amazon HealthOmics — 1 operation(s) for variantstores.
  name: Amazon HealthOmics VariantStores API
  slug: amazon-healthomics-variantstores-api
- description: The Workflow API from Amazon HealthOmics — 2 operation(s) for workflow.
  name: Amazon HealthOmics Workflow API
  slug: amazon-healthomics-workflow-api
arazzos:
- description: Start a read set activation job in a sequence store and poll it to completion.
  name: Amazon HealthOmics Activate an Archived Read Set
  slug: amazon-healthomics-activate-read-set-workflow
- description: Start a read set export job to Amazon S3 and poll it to completion.
  name: Amazon HealthOmics Export a Read Set to S3
  slug: amazon-healthomics-export-read-set-workflow
- description: Create an annotation store, start an annotation import job, and poll it to completion.
  name: Amazon HealthOmics Import Annotations
  slug: amazon-healthomics-import-annotations-workflow
- description: Provision a sequence store, start a read set import job, and poll it to completion.
  name: Amazon HealthOmics Import Read Set
  slug: amazon-healthomics-import-read-set-workflow
- description: Provision a reference store, start a reference import job, and poll it to completion.
  name: Amazon HealthOmics Import Reference Genome
  slug: amazon-healthomics-import-reference-workflow
- description: Create a variant store, start a variant import job, and poll it to completion.
  name: Amazon HealthOmics Import Variants
  slug: amazon-healthomics-import-variants-workflow
- description: Confirm a run exists, list its tasks, and fetch detail for the first task.
  name: Amazon HealthOmics Inspect a Run Task
  slug: amazon-healthomics-inspect-run-task-workflow
- description: Stand up a reference store with an imported reference, then a sequence store ready for read sets.
  name: Amazon HealthOmics Provision Genomics Stores
  slug: amazon-healthomics-provision-genomics-stores-workflow
- description: Register a private workflow, start a run, poll it to completion, and list its tasks.
  name: Amazon HealthOmics Run a Private Workflow
  slug: amazon-healthomics-run-private-workflow
- description: Create a run group, start a run inside it, and poll the run to completion.
  name: Amazon HealthOmics Run a Workflow in a Run Group
  slug: amazon-healthomics-run-workflow-in-group-workflow
artifact_total: 1176
collections:
- collection_type: postman
  name: Amazon Omics AnnotationStore API
  slug: postman-amazon-healthomics-annotationstore-api
- collection_type: postman
  name: Amazon Omics AnnotationStore AnnotationStores API
  slug: postman-amazon-healthomics-annotationstores-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Import API
  slug: postman-amazon-healthomics-import-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Referencestore API
  slug: postman-amazon-healthomics-referencestore-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Referencestores API
  slug: postman-amazon-healthomics-referencestores-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Run API
  slug: postman-amazon-healthomics-run-api
- collection_type: postman
  name: Amazon Omics AnnotationStore RunGroup API
  slug: postman-amazon-healthomics-rungroup-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Sequencestore API
  slug: postman-amazon-healthomics-sequencestore-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Sequencestores API
  slug: postman-amazon-healthomics-sequencestores-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Tags API
  slug: postman-amazon-healthomics-tags-api
- collection_type: postman
  name: Amazon Omics AnnotationStore VariantStore API
  slug: postman-amazon-healthomics-variantstore-api
- collection_type: postman
  name: Amazon Omics AnnotationStore VariantStores API
  slug: postman-amazon-healthomics-variantstores-api
- collection_type: postman
  name: Amazon Omics AnnotationStore Workflow API
  slug: postman-amazon-healthomics-workflow-api
- collection_type: postman
  name: Amazon Omics
  slug: postman-amazon-healthomics
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-healthomics-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-healthomics-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-healthomics-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-healthomics-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-healthomics-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-healthomics/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-activate-read-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-export-read-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-import-annotations-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-import-read-set-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-import-reference-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-import-variants-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-inspect-run-task-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-provision-genomics-stores-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-run-private-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-healthomics-run-workflow-in-group-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/healthomics/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/omics/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://aws.amazon.com/service-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://aws.amazon.com/privacy/
- group: operate
  title: ''
  type: Support
  url: https://aws.amazon.com/premiumsupport/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/industries/healthcare/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/omics/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: build
  title: ''
  type: SDKs
  url: https://aws.amazon.com/developer/tools/
- group: build
  title: ''
  type: CLI
  url: https://awscli.amazonaws.com/v2/documentation/api/latest/reference/omics/index.html
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-healthomics-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-healthomics-vocabulary.yaml
created: '2026-03-16'
description: AWS HealthOmics is a purpose-built service for healthcare and life sciences organizations that helps store, query, and analyze genomic, transcriptomic, and other omics data to generate insights and accelerate scientific discoveries and improve healthcare.
examples:
- key_count: 0
  name: Healthomics Abort Multipart Read Set Upload Request Example
  slug: healthomics-abort-multipart-read-set-upload-request-example
- key_count: 0
  name: Healthomics Abort Multipart Read Set Upload Response Example
  slug: healthomics-abort-multipart-read-set-upload-response-example
- key_count: 3
  name: Healthomics Activate Read Set Filter Example
  slug: healthomics-activate-read-set-filter-example
- key_count: 5
  name: Healthomics Activate Read Set Job Item Example
  slug: healthomics-activate-read-set-job-item-example
- key_count: 3
  name: Healthomics Activate Read Set Source Item Example
  slug: healthomics-activate-read-set-source-item-example
- key_count: 2
  name: Healthomics Annotation Import Item Detail Example
  slug: healthomics-annotation-import-item-detail-example
- key_count: 1
  name: Healthomics Annotation Import Item Source Example
  slug: healthomics-annotation-import-item-source-example
- key_count: 5
  name: Healthomics Annotation Import Job Item Example
  slug: healthomics-annotation-import-job-item-example
- key_count: 5
  name: Healthomics Annotation Store Item Example
  slug: healthomics-annotation-store-item-example
- key_count: 1
  name: Healthomics Batch Delete Read Set Request Example
  slug: healthomics-batch-delete-read-set-request-example
- key_count: 1
  name: Healthomics Batch Delete Read Set Response Example
  slug: healthomics-batch-delete-read-set-response-example
- key_count: 0
  name: Healthomics Cancel Annotation Import Request Example
  slug: healthomics-cancel-annotation-import-request-example
- key_count: 0
  name: Healthomics Cancel Annotation Import Response Example
  slug: healthomics-cancel-annotation-import-response-example
- key_count: 0
  name: Healthomics Cancel Run Request Example
  slug: healthomics-cancel-run-request-example
- key_count: 0
  name: Healthomics Cancel Variant Import Request Example
  slug: healthomics-cancel-variant-import-request-example
- key_count: 0
  name: Healthomics Cancel Variant Import Response Example
  slug: healthomics-cancel-variant-import-response-example
- key_count: 1
  name: Healthomics Complete Multipart Read Set Upload Request Example
  slug: healthomics-complete-multipart-read-set-upload-request-example
- key_count: 1
  name: Healthomics Complete Multipart Read Set Upload Response Example
  slug: healthomics-complete-multipart-read-set-upload-response-example
- key_count: 3
  name: Healthomics Complete Read Set Upload Part List Item Example
  slug: healthomics-complete-read-set-upload-part-list-item-example
- key_count: 5
  name: Healthomics Create Annotation Store Request Example
  slug: healthomics-create-annotation-store-request-example
- key_count: 5
  name: Healthomics Create Annotation Store Response Example
  slug: healthomics-create-annotation-store-response-example
- key_count: 5
  name: Healthomics Create Multipart Read Set Upload Request Example
  slug: healthomics-create-multipart-read-set-upload-request-example
- key_count: 5
  name: Healthomics Create Multipart Read Set Upload Response Example
  slug: healthomics-create-multipart-read-set-upload-response-example
- key_count: 5
  name: Healthomics Create Reference Store Request Example
  slug: healthomics-create-reference-store-request-example
- key_count: 5
  name: Healthomics Create Reference Store Response Example
  slug: healthomics-create-reference-store-response-example
- key_count: 5
  name: Healthomics Create Run Group Request Example
  slug: healthomics-create-run-group-request-example
- key_count: 3
  name: Healthomics Create Run Group Response Example
  slug: healthomics-create-run-group-response-example
- key_count: 5
  name: Healthomics Create Sequence Store Request Example
  slug: healthomics-create-sequence-store-request-example
- key_count: 5
  name: Healthomics Create Sequence Store Response Example
  slug: healthomics-create-sequence-store-response-example
- key_count: 5
  name: Healthomics Create Variant Store Request Example
  slug: healthomics-create-variant-store-request-example
- key_count: 5
  name: Healthomics Create Variant Store Response Example
  slug: healthomics-create-variant-store-response-example
- key_count: 5
  name: Healthomics Create Workflow Request Example
  slug: healthomics-create-workflow-request-example
- key_count: 4
  name: Healthomics Create Workflow Response Example
  slug: healthomics-create-workflow-response-example
- key_count: 0
  name: Healthomics Delete Annotation Store Request Example
  slug: healthomics-delete-annotation-store-request-example
- key_count: 1
  name: Healthomics Delete Annotation Store Response Example
  slug: healthomics-delete-annotation-store-response-example
- key_count: 0
  name: Healthomics Delete Reference Request Example
  slug: healthomics-delete-reference-request-example
- key_count: 0
  name: Healthomics Delete Reference Response Example
  slug: healthomics-delete-reference-response-example
- key_count: 0
  name: Healthomics Delete Reference Store Request Example
  slug: healthomics-delete-reference-store-request-example
- key_count: 0
  name: Healthomics Delete Reference Store Response Example
  slug: healthomics-delete-reference-store-response-example
- key_count: 0
  name: Healthomics Delete Run Group Request Example
  slug: healthomics-delete-run-group-request-example
- key_count: 0
  name: Healthomics Delete Run Request Example
  slug: healthomics-delete-run-request-example
- key_count: 0
  name: Healthomics Delete Sequence Store Request Example
  slug: healthomics-delete-sequence-store-request-example
- key_count: 0
  name: Healthomics Delete Sequence Store Response Example
  slug: healthomics-delete-sequence-store-response-example
- key_count: 0
  name: Healthomics Delete Variant Store Request Example
  slug: healthomics-delete-variant-store-request-example
- key_count: 1
  name: Healthomics Delete Variant Store Response Example
  slug: healthomics-delete-variant-store-response-example
- key_count: 0
  name: Healthomics Delete Workflow Request Example
  slug: healthomics-delete-workflow-request-example
- key_count: 3
  name: Healthomics Export Read Set Detail Example
  slug: healthomics-export-read-set-detail-example
- key_count: 1
  name: Healthomics Export Read Set Example
  slug: healthomics-export-read-set-example
- key_count: 3
  name: Healthomics Export Read Set Filter Example
  slug: healthomics-export-read-set-filter-example
- key_count: 5
  name: Healthomics Export Read Set Job Detail Example
  slug: healthomics-export-read-set-job-detail-example
- key_count: 3
  name: Healthomics File Information Example
  slug: healthomics-file-information-example
- key_count: 2
  name: Healthomics Format Options Example
  slug: healthomics-format-options-example
- key_count: 0
  name: Healthomics Get Annotation Import Request Example
  slug: healthomics-get-annotation-import-request-example
- key_count: 5
  name: Healthomics Get Annotation Import Response Example
  slug: healthomics-get-annotation-import-response-example
- key_count: 0
  name: Healthomics Get Annotation Store Request Example
  slug: healthomics-get-annotation-store-request-example
- key_count: 5
  name: Healthomics Get Annotation Store Response Example
  slug: healthomics-get-annotation-store-response-example
- key_count: 0
  name: Healthomics Get Read Set Activation Job Request Example
  slug: healthomics-get-read-set-activation-job-request-example
- key_count: 5
  name: Healthomics Get Read Set Activation Job Response Example
  slug: healthomics-get-read-set-activation-job-response-example
- key_count: 0
  name: Healthomics Get Read Set Export Job Request Example
  slug: healthomics-get-read-set-export-job-request-example
- key_count: 5
  name: Healthomics Get Read Set Export Job Response Example
  slug: healthomics-get-read-set-export-job-response-example
- key_count: 0
  name: Healthomics Get Read Set Import Job Request Example
  slug: healthomics-get-read-set-import-job-request-example
- key_count: 5
  name: Healthomics Get Read Set Import Job Response Example
  slug: healthomics-get-read-set-import-job-response-example
- key_count: 0
  name: Healthomics Get Read Set Metadata Request Example
  slug: healthomics-get-read-set-metadata-request-example
- key_count: 5
  name: Healthomics Get Read Set Metadata Response Example
  slug: healthomics-get-read-set-metadata-response-example
- key_count: 0
  name: Healthomics Get Read Set Request Example
  slug: healthomics-get-read-set-request-example
- key_count: 1
  name: Healthomics Get Read Set Response Example
  slug: healthomics-get-read-set-response-example
- key_count: 0
  name: Healthomics Get Reference Import Job Request Example
  slug: healthomics-get-reference-import-job-request-example
- key_count: 5
  name: Healthomics Get Reference Import Job Response Example
  slug: healthomics-get-reference-import-job-response-example
- key_count: 0
  name: Healthomics Get Reference Metadata Request Example
  slug: healthomics-get-reference-metadata-request-example
- key_count: 5
  name: Healthomics Get Reference Metadata Response Example
  slug: healthomics-get-reference-metadata-response-example
- key_count: 0
  name: Healthomics Get Reference Request Example
  slug: healthomics-get-reference-request-example
- key_count: 1
  name: Healthomics Get Reference Response Example
  slug: healthomics-get-reference-response-example
- key_count: 0
  name: Healthomics Get Reference Store Request Example
  slug: healthomics-get-reference-store-request-example
- key_count: 5
  name: Healthomics Get Reference Store Response Example
  slug: healthomics-get-reference-store-response-example
- key_count: 0
  name: Healthomics Get Run Group Request Example
  slug: healthomics-get-run-group-request-example
- key_count: 5
  name: Healthomics Get Run Group Response Example
  slug: healthomics-get-run-group-response-example
- key_count: 0
  name: Healthomics Get Run Request Example
  slug: healthomics-get-run-request-example
- key_count: 5
  name: Healthomics Get Run Response Example
  slug: healthomics-get-run-response-example
- key_count: 0
  name: Healthomics Get Run Task Request Example
  slug: healthomics-get-run-task-request-example
- key_count: 5
  name: Healthomics Get Run Task Response Example
  slug: healthomics-get-run-task-response-example
- key_count: 0
  name: Healthomics Get Sequence Store Request Example
  slug: healthomics-get-sequence-store-request-example
- key_count: 5
  name: Healthomics Get Sequence Store Response Example
  slug: healthomics-get-sequence-store-response-example
- key_count: 0
  name: Healthomics Get Variant Import Request Example
  slug: healthomics-get-variant-import-request-example
- key_count: 5
  name: Healthomics Get Variant Import Response Example
  slug: healthomics-get-variant-import-response-example
- key_count: 0
  name: Healthomics Get Variant Store Request Example
  slug: healthomics-get-variant-store-request-example
- key_count: 5
  name: Healthomics Get Variant Store Response Example
  slug: healthomics-get-variant-store-response-example
- key_count: 0
  name: Healthomics Get Workflow Request Example
  slug: healthomics-get-workflow-request-example
- key_count: 5
  name: Healthomics Get Workflow Response Example
  slug: healthomics-get-workflow-response-example
- key_count: 3
  name: Healthomics Import Read Set Filter Example
  slug: healthomics-import-read-set-filter-example
- key_count: 5
  name: Healthomics Import Read Set Job Item Example
  slug: healthomics-import-read-set-job-item-example
- key_count: 5
  name: Healthomics Import Read Set Source Item Example
  slug: healthomics-import-read-set-source-item-example
- key_count: 3
  name: Healthomics Import Reference Filter Example
  slug: healthomics-import-reference-filter-example
- key_count: 5
  name: Healthomics Import Reference Job Item Example
  slug: healthomics-import-reference-job-item-example
- key_count: 5
  name: Healthomics Import Reference Source Item Example
  slug: healthomics-import-reference-source-item-example
- key_count: 2
  name: Healthomics List Annotation Import Jobs Filter Example
  slug: healthomics-list-annotation-import-jobs-filter-example
- key_count: 2
  name: Healthomics List Annotation Import Jobs Request Example
  slug: healthomics-list-annotation-import-jobs-request-example
- key_count: 2
  name: Healthomics List Annotation Import Jobs Response Example
  slug: healthomics-list-annotation-import-jobs-response-example
- key_count: 1
  name: Healthomics List Annotation Stores Filter Example
  slug: healthomics-list-annotation-stores-filter-example
- key_count: 2
  name: Healthomics List Annotation Stores Request Example
  slug: healthomics-list-annotation-stores-request-example
- key_count: 2
  name: Healthomics List Annotation Stores Response Example
  slug: healthomics-list-annotation-stores-response-example
- key_count: 0
  name: Healthomics List Multipart Read Set Uploads Request Example
  slug: healthomics-list-multipart-read-set-uploads-request-example
- key_count: 2
  name: Healthomics List Multipart Read Set Uploads Response Example
  slug: healthomics-list-multipart-read-set-uploads-response-example
- key_count: 1
  name: Healthomics List Read Set Activation Jobs Request Example
  slug: healthomics-list-read-set-activation-jobs-request-example
- key_count: 2
  name: Healthomics List Read Set Activation Jobs Response Example
  slug: healthomics-list-read-set-activation-jobs-response-example
- key_count: 1
  name: Healthomics List Read Set Export Jobs Request Example
  slug: healthomics-list-read-set-export-jobs-request-example
- key_count: 2
  name: Healthomics List Read Set Export Jobs Response Example
  slug: healthomics-list-read-set-export-jobs-response-example
- key_count: 1
  name: Healthomics List Read Set Import Jobs Request Example
  slug: healthomics-list-read-set-import-jobs-request-example
- key_count: 2
  name: Healthomics List Read Set Import Jobs Response Example
  slug: healthomics-list-read-set-import-jobs-response-example
- key_count: 2
  name: Healthomics List Read Set Upload Parts Request Example
  slug: healthomics-list-read-set-upload-parts-request-example
- key_count: 2
  name: Healthomics List Read Set Upload Parts Response Example
  slug: healthomics-list-read-set-upload-parts-response-example
- key_count: 1
  name: Healthomics List Read Sets Request Example
  slug: healthomics-list-read-sets-request-example
- key_count: 2
  name: Healthomics List Read Sets Response Example
  slug: healthomics-list-read-sets-response-example
- key_count: 1
  name: Healthomics List Reference Import Jobs Request Example
  slug: healthomics-list-reference-import-jobs-request-example
- key_count: 2
  name: Healthomics List Reference Import Jobs Response Example
  slug: healthomics-list-reference-import-jobs-response-example
- key_count: 1
  name: Healthomics List Reference Stores Request Example
  slug: healthomics-list-reference-stores-request-example
- key_count: 2
  name: Healthomics List Reference Stores Response Example
  slug: healthomics-list-reference-stores-response-example
- key_count: 1
  name: Healthomics List References Request Example
  slug: healthomics-list-references-request-example
- key_count: 2
  name: Healthomics List References Response Example
  slug: healthomics-list-references-response-example
- key_count: 0
  name: Healthomics List Run Groups Request Example
  slug: healthomics-list-run-groups-request-example
- key_count: 2
  name: Healthomics List Run Groups Response Example
  slug: healthomics-list-run-groups-response-example
- key_count: 0
  name: Healthomics List Run Tasks Request Example
  slug: healthomics-list-run-tasks-request-example
- key_count: 2
  name: Healthomics List Run Tasks Response Example
  slug: healthomics-list-run-tasks-response-example
- key_count: 0
  name: Healthomics List Runs Request Example
  slug: healthomics-list-runs-request-example
- key_count: 2
  name: Healthomics List Runs Response Example
  slug: healthomics-list-runs-response-example
- key_count: 1
  name: Healthomics List Sequence Stores Request Example
  slug: healthomics-list-sequence-stores-request-example
- key_count: 2
  name: Healthomics List Sequence Stores Response Example
  slug: healthomics-list-sequence-stores-response-example
- key_count: 0
  name: Healthomics List Tags For Resource Request Example
  slug: healthomics-list-tags-for-resource-request-example
- key_count: 1
  name: Healthomics List Tags For Resource Response Example
  slug: healthomics-list-tags-for-resource-response-example
- key_count: 2
  name: Healthomics List Variant Import Jobs Filter Example
  slug: healthomics-list-variant-import-jobs-filter-example
- key_count: 2
  name: Healthomics List Variant Import Jobs Request Example
  slug: healthomics-list-variant-import-jobs-request-example
- key_count: 2
  name: Healthomics List Variant Import Jobs Response Example
  slug: healthomics-list-variant-import-jobs-response-example
- key_count: 1
  name: Healthomics List Variant Stores Filter Example
  slug: healthomics-list-variant-stores-filter-example
- key_count: 2
  name: Healthomics List Variant Stores Request Example
  slug: healthomics-list-variant-stores-request-example
- key_count: 2
  name: Healthomics List Variant Stores Response Example
  slug: healthomics-list-variant-stores-response-example
- key_count: 0
  name: Healthomics List Workflows Request Example
  slug: healthomics-list-workflows-request-example
- key_count: 2
  name: Healthomics List Workflows Response Example
  slug: healthomics-list-workflows-response-example
- key_count: 5
  name: Healthomics Multipart Read Set Upload List Item Example
  slug: healthomics-multipart-read-set-upload-list-item-example
- key_count: 5
  name: Healthomics Read Options Example
  slug: healthomics-read-options-example
- key_count: 3
  name: Healthomics Read Set Batch Error Example
  slug: healthomics-read-set-batch-error-example
- key_count: 3
  name: Healthomics Read Set Files Example
  slug: healthomics-read-set-files-example
- key_count: 5
  name: Healthomics Read Set Filter Example
  slug: healthomics-read-set-filter-example
- key_count: 5
  name: Healthomics Read Set List Item Example
  slug: healthomics-read-set-list-item-example
- key_count: 2
  name: Healthomics Read Set Upload Part List Filter Example
  slug: healthomics-read-set-upload-part-list-filter-example
- key_count: 5
  name: Healthomics Read Set Upload Part List Item Example
  slug: healthomics-read-set-upload-part-list-item-example
- key_count: 2
  name: Healthomics Reference Files Example
  slug: healthomics-reference-files-example
- key_count: 4
  name: Healthomics Reference Filter Example
  slug: healthomics-reference-filter-example
- key_count: 1
  name: Healthomics Reference Item Example
  slug: healthomics-reference-item-example
- key_count: 5
  name: Healthomics Reference List Item Example
  slug: healthomics-reference-list-item-example
- key_count: 5
  name: Healthomics Reference Store Detail Example
  slug: healthomics-reference-store-detail-example
- key_count: 3
  name: Healthomics Reference Store Filter Example
  slug: healthomics-reference-store-filter-example
- key_count: 5
  name: Healthomics Run Group List Item Example
  slug: healthomics-run-group-list-item-example
- key_count: 5
  name: Healthomics Run List Item Example
  slug: healthomics-run-list-item-example
- key_count: 0
  name: Healthomics Run Parameters Example
  slug: healthomics-run-parameters-example
- key_count: 4
  name: Healthomics Sequence Information Example
  slug: healthomics-sequence-information-example
- key_count: 5
  name: Healthomics Sequence Store Detail Example
  slug: healthomics-sequence-store-detail-example
- key_count: 3
  name: Healthomics Sequence Store Filter Example
  slug: healthomics-sequence-store-filter-example
- key_count: 2
  name: Healthomics Source Files Example
  slug: healthomics-source-files-example
- key_count: 2
  name: Healthomics Sse Config Example
  slug: healthomics-sse-config-example
- key_count: 5
  name: Healthomics Start Annotation Import Request Example
  slug: healthomics-start-annotation-import-request-example
- key_count: 1
  name: Healthomics Start Annotation Import Response Example
  slug: healthomics-start-annotation-import-response-example
- key_count: 2
  name: Healthomics Start Read Set Activation Job Request Example
  slug: healthomics-start-read-set-activation-job-request-example
- key_count: 4
  name: Healthomics Start Read Set Activation Job Response Example
  slug: healthomics-start-read-set-activation-job-response-example
- key_count: 1
  name: Healthomics Start Read Set Activation Job Source Item Example
  slug: healthomics-start-read-set-activation-job-source-item-example
- key_count: 4
  name: Healthomics Start Read Set Export Job Request Example
  slug: healthomics-start-read-set-export-job-request-example
- key_count: 5
  name: Healthomics Start Read Set Export Job Response Example
  slug: healthomics-start-read-set-export-job-response-example
- key_count: 3
  name: Healthomics Start Read Set Import Job Request Example
  slug: healthomics-start-read-set-import-job-request-example
- key_count: 5
  name: Healthomics Start Read Set Import Job Response Example
  slug: healthomics-start-read-set-import-job-response-example
- key_count: 5
  name: Healthomics Start Read Set Import Job Source Item Example
  slug: healthomics-start-read-set-import-job-source-item-example
- key_count: 3
  name: Healthomics Start Reference Import Job Request Example
  slug: healthomics-start-reference-import-job-request-example
- key_count: 5
  name: Healthomics Start Reference Import Job Response Example
  slug: healthomics-start-reference-import-job-response-example
- key_count: 4
  name: Healthomics Start Reference Import Job Source Item Example
  slug: healthomics-start-reference-import-job-source-item-example
- key_count: 5
  name: Healthomics Start Run Request Example
  slug: healthomics-start-run-request-example
- key_count: 4
  name: Healthomics Start Run Response Example
  slug: healthomics-start-run-response-example
- key_count: 5
  name: Healthomics Start Variant Import Request Example
  slug: healthomics-start-variant-import-request-example
- key_count: 1
  name: Healthomics Start Variant Import Response Example
  slug: healthomics-start-variant-import-response-example
- key_count: 1
  name: Healthomics Store Options Example
  slug: healthomics-store-options-example
- key_count: 1
  name: Healthomics Tag Resource Request Example
  slug: healthomics-tag-resource-request-example
- key_count: 0
  name: Healthomics Tag Resource Response Example
  slug: healthomics-tag-resource-response-example
- key_count: 5
  name: Healthomics Task List Item Example
  slug: healthomics-task-list-item-example
- key_count: 1
  name: Healthomics Tsv Options Example
  slug: healthomics-tsv-options-example
- key_count: 3
  name: Healthomics Tsv Store Options Example
  slug: healthomics-tsv-store-options-example
- key_count: 0
  name: Healthomics Untag Resource Request Example
  slug: healthomics-untag-resource-request-example
- key_count: 0
  name: Healthomics Untag Resource Response Example
  slug: healthomics-untag-resource-response-example
- key_count: 1
  name: Healthomics Update Annotation Store Request Example
  slug: healthomics-update-annotation-store-request-example
- key_count: 5
  name: Healthomics Update Annotation Store Response Example
  slug: healthomics-update-annotation-store-response-example
- key_count: 5
  name: Healthomics Update Run Group Request Example
  slug: healthomics-update-run-group-request-example
- key_count: 1
  name: Healthomics Update Variant Store Request Example
  slug: healthomics-update-variant-store-request-example
- key_count: 5
  name: Healthomics Update Variant Store Response Example
  slug: healthomics-update-variant-store-response-example
- key_count: 2
  name: Healthomics Update Workflow Request Example
  slug: healthomics-update-workflow-request-example
- key_count: 1
  name: Healthomics Upload Read Set Part Request Example
  slug: healthomics-upload-read-set-part-request-example
- key_count: 1
  name: Healthomics Upload Read Set Part Response Example
  slug: healthomics-upload-read-set-part-response-example
- key_count: 3
  name: Healthomics Variant Import Item Detail Example
  slug: healthomics-variant-import-item-detail-example
- key_count: 1
  name: Healthomics Variant Import Item Source Example
  slug: healthomics-variant-import-item-source-example
- key_count: 5
  name: Healthomics Variant Import Job Item Example
  slug: healthomics-variant-import-job-item-example
- key_count: 5
  name: Healthomics Variant Store Item Example
  slug: healthomics-variant-store-item-example
- key_count: 2
  name: Healthomics Vcf Options Example
  slug: healthomics-vcf-options-example
- key_count: 5
  name: Healthomics Workflow List Item Example
  slug: healthomics-workflow-list-item-example
- key_count: 2
  name: Healthomics Workflow Parameter Example
  slug: healthomics-workflow-parameter-example
features:
- description: Purpose-built storage for genomic, transcriptomic, and other omics data with automatic optimization.
  name: Omics Storage
- description: Run industry-standard bioinformatics tools and pipelines using WDL and Nextflow workflow definitions.
  name: Bioinformatics Workflows
- description: Store and query genomic annotation data from sources like ClinVar, Ensembl, and custom datasets.
  name: Annotation Stores
- description: Store and query genomic variant data in VCF and other standard bioinformatics formats.
  name: Variant Stores
- description: Efficiently store and retrieve genomic sequence read sets in FASTQ, BAM, and CRAM formats.
  name: Sequence Stores
- description: Store and access reference genome files for alignment and analysis workflows.
  name: Reference Genomes
- description: Fully managed compute infrastructure for running bioinformatics workflows at scale.
  name: Managed Compute
finops:
- name: Amazon Healthomics Finops
  service_category: API
  slug: amazon-healthomics-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/amazon-healthomics.png
json_schemas:
- name: AbortMultipartReadSetUploadRequest
  property_count: 0
  slug: healthomics-abort-multipart-read-set-upload-request
- name: AbortMultipartReadSetUploadResponse
  property_count: 0
  slug: healthomics-abort-multipart-read-set-upload-response
- name: Accelerators
  property_count: 0
  slug: healthomics-accelerators
- name: AccessDeniedException
  property_count: 0
  slug: healthomics-access-denied-exception
- name: ActivateReadSetFilter
  property_count: 3
  slug: healthomics-activate-read-set-filter
- name: ActivateReadSetJobItem
  property_count: 5
  slug: healthomics-activate-read-set-job-item
- name: ActivateReadSetJobList
  property_count: 0
  slug: healthomics-activate-read-set-job-list
- name: ActivateReadSetSourceItem
  property_count: 3
  slug: healthomics-activate-read-set-source-item
- name: ActivateReadSetSourceList
  property_count: 0
  slug: healthomics-activate-read-set-source-list
- name: ActivationJobId
  property_count: 0
  slug: healthomics-activation-job-id
- name: AnnotationFieldMapKeyString
  property_count: 0
  slug: healthomics-annotation-field-map-key-string
- name: AnnotationFieldMap
  property_count: 0
  slug: healthomics-annotation-field-map
- name: AnnotationFieldMapValueString
  property_count: 0
  slug: healthomics-annotation-field-map-value-string
- name: AnnotationImportItemDetail
  property_count: 2
  slug: healthomics-annotation-import-item-detail
- name: AnnotationImportItemDetails
  property_count: 0
  slug: healthomics-annotation-import-item-details
- name: AnnotationImportItemSource
  property_count: 1
  slug: healthomics-annotation-import-item-source
- name: AnnotationImportItemSources
  property_count: 0
  slug: healthomics-annotation-import-item-sources
- name: AnnotationImportJobItem
  property_count: 9
  slug: healthomics-annotation-import-job-item
- name: AnnotationImportJobItems
  property_count: 0
  slug: healthomics-annotation-import-job-items
- name: AnnotationStoreItem
  property_count: 12
  slug: healthomics-annotation-store-item
- name: AnnotationStoreItems
  property_count: 0
  slug: healthomics-annotation-store-items
- name: AnnotationType
  property_count: 0
  slug: healthomics-annotation-type
- name: Arn
  property_count: 0
  slug: healthomics-arn
- name: BatchDeleteReadSetRequest
  property_count: 1
  slug: healthomics-batch-delete-read-set-request
- name: BatchDeleteReadSetResponse
  property_count: 1
  slug: healthomics-batch-delete-read-set-response
- name: Blob
  property_count: 0
  slug: healthomics-blob
- name: Boolean
  property_count: 0
  slug: healthomics-boolean
- name: CancelAnnotationImportRequest
  property_count: 0
  slug: healthomics-cancel-annotation-import-request
- name: CancelAnnotationImportResponse
  property_count: 0
  slug: healthomics-cancel-annotation-import-response
- name: CancelRunRequest
  property_count: 0
  slug: healthomics-cancel-run-request
- name: CancelVariantImportRequest
  property_count: 0
  slug: healthomics-cancel-variant-import-request
- name: CancelVariantImportResponse
  property_count: 0
  slug: healthomics-cancel-variant-import-response
- name: ClientToken
  property_count: 0
  slug: healthomics-client-token
- name: CommentChar
  property_count: 0
  slug: healthomics-comment-char
- name: CompleteMultipartReadSetUploadRequest
  property_count: 1
  slug: healthomics-complete-multipart-read-set-upload-request
- name: CompleteMultipartReadSetUploadResponse
  property_count: 1
  slug: healthomics-complete-multipart-read-set-upload-response
- name: CompleteReadSetUploadPartListItemPartNumberInteger
  property_count: 0
  slug: healthomics-complete-read-set-upload-part-list-item-part-number-integer
- name: CompleteReadSetUploadPartListItem
  property_count: 3
  slug: healthomics-complete-read-set-upload-part-list-item
- name: CompleteReadSetUploadPartList
  property_count: 0
  slug: healthomics-complete-read-set-upload-part-list
- name: CompletionTime
  property_count: 0
  slug: healthomics-completion-time
- name: ConflictException
  property_count: 0
  slug: healthomics-conflict-exception
- name: CreateAnnotationStoreRequestNameString
  property_count: 0
  slug: healthomics-create-annotation-store-request-name-string
- name: CreateAnnotationStoreRequest
  property_count: 7
  slug: healthomics-create-annotation-store-request
- name: CreateAnnotationStoreResponse
  property_count: 7
  slug: healthomics-create-annotation-store-response
- name: CreateMultipartReadSetUploadRequest
  property_count: 9
  slug: healthomics-create-multipart-read-set-upload-request
- name: CreateMultipartReadSetUploadResponse
  property_count: 11
  slug: healthomics-create-multipart-read-set-upload-response
- name: CreateReferenceStoreRequest
  property_count: 5
  slug: healthomics-create-reference-store-request
- name: CreateReferenceStoreResponse
  property_count: 6
  slug: healthomics-create-reference-store-response
- name: CreateRunGroupRequestMaxCpusInteger
  property_count: 0
  slug: healthomics-create-run-group-request-max-cpus-integer
- name: CreateRunGroupRequestMaxDurationInteger
  property_count: 0
  slug: healthomics-create-run-group-request-max-duration-integer
- name: CreateRunGroupRequestMaxGpusInteger
  property_count: 0
  slug: healthomics-create-run-group-request-max-gpus-integer
- name: CreateRunGroupRequestMaxRunsInteger
  property_count: 0
  slug: healthomics-create-run-group-request-max-runs-integer
- name: CreateRunGroupRequest
  property_count: 7
  slug: healthomics-create-run-group-request
- name: CreateRunGroupResponse
  property_count: 3
  slug: healthomics-create-run-group-response
- name: CreateSequenceStoreRequest
  property_count: 6
  slug: healthomics-create-sequence-store-request
- name: CreateSequenceStoreResponse
  property_count: 7
  slug: healthomics-create-sequence-store-response
- name: CreateVariantStoreRequestNameString
  property_count: 0
  slug: healthomics-create-variant-store-request-name-string
- name: CreateVariantStoreRequest
  property_count: 5
  slug: healthomics-create-variant-store-request
- name: CreateVariantStoreResponse
  property_count: 5
  slug: healthomics-create-variant-store-response
- name: CreateWorkflowRequest
  property_count: 11
  slug: healthomics-create-workflow-request
- name: CreateWorkflowRequestStorageCapacityInteger
  property_count: 0
  slug: healthomics-create-workflow-request-storage-capacity-integer
- name: CreateWorkflowResponse
  property_count: 4
  slug: healthomics-create-workflow-response
- name: CreationTime
  property_count: 0
  slug: healthomics-creation-time
- name: CreationType
  property_count: 0
  slug: healthomics-creation-type
- name: DeleteAnnotationStoreRequest
  property_count: 0
  slug: healthomics-delete-annotation-store-request
- name: DeleteAnnotationStoreResponse
  property_count: 1
  slug: healthomics-delete-annotation-store-response
- name: DeleteReferenceRequest
  property_count: 0
  slug: healthomics-delete-reference-request
- name: DeleteReferenceResponse
  property_count: 0
  slug: healthomics-delete-reference-response
- name: DeleteReferenceStoreRequest
  property_count: 0
  slug: healthomics-delete-reference-store-request
- name: DeleteReferenceStoreResponse
  property_count: 0
  slug: healthomics-delete-reference-store-response
- name: DeleteRunGroupRequest
  property_count: 0
  slug: healthomics-delete-run-group-request
- name: DeleteRunRequest
  property_count: 0
  slug: healthomics-delete-run-request
- name: DeleteSequenceStoreRequest
  property_count: 0
  slug: healthomics-delete-sequence-store-request
- name: DeleteSequenceStoreResponse
  property_count: 0
  slug: healthomics-delete-sequence-store-response
- name: DeleteVariantStoreRequest
  property_count: 0
  slug: healthomics-delete-variant-store-request
- name: DeleteVariantStoreResponse
  property_count: 1
  slug: healthomics-delete-variant-store-response
- name: DeleteWorkflowRequest
  property_count: 0
  slug: healthomics-delete-workflow-request
- name: Encoding
  property_count: 0
  slug: healthomics-encoding
- name: EncryptionType
  property_count: 0
  slug: healthomics-encryption-type
- name: EscapeChar
  property_count: 0
  slug: healthomics-escape-char
- name: EscapeQuotes
  property_count: 0
  slug: healthomics-escape-quotes
- name: ExportJobId
  property_count: 0
  slug: healthomics-export-job-id
- name: ExportReadSetDetailList
  property_count: 0
  slug: healthomics-export-read-set-detail-list
- name: ExportReadSetDetail
  property_count: 3
  slug: healthomics-export-read-set-detail
- name: ExportReadSetFilter
  property_count: 3
  slug: healthomics-export-read-set-filter
- name: ExportReadSetJobDetailList
  property_count: 0
  slug: healthomics-export-read-set-job-detail-list
- name: ExportReadSetJobDetail
  property_count: 6
  slug: healthomics-export-read-set-job-detail
- name: ExportReadSet
  property_count: 1
  slug: healthomics-export-read-set
- name: FileInformationContentLengthLong
  property_count: 0
  slug: healthomics-file-information-content-length-long
- name: FileInformationPartSizeLong
  property_count: 0
  slug: healthomics-file-information-part-size-long
- name: FileInformation
  property_count: 3
  slug: healthomics-file-information
- name: FileInformationTotalPartsInteger
  property_count: 0
  slug: healthomics-file-information-total-parts-integer
- name: FileType
  property_count: 0
  slug: healthomics-file-type
- name: FormatOptions
  property_count: 2
  slug: healthomics-format-options
- name: FormatToHeaderKey
  property_count: 0
  slug: healthomics-format-to-header-key
- name: FormatToHeader
  property_count: 0
  slug: healthomics-format-to-header
- name: FormatToHeaderValueString
  property_count: 0
  slug: healthomics-format-to-header-value-string
- name: GeneratedFrom
  property_count: 0
  slug: healthomics-generated-from
- name: GetAnnotationImportRequest
  property_count: 0
  slug: healthomics-get-annotation-import-request
- name: GetAnnotationImportResponse
  property_count: 12
  slug: healthomics-get-annotation-import-response
- name: GetAnnotationStoreRequest
  property_count: 0
  slug: healthomics-get-annotation-store-request
- name: GetAnnotationStoreResponse
  property_count: 14
  slug: healthomics-get-annotation-store-response
- name: GetReadSetActivationJobRequest
  property_count: 0
  slug: healthomics-get-read-set-activation-job-request
- name: GetReadSetActivationJobResponse
  property_count: 7
  slug: healthomics-get-read-set-activation-job-response
- name: GetReadSetExportJobRequest
  property_count: 0
  slug: healthomics-get-read-set-export-job-request
- name: GetReadSetExportJobResponse
  property_count: 8
  slug: healthomics-get-read-set-export-job-response
- name: GetReadSetImportJobRequest
  property_count: 0
  slug: healthomics-get-read-set-import-job-request
- name: GetReadSetImportJobResponse
  property_count: 8
  slug: healthomics-get-read-set-import-job-response
- name: GetReadSetMetadataRequest
  property_count: 0
  slug: healthomics-get-read-set-metadata-request
- name: GetReadSetMetadataResponse
  property_count: 15
  slug: healthomics-get-read-set-metadata-response
- name: GetReadSetRequestPartNumberInteger
  property_count: 0
  slug: healthomics-get-read-set-request-part-number-integer
- name: GetReadSetRequest
  property_count: 0
  slug: healthomics-get-read-set-request
- name: GetReadSetResponse
  property_count: 1
  slug: healthomics-get-read-set-response
- name: GetReferenceImportJobRequest
  property_count: 0
  slug: healthomics-get-reference-import-job-request
- name: GetReferenceImportJobResponse
  property_count: 8
  slug: healthomics-get-reference-import-job-response
- name: GetReferenceMetadataRequest
  property_count: 0
  slug: healthomics-get-reference-metadata-request
- name: GetReferenceMetadataResponse
  property_count: 10
  slug: healthomics-get-reference-metadata-response
- name: GetReferenceRequestPartNumberInteger
  property_count: 0
  slug: healthomics-get-reference-request-part-number-integer
- name: GetReferenceRequest
  property_count: 0
  slug: healthomics-get-reference-request
- name: GetReferenceResponse
  property_count: 1
  slug: healthomics-get-reference-response
- name: GetReferenceStoreRequest
  property_count: 0
  slug: healthomics-get-reference-store-request
- name: GetReferenceStoreResponse
  property_count: 6
  slug: healthomics-get-reference-store-response
- name: GetRunGroupRequest
  property_count: 0
  slug: healthomics-get-run-group-request
- name: GetRunGroupResponseMaxCpusInteger
  property_count: 0
  slug: healthomics-get-run-group-response-max-cpus-integer
- name: GetRunGroupResponseMaxDurationInteger
  property_count: 0
  slug: healthomics-get-run-group-response-max-duration-integer
- name: GetRunGroupResponseMaxGpusInteger
  property_count: 0
  slug: healthomics-get-run-group-response-max-gpus-integer
- name: GetRunGroupResponseMaxRunsInteger
  property_count: 0
  slug: healthomics-get-run-group-response-max-runs-integer
- name: GetRunGroupResponse
  property_count: 9
  slug: healthomics-get-run-group-response
- name: GetRunRequest
  property_count: 0
  slug: healthomics-get-run-request
- name: GetRunResponsePriorityInteger
  property_count: 0
  slug: healthomics-get-run-response-priority-integer
- name: GetRunResponse
  property_count: 24
  slug: healthomics-get-run-response
- name: GetRunResponseStorageCapacityInteger
  property_count: 0
  slug: healthomics-get-run-response-storage-capacity-integer
- name: GetRunTaskRequest
  property_count: 0
  slug: healthomics-get-run-task-request
- name: GetRunTaskResponseCpusInteger
  property_count: 0
  slug: healthomics-get-run-task-response-cpus-integer
- name: GetRunTaskResponseGpusInteger
  property_count: 0
  slug: healthomics-get-run-task-response-gpus-integer
- name: GetRunTaskResponseMemoryInteger
  property_count: 0
  slug: healthomics-get-run-task-response-memory-integer
- name: GetRunTaskResponse
  property_count: 11
  slug: healthomics-get-run-task-response
- name: GetSequenceStoreRequest
  property_count: 0
  slug: healthomics-get-sequence-store-request
- name: GetSequenceStoreResponse
  property_count: 7
  slug: healthomics-get-sequence-store-response
- name: GetVariantImportRequest
  property_count: 0
  slug: healthomics-get-variant-import-request
- name: GetVariantImportResponse
  property_count: 11
  slug: healthomics-get-variant-import-response
- name: GetVariantStoreRequest
  property_count: 0
  slug: healthomics-get-variant-store-request
- name: GetVariantStoreResponse
  property_count: 12
  slug: healthomics-get-variant-store-response
- name: GetWorkflowRequest
  property_count: 0
  slug: healthomics-get-workflow-request
- name: GetWorkflowResponse
  property_count: 17
  slug: healthomics-get-workflow-response
- name: GetWorkflowResponseStorageCapacityInteger
  property_count: 0
  slug: healthomics-get-workflow-response-storage-capacity-integer
- name: Header
  property_count: 0
  slug: healthomics-header
- name: ImportJobId
  property_count: 0
  slug: healthomics-import-job-id
- name: ImportReadSetFilter
  property_count: 3
  slug: healthomics-import-read-set-filter
- name: ImportReadSetJobItem
  property_count: 6
  slug: healthomics-import-read-set-job-item
- name: ImportReadSetJobList
  property_count: 0
  slug: healthomics-import-read-set-job-list
- name: ImportReadSetSourceItem
  property_count: 11
  slug: healthomics-import-read-set-source-item
- name: ImportReadSetSourceList
  property_count: 0
  slug: healthomics-import-read-set-source-list
- name: ImportReferenceFilter
  property_count: 3
  slug: healthomics-import-reference-filter
- name: ImportReferenceJobItem
  property_count: 6
  slug: healthomics-import-reference-job-item
- name: ImportReferenceJobList
  property_count: 0
  slug: healthomics-import-reference-job-list
- name: ImportReferenceSourceItem
  property_count: 6
  slug: healthomics-import-reference-source-item
- name: ImportReferenceSourceList
  property_count: 0
  slug: healthomics-import-reference-source-list
- name: InternalServerException
  property_count: 0
  slug: healthomics-internal-server-exception
- name: JobStatusMessage
  property_count: 0
  slug: healthomics-job-status-message
- name: JobStatusMsg
  property_count: 0
  slug: healthomics-job-status-msg
- name: JobStatus
  property_count: 0
  slug: healthomics-job-status
- name: LineSep
  property_count: 0
  slug: healthomics-line-sep
- name: ListAnnotationImportJobsFilter
  property_count: 2
  slug: healthomics-list-annotation-import-jobs-filter
- name: ListAnnotationImportJobsRequestIdsList
  property_count: 0
  slug: healthomics-list-annotation-import-jobs-request-ids-list
- name: ListAnnotationImportJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-annotation-import-jobs-request-max-results-integer
- name: ListAnnotationImportJobsRequestNextTokenString
  property_count: 0
  slug: healthomics-list-annotation-import-jobs-request-next-token-string
- name: ListAnnotationImportJobsRequest
  property_count: 2
  slug: healthomics-list-annotation-import-jobs-request
- name: ListAnnotationImportJobsResponse
  property_count: 2
  slug: healthomics-list-annotation-import-jobs-response
- name: ListAnnotationStoresFilter
  property_count: 1
  slug: healthomics-list-annotation-stores-filter
- name: ListAnnotationStoresRequestIdsList
  property_count: 0
  slug: healthomics-list-annotation-stores-request-ids-list
- name: ListAnnotationStoresRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-annotation-stores-request-max-results-integer
- name: ListAnnotationStoresRequestNextTokenString
  property_count: 0
  slug: healthomics-list-annotation-stores-request-next-token-string
- name: ListAnnotationStoresRequest
  property_count: 2
  slug: healthomics-list-annotation-stores-request
- name: ListAnnotationStoresResponse
  property_count: 2
  slug: healthomics-list-annotation-stores-response
- name: ListMultipartReadSetUploadsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-multipart-read-set-uploads-request-max-results-integer
- name: ListMultipartReadSetUploadsRequest
  property_count: 0
  slug: healthomics-list-multipart-read-set-uploads-request
- name: ListMultipartReadSetUploadsResponse
  property_count: 2
  slug: healthomics-list-multipart-read-set-uploads-response
- name: ListReadSetActivationJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-read-set-activation-jobs-request-max-results-integer
- name: ListReadSetActivationJobsRequest
  property_count: 1
  slug: healthomics-list-read-set-activation-jobs-request
- name: ListReadSetActivationJobsResponse
  property_count: 2
  slug: healthomics-list-read-set-activation-jobs-response
- name: ListReadSetExportJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-read-set-export-jobs-request-max-results-integer
- name: ListReadSetExportJobsRequest
  property_count: 1
  slug: healthomics-list-read-set-export-jobs-request
- name: ListReadSetExportJobsResponse
  property_count: 2
  slug: healthomics-list-read-set-export-jobs-response
- name: ListReadSetImportJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-read-set-import-jobs-request-max-results-integer
- name: ListReadSetImportJobsRequest
  property_count: 1
  slug: healthomics-list-read-set-import-jobs-request
- name: ListReadSetImportJobsResponse
  property_count: 2
  slug: healthomics-list-read-set-import-jobs-response
- name: ListReadSetUploadPartsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-read-set-upload-parts-request-max-results-integer
- name: ListReadSetUploadPartsRequest
  property_count: 2
  slug: healthomics-list-read-set-upload-parts-request
- name: ListReadSetUploadPartsResponse
  property_count: 2
  slug: healthomics-list-read-set-upload-parts-response
- name: ListReadSetsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-read-sets-request-max-results-integer
- name: ListReadSetsRequest
  property_count: 1
  slug: healthomics-list-read-sets-request
- name: ListReadSetsResponse
  property_count: 2
  slug: healthomics-list-read-sets-response
- name: ListReferenceImportJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-reference-import-jobs-request-max-results-integer
- name: ListReferenceImportJobsRequest
  property_count: 1
  slug: healthomics-list-reference-import-jobs-request
- name: ListReferenceImportJobsResponse
  property_count: 2
  slug: healthomics-list-reference-import-jobs-response
- name: ListReferenceStoresRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-reference-stores-request-max-results-integer
- name: ListReferenceStoresRequest
  property_count: 1
  slug: healthomics-list-reference-stores-request
- name: ListReferenceStoresResponse
  property_count: 2
  slug: healthomics-list-reference-stores-response
- name: ListReferencesRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-references-request-max-results-integer
- name: ListReferencesRequest
  property_count: 1
  slug: healthomics-list-references-request
- name: ListReferencesResponse
  property_count: 2
  slug: healthomics-list-references-response
- name: ListRunGroupsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-run-groups-request-max-results-integer
- name: ListRunGroupsRequest
  property_count: 0
  slug: healthomics-list-run-groups-request
- name: ListRunGroupsResponse
  property_count: 2
  slug: healthomics-list-run-groups-response
- name: ListRunTasksRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-run-tasks-request-max-results-integer
- name: ListRunTasksRequest
  property_count: 0
  slug: healthomics-list-run-tasks-request
- name: ListRunTasksResponse
  property_count: 2
  slug: healthomics-list-run-tasks-response
- name: ListRunsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-runs-request-max-results-integer
- name: ListRunsRequest
  property_count: 0
  slug: healthomics-list-runs-request
- name: ListRunsResponse
  property_count: 2
  slug: healthomics-list-runs-response
- name: ListSequenceStoresRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-sequence-stores-request-max-results-integer
- name: ListSequenceStoresRequest
  property_count: 1
  slug: healthomics-list-sequence-stores-request
- name: ListSequenceStoresResponse
  property_count: 2
  slug: healthomics-list-sequence-stores-response
- name: ListTagsForResourceRequest
  property_count: 0
  slug: healthomics-list-tags-for-resource-request
- name: ListTagsForResourceResponse
  property_count: 1
  slug: healthomics-list-tags-for-resource-response
- name: ListVariantImportJobsFilter
  property_count: 2
  slug: healthomics-list-variant-import-jobs-filter
- name: ListVariantImportJobsRequestIdsList
  property_count: 0
  slug: healthomics-list-variant-import-jobs-request-ids-list
- name: ListVariantImportJobsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-variant-import-jobs-request-max-results-integer
- name: ListVariantImportJobsRequestNextTokenString
  property_count: 0
  slug: healthomics-list-variant-import-jobs-request-next-token-string
- name: ListVariantImportJobsRequest
  property_count: 2
  slug: healthomics-list-variant-import-jobs-request
- name: ListVariantImportJobsResponse
  property_count: 2
  slug: healthomics-list-variant-import-jobs-response
- name: ListVariantStoresFilter
  property_count: 1
  slug: healthomics-list-variant-stores-filter
- name: ListVariantStoresRequestIdsList
  property_count: 0
  slug: healthomics-list-variant-stores-request-ids-list
- name: ListVariantStoresRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-variant-stores-request-max-results-integer
- name: ListVariantStoresRequestNextTokenString
  property_count: 0
  slug: healthomics-list-variant-stores-request-next-token-string
- name: ListVariantStoresRequest
  property_count: 2
  slug: healthomics-list-variant-stores-request
- name: ListVariantStoresResponse
  property_count: 2
  slug: healthomics-list-variant-stores-response
- name: ListWorkflowsRequestMaxResultsInteger
  property_count: 0
  slug: healthomics-list-workflows-request-max-results-integer
- name: ListWorkflowsRequest
  property_count: 0
  slug: healthomics-list-workflows-request
- name: ListWorkflowsResponse
  property_count: 2
  slug: healthomics-list-workflows-response
- name: Long
  property_count: 0
  slug: healthomics-long
- name: Md5
  property_count: 0
  slug: healthomics-md5
- name: MultipartReadSetUploadListItem
  property_count: 11
  slug: healthomics-multipart-read-set-upload-list-item
- name: MultipartReadSetUploadList
  property_count: 0
  slug: healthomics-multipart-read-set-upload-list
- name: NextToken
  property_count: 0
  slug: healthomics-next-token
- name: NotSupportedOperationException
  property_count: 0
  slug: healthomics-not-supported-operation-exception
- name: PrimitiveBoolean
  property_count: 0
  slug: healthomics-primitive-boolean
- name: QuoteAll
  property_count: 0
  slug: healthomics-quote-all
- name: Quote
  property_count: 0
  slug: healthomics-quote
- name: RangeNotSatisfiableException
  property_count: 0
  slug: healthomics-range-not-satisfiable-exception
- name: Range
  property_count: 0
  slug: healthomics-range
- name: ReadOptions
  property_count: 9
  slug: healthomics-read-options
- name: ReadSetActivationJobItemStatus
  property_count: 0
  slug: healthomics-read-set-activation-job-item-status
- name: ReadSetActivationJobStatus
  property_count: 0
  slug: healthomics-read-set-activation-job-status
- name: ReadSetArn
  property_count: 0
  slug: healthomics-read-set-arn
- name: ReadSetBatchErrorList
  property_count: 0
  slug: healthomics-read-set-batch-error-list
- name: ReadSetBatchError
  property_count: 3
  slug: healthomics-read-set-batch-error
- name: ReadSetDescription
  property_count: 0
  slug: healthomics-read-set-description
- name: ReadSetExportJobItemStatus
  property_count: 0
  slug: healthomics-read-set-export-job-item-status
- name: ReadSetExportJobStatus
  property_count: 0
  slug: healthomics-read-set-export-job-status
- name: ReadSetFile
  property_count: 0
  slug: healthomics-read-set-file
- name: ReadSetFiles
  property_count: 3
  slug: healthomics-read-set-files
- name: ReadSetFilter
  property_count: 9
  slug: healthomics-read-set-filter
- name: ReadSetIdList
  property_count: 0
  slug: healthomics-read-set-id-list
- name: ReadSetId
  property_count: 0
  slug: healthomics-read-set-id
- name: ReadSetImportJobItemStatus
  property_count: 0
  slug: healthomics-read-set-import-job-item-status
- name: ReadSetImportJobStatus
  property_count: 0
  slug: healthomics-read-set-import-job-status
- name: ReadSetListItem
  property_count: 14
  slug: healthomics-read-set-list-item
- name: ReadSetList
  property_count: 0
  slug: healthomics-read-set-list
- name: ReadSetName
  property_count: 0
  slug: healthomics-read-set-name
- name: ReadSetPartSource
  property_count: 0
  slug: healthomics-read-set-part-source
- name: ReadSetPartStreamingBlob
  property_count: 0
  slug: healthomics-read-set-part-streaming-blob
- name: ReadSetStatusMessage
  property_count: 0
  slug: healthomics-read-set-status-message
- name: ReadSetStatus
  property_count: 0
  slug: healthomics-read-set-status
- name: ReadSetStreamingBlob
  property_count: 0
  slug: healthomics-read-set-streaming-blob
- name: ReadSetUploadPartListFilter
  property_count: 2
  slug: healthomics-read-set-upload-part-list-filter
- name: ReadSetUploadPartListItemPartNumberInteger
  property_count: 0
  slug: healthomics-read-set-upload-part-list-item-part-number-integer
- name: ReadSetUploadPartListItemPartSizeLong
  property_count: 0
  slug: healthomics-read-set-upload-part-list-item-part-size-long
- name: ReadSetUploadPartListItem
  property_count: 6
  slug: healthomics-read-set-upload-part-list-item
- name: ReadSetUploadPartList
  property_count: 0
  slug: healthomics-read-set-upload-part-list
- name: ReferenceArn
  property_count: 0
  slug: healthomics-reference-arn
- name: ReferenceDescription
  property_count: 0
  slug: healthomics-reference-description
- name: ReferenceFile
  property_count: 0
  slug: healthomics-reference-file
- name: ReferenceFiles
  property_count: 2
  slug: healthomics-reference-files
- name: ReferenceFilter
  property_count: 4
  slug: healthomics-reference-filter
- name: ReferenceId
  property_count: 0
  slug: healthomics-reference-id
- name: ReferenceImportJobItemStatus
  property_count: 0
  slug: healthomics-reference-import-job-item-status
- name: ReferenceImportJobStatus
  property_count: 0
  slug: healthomics-reference-import-job-status
- name: ReferenceItem
  property_count: 1
  slug: healthomics-reference-item
- name: ReferenceListItem
  property_count: 9
  slug: healthomics-reference-list-item
- name: ReferenceList
  property_count: 0
  slug: healthomics-reference-list
- name: ReferenceName
  property_count: 0
  slug: healthomics-reference-name
- name: ReferenceStatus
  property_count: 0
  slug: healthomics-reference-status
- name: ReferenceStoreArn
  property_count: 0
  slug: healthomics-reference-store-arn
- name: ReferenceStoreDescription
  property_count: 0
  slug: healthomics-reference-store-description
- name: ReferenceStoreDetailList
  property_count: 0
  slug: healthomics-reference-store-detail-list
- name: ReferenceStoreDetail
  property_count: 6
  slug: healthomics-reference-store-detail
- name: ReferenceStoreFilter
  property_count: 3
  slug: healthomics-reference-store-filter
- name: ReferenceStoreId
  property_count: 0
  slug: healthomics-reference-store-id
- name: ReferenceStoreName
  property_count: 0
  slug: healthomics-reference-store-name
- name: ReferenceStreamingBlob
  property_count: 0
  slug: healthomics-reference-streaming-blob
- name: RequestTimeoutException
  property_count: 0
  slug: healthomics-request-timeout-exception
- name: ResourceId
  property_count: 0
  slug: healthomics-resource-id
- name: ResourceIdentifier
  property_count: 0
  slug: healthomics-resource-identifier
- name: ResourceNotFoundException
  property_count: 0
  slug: healthomics-resource-not-found-exception
- name: RoleArn
  property_count: 0
  slug: healthomics-role-arn
- name: RunArn
  property_count: 0
  slug: healthomics-run-arn
- name: RunExportList
  property_count: 0
  slug: healthomics-run-export-list
- name: RunExport
  property_count: 0
  slug: healthomics-run-export
- name: RunGroupArn
  property_count: 0
  slug: healthomics-run-group-arn
- name: RunGroupId
  property_count: 0
  slug: healthomics-run-group-id
- name: RunGroupListItemMaxCpusInteger
  property_count: 0
  slug: healthomics-run-group-list-item-max-cpus-integer
- name: RunGroupListItemMaxDurationInteger
  property_count: 0
  slug: healthomics-run-group-list-item-max-duration-integer
- name: RunGroupListItemMaxGpusInteger
  property_count: 0
  slug: healthomics-run-group-list-item-max-gpus-integer
- name: RunGroupListItemMaxRunsInteger
  property_count: 0
  slug: healthomics-run-group-list-item-max-runs-integer
- name: RunGroupListItem
  property_count: 8
  slug: healthomics-run-group-list-item
- name: RunGroupList
  property_count: 0
  slug: healthomics-run-group-list
- name: RunGroupListToken
  property_count: 0
  slug: healthomics-run-group-list-token
- name: RunGroupName
  property_count: 0
  slug: healthomics-run-group-name
- name: RunGroupRequestId
  property_count: 0
  slug: healthomics-run-group-request-id
- name: RunGroupTimestamp
  property_count: 0
  slug: healthomics-run-group-timestamp
- name: RunId
  property_count: 0
  slug: healthomics-run-id
- name: RunLeftNormalization
  property_count: 0
  slug: healthomics-run-left-normalization
- name: RunListItemPriorityInteger
  property_count: 0
  slug: healthomics-run-list-item-priority-integer
- name: RunListItem
  property_count: 10
  slug: healthomics-run-list-item
- name: RunListItemStorageCapacityInteger
  property_count: 0
  slug: healthomics-run-list-item-storage-capacity-integer
- name: RunList
  property_count: 0
  slug: healthomics-run-list
- name: RunListToken
  property_count: 0
  slug: healthomics-run-list-token
- name: RunLogLevel
  property_count: 0
  slug: healthomics-run-log-level
- name: RunName
  property_count: 0
  slug: healthomics-run-name
- name: RunOutputUri
  property_count: 0
  slug: healthomics-run-output-uri
- name: RunParameters
  property_count: 0
  slug: healthomics-run-parameters
- name: RunRequestId
  property_count: 0
  slug: healthomics-run-request-id
- name: RunResourceDigestKey
  property_count: 0
  slug: healthomics-run-resource-digest-key
- name: RunResourceDigest
  property_count: 0
  slug: healthomics-run-resource-digest
- name: RunResourceDigests
  property_count: 0
  slug: healthomics-run-resource-digests
- name: RunRoleArn
  property_count: 0
  slug: healthomics-run-role-arn
- name: RunStartedBy
  property_count: 0
  slug: healthomics-run-started-by
- name: RunStatusMessage
  property_count: 0
  slug: healthomics-run-status-message
- name: RunStatus
  property_count: 0
  slug: healthomics-run-status
- name: RunTimestamp
  property_count: 0
  slug: healthomics-run-timestamp
- name: S3Destination
  property_count: 0
  slug: healthomics-s3-destination
- name: S3Uri
  property_count: 0
  slug: healthomics-s3-uri
- name: SampleId
  property_count: 0
  slug: healthomics-sample-id
- name: SchemaItemKeyString
  property_count: 0
  slug: healthomics-schema-item-key-string
- name: SchemaItem
  property_count: 0
  slug: healthomics-schema-item
- name: SchemaValueType
  property_count: 0
  slug: healthomics-schema-value-type
- name: Separator
  property_count: 0
  slug: healthomics-separator
- name: SequenceInformation
  property_count: 4
  slug: healthomics-sequence-information
- name: SequenceStoreArn
  property_count: 0
  slug: healthomics-sequence-store-arn
- name: SequenceStoreDescription
  property_count: 0
  slug: healthomics-sequence-store-description
- name: SequenceStoreDetailList
  property_count: 0
  slug: healthomics-sequence-store-detail-list
- name: SequenceStoreDetail
  property_count: 7
  slug: healthomics-sequence-store-detail
- name: SequenceStoreFilter
  property_count: 3
  slug: healthomics-sequence-store-filter
- name: SequenceStoreId
  property_count: 0
  slug: healthomics-sequence-store-id
- name: SequenceStoreName
  property_count: 0
  slug: healthomics-sequence-store-name
- name: ServiceQuotaExceededException
  property_count: 0
  slug: healthomics-service-quota-exceeded-exception
- name: SourceFiles
  property_count: 2
  slug: healthomics-source-files
- name: SseConfigKeyArnString
  property_count: 0
  slug: healthomics-sse-config-key-arn-string
- name: SseConfig
  property_count: 2
  slug: healthomics-sse-config
- name: StartAnnotationImportRequest
  property_count: 6
  slug: healthomics-start-annotation-import-request
- name: StartAnnotationImportResponse
  property_count: 1
  slug: healthomics-start-annotation-import-response
- name: StartReadSetActivationJobRequest
  property_count: 2
  slug: healthomics-start-read-set-activation-job-request
- name: StartReadSetActivationJobRequestSourcesList
  property_count: 0
  slug: healthomics-start-read-set-activation-job-request-sources-list
- name: StartReadSetActivationJobResponse
  property_count: 4
  slug: healthomics-start-read-set-activation-job-response
- name: StartReadSetActivationJobSourceItem
  property_count: 1
  slug: healthomics-start-read-set-activation-job-source-item
- name: StartReadSetExportJobRequest
  property_count: 4
  slug: healthomics-start-read-set-export-job-request
- name: StartReadSetExportJobRequestSourcesList
  property_count: 0
  slug: healthomics-start-read-set-export-job-request-sources-list
- name: StartReadSetExportJobResponse
  property_count: 5
  slug: healthomics-start-read-set-export-job-response
- name: StartReadSetImportJobRequest
  property_count: 3
  slug: healthomics-start-read-set-import-job-request
- name: StartReadSetImportJobRequestSourcesList
  property_count: 0
  slug: healthomics-start-read-set-import-job-request-sources-list
- name: StartReadSetImportJobResponse
  property_count: 5
  slug: healthomics-start-read-set-import-job-response
- name: StartReadSetImportJobSourceItem
  property_count: 9
  slug: healthomics-start-read-set-import-job-source-item
- name: StartReferenceImportJobRequest
  property_count: 3
  slug: healthomics-start-reference-import-job-request
- name: StartReferenceImportJobRequestSourcesList
  property_count: 0
  slug: healthomics-start-reference-import-job-request-sources-list
- name: StartReferenceImportJobResponse
  property_count: 5
  slug: healthomics-start-reference-import-job-response
- name: StartReferenceImportJobSourceItem
  property_count: 4
  slug: healthomics-start-reference-import-job-source-item
- name: StartRunRequestPriorityInteger
  property_count: 0
  slug: healthomics-start-run-request-priority-integer
- name: StartRunRequest
  property_count: 13
  slug: healthomics-start-run-request
- name: StartRunRequestStorageCapacityInteger
  property_count: 0
  slug: healthomics-start-run-request-storage-capacity-integer
- name: StartRunResponse
  property_count: 4
  slug: healthomics-start-run-response
- name: StartVariantImportRequest
  property_count: 5
  slug: healthomics-start-variant-import-request
- name: StartVariantImportResponse
  property_count: 1
  slug: healthomics-start-variant-import-response
- name: StatusMessage
  property_count: 0
  slug: healthomics-status-message
- name: StoreDescription
  property_count: 0
  slug: healthomics-store-description
- name: StoreFormat
  property_count: 0
  slug: healthomics-store-format
- name: StoreName
  property_count: 0
  slug: healthomics-store-name
- name: StoreOptions
  property_count: 1
  slug: healthomics-store-options
- name: StoreStatus
  property_count: 0
  slug: healthomics-store-status
- name: String
  property_count: 0
  slug: healthomics-string
- name: SubjectId
  property_count: 0
  slug: healthomics-subject-id
- name: SyntheticTimestamp_date_time
  property_count: 0
  slug: healthomics-synthetic-timestamp_date_time
- name: TagArn
  property_count: 0
  slug: healthomics-tag-arn
- name: TagKeyList
  property_count: 0
  slug: healthomics-tag-key-list
- name: TagKey
  property_count: 0
  slug: healthomics-tag-key
- name: TagMap
  property_count: 0
  slug: healthomics-tag-map
- name: TagResourceRequest
  property_count: 1
  slug: healthomics-tag-resource-request
- name: TagResourceRequestTagsMap
  property_count: 0
  slug: healthomics-tag-resource-request-tags-map
- name: TagResourceResponse
  property_count: 0
  slug: healthomics-tag-resource-response
- name: TagValue
  property_count: 0
  slug: healthomics-tag-value
- name: TaskId
  property_count: 0
  slug: healthomics-task-id
- name: TaskListItemCpusInteger
  property_count: 0
  slug: healthomics-task-list-item-cpus-integer
- name: TaskListItemGpusInteger
  property_count: 0
  slug: healthomics-task-list-item-gpus-integer
- name: TaskListItemMemoryInteger
  property_count: 0
  slug: healthomics-task-list-item-memory-integer
- name: TaskListItem
  property_count: 9
  slug: healthomics-task-list-item
- name: TaskList
  property_count: 0
  slug: healthomics-task-list
- name: TaskListToken
  property_count: 0
  slug: healthomics-task-list-token
- name: TaskLogStream
  property_count: 0
  slug: healthomics-task-log-stream
- name: TaskName
  property_count: 0
  slug: healthomics-task-name
- name: TaskStatusMessage
  property_count: 0
  slug: healthomics-task-status-message
- name: TaskStatus
  property_count: 0
  slug: healthomics-task-status
- name: TaskTimestamp
  property_count: 0
  slug: healthomics-task-timestamp
- name: ThrottlingException
  property_count: 0
  slug: healthomics-throttling-exception
- name: TsvOptions
  property_count: 1
  slug: healthomics-tsv-options
- name: TsvStoreOptionsSchemaList
  property_count: 0
  slug: healthomics-tsv-store-options-schema-list
- name: TsvStoreOptions
  property_count: 3
  slug: healthomics-tsv-store-options
- name: UntagResourceRequest
  property_count: 0
  slug: healthomics-untag-resource-request
- name: UntagResourceResponse
  property_count: 0
  slug: healthomics-untag-resource-response
- name: UpdateAnnotationStoreRequest
  property_count: 1
  slug: healthomics-update-annotation-store-request
- name: UpdateAnnotationStoreResponse
  property_count: 9
  slug: healthomics-update-annotation-store-response
- name: UpdateRunGroupRequestMaxCpusInteger
  property_count: 0
  slug: healthomics-update-run-group-request-max-cpus-integer
- name: UpdateRunGroupRequestMaxDurationInteger
  property_count: 0
  slug: healthomics-update-run-group-request-max-duration-integer
- name: UpdateRunGroupRequestMaxGpusInteger
  property_count: 0
  slug: healthomics-update-run-group-request-max-gpus-integer
- name: UpdateRunGroupRequestMaxRunsInteger
  property_count: 0
  slug: healthomics-update-run-group-request-max-runs-integer
- name: UpdateRunGroupRequest
  property_count: 5
  slug: healthomics-update-run-group-request
- name: UpdateTime
  property_count: 0
  slug: healthomics-update-time
- name: UpdateVariantStoreRequest
  property_count: 1
  slug: healthomics-update-variant-store-request
- name: UpdateVariantStoreResponse
  property_count: 7
  slug: healthomics-update-variant-store-response
- name: UpdateWorkflowRequest
  property_count: 2
  slug: healthomics-update-workflow-request
- name: UploadId
  property_count: 0
  slug: healthomics-upload-id
- name: UploadReadSetPartRequestPartNumberInteger
  property_count: 0
  slug: healthomics-upload-read-set-part-request-part-number-integer
- name: UploadReadSetPartRequest
  property_count: 1
  slug: healthomics-upload-read-set-part-request
- name: UploadReadSetPartResponse
  property_count: 1
  slug: healthomics-upload-read-set-part-response
- name: ValidationException
  property_count: 0
  slug: healthomics-validation-exception
- name: VariantImportItemDetail
  property_count: 3
  slug: healthomics-variant-import-item-detail
- name: VariantImportItemDetails
  property_count: 0
  slug: healthomics-variant-import-item-details
- name: VariantImportItemSource
  property_count: 1
  slug: healthomics-variant-import-item-source
- name: VariantImportItemSources
  property_count: 0
  slug: healthomics-variant-import-item-sources
- name: VariantImportJobItem
  property_count: 9
  slug: healthomics-variant-import-job-item
- name: VariantImportJobItems
  property_count: 0
  slug: healthomics-variant-import-job-items
- name: VariantStoreItem
  property_count: 11
  slug: healthomics-variant-store-item
- name: VariantStoreItems
  property_count: 0
  slug: healthomics-variant-store-items
- name: VcfOptions
  property_count: 2
  slug: healthomics-vcf-options
- name: WorkflowArn
  property_count: 0
  slug: healthomics-workflow-arn
- name: WorkflowDefinition
  property_count: 0
  slug: healthomics-workflow-definition
- name: WorkflowDescription
  property_count: 0
  slug: healthomics-workflow-description
- name: WorkflowDigest
  property_count: 0
  slug: healthomics-workflow-digest
- name: WorkflowEngine
  property_count: 0
  slug: healthomics-workflow-engine
- name: WorkflowExportList
  property_count: 0
  slug: healthomics-workflow-export-list
- name: WorkflowExport
  property_count: 0
  slug: healthomics-workflow-export
- name: WorkflowId
  property_count: 0
  slug: healthomics-workflow-id
- name: WorkflowListItem
  property_count: 8
  slug: healthomics-workflow-list-item
- name: WorkflowList
  property_count: 0
  slug: healthomics-workflow-list
- name: WorkflowListToken
  property_count: 0
  slug: healthomics-workflow-list-token
- name: WorkflowMain
  property_count: 0
  slug: healthomics-workflow-main
- name: WorkflowMetadataKey
  property_count: 0
  slug: healthomics-workflow-metadata-key
- name: WorkflowMetadata
  property_count: 0
  slug: healthomics-workflow-metadata
- name: WorkflowMetadataValue
  property_count: 0
  slug: healthomics-workflow-metadata-value
- name: WorkflowName
  property_count: 0
  slug: healthomics-workflow-name
- name: WorkflowParameterDescription
  property_count: 0
  slug: healthomics-workflow-parameter-description
- name: WorkflowParameterName
  property_count: 0
  slug: healthomics-workflow-parameter-name
- name: WorkflowParameter
  property_count: 2
  slug: healthomics-workflow-parameter
- name: WorkflowParameterTemplate
  property_count: 0
  slug: healthomics-workflow-parameter-template
- name: WorkflowRequestId
  property_count: 0
  slug: healthomics-workflow-request-id
- name: WorkflowStatusMessage
  property_count: 0
  slug: healthomics-workflow-status-message
- name: WorkflowStatus
  property_count: 0
  slug: healthomics-workflow-status
- name: WorkflowTimestamp
  property_count: 0
  slug: healthomics-workflow-timestamp
- name: WorkflowType
  property_count: 0
  slug: healthomics-workflow-type
json_structures:
- name: Healthomics Abort Multipart Read Set Upload Request Structure
  property_count: 0
  slug: healthomics-abort-multipart-read-set-upload-request-structure
- name: Healthomics Abort Multipart Read Set Upload Response Structure
  property_count: 0
  slug: healthomics-abort-multipart-read-set-upload-response-structure
- name: Healthomics Accelerators Structure
  property_count: 0
  slug: healthomics-accelerators-structure
- name: Healthomics Access Denied Exception Structure
  property_count: 0
  slug: healthomics-access-denied-exception-structure
- name: Healthomics Activate Read Set Filter Structure
  property_count: 3
  slug: healthomics-activate-read-set-filter-structure
- name: Healthomics Activate Read Set Job Item Structure
  property_count: 5
  slug: healthomics-activate-read-set-job-item-structure
- name: Healthomics Activate Read Set Job List Structure
  property_count: 0
  slug: healthomics-activate-read-set-job-list-structure
- name: Healthomics Activate Read Set Source Item Structure
  property_count: 3
  slug: healthomics-activate-read-set-source-item-structure
- name: Healthomics Activate Read Set Source List Structure
  property_count: 0
  slug: healthomics-activate-read-set-source-list-structure
- name: Healthomics Activation Job Id Structure
  property_count: 0
  slug: healthomics-activation-job-id-structure
- name: Healthomics Annotation Field Map Key String Structure
  property_count: 0
  slug: healthomics-annotation-field-map-key-string-structure
- name: Healthomics Annotation Field Map Structure
  property_count: 0
  slug: healthomics-annotation-field-map-structure
- name: Healthomics Annotation Field Map Value String Structure
  property_count: 0
  slug: healthomics-annotation-field-map-value-string-structure
- name: Healthomics Annotation Import Item Detail Structure
  property_count: 2
  slug: healthomics-annotation-import-item-detail-structure
- name: Healthomics Annotation Import Item Details Structure
  property_count: 0
  slug: healthomics-annotation-import-item-details-structure
- name: Healthomics Annotation Import Item Source Structure
  property_count: 1
  slug: healthomics-annotation-import-item-source-structure
- name: Healthomics Annotation Import Item Sources Structure
  property_count: 0
  slug: healthomics-annotation-import-item-sources-structure
- name: Healthomics Annotation Import Job Item Structure
  property_count: 9
  slug: healthomics-annotation-import-job-item-structure
- name: Healthomics Annotation Import Job Items Structure
  property_count: 0
  slug: healthomics-annotation-import-job-items-structure
- name: Healthomics Annotation Store Item Structure
  property_count: 12
  slug: healthomics-annotation-store-item-structure
- name: Healthomics Annotation Store Items Structure
  property_count: 0
  slug: healthomics-annotation-store-items-structure
- name: Healthomics Annotation Type Structure
  property_count: 0
  slug: healthomics-annotation-type-structure
- name: Healthomics Arn Structure
  property_count: 0
  slug: healthomics-arn-structure
- name: Healthomics Batch Delete Read Set Request Structure
  property_count: 1
  slug: healthomics-batch-delete-read-set-request-structure
- name: Healthomics Batch Delete Read Set Response Structure
  property_count: 1
  slug: healthomics-batch-delete-read-set-response-structure
- name: Healthomics Blob Structure
  property_count: 0
  slug: healthomics-blob-structure
- name: Healthomics Boolean Structure
  property_count: 0
  slug: healthomics-boolean-structure
- name: Healthomics Cancel Annotation Import Request Structure
  property_count: 0
  slug: healthomics-cancel-annotation-import-request-structure
- name: Healthomics Cancel Annotation Import Response Structure
  property_count: 0
  slug: healthomics-cancel-annotation-import-response-structure
- name: Healthomics Cancel Run Request Structure
  property_count: 0
  slug: healthomics-cancel-run-request-structure
- name: Healthomics Cancel Variant Import Request Structure
  property_count: 0
  slug: healthomics-cancel-variant-import-request-structure
- name: Healthomics Cancel Variant Import Response Structure
  property_count: 0
  slug: healthomics-cancel-variant-import-response-structure
- name: Healthomics Client Token Structure
  property_count: 0
  slug: healthomics-client-token-structure
- name: Healthomics Comment Char Structure
  property_count: 0
  slug: healthomics-comment-char-structure
- name: Healthomics Complete Multipart Read Set Upload Request Structure
  property_count: 1
  slug: healthomics-complete-multipart-read-set-upload-request-structure
- name: Healthomics Complete Multipart Read Set Upload Response Structure
  property_count: 1
  slug: healthomics-complete-multipart-read-set-upload-response-structure
- name: Healthomics Complete Read Set Upload Part List Item Part Number Integer Structure
  property_count: 0
  slug: healthomics-complete-read-set-upload-part-list-item-part-number-integer-structure
- name: Healthomics Complete Read Set Upload Part List Item Structure
  property_count: 3
  slug: healthomics-complete-read-set-upload-part-list-item-structure
- name: Healthomics Complete Read Set Upload Part List Structure
  property_count: 0
  slug: healthomics-complete-read-set-upload-part-list-structure
- name: Healthomics Completion Time Structure
  property_count: 0
  slug: healthomics-completion-time-structure
- name: Healthomics Conflict Exception Structure
  property_count: 0
  slug: healthomics-conflict-exception-structure
- name: Healthomics Create Annotation Store Request Name String Structure
  property_count: 0
  slug: healthomics-create-annotation-store-request-name-string-structure
- name: Healthomics Create Annotation Store Request Structure
  property_count: 7
  slug: healthomics-create-annotation-store-request-structure
- name: Healthomics Create Annotation Store Response Structure
  property_count: 7
  slug: healthomics-create-annotation-store-response-structure
- name: Healthomics Create Multipart Read Set Upload Request Structure
  property_count: 9
  slug: healthomics-create-multipart-read-set-upload-request-structure
- name: Healthomics Create Multipart Read Set Upload Response Structure
  property_count: 11
  slug: healthomics-create-multipart-read-set-upload-response-structure
- name: Healthomics Create Reference Store Request Structure
  property_count: 5
  slug: healthomics-create-reference-store-request-structure
- name: Healthomics Create Reference Store Response Structure
  property_count: 6
  slug: healthomics-create-reference-store-response-structure
- name: Healthomics Create Run Group Request Max Cpus Integer Structure
  property_count: 0
  slug: healthomics-create-run-group-request-max-cpus-integer-structure
- name: Healthomics Create Run Group Request Max Duration Integer Structure
  property_count: 0
  slug: healthomics-create-run-group-request-max-duration-integer-structure
- name: Healthomics Create Run Group Request Max Gpus Integer Structure
  property_count: 0
  slug: healthomics-create-run-group-request-max-gpus-integer-structure
- name: Healthomics Create Run Group Request Max Runs Integer Structure
  property_count: 0
  slug: healthomics-create-run-group-request-max-runs-integer-structure
- name: Healthomics Create Run Group Request Structure
  property_count: 7
  slug: healthomics-create-run-group-request-structure
- name: Healthomics Create Run Group Response Structure
  property_count: 3
  slug: healthomics-create-run-group-response-structure
- name: Healthomics Create Sequence Store Request Structure
  property_count: 6
  slug: healthomics-create-sequence-store-request-structure
- name: Healthomics Create Sequence Store Response Structure
  property_count: 7
  slug: healthomics-create-sequence-store-response-structure
- name: Healthomics Create Variant Store Request Name String Structure
  property_count: 0
  slug: healthomics-create-variant-store-request-name-string-structure
- name: Healthomics Create Variant Store Request Structure
  property_count: 5
  slug: healthomics-create-variant-store-request-structure
- name: Healthomics Create Variant Store Response Structure
  property_count: 5
  slug: healthomics-create-variant-store-response-structure
- name: Healthomics Create Workflow Request Storage Capacity Integer Structure
  property_count: 0
  slug: healthomics-create-workflow-request-storage-capacity-integer-structure
- name: Healthomics Create Workflow Request Structure
  property_count: 11
  slug: healthomics-create-workflow-request-structure
- name: Healthomics Create Workflow Response Structure
  property_count: 4
  slug: healthomics-create-workflow-response-structure
- name: Healthomics Creation Time Structure
  property_count: 0
  slug: healthomics-creation-time-structure
- name: Healthomics Creation Type Structure
  property_count: 0
  slug: healthomics-creation-type-structure
- name: Healthomics Delete Annotation Store Request Structure
  property_count: 0
  slug: healthomics-delete-annotation-store-request-structure
- name: Healthomics Delete Annotation Store Response Structure
  property_count: 1
  slug: healthomics-delete-annotation-store-response-structure
- name: Healthomics Delete Reference Request Structure
  property_count: 0
  slug: healthomics-delete-reference-request-structure
- name: Healthomics Delete Reference Response Structure
  property_count: 0
  slug: healthomics-delete-reference-response-structure
- name: Healthomics Delete Reference Store Request Structure
  property_count: 0
  slug: healthomics-delete-reference-store-request-structure
- name: Healthomics Delete Reference Store Response Structure
  property_count: 0
  slug: healthomics-delete-reference-store-response-structure
- name: Healthomics Delete Run Group Request Structure
  property_count: 0
  slug: healthomics-delete-run-group-request-structure
- name: Healthomics Delete Run Request Structure
  property_count: 0
  slug: healthomics-delete-run-request-structure
- name: Healthomics Delete Sequence Store Request Structure
  property_count: 0
  slug: healthomics-delete-sequence-store-request-structure
- name: Healthomics Delete Sequence Store Response Structure
  property_count: 0
  slug: healthomics-delete-sequence-store-response-structure
- name: Healthomics Delete Variant Store Request Structure
  property_count: 0
  slug: healthomics-delete-variant-store-request-structure
- name: Healthomics Delete Variant Store Response Structure
  property_count: 1
  slug: healthomics-delete-variant-store-response-structure
- name: Healthomics Delete Workflow Request Structure
  property_count: 0
  slug: healthomics-delete-workflow-request-structure
- name: Healthomics Encoding Structure
  property_count: 0
  slug: healthomics-encoding-structure
- name: Healthomics Encryption Type Structure
  property_count: 0
  slug: healthomics-encryption-type-structure
- name: Healthomics Escape Char Structure
  property_count: 0
  slug: healthomics-escape-char-structure
- name: Healthomics Escape Quotes Structure
  property_count: 0
  slug: healthomics-escape-quotes-structure
- name: Healthomics Export Job Id Structure
  property_count: 0
  slug: healthomics-export-job-id-structure
- name: Healthomics Export Read Set Detail List Structure
  property_count: 0
  slug: healthomics-export-read-set-detail-list-structure
- name: Healthomics Export Read Set Detail Structure
  property_count: 3
  slug: healthomics-export-read-set-detail-structure
- name: Healthomics Export Read Set Filter Structure
  property_count: 3
  slug: healthomics-export-read-set-filter-structure
- name: Healthomics Export Read Set Job Detail List Structure
  property_count: 0
  slug: healthomics-export-read-set-job-detail-list-structure
- name: Healthomics Export Read Set Job Detail Structure
  property_count: 6
  slug: healthomics-export-read-set-job-detail-structure
- name: Healthomics Export Read Set Structure
  property_count: 1
  slug: healthomics-export-read-set-structure
- name: Healthomics File Information Content Length Long Structure
  property_count: 0
  slug: healthomics-file-information-content-length-long-structure
- name: Healthomics File Information Part Size Long Structure
  property_count: 0
  slug: healthomics-file-information-part-size-long-structure
- name: Healthomics File Information Structure
  property_count: 3
  slug: healthomics-file-information-structure
- name: Healthomics File Information Total Parts Integer Structure
  property_count: 0
  slug: healthomics-file-information-total-parts-integer-structure
- name: Healthomics File Type Structure
  property_count: 0
  slug: healthomics-file-type-structure
- name: Healthomics Format Options Structure
  property_count: 2
  slug: healthomics-format-options-structure
- name: Healthomics Format To Header Key Structure
  property_count: 0
  slug: healthomics-format-to-header-key-structure
- name: Healthomics Format To Header Structure
  property_count: 0
  slug: healthomics-format-to-header-structure
- name: Healthomics Format To Header Value String Structure
  property_count: 0
  slug: healthomics-format-to-header-value-string-structure
- name: Healthomics Generated From Structure
  property_count: 0
  slug: healthomics-generated-from-structure
- name: Healthomics Get Annotation Import Request Structure
  property_count: 0
  slug: healthomics-get-annotation-import-request-structure
- name: Healthomics Get Annotation Import Response Structure
  property_count: 12
  slug: healthomics-get-annotation-import-response-structure
- name: Healthomics Get Annotation Store Request Structure
  property_count: 0
  slug: healthomics-get-annotation-store-request-structure
- name: Healthomics Get Annotation Store Response Structure
  property_count: 14
  slug: healthomics-get-annotation-store-response-structure
- name: Healthomics Get Read Set Activation Job Request Structure
  property_count: 0
  slug: healthomics-get-read-set-activation-job-request-structure
- name: Healthomics Get Read Set Activation Job Response Structure
  property_count: 7
  slug: healthomics-get-read-set-activation-job-response-structure
- name: Healthomics Get Read Set Export Job Request Structure
  property_count: 0
  slug: healthomics-get-read-set-export-job-request-structure
- name: Healthomics Get Read Set Export Job Response Structure
  property_count: 8
  slug: healthomics-get-read-set-export-job-response-structure
- name: Healthomics Get Read Set Import Job Request Structure
  property_count: 0
  slug: healthomics-get-read-set-import-job-request-structure
- name: Healthomics Get Read Set Import Job Response Structure
  property_count: 8
  slug: healthomics-get-read-set-import-job-response-structure
- name: Healthomics Get Read Set Metadata Request Structure
  property_count: 0
  slug: healthomics-get-read-set-metadata-request-structure
- name: Healthomics Get Read Set Metadata Response Structure
  property_count: 15
  slug: healthomics-get-read-set-metadata-response-structure
- name: Healthomics Get Read Set Request Part Number Integer Structure
  property_count: 0
  slug: healthomics-get-read-set-request-part-number-integer-structure
- name: Healthomics Get Read Set Request Structure
  property_count: 0
  slug: healthomics-get-read-set-request-structure
- name: Healthomics Get Read Set Response Structure
  property_count: 1
  slug: healthomics-get-read-set-response-structure
- name: Healthomics Get Reference Import Job Request Structure
  property_count: 0
  slug: healthomics-get-reference-import-job-request-structure
- name: Healthomics Get Reference Import Job Response Structure
  property_count: 8
  slug: healthomics-get-reference-import-job-response-structure
- name: Healthomics Get Reference Metadata Request Structure
  property_count: 0
  slug: healthomics-get-reference-metadata-request-structure
- name: Healthomics Get Reference Metadata Response Structure
  property_count: 10
  slug: healthomics-get-reference-metadata-response-structure
- name: Healthomics Get Reference Request Part Number Integer Structure
  property_count: 0
  slug: healthomics-get-reference-request-part-number-integer-structure
- name: Healthomics Get Reference Request Structure
  property_count: 0
  slug: healthomics-get-reference-request-structure
- name: Healthomics Get Reference Response Structure
  property_count: 1
  slug: healthomics-get-reference-response-structure
- name: Healthomics Get Reference Store Request Structure
  property_count: 0
  slug: healthomics-get-reference-store-request-structure
- name: Healthomics Get Reference Store Response Structure
  property_count: 6
  slug: healthomics-get-reference-store-response-structure
- name: Healthomics Get Run Group Request Structure
  property_count: 0
  slug: healthomics-get-run-group-request-structure
- name: Healthomics Get Run Group Response Max Cpus Integer Structure
  property_count: 0
  slug: healthomics-get-run-group-response-max-cpus-integer-structure
- name: Healthomics Get Run Group Response Max Duration Integer Structure
  property_count: 0
  slug: healthomics-get-run-group-response-max-duration-integer-structure
- name: Healthomics Get Run Group Response Max Gpus Integer Structure
  property_count: 0
  slug: healthomics-get-run-group-response-max-gpus-integer-structure
- name: Healthomics Get Run Group Response Max Runs Integer Structure
  property_count: 0
  slug: healthomics-get-run-group-response-max-runs-integer-structure
- name: Healthomics Get Run Group Response Structure
  property_count: 9
  slug: healthomics-get-run-group-response-structure
- name: Healthomics Get Run Request Structure
  property_count: 0
  slug: healthomics-get-run-request-structure
- name: Healthomics Get Run Response Priority Integer Structure
  property_count: 0
  slug: healthomics-get-run-response-priority-integer-structure
- name: Healthomics Get Run Response Storage Capacity Integer Structure
  property_count: 0
  slug: healthomics-get-run-response-storage-capacity-integer-structure
- name: Healthomics Get Run Response Structure
  property_count: 24
  slug: healthomics-get-run-response-structure
- name: Healthomics Get Run Task Request Structure
  property_count: 0
  slug: healthomics-get-run-task-request-structure
- name: Healthomics Get Run Task Response Cpus Integer Structure
  property_count: 0
  slug: healthomics-get-run-task-response-cpus-integer-structure
- name: Healthomics Get Run Task Response Gpus Integer Structure
  property_count: 0
  slug: healthomics-get-run-task-response-gpus-integer-structure
- name: Healthomics Get Run Task Response Memory Integer Structure
  property_count: 0
  slug: healthomics-get-run-task-response-memory-integer-structure
- name: Healthomics Get Run Task Response Structure
  property_count: 11
  slug: healthomics-get-run-task-response-structure
- name: Healthomics Get Sequence Store Request Structure
  property_count: 0
  slug: healthomics-get-sequence-store-request-structure
- name: Healthomics Get Sequence Store Response Structure
  property_count: 7
  slug: healthomics-get-sequence-store-response-structure
- name: Healthomics Get Variant Import Request Structure
  property_count: 0
  slug: healthomics-get-variant-import-request-structure
- name: Healthomics Get Variant Import Response Structure
  property_count: 11
  slug: healthomics-get-variant-import-response-structure
- name: Healthomics Get Variant Store Request Structure
  property_count: 0
  slug: healthomics-get-variant-store-request-structure
- name: Healthomics Get Variant Store Response Structure
  property_count: 12
  slug: healthomics-get-variant-store-response-structure
- name: Healthomics Get Workflow Request Structure
  property_count: 0
  slug: healthomics-get-workflow-request-structure
- name: Healthomics Get Workflow Response Storage Capacity Integer Structure
  property_count: 0
  slug: healthomics-get-workflow-response-storage-capacity-integer-structure
- name: Healthomics Get Workflow Response Structure
  property_count: 17
  slug: healthomics-get-workflow-response-structure
- name: Healthomics Header Structure
  property_count: 0
  slug: healthomics-header-structure
- name: Healthomics Import Job Id Structure
  property_count: 0
  slug: healthomics-import-job-id-structure
- name: Healthomics Import Read Set Filter Structure
  property_count: 3
  slug: healthomics-import-read-set-filter-structure
- name: Healthomics Import Read Set Job Item Structure
  property_count: 6
  slug: healthomics-import-read-set-job-item-structure
- name: Healthomics Import Read Set Job List Structure
  property_count: 0
  slug: healthomics-import-read-set-job-list-structure
- name: Healthomics Import Read Set Source Item Structure
  property_count: 11
  slug: healthomics-import-read-set-source-item-structure
- name: Healthomics Import Read Set Source List Structure
  property_count: 0
  slug: healthomics-import-read-set-source-list-structure
- name: Healthomics Import Reference Filter Structure
  property_count: 3
  slug: healthomics-import-reference-filter-structure
- name: Healthomics Import Reference Job Item Structure
  property_count: 6
  slug: healthomics-import-reference-job-item-structure
- name: Healthomics Import Reference Job List Structure
  property_count: 0
  slug: healthomics-import-reference-job-list-structure
- name: Healthomics Import Reference Source Item Structure
  property_count: 6
  slug: healthomics-import-reference-source-item-structure
- name: Healthomics Import Reference Source List Structure
  property_count: 0
  slug: healthomics-import-reference-source-list-structure
- name: Healthomics Internal Server Exception Structure
  property_count: 0
  slug: healthomics-internal-server-exception-structure
- name: Healthomics Job Status Message Structure
  property_count: 0
  slug: healthomics-job-status-message-structure
- name: Healthomics Job Status Msg Structure
  property_count: 0
  slug: healthomics-job-status-msg-structure
- name: Healthomics Job Status Structure
  property_count: 0
  slug: healthomics-job-status-structure
- name: Healthomics Line Sep Structure
  property_count: 0
  slug: healthomics-line-sep-structure
- name: Healthomics List Annotation Import Jobs Filter Structure
  property_count: 2
  slug: healthomics-list-annotation-import-jobs-filter-structure
- name: Healthomics List Annotation Import Jobs Request Ids List Structure
  property_count: 0
  slug: healthomics-list-annotation-import-jobs-request-ids-list-structure
- name: Healthomics List Annotation Import Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-annotation-import-jobs-request-max-results-integer-structure
- name: Healthomics List Annotation Import Jobs Request Next Token String Structure
  property_count: 0
  slug: healthomics-list-annotation-import-jobs-request-next-token-string-structure
- name: Healthomics List Annotation Import Jobs Request Structure
  property_count: 2
  slug: healthomics-list-annotation-import-jobs-request-structure
- name: Healthomics List Annotation Import Jobs Response Structure
  property_count: 2
  slug: healthomics-list-annotation-import-jobs-response-structure
- name: Healthomics List Annotation Stores Filter Structure
  property_count: 1
  slug: healthomics-list-annotation-stores-filter-structure
- name: Healthomics List Annotation Stores Request Ids List Structure
  property_count: 0
  slug: healthomics-list-annotation-stores-request-ids-list-structure
- name: Healthomics List Annotation Stores Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-annotation-stores-request-max-results-integer-structure
- name: Healthomics List Annotation Stores Request Next Token String Structure
  property_count: 0
  slug: healthomics-list-annotation-stores-request-next-token-string-structure
- name: Healthomics List Annotation Stores Request Structure
  property_count: 2
  slug: healthomics-list-annotation-stores-request-structure
- name: Healthomics List Annotation Stores Response Structure
  property_count: 2
  slug: healthomics-list-annotation-stores-response-structure
- name: Healthomics List Multipart Read Set Uploads Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-multipart-read-set-uploads-request-max-results-integer-structure
- name: Healthomics List Multipart Read Set Uploads Request Structure
  property_count: 0
  slug: healthomics-list-multipart-read-set-uploads-request-structure
- name: Healthomics List Multipart Read Set Uploads Response Structure
  property_count: 2
  slug: healthomics-list-multipart-read-set-uploads-response-structure
- name: Healthomics List Read Set Activation Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-read-set-activation-jobs-request-max-results-integer-structure
- name: Healthomics List Read Set Activation Jobs Request Structure
  property_count: 1
  slug: healthomics-list-read-set-activation-jobs-request-structure
- name: Healthomics List Read Set Activation Jobs Response Structure
  property_count: 2
  slug: healthomics-list-read-set-activation-jobs-response-structure
- name: Healthomics List Read Set Export Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-read-set-export-jobs-request-max-results-integer-structure
- name: Healthomics List Read Set Export Jobs Request Structure
  property_count: 1
  slug: healthomics-list-read-set-export-jobs-request-structure
- name: Healthomics List Read Set Export Jobs Response Structure
  property_count: 2
  slug: healthomics-list-read-set-export-jobs-response-structure
- name: Healthomics List Read Set Import Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-read-set-import-jobs-request-max-results-integer-structure
- name: Healthomics List Read Set Import Jobs Request Structure
  property_count: 1
  slug: healthomics-list-read-set-import-jobs-request-structure
- name: Healthomics List Read Set Import Jobs Response Structure
  property_count: 2
  slug: healthomics-list-read-set-import-jobs-response-structure
- name: Healthomics List Read Set Upload Parts Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-read-set-upload-parts-request-max-results-integer-structure
- name: Healthomics List Read Set Upload Parts Request Structure
  property_count: 2
  slug: healthomics-list-read-set-upload-parts-request-structure
- name: Healthomics List Read Set Upload Parts Response Structure
  property_count: 2
  slug: healthomics-list-read-set-upload-parts-response-structure
- name: Healthomics List Read Sets Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-read-sets-request-max-results-integer-structure
- name: Healthomics List Read Sets Request Structure
  property_count: 1
  slug: healthomics-list-read-sets-request-structure
- name: Healthomics List Read Sets Response Structure
  property_count: 2
  slug: healthomics-list-read-sets-response-structure
- name: Healthomics List Reference Import Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-reference-import-jobs-request-max-results-integer-structure
- name: Healthomics List Reference Import Jobs Request Structure
  property_count: 1
  slug: healthomics-list-reference-import-jobs-request-structure
- name: Healthomics List Reference Import Jobs Response Structure
  property_count: 2
  slug: healthomics-list-reference-import-jobs-response-structure
- name: Healthomics List Reference Stores Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-reference-stores-request-max-results-integer-structure
- name: Healthomics List Reference Stores Request Structure
  property_count: 1
  slug: healthomics-list-reference-stores-request-structure
- name: Healthomics List Reference Stores Response Structure
  property_count: 2
  slug: healthomics-list-reference-stores-response-structure
- name: Healthomics List References Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-references-request-max-results-integer-structure
- name: Healthomics List References Request Structure
  property_count: 1
  slug: healthomics-list-references-request-structure
- name: Healthomics List References Response Structure
  property_count: 2
  slug: healthomics-list-references-response-structure
- name: Healthomics List Run Groups Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-run-groups-request-max-results-integer-structure
- name: Healthomics List Run Groups Request Structure
  property_count: 0
  slug: healthomics-list-run-groups-request-structure
- name: Healthomics List Run Groups Response Structure
  property_count: 2
  slug: healthomics-list-run-groups-response-structure
- name: Healthomics List Run Tasks Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-run-tasks-request-max-results-integer-structure
- name: Healthomics List Run Tasks Request Structure
  property_count: 0
  slug: healthomics-list-run-tasks-request-structure
- name: Healthomics List Run Tasks Response Structure
  property_count: 2
  slug: healthomics-list-run-tasks-response-structure
- name: Healthomics List Runs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-runs-request-max-results-integer-structure
- name: Healthomics List Runs Request Structure
  property_count: 0
  slug: healthomics-list-runs-request-structure
- name: Healthomics List Runs Response Structure
  property_count: 2
  slug: healthomics-list-runs-response-structure
- name: Healthomics List Sequence Stores Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-sequence-stores-request-max-results-integer-structure
- name: Healthomics List Sequence Stores Request Structure
  property_count: 1
  slug: healthomics-list-sequence-stores-request-structure
- name: Healthomics List Sequence Stores Response Structure
  property_count: 2
  slug: healthomics-list-sequence-stores-response-structure
- name: Healthomics List Tags For Resource Request Structure
  property_count: 0
  slug: healthomics-list-tags-for-resource-request-structure
- name: Healthomics List Tags For Resource Response Structure
  property_count: 1
  slug: healthomics-list-tags-for-resource-response-structure
- name: Healthomics List Variant Import Jobs Filter Structure
  property_count: 2
  slug: healthomics-list-variant-import-jobs-filter-structure
- name: Healthomics List Variant Import Jobs Request Ids List Structure
  property_count: 0
  slug: healthomics-list-variant-import-jobs-request-ids-list-structure
- name: Healthomics List Variant Import Jobs Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-variant-import-jobs-request-max-results-integer-structure
- name: Healthomics List Variant Import Jobs Request Next Token String Structure
  property_count: 0
  slug: healthomics-list-variant-import-jobs-request-next-token-string-structure
- name: Healthomics List Variant Import Jobs Request Structure
  property_count: 2
  slug: healthomics-list-variant-import-jobs-request-structure
- name: Healthomics List Variant Import Jobs Response Structure
  property_count: 2
  slug: healthomics-list-variant-import-jobs-response-structure
- name: Healthomics List Variant Stores Filter Structure
  property_count: 1
  slug: healthomics-list-variant-stores-filter-structure
- name: Healthomics List Variant Stores Request Ids List Structure
  property_count: 0
  slug: healthomics-list-variant-stores-request-ids-list-structure
- name: Healthomics List Variant Stores Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-variant-stores-request-max-results-integer-structure
- name: Healthomics List Variant Stores Request Next Token String Structure
  property_count: 0
  slug: healthomics-list-variant-stores-request-next-token-string-structure
- name: Healthomics List Variant Stores Request Structure
  property_count: 2
  slug: healthomics-list-variant-stores-request-structure
- name: Healthomics List Variant Stores Response Structure
  property_count: 2
  slug: healthomics-list-variant-stores-response-structure
- name: Healthomics List Workflows Request Max Results Integer Structure
  property_count: 0
  slug: healthomics-list-workflows-request-max-results-integer-structure
- name: Healthomics List Workflows Request Structure
  property_count: 0
  slug: healthomics-list-workflows-request-structure
- name: Healthomics List Workflows Response Structure
  property_count: 2
  slug: healthomics-list-workflows-response-structure
- name: Healthomics Long Structure
  property_count: 0
  slug: healthomics-long-structure
- name: Healthomics Md5 Structure
  property_count: 0
  slug: healthomics-md5-structure
- name: Healthomics Multipart Read Set Upload List Item Structure
  property_count: 11
  slug: healthomics-multipart-read-set-upload-list-item-structure
- name: Healthomics Multipart Read Set Upload List Structure
  property_count: 0
  slug: healthomics-multipart-read-set-upload-list-structure
- name: Healthomics Next Token Structure
  property_count: 0
  slug: healthomics-next-token-structure
- name: Healthomics Not Supported Operation Exception Structure
  property_count: 0
  slug: healthomics-not-supported-operation-exception-structure
- name: Healthomics Primitive Boolean Structure
  property_count: 0
  slug: healthomics-primitive-boolean-structure
- name: Healthomics Quote All Structure
  property_count: 0
  slug: healthomics-quote-all-structure
- name: Healthomics Quote Structure
  property_count: 0
  slug: healthomics-quote-structure
- name: Healthomics Range Not Satisfiable Exception Structure
  property_count: 0
  slug: healthomics-range-not-satisfiable-exception-structure
- name: Healthomics Range Structure
  property_count: 0
  slug: healthomics-range-structure
- name: Healthomics Read Options Structure
  property_count: 9
  slug: healthomics-read-options-structure
- name: Healthomics Read Set Activation Job Item Status Structure
  property_count: 0
  slug: healthomics-read-set-activation-job-item-status-structure
- name: Healthomics Read Set Activation Job Status Structure
  property_count: 0
  slug: healthomics-read-set-activation-job-status-structure
- name: Healthomics Read Set Arn Structure
  property_count: 0
  slug: healthomics-read-set-arn-structure
- name: Healthomics Read Set Batch Error List Structure
  property_count: 0
  slug: healthomics-read-set-batch-error-list-structure
- name: Healthomics Read Set Batch Error Structure
  property_count: 3
  slug: healthomics-read-set-batch-error-structure
- name: Healthomics Read Set Description Structure
  property_count: 0
  slug: healthomics-read-set-description-structure
- name: Healthomics Read Set Export Job Item Status Structure
  property_count: 0
  slug: healthomics-read-set-export-job-item-status-structure
- name: Healthomics Read Set Export Job Status Structure
  property_count: 0
  slug: healthomics-read-set-export-job-status-structure
- name: Healthomics Read Set File Structure
  property_count: 0
  slug: healthomics-read-set-file-structure
- name: Healthomics Read Set Files Structure
  property_count: 3
  slug: healthomics-read-set-files-structure
- name: Healthomics Read Set Filter Structure
  property_count: 9
  slug: healthomics-read-set-filter-structure
- name: Healthomics Read Set Id List Structure
  property_count: 0
  slug: healthomics-read-set-id-list-structure
- name: Healthomics Read Set Id Structure
  property_count: 0
  slug: healthomics-read-set-id-structure
- name: Healthomics Read Set Import Job Item Status Structure
  property_count: 0
  slug: healthomics-read-set-import-job-item-status-structure
- name: Healthomics Read Set Import Job Status Structure
  property_count: 0
  slug: healthomics-read-set-import-job-status-structure
- name: Healthomics Read Set List Item Structure
  property_count: 14
  slug: healthomics-read-set-list-item-structure
- name: Healthomics Read Set List Structure
  property_count: 0
  slug: healthomics-read-set-list-structure
- name: Healthomics Read Set Name Structure
  property_count: 0
  slug: healthomics-read-set-name-structure
- name: Healthomics Read Set Part Source Structure
  property_count: 0
  slug: healthomics-read-set-part-source-structure
- name: Healthomics Read Set Part Streaming Blob Structure
  property_count: 0
  slug: healthomics-read-set-part-streaming-blob-structure
- name: Healthomics Read Set Status Message Structure
  property_count: 0
  slug: healthomics-read-set-status-message-structure
- name: Healthomics Read Set Status Structure
  property_count: 0
  slug: healthomics-read-set-status-structure
- name: Healthomics Read Set Streaming Blob Structure
  property_count: 0
  slug: healthomics-read-set-streaming-blob-structure
- name: Healthomics Read Set Upload Part List Filter Structure
  property_count: 2
  slug: healthomics-read-set-upload-part-list-filter-structure
- name: Healthomics Read Set Upload Part List Item Part Number Integer Structure
  property_count: 0
  slug: healthomics-read-set-upload-part-list-item-part-number-integer-structure
- name: Healthomics Read Set Upload Part List Item Part Size Long Structure
  property_count: 0
  slug: healthomics-read-set-upload-part-list-item-part-size-long-structure
- name: Healthomics Read Set Upload Part List Item Structure
  property_count: 6
  slug: healthomics-read-set-upload-part-list-item-structure
- name: Healthomics Read Set Upload Part List Structure
  property_count: 0
  slug: healthomics-read-set-upload-part-list-structure
- name: Healthomics Reference Arn Structure
  property_count: 0
  slug: healthomics-reference-arn-structure
- name: Healthomics Reference Description Structure
  property_count: 0
  slug: healthomics-reference-description-structure
- name: Healthomics Reference File Structure
  property_count: 0
  slug: healthomics-reference-file-structure
- name: Healthomics Reference Files Structure
  property_count: 2
  slug: healthomics-reference-files-structure
- name: Healthomics Reference Filter Structure
  property_count: 4
  slug: healthomics-reference-filter-structure
- name: Healthomics Reference Id Structure
  property_count: 0
  slug: healthomics-reference-id-structure
- name: Healthomics Reference Import Job Item Status Structure
  property_count: 0
  slug: healthomics-reference-import-job-item-status-structure
- name: Healthomics Reference Import Job Status Structure
  property_count: 0
  slug: healthomics-reference-import-job-status-structure
- name: Healthomics Reference Item Structure
  property_count: 1
  slug: healthomics-reference-item-structure
- name: Healthomics Reference List Item Structure
  property_count: 9
  slug: healthomics-reference-list-item-structure
- name: Healthomics Reference List Structure
  property_count: 0
  slug: healthomics-reference-list-structure
- name: Healthomics Reference Name Structure
  property_count: 0
  slug: healthomics-reference-name-structure
- name: Healthomics Reference Status Structure
  property_count: 0
  slug: healthomics-reference-status-structure
- name: Healthomics Reference Store Arn Structure
  property_count: 0
  slug: healthomics-reference-store-arn-structure
- name: Healthomics Reference Store Description Structure
  property_count: 0
  slug: healthomics-reference-store-description-structure
- name: Healthomics Reference Store Detail List Structure
  property_count: 0
  slug: healthomics-reference-store-detail-list-structure
- name: Healthomics Reference Store Detail Structure
  property_count: 6
  slug: healthomics-reference-store-detail-structure
- name: Healthomics Reference Store Filter Structure
  property_count: 3
  slug: healthomics-reference-store-filter-structure
- name: Healthomics Reference Store Id Structure
  property_count: 0
  slug: healthomics-reference-store-id-structure
- name: Healthomics Reference Store Name Structure
  property_count: 0
  slug: healthomics-reference-store-name-structure
- name: Healthomics Reference Streaming Blob Structure
  property_count: 0
  slug: healthomics-reference-streaming-blob-structure
- name: Healthomics Request Timeout Exception Structure
  property_count: 0
  slug: healthomics-request-timeout-exception-structure
- name: Healthomics Resource Id Structure
  property_count: 0
  slug: healthomics-resource-id-structure
- name: Healthomics Resource Identifier Structure
  property_count: 0
  slug: healthomics-resource-identifier-structure
- name: Healthomics Resource Not Found Exception Structure
  property_count: 0
  slug: healthomics-resource-not-found-exception-structure
- name: Healthomics Role Arn Structure
  property_count: 0
  slug: healthomics-role-arn-structure
- name: Healthomics Run Arn Structure
  property_count: 0
  slug: healthomics-run-arn-structure
- name: Healthomics Run Export List Structure
  property_count: 0
  slug: healthomics-run-export-list-structure
- name: Healthomics Run Export Structure
  property_count: 0
  slug: healthomics-run-export-structure
- name: Healthomics Run Group Arn Structure
  property_count: 0
  slug: healthomics-run-group-arn-structure
- name: Healthomics Run Group Id Structure
  property_count: 0
  slug: healthomics-run-group-id-structure
- name: Healthomics Run Group List Item Max Cpus Integer Structure
  property_count: 0
  slug: healthomics-run-group-list-item-max-cpus-integer-structure
- name: Healthomics Run Group List Item Max Duration Integer Structure
  property_count: 0
  slug: healthomics-run-group-list-item-max-duration-integer-structure
- name: Healthomics Run Group List Item Max Gpus Integer Structure
  property_count: 0
  slug: healthomics-run-group-list-item-max-gpus-integer-structure
- name: Healthomics Run Group List Item Max Runs Integer Structure
  property_count: 0
  slug: healthomics-run-group-list-item-max-runs-integer-structure
- name: Healthomics Run Group List Item Structure
  property_count: 8
  slug: healthomics-run-group-list-item-structure
- name: Healthomics Run Group List Structure
  property_count: 0
  slug: healthomics-run-group-list-structure
- name: Healthomics Run Group List Token Structure
  property_count: 0
  slug: healthomics-run-group-list-token-structure
- name: Healthomics Run Group Name Structure
  property_count: 0
  slug: healthomics-run-group-name-structure
- name: Healthomics Run Group Request Id Structure
  property_count: 0
  slug: healthomics-run-group-request-id-structure
- name: Healthomics Run Group Timestamp Structure
  property_count: 0
  slug: healthomics-run-group-timestamp-structure
- name: Healthomics Run Id Structure
  property_count: 0
  slug: healthomics-run-id-structure
- name: Healthomics Run Left Normalization Structure
  property_count: 0
  slug: healthomics-run-left-normalization-structure
- name: Healthomics Run List Item Priority Integer Structure
  property_count: 0
  slug: healthomics-run-list-item-priority-integer-structure
- name: Healthomics Run List Item Storage Capacity Integer Structure
  property_count: 0
  slug: healthomics-run-list-item-storage-capacity-integer-structure
- name: Healthomics Run List Item Structure
  property_count: 10
  slug: healthomics-run-list-item-structure
- name: Healthomics Run List Structure
  property_count: 0
  slug: healthomics-run-list-structure
- name: Healthomics Run List Token Structure
  property_count: 0
  slug: healthomics-run-list-token-structure
- name: Healthomics Run Log Level Structure
  property_count: 0
  slug: healthomics-run-log-level-structure
- name: Healthomics Run Name Structure
  property_count: 0
  slug: healthomics-run-name-structure
- name: Healthomics Run Output Uri Structure
  property_count: 0
  slug: healthomics-run-output-uri-structure
- name: Healthomics Run Parameters Structure
  property_count: 0
  slug: healthomics-run-parameters-structure
- name: Healthomics Run Request Id Structure
  property_count: 0
  slug: healthomics-run-request-id-structure
- name: Healthomics Run Resource Digest Key Structure
  property_count: 0
  slug: healthomics-run-resource-digest-key-structure
- name: Healthomics Run Resource Digest Structure
  property_count: 0
  slug: healthomics-run-resource-digest-structure
- name: Healthomics Run Resource Digests Structure
  property_count: 0
  slug: healthomics-run-resource-digests-structure
- name: Healthomics Run Role Arn Structure
  property_count: 0
  slug: healthomics-run-role-arn-structure
- name: Healthomics Run Started By Structure
  property_count: 0
  slug: healthomics-run-started-by-structure
- name: Healthomics Run Status Message Structure
  property_count: 0
  slug: healthomics-run-status-message-structure
- name: Healthomics Run Status Structure
  property_count: 0
  slug: healthomics-run-status-structure
- name: Healthomics Run Timestamp Structure
  property_count: 0
  slug: healthomics-run-timestamp-structure
- name: Healthomics S3 Destination Structure
  property_count: 0
  slug: healthomics-s3-destination-structure
- name: Healthomics S3 Uri Structure
  property_count: 0
  slug: healthomics-s3-uri-structure
- name: Healthomics Sample Id Structure
  property_count: 0
  slug: healthomics-sample-id-structure
- name: Healthomics Schema Item Key String Structure
  property_count: 0
  slug: healthomics-schema-item-key-string-structure
- name: Healthomics Schema Item Structure
  property_count: 0
  slug: healthomics-schema-item-structure
- name: Healthomics Schema Value Type Structure
  property_count: 0
  slug: healthomics-schema-value-type-structure
- name: Healthomics Separator Structure
  property_count: 0
  slug: healthomics-separator-structure
- name: Healthomics Sequence Information Structure
  property_count: 4
  slug: healthomics-sequence-information-structure
- name: Healthomics Sequence Store Arn Structure
  property_count: 0
  slug: healthomics-sequence-store-arn-structure
- name: Healthomics Sequence Store Description Structure
  property_count: 0
  slug: healthomics-sequence-store-description-structure
- name: Healthomics Sequence Store Detail List Structure
  property_count: 0
  slug: healthomics-sequence-store-detail-list-structure
- name: Healthomics Sequence Store Detail Structure
  property_count: 7
  slug: healthomics-sequence-store-detail-structure
- name: Healthomics Sequence Store Filter Structure
  property_count: 3
  slug: healthomics-sequence-store-filter-structure
- name: Healthomics Sequence Store Id Structure
  property_count: 0
  slug: healthomics-sequence-store-id-structure
- name: Healthomics Sequence Store Name Structure
  property_count: 0
  slug: healthomics-sequence-store-name-structure
- name: Healthomics Service Quota Exceeded Exception Structure
  property_count: 0
  slug: healthomics-service-quota-exceeded-exception-structure
- name: Healthomics Source Files Structure
  property_count: 2
  slug: healthomics-source-files-structure
- name: Healthomics Sse Config Key Arn String Structure
  property_count: 0
  slug: healthomics-sse-config-key-arn-string-structure
- name: Healthomics Sse Config Structure
  property_count: 2
  slug: healthomics-sse-config-structure
- name: Healthomics Start Annotation Import Request Structure
  property_count: 6
  slug: healthomics-start-annotation-import-request-structure
- name: Healthomics Start Annotation Import Response Structure
  property_count: 1
  slug: healthomics-start-annotation-import-response-structure
- name: Healthomics Start Read Set Activation Job Request Sources List Structure
  property_count: 0
  slug: healthomics-start-read-set-activation-job-request-sources-list-structure
- name: Healthomics Start Read Set Activation Job Request Structure
  property_count: 2
  slug: healthomics-start-read-set-activation-job-request-structure
- name: Healthomics Start Read Set Activation Job Response Structure
  property_count: 4
  slug: healthomics-start-read-set-activation-job-response-structure
- name: Healthomics Start Read Set Activation Job Source Item Structure
  property_count: 1
  slug: healthomics-start-read-set-activation-job-source-item-structure
- name: Healthomics Start Read Set Export Job Request Sources List Structure
  property_count: 0
  slug: healthomics-start-read-set-export-job-request-sources-list-structure
- name: Healthomics Start Read Set Export Job Request Structure
  property_count: 4
  slug: healthomics-start-read-set-export-job-request-structure
- name: Healthomics Start Read Set Export Job Response Structure
  property_count: 5
  slug: healthomics-start-read-set-export-job-response-structure
- name: Healthomics Start Read Set Import Job Request Sources List Structure
  property_count: 0
  slug: healthomics-start-read-set-import-job-request-sources-list-structure
- name: Healthomics Start Read Set Import Job Request Structure
  property_count: 3
  slug: healthomics-start-read-set-import-job-request-structure
- name: Healthomics Start Read Set Import Job Response Structure
  property_count: 5
  slug: healthomics-start-read-set-import-job-response-structure
- name: Healthomics Start Read Set Import Job Source Item Structure
  property_count: 9
  slug: healthomics-start-read-set-import-job-source-item-structure
- name: Healthomics Start Reference Import Job Request Sources List Structure
  property_count: 0
  slug: healthomics-start-reference-import-job-request-sources-list-structure
- name: Healthomics Start Reference Import Job Request Structure
  property_count: 3
  slug: healthomics-start-reference-import-job-request-structure
- name: Healthomics Start Reference Import Job Response Structure
  property_count: 5
  slug: healthomics-start-reference-import-job-response-structure
- name: Healthomics Start Reference Import Job Source Item Structure
  property_count: 4
  slug: healthomics-start-reference-import-job-source-item-structure
- name: Healthomics Start Run Request Priority Integer Structure
  property_count: 0
  slug: healthomics-start-run-request-priority-integer-structure
- name: Healthomics Start Run Request Storage Capacity Integer Structure
  property_count: 0
  slug: healthomics-start-run-request-storage-capacity-integer-structure
- name: Healthomics Start Run Request Structure
  property_count: 13
  slug: healthomics-start-run-request-structure
- name: Healthomics Start Run Response Structure
  property_count: 4
  slug: healthomics-start-run-response-structure
- name: Healthomics Start Variant Import Request Structure
  property_count: 5
  slug: healthomics-start-variant-import-request-structure
- name: Healthomics Start Variant Import Response Structure
  property_count: 1
  slug: healthomics-start-variant-import-response-structure
- name: Healthomics Status Message Structure
  property_count: 0
  slug: healthomics-status-message-structure
- name: Healthomics Store Description Structure
  property_count: 0
  slug: healthomics-store-description-structure
- name: Healthomics Store Format Structure
  property_count: 0
  slug: healthomics-store-format-structure
- name: Healthomics Store Name Structure
  property_count: 0
  slug: healthomics-store-name-structure
- name: Healthomics Store Options Structure
  property_count: 1
  slug: healthomics-store-options-structure
- name: Healthomics Store Status Structure
  property_count: 0
  slug: healthomics-store-status-structure
- name: Healthomics String Structure
  property_count: 0
  slug: healthomics-string-structure
- name: Healthomics Subject Id Structure
  property_count: 0
  slug: healthomics-subject-id-structure
- name: Healthomics Synthetic Timestamp_Date_Time Structure
  property_count: 0
  slug: healthomics-synthetic-timestamp_date_time-structure
- name: Healthomics Tag Arn Structure
  property_count: 0
  slug: healthomics-tag-arn-structure
- name: Healthomics Tag Key List Structure
  property_count: 0
  slug: healthomics-tag-key-list-structure
- name: Healthomics Tag Key Structure
  property_count: 0
  slug: healthomics-tag-key-structure
- name: Healthomics Tag Map Structure
  property_count: 0
  slug: healthomics-tag-map-structure
- name: Healthomics Tag Resource Request Structure
  property_count: 1
  slug: healthomics-tag-resource-request-structure
- name: Healthomics Tag Resource Request Tags Map Structure
  property_count: 0
  slug: healthomics-tag-resource-request-tags-map-structure
- name: Healthomics Tag Resource Response Structure
  property_count: 0
  slug: healthomics-tag-resource-response-structure
- name: Healthomics Tag Value Structure
  property_count: 0
  slug: healthomics-tag-value-structure
- name: Healthomics Task Id Structure
  property_count: 0
  slug: healthomics-task-id-structure
- name: Healthomics Task List Item Cpus Integer Structure
  property_count: 0
  slug: healthomics-task-list-item-cpus-integer-structure
- name: Healthomics Task List Item Gpus Integer Structure
  property_count: 0
  slug: healthomics-task-list-item-gpus-integer-structure
- name: Healthomics Task List Item Memory Integer Structure
  property_count: 0
  slug: healthomics-task-list-item-memory-integer-structure
- name: Healthomics Task List Item Structure
  property_count: 9
  slug: healthomics-task-list-item-structure
- name: Healthomics Task List Structure
  property_count: 0
  slug: healthomics-task-list-structure
- name: Healthomics Task List Token Structure
  property_count: 0
  slug: healthomics-task-list-token-structure
- name: Healthomics Task Log Stream Structure
  property_count: 0
  slug: healthomics-task-log-stream-structure
- name: Healthomics Task Name Structure
  property_count: 0
  slug: healthomics-task-name-structure
- name: Healthomics Task Status Message Structure
  property_count: 0
  slug: healthomics-task-status-message-structure
- name: Healthomics Task Status Structure
  property_count: 0
  slug: healthomics-task-status-structure
- name: Healthomics Task Timestamp Structure
  property_count: 0
  slug: healthomics-task-timestamp-structure
- name: Healthomics Throttling Exception Structure
  property_count: 0
  slug: healthomics-throttling-exception-structure
- name: Healthomics Tsv Options Structure
  property_count: 1
  slug: healthomics-tsv-options-structure
- name: Healthomics Tsv Store Options Schema List Structure
  property_count: 0
  slug: healthomics-tsv-store-options-schema-list-structure
- name: Healthomics Tsv Store Options Structure
  property_count: 3
  slug: healthomics-tsv-store-options-structure
- name: Healthomics Untag Resource Request Structure
  property_count: 0
  slug: healthomics-untag-resource-request-structure
- name: Healthomics Untag Resource Response Structure
  property_count: 0
  slug: healthomics-untag-resource-response-structure
- name: Healthomics Update Annotation Store Request Structure
  property_count: 1
  slug: healthomics-update-annotation-store-request-structure
- name: Healthomics Update Annotation Store Response Structure
  property_count: 9
  slug: healthomics-update-annotation-store-response-structure
- name: Healthomics Update Run Group Request Max Cpus Integer Structure
  property_count: 0
  slug: healthomics-update-run-group-request-max-cpus-integer-structure
- name: Healthomics Update Run Group Request Max Duration Integer Structure
  property_count: 0
  slug: healthomics-update-run-group-request-max-duration-integer-structure
- name: Healthomics Update Run Group Request Max Gpus Integer Structure
  property_count: 0
  slug: healthomics-update-run-group-request-max-gpus-integer-structure
- name: Healthomics Update Run Group Request Max Runs Integer Structure
  property_count: 0
  slug: healthomics-update-run-group-request-max-runs-integer-structure
- name: Healthomics Update Run Group Request Structure
  property_count: 5
  slug: healthomics-update-run-group-request-structure
- name: Healthomics Update Time Structure
  property_count: 0
  slug: healthomics-update-time-structure
- name: Healthomics Update Variant Store Request Structure
  property_count: 1
  slug: healthomics-update-variant-store-request-structure
- name: Healthomics Update Variant Store Response Structure
  property_count: 7
  slug: healthomics-update-variant-store-response-structure
- name: Healthomics Update Workflow Request Structure
  property_count: 2
  slug: healthomics-update-workflow-request-structure
- name: Healthomics Upload Id Structure
  property_count: 0
  slug: healthomics-upload-id-structure
- name: Healthomics Upload Read Set Part Request Part Number Integer Structure
  property_count: 0
  slug: healthomics-upload-read-set-part-request-part-number-integer-structure
- name: Healthomics Upload Read Set Part Request Structure
  property_count: 1
  slug: healthomics-upload-read-set-part-request-structure
- name: Healthomics Upload Read Set Part Response Structure
  property_count: 1
  slug: healthomics-upload-read-set-part-response-structure
- name: Healthomics Validation Exception Structure
  property_count: 0
  slug: healthomics-validation-exception-structure
- name: Healthomics Variant Import Item Detail Structure
  property_count: 3
  slug: healthomics-variant-import-item-detail-structure
- name: Healthomics Variant Import Item Details Structure
  property_count: 0
  slug: healthomics-variant-import-item-details-structure
- name: Healthomics Variant Import Item Source Structure
  property_count: 1
  slug: healthomics-variant-import-item-source-structure
- name: Healthomics Variant Import Item Sources Structure
  property_count: 0
  slug: healthomics-variant-import-item-sources-structure
- name: Healthomics Variant Import Job Item Structure
  property_count: 9
  slug: healthomics-variant-import-job-item-structure
- name: Healthomics Variant Import Job Items Structure
  property_count: 0
  slug: healthomics-variant-import-job-items-structure
- name: Healthomics Variant Store Item Structure
  property_count: 11
  slug: healthomics-variant-store-item-structure
- name: Healthomics Variant Store Items Structure
  property_count: 0
  slug: healthomics-variant-store-items-structure
- name: Healthomics Vcf Options Structure
  property_count: 2
  slug: healthomics-vcf-options-structure
- name: Healthomics Workflow Arn Structure
  property_count: 0
  slug: healthomics-workflow-arn-structure
- name: Healthomics Workflow Definition Structure
  property_count: 0
  slug: healthomics-workflow-definition-structure
- name: Healthomics Workflow Description Structure
  property_count: 0
  slug: healthomics-workflow-description-structure
- name: Healthomics Workflow Digest Structure
  property_count: 0
  slug: healthomics-workflow-digest-structure
- name: Healthomics Workflow Engine Structure
  property_count: 0
  slug: healthomics-workflow-engine-structure
- name: Healthomics Workflow Export List Structure
  property_count: 0
  slug: healthomics-workflow-export-list-structure
- name: Healthomics Workflow Export Structure
  property_count: 0
  slug: healthomics-workflow-export-structure
- name: Healthomics Workflow Id Structure
  property_count: 0
  slug: healthomics-workflow-id-structure
- name: Healthomics Workflow List Item Structure
  property_count: 8
  slug: healthomics-workflow-list-item-structure
- name: Healthomics Workflow List Structure
  property_count: 0
  slug: healthomics-workflow-list-structure
- name: Healthomics Workflow List Token Structure
  property_count: 0
  slug: healthomics-workflow-list-token-structure
- name: Healthomics Workflow Main Structure
  property_count: 0
  slug: healthomics-workflow-main-structure
- name: Healthomics Workflow Metadata Key Structure
  property_count: 0
  slug: healthomics-workflow-metadata-key-structure
- name: Healthomics Workflow Metadata Structure
  property_count: 0
  slug: healthomics-workflow-metadata-structure
- name: Healthomics Workflow Metadata Value Structure
  property_count: 0
  slug: healthomics-workflow-metadata-value-structure
- name: Healthomics Workflow Name Structure
  property_count: 0
  slug: healthomics-workflow-name-structure
- name: Healthomics Workflow Parameter Description Structure
  property_count: 0
  slug: healthomics-workflow-parameter-description-structure
- name: Healthomics Workflow Parameter Name Structure
  property_count: 0
  slug: healthomics-workflow-parameter-name-structure
- name: Healthomics Workflow Parameter Structure
  property_count: 2
  slug: healthomics-workflow-parameter-structure
- name: Healthomics Workflow Parameter Template Structure
  property_count: 0
  slug: healthomics-workflow-parameter-template-structure
- name: Healthomics Workflow Request Id Structure
  property_count: 0
  slug: healthomics-workflow-request-id-structure
- name: Healthomics Workflow Status Message Structure
  property_count: 0
  slug: healthomics-workflow-status-message-structure
- name: Healthomics Workflow Status Structure
  property_count: 0
  slug: healthomics-workflow-status-structure
- name: Healthomics Workflow Timestamp Structure
  property_count: 0
  slug: healthomics-workflow-timestamp-structure
- name: Healthomics Workflow Type Structure
  property_count: 0
  slug: healthomics-workflow-type-structure
jsonld:
- class_count: 459
  name: Amazon Healthomics Context
  property_count: 0
  slug: amazon-healthomics-context
layout: provider
modified: '2026-05-19'
name: Amazon HealthOmics
nav: Providers
network: true
overview: 'Amazon HealthOmics publishes 13 APIs on the [APIs.io](https://apis.io/) network, including AnnotationStore API, AnnotationStores API, Import API, and 10 more. Tagged areas include Bioinformatics, Genomics, Healthcare, Life Sciences, and Cloud Computing.


  The Amazon HealthOmics catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon HealthOmics'' developer surface includes authentication, developer portal, documentation, support, engineering blog, developer console, signup flow, and 24 more developer resources.'
plans:
- name: Amazon Healthomics Plans Pricing
  plan_count: 3
  slug: amazon-healthomics-plans-pricing
random_paper: 12
rate_limits:
- limit_count: 5
  name: Amazon Healthomics Rate Limits
  slug: amazon-healthomics-rate-limits
rules:
- name: Amazon HealthOmics API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: amazon-healthomics-jsonschema-spectral-rules
- name: Amazon HealthOmics API Rules
  rule_count: 16
  severity_counts:
    error: 3
    hint: 0
    info: 5
    warn: 8
  slug: amazon-healthomics-spectral-rules
score:
  band: strong
  composite: 62.6
  delta: -8.9
  facets:
    commercial_clarity: 68.4
    contract_quality: 71.0
    developer_ergonomics: 58.7
    discoverability: 74.1
    governance: 68.8
    operational_transparency: 52.6
  previous_composite: 71.5
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 13
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 45.0
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-healthomics/refs/heads/main/screenshots/amazon-healthomics-2026-07-25T200010.png
security:
- kind: authentication
  name: Amazon Healthomics Authentication
  slug: amazon-healthomics-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Healthomics Domain Security
  slug: amazon-healthomics-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Healthomics Vulnerability Disclosure
  slug: amazon-healthomics-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Healthomics Trust Center
  slug: amazon-healthomics-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-healthomics
tags:
- Bioinformatics
- Genomics
- Healthcare
- Life Sciences
- Cloud Computing
use_cases:
- description: Store, analyze, and interpret whole genome sequencing data for research and clinical applications.
  name: Whole Genome Sequencing
- description: Run standard variant calling workflows on genomic data to identify genetic variants.
  name: Variant Calling Pipelines
- description: Analyze genomic data to understand drug response and develop personalized medicine approaches.
  name: Pharmacogenomics Research
- description: Process and analyze large-scale genomic datasets across patient populations for research.
  name: Population Genomics
- description: Support clinical genomics workflows for diagnosis and treatment of genetic disorders.
  name: Clinical Genomics
website: https://aws.amazon.com/healthomics/
---

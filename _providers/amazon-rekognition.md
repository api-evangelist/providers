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
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    auth_clarity: true
    consent_identity: true
    dry_run_mode: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: documented
    openapi_examples: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 48.5
  scored_at: '2026-08-19'
agentic_access:
- acting_count: 15
  human_in_the_loop: 0
  name: Amazon Rekognition Agentic Access
  operation_count: 15
  slug: amazon-rekognition-agentic-access
  summary_line: 15 operations · 15 acting
api_count: 10
apis:
- description: Identify celebrities in images and videos.
  name: Amazon Rekognition Celebrity Recognition API
  slug: amazon-rekognition-celebrity-recognition-api
- description: Detect inappropriate or explicit content.
  name: Amazon Rekognition Content Moderation API
  slug: amazon-rekognition-content-moderation-api
- description: Train and use custom image classifiers.
  name: Amazon Rekognition Custom Labels API
  slug: amazon-rekognition-custom-labels-api
- description: Create and manage searchable face collections.
  name: Amazon Rekognition Face Collections API
  slug: amazon-rekognition-face-collections-api
- description: Verify that a user is physically present during identity verification.
  name: Amazon Rekognition Face Liveness API
  slug: amazon-rekognition-face-liveness-api
- description: Search for matching faces within collections.
  name: Amazon Rekognition Face Search API
  slug: amazon-rekognition-face-search-api
- description: Detect and analyze faces with detailed attributes.
  name: Amazon Rekognition Facial Analysis API
  slug: amazon-rekognition-facial-analysis-api
- description: Detect labels, objects, scenes, and concepts in images.
  name: Amazon Rekognition Image Analysis API
  slug: amazon-rekognition-image-analysis-api
- description: Asynchronous analysis of videos stored in Amazon S3.
  name: Amazon Rekognition Stored Video Analysis API
  slug: amazon-rekognition-stored-video-analysis-api
- description: Detect and extract text from images and videos.
  name: Amazon Rekognition Text Detection API
  slug: amazon-rekognition-text-detection-api
arazzos:
- description: Recognize celebrities in an image and then label the same image for scene context.
  name: Amazon Rekognition Celebrity Scene Context
  slug: amazon-rekognition-celebrity-scene-context-workflow
- description: Run a Custom Labels model on an image and then screen the same image for unsafe content.
  name: Amazon Rekognition Custom Labels and Moderate
  slug: amazon-rekognition-custom-labels-and-moderate-workflow
- description: Confirm a face exists in the source image, then compare it against every face in a target image.
  name: Amazon Rekognition Detect then Compare Faces
  slug: amazon-rekognition-detect-then-compare-faces-workflow
- description: Create a face collection, index a face into it, then search the collection by a query image.
  name: Amazon Rekognition Enroll and Search a Face
  slug: amazon-rekognition-enroll-and-search-face-workflow
- description: Create a Face Liveness session, then poll for its results until a terminal status is reached.
  name: Amazon Rekognition Face Liveness Session
  slug: amazon-rekognition-face-liveness-session-workflow
- description: Detect general labels in an image and then screen the same image for unsafe content.
  name: Amazon Rekognition Label and Moderate an Image
  slug: amazon-rekognition-label-and-moderate-image-workflow
- description: Detect a face and check its quality, then index it into a collection only when a face is present.
  name: Amazon Rekognition Quality Gated Enrollment
  slug: amazon-rekognition-quality-gated-enrollment-workflow
- description: List collections, branch to create the collection only if missing, then index a face into it.
  name: Amazon Rekognition Reuse or Create Collection then Enroll
  slug: amazon-rekognition-reuse-or-create-collection-enroll-workflow
- description: Extract text from an image and then screen the same image for unsafe content.
  name: Amazon Rekognition Text and Moderation Screen
  slug: amazon-rekognition-text-and-moderation-screen-workflow
- description: Detect a face in an image to confirm a single subject, then search a collection to verify identity.
  name: Amazon Rekognition Verify a Face Against a Collection
  slug: amazon-rekognition-verify-face-against-collection-workflow
- description: Start an asynchronous video label detection job, poll until it succeeds, then read the results.
  name: Amazon Rekognition Video Label Detection Job
  slug: amazon-rekognition-video-label-detection-job-workflow
artifact_total: 178
collections:
- collection_type: postman
  name: Amazon Rekognition
  slug: postman-amazon-rekognition
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition API
  slug: open-amazon-rekognition-celebrity-recognition-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Content Moderation API
  slug: open-amazon-rekognition-content-moderation-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Custom Labels API
  slug: open-amazon-rekognition-custom-labels-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Face Collections API
  slug: open-amazon-rekognition-face-collections-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Face Liveness API
  slug: open-amazon-rekognition-face-liveness-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Face Search API
  slug: open-amazon-rekognition-face-search-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Facial Analysis API
  slug: open-amazon-rekognition-facial-analysis-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Image Analysis API
  slug: open-amazon-rekognition-image-analysis-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Stored Video Analysis API
  slug: open-amazon-rekognition-stored-video-analysis-api
- collection_type: open
  name: Amazon Rekognition Celebrity Recognition Text Detection API
  slug: open-amazon-rekognition-text-detection-api
- collection_type: open
  name: Amazon Rekognition
  slug: open-amazon-rekognition
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/amazon-rekognition-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/amazon-rekognition-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/amazon-rekognition-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/amazon-rekognition-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/amazon-rekognition-authentication.yml
- group: build
  title: ''
  type: Packages
  url: packages/amazon-rekognition-packages.yml
- group: agent
  title: ''
  type: MCPServer
  url: mcp/amazon-rekognition-mcp.yml
- group: agent
  title: ''
  type: WellKnown
  url: well-known/amazon-rekognition-well-known.yml
- group: auth
  title: ''
  type: SecurityTxt
  url: well-known/amazon-rekognition-security.txt
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/amazon-rekognition-llms.txt
- group: other
  title: ''
  type: Overlay
  url: overlays/amazon-rekognition-openapi-overlay.yaml
- group: design
  title: ''
  type: ErrorCatalog
  url: errors/amazon-rekognition-problem-types.yml
- group: design
  title: ''
  type: Lifecycle
  url: lifecycle/amazon-rekognition-lifecycle.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/amazon-rekognition-conformance.yml
- group: design
  title: ''
  type: Conventions
  url: conventions/amazon-rekognition-conventions.yml
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/amazon-rekognition-changelog.yml
- group: build
  title: ''
  type: CLI
  url: cli/amazon-rekognition-cli.yml
- group: design
  title: ''
  type: Components
  url: components/amazon-rekognition-components.yml
- group: design
  title: ''
  type: DataModel
  url: data-model/amazon-rekognition-data-model.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/amazon-rekognition/overview
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-celebrity-scene-context-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-custom-labels-and-moderate-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-detect-then-compare-faces-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-enroll-and-search-face-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-face-liveness-session-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-label-and-moderate-image-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-quality-gated-enrollment-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-reuse-or-create-collection-enroll-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-text-and-moderation-screen-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-verify-face-against-collection-workflow.yml
- group: design
  title: ''
  type: Arazzo
  url: arazzo/amazon-rekognition-video-label-detection-job-workflow.yml
- group: start
  title: ''
  type: Portal
  url: https://aws.amazon.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://aws.amazon.com/rekognition/
- group: docs
  title: ''
  type: Documentation
  url: https://docs.aws.amazon.com/rekognition/
- group: start
  title: ''
  type: Console
  url: https://console.aws.amazon.com/rekognition/
- group: start
  title: ''
  type: Signup
  url: https://portal.aws.amazon.com/billing/signup
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/rekognition/pricing/
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
  url: https://aws.amazon.com/support/
- group: operate
  title: ''
  type: FAQ
  url: https://aws.amazon.com/rekognition/faqs/
- group: company
  title: ''
  type: Blog
  url: https://aws.amazon.com/blogs/machine-learning/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/aws
- group: operate
  title: ''
  type: StatusPage
  url: https://health.aws.amazon.com/health/status
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/AmazonWebServices
- group: operate
  title: ''
  type: StackOverflow
  url: https://stackoverflow.com/questions/tagged/amazon-rekognition
- group: operate
  title: ''
  type: Contact
  url: https://aws.amazon.com/contact-us/
- group: auth
  title: ''
  type: Security
  url: https://aws.amazon.com/security/
- group: auth
  title: ''
  type: Compliance
  url: https://aws.amazon.com/compliance/
- group: other
  title: ''
  type: KnowledgeCenter
  url: https://repost.aws/knowledge-center
- group: design
  title: ''
  type: SpectralRules
  url: rules/amazon-rekognition-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/amazon-rekognition-vocabulary.yaml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/amazon-rekognition-context.jsonld
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-bounding-box-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-compare-faces-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-compare-faces-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-create-collection-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-create-collection-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-create-face-liveness-session-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-create-face-liveness-session-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-custom-labels-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-custom-labels-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-faces-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-faces-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-labels-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-labels-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-moderation-labels-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-moderation-labels-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detect-text-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-detectlabelsresponse-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-face-detail-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-get-face-liveness-session-results-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-get-face-liveness-session-results-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-get-label-detection-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-get-video-job-result-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-image-only-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-image-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-index-faces-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-index-faces-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-label-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-list-collections-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-notification-channel-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-recognize-celebrities-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-s3-object-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-search-faces-by-image-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-search-faces-by-image-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-start-label-detection-request-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-start-video-job-response-schema.json
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/amazon-rekognition-video-schema.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-bounding-box-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-compare-faces-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-compare-faces-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-create-collection-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-create-collection-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-create-face-liveness-session-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-create-face-liveness-session-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-custom-labels-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-custom-labels-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-faces-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-faces-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-labels-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-labels-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-moderation-labels-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-moderation-labels-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detect-text-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-detectlabelsresponse-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-face-detail-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-get-face-liveness-session-results-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-get-face-liveness-session-results-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-get-label-detection-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-get-video-job-result-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-image-only-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-image-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-index-faces-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-index-faces-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-label-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-list-collections-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-notification-channel-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-recognize-celebrities-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-s3-object-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-search-faces-by-image-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-search-faces-by-image-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-start-label-detection-request-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-start-video-job-response-structure.json
- group: design
  title: ''
  type: JSONStructure
  url: json-structure/amazon-rekognition-video-structure.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-bounding-box-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-compare-faces-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-compare-faces-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-create-collection-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-create-collection-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-create-face-liveness-session-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-create-face-liveness-session-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-custom-labels-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-custom-labels-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-faces-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-faces-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-labels-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-labels-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-moderation-labels-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-moderation-labels-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detect-text-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-detectlabelsresponse-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-face-detail-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-get-face-liveness-session-results-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-get-face-liveness-session-results-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-get-label-detection-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-get-video-job-result-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-image-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-image-only-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-index-faces-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-index-faces-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-label-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-list-collections-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-notification-channel-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-recognize-celebrities-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-s3-object-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-search-faces-by-image-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-search-faces-by-image-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-start-label-detection-request-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-start-video-job-response-example.json
- group: build
  title: ''
  type: Examples
  url: examples/amazon-rekognition-video-example.json
created: '2024-01-15'
description: Amazon Rekognition is a cloud-based computer vision service that makes it easy to add image and video analysis to your applications, providing capabilities such as object and scene detection, facial analysis, face comparison, celebrity recognition, text detection, content moderation, custom labels, face liveness detection, and streaming video analysis using deep learning technology.
examples:
- key_count: 4
  name: Amazon Rekognition Bounding Box Example
  slug: amazon-rekognition-bounding-box-example
- key_count: 4
  name: Amazon Rekognition Compare Faces Request Example
  slug: amazon-rekognition-compare-faces-request-example
- key_count: 3
  name: Amazon Rekognition Compare Faces Response Example
  slug: amazon-rekognition-compare-faces-response-example
- key_count: 2
  name: Amazon Rekognition Create Collection Request Example
  slug: amazon-rekognition-create-collection-request-example
- key_count: 3
  name: Amazon Rekognition Create Collection Response Example
  slug: amazon-rekognition-create-collection-response-example
- key_count: 3
  name: Amazon Rekognition Create Face Liveness Session Request Example
  slug: amazon-rekognition-create-face-liveness-session-request-example
- key_count: 1
  name: Amazon Rekognition Create Face Liveness Session Response Example
  slug: amazon-rekognition-create-face-liveness-session-response-example
- key_count: 4
  name: Amazon Rekognition Detect Custom Labels Request Example
  slug: amazon-rekognition-detect-custom-labels-request-example
- key_count: 1
  name: Amazon Rekognition Detect Custom Labels Response Example
  slug: amazon-rekognition-detect-custom-labels-response-example
- key_count: 2
  name: Amazon Rekognition Detect Faces Request Example
  slug: amazon-rekognition-detect-faces-request-example
- key_count: 2
  name: Amazon Rekognition Detect Faces Response Example
  slug: amazon-rekognition-detect-faces-response-example
- key_count: 5
  name: Amazon Rekognition Detect Labels Request Example
  slug: amazon-rekognition-detect-labels-request-example
- key_count: 4
  name: Amazon Rekognition Detect Labels Response Example
  slug: amazon-rekognition-detect-labels-response-example
- key_count: 4
  name: Amazon Rekognition Detect Moderation Labels Request Example
  slug: amazon-rekognition-detect-moderation-labels-request-example
- key_count: 4
  name: Amazon Rekognition Detect Moderation Labels Response Example
  slug: amazon-rekognition-detect-moderation-labels-response-example
- key_count: 2
  name: Amazon Rekognition Detect Text Response Example
  slug: amazon-rekognition-detect-text-response-example
- key_count: 3
  name: Amazon Rekognition Detectlabelsresponse Example
  slug: amazon-rekognition-detectlabelsresponse-example
- key_count: 6
  name: Amazon Rekognition Face Detail Example
  slug: amazon-rekognition-face-detail-example
- key_count: 1
  name: Amazon Rekognition Get Face Liveness Session Results Request Example
  slug: amazon-rekognition-get-face-liveness-session-results-request-example
- key_count: 5
  name: Amazon Rekognition Get Face Liveness Session Results Response Example
  slug: amazon-rekognition-get-face-liveness-session-results-response-example
- key_count: 7
  name: Amazon Rekognition Get Label Detection Response Example
  slug: amazon-rekognition-get-label-detection-response-example
- key_count: 5
  name: Amazon Rekognition Get Video Job Result Request Example
  slug: amazon-rekognition-get-video-job-result-request-example
- key_count: 2
  name: Amazon Rekognition Image Example
  slug: amazon-rekognition-image-example
- key_count: 1
  name: Amazon Rekognition Image Only Request Example
  slug: amazon-rekognition-image-only-request-example
- key_count: 6
  name: Amazon Rekognition Index Faces Request Example
  slug: amazon-rekognition-index-faces-request-example
- key_count: 4
  name: Amazon Rekognition Index Faces Response Example
  slug: amazon-rekognition-index-faces-response-example
- key_count: 4
  name: Amazon Rekognition Label Example
  slug: amazon-rekognition-label-example
- key_count: 3
  name: Amazon Rekognition List Collections Response Example
  slug: amazon-rekognition-list-collections-response-example
- key_count: 2
  name: Amazon Rekognition Notification Channel Example
  slug: amazon-rekognition-notification-channel-example
- key_count: 2
  name: Amazon Rekognition Recognize Celebrities Response Example
  slug: amazon-rekognition-recognize-celebrities-response-example
- key_count: 3
  name: Amazon Rekognition S3 Object Example
  slug: amazon-rekognition-s3-object-example
- key_count: 5
  name: Amazon Rekognition Search Faces By Image Request Example
  slug: amazon-rekognition-search-faces-by-image-request-example
- key_count: 4
  name: Amazon Rekognition Search Faces By Image Response Example
  slug: amazon-rekognition-search-faces-by-image-response-example
- key_count: 7
  name: Amazon Rekognition Start Label Detection Request Example
  slug: amazon-rekognition-start-label-detection-request-example
- key_count: 1
  name: Amazon Rekognition Start Video Job Response Example
  slug: amazon-rekognition-start-video-job-response-example
- key_count: 1
  name: Amazon Rekognition Video Example
  slug: amazon-rekognition-video-example
features:
- description: Detect thousands of objects, scenes, and concepts in images and videos with high confidence scores using deep learning.
  name: Object and Scene Detection
- description: Detect and analyze faces with attributes including age range, emotions, gender, and facial landmarks.
  name: Facial Analysis
- description: Compare faces across images to determine if they are the same person with a similarity score.
  name: Face Comparison
- description: Create searchable face collections to index and search millions of faces in near real-time.
  name: Face Collections
- description: Identify thousands of celebrities in images and videos across categories like sports, entertainment, and politics.
  name: Celebrity Recognition
- description: Detect and extract printed and handwritten text from images and videos in multiple languages.
  name: Text Detection
- description: Detect explicit, inappropriate, or violent content in images and videos for automated content moderation.
  name: Content Moderation
- description: Build and train custom image classifiers using your own labeled images for domain-specific object detection.
  name: Custom Labels
- description: Detect personal protective equipment such as face covers, hand covers, and head covers on persons in images.
  name: Protective Equipment Detection
- description: Verify that a user is physically present during identity verification to prevent spoofing attacks.
  name: Face Liveness Detection
- description: Track and follow identified people across frames in stored video footage.
  name: People Pathing
- description: Identify technical cues and segments such as black frames, end credits, and color bars in video content.
  name: Video Segmentation
- description: Analyze live streaming video in real-time using Amazon Kinesis Video Streams integration.
  name: Streaming Video Analysis
- description: Evaluate image quality attributes including sharpness, brightness, contrast, and dominant colors.
  name: Image Properties Analysis
finops:
- name: Amazon Rekognition Finops
  service_category: API
  slug: amazon-rekognition-finops
graphqls:
- description: This directory contains a conceptual GraphQL schema for the Amazon Rekognition API. The schema is derived from the Amazon Rekognition REST API and its public documentation at https://docs.aws.amazon.c
  name: Amazon Rekognition GraphQL Schema
  slug: amazon-rekognition-graphql
image: https://a0.awsstatic.com/libra-css/images/logos/aws_logo_smile_1200x630.png
json_schemas:
- name: BoundingBox
  property_count: 4
  slug: amazon-rekognition-bounding-box
- name: CompareFacesRequest
  property_count: 4
  slug: amazon-rekognition-compare-faces-request
- name: CompareFacesResponse
  property_count: 3
  slug: amazon-rekognition-compare-faces-response
- name: CreateCollectionRequest
  property_count: 2
  slug: amazon-rekognition-create-collection-request
- name: CreateCollectionResponse
  property_count: 3
  slug: amazon-rekognition-create-collection-response
- name: CreateFaceLivenessSessionRequest
  property_count: 3
  slug: amazon-rekognition-create-face-liveness-session-request
- name: CreateFaceLivenessSessionResponse
  property_count: 1
  slug: amazon-rekognition-create-face-liveness-session-response
- name: DetectCustomLabelsRequest
  property_count: 4
  slug: amazon-rekognition-detect-custom-labels-request
- name: DetectCustomLabelsResponse
  property_count: 1
  slug: amazon-rekognition-detect-custom-labels-response
- name: DetectFacesRequest
  property_count: 2
  slug: amazon-rekognition-detect-faces-request
- name: DetectFacesResponse
  property_count: 2
  slug: amazon-rekognition-detect-faces-response
- name: DetectLabelsRequest
  property_count: 5
  slug: amazon-rekognition-detect-labels-request
- name: DetectLabelsResponse
  property_count: 4
  slug: amazon-rekognition-detect-labels-response
- name: DetectModerationLabelsRequest
  property_count: 4
  slug: amazon-rekognition-detect-moderation-labels-request
- name: DetectModerationLabelsResponse
  property_count: 4
  slug: amazon-rekognition-detect-moderation-labels-response
- name: DetectTextResponse
  property_count: 2
  slug: amazon-rekognition-detect-text-response
- name: DetectLabelsResponse
  property_count: 3
  slug: amazon-rekognition-detectlabelsresponse
- name: FaceDetail
  property_count: 6
  slug: amazon-rekognition-face-detail
- name: GetFaceLivenessSessionResultsRequest
  property_count: 1
  slug: amazon-rekognition-get-face-liveness-session-results-request
- name: GetFaceLivenessSessionResultsResponse
  property_count: 5
  slug: amazon-rekognition-get-face-liveness-session-results-response
- name: GetLabelDetectionResponse
  property_count: 7
  slug: amazon-rekognition-get-label-detection-response
- name: GetVideoJobResultRequest
  property_count: 5
  slug: amazon-rekognition-get-video-job-result-request
- name: ImageOnlyRequest
  property_count: 1
  slug: amazon-rekognition-image-only-request
- name: Image
  property_count: 2
  slug: amazon-rekognition-image
- name: IndexFacesRequest
  property_count: 6
  slug: amazon-rekognition-index-faces-request
- name: IndexFacesResponse
  property_count: 4
  slug: amazon-rekognition-index-faces-response
- name: Label
  property_count: 4
  slug: amazon-rekognition-label
- name: ListCollectionsResponse
  property_count: 3
  slug: amazon-rekognition-list-collections-response
- name: NotificationChannel
  property_count: 2
  slug: amazon-rekognition-notification-channel
- name: RecognizeCelebritiesResponse
  property_count: 2
  slug: amazon-rekognition-recognize-celebrities-response
- name: S3Object
  property_count: 3
  slug: amazon-rekognition-s3-object
- name: SearchFacesByImageRequest
  property_count: 5
  slug: amazon-rekognition-search-faces-by-image-request
- name: SearchFacesByImageResponse
  property_count: 4
  slug: amazon-rekognition-search-faces-by-image-response
- name: StartLabelDetectionRequest
  property_count: 7
  slug: amazon-rekognition-start-label-detection-request
- name: StartVideoJobResponse
  property_count: 1
  slug: amazon-rekognition-start-video-job-response
- name: Video
  property_count: 1
  slug: amazon-rekognition-video
json_structures:
- name: Amazon Rekognition Bounding Box Structure
  property_count: 4
  slug: amazon-rekognition-bounding-box-structure
- name: Amazon Rekognition Compare Faces Request Structure
  property_count: 4
  slug: amazon-rekognition-compare-faces-request-structure
- name: Amazon Rekognition Compare Faces Response Structure
  property_count: 3
  slug: amazon-rekognition-compare-faces-response-structure
- name: Amazon Rekognition Create Collection Request Structure
  property_count: 2
  slug: amazon-rekognition-create-collection-request-structure
- name: Amazon Rekognition Create Collection Response Structure
  property_count: 3
  slug: amazon-rekognition-create-collection-response-structure
- name: Amazon Rekognition Create Face Liveness Session Request Structure
  property_count: 3
  slug: amazon-rekognition-create-face-liveness-session-request-structure
- name: Amazon Rekognition Create Face Liveness Session Response Structure
  property_count: 1
  slug: amazon-rekognition-create-face-liveness-session-response-structure
- name: Amazon Rekognition Detect Custom Labels Request Structure
  property_count: 4
  slug: amazon-rekognition-detect-custom-labels-request-structure
- name: Amazon Rekognition Detect Custom Labels Response Structure
  property_count: 1
  slug: amazon-rekognition-detect-custom-labels-response-structure
- name: Amazon Rekognition Detect Faces Request Structure
  property_count: 2
  slug: amazon-rekognition-detect-faces-request-structure
- name: Amazon Rekognition Detect Faces Response Structure
  property_count: 2
  slug: amazon-rekognition-detect-faces-response-structure
- name: Amazon Rekognition Detect Labels Request Structure
  property_count: 5
  slug: amazon-rekognition-detect-labels-request-structure
- name: Amazon Rekognition Detect Labels Response Structure
  property_count: 4
  slug: amazon-rekognition-detect-labels-response-structure
- name: Amazon Rekognition Detect Moderation Labels Request Structure
  property_count: 4
  slug: amazon-rekognition-detect-moderation-labels-request-structure
- name: Amazon Rekognition Detect Moderation Labels Response Structure
  property_count: 4
  slug: amazon-rekognition-detect-moderation-labels-response-structure
- name: Amazon Rekognition Detect Text Response Structure
  property_count: 2
  slug: amazon-rekognition-detect-text-response-structure
- name: Amazon Rekognition Detectlabelsresponse Structure
  property_count: 3
  slug: amazon-rekognition-detectlabelsresponse-structure
- name: Amazon Rekognition Face Detail Structure
  property_count: 6
  slug: amazon-rekognition-face-detail-structure
- name: Amazon Rekognition Get Face Liveness Session Results Request Structure
  property_count: 1
  slug: amazon-rekognition-get-face-liveness-session-results-request-structure
- name: Amazon Rekognition Get Face Liveness Session Results Response Structure
  property_count: 5
  slug: amazon-rekognition-get-face-liveness-session-results-response-structure
- name: Amazon Rekognition Get Label Detection Response Structure
  property_count: 7
  slug: amazon-rekognition-get-label-detection-response-structure
- name: Amazon Rekognition Get Video Job Result Request Structure
  property_count: 5
  slug: amazon-rekognition-get-video-job-result-request-structure
- name: Amazon Rekognition Image Only Request Structure
  property_count: 1
  slug: amazon-rekognition-image-only-request-structure
- name: Amazon Rekognition Image Structure
  property_count: 2
  slug: amazon-rekognition-image-structure
- name: Amazon Rekognition Index Faces Request Structure
  property_count: 6
  slug: amazon-rekognition-index-faces-request-structure
- name: Amazon Rekognition Index Faces Response Structure
  property_count: 4
  slug: amazon-rekognition-index-faces-response-structure
- name: Amazon Rekognition Label Structure
  property_count: 4
  slug: amazon-rekognition-label-structure
- name: Amazon Rekognition List Collections Response Structure
  property_count: 3
  slug: amazon-rekognition-list-collections-response-structure
- name: Amazon Rekognition Notification Channel Structure
  property_count: 2
  slug: amazon-rekognition-notification-channel-structure
- name: Amazon Rekognition Recognize Celebrities Response Structure
  property_count: 2
  slug: amazon-rekognition-recognize-celebrities-response-structure
- name: Amazon Rekognition S3 Object Structure
  property_count: 3
  slug: amazon-rekognition-s3-object-structure
- name: Amazon Rekognition Search Faces By Image Request Structure
  property_count: 5
  slug: amazon-rekognition-search-faces-by-image-request-structure
- name: Amazon Rekognition Search Faces By Image Response Structure
  property_count: 4
  slug: amazon-rekognition-search-faces-by-image-response-structure
- name: Amazon Rekognition Start Label Detection Request Structure
  property_count: 7
  slug: amazon-rekognition-start-label-detection-request-structure
- name: Amazon Rekognition Start Video Job Response Structure
  property_count: 1
  slug: amazon-rekognition-start-video-job-response-structure
- name: Amazon Rekognition Video Structure
  property_count: 1
  slug: amazon-rekognition-video-structure
jsonld:
- class_count: 30
  name: Amazon Rekognition Context
  property_count: 108
  slug: amazon-rekognition-context
layout: provider
mcp_servers:
- description: ''
  name: amazon-rekognition-mcp.yml
  slug: amazon-rekognition-mcpyml
modified: '2026-06-20'
name: Amazon Rekognition
nav: Providers
network: true
overview: 'Amazon Rekognition publishes 10 APIs on the [APIs.io](https://apis.io/) network, including Celebrity Recognition API, Content Moderation API, Custom Labels API, and 7 more. Tagged areas include Celebrity Recognition, Computer Vision, Content Moderation, Custom Labels, and Deep Learning.


  The Amazon Rekognition catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Amazon Rekognition''s developer surface includes authentication, changelog, CLI, developer portal, documentation, developer console, signup flow, and 154 more developer resources.'
plans:
- name: Amazon Rekognition Plans Pricing
  plan_count: 3
  slug: amazon-rekognition-plans-pricing
random_paper: 96
rate_limits:
- limit_count: 5
  name: Amazon Rekognition Rate Limits
  slug: amazon-rekognition-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Amazon Rekognition API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: amazon-rekognition-jsonschema-spectral-rules
- effective_rule_count: 64
  extends:
  - spectral:oas
  name: Amazon Rekognition API Rules
  rule_count: 23
  severity_counts:
    error: 8
    hint: 0
    info: 2
    warn: 13
  slug: amazon-rekognition-spectral-rules
score:
  band: strong
  composite: 55.3
  delta: -6.1
  facets:
    access_clarity: 76.3
    commercial_clarity: 76.3
    contract_governance: 41.7
    contract_quality: 32.3
    developer_ergonomics: 57.1
    discoverability: 87.0
    governance: 41.7
    operational_transparency: 52.6
  previous_composite: 61.4
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 10
      marker_coverage: 100.0
      total: 10
    mcp: first-party
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/amazon-rekognition/refs/heads/main/screenshots/amazon-rekognition-2026-06-20T171807.png
security:
- kind: authentication
  name: Amazon Rekognition Authentication
  slug: amazon-rekognition-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Amazon Rekognition Domain Security
  slug: amazon-rekognition-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Amazon Rekognition Vulnerability Disclosure
  slug: amazon-rekognition-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Amazon Rekognition Trust Center
  slug: amazon-rekognition-trust-center
  summary_line: PCI DSS, HIPAA, FedRAMP, GDPR, FIPS 140
slug: amazon-rekognition
tags:
- Celebrity Recognition
- Computer Vision
- Content Moderation
- Custom Labels
- Deep Learning
- Face Liveness
- Facial Recognition
- Image Analysis
- Machine Learning
- Object Detection
- Text Detection
- Video Analysis
use_cases:
- description: Verify user identities by comparing selfies to ID documents or previously stored face images for onboarding and authentication.
  name: Identity Verification
- description: Automatically moderate user-generated content on platforms to detect and filter explicit or inappropriate imagery.
  name: Content Moderation
- description: Build searchable image and video archives by automatically tagging media with detected labels, faces, and text.
  name: Searchable Media Libraries
- description: Monitor camera feeds to detect whether workers are wearing required personal protective equipment in industrial settings.
  name: Workplace Safety Compliance
- description: Prevent identity fraud during digital onboarding by using face liveness detection to confirm real users.
  name: Fraud Prevention
- description: Analyze in-store camera feeds to track customer behavior, measure foot traffic, and optimize product placement.
  name: Smart Retail Analytics
- description: Search video archives for persons of interest by comparing faces against a known collection.
  name: Public Safety and Security
- description: Automatically tag celebrities in photos and videos for media companies to improve content discoverability.
  name: Media and Entertainment
- description: Train custom classifiers to detect proprietary products, logos, brand assets, or industry-specific objects.
  name: Custom Object Detection
website: https://aws.amazon.com/rekognition/
---

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
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 35.6
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 2
  human_in_the_loop: 0
  name: Google Slides Agentic Access
  operation_count: 5
  slug: google-slides-agentic-access
  summary_line: 5 operations · 2 acting
api_count: 1
apis:
- description: Operations on pages within presentations
  name: Google Slides Pages API
  slug: google-slides-pages-api
- description: Operations on Google Slides presentations
  name: Google Slides Presentations API
  slug: google-slides-presentations-api
artifact_total: 445
collections:
- collection_type: postman
  name: Google Slides Pages API
  slug: postman-google-slides-pages-api
- collection_type: postman
  name: Google Slides Pages Presentations API
  slug: postman-google-slides-presentations-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Google Slides API
  slug: open-google-slides-api
- collection_type: open
  name: Google Slides Pages API
  slug: open-google-slides-pages-api
- collection_type: open
  name: Google Slides Pages Presentations API
  slug: open-google-slides-presentations-api
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/googleworkspace/slides-api/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/googleworkspace/slides-api/blob/main/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/googleworkspace/slides-api/blob/main/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/googleworkspace/slides-api/blob/main/LICENSE
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/google-slides/overview
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/google-slides-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/google-slides-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/google-slides-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/google-slides-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/google-slides-scopes.yml
- group: start
  title: ''
  type: Portal
  url: https://console.cloud.google.com/
- group: auth
  title: ''
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.google.com/slides/api/quickstart/python
- group: operate
  title: ''
  type: StatusPage
  url: https://status.cloud.google.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://policies.google.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://policies.google.com/terms
- group: docs
  title: Developer Products
  type: Documentation
  url: https://developers.google.com/workspace/products
- group: docs
  title: Credentials
  type: Documentation
  url: https://developers.google.com/workspace/guides/create-credentials
- group: docs
  title: Enable APIs
  type: Documentation
  url: https://developers.google.com/workspace/guides/enable-apis
- group: docs
  title: OAuth Consent Screen
  type: Documentation
  url: https://developers.google.com/workspace/guides/configure-oauth-consent
- group: auth
  title: OAuth Scopes
  type: Authentication
  url: https://developers.google.com/identity/protocols/oauth2/scopes
- group: operate
  title: Issue Tracker
  type: Support
  url: https://issuetracker.google.com/bookmark-groups/78025
- group: operate
  title: Workspace Release Notes
  type: ReleaseNotes
  url: https://developers.google.com/workspace/release-notes
- group: company
  title: ''
  type: Blog
  url: https://cloud.google.com/blog/products/application-development/introducing-google-slides-api
- group: design
  title: ''
  type: SpectralRules
  url: rules/google-slides-spectral-rules.yml
created: '2024-01-01'
description: An API for creating, reading, and editing Google Slides presentations.
examples:
- key_count: 7
  name: Google Slides Affine Transform Example
  slug: google-slides-affine-transform-example
- key_count: 2
  name: Google Slides Auto Text Example
  slug: google-slides-auto-text-example
- key_count: 2
  name: Google Slides Autofit Example
  slug: google-slides-autofit-example
- key_count: 1
  name: Google Slides Batch Update Presentation Request Example
  slug: google-slides-batch-update-presentation-request-example
- key_count: 2
  name: Google Slides Batch Update Presentation Response Example
  slug: google-slides-batch-update-presentation-response-example
- key_count: 3
  name: Google Slides Bullet Example
  slug: google-slides-bullet-example
- key_count: 1
  name: Google Slides Color Scheme Example
  slug: google-slides-color-scheme-example
- key_count: 2
  name: Google Slides Color Stop Example
  slug: google-slides-color-stop-example
- key_count: 2
  name: Google Slides Create Image Request Example
  slug: google-slides-create-image-request-example
- key_count: 1
  name: Google Slides Create Image Response Example
  slug: google-slides-create-image-response-example
- key_count: 3
  name: Google Slides Create Line Request Example
  slug: google-slides-create-line-request-example
- key_count: 1
  name: Google Slides Create Line Response Example
  slug: google-slides-create-line-response-example
- key_count: 2
  name: Google Slides Create Paragraph Bullets Request Example
  slug: google-slides-create-paragraph-bullets-request-example
- key_count: 2
  name: Google Slides Create Shape Request Example
  slug: google-slides-create-shape-request-example
- key_count: 1
  name: Google Slides Create Shape Response Example
  slug: google-slides-create-shape-response-example
- key_count: 4
  name: Google Slides Create Sheets Chart Request Example
  slug: google-slides-create-sheets-chart-request-example
- key_count: 1
  name: Google Slides Create Sheets Chart Response Example
  slug: google-slides-create-sheets-chart-response-example
- key_count: 3
  name: Google Slides Create Slide Request Example
  slug: google-slides-create-slide-request-example
- key_count: 1
  name: Google Slides Create Slide Response Example
  slug: google-slides-create-slide-response-example
- key_count: 3
  name: Google Slides Create Table Request Example
  slug: google-slides-create-table-request-example
- key_count: 1
  name: Google Slides Create Table Response Example
  slug: google-slides-create-table-response-example
- key_count: 3
  name: Google Slides Create Video Request Example
  slug: google-slides-create-video-request-example
- key_count: 1
  name: Google Slides Create Video Response Example
  slug: google-slides-create-video-response-example
- key_count: 5
  name: Google Slides Crop Properties Example
  slug: google-slides-crop-properties-example
- key_count: 1
  name: Google Slides Delete Object Request Example
  slug: google-slides-delete-object-request-example
- key_count: 1
  name: Google Slides Delete Paragraph Bullets Request Example
  slug: google-slides-delete-paragraph-bullets-request-example
- key_count: 1
  name: Google Slides Delete Table Column Request Example
  slug: google-slides-delete-table-column-request-example
- key_count: 1
  name: Google Slides Delete Table Row Request Example
  slug: google-slides-delete-table-row-request-example
- key_count: 1
  name: Google Slides Delete Text Request Example
  slug: google-slides-delete-text-request-example
- key_count: 2
  name: Google Slides Dimension Example
  slug: google-slides-dimension-example
- key_count: 2
  name: Google Slides Duplicate Object Request Example
  slug: google-slides-duplicate-object-request-example
- key_count: 1
  name: Google Slides Duplicate Object Response Example
  slug: google-slides-duplicate-object-response-example
- key_count: 1
  name: Google Slides Error Response Example
  slug: google-slides-error-response-example
- key_count: 1
  name: Google Slides Group Example
  slug: google-slides-group-example
- key_count: 2
  name: Google Slides Group Objects Request Example
  slug: google-slides-group-objects-request-example
- key_count: 1
  name: Google Slides Group Objects Response Example
  slug: google-slides-group-objects-response-example
- key_count: 2
  name: Google Slides Image Example
  slug: google-slides-image-example
- key_count: 3
  name: Google Slides Image Properties Example
  slug: google-slides-image-properties-example
- key_count: 3
  name: Google Slides Insert Table Columns Request Example
  slug: google-slides-insert-table-columns-request-example
- key_count: 3
  name: Google Slides Insert Table Rows Request Example
  slug: google-slides-insert-table-rows-request-example
- key_count: 3
  name: Google Slides Insert Text Request Example
  slug: google-slides-insert-text-request-example
- key_count: 2
  name: Google Slides Layout Placeholder Id Mapping Example
  slug: google-slides-layout-placeholder-id-mapping-example
- key_count: 3
  name: Google Slides Layout Properties Example
  slug: google-slides-layout-properties-example
- key_count: 2
  name: Google Slides Layout Reference Example
  slug: google-slides-layout-reference-example
- key_count: 2
  name: Google Slides Line Connection Example
  slug: google-slides-line-connection-example
- key_count: 2
  name: Google Slides Line Example
  slug: google-slides-line-example
- key_count: 0
  name: Google Slides Line Fill Example
  slug: google-slides-line-fill-example
- key_count: 3
  name: Google Slides Line Properties Example
  slug: google-slides-line-properties-example
- key_count: 4
  name: Google Slides Link Example
  slug: google-slides-link-example
- key_count: 2
  name: Google Slides List Example
  slug: google-slides-list-example
- key_count: 1
  name: Google Slides Master Properties Example
  slug: google-slides-master-properties-example
- key_count: 1
  name: Google Slides Merge Table Cells Request Example
  slug: google-slides-merge-table-cells-request-example
- key_count: 0
  name: Google Slides Nesting Level Example
  slug: google-slides-nesting-level-example
- key_count: 1
  name: Google Slides Notes Properties Example
  slug: google-slides-notes-properties-example
- key_count: 1
  name: Google Slides Opaque Color Example
  slug: google-slides-opaque-color-example
- key_count: 0
  name: Google Slides Optional Color Example
  slug: google-slides-optional-color-example
- key_count: 2
  name: Google Slides Outline Example
  slug: google-slides-outline-example
- key_count: 0
  name: Google Slides Outline Fill Example
  slug: google-slides-outline-fill-example
- key_count: 1
  name: Google Slides Page Background Fill Example
  slug: google-slides-page-background-fill-example
- key_count: 3
  name: Google Slides Page Element Example
  slug: google-slides-page-element-example
- key_count: 1
  name: Google Slides Page Element Properties Example
  slug: google-slides-page-element-properties-example
- key_count: 4
  name: Google Slides Page Example
  slug: google-slides-page-example
- key_count: 0
  name: Google Slides Page Properties Example
  slug: google-slides-page-properties-example
- key_count: 0
  name: Google Slides Paragraph Marker Example
  slug: google-slides-paragraph-marker-example
- key_count: 4
  name: Google Slides Paragraph Style Example
  slug: google-slides-paragraph-style-example
- key_count: 3
  name: Google Slides Placeholder Example
  slug: google-slides-placeholder-example
- key_count: 7
  name: Google Slides Presentation Example
  slug: google-slides-presentation-example
- key_count: 3
  name: Google Slides Range Example
  slug: google-slides-range-example
- key_count: 2
  name: Google Slides Recolor Example
  slug: google-slides-recolor-example
- key_count: 1
  name: Google Slides Refresh Sheets Chart Request Example
  slug: google-slides-refresh-sheets-chart-request-example
- key_count: 3
  name: Google Slides Replace All Shapes With Image Request Example
  slug: google-slides-replace-all-shapes-with-image-request-example
- key_count: 1
  name: Google Slides Replace All Shapes With Image Response Example
  slug: google-slides-replace-all-shapes-with-image-response-example
- key_count: 4
  name: Google Slides Replace All Shapes With Sheets Chart Request Example
  slug: google-slides-replace-all-shapes-with-sheets-chart-request-example
- key_count: 1
  name: Google Slides Replace All Shapes With Sheets Chart Response Example
  slug: google-slides-replace-all-shapes-with-sheets-chart-response-example
- key_count: 2
  name: Google Slides Replace All Text Request Example
  slug: google-slides-replace-all-text-request-example
- key_count: 1
  name: Google Slides Replace All Text Response Example
  slug: google-slides-replace-all-text-response-example
- key_count: 3
  name: Google Slides Replace Image Request Example
  slug: google-slides-replace-image-request-example
- key_count: 0
  name: Google Slides Request Example
  slug: google-slides-request-example
- key_count: 1
  name: Google Slides Reroute Line Request Example
  slug: google-slides-reroute-line-request-example
- key_count: 0
  name: Google Slides Response Example
  slug: google-slides-response-example
- key_count: 3
  name: Google Slides Rgb Color Example
  slug: google-slides-rgb-color-example
- key_count: 5
  name: Google Slides Shadow Example
  slug: google-slides-shadow-example
- key_count: 1
  name: Google Slides Shape Background Fill Example
  slug: google-slides-shape-background-fill-example
- key_count: 1
  name: Google Slides Shape Example
  slug: google-slides-shape-example
- key_count: 1
  name: Google Slides Shape Properties Example
  slug: google-slides-shape-properties-example
- key_count: 3
  name: Google Slides Sheets Chart Example
  slug: google-slides-sheets-chart-example
- key_count: 0
  name: Google Slides Sheets Chart Properties Example
  slug: google-slides-sheets-chart-properties-example
- key_count: 0
  name: Google Slides Size Example
  slug: google-slides-size-example
- key_count: 3
  name: Google Slides Slide Properties Example
  slug: google-slides-slide-properties-example
- key_count: 1
  name: Google Slides Solid Fill Example
  slug: google-slides-solid-fill-example
- key_count: 0
  name: Google Slides Speaker Spotlight Example
  slug: google-slides-speaker-spotlight-example
- key_count: 0
  name: Google Slides Speaker Spotlight Properties Example
  slug: google-slides-speaker-spotlight-properties-example
- key_count: 1
  name: Google Slides Stretched Picture Fill Example
  slug: google-slides-stretched-picture-fill-example
- key_count: 2
  name: Google Slides Substring Match Criteria Example
  slug: google-slides-substring-match-criteria-example
- key_count: 0
  name: Google Slides Table Border Cell Example
  slug: google-slides-table-border-cell-example
- key_count: 0
  name: Google Slides Table Border Fill Example
  slug: google-slides-table-border-fill-example
- key_count: 1
  name: Google Slides Table Border Properties Example
  slug: google-slides-table-border-properties-example
- key_count: 1
  name: Google Slides Table Border Row Example
  slug: google-slides-table-border-row-example
- key_count: 1
  name: Google Slides Table Cell Background Fill Example
  slug: google-slides-table-cell-background-fill-example
- key_count: 2
  name: Google Slides Table Cell Example
  slug: google-slides-table-cell-example
- key_count: 2
  name: Google Slides Table Cell Location Example
  slug: google-slides-table-cell-location-example
- key_count: 1
  name: Google Slides Table Cell Properties Example
  slug: google-slides-table-cell-properties-example
- key_count: 0
  name: Google Slides Table Column Properties Example
  slug: google-slides-table-column-properties-example
- key_count: 6
  name: Google Slides Table Example
  slug: google-slides-table-example
- key_count: 2
  name: Google Slides Table Range Example
  slug: google-slides-table-range-example
- key_count: 1
  name: Google Slides Table Row Example
  slug: google-slides-table-row-example
- key_count: 0
  name: Google Slides Table Row Properties Example
  slug: google-slides-table-row-properties-example
- key_count: 2
  name: Google Slides Text Content Example
  slug: google-slides-text-content-example
- key_count: 2
  name: Google Slides Text Element Example
  slug: google-slides-text-element-example
- key_count: 1
  name: Google Slides Text Run Example
  slug: google-slides-text-run-example
- key_count: 7
  name: Google Slides Text Style Example
  slug: google-slides-text-style-example
- key_count: 1
  name: Google Slides Theme Color Pair Example
  slug: google-slides-theme-color-pair-example
- key_count: 3
  name: Google Slides Thumbnail Example
  slug: google-slides-thumbnail-example
- key_count: 1
  name: Google Slides Ungroup Objects Request Example
  slug: google-slides-ungroup-objects-request-example
- key_count: 1
  name: Google Slides Unmerge Table Cells Request Example
  slug: google-slides-unmerge-table-cells-request-example
- key_count: 2
  name: Google Slides Update Image Properties Request Example
  slug: google-slides-update-image-properties-request-example
- key_count: 2
  name: Google Slides Update Line Category Request Example
  slug: google-slides-update-line-category-request-example
- key_count: 2
  name: Google Slides Update Line Properties Request Example
  slug: google-slides-update-line-properties-request-example
- key_count: 3
  name: Google Slides Update Page Element Alt Text Request Example
  slug: google-slides-update-page-element-alt-text-request-example
- key_count: 2
  name: Google Slides Update Page Element Transform Request Example
  slug: google-slides-update-page-element-transform-request-example
- key_count: 2
  name: Google Slides Update Page Elements Z Order Request Example
  slug: google-slides-update-page-elements-z-order-request-example
- key_count: 2
  name: Google Slides Update Page Properties Request Example
  slug: google-slides-update-page-properties-request-example
- key_count: 2
  name: Google Slides Update Paragraph Style Request Example
  slug: google-slides-update-paragraph-style-request-example
- key_count: 2
  name: Google Slides Update Shape Properties Request Example
  slug: google-slides-update-shape-properties-request-example
- key_count: 2
  name: Google Slides Update Slide Properties Request Example
  slug: google-slides-update-slide-properties-request-example
- key_count: 2
  name: Google Slides Update Slides Position Request Example
  slug: google-slides-update-slides-position-request-example
- key_count: 3
  name: Google Slides Update Table Border Properties Request Example
  slug: google-slides-update-table-border-properties-request-example
- key_count: 2
  name: Google Slides Update Table Cell Properties Request Example
  slug: google-slides-update-table-cell-properties-request-example
- key_count: 3
  name: Google Slides Update Table Column Properties Request Example
  slug: google-slides-update-table-column-properties-request-example
- key_count: 3
  name: Google Slides Update Table Row Properties Request Example
  slug: google-slides-update-table-row-properties-request-example
- key_count: 2
  name: Google Slides Update Text Style Request Example
  slug: google-slides-update-text-style-request-example
- key_count: 2
  name: Google Slides Update Video Properties Request Example
  slug: google-slides-update-video-properties-request-example
- key_count: 3
  name: Google Slides Video Example
  slug: google-slides-video-example
- key_count: 4
  name: Google Slides Video Properties Example
  slug: google-slides-video-properties-example
- key_count: 2
  name: Google Slides Weighted Font Family Example
  slug: google-slides-weighted-font-family-example
- key_count: 1
  name: Google Slides Word Art Example
  slug: google-slides-word-art-example
- key_count: 1
  name: Google Slides Write Control Example
  slug: google-slides-write-control-example
features:
- description: Create blank or pre-configured presentations programmatically with custom titles and layouts.
  name: Presentation Creation
- description: Apply multiple changes to a presentation in a single atomic request for efficient editing.
  name: Batch Updates
- description: Add, reorder, duplicate, and delete slides within presentations.
  name: Slide Management
- description: Insert and format text, shapes, images, videos, tables, and charts on slides.
  name: Text and Shape Editing
- description: Generate thumbnail images of individual slides for previews and exports.
  name: Page Thumbnails
- description: Use existing presentations as templates and populate them with dynamic content.
  name: Template Support
finops:
- name: Google Slides Finops
  service_category: API
  slug: google-slides-finops
image: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
integrations:
- description: Embed live charts and data from Google Sheets into presentations for dynamic data visualization.
  name: Google Sheets
- description: Store, organize, and share presentations through Google Drive with collaboration permissions.
  name: Google Drive
- description: Part of the Google Workspace suite with seamless integration across Docs, Sheets, and other apps.
  name: Google Workspace
- description: Automate Slides workflows using Apps Script for custom macros and triggers.
  name: Google Apps Script
- description: Deploy Slides API integrations on Google Cloud Platform infrastructure.
  name: Google Cloud
json_schemas:
- name: AffineTransform
  property_count: 7
  slug: google-slides-affine-transform
- name: AutoText
  property_count: 2
  slug: google-slides-auto-text
- name: Autofit
  property_count: 2
  slug: google-slides-autofit
- name: BatchUpdatePresentationRequest
  property_count: 1
  slug: google-slides-batch-update-presentation-request
- name: BatchUpdatePresentationResponse
  property_count: 2
  slug: google-slides-batch-update-presentation-response
- name: Bullet
  property_count: 3
  slug: google-slides-bullet
- name: ColorScheme
  property_count: 1
  slug: google-slides-color-scheme
- name: ColorStop
  property_count: 2
  slug: google-slides-color-stop
- name: CreateImageRequest
  property_count: 2
  slug: google-slides-create-image-request
- name: CreateImageResponse
  property_count: 1
  slug: google-slides-create-image-response
- name: CreateLineRequest
  property_count: 3
  slug: google-slides-create-line-request
- name: CreateLineResponse
  property_count: 1
  slug: google-slides-create-line-response
- name: CreateParagraphBulletsRequest
  property_count: 2
  slug: google-slides-create-paragraph-bullets-request
- name: CreateShapeRequest
  property_count: 2
  slug: google-slides-create-shape-request
- name: CreateShapeResponse
  property_count: 1
  slug: google-slides-create-shape-response
- name: CreateSheetsChartRequest
  property_count: 4
  slug: google-slides-create-sheets-chart-request
- name: CreateSheetsChartResponse
  property_count: 1
  slug: google-slides-create-sheets-chart-response
- name: CreateSlideRequest
  property_count: 3
  slug: google-slides-create-slide-request
- name: CreateSlideResponse
  property_count: 1
  slug: google-slides-create-slide-response
- name: CreateTableRequest
  property_count: 3
  slug: google-slides-create-table-request
- name: CreateTableResponse
  property_count: 1
  slug: google-slides-create-table-response
- name: CreateVideoRequest
  property_count: 3
  slug: google-slides-create-video-request
- name: CreateVideoResponse
  property_count: 1
  slug: google-slides-create-video-response
- name: CropProperties
  property_count: 5
  slug: google-slides-crop-properties
- name: DeleteObjectRequest
  property_count: 1
  slug: google-slides-delete-object-request
- name: DeleteParagraphBulletsRequest
  property_count: 1
  slug: google-slides-delete-paragraph-bullets-request
- name: DeleteTableColumnRequest
  property_count: 1
  slug: google-slides-delete-table-column-request
- name: DeleteTableRowRequest
  property_count: 1
  slug: google-slides-delete-table-row-request
- name: DeleteTextRequest
  property_count: 1
  slug: google-slides-delete-text-request
- name: Dimension
  property_count: 2
  slug: google-slides-dimension
- name: DuplicateObjectRequest
  property_count: 2
  slug: google-slides-duplicate-object-request
- name: DuplicateObjectResponse
  property_count: 1
  slug: google-slides-duplicate-object-response
- name: ErrorResponse
  property_count: 1
  slug: google-slides-error-response
- name: GroupObjectsRequest
  property_count: 2
  slug: google-slides-group-objects-request
- name: GroupObjectsResponse
  property_count: 1
  slug: google-slides-group-objects-response
- name: Group
  property_count: 1
  slug: google-slides-group
- name: ImageProperties
  property_count: 3
  slug: google-slides-image-properties
- name: Image
  property_count: 2
  slug: google-slides-image
- name: InsertTableColumnsRequest
  property_count: 3
  slug: google-slides-insert-table-columns-request
- name: InsertTableRowsRequest
  property_count: 3
  slug: google-slides-insert-table-rows-request
- name: InsertTextRequest
  property_count: 3
  slug: google-slides-insert-text-request
- name: LayoutPlaceholderIdMapping
  property_count: 2
  slug: google-slides-layout-placeholder-id-mapping
- name: LayoutProperties
  property_count: 3
  slug: google-slides-layout-properties
- name: LayoutReference
  property_count: 2
  slug: google-slides-layout-reference
- name: LineConnection
  property_count: 2
  slug: google-slides-line-connection
- name: LineFill
  property_count: 0
  slug: google-slides-line-fill
- name: LineProperties
  property_count: 3
  slug: google-slides-line-properties
- name: Line
  property_count: 2
  slug: google-slides-line
- name: Link
  property_count: 4
  slug: google-slides-link
- name: List
  property_count: 2
  slug: google-slides-list
- name: MasterProperties
  property_count: 1
  slug: google-slides-master-properties
- name: MergeTableCellsRequest
  property_count: 1
  slug: google-slides-merge-table-cells-request
- name: NestingLevel
  property_count: 0
  slug: google-slides-nesting-level
- name: NotesProperties
  property_count: 1
  slug: google-slides-notes-properties
- name: OpaqueColor
  property_count: 1
  slug: google-slides-opaque-color
- name: OptionalColor
  property_count: 0
  slug: google-slides-optional-color
- name: OutlineFill
  property_count: 0
  slug: google-slides-outline-fill
- name: Outline
  property_count: 2
  slug: google-slides-outline
- name: PageBackgroundFill
  property_count: 1
  slug: google-slides-page-background-fill
- name: PageElementProperties
  property_count: 1
  slug: google-slides-page-element-properties
- name: PageElement
  property_count: 3
  slug: google-slides-page-element
- name: PageProperties
  property_count: 0
  slug: google-slides-page-properties
- name: Page
  property_count: 4
  slug: google-slides-page
- name: ParagraphMarker
  property_count: 0
  slug: google-slides-paragraph-marker
- name: ParagraphStyle
  property_count: 4
  slug: google-slides-paragraph-style
- name: Placeholder
  property_count: 3
  slug: google-slides-placeholder
- name: Presentation
  property_count: 7
  slug: google-slides-presentation
- name: Range
  property_count: 3
  slug: google-slides-range
- name: Recolor
  property_count: 2
  slug: google-slides-recolor
- name: RefreshSheetsChartRequest
  property_count: 1
  slug: google-slides-refresh-sheets-chart-request
- name: ReplaceAllShapesWithImageRequest
  property_count: 3
  slug: google-slides-replace-all-shapes-with-image-request
- name: ReplaceAllShapesWithImageResponse
  property_count: 1
  slug: google-slides-replace-all-shapes-with-image-response
- name: ReplaceAllShapesWithSheetsChartRequest
  property_count: 4
  slug: google-slides-replace-all-shapes-with-sheets-chart-request
- name: ReplaceAllShapesWithSheetsChartResponse
  property_count: 1
  slug: google-slides-replace-all-shapes-with-sheets-chart-response
- name: ReplaceAllTextRequest
  property_count: 2
  slug: google-slides-replace-all-text-request
- name: ReplaceAllTextResponse
  property_count: 1
  slug: google-slides-replace-all-text-response
- name: ReplaceImageRequest
  property_count: 3
  slug: google-slides-replace-image-request
- name: Request
  property_count: 0
  slug: google-slides-request
- name: RerouteLineRequest
  property_count: 1
  slug: google-slides-reroute-line-request
- name: Response
  property_count: 0
  slug: google-slides-response
- name: RgbColor
  property_count: 3
  slug: google-slides-rgb-color
- name: Shadow
  property_count: 5
  slug: google-slides-shadow
- name: ShapeBackgroundFill
  property_count: 1
  slug: google-slides-shape-background-fill
- name: ShapeProperties
  property_count: 1
  slug: google-slides-shape-properties
- name: Shape
  property_count: 1
  slug: google-slides-shape
- name: SheetsChartProperties
  property_count: 0
  slug: google-slides-sheets-chart-properties
- name: SheetsChart
  property_count: 3
  slug: google-slides-sheets-chart
- name: Size
  property_count: 0
  slug: google-slides-size
- name: SlideProperties
  property_count: 3
  slug: google-slides-slide-properties
- name: SolidFill
  property_count: 1
  slug: google-slides-solid-fill
- name: SpeakerSpotlightProperties
  property_count: 0
  slug: google-slides-speaker-spotlight-properties
- name: SpeakerSpotlight
  property_count: 0
  slug: google-slides-speaker-spotlight
- name: StretchedPictureFill
  property_count: 1
  slug: google-slides-stretched-picture-fill
- name: SubstringMatchCriteria
  property_count: 2
  slug: google-slides-substring-match-criteria
- name: TableBorderCell
  property_count: 0
  slug: google-slides-table-border-cell
- name: TableBorderFill
  property_count: 0
  slug: google-slides-table-border-fill
- name: TableBorderProperties
  property_count: 1
  slug: google-slides-table-border-properties
- name: TableBorderRow
  property_count: 1
  slug: google-slides-table-border-row
- name: TableCellBackgroundFill
  property_count: 1
  slug: google-slides-table-cell-background-fill
- name: TableCellLocation
  property_count: 2
  slug: google-slides-table-cell-location
- name: TableCellProperties
  property_count: 1
  slug: google-slides-table-cell-properties
- name: TableCell
  property_count: 2
  slug: google-slides-table-cell
- name: TableColumnProperties
  property_count: 0
  slug: google-slides-table-column-properties
- name: TableRange
  property_count: 2
  slug: google-slides-table-range
- name: TableRowProperties
  property_count: 0
  slug: google-slides-table-row-properties
- name: TableRow
  property_count: 1
  slug: google-slides-table-row
- name: Table
  property_count: 6
  slug: google-slides-table
- name: TextContent
  property_count: 2
  slug: google-slides-text-content
- name: TextElement
  property_count: 2
  slug: google-slides-text-element
- name: TextRun
  property_count: 1
  slug: google-slides-text-run
- name: TextStyle
  property_count: 7
  slug: google-slides-text-style
- name: ThemeColorPair
  property_count: 1
  slug: google-slides-theme-color-pair
- name: Thumbnail
  property_count: 3
  slug: google-slides-thumbnail
- name: UngroupObjectsRequest
  property_count: 1
  slug: google-slides-ungroup-objects-request
- name: UnmergeTableCellsRequest
  property_count: 1
  slug: google-slides-unmerge-table-cells-request
- name: UpdateImagePropertiesRequest
  property_count: 2
  slug: google-slides-update-image-properties-request
- name: UpdateLineCategoryRequest
  property_count: 2
  slug: google-slides-update-line-category-request
- name: UpdateLinePropertiesRequest
  property_count: 2
  slug: google-slides-update-line-properties-request
- name: UpdatePageElementAltTextRequest
  property_count: 3
  slug: google-slides-update-page-element-alt-text-request
- name: UpdatePageElementTransformRequest
  property_count: 2
  slug: google-slides-update-page-element-transform-request
- name: UpdatePageElementsZOrderRequest
  property_count: 2
  slug: google-slides-update-page-elements-z-order-request
- name: UpdatePagePropertiesRequest
  property_count: 2
  slug: google-slides-update-page-properties-request
- name: UpdateParagraphStyleRequest
  property_count: 2
  slug: google-slides-update-paragraph-style-request
- name: UpdateShapePropertiesRequest
  property_count: 2
  slug: google-slides-update-shape-properties-request
- name: UpdateSlidePropertiesRequest
  property_count: 2
  slug: google-slides-update-slide-properties-request
- name: UpdateSlidesPositionRequest
  property_count: 2
  slug: google-slides-update-slides-position-request
- name: UpdateTableBorderPropertiesRequest
  property_count: 3
  slug: google-slides-update-table-border-properties-request
- name: UpdateTableCellPropertiesRequest
  property_count: 2
  slug: google-slides-update-table-cell-properties-request
- name: UpdateTableColumnPropertiesRequest
  property_count: 3
  slug: google-slides-update-table-column-properties-request
- name: UpdateTableRowPropertiesRequest
  property_count: 3
  slug: google-slides-update-table-row-properties-request
- name: UpdateTextStyleRequest
  property_count: 2
  slug: google-slides-update-text-style-request
- name: UpdateVideoPropertiesRequest
  property_count: 2
  slug: google-slides-update-video-properties-request
- name: VideoProperties
  property_count: 4
  slug: google-slides-video-properties
- name: Video
  property_count: 3
  slug: google-slides-video
- name: WeightedFontFamily
  property_count: 2
  slug: google-slides-weighted-font-family
- name: WordArt
  property_count: 1
  slug: google-slides-word-art
- name: WriteControl
  property_count: 1
  slug: google-slides-write-control
json_structures:
- name: Google Slides Affine Transform Structure
  property_count: 7
  slug: google-slides-affine-transform-structure
- name: Google Slides Auto Text Structure
  property_count: 2
  slug: google-slides-auto-text-structure
- name: Google Slides Autofit Structure
  property_count: 2
  slug: google-slides-autofit-structure
- name: Google Slides Batch Update Presentation Request Structure
  property_count: 1
  slug: google-slides-batch-update-presentation-request-structure
- name: Google Slides Batch Update Presentation Response Structure
  property_count: 2
  slug: google-slides-batch-update-presentation-response-structure
- name: Google Slides Bullet Structure
  property_count: 3
  slug: google-slides-bullet-structure
- name: Google Slides Color Scheme Structure
  property_count: 1
  slug: google-slides-color-scheme-structure
- name: Google Slides Color Stop Structure
  property_count: 2
  slug: google-slides-color-stop-structure
- name: Google Slides Create Image Request Structure
  property_count: 2
  slug: google-slides-create-image-request-structure
- name: Google Slides Create Image Response Structure
  property_count: 1
  slug: google-slides-create-image-response-structure
- name: Google Slides Create Line Request Structure
  property_count: 3
  slug: google-slides-create-line-request-structure
- name: Google Slides Create Line Response Structure
  property_count: 1
  slug: google-slides-create-line-response-structure
- name: Google Slides Create Paragraph Bullets Request Structure
  property_count: 2
  slug: google-slides-create-paragraph-bullets-request-structure
- name: Google Slides Create Shape Request Structure
  property_count: 2
  slug: google-slides-create-shape-request-structure
- name: Google Slides Create Shape Response Structure
  property_count: 1
  slug: google-slides-create-shape-response-structure
- name: Google Slides Create Sheets Chart Request Structure
  property_count: 4
  slug: google-slides-create-sheets-chart-request-structure
- name: Google Slides Create Sheets Chart Response Structure
  property_count: 1
  slug: google-slides-create-sheets-chart-response-structure
- name: Google Slides Create Slide Request Structure
  property_count: 3
  slug: google-slides-create-slide-request-structure
- name: Google Slides Create Slide Response Structure
  property_count: 1
  slug: google-slides-create-slide-response-structure
- name: Google Slides Create Table Request Structure
  property_count: 3
  slug: google-slides-create-table-request-structure
- name: Google Slides Create Table Response Structure
  property_count: 1
  slug: google-slides-create-table-response-structure
- name: Google Slides Create Video Request Structure
  property_count: 3
  slug: google-slides-create-video-request-structure
- name: Google Slides Create Video Response Structure
  property_count: 1
  slug: google-slides-create-video-response-structure
- name: Google Slides Crop Properties Structure
  property_count: 5
  slug: google-slides-crop-properties-structure
- name: Google Slides Delete Object Request Structure
  property_count: 1
  slug: google-slides-delete-object-request-structure
- name: Google Slides Delete Paragraph Bullets Request Structure
  property_count: 1
  slug: google-slides-delete-paragraph-bullets-request-structure
- name: Google Slides Delete Table Column Request Structure
  property_count: 1
  slug: google-slides-delete-table-column-request-structure
- name: Google Slides Delete Table Row Request Structure
  property_count: 1
  slug: google-slides-delete-table-row-request-structure
- name: Google Slides Delete Text Request Structure
  property_count: 1
  slug: google-slides-delete-text-request-structure
- name: Google Slides Dimension Structure
  property_count: 2
  slug: google-slides-dimension-structure
- name: Google Slides Duplicate Object Request Structure
  property_count: 2
  slug: google-slides-duplicate-object-request-structure
- name: Google Slides Duplicate Object Response Structure
  property_count: 1
  slug: google-slides-duplicate-object-response-structure
- name: Google Slides Error Response Structure
  property_count: 1
  slug: google-slides-error-response-structure
- name: Google Slides Group Objects Request Structure
  property_count: 2
  slug: google-slides-group-objects-request-structure
- name: Google Slides Group Objects Response Structure
  property_count: 1
  slug: google-slides-group-objects-response-structure
- name: Google Slides Group Structure
  property_count: 1
  slug: google-slides-group-structure
- name: Google Slides Image Properties Structure
  property_count: 3
  slug: google-slides-image-properties-structure
- name: Google Slides Image Structure
  property_count: 2
  slug: google-slides-image-structure
- name: Google Slides Insert Table Columns Request Structure
  property_count: 3
  slug: google-slides-insert-table-columns-request-structure
- name: Google Slides Insert Table Rows Request Structure
  property_count: 3
  slug: google-slides-insert-table-rows-request-structure
- name: Google Slides Insert Text Request Structure
  property_count: 3
  slug: google-slides-insert-text-request-structure
- name: Google Slides Layout Placeholder Id Mapping Structure
  property_count: 2
  slug: google-slides-layout-placeholder-id-mapping-structure
- name: Google Slides Layout Properties Structure
  property_count: 3
  slug: google-slides-layout-properties-structure
- name: Google Slides Layout Reference Structure
  property_count: 2
  slug: google-slides-layout-reference-structure
- name: Google Slides Line Connection Structure
  property_count: 2
  slug: google-slides-line-connection-structure
- name: Google Slides Line Fill Structure
  property_count: 0
  slug: google-slides-line-fill-structure
- name: Google Slides Line Properties Structure
  property_count: 3
  slug: google-slides-line-properties-structure
- name: Google Slides Line Structure
  property_count: 2
  slug: google-slides-line-structure
- name: Google Slides Link Structure
  property_count: 4
  slug: google-slides-link-structure
- name: Google Slides List Structure
  property_count: 2
  slug: google-slides-list-structure
- name: Google Slides Master Properties Structure
  property_count: 1
  slug: google-slides-master-properties-structure
- name: Google Slides Merge Table Cells Request Structure
  property_count: 1
  slug: google-slides-merge-table-cells-request-structure
- name: Google Slides Nesting Level Structure
  property_count: 0
  slug: google-slides-nesting-level-structure
- name: Google Slides Notes Properties Structure
  property_count: 1
  slug: google-slides-notes-properties-structure
- name: Google Slides Opaque Color Structure
  property_count: 1
  slug: google-slides-opaque-color-structure
- name: Google Slides Optional Color Structure
  property_count: 0
  slug: google-slides-optional-color-structure
- name: Google Slides Outline Fill Structure
  property_count: 0
  slug: google-slides-outline-fill-structure
- name: Google Slides Outline Structure
  property_count: 2
  slug: google-slides-outline-structure
- name: Google Slides Page Background Fill Structure
  property_count: 1
  slug: google-slides-page-background-fill-structure
- name: Google Slides Page Element Properties Structure
  property_count: 1
  slug: google-slides-page-element-properties-structure
- name: Google Slides Page Element Structure
  property_count: 3
  slug: google-slides-page-element-structure
- name: Google Slides Page Properties Structure
  property_count: 0
  slug: google-slides-page-properties-structure
- name: Google Slides Page Structure
  property_count: 4
  slug: google-slides-page-structure
- name: Google Slides Paragraph Marker Structure
  property_count: 0
  slug: google-slides-paragraph-marker-structure
- name: Google Slides Paragraph Style Structure
  property_count: 4
  slug: google-slides-paragraph-style-structure
- name: Google Slides Placeholder Structure
  property_count: 3
  slug: google-slides-placeholder-structure
- name: Google Slides Presentation Structure
  property_count: 7
  slug: google-slides-presentation-structure
- name: Google Slides Range Structure
  property_count: 3
  slug: google-slides-range-structure
- name: Google Slides Recolor Structure
  property_count: 2
  slug: google-slides-recolor-structure
- name: Google Slides Refresh Sheets Chart Request Structure
  property_count: 1
  slug: google-slides-refresh-sheets-chart-request-structure
- name: Google Slides Replace All Shapes With Image Request Structure
  property_count: 3
  slug: google-slides-replace-all-shapes-with-image-request-structure
- name: Google Slides Replace All Shapes With Image Response Structure
  property_count: 1
  slug: google-slides-replace-all-shapes-with-image-response-structure
- name: Google Slides Replace All Shapes With Sheets Chart Request Structure
  property_count: 4
  slug: google-slides-replace-all-shapes-with-sheets-chart-request-structure
- name: Google Slides Replace All Shapes With Sheets Chart Response Structure
  property_count: 1
  slug: google-slides-replace-all-shapes-with-sheets-chart-response-structure
- name: Google Slides Replace All Text Request Structure
  property_count: 2
  slug: google-slides-replace-all-text-request-structure
- name: Google Slides Replace All Text Response Structure
  property_count: 1
  slug: google-slides-replace-all-text-response-structure
- name: Google Slides Replace Image Request Structure
  property_count: 3
  slug: google-slides-replace-image-request-structure
- name: Google Slides Request Structure
  property_count: 0
  slug: google-slides-request-structure
- name: Google Slides Reroute Line Request Structure
  property_count: 1
  slug: google-slides-reroute-line-request-structure
- name: Google Slides Response Structure
  property_count: 0
  slug: google-slides-response-structure
- name: Google Slides Rgb Color Structure
  property_count: 3
  slug: google-slides-rgb-color-structure
- name: Google Slides Shadow Structure
  property_count: 5
  slug: google-slides-shadow-structure
- name: Google Slides Shape Background Fill Structure
  property_count: 1
  slug: google-slides-shape-background-fill-structure
- name: Google Slides Shape Properties Structure
  property_count: 1
  slug: google-slides-shape-properties-structure
- name: Google Slides Shape Structure
  property_count: 1
  slug: google-slides-shape-structure
- name: Google Slides Sheets Chart Properties Structure
  property_count: 0
  slug: google-slides-sheets-chart-properties-structure
- name: Google Slides Sheets Chart Structure
  property_count: 3
  slug: google-slides-sheets-chart-structure
- name: Google Slides Size Structure
  property_count: 0
  slug: google-slides-size-structure
- name: Google Slides Slide Properties Structure
  property_count: 3
  slug: google-slides-slide-properties-structure
- name: Google Slides Solid Fill Structure
  property_count: 1
  slug: google-slides-solid-fill-structure
- name: Google Slides Speaker Spotlight Properties Structure
  property_count: 0
  slug: google-slides-speaker-spotlight-properties-structure
- name: Google Slides Speaker Spotlight Structure
  property_count: 0
  slug: google-slides-speaker-spotlight-structure
- name: Google Slides Stretched Picture Fill Structure
  property_count: 1
  slug: google-slides-stretched-picture-fill-structure
- name: Google Slides Substring Match Criteria Structure
  property_count: 2
  slug: google-slides-substring-match-criteria-structure
- name: Google Slides Table Border Cell Structure
  property_count: 0
  slug: google-slides-table-border-cell-structure
- name: Google Slides Table Border Fill Structure
  property_count: 0
  slug: google-slides-table-border-fill-structure
- name: Google Slides Table Border Properties Structure
  property_count: 1
  slug: google-slides-table-border-properties-structure
- name: Google Slides Table Border Row Structure
  property_count: 1
  slug: google-slides-table-border-row-structure
- name: Google Slides Table Cell Background Fill Structure
  property_count: 1
  slug: google-slides-table-cell-background-fill-structure
- name: Google Slides Table Cell Location Structure
  property_count: 2
  slug: google-slides-table-cell-location-structure
- name: Google Slides Table Cell Properties Structure
  property_count: 1
  slug: google-slides-table-cell-properties-structure
- name: Google Slides Table Cell Structure
  property_count: 2
  slug: google-slides-table-cell-structure
- name: Google Slides Table Column Properties Structure
  property_count: 0
  slug: google-slides-table-column-properties-structure
- name: Google Slides Table Range Structure
  property_count: 2
  slug: google-slides-table-range-structure
- name: Google Slides Table Row Properties Structure
  property_count: 0
  slug: google-slides-table-row-properties-structure
- name: Google Slides Table Row Structure
  property_count: 1
  slug: google-slides-table-row-structure
- name: Google Slides Table Structure
  property_count: 6
  slug: google-slides-table-structure
- name: Google Slides Text Content Structure
  property_count: 2
  slug: google-slides-text-content-structure
- name: Google Slides Text Element Structure
  property_count: 2
  slug: google-slides-text-element-structure
- name: Google Slides Text Run Structure
  property_count: 1
  slug: google-slides-text-run-structure
- name: Google Slides Text Style Structure
  property_count: 7
  slug: google-slides-text-style-structure
- name: Google Slides Theme Color Pair Structure
  property_count: 1
  slug: google-slides-theme-color-pair-structure
- name: Google Slides Thumbnail Structure
  property_count: 3
  slug: google-slides-thumbnail-structure
- name: Google Slides Ungroup Objects Request Structure
  property_count: 1
  slug: google-slides-ungroup-objects-request-structure
- name: Google Slides Unmerge Table Cells Request Structure
  property_count: 1
  slug: google-slides-unmerge-table-cells-request-structure
- name: Google Slides Update Image Properties Request Structure
  property_count: 2
  slug: google-slides-update-image-properties-request-structure
- name: Google Slides Update Line Category Request Structure
  property_count: 2
  slug: google-slides-update-line-category-request-structure
- name: Google Slides Update Line Properties Request Structure
  property_count: 2
  slug: google-slides-update-line-properties-request-structure
- name: Google Slides Update Page Element Alt Text Request Structure
  property_count: 3
  slug: google-slides-update-page-element-alt-text-request-structure
- name: Google Slides Update Page Element Transform Request Structure
  property_count: 2
  slug: google-slides-update-page-element-transform-request-structure
- name: Google Slides Update Page Elements Z Order Request Structure
  property_count: 2
  slug: google-slides-update-page-elements-z-order-request-structure
- name: Google Slides Update Page Properties Request Structure
  property_count: 2
  slug: google-slides-update-page-properties-request-structure
- name: Google Slides Update Paragraph Style Request Structure
  property_count: 2
  slug: google-slides-update-paragraph-style-request-structure
- name: Google Slides Update Shape Properties Request Structure
  property_count: 2
  slug: google-slides-update-shape-properties-request-structure
- name: Google Slides Update Slide Properties Request Structure
  property_count: 2
  slug: google-slides-update-slide-properties-request-structure
- name: Google Slides Update Slides Position Request Structure
  property_count: 2
  slug: google-slides-update-slides-position-request-structure
- name: Google Slides Update Table Border Properties Request Structure
  property_count: 3
  slug: google-slides-update-table-border-properties-request-structure
- name: Google Slides Update Table Cell Properties Request Structure
  property_count: 2
  slug: google-slides-update-table-cell-properties-request-structure
- name: Google Slides Update Table Column Properties Request Structure
  property_count: 3
  slug: google-slides-update-table-column-properties-request-structure
- name: Google Slides Update Table Row Properties Request Structure
  property_count: 3
  slug: google-slides-update-table-row-properties-request-structure
- name: Google Slides Update Text Style Request Structure
  property_count: 2
  slug: google-slides-update-text-style-request-structure
- name: Google Slides Update Video Properties Request Structure
  property_count: 2
  slug: google-slides-update-video-properties-request-structure
- name: Google Slides Video Properties Structure
  property_count: 4
  slug: google-slides-video-properties-structure
- name: Google Slides Video Structure
  property_count: 3
  slug: google-slides-video-structure
- name: Google Slides Weighted Font Family Structure
  property_count: 2
  slug: google-slides-weighted-font-family-structure
- name: Google Slides Word Art Structure
  property_count: 1
  slug: google-slides-word-art-structure
- name: Google Slides Write Control Structure
  property_count: 1
  slug: google-slides-write-control-structure
jsonld:
- class_count: 0
  name: Google Slides Context
  property_count: 0
  slug: google-slides-context
layout: provider
modified: '2026-05-19'
name: Google Slides
nav: Providers
network: true
overview: 'Google Slides publishes 2 APIs on the [APIs.io](https://apis.io/) network: Pages API and Presentations API. Tagged areas include Collaboration, Google Workspace, Presentations, Productivity, and Slides.


  The Google Slides catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Google Slides'' developer surface includes authentication, developer portal, getting-started guide, documentation, support, release notes, engineering blog, and 18 more developer resources.'
plans:
- name: Google Slides Plans Pricing
  plan_count: 3
  slug: google-slides-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Google Slides Rate Limits
  slug: google-slides-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Google Slides API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: google-slides-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Google Slides API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: google-slides-spectral-rules
scopes:
- name: Google Slides Scopes
  scope_count: 7
  slug: google-slides-scopes
  summary_line: 7 scopes · authorizationCode
score:
  band: strong
  composite: 55.8
  coverage:
    artifact_dirs: 18
    catalog_gap: 58.5
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.4
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 13.6
    contract_quality: 72.1
    developer_ergonomics: 61.9
    discoverability: 66.7
    governance: 13.6
    operational_transparency: 55.3
  open_source:
    applies: true
    score: 60.0
  previous_composite: 55.4
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 2
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/google-slides/refs/heads/main/screenshots/google-slides-2026-08-17T083628.png
security:
- kind: authentication
  name: Google Slides Authentication
  slug: google-slides-authentication
  summary_line: oauth2 · 1 scheme
- kind: domain-security
  name: Google Slides Domain Security
  slug: google-slides-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Google Slides Vulnerability Disclosure
  slug: google-slides-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: google-slides
tags:
- Collaboration
- Google Workspace
- Presentations
- Productivity
- Slides
use_cases:
- description: Generate presentation reports from data sources, populating charts, tables, and text automatically.
  name: Automated Report Generation
- description: Create branded presentations from templates, filling in customer-specific data for sales or marketing decks.
  name: Dynamic Presentation Templates
- description: Build educational slide decks programmatically from lesson plans, quizzes, or course materials.
  name: Educational Content Creation
- description: Automatically compile meeting agendas, status updates, and metrics into presentation format.
  name: Meeting Preparation
website: https://console.cloud.google.com/
---

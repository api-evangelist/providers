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
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: verified
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 63.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 34
  human_in_the_loop: 1
  name: Canva Agentic Access
  operation_count: 81
  slug: canva-agentic-access
  summary_line: 81 operations · 34 acting · 1 human-in-the-loop
api_count: 1
apis:
- description: Build apps that extend Canva's editor with custom functionality, content, and integrations.
  name: Canva Apps SDK
  slug: canva-apps-sdk
- description: Enables print service providers to integrate Canva design tools into their customer journey, allowing customers to create designs with Canva and print them from partner websites.
  name: Canva Print Partnerships API
  slug: canva-print-partnerships-api
- description: Enables embedding Canva design capabilities directly into websites and applications through HTML and JavaScript APIs for creating and editing designs.
  name: Canva Button API
  slug: canva-button-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Upload and manage image and video assets
  name: Canva Assets API
  phrasing_intents:
  - id: getAsset
    intent: Get an asset's details
    question: What is the import status and owner of one of my assets?
  - id: deleteAsset
    intent: Delete an asset
    question: Can I delete an image I uploaded to my Canva account?
  - id: createAssetUploadJob
    intent: Upload an image or video asset
    question: How do I upload an image or video to my Canva account?
  - id: getAssetUploadJob
    intent: Check an asset upload job
    question: Is my image upload done, and what asset did it create?
  phrasing_ops: 4
  slug: canva-assets-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Create designs from brand templates using autofill data
  name: Canva Autofills API
  phrasing_intents:
  - id: createDesignAutofillJob
    intent: Autofill a brand template with data
    question: How do I create a design by filling a brand template with text, images or chart data?
  - id: getDesignAutofillJob
    intent: Get an autofill job's result
    question: Is my template autofill finished?
  phrasing_ops: 2
  slug: canva-autofills-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: List and retrieve brand templates and their datasets
  name: Canva Brand Templates API
  phrasing_intents:
  - id: listBrandTemplates
    intent: List brand templates
    question: What brand templates can I use in my Canva account?
  - id: getBrandTemplate
    intent: Get a brand template
    question: How do I get the metadata for one brand template?
  - id: getBrandTemplateDataset
    intent: Get a brand template's dataset
    question: Which fields can I autofill in a brand template?
  phrasing_ops: 3
  slug: canva-brand-templates-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Create and manage comments on designs
  name: Canva Comments API
  phrasing_intents:
  - id: createComment
    intent: Add a top-level comment to a design
    question: How do I leave a new comment on a Canva design?
  - id: createReply
    intent: Reply to an existing comment
    question: How do I reply to an existing comment on a design?
  phrasing_ops: 2
  slug: canva-comments-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Create, retrieve, and list designs
  name: Canva Designs API
  phrasing_intents:
  - id: listDesigns
    intent: List designs I can access
    question: What designs can I access in Canva?
  - id: createDesign
    intent: Create a design
    question: How do I create a new doc, whiteboard or presentation?
  - id: getDesign
    intent: Get a design
    question: How many pages does a design have and when was it updated?
  phrasing_ops: 3
  slug: canva-designs-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Export designs to PDF, PNG, JPG, GIF, PPTX, and MP4
  name: Canva Exports API
  phrasing_intents:
  - id: createDesignExportJob
    intent: Export a design
    question: Can I export a design as MP4, GIF or PPTX?
  - id: getDesignExportJob
    intent: Get an export job
    question: Has my export finished, and where are the files?
  phrasing_ops: 2
  slug: canva-exports-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Retrieve folders and list folder contents
  name: Canva Folders API
  phrasing_intents:
  - id: getFolder
    intent: Get a folder
    question: How do I get a folder's name and thumbnail?
  - id: listFolderItems
    intent: List items in a folder
    question: What is inside one of my Canva folders?
  - id: moveFolderItem
    intent: Move an item into a folder
    question: How do I move a design, image or folder into a specific folder?
  phrasing_ops: 3
  slug: canva-folders-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Resize designs to different dimensions or preset types
  name: Canva Resizes API
  phrasing_intents:
  - id: createDesignResizeJob
    intent: Resize a design
    question: Can I resize a design to custom dimensions without changing the original?
  - id: getDesignResizeJob
    intent: Get a resize job's result
    question: Is my resize job done?
  phrasing_ops: 2
  slug: canva-resizes-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: Retrieve information about the authenticated user
  name: Canva Users API
  phrasing_intents:
  - id: getUsersMe
    intent: Get the current user
    question: Who is the currently authenticated Canva user?
  phrasing_ops: 1
  slug: canva-users-api
- baseURL: https://api.canva.com/rest/v1
  baseurl_source: declared
  description: The umbrella Canva Connect REST API as Canva publishes it — 59 operations across designs, assets, folders, brand templates, autofills, exports, resizes, imports, merges, comments, analytics, users, OA
  name: Canva Connect API
  phrasing_intents:
  - id: getSigningPublicKeys
    intent: Get keys to verify webhook signatures
    question: How do I verify that a webhook really came from Canva?
  phrasing_ops: 1
  slug: canva-connect-api
- description: SCIM 2.0 API for automating provisioning and deprovisioning of Canva user accounts and groups. Canva states it implements the SCIM v2 specification (RFC 7644). Available to Canva Enterprise single tea
  name: Canva SCIM API
  slug: canva-scim-api
- description: Partner-gated REST API for print order fulfilment. Uniquely bidirectional — Canva acts as the API CLIENT when sending orders to a print partner, and as the API SERVER when the partner sends order stat
  name: Canva Print API
  slug: canva-print-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The analytics API from Canva — 5 operation(s) for analytics.
  name: Canva Analytics API
  phrasing_intents:
  - id: getDesignAnalytics
    intent: Get overall view analytics for a design
    question: How many total views and unique viewers has my Canva design had?
  - id: getDesignAnalyticsViewers
    intent: List the people who viewed a design
    question: Who has viewed my design, most recent first?
  - id: getDesignAnalyticsViewsOverTime
    intent: Chart a design's views over time
    question: How have views on my design trended day by day?
  - id: getDesignAnalyticsPageViews
    intent: Get per-page view duration for a design
    question: Which pages of my presentation do viewers spend the most time on?
  - id: getDesignAnalyticsLinks
    intent: List trackable links for a design
    question: Which trackable share links exist for my design and how are they performing?
  phrasing_ops: 5
  slug: canva-analytics-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The app API from Canva — 1 operation(s) for app.
  name: Canva App API
  phrasing_intents:
  - id: getAppJwks
    intent: Get an app's public signing keys
    question: Where do I get the public keys to verify JWTs sent to my Canva app backend?
  phrasing_ops: 1
  slug: canva-app-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The asset API from Canva — 5 operation(s) for asset.
  name: Canva Asset API
  phrasing_intents:
  - id: deleteAsset
    intent: Delete an asset
    question: Can I remove an asset from my Canva library through the API?
  - id: getAsset
    intent: Get an asset's metadata
    question: How do I look up the name, tags and thumbnail of an uploaded asset?
  - id: updateAsset
    intent: Rename or retag an asset
    question: How do I rename an asset in my content library?
  - id: CreateAssetUploadJob
    intent: Upload a file as an asset
    question: How do I upload an image file from disk into a user's content library?
  - id: GetAssetUploadJob
    intent: Check a file asset upload job
    question: Has my file upload to Canva finished yet?
  - id: createUrlAssetUploadJob
    intent: Upload an asset from a URL
    question: Can I add an image to the content library straight from a public URL?
  - id: getUrlAssetUploadJob
    intent: Check a URL asset upload job
    question: Did my asset upload from a URL complete?
  phrasing_ops: 7
  slug: canva-asset-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The autofill API from Canva — 2 operation(s) for autofill.
  name: Canva Autofill API
  phrasing_intents:
  - id: createDesignAutofillJob
    intent: Autofill a brand template into a design
    question: How do I generate a new design by filling a brand template with my data?
  - id: getDesignAutofillJob
    intent: Check a design autofill job
    question: Has my autofill job produced the new design yet?
  phrasing_ops: 2
  slug: canva-autofill-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The brand_template API from Canva — 3 operation(s) for brand_template.
  name: Canva Brand Template API
  phrasing_intents:
  - id: listBrandTemplates
    intent: List brand templates
    question: Which brand templates does my team have?
  - id: publishBrandTemplate
    intent: Publish a design as a brand template
    question: How do I turn one of my designs into a brand template?
  - id: getBrandTemplate
    intent: Get a brand template
    question: How do I look up a single brand template's title and URLs?
  - id: getBrandTemplateDataset
    intent: Get a brand template's autofill fields
    question: What data fields does a brand template expect for autofill?
  phrasing_ops: 4
  slug: canva-brand-template-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The comment API from Canva — 5 operation(s) for comment.
  name: Canva Comment API
  phrasing_intents:
  - id: createComment
    intent: Add a top-level comment (deprecated)
    question: Can I still post a top-level comment with the older comments endpoint?
  - id: listReplies
    intent: List replies in a comment thread
    question: How do I see all the replies in a comment thread on my design?
  - id: createReply
    intent: Reply to a comment thread
    question: How do I respond to a comment someone left on my design?
  - id: getThread
    intent: Get a comment thread
    question: How do I fetch a single comment or suggestion thread on a design?
  - id: getReply
    intent: Get one reply in a comment thread
    question: Can I retrieve one specific reply within a comment thread?
  - id: createThread
    intent: Start a comment thread on a design
    question: How do I start a new comment thread on a design?
  phrasing_ops: 6
  slug: canva-comment-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The design API from Canva — 7 operation(s) for design.
  name: Canva Design API
  phrasing_intents:
  - id: listDesigns
    intent: List or search my designs
    question: How do I list all the designs in my Canva projects?
  - id: createDesign
    intent: Create a new design
    question: How do I create a blank presentation or custom-size design?
  - id: getDesign
    intent: Get a design's metadata
    question: How do I get the edit and view URLs for a design?
  - id: getDesignPages
    intent: List the pages in a design
    question: Can I get thumbnails for each page of a design?
  - id: getDesignExportFormats
    intent: List export formats available for a design
    question: Which file formats can I export this design to?
  - id: getDesignDataset
    intent: Get a design's autofill data fields
    question: Does my design contain autofill data fields, and what types do they take?
  - id: createPrintPartnerDesign
    intent: Create a design for a print product
    question: As a print partner, how do I create a design from a product ID?
  - id: getPrintPartnerDesign
    intent: Get a print partner design with proofing
    question: How does a print partner fetch a design's URLs with proofing settings applied?
  phrasing_ops: 8
  slug: canva-design-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The design_import API from Canva — 4 operation(s) for design_import.
  name: Canva Design Import API
  phrasing_intents:
  - id: createDesignImportJob
    intent: Import an uploaded file as a design
    question: How do I turn a PDF or PowerPoint file into an editable Canva design?
  - id: getDesignImportJob
    intent: Check a file import job
    question: Has my uploaded file finished importing as a design?
  - id: createUrlImportJob
    intent: Import a file from a URL as a design
    question: Can Canva import a presentation from a link instead of an upload?
  - id: getUrlImportJob
    intent: Check a URL import job
    question: Is my import from a URL done yet?
  phrasing_ops: 4
  slug: canva-design-import-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The export API from Canva — 3 operation(s) for export.
  name: Canva Export API
  phrasing_intents:
  - id: createDesignExportJob
    intent: Export a design to a file
    question: How do I export a Canva design as a PDF or PNG?
  - id: createPrintPartnerDesignExportJob
    intent: Export a print-ready file for a print partner
    question: As a print partner, how do I export a print-ready file of a customer design?
  - id: getDesignExportJob
    intent: Get an export job's download links
    question: Is my design export ready to download?
  phrasing_ops: 3
  slug: canva-export-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The folder API from Canva — 4 operation(s) for folder.
  name: Canva Folder API
  phrasing_intents:
  - id: deleteFolder
    intent: Delete a folder
    question: What happens to the contents when I delete a folder?
  - id: getFolder
    intent: Get a folder's details
    question: How do I look up a folder's name by its ID?
  - id: updateFolder
    intent: Rename a folder
    question: How do I rename a folder?
  - id: listFolderItems
    intent: List the contents of a folder
    question: What designs, images and subfolders are inside a folder?
  - id: moveFolderItem
    intent: Move an item to another folder
    question: How do I move a design into a different folder?
  - id: createFolder
    intent: Create a folder
    question: How do I create a new folder in my Canva projects?
  phrasing_ops: 6
  slug: canva-folder-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The merge API from Canva — 2 operation(s) for merge.
  name: Canva Merge API
  phrasing_intents:
  - id: createDesignMergeJob
    intent: Merge design pages into a design
    question: How do I combine pages from several designs into one?
  - id: getDesignMergeJob
    intent: Check a design merge job
    question: Has my page merge finished?
  phrasing_ops: 2
  slug: canva-merge-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The oidc API from Canva — 2 operation(s) for oidc.
  name: Canva Oidc API
  phrasing_intents:
  - id: getOidcJwks
    intent: Get the OIDC public keys
    question: Where are the public keys for verifying OpenID Connect ID tokens?
  - id: userInfo
    intent: Get the signed-in user's OIDC claims
    question: How do I get the signed-in user's name and email via OpenID Connect?
  phrasing_ops: 2
  slug: canva-oidc-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The resize API from Canva — 2 operation(s) for resize.
  name: Canva Resize API
  phrasing_intents:
  - id: createDesignResizeJob
    intent: Resize a design into a new copy
    question: How do I resize a design to a different format like a presentation?
  - id: getDesignResizeJob
    intent: Check a design resize job
    question: Has my design resize completed?
  phrasing_ops: 2
  slug: canva-resize-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The user API from Canva — 3 operation(s) for user.
  name: Canva User API
  phrasing_intents:
  - id: usersMe
    intent: Get my user and team IDs
    question: How do I find the user ID and team ID behind an access token?
  - id: getUserCapabilities
    intent: List the API capabilities of my account
    question: Which API features is the connected user allowed to use?
  - id: getUserProfile
    intent: Get my display name
    question: How do I get the display name of the connected user?
  phrasing_ops: 3
  slug: canva-user-api
- baseURL: https://api.canva.com
  baseurl_source: declared
  description: The OAuth API from Canva — 3 operation(s) for oauth.
  name: Canva O Auth API
  phrasing_intents:
  - id: exchangeAccessToken
    intent: Get an access token via OAuth
    question: How do I exchange an authorization code for an access token?
  - id: introspectToken
    intent: Check whether a token is active
    question: How do I check if an access token is still valid?
  - id: revokeTokens
    intent: Revoke an access or refresh token
    question: How do I revoke a user's token when they disconnect my integration?
  phrasing_ops: 3
  slug: canva-oauth-api
artifact_total: 259
asyncapis:
- description: ''
  name: Canva Webhooks
  slug: canva-webhooks
collections:
- collection_type: postman
  name: Canva Connect Assets API
  slug: postman-canva-assets-api
- collection_type: postman
  name: Canva Connect Assets Autofills API
  slug: postman-canva-autofills-api
- collection_type: postman
  name: Canva Connect Assets Brand Templates API
  slug: postman-canva-brand-templates-api
- collection_type: postman
  name: Canva Connect Assets Comments API
  slug: postman-canva-comments-api
- collection_type: postman
  name: Canva Connect Assets Designs API
  slug: postman-canva-designs-api
- collection_type: postman
  name: Canva Connect Assets Exports API
  slug: postman-canva-exports-api
- collection_type: postman
  name: Canva Connect Assets Folders API
  slug: postman-canva-folders-api
- collection_type: postman
  name: Canva Connect Assets Resizes API
  slug: postman-canva-resizes-api
- collection_type: postman
  name: Canva Connect Assets Users API
  slug: postman-canva-users-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Canva Connect Assets API
  slug: open-canva-assets-api
- collection_type: open
  name: Canva Connect Assets Autofills API
  slug: open-canva-autofills-api
- collection_type: open
  name: Canva Connect Assets Brand Templates API
  slug: open-canva-brand-templates-api
- collection_type: open
  name: Canva Connect Assets Comments API
  slug: open-canva-comments-api
- collection_type: open
  name: Canva Connect API
  slug: open-canva-connect-api
- collection_type: open
  name: Canva Connect Assets Designs API
  slug: open-canva-designs-api
- collection_type: open
  name: Canva Connect Assets Exports API
  slug: open-canva-exports-api
- collection_type: open
  name: Canva Connect Assets Folders API
  slug: open-canva-folders-api
- collection_type: open
  name: Canva Connect Assets Resizes API
  slug: open-canva-resizes-api
- collection_type: open
  name: Canva Connect Assets Users API
  slug: open-canva-users-api
common:
- group: company
  title: ''
  type: Website
  url: https://canva.dev
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/canva/overview
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/agentic-access/canva-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/canva-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/security/canva-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/canva-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/security/canva-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/canva-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/security/canva-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/canva-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/authentication/canva-authentication.yml
  title: ''
  type: Authentication
  url: authentication/canva-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/scopes/canva-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/canva-scopes.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/canva
- group: start
  title: ''
  type: DeveloperPortal
  url: https://www.canva.com/developers/
- group: auth
  title: ''
  type: Authentication
  url: https://www.canva.com/developers/docs/authentication/
- group: operate
  title: ''
  type: Support
  url: https://www.canva.com/developers/support/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.canva.com/policies/developer-terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.canva.com/policies/privacy-policy/
- group: docs
  title: Community
  type: Documentation
  url: https://community.canva.com/developers
- group: company
  title: ''
  type: Blog
  url: https://www.canva.com/newsroom/developers/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.canva.com/
- group: docs
  title: Developer Documentation
  type: Documentation
  url: https://www.canva.dev/docs/
- group: docs
  title: Developer Community
  type: Documentation
  url: https://community.canva.dev/
- group: docs
  title: ''
  type: OpenAPI
  url: https://www.canva.dev/sources/connect/api/latest/api.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/canva-sdks
- group: docs
  title: Postman Collection
  type: Documentation
  url: https://www.postman.com/canva-developers/canva-developers/collection/oi7dfns/canva-connect-api
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.canva.dev/docs/connect/changelog/
- group: auth
  title: ''
  type: Security
  url: https://www.canva.dev/docs/connect/guidelines/security/
- group: operate
  title: ''
  type: RateLimits
  url: https://www.canva.dev/docs/connect/api-requests-responses/
- group: company
  title: Developer Blog
  type: Blog
  url: https://www.canva.dev/blog/developers/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.canva.dev/blog/developers/feed.xml
- group: commercial
  title: Developer Terms
  type: TermsOfService
  url: https://www.canva.com/policies/canva-developer-terms/
- group: commercial
  title: Acceptable Use Policy
  type: Legal
  url: https://www.canva.com/policies/acceptable-use-policy/
- group: commercial
  title: Terms of Use
  type: TermsOfService
  url: https://www.canva.com/policies/terms-of-use/
- group: docs
  title: Premium Apps Program
  type: Documentation
  url: https://www.canva.com/developers/premium-apps-program/
- group: docs
  title: Innovation Fund
  type: Documentation
  url: https://www.canva.dev/docs/apps/innovation-fund/
- group: docs
  title: Deprecation Policy
  type: Documentation
  url: https://www.canva.dev/docs/extensions/platform-concepts/deprecation-policy/
- group: operate
  title: Help Center
  type: FAQ
  url: https://www.canva.com/help/canva-api/
- group: other
  title: ''
  type: Events
  url: https://www.canva.com/canva-extend/
- group: build
  title: ''
  type: CLI
  url: https://www.npmjs.com/package/@canva/cli
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/rules/canva-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/canva-spectral-rules.yml
- group: agent
  title: ''
  type: AgentSkills
  url: https://github.com/canva-sdks/canva-claude-skills
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/packages/canva-packages.yml
  title: ''
  type: Packages
  url: packages/canva-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/packages/canva-packages.yml
  title: ''
  type: SDKs
  url: packages/canva-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/well-known/canva-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/canva-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/well-known/canva-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/canva-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/security/canva-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/canva-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/security/canva-trust-center.yml
  title: ''
  type: Compliance
  url: security/canva-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/conformance/canva-conformance.yml
  title: ''
  type: Conformance
  url: conformance/canva-conformance.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/mcp/canva-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/canva-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/mcp/canva-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/canva-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/llms/canva-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/canva-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/conventions/canva-conventions.yml
  title: ''
  type: Conventions
  url: conventions/canva-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/errors/canva-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/canva-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/lifecycle/canva-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/canva-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/lifecycle/canva-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/canva-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://www.canvastatus.com/
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/changelog/canva-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/canva-changelog.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/rate-limits/canva-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/canva-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/plans/canva-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/canva-plans-pricing.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/finops/canva-finops.yml
  title: ''
  type: FinOps
  url: finops/canva-finops.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/cli/canva-cli.yml
  title: ''
  type: CLI
  url: cli/canva-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/components/canva-components.yml
  title: ''
  type: Components
  url: components/canva-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/data-model/canva-data-model.yml
  title: ''
  type: DataModel
  url: data-model/canva-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/asyncapi/canva-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/canva-webhooks.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/overlays/canva-connect-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/canva-connect-api-overlay.yaml
- group: docs
  title: ''
  type: APIReference
  url: https://www.canva.dev/docs/connect/api-reference/designs/create-design/
- group: start
  title: ''
  type: GettingStarted
  url: https://www.canva.dev/docs/connect/quickstart/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.canva.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://www.canva.dev/docs/audit-logs/
- group: docs
  title: ''
  type: Documentation
  url: https://www.canva.dev/docs/print/
created: '2024-01-01'
description: 'Canva is the visual design platform used by hundreds of millions of people, and it exposes four distinct developer surfaces: the Connect APIs (a REST API for creating, autofilling, exporting, resizing, importing and commenting on designs from another application), the Apps SDK (React apps that run inside the Canva editor), the SCIM and Audit Logs APIs for enterprise identity and compliance, and the partner-gated Print API. Canva publishes its own OpenAPI description, a dated changelog, per-product llms.txt indexes, a hosted MCP server and a public set of Agent Skills.'
examples:
- key_count: 6
  name: Canva Connect Asset Example
  slug: canva-connect-asset-example
- key_count: 0
  name: Canva Connect Asset Response Example
  slug: canva-connect-asset-response-example
- key_count: 1
  name: Canva Connect Asset Upload Job Response Example
  slug: canva-connect-asset-upload-job-response-example
- key_count: 2
  name: Canva Connect Autofill Chart Value Example
  slug: canva-connect-autofill-chart-value-example
- key_count: 0
  name: Canva Connect Autofill Data Value Example
  slug: canva-connect-autofill-data-value-example
- key_count: 2
  name: Canva Connect Autofill Image Value Example
  slug: canva-connect-autofill-image-value-example
- key_count: 4
  name: Canva Connect Autofill Job Example
  slug: canva-connect-autofill-job-example
- key_count: 0
  name: Canva Connect Autofill Job Response Example
  slug: canva-connect-autofill-job-response-example
- key_count: 2
  name: Canva Connect Autofill Text Value Example
  slug: canva-connect-autofill-text-value-example
- key_count: 1
  name: Canva Connect Brand Template Dataset Response Example
  slug: canva-connect-brand-template-dataset-response-example
- key_count: 6
  name: Canva Connect Brand Template Example
  slug: canva-connect-brand-template-example
- key_count: 0
  name: Canva Connect Brand Template Response Example
  slug: canva-connect-brand-template-response-example
- key_count: 2
  name: Canva Connect Comment Attachment Example
  slug: canva-connect-comment-attachment-example
- key_count: 6
  name: Canva Connect Comment Example
  slug: canva-connect-comment-example
- key_count: 0
  name: Canva Connect Comment Response Example
  slug: canva-connect-comment-response-example
- key_count: 2
  name: Canva Connect Comment User Example
  slug: canva-connect-comment-user-example
- key_count: 3
  name: Canva Connect Create Autofill Job Request Example
  slug: canva-connect-create-autofill-job-request-example
- key_count: 2
  name: Canva Connect Create Comment Request Example
  slug: canva-connect-create-comment-request-example
- key_count: 2
  name: Canva Connect Create Design Request Example
  slug: canva-connect-create-design-request-example
- key_count: 1
  name: Canva Connect Create Export Job Request Example
  slug: canva-connect-create-export-job-request-example
- key_count: 1
  name: Canva Connect Create Reply Request Example
  slug: canva-connect-create-reply-request-example
- key_count: 1
  name: Canva Connect Create Resize Job Request Example
  slug: canva-connect-create-resize-job-request-example
- key_count: 3
  name: Canva Connect Custom Design Type Example
  slug: canva-connect-custom-design-type-example
- key_count: 1
  name: Canva Connect Dataset Field Example
  slug: canva-connect-dataset-field-example
- key_count: 5
  name: Canva Connect Design Example
  slug: canva-connect-design-example
- key_count: 0
  name: Canva Connect Design Response Example
  slug: canva-connect-design-response-example
- key_count: 0
  name: Canva Connect Design Type Example
  slug: canva-connect-design-type-example
- key_count: 2
  name: Canva Connect Design Urls Example
  slug: canva-connect-design-urls-example
- key_count: 2
  name: Canva Connect Error Example
  slug: canva-connect-error-example
- key_count: 2
  name: Canva Connect Export Error Example
  slug: canva-connect-export-error-example
- key_count: 0
  name: Canva Connect Export Format Example
  slug: canva-connect-export-format-example
- key_count: 3
  name: Canva Connect Export Job Example
  slug: canva-connect-export-job-example
- key_count: 0
  name: Canva Connect Export Job Response Example
  slug: canva-connect-export-job-response-example
- key_count: 4
  name: Canva Connect Folder Example
  slug: canva-connect-folder-example
- key_count: 1
  name: Canva Connect Folder Item Example
  slug: canva-connect-folder-item-example
- key_count: 0
  name: Canva Connect Folder Response Example
  slug: canva-connect-folder-response-example
- key_count: 5
  name: Canva Connect Gif Export Format Example
  slug: canva-connect-gif-export-format-example
- key_count: 2
  name: Canva Connect Import Status Example
  slug: canva-connect-import-status-example
- key_count: 6
  name: Canva Connect Jpg Export Format Example
  slug: canva-connect-jpg-export-format-example
- key_count: 2
  name: Canva Connect List Brand Templates Response Example
  slug: canva-connect-list-brand-templates-response-example
- key_count: 2
  name: Canva Connect List Designs Response Example
  slug: canva-connect-list-designs-response-example
- key_count: 2
  name: Canva Connect List Folder Items Response Example
  slug: canva-connect-list-folder-items-response-example
- key_count: 3
  name: Canva Connect Mentioned User Example
  slug: canva-connect-mentioned-user-example
- key_count: 2
  name: Canva Connect Move Folder Item Request Example
  slug: canva-connect-move-folder-item-request-example
- key_count: 4
  name: Canva Connect Mp4 Export Format Example
  slug: canva-connect-mp4-export-format-example
- key_count: 2
  name: Canva Connect Owner Example
  slug: canva-connect-owner-example
- key_count: 4
  name: Canva Connect Pdf Export Format Example
  slug: canva-connect-pdf-export-format-example
- key_count: 8
  name: Canva Connect Png Export Format Example
  slug: canva-connect-png-export-format-example
- key_count: 2
  name: Canva Connect Pptx Export Format Example
  slug: canva-connect-pptx-export-format-example
- key_count: 2
  name: Canva Connect Preset Design Type Example
  slug: canva-connect-preset-design-type-example
- key_count: 4
  name: Canva Connect Resize Job Example
  slug: canva-connect-resize-job-example
- key_count: 0
  name: Canva Connect Resize Job Response Example
  slug: canva-connect-resize-job-response-example
- key_count: 2
  name: Canva Connect Team User Example
  slug: canva-connect-team-user-example
- key_count: 3
  name: Canva Connect Thumbnail Example
  slug: canva-connect-thumbnail-example
- key_count: 0
  name: Canva Connect Users Me Response Example
  slug: canva-connect-users-me-response-example
features:
- description: Create and manage Canva designs programmatically from external applications.
  name: Design Creation
- description: Upload, retrieve, and manage image and video assets within Canva.
  name: Asset Management
- description: Access and list brand templates with dataset definitions for consistent brand content.
  name: Brand Templates
- description: Automatically populate brand templates with dynamic data for bulk content creation.
  name: Design Autofill
- description: Export designs to PDF, PNG, JPG, GIF, PPTX, and MP4 formats.
  name: Design Export
- description: Resize designs to different dimensions or preset types for multi-channel publishing.
  name: Design Resize
- description: Organize designs into folders with move, list, and retrieval capabilities.
  name: Folder Organization
- description: Create and manage comments on designs for team review and feedback workflows.
  name: Comments and Collaboration
- description: Receive real-time notifications for design events via webhook subscriptions.
  name: Webhooks
- description: Build custom apps that extend the Canva editor with new functionality and content.
  name: Apps SDK
finops:
- name: Canva Finops
  service_category: Design SaaS
  slug: canva-finops
image: https://www.canva.com/favicon.ico
integrations:
- description: Share Canva designs directly to Slack channels for team review and approval.
  name: Slack
- description: Save and sync Canva designs with Google Drive for file management.
  name: Google Drive
- description: Connect Canva with Dropbox for cloud storage and asset management.
  name: Dropbox
- description: Create marketing visuals within HubSpot using Canva design capabilities.
  name: HubSpot
- description: Design product images and marketing materials for Shopify stores.
  name: Shopify
- description: Create and embed Canva designs directly into WordPress posts and pages.
  name: WordPress
json_schemas:
- name: AssetResponse
  property_count: 0
  slug: canva-connect-asset-response
- name: Asset
  property_count: 6
  slug: canva-connect-asset
- name: AssetUploadJobResponse
  property_count: 1
  slug: canva-connect-asset-upload-job-response
- name: AutofillChartValue
  property_count: 2
  slug: canva-connect-autofill-chart-value
- name: AutofillDataValue
  property_count: 0
  slug: canva-connect-autofill-data-value
- name: AutofillImageValue
  property_count: 2
  slug: canva-connect-autofill-image-value
- name: AutofillJobResponse
  property_count: 0
  slug: canva-connect-autofill-job-response
- name: AutofillJob
  property_count: 4
  slug: canva-connect-autofill-job
- name: AutofillTextValue
  property_count: 2
  slug: canva-connect-autofill-text-value
- name: BrandTemplateDatasetResponse
  property_count: 1
  slug: canva-connect-brand-template-dataset-response
- name: BrandTemplateResponse
  property_count: 0
  slug: canva-connect-brand-template-response
- name: BrandTemplate
  property_count: 6
  slug: canva-connect-brand-template
- name: CommentAttachment
  property_count: 2
  slug: canva-connect-comment-attachment
- name: CommentResponse
  property_count: 0
  slug: canva-connect-comment-response
- name: Comment
  property_count: 6
  slug: canva-connect-comment
- name: CommentUser
  property_count: 2
  slug: canva-connect-comment-user
- name: CreateAutofillJobRequest
  property_count: 3
  slug: canva-connect-create-autofill-job-request
- name: CreateCommentRequest
  property_count: 2
  slug: canva-connect-create-comment-request
- name: CreateDesignRequest
  property_count: 2
  slug: canva-connect-create-design-request
- name: CreateExportJobRequest
  property_count: 1
  slug: canva-connect-create-export-job-request
- name: CreateReplyRequest
  property_count: 1
  slug: canva-connect-create-reply-request
- name: CreateResizeJobRequest
  property_count: 1
  slug: canva-connect-create-resize-job-request
- name: CustomDesignType
  property_count: 3
  slug: canva-connect-custom-design-type
- name: DatasetField
  property_count: 1
  slug: canva-connect-dataset-field
- name: DesignResponse
  property_count: 0
  slug: canva-connect-design-response
- name: Design
  property_count: 5
  slug: canva-connect-design
- name: DesignType
  property_count: 0
  slug: canva-connect-design-type
- name: DesignUrls
  property_count: 2
  slug: canva-connect-design-urls
- name: Error
  property_count: 2
  slug: canva-connect-error
- name: ExportError
  property_count: 2
  slug: canva-connect-export-error
- name: ExportFormat
  property_count: 0
  slug: canva-connect-export-format
- name: ExportJobResponse
  property_count: 0
  slug: canva-connect-export-job-response
- name: ExportJob
  property_count: 3
  slug: canva-connect-export-job
- name: FolderItem
  property_count: 1
  slug: canva-connect-folder-item
- name: FolderResponse
  property_count: 0
  slug: canva-connect-folder-response
- name: Folder
  property_count: 4
  slug: canva-connect-folder
- name: GifExportFormat
  property_count: 5
  slug: canva-connect-gif-export-format
- name: ImportStatus
  property_count: 2
  slug: canva-connect-import-status
- name: JpgExportFormat
  property_count: 6
  slug: canva-connect-jpg-export-format
- name: ListBrandTemplatesResponse
  property_count: 2
  slug: canva-connect-list-brand-templates-response
- name: ListDesignsResponse
  property_count: 2
  slug: canva-connect-list-designs-response
- name: ListFolderItemsResponse
  property_count: 2
  slug: canva-connect-list-folder-items-response
- name: MentionedUser
  property_count: 3
  slug: canva-connect-mentioned-user
- name: MoveFolderItemRequest
  property_count: 2
  slug: canva-connect-move-folder-item-request
- name: Mp4ExportFormat
  property_count: 4
  slug: canva-connect-mp4-export-format
- name: Owner
  property_count: 2
  slug: canva-connect-owner
- name: PdfExportFormat
  property_count: 4
  slug: canva-connect-pdf-export-format
- name: PngExportFormat
  property_count: 8
  slug: canva-connect-png-export-format
- name: PptxExportFormat
  property_count: 2
  slug: canva-connect-pptx-export-format
- name: PresetDesignType
  property_count: 2
  slug: canva-connect-preset-design-type
- name: ResizeJobResponse
  property_count: 0
  slug: canva-connect-resize-job-response
- name: ResizeJob
  property_count: 4
  slug: canva-connect-resize-job
- name: TeamUser
  property_count: 2
  slug: canva-connect-team-user
- name: Thumbnail
  property_count: 3
  slug: canva-connect-thumbnail
- name: UsersMeResponse
  property_count: 0
  slug: canva-connect-users-me-response
- name: Canva Connect API Core Models
  property_count: 0
  slug: canva-design
json_structures:
- name: Canva Connect Asset Response Structure
  property_count: 0
  slug: canva-connect-asset-response-structure
- name: Canva Connect Asset Structure
  property_count: 6
  slug: canva-connect-asset-structure
- name: Canva Connect Asset Upload Job Response Structure
  property_count: 1
  slug: canva-connect-asset-upload-job-response-structure
- name: Canva Connect Autofill Chart Value Structure
  property_count: 2
  slug: canva-connect-autofill-chart-value-structure
- name: Canva Connect Autofill Data Value Structure
  property_count: 0
  slug: canva-connect-autofill-data-value-structure
- name: Canva Connect Autofill Image Value Structure
  property_count: 2
  slug: canva-connect-autofill-image-value-structure
- name: Canva Connect Autofill Job Response Structure
  property_count: 0
  slug: canva-connect-autofill-job-response-structure
- name: Canva Connect Autofill Job Structure
  property_count: 4
  slug: canva-connect-autofill-job-structure
- name: Canva Connect Autofill Text Value Structure
  property_count: 2
  slug: canva-connect-autofill-text-value-structure
- name: Canva Connect Brand Template Dataset Response Structure
  property_count: 1
  slug: canva-connect-brand-template-dataset-response-structure
- name: Canva Connect Brand Template Response Structure
  property_count: 0
  slug: canva-connect-brand-template-response-structure
- name: Canva Connect Brand Template Structure
  property_count: 6
  slug: canva-connect-brand-template-structure
- name: Canva Connect Comment Attachment Structure
  property_count: 2
  slug: canva-connect-comment-attachment-structure
- name: Canva Connect Comment Response Structure
  property_count: 0
  slug: canva-connect-comment-response-structure
- name: Canva Connect Comment Structure
  property_count: 6
  slug: canva-connect-comment-structure
- name: Canva Connect Comment User Structure
  property_count: 2
  slug: canva-connect-comment-user-structure
- name: Canva Connect Create Autofill Job Request Structure
  property_count: 3
  slug: canva-connect-create-autofill-job-request-structure
- name: Canva Connect Create Comment Request Structure
  property_count: 2
  slug: canva-connect-create-comment-request-structure
- name: Canva Connect Create Design Request Structure
  property_count: 2
  slug: canva-connect-create-design-request-structure
- name: Canva Connect Create Export Job Request Structure
  property_count: 1
  slug: canva-connect-create-export-job-request-structure
- name: Canva Connect Create Reply Request Structure
  property_count: 1
  slug: canva-connect-create-reply-request-structure
- name: Canva Connect Create Resize Job Request Structure
  property_count: 1
  slug: canva-connect-create-resize-job-request-structure
- name: Canva Connect Custom Design Type Structure
  property_count: 3
  slug: canva-connect-custom-design-type-structure
- name: Canva Connect Dataset Field Structure
  property_count: 1
  slug: canva-connect-dataset-field-structure
- name: Canva Connect Design Response Structure
  property_count: 0
  slug: canva-connect-design-response-structure
- name: Canva Connect Design Structure
  property_count: 5
  slug: canva-connect-design-structure
- name: Canva Connect Design Type Structure
  property_count: 0
  slug: canva-connect-design-type-structure
- name: Canva Connect Design Urls Structure
  property_count: 2
  slug: canva-connect-design-urls-structure
- name: Canva Connect Error Structure
  property_count: 2
  slug: canva-connect-error-structure
- name: Canva Connect Export Error Structure
  property_count: 2
  slug: canva-connect-export-error-structure
- name: Canva Connect Export Format Structure
  property_count: 0
  slug: canva-connect-export-format-structure
- name: Canva Connect Export Job Response Structure
  property_count: 0
  slug: canva-connect-export-job-response-structure
- name: Canva Connect Export Job Structure
  property_count: 3
  slug: canva-connect-export-job-structure
- name: Canva Connect Folder Item Structure
  property_count: 1
  slug: canva-connect-folder-item-structure
- name: Canva Connect Folder Response Structure
  property_count: 0
  slug: canva-connect-folder-response-structure
- name: Canva Connect Folder Structure
  property_count: 4
  slug: canva-connect-folder-structure
- name: Canva Connect Gif Export Format Structure
  property_count: 5
  slug: canva-connect-gif-export-format-structure
- name: Canva Connect Import Status Structure
  property_count: 2
  slug: canva-connect-import-status-structure
- name: Canva Connect Jpg Export Format Structure
  property_count: 6
  slug: canva-connect-jpg-export-format-structure
- name: Canva Connect List Brand Templates Response Structure
  property_count: 2
  slug: canva-connect-list-brand-templates-response-structure
- name: Canva Connect List Designs Response Structure
  property_count: 2
  slug: canva-connect-list-designs-response-structure
- name: Canva Connect List Folder Items Response Structure
  property_count: 2
  slug: canva-connect-list-folder-items-response-structure
- name: Canva Connect Mentioned User Structure
  property_count: 3
  slug: canva-connect-mentioned-user-structure
- name: Canva Connect Move Folder Item Request Structure
  property_count: 2
  slug: canva-connect-move-folder-item-request-structure
- name: Canva Connect Mp4 Export Format Structure
  property_count: 4
  slug: canva-connect-mp4-export-format-structure
- name: Canva Connect Owner Structure
  property_count: 2
  slug: canva-connect-owner-structure
- name: Canva Connect Pdf Export Format Structure
  property_count: 4
  slug: canva-connect-pdf-export-format-structure
- name: Canva Connect Png Export Format Structure
  property_count: 8
  slug: canva-connect-png-export-format-structure
- name: Canva Connect Pptx Export Format Structure
  property_count: 2
  slug: canva-connect-pptx-export-format-structure
- name: Canva Connect Preset Design Type Structure
  property_count: 2
  slug: canva-connect-preset-design-type-structure
- name: Canva Connect Resize Job Response Structure
  property_count: 0
  slug: canva-connect-resize-job-response-structure
- name: Canva Connect Resize Job Structure
  property_count: 4
  slug: canva-connect-resize-job-structure
- name: Canva Connect Team User Structure
  property_count: 2
  slug: canva-connect-team-user-structure
- name: Canva Connect Thumbnail Structure
  property_count: 3
  slug: canva-connect-thumbnail-structure
- name: Canva Connect Users Me Response Structure
  property_count: 0
  slug: canva-connect-users-me-response-structure
jsonld:
- class_count: 0
  name: Canva Connect Context
  property_count: 0
  slug: canva-connect-context
- class_count: 0
  name: Canva Context
  property_count: 13
  slug: canva-context
layout: provider
mcp_servers:
- description: 'Canva ships TWO distinct MCP surfaces and they are not interchangeable. (1) A hosted, remote MCP server at https://mcp.canva.com/mcp — the "Canva AI Connector" — which an MCP client POSTs to directly '
  name: Canva MCP Server
  slug: canva-mcp-yml
modified: '2026-09-16'
name: Canva
nav: Providers
network: true
overview: 'Canva publishes 30 APIs on the [APIs.io](https://apis.io/) network, including Assets API, Autofills API, Brand Templates API, and 27 more. Tagged areas include Application, Automation, Brand Management, Collaboration, and Design.


  The Canva catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Canva''s developer surface includes authentication, support, documentation, engineering blog, changelog, legal docs, FAQ, and 61 more developer resources.'
plans:
- name: Canva Plans Pricing
  plan_count: 0
  slug: canva-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 0
  name: Canva Rate Limits
  slug: canva-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Canva API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: canva-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Canva API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 0
    warn: 10
  slug: canva-spectral-rules
scopes:
- name: Canva Scopes
  scope_count: 18
  slug: canva-scopes
  summary_line: 18 scopes · authorizationCode
score:
  band: exemplar
  composite: 70.9
  coverage:
    artifact_dirs: 34
    catalog_earned: 57.9
    catalog_earned_first_party: 0.0
    catalog_gap: 57.1
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.4
  facets:
    access_clarity: 55.3
    contract_governance: 31.8
    contract_quality: 77.0
    developer_ergonomics: 79.8
    discoverability: 81.7
    operational_transparency: 60.5
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - australia
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
    regions:
    - anz
  previous_composite: 70.5
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 25
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 11.1
screenshot: https://raw.githubusercontent.com/api-evangelist/canva/refs/heads/main/screenshots/canva-2026-06-20T173931.png
security:
- kind: authentication
  name: Canva Authentication
  slug: canva-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Canva Domain Security
  slug: canva-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Canva Vulnerability Disclosure
  slug: canva-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Canva Trust Center
  slug: canva-trust-center
  summary_line: SOC 2, ISO 27001, PCI DSS, GDPR
skill_count: 7
skills:
- name: canva-branded-presentation
  slug: canva-branded-presentation
- name: canva-bulk-create
  slug: canva-bulk-create
- name: canva-classroom-helper
  slug: canva-classroom-helper
- name: canva-implement-feedback
  slug: canva-implement-feedback
- name: canva-presentation-time-fitting
  slug: canva-presentation-time-fitting
- name: canva-resize-for-social-media
  slug: canva-resize-for-social-media
- name: canva-translate-design
  slug: canva-translate-design
slug: canva
tags:
- Application
- Automation
- Brand Management
- Collaboration
- Design
- Graphics
- Marketing
- Print
- Templates
- Visual Content
- Australia
use_cases:
- description: Generate branded marketing materials at scale by autofilling templates with campaign-specific data.
  name: Marketing Automation
- description: Integrate Canva design tools into e-commerce platforms for custom product design and print ordering.
  name: Print-on-Demand
- description: Build content pipelines that create, export, and distribute visual content across multiple channels.
  name: Content Management
- description: Ensure brand compliance by using locked brand templates with controlled editable elements.
  name: Brand Consistency
- description: Create and export social media graphics in multiple formats and sizes for cross-platform publishing.
  name: Social Media Publishing
website: https://canva.dev
---

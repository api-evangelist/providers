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
    agent_skills: derived
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
    openapi_examples: false
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 57.3
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 38
  human_in_the_loop: 0
  name: Omnisend Agentic Access
  operation_count: 60
  slug: omnisend-agentic-access
  summary_line: 60 operations · 38 acting
api_count: 21
apis:
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Brands API from Omnisend — 2 operation(s) for brands. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Brands API
  phrasing_intents:
  - id: getBrandsCurrent
    intent: Get the current brand's information
    question: Which store is connected to my Omnisend account?
  - id: postBrandsCurrent
    intent: Connect a store as a brand
    question: How do I connect my store's website to the platform through the OAuth flow?
  phrasing_ops: 2
  slug: omnisend-brands-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Campaigns API from Omnisend — 14 operation(s) for campaigns. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Campaigns API
  phrasing_intents:
  - id: getCampaigns
    intent: List campaigns
    question: Which of my campaigns are still drafts?
  - id: postCampaigns
    intent: Create a campaign draft
    question: How do I create a new email campaign draft?
  - id: deleteCampaignsById
    intent: Delete a campaign
    question: Can I delete a campaign I don't need anymore?
  - id: getCampaignsById
    intent: Get one campaign
    question: What content and audience does one particular campaign have?
  - id: patchCampaignsById
    intent: Edit a draft campaign
    question: Why does editing my campaign return a conflict once it's scheduled?
  - id: postCampaignsByIdAbTestResume
    intent: Resume a stopped A/B test
    question: Can I restart automatic winner selection on an A/B test I stopped earlier?
  - id: postCampaignsByIdAbTestStop
    intent: Stop a running A/B test
    question: How do I halt automatic winner picking on a running A/B test?
  - id: postCampaignsByIdAbTestWinner
    intent: Pick an A/B test winner manually
    question: Can I manually choose which A/B variant wins and gets sent?
  phrasing_ops: 14
  slug: omnisend-campaigns-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Contacts API from Omnisend — 7 operation(s) for contacts. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Contacts API
  phrasing_intents:
  - id: getContacts
    intent: List contacts
    question: Which contacts carry a specific tag?
  - id: patchContacts
    intent: Update a contact by email address
    question: Can I update a contact using only their email address?
  - id: postContacts
    intent: Create or upsert a contact
    question: How do I add a new subscriber, or update them if the email already exists?
  - id: getContactsById
    intent: Get one contact by ID
    question: Can I fetch one contact's full profile by its contact ID?
  - id: patchContactsById
    intent: Update a contact by ID
    question: How do I update a contact's details when I have their contact ID?
  - id: deleteContactsTags
    intent: Remove tags from many contacts
    question: Can I remove a tag from many contacts in one call?
  - id: postContactsTags
    intent: Add tags to many contacts
    question: Can I add a tag to every contact in a segment at once?
  phrasing_ops: 7
  slug: omnisend-contacts-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Events API from Omnisend — 1 operation(s) for events. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Events API
  phrasing_intents:
  - id: postEvents
    intent: Send a customer event
    question: How do I send a customer event so it can trigger an automation?
  phrasing_ops: 1
  slug: omnisend-events-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Images API from Omnisend — 5 operation(s) for images. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Images API
  phrasing_intents:
  - id: getImages
    intent: List images in the library
    question: Which images are in my brand's image library?
  - id: postImages
    intent: Add an image from a URL
    question: Can I add an image to my library from a public URL?
  - id: deleteImagesById
    intent: Delete an image
    question: Can I delete an image from my library?
  - id: getImagesById
    intent: Get one image
    question: Can I get the details of a single library image by its ID?
  - id: postImagesUpload
    intent: Upload an image file
    question: How do I upload an image file directly from my computer?
  phrasing_ops: 5
  slug: omnisend-images-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Products API from Omnisend — 5 operation(s) for products. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Products API
  phrasing_intents:
  - id: getProducts
    intent: List products in the catalog
    question: Which products are in my synced catalog?
  - id: postProducts
    intent: Create a product
    question: How do I add a new product with its variants and images?
  - id: deleteProductsByProductID
    intent: Delete a product
    question: Can I delete a product I no longer sell?
  - id: getProductsByProductID
    intent: Get one product
    question: Can I fetch a single product by its ID?
  - id: putProductsByProductID
    intent: Replace a product
    question: Can I overwrite an existing product record with an updated title and variants?
  phrasing_ops: 5
  slug: omnisend-products-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Segments API from Omnisend — 6 operation(s) for segments. Version 2026-03-15, harvested from Omnisend's published contract.
  name: Omnisend Segments API
  phrasing_intents:
  - id: getSegments
    intent: List segments
    question: Which audience segments have I set up?
  - id: postSegments
    intent: Create a segment
    question: How do I create a new segment from condition groups?
  - id: deleteSegmentsBySegmentID
    intent: Delete a segment
    question: Can I permanently delete a segment I no longer need?
  - id: getSegmentsBySegmentID
    intent: Get one segment
    question: What conditions define a specific segment?
  - id: putSegmentsBySegmentID
    intent: Update a segment
    question: Why does updating my segment return a conflict while it's still building?
  - id: getSegmentsBySegmentIDStatistics
    intent: Get a segment's contact count
    question: How many contacts match a segment right now?
  phrasing_ops: 6
  slug: omnisend-segments-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Automations API from Omnisend — 13 operation(s) for creating, enabling, copying and restructuring event-triggered automation workflows, including the sendWebhook action block that is Omnisend's on
  name: Omnisend Automations API
  phrasing_intents:
  - id: getAutomations
    intent: List automation workflows
    question: Which of my automation workflows are currently enabled?
  - id: postAutomations
    intent: Create an automation workflow
    question: 'What do I need to build a brand-new automation workflow: a trigger, blocks and a name?'
  - id: deleteAutomationsById
    intent: Delete an automation workflow
    question: Can I permanently remove an automation workflow I no longer use?
  - id: getAutomationsById
    intent: Get one automation workflow
    question: What trigger and blocks does one specific automation workflow have?
  - id: patchAutomationsById
    intent: Edit fields of an automation workflow
    question: Why can't I edit an automation workflow while it is enabled?
  - id: putAutomationsByIdBlocks
    intent: Replace an automation's full block tree
    question: How do I replace the whole block tree of an automation flow in one call?
  - id: postAutomationsByIdBlocksByBlockIDTestEmail
    intent: Send a test of an automation email block
    question: Can I preview one email step of an automation by sending it to my inbox?
  - id: getAutomationsByIdBlocksByBlockIDUtm
    intent: Get UTM tags for one automation block
    question: What UTM tags are set on a single send step of my automation?
  phrasing_ops: 13
  slug: omnisend-automations-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Event Metadata API from Omnisend — 3 operation(s) for declaring, merging and querying brand-custom event schemas. The only Omnisend operations that carry an operationId.
  name: Omnisend Event Metadata API
  phrasing_intents:
  - id: post_event_metadata
    intent: Declare a new custom event schema
    question: How can I register a brand-new custom event type so segments and automations can use it?
  - id: put_event_metadata
    intent: Update an existing custom event's schema
    question: How do I add new properties to a custom event I already defined in Omnisend?
  - id: post_event_metadata_query
    intent: Look up event metadata by category
    question: Which events are available to build segments on in Omnisend?
  phrasing_ops: 3
  slug: omnisend-event-metadata-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Batch API from Omnisend — 3 operation(s) for batch.
  name: Omnisend Batch API
  phrasing_intents:
  - id: getBatches
    intent: List batch operations
    question: Which batch jobs did I run against the products endpoint?
  - id: postBatches
    intent: Start a bulk batch operation
    question: How do I create or update up to 100 contacts in a single request to avoid rate limits?
  - id: getBatchesByBatchID
    intent: Check the status of a batch
    question: Has the bulk batch job I submitted earlier finished processing yet?
  - id: getBatchesByBatchIDItems
    intent: List the items in a batch
    question: Can I see the individual records that were processed inside a batch?
  phrasing_ops: 4
  slug: omnisend-batch-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Email Content API from Omnisend — 2 operation(s) for email content.
  name: Omnisend Email Content API
  phrasing_intents:
  - id: getEmailContentById
    intent: Get email content
    question: What sections and general settings make up a piece of email content?
  - id: putEmailContentById
    intent: Replace email content
    question: How do I fully replace the sections of an existing email's content?
  - id: postEmailContentByIdRender
    intent: Render email content to HTML
    question: Can I turn stored email content into HTML to preview it?
  phrasing_ops: 3
  slug: omnisend-email-content-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Email Templates API from Omnisend — 4 operation(s) for email templates.
  name: Omnisend Email Templates API
  phrasing_intents:
  - id: getEmailTemplates
    intent: List email templates
    question: Which email templates do I have, sorted by name?
  - id: postEmailTemplates
    intent: Create an email template
    question: How do I create a new email template from content sections?
  - id: deleteEmailTemplatesById
    intent: Delete an email template
    question: Can I delete an email template I no longer need?
  - id: getEmailTemplatesById
    intent: Get one email template
    question: Can I fetch a single email template's structure by its ID?
  - id: putEmailTemplatesById
    intent: Replace an email template
    question: How do I overwrite an existing email template with new sections?
  - id: postEmailTemplatesByIdRender
    intent: Render an email template to HTML
    question: Can I get the full HTML body of a saved email template for preview?
  - id: postEmailTemplatesImport
    intent: Import an email template from HTML
    question: Can I turn raw HTML into an editable email template?
  phrasing_ops: 7
  slug: omnisend-email-templates-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Email Universal Layouts API from Omnisend — 2 operation(s) for email universal layouts.
  name: Omnisend Email Universal Layouts API
  phrasing_intents:
  - id: getEmailUniversalLayouts
    intent: List universal layouts
    question: Which universal email layouts exist in my account?
  - id: postEmailUniversalLayouts
    intent: Create a universal layout
    question: How do I create a reusable universal layout for my emails?
  - id: deleteEmailUniversalLayoutsById
    intent: Delete a universal layout
    question: Can I delete a universal layout I don't use anymore?
  - id: getEmailUniversalLayoutsById
    intent: Get one universal layout
    question: What content does a specific universal layout hold?
  - id: putEmailUniversalLayoutsById
    intent: Replace a universal layout
    question: How do I fully replace an existing universal layout's content?
  phrasing_ops: 5
  slug: omnisend-email-universal-layouts-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Product Categories API from Omnisend — 2 operation(s) for product categories.
  name: Omnisend Product Categories API
  phrasing_intents:
  - id: getProductCategories
    intent: List product categories
    question: Which product categories are synced to my account?
  - id: postProductCategories
    intent: Create a product category
    question: How do I add a new product category to my catalog?
  - id: deleteProductCategoriesByCategoryID
    intent: Delete a product category
    question: Can I delete a product category I no longer sell?
  - id: getProductCategoriesByCategoryID
    intent: Get one product category
    question: Can I fetch one product category by its ID?
  - id: patchProductCategoriesByCategoryID
    intent: Rename a product category
    question: Can I rename an existing product category?
  phrasing_ops: 5
  slug: omnisend-product-categories-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Reports API from Omnisend — 1 operation(s) for reports.
  name: Omnisend Reports API
  phrasing_intents:
  - id: postAnalyticsReports
    intent: Report marketing results by send date
    question: How did my campaigns and automations perform, grouped by the date messages were sent?
  phrasing_ops: 1
  slug: omnisend-reports-api
- baseURL: https://api.omnisend.com/api
  baseurl_source: declared
  description: The Statistics API from Omnisend — 1 operation(s) for statistics.
  name: Omnisend Statistics API
  phrasing_intents:
  - id: postAnalyticsStatistics
    intent: Get marketing statistics by event date
    question: Can I see opens, clicks and orders grouped by the date they actually happened?
  phrasing_ops: 1
  slug: omnisend-statistics-api
arazzos:
- description: Copy an existing campaign, read the copy to confirm, then queue it for sending.
  name: Omnisend Copy and Send Campaign
  slug: omnisend-copy-and-send-campaign-workflow
- description: Create a campaign, read it back to confirm, then queue it for sending.
  name: Omnisend Create and Send Campaign
  slug: omnisend-create-and-send-campaign-workflow
- description: Create a product category, then read it back by id to confirm it was stored.
  name: Omnisend Create and Verify Product Category
  slug: omnisend-create-and-verify-category-workflow
- description: Create or update a contact, then read it back by id to confirm the write.
  name: Omnisend Create and Verify Contact
  slug: omnisend-create-and-verify-contact-workflow
- description: Create a product, then read it back by id to confirm it was stored.
  name: Omnisend Create and Verify Product
  slug: omnisend-create-and-verify-product-workflow
- description: Create a segment, read it back to confirm, then pull its membership statistics.
  name: Omnisend Create Segment and Read Statistics
  slug: omnisend-create-segment-and-stats-workflow
- description: Read a product by id, then replace it with an updated representation.
  name: Omnisend Refresh Product Catalog Entry
  slug: omnisend-replace-product-workflow
- description: Create or update a subscriber, then send a subscribed event to trigger the welcome automation.
  name: Omnisend Subscribe and Trigger Welcome
  slug: omnisend-subscribe-and-welcome-workflow
- description: Create or update a contact, then apply tags to it for segmentation.
  name: Omnisend Create and Tag Contact
  slug: omnisend-tag-contact-workflow
- description: Create or update the shopper contact, then send an added-to-cart customer event for them.
  name: Omnisend Track Added-to-Cart Event
  slug: omnisend-track-cart-event-workflow
- description: Create or update the buyer contact, then send a placed-order customer event for them.
  name: Omnisend Track Placed Order Event
  slug: omnisend-track-order-event-workflow
- description: Read a product category by id, then patch it with new values.
  name: Omnisend Update Product Category
  slug: omnisend-update-category-workflow
- description: Look up a contact by id and update it if it exists, otherwise create or update it by email.
  name: Omnisend Upsert a Contact
  slug: omnisend-upsert-contact-workflow
artifact_total: 79
asyncapis:
- description: ''
  name: Omnisend Webhooks
  slug: omnisend-webhooks
collections:
- collection_type: postman
  name: Omnisend REST API
  slug: postman-omnisend
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Analytics API
  slug: open-omnisend-analytics-api
- collection_type: open
  name: Automations API
  slug: open-omnisend-automations-api
- collection_type: open
  name: Batches API
  slug: open-omnisend-batches-api
- collection_type: open
  name: Brands API
  slug: open-omnisend-brands-api
- collection_type: open
  name: Campaigns API
  slug: open-omnisend-campaigns-api
- collection_type: open
  name: Contacts API
  slug: open-omnisend-contacts-api
- collection_type: open
  name: Email Content API
  slug: open-omnisend-emailcontent-api
- collection_type: open
  name: Email Templates API
  slug: open-omnisend-emailtemplates-api
- collection_type: open
  name: Email Universal Layouts API
  slug: open-omnisend-emailuniversallayouts-api
- collection_type: open
  name: Event Metadata API
  slug: open-omnisend-event-metadata-api
- collection_type: open
  name: Events API
  slug: open-omnisend-events-api
- collection_type: open
  name: Images API
  slug: open-omnisend-images-api
- collection_type: open
  name: Product Categories API
  slug: open-omnisend-productcategories-api
- collection_type: open
  name: Products API
  slug: open-omnisend-products-api
- collection_type: open
  name: Segments API
  slug: open-omnisend-segments-api
- collection_type: open
  name: Omnisend REST API
  slug: open-omnisend
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/capabilities/omnisend-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/omnisend-capability-edges.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/agentic-access/omnisend-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/omnisend-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/security/omnisend-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/omnisend-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/security/omnisend-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/omnisend-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/authentication/omnisend-authentication.yml
  title: ''
  type: Authentication
  url: authentication/omnisend-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/scopes/omnisend-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/omnisend-scopes.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/omnisend/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-copy-and-send-campaign-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-copy-and-send-campaign-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-create-and-send-campaign-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-send-campaign-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-create-and-verify-category-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-verify-category-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-create-and-verify-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-verify-contact-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-create-and-verify-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-and-verify-product-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-create-segment-and-stats-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-create-segment-and-stats-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-replace-product-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-replace-product-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-subscribe-and-welcome-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-subscribe-and-welcome-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-tag-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-tag-contact-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-track-cart-event-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-track-cart-event-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-track-order-event-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-track-order-event-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-update-category-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-update-category-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/arazzo/omnisend-upsert-contact-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/omnisend-upsert-contact-workflow.yml
- group: company
  title: ''
  type: Website
  url: https://www.omnisend.com
- group: start
  title: ''
  type: Portal
  url: https://www.omnisend.com
- group: docs
  title: ''
  type: Documentation
  url: https://api-docs.omnisend.com
- group: docs
  title: ''
  type: APIReference
  url: https://api-docs.omnisend.com/reference/overview
- group: start
  title: ''
  type: GettingStarted
  url: https://api-docs.omnisend.com/docs/getting-started
- group: auth
  title: ''
  type: Authentication
  url: https://api-docs.omnisend.com/reference/authentication
- group: auth
  title: ''
  type: OAuth
  url: https://api-docs.omnisend.com/reference/oauth
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.omnisend.com/changelog/
- group: agent
  title: ''
  type: LLMsTxt
  url: https://api-docs.omnisend.com/llms.txt
- group: commercial
  title: ''
  type: Pricing
  url: https://www.omnisend.com/pricing
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/plans/omnisend-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/omnisend-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/rate-limits/omnisend-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/omnisend-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/finops/omnisend-finops.yml
  title: ''
  type: FinOps
  url: finops/omnisend-finops.yml
- group: start
  title: ''
  type: SignUp
  url: https://app.omnisend.com/signup
- group: start
  title: ''
  type: Login
  url: https://app.omnisend.com/login
- group: operate
  title: ''
  type: Support
  url: https://support.omnisend.com
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.omnisend.com/en/articles/1061798-omnisend-api-documentation
- group: operate
  title: ''
  type: ContactSupport
  url: https://www.omnisend.com/contact-us/support
- group: operate
  title: ''
  type: StatusPage
  url: https://status.omnisend.com
- group: company
  title: ''
  type: Blog
  url: https://www.omnisend.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/omnisend
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/omnisend
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.omnisend.com/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.omnisend.com/terms
- group: build
  title: ''
  type: SDKs
  url: https://github.com/omnisend/php-sdk
- group: build
  title: ''
  type: Plugin
  url: https://github.com/omnisend/wp-omnisend
- group: build
  title: ''
  type: Plugin
  url: https://github.com/omnisend/magento2-plugin
- group: build
  title: ''
  type: Plugin
  url: https://www.omnisend.com/integrations/woocommerce
- group: build
  title: ''
  type: Plugin
  url: https://www.omnisend.com/integrations/shopify
- group: build
  title: ''
  type: Plugin
  url: https://www.omnisend.com/integrations/bigcommerce
- group: other
  title: ''
  type: AppMarket
  url: https://www.omnisend.com/app-market
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/packages/omnisend-packages.yml
  title: ''
  type: Packages
  url: packages/omnisend-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/well-known/omnisend-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/omnisend-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/well-known/omnisend-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/omnisend-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/mcp/omnisend-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/omnisend-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/mcp/omnisend-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/omnisend-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/llms/omnisend-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/omnisend-llms.txt
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/conformance/omnisend-conformance.yml
  title: ''
  type: Conformance
  url: conformance/omnisend-conformance.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/errors/omnisend-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/omnisend-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/lifecycle/omnisend-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/omnisend-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/lifecycle/omnisend-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/omnisend-lifecycle.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/security/omnisend-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/omnisend-vulnerability-disclosure.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/conventions/omnisend-conventions.yml
  title: ''
  type: Conventions
  url: conventions/omnisend-conventions.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/changelog/omnisend-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/omnisend-changelog.yml
- group: operate
  title: ''
  type: Roadmap
  url: https://www.omnisend.com/changelog/#roadmap
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/components/omnisend-components.yml
  title: ''
  type: Components
  url: components/omnisend-components.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/data-model/omnisend-data-model.yml
  title: ''
  type: DataModel
  url: data-model/omnisend-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/asyncapi/omnisend-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/omnisend-webhooks.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: start
  title: ''
  type: DeveloperPortal
  url: https://api-docs.omnisend.com
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-analytics-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-analytics-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-automations-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-automations-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-batches-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-batches-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-brands-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-brands-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-campaigns-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-campaigns-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-contacts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-contacts-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-emailcontent-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-emailcontent-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-emailtemplates-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-emailtemplates-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-emailuniversallayouts-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-emailuniversallayouts-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-event-metadata-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-event-metadata-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-events-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-events-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-images-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-images-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-productcategories-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-productcategories-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-products-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-products-api-overlay.yaml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/overlays/omnisend-segments-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/omnisend-segments-api-overlay.yaml
created: '2026-05-11'
description: Omnisend is a Lithuanian-headquartered email and SMS marketing automation platform purpose-built for ecommerce, with first-class integrations into Shopify, BigCommerce, WooCommerce, Magento, Wix, Square Online, and other storefronts. The platform unifies automation workflows, campaign builders, segmentation, popups and forms, web push, product recommendations, A/B testing, and reporting to drive customer engagement and revenue. The REST API at version 2026-03-15 is served from https://api.omnisend.com/api and covers contacts, events and custom event metadata, products, product categories, segments, campaigns, automations, batches, email templates, email content, universal layouts, images, brands and analytics — 82 published operations across 15 OpenAPI 3.0.0 documents. Authentication is an API key on the Authorization header (Omnisend-API-Key {key}) or OAuth 2.0 authorization code with PKCE and 26 resource scopes; every request must also carry an Omnisend-Version header, and
  a retired version returns 410. Omnisend additionally operates two first-party hosted MCP servers at mcp.omnisend.com and is listed in Claude's Connector Directory.
features:
- Email marketing automation with prebuilt ecommerce workflows (welcome, cart abandonment, browse abandonment, order confirmation, post-purchase, win-back)
- SMS marketing with global coverage and TCPA / GDPR compliant opt-in management
- Web push notifications across desktop and mobile browsers
- Drag-and-drop campaign builder with dynamic content blocks, product recommender, and conditional logic
- Audience segmentation with behavioral, lifecycle, predictive, and custom-event criteria
- Forms, popups, and signup boxes with Wheel-of-Fortune gamified opt-ins
- A/B testing on subject lines, content, and send time
- Advanced analytics and reporting with revenue attribution per campaign and workflow
- Native integrations with Shopify, BigCommerce, WooCommerce, Wix, Square Online, Magento, and PrestaShop
- REST API with X-API-KEY and OAuth 2.0 authentication, resource-scoped permissions, and cursor-based pagination
- Batch API for bulk contact, product, and event imports (up to 100 actions per batch)
- Email Templates, Email Content, and Email Universal Layouts APIs for programmatic template management
- Customer events tracking (predefined and custom) for automation triggers
- Brands API for managing brand identity across templates
- Analytics Reports and Statistics APIs for aggregated marketing performance data
- Postman public workspace and llms.txt feed for AI-agent friendly discovery
- 24/7 live support across all paid plans
- Free plan for up to 250 contacts and 500 emails/month
finops:
- name: Omnisend Finops
  service_category: Marketing and Commerce
  slug: omnisend-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/omnisend.png
json_schemas:
- name: Omnisend Contact
  property_count: 17
  slug: omnisend-contact
- name: Omnisend Customer Event
  property_count: 8
  slug: omnisend-event
jsonld:
- class_count: 0
  name: Omnisend Context
  property_count: 7
  slug: omnisend-context
layout: provider
mcp_servers:
- description: Omnisend ships two first-party hosted, remote MCP servers — the original at https://mcp.omnisend.com/mcp (4 tools) and a v2 at https://mcp.omnisend.com/v2/mcp (7 tools). Both are HTTPS endpoints an MC
  name: Omnisend MCP Server
  slug: omnisend-mcp-yml
modified: '2026-08-13'
name: Omnisend
nav: Providers
network: true
overview: 'Omnisend publishes 16 APIs on the [APIs.io](https://apis.io/) network, including Brands API, Campaigns API, Contacts API, and 13 more. Tagged areas include Email Marketing, Marketing Automation, E-Commerce, SMS Marketing, and Customer Engagement.


  The Omnisend catalog on APIs.io includes 1 event-driven AsyncAPI specification, 1 JSON-LD context, and 1 Spectral governance ruleset.


  Omnisend''s developer surface includes authentication, developer portal, documentation, API reference, getting-started guide, changelog, pricing, and 78 more developer resources.'
plans:
- name: Omnisend Plans Pricing
  plan_count: 4
  slug: omnisend-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 7
  name: Omnisend Rate Limits
  slug: omnisend-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Omnisend API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: omnisend-jsonschema-spectral-rules
scopes:
- name: Omnisend Scopes
  scope_count: 20
  slug: omnisend-scopes
  summary_line: 20 scopes · clientCredentials
score:
  band: exemplar
  composite: 72.9
  coverage:
    artifact_dirs: 32
    catalog_earned: 84.3
    catalog_earned_first_party: 24.0
    catalog_gap: 30.8
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 77.6
    contract_governance: 28.0
    contract_quality: 68.6
    developer_ergonomics: 49.4
    discoverability: 80.0
    operational_transparency: 97.4
  previous_composite: 72.9
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 16
    mcp: first-party
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 40.2
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 33.3
screenshot: https://raw.githubusercontent.com/api-evangelist/omnisend/refs/heads/main/screenshots/omnisend-2026-06-20T190706.png
security:
- kind: authentication
  name: Omnisend Authentication
  slug: omnisend-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Omnisend Domain Security
  slug: omnisend-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Omnisend Vulnerability Disclosure
  slug: omnisend-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: omnisend
tags:
- Email Marketing
- Marketing Automation
- E-Commerce
- SMS Marketing
- Customer Engagement
- Segmentation
- Campaigns
- Forms
- Popups
- Web Push
- Automation Workflows
- Analytics
- MCP
- Agent Ready
- Transactional Messaging
website: https://www.omnisend.com
---

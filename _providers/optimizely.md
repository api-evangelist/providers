---
access_model:
  confidence: medium
  label: Enterprise
  onboarding: unknown
  pricing: enterprise
  public: false
  source:
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
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
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: distinct
    pagination_ratio: partial
    protected_resource_metadata: verified
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 62.9
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 1793
  human_in_the_loop: 17
  name: Optimizely Agentic Access
  operation_count: 3530
  slug: optimizely-agentic-access
  summary_line: 3530 operations · 1793 acting · 17 human-in-the-loop
api_count: 37
apis:
- description: Optimizely's hosted remote Model Context Protocol server for Web and Feature Experimentation, on the Opal MCP platform. Tools are prefixed exp_ and cover querying projects/flags/experiments/environmen
  name: Optimizely Remote MCP Server — Experimentation
  slug: mcp-experimentation
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage campaign assets such as images and media files.
  name: Optimizely Assets API
  phrasing_intents:
  - id: listAssets
    intent: List campaign assets for a Campaign client
    question: Which images and media files are stored for my Optimizely Campaign client?
  - id: uploadAsset
    intent: Upload a campaign asset
    question: How do I upload a media file to use in my campaigns?
  - id: count
    intent: Count the images in a Campaign client
    question: How many images are stored in my campaign image library?
  - id: getAllImages
    intent: List campaign images with dimensions
    question: Can I get every campaign image with its URL, width and height?
  - id: createImage
    intent: Upload an image to a Campaign client
    question: How do I upload an image file for use in mailings?
  - id: getImage
    intent: Get details of one campaign image
    question: What is the URL and pixel size of a specific campaign image?
  - id: updateImage
    intent: Rename a campaign image
    question: Can I rename an image that is already uploaded?
  - id: deleteImage
    intent: Delete a campaign image
    question: How do I remove an image from my campaign image library?
  phrasing_ops: 14
  slug: optimizely-assets-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage custom attributes used for audience targeting and segmentation.
  name: Optimizely Attributes API
  phrasing_intents:
  - id: listAttributes
    intent: List audience attributes in a project
    question: How do I see all the custom attributes defined in an experimentation project?
  - id: create_attribute
    intent: Create an audience attribute
    question: How do I add a custom attribute for audience targeting in Optimizely?
  - id: delete_attribute
    intent: Archive an audience attribute
    question: How do I archive an attribute I no longer target on?
  - id: get_attribute
    intent: Get an audience attribute
    question: How do I look up a single attribute by its ID?
  - id: update_attribute
    intent: Update an audience attribute
    question: How do I rename an attribute or change its description?
  phrasing_ops: 5
  slug: optimizely-attributes-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create and manage audience segments for targeting experiments and rollouts.
  name: Optimizely Audiences API
  phrasing_intents:
  - id: listAudiences
    intent: List a project's audiences
    question: Which audiences are defined in my Optimizely project?
  - id: createAudience
    intent: Create an audience
    question: How do I define a new targeting audience with conditions?
  - id: getAudience
    intent: Get an audience's details
    question: What conditions make up a particular audience?
  - id: updateAudience
    intent: Update an audience
    question: Can I change an existing audience's conditions?
  phrasing_ops: 4
  slug: optimizely-audiences-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage content campaigns and editorial calendar entries.
  name: Optimizely Campaigns API
  phrasing_intents:
  - id: listCampaigns
    intent: List editorial calendar campaigns
    question: Which content campaigns are on my editorial calendar?
  - id: createCampaign
    intent: Create a content marketing campaign
    question: How do I create a new campaign in my content marketing calendar?
  - id: getCampaign
    intent: Get an editorial calendar campaign
    question: What are the details of one content campaign on my editorial calendar?
  - id: getCampaignsById
    intent: Get a content campaign record by id
    question: Where do I read the CMP campaign record that its fields, comments and attachments hang off?
  - id: updateCampaign
    intent: Update a content campaign's title or dates
    question: How do I rename a content marketing campaign or move its dates?
  - id: addCommentToCampaign
    intent: Comment on a campaign
    question: Can I post a comment on a campaign and mention a teammate?
  - id: listCampaignFields
    intent: List a campaign's custom fields
    question: Which custom fields are defined on a given campaign?
  - id: addFieldToCampaign
    intent: Add a field to a campaign
    question: How do I attach a new custom field to a campaign?
  phrasing_ops: 17
  slug: optimizely-campaigns-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage catalog entries including products, variants, packages, and bundles.
  name: Optimizely Catalog Entries API
  phrasing_intents:
  - id: getCatalogEntry
    intent: Get a catalog entry
    question: How do I look up a product, variant, package or bundle in my Optimizely Commerce catalog by its code?
  - id: updateCatalogEntry
    intent: Update a published catalog entry
    question: How do I rename a product in the catalog directly, not just its draft?
  - id: deleteCatalogEntry
    intent: Delete a catalog entry
    question: How do I permanently remove a product or variant from the catalog?
  - id: updateCatalogEntryDraft
    intent: Edit a catalog entry's language draft
    question: How do I update the draft of a catalog entry for a specific language without publishing?
  phrasing_ops: 4
  slug: optimizely-catalog-entries-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage relationships between catalog entries and nodes.
  name: Optimizely Catalog Entry Relations API
  phrasing_intents:
  - id: getEntryNodeRelations
    intent: Get the catalog nodes an entry belongs to
    question: Which catalog categories is a product entry placed in?
  - id: updateEntryNodeRelations
    intent: Update the catalog nodes an entry belongs to
    question: How do I move a product entry into different catalog categories?
  phrasing_ops: 2
  slug: optimizely-catalog-entry-relations-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage catalog nodes (categories) for organizing entries.
  name: Optimizely Catalog Nodes API
  phrasing_intents:
  - id: getCatalogNode
    intent: Get a catalog category
    question: How do I look up a category node in my Optimizely Commerce catalog by its code?
  - id: updateCatalogNode
    intent: Update a catalog category
    question: How do I move a category under a different parent node?
  - id: deleteCatalogNode
    intent: Delete a catalog category
    question: How do I permanently delete a category from the catalog?
  phrasing_ops: 3
  slug: optimizely-catalog-nodes-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage product catalogs that organize commerce content.
  name: Optimizely Catalogs API
  phrasing_intents:
  - id: listCatalogs
    intent: List product catalogs
    question: What product catalogs exist in my Optimizely commerce system?
  - id: createCatalog
    intent: Create a product catalog
    question: How do I create a new product catalog?
  - id: getCatalog
    intent: Get a catalog by name
    question: How do I look up one catalog's details by its name?
  - id: updateCatalog
    intent: Update a catalog's settings
    question: How do I deactivate a catalog?
  - id: deleteCatalog
    intent: Delete a catalog and its contents
    question: How do I permanently delete a catalog?
  phrasing_ops: 5
  slug: optimizely-catalogs-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage content items including articles and other content types within the CMP content repository.
  name: Optimizely Content API
  phrasing_intents:
  - id: listContent
    intent: List items in the CMP content repository
    question: What content items are sitting in my Optimizely CMP content repository?
  - id: contentImport
    intent: Import a content item from a URL
    question: How do I ingest an article into the content library just by giving its URL?
  - id: getContent
    intent: Get a CMP content item's details
    question: How can I look up the details of a single item in the CMP content repository?
  - id: Content_PageByType
    intent: Get a storefront page by its page type
    question: How do I fetch the storefront page definition for a given page type like the home page?
  - id: Content_PagesByParent
    intent: List storefront pages under a parent node
    question: Which storefront pages sit underneath a given parent node in the page tree?
  - id: Content_PageByUrl
    intent: Get a storefront page by its URL
    question: How do I resolve a storefront URL path to the page that renders it?
  - id: Content_PageUrlByType
    intent: Look up the URL of a storefront page type
    question: What URL does the storefront use for a particular page type, say the cart page?
  - id: Content_PageLinks
    intent: Get the storefront's page links for navigation
    question: How do I pull the set of page links that drive my storefront navigation?
  phrasing_ops: 27
  slug: optimizely-content-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Retrieve available content type definitions.
  name: Optimizely Content Types API
  phrasing_intents:
  - id: listContentTypes
    intent: List CMS content types
    question: Which content types are defined in my Optimizely CMS instance?
  phrasing_ops: 1
  slug: optimizely-content-types-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage customer accounts and contact information.
  name: Optimizely Customers API
  phrasing_intents:
  - id: getCustomer
    intent: Get a commerce customer account
    question: How do I look up a commerce customer account by its customer ID?
  - id: Customers_Get
    intent: List and filter customer records
    question: How can I list every customer record in the Optimizely commerce admin?
  - id: Customers_Post
    intent: Create a customer record
    question: How do I add a new B2B customer account through the admin API?
  - id: Customers_GetById
    intent: Get an admin customer record by ID
    question: Is there a call to fetch one customer record from the admin API by its ID?
  - id: Customers_PutById
    intent: Replace a customer record
    question: What's the call to overwrite an entire customer record with a full new version?
  - id: Customers_DeleteById
    intent: Delete one customer record
    question: How do I permanently delete a single customer by ID?
  - id: Customers_PatchById
    intent: Update fields on a customer
    question: How do I change just a few fields on an existing customer, like the credit limit?
  - id: Customers_Default
    intent: Get the default customer template
    question: What does a blank default customer look like before I fill it in?
  phrasing_ops: 35
  slug: optimizely-customers-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage environments within a project for developing, staging, and deploying flag configurations.
  name: Optimizely Environments API
  phrasing_intents:
  - id: listEnvironments
    intent: List environments for a project
    question: Which environments, like staging and production, exist for my experimentation project?
  - id: createEnvironment
    intent: Create an environment
    question: How do I add a new staging environment to my project?
  - id: getEnvironment
    intent: Get an environment's details
    question: Where can I see the key, name and primary flag of one environment?
  - id: updateEnvironment
    intent: Update an environment
    question: Can I rename an existing environment?
  - id: delete_environment
    intent: Archive an environment
    question: How do I archive an environment I no longer use?
  - id: list_environments
    intent: List a project's environments with paging and filters
    question: Can I list only the archived environments under a project path?
  - id: get_datafile
    intent: Get the datafile for an environment
    question: How do I download the JSON datafile the SDK uses for an environment?
  phrasing_ops: 7
  slug: optimizely-environments-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Send customer events to ODP for tracking actions, behaviors, and interactions across channels.
  name: Optimizely Events API
  phrasing_intents:
  - id: listEvents
    intent: List marketing calendar events
    question: Which events are on my Optimizely CMP marketing calendar between two dates?
  - id: createEvent
    intent: Create a marketing calendar event
    question: How do I add an all-day event to the marketing calendar?
  - id: getEvent
    intent: Get a marketing calendar event
    question: What are the dates and description of one event on my marketing calendar?
  - id: updateEvent
    intent: Reschedule or edit a marketing calendar event
    question: How do I move a calendar event to new start and end dates?
  - id: updateEventFields
    intent: Replace the fields on a calendar event
    question: How do I overwrite all the custom field values on a calendar event at once?
  - id: listEventFields
    intent: List the fields on a calendar event
    question: Which custom fields are attached to a marketing calendar event?
  - id: post-FxEventHandler
    intent: Send an event to the FX event handler
    question: Where do I post events meant for the FX event handler endpoint?
  - id: getEventsByEventId
    intent: Get an experimentation event
    question: What is the key and type of a tracked experiment event in my project?
  phrasing_ops: 16
  slug: optimizely-events-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create and manage A/B test experiments on top of feature flags.
  name: Optimizely Experiments API
  phrasing_intents:
  - id: Experiments_Get
    intent: List commerce content experiments
    question: Which A/B content experiments are set up in my Configured Commerce admin?
  - id: Experiments_Post
    intent: Create a commerce content experiment
    question: How do I set up a new A/B content experiment on my commerce storefront?
  - id: Experiments_GetById
    intent: Get a commerce content experiment
    question: What allocation and variants does one commerce content experiment use?
  - id: Experiments_PutById
    intent: Replace a commerce content experiment
    question: How do I overwrite a commerce content experiment with a complete new definition?
  - id: Experiments_DeleteById
    intent: Delete a commerce content experiment
    question: Can I remove one commerce content experiment by its ID?
  - id: Experiments_PatchById
    intent: Update a commerce content experiment
    question: How do I pause a running commerce content experiment without resending everything?
  - id: Experiments_Default
    intent: Get a blank commerce experiment template
    question: What default values does a new commerce content experiment start with?
  - id: Experiments_End_1
    intent: End a commerce content experiment
    question: How do I stop a commerce content experiment by passing its experiment ID?
  phrasing_ops: 21
  slug: optimizely-experiments-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage reusable extensions that encapsulate experiment logic and visual changes.
  name: Optimizely Extensions API
  phrasing_intents:
  - id: listExtensions
    intent: List a project's extensions
    question: Which reusable extensions exist in my Web Experimentation project?
  - id: create_extension
    intent: Create an extension template
    question: How do I create a reusable extension for experiment changes?
  - id: delete_extension
    intent: Archive an extension
    question: How do I archive an extension I no longer use?
  - id: get_extension
    intent: Get an extension
    question: What code and fields does a specific extension define?
  - id: update_extension
    intent: Update an extension
    question: How do I change the code of an existing extension?
  phrasing_ops: 5
  slug: optimizely-extensions-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage features with variables used in feature flag configurations.
  name: Optimizely Features API
  phrasing_intents:
  - id: listFeatures
    intent: List features in a project
    question: Which feature flags exist in my project?
  - id: create_feature
    intent: Create a feature
    question: How do I create a new feature flag with a key in a project?
  - id: getFeature
    intent: Get a feature
    question: What variables and environment rollouts does a given feature have?
  - id: delete_feature
    intent: Archive a feature
    question: How do I archive a feature flag I no longer use?
  - id: update_feature
    intent: Update a feature
    question: Can I change a feature's rollout configuration per environment?
  phrasing_ops: 5
  slug: optimizely-features-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create and manage feature flags with variables and variations for controlled rollouts and experimentation.
  name: Optimizely Flags API
  phrasing_intents:
  - id: listFlags
    intent: List feature flags in a project
    question: Which feature flags exist in my Optimizely project?
  - id: createFlag
    intent: Create a feature flag
    question: How do I create a new feature flag in a project?
  - id: update_flags
    intent: Bulk update flags with a JSON patch
    question: Can I update several feature flags at once with one JSON patch?
  - id: getFlag
    intent: Get one feature flag
    question: What variables and variations does a particular flag have?
  - id: updateFlag
    intent: Update a single feature flag
    question: How do I rename one feature flag or change its description?
  - id: deleteFlag
    intent: Delete a feature flag permanently
    question: How do I permanently delete a feature flag instead of archiving it?
  - id: archive_flags
    intent: Archive feature flags
    question: How do I archive flags I no longer use without deleting them?
  - id: unarchive_flags
    intent: Restore archived feature flags
    question: Can I bring archived flags back into use?
  phrasing_ops: 8
  slug: optimizely-flags-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage labels used for categorizing and organizing content.
  name: Optimizely Labels API
  phrasing_intents:
  - id: listLabels
    intent: List content labels
    question: Which labels are used to categorize content in the Optimizely CMP?
  - id: listLabelGroups
    intent: List label groups
    question: How are my CMP labels organized into groups?
  phrasing_ops: 2
  slug: optimizely-labels-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage mailing lists used for campaign distribution.
  name: Optimizely Mailing Lists API
  phrasing_intents:
  - id: listMailingLists
    intent: List mailing lists for a Campaign client
    question: Which mailing lists exist under my Optimizely Campaign client?
  - id: getMailingList
    intent: Get one mailing list
    question: What are the details of a specific mailing list?
  phrasing_ops: 2
  slug: optimizely-mailing-lists-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create, update, and manage objects such as products, orders, and custom entities in ODP.
  name: Optimizely Objects API
  phrasing_intents:
  - id: update-object
    intent: Update a named custom object
    question: How do I update order summary fields without generating events?
  - id: upsertObjects
    intent: Create or update objects of a type
    question: How do I bulk load products or orders into the customer data platform?
  - id: getObject
    intent: Get an object by type and ID
    question: What is stored in the data platform for a particular order or product?
  phrasing_ops: 3
  slug: optimizely-objects-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage purchase orders, cart operations, and order workflows.
  name: Optimizely Orders API
  phrasing_intents:
  - id: listCustomerOrders
    intent: List all orders for a customer
    question: How do I get every order a specific customer has placed?
  - id: getOrder
    intent: Get an order by its order group id
    question: How do I retrieve one commerce order using its order group id?
  - id: searchOrders
    intent: Page through commerce orders
    question: How do I search commerce orders a page at a time?
  - id: OrdersV1_GetCollectionAsync
    intent: Find the storefront user's orders by filters
    question: How do I find my orders by PO number or status on the storefront?
  - id: OrdersV1_GetAsync
    intent: Get a storefront order by order id
    question: How do I view the lines and totals of one storefront order?
  - id: OrdersV1_PatchAsync
    intent: Update a storefront order
    question: How do I change the status of a storefront order?
  - id: OrdersV1_PostRmaAsync
    intent: Request a return (RMA) on an order
    question: How do I request a return authorization for items on an order?
  - id: OrdersV1_Post
    intent: Share an order by email
    question: How do I email a copy of an order to a colleague?
  phrasing_ops: 8
  slug: optimizely-orders-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage page definitions that specify which URLs or conditions trigger experiments.
  name: Optimizely Pages API
  phrasing_intents:
  - id: Pages_Get
    intent: List CMS page variants
    question: Which content page variants exist in my commerce admin?
  - id: Pages_Post
    intent: Create a CMS page variant
    question: How do I add a new variant of a content page in the commerce admin?
  - id: Pages_GetById
    intent: Get a CMS page variant
    question: What layout and node is a particular CMS page variant attached to?
  - id: Pages_PutById
    intent: Replace a CMS page variant
    question: How do I overwrite a whole CMS page variant record in one call?
  - id: Pages_DeleteById
    intent: Delete a CMS page variant
    question: How do I delete one CMS page variant by its ID?
  - id: Pages_PatchById
    intent: Update a CMS page variant
    question: Can I rename a CMS page variant without resending the whole record?
  - id: Pages_Default
    intent: Get a blank CMS page template
    question: What default values does a new CMS page variant start with?
  - id: Pages_DeleteRoute
    intent: Bulk delete CMS page variants
    question: How do I delete several CMS page variants at once?
  phrasing_ops: 15
  slug: optimizely-pages-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Create, update, and retrieve customer profiles with unified identity resolution.
  name: Optimizely Profiles API
  phrasing_intents:
  - id: upsertProfile
    intent: Create or update a customer profile
    question: How do I create a customer profile in ODP keyed by email?
  - id: getProfile
    intent: Get a customer profile by identifier
    question: Can I look up a customer profile by email address?
  phrasing_ops: 2
  slug: optimizely-profiles-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage Feature Experimentation projects that serve as containers for flags, experiments, and environments.
  name: Optimizely Projects API
  phrasing_intents:
  - id: listProjects
    intent: List Feature Experimentation projects
    question: Which Feature Experimentation projects can I access in Optimizely?
  - id: createProject
    intent: Create a Feature Experimentation project
    question: How do I start a new Feature Experimentation project?
  - id: getProject
    intent: Get a project's details
    question: What are the details of a specific experimentation project?
  - id: updateProject
    intent: Rename or change a project's status
    question: Can I rename an existing experimentation project?
  - id: deleteProject
    intent: Permanently delete a project
    question: What happens to experiments, audiences and events when a project is deleted?
  phrasing_ops: 5
  slug: optimizely-projects-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage recipients and recipient lists for email campaigns.
  name: Optimizely Recipients API
  phrasing_intents:
  - id: listRecipients
    intent: List recipients in a recipient list
    question: Who is on one of my Optimizely Campaign recipient lists?
  - id: addRecipient
    intent: Add a single recipient to a list
    question: How can I subscribe one new email address to a recipient list?
  - id: addRecipients
    intent: Bulk add recipients to a list
    question: How do I import a batch of recipients into a recipient list in one request?
  - id: deleteRecipients
    intent: Remove many recipients from a list
    question: Can I remove several recipients from a list by their IDs in one call?
  - id: getRecipient
    intent: Get one recipient's details
    question: What details are stored for a specific recipient on a list?
  - id: updateRecipient
    intent: Update a recipient's email and name
    question: How do I correct a subscriber's first or last name on a list?
  - id: deleteRecipient
    intent: Remove one recipient from a list
    question: How do I take a single subscriber off a recipient list?
  - id: modifyRecipientAttributes
    intent: Update attribute values of one recipient
    question: Can I append text to one recipient's string field instead of overwriting it?
  phrasing_ops: 20
  slug: optimizely-recipients-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage rulesets that define which variation a flag delivers to visitors within a given environment.
  name: Optimizely Rulesets API
  phrasing_intents:
  - id: getRuleset
    intent: Get a flag's ruleset in an environment
    question: What rules decide which variation my flag serves in production?
  - id: updateRuleset
    intent: Update a flag's ruleset in an environment
    question: How do I change or reorder the rules of a flag in one environment?
  - id: enableRuleset
    intent: Turn a flag on in an environment
    question: How do I switch a feature flag on in production?
  - id: disableRuleset
    intent: Turn a flag off in an environment
    question: How do I switch a feature flag off in one environment?
  phrasing_ops: 4
  slug: optimizely-rulesets-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage the ODP schema including domain objects and their fields.
  name: Optimizely Schema API
  phrasing_intents:
  - id: listSchemaObjects
    intent: List object types in the data platform schema
    question: What object types are defined in my Optimizely Data Platform schema?
  - id: getSchemaObject
    intent: Get one object type's schema definition
    question: How do I see the fields defined on one schema object type?
  - id: createSchemaObject
    intent: Create a new object type in the schema
    question: How do I add a custom object type to the data platform schema?
  - id: createSchemaField
    intent: Add a field to a schema object
    question: How do I add a new field to an existing object type?
  phrasing_ops: 4
  slug: optimizely-schema-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Query customer segments and audience definitions.
  name: Optimizely Segments API
  phrasing_intents:
  - id: listSegments
    intent: List customer segments
    question: Which customer segments are defined in the Data Platform?
  phrasing_ops: 1
  slug: optimizely-segments-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Retrieve site definitions including language settings and configuration.
  name: Optimizely Sites API
  phrasing_intents:
  - id: listSites
    intent: List CMS sites
    question: Which sites are configured in my Optimizely CMS instance?
  phrasing_ops: 1
  slug: optimizely-sites-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage smart campaigns that automate multi-step marketing workflows.
  name: Optimizely Smart Campaigns API
  phrasing_intents:
  - id: listSmartCampaigns
    intent: List smart campaigns for a Campaign client
    question: Which smart campaigns exist under my Optimizely Campaign client?
  - id: createOrCopySmartCampaign
    intent: Create a new smart campaign or copy an existing one
    question: How do I create a new smart campaign through the API?
  - id: getSmartCampaign
    intent: Get details of one smart campaign
    question: What are the details and current status of a particular smart campaign?
  - id: updateCampaignMessage_2
    intent: Rename a smart campaign
    question: How do I rename a smart campaign after it's been created?
  - id: deleteSmartCampaign
    intent: Delete a smart campaign
    question: How do I permanently remove a smart campaign I no longer need?
  - id: startSmartCampaign
    intent: Start a smart campaign's automated workflow
    question: How do I kick off the automated workflow of a smart campaign?
  - id: pauseSmartCampaign
    intent: Pause a running smart campaign
    question: Can I temporarily pause a whole smart campaign without cancelling it?
  - id: activateSmartCampaign
    intent: Activate a smart campaign
    question: How do I move a smart campaign into the Activated status?
  phrasing_ops: 65
  slug: optimizely-smart-campaigns-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage content tasks, assignments, and workflow steps within the content marketing platform.
  name: Optimizely Tasks API
  phrasing_intents:
  - id: listTasks
    intent: List content tasks with their workflow status
    question: Can I pull a list of all our content tasks and see where each one sits in the workflow?
  - id: createTask
    intent: Create a content task
    question: How do I open a new content task in Optimizely CMP from code?
  - id: getTask
    intent: Get a content task by its taskId
    question: What details come back when I look up a single content task by its taskId?
  - id: updateTask
    intent: Replace a task's title, assignee or due date
    question: Can I change a task's assignee_id and due_date with a full PUT update?
  - id: getTasksById
    intent: Get a CMP task by id
    question: How do I read a CMP task by its id to check its owner, start and due dates?
  - id: patchTasksById
    intent: Patch a task's owner, schedule or workflow
    question: Can I move a task to a different owner or change its start_at and due_at dates with a partial update?
  - id: addUrlToTask
    intent: Attach a URL to a task
    question: Can I attach a web link to a content task?
  - id: getTaskBrief
    intent: Get a task's brief
    question: Where do I read the creative brief written for a task?
  phrasing_ops: 46
  slug: optimizely-tasks-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Send transactional emails triggered by recipient actions or events.
  name: Optimizely Transactional Mail API
  phrasing_intents:
  - id: sendTransactionalMail
    intent: Send a transactional email
    question: How do I send an order confirmation or password reset email to one recipient?
  phrasing_ops: 1
  slug: optimizely-transactional-mail-api
- baseURL: https://api.optimizely.com/v2
  baseurl_source: declared
  description: Manage unsubscribe lists for opt-out recipients.
  name: Optimizely Unsubscribes API
  phrasing_intents:
  - id: listUnsubscribes
    intent: List unsubscribed recipients
    question: Who has unsubscribed from our email communications?
  - id: addUnsubscribe
    intent: Unsubscribe a recipient
    question: How do I add someone to the unsubscribe list by email?
  - id: removeUnsubscribes
    intent: Resubscribe recipients
    question: Can I take several recipients off the internal unsubscribe list?
  - id: countUnsubscribes
    intent: Count unsubscribed recipients
    question: How many recipients are currently unsubscribed?
  phrasing_ops: 4
  slug: optimizely-unsubscribes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Accounts API from Optimizely — 7 operation(s) for accounts.
  name: Optimizely Accounts API
  phrasing_intents:
  - id: AccountShipTosV1_Patch
    intent: Update an account's ship-to assignments
    question: How do I change which ship-to addresses a user account can order to?
  - id: AccountsV1_GetCollectionAsync
    intent: List user accounts
    question: How do I search the user accounts in my Optimizely B2B storefront by name?
  - id: AccountsV1_PostAsync
    intent: Create a user account
    question: How do I register a new user account with an email and password?
  - id: AccountsV1_GetAsync
    intent: Get a user account
    question: What role and default ship-to does a specific user account have?
  - id: AccountsV1_PatchAsync
    intent: Update a user account
    question: How do I change a user's role or name on their account?
  - id: AccountsV1_PostVmiAsync
    intent: Import VMI users
    question: How do I bulk import vendor managed inventory users?
  - id: AccountsV1_PatchVmiAsync
    intent: Update a VMI user's role and locations
    question: How do I change which VMI locations a vendor managed inventory user can access?
  - id: AccountPaymentProfilesV1_GetCollectionAsync
    intent: List my saved payment profiles
    question: Which saved cards are on the current user's account?
  phrasing_ops: 12
  slug: optimizely-accounts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Activate API from Optimizely — 1 operation(s) for activate.
  name: Optimizely Activate API
  phrasing_intents:
  - id: activate
    intent: Decide features and experiments for a user
    question: Which features and experiment variations is a given user bucketed into?
  phrasing_ops: 1
  slug: optimizely-activate-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin Action Configurations API from Optimizely — 6 operation(s) for admin action configurations.
  name: Optimizely Admin Action Configurations API
  phrasing_intents:
  - id: AdminActionConfigurations_Get
    intent: List admin action configurations
    question: How do I list the configured admin console actions?
  - id: AdminActionConfigurations_Post
    intent: Create an admin action configuration
    question: How do I add a custom action button to an admin form?
  - id: AdminActionConfigurations_GetById
    intent: Get one admin action configuration
    question: How do I look up a single admin action configuration by its id?
  - id: AdminActionConfigurations_PutById
    intent: Replace an admin action configuration
    question: How do I overwrite an admin action configuration completely?
  - id: AdminActionConfigurations_DeleteById
    intent: Delete an admin action configuration
    question: How do I remove a single admin action configuration?
  - id: AdminActionConfigurations_PatchById
    intent: Update fields on an admin action configuration
    question: How do I change just the tooltip text of an admin action?
  - id: AdminActionConfigurations_Default
    intent: Get the default admin action configuration
    question: What are the default values for a new admin action configuration?
  - id: AdminActionConfigurations_DeleteRoute
    intent: Bulk delete admin action configurations
    question: How do I delete several admin action configurations at once?
  phrasing_ops: 10
  slug: optimizely-admin-action-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin Action Permissions API from Optimizely — 5 operation(s) for admin action permissions.
  name: Optimizely Admin Action Permissions API
  phrasing_intents:
  - id: AdminActionPermissions_Get
    intent: List admin action permissions
    question: Which roles are allowed to run which admin actions in my commerce admin console?
  - id: AdminActionPermissions_Post
    intent: Grant a role permission for an admin action
    question: How do I give a role permission to perform an admin action?
  - id: AdminActionPermissions_GetById
    intent: Get one admin action permission
    question: What role and permission type does a specific admin action permission record hold?
  - id: AdminActionPermissions_PutById
    intent: Replace an admin action permission
    question: Is there a way to overwrite an entire admin action permission record in one go?
  - id: AdminActionPermissions_DeleteById
    intent: Delete one admin action permission
    question: How do I revoke a single admin action permission from a role?
  - id: AdminActionPermissions_PatchById
    intent: Update fields of an admin action permission
    question: Can I change just the role on an existing admin action permission?
  - id: AdminActionPermissions_Default
    intent: Call the Default function on admin action permissions
    question: What does the Default function on the admin action permissions entity set return?
  - id: AdminActionPermissions_DeleteRoute
    intent: Bulk delete admin action permissions by ID
    question: Can I delete several admin action permissions in one request?
  phrasing_ops: 9
  slug: optimizely-admin-action-permissions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profile Passwords API from Optimizely — 5 operation(s) for admin user profile passwords.
  name: Optimizely Admin User Profile Passwords API
  phrasing_intents:
  - id: AdminUserProfilePasswords_Get
    intent: List stored admin user password records
    question: How do I list the password history records for admin users?
  - id: AdminUserProfilePasswords_Post
    intent: Add a password record for an admin user
    question: How do I store a new password hash for an admin user?
  - id: AdminUserProfilePasswords_GetById
    intent: Get one admin password record
    question: How do I look up a single admin password record by id?
  - id: AdminUserProfilePasswords_PutById
    intent: Replace an admin password record
    question: How do I overwrite an admin password record entirely?
  - id: AdminUserProfilePasswords_DeleteById
    intent: Delete an admin password record
    question: How do I remove one stored admin password record?
  - id: AdminUserProfilePasswords_PatchById
    intent: Update fields on an admin password record
    question: How do I change just the password-changed date on an admin password record?
  - id: AdminUserProfilePasswords_Default
    intent: Get the default admin password record
    question: What does a default admin password record look like?
  - id: AdminUserProfilePasswords_DeleteRoute
    intent: Bulk delete admin password records
    question: How do I delete many admin password records in one call?
  phrasing_ops: 9
  slug: optimizely-admin-user-profile-passwords-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profile Preferences API from Optimizely — 7 operation(s) for admin user profile preferences.
  name: Optimizely Admin User Profile Preferences API
  phrasing_intents:
  - id: AdminUserProfilePreferences_Get
    intent: List admin user profile preferences
    question: Which saved preferences exist across all admin user profiles?
  - id: AdminUserProfilePreferences_Post
    intent: Create a preference for an admin user profile
    question: How do I save a named preference for a specific admin user profile?
  - id: AdminUserProfilePreferences_GetById
    intent: Get an admin user profile preference by ID
    question: What value is stored in one admin preference record by its ID?
  - id: AdminUserProfilePreferences_PutById
    intent: Replace an admin user profile preference
    question: How do I overwrite an entire admin preference record by ID?
  - id: AdminUserProfilePreferences_DeleteById
    intent: Delete an admin user profile preference by ID
    question: Can I delete one admin preference record by its ID?
  - id: AdminUserProfilePreferences_PatchById
    intent: Update an admin user profile preference by ID
    question: How do I change the value of one admin preference record by ID?
  - id: AdminUserProfilePreferences_Default
    intent: Get a default admin preference template
    question: What default values does a new admin user profile preference start with?
  - id: AdminUserProfilePreferences_GetPreferencesForCurrentUser_1
    intent: Get my admin preferences via the Current() function
    question: How do I read the signed-in admin's preferences through the OData Current() function?
  phrasing_ops: 14
  slug: optimizely-admin-user-profile-preferences-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profile Websites API from Optimizely — 5 operation(s) for admin user profile websites.
  name: Optimizely Admin User Profile Websites API
  phrasing_intents:
  - id: AdminUserProfileWebsites_Get
    intent: List admin user website assignments
    question: Which websites is each admin user allowed to manage?
  - id: AdminUserProfileWebsites_Post
    intent: Give an admin user access to a website
    question: How do I grant an admin user access to another storefront website?
  - id: AdminUserProfileWebsites_GetById
    intent: Get an admin user website assignment
    question: Can I look up one admin-to-website assignment by its id?
  - id: AdminUserProfileWebsites_PutById
    intent: Replace an admin user website assignment
    question: Can I fully rewrite an existing admin website assignment?
  - id: AdminUserProfileWebsites_DeleteById
    intent: Remove an admin user's access to a website
    question: How do I revoke an admin user's access to a single website?
  - id: AdminUserProfileWebsites_PatchById
    intent: Update an admin user website assignment
    question: Can I point an existing admin assignment at a different website?
  - id: AdminUserProfileWebsites_Default
    intent: Call the admin user websites Default function
    question: What does the Default function return for admin user profile websites?
  - id: AdminUserProfileWebsites_DeleteRoute
    intent: Bulk delete admin user website assignments
    question: Can I remove many admin website assignments in a single call?
  phrasing_ops: 9
  slug: optimizely-admin-user-profile-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Admin User Profiles API from Optimizely — 12 operation(s) for admin user profiles.
  name: Optimizely Admin User Profiles API
  phrasing_intents:
  - id: AdminUserProfiles_Get
    intent: List admin console user profiles
    question: How do I list every admin user who can sign in to the Optimizely Commerce admin console?
  - id: AdminUserProfiles_Post
    intent: Create an admin console user
    question: How do I add a new administrator to the commerce admin console?
  - id: AdminUserProfiles_GetById
    intent: Get one admin user profile
    question: How do I look up a single admin user's profile by its ID?
  - id: AdminUserProfiles_PutById
    intent: Replace an admin user profile
    question: How do I overwrite an entire admin user profile with a new record?
  - id: AdminUserProfiles_DeleteById
    intent: Delete an admin user profile
    question: How do I permanently remove one admin user from the admin console?
  - id: AdminUserProfiles_PatchById
    intent: Update fields on an admin user profile
    question: How do I change an admin user's phone number or email without resending everything?
  - id: AdminUserProfiles_Default
    intent: Get a blank admin user profile template
    question: What default values does a new admin user profile start with?
  - id: AdminUserProfiles_GetRolesById
    intent: Call the Roles function for an admin user
    question: How do I call the OData Roles function to see which roles an admin user holds?
  phrasing_ops: 19
  slug: optimizely-admin-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Adyen API from Optimizely — 1 operation(s) for adyen.
  name: Optimizely Adyen API
  phrasing_intents:
  - id: AdyenV1_Get
    intent: Get the Adyen payment configuration
    question: How does my Optimizely commerce storefront load its Adyen payment settings?
  phrasing_ops: 1
  slug: optimizely-adyen-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Affiliates API from Optimizely — 7 operation(s) for affiliates.
  name: Optimizely Affiliates API
  phrasing_intents:
  - id: Affiliates_Get
    intent: List affiliate partners
    question: How can I see every affiliate configured in Commerce admin?
  - id: Affiliates_Post
    intent: Add a new affiliate partner
    question: What information do I need to register a new affiliate?
  - id: Affiliates_GetById
    intent: Get one affiliate by id
    question: How do I look up a single affiliate's details?
  - id: Affiliates_PutById
    intent: Replace an affiliate record
    question: Can I overwrite an affiliate's whole record at once?
  - id: Affiliates_DeleteById
    intent: Delete a single affiliate
    question: How do I delete one affiliate?
  - id: Affiliates_PatchById
    intent: Update part of an affiliate
    question: Can I just change an affiliate's website URL?
  - id: Affiliates_Default
    intent: Get default values for a new affiliate
    question: What defaults does a new affiliate record start with?
  - id: Affiliates_Archive
    intent: Archive affiliates via the OData archive action
    question: How do I archive affiliates with the OData Default.archive action?
  phrasing_ops: 11
  slug: optimizely-affiliates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Application Es Logs API from Optimizely — 2 operation(s) for application es logs.
  name: Optimizely Application Es Logs API
  phrasing_intents:
  - id: ApplicationEsLogs_Get
    intent: List application search logs
    question: Where can I see the Elasticsearch application log entries for my commerce site?
  - id: ApplicationEsLogs_GetById
    intent: Get one application search log entry
    question: How do I open the full details of one application search log entry?
  phrasing_ops: 2
  slug: optimizely-application-es-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Application Logs API from Optimizely — 5 operation(s) for application logs.
  name: Optimizely Application Logs API
  phrasing_intents:
  - id: ApplicationLogs_Get
    intent: List application log entries
    question: Where can I see recent application log messages from the commerce site?
  - id: ApplicationLogs_Post
    intent: Write an application log entry
    question: Can I record my own message in the application log?
  - id: ApplicationLogs_GetById
    intent: Get an application log entry
    question: Can I open one application log entry by its id to read the full message?
  - id: ApplicationLogs_PutById
    intent: Replace an application log entry
    question: Is there a way to overwrite a whole application log record?
  - id: ApplicationLogs_DeleteById
    intent: Delete an application log entry
    question: Can I delete one application log entry by id?
  - id: ApplicationLogs_PatchById
    intent: Update fields on a log entry
    question: How do I correct just the message text on an existing log entry?
  - id: ApplicationLogs_Default
    intent: Get a blank application log template
    question: What default values does a new application log entry have?
  - id: ApplicationLogs_DeleteRoute
    intent: Bulk delete application log entries
    question: Can I purge many application log entries at once?
  phrasing_ops: 9
  slug: optimizely-application-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Application Messages API from Optimizely — 5 operation(s) for application messages.
  name: Optimizely Application Messages API
  phrasing_intents:
  - id: ApplicationMessages_Get
    intent: List application messages
    question: Which storefront messages and labels are defined in my Optimizely commerce site?
  - id: ApplicationMessages_Post
    intent: Create an application message
    question: How do I add a new message text that the storefront displays?
  - id: ApplicationMessages_GetById
    intent: Get an application message
    question: What text does a particular application message show?
  - id: ApplicationMessages_PutById
    intent: Replace an application message
    question: How do I overwrite an application message record entirely?
  - id: ApplicationMessages_DeleteById
    intent: Delete an application message
    question: How do I remove an application message?
  - id: ApplicationMessages_PatchById
    intent: Edit an application message's text
    question: How do I change the wording of an existing storefront message?
  - id: ApplicationMessages_Default
    intent: Get a blank default application message
    question: What does an empty application message object contain?
  - id: ApplicationMessages_DeleteRoute
    intent: Delete several application messages
    question: Can I delete a batch of application messages in one request?
  phrasing_ops: 9
  slug: optimizely-application-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage email attachments
  name: Optimizely Attachments API
  phrasing_intents:
  - id: count_1
    intent: Count email attachments for a client
    question: How many attachments are stored for my Optimizely Campaign client?
  - id: getAllAttachments
    intent: List a client's email attachments
    question: What attachments does my client have, with their mime types and sizes?
  - id: createAttachment
    intent: Upload a new email attachment
    question: How do I upload a file to use as an attachment in my mailings?
  - id: getUploadAttachment
    intent: Download an attachment's file content
    question: How do I download the actual file behind an attachment?
  - id: uploadAttachment
    intent: Replace an attachment's file content
    question: Can I swap in a new file for an existing attachment without creating another one?
  - id: getAttachment
    intent: Get an attachment's details
    question: What type, size and creation date does a specific attachment have?
  - id: updateAttachment
    intent: Rename or retype an attachment
    question: How do I rename an attachment or change its file name?
  - id: deleteAttachment
    intent: Delete an attachment
    question: How do I remove an attachment I no longer use in mailings?
  phrasing_ops: 9
  slug: optimizely-attachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Attribute Types API from Optimizely — 9 operation(s) for attribute types.
  name: Optimizely Attribute Types API
  phrasing_intents:
  - id: AttributeTypes_Get
    intent: List product attribute types
    question: What product attribute types are defined in the catalog, like color or size?
  - id: AttributeTypes_Post
    intent: Create an attribute type
    question: How do I add a new product attribute such as material to the catalog?
  - id: AttributeTypes_GetById
    intent: Get an attribute type by id
    question: Can I look up one attribute type's settings by its id?
  - id: AttributeTypes_PutById
    intent: Replace an attribute type
    question: Is there a way to overwrite every field of an attribute type at once?
  - id: AttributeTypes_DeleteById
    intent: Delete an attribute type
    question: Can I permanently delete one attribute type by id?
  - id: AttributeTypes_PatchById
    intent: Update fields on an attribute type
    question: How do I turn off an attribute type without resending all its fields?
  - id: AttributeTypes_Default
    intent: Get a blank attribute type template
    question: What default settings does a new attribute type start with?
  - id: AttributeTypes_Archive
    intent: Archive attribute types via the archive action
    question: Can I archive attribute types by posting to the archive action instead of deleting them?
  phrasing_ops: 13
  slug: optimizely-attribute-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Attribute Values API from Optimizely — 11 operation(s) for attribute values.
  name: Optimizely Attribute Values API
  phrasing_intents:
  - id: AttributeValues_Get
    intent: List product attribute values
    question: What attribute values, like Red or Large, exist in my commerce catalog?
  - id: AttributeValues_Post
    intent: Create an attribute value
    question: How do I add a new option such as Navy to an existing product attribute?
  - id: AttributeValues_GetById
    intent: Get an attribute value by id
    question: Can I look up a single attribute value record by its id?
  - id: AttributeValues_PutById
    intent: Replace an attribute value
    question: Is there a way to overwrite every field of an attribute value in one call?
  - id: AttributeValues_DeleteById
    intent: Delete an attribute value
    question: Can I permanently delete one attribute value by its id?
  - id: AttributeValues_PatchById
    intent: Update fields on an attribute value
    question: How do I deactivate an attribute value without resending the whole record?
  - id: AttributeValues_Default
    intent: Get a blank attribute value template
    question: What default fields does a new attribute value start with?
  - id: AttributeValues_Archive
    intent: Archive attribute values via the archive action
    question: Can I archive attribute values with the POST archive action instead of deleting them?
  phrasing_ops: 15
  slug: optimizely-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get a list of bucketing decisions for a visitor.
  name: Optimizely Attribution API
  phrasing_intents:
  - id: get_bucketing_history
    intent: Get a visitor's experiment bucketing history
    question: Which experiments has a specific visitor been exposed to?
  phrasing_ops: 1
  slug: optimizely-attribution-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Audits API from Optimizely — 5 operation(s) for audits.
  name: Optimizely Audits API
  phrasing_intents:
  - id: Audits_Get
    intent: List admin audit log entries
    question: What actions have admins taken in Optimizely Commerce recently?
  - id: Audits_Post
    intent: Record an audit log entry
    question: Can I write my own entry into the audit trail?
  - id: Audits_GetById
    intent: Get one audit log entry
    question: Who performed a particular audited action, and from where?
  - id: Audits_PutById
    intent: Replace an audit log entry
    question: Can an audit record be overwritten in full?
  - id: Audits_DeleteById
    intent: Delete one audit log entry
    question: Is it possible to delete a single audit trail record?
  - id: Audits_PatchById
    intent: Edit fields of an audit log entry
    question: Can I correct just the description on an existing audit record?
  - id: Audits_Default
    intent: Get default values for an audit entry
    question: What defaults does a new audit record start with?
  - id: Audits_DeleteRoute
    intent: Bulk delete audit log entries
    question: Can I purge many audit records in one request?
  phrasing_ops: 9
  slug: optimizely-audits-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Autocomplete API from Optimizely — 2 operation(s) for autocomplete.
  name: Optimizely Autocomplete API
  phrasing_intents:
  - id: AutocompleteV1_GetAsync
    intent: Get search autocomplete suggestions
    question: How do I show type-ahead suggestions as a shopper types in the storefront search box?
  - id: ProductsV1_GetAutoCompleteAsync
    intent: Get product-only autocomplete suggestions
    question: How do I autocomplete only product names from a partial search term?
  phrasing_ops: 2
  slug: optimizely-autocomplete-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Available Languages API from Optimizely — 1 operation(s) for available languages.
  name: Optimizely Available Languages API
  phrasing_intents:
  - id: AvailableLanguages_Get
    intent: List languages available to the site
    question: Which languages are available to use in Optimizely Commerce?
  phrasing_ops: 1
  slug: optimizely-available-languages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Badge Attribute Values API from Optimizely — 5 operation(s) for badge attribute values.
  name: Optimizely Badge Attribute Values API
  phrasing_intents:
  - id: BadgeAttributeValues_Get
    intent: List badge attribute value links
    question: Which attribute values are tied to product badges in Optimizely Configured Commerce?
  - id: BadgeAttributeValues_Post
    intent: Link an attribute value to a badge
    question: How do I make a badge apply to products with a certain attribute value?
  - id: BadgeAttributeValues_GetById
    intent: Get one badge attribute value link
    question: How do I look up a single badge-to-attribute-value link by its ID?
  - id: BadgeAttributeValues_PutById
    intent: Replace a badge attribute value link
    question: Can I overwrite a badge attribute value link with a new badge and value?
  - id: BadgeAttributeValues_DeleteById
    intent: Delete a badge attribute value link
    question: How do I unlink one attribute value from a badge?
  - id: BadgeAttributeValues_PatchById
    intent: Update a badge attribute value link
    question: Can I switch just the attribute value on an existing badge link?
  - id: BadgeAttributeValues_Default
    intent: Get default values for a badge attribute value
    question: What defaults does the admin pre-fill for a new badge attribute value?
  - id: BadgeAttributeValues_DeleteRoute
    intent: Bulk delete badge attribute values
    question: How do I unlink many attribute values from badges in one request?
  phrasing_ops: 9
  slug: optimizely-badge-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Badge Products API from Optimizely — 5 operation(s) for badge products.
  name: Optimizely Badge Products API
  phrasing_intents:
  - id: BadgeProducts_Get
    intent: List badge-to-product assignments
    question: How do I see which products have which badges assigned?
  - id: BadgeProducts_Post
    intent: Assign a badge to a product
    question: Can I put a badge like 'New' on a product through the admin API?
  - id: BadgeProducts_GetById
    intent: Get one badge assignment
    question: Where do I look up a single badge-product assignment by its id?
  - id: BadgeProducts_PutById
    intent: Replace a badge assignment
    question: How do I fully overwrite a badge-product assignment record?
  - id: BadgeProducts_DeleteById
    intent: Remove a badge from a product
    question: Can I take a badge off a product by deleting its assignment?
  - id: BadgeProducts_PatchById
    intent: Update fields on a badge assignment
    question: Can I change just the manual-assignment flag on an existing badge assignment?
  - id: BadgeProducts_Default
    intent: Call the Default function on badge products
    question: What does the Default function on the BadgeProducts set return?
  - id: BadgeProducts_DeleteRoute
    intent: Bulk remove badge assignments
    question: Can I remove many badge assignments at once by id?
  phrasing_ops: 9
  slug: optimizely-badge-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Badges API from Optimizely — 7 operation(s) for badges.
  name: Optimizely Badges API
  phrasing_intents:
  - id: Badges_Get
    intent: List product badges
    question: How do I list all the product badges set up in my commerce admin?
  - id: Badges_Post
    intent: Create a product badge
    question: How do I create a new badge like 'Sale' or 'New' for products?
  - id: Badges_GetById
    intent: Get a product badge
    question: How do I look up one badge's settings by its ID?
  - id: Badges_PutById
    intent: Replace a product badge
    question: How do I overwrite a badge record with a full new definition?
  - id: Badges_DeleteById
    intent: Delete a product badge
    question: How do I delete one badge by its ID?
  - id: Badges_PatchById
    intent: Update a product badge
    question: How do I change just the color of an existing badge?
  - id: Badges_Default
    intent: Get a default badge template
    question: What default values does a new badge start with?
  - id: Badges_DeleteRoute
    intent: Bulk delete product badges
    question: How do I delete several badges at once?
  phrasing_ops: 11
  slug: optimizely-badges-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Batch API from Optimizely — 1 operation(s) for batch.
  name: Optimizely Batch API
  phrasing_intents:
  - id: BatchmultipleAPIendpointsintoonerequest.
    intent: Batch several Agent requests into one call
    question: Can I send a batch of activate decisions for many users in one request to Optimizely Agent?
  phrasing_ops: 1
  slug: optimizely-batch-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Create and send messages as batches to recipients segmented in separate platform
  name: Optimizely Batch sending API
  phrasing_intents:
  - id: getSendingBatch
    intent: Check the status of a sending batch
    question: What state is my campaign sending batch in, and which recipient list does it use?
  - id: addRecipients_1
    intent: Upload a chunk of recipients to a batch
    question: How do I upload recipients to a sending batch in chunks before sending anything?
  - id: importRecipientsAndSendBatch
    intent: Import recipients and send the batch campaign
    question: How do I finish a sending batch and actually start the campaign going out?
  - id: selectSendingBatches
    intent: List all sending batches
    question: Which sending batches exist for my client, and what state is each in?
  - id: prepareNewBatch
    intent: Prepare a new campaign sending batch
    question: How do I set up a new sending batch from a campaign definition?
  phrasing_ops: 5
  slug: optimizely-batch-sending-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Bill To Address Fields API from Optimizely — 5 operation(s) for bill to address fields.
  name: Optimizely Bill To Address Fields API
  phrasing_intents:
  - id: BillToAddressFields_Get
    intent: List bill-to address fields
    question: Which fields appear on the bill-to address form at checkout?
  - id: BillToAddressFields_Post
    intent: Add a bill-to address field
    question: How do I add a new field to the billing address form?
  - id: BillToAddressFields_GetById
    intent: Get one bill-to address field
    question: How do I read the settings of a single billing address field?
  - id: BillToAddressFields_PutById
    intent: Replace a bill-to address field
    question: What's the call to overwrite a billing address field definition entirely?
  - id: BillToAddressFields_DeleteById
    intent: Delete a bill-to address field
    question: How do I remove a field from the billing address form?
  - id: BillToAddressFields_PatchById
    intent: Update a bill-to address field
    question: How do I hide a billing address field without deleting it?
  - id: BillToAddressFields_Default
    intent: Get the default bill-to field template
    question: What are the default settings for a new billing address field?
  - id: BillToAddressFields_DeleteRoute
    intent: Bulk delete bill-to address fields
    question: Can I remove several billing address fields at once?
  phrasing_ops: 9
  slug: optimizely-bill-to-address-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Billtos API from Optimizely — 4 operation(s) for billtos.
  name: Optimizely Billtos API
  phrasing_intents:
  - id: ShipTosV1_GetAsync
    intent: Get one ship-to address under a bill-to
    question: How do I look up a specific ship-to address for a billing account?
  - id: ShipTosV1_PatchAsync
    intent: Update a ship-to address
    question: How do I change the street or city on an existing ship-to address?
  - id: ShipTosV1_GetCollectionAsync
    intent: List ship-to addresses for a bill-to
    question: Which shipping addresses are on file for a billing account?
  - id: ShipTosV1_PostAsync
    intent: Add a ship-to address to a bill-to
    question: How do I add a new shipping address to a customer's billing account?
  - id: BillTosV1_GetCollectionAsync
    intent: List bill-to billing accounts
    question: Which billing accounts can the current storefront user order against?
  - id: BillTosV1_PostAsync
    intent: Create a bill-to billing account
    question: How do I create a new billing address for a customer?
  - id: BillTosV1_GetAsync
    intent: Get one bill-to billing account
    question: How do I view the details of a single billing account, including its cost codes?
  - id: BillTosV1_PatchAsync
    intent: Update a bill-to billing account
    question: How do I change the billing address or contact on a bill-to?
  phrasing_ops: 8
  slug: optimizely-billtos-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Blob Storage Containers API from Optimizely — 2 operation(s) for blob storage containers.
  name: Optimizely Blob Storage Containers API
  phrasing_intents:
  - id: BlobStorageContainersApi_GetBlobStorageContainers
    intent: List blob storage containers for an environment
    question: Which blob storage containers exist for my Optimizely DXP project in a given environment?
  - id: BlobStorageContainersApi_GenerateSasLink
    intent: Generate a SAS link to a storage container
    question: How do I get a SAS link to download files from a blob storage container?
  phrasing_ops: 2
  slug: optimizely-blob-storage-containers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage recipients on the blocklist
  name: Optimizely Blocklist entries API
  phrasing_intents:
  - id: blacklisted
    intent: Check if an address is blocklisted
    question: Is this email address on my blocklist?
  - id: count_2
    intent: Count blocklist entries
    question: How many entries are on my client's blocklist?
  - id: findAllBlacklistEntries
    intent: List blocklist entries
    question: Which addresses and patterns are on my blocklist, and why?
  - id: createBlacklistEntry
    intent: Add an address or pattern to the blocklist
    question: How do I stop mailings from going to a certain address or domain?
  - id: deleteBlacklistEntries
    intent: Remove several blocklist entries
    question: Can I unblock multiple addresses in one request?
  - id: getBlacklistEntry
    intent: Get a blocklist entry's details
    question: Why was a specific address added to the blocklist, and when?
  - id: deleteBlacklistEntry
    intent: Remove one blocklist entry
    question: How do I take a single address off the blocklist?
  phrasing_ops: 7
  slug: optimizely-blocklist-entries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brand Category Images API from Optimizely — 6 operation(s) for brand category images.
  name: Optimizely Brand Category Images API
  phrasing_intents:
  - id: BrandCategoryImages_Get
    intent: List brand category images
    question: Which images are set up for our brand category pages?
  - id: BrandCategoryImages_Post
    intent: Add an image for a brand category
    question: How do I set a manual image for a brand's category page?
  - id: BrandCategoryImages_GetById
    intent: Get a brand category image by id
    question: What image path and alt text are stored on a particular brand category image?
  - id: BrandCategoryImages_PutById
    intent: Replace a brand category image record
    question: Can I overwrite every setting of a brand category image in one request?
  - id: BrandCategoryImages_DeleteById
    intent: Delete a brand category image
    question: How do I remove one image from a brand category page?
  - id: BrandCategoryImages_PatchById
    intent: Update fields on a brand category image
    question: Can I just change the alt text on a brand category image?
  - id: BrandCategoryImages_Default
    intent: Call the brand category images Default function
    question: What does the Default function on brand category images return?
  - id: BrandCategoryImages_GetManualProductImagesByBrandidAndParentcategoryid
    intent: Get product images to choose for a brand category
    question: Which product images can I pick from when setting a manual image for a brand's category?
  phrasing_ops: 10
  slug: optimizely-brand-category-images-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brand Compliance API from Optimizely — 2 operation(s) for brand compliance.
  name: Optimizely Brand Compliance API
  phrasing_intents:
  - id: getTaskAssetDraftBrandCompliance
    intent: Get a draft's brand compliance check
    question: Did this asset draft pass the brand compliance review?
  - id: updateTaskAssetDraftBrandCompliance
    intent: Record a draft's brand compliance result
    question: How do I mark an asset draft as brand compliant or not?
  - id: listBrandComplianceCategories
    intent: List brand compliance categories
    question: What brand compliance categories can a draft be checked against?
  phrasing_ops: 3
  slug: optimizely-brand-compliance-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brandalphabet API from Optimizely — 1 operation(s) for brandalphabet.
  name: Optimizely Brandalphabet API
  phrasing_intents:
  - id: BrandAlphabetV1_GetAsync
    intent: Get the brand alphabet index
    question: Which letters of the alphabet have brands for an A to Z brand directory?
  phrasing_ops: 1
  slug: optimizely-brandalphabet-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Brands API from Optimizely — 23 operation(s) for brands.
  name: Optimizely Brands API
  phrasing_intents:
  - id: Brands_Get
    intent: List brands in the commerce admin
    question: How do I pull every brand record from the Optimizely Configured Commerce admin API?
  - id: Brands_Post
    intent: Create a new brand
    question: What fields do I need to set up a new brand, like logos, URL segment and SEO title?
  - id: Brands_GetById
    intent: Get one brand's admin record
    question: How can I look up a single brand's admin record by its ID?
  - id: Brands_PutById
    intent: Replace a brand record entirely
    question: Can I overwrite an existing brand with a complete new set of values?
  - id: Brands_DeleteById
    intent: Delete a single brand
    question: How do I remove one brand from the catalog by its ID?
  - id: Brands_PatchById
    intent: Update selected fields on a brand
    question: Can I change just a brand's sort order or logo alt text without resending everything?
  - id: Brands_Default
    intent: Get default values for a new brand
    question: What default values does the admin API pre-fill for a brand before I create one?
  - id: Brands_CheckBrandsPageByWebsiteid_1
    intent: Check a website's brands page (OData function)
    question: How can I check whether a website has a brands page using the OData Default.checkbrandspage function?
  phrasing_ops: 27
  slug: optimizely-brands-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Budget Calendars API from Optimizely — 5 operation(s) for budget calendars.
  name: Optimizely Budget Calendars API
  phrasing_intents:
  - id: BudgetCalendars_Get
    intent: List budget calendars
    question: What fiscal-year budget calendars are set up for my B2B customers?
  - id: BudgetCalendars_Post
    intent: Create a budget calendar
    question: How do I define budget periods for a customer's fiscal year?
  - id: BudgetCalendars_GetById
    intent: Get a budget calendar by id
    question: When does each budget period start for a given budget calendar?
  - id: BudgetCalendars_PutById
    intent: Replace a budget calendar
    question: How do I overwrite every period date on a budget calendar at once?
  - id: BudgetCalendars_DeleteById
    intent: Delete a budget calendar
    question: Can I remove one budget calendar by its id?
  - id: BudgetCalendars_PatchById
    intent: Update dates on a budget calendar
    question: How do I shift just one period's start date on a budget calendar?
  - id: BudgetCalendars_Default
    intent: Get a blank budget calendar template
    question: What default values does a new budget calendar start with?
  - id: BudgetCalendars_DeleteRoute
    intent: Bulk delete budget calendars
    question: Can I delete several budget calendars in one request?
  phrasing_ops: 12
  slug: optimizely-budget-calendars-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Budgets API from Optimizely — 2 operation(s) for budgets.
  name: Optimizely Budgets API
  phrasing_intents:
  - id: BudgetsV1_GetCollectionAsync
    intent: List budgets
    question: Which budgets are available to me in the storefront?
  - id: BudgetsV1_GetAsync
    intent: Get the budget for a fiscal year
    question: What does my budget look like for a given fiscal year?
  - id: BudgetsV1_PatchAsync
    intent: Update the budget for a fiscal year
    question: How do I change budget amounts for a fiscal year?
  phrasing_ops: 3
  slug: optimizely-budgets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Packages API from Optimizely — 7 operation(s) for carrier packages.
  name: Optimizely Carrier Packages API
  phrasing_intents:
  - id: CarrierPackages_Get
    intent: List carrier package types
    question: How do I list the shipping package sizes defined for my carriers in Optimizely Configured Commerce?
  - id: CarrierPackages_Post
    intent: Create a carrier package
    question: What dimensions and weight can I set on a new carrier package?
  - id: CarrierPackages_GetById
    intent: Get one carrier package
    question: How can I see the dimensions of a single carrier package?
  - id: CarrierPackages_PutById
    intent: Replace a carrier package
    question: Can I overwrite a carrier package with a full new set of dimensions?
  - id: CarrierPackages_DeleteById
    intent: Delete a carrier package
    question: How do I delete one carrier package by ID?
  - id: CarrierPackages_PatchById
    intent: Update a carrier package's fields
    question: Can I deactivate a carrier package without resending its dimensions?
  - id: CarrierPackages_Default
    intent: Get default values for a carrier package
    question: What defaults are pre-filled for a carrier package before I create it?
  - id: CarrierPackages_Archive
    intent: Archive carrier packages (OData action)
    question: Can I archive old carrier packages with the Default.archive POST action?
  phrasing_ops: 11
  slug: optimizely-carrier-packages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Zone Postal Code Ranges API from Optimizely — 5 operation(s) for carrier zone postal code ranges.
  name: Optimizely Carrier Zone Postal Code Ranges API
  phrasing_intents:
  - id: CarrierZonePostalCodeRanges_Get
    intent: List carrier zone postal code ranges
    question: Which postal code ranges map to each carrier shipping zone?
  - id: CarrierZonePostalCodeRanges_Post
    intent: Add a postal code range to a carrier zone
    question: How do I assign a range of ZIP codes to a carrier zone?
  - id: CarrierZonePostalCodeRanges_GetById
    intent: Get a carrier zone postal code range
    question: Can I look up one postal code range by its ID?
  - id: CarrierZonePostalCodeRanges_PutById
    intent: Replace a carrier zone postal code range
    question: Can I overwrite a postal code range record completely?
  - id: CarrierZonePostalCodeRanges_DeleteById
    intent: Delete a carrier zone postal code range
    question: How do I remove one ZIP range from a carrier zone?
  - id: CarrierZonePostalCodeRanges_PatchById
    intent: Update a carrier zone postal code range
    question: Can I widen a ZIP range by changing just its end value?
  - id: CarrierZonePostalCodeRanges_Default
    intent: Get default values for a postal code range
    question: What defaults are pre-filled for a new postal code range?
  - id: CarrierZonePostalCodeRanges_DeleteRoute
    intent: Delete several postal code ranges
    question: Can I bulk delete postal code ranges in one request?
  phrasing_ops: 9
  slug: optimizely-carrier-zone-postal-code-ranges-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Zone Rates API from Optimizely — 5 operation(s) for carrier zone rates.
  name: Optimizely Carrier Zone Rates API
  phrasing_intents:
  - id: CarrierZoneRates_Get
    intent: List carrier zone shipping rates
    question: How do I see the weight-based shipping rates for each carrier zone?
  - id: CarrierZoneRates_Post
    intent: Add a weight rate to a carrier zone
    question: How do I add a shipping rate for a weight break in a carrier zone?
  - id: CarrierZoneRates_GetById
    intent: Get one carrier zone rate
    question: How do I look up a single carrier zone rate by its ID?
  - id: CarrierZoneRates_PutById
    intent: Replace a carrier zone rate
    question: How do I overwrite a whole carrier zone rate record?
  - id: CarrierZoneRates_DeleteById
    intent: Delete a carrier zone rate
    question: How do I remove one weight rate from a carrier zone?
  - id: CarrierZoneRates_PatchById
    intent: Change the price on a carrier zone rate
    question: How do I raise the shipping price on an existing zone rate?
  - id: CarrierZoneRates_Default
    intent: Get a blank carrier zone rate template
    question: What default values does a new carrier zone rate start with?
  - id: CarrierZoneRates_DeleteRoute
    intent: Bulk delete carrier zone rates
    question: How do I delete several carrier zone rates at once?
  phrasing_ops: 9
  slug: optimizely-carrier-zone-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carrier Zones API from Optimizely — 7 operation(s) for carrier zones.
  name: Optimizely Carrier Zones API
  phrasing_intents:
  - id: CarrierZones_Get
    intent: List carrier shipping zones
    question: Which shipping zones are set up for my carriers?
  - id: CarrierZones_Post
    intent: Add a shipping zone to a carrier
    question: How do I define a new shipping zone for a carrier?
  - id: CarrierZones_GetById
    intent: Get one carrier zone
    question: How do I look up a single carrier zone by its ID?
  - id: CarrierZones_PutById
    intent: Replace a carrier zone record
    question: How do I overwrite a carrier zone with a complete new record?
  - id: CarrierZones_DeleteById
    intent: Delete a carrier zone
    question: How do I remove one shipping zone from a carrier?
  - id: CarrierZones_PatchById
    intent: Rename or reassign a carrier zone
    question: Can I just rename a carrier zone without touching its other fields?
  - id: CarrierZones_Default
    intent: Call the Default function on carrier zones
    question: What does the Default OData function on carrier zones give back?
  - id: CarrierZones_DeleteRoute
    intent: Bulk delete carrier zones by ID
    question: Can I remove several carrier zones in a single request?
  phrasing_ops: 11
  slug: optimizely-carrier-zones-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carriers API from Optimizely — 12 operation(s) for carriers.
  name: Optimizely Carriers API
  phrasing_intents:
  - id: Carriers_Get
    intent: List shipping carriers
    question: Which shipping carriers are configured in Optimizely Commerce?
  - id: Carriers_Post
    intent: Add a shipping carrier
    question: What credentials and URLs do I need to register a new carrier?
  - id: Carriers_GetById
    intent: Get one shipping carrier
    question: What settings are stored for a single carrier?
  - id: Carriers_PutById
    intent: Replace a shipping carrier's full setup
    question: Can I overwrite a carrier's entire configuration in one call?
  - id: Carriers_DeleteById
    intent: Delete one shipping carrier
    question: How do I remove a single shipping carrier?
  - id: Carriers_PatchById
    intent: Update selected carrier settings
    question: Can I switch a carrier from test to live mode without resending everything?
  - id: Carriers_Default
    intent: Get default values for a new carrier
    question: What defaults does a new carrier record start with?
  - id: Carriers_DeleteRoute
    intent: Bulk delete shipping carriers
    question: Can I remove several carriers in one request?
  phrasing_ops: 16
  slug: optimizely-carriers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Carts API from Optimizely — 8 operation(s) for carts.
  name: Optimizely Carts API
  phrasing_intents:
  - id: PromotionsV1_GetCollectionAsync
    intent: List promotions applied to a cart
    question: Which promotions are currently applied to a shopper's cart?
  - id: PromotionsV1_PostAsync
    intent: Apply a promotion code to a cart
    question: How do I apply a promo code to a customer's cart?
  - id: PromotionsV1_DeleteCollectionAsync
    intent: Remove all promotions from a cart
    question: How do I strip every promo code off a cart at once?
  - id: PromotionsV1_GetAsync
    intent: Get one promotion applied to a cart
    question: What discount amount did a specific promotion give on a cart?
  - id: PromotionsV1_DeleteAsync
    intent: Remove one promotion from a cart
    question: How do I remove just one promo code from a cart and keep the others?
  - id: CartsV1_GetCollectionAsync
    intent: List carts and orders in progress
    question: How do I find all carts for a particular bill-to account?
  - id: CartsV1_PostAsync
    intent: Create a new cart
    question: How do I start a new cart for a customer's bill-to and ship-to addresses?
  - id: CartsV1_GetAsync
    intent: Get a cart's details and totals
    question: What's the grand total, tax and shipping on a specific cart?
  phrasing_ops: 18
  slug: optimizely-carts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Catalogpages API from Optimizely — 1 operation(s) for catalogpages.
  name: Optimizely Catalogpages API
  phrasing_intents:
  - id: CategoriesV1_GetAsync
    intent: Get a catalog page by its URL path
    question: How do I resolve a storefront URL path to its catalog page?
  phrasing_ops: 1
  slug: optimizely-catalogpages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Categories API from Optimizely — 22 operation(s) for categories.
  name: Optimizely Categories API
  phrasing_intents:
  - id: Categories_Get
    intent: List product categories in the admin console
    question: How do I pull every product category from the Commerce admin API?
  - id: Categories_Post
    intent: Create a new product category
    question: What fields are required when I add a new product category?
  - id: Categories_GetById
    intent: Get one category by its id in the admin API
    question: How can I look up a single category record by its id as an admin?
  - id: Categories_PutById
    intent: Replace a category record entirely
    question: Can I overwrite every field of an existing category in one call?
  - id: Categories_DeleteById
    intent: Delete a single category by id
    question: How do I delete one category by its id?
  - id: Categories_PatchById
    intent: Update some fields on a category
    question: Can I change just a category's meta description without resending everything?
  - id: Categories_Default
    intent: Get default values for a new category
    question: What default values does a brand-new category start with?
  - id: Categories_Archive
    intent: Archive categories via the OData archive action
    question: How do I archive several categories using the OData archive action?
  phrasing_ops: 26
  slug: optimizely-categories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Attribute Types API from Optimizely — 7 operation(s) for category attribute types.
  name: Optimizely Category Attribute Types API
  phrasing_intents:
  - id: CategoryAttributeTypes_Get
    intent: List attribute types assigned to categories
    question: How do I list which attribute types are attached to product categories?
  - id: CategoryAttributeTypes_Post
    intent: Assign an attribute type to a category
    question: How do I attach an attribute type like color or size to a product category?
  - id: CategoryAttributeTypes_GetById
    intent: Get one category attribute type assignment
    question: How do I look up a single category-to-attribute-type link by its id?
  - id: CategoryAttributeTypes_PutById
    intent: Replace a category attribute type assignment
    question: How do I overwrite a category attribute type assignment entirely?
  - id: CategoryAttributeTypes_DeleteById
    intent: Remove an attribute type from a category
    question: How do I detach one attribute type from a category?
  - id: CategoryAttributeTypes_PatchById
    intent: Update fields on a category attribute type
    question: How do I deactivate an attribute type on a category without resending everything?
  - id: CategoryAttributeTypes_Default
    intent: Get the default category attribute type record
    question: What does a default category attribute type record look like?
  - id: CategoryAttributeTypes_Archive
    intent: Archive category attribute types via action
    question: How do I archive category attribute assignments with the OData archive action?
  phrasing_ops: 11
  slug: optimizely-category-attribute-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Attribute Values API from Optimizely — 5 operation(s) for category attribute values.
  name: Optimizely Category Attribute Values API
  phrasing_intents:
  - id: CategoryAttributeValues_Get
    intent: List category attribute value links
    question: Which attribute values are assigned to which categories?
  - id: CategoryAttributeValues_Post
    intent: Assign an attribute value to a category
    question: How do I attach an attribute value to a product category?
  - id: CategoryAttributeValues_GetById
    intent: Get a category attribute value link
    question: How do I look up one category-to-attribute-value link?
  - id: CategoryAttributeValues_PutById
    intent: Replace a category attribute value link
    question: How do I overwrite a category attribute value record completely?
  - id: CategoryAttributeValues_DeleteById
    intent: Remove an attribute value from a category
    question: How do I unassign an attribute value from a category?
  - id: CategoryAttributeValues_PatchById
    intent: Update a category attribute value link
    question: How do I switch just the attribute value on a category link?
  - id: CategoryAttributeValues_Default
    intent: Get the default category attribute value template
    question: What default values does a new category attribute value link start with?
  - id: CategoryAttributeValues_DeleteRoute
    intent: Bulk delete category attribute value links
    question: How do I remove many category attribute value links at once?
  phrasing_ops: 9
  slug: optimizely-category-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Persona Extendeds API from Optimizely — 5 operation(s) for category persona extendeds.
  name: Optimizely Category Persona Extendeds API
  phrasing_intents:
  - id: CategoryPersonaExtendeds_Get
    intent: List category-to-persona assignments
    question: Which product categories are targeted to which personas?
  - id: CategoryPersonaExtendeds_Post
    intent: Link a category to a persona
    question: How do I show a category only to a particular persona?
  - id: CategoryPersonaExtendeds_GetById
    intent: Get a category persona assignment
    question: Which category and persona does a given assignment connect?
  - id: CategoryPersonaExtendeds_PutById
    intent: Replace a category persona assignment
    question: How do I overwrite a category persona record completely?
  - id: CategoryPersonaExtendeds_DeleteById
    intent: Remove a category persona assignment
    question: How do I stop targeting a category to a persona?
  - id: CategoryPersonaExtendeds_PatchById
    intent: Change the persona on a category assignment
    question: How do I switch an existing category assignment to a different persona?
  - id: CategoryPersonaExtendeds_Default
    intent: Get defaults for a new category persona link
    question: What defaults does a new category persona assignment start with?
  - id: CategoryPersonaExtendeds_DeleteRoute
    intent: Delete several category persona assignments
    question: How do I bulk remove category persona links?
  phrasing_ops: 9
  slug: optimizely-category-persona-extendeds-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Personas API from Optimizely — 5 operation(s) for category personas.
  name: Optimizely Category Personas API
  phrasing_intents:
  - id: CategoryPersonas_Get
    intent: List category-persona assignments
    question: Which catalog categories are targeted to which personas?
  - id: CategoryPersonas_Post
    intent: Assign a category to a persona
    question: How do I show a catalog category only to a certain persona?
  - id: CategoryPersonas_GetById
    intent: Get a category-persona assignment
    question: Can I look up one category-persona link by ID?
  - id: CategoryPersonas_PutById
    intent: Replace a category-persona assignment
    question: How do I overwrite a category-persona link entirely?
  - id: CategoryPersonas_DeleteById
    intent: Remove a category-persona assignment
    question: How do I stop targeting a category to a persona?
  - id: CategoryPersonas_PatchById
    intent: Change a category-persona assignment
    question: Can I point an existing assignment at a different persona?
  - id: CategoryPersonas_Default
    intent: Get default values for a new category-persona link
    question: What defaults does a new category-persona assignment start with?
  - id: CategoryPersonas_DeleteRoute
    intent: Bulk remove category-persona assignments
    question: Can I delete many category-persona links in one call?
  phrasing_ops: 9
  slug: optimizely-category-personas-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Products API from Optimizely — 5 operation(s) for category products.
  name: Optimizely Category Products API
  phrasing_intents:
  - id: CategoryProducts_Get
    intent: List product-to-category assignments
    question: Which products are assigned to which categories in my catalog?
  - id: CategoryProducts_Post
    intent: Assign a product to a category
    question: How do I put a product into a catalog category?
  - id: CategoryProducts_GetById
    intent: Get a product-to-category assignment
    question: What product and category does a given assignment record link?
  - id: CategoryProducts_PutById
    intent: Replace a product-to-category assignment
    question: How do I overwrite a whole category assignment record?
  - id: CategoryProducts_DeleteById
    intent: Remove a product from a category
    question: How do I take a product out of a category using its assignment ID?
  - id: CategoryProducts_PatchById
    intent: Update a product-to-category assignment
    question: Can I make an existing category assignment the product's primary category?
  - id: CategoryProducts_Default
    intent: Get a blank category assignment template
    question: What default values does a new category product link start with?
  - id: CategoryProducts_DeleteRoute
    intent: Bulk remove products from categories
    question: How do I remove many category assignments in one call?
  phrasing_ops: 9
  slug: optimizely-category-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Related Products API from Optimizely — 5 operation(s) for category related products.
  name: Optimizely Category Related Products API
  phrasing_intents:
  - id: CategoryRelatedProducts_Get
    intent: List category related products
    question: Which products are linked as related products to my catalog categories?
  - id: CategoryRelatedProducts_Post
    intent: Relate a product to a category
    question: How do I link a related product to a category?
  - id: CategoryRelatedProducts_GetById
    intent: Get a category related product link
    question: What category and product does one related-product record connect?
  - id: CategoryRelatedProducts_PutById
    intent: Replace a category related product link
    question: How do I overwrite a category related product record completely?
  - id: CategoryRelatedProducts_DeleteById
    intent: Delete a category related product link
    question: Can I unlink a related product from a category by the record ID?
  - id: CategoryRelatedProducts_PatchById
    intent: Update a category related product link
    question: How do I change the position of a related product within a category?
  - id: CategoryRelatedProducts_Default
    intent: Get a blank category related product template
    question: What default values does a new category related product have?
  - id: CategoryRelatedProducts_DeleteRoute
    intent: Bulk delete category related products
    question: Can I remove many category-product links at once?
  phrasing_ops: 9
  slug: optimizely-category-related-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Category Tax Exemptions API from Optimizely — 5 operation(s) for category tax exemptions.
  name: Optimizely Category Tax Exemptions API
  phrasing_intents:
  - id: CategoryTaxExemptions_Get
    intent: List category tax exemptions
    question: Which product categories have tax exemptions assigned?
  - id: CategoryTaxExemptions_Post
    intent: Assign a tax exemption to a category
    question: How do I make a product category tax exempt?
  - id: CategoryTaxExemptions_GetById
    intent: Get a category tax exemption by ID
    question: Which category and exemption does one category tax exemption record link?
  - id: CategoryTaxExemptions_PutById
    intent: Replace a category tax exemption
    question: Can I overwrite a whole category tax exemption record at once?
  - id: CategoryTaxExemptions_DeleteById
    intent: Remove a tax exemption from a category
    question: How do I stop a category from being tax exempt?
  - id: CategoryTaxExemptions_PatchById
    intent: Update a category tax exemption
    question: How do I switch an existing category exemption to a different tax exemption?
  - id: CategoryTaxExemptions_Default
    intent: Get a default category tax exemption template
    question: What default values does a new category tax exemption start with?
  - id: CategoryTaxExemptions_DeleteRoute
    intent: Bulk delete category tax exemptions
    question: How do I delete several category tax exemptions at once?
  phrasing_ops: 9
  slug: optimizely-category-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with approval of flag changes
  name: Optimizely Change Approvals API
  phrasing_intents:
  - id: get_environment_approval_settings
    intent: Get an environment's change approval settings
    question: Does this environment require approval before changes go live?
  phrasing_ops: 1
  slug: optimizely-change-approvals-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get a list of changes by project.
  name: Optimizely Change History API
  phrasing_intents:
  - id: list_change_history
    intent: List changes made in a project
    question: How do I see who changed what in an Optimizely project?
  phrasing_ops: 1
  slug: optimizely-change-history-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Changes API from Optimizely — 1 operation(s) for changes.
  name: Optimizely Changes API
  phrasing_intents:
  - id: entities
    intent: Get change history for a feature flag
    question: What has changed on a feature flag in my project?
  phrasing_ops: 1
  slug: optimizely-changes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Checks API from Optimizely — 2 operation(s) for checks.
  name: Optimizely Checks API
  phrasing_intents:
  - id: Checks_PostStart
    intent: Run the post-start health check
    question: Is there a check that confirms the Commerce instance finished starting up?
  - id: Checks_PreStop
    intent: Run the pre-stop check before shutdown
    question: Is there a check to call before shutting a Commerce instance down?
  phrasing_ops: 2
  slug: optimizely-checks-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage click profiles
  name: Optimizely Click profiles API
  phrasing_intents:
  - id: selectClickProfiles
    intent: List click profiles
    question: Which click profiles exist for categorizing link clicks in Optimizely Campaign?
  - id: createClickProfile
    intent: Create a click profile
    question: How do I set up a new click profile to tag links in my mailings?
  - id: getAssignedLinks
    intent: List links assigned to a click profile
    question: Which mailing links is a click profile attached to?
  - id: assignLinksToClickProfile
    intent: Assign links to a click profile
    question: How do I attach specific links to a click profile?
  - id: unAssignLinksFromClickProfile
    intent: Unassign links from a click profile
    question: How can I detach links from a click profile without deleting the profile?
  - id: getClickProfile
    intent: Get one click profile's details
    question: What name, description and rule pattern does a specific click profile have?
  - id: updateClickProfile
    intent: Update a click profile
    question: Can I rename an existing click profile or change its description?
  phrasing_ops: 7
  slug: optimizely-click-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Collaborators API from Optimizely — 2 operation(s) for collaborators.
  name: Optimizely Collaborators API
  phrasing_intents:
  - id: list_collaborators
    intent: List account collaborators
    question: Who are the collaborators on my Optimizely account?
  - id: create_collaborators
    intent: Invite collaborators to projects
    question: How do I invite teammates to specific projects on my account?
  - id: list_invitations
    intent: List pending collaborator invitations
    question: Which invited collaborators have not accepted yet?
  phrasing_ops: 3
  slug: optimizely-collaborators-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Compliance API from Optimizely — 7 operation(s) for compliance.
  name: Optimizely Compliance API
  phrasing_intents:
  - id: gdpr-delete
    intent: Request GDPR deletion of a customer's data
    question: How do I honour a GDPR right-to-erasure request for a customer in Optimizely?
  - id: ccpa-delete
    intent: Request CCPA deletion of a customer's data
    question: What call deletes a California customer's data under CCPA?
  - id: ccpa-optout
    intent: Opt a customer out of data sale under CCPA
    question: How do I record a customer's CCPA opt-out request?
  - id: lgpd-delete
    intent: Request LGPD deletion of a customer's data
    question: How do I delete a Brazilian customer's data under LGPD?
  - id: gdpr-status
    intent: Check a GDPR delete request's status
    question: Has my earlier GDPR delete request been completed yet?
  - id: ccpa-status
    intent: Check a CCPA delete or opt-out request's status
    question: Is my CCPA delete or opt-out request still pending?
  - id: lgpd-status
    intent: Check an LGPD delete request's status
    question: Has my LGPD delete request finished processing?
  phrasing_ops: 7
  slug: optimizely-compliance-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Config API from Optimizely — 1 operation(s) for config.
  name: Optimizely Config API
  phrasing_intents:
  - id: getConfig
    intent: Get the experiment and feature config
    question: Which experiments and feature flags are defined for this environment?
  phrasing_ops: 1
  slug: optimizely-config-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage registration confirmations (opt-in emails)
  name: Optimizely Confirmations API
  phrasing_intents:
  - id: selectConfirmationMailings
    intent: List confirmation mailings
    question: Which confirmation mailings do I have set up and what status is each one in?
  - id: createConfirmationMailing
    intent: Create a confirmation mailing
    question: How do I set up a new confirmation email that goes to a recipient list?
  - id: getConfirmationMailing
    intent: Get a confirmation mailing
    question: What is the current status and type of one particular confirmation mailing?
  - id: deleteConfirmationMailing
    intent: Delete a confirmation mailing
    question: How do I permanently remove a confirmation mailing I no longer use?
  - id: updateCampaignMessage
    intent: Update a confirmation mailing's message
    question: How do I change the subject line or content of an existing confirmation mailing?
  - id: addAttachments
    intent: Attach files to a confirmation email
    question: How do I add a PDF or other attachment to a confirmation email?
  - id: deleteAttachments
    intent: Remove attachments from a confirmation email
    question: How do I take an attachment off a confirmation email message?
  - id: getCampaignMessageContent
    intent: Get a confirmation email's content
    question: What does the body of my confirmation email actually contain?
  phrasing_ops: 21
  slug: optimizely-confirmations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Consent API from Optimizely — 2 operation(s) for consent.
  name: Optimizely Consent API
  phrasing_intents:
  - id: update-consent
    intent: Update marketing consent for customers
    question: How do I record marketing opt-ins for many customers at once?
  - id: get-consent
    intent: Check a customer's marketing consent
    question: Has this customer consented to receive marketing emails?
  phrasing_ops: 2
  slug: optimizely-consent-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The legacy Consent API is only available for the United States region. Migrate to the latest Update consent API.
  name: Optimizely Consent (Legacy) API
  phrasing_intents:
  - id: consent-legacy
    intent: Update a customer's marketing consent
    question: How do I record that a customer opted in or out of marketing by email?
  phrasing_ops: 1
  slug: optimizely-consent-legacy-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Item Fields API from Optimizely — 5 operation(s) for content item fields.
  name: Optimizely Content Item Fields API
  phrasing_intents:
  - id: ContentItemFields_Get
    intent: List CMS content item fields
    question: How can I see all the content item fields stored for my site's CMS content?
  - id: ContentItemFields_Post
    intent: Create a content item field
    question: How do I add a new field value to a content item?
  - id: ContentItemFields_GetById
    intent: Get one content item field
    question: How can I read a single content item field by its id?
  - id: ContentItemFields_PutById
    intent: Replace a content item field
    question: How do I overwrite every property of a content item field?
  - id: ContentItemFields_DeleteById
    intent: Delete one content item field
    question: How do I remove a single content item field?
  - id: ContentItemFields_PatchById
    intent: Update fields of a content item field
    question: How can I change only the text value of a content field?
  - id: ContentItemFields_Default
    intent: Get defaults for a new content item field
    question: What default values does a new content item field get?
  - id: ContentItemFields_DeleteRoute
    intent: Bulk delete content item fields
    question: How do I delete many content item fields at once?
  phrasing_ops: 9
  slug: optimizely-content-item-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Items API from Optimizely — 5 operation(s) for content items.
  name: Optimizely Content Items API
  phrasing_intents:
  - id: ContentItems_Get
    intent: List CMS content items
    question: Which content items and pages exist on my commerce website's CMS?
  - id: ContentItems_Post
    intent: Create a content item
    question: How do I add a new page or widget content item to the CMS?
  - id: ContentItems_GetById
    intent: Get one content item
    question: What is the publish and approval status of a specific content item?
  - id: ContentItems_PutById
    intent: Replace a content item record
    question: How do I overwrite a content item with a complete new record?
  - id: ContentItems_DeleteById
    intent: Delete a content item
    question: How do I remove a single content item from the CMS?
  - id: ContentItems_PatchById
    intent: Partially update a content item
    question: Can I change just the publish date of an existing content item?
  - id: ContentItems_Default
    intent: Get the default content item template
    question: What default values does a new content item start with?
  - id: ContentItems_DeleteRoute
    intent: Bulk delete content items
    question: How do I delete many content items in one request?
  phrasing_ops: 9
  slug: optimizely-content-items-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Managers API from Optimizely — 6 operation(s) for content managers.
  name: Optimizely Content Managers API
  phrasing_intents:
  - id: ContentManagers_Get
    intent: List content managers
    question: Which content managers are set up in the commerce admin?
  - id: ContentManagers_Post
    intent: Create a content manager
    question: How do I register a new content manager container for page content?
  - id: ContentManagers_GetById
    intent: Get a content manager by id
    question: Can I look up one content manager by its id?
  - id: ContentManagers_PutById
    intent: Replace a content manager
    question: Is there a way to overwrite a content manager record completely?
  - id: ContentManagers_DeleteById
    intent: Delete a content manager
    question: Can I delete one content manager by id?
  - id: ContentManagers_PatchById
    intent: Rename or update a content manager
    question: How do I rename an existing content manager without replacing it?
  - id: ContentManagers_Default
    intent: Get a blank content manager template
    question: What default values does a new content manager start with?
  - id: ContentManagers_DeleteRoute
    intent: Bulk delete content managers
    question: Can I delete many content managers in one request?
  phrasing_ops: 10
  slug: optimizely-content-managers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Content Page States API from Optimizely — 5 operation(s) for content page states.
  name: Optimizely Content Page States API
  phrasing_intents:
  - id: ContentPageStates_Get
    intent: List content page states
    question: How can I see all the saved page states in the CMS?
  - id: ContentPageStates_Post
    intent: Create a content page state
    question: What is required to create a new content page state?
  - id: ContentPageStates_GetById
    intent: Get one content page state
    question: How do I open a single content page state by id?
  - id: ContentPageStates_PutById
    intent: Replace a content page state
    question: Can I overwrite a whole content page state record?
  - id: ContentPageStates_DeleteById
    intent: Delete a single content page state
    question: How do I delete one content page state?
  - id: ContentPageStates_PatchById
    intent: Schedule or edit part of a content page state
    question: Can I schedule an existing page state to publish later?
  - id: ContentPageStates_Default
    intent: Get default values for a new page state
    question: What defaults does a new content page state start with?
  - id: ContentPageStates_DeleteRoute
    intent: Delete several content page states at once
    question: How do I bulk delete content page states?
  phrasing_ops: 9
  slug: optimizely-content-page-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Contents API from Optimizely — 5 operation(s) for contents.
  name: Optimizely Contents API
  phrasing_intents:
  - id: Contents_Get
    intent: List CMS content revisions
    question: How do I list the content records managed in the commerce CMS?
  - id: Contents_Post
    intent: Create a content revision
    question: How do I add a new piece of HTML content for a device type?
  - id: Contents_GetById
    intent: Get a content revision
    question: How do I fetch one content record and its HTML by ID?
  - id: Contents_PutById
    intent: Replace a content revision
    question: How do I overwrite a content record in full?
  - id: Contents_DeleteById
    intent: Delete a content revision
    question: How do I delete one content record?
  - id: Contents_PatchById
    intent: Update a content revision
    question: How do I change just the HTML of an existing content record?
  - id: Contents_Default
    intent: Get a default content template
    question: What default values does a new content record start with?
  - id: Contents_DeleteRoute
    intent: Bulk delete content revisions
    question: How do I delete several content records at once?
  phrasing_ops: 9
  slug: optimizely-contents-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Countries API from Optimizely — 7 operation(s) for countries.
  name: Optimizely Countries API
  phrasing_intents:
  - id: Countries_Get
    intent: List the countries configured in the store
    question: Which countries are set up in our Optimizely Commerce admin?
  - id: Countries_Post
    intent: Add a new country
    question: What ISO codes and unit settings are required to add a country?
  - id: Countries_GetById
    intent: Get a country by id
    question: How do I look up one country's ISO codes and VAT default by its id?
  - id: Countries_PutById
    intent: Replace a country record
    question: Can I overwrite a country's whole record, including its ISO codes, in one call?
  - id: Countries_DeleteById
    intent: Delete a country
    question: Can I remove a single country from the store configuration?
  - id: Countries_PatchById
    intent: Update fields on a country
    question: How do I deactivate a country without resending all its details?
  - id: Countries_Default
    intent: Call the countries Default function
    question: What does the Default function on the Countries set return?
  - id: Countries_DeleteRoute
    intent: Bulk delete countries by id
    question: Can I delete several countries in one request by passing a list of ids?
  phrasing_ops: 11
  slug: optimizely-countries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Country Vat Rates API from Optimizely — 5 operation(s) for country vat rates.
  name: Optimizely Country Vat Rates API
  phrasing_intents:
  - id: CountryVatRates_Get
    intent: List country VAT rates
    question: How do I see the VAT rates configured per country in Optimizely Configured Commerce?
  - id: CountryVatRates_Post
    intent: Add a VAT rate for a country
    question: How can I set up a new VAT rate for a country and VAT code?
  - id: CountryVatRates_GetById
    intent: Get one country VAT rate
    question: What rate is stored on a particular country VAT rate record?
  - id: CountryVatRates_PutById
    intent: Replace a country VAT rate
    question: Can I overwrite a country VAT rate record with all new values?
  - id: CountryVatRates_DeleteById
    intent: Delete a country VAT rate
    question: How do I remove one country's VAT rate record?
  - id: CountryVatRates_PatchById
    intent: Change a country VAT rate
    question: The VAT rate changed in a country, can I update just the percentage?
  - id: CountryVatRates_Default
    intent: Get default values for a VAT rate
    question: What defaults are pre-filled for a new country VAT rate?
  - id: CountryVatRates_DeleteRoute
    intent: Delete several country VAT rates
    question: Can I bulk delete a set of country VAT rates?
  phrasing_ops: 9
  slug: optimizely-country-vat-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage coupon blocks that organize coupon codes
  name: Optimizely Coupon blocks API
  phrasing_intents:
  - id: selectCouponBlocks
    intent: List coupon blocks
    question: Which coupon blocks exist in my email marketing account?
  - id: createCouponBlock
    intent: Create a coupon block
    question: How do I set up a new coupon block to hand out discount codes in mailings?
  - id: getCouponBlock
    intent: Get a coupon block
    question: What is the name and coupon source of a specific coupon block?
  - id: deleteCouponBlock
    intent: Delete a coupon block
    question: Can I remove a whole coupon block I no longer use?
  - id: selectCouponCodes
    intent: List codes in a coupon block
    question: How many unassigned coupon codes are left in a coupon block?
  - id: createCouponCodes
    intent: Add coupon codes to a block
    question: How do I upload a batch of discount codes into a coupon block?
  - id: deleteAllCouponCodes
    intent: Delete several coupon codes from a block
    question: Can I delete a list of coupon codes from a coupon block in one request?
  - id: getCouponCode
    intent: Get a single coupon code
    question: Which mailing and recipient was a specific coupon code assigned to?
  phrasing_ops: 11
  slug: optimizely-coupon-blocks-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Credit Card Transactions API from Optimizely — 5 operation(s) for credit card transactions.
  name: Optimizely Credit Card Transactions API
  phrasing_intents:
  - id: CreditCardTransactions_Get
    intent: List credit card transactions
    question: Which credit card authorizations and captures has my store processed?
  - id: CreditCardTransactions_Post
    intent: Record a credit card transaction
    question: How do I log a gateway card transaction against an order?
  - id: CreditCardTransactions_GetById
    intent: Get one credit card transaction
    question: How do I pull up the gateway response for a single card transaction?
  - id: CreditCardTransactions_PutById
    intent: Replace a credit card transaction record
    question: How do I overwrite a card transaction record with a full set of fields?
  - id: CreditCardTransactions_DeleteById
    intent: Delete a credit card transaction record
    question: How do I remove a card transaction record from the admin data?
  - id: CreditCardTransactions_PatchById
    intent: Update fields on a card transaction
    question: Can I flag a card transaction as posted to the ERP without touching anything else?
  - id: CreditCardTransactions_Default
    intent: Call the Default function on card transactions
    question: What does the Default OData function on credit card transactions return?
  - id: CreditCardTransactions_DeleteRoute
    intent: Bulk delete credit card transactions
    question: Can I delete several card transaction records at once?
  phrasing_ops: 9
  slug: optimizely-credit-card-transactions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Criteria Types API from Optimizely — 1 operation(s) for criteria types.
  name: Optimizely Criteria Types API
  phrasing_intents:
  - id: CriteriaTypes_Get
    intent: List rule criteria types
    question: What criteria types can I use when building rules in the commerce admin?
  phrasing_ops: 1
  slug: optimizely-criteria-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Currencies API from Optimizely — 7 operation(s) for currencies.
  name: Optimizely Currencies API
  phrasing_intents:
  - id: Currencies_Get
    intent: List currencies
    question: Which currencies are configured in my Optimizely commerce admin?
  - id: Currencies_Post
    intent: Add a currency
    question: How do I add a new currency like EUR with its symbol?
  - id: Currencies_GetById
    intent: Get a currency
    question: What symbol and code does a given currency record use?
  - id: Currencies_PutById
    intent: Replace a currency record
    question: How do I overwrite a whole currency definition?
  - id: Currencies_DeleteById
    intent: Delete a currency
    question: How do I remove a currency we no longer sell in?
  - id: Currencies_PatchById
    intent: Update a currency
    question: How do I change just the symbol of a currency?
  - id: Currencies_Default
    intent: Get a blank default currency
    question: What does a blank currency object look like before I create one?
  - id: Currencies_DeleteRoute
    intent: Delete several currencies
    question: Can I delete multiple currencies in one call?
  phrasing_ops: 11
  slug: optimizely-currencies-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Currency Rates API from Optimizely — 5 operation(s) for currency rates.
  name: Optimizely Currency Rates API
  phrasing_intents:
  - id: CurrencyRates_Get
    intent: List currency conversion rates
    question: What currency conversion rates are configured in my commerce store?
  - id: CurrencyRates_Post
    intent: Add a currency conversion rate
    question: How do I add a new exchange rate for a currency?
  - id: CurrencyRates_GetById
    intent: Get one currency rate
    question: What conversion rate and effective date does a specific currency rate record hold?
  - id: CurrencyRates_PutById
    intent: Replace a currency rate record
    question: Is there a way to overwrite a whole currency rate record at once?
  - id: CurrencyRates_DeleteById
    intent: Delete one currency rate
    question: How do I remove an exchange rate that was entered by mistake?
  - id: CurrencyRates_PatchById
    intent: Update a currency conversion rate
    question: Can I change just the conversion rate value of an existing currency rate?
  - id: CurrencyRates_Default
    intent: Call the Default function on currency rates
    question: What does the Default function on the currency rates entity set return?
  - id: CurrencyRates_DeleteRoute
    intent: Bulk delete currency rates by ID
    question: Can I delete many currency rates in one call?
  phrasing_ops: 9
  slug: optimizely-currency-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage custom blocklists
  name: Optimizely Custom blocklists API
  phrasing_intents:
  - id: selectCustomBlacklists
    intent: List custom blocklists
    question: Which custom blocklists does my Optimizely client have, and what hash algorithm does each use?
  - id: createCustomBlacklist
    intent: Create a custom blocklist
    question: How do I create a new blocklist to keep certain recipients out of mailings?
  - id: selectCustomBlacklistEntries
    intent: List entries in a custom blocklist
    question: What patterns are in a custom blocklist, and why was each blocked?
  - id: createBlacklistEntries
    intent: Add patterns to a custom blocklist
    question: How do I block new email addresses or domains by adding them to a blocklist?
  - id: wipeCustomBlacklistEntries
    intent: Clear all entries from a custom blocklist
    question: How do I empty a blocklist completely while keeping the list itself?
  - id: getCustomBlacklistEntry
    intent: Get one custom blocklist entry
    question: When was a specific blocklist entry created and for what reason?
  - id: updateCustomBlacklistEntry
    intent: Update a custom blocklist entry's reason
    question: How do I change the reason recorded on a blocklist entry?
  - id: deleteCustomBlacklistEntry
    intent: Remove one entry from a custom blocklist
    question: How do I unblock a single address by deleting its blocklist entry?
  phrasing_ops: 10
  slug: optimizely-custom-blocklists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to manage Custom Field definitions for organizing and annotating flags
  name: Optimizely Custom Fields API
  phrasing_intents:
  - id: list_custom_fields
    intent: List custom fields in a project
    question: Which custom fields are defined in my experimentation project?
  - id: create_custom_field
    intent: Create a custom field
    question: How do I add a custom field to flags or experiments in a project?
  - id: update_custom_field
    intent: Update a custom field
    question: How do I rename an existing custom field?
  - id: archive_custom_field
    intent: Archive a custom field
    question: How do I retire a custom field without deleting it?
  - id: unarchive_custom_field
    intent: Restore an archived custom field
    question: How do I bring back a custom field I archived?
  phrasing_ops: 5
  slug: optimizely-custom-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Custom Properties API from Optimizely — 6 operation(s) for custom properties.
  name: Optimizely Custom Properties API
  phrasing_intents:
  - id: CustomProperties_Get
    intent: List custom properties
    question: Which custom properties have been added across my commerce entities?
  - id: CustomProperties_Post
    intent: Add a custom property to an entity
    question: How do I attach a custom name/value property to a commerce record?
  - id: CustomProperties_GetById
    intent: Get a custom property by id
    question: What name and value does a specific custom property hold?
  - id: CustomProperties_PutById
    intent: Replace a custom property
    question: How do I overwrite a custom property's entire record?
  - id: CustomProperties_DeleteById
    intent: Delete one custom property
    question: How do I remove a single custom property by id?
  - id: CustomProperties_PatchById
    intent: Change a custom property's value
    question: Can I update only the value of an existing custom property?
  - id: CustomProperties_Default
    intent: Get default values for a new custom property
    question: What defaults does a brand-new custom property carry?
  - id: CustomProperties_GetFullCustomPropertiesByParentidAndParententityname
    intent: Get all custom properties of a record via Default.GetAll
    question: How do I pull every custom property attached to one product or customer record?
  phrasing_ops: 10
  slug: optimizely-custom-properties-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Budgets API from Optimizely — 5 operation(s) for customer budgets.
  name: Optimizely Customer Budgets API
  phrasing_intents:
  - id: CustomerBudgets_Get
    intent: List customer budgets
    question: How do I list the spending budgets set for B2B customers?
  - id: CustomerBudgets_Post
    intent: Create a budget for a customer
    question: How do I set up a fiscal-year budget for a customer account?
  - id: CustomerBudgets_GetById
    intent: Get one customer budget
    question: How do I see a customer's budget versus actual spending by period?
  - id: CustomerBudgets_PutById
    intent: Replace a customer budget
    question: How do I overwrite an entire customer budget with new period figures?
  - id: CustomerBudgets_DeleteById
    intent: Delete a customer budget
    question: How do I delete a single customer budget?
  - id: CustomerBudgets_PatchById
    intent: Update selected periods of a customer budget
    question: How do I change the budget for just one period of a customer's year?
  - id: CustomerBudgets_Default
    intent: Get the default customer budget record
    question: What does an empty customer budget look like before I fill it in?
  - id: CustomerBudgets_DeleteRoute
    intent: Bulk delete customer budgets
    question: How do I delete several customer budgets at once?
  phrasing_ops: 9
  slug: optimizely-customer-budgets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Carriers API from Optimizely — 5 operation(s) for customer carriers.
  name: Optimizely Customer Carriers API
  phrasing_intents:
  - id: CustomerCarriers_Get
    intent: List customer shipping carrier assignments
    question: Which shipping carriers are assigned to which customers?
  - id: CustomerCarriers_Post
    intent: Assign a shipping carrier to a customer
    question: How do I restrict a customer to ship with a particular carrier?
  - id: CustomerCarriers_GetById
    intent: Get a customer carrier assignment
    question: Can I look up a single customer carrier link by its id?
  - id: CustomerCarriers_PutById
    intent: Replace a customer carrier assignment
    question: Can I fully rewrite a customer carrier assignment in one request?
  - id: CustomerCarriers_DeleteById
    intent: Remove a carrier from a customer
    question: How do I stop a customer from using a carrier they were assigned?
  - id: CustomerCarriers_PatchById
    intent: Change the carrier on a customer assignment
    question: Can I swap the carrier on an existing customer assignment without recreating it?
  - id: CustomerCarriers_Default
    intent: Call the customer carriers Default function
    question: What does the Default function on customer carriers return?
  - id: CustomerCarriers_DeleteRoute
    intent: Bulk delete customer carrier assignments
    question: Can I drop several customer carrier assignments at once?
  phrasing_ops: 9
  slug: optimizely-customer-carriers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Cost Codes API from Optimizely — 7 operation(s) for customer cost codes.
  name: Optimizely Customer Cost Codes API
  phrasing_intents:
  - id: CustomerCostCodes_Get
    intent: List customer cost codes
    question: Which cost codes are set up for my B2B customers?
  - id: CustomerCostCodes_Post
    intent: Create a customer cost code
    question: How do I add a cost code that a customer can charge orders to?
  - id: CustomerCostCodes_GetById
    intent: Get a customer cost code
    question: What customer and description belong to a given cost code record?
  - id: CustomerCostCodes_PutById
    intent: Replace a customer cost code
    question: How do I overwrite a cost code record completely?
  - id: CustomerCostCodes_DeleteById
    intent: Delete one customer cost code
    question: How do I remove a single cost code by id?
  - id: CustomerCostCodes_PatchById
    intent: Update fields on a customer cost code
    question: Can I deactivate a cost code without resending the whole record?
  - id: CustomerCostCodes_Default
    intent: Get default values for a new cost code
    question: What defaults does a new customer cost code start with?
  - id: CustomerCostCodes_Archive
    intent: Archive cost codes via the archive action
    question: Can I archive a batch of cost codes instead of deleting them?
  phrasing_ops: 11
  slug: optimizely-customer-cost-codes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Changes API from Optimizely — 5 operation(s) for customer order changes.
  name: Optimizely Customer Order Changes API
  phrasing_intents:
  - id: CustomerOrderChanges_Get
    intent: List customer order change records
    question: Where can I see the history of changes made to customer orders?
  - id: CustomerOrderChanges_Post
    intent: Record a change to a customer order
    question: How do I log that a product price or quantity changed on an order?
  - id: CustomerOrderChanges_GetById
    intent: Get a customer order change record
    question: Can I open one order change record by its id?
  - id: CustomerOrderChanges_PutById
    intent: Replace a customer order change record
    question: Is there a way to overwrite an order change record in full?
  - id: CustomerOrderChanges_DeleteById
    intent: Delete a customer order change record
    question: Can I delete one order change record by id?
  - id: CustomerOrderChanges_PatchById
    intent: Update fields on an order change record
    question: How do I fix just the new value on an order change entry?
  - id: CustomerOrderChanges_Default
    intent: Get a blank order change template
    question: What default values does a new order change record start with?
  - id: CustomerOrderChanges_DeleteRoute
    intent: Bulk delete order change records
    question: Can I delete many order change records at once?
  phrasing_ops: 9
  slug: optimizely-customer-order-changes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Gift Cards API from Optimizely — 5 operation(s) for customer order gift cards.
  name: Optimizely Customer Order Gift Cards API
  phrasing_intents:
  - id: CustomerOrderGiftCards_Get
    intent: List gift cards applied to orders
    question: Which gift cards have been applied to customer orders in my Optimizely commerce admin?
  - id: CustomerOrderGiftCards_Post
    intent: Apply a gift card to an order
    question: How do I attach a gift card to a customer order?
  - id: CustomerOrderGiftCards_GetById
    intent: Get an order gift card link
    question: Which order and gift card does a given link record connect?
  - id: CustomerOrderGiftCards_PutById
    intent: Replace an order gift card link
    question: How do I overwrite an order gift card record entirely?
  - id: CustomerOrderGiftCards_DeleteById
    intent: Remove a gift card from an order
    question: How do I detach a gift card that was applied to an order?
  - id: CustomerOrderGiftCards_PatchById
    intent: Change the gift card on an order link
    question: How do I swap the gift card on an existing order link?
  - id: CustomerOrderGiftCards_Default
    intent: Get a blank default order gift card
    question: What does an empty order gift card record look like?
  - id: CustomerOrderGiftCards_DeleteRoute
    intent: Delete several order gift card links
    question: Can I remove multiple order gift card links at once?
  phrasing_ops: 9
  slug: optimizely-customer-order-gift-cards-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Promotions API from Optimizely — 5 operation(s) for customer order promotions.
  name: Optimizely Customer Order Promotions API
  phrasing_intents:
  - id: CustomerOrderPromotions_Get
    intent: List promotions applied to orders
    question: Which promotions have been applied to customer orders?
  - id: CustomerOrderPromotions_Post
    intent: Apply a promotion to an order
    question: How do I record a promotion against a customer order?
  - id: CustomerOrderPromotions_GetById
    intent: Get an applied order promotion
    question: What discount amount did a particular order promotion record give?
  - id: CustomerOrderPromotions_PutById
    intent: Replace an applied order promotion
    question: How do I overwrite an order promotion record in full?
  - id: CustomerOrderPromotions_DeleteById
    intent: Remove a promotion from an order
    question: How do I take a promotion off a customer order?
  - id: CustomerOrderPromotions_PatchById
    intent: Adjust an applied order promotion
    question: Can I change just the discount amount on an applied promotion?
  - id: CustomerOrderPromotions_Default
    intent: Get default values for a new order promotion
    question: What defaults does a new order promotion record start with?
  - id: CustomerOrderPromotions_DeleteRoute
    intent: Bulk delete order promotions
    question: Can I remove many applied promotions in one request?
  phrasing_ops: 9
  slug: optimizely-customer-order-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Order Taxes API from Optimizely — 5 operation(s) for customer order taxes.
  name: Optimizely Customer Order Taxes API
  phrasing_intents:
  - id: CustomerOrderTaxes_Get
    intent: List tax lines on customer orders
    question: What tax lines have been applied to orders in Optimizely Commerce?
  - id: CustomerOrderTaxes_Post
    intent: Add a tax line to a customer order
    question: How do I attach a tax line with a code and rate to an order?
  - id: CustomerOrderTaxes_GetById
    intent: Get one order tax line
    question: What rate and amount were charged on a specific order tax line?
  - id: CustomerOrderTaxes_PutById
    intent: Replace an order tax line
    question: Can I overwrite an order tax line in full?
  - id: CustomerOrderTaxes_DeleteById
    intent: Delete one order tax line
    question: How do I remove a tax line from an order?
  - id: CustomerOrderTaxes_PatchById
    intent: Adjust the rate or amount of an order tax
    question: Can I correct just the tax amount on an order tax line?
  - id: CustomerOrderTaxes_Default
    intent: Get default values for an order tax line
    question: What defaults does a new order tax line start with?
  - id: CustomerOrderTaxes_DeleteRoute
    intent: Bulk delete order tax lines
    question: Can I remove many order tax lines in one request?
  phrasing_ops: 9
  slug: optimizely-customer-order-taxes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Orders API from Optimizely — 14 operation(s) for customer orders.
  name: Optimizely Customer Orders API
  phrasing_intents:
  - id: CustomerOrders_Get
    intent: List customer orders
    question: Which customer orders are in the commerce admin right now?
  - id: CustomerOrders_Post
    intent: Create a customer order
    question: How do I create a new customer order through the admin API?
  - id: CustomerOrders_GetById
    intent: Get a customer order
    question: Can I pull up one customer order by its ID?
  - id: CustomerOrders_PutById
    intent: Replace a customer order
    question: How do I overwrite an entire customer order record with new values?
  - id: CustomerOrders_DeleteById
    intent: Delete a customer order
    question: How do I remove a single customer order by ID?
  - id: CustomerOrders_PatchById
    intent: Update fields on a customer order
    question: Can I change just the notes or status on an existing customer order?
  - id: CustomerOrders_Default
    intent: Get default values for a new customer order
    question: What default values does a brand-new customer order start with?
  - id: CustomerOrders_TotalsById
    intent: Calculate totals for a customer order
    question: Can I get the calculated totals for a customer order via the OData Totals function?
  phrasing_ops: 18
  slug: optimizely-customer-orders-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Set Products API from Optimizely — 5 operation(s) for customer product set products.
  name: Optimizely Customer Product Set Products API
  phrasing_intents:
  - id: CustomerProductSetProducts_Get
    intent: List products in customer product sets
    question: Which products are included in my customers' restricted product sets in Optimizely Configured Commerce?
  - id: CustomerProductSetProducts_Post
    intent: Add a product to a customer product set
    question: How do I add a product to a customer-specific product set?
  - id: CustomerProductSetProducts_GetById
    intent: Get one customer product set entry
    question: How do I look up a single product-in-set entry by its ID?
  - id: CustomerProductSetProducts_PutById
    intent: Replace a customer product set entry
    question: Can I overwrite a product set entry with a different product and set?
  - id: CustomerProductSetProducts_DeleteById
    intent: Remove a product from a customer product set
    question: How do I take one product out of a customer product set?
  - id: CustomerProductSetProducts_PatchById
    intent: Update a customer product set entry
    question: Can I move a product set entry to a different customer product set?
  - id: CustomerProductSetProducts_Default
    intent: Get default values for a product set entry
    question: What defaults does the admin pre-fill for a new customer product set product?
  - id: CustomerProductSetProducts_DeleteRoute
    intent: Bulk remove products from customer product sets
    question: How do I remove many products from customer product sets at once?
  phrasing_ops: 9
  slug: optimizely-customer-product-set-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Sets API from Optimizely — 8 operation(s) for customer product sets.
  name: Optimizely Customer Product Sets API
  phrasing_intents:
  - id: CustomerProductSets_Get
    intent: List customer product sets
    question: Which customer-specific product sets exist in my commerce admin?
  - id: CustomerProductSets_Post
    intent: Create a customer product set
    question: How do I create a curated set of products for a specific customer?
  - id: CustomerProductSets_GetById
    intent: Get a customer product set
    question: What customer and dates are attached to one product set?
  - id: CustomerProductSets_PutById
    intent: Replace a customer product set
    question: How do I overwrite a customer product set's whole record?
  - id: CustomerProductSets_DeleteById
    intent: Delete one customer product set
    question: How do I remove a single customer product set by id?
  - id: CustomerProductSets_PatchById
    intent: Update fields on a customer product set
    question: Can I just change the end date of a customer product set?
  - id: CustomerProductSets_Default
    intent: Get default values for a new product set
    question: What defaults does a new customer product set start with?
  - id: CustomerProductSets_Archive
    intent: Archive product sets via the archive action
    question: Can I archive several customer product sets rather than delete them?
  phrasing_ops: 12
  slug: optimizely-customer-product-sets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Visibility Additions API from Optimizely — 5 operation(s) for customer product visibility additions.
  name: Optimizely Customer Product Visibility Additions API
  phrasing_intents:
  - id: CustomerProductVisibilityAdditions_Get
    intent: List customer product visibility additions
    question: How do I see which products have been made visible to specific customers?
  - id: CustomerProductVisibilityAdditions_Post
    intent: Make a product visible to a customer
    question: Can I let one customer see a product that's otherwise hidden?
  - id: CustomerProductVisibilityAdditions_GetById
    intent: Get one customer visibility addition
    question: Where do I look up a single customer visibility addition by id?
  - id: CustomerProductVisibilityAdditions_PutById
    intent: Replace a customer visibility addition
    question: How do I overwrite a customer visibility addition with a new customer and product?
  - id: CustomerProductVisibilityAdditions_DeleteById
    intent: Revoke a customer's product visibility
    question: Can I stop a customer from seeing a product I previously made visible to them?
  - id: CustomerProductVisibilityAdditions_PatchById
    intent: Update a customer visibility addition
    question: Can I change just the product on an existing customer visibility addition?
  - id: CustomerProductVisibilityAdditions_Default
    intent: Call the Default function on visibility additions
    question: What does the Default function on CustomerProductVisibilityAdditions return?
  - id: CustomerProductVisibilityAdditions_DeleteRoute
    intent: Bulk remove customer visibility additions
    question: Can I remove many customer visibility grants at once by id?
  phrasing_ops: 9
  slug: optimizely-customer-product-visibility-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Product Visibility Exceptions API from Optimizely — 5 operation(s) for customer product visibility exceptions.
  name: Optimizely Customer Product Visibility Exceptions API
  phrasing_intents:
  - id: CustomerProductVisibilityExceptions_Get
    intent: List customer product visibility exceptions
    question: Which products are hidden from specific customers?
  - id: CustomerProductVisibilityExceptions_Post
    intent: Hide a product from a customer
    question: How do I stop a specific customer from seeing a product?
  - id: CustomerProductVisibilityExceptions_GetById
    intent: Get a visibility exception
    question: Is there a call to read a single product visibility exception by ID?
  - id: CustomerProductVisibilityExceptions_PutById
    intent: Replace a visibility exception
    question: What's the call to overwrite a product visibility exception record?
  - id: CustomerProductVisibilityExceptions_DeleteById
    intent: Unhide a product for a customer
    question: How do I remove a visibility exception so the customer can see the product again?
  - id: CustomerProductVisibilityExceptions_PatchById
    intent: Update a visibility exception
    question: How do I point an existing visibility exception at a different product?
  - id: CustomerProductVisibilityExceptions_Default
    intent: Get the default visibility exception
    question: What does a blank customer product visibility exception look like?
  - id: CustomerProductVisibilityExceptions_DeleteRoute
    intent: Bulk delete visibility exceptions
    question: Can I remove many product visibility exceptions at once?
  phrasing_ops: 9
  slug: optimizely-customer-product-visibility-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer Products API from Optimizely — 5 operation(s) for customer products.
  name: Optimizely Customer Products API
  phrasing_intents:
  - id: CustomerProducts_Get
    intent: List customer-specific product names
    question: Which customers have their own part names for my products?
  - id: CustomerProducts_Post
    intent: Map a product to a customer's own part name
    question: How do I give a B2B customer their own name for one of my products?
  - id: CustomerProducts_GetById
    intent: Get a customer product by id
    question: What part name does one customer product mapping use?
  - id: CustomerProducts_PutById
    intent: Replace a customer product mapping
    question: How do I overwrite a whole customer product record at once?
  - id: CustomerProducts_DeleteById
    intent: Delete a customer product mapping
    question: Can I remove one customer's product alias by its id?
  - id: CustomerProducts_PatchById
    intent: Rename a customer product mapping
    question: How do I change just the name a customer uses for a product?
  - id: CustomerProducts_Default
    intent: Get a blank customer product template
    question: What default values does a new customer product start with?
  - id: CustomerProducts_DeleteRoute
    intent: Bulk delete customer products
    question: Can I delete several customer product mappings at once?
  phrasing_ops: 9
  slug: optimizely-customer-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Customer User Profiles API from Optimizely — 5 operation(s) for customer user profiles.
  name: Optimizely Customer User Profiles API
  phrasing_intents:
  - id: CustomerUserProfiles_Get
    intent: List customer-to-user assignments
    question: Which user profiles are linked to which customer accounts?
  - id: CustomerUserProfiles_Post
    intent: Assign a user to a customer account
    question: How do I give a user profile access to a customer account?
  - id: CustomerUserProfiles_GetById
    intent: Get a customer-to-user assignment
    question: Can I look up one customer and user link by its ID?
  - id: CustomerUserProfiles_PutById
    intent: Replace a customer-to-user assignment
    question: Can I overwrite a customer user link with a different pairing?
  - id: CustomerUserProfiles_DeleteById
    intent: Remove a user from a customer account
    question: How do I take away a user's access to one customer account?
  - id: CustomerUserProfiles_PatchById
    intent: Update a customer-to-user assignment
    question: Can I move a link to a different customer without resending everything?
  - id: CustomerUserProfiles_Default
    intent: Get default values for a customer user link
    question: What defaults are pre-filled for a new customer user profile?
  - id: CustomerUserProfiles_DeleteRoute
    intent: Remove several customer-to-user assignments
    question: Can I bulk remove customer user links in one call?
  phrasing_ops: 9
  slug: optimizely-customer-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dashboard Panel Positions API from Optimizely — 5 operation(s) for dashboard panel positions.
  name: Optimizely Dashboard Panel Positions API
  phrasing_intents:
  - id: DashboardPanelPositions_Get
    intent: List admin dashboard panel positions
    question: How do I see how each admin user has arranged the panels on their dashboard?
  - id: DashboardPanelPositions_Post
    intent: Place a panel on a user's dashboard
    question: How do I add a panel to an admin user's dashboard layout?
  - id: DashboardPanelPositions_GetById
    intent: Get one dashboard panel position
    question: How do I look up a single dashboard panel placement by ID?
  - id: DashboardPanelPositions_PutById
    intent: Replace a dashboard panel position
    question: How do I overwrite a whole dashboard panel position record?
  - id: DashboardPanelPositions_DeleteById
    intent: Remove a panel from a dashboard
    question: How do I take a panel off an admin user's dashboard?
  - id: DashboardPanelPositions_PatchById
    intent: Reorder a panel on a dashboard
    question: How do I move a dashboard panel to a different position?
  - id: DashboardPanelPositions_Default
    intent: Get a blank dashboard panel position template
    question: What default values does a new dashboard panel position start with?
  - id: DashboardPanelPositions_DeleteRoute
    intent: Bulk delete dashboard panel positions
    question: How do I clear several dashboard panel placements at once?
  phrasing_ops: 9
  slug: optimizely-dashboard-panel-positions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dashboardpanels API from Optimizely — 1 operation(s) for dashboardpanels.
  name: Optimizely Dashboardpanels API
  phrasing_intents:
  - id: DashboardsV1_GetAsync
    intent: Get the account dashboard panels
    question: Which panels appear on the signed-in user's account dashboard?
  phrasing_ops: 1
  slug: optimizely-dashboardpanels-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Data Generation API from Optimizely — 1 operation(s) for data generation.
  name: Optimizely Data Generation API
  phrasing_intents:
  - id: DataGeneration_PostAsync
    intent: Generate product content with AI
    question: Can the commerce admin generate or rewrite product content for me?
  phrasing_ops: 1
  slug: optimizely-data-generation-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Database Scripts API from Optimizely — 5 operation(s) for database scripts.
  name: Optimizely Database Scripts API
  phrasing_intents:
  - id: DatabaseScripts_Get
    intent: List applied database scripts
    question: Which database upgrade scripts have been applied to my commerce instance?
  - id: DatabaseScripts_Post
    intent: Record a database script
    question: How do I record that a database script was applied?
  - id: DatabaseScripts_GetById
    intent: Get a database script record
    question: How do I check when one database script was applied?
  - id: DatabaseScripts_PutById
    intent: Replace a database script record
    question: How do I overwrite a database script record in full?
  - id: DatabaseScripts_DeleteById
    intent: Delete a database script record
    question: How do I remove a database script record?
  - id: DatabaseScripts_PatchById
    intent: Update a database script record
    question: How do I correct the run time logged for a database script?
  - id: DatabaseScripts_Default
    intent: Get the default database script template
    question: What default values does a new database script record start with?
  - id: DatabaseScripts_DeleteRoute
    intent: Bulk delete database script records
    question: How do I delete several database script records at once?
  phrasing_ops: 9
  slug: optimizely-database-scripts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The DatabaseExports API from Optimizely — 2 operation(s) for databaseexports.
  name: Optimizely Database Exports API
  phrasing_intents:
  - id: DatabaseExportApi_ExportDatabase
    intent: Export a DXP database
    question: How do I export my CMS or Commerce database from a DXP environment as a bacpac?
  - id: DatabaseExportApi_GetExportDatabase
    intent: Check a database export's status
    question: Is my database export finished, and where do I download the bacpac?
  phrasing_ops: 2
  slug: optimizely-databaseexports-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dealer Categories API from Optimizely — 5 operation(s) for dealer categories.
  name: Optimizely Dealer Categories API
  phrasing_intents:
  - id: DealerCategories_Get
    intent: List dealer category assignments
    question: Which product categories does each dealer carry?
  - id: DealerCategories_Post
    intent: Assign a category to a dealer
    question: How do I tell the dealer locator that a dealer sells a category?
  - id: DealerCategories_GetById
    intent: Get a dealer category assignment
    question: Which dealer and category does a given assignment connect?
  - id: DealerCategories_PutById
    intent: Replace a dealer category assignment
    question: How do I overwrite a dealer category record completely?
  - id: DealerCategories_DeleteById
    intent: Remove a category from a dealer
    question: How do I stop listing a category for a dealer?
  - id: DealerCategories_PatchById
    intent: Change the category on a dealer assignment
    question: How do I switch an existing dealer assignment to another category?
  - id: DealerCategories_Default
    intent: Get defaults for a new dealer category
    question: What defaults does a new dealer category record start with?
  - id: DealerCategories_DeleteRoute
    intent: Delete several dealer category assignments
    question: How do I bulk remove dealer category records?
  phrasing_ops: 9
  slug: optimizely-dealer-categories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dealer Products API from Optimizely — 5 operation(s) for dealer products.
  name: Optimizely Dealer Products API
  phrasing_intents:
  - id: DealerProducts_Get
    intent: List dealer-product assignments
    question: Which products are carried by which dealers?
  - id: DealerProducts_Post
    intent: Assign a product to a dealer
    question: How do I mark a product as carried by a dealer?
  - id: DealerProducts_GetById
    intent: Get a dealer-product assignment
    question: Can I look up one dealer-product link by ID?
  - id: DealerProducts_PutById
    intent: Replace a dealer-product assignment
    question: How do I overwrite a dealer-product link completely?
  - id: DealerProducts_DeleteById
    intent: Remove a dealer-product assignment
    question: How do I stop a dealer from carrying a product?
  - id: DealerProducts_PatchById
    intent: Change a dealer-product assignment
    question: Can I switch an existing assignment to a different dealer?
  - id: DealerProducts_Default
    intent: Get default values for a new dealer-product link
    question: What defaults does a new dealer-product assignment start with?
  - id: DealerProducts_DeleteRoute
    intent: Bulk remove dealer-product assignments
    question: Can I delete many dealer-product links in one call?
  phrasing_ops: 9
  slug: optimizely-dealer-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Dealers API from Optimizely — 11 operation(s) for dealers.
  name: Optimizely Dealers API
  phrasing_intents:
  - id: Dealers_Get
    intent: List dealers in the admin console
    question: How can I pull the full dealer list as an admin, with filtering?
  - id: Dealers_Post
    intent: Create a dealer
    question: What address details are required when I add a new dealer location?
  - id: Dealers_GetById
    intent: Get a dealer record by ID (admin)
    question: Can I fetch one dealer's full admin record by its GUID?
  - id: Dealers_PutById
    intent: Replace a dealer record
    question: Can I overwrite an entire dealer record with a new address?
  - id: Dealers_DeleteById
    intent: Delete a dealer
    question: How do I remove a single dealer that has closed?
  - id: Dealers_PatchById
    intent: Update a dealer's details
    question: Can I change just a dealer's phone number without resending the address?
  - id: Dealers_Default
    intent: Get default values for a new dealer
    question: What does a blank dealer template look like before I fill it in?
  - id: Dealers_DeleteRoute
    intent: Delete several dealers at once
    question: Can I bulk delete a batch of dealers in one call?
  phrasing_ops: 15
  slug: optimizely-dealers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Decide API from Optimizely — 1 operation(s) for decide.
  name: Optimizely Decide API
  phrasing_intents:
  - id: decide
    intent: Decide feature flag variations for a user
    question: How do I find out which feature flag variations a user should get from Optimizely?
  phrasing_ops: 1
  slug: optimizely-decide-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📖 Definition ( v2 ) API from Optimizely — 2 operation(s) for 📖 definition ( v2 ).
  name: Optimizely 📖 Definition ( v2 ) API
  phrasing_intents:
  - id: post-ContentV2DataHandler
    intent: Sync content data for a Graph source
    question: How do I push content data from a source into Optimizely Graph?
  - id: delete-ContentV2DataHandler
    intent: Purge content data for a Graph source
    question: Can I wipe all indexed content data for one source?
  - id: post-ContentV2TypeHandler
    intent: Sync content type definitions to Graph
    question: How do I register my content types and property types with the Graph index?
  phrasing_ops: 3
  slug: optimizely-definition-v2-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📖 Definition ( v3 ) API from Optimizely — 2 operation(s) for 📖 definition ( v3 ).
  name: Optimizely 📖 Definition ( v3 ) API
  phrasing_intents:
  - id: get-ContentV3SourceHandler
    intent: Get content source metadata
    question: What content sources are defined in my Optimizely Graph instance and which languages do they cover?
  - id: delete-ContentV3SourceHandler
    intent: Delete a content source's types or data
    question: How do I wipe the indexed content and type definitions for a source?
  - id: post-ContentV3SourceHandler
    intent: Update a content source's label and description
    question: How do I rename a content source or change its description?
  - id: get-ContentV3TypeHandler
    intent: Get a source's content types
    question: Which content types are defined for a content source?
  - id: post-ContentV3TypeHandler
    intent: Partially update a source's content types
    question: How do I add or change a few content types without overwriting the rest?
  - id: put-ContentV3TypeHandler
    intent: Overwrite all content types of a source
    question: How do I replace every content type definition on a source at once?
  phrasing_ops: 6
  slug: optimizely-definition-v3-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Delivery management operations
  name: Optimizely Deliveries API
  phrasing_intents:
  - id: deliveriesList
    intent: List content recommendation deliveries
    question: Which widget deliveries are configured for content recommendations?
  - id: deliveryGet
    intent: Get a delivery by its API key
    question: How do I fetch the details of the delivery I'm authenticated as?
  phrasing_ops: 2
  slug: optimizely-deliveries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Deployments API from Optimizely — 5 operation(s) for deployments.
  name: Optimizely Deployments API
  phrasing_intents:
  - id: UploadPackageApi_GetUploadPackageLocation
    intent: Get an upload location for deployment packages
    question: Where do I upload a code package before deploying to DXP?
  - id: ResetCodeDeploymentApi_ResetCodeDeployment
    intent: Reset a deployment in verification
    question: How do I abort a deployment that's sitting in verification and reset the slot?
  - id: GetDeploymentDetailsApi_GetDeploymentDetails
    intent: Get a deployment's status and details
    question: What stage is a particular deployment in right now?
  - id: CompleteCodeDeploymentApi_CompleteCodeDeployment
    intent: Complete a deployment and swap to production
    question: How do I finish a verified deployment and swap it into production?
  - id: DeploymentApi_GetDeploymentList
    intent: List a project's deployments
    question: Which deployments have run for my DXP project?
  - id: DeploymentApi_StartCodeDeployment
    intent: Start a deployment to an environment
    question: How do I deploy a code package to a target environment?
  phrasing_ops: 6
  slug: optimizely-deployments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Device Tokens API from Optimizely — 7 operation(s) for device tokens.
  name: Optimizely Device Tokens API
  phrasing_intents:
  - id: DeviceTokensV1_RegisterDeviceToken
    intent: Register a device for push notifications
    question: How do I register a mobile device token so the current user gets push notifications?
  - id: DeviceTokensV1_UnregisterDeviceToken
    intent: Stop push notifications to a device
    question: How can an app stop push notifications to a device when the user logs out?
  - id: DeviceTokens_Get
    intent: List stored device tokens
    question: Which device tokens are stored in the Optimizely Commerce admin?
  - id: DeviceTokens_Post
    intent: Create a device token record as an admin
    question: Can an admin add a device token record directly for a user profile?
  - id: DeviceTokens_GetById
    intent: Get one device token record
    question: Which user does a stored device token belong to?
  - id: DeviceTokens_PutById
    intent: Replace a device token record
    question: Can I overwrite a stored device token record entirely?
  - id: DeviceTokens_DeleteById
    intent: Delete one device token record
    question: How do I delete a single stored device token record?
  - id: DeviceTokens_PatchById
    intent: Enable or disable a stored device token
    question: Can I disable a stored device token without deleting it?
  phrasing_ops: 11
  slug: optimizely-device-tokens-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Documents API from Optimizely — 5 operation(s) for documents.
  name: Optimizely Documents API
  phrasing_intents:
  - id: Documents_Get
    intent: List catalog documents
    question: Which documents, like spec sheets or manuals, are attached across my catalog?
  - id: Documents_Post
    intent: Add a document to a record
    question: How do I attach a spec sheet PDF to a product?
  - id: Documents_GetById
    intent: Get a catalog document
    question: Where is the file for a particular document stored?
  - id: Documents_PutById
    intent: Replace a catalog document
    question: How do I overwrite a document record in full?
  - id: Documents_DeleteById
    intent: Delete a catalog document
    question: How do I delete a document that is out of date?
  - id: Documents_PatchById
    intent: Update a catalog document
    question: Can I point an existing document at a new file without resending everything?
  - id: Documents_Default
    intent: Get a blank document template
    question: What default values does a new document record start with?
  - id: Documents_DeleteRoute
    intent: Bulk delete catalog documents
    question: How do I delete many documents at once?
  phrasing_ops: 9
  slug: optimizely-documents-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email API from Optimizely — 3 operation(s) for email.
  name: Optimizely Email API
  phrasing_intents:
  - id: EmailV1_Get
    intent: Get the storefront email resource
    question: What does the storefront email endpoint return in Optimizely Configured Commerce?
  - id: EmailV1_PostTellAFriend
    intent: Email a product to a friend
    question: How do I let a shopper send a product page to a friend by email?
  - id: EmailV1_PostContactUs
    intent: Submit a contact-us message
    question: How do I submit a storefront contact-us form on a customer's behalf?
  phrasing_ops: 3
  slug: optimizely-email-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Lists API from Optimizely — 7 operation(s) for email lists.
  name: Optimizely Email Lists API
  phrasing_intents:
  - id: EmailLists_Get
    intent: List email lists
    question: Which email lists are configured in the Optimizely Configured Commerce admin?
  - id: EmailLists_Post
    intent: Create an email list
    question: What do I need to set up a new email list with its subject and sender address?
  - id: EmailLists_GetById
    intent: Get one email list by ID
    question: How do I look up a single email list's subject and sender by its ID?
  - id: EmailLists_PutById
    intent: Replace an email list record entirely
    question: Can I overwrite an email list with a completely new set of values?
  - id: EmailLists_DeleteById
    intent: Delete a single email list
    question: How do I remove one email list by its ID?
  - id: EmailLists_PatchById
    intent: Update selected fields on an email list
    question: Can I change just the subject line of an email list?
  - id: EmailLists_Default
    intent: Get default values for a new email list
    question: What defaults does the admin pre-fill for an email list before I create one?
  - id: EmailLists_DeleteRoute
    intent: Bulk delete email lists by ID
    question: How do I delete several email lists in one request?
  phrasing_ops: 11
  slug: optimizely-email-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Message Addresses API from Optimizely — 5 operation(s) for email message addresses.
  name: Optimizely Email Message Addresses API
  phrasing_intents:
  - id: EmailMessageAddresses_Get
    intent: List email message addresses
    question: Which recipient addresses are recorded on outgoing commerce emails?
  - id: EmailMessageAddresses_Post
    intent: Add an address to an email message
    question: How do I add a recipient address to an email message?
  - id: EmailMessageAddresses_GetById
    intent: Get an email message address
    question: What address and recipient type does one email message address record hold?
  - id: EmailMessageAddresses_PutById
    intent: Replace an email message address
    question: How do I overwrite an email message address record completely?
  - id: EmailMessageAddresses_DeleteById
    intent: Delete an email message address
    question: Can I remove one recipient address from an email message?
  - id: EmailMessageAddresses_PatchById
    intent: Update an email message address
    question: How do I fix a typo in a recipient address on an email message?
  - id: EmailMessageAddresses_Default
    intent: Get a blank email message address template
    question: What default values does a new email message address have?
  - id: EmailMessageAddresses_DeleteRoute
    intent: Bulk delete email message addresses
    question: Can I delete several email message addresses at once?
  phrasing_ops: 9
  slug: optimizely-email-message-addresses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Message Attachments API from Optimizely — 5 operation(s) for email message attachments.
  name: Optimizely Email Message Attachments API
  phrasing_intents:
  - id: EmailMessageAttachments_Get
    intent: List email message attachments
    question: Which files are attached to emails the commerce site has sent?
  - id: EmailMessageAttachments_Post
    intent: Attach a file to an email message
    question: How do I add a file attachment to a stored email message?
  - id: EmailMessageAttachments_GetById
    intent: Get an email message attachment by ID
    question: What file name and content does one email attachment hold?
  - id: EmailMessageAttachments_PutById
    intent: Replace an email message attachment
    question: Can I overwrite an entire email attachment record, file and all?
  - id: EmailMessageAttachments_DeleteById
    intent: Delete an email message attachment by ID
    question: How do I remove one attachment from a stored email?
  - id: EmailMessageAttachments_PatchById
    intent: Update an email message attachment
    question: How do I rename the file on an existing email attachment?
  - id: EmailMessageAttachments_Default
    intent: Get a default email attachment template
    question: What default values does a new email message attachment start with?
  - id: EmailMessageAttachments_DeleteRoute
    intent: Bulk delete email message attachments
    question: How do I delete several email attachments at once?
  phrasing_ops: 9
  slug: optimizely-email-message-attachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Message Delivery Attempts API from Optimizely — 5 operation(s) for email message delivery attempts.
  name: Optimizely Email Message Delivery Attempts API
  phrasing_intents:
  - id: EmailMessageDeliveryAttempts_Get
    intent: List email delivery attempts
    question: How can I see every attempt the site made to deliver its emails?
  - id: EmailMessageDeliveryAttempts_Post
    intent: Record an email delivery attempt
    question: How do I log a new delivery attempt for an email message?
  - id: EmailMessageDeliveryAttempts_GetById
    intent: Get one email delivery attempt
    question: How can I look up a single email delivery attempt?
  - id: EmailMessageDeliveryAttempts_PutById
    intent: Replace an email delivery attempt
    question: How do I overwrite an entire email delivery attempt record?
  - id: EmailMessageDeliveryAttempts_DeleteById
    intent: Delete one email delivery attempt
    question: How do I remove a single email delivery attempt from the log?
  - id: EmailMessageDeliveryAttempts_PatchById
    intent: Update an email delivery attempt
    question: How can I mark a delivery attempt as delivered after the fact?
  - id: EmailMessageDeliveryAttempts_Default
    intent: Get defaults for a new delivery attempt
    question: What default values does a new email delivery attempt have?
  - id: EmailMessageDeliveryAttempts_DeleteRoute
    intent: Bulk delete email delivery attempts
    question: How do I purge many email delivery attempts at once?
  phrasing_ops: 9
  slug: optimizely-email-message-delivery-attempts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Messages API from Optimizely — 8 operation(s) for email messages.
  name: Optimizely Email Messages API
  phrasing_intents:
  - id: EmailMessages_Get
    intent: List sent email messages
    question: How do I list the email messages the commerce platform has logged?
  - id: EmailMessages_Post
    intent: Record a new email message
    question: How do I add an email message record with a subject and body?
  - id: EmailMessages_GetById
    intent: Get one email message
    question: Is there a call to read a single email message by its ID?
  - id: EmailMessages_PutById
    intent: Replace an email message record
    question: What's the call to overwrite an email message record completely?
  - id: EmailMessages_DeleteById
    intent: Delete one email message
    question: How do I delete a single logged email message?
  - id: EmailMessages_PatchById
    intent: Update fields on an email message
    question: How do I change just the subject of an existing email message?
  - id: EmailMessages_Default
    intent: Get the default email message template
    question: What does a default, empty email message record contain?
  - id: EmailMessages_DeleteRoute
    intent: Bulk delete email messages
    question: Can I delete a batch of email messages at once?
  phrasing_ops: 12
  slug: optimizely-email-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Subscriber Email Lists API from Optimizely — 5 operation(s) for email subscriber email lists.
  name: Optimizely Email Subscriber Email Lists API
  phrasing_intents:
  - id: EmailSubscriberEmailLists_Get
    intent: List email subscriber list memberships
    question: Which email subscribers belong to which email lists in my commerce admin?
  - id: EmailSubscriberEmailLists_Post
    intent: Add an email subscriber to an email list
    question: How do I put an existing email subscriber onto an email list?
  - id: EmailSubscriberEmailLists_GetById
    intent: Get one subscriber list membership
    question: What subscriber and list does a given membership record connect?
  - id: EmailSubscriberEmailLists_PutById
    intent: Replace a subscriber list membership
    question: How do I overwrite a subscriber list membership record entirely?
  - id: EmailSubscriberEmailLists_DeleteById
    intent: Remove a subscriber from an email list
    question: How do I take a subscriber off an email list by deleting the membership?
  - id: EmailSubscriberEmailLists_PatchById
    intent: Move a subscriber membership to another list
    question: Can I change just the email list on an existing membership?
  - id: EmailSubscriberEmailLists_Default
    intent: Get the default membership template
    question: What default values does a new subscriber list membership start with?
  - id: EmailSubscriberEmailLists_DeleteRoute
    intent: Bulk remove subscriber list memberships
    question: How do I remove many subscribers from lists in one request?
  phrasing_ops: 9
  slug: optimizely-email-subscriber-email-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Subscribers API from Optimizely — 6 operation(s) for email subscribers.
  name: Optimizely Email Subscribers API
  phrasing_intents:
  - id: EmailSubscribers_Get
    intent: List email subscribers
    question: Who is subscribed to emails in Optimizely Commerce?
  - id: EmailSubscribers_Post
    intent: Add an email subscriber
    question: How do I add a new email address to the subscriber list?
  - id: EmailSubscribers_GetById
    intent: Get one email subscriber
    question: What is stored about a single email subscriber?
  - id: EmailSubscribers_PutById
    intent: Replace an email subscriber record
    question: Can I overwrite an email subscriber record entirely?
  - id: EmailSubscribers_DeleteById
    intent: Remove one email subscriber
    question: How do I delete a single email subscriber?
  - id: EmailSubscribers_PatchById
    intent: Change a subscriber's email address
    question: Can I correct a typo in a subscriber's email address?
  - id: EmailSubscribers_Default
    intent: Get default values for a new subscriber
    question: What defaults does a new email subscriber record start with?
  - id: EmailSubscribers_DeleteRoute
    intent: Bulk delete email subscribers
    question: Can I remove many email subscribers at once?
  phrasing_ops: 10
  slug: optimizely-email-subscribers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Email Templates API from Optimizely — 10 operation(s) for email templates.
  name: Optimizely Email Templates API
  phrasing_intents:
  - id: EmailTemplates_Get
    intent: List the email templates
    question: How can I see all the email templates set up in Commerce admin?
  - id: EmailTemplates_Post
    intent: Create a new email template
    question: What do I need to supply to add a new email template?
  - id: EmailTemplates_GetById
    intent: Get one email template by id
    question: How do I open a single email template record?
  - id: EmailTemplates_PutById
    intent: Replace an email template record
    question: Can I replace an entire email template record in one request?
  - id: EmailTemplates_DeleteById
    intent: Delete a single email template
    question: How do I delete one email template by id?
  - id: EmailTemplates_PatchById
    intent: Rename or edit part of an email template
    question: Can I just rename an email template without replacing it?
  - id: EmailTemplates_Default
    intent: Get default values for a new email template
    question: What values does a new email template record start with?
  - id: EmailTemplates_DefaultTemplates_1
    intent: List built-in default templates via OData action
    question: Which built-in default email templates ship with the platform, via the OData defaulttemplates function?
  phrasing_ops: 14
  slug: optimizely-email-templates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The EmailAttachments API from Optimizely — 1 operation(s) for emailattachments.
  name: Optimizely Email Attachments API
  phrasing_intents:
  - id: EmailAttachmentsV1_GetAsync
    intent: Download an email attachment
    question: How do I download a file that was attached to a storefront email?
  phrasing_ops: 1
  slug: optimizely-emailattachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity API from Optimizely — 3 operation(s) for entity.
  name: Optimizely Entity API
  phrasing_intents:
  - id: get_user_permissions_for_project_entity_type_users__user_id__projects__project_id___entity_type__get
    intent: List a user's permissions on a project entity type
    question: What permissions does a given user have on a type of entity in a project?
  - id: get_team_permissions_for_project_entity_type_teams__team_id__projects__project_id___entity_type__get
    intent: List a team's permissions on a project entity type
    question: Which permissions does a team hold on a type of entity in a project?
  - id: get_entity_permissions_projects__project_id___entity_type___entity_id__get
    intent: Get who has access to one project entity
    question: Who has access to a specific entity in my project?
  - id: change_permissions_projects__project_id___entity_type___entity_id__patch
    intent: Change access permissions on a project entity
    question: How do I change who can access a specific entity in a project?
  phrasing_ops: 4
  slug: optimizely-entity-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity Configurations API from Optimizely — 7 operation(s) for entity configurations.
  name: Optimizely Entity Configurations API
  phrasing_intents:
  - id: EntityConfigurations_Get
    intent: List admin entity configurations
    question: How do I list the entity configurations that shape the admin console?
  - id: EntityConfigurations_Post
    intent: Create an entity configuration
    question: How do I define a new entity configuration with a label and permissions?
  - id: EntityConfigurations_GetById
    intent: Get one entity configuration
    question: Is there a call to read a single entity configuration by ID?
  - id: EntityConfigurations_PutById
    intent: Replace an entity configuration
    question: What's the call to overwrite an entire entity configuration?
  - id: EntityConfigurations_DeleteById
    intent: Delete an entity configuration
    question: How do I remove an entity configuration by ID?
  - id: EntityConfigurations_PatchById
    intent: Update an entity configuration
    question: How do I change the instructional text shown for an entity?
  - id: EntityConfigurations_Default
    intent: Get the default entity configuration
    question: What does a default entity configuration look like?
  - id: EntityConfigurations_DeleteRoute
    intent: Bulk delete entity configurations
    question: Can I delete several entity configurations in one call?
  phrasing_ops: 11
  slug: optimizely-entity-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity Definitions API from Optimizely — 6 operation(s) for entity definitions.
  name: Optimizely Entity Definitions API
  phrasing_intents:
  - id: EntityDefinitions_Get
    intent: List admin entity definitions
    question: Which entity types does the commerce admin define, with their properties?
  - id: EntityDefinitions_GetByName
    intent: Get one entity definition by name
    question: What properties does a specific admin entity, like customerOrder, have?
  - id: EntityDefinitions_GetPropertyValidationsByEntityname_1
    intent: Get property validations via OData function
    question: Can I read an entity's field validation rules through the OData PropertyValidations function?
  - id: EntityDefinitions_GetDisplayNameFormats_1
    intent: Get display name formats via OData function
    question: How are entity display names formatted, via the OData DisplayNameFormats function?
  - id: EntityDefinitions_GetPropertyValidationsByEntityname_2
    intent: Get property validations via route
    question: Is there a plain route for an entity's property validation rules?
  - id: EntityDefinitions_GetDisplayNameFormats_2
    intent: Get display name formats via route
    question: Is there a simple displayNameFormats route for entity naming templates?
  phrasing_ops: 6
  slug: optimizely-entity-definitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Entity Permissions API from Optimizely — 5 operation(s) for entity permissions.
  name: Optimizely Entity Permissions API
  phrasing_intents:
  - id: EntityPermissions_Get
    intent: List entity permissions by role
    question: Which roles have view, edit, create or delete rights on admin entities?
  - id: EntityPermissions_Post
    intent: Grant a role permissions on an entity
    question: How do I give a role edit rights on an admin entity?
  - id: EntityPermissions_GetById
    intent: Get one entity permission
    question: How do I look up a single entity permission record?
  - id: EntityPermissions_PutById
    intent: Replace an entity permission
    question: Can I overwrite an entire entity permission record?
  - id: EntityPermissions_DeleteById
    intent: Revoke a single entity permission
    question: How do I remove one entity permission?
  - id: EntityPermissions_PatchById
    intent: Change specific rights on an entity permission
    question: Can I toggle just the edit right on an existing permission?
  - id: EntityPermissions_Default
    intent: Get default values for a new entity permission
    question: What rights does a new entity permission have by default?
  - id: EntityPermissions_DeleteRoute
    intent: Delete several entity permissions at once
    question: How do I bulk delete entity permissions?
  phrasing_ops: 9
  slug: optimizely-entity-permissions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Experiment Participants API from Optimizely — 7 operation(s) for experiment participants.
  name: Optimizely Experiment Participants API
  phrasing_intents:
  - id: ExperimentParticipants_Get
    intent: List experiment participants
    question: Which shoppers took part in my commerce page experiments?
  - id: ExperimentParticipants_Post
    intent: Record an experiment participant
    question: How do I log a new visitor as a participant in an experiment?
  - id: ExperimentParticipants_GetById
    intent: Get an experiment participant by id
    question: Can I look up one experiment participant record by id?
  - id: ExperimentParticipants_PutById
    intent: Replace an experiment participant record
    question: How do I overwrite all fields of a participant record at once?
  - id: ExperimentParticipants_DeleteById
    intent: Delete an experiment participant
    question: Can I remove a single participant from experiment data?
  - id: ExperimentParticipants_PatchById
    intent: Update fields on an experiment participant
    question: How do I mark an existing participant as having placed an order?
  - id: ExperimentParticipants_Default
    intent: Get a blank experiment participant template
    question: What default values does a new experiment participant record have?
  - id: ExperimentParticipants_StatisticsByExperimentid_1
    intent: Get experiment statistics via the OData function
    question: Can I get participant statistics for an experiment through the Default.statistics function?
  phrasing_ops: 11
  slug: optimizely-experiment-participants-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The ExperimentSummary API from Optimizely — 1 operation(s) for experimentsummary.
  name: Optimizely Experiment Summary API
  phrasing_intents:
  - id: get_experiment_summaries
    intent: Summarize a project's experiments and campaigns
    question: How do I get a quick summary of every experiment and campaign in an Optimizely project?
  phrasing_ops: 1
  slug: optimizely-experimentsummary-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get credentials to access experimentation events export data.
  name: Optimizely Export Credentials API
  phrasing_intents:
  - id: get_enriched_events_export_credentials
    intent: Get AWS credentials for events export
    question: How do I get temporary AWS credentials to read my experimentation events export?
  - id: get_gcp_e3_credentials
    intent: Get GCP token for events export
    question: Can I get a Google Cloud access token for experimentation events export data?
  phrasing_ops: 2
  slug: optimizely-export-credentials-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Exports API from Optimizely — 4 operation(s) for exports.
  name: Optimizely Exports API
  phrasing_intents:
  - id: export
    intent: Export objects and events data to S3
    question: How do I export my customer and event data out to Amazon S3?
  - id: export_1
    intent: Export segment members to S3
    question: How can I export the members of a segment to Amazon S3?
  - id: getExportJobStatus
    intent: Check a data export job's status
    question: Has my objects and events data export finished yet?
  - id: getSegmentExportJobStatus
    intent: Check a segment export job's status
    question: Is my segment member export done?
  phrasing_ops: 4
  slug: optimizely-exports-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Feederdata API from Optimizely — 6 operation(s) for feederdata.
  name: Optimizely Feederdata API
  phrasing_intents:
  - id: FeederData_GetRestrictionGroup
    intent: Find the restriction group with most products
    question: Which product restriction group covers the most products, for test data?
  - id: FeederData_GetCustomerWithMostShipTos
    intent: Find the customer with most ship-to addresses
    question: Which customer has the most ship-to addresses on file?
  - id: FeederData_GetWishlistWithMostProducts
    intent: Find the wish list with most products
    question: Which wish list holds the most products?
  - id: FeederData_GetProductWithMostWarehouses
    intent: Find the product stocked in most warehouses
    question: Which product is stocked across the most warehouses?
  - id: FeederData_GetQuickOrderUploadProducts
    intent: Get sample products for quick order upload
    question: Which products can I use to test a quick order bulk upload?
  - id: FeederData_GetBrandWithMostProducts
    intent: Find the brand with most products
    question: Which brand has the most products in the catalog?
  phrasing_ops: 6
  slug: optimizely-feederdata-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Fields API from Optimizely — 4 operation(s) for fields.
  name: Optimizely Fields API
  phrasing_intents:
  - id: listFields
    intent: List an organization's custom fields
    question: Which custom fields are defined in my Optimizely CMP organization?
  - id: createField
    intent: Add a new field to the organization
    question: How do I add a new custom field to my CMP organization?
  - id: updateField
    intent: Update an organization field
    question: How do I change an existing field's settings in CMP?
  - id: createFieldChoices
    intent: Add choices to a field
    question: How do I add dropdown options to a choice field?
  - id: updateFieldChoice
    intent: Update a field's choice
    question: How do I rename one option on a choice field?
  - id: deleteFieldChoice
    intent: Delete a choice from a field
    question: Can I remove a single option from a choice field?
  phrasing_ops: 6
  slug: optimizely-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Fields schema API from Optimizely — 2 operation(s) for fields schema.
  name: Optimizely Fields schema API
  phrasing_intents:
  - id: create-field
    intent: Create a field on a data platform object
    question: How do I add a new custom field, like ticket_id, to an object?
  - id: list-fields
    intent: List the fields on a data platform object
    question: What fields are defined on the customers object in Optimizely Data Platform?
  - id: get-field
    intent: Get one field on a data platform object
    question: Where can I see the type and description of a single field on an object?
  phrasing_ops: 3
  slug: optimizely-fields-schema-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage folders for mailings, message templates, custom blacklists, images, recipient list and attachment
  name: Optimizely Folders API
  phrasing_intents:
  - id: selectFolders
    intent: List campaign folders
    question: Which folders exist in my campaign client, with their parents and children?
  - id: createFolder
    intent: Create a campaign folder
    question: How do I create a folder to organize my mailings?
  - id: assign
    intent: Put an item into a folder
    question: Can I file a mailing or recipient list into a folder?
  - id: getFolder
    intent: Get details of one folder
    question: What are the name and creation date of a specific folder?
  - id: updateFolder
    intent: Rename or move a folder
    question: Can I rename a folder or move it to a different parent?
  - id: deleteFolder
    intent: Delete an empty folder
    question: Can I delete a folder that still has items in it?
  - id: unassign
    intent: Take an item out of a folder
    question: How do I remove a mailing from a folder without deleting it?
  phrasing_ops: 7
  slug: optimizely-folders-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Forms API from Optimizely — 2 operation(s) for forms.
  name: Optimizely Forms API
  phrasing_intents:
  - id: Forms_Get
    intent: List admin forms
    question: Which forms are defined in my Optimizely Configured Commerce admin?
  - id: Forms_GetByName
    intent: Get a form by name
    question: How do I fetch the definition of one form using its name?
  phrasing_ops: 2
  slug: optimizely-forms-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Gift Card Transactions API from Optimizely — 5 operation(s) for gift card transactions.
  name: Optimizely Gift Card Transactions API
  phrasing_intents:
  - id: GiftCardTransactions_Get
    intent: List gift card transactions
    question: How do I see all gift card transactions in the commerce admin?
  - id: GiftCardTransactions_Post
    intent: Record a gift card transaction
    question: How do I log a gift card being used on an order?
  - id: GiftCardTransactions_GetById
    intent: Get a gift card transaction
    question: How do I look up a single gift card transaction?
  - id: GiftCardTransactions_PutById
    intent: Replace a gift card transaction
    question: How do I overwrite a gift card transaction record in full?
  - id: GiftCardTransactions_DeleteById
    intent: Delete a gift card transaction
    question: How do I delete a single gift card transaction?
  - id: GiftCardTransactions_PatchById
    intent: Update a gift card transaction
    question: How do I correct the amount on a gift card transaction?
  - id: GiftCardTransactions_Default
    intent: Get a default gift card transaction template
    question: What default values does a new gift card transaction start with?
  - id: GiftCardTransactions_DeleteRoute
    intent: Bulk delete gift card transactions
    question: How do I delete several gift card transactions at once?
  phrasing_ops: 9
  slug: optimizely-gift-card-transactions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Gift Cards API from Optimizely — 9 operation(s) for gift cards.
  name: Optimizely Gift Cards API
  phrasing_intents:
  - id: GiftCards_Get
    intent: List gift cards
    question: Which gift cards have been issued in Optimizely Commerce?
  - id: GiftCards_Post
    intent: Issue a new gift card
    question: What details are required to issue a gift card to someone?
  - id: GiftCards_GetById
    intent: Get one gift card
    question: What is the balance and expiry of a specific gift card?
  - id: GiftCards_PutById
    intent: Replace a gift card record
    question: Can I overwrite a whole gift card record at once?
  - id: GiftCards_DeleteById
    intent: Delete one gift card
    question: How do I remove a single gift card record?
  - id: GiftCards_PatchById
    intent: Update part of a gift card
    question: Can I deactivate a gift card without deleting it?
  - id: GiftCards_Default
    intent: Get default values for a new gift card
    question: What defaults does a new gift card record start with?
  - id: GiftCards_Archive
    intent: Archive gift cards via the OData archive action
    question: Can I retire gift cards with the OData Default.archive action?
  phrasing_ops: 13
  slug: optimizely-gift-cards-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Global Synonyms API from Optimizely — 5 operation(s) for global synonyms.
  name: Optimizely Global Synonyms API
  phrasing_intents:
  - id: GlobalSynonyms_Get
    intent: List search synonyms
    question: How do I see all the global search synonyms configured in Optimizely Configured Commerce?
  - id: GlobalSynonyms_Post
    intent: Add a search synonym
    question: How can I make searches for one word also match another term?
  - id: GlobalSynonyms_GetById
    intent: Get one search synonym
    question: What does a particular synonym map its lookup term to?
  - id: GlobalSynonyms_PutById
    intent: Replace a search synonym
    question: Can I overwrite a synonym with a new lookup and mapped value?
  - id: GlobalSynonyms_DeleteById
    intent: Delete a search synonym
    question: How do I stop a synonym from affecting search by deleting it?
  - id: GlobalSynonyms_PatchById
    intent: Update a search synonym
    question: Can I change only the mapped term of an existing synonym?
  - id: GlobalSynonyms_Default
    intent: Get default values for a synonym
    question: What defaults are pre-filled for a new global synonym?
  - id: GlobalSynonyms_DeleteRoute
    intent: Delete several search synonyms
    question: Can I bulk delete a list of synonyms?
  phrasing_ops: 9
  slug: optimizely-global-synonyms-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with mutual exclusion groups
  name: Optimizely Groups API
  phrasing_intents:
  - id: list_groups
    intent: List a project's exclusion groups by environment
    question: Which exclusion groups exist in my Feature Experimentation project for a given environment?
  - id: update_groups
    intent: Patch several exclusion groups at once
    question: Can I update multiple exclusion groups in a project with one JSON patch request?
  - id: create_group
    intent: Create an exclusion group in an environment
    question: How do I create a mutually exclusive group of flag rules in one environment?
  - id: archive_groups
    intent: Archive exclusion groups
    question: How do I hide exclusion groups I no longer use without deleting them?
  - id: unarchive_groups
    intent: Restore archived exclusion groups
    question: How do I bring back exclusion groups I archived earlier?
  - id: delete_group
    intent: Permanently delete an exclusion group
    question: How do I permanently delete an exclusion group so its data is gone?
  - id: fetch_group
    intent: Fetch an exclusion group within a project
    question: What rules and settings does one exclusion group in my project have?
  - id: getGroups
    intent: List exclusion groups (Web Experimentation v2)
    question: Which exclusion groups exist in my Web Experimentation project?
  phrasing_ops: 12
  slug: optimizely-groups-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Holdouts API from Optimizely — 4 operation(s) for holdouts.
  name: Optimizely Holdouts API
  phrasing_intents:
  - id: list_holdouts
    intent: List holdouts in a project
    question: Which holdouts are currently running in my Optimizely project?
  - id: create_holdout
    intent: Create a holdout control group
    question: How do I reserve a slice of traffic as a baseline that sees no experiments?
  - id: delete_holdout
    intent: Permanently delete a holdout
    question: Can I recover a holdout's metric history after deleting it?
  - id: fetch_holdout
    intent: Get a holdout's configuration
    question: What traffic allocation and status does a specific holdout have?
  - id: update_holdouts
    intent: Update a holdout with JSON Patch
    question: How do I move a holdout from draft to running?
  - id: fetch_holdout_experiments
    intent: List experiments connected to a holdout
    question: Which experiments are affected by a particular holdout?
  - id: get_holdout_results_csv
    intent: Export holdout results as CSV
    question: How do I download a holdout's results as a spreadsheet?
  phrasing_ops: 7
  slug: optimizely-holdouts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Html Redirects API from Optimizely — 5 operation(s) for html redirects.
  name: Optimizely Html Redirects API
  phrasing_intents:
  - id: HtmlRedirects_Get
    intent: List URL redirects
    question: Which old URLs are currently redirected on my storefront?
  - id: HtmlRedirects_Post
    intent: Create a URL redirect
    question: How do I redirect an old page URL to a new one?
  - id: HtmlRedirects_GetById
    intent: Get one URL redirect
    question: How do I look up a single redirect rule by its ID?
  - id: HtmlRedirects_PutById
    intent: Replace a URL redirect
    question: How do I overwrite a redirect rule with both new source and target URLs?
  - id: HtmlRedirects_DeleteById
    intent: Delete a URL redirect
    question: How do I stop redirecting an old URL?
  - id: HtmlRedirects_PatchById
    intent: Change a redirect's target URL
    question: Can I point an existing redirect at a different destination?
  - id: HtmlRedirects_Default
    intent: Call the Default function on redirects
    question: What does the Default OData function on HTML redirects return?
  - id: HtmlRedirects_DeleteRoute
    intent: Bulk delete URL redirects
    question: Can I remove many redirect rules in one request after a site migration?
  phrasing_ops: 9
  slug: optimizely-html-redirects-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Identifiers API from Optimizely — 3 operation(s) for identifiers.
  name: Optimizely Identifiers API
  phrasing_intents:
  - id: create-identifier
    intent: Create a customer identifier for user resolution
    question: How do I add a new identifier type, like a loyalty number, to Optimizely Data Platform?
  - id: update-identifier-metadata
    intent: Update metadata for an identifier
    question: Can I update the metadata attached to a customer identifier value?
  - id: get-identifier-metadata
    intent: Get metadata for an identifier
    question: What metadata does ODP hold for a specific email address?
  phrasing_ops: 3
  slug: optimizely-identifiers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Impressions Usage API from Optimizely — 2 operation(s) for impressions usage.
  name: Optimizely Impressions Usage API
  phrasing_intents:
  - id: get_impressions_usage_request
    intent: Get impressions usage for a date range
    question: How many impressions has my account used between two dates?
  - id: get_impressions_usage_summary_request
    intent: Get an impressions usage summary
    question: What is my account's overall impressions usage summary?
  phrasing_ops: 2
  slug: optimizely-impressions-usage-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Connections API from Optimizely — 5 operation(s) for integration connections.
  name: Optimizely Integration Connections API
  phrasing_intents:
  - id: IntegrationConnections_Get
    intent: List integration connections
    question: Which integration connections are set up for my commerce integration jobs?
  - id: IntegrationConnections_Post
    intent: Create an integration connection
    question: How do I register a new connection that integration jobs can pull data through?
  - id: IntegrationConnections_GetById
    intent: Get one integration connection
    question: What settings does a particular integration connection use?
  - id: IntegrationConnections_PutById
    intent: Replace an integration connection
    question: Is there a way to overwrite every setting of an integration connection at once?
  - id: IntegrationConnections_DeleteById
    intent: Delete an integration connection
    question: How do I remove an integration connection that is no longer used?
  - id: IntegrationConnections_PatchById
    intent: Update settings of an integration connection
    question: Can I change just the password on an existing integration connection?
  - id: IntegrationConnections_Default
    intent: Call the Default function on integration connections
    question: What does the Default function on the integration connections entity set return?
  - id: IntegrationConnections_DeleteRoute
    intent: Bulk delete integration connections by ID
    question: Can I delete several integration connections in a single request?
  phrasing_ops: 9
  slug: optimizely-integration-connections-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Job Es Logs API from Optimizely — 2 operation(s) for integration job es logs.
  name: Optimizely Integration Job Es Logs API
  phrasing_intents:
  - id: IntegrationJobEsLogs_Get
    intent: List integration job log entries
    question: Where can I see the log output from integration jobs in Optimizely Commerce?
  - id: IntegrationJobEsLogs_GetById
    intent: Get one integration job log entry
    question: What does a single integration job log entry contain?
  phrasing_ops: 2
  slug: optimizely-integration-job-es-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Job Logs API from Optimizely — 5 operation(s) for integration job logs.
  name: Optimizely Integration Job Logs API
  phrasing_intents:
  - id: IntegrationJobLogs_Get
    intent: List integration job log entries
    question: How do I see the log messages written by integration jobs?
  - id: IntegrationJobLogs_Post
    intent: Write a log entry for an integration job
    question: How do I add a log message to an integration job run?
  - id: IntegrationJobLogs_GetById
    intent: Get one integration job log entry
    question: How do I read a single integration job log entry by id?
  - id: IntegrationJobLogs_PutById
    intent: Replace an integration job log entry
    question: How do I overwrite an integration job log entry completely?
  - id: IntegrationJobLogs_DeleteById
    intent: Delete an integration job log entry
    question: How do I delete one integration job log entry?
  - id: IntegrationJobLogs_PatchById
    intent: Update fields on an integration job log entry
    question: How do I correct just the message text on a job log entry?
  - id: IntegrationJobLogs_Default
    intent: Get the default integration job log record
    question: What does a default integration job log record contain?
  - id: IntegrationJobLogs_DeleteRoute
    intent: Bulk delete integration job logs
    question: How do I clear out many integration job log entries at once?
  phrasing_ops: 9
  slug: optimizely-integration-job-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Job Parameters API from Optimizely — 5 operation(s) for integration job parameters.
  name: Optimizely Integration Job Parameters API
  phrasing_intents:
  - id: IntegrationJobParameters_Get
    intent: List integration job parameters
    question: What parameter values were passed to our integration jobs?
  - id: IntegrationJobParameters_Post
    intent: Add a parameter value to an integration job
    question: How do I supply a parameter value for an integration job before it runs?
  - id: IntegrationJobParameters_GetById
    intent: Get an integration job parameter
    question: What value does a particular integration job parameter hold?
  - id: IntegrationJobParameters_PutById
    intent: Replace an integration job parameter
    question: Can I rewrite a job parameter record entirely, including which job it belongs to?
  - id: IntegrationJobParameters_DeleteById
    intent: Delete an integration job parameter
    question: How do I remove a parameter I set on an integration job by mistake?
  - id: IntegrationJobParameters_PatchById
    intent: Change the value of an integration job parameter
    question: Can I just change the value of one job parameter?
  - id: IntegrationJobParameters_Default
    intent: Call the integration job parameters Default function
    question: What does the Default function on integration job parameters return?
  - id: IntegrationJobParameters_DeleteRoute
    intent: Bulk delete integration job parameters
    question: Can I clear several integration job parameters in one request?
  phrasing_ops: 9
  slug: optimizely-integration-job-parameters-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Integration Jobs API from Optimizely — 7 operation(s) for integration jobs.
  name: Optimizely Integration Jobs API
  phrasing_intents:
  - id: IntegrationJobs_Get
    intent: List integration job runs
    question: How can I see recent integration job runs and their status?
  - id: IntegrationJobs_Post
    intent: Queue an integration job
    question: Can I kick off a new run of an existing job definition?
  - id: IntegrationJobs_GetById
    intent: Get an integration job run
    question: How many records did a specific integration job add, modify or delete?
  - id: IntegrationJobs_PutById
    intent: Replace an integration job record
    question: Can I overwrite a whole integration job record?
  - id: IntegrationJobs_DeleteById
    intent: Delete an integration job run
    question: How do I remove one integration job run from history?
  - id: IntegrationJobs_PatchById
    intent: Update an integration job's status
    question: Can I change only the status of an integration job run?
  - id: IntegrationJobs_Default
    intent: Get default values for an integration job
    question: What defaults are pre-filled for a new integration job?
  - id: IntegrationJobs_DeleteRoute
    intent: Delete several integration job runs
    question: Can I purge a batch of old integration job runs at once?
  phrasing_ops: 11
  slug: optimizely-integration-jobs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoice Histories API from Optimizely — 7 operation(s) for invoice histories.
  name: Optimizely Invoice Histories API
  phrasing_intents:
  - id: InvoiceHistories_Get
    intent: List historical invoices
    question: How do I pull invoice history synced from our ERP?
  - id: InvoiceHistories_Post
    intent: Add a historical invoice record
    question: How do I load an ERP invoice into the invoice history?
  - id: InvoiceHistories_GetById
    intent: Get one historical invoice
    question: How do I view the totals and current balance of one invoice?
  - id: InvoiceHistories_PutById
    intent: Replace a historical invoice record
    question: How do I overwrite an entire invoice history record?
  - id: InvoiceHistories_DeleteById
    intent: Delete a historical invoice
    question: How do I remove one invoice from invoice history?
  - id: InvoiceHistories_PatchById
    intent: Update fields on a historical invoice
    question: How do I mark a past invoice as closed?
  - id: InvoiceHistories_Default
    intent: Get a blank invoice history template
    question: What default values does a new invoice history record start with?
  - id: InvoiceHistories_DeleteRoute
    intent: Bulk delete historical invoices
    question: How do I delete several past invoices at once?
  phrasing_ops: 11
  slug: optimizely-invoice-histories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoice History Lines API from Optimizely — 5 operation(s) for invoice history lines.
  name: Optimizely Invoice History Lines API
  phrasing_intents:
  - id: InvoiceHistoryLines_Get
    intent: List invoice history lines
    question: Where can I see the individual line items from past invoices?
  - id: InvoiceHistoryLines_Post
    intent: Add a line to an invoice history
    question: How do I load a line item from my ERP into an invoice history record?
  - id: InvoiceHistoryLines_GetById
    intent: Get an invoice history line
    question: Can I open one invoice line to see its tax and discount amounts?
  - id: InvoiceHistoryLines_PutById
    intent: Replace an invoice history line
    question: Is there a way to overwrite an entire invoice line from the ERP?
  - id: InvoiceHistoryLines_DeleteById
    intent: Delete an invoice history line
    question: Can I remove one line from an invoice history by id?
  - id: InvoiceHistoryLines_PatchById
    intent: Update fields on an invoice line
    question: How do I correct just the quantity invoiced on one line?
  - id: InvoiceHistoryLines_Default
    intent: Get a blank invoice line template
    question: What default values does a new invoice history line start with?
  - id: InvoiceHistoryLines_DeleteRoute
    intent: Bulk delete invoice history lines
    question: Can I delete many invoice lines in one request?
  phrasing_ops: 9
  slug: optimizely-invoice-history-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoice History Taxes API from Optimizely — 5 operation(s) for invoice history taxes.
  name: Optimizely Invoice History Taxes API
  phrasing_intents:
  - id: InvoiceHistoryTaxes_Get
    intent: List invoice tax lines
    question: What tax lines are recorded against historical invoices in Optimizely Configured Commerce?
  - id: InvoiceHistoryTaxes_Post
    intent: Add a tax line to an invoice
    question: How do I record a tax line with its code, rate and amount on an invoice?
  - id: InvoiceHistoryTaxes_GetById
    intent: Get an invoice tax line
    question: What rate and amount were charged on a specific invoice tax line?
  - id: InvoiceHistoryTaxes_PutById
    intent: Replace an invoice tax line
    question: How do I overwrite an entire invoice tax line record?
  - id: InvoiceHistoryTaxes_DeleteById
    intent: Delete an invoice tax line
    question: How do I remove a tax line recorded on an invoice?
  - id: InvoiceHistoryTaxes_PatchById
    intent: Correct an invoice tax line
    question: How do I fix the tax amount on an existing invoice tax line?
  - id: InvoiceHistoryTaxes_Default
    intent: Get a blank default invoice tax line
    question: What does an empty invoice tax line object look like?
  - id: InvoiceHistoryTaxes_DeleteRoute
    intent: Delete several invoice tax lines
    question: Can I delete many invoice tax lines at once?
  phrasing_ops: 9
  slug: optimizely-invoice-history-taxes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Invoices API from Optimizely — 3 operation(s) for invoices.
  name: Optimizely Invoices API
  phrasing_intents:
  - id: InvoicesV1_GetCollectionAsync
    intent: Search a customer's invoices
    question: Which of my invoices are still open?
  - id: InvoicesV1_GetAsync
    intent: Get one invoice
    question: What are the line items and totals on a specific invoice?
  - id: InvoicesV1_Post
    intent: Email an invoice to someone
    question: How do I share an invoice by email with a colleague?
  phrasing_ops: 3
  slug: optimizely-invoices-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Parameters API from Optimizely — 5 operation(s) for job definition parameters.
  name: Optimizely Job Definition Parameters API
  phrasing_intents:
  - id: JobDefinitionParameters_Get
    intent: List job definition parameters
    question: Which parameters are defined for my integration job definitions?
  - id: JobDefinitionParameters_Post
    intent: Add a parameter to a job definition
    question: How do I add an input parameter to an integration job definition?
  - id: JobDefinitionParameters_GetById
    intent: Get a job definition parameter
    question: What default value and prompt does a given job parameter have?
  - id: JobDefinitionParameters_PutById
    intent: Replace a job definition parameter
    question: How do I overwrite a job parameter's whole definition?
  - id: JobDefinitionParameters_DeleteById
    intent: Delete one job definition parameter
    question: How do I remove a parameter from a job definition?
  - id: JobDefinitionParameters_PatchById
    intent: Change a job parameter's default or order
    question: Can I change only the default value of a job parameter?
  - id: JobDefinitionParameters_Default
    intent: Get default values for a new job parameter
    question: What defaults does a new job definition parameter start with?
  - id: JobDefinitionParameters_DeleteRoute
    intent: Bulk delete job definition parameters
    question: Can I remove many job parameters in one call?
  phrasing_ops: 9
  slug: optimizely-job-definition-parameters-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Step Field Maps API from Optimizely — 5 operation(s) for job definition step field maps.
  name: Optimizely Job Definition Step Field Maps API
  phrasing_intents:
  - id: JobDefinitionStepFieldMaps_Get
    intent: List integration job field mappings
    question: Which field mappings are defined on integration job steps in Optimizely Commerce?
  - id: JobDefinitionStepFieldMaps_Post
    intent: Map a source field to a target in a job step
    question: How do I map an ERP column to a Commerce property in an integration job step?
  - id: JobDefinitionStepFieldMaps_GetById
    intent: Get one job step field mapping
    question: What source and target properties does a given field map connect?
  - id: JobDefinitionStepFieldMaps_PutById
    intent: Replace a job step field mapping
    question: Can I overwrite an entire field mapping definition?
  - id: JobDefinitionStepFieldMaps_DeleteById
    intent: Delete one job step field mapping
    question: How do I drop a single field mapping from a job step?
  - id: JobDefinitionStepFieldMaps_PatchById
    intent: Tweak a job step field mapping
    question: Can I mark an existing field map as the ERP key?
  - id: JobDefinitionStepFieldMaps_Default
    intent: Get default values for a field mapping
    question: What defaults does a new job step field map start with?
  - id: JobDefinitionStepFieldMaps_DeleteRoute
    intent: Bulk delete job step field mappings
    question: Can I remove many field mappings in one request?
  phrasing_ops: 9
  slug: optimizely-job-definition-step-field-maps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Step Parameters API from Optimizely — 5 operation(s) for job definition step parameters.
  name: Optimizely Job Definition Step Parameters API
  phrasing_intents:
  - id: JobDefinitionStepParameters_Get
    intent: List integration job step parameters
    question: Which parameters are defined on my integration job steps in Optimizely Configured Commerce?
  - id: JobDefinitionStepParameters_Post
    intent: Add a parameter to a job definition step
    question: How do I add a prompted parameter with a default value to an integration job step?
  - id: JobDefinitionStepParameters_GetById
    intent: Get one job step parameter
    question: How do I look up a single job step parameter's default value by ID?
  - id: JobDefinitionStepParameters_PutById
    intent: Replace a job step parameter
    question: Can I overwrite a job step parameter with a complete new definition?
  - id: JobDefinitionStepParameters_DeleteById
    intent: Delete a job step parameter
    question: How do I remove one parameter from an integration job step?
  - id: JobDefinitionStepParameters_PatchById
    intent: Update a job step parameter
    question: Can I change just the default value of a job step parameter?
  - id: JobDefinitionStepParameters_Default
    intent: Get default values for a job step parameter
    question: What defaults does the admin pre-fill for a new job step parameter?
  - id: JobDefinitionStepParameters_DeleteRoute
    intent: Bulk delete job step parameters
    question: How do I delete several job step parameters in one request?
  phrasing_ops: 9
  slug: optimizely-job-definition-step-parameters-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definition Steps API from Optimizely — 7 operation(s) for job definition steps.
  name: Optimizely Job Definition Steps API
  phrasing_intents:
  - id: JobDefinitionSteps_Get
    intent: List integration job steps
    question: Which steps make up my integration job definitions?
  - id: JobDefinitionSteps_Post
    intent: Add a step to an integration job
    question: How do I add a new step to an integration job definition?
  - id: JobDefinitionSteps_GetById
    intent: Get an integration job step
    question: How do I see the query and delete action configured on one job step?
  - id: JobDefinitionSteps_PutById
    intent: Replace an integration job step
    question: How do I overwrite a whole job definition step in one call?
  - id: JobDefinitionSteps_DeleteById
    intent: Delete an integration job step
    question: How do I remove one step from an integration job?
  - id: JobDefinitionSteps_PatchById
    intent: Update an integration job step
    question: How do I change the sequence of a job step?
  - id: JobDefinitionSteps_Default
    intent: Get the default job step template
    question: What default values does a new job definition step start with?
  - id: JobDefinitionSteps_DeleteRoute
    intent: Bulk delete job steps
    question: How do I delete several job definition steps at once?
  phrasing_ops: 11
  slug: optimizely-job-definition-steps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Job Definitions API from Optimizely — 8 operation(s) for job definitions.
  name: Optimizely Job Definitions API
  phrasing_intents:
  - id: JobDefinitions_Get
    intent: List integration job definitions
    question: How can I see every integration job definition configured in Configured Commerce?
  - id: JobDefinitions_Post
    intent: Create an integration job definition
    question: What must I supply to define a new import or export job?
  - id: JobDefinitions_GetById
    intent: Get a job definition
    question: Can I see the schedule and processors of one job definition?
  - id: JobDefinitions_PutById
    intent: Replace a job definition
    question: Can I overwrite an entire job definition with a new configuration?
  - id: JobDefinitions_DeleteById
    intent: Delete a job definition
    question: How do I remove an integration job definition I no longer use?
  - id: JobDefinitions_PatchById
    intent: Update a job definition's settings
    question: Can I change only the notification email on a job definition?
  - id: JobDefinitions_Default
    intent: Get default values for a job definition
    question: What defaults are pre-filled for a new job definition?
  - id: JobDefinitions_DeleteRoute
    intent: Delete several job definitions
    question: Can I bulk delete job definitions in a single request?
  phrasing_ops: 12
  slug: optimizely-job-definitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Jobquotes API from Optimizely — 2 operation(s) for jobquotes.
  name: Optimizely Jobquotes API
  phrasing_intents:
  - id: JobQuotesV1_GetCollectionAsync
    intent: List job quotes
    question: Which job quotes are available to my account?
  - id: JobQuotesV1_GetAsync
    intent: Get a job quote
    question: Can I see the lines, total and expiration date of a specific job quote?
  - id: JobQuotesV1_PatchAsync
    intent: Update a job quote
    question: How do I change the job name or notes on a job quote?
  phrasing_ops: 3
  slug: optimizely-jobquotes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Languages API from Optimizely — 6 operation(s) for languages.
  name: Optimizely Languages API
  phrasing_intents:
  - id: Languages_Get
    intent: List storefront languages
    question: Which languages are set up in the Optimizely Configured Commerce admin?
  - id: Languages_Post
    intent: Add a language
    question: What codes and tags do I need to add a new language to the storefront?
  - id: Languages_GetById
    intent: Get one language by ID
    question: How do I look up a single language's culture code by its ID?
  - id: Languages_PutById
    intent: Replace a language record entirely
    question: Can I overwrite a language with a complete new set of values?
  - id: Languages_DeleteById
    intent: Delete a single language
    question: How do I remove one language from the storefront by its ID?
  - id: Languages_PatchById
    intent: Update selected fields on a language
    question: Can I change just where the currency symbol is positioned for a language?
  - id: Languages_Default
    intent: Get default values for a new language
    question: What defaults does the admin pre-fill for a language before I add one?
  - id: Languages_DeleteRoute
    intent: Bulk delete languages by ID
    question: How do I delete several languages in one request?
  phrasing_ops: 10
  slug: optimizely-languages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Library API from Optimizely — 24 operation(s) for library.
  name: Optimizely Library API
  phrasing_intents:
  - id: listFolders
    intent: List library folders
    question: How do I see all the folders in my content marketing library?
  - id: createFolder
    intent: Create a library folder
    question: How do I make a new folder in the Optimizely content library?
  - id: getFolder
    intent: Get a library folder
    question: What are the details of a single library folder by its ID?
  - id: updateFolder
    intent: Rename or move a library folder
    question: How do I rename an existing library folder?
  - id: deleteFolder
    intent: Delete a library folder
    question: How do I remove a folder from my library?
  - id: listFolderPermissions
    intent: List who can access a folder
    question: Who has access to a particular library folder?
  - id: addFolderPermissions
    intent: Grant folder access to users or teams
    question: How do I share a library folder with a team?
  - id: updateFolderPermission
    intent: Change someone's access level on a folder
    question: How do I change a user's access level on a library folder?
  phrasing_ops: 41
  slug: optimizely-library-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: 'A List Attribute is a set of user identifiers that you have uploaded to Optimizely. Membership in a list can be used to define an Optimizely audience, so you can target experiments and campaigns only '
  name: Optimizely List Attributes API
  phrasing_intents:
  - id: list_list_attributes
    intent: List a project's list attributes
    question: Which uploaded targeting lists exist in my project?
  - id: create_list_attribute
    intent: Create a list attribute for audience targeting
    question: How do I upload a list of user IDs or ZIP codes to target an audience?
  - id: archive_list_attribute
    intent: Archive a list attribute
    question: How do I retire a targeting list I no longer use?
  - id: get_list_attribute
    intent: Get a list attribute's metadata
    question: What key field and list type does a particular List Attribute use?
  - id: update_list_attribute
    intent: Update a list attribute
    question: Can I replace the IDs inside an existing targeting list?
  phrasing_ops: 5
  slug: optimizely-list-attributes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Lists API from Optimizely — 2 operation(s) for lists.
  name: Optimizely Lists API
  phrasing_intents:
  - id: get-subscription-status
    intent: Check list subscription status for a customer
    question: Is a customer subscribed to my Optimizely Data Platform lists?
  - id: subscribeunsubscribe
    intent: Subscribe or unsubscribe a customer from a list
    question: How do I add a customer to an ODP list or take them off it?
  - id: get-lists
    intent: List all ODP lists
    question: What lists exist in my Optimizely Data Platform account?
  - id: create-list
    intent: Create an ODP list
    question: How do I create a new marketing list in ODP?
  phrasing_ops: 4
  slug: optimizely-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Local Tax Rate Tax Exemptions API from Optimizely — 5 operation(s) for local tax rate tax exemptions.
  name: Optimizely Local Tax Rate Tax Exemptions API
  phrasing_intents:
  - id: LocalTaxRateTaxExemptions_Get
    intent: List tax exemptions on local tax rates
    question: How do I see which tax exemptions are linked to which local tax rates?
  - id: LocalTaxRateTaxExemptions_Post
    intent: Link a tax exemption to a local tax rate
    question: Can I attach a tax exemption to a specific postal-code tax rate?
  - id: LocalTaxRateTaxExemptions_GetById
    intent: Get one tax rate exemption link
    question: Where do I look up a single tax rate exemption link by id?
  - id: LocalTaxRateTaxExemptions_PutById
    intent: Replace a tax rate exemption link
    question: How do I overwrite a tax rate exemption link with new ids?
  - id: LocalTaxRateTaxExemptions_DeleteById
    intent: Unlink a tax exemption from a local rate
    question: Can I detach an exemption from a local tax rate?
  - id: LocalTaxRateTaxExemptions_PatchById
    intent: Update a tax rate exemption link
    question: Can I switch an existing link to a different tax exemption?
  - id: LocalTaxRateTaxExemptions_Default
    intent: Call the Default function on tax rate exemptions
    question: What does the Default function on LocalTaxRateTaxExemptions return?
  - id: LocalTaxRateTaxExemptions_DeleteRoute
    intent: Bulk remove tax rate exemption links
    question: Can I remove many exemption-to-rate links at once by id?
  phrasing_ops: 9
  slug: optimizely-local-tax-rate-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Local Tax Rates API from Optimizely — 6 operation(s) for local tax rates.
  name: Optimizely Local Tax Rates API
  phrasing_intents:
  - id: LocalTaxRates_Get
    intent: List local tax rates
    question: How do I see every local tax rate configured by postal code?
  - id: LocalTaxRates_Post
    intent: Add a local tax rate for a postal code
    question: What do I need to add a new sales tax rate for a postal code?
  - id: LocalTaxRates_GetById
    intent: Get one local tax rate
    question: Where do I look up a single local tax rate by its id?
  - id: LocalTaxRates_PutById
    intent: Replace a local tax rate record
    question: How do I overwrite a local tax rate record with a complete new version?
  - id: LocalTaxRates_DeleteById
    intent: Delete a local tax rate
    question: Can I remove one local tax rate that no longer applies?
  - id: LocalTaxRates_PatchById
    intent: Change fields on a local tax rate
    question: Can I change just the percentage on an existing local tax rate?
  - id: LocalTaxRates_Default
    intent: Call the Default function on local tax rates
    question: What does the Default function on the LocalTaxRates set return?
  - id: LocalTaxRates_DeleteRoute
    intent: Bulk delete local tax rates
    question: Can I delete many local tax rates at once by listing their ids?
  phrasing_ops: 10
  slug: optimizely-local-tax-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📜 Logs API from Optimizely — 1 operation(s) for 📜 logs.
  name: Optimizely 📜 Logs API
  phrasing_intents:
  - id: get-RequestLogHandler
    intent: View Graph request logs
    question: Where can I see the incoming and outgoing requests Optimizely Graph logged?
  phrasing_ops: 1
  slug: optimizely-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Lookup API from Optimizely — 1 operation(s) for lookup.
  name: Optimizely Lookup API
  phrasing_intents:
  - id: lookup
    intent: Look up a user's saved profile
    question: How do I retrieve the saved user profile Optimizely Agent keeps for a user?
  phrasing_ops: 1
  slug: optimizely-lookup-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get archived mailings
  name: Optimizely Mail archive API
  phrasing_intents:
  - id: getArchivedMailMetaData
    intent: Get details of one archived mailing
    question: How do I see metadata for a single archived email sent to a recipient?
  - id: selectArchiveMails
    intent: Search archived mailings
    question: Which emails were archived for a given recipient address?
  - id: getArchivedMailContent
    intent: Download an archived mailing's content
    question: How do I retrieve the actual content of an archived email?
  - id: selectArchivedMailContents
    intent: Bulk download archived mailing contents
    question: How do I export the contents of many archived emails at once?
  phrasing_ops: 4
  slug: optimizely-mail-archive-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get information about a mail ID
  name: Optimizely Mail ID API
  phrasing_intents:
  - id: getDetailedMailIdInformationByEncodedId
    intent: Decode a full mail ID
    question: Which mailing, recipient list and recipient does a mail ID stand for?
  - id: getDetailedMailIdInformationByEncodedPlainId
    intent: Decode a plain mail ID to its mailing
    question: What mailing does a plain mail ID, one without recipient data, refer to?
  - id: retrieveBmMailId
    intent: Generate a mail ID for a mailing recipient
    question: How do I get the mail ID for a particular mailing-to-user record?
  phrasing_ops: 3
  slug: optimizely-mail-id-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Message Audits API from Optimizely — 5 operation(s) for message audits.
  name: Optimizely Message Audits API
  phrasing_intents:
  - id: MessageAudits_Get
    intent: List message audit entries
    question: How do I review the audit trail of messages sent between users?
  - id: MessageAudits_Post
    intent: Record a message audit entry
    question: How do I log a message audit entry for an order?
  - id: MessageAudits_GetById
    intent: Get one message audit entry
    question: Is there a call to read a single message audit record?
  - id: MessageAudits_PutById
    intent: Replace a message audit entry
    question: What's the call to overwrite a message audit record entirely?
  - id: MessageAudits_DeleteById
    intent: Delete a message audit entry
    question: How do I remove a single message audit record?
  - id: MessageAudits_PatchById
    intent: Update a message audit entry
    question: How do I correct the recipient on a message audit record?
  - id: MessageAudits_Default
    intent: Get the default message audit template
    question: What does a default message audit record look like?
  - id: MessageAudits_DeleteRoute
    intent: Bulk delete message audit entries
    question: Is it possible to purge many message audit records at once?
  phrasing_ops: 9
  slug: optimizely-message-audits-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Message Statuses API from Optimizely — 5 operation(s) for message statuses.
  name: Optimizely Message Statuses API
  phrasing_intents:
  - id: MessageStatuses_Get
    intent: List message read statuses
    question: Which users have read the site messages I posted?
  - id: MessageStatuses_Post
    intent: Record a message status for a user
    question: How do I track whether a user has read a specific message?
  - id: MessageStatuses_GetById
    intent: Get a message status by id
    question: Has a given message status been marked as read?
  - id: MessageStatuses_PutById
    intent: Replace a message status
    question: How do I overwrite an entire message status record?
  - id: MessageStatuses_DeleteById
    intent: Delete a message status
    question: Can I remove a single message status by its id?
  - id: MessageStatuses_PatchById
    intent: Mark a message as read or unread
    question: How do I flip one message status to read without resending the rest?
  - id: MessageStatuses_Default
    intent: Get a blank message status template
    question: What default values does a new message status start with?
  - id: MessageStatuses_DeleteRoute
    intent: Bulk delete message statuses
    question: Can I delete several message statuses in one request?
  phrasing_ops: 9
  slug: optimizely-message-statuses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Message Targets API from Optimizely — 5 operation(s) for message targets.
  name: Optimizely Message Targets API
  phrasing_intents:
  - id: MessageTargets_Get
    intent: List message targets
    question: Who are site messages targeted at, across all messages?
  - id: MessageTargets_Post
    intent: Target a message at an audience
    question: How do I aim a storefront message at a specific customer or role?
  - id: MessageTargets_GetById
    intent: Get a message target
    question: Can I look up one message target by ID?
  - id: MessageTargets_PutById
    intent: Replace a message target
    question: Can I overwrite a message target with a new audience?
  - id: MessageTargets_DeleteById
    intent: Delete a message target
    question: How do I stop a message going to one audience?
  - id: MessageTargets_PatchById
    intent: Update a message target
    question: Can I change only the target key on a message target?
  - id: MessageTargets_Default
    intent: Get default values for a message target
    question: What defaults are pre-filled for a new message target?
  - id: MessageTargets_DeleteRoute
    intent: Delete several message targets
    question: Can I bulk delete message targets in one request?
  phrasing_ops: 9
  slug: optimizely-message-targets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage message templates
  name: Optimizely Message templates API
  phrasing_intents:
  - id: selectMessageTemplates
    intent: List message templates for a client
    question: Which email message templates exist in my Optimizely Campaign client?
  - id: createOrCopyMessageTemplate
    intent: Create or copy a message template
    question: How do I create a new email message template from a CMS content template or a mailing?
  - id: getMessageTemplate
    intent: Get details of one message template
    question: What reply-to address and subject does a specific message template use?
  - id: updateMessageTemplate
    intent: Update an existing message template
    question: How do I rename an existing message template or change its subject?
  - id: deleteMessageTemplate
    intent: Delete a message template
    question: Can I permanently delete a message template I no longer need?
  - id: testMessageTemplate
    intent: Send a test mailing of a message template
    question: How do I send a test email to check a template's content and layout before the real send?
  phrasing_ops: 6
  slug: optimizely-message-templates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Messages API from Optimizely — 11 operation(s) for messages.
  name: Optimizely Messages API
  phrasing_intents:
  - id: Messages_Get
    intent: List site messages in the admin console
    question: Which admin-managed site messages are currently set up in Optimizely Commerce?
  - id: Messages_Post
    intent: Create a site message as an admin
    question: How do I publish a new site message with a subject and body from the admin API?
  - id: Messages_GetById
    intent: Get one admin site message
    question: What does a single admin site message record contain?
  - id: Messages_PutById
    intent: Replace an admin site message
    question: Can I overwrite an entire admin message record in one call?
  - id: Messages_DeleteById
    intent: Delete one admin site message
    question: How do I remove a single admin site message?
  - id: Messages_PatchById
    intent: Edit part of an admin site message
    question: Can I push back the hide date on an existing admin message?
  - id: Messages_Default
    intent: Get default values for a new site message
    question: What defaults does a blank admin message start with?
  - id: Messages_DeleteRoute
    intent: Bulk delete admin site messages
    question: Can I remove several admin site messages in one request?
  phrasing_ops: 17
  slug: optimizely-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Milestones API from Optimizely — 2 operation(s) for milestones.
  name: Optimizely Milestones API
  phrasing_intents:
  - id: listMilestones
    intent: List campaign milestones
    question: Which milestones are coming due in my Optimizely campaign?
  - id: createMilestone
    intent: Create a campaign milestone
    question: How do I add a milestone with a due date and colored label to a campaign?
  - id: getMilestone
    intent: Get a milestone
    question: What's the due date and task list on a particular milestone?
  - id: updateMilestone
    intent: Update a milestone
    question: Can I push back a milestone's due date without changing anything else?
  phrasing_ops: 4
  slug: optimizely-milestones-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Mobilecontent API from Optimizely — 1 operation(s) for mobilecontent.
  name: Optimizely Mobilecontent API
  phrasing_intents:
  - id: MobileAppV1_GetMobileContentAsync
    intent: Get mobile app content for a page
    question: How does the mobile app fetch the content of a named page?
  phrasing_ops: 1
  slug: optimizely-mobilecontent-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Mobius Themes API from Optimizely — 5 operation(s) for mobius themes.
  name: Optimizely Mobius Themes API
  phrasing_intents:
  - id: MobiusThemes_Get
    intent: List Mobius storefront themes
    question: How do I list the Mobius themes configured across my commerce websites?
  - id: MobiusThemes_Post
    intent: Create a Mobius theme for a website
    question: How do I save a new Mobius theme for one of my websites?
  - id: MobiusThemes_GetById
    intent: Get one Mobius theme
    question: How do I read the theme value saved for a specific Mobius theme?
  - id: MobiusThemes_PutById
    intent: Replace a Mobius theme
    question: How do I overwrite an entire Mobius theme record?
  - id: MobiusThemes_DeleteById
    intent: Delete a Mobius theme
    question: How do I remove a Mobius theme from a website?
  - id: MobiusThemes_PatchById
    intent: Update a Mobius theme's value
    question: How do I tweak the saved value of an existing Mobius theme?
  - id: MobiusThemes_Default
    intent: Get a blank Mobius theme template
    question: What default values does a new Mobius theme start with?
  - id: MobiusThemes_DeleteRoute
    intent: Bulk delete Mobius themes
    question: How do I delete several Mobius themes at once?
  phrasing_ops: 9
  slug: optimizely-mobius-themes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Nodes API from Optimizely — 6 operation(s) for nodes.
  name: Optimizely Nodes API
  phrasing_intents:
  - id: Nodes_Get
    intent: List content tree nodes
    question: How do I list the content tree nodes for my commerce site?
  - id: Nodes_Post
    intent: Create a content node
    question: How do I add a new node to a website's content tree?
  - id: Nodes_GetById
    intent: Get one content node
    question: Is there a call to read a single content node by ID?
  - id: Nodes_PutById
    intent: Replace a content node
    question: What's the call to overwrite a content node record in full?
  - id: Nodes_DeleteById
    intent: Delete a content node
    question: How do I remove a node from the content tree?
  - id: Nodes_PatchById
    intent: Move or reorder a content node
    question: How do I move a node under a different parent?
  - id: Nodes_Default
    intent: Get the default node template
    question: What does a default content node record look like?
  - id: Nodes_DeleteRoute
    intent: Bulk delete content nodes
    question: Can I delete several content nodes at once?
  phrasing_ops: 10
  slug: optimizely-nodes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Object schema API from Optimizely — 2 operation(s) for object schema.
  name: Optimizely Object schema API
  phrasing_intents:
  - id: create-object
    intent: Create a custom data object
    question: How do I add a custom object like tickets to my data schema?
  - id: list-objects
    intent: List data platform objects
    question: Which objects exist in my Optimizely Data Platform account?
  - id: get-object
    intent: Get one data object's schema
    question: How can I see the fields and relations of one specific object?
  phrasing_ops: 3
  slug: optimizely-object-schema-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Odpimport API from Optimizely — 1 operation(s) for odpimport.
  name: Optimizely Odpimport API
  phrasing_intents:
  - id: ImportPersona_Personas
    intent: Import an ODP segment as personas
    question: Can I bring a Data Platform segment into Commerce as a persona?
  phrasing_ops: 1
  slug: optimizely-odpimport-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 🔒 OIDC API from Optimizely — 1 operation(s) for 🔒 oidc.
  name: Optimizely 🔒 OIDC API
  phrasing_intents:
  - id: upsert-OidcConfigHandler
    intent: Enable or update OIDC config for Graph
    question: How do I turn on OIDC authentication for my Optimizely Graph account?
  - id: delete-OidcConfigHandler
    intent: Delete the OIDC config
    question: Can I turn off OIDC support for my Graph account?
  phrasing_ops: 2
  slug: optimizely-oidc-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: View, update and create opt-in processes
  name: Optimizely Opt-in processes API
  phrasing_intents:
  - id: selectOptinProcesses
    intent: List opt-in processes
    question: Which double opt-in processes are set up for my Optimizely Campaign client?
  - id: createOptinProcess
    intent: Create an opt-in process
    question: How do I set up a new opt-in process for newsletter sign-ups?
  - id: getOptinProcess
    intent: Get one opt-in process
    question: How do I see the type and creation date of a specific opt-in process?
  - id: updateOptinProcess
    intent: Update an opt-in process
    question: Can I rename an existing opt-in process or change its description?
  phrasing_ops: 4
  slug: optimizely-opt-in-processes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Optimizely Edge Decider API from Optimizely — 1 operation(s) for optimizely edge decider.
  name: Optimizely Edge Decider API
  phrasing_intents:
  - id: getByAccountIdByProjectId
    intent: Fetch an Edge experiment microsnippet for a page
    question: How do I get the JavaScript microsnippet that applies Performance Edge experiment variations to a page?
  phrasing_ops: 1
  slug: optimizely-optimizely-edge-decider-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Histories API from Optimizely — 8 operation(s) for order histories.
  name: Optimizely Order Histories API
  phrasing_intents:
  - id: OrderHistories_Get
    intent: List historical orders
    question: How do I pull the order history synced from our ERP into the commerce admin?
  - id: OrderHistories_Post
    intent: Add a historical order record
    question: How do I load an order from our ERP into the order history?
  - id: OrderHistories_GetById
    intent: Get one historical order
    question: How do I see the totals and addresses on one past order?
  - id: OrderHistories_PutById
    intent: Replace a historical order record
    question: How do I overwrite a whole order history record with fresh ERP data?
  - id: OrderHistories_DeleteById
    intent: Delete a historical order
    question: How do I remove one order from the order history?
  - id: OrderHistories_PatchById
    intent: Update fields on a historical order
    question: How do I change the status of a past order in order history?
  - id: OrderHistories_Default
    intent: Get a blank order history template
    question: What default values does a new order history record start with?
  - id: OrderHistories_DeleteRoute
    intent: Bulk delete historical orders
    question: How do I delete several past orders at once?
  phrasing_ops: 12
  slug: optimizely-order-histories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order History Lines API from Optimizely — 5 operation(s) for order history lines.
  name: Optimizely Order History Lines API
  phrasing_intents:
  - id: OrderHistoryLines_Get
    intent: List order history lines
    question: What line items are recorded in past orders from the ERP?
  - id: OrderHistoryLines_Post
    intent: Add a line to an order history record
    question: How do I add a line item to a historical order imported from the ERP?
  - id: OrderHistoryLines_GetById
    intent: Get an order history line
    question: How do I see the quantities and pricing on one historical order line?
  - id: OrderHistoryLines_PutById
    intent: Replace an order history line
    question: How do I overwrite an entire historical order line from the ERP?
  - id: OrderHistoryLines_DeleteById
    intent: Delete an order history line
    question: How do I remove a line from a historical order?
  - id: OrderHistoryLines_PatchById
    intent: Update an order history line
    question: How do I update the shipped quantity on a past order line?
  - id: OrderHistoryLines_Default
    intent: Get the default order history line template
    question: What default values does a new order history line start with?
  - id: OrderHistoryLines_DeleteRoute
    intent: Bulk delete order history lines
    question: How do I delete many order history lines at once?
  phrasing_ops: 9
  slug: optimizely-order-history-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order History Promotions API from Optimizely — 5 operation(s) for order history promotions.
  name: Optimizely Order History Promotions API
  phrasing_intents:
  - id: OrderHistoryPromotions_Get
    intent: List promotions recorded on past orders
    question: Which promotions were applied to historical orders?
  - id: OrderHistoryPromotions_Post
    intent: Record a promotion on a historical order
    question: How do I record a discount against an order from order history?
  - id: OrderHistoryPromotions_GetById
    intent: Get a promotion on a past order
    question: How much did a promotion save on a historical order?
  - id: OrderHistoryPromotions_PutById
    intent: Replace a promotion on a past order
    question: How do I overwrite every field of an order history promotion?
  - id: OrderHistoryPromotions_DeleteById
    intent: Delete a promotion from a past order
    question: How do I remove a promotion record from order history?
  - id: OrderHistoryPromotions_PatchById
    intent: Correct the amount on a past order promotion
    question: How do I fix the discount amount recorded on an old order?
  - id: OrderHistoryPromotions_Default
    intent: Get defaults for a new order history promotion
    question: What defaults does a new order history promotion start with?
  - id: OrderHistoryPromotions_DeleteRoute
    intent: Delete several order history promotions
    question: How do I bulk delete promotions from order history?
  phrasing_ops: 9
  slug: optimizely-order-history-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order History Taxes API from Optimizely — 5 operation(s) for order history taxes.
  name: Optimizely Order History Taxes API
  phrasing_intents:
  - id: OrderHistoryTaxes_Get
    intent: List order history tax lines
    question: Which tax lines are recorded on historical orders?
  - id: OrderHistoryTaxes_Post
    intent: Add a tax line to order history
    question: How do I record a tax line on an imported historical order?
  - id: OrderHistoryTaxes_GetById
    intent: Get an order history tax line
    question: Can I look up one historical order tax line by ID?
  - id: OrderHistoryTaxes_PutById
    intent: Replace an order history tax line
    question: How do I overwrite a historical order tax line completely?
  - id: OrderHistoryTaxes_DeleteById
    intent: Delete an order history tax line
    question: How do I remove a tax line from a historical order?
  - id: OrderHistoryTaxes_PatchById
    intent: Correct an order history tax line
    question: Can I fix only the tax amount on a historical order line?
  - id: OrderHistoryTaxes_Default
    intent: Get default values for a new order history tax
    question: What defaults does a new order history tax line start with?
  - id: OrderHistoryTaxes_DeleteRoute
    intent: Bulk delete order history tax lines
    question: Can I delete many historical order tax lines at once?
  phrasing_ops: 9
  slug: optimizely-order-history-taxes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Line Requisitions API from Optimizely — 5 operation(s) for order line requisitions.
  name: Optimizely Order Line Requisitions API
  phrasing_intents:
  - id: OrderLineRequisitions_Get
    intent: List order line requisitions
    question: Which requisitions have buyers raised against order lines?
  - id: OrderLineRequisitions_Post
    intent: Create an order line requisition
    question: How do I record a requisition for a quantity on an order line?
  - id: OrderLineRequisitions_GetById
    intent: Get an order line requisition
    question: Who requested a given requisition and for what quantity?
  - id: OrderLineRequisitions_PutById
    intent: Replace an order line requisition
    question: How do I overwrite an order line requisition in full?
  - id: OrderLineRequisitions_DeleteById
    intent: Delete an order line requisition
    question: How do I cancel out a requisition record by deleting it?
  - id: OrderLineRequisitions_PatchById
    intent: Update an order line requisition
    question: Can I change just the quantity on an existing requisition?
  - id: OrderLineRequisitions_Default
    intent: Get a blank requisition template
    question: What default values does a new order line requisition start with?
  - id: OrderLineRequisitions_DeleteRoute
    intent: Bulk delete order line requisitions
    question: How do I delete many requisitions at once?
  phrasing_ops: 9
  slug: optimizely-order-line-requisitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Line Rfqs API from Optimizely — 5 operation(s) for order line rfqs.
  name: Optimizely Order Line Rfqs API
  phrasing_intents:
  - id: OrderLineRfqs_Get
    intent: List order line RFQ quotes
    question: Which order lines have RFQ quantity-break pricing on them?
  - id: OrderLineRfqs_Post
    intent: Create quantity-break pricing for an order line
    question: How do I quote tiered pricing on an order line for a request for quote?
  - id: OrderLineRfqs_GetById
    intent: Get an order line RFQ
    question: What quantity breaks and prices were quoted on one order line RFQ?
  - id: OrderLineRfqs_PutById
    intent: Replace an order line RFQ
    question: How do I overwrite all the price breaks on an order line RFQ?
  - id: OrderLineRfqs_DeleteById
    intent: Delete an order line RFQ
    question: Can I remove the RFQ pricing from one order line?
  - id: OrderLineRfqs_PatchById
    intent: Update an order line RFQ
    question: How do I change just the second price break on an order line RFQ?
  - id: OrderLineRfqs_Default
    intent: Get a blank order line RFQ template
    question: What default values does a new order line RFQ start with?
  - id: OrderLineRfqs_DeleteRoute
    intent: Bulk delete order line RFQs
    question: Can I delete several order line RFQs at once?
  phrasing_ops: 9
  slug: optimizely-order-line-rfqs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Line Vats API from Optimizely — 5 operation(s) for order line vats.
  name: Optimizely Order Line Vats API
  phrasing_intents:
  - id: OrderLineVats_Get
    intent: List VAT entries on order lines
    question: What VAT has been charged across my order lines?
  - id: OrderLineVats_Post
    intent: Add a VAT entry to an order line
    question: How do I record VAT against a specific order line?
  - id: OrderLineVats_GetById
    intent: Get an order line VAT entry by ID
    question: What rate and amount does one order line VAT record hold?
  - id: OrderLineVats_PutById
    intent: Replace an order line VAT entry
    question: Can I overwrite an entire order line VAT record at once?
  - id: OrderLineVats_DeleteById
    intent: Delete an order line VAT entry by ID
    question: How do I remove a VAT entry from an order line?
  - id: OrderLineVats_PatchById
    intent: Update an order line VAT entry
    question: How do I correct the VAT amount on an existing order line VAT entry?
  - id: OrderLineVats_Default
    intent: Get a default order line VAT template
    question: What default values does a new order line VAT entry start with?
  - id: OrderLineVats_DeleteRoute
    intent: Bulk delete order line VAT entries
    question: How do I delete several order line VAT records at once?
  phrasing_ops: 9
  slug: optimizely-order-line-vats-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Lines API from Optimizely — 6 operation(s) for order lines.
  name: Optimizely Order Lines API
  phrasing_intents:
  - id: OrderLines_Get
    intent: List order lines
    question: What line items are on my customer orders in Optimizely Commerce?
  - id: OrderLines_Post
    intent: Add a line to a customer order
    question: How do I add a new product line to an existing customer order?
  - id: OrderLines_GetById
    intent: Get an order line by id
    question: Can I look up a single order line and its pricing by id?
  - id: OrderLines_PutById
    intent: Replace an order line
    question: How do I overwrite every field of an order line in one call?
  - id: OrderLines_DeleteById
    intent: Delete an order line
    question: Can I remove one line item from an order by its id?
  - id: OrderLines_PatchById
    intent: Update fields on an order line
    question: How do I change just the quantity on an existing order line?
  - id: OrderLines_Default
    intent: Get a blank order line template
    question: What default values does a new order line start with?
  - id: OrderLines_DeleteRoute
    intent: Bulk delete order lines
    question: Can I delete several order lines by id in one request?
  phrasing_ops: 10
  slug: optimizely-order-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Promotion Codes API from Optimizely — 5 operation(s) for order promotion codes.
  name: Optimizely Order Promotion Codes API
  phrasing_intents:
  - id: OrderPromotionCodes_Get
    intent: List promotion codes applied to orders
    question: How can I see which promotion codes were used on orders?
  - id: OrderPromotionCodes_Post
    intent: Apply a promotion code to an order
    question: How do I attach a promo code to a customer order?
  - id: OrderPromotionCodes_GetById
    intent: Get one order promotion code
    question: How can I look up a single order promotion code record?
  - id: OrderPromotionCodes_PutById
    intent: Replace an order promotion code
    question: How do I overwrite an order promotion code record completely?
  - id: OrderPromotionCodes_DeleteById
    intent: Remove a promotion code from an order
    question: How do I delete one promo code record from an order?
  - id: OrderPromotionCodes_PatchById
    intent: Update an order promotion code
    question: How can I correct a mistyped promo code on an order?
  - id: OrderPromotionCodes_Default
    intent: Get defaults for a new order promotion code
    question: What default values does a new order promotion code record have?
  - id: OrderPromotionCodes_DeleteRoute
    intent: Bulk delete order promotion codes
    question: How do I delete several order promotion code records at once?
  phrasing_ops: 9
  slug: optimizely-order-promotion-codes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Order Status Mappings API from Optimizely — 5 operation(s) for order status mappings.
  name: Optimizely Order Status Mappings API
  phrasing_intents:
  - id: OrderStatusMappings_Get
    intent: List order status mappings
    question: How are my ERP order statuses mapped to the names customers see?
  - id: OrderStatusMappings_Post
    intent: Map an ERP order status to a display name
    question: How do I add a mapping from an ERP order status to a customer-facing label?
  - id: OrderStatusMappings_GetById
    intent: Get one order status mapping
    question: What display name and rules does a specific order status mapping have?
  - id: OrderStatusMappings_PutById
    intent: Replace an order status mapping
    question: How do I overwrite an order status mapping entirely?
  - id: OrderStatusMappings_DeleteById
    intent: Delete an order status mapping
    question: How do I remove a single order status mapping?
  - id: OrderStatusMappings_PatchById
    intent: Partially update an order status mapping
    question: Can I just rename the label customers see for an order status?
  - id: OrderStatusMappings_Default
    intent: Get the default order status mapping template
    question: What default values does a new order status mapping start with?
  - id: OrderStatusMappings_DeleteRoute
    intent: Bulk delete order status mappings
    question: How do I delete several order status mappings at once?
  phrasing_ops: 10
  slug: optimizely-order-status-mappings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Orderapprovals API from Optimizely — 2 operation(s) for orderapprovals.
  name: Optimizely Orderapprovals API
  phrasing_intents:
  - id: OrderApprovalsV1_GetCollectionAsync
    intent: List orders awaiting approval
    question: Which orders are waiting for me to approve them?
  - id: OrderApprovalsV1_GetAsync
    intent: Get an order awaiting approval
    question: What is in a specific cart that is waiting for approval?
  phrasing_ops: 2
  slug: optimizely-orderapprovals-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Orderfeed API from Optimizely — 1 operation(s) for orderfeed.
  name: Optimizely Orderfeed API
  phrasing_intents:
  - id: ProductRecommendationOrderFeedV1_GetAsync
    intent: Get the order feed for product recommendations
    question: How do I pull the order feed used to train product recommendations?
  phrasing_ops: 1
  slug: optimizely-orderfeed-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Override API from Optimizely — 1 operation(s) for override.
  name: Optimizely Override API
  phrasing_intents:
  - id: override
    intent: Force a user into an experiment variation
    question: How can I force a test user into a specific variation for debugging?
  phrasing_ops: 1
  slug: optimizely-override-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page State Contexts API from Optimizely — 5 operation(s) for page state contexts.
  name: Optimizely Page State Contexts API
  phrasing_intents:
  - id: PageStateContexts_Get
    intent: List page state contexts
    question: How can I see every language, persona and device context for my page states?
  - id: PageStateContexts_Post
    intent: Create a page state context
    question: How do I add a language or persona context to a page state?
  - id: PageStateContexts_GetById
    intent: Get one page state context
    question: How do I look up a single page state context by id?
  - id: PageStateContexts_PutById
    intent: Replace a page state context
    question: Can I overwrite a whole page state context record?
  - id: PageStateContexts_DeleteById
    intent: Delete a single page state context
    question: How do I delete one page state context?
  - id: PageStateContexts_PatchById
    intent: Set rollback or approval on a page state context
    question: Can I schedule a rollback date on an existing page state context?
  - id: PageStateContexts_Default
    intent: Get default values for a new page state context
    question: What defaults does a new page state context start with?
  - id: PageStateContexts_DeleteRoute
    intent: Delete several page state contexts at once
    question: How do I bulk delete page state contexts?
  phrasing_ops: 9
  slug: optimizely-page-state-contexts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page States API from Optimizely — 6 operation(s) for page states.
  name: Optimizely Page States API
  phrasing_intents:
  - id: PageStates_Get
    intent: List CMS page states
    question: How can I list the page states behind the storefront's content tree?
  - id: PageStates_Post
    intent: Create a page state
    question: Can I add a page state for a page node on a website?
  - id: PageStates_GetById
    intent: Get a page state
    question: Can I look up one page state and see whether it has an experiment?
  - id: PageStates_PutById
    intent: Replace a page state
    question: Can I overwrite a whole page state record?
  - id: PageStates_DeleteById
    intent: Delete a page state
    question: How do I remove a single page state?
  - id: PageStates_PatchById
    intent: Update a page state
    question: Can I change only the sort order of a page state?
  - id: PageStates_Default
    intent: Get default values for a page state
    question: What defaults are pre-filled for a new page state?
  - id: PageStates_DeleteRoute
    intent: Delete several page states
    question: Can I bulk delete page states in one call?
  phrasing_ops: 10
  slug: optimizely-page-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page Temporaries API from Optimizely — 5 operation(s) for page temporaries.
  name: Optimizely Page Temporaries API
  phrasing_intents:
  - id: PageTemporaries_Get
    intent: List temporary page records
    question: How do I list the temporary page records stored in the commerce admin?
  - id: PageTemporaries_Post
    intent: Create a temporary page record
    question: How do I store a new temporary page value?
  - id: PageTemporaries_GetById
    intent: Get a temporary page record
    question: How do I read one temporary page record by ID?
  - id: PageTemporaries_PutById
    intent: Replace a temporary page record
    question: How do I overwrite a temporary page record completely?
  - id: PageTemporaries_DeleteById
    intent: Delete a temporary page record
    question: How do I delete one temporary page record?
  - id: PageTemporaries_PatchById
    intent: Update a temporary page record
    question: How do I change only the value of a page temporary?
  - id: PageTemporaries_Default
    intent: Get a default page temporary template
    question: What default values does a new page temporary start with?
  - id: PageTemporaries_DeleteRoute
    intent: Bulk delete temporary page records
    question: How do I clear out several temporary page records at once?
  phrasing_ops: 9
  slug: optimizely-page-temporaries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page Urls API from Optimizely — 5 operation(s) for page urls.
  name: Optimizely Page Urls API
  phrasing_intents:
  - id: PageUrls_Get
    intent: List content page URLs
    question: How do I list every page URL on my Optimizely Configured Commerce websites?
  - id: PageUrls_Post
    intent: Create a page URL
    question: Can I give a content page a new URL with a publish window?
  - id: PageUrls_GetById
    intent: Get one page URL
    question: How can I see the settings on a single page URL record?
  - id: PageUrls_PutById
    intent: Replace a page URL record
    question: Can I overwrite a page URL record with all new values?
  - id: PageUrls_DeleteById
    intent: Delete a page URL
    question: How do I delete one page URL?
  - id: PageUrls_PatchById
    intent: Update a page URL's settings
    question: Can I hide an existing page from search engines without resending the whole record?
  - id: PageUrls_Default
    intent: Get default values for a page URL
    question: What defaults are pre-filled for a new page URL?
  - id: PageUrls_DeleteRoute
    intent: Delete several page URLs
    question: Can I bulk delete a batch of page URLs?
  phrasing_ops: 9
  slug: optimizely-page-urls-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Page Versions API from Optimizely — 5 operation(s) for page versions.
  name: Optimizely Page Versions API
  phrasing_intents:
  - id: PageVersions_Get
    intent: List storefront page versions
    question: Which versions of my storefront pages are waiting for approval?
  - id: PageVersions_Post
    intent: Create a page version
    question: How do I save a new version of a storefront page scheduled to publish later?
  - id: PageVersions_GetById
    intent: Get one page version
    question: How do I read a single page version, including who published it?
  - id: PageVersions_PutById
    intent: Replace a page version
    question: How do I overwrite a page version record completely?
  - id: PageVersions_DeleteById
    intent: Delete a page version
    question: How do I discard an unwanted page version?
  - id: PageVersions_PatchById
    intent: Reschedule or approve a page version
    question: Can I change only the publish date of a scheduled page version?
  - id: PageVersions_Default
    intent: Call the Default function on page versions
    question: What does the Default OData function on page versions return?
  - id: PageVersions_DeleteRoute
    intent: Bulk delete page versions
    question: Can I clean up many old page versions in one call?
  phrasing_ops: 9
  slug: optimizely-page-versions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Payment Methods API from Optimizely — 7 operation(s) for payment methods.
  name: Optimizely Payment Methods API
  phrasing_intents:
  - id: PaymentMethods_Get
    intent: List payment methods
    question: Which payment methods are configured for checkout?
  - id: PaymentMethods_Post
    intent: Create a payment method
    question: How do I add a new payment option like buy now pay later?
  - id: PaymentMethods_GetById
    intent: Get a payment method
    question: Is a given payment method a credit card, eCheck or BNPL option?
  - id: PaymentMethods_PutById
    intent: Replace a payment method entirely
    question: How do I overwrite every field of a payment method?
  - id: PaymentMethods_DeleteById
    intent: Delete a payment method
    question: How do I permanently delete one payment method?
  - id: PaymentMethods_PatchById
    intent: Update some fields of a payment method
    question: How do I set a deactivation date on a payment method?
  - id: PaymentMethods_Default
    intent: Get default values for a new payment method
    question: What defaults does a new payment method start with?
  - id: PaymentMethods_Archive
    intent: Archive payment methods via the archive action
    question: How do I archive payment methods with the POST archive action?
  phrasing_ops: 11
  slug: optimizely-payment-methods-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Paymentauthentication API from Optimizely — 9 operation(s) for paymentauthentication.
  name: Optimizely Paymentauthentication API
  phrasing_intents:
  - id: PaymentAuthenticationV1_Post
    intent: Start payment authentication for a card
    question: How do I run payment authentication on a card before placing a storefront order?
  - id: PaymentAuthenticationV1_Post2
    intent: Receive a 3-D Secure notification
    question: Where does the storefront receive the 3-D Secure notify post after a card check?
  - id: PaymentAuthenticationV1_AdyenWebhook
    intent: Receive a payment gateway webhook notification
    question: Which endpoint accepts the payment gateway's webhook notifications for the storefront?
  - id: PaymentAuthenticationV1_AdyenPaymentDetails
    intent: Submit additional gateway payment details
    question: How do I pass the extra details the gateway asks for after the first payment step?
  - id: PaymentAuthenticationV1_AdyenPayment
    intent: Make a payment through the payment gateway
    question: Which endpoint starts a new payment through the storefront's payment gateway integration?
  - id: PaymentAuthenticationV1_Refund
    intent: Refund a gateway payment
    question: How do I refund an order that was paid through the payment gateway?
  - id: PaymentAuthenticationV1_PostAsync
    intent: Submit a 3-D Secure challenge response
    question: Where does the shopper's answer to a 3-D Secure challenge get posted?
  - id: PaymentAuthenticationV1_PostAsync2
    intent: Handle a 3-D Secure callback
    question: Which URL handles the 3-D Secure callback after the issuer finishes?
  phrasing_ops: 9
  slug: optimizely-paymentauthentication-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Paymetric API from Optimizely — 2 operation(s) for paymetric.
  name: Optimizely Paymetric API
  phrasing_intents:
  - id: PaymetricV1_GetConfigAsync
    intent: Get the Paymetric payment configuration
    question: How does the storefront get its Paymetric card-entry configuration?
  - id: PaymetricV1_GetResponsePacketAsync
    intent: Get the Paymetric response packet
    question: How do I retrieve the Paymetric response packet after a card is entered?
  phrasing_ops: 2
  slug: optimizely-paymetric-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Persona User Profiles API from Optimizely — 5 operation(s) for persona user profiles.
  name: Optimizely Persona User Profiles API
  phrasing_intents:
  - id: PersonaUserProfiles_Get
    intent: List persona assignments for users
    question: How do I list which personas are assigned to which user profiles?
  - id: PersonaUserProfiles_Post
    intent: Assign a persona to a user profile
    question: How do I give a shopper a persona for personalized content?
  - id: PersonaUserProfiles_GetById
    intent: Get one persona assignment
    question: How do I look up a single persona-to-user assignment by id?
  - id: PersonaUserProfiles_PutById
    intent: Replace a persona assignment
    question: How do I overwrite a persona assignment record entirely?
  - id: PersonaUserProfiles_DeleteById
    intent: Remove a persona from a user
    question: How do I take a persona away from a user profile?
  - id: PersonaUserProfiles_PatchById
    intent: Change the persona on an assignment
    question: How do I switch a user's assigned persona to a different one?
  - id: PersonaUserProfiles_Default
    intent: Get the default persona assignment record
    question: What does a default persona user profile record look like?
  - id: PersonaUserProfiles_DeleteRoute
    intent: Bulk remove persona assignments
    question: How do I delete many persona assignments in one call?
  phrasing_ops: 9
  slug: optimizely-persona-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage personalized email attachments
  name: Optimizely Personalized Attachments API
  phrasing_intents:
  - id: createAttachment_1
    intent: Create a personalized attachment
    question: How do I upload a personalized attachment for my mailings?
  phrasing_ops: 1
  slug: optimizely-personalized-attachments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Personas API from Optimizely — 10 operation(s) for personas.
  name: Optimizely Personas API
  phrasing_intents:
  - id: Personas_Get
    intent: List personalization personas
    question: How do I list every persona set up for personalization in Optimizely Configured Commerce?
  - id: Personas_Post
    intent: Create a persona
    question: What do I need to define a new shopper persona with a name and description?
  - id: Personas_GetById
    intent: Get a persona by ID
    question: How can I see the settings of one persona, like its activation dates and boost value?
  - id: Personas_PutById
    intent: Replace a persona record
    question: Can I overwrite a persona with a full new definition in one call?
  - id: Personas_DeleteById
    intent: Delete one persona
    question: How do I permanently delete a single persona?
  - id: Personas_PatchById
    intent: Update part of a persona
    question: Can I turn on search boosting for an existing persona without replacing it?
  - id: Personas_Default
    intent: Get default values for a new persona
    question: What defaults does the admin API fill in for a persona before it's created?
  - id: Personas_Archive
    intent: Archive personas (OData action)
    question: Can I archive personas I no longer use instead of deleting them, via the Default.archive action?
  phrasing_ops: 14
  slug: optimizely-personas-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 🏆 Pinned Results API from Optimizely — 5 operation(s) for 🏆 pinned results.
  name: Optimizely 🏆 Pinned Results API
  phrasing_intents:
  - id: list-PinnedCollectionHandler
    intent: List pinned collections
    question: Which pinned result collections exist in my search index?
  - id: create-PinnedCollectionHandler
    intent: Create a pinned collection
    question: How do I set up a new collection for pinned search results?
  - id: get-PinnedCollectionHandler
    intent: Get a pinned collection
    question: How do I look up one pinned collection by its id?
  - id: update-PinnedCollectionHandler
    intent: Update a pinned collection
    question: How do I rename a pinned collection or turn it off?
  - id: delete-PinnedCollectionHandler
    intent: Delete a pinned collection
    question: How do I delete an entire pinned collection?
  - id: list-PinnedItemHandler
    intent: List pinned items in a collection
    question: Which items are pinned inside a given collection?
  - id: create-PinnedItemHandler
    intent: Pin a document to search phrases
    question: How do I pin a specific document to the top of results for a search phrase?
  - id: clear-PinnedItemHandler
    intent: Clear all pinned items in a collection
    question: How do I wipe every pinned item from a collection but keep the collection?
  phrasing_ops: 12
  slug: optimizely-pinned-results-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Plan & Usage information for current account
  name: Optimizely Plan API
  phrasing_intents:
  - id: get_plan
    intent: Get plan and usage for all products
    question: What plan is my Optimizely account on, and how much of each product have we used?
  phrasing_ops: 1
  slug: optimizely-plan-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Plugins API from Optimizely — 7 operation(s) for plugins.
  name: Optimizely Plugins API
  phrasing_intents:
  - id: Plugins_Get
    intent: List plugins
    question: Which integration plugins are registered in the commerce admin?
  - id: Plugins_Post
    intent: Register a plugin
    question: How do I register a new integration plugin with its interface and version?
  - id: Plugins_GetById
    intent: Get a plugin
    question: Can I see one plugin's interface, version and connection?
  - id: Plugins_PutById
    intent: Replace a plugin
    question: How do I overwrite a plugin record completely?
  - id: Plugins_DeleteById
    intent: Delete a plugin
    question: How do I permanently delete a plugin?
  - id: Plugins_PatchById
    intent: Update fields on a plugin
    question: Can I deactivate a plugin without replacing it?
  - id: Plugins_Default
    intent: Get default values for a new plugin
    question: What defaults does a new plugin record start with?
  - id: Plugins_Archive
    intent: Archive plugins via OData action
    question: Can I archive plugins using the OData archive action?
  phrasing_ops: 11
  slug: optimizely-plugins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Price Matrices API from Optimizely — 7 operation(s) for price matrices.
  name: Optimizely Price Matrices API
  phrasing_intents:
  - id: PriceMatrices_Get
    intent: List price matrices
    question: Which price matrix records are set up for customer and product pricing?
  - id: PriceMatrices_Post
    intent: Create a price matrix
    question: How do I set up quantity break pricing for a product in a price matrix?
  - id: PriceMatrices_GetById
    intent: Get a price matrix
    question: What quantity breaks and amounts does a particular price matrix define?
  - id: PriceMatrices_PutById
    intent: Replace a price matrix
    question: How do I overwrite an entire price matrix record at once?
  - id: PriceMatrices_DeleteById
    intent: Delete a price matrix
    question: How do I permanently delete one price matrix?
  - id: PriceMatrices_PatchById
    intent: Update a price matrix
    question: Can I change the expiry date of a price matrix without resending it all?
  - id: PriceMatrices_Default
    intent: Get a blank price matrix template
    question: What default values does a new price matrix start with?
  - id: PriceMatrices_Archive
    intent: Archive price matrices via the archive action
    question: How do I archive old price matrices using the OData archive action?
  phrasing_ops: 11
  slug: optimizely-price-matrices-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Also Purchased Withs API from Optimizely — 5 operation(s) for product also purchased withs.
  name: Optimizely Product Also Purchased Withs API
  phrasing_intents:
  - id: ProductAlsoPurchasedWiths_Get
    intent: List frequently-bought-together product pairs
    question: Which products are most often bought together with each other?
  - id: ProductAlsoPurchasedWiths_Post
    intent: Add a bought-together product pair
    question: How do I record that one product is commonly purchased with another?
  - id: ProductAlsoPurchasedWiths_GetById
    intent: Get an also-purchased-with record
    question: How many customers bought a given product pair together?
  - id: ProductAlsoPurchasedWiths_PutById
    intent: Replace an also-purchased-with record
    question: Can I overwrite all the stats on a bought-together record at once?
  - id: ProductAlsoPurchasedWiths_DeleteById
    intent: Delete an also-purchased-with record
    question: How do I remove a bought-together suggestion that no longer makes sense?
  - id: ProductAlsoPurchasedWiths_PatchById
    intent: Update the scores on an also-purchased record
    question: Can I adjust only the weighted score of a bought-together pair?
  - id: ProductAlsoPurchasedWiths_Default
    intent: Call the also-purchased-with Default function
    question: What does the Default function on also-purchased-with records return?
  - id: ProductAlsoPurchasedWiths_DeleteRoute
    intent: Bulk delete also-purchased-with records
    question: Can I wipe many bought-together records in one request?
  phrasing_ops: 9
  slug: optimizely-product-also-purchased-withs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Attribute Values API from Optimizely — 5 operation(s) for product attribute values.
  name: Optimizely Product Attribute Values API
  phrasing_intents:
  - id: ProductAttributeValues_Get
    intent: List product attribute value links
    question: Which attribute values, like color or size, are assigned to my products?
  - id: ProductAttributeValues_Post
    intent: Assign an attribute value to a product
    question: How do I tag a product with an attribute value such as Blue?
  - id: ProductAttributeValues_GetById
    intent: Get a product attribute value link
    question: Can I look up one product-to-attribute assignment by its id?
  - id: ProductAttributeValues_PutById
    intent: Replace a product attribute value link
    question: Is there a way to overwrite a product attribute assignment completely?
  - id: ProductAttributeValues_DeleteById
    intent: Remove an attribute value from a product
    question: Can I unassign one attribute value from a product by id?
  - id: ProductAttributeValues_PatchById
    intent: Change the value on a product attribute link
    question: How do I switch a product's attribute to a different value?
  - id: ProductAttributeValues_Default
    intent: Get a blank product attribute value template
    question: What default values does a new product attribute assignment start with?
  - id: ProductAttributeValues_DeleteRoute
    intent: Bulk remove product attribute values
    question: Can I remove many product attribute assignments at once?
  phrasing_ops: 9
  slug: optimizely-product-attribute-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Images API from Optimizely — 7 operation(s) for product images.
  name: Optimizely Product Images API
  phrasing_intents:
  - id: ProductImages_Get
    intent: List product images
    question: Which images are attached to products in my commerce catalog?
  - id: ProductImages_Post
    intent: Add an image to a product
    question: How do I attach a new image to a product with small, medium and large paths?
  - id: ProductImages_GetById
    intent: Get a product image
    question: What image paths and alt text does one product image record hold?
  - id: ProductImages_PutById
    intent: Replace a product image
    question: How do I overwrite a product image record entirely?
  - id: ProductImages_DeleteById
    intent: Delete a product image
    question: Can I remove one image from a product by its image ID?
  - id: ProductImages_PatchById
    intent: Update a product image
    question: How do I change just the alt text on an existing product image?
  - id: ProductImages_Default
    intent: Get a blank product image template
    question: What default values does a new product image start with?
  - id: ProductImages_SetSortOrders_1
    intent: Reorder several product images
    question: How do I reorder a product's images in one call?
  phrasing_ops: 11
  slug: optimizely-product-images-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Kit Section Options API from Optimizely — 5 operation(s) for product kit section options.
  name: Optimizely Product Kit Section Options API
  phrasing_intents:
  - id: ProductKitSectionOptions_Get
    intent: List product kit section options
    question: What options can buyers choose within configurable product kit sections in Optimizely commerce?
  - id: ProductKitSectionOptions_Post
    intent: Add an option to a product kit section
    question: How do I add a selectable product option to a kit section?
  - id: ProductKitSectionOptions_GetById
    intent: Get a product kit section option
    question: What price and quantity does a specific kit option have?
  - id: ProductKitSectionOptions_PutById
    intent: Replace a product kit section option
    question: How do I overwrite a kit option record entirely?
  - id: ProductKitSectionOptions_DeleteById
    intent: Delete a product kit section option
    question: How do I remove an option from a product kit section?
  - id: ProductKitSectionOptions_PatchById
    intent: Update a product kit section option
    question: How do I change the price of one kit option?
  - id: ProductKitSectionOptions_Default
    intent: Get a blank default kit section option
    question: What does an empty kit section option look like?
  - id: ProductKitSectionOptions_DeleteRoute
    intent: Delete several kit section options
    question: Can I delete multiple kit options in one request?
  phrasing_ops: 9
  slug: optimizely-product-kit-section-options-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Kit Sections API from Optimizely — 6 operation(s) for product kit sections.
  name: Optimizely Product Kit Sections API
  phrasing_intents:
  - id: ProductKitSections_Get
    intent: List product kit sections
    question: How do I list the sections that make up configurable product kits?
  - id: ProductKitSections_Post
    intent: Add a section to a product kit
    question: How do I add a new section to a configurable product kit?
  - id: ProductKitSections_GetById
    intent: Get one product kit section
    question: How do I look up a single kit section by its ID?
  - id: ProductKitSections_PutById
    intent: Replace a product kit section
    question: How do I overwrite a whole kit section record?
  - id: ProductKitSections_DeleteById
    intent: Delete a product kit section
    question: How do I remove one section from a product kit?
  - id: ProductKitSections_PatchById
    intent: Update a product kit section
    question: How do I rename the label shown on a kit section?
  - id: ProductKitSections_Default
    intent: Get a blank kit section template
    question: What default values does a new product kit section start with?
  - id: ProductKitSections_DeleteRoute
    intent: Bulk delete product kit sections
    question: How do I delete several kit sections at once?
  phrasing_ops: 10
  slug: optimizely-product-kit-sections-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Lines API from Optimizely — 6 operation(s) for product lines.
  name: Optimizely Product Lines API
  phrasing_intents:
  - id: ProductLines_Get
    intent: List product lines
    question: Which product lines do we have in the catalog?
  - id: ProductLines_Post
    intent: Create a product line
    question: How do I add a new product line under a brand?
  - id: ProductLines_GetById
    intent: Get a product line
    question: How do I look up one product line's details and image settings?
  - id: ProductLines_PutById
    intent: Replace a product line
    question: How do I overwrite a product line record completely?
  - id: ProductLines_DeleteById
    intent: Delete a product line
    question: How do I remove a product line from the catalog?
  - id: ProductLines_PatchById
    intent: Update a product line
    question: How do I boost a product line in search results?
  - id: ProductLines_Default
    intent: Get the default product line template
    question: What default values does a new product line start with?
  - id: ProductLines_DeleteRoute
    intent: Bulk delete product lines
    question: How do I delete several product lines in one request?
  phrasing_ops: 10
  slug: optimizely-product-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Related Products API from Optimizely — 5 operation(s) for product related products.
  name: Optimizely Product Related Products API
  phrasing_intents:
  - id: ProductRelatedProducts_Get
    intent: List related-product links
    question: Which cross-sell and related-product links are set up in my catalog?
  - id: ProductRelatedProducts_Post
    intent: Link a related product to a product
    question: How do I mark one product as related to another?
  - id: ProductRelatedProducts_GetById
    intent: Get a related-product link
    question: What two products does a related-product record connect?
  - id: ProductRelatedProducts_PutById
    intent: Replace a related-product link
    question: How do I overwrite a related-product link completely?
  - id: ProductRelatedProducts_DeleteById
    intent: Remove a related-product link
    question: How do I unlink a related product from a product?
  - id: ProductRelatedProducts_PatchById
    intent: Reorder or retarget a related-product link
    question: Can I change just the sort order of a related product?
  - id: ProductRelatedProducts_Default
    intent: Get default values for a new related-product link
    question: What defaults does a new related-product link start with?
  - id: ProductRelatedProducts_DeleteRoute
    intent: Bulk delete related-product links
    question: Can I remove many related-product links in one request?
  phrasing_ops: 9
  slug: optimizely-product-related-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Tax Exemptions API from Optimizely — 5 operation(s) for product tax exemptions.
  name: Optimizely Product Tax Exemptions API
  phrasing_intents:
  - id: ProductTaxExemptions_Get
    intent: List product tax exemptions
    question: Which products carry a tax exemption in Optimizely Commerce?
  - id: ProductTaxExemptions_Post
    intent: Exempt a product from a tax
    question: How do I make a product exempt from a particular tax?
  - id: ProductTaxExemptions_GetById
    intent: Get one product tax exemption
    question: Which product and exemption does a given exemption link connect?
  - id: ProductTaxExemptions_PutById
    intent: Replace a product tax exemption link
    question: Can I overwrite a product tax exemption record entirely?
  - id: ProductTaxExemptions_DeleteById
    intent: Remove a product's tax exemption
    question: How do I make a product taxable again by removing its exemption?
  - id: ProductTaxExemptions_PatchById
    intent: Switch a product exemption to another tax
    question: Can I point an existing product exemption at a different tax exemption?
  - id: ProductTaxExemptions_Default
    intent: Get default values for a product exemption
    question: What defaults does a new product tax exemption start with?
  - id: ProductTaxExemptions_DeleteRoute
    intent: Bulk delete product tax exemptions
    question: Can I remove many product tax exemptions at once?
  phrasing_ops: 9
  slug: optimizely-product-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Top Sellers API from Optimizely — 5 operation(s) for product top sellers.
  name: Optimizely Product Top Sellers API
  phrasing_intents:
  - id: ProductTopSellers_Get
    intent: List top-selling product records
    question: Which products are my top sellers in Optimizely Configured Commerce?
  - id: ProductTopSellers_Post
    intent: Add a product top seller record
    question: How do I record a product as a top seller for a website and category?
  - id: ProductTopSellers_GetById
    intent: Get one top seller record
    question: How do I look up a single top seller record's purchase stats by ID?
  - id: ProductTopSellers_PutById
    intent: Replace a top seller record
    question: Can I overwrite a top seller record with a full new set of sales figures?
  - id: ProductTopSellers_DeleteById
    intent: Delete a top seller record
    question: How do I remove a product from the top sellers by record ID?
  - id: ProductTopSellers_PatchById
    intent: Update a top seller record
    question: Can I flag an existing top seller as seasonal?
  - id: ProductTopSellers_Default
    intent: Get default values for a top seller record
    question: What defaults does the admin pre-fill for a new top seller record?
  - id: ProductTopSellers_DeleteRoute
    intent: Bulk delete top seller records
    question: How do I clear several top seller records in one request?
  phrasing_ops: 9
  slug: optimizely-product-top-sellers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Unit Of Measures API from Optimizely — 5 operation(s) for product unit of measures.
  name: Optimizely Product Unit Of Measures API
  phrasing_intents:
  - id: ProductUnitOfMeasures_Get
    intent: List product units of measure
    question: How do I list all the selling units, like each, box or case, defined across products?
  - id: ProductUnitOfMeasures_Post
    intent: Add a unit of measure to a product
    question: What do I need to add a case or box unit to a product?
  - id: ProductUnitOfMeasures_GetById
    intent: Get one product unit of measure
    question: Where do I look up a single product unit of measure by its id?
  - id: ProductUnitOfMeasures_PutById
    intent: Replace a product unit of measure
    question: How do I overwrite a product unit of measure record completely?
  - id: ProductUnitOfMeasures_DeleteById
    intent: Delete a product unit of measure
    question: Can I remove a unit of measure a product no longer sells in?
  - id: ProductUnitOfMeasures_PatchById
    intent: Update fields on a product unit of measure
    question: Can I make an existing unit of measure the product's default?
  - id: ProductUnitOfMeasures_Default
    intent: Call the Default function on units of measure
    question: What does the Default function on ProductUnitOfMeasures return?
  - id: ProductUnitOfMeasures_DeleteRoute
    intent: Bulk delete product units of measure
    question: Can I delete many unit of measure records at once by id?
  phrasing_ops: 9
  slug: optimizely-product-unit-of-measures-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Product Warehouses API from Optimizely — 5 operation(s) for product warehouses.
  name: Optimizely Product Warehouses API
  phrasing_intents:
  - id: ProductWarehouses_Get
    intent: List product stock by warehouse
    question: How do I see product inventory across all warehouses?
  - id: ProductWarehouses_Post
    intent: Stock a product in a warehouse
    question: How do I add a product to a warehouse with its available quantity?
  - id: ProductWarehouses_GetById
    intent: Get one product warehouse record
    question: How do I check the stock record for one product-warehouse pairing?
  - id: ProductWarehouses_PutById
    intent: Replace a product warehouse record
    question: What's the call to overwrite a product warehouse stock record entirely?
  - id: ProductWarehouses_DeleteById
    intent: Remove a product from a warehouse
    question: How do I delete a product's stock record from a warehouse?
  - id: ProductWarehouses_PatchById
    intent: Update warehouse stock for a product
    question: How do I update the available quantity of a product in a warehouse?
  - id: ProductWarehouses_Default
    intent: Get the default product warehouse record
    question: What does a blank product warehouse stock record contain?
  - id: ProductWarehouses_DeleteRoute
    intent: Bulk delete product warehouse records
    question: Can I remove many product warehouse records in one go?
  phrasing_ops: 9
  slug: optimizely-product-warehouses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Products API from Optimizely — 54 operation(s) for products.
  name: Optimizely Products API
  phrasing_intents:
  - id: Products_Get
    intent: List products in the commerce admin
    question: How do I pull every product record out of the Configured Commerce admin API?
  - id: Products_Post
    intent: Create a new product record
    question: How do I add a brand-new product to the commerce catalog through the admin API?
  - id: Products_GetById
    intent: Get one product record by id
    question: How do I look up a single product's full admin record when I have its id?
  - id: Products_PutById
    intent: Replace a product record entirely
    question: How do I overwrite an entire product record with a new full version?
  - id: Products_DeleteById
    intent: Delete a single product record
    question: How do I permanently remove one product from the commerce admin by its id?
  - id: Products_PatchById
    intent: Update selected fields on a product
    question: How do I change just a product's sale price without resending the whole record?
  - id: Products_Default
    intent: Call the Default function on products
    question: What does the Default function on the admin Products entity set return?
  - id: Products_Archive
    intent: Archive products via the OData archive action
    question: How do I archive a batch of products using the Default.archive action?
  phrasing_ops: 58
  slug: optimizely-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Productsrssfeed API from Optimizely — 1 operation(s) for productsrssfeed.
  name: Optimizely Productsrssfeed API
  phrasing_intents:
  - id: ProductRecommendationsRssFeedV1_GetAsync
    intent: Get the product recommendations RSS feed
    question: Is there an RSS feed of recommended products I can plug into emails or other channels?
  phrasing_ops: 1
  slug: optimizely-productsrssfeed-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotion Result Products API from Optimizely — 5 operation(s) for promotion result products.
  name: Optimizely Promotion Result Products API
  phrasing_intents:
  - id: PromotionResultProducts_Get
    intent: List promotion result products
    question: Which products are tied to my promotion results, like free-gift items?
  - id: PromotionResultProducts_Post
    intent: Attach a product to a promotion result
    question: How do I link a product to a promotion's outcome?
  - id: PromotionResultProducts_GetById
    intent: Get a promotion result product by id
    question: Which product and promotion result does one link record connect?
  - id: PromotionResultProducts_PutById
    intent: Replace a promotion result product
    question: How do I overwrite a promotion result product record entirely?
  - id: PromotionResultProducts_DeleteById
    intent: Remove a product from a promotion result
    question: Can I unlink one product from a promotion result by id?
  - id: PromotionResultProducts_PatchById
    intent: Swap the product on a promotion result link
    question: How do I change which product a promotion result points to?
  - id: PromotionResultProducts_Default
    intent: Get a blank promotion result product template
    question: What default values does a new promotion result product have?
  - id: PromotionResultProducts_DeleteRoute
    intent: Bulk delete promotion result products
    question: Can I remove many promotion result products in one call?
  phrasing_ops: 9
  slug: optimizely-promotion-result-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotion Result Types API from Optimizely — 1 operation(s) for promotion result types.
  name: Optimizely Promotion Result Types API
  phrasing_intents:
  - id: PromotionResultTypes_Get
    intent: List the available promotion result types
    question: What kinds of promotion outcomes, like discounts, can a promotion apply?
  phrasing_ops: 1
  slug: optimizely-promotion-result-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotion Results API from Optimizely — 12 operation(s) for promotion results.
  name: Optimizely Promotion Results API
  phrasing_intents:
  - id: PromotionResults_Get
    intent: List promotion results
    question: What discounts and rewards are configured across promotions?
  - id: PromotionResults_Post
    intent: Create a promotion result
    question: How do I add a percentage discount reward to a promotion?
  - id: PromotionResults_GetById
    intent: Get a promotion result
    question: What reward does a particular promotion result grant?
  - id: PromotionResults_PutById
    intent: Replace a promotion result entirely
    question: How do I overwrite every field of a promotion result?
  - id: PromotionResults_DeleteById
    intent: Delete a promotion result
    question: How do I remove a single reward from a promotion?
  - id: PromotionResults_PatchById
    intent: Update some fields of a promotion result
    question: How do I change just the discount amount on a promotion result?
  - id: PromotionResults_Default
    intent: Get default values for a new promotion result
    question: What defaults does a new promotion result start with?
  - id: PromotionResults_ImportProductsAsyncById
    intent: Import products into a promotion result
    question: How do I import a product list into a promotion result using the OData import action?
  phrasing_ops: 16
  slug: optimizely-promotion-results-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Promotions API from Optimizely — 12 operation(s) for promotions.
  name: Optimizely Promotions API
  phrasing_intents:
  - id: Promotions_Get
    intent: List promotions
    question: Which promotions are set up in the commerce admin?
  - id: Promotions_Post
    intent: Create a promotion
    question: How do I set up a new promotion with a promo code?
  - id: Promotions_GetById
    intent: Get a promotion
    question: Can I pull up one promotion's details by its ID?
  - id: Promotions_PutById
    intent: Replace a promotion
    question: How do I overwrite a promotion record completely?
  - id: Promotions_DeleteById
    intent: Delete a promotion
    question: How do I permanently delete one promotion?
  - id: Promotions_PatchById
    intent: Update fields on a promotion
    question: Can I change just the deactivation date of a promotion?
  - id: Promotions_Default
    intent: Get default values for a new promotion
    question: What defaults does a newly created promotion start with?
  - id: Promotions_Archive
    intent: Archive promotions via OData action
    question: Can I archive a batch of promotions with the OData archive action?
  phrasing_ops: 16
  slug: optimizely-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Property Attribute Configurations API from Optimizely — 5 operation(s) for property attribute configurations.
  name: Optimizely Property Attribute Configurations API
  phrasing_intents:
  - id: PropertyAttributeConfigurations_Get
    intent: List property attribute configurations
    question: Which name/value attributes are configured on admin property configurations?
  - id: PropertyAttributeConfigurations_Post
    intent: Add an attribute to a property configuration
    question: How do I add a name and value attribute to a property configuration?
  - id: PropertyAttributeConfigurations_GetById
    intent: Get a property attribute configuration
    question: Can I look up one property attribute configuration by ID?
  - id: PropertyAttributeConfigurations_PutById
    intent: Replace a property attribute configuration
    question: Can I overwrite a property attribute configuration completely?
  - id: PropertyAttributeConfigurations_DeleteById
    intent: Delete a property attribute configuration
    question: How do I remove one attribute from a property configuration?
  - id: PropertyAttributeConfigurations_PatchById
    intent: Update a property attribute's value
    question: Can I change only the value of a property attribute?
  - id: PropertyAttributeConfigurations_Default
    intent: Get default values for a property attribute
    question: What defaults are pre-filled for a new property attribute configuration?
  - id: PropertyAttributeConfigurations_DeleteRoute
    intent: Delete several property attribute configurations
    question: Can I bulk delete property attribute configurations?
  phrasing_ops: 9
  slug: optimizely-property-attribute-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Property Configurations API from Optimizely — 7 operation(s) for property configurations.
  name: Optimizely Property Configurations API
  phrasing_intents:
  - id: PropertyConfigurations_Get
    intent: List property configurations
    question: Which field configurations are defined for admin entities?
  - id: PropertyConfigurations_Post
    intent: Create a property configuration
    question: How do I add a new custom field configuration to an entity?
  - id: PropertyConfigurations_GetById
    intent: Get a property configuration by ID
    question: What control type and label does one property configuration use?
  - id: PropertyConfigurations_PutById
    intent: Replace a property configuration
    question: Can I overwrite an entire property configuration record at once?
  - id: PropertyConfigurations_DeleteById
    intent: Delete a property configuration by ID
    question: How do I delete one property configuration?
  - id: PropertyConfigurations_PatchById
    intent: Update a property configuration
    question: How do I change the hint text or tooltip of an existing property?
  - id: PropertyConfigurations_Default
    intent: Get a default property configuration template
    question: What default values does a new property configuration start with?
  - id: PropertyConfigurations_DeleteRoute
    intent: Bulk delete property configurations
    question: How do I delete several property configurations at once?
  phrasing_ops: 11
  slug: optimizely-property-configurations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Property Permissions API from Optimizely — 5 operation(s) for property permissions.
  name: Optimizely Property Permissions API
  phrasing_intents:
  - id: PropertyPermissions_Get
    intent: List field-level property permissions
    question: How do I see which admin roles can view or edit each configured property?
  - id: PropertyPermissions_Post
    intent: Grant a role access to a property
    question: How do I let a role view but not edit a specific property?
  - id: PropertyPermissions_GetById
    intent: Get one property permission
    question: How do I check the view and edit flags on a single property permission?
  - id: PropertyPermissions_PutById
    intent: Replace a property permission
    question: How do I overwrite a whole property permission record?
  - id: PropertyPermissions_DeleteById
    intent: Delete a property permission
    question: How do I remove a role's permission on a property?
  - id: PropertyPermissions_PatchById
    intent: Change a role's view or edit rights on a property
    question: How do I revoke edit rights on a property for a role without deleting the permission?
  - id: PropertyPermissions_Default
    intent: Get a blank property permission template
    question: What default values does a new property permission start with?
  - id: PropertyPermissions_DeleteRoute
    intent: Bulk delete property permissions
    question: How do I delete several property permissions at once?
  phrasing_ops: 9
  slug: optimizely-property-permissions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Publishing API from Optimizely — 4 operation(s) for publishing.
  name: Optimizely Publishing API
  phrasing_intents:
  - id: listPublishingChannels
    intent: List publishing channels
    question: Which publishing channels are available in my Optimizely CMP organization?
  - id: getPublishingEvent
    intent: Get a publishing event
    question: What are the details of a specific publishing event?
  - id: listPublishingEventMetadata
    intent: List asset publishing metadata for an event
    question: Which assets in a publishing event failed or succeeded to publish?
  - id: bulkCreatePublishingEventMetadata
    intent: Record publishing metadata for assets in bulk
    question: How do I report publishing results for many assets of an event at once?
  - id: getPublishingEventAssetMetadata
    intent: Get one asset's publishing metadata
    question: Where can I see the publishing metadata record for one asset in an event?
  phrasing_ops: 5
  slug: optimizely-publishing-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Customer User Profile Maps API from Optimizely — 5 operation(s) for punch out customer user profile maps.
  name: Optimizely Punch Out Customer User Profile Maps API
  phrasing_intents:
  - id: PunchOutCustomerUserProfileMaps_Get
    intent: List punchout customer-user mappings
    question: Which punchout users are mapped to which customers and addresses?
  - id: PunchOutCustomerUserProfileMaps_Post
    intent: Map a punchout user to a customer
    question: How do I map a punchout user profile to a customer and ship-to address?
  - id: PunchOutCustomerUserProfileMaps_GetById
    intent: Get a punchout customer-user mapping
    question: How do I look up one punchout customer user mapping?
  - id: PunchOutCustomerUserProfileMaps_PutById
    intent: Replace a punchout customer-user mapping
    question: How do I overwrite a punchout customer user mapping entirely?
  - id: PunchOutCustomerUserProfileMaps_DeleteById
    intent: Delete a punchout customer-user mapping
    question: How do I unmap a punchout user from a customer?
  - id: PunchOutCustomerUserProfileMaps_PatchById
    intent: Update a punchout customer-user mapping
    question: How do I change the ship-to address on a punchout user mapping?
  - id: PunchOutCustomerUserProfileMaps_Default
    intent: Get the default punchout mapping template
    question: What default values does a new punchout customer user mapping start with?
  - id: PunchOutCustomerUserProfileMaps_DeleteRoute
    intent: Bulk delete punchout customer-user mappings
    question: How do I delete several punchout user mappings at once?
  phrasing_ops: 9
  slug: optimizely-punch-out-customer-user-profile-maps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Extrinsics API from Optimizely — 5 operation(s) for punch out order request extrinsics.
  name: Optimizely Punch Out Order Request Extrinsics API
  phrasing_intents:
  - id: PunchOutOrderRequestExtrinsics_Get
    intent: List punchout order request extrinsics
    question: Which extrinsic name-value pairs came in on punchout order requests?
  - id: PunchOutOrderRequestExtrinsics_Post
    intent: Add an extrinsic to a punchout order request
    question: How do I store a cXML extrinsic on a punchout order request?
  - id: PunchOutOrderRequestExtrinsics_GetById
    intent: Get a punchout order request extrinsic
    question: What value does a specific punchout extrinsic hold?
  - id: PunchOutOrderRequestExtrinsics_PutById
    intent: Replace a punchout extrinsic
    question: How do I overwrite a punchout extrinsic record completely?
  - id: PunchOutOrderRequestExtrinsics_DeleteById
    intent: Delete a punchout extrinsic
    question: How do I delete one extrinsic from a punchout order request?
  - id: PunchOutOrderRequestExtrinsics_PatchById
    intent: Update a punchout extrinsic's value
    question: How do I change just the value of an existing punchout extrinsic?
  - id: PunchOutOrderRequestExtrinsics_Default
    intent: Get defaults for a new punchout extrinsic
    question: What defaults does a new punchout extrinsic start with?
  - id: PunchOutOrderRequestExtrinsics_DeleteRoute
    intent: Delete several punchout extrinsics
    question: How do I bulk delete punchout order request extrinsics?
  phrasing_ops: 9
  slug: optimizely-punch-out-order-request-extrinsics-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Item Out Extrinsics API from Optimizely — 5 operation(s) for punch out order request item out extrinsics.
  name: Optimizely Punch Out Order Request Item Out Extrinsics API
  phrasing_intents:
  - id: PunchOutOrderRequestItemOutExtrinsics_Get
    intent: List punchout item extrinsics
    question: Which extrinsic name/value pairs are attached to outgoing punchout order request items?
  - id: PunchOutOrderRequestItemOutExtrinsics_Post
    intent: Add an extrinsic to a punchout item
    question: How do I attach an extra name/value field to an outgoing punchout item?
  - id: PunchOutOrderRequestItemOutExtrinsics_GetById
    intent: Get a punchout item extrinsic
    question: Can I look up one punchout item extrinsic by ID?
  - id: PunchOutOrderRequestItemOutExtrinsics_PutById
    intent: Replace a punchout item extrinsic
    question: How do I overwrite a punchout item extrinsic entirely?
  - id: PunchOutOrderRequestItemOutExtrinsics_DeleteById
    intent: Delete a punchout item extrinsic
    question: How do I remove one extrinsic from a punchout item?
  - id: PunchOutOrderRequestItemOutExtrinsics_PatchById
    intent: Change a punchout item extrinsic value
    question: Can I change only the value of a punchout item extrinsic?
  - id: PunchOutOrderRequestItemOutExtrinsics_Default
    intent: Get default values for a new punchout item extrinsic
    question: What defaults does a new punchout item extrinsic start with?
  - id: PunchOutOrderRequestItemOutExtrinsics_DeleteRoute
    intent: Bulk delete punchout item extrinsics
    question: Can I delete many punchout item extrinsics at once?
  phrasing_ops: 9
  slug: optimizely-punch-out-order-request-item-out-extrinsics-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Item Outs API from Optimizely — 7 operation(s) for punch out order request item outs.
  name: Optimizely Punch Out Order Request Item Outs API
  phrasing_intents:
  - id: PunchOutOrderRequestItemOuts_Get
    intent: List punchout order request line items
    question: How can I see all the line items that came in on punchout order requests?
  - id: PunchOutOrderRequestItemOuts_Post
    intent: Add a line item to a punchout order request
    question: How do I record a new line on a procurement punchout order request?
  - id: PunchOutOrderRequestItemOuts_GetById
    intent: Get one punchout order request item
    question: How can I inspect a single punchout order request line by its id?
  - id: PunchOutOrderRequestItemOuts_PutById
    intent: Replace a punchout order request item
    question: How do I overwrite an entire punchout order request line?
  - id: PunchOutOrderRequestItemOuts_DeleteById
    intent: Delete one punchout order request item
    question: How do I remove a single line from a punchout order request?
  - id: PunchOutOrderRequestItemOuts_PatchById
    intent: Update fields on a punchout order request item
    question: How can I change only the quantity on a punchout order line?
  - id: PunchOutOrderRequestItemOuts_Default
    intent: Get defaults for a new punchout order item
    question: What default values does a new punchout order request item get?
  - id: PunchOutOrderRequestItemOuts_DeleteRoute
    intent: Bulk delete punchout order request items
    question: How do I delete several punchout order request lines in one call?
  phrasing_ops: 11
  slug: optimizely-punch-out-order-request-item-outs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Request Messages API from Optimizely — 5 operation(s) for punch out order request messages.
  name: Optimizely Punch Out Order Request Messages API
  phrasing_intents:
  - id: PunchOutOrderRequestMessages_Get
    intent: List punchout order validation messages
    question: What validation errors and warnings were logged for punchout orders?
  - id: PunchOutOrderRequestMessages_Post
    intent: Log a punchout order validation message
    question: How do I record a validation warning against a punchout order request?
  - id: PunchOutOrderRequestMessages_GetById
    intent: Get a punchout validation message by ID
    question: What does a particular punchout validation message say?
  - id: PunchOutOrderRequestMessages_PutById
    intent: Replace a punchout validation message
    question: How do I overwrite a punchout validation message record in full?
  - id: PunchOutOrderRequestMessages_DeleteById
    intent: Delete a punchout validation message
    question: How do I clear one punchout validation message once it is resolved?
  - id: PunchOutOrderRequestMessages_PatchById
    intent: Update a punchout validation message
    question: Can I change just the wording of a punchout validation message?
  - id: PunchOutOrderRequestMessages_Default
    intent: Get a blank punchout message template
    question: What default values does a new punchout validation message start with?
  - id: PunchOutOrderRequestMessages_DeleteRoute
    intent: Bulk delete punchout validation messages
    question: How do I clear many punchout validation messages in one go?
  phrasing_ops: 9
  slug: optimizely-punch-out-order-request-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Order Requests API from Optimizely — 8 operation(s) for punch out order requests.
  name: Optimizely Punch Out Order Requests API
  phrasing_intents:
  - id: PunchOutOrderRequests_Get
    intent: List punchout order requests
    question: Which punchout purchase orders have come in from procurement systems?
  - id: PunchOutOrderRequests_Post
    intent: Record a punchout order request
    question: How do I store an incoming cXML punchout order request in the commerce admin?
  - id: PunchOutOrderRequests_GetById
    intent: Get a punchout order request
    question: What are the ship-to and bill-to details of one punchout order request?
  - id: PunchOutOrderRequests_PutById
    intent: Replace a punchout order request
    question: How do I overwrite a full punchout order request record?
  - id: PunchOutOrderRequests_DeleteById
    intent: Delete a punchout order request
    question: How do I remove one punchout order request by its ID?
  - id: PunchOutOrderRequests_PatchById
    intent: Update a punchout order request
    question: Can I change just the status of a punchout order request?
  - id: PunchOutOrderRequests_Default
    intent: Get a blank punchout order request template
    question: What default values does a new punchout order request start with?
  - id: PunchOutOrderRequests_DeleteRoute
    intent: Bulk delete punchout order requests
    question: How do I delete many punchout order requests at once?
  phrasing_ops: 12
  slug: optimizely-punch-out-order-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Session Accesses API from Optimizely — 5 operation(s) for punch out session accesses.
  name: Optimizely Punch Out Session Accesses API
  phrasing_intents:
  - id: PunchOutSessionAccesses_Get
    intent: List punchout session access records
    question: Which IP addresses have accessed my punchout sessions?
  - id: PunchOutSessionAccesses_Post
    intent: Record a punchout session access
    question: How do I log an IP address against a punchout session?
  - id: PunchOutSessionAccesses_GetById
    intent: Get a punchout session access record
    question: What IP address is on a particular punchout access record?
  - id: PunchOutSessionAccesses_PutById
    intent: Replace a punchout session access record
    question: How do I overwrite a punchout access record in full?
  - id: PunchOutSessionAccesses_DeleteById
    intent: Delete a punchout session access record
    question: Can I remove one punchout access record by ID?
  - id: PunchOutSessionAccesses_PatchById
    intent: Update a punchout session access record
    question: How do I correct the IP address on a punchout access record?
  - id: PunchOutSessionAccesses_Default
    intent: Get a blank punchout access template
    question: What default values does a new punchout session access have?
  - id: PunchOutSessionAccesses_DeleteRoute
    intent: Bulk delete punchout session accesses
    question: Can I clear out several punchout access records at once?
  phrasing_ops: 9
  slug: optimizely-punch-out-session-accesses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Session Extrinsics API from Optimizely — 5 operation(s) for punch out session extrinsics.
  name: Optimizely Punch Out Session Extrinsics API
  phrasing_intents:
  - id: PunchOutSessionExtrinsics_Get
    intent: List punchout session extrinsics
    question: Which extrinsic values did buyers' procurement systems send in punchout sessions?
  - id: PunchOutSessionExtrinsics_Post
    intent: Add an extrinsic to a punchout session
    question: How do I store a name/value extrinsic on a punchout session?
  - id: PunchOutSessionExtrinsics_GetById
    intent: Get a punchout session extrinsic by ID
    question: What name and value does one punchout extrinsic record hold?
  - id: PunchOutSessionExtrinsics_PutById
    intent: Replace a punchout session extrinsic
    question: Can I overwrite a whole punchout extrinsic record at once?
  - id: PunchOutSessionExtrinsics_DeleteById
    intent: Delete a punchout session extrinsic by ID
    question: How do I remove one extrinsic from a punchout session?
  - id: PunchOutSessionExtrinsics_PatchById
    intent: Update a punchout session extrinsic
    question: How do I change the value of an existing punchout extrinsic?
  - id: PunchOutSessionExtrinsics_Default
    intent: Get a default punchout extrinsic template
    question: What default values does a new punchout session extrinsic start with?
  - id: PunchOutSessionExtrinsics_DeleteRoute
    intent: Bulk delete punchout session extrinsics
    question: How do I delete several punchout extrinsics at once?
  phrasing_ops: 9
  slug: optimizely-punch-out-session-extrinsics-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Session Item Ins API from Optimizely — 5 operation(s) for punch out session item ins.
  name: Optimizely Punch Out Session Item Ins API
  phrasing_intents:
  - id: PunchOutSessionItemIns_Get
    intent: List items brought into punchout sessions
    question: How can I see the items a buyer's procurement system sent into punchout sessions?
  - id: PunchOutSessionItemIns_Post
    intent: Add an item to a punchout session
    question: How do I record an item coming into a punchout session?
  - id: PunchOutSessionItemIns_GetById
    intent: Get one punchout session item
    question: How can I look up a single item in a punchout session?
  - id: PunchOutSessionItemIns_PutById
    intent: Replace a punchout session item
    question: How do I overwrite a punchout session item completely?
  - id: PunchOutSessionItemIns_DeleteById
    intent: Delete one punchout session item
    question: How do I remove a single item from a punchout session?
  - id: PunchOutSessionItemIns_PatchById
    intent: Update a punchout session item
    question: How can I fix only the supplier part id on a punchout session item?
  - id: PunchOutSessionItemIns_Default
    intent: Get defaults for a new punchout session item
    question: What default values does a new punchout session item have?
  - id: PunchOutSessionItemIns_DeleteRoute
    intent: Bulk delete punchout session items
    question: How do I delete several punchout session items at once?
  phrasing_ops: 9
  slug: optimizely-punch-out-session-item-ins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Sessions API from Optimizely — 10 operation(s) for punch out sessions.
  name: Optimizely Punch Out Sessions API
  phrasing_intents:
  - id: PunchOutSessions_Get
    intent: List punchout sessions
    question: Which procurement punchout sessions have buyers opened against my commerce site?
  - id: PunchOutSessions_Post
    intent: Create a punchout session record
    question: How do I record a new punchout session from a buyer's procurement system?
  - id: PunchOutSessions_GetById
    intent: Get one punchout session
    question: How do I look up a single punchout session and its ship-to details?
  - id: PunchOutSessions_PutById
    intent: Replace a punchout session record
    question: How do I overwrite every field of an existing punchout session?
  - id: PunchOutSessions_DeleteById
    intent: Delete a punchout session
    question: How do I remove a single punchout session record?
  - id: PunchOutSessions_PatchById
    intent: Update fields on a punchout session
    question: Can I change just the ship-to address on a punchout session?
  - id: PunchOutSessions_Default
    intent: Call the Default function on punchout sessions
    question: What does the Default OData function on the punchout sessions set return?
  - id: PunchOutSessions_DeleteRoute
    intent: Bulk delete punchout sessions by ID
    question: Can I delete several punchout sessions in one call?
  phrasing_ops: 14
  slug: optimizely-punch-out-sessions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punch Out Setup Requests API from Optimizely — 5 operation(s) for punch out setup requests.
  name: Optimizely Punch Out Setup Requests API
  phrasing_intents:
  - id: PunchOutSetupRequests_Get
    intent: List PunchOut setup requests
    question: Which cXML PunchOut setup requests have procurement systems sent to my store?
  - id: PunchOutSetupRequests_Post
    intent: Record a PunchOut setup request
    question: How do I store a new cXML PunchOut setup request with its response?
  - id: PunchOutSetupRequests_GetById
    intent: Get one PunchOut setup request
    question: What cXML and response were recorded for a specific PunchOut setup request?
  - id: PunchOutSetupRequests_PutById
    intent: Replace a PunchOut setup request record
    question: How do I overwrite a stored PunchOut setup request entirely?
  - id: PunchOutSetupRequests_DeleteById
    intent: Delete a PunchOut setup request
    question: How do I remove one logged PunchOut setup request?
  - id: PunchOutSetupRequests_PatchById
    intent: Partially update a PunchOut setup request
    question: Can I change only the response stored on a PunchOut setup request?
  - id: PunchOutSetupRequests_Default
    intent: Get the default PunchOut setup request template
    question: What default values does a new PunchOut setup request record start with?
  - id: PunchOutSetupRequests_DeleteRoute
    intent: Bulk delete PunchOut setup requests
    question: How do I purge many PunchOut setup requests in one call?
  phrasing_ops: 9
  slug: optimizely-punch-out-setup-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Punchout API from Optimizely — 5 operation(s) for punchout.
  name: Optimizely Punchout API
  phrasing_intents:
  - id: PunchOutV1_SetupRequestAsync
    intent: Start a punchout setup request
    question: How does a buyer's procurement system start a punchout session with the storefront?
  - id: PunchOutV1_SessionRequestAsync
    intent: Resume a punchout session
    question: Can I load an existing punchout session by its session id?
  - id: PunchOutV1_ProfileTransactionRequestAsync
    intent: Send a punchout profile transaction request
    question: Which punchout transactions does the storefront support, per a profile request?
  - id: PunchOutV1_PoRequisitionAsync
    intent: Return the cart as a punchout PO requisition
    question: How do I send the punchout cart back to the buyer's procurement system as a requisition?
  - id: PunchOutV1_OrderRequestAsync
    intent: Submit a punchout purchase order request
    question: How does an approved purchase order come back from procurement into the storefront?
  phrasing_ops: 5
  slug: optimizely-punchout-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Push Notification Logs API from Optimizely — 5 operation(s) for push notification logs.
  name: Optimizely Push Notification Logs API
  phrasing_intents:
  - id: PushNotificationLogs_Get
    intent: List push notification delivery logs
    question: How can I see the delivery log for push notifications sent to devices?
  - id: PushNotificationLogs_Post
    intent: Record a push notification delivery attempt
    question: What goes into a push notification log entry?
  - id: PushNotificationLogs_GetById
    intent: Get one push notification log entry
    question: How do I look up one push notification log entry?
  - id: PushNotificationLogs_PutById
    intent: Replace a push notification log entry
    question: Can I overwrite an entire push notification log record?
  - id: PushNotificationLogs_DeleteById
    intent: Delete a single push notification log
    question: How do I delete one push notification log entry?
  - id: PushNotificationLogs_PatchById
    intent: Mark a push notification as delivered
    question: Can I update a push log with the date it was delivered?
  - id: PushNotificationLogs_Default
    intent: Get default values for a new push log
    question: What defaults does a new push notification log start with?
  - id: PushNotificationLogs_DeleteRoute
    intent: Delete several push notification logs at once
    question: How do I bulk clear push notification logs?
  phrasing_ops: 9
  slug: optimizely-push-notification-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Push Notification Messages API from Optimizely — 6 operation(s) for push notification messages.
  name: Optimizely Push Notification Messages API
  phrasing_intents:
  - id: PushNotificationMessages_Get
    intent: List push notification messages
    question: Which push notifications have been sent to app users?
  - id: PushNotificationMessages_Post
    intent: Create a push notification message
    question: How do I create a push notification for a specific user?
  - id: PushNotificationMessages_GetById
    intent: Get a push notification message
    question: What did a particular push notification say and when was it sent?
  - id: PushNotificationMessages_PutById
    intent: Replace a push notification message
    question: How do I overwrite every field of a push notification message?
  - id: PushNotificationMessages_DeleteById
    intent: Delete a push notification message
    question: How do I delete one push notification message?
  - id: PushNotificationMessages_PatchById
    intent: Update a push notification message
    question: How do I edit the title of an existing push notification?
  - id: PushNotificationMessages_Default
    intent: Get default values for a new push message
    question: What defaults does a new push notification message start with?
  - id: PushNotificationMessages_DeleteRoute
    intent: Delete several push notification messages
    question: How do I bulk delete old push notification messages?
  phrasing_ops: 10
  slug: optimizely-push-notification-messages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The ▶️ Query ( GraphQL ) API from Optimizely — 1 operation(s) for ▶️ query ( graphql ).
  name: Optimizely ▶️ Query ( GraphQL ) API
  phrasing_intents:
  - id: get-GraphQLV2Handler
    intent: Run a GraphQL content query via GET
    question: Can I query Optimizely Graph content with a GraphQL query in the URL query string?
  - id: post-GraphQLV2Handler
    intent: Run a GraphQL content query via POST
    question: How do I POST a GraphQL query body to fetch content?
  phrasing_ops: 2
  slug: optimizely-query-graphql-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Quotes API from Optimizely — 4 operation(s) for quotes.
  name: Optimizely Quotes API
  phrasing_intents:
  - id: QuotesV1_GetCollectionAsync
    intent: Search quotes by customer, status or date
    question: Which quotes are still open for a particular customer?
  - id: QuotesV1_PostAsync
    intent: Request a quote from the cart
    question: How does a B2B buyer submit a request for quote?
  - id: QuotesV1_GetAsync
    intent: Get a quote
    question: What is the current status and expiration date of a specific quote?
  - id: QuotesV1_DeleteAsync
    intent: Delete a quote
    question: Can I delete a quote the customer no longer wants?
  - id: QuotesV1_PatchAsync
    intent: Update, price or accept a quote
    question: How does a sales rep apply a percentage discount to a quote?
  - id: QuotesV1_PostMessageAsync
    intent: Send a message on a quote
    question: Can the buyer and sales rep message each other about a quote?
  - id: QuoteLinesV1_GetAsync
    intent: Get a line item on a quote
    question: What quantity and pricing are on a specific line of a quote?
  - id: QuoteLinesV1_PatchAsync
    intent: Update quantity or pricing on a quote line
    question: Can I change the quantity of a product on a quote line?
  phrasing_ops: 8
  slug: optimizely-quotes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rating Services API from Optimizely — 1 operation(s) for rating services.
  name: Optimizely Rating Services API
  phrasing_intents:
  - id: RatingServices_Get
    intent: List rating services
    question: Which rating services are configured in my commerce admin?
  phrasing_ops: 1
  slug: optimizely-rating-services-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Reachability API from Optimizely — 2 operation(s) for reachability.
  name: Optimizely Reachability API
  phrasing_intents:
  - id: update-reachability
    intent: Update whether an identifier is reachable
    question: How do I mark an email address as unreachable after a hard bounce?
  - id: get-reachability
    intent: Check if an identifier is reachable
    question: Can I still send messages to a given email address, or is it unreachable?
  phrasing_ops: 2
  slug: optimizely-reachability-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Realtimecartinventory API from Optimizely — 1 operation(s) for realtimecartinventory.
  name: Optimizely Realtimecartinventory API
  phrasing_intents:
  - id: RealTimeCartInventoryV1_PostAsync
    intent: Check real-time inventory for a cart
    question: Are the items in a cart in stock right now?
  phrasing_ops: 1
  slug: optimizely-realtimecartinventory-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Realtimeinventory API from Optimizely — 1 operation(s) for realtimeinventory.
  name: Optimizely Realtimeinventory API
  phrasing_intents:
  - id: RealTimeInventoryV1_PostAsync
    intent: Look up real-time inventory for products
    question: How can I check live stock levels for a set of products?
  phrasing_ops: 1
  slug: optimizely-realtimeinventory-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Realtimepricing API from Optimizely — 1 operation(s) for realtimepricing.
  name: Optimizely Realtimepricing API
  phrasing_intents:
  - id: RealTimePricingV1_PostAsync
    intent: Get real-time prices for products
    question: How do I get live, real-time prices for several products in one request?
  phrasing_ops: 1
  slug: optimizely-realtimepricing-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The RealtimeSegments API from Optimizely — 3 operation(s) for realtimesegments.
  name: Optimizely Realtime Segments API
  phrasing_intents:
  - id: RealtimeSegments_ListSegments
    intent: List real-time segments
    question: Which real-time segments are defined in my account?
  - id: RealtimeSegments_GetSegment
    intent: Get a real-time segment's definition
    question: How can I see how a real-time segment is defined?
  - id: RealtimeSegments_UninstallSegment
    intent: Delete a real-time segment
    question: How do I remove a real-time segment I no longer need?
  - id: RealtimeSegments_CreateSegment
    intent: Create a new real-time segment
    question: How do I create a new real-time audience segment?
  - id: RealtimeSegments_InstallSegment
    intent: Update an existing real-time segment
    question: How do I change the rules of a real-time segment that already exists?
  - id: RealtimeSegments_ValidateSegment
    intent: Validate a segment definition
    question: Can I check a segment definition for errors before saving it?
  phrasing_ops: 6
  slug: optimizely-realtimesegments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: View, copy and update recipient lists
  name: Optimizely Recipient lists API
  phrasing_intents:
  - id: selectRecipientLists
    intent: List all recipient lists
    question: Which recipient lists does my Optimizely Campaign client have and how many recipients are in each?
  - id: copyRecipientList
    intent: Copy a recipient list
    question: How do I duplicate an existing recipient list?
  - id: getRecipientList
    intent: Get details of one recipient list
    question: How many recipients are on a specific recipient list?
  - id: updateRecipientList
    intent: Update a recipient list's name or test flag
    question: Can I rename a recipient list or change its description?
  - id: getRecipientListAttributeNames
    intent: Get a recipient list's attribute names
    question: What attribute names can I use for personalization on a recipient list?
  - id: getRecipientListFields
    intent: Get a recipient list's fields
    question: What fields does a recipient list store for each recipient?
  phrasing_ops: 6
  slug: optimizely-recipient-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Recommendations API from Optimizely — 5 operation(s) for recommendations.
  name: Optimizely Recommendations API
  phrasing_intents:
  - id: get-recommended-products
    intent: Get product recommendations
    question: How do I get personalized product recommendations for a customer?
  - id: recommendationUpdate
    intent: Mark a recommendation as read
    question: Can I dismiss a pending recommendation once I've reviewed it?
  - id: get_recs_catalog_csv
    intent: Download a recommendations catalog as CSV
    question: Can I export the product catalog data the recommender is using as a CSV?
  - id: get_recs_output_csv
    intent: Download computed recommendations as CSV
    question: Can I pull the full recommendations a recommender computed into a CSV?
  - id: get_recs_stats_csv
    intent: Download recommendation summary stats as CSV
    question: Where can I get summary statistics about a recommendations catalog?
  phrasing_ops: 5
  slug: optimizely-recommendations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Relationships schema API from Optimizely — 2 operation(s) for relationships schema.
  name: Optimizely Relationships schema API
  phrasing_intents:
  - id: create-relationship
    intent: Create a relationship between objects
    question: How do I relate one Optimizely Data Platform object to another?
  - id: list-relations
    intent: List an object's relationships
    question: Which relationships does a data platform object have to other objects?
  - id: get-relation
    intent: Get one relationship of an object
    question: What join fields does a specific relation on an object use?
  phrasing_ops: 3
  slug: optimizely-relationships-schema-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Reports
  name: Optimizely Reports API
  phrasing_intents:
  - id: list_reports
    intent: List experiment reports in an environment
    question: Which reports exist in a given project environment?
  - id: archive_reports
    intent: Archive reports
    question: Can I hide old reports without permanently deleting them?
  - id: unarchive_reports
    intent: Restore archived reports
    question: How do I bring an archived report back into the active list?
  - id: delete_report
    intent: Permanently delete a report
    question: Is deleting a report permanent, or can I get the data back?
  - id: fetch_report
    intent: Get a single report
    question: Can I open one report by its key in a specific environment?
  - id: reset_results
    intent: Reset a report's results
    question: Can I clear a report's results and start counting from now?
  - id: get_experiment_report
    intent: Get an experiment's results report
    question: Did my experiment's variations reach statistical significance?
  phrasing_ops: 7
  slug: optimizely-reports-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Requisitions API from Optimizely — 4 operation(s) for requisitions.
  name: Optimizely Requisitions API
  phrasing_intents:
  - id: RequisitionsV1_GetCollectionAsync
    intent: List purchase requisitions
    question: Which purchase requisitions are waiting for my approval?
  - id: RequisitionsV1_GetAsync
    intent: Get one purchase requisition
    question: How do I open a single requisition to review it?
  - id: RequisitionLinesV1_GetCollectionAsync
    intent: List the lines on a requisition
    question: Which products and quantities are on a requisition?
  - id: RequisitionLinesV1_GetAsync
    intent: Get one requisition line
    question: How do I see who requested a specific line item and when?
  - id: RequisitionLinesV1_DeleteAsync
    intent: Remove a line from a requisition
    question: How do I reject or drop one line item from a requisition?
  - id: RequisitionLinesV1_PatchAsync
    intent: Change quantity or cost code on a requisition line
    question: Can I change the quantity requested on a requisition line before approving it?
  phrasing_ops: 6
  slug: optimizely-requisitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The 📝 Resources API from Optimizely — 2 operation(s) for 📝 resources.
  name: Optimizely 📝 Resources API
  phrasing_intents:
  - id: upsert-StopwordHandler
    intent: Store search stop words
    question: How do I tell search to ignore common words like 'the' and 'and'?
  - id: delete-StopwordHandler
    intent: Delete search stop words
    question: Can I wipe the stop word list so every word counts in search?
  - id: list-SynonymHandler
    intent: List search synonyms for a slot
    question: Which synonyms are stored for my search index?
  - id: upsert-SynonymHandler
    intent: Store search synonyms
    question: How do I expand search queries so 'H2O' also finds 'water'?
  - id: delete-SynonymHandler
    intent: Delete search synonyms
    question: Can I clear out every synonym stored for search?
  phrasing_ops: 5
  slug: optimizely-resources-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage mailing responses, such as hard or soft bounces
  name: Optimizely Responses API
  phrasing_intents:
  - id: getBounceCounter
    intent: Get a recipient's bounce count
    question: How many hard or soft bounces has a recipient produced so far?
  - id: resetBounceCounter
    intent: Reset a recipient's bounces
    question: How do I clear the hard and soft bounces of a recipient so they get mailings again?
  - id: isBounceCounterThresholdExceeded
    intent: Check if a recipient exceeded the bounce limit
    question: Has a recipient gone over the hard or soft bounce threshold?
  - id: getBounceCounterThreshold
    intent: Get the allowed bounce threshold
    question: What is the maximum number of soft bounces allowed before mailings stop?
  - id: selectResponses
    intent: List a recipient's responses
    question: What responses, like auto-replies or bounces, did a recipient send back?
  phrasing_ops: 5
  slug: optimizely-responses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Customer Additions API from Optimizely — 5 operation(s) for restriction group customer additions.
  name: Optimizely Restriction Group Customer Additions API
  phrasing_intents:
  - id: RestrictionGroupCustomerAdditions_Get
    intent: List customers added to restriction groups
    question: Which customers have been added to product restriction groups?
  - id: RestrictionGroupCustomerAdditions_Post
    intent: Add a customer to a restriction group
    question: How do I put a customer into a product restriction group?
  - id: RestrictionGroupCustomerAdditions_GetById
    intent: Get a restriction group customer addition
    question: How do I look up one customer-to-restriction-group assignment?
  - id: RestrictionGroupCustomerAdditions_PutById
    intent: Replace a restriction group customer addition
    question: How do I overwrite a restriction group assignment record in full?
  - id: RestrictionGroupCustomerAdditions_DeleteById
    intent: Remove a customer from a restriction group
    question: How do I take a customer out of a restriction group?
  - id: RestrictionGroupCustomerAdditions_PatchById
    intent: Update a restriction group customer addition
    question: How do I move a customer's addition to a different restriction group?
  - id: RestrictionGroupCustomerAdditions_Default
    intent: Get a default restriction group addition template
    question: What default values does a new restriction group addition start with?
  - id: RestrictionGroupCustomerAdditions_DeleteRoute
    intent: Bulk remove restriction group customer additions
    question: How do I remove many customers from restriction groups at once?
  phrasing_ops: 9
  slug: optimizely-restriction-group-customer-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Customer Exceptions API from Optimizely — 5 operation(s) for restriction group customer exceptions.
  name: Optimizely Restriction Group Customer Exceptions API
  phrasing_intents:
  - id: RestrictionGroupCustomerExceptions_Get
    intent: List customer exceptions to restriction groups
    question: Which customers are exempted from product restriction groups in Optimizely Configured Commerce?
  - id: RestrictionGroupCustomerExceptions_Post
    intent: Exempt a customer from a restriction group
    question: How do I let one customer see products that a restriction group normally hides?
  - id: RestrictionGroupCustomerExceptions_GetById
    intent: Get one restriction group exception
    question: How can I look up a single customer exception record by ID?
  - id: RestrictionGroupCustomerExceptions_PutById
    intent: Replace a restriction group exception
    question: Can I overwrite an exception record with a different customer and group?
  - id: RestrictionGroupCustomerExceptions_DeleteById
    intent: Remove a customer's restriction exception
    question: How do I take away a customer's exemption from a restriction group?
  - id: RestrictionGroupCustomerExceptions_PatchById
    intent: Update a restriction group exception
    question: Can I move an existing exception to a different restriction group?
  - id: RestrictionGroupCustomerExceptions_Default
    intent: Get default values for an exception
    question: What defaults are pre-filled for a new restriction group customer exception?
  - id: RestrictionGroupCustomerExceptions_DeleteRoute
    intent: Delete several restriction group exceptions
    question: Can I bulk remove customer exceptions from restriction groups?
  phrasing_ops: 9
  slug: optimizely-restriction-group-customer-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Customers API from Optimizely — 5 operation(s) for restriction group customers.
  name: Optimizely Restriction Group Customers API
  phrasing_intents:
  - id: RestrictionGroupCustomers_Get
    intent: List customer assignments to restriction groups
    question: Which customers are assigned to product restriction groups?
  - id: RestrictionGroupCustomers_Post
    intent: Assign a customer to a restriction group
    question: How do I put a customer into a restriction group so their catalog is limited?
  - id: RestrictionGroupCustomers_GetById
    intent: Get one restriction group assignment
    question: How do I look up a single customer-to-restriction-group assignment?
  - id: RestrictionGroupCustomers_PutById
    intent: Replace a restriction group assignment
    question: How do I overwrite a customer's restriction group assignment in full?
  - id: RestrictionGroupCustomers_DeleteById
    intent: Remove a customer from a restriction group
    question: How do I lift a product restriction by removing the customer from the group?
  - id: RestrictionGroupCustomers_PatchById
    intent: Change when a restriction applies to a customer
    question: Can I switch a restriction to apply only when the customer is the bill-to?
  - id: RestrictionGroupCustomers_Default
    intent: Call the Default function on restriction assignments
    question: What does the Default OData function on restriction group customers return?
  - id: RestrictionGroupCustomers_DeleteRoute
    intent: Bulk remove restriction group assignments
    question: Can I remove many customers from restriction groups in a single call?
  phrasing_ops: 9
  slug: optimizely-restriction-group-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Product Additions API from Optimizely — 5 operation(s) for restriction group product additions.
  name: Optimizely Restriction Group Product Additions API
  phrasing_intents:
  - id: RestrictionGroupProductAdditions_Get
    intent: List products added to restriction groups
    question: Which products have been explicitly added to restriction groups in my commerce catalog?
  - id: RestrictionGroupProductAdditions_Post
    intent: Add a product to a restriction group
    question: How do I add a product to a restriction group?
  - id: RestrictionGroupProductAdditions_GetById
    intent: Get one restriction group product addition
    question: Which product and restriction group does a specific addition record link?
  - id: RestrictionGroupProductAdditions_PutById
    intent: Replace a restriction group product addition
    question: Is there a way to overwrite a whole restriction group product addition record?
  - id: RestrictionGroupProductAdditions_DeleteById
    intent: Remove a product from a restriction group
    question: How do I take a product back out of a restriction group?
  - id: RestrictionGroupProductAdditions_PatchById
    intent: Update a restriction group product addition
    question: Can I move an existing product addition to a different restriction group?
  - id: RestrictionGroupProductAdditions_Default
    intent: Call the Default function on restriction group additions
    question: What does the Default function on restriction group product additions return?
  - id: RestrictionGroupProductAdditions_DeleteRoute
    intent: Bulk delete restriction group product additions
    question: Can I pull many products out of restriction groups in one request?
  phrasing_ops: 9
  slug: optimizely-restriction-group-product-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Product Exceptions API from Optimizely — 5 operation(s) for restriction group product exceptions.
  name: Optimizely Restriction Group Product Exceptions API
  phrasing_intents:
  - id: RestrictionGroupProductExceptions_Get
    intent: List product exceptions to restriction groups
    question: How do I list products that are exempt from a restriction group?
  - id: RestrictionGroupProductExceptions_Post
    intent: Exempt a product from a restriction group
    question: How do I let one product bypass a restriction group?
  - id: RestrictionGroupProductExceptions_GetById
    intent: Get one restriction group product exception
    question: How do I look up a single restriction group exception by id?
  - id: RestrictionGroupProductExceptions_PutById
    intent: Replace a restriction group product exception
    question: How do I overwrite a restriction group exception record entirely?
  - id: RestrictionGroupProductExceptions_DeleteById
    intent: Remove a product's restriction exception
    question: How do I make a product subject to its restriction group again?
  - id: RestrictionGroupProductExceptions_PatchById
    intent: Update a restriction group product exception
    question: How do I point an existing exception at a different product?
  - id: RestrictionGroupProductExceptions_Default
    intent: Get the default restriction exception record
    question: What does a default restriction group product exception look like?
  - id: RestrictionGroupProductExceptions_DeleteRoute
    intent: Bulk delete restriction exceptions
    question: How do I remove many product exceptions in one call?
  phrasing_ops: 9
  slug: optimizely-restriction-group-product-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Products API from Optimizely — 5 operation(s) for restriction group products.
  name: Optimizely Restriction Group Products API
  phrasing_intents:
  - id: RestrictionGroupProducts_Get
    intent: List products in restriction groups
    question: Which products are covered by our product restriction groups?
  - id: RestrictionGroupProducts_Post
    intent: Add a product to a restriction group
    question: How do I restrict who can buy a product by adding it to a restriction group?
  - id: RestrictionGroupProducts_GetById
    intent: Get a restriction group product entry
    question: Which product and restriction group does a given entry link?
  - id: RestrictionGroupProducts_PutById
    intent: Replace a restriction group product entry
    question: Can I rewrite a restriction group product entry in full?
  - id: RestrictionGroupProducts_DeleteById
    intent: Remove a product from a restriction group
    question: How do I lift a restriction on a product by removing it from its group?
  - id: RestrictionGroupProducts_PatchById
    intent: Move a restricted product to another group
    question: Can I move a restricted product into a different restriction group?
  - id: RestrictionGroupProducts_Default
    intent: Call the restriction group products Default function
    question: What does the Default function on restriction group products return?
  - id: RestrictionGroupProducts_DeleteRoute
    intent: Bulk remove products from restriction groups
    question: Can I unrestrict many products at once by deleting their entries?
  phrasing_ops: 9
  slug: optimizely-restriction-group-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Group Websites API from Optimizely — 5 operation(s) for restriction group websites.
  name: Optimizely Restriction Group Websites API
  phrasing_intents:
  - id: RestrictionGroupWebsites_Get
    intent: List restriction group website links
    question: Which websites are product restriction groups applied to?
  - id: RestrictionGroupWebsites_Post
    intent: Apply a restriction group to a website
    question: How do I apply a product restriction group to one of my storefront websites?
  - id: RestrictionGroupWebsites_GetById
    intent: Get a restriction group website link
    question: Can I look up one restriction group to website link by id?
  - id: RestrictionGroupWebsites_PutById
    intent: Replace a restriction group website link
    question: Is there a way to overwrite a restriction group website link entirely?
  - id: RestrictionGroupWebsites_DeleteById
    intent: Remove a restriction group from a website
    question: Can I stop a restriction group applying to a website by deleting the link?
  - id: RestrictionGroupWebsites_PatchById
    intent: Change a restriction group website link
    question: How do I move a restriction group link to a different website?
  - id: RestrictionGroupWebsites_Default
    intent: Get a blank restriction group website template
    question: What default values does a new restriction group website link start with?
  - id: RestrictionGroupWebsites_DeleteRoute
    intent: Bulk remove restriction group website links
    question: Can I delete many restriction group website links in one request?
  phrasing_ops: 9
  slug: optimizely-restriction-group-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Restriction Groups API from Optimizely — 12 operation(s) for restriction groups.
  name: Optimizely Restriction Groups API
  phrasing_intents:
  - id: RestrictionGroups_Get
    intent: List restriction groups
    question: Which restriction groups are set up to limit what customers can buy in my Optimizely commerce site?
  - id: RestrictionGroups_Post
    intent: Create a restriction group
    question: How do I create a restriction group that controls product visibility for certain customers?
  - id: RestrictionGroups_GetById
    intent: Get a restriction group
    question: What are the settings of one specific restriction group?
  - id: RestrictionGroups_PutById
    intent: Replace a restriction group
    question: How do I overwrite a restriction group's full definition?
  - id: RestrictionGroups_DeleteById
    intent: Delete a restriction group
    question: How do I remove a restriction group I no longer need?
  - id: RestrictionGroups_PatchById
    intent: Update a restriction group
    question: How do I deactivate a restriction group without deleting it?
  - id: RestrictionGroups_Default
    intent: Get a blank default restriction group
    question: What fields does a default restriction group start with?
  - id: RestrictionGroups_DeleteRoute
    intent: Delete several restriction groups
    question: Can I delete a batch of restriction groups by their ids?
  phrasing_ops: 16
  slug: optimizely-restriction-groups-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Roles API from Optimizely — 1 operation(s) for roles.
  name: Optimizely Roles API
  phrasing_intents:
  - id: Roles_Get
    intent: List admin roles
    question: Which admin roles are defined in the commerce console?
  - id: Roles_Post
    intent: Create an admin role
    question: How do I create a new admin role?
  phrasing_ops: 2
  slug: optimizely-roles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Clause Customers API from Optimizely — 5 operation(s) for rule clause customers.
  name: Optimizely Rule Clause Customers API
  phrasing_intents:
  - id: RuleClauseCustomers_Get
    intent: List customers attached to rule clauses
    question: Which customers are targeted by rule clauses in my Optimizely commerce rules?
  - id: RuleClauseCustomers_Post
    intent: Attach a customer to a rule clause
    question: How do I make a rule clause apply to a specific customer?
  - id: RuleClauseCustomers_GetById
    intent: Get a rule clause customer link
    question: Which customer and rule clause does a given link record connect?
  - id: RuleClauseCustomers_PutById
    intent: Replace a rule clause customer link
    question: How do I overwrite a rule clause customer record?
  - id: RuleClauseCustomers_DeleteById
    intent: Detach a customer from a rule clause
    question: How do I stop a rule clause from applying to a customer?
  - id: RuleClauseCustomers_PatchById
    intent: Change the customer on a rule clause link
    question: How do I switch a rule clause link to a different customer?
  - id: RuleClauseCustomers_Default
    intent: Get a blank default rule clause customer
    question: What does an empty rule clause customer object contain?
  - id: RuleClauseCustomers_DeleteRoute
    intent: Delete several rule clause customer links
    question: Can I remove many rule clause customer links at once?
  phrasing_ops: 9
  slug: optimizely-rule-clause-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Clause Products API from Optimizely — 5 operation(s) for rule clause products.
  name: Optimizely Rule Clause Products API
  phrasing_intents:
  - id: RuleClauseProducts_Get
    intent: List products used in rule clauses
    question: Which products are referenced by my promotion or pricing rule clauses?
  - id: RuleClauseProducts_Post
    intent: Add a product to a rule clause
    question: How do I include a product in a rule clause?
  - id: RuleClauseProducts_GetById
    intent: Get a rule clause product link
    question: Which product and rule clause does a given record tie together?
  - id: RuleClauseProducts_PutById
    intent: Replace a rule clause product link
    question: How do I overwrite a rule clause product record entirely?
  - id: RuleClauseProducts_DeleteById
    intent: Remove a product from a rule clause
    question: How do I take a product out of a rule clause?
  - id: RuleClauseProducts_PatchById
    intent: Change the product or clause on a link
    question: Can I swap only the product on a rule clause product record?
  - id: RuleClauseProducts_Default
    intent: Get default values for a new rule clause product
    question: What defaults does a new rule clause product start with?
  - id: RuleClauseProducts_DeleteRoute
    intent: Bulk delete rule clause products
    question: Can I remove many products from rule clauses in one request?
  phrasing_ops: 9
  slug: optimizely-rule-clause-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Clauses API from Optimizely — 15 operation(s) for rule clauses.
  name: Optimizely Rule Clauses API
  phrasing_intents:
  - id: RuleClauses_Get
    intent: List rule clauses
    question: Which rule clauses are configured across my commerce rules?
  - id: RuleClauses_Post
    intent: Create a rule clause
    question: How do I add a new condition clause to a promotion or shipping rule?
  - id: RuleClauses_GetById
    intent: Get a rule clause
    question: How do I look up the condition and values of one specific rule clause?
  - id: RuleClauses_PutById
    intent: Replace a rule clause
    question: How do I overwrite an entire rule clause definition in one call?
  - id: RuleClauses_DeleteById
    intent: Delete a rule clause
    question: How do I remove one condition from a rule?
  - id: RuleClauses_PatchById
    intent: Update a rule clause
    question: How do I change just the comparison value on an existing rule clause?
  - id: RuleClauses_Default
    intent: Get the default rule clause template
    question: What default values does a brand-new rule clause start with?
  - id: RuleClauses_ImportProductsAsyncById
    intent: Import products into a rule clause
    question: How do I bulk import a product list into a rule clause condition?
  phrasing_ops: 19
  slug: optimizely-rule-clauses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Managers API from Optimizely — 8 operation(s) for rule managers.
  name: Optimizely Rule Managers API
  phrasing_intents:
  - id: RuleManagers_Get
    intent: List rule managers
    question: Which rule managers are defined in my commerce admin?
  - id: RuleManagers_Post
    intent: Create a rule manager
    question: How do I create a new rule manager for my commerce rules?
  - id: RuleManagers_GetById
    intent: Get a rule manager
    question: What rule type does a given rule manager use?
  - id: RuleManagers_PutById
    intent: Replace a rule manager
    question: How do I overwrite a rule manager record in full?
  - id: RuleManagers_DeleteById
    intent: Delete a rule manager
    question: Can I delete a single rule manager by ID?
  - id: RuleManagers_PatchById
    intent: Update a rule manager
    question: How do I rename an existing rule manager?
  - id: RuleManagers_Default
    intent: Get a blank rule manager template
    question: What default values does a new rule manager have?
  - id: RuleManagers_SetRulesById
    intent: Set the rule clauses of a rule manager
    question: How do I define the rule clauses a rule manager evaluates?
  phrasing_ops: 12
  slug: optimizely-rule-managers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Type Options API from Optimizely — 5 operation(s) for rule type options.
  name: Optimizely Rule Type Options API
  phrasing_intents:
  - id: RuleTypeOptions_Get
    intent: List rule type criteria options
    question: What criteria options can rules be built from in Optimizely Commerce?
  - id: RuleTypeOptions_Post
    intent: Add a criteria option to a rule type
    question: How do I define a new criterion that rules of a given type can check?
  - id: RuleTypeOptions_GetById
    intent: Get one rule type option
    question: What property and value type does a specific rule criteria option check?
  - id: RuleTypeOptions_PutById
    intent: Replace a rule type option
    question: Can I overwrite a rule criteria option entirely?
  - id: RuleTypeOptions_DeleteById
    intent: Delete one rule type option
    question: How do I remove a criteria option from a rule type?
  - id: RuleTypeOptions_PatchById
    intent: Edit a rule type option's criteria
    question: Can I change just the description shown for a rule criteria option?
  - id: RuleTypeOptions_Default
    intent: Get default values for a rule type option
    question: What defaults does a new rule type option start with?
  - id: RuleTypeOptions_DeleteRoute
    intent: Bulk delete rule type options
    question: Can I remove many rule type options in one request?
  phrasing_ops: 9
  slug: optimizely-rule-type-options-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Rule Types API from Optimizely — 6 operation(s) for rule types.
  name: Optimizely Rule Types API
  phrasing_intents:
  - id: RuleTypes_Get
    intent: List rule types
    question: Which rule types are available for building promotion and pricing rules?
  - id: RuleTypes_Post
    intent: Create a rule type
    question: How do I add a new rule type?
  - id: RuleTypes_GetById
    intent: Get a rule type
    question: Can I look up one rule type by its ID?
  - id: RuleTypes_PutById
    intent: Replace a rule type
    question: How do I overwrite a rule type record in full?
  - id: RuleTypes_DeleteById
    intent: Delete a rule type
    question: How do I permanently delete one rule type?
  - id: RuleTypes_PatchById
    intent: Rename a rule type
    question: Can I change just the name of an existing rule type?
  - id: RuleTypes_Default
    intent: Get default values for a new rule type
    question: What defaults does a new rule type start with?
  - id: RuleTypes_DeleteRoute
    intent: Bulk delete rule types
    question: Can I delete several rule types at once by ID?
  phrasing_ops: 10
  slug: optimizely-rule-types-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Rules
  name: Optimizely Rules API
  phrasing_intents:
  - id: fetch_holdouts_by_rule_key
    intent: List holdouts applied to a rule
    question: Which holdouts are excluding traffic from a given rule in an environment?
  - id: fetch_rule
    intent: Get a flag's rule in an environment
    question: How do I see the configuration of one rule on a feature flag in production?
  - id: list_all_rules_in_project
    intent: List rules across a project
    question: How can I list every rule in my Optimizely project?
  - id: fetch_rule_by_experiment_id
    intent: Find the rule behind an experiment id
    question: Which rule corresponds to a given experiment id?
  phrasing_ops: 4
  slug: optimizely-rules-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Salespersons API from Optimizely — 7 operation(s) for salespersons.
  name: Optimizely Salespersons API
  phrasing_intents:
  - id: Salespersons_Get
    intent: List salespersons
    question: Who are all the sales reps configured in my Optimizely commerce admin?
  - id: Salespersons_Post
    intent: Create a salesperson
    question: How do I add a new sales rep with their number, email and phone?
  - id: Salespersons_GetById
    intent: Get one salesperson
    question: What contact details are on file for a specific sales rep?
  - id: Salespersons_PutById
    intent: Replace a salesperson record
    question: How do I overwrite a sales rep's entire record in one request?
  - id: Salespersons_DeleteById
    intent: Delete a salesperson
    question: How do I remove a single sales rep by ID?
  - id: Salespersons_PatchById
    intent: Partially update a salesperson
    question: Can I change just a sales rep's phone number or title?
  - id: Salespersons_Default
    intent: Get the default salesperson template
    question: What default values does a new salesperson record start with?
  - id: Salespersons_DeleteRoute
    intent: Bulk delete salespersons
    question: How do I delete several sales reps in one call?
  phrasing_ops: 11
  slug: optimizely-salespersons-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Save API from Optimizely — 1 operation(s) for save.
  name: Optimizely Save API
  phrasing_intents:
  - id: save
    intent: Save a user's bucketing profile
    question: How do I persist which variations a user was bucketed into with Optimizely Agent?
  phrasing_ops: 1
  slug: optimizely-save-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Scheduled Change of a flag in an environment
  name: Optimizely Scheduled Change API
  phrasing_intents:
  - id: delete_scheduled_change
    intent: Delete a flag's scheduled change
    question: How do I cancel a scheduled change on a feature flag?
  - id: update_scheduled_change
    intent: Update a flag's scheduled change
    question: How can I reschedule a planned change to a feature flag?
  phrasing_ops: 2
  slug: optimizely-scheduled-change-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Scheduled Change of a flag
  name: Optimizely Scheduled Changes API
  phrasing_intents:
  - id: list_scheduled_changes
    intent: List a feature flag's scheduled changes
    question: What changes are scheduled for my feature flag, and when do they run?
  - id: create_scheduled_change
    intent: Schedule a change to a feature flag
    question: How do I schedule a feature flag to turn on at a specific time?
  phrasing_ops: 2
  slug: optimizely-scheduled-changes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Get information about scheduled jobs
  name: Optimizely Scheduled jobs API
  phrasing_intents:
  - id: selectAllConfiguredJobs
    intent: List configured scheduled jobs for a client
    question: Which scheduled jobs are configured on my client account and what triggers them?
  - id: selectAllRunningJobs
    intent: List scheduled jobs running right now
    question: What scheduled jobs are running at the moment on my client account?
  - id: list_scheduled_jobs
    intent: List my account's experiment scheduled jobs
    question: What scheduled jobs belong to my Optimizely experimentation account?
  - id: create_scheduled_job
    intent: Create a scheduled job for experiments
    question: How do I schedule a recurring job for the experiments in a project?
  - id: delete_scheduled_job
    intent: Archive a scheduled job
    question: How do I archive a scheduled job I no longer need?
  - id: get_scheduled_job
    intent: Get one scheduled job
    question: How do I look up the frequency and targets of a single scheduled job?
  - id: update_scheduled_job
    intent: Update a scheduled job
    question: How do I change how often a scheduled job runs?
  phrasing_ops: 7
  slug: optimizely-scheduled-jobs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search API from Optimizely — 2 operation(s) for search.
  name: Optimizely Search API
  phrasing_intents:
  - id: Search_Get
    intent: Look up a storefront search redirect
    question: Does a storefront search term redirect shoppers to a specific page?
  - id: get_search_results
    intent: Search entities in my experimentation account
    question: How do I find experiments, flags or campaigns in my account by name?
  phrasing_ops: 2
  slug: optimizely-search-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Boost Analyzers API from Optimizely — 1 operation(s) for search boost analyzers.
  name: Optimizely Search Boost Analyzers API
  phrasing_intents:
  - id: SearchBoostAnalyzers_Get
    intent: List search boost analyzers
    question: Which analyzers can I use when boosting product search results?
  phrasing_ops: 1
  slug: optimizely-search-boost-analyzers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Boosts API from Optimizely — 5 operation(s) for search boosts.
  name: Optimizely Search Boosts API
  phrasing_intents:
  - id: SearchBoosts_Get
    intent: List search boost rules
    question: Which search boosts are configured for my Optimizely Configured Commerce storefront?
  - id: SearchBoosts_Post
    intent: Create a search boost
    question: How do I boost certain results for a search query?
  - id: SearchBoosts_GetById
    intent: Get one search boost
    question: How do I look up a single search boost's query and value by ID?
  - id: SearchBoosts_PutById
    intent: Replace a search boost
    question: Can I overwrite a search boost with a completely new rule?
  - id: SearchBoosts_DeleteById
    intent: Delete a search boost
    question: How do I remove one search boost by its ID?
  - id: SearchBoosts_PatchById
    intent: Update a search boost
    question: Can I change just the boost value on an existing rule?
  - id: SearchBoosts_Default
    intent: Get default values for a search boost
    question: What defaults does the admin pre-fill for a new search boost?
  - id: SearchBoosts_DeleteRoute
    intent: Bulk delete search boosts
    question: How do I delete several search boosts in one request?
  phrasing_ops: 9
  slug: optimizely-search-boosts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Stopwords API from Optimizely — 5 operation(s) for search stopwords.
  name: Optimizely Search Stopwords API
  phrasing_intents:
  - id: SearchStopwords_Get
    intent: List search stopwords
    question: Which words does the storefront search ignore as stopwords?
  - id: SearchStopwords_Post
    intent: Add a search stopword
    question: How do I make site search ignore a word like 'the' or 'and'?
  - id: SearchStopwords_GetById
    intent: Get one search stopword
    question: Where do I look up a single stopword record by id?
  - id: SearchStopwords_PutById
    intent: Replace a search stopword
    question: How do I fully overwrite a stopword record?
  - id: SearchStopwords_DeleteById
    intent: Delete a search stopword
    question: Can I let search match a word again by deleting its stopword?
  - id: SearchStopwords_PatchById
    intent: Update a search stopword
    question: Can I change the language of an existing stopword without replacing it?
  - id: SearchStopwords_Default
    intent: Call the Default function on search stopwords
    question: What does the Default function on SearchStopwords return?
  - id: SearchStopwords_DeleteRoute
    intent: Bulk delete search stopwords
    question: Can I remove many stopwords at once by id?
  phrasing_ops: 9
  slug: optimizely-search-stopwords-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Synonyms API from Optimizely — 5 operation(s) for search synonyms.
  name: Optimizely Search Synonyms API
  phrasing_intents:
  - id: SearchSynonyms_Get
    intent: List catalog search synonyms
    question: Which search synonyms are configured for the storefront catalog?
  - id: SearchSynonyms_Post
    intent: Add a catalog search synonym
    question: How do I make product search treat two words as the same?
  - id: SearchSynonyms_GetById
    intent: Get one catalog search synonym
    question: Is there a call to read a single search synonym entry?
  - id: SearchSynonyms_PutById
    intent: Replace a catalog search synonym
    question: What's the call to overwrite a search synonym entry in full?
  - id: SearchSynonyms_DeleteById
    intent: Delete a catalog search synonym
    question: How do I remove one search synonym so words stop matching?
  - id: SearchSynonyms_PatchById
    intent: Update a catalog search synonym
    question: How do I make an existing synonym one-way only?
  - id: SearchSynonyms_Default
    intent: Get the default search synonym template
    question: What does a default search synonym record contain?
  - id: SearchSynonyms_DeleteRoute
    intent: Bulk delete catalog search synonyms
    question: Can I remove many search synonyms at once?
  phrasing_ops: 9
  slug: optimizely-search-synonyms-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Search Term Redirects API from Optimizely — 7 operation(s) for search term redirects.
  name: Optimizely Search Term Redirects API
  phrasing_intents:
  - id: SearchTermRedirects_Get
    intent: List search term redirects
    question: Which search terms currently redirect shoppers to another page?
  - id: SearchTermRedirects_Post
    intent: Redirect a search term to a page
    question: How do I send shoppers who search a certain word straight to a specific page?
  - id: SearchTermRedirects_GetById
    intent: Get one search term redirect
    question: How do I look up a single search redirect by id?
  - id: SearchTermRedirects_PutById
    intent: Replace a search term redirect
    question: Can I fully replace an existing search redirect's term and target?
  - id: SearchTermRedirects_DeleteById
    intent: Delete a single search term redirect
    question: How do I stop one search term from redirecting?
  - id: SearchTermRedirects_PatchById
    intent: Change where a search term redirects
    question: Can I point an existing search redirect at a new URL?
  - id: SearchTermRedirects_Default
    intent: Get default values for a new search redirect
    question: What defaults does a new search term redirect start with?
  - id: SearchTermRedirects_Archive
    intent: Archive search redirects via the OData action
    question: How do I archive search redirects with the OData Default.archive action?
  phrasing_ops: 11
  slug: optimizely-search-term-redirects-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Section management operations
  name: Optimizely Sections API
  phrasing_intents:
  - id: sectionGetMany
    intent: Get a content section
    question: Can I fetch the details of a content section by its id?
  - id: sectionUpdate
    intent: Update a content section
    question: How do I rename a content section or change its description?
  - id: sectionContentList
    intent: List content items in a content section
    question: Which content items are assigned to a content section?
  - id: get_experiment_sections
    intent: List sections in a multivariate test
    question: Which sections make up my multivariate test?
  - id: create_section
    intent: Add a section to a multivariate test
    question: How do I add a new section with its own variations to a multivariate test?
  - id: delete_section
    intent: Archive a multivariate test section
    question: How do I archive a section I no longer want in a multivariate test?
  - id: get_section
    intent: Get a section of a multivariate test
    question: Can I read the metadata for one section of a multivariate test?
  - id: update_section
    intent: Update a multivariate test section
    question: Can I rename a multivariate test section or change its variations?
  phrasing_ops: 8
  slug: optimizely-sections-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Send Odp Event API from Optimizely — 1 operation(s) for send odp event.
  name: Optimizely Send Odp Event API
  phrasing_intents:
  - id: sendOdpEvent
    intent: Send an event to Optimizely Data Platform
    question: How do I send a custom event to Optimizely Data Platform?
  phrasing_ops: 1
  slug: optimizely-send-odp-event-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Sessions API from Optimizely — 3 operation(s) for sessions.
  name: Optimizely Sessions API
  phrasing_intents:
  - id: SessionsV1_GetAsync
    intent: Get the current shopper session
    question: Is the current shopper signed in, and as which user?
  - id: SessionsV1_DeleteAsync
    intent: Sign out of the current session
    question: How do I log a shopper out of the storefront?
  - id: SessionsV1_PatchAsync
    intent: Update the current shopper session
    question: How do I switch the active bill-to and ship-to on my current session?
  - id: SessionsV1_PostAsync
    intent: Sign in and start a shopper session
    question: How do I sign a user in to the commerce storefront through the API?
  - id: SessionsV1_DeleteAuthenticationAsync
    intent: Remove authentication from the current session
    question: Can I drop the signed-in identity but keep the session itself?
  phrasing_ops: 5
  slug: optimizely-sessions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Settings API from Optimizely — 9 operation(s) for settings.
  name: Optimizely Settings API
  phrasing_intents:
  - id: WebsitesV1_GetSettingsAsync
    intent: Get storefront website settings
    question: What website-level settings is my commerce storefront running with?
  - id: QuotesV1_GetSettingsAsync
    intent: Get quote settings
    question: What are the request-for-quote settings on my storefront?
  - id: CartsV1_GetSettingsAsync
    intent: Get cart settings
    question: What cart and checkout settings are enabled on the storefront?
  - id: AccountsV1_GetSettingsAsync
    intent: Get account settings
    question: What user account and sign-up settings does the storefront use?
  - id: WishListsV1_GetSettingsAsync
    intent: Get wish list settings
    question: How are wish lists configured on my storefront?
  - id: SettingsV1_GetAsync
    intent: Get all storefront settings
    question: Can I pull every storefront settings group in one request?
  - id: ProductsV1_GetSettingsAsync
    intent: Get product settings
    question: What product catalog display settings does the storefront have?
  - id: MobileAppV1_GetSettingsAsync
    intent: Get mobile app settings
    question: What settings does the commerce mobile app pull from the server?
  phrasing_ops: 10
  slug: optimizely-settings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Charges API from Optimizely — 5 operation(s) for ship charges.
  name: Optimizely Ship Charges API
  phrasing_intents:
  - id: ShipCharges_Get
    intent: List shipping charges
    question: What shipping charges are configured for my carriers and ship methods?
  - id: ShipCharges_Post
    intent: Create a shipping charge
    question: How do I add a flat shipping charge to a carrier's ship method?
  - id: ShipCharges_GetById
    intent: Get a shipping charge by id
    question: How much is a particular ship charge and is it enabled?
  - id: ShipCharges_PutById
    intent: Replace a shipping charge
    question: How do I overwrite every field of a ship charge at once?
  - id: ShipCharges_DeleteById
    intent: Delete a shipping charge
    question: Can I remove one ship charge by its id?
  - id: ShipCharges_PatchById
    intent: Change the amount or status of a ship charge
    question: How do I raise the price of an existing ship charge?
  - id: ShipCharges_Default
    intent: Get a blank ship charge template
    question: What default values does a new ship charge start with?
  - id: ShipCharges_DeleteRoute
    intent: Bulk delete shipping charges
    question: Can I delete several ship charges in one request?
  phrasing_ops: 9
  slug: optimizely-ship-charges-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Rates API from Optimizely — 5 operation(s) for ship rates.
  name: Optimizely Ship Rates API
  phrasing_intents:
  - id: ShipRates_Get
    intent: List shipping rates
    question: What shipping charges are set up by order amount?
  - id: ShipRates_Post
    intent: Create a shipping rate
    question: How do I charge a flat shipping fee above a certain order amount?
  - id: ShipRates_GetById
    intent: Get a shipping rate
    question: Can I look up one ship rate by its ID?
  - id: ShipRates_PutById
    intent: Replace a shipping rate
    question: Can I overwrite a ship rate record completely?
  - id: ShipRates_DeleteById
    intent: Delete a shipping rate
    question: How do I remove one shipping rate tier?
  - id: ShipRates_PatchById
    intent: Change a shipping rate's charge
    question: Can I change only the charge amount of a ship rate?
  - id: ShipRates_Default
    intent: Get default values for a shipping rate
    question: What defaults are pre-filled for a new ship rate?
  - id: ShipRates_DeleteRoute
    intent: Delete several shipping rates
    question: Can I bulk delete ship rates in one request?
  phrasing_ops: 9
  slug: optimizely-ship-rates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Rules API from Optimizely — 5 operation(s) for ship rules.
  name: Optimizely Ship Rules API
  phrasing_intents:
  - id: ShipRules_Get
    intent: List shipping rules
    question: How do I see all the rules that decide which carriers and ship methods apply to an order?
  - id: ShipRules_Post
    intent: Create a shipping rule
    question: How do I add a rule that restricts a ship method by postal code range or order amount?
  - id: ShipRules_GetById
    intent: Get one shipping rule
    question: How do I look up the conditions on a single ship rule?
  - id: ShipRules_PutById
    intent: Replace a shipping rule
    question: How do I overwrite a whole ship rule definition?
  - id: ShipRules_DeleteById
    intent: Delete a shipping rule
    question: How do I remove one shipping rule?
  - id: ShipRules_PatchById
    intent: Adjust limits on a shipping rule
    question: How do I change the minimum or maximum order amount on a ship rule?
  - id: ShipRules_Default
    intent: Get a blank shipping rule template
    question: What default values does a new ship rule start with?
  - id: ShipRules_DeleteRoute
    intent: Bulk delete shipping rules
    question: How do I delete several ship rules at once?
  phrasing_ops: 9
  slug: optimizely-ship-rules-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship To Address Fields API from Optimizely — 5 operation(s) for ship to address fields.
  name: Optimizely Ship To Address Fields API
  phrasing_intents:
  - id: ShipToAddressFields_Get
    intent: List ship-to address fields
    question: Which fields appear on the shipping address form at checkout?
  - id: ShipToAddressFields_Post
    intent: Add a ship-to address field
    question: How do I add a new field to the shipping address form?
  - id: ShipToAddressFields_GetById
    intent: Get a ship-to address field
    question: How do I read the settings of one shipping address field?
  - id: ShipToAddressFields_PutById
    intent: Replace a ship-to address field
    question: How do I overwrite a shipping address field definition completely?
  - id: ShipToAddressFields_DeleteById
    intent: Delete a ship-to address field
    question: How do I remove a field from the shipping address form?
  - id: ShipToAddressFields_PatchById
    intent: Update a ship-to address field
    question: How do I hide a shipping address field without deleting it?
  - id: ShipToAddressFields_Default
    intent: Get the default ship-to field template
    question: What are the default settings for a new shipping address field?
  - id: ShipToAddressFields_DeleteRoute
    intent: Bulk delete ship-to address fields
    question: How do I remove several shipping address fields at once?
  phrasing_ops: 9
  slug: optimizely-ship-to-address-fields-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Ship Vias API from Optimizely — 11 operation(s) for ship vias.
  name: Optimizely Ship Vias API
  phrasing_intents:
  - id: ShipVias_Get
    intent: List shipping methods
    question: Which ship vias (shipping methods) are configured in my commerce store?
  - id: ShipVias_Post
    intent: Create a shipping method
    question: How do I add a new shipping method with its ERP ship code?
  - id: ShipVias_GetById
    intent: Get a shipping method
    question: What fees and carrier does one ship via use?
  - id: ShipVias_PutById
    intent: Replace a shipping method
    question: How do I overwrite a ship via with a completely new definition?
  - id: ShipVias_DeleteById
    intent: Delete a shipping method
    question: Can I permanently delete one ship via by its ID?
  - id: ShipVias_PatchById
    intent: Update a shipping method
    question: How do I disable a single shipping method without resending all of it?
  - id: ShipVias_Default
    intent: Get a blank shipping method template
    question: What default values does a new ship via start with?
  - id: ShipVias_Archive
    intent: Archive shipping methods
    question: Can I archive shipping methods instead of deleting them?
  phrasing_ops: 15
  slug: optimizely-ship-vias-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Shipment Package Lines API from Optimizely — 5 operation(s) for shipment package lines.
  name: Optimizely Shipment Package Lines API
  phrasing_intents:
  - id: ShipmentPackageLines_Get
    intent: List shipment package lines
    question: Which products were packed in each shipment package?
  - id: ShipmentPackageLines_Post
    intent: Add a product line to a shipment package
    question: How do I record what was packed in a shipment package?
  - id: ShipmentPackageLines_GetById
    intent: Get a shipment package line
    question: How many units of a product shipped on a given package line?
  - id: ShipmentPackageLines_PutById
    intent: Replace a shipment package line
    question: How do I overwrite every field of a shipment package line?
  - id: ShipmentPackageLines_DeleteById
    intent: Delete a shipment package line
    question: How do I remove one line from a shipment package?
  - id: ShipmentPackageLines_PatchById
    intent: Correct the shipped quantity on a package line
    question: How do I fix the quantity shipped on an existing package line?
  - id: ShipmentPackageLines_Default
    intent: Get defaults for a new shipment package line
    question: What defaults does a new shipment package line start with?
  - id: ShipmentPackageLines_DeleteRoute
    intent: Delete several shipment package lines
    question: How do I bulk delete shipment package lines?
  phrasing_ops: 9
  slug: optimizely-shipment-package-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Shipment Packages API from Optimizely — 6 operation(s) for shipment packages.
  name: Optimizely Shipment Packages API
  phrasing_intents:
  - id: ShipmentPackages_Get
    intent: List shipment packages
    question: Which packages have been recorded against my shipments?
  - id: ShipmentPackages_Post
    intent: Add a package to a shipment
    question: How do I record a new package with its carrier and tracking number?
  - id: ShipmentPackages_GetById
    intent: Get a shipment package
    question: What tracking number and carrier does a specific package have?
  - id: ShipmentPackages_PutById
    intent: Replace a shipment package
    question: How do I overwrite a shipment package record entirely?
  - id: ShipmentPackages_DeleteById
    intent: Delete a shipment package
    question: Can I delete one package from a shipment by its ID?
  - id: ShipmentPackages_PatchById
    intent: Update a shipment package
    question: How do I correct the tracking number on an existing package?
  - id: ShipmentPackages_Default
    intent: Get a blank shipment package template
    question: What default values does a new shipment package have?
  - id: ShipmentPackages_DeleteRoute
    intent: Bulk delete shipment packages
    question: Can I delete several shipment packages at once?
  phrasing_ops: 10
  slug: optimizely-shipment-packages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Shipments API from Optimizely — 6 operation(s) for shipments.
  name: Optimizely Shipments API
  phrasing_intents:
  - id: Shipments_Get
    intent: List order shipments
    question: Which shipments have gone out for my commerce orders?
  - id: Shipments_Post
    intent: Record a shipment for an order
    question: How do I record a new shipment against an order?
  - id: Shipments_GetById
    intent: Get a shipment by ID
    question: When did a specific shipment go out and was the ASN sent?
  - id: Shipments_PutById
    intent: Replace a shipment record
    question: Can I overwrite an entire shipment record in one request?
  - id: Shipments_DeleteById
    intent: Delete a shipment by ID
    question: How do I delete a shipment record entered in error?
  - id: Shipments_PatchById
    intent: Update a shipment
    question: How do I mark the shipment email or ASN as sent on an existing shipment?
  - id: Shipments_Default
    intent: Get a default shipment template
    question: What default values does a new shipment start with?
  - id: Shipments_DeleteRoute
    intent: Bulk delete shipments
    question: How do I delete several shipment records at once?
  phrasing_ops: 10
  slug: optimizely-shipments-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Site API from Optimizely — 2 operation(s) for site.
  name: Optimizely Site API
  phrasing_intents:
  - id: Site_List
    intent: List CMS sites
    question: Which sites are configured in my Optimizely CMS instance?
  - id: Site_Get
    intent: Get a CMS site by ID
    question: Can I fetch the settings of one site by its identifier?
  phrasing_ops: 2
  slug: optimizely-site-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Specifications API from Optimizely — 7 operation(s) for specifications.
  name: Optimizely Specifications API
  phrasing_intents:
  - id: Specifications_Get
    intent: List product specifications
    question: How do I list all product specifications in the commerce admin?
  - id: Specifications_Post
    intent: Create a product specification
    question: How do I add a new specification like dimensions or material to a product?
  - id: Specifications_GetById
    intent: Get a product specification
    question: How do I look up one specification by its ID?
  - id: Specifications_PutById
    intent: Replace a product specification
    question: How do I overwrite an entire specification record?
  - id: Specifications_DeleteById
    intent: Delete a product specification
    question: How do I permanently delete a single specification?
  - id: Specifications_PatchById
    intent: Update a product specification
    question: How do I change only the value of an existing specification?
  - id: Specifications_Default
    intent: Get a default specification template
    question: What default values does a new specification start with?
  - id: Specifications_Archive
    intent: Archive specifications via the archive action
    question: How do I archive several specifications using the OData archive action?
  phrasing_ops: 11
  slug: optimizely-specifications-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Spire Logs API from Optimizely — 2 operation(s) for spire logs.
  name: Optimizely Spire Logs API
  phrasing_intents:
  - id: SpireLogs_Get
    intent: List Spire storefront log entries
    question: How do I browse the Spire logs from the commerce admin API?
  - id: SpireLogs_GetById
    intent: Get one Spire log entry
    question: How do I open a single Spire log entry by its ID?
  phrasing_ops: 2
  slug: optimizely-spire-logs-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Spreedly API from Optimizely — 2 operation(s) for spreedly.
  name: Optimizely Spreedly API
  phrasing_intents:
  - id: SpreedlyV1_Get
    intent: Get the Spreedly payment configuration
    question: How do I get the storefront's Spreedly payment settings?
  - id: SpreedlyV1_BnplRedirect
    intent: Handle a buy-now-pay-later redirect
    question: How do I handle the return from a Spreedly buy-now-pay-later checkout?
  phrasing_ops: 2
  slug: optimizely-spreedly-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Spreedly Config API from Optimizely — 1 operation(s) for spreedly config.
  name: Optimizely Spreedly Config API
  phrasing_intents:
  - id: SpreedlyConfig_Get
    intent: Get the Spreedly payment gateway configuration
    question: How is the Spreedly payment integration configured in Commerce admin?
  phrasing_ops: 1
  slug: optimizely-spreedly-config-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Sso Clients API from Optimizely — 2 operation(s) for sso clients.
  name: Optimizely Sso Clients API
  phrasing_intents:
  - id: SsoClients_Get
    intent: List SSO clients
    question: Which SSO clients are registered with my commerce identity server?
  - id: SsoClients_Post
    intent: Register an SSO client
    question: How do I register a new OAuth client for single sign-on?
  - id: SsoClients_GetByClientid
    intent: Get an SSO client
    question: What flow, scopes and token lifetimes does one SSO client use?
  - id: SsoClients_DeleteByClientid
    intent: Delete an SSO client
    question: Can I remove an SSO client so it can no longer sign in?
  - id: SsoClients_PatchByClientid
    intent: Update an SSO client
    question: How do I disable an existing SSO client?
  phrasing_ops: 5
  slug: optimizely-sso-clients-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The State Tax Exemptions API from Optimizely — 5 operation(s) for state tax exemptions.
  name: Optimizely State Tax Exemptions API
  phrasing_intents:
  - id: StateTaxExemptions_Get
    intent: List state tax exemptions
    question: Which tax exemptions apply in which states?
  - id: StateTaxExemptions_Post
    intent: Apply a tax exemption to a state
    question: How do I make a tax exemption valid in a particular state?
  - id: StateTaxExemptions_GetById
    intent: Get a state tax exemption
    question: Can I look up one state tax exemption link by ID?
  - id: StateTaxExemptions_PutById
    intent: Replace a state tax exemption
    question: How do I overwrite a state tax exemption record completely?
  - id: StateTaxExemptions_DeleteById
    intent: Remove a state tax exemption
    question: How do I stop a tax exemption applying in a state?
  - id: StateTaxExemptions_PatchById
    intent: Change a state tax exemption
    question: Can I move an existing exemption record to another state?
  - id: StateTaxExemptions_Default
    intent: Get default values for a new state tax exemption
    question: What defaults does a new state tax exemption start with?
  - id: StateTaxExemptions_DeleteRoute
    intent: Bulk remove state tax exemptions
    question: Can I delete many state tax exemptions in one call?
  phrasing_ops: 9
  slug: optimizely-state-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The States API from Optimizely — 9 operation(s) for states.
  name: Optimizely States API
  phrasing_intents:
  - id: States_Get
    intent: List states and provinces
    question: Which states and provinces are set up in the Optimizely Configured Commerce admin?
  - id: States_Post
    intent: Add a state with its tax settings
    question: What tax codes and descriptions do I need to add a new state?
  - id: States_GetById
    intent: Get one state by ID
    question: How do I look up a single state's tax configuration by its ID?
  - id: States_PutById
    intent: Replace a state record entirely
    question: Can I overwrite a state with a complete new set of tax values?
  - id: States_DeleteById
    intent: Delete a single state
    question: How do I remove one state from the admin by its ID?
  - id: States_PatchById
    intent: Update selected fields on a state
    question: Can I change just a state's tax rate without resending everything?
  - id: States_Default
    intent: Get default values for a new state
    question: What default values does the admin pre-fill for a state before I create one?
  - id: States_Archive
    intent: Archive states with the archive action
    question: Can I archive several states at once with the OData archive action?
  phrasing_ops: 13
  slug: optimizely-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Structured Contents API from Optimizely — 11 operation(s) for structured contents.
  name: Optimizely Structured Contents API
  phrasing_intents:
  - id: listSCContentTypes
    intent: List structured content types
    question: Which structured content types are defined in my Optimizely CMP?
  - id: createSCContentType
    intent: Create a structured content type
    question: How do I define a new structured content type with its own field definitions?
  - id: getSCContentType
    intent: Get a structured content type
    question: What does a single structured content type look like when I fetch it by ID?
  - id: updateSCContentType
    intent: Update a structured content type's details
    question: Can I rename or change the details of an existing structured content type?
  - id: listSCContentTypeVersions
    intent: List versions of a content type
    question: What versions exist for a given structured content type?
  - id: createSCContentTypeVersion
    intent: Add a new version to a content type
    question: How do I publish a new version of a content type with changed field definitions?
  - id: getSCContentTypeVersion
    intent: Get one version of a content type
    question: How can I inspect the field definitions of one specific content type version?
  - id: migrateSCContent
    intent: Migrate a content item to a content type version
    question: How do I move a single piece of structured content onto a newer content type version?
  phrasing_ops: 17
  slug: optimizely-structured-contents-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Classes API from Optimizely — 8 operation(s) for style classes.
  name: Optimizely Style Classes API
  phrasing_intents:
  - id: StyleClasses_Get
    intent: List product style classes
    question: Which style classes are defined in my commerce catalog?
  - id: StyleClasses_Post
    intent: Create a style class
    question: How do I create a new style class for product variants?
  - id: StyleClasses_GetById
    intent: Get a style class by ID
    question: What are the details of one style class by its ID?
  - id: StyleClasses_PutById
    intent: Replace a style class
    question: Can I overwrite a whole style class record in one request?
  - id: StyleClasses_DeleteById
    intent: Delete a style class by ID
    question: How do I permanently delete one style class?
  - id: StyleClasses_PatchById
    intent: Update a style class
    question: How do I rename an existing style class?
  - id: StyleClasses_Default
    intent: Get a default style class template
    question: What default values does a new style class start with?
  - id: StyleClasses_Archive
    intent: Archive style classes with the archive action
    question: Can I archive style classes using the OData archive action instead of deleting them?
  phrasing_ops: 12
  slug: optimizely-style-classes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Trait Value Products API from Optimizely — 5 operation(s) for style trait value products.
  name: Optimizely Style Trait Value Products API
  phrasing_intents:
  - id: StyleTraitValueProducts_Get
    intent: List product style trait value links
    question: Which products are linked to style trait values like a color or size?
  - id: StyleTraitValueProducts_Post
    intent: Link a product to a style trait value
    question: How do I tag a product variant with a style trait value such as Red or Large?
  - id: StyleTraitValueProducts_GetById
    intent: Get a product style trait value link
    question: Which product and trait value does a given style link record connect?
  - id: StyleTraitValueProducts_PutById
    intent: Replace a product style trait value link
    question: How do I overwrite a style trait value link record in full?
  - id: StyleTraitValueProducts_DeleteById
    intent: Unlink a product from a style trait value
    question: How do I remove a style trait value from a product variant?
  - id: StyleTraitValueProducts_PatchById
    intent: Update a product style trait value link
    question: Can I switch a variant to a different trait value without recreating the link?
  - id: StyleTraitValueProducts_Default
    intent: Get a blank style trait link template
    question: What default values does a new style trait value product link start with?
  - id: StyleTraitValueProducts_DeleteRoute
    intent: Bulk unlink products from style trait values
    question: How do I delete many style trait value links at once?
  phrasing_ops: 9
  slug: optimizely-style-trait-value-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Trait Values API from Optimizely — 6 operation(s) for style trait values.
  name: Optimizely Style Trait Values API
  phrasing_intents:
  - id: StyleTraitValues_Get
    intent: List style trait values
    question: How can I see all the style trait values, like each color or size option?
  - id: StyleTraitValues_Post
    intent: Create a style trait value
    question: How do I add a new option such as a color to a style trait?
  - id: StyleTraitValues_GetById
    intent: Get one style trait value
    question: How can I look up a single style trait value by id?
  - id: StyleTraitValues_PutById
    intent: Replace a style trait value
    question: How do I overwrite all fields of a style trait value?
  - id: StyleTraitValues_DeleteById
    intent: Delete one style trait value
    question: How do I remove a single style trait value?
  - id: StyleTraitValues_PatchById
    intent: Update fields of a style trait value
    question: How can I change the sort order of one style trait value?
  - id: StyleTraitValues_Default
    intent: Get defaults for a new style trait value
    question: What default values does a new style trait value start with?
  - id: StyleTraitValues_DeleteRoute
    intent: Bulk delete style trait values
    question: How do I delete several style trait values at once?
  phrasing_ops: 10
  slug: optimizely-style-trait-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Style Traits API from Optimizely — 6 operation(s) for style traits.
  name: Optimizely Style Traits API
  phrasing_intents:
  - id: StyleTraits_Get
    intent: List product style traits
    question: Which style traits like color or size are defined for my product variants?
  - id: StyleTraits_Post
    intent: Create a style trait
    question: How do I add a new style trait such as Color to a style class?
  - id: StyleTraits_GetById
    intent: Get one style trait
    question: What are the display settings of a specific style trait?
  - id: StyleTraits_PutById
    intent: Replace a style trait record
    question: How do I overwrite every field of a style trait at once?
  - id: StyleTraits_DeleteById
    intent: Delete a style trait
    question: How do I remove a single style trait?
  - id: StyleTraits_PatchById
    intent: Partially update a style trait
    question: Can I change only the sort order of a style trait?
  - id: StyleTraits_Default
    intent: Get the default style trait template
    question: What default values does a new style trait start with?
  - id: StyleTraits_DeleteRoute
    intent: Bulk delete style traits
    question: How do I delete several style traits in one request?
  phrasing_ops: 10
  slug: optimizely-style-traits-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage information about Subject Access Requests (includes GDPR)
  name: Optimizely Subject Access Requests API
  phrasing_intents:
  - id: list_sar_requests_by_team
    intent: List subject access requests by data source and status
    question: Which privacy requests are still pending for a given data source?
  - id: update_sar_request
    intent: Update a subject access request via PATCH
    question: How do I patch the status of a subject access request?
  - id: update_sar_request_by_post
    intent: Update a subject access request via POST
    question: Is there a POST form of updating a subject access request's status?
  - id: list_sar_requests_by_account
    intent: List subject access requests from my account
    question: What GDPR access or deletion requests has my account submitted to Optimizely?
  - id: create_sar_request
    intent: Submit a data access or deletion request
    question: How do I request deletion of all data tied to an end user's email?
  - id: get_sar_request
    intent: Check the status of a subject access request
    question: Has my privacy request finished processing yet?
  phrasing_ops: 6
  slug: optimizely-subject-access-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Subscription Lines API from Optimizely — 5 operation(s) for subscription lines.
  name: Optimizely Subscription Lines API
  phrasing_intents:
  - id: SubscriptionLines_Get
    intent: List subscription lines
    question: Which products are on my customers' recurring subscriptions?
  - id: SubscriptionLines_Post
    intent: Add a product to a subscription
    question: How do I add a product line to a recurring subscription?
  - id: SubscriptionLines_GetById
    intent: Get a subscription line
    question: What product, quantity and price are on a specific subscription line?
  - id: SubscriptionLines_PutById
    intent: Replace a subscription line
    question: How do I overwrite a subscription line record completely?
  - id: SubscriptionLines_DeleteById
    intent: Delete a subscription line
    question: Can I remove one product line from a subscription?
  - id: SubscriptionLines_PatchById
    intent: Update a subscription line
    question: How do I change the quantity on an existing subscription line?
  - id: SubscriptionLines_Default
    intent: Get a blank subscription line template
    question: What default values does a new subscription line start with?
  - id: SubscriptionLines_DeleteRoute
    intent: Bulk delete subscription lines
    question: Can I delete several subscription lines at once?
  phrasing_ops: 9
  slug: optimizely-subscription-lines-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Subscription Products API from Optimizely — 5 operation(s) for subscription products.
  name: Optimizely Subscription Products API
  phrasing_intents:
  - id: SubscriptionProducts_Get
    intent: List subscription products
    question: Which products are bundled into my subscription products?
  - id: SubscriptionProducts_Post
    intent: Add a product to a subscription
    question: How do I add a product to a subscription parent product?
  - id: SubscriptionProducts_GetById
    intent: Get a subscription product by ID
    question: What product and quantity does one subscription product record hold?
  - id: SubscriptionProducts_PutById
    intent: Replace a subscription product
    question: Can I overwrite a whole subscription product record at once?
  - id: SubscriptionProducts_DeleteById
    intent: Remove a product from a subscription
    question: How do I take a product out of a subscription?
  - id: SubscriptionProducts_PatchById
    intent: Update a subscription product
    question: How do I change the quantity of a product inside a subscription?
  - id: SubscriptionProducts_Default
    intent: Get a default subscription product template
    question: What default values does a new subscription product start with?
  - id: SubscriptionProducts_DeleteRoute
    intent: Bulk delete subscription products
    question: How do I delete several subscription products at once?
  phrasing_ops: 9
  slug: optimizely-subscription-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Subscriptions API from Optimizely — 9 operation(s) for subscriptions.
  name: Optimizely Subscriptions API
  phrasing_intents:
  - id: Subscriptions_Get
    intent: List product subscriptions
    question: Which customers have recurring product subscriptions set up?
  - id: Subscriptions_Post
    intent: Create a recurring product subscription
    question: How do I set up a monthly repeat order for a customer?
  - id: Subscriptions_GetById
    intent: Get a subscription
    question: What cycle and ship-to does a given subscription use?
  - id: Subscriptions_PutById
    intent: Replace a subscription entirely
    question: How do I overwrite every field on a subscription record?
  - id: Subscriptions_DeleteById
    intent: Delete a subscription
    question: How do I permanently remove one subscription?
  - id: Subscriptions_PatchById
    intent: Update some fields of a subscription
    question: How do I change when a subscription deactivates?
  - id: Subscriptions_Default
    intent: Get default values for a new subscription
    question: What defaults does a new subscription start with?
  - id: Subscriptions_Archive
    intent: Archive subscriptions via the archive action
    question: How do I archive subscriptions using the POST archive action?
  phrasing_ops: 13
  slug: optimizely-subscriptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Files API from Optimizely — 2 operation(s) for system files.
  name: Optimizely System Files API
  phrasing_intents:
  - id: SystemFilesV1_GetAsync
    intent: Browse system files at a path
    question: How do I see what system files are stored under a folder path in the commerce admin?
  - id: SystemFilesV1_ContentAsync
    intent: Send file content to a system file path
    question: Which endpoint posts file content to a system file location?
  phrasing_ops: 2
  slug: optimizely-system-files-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Folders API from Optimizely — 1 operation(s) for system folders.
  name: Optimizely System Folders API
  phrasing_intents:
  - id: SystemFoldersV1_GetAsync
    intent: List system folders
    question: Which system folders exist in the commerce admin?
  phrasing_ops: 1
  slug: optimizely-system-folders-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System List Values API from Optimizely — 7 operation(s) for system list values.
  name: Optimizely System List Values API
  phrasing_intents:
  - id: SystemListValues_Get
    intent: List system list values
    question: How do I see all the dropdown values stored in system lists in Optimizely Configured Commerce?
  - id: SystemListValues_Post
    intent: Add a value to a system list
    question: What's needed to add a new option to a system list?
  - id: SystemListValues_GetById
    intent: Get one system list value
    question: How can I look up a single system list value by its ID?
  - id: SystemListValues_PutById
    intent: Replace a system list value
    question: Can I overwrite a system list value with a whole new record?
  - id: SystemListValues_DeleteById
    intent: Delete a system list value
    question: How do I delete one value from a system list?
  - id: SystemListValues_PatchById
    intent: Update part of a system list value
    question: Can I set just the deactivation date on an existing system list value?
  - id: SystemListValues_Default
    intent: Get default values for a system list value
    question: What defaults are pre-filled for a new system list value?
  - id: SystemListValues_Archive
    intent: Archive system list values (OData action)
    question: Can I archive list values with the Default.archive POST action?
  phrasing_ops: 11
  slug: optimizely-system-list-values-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Lists API from Optimizely — 8 operation(s) for system lists.
  name: Optimizely System Lists API
  phrasing_intents:
  - id: SystemLists_Get
    intent: List and filter system lists
    question: How can I see all the system lists that drive dropdowns in my commerce admin?
  - id: SystemLists_Post
    intent: Create a system list
    question: How do I add a new system list of predefined values?
  - id: SystemLists_GetById
    intent: Get one system list by id
    question: How can I look up a single system list by its id?
  - id: SystemLists_PutById
    intent: Replace a system list entirely
    question: How do I overwrite every field of a system list in one call?
  - id: SystemLists_DeleteById
    intent: Delete one system list
    question: How do I remove one system list permanently?
  - id: SystemLists_PatchById
    intent: Update some fields of a system list
    question: How can I change only the description of a system list?
  - id: SystemLists_Default
    intent: Get default values for a new system list
    question: What defaults does a new system list come with?
  - id: SystemLists_Archive
    intent: Archive system lists with the archive action
    question: How do I archive system lists using the archive action?
  phrasing_ops: 12
  slug: optimizely-system-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The System Settings API from Optimizely — 14 operation(s) for system settings.
  name: Optimizely System Settings API
  phrasing_intents:
  - id: SystemSettings_GetList
    intent: List system settings
    question: How do I see every system setting configured in my Optimizely Configured Commerce admin?
  - id: SystemSettings_Post
    intent: Create a system setting
    question: How do I add a new named system setting with a value?
  - id: SystemSettings_GetSingleById
    intent: Get a system setting by its id
    question: What value does the system setting with a given id currently hold?
  - id: SystemSettings_PutById
    intent: Replace a system setting
    question: How do I overwrite an entire system setting record rather than patching one field?
  - id: SystemSettings_DeleteById
    intent: Delete a system setting
    question: How do I remove a single system setting by its id?
  - id: SystemSettings_PatchById
    intent: Update a system setting's value
    question: How do I change the value of an existing system setting?
  - id: SystemSettings_Default
    intent: Get a blank default system setting
    question: What does an empty system setting record look like before I fill it in?
  - id: SystemSettings_SetSettings_1
    intent: Save many settings via the Default.batch action
    question: Can I save a whole set of settings for a website in one OData batch action?
  phrasing_ops: 18
  slug: optimizely-system-settings-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Task Step API from Optimizely — 1 operation(s) for task step.
  name: Optimizely Task Step API
  phrasing_intents:
  - id: updateTaskStep
    intent: Change a task step's due date
    question: How do I reschedule a step within an Optimizely task?
  phrasing_ops: 1
  slug: optimizely-task-step-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Tax Exemptions API from Optimizely — 11 operation(s) for tax exemptions.
  name: Optimizely Tax Exemptions API
  phrasing_intents:
  - id: TaxExemptions_Get
    intent: List and filter tax exemptions
    question: How can I see all the tax exemptions configured in my commerce site?
  - id: TaxExemptions_Post
    intent: Create a tax exemption
    question: How do I set up a new tax exemption with an exempt amount?
  - id: TaxExemptions_GetById
    intent: Get one tax exemption by id
    question: How can I look up the details of a single tax exemption?
  - id: TaxExemptions_PutById
    intent: Replace a tax exemption entirely
    question: How do I overwrite all fields of an existing tax exemption at once?
  - id: TaxExemptions_DeleteById
    intent: Delete one tax exemption
    question: How do I remove a single tax exemption permanently?
  - id: TaxExemptions_PatchById
    intent: Update some fields of a tax exemption
    question: How can I change just the exempt amount on a tax exemption?
  - id: TaxExemptions_Default
    intent: Get default values for a new tax exemption
    question: What defaults does a new tax exemption start with?
  - id: TaxExemptions_Archive
    intent: Archive tax exemptions with the archive action
    question: How do I archive tax exemptions I no longer use via the archive action?
  phrasing_ops: 15
  slug: optimizely-tax-exemptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Team Management API from Optimizely — 2 operation(s) for team management.
  name: Optimizely Team Management API
  phrasing_intents:
  - id: get_teams_accounts__account_id__teams_get
    intent: List teams in an account
    question: What teams have been set up in my Optimizely account?
  - id: create_team_accounts__account_id__teams_post
    intent: Create a team
    question: How do I set up a new team and add people to it?
  - id: delete_team_accounts__account_id__teams__team_id__delete
    intent: Delete a team
    question: How do I remove a team that is no longer needed?
  - id: get_team_info_accounts__account_id__teams__team_id__get
    intent: Get a team's details
    question: Who belongs to a particular team?
  - id: update_team_info_accounts__account_id__teams__team_id__patch
    intent: Update a team or its membership
    question: How do I add or remove people from an existing team?
  phrasing_ops: 5
  slug: optimizely-team-management-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Teams API from Optimizely — 2 operation(s) for teams.
  name: Optimizely Teams API
  phrasing_intents:
  - id: listTeams
    intent: List teams in the CMP
    question: Which teams exist in my Optimizely CMP organization?
  - id: getTeam
    intent: Get one CMP team
    question: How do I look up the details of a single team by its ID?
  phrasing_ops: 2
  slug: optimizely-teams-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Telemetry API from Optimizely — 2 operation(s) for telemetry.
  name: Optimizely Telemetry API
  phrasing_intents:
  - id: TelemetryV1_TrackEvent
    intent: Send a custom telemetry event
    question: How do I record a named usage event from the admin console in telemetry?
  - id: TelemetryV1_ScreenEvent
    intent: Record a screen view in telemetry
    question: How do I log that an admin user viewed a particular screen?
  phrasing_ops: 2
  slug: optimizely-telemetry-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Templates API from Optimizely — 2 operation(s) for templates.
  name: Optimizely Templates API
  phrasing_intents:
  - id: listTemplates
    intent: List templates
    question: What templates are available to start new work from in Optimizely?
  - id: getTemplate
    intent: Get a template by id
    question: What does a specific template contain?
  phrasing_ops: 2
  slug: optimizely-templates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Themes API from Optimizely — 5 operation(s) for themes.
  name: Optimizely Themes API
  phrasing_intents:
  - id: Themes_Get
    intent: List storefront themes
    question: How can I see all the themes available for my storefront?
  - id: Themes_Post
    intent: Create a theme
    question: How do I create a new storefront theme?
  - id: Themes_GetById
    intent: Get one theme by id
    question: How can I look up a single theme by id?
  - id: Themes_PutById
    intent: Replace a theme entirely
    question: How do I overwrite every setting of a theme at once?
  - id: Themes_DeleteById
    intent: Delete one theme
    question: How do I remove a theme I no longer use?
  - id: Themes_PatchById
    intent: Update some fields of a theme
    question: How can I just rename a theme?
  - id: Themes_Default
    intent: Get default values for a new theme
    question: What defaults does a new theme start with?
  - id: Themes_DeleteRoute
    intent: Bulk delete themes
    question: How do I delete several themes at once?
  phrasing_ops: 9
  slug: optimizely-themes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Token Ex Config API from Optimizely — 1 operation(s) for token ex config.
  name: Optimizely Token Ex Config API
  phrasing_intents:
  - id: TokenExConfig_Get
    intent: Get the TokenEx payment tokenization config
    question: What TokenEx configuration does my commerce admin use for card tokenization?
  - id: TokenExConfigV1_Get
    intent: Get TokenEx payment tokenization settings
    question: What TokenEx configuration does the storefront need to tokenize card details?
  phrasing_ops: 2
  slug: optimizely-token-ex-config-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Track API from Optimizely — 1 operation(s) for track.
  name: Optimizely Track API
  phrasing_intents:
  - id: trackEvent
    intent: Track a conversion event for a user
    question: How do I send a conversion event so it shows up in my Optimizely experiment results?
  phrasing_ops: 1
  slug: optimizely-track-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage transactional mails that are triggered by a recipient action or event
  name: Optimizely Transactional mails API
  phrasing_intents:
  - id: selectTransactionalCampaigns
    intent: List all transactional mails
    question: How do I see every transactional mail set up in my Optimizely Campaign client?
  - id: createTransactionalMailing
    intent: Create a transactional mail
    question: How do I set up a new transactional mail with a subject, sender and content?
  - id: getTransactionalMailing
    intent: Get details of one transactional mail
    question: What is the current status and type of a specific transactional mail?
  - id: deleteTransactionalMailing
    intent: Delete a transactional mail
    question: How do I permanently remove a transactional mail I no longer use?
  - id: updateCampaignMessage_3
    intent: Update a transactional mail's message settings
    question: How do I change the subject or sender of an existing transactional mail?
  - id: addAttachments_2
    intent: Attach files to a transactional email
    question: How do I add attachments to a transactional email message?
  - id: deleteAttachments_2
    intent: Remove attachments from a transactional email
    question: How do I take an attachment off a transactional email?
  - id: getCampaignMessageContent_2
    intent: Get the content of a transactional email
    question: Can I download the HTML or plain-text body of a transactional email?
  phrasing_ops: 24
  slug: optimizely-transactional-mails-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Translation Dictionaries API from Optimizely — 5 operation(s) for translation dictionaries.
  name: Optimizely Translation Dictionaries API
  phrasing_intents:
  - id: TranslationDictionaries_Get
    intent: List translation dictionary entries
    question: Which storefront labels have translations in my translation dictionary?
  - id: TranslationDictionaries_Post
    intent: Add a translation for a keyword
    question: How do I add a translated label for a storefront keyword?
  - id: TranslationDictionaries_GetById
    intent: Get one translation entry
    question: What is the stored translation for a specific dictionary entry?
  - id: TranslationDictionaries_PutById
    intent: Replace a translation entry
    question: How do I overwrite a translation entry's keyword, source and text together?
  - id: TranslationDictionaries_DeleteById
    intent: Delete a translation entry
    question: How do I remove one translation from the dictionary?
  - id: TranslationDictionaries_PatchById
    intent: Fix the text of a translation
    question: Can I correct just the translated text of an existing entry?
  - id: TranslationDictionaries_Default
    intent: Get the default translation entry template
    question: What default values does a new translation entry start with?
  - id: TranslationDictionaries_DeleteRoute
    intent: Bulk delete translation entries
    question: How do I delete many translations at once?
  phrasing_ops: 10
  slug: optimizely-translation-dictionaries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Translation Properties API from Optimizely — 7 operation(s) for translation properties.
  name: Optimizely Translation Properties API
  phrasing_intents:
  - id: TranslationProperties_Get
    intent: List translated property values
    question: Which translated field values exist across my commerce data?
  - id: TranslationProperties_Post
    intent: Add a translation for a property
    question: How do I store a translated value for a field on a product or other record?
  - id: TranslationProperties_GetById
    intent: Get one translation property
    question: How do I look up a single translated value by its ID?
  - id: TranslationProperties_PutById
    intent: Replace a translation property
    question: How do I overwrite a translation property record completely?
  - id: TranslationProperties_DeleteById
    intent: Delete a translation property
    question: How do I remove a translated value I no longer need?
  - id: TranslationProperties_PatchById
    intent: Change a translated value
    question: Can I just fix the wording of an existing translation?
  - id: TranslationProperties_Default
    intent: Call the Default function on translations
    question: What does the Default OData function on translation properties return?
  - id: TranslationProperties_GetForEntityByEntityname_1
    intent: Get translation properties for an entity type
    question: Which translatable properties exist for a given entity like product or category?
  phrasing_ops: 11
  slug: optimizely-translation-properties-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Uploader API from Optimizely — 4 operation(s) for uploader.
  name: Optimizely Uploader API
  phrasing_intents:
  - id: getUploadUrl
    intent: Get a presigned URL to upload a file
    question: How do I get a presigned URL for uploading a single file?
  - id: createMultipartUpload
    intent: Start a multipart upload for a large file
    question: How do I upload a very large file in parts?
  - id: getMultipartUploadStatus
    intent: Check a multipart upload's status
    question: How do I check the progress of a multipart upload?
  - id: completeMultipartUpload
    intent: Finish a multipart upload
    question: What do I call after all parts of a large file are uploaded?
  phrasing_ops: 4
  slug: optimizely-uploader-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: User related information for the current account
  name: Optimizely User API
  phrasing_intents:
  - id: get_me
    intent: Get the signed-in user's profile
    question: Who am I authenticated as with this API token?
  phrasing_ops: 1
  slug: optimizely-user-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Files API from Optimizely — 1 operation(s) for user files.
  name: Optimizely User Files API
  phrasing_intents:
  - id: UserFilesV1_PutAsyncByFilename
    intent: Upload or replace a user file (PUT)
    question: How do I overwrite an existing admin user file by its filename?
  - id: UserFilesV1_PostAsyncByFilename
    intent: Upload a user file (POST)
    question: How do I upload a new file to the admin user files area?
  phrasing_ops: 2
  slug: optimizely-user-files-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Payment Profiles API from Optimizely — 5 operation(s) for user payment profiles.
  name: Optimizely User Payment Profiles API
  phrasing_intents:
  - id: UserPaymentProfiles_Get
    intent: List saved customer payment cards
    question: How can I see the saved payment cards on file for storefront users?
  - id: UserPaymentProfiles_Post
    intent: Save a payment card to a user profile
    question: What card and billing address details are needed to save a payment profile?
  - id: UserPaymentProfiles_GetById
    intent: Get one saved payment profile
    question: How do I look up one saved card by its payment profile id?
  - id: UserPaymentProfiles_PutById
    intent: Replace a saved payment profile
    question: Can I overwrite every field of a saved card record at once?
  - id: UserPaymentProfiles_DeleteById
    intent: Remove a saved payment card
    question: How do I remove one saved card from a customer's account?
  - id: UserPaymentProfiles_PatchById
    intent: Update a saved card's expiry or default flag
    question: Can I update just the expiration date on a saved card?
  - id: UserPaymentProfiles_Default
    intent: Get default values for a new payment profile
    question: What defaults does a new user payment profile start with?
  - id: UserPaymentProfiles_DeleteRoute
    intent: Delete several saved payment profiles
    question: How do I bulk delete saved payment cards?
  phrasing_ops: 9
  slug: optimizely-user-payment-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Email Lists API from Optimizely — 5 operation(s) for user profile email lists.
  name: Optimizely User Profile Email Lists API
  phrasing_intents:
  - id: UserProfileEmailLists_Get
    intent: List user email list subscriptions
    question: Which user profiles are subscribed to which email lists?
  - id: UserProfileEmailLists_Post
    intent: Subscribe a user profile to an email list
    question: How do I add a user to an email list?
  - id: UserProfileEmailLists_GetById
    intent: Get a user email list membership
    question: How do I look up one user-to-email-list membership by ID?
  - id: UserProfileEmailLists_PutById
    intent: Replace a user email list membership
    question: How do I overwrite an email list membership record in full?
  - id: UserProfileEmailLists_DeleteById
    intent: Unsubscribe a user from an email list
    question: How do I remove a user from an email list?
  - id: UserProfileEmailLists_PatchById
    intent: Update a user email list membership
    question: How do I switch a user's membership to a different email list?
  - id: UserProfileEmailLists_Default
    intent: Get a default email list membership template
    question: What default values does a new email list membership start with?
  - id: UserProfileEmailLists_DeleteRoute
    intent: Bulk remove user email list memberships
    question: How do I remove many users from email lists in one go?
  phrasing_ops: 9
  slug: optimizely-user-profile-email-lists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Passwords API from Optimizely — 5 operation(s) for user profile passwords.
  name: Optimizely User Profile Passwords API
  phrasing_intents:
  - id: UserProfilePasswords_Get
    intent: List stored user password records
    question: How do I list the password history records kept for user profiles in Optimizely Configured Commerce?
  - id: UserProfilePasswords_Post
    intent: Store a password hash for a user
    question: Can I add a password hash record for a user profile?
  - id: UserProfilePasswords_GetById
    intent: Get one user password record
    question: How can I read a single user profile password record by ID?
  - id: UserProfilePasswords_PutById
    intent: Replace a user password record
    question: Can I overwrite a whole user password record?
  - id: UserProfilePasswords_DeleteById
    intent: Delete a user password record
    question: How do I delete one stored password record?
  - id: UserProfilePasswords_PatchById
    intent: Update a user password record
    question: Can I update just the password-changed date on a record?
  - id: UserProfilePasswords_Default
    intent: Get default values for a password record
    question: What defaults are pre-filled for a new user password record?
  - id: UserProfilePasswords_DeleteRoute
    intent: Delete several user password records
    question: Can I bulk delete old password history records?
  phrasing_ops: 9
  slug: optimizely-user-profile-passwords-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Websites API from Optimizely — 5 operation(s) for user profile websites.
  name: Optimizely User Profile Websites API
  phrasing_intents:
  - id: UserProfileWebsites_Get
    intent: List user-to-website assignments
    question: Which users have access to which of my commerce websites?
  - id: UserProfileWebsites_Post
    intent: Give a user access to a website
    question: How do I grant a user profile access to another website?
  - id: UserProfileWebsites_GetById
    intent: Get one user-to-website assignment
    question: How do I read a single user profile website link by ID?
  - id: UserProfileWebsites_PutById
    intent: Replace a user-to-website assignment
    question: How do I overwrite a user website assignment with a full new record?
  - id: UserProfileWebsites_DeleteById
    intent: Remove a user's access to a website
    question: How do I revoke a user's access to one website?
  - id: UserProfileWebsites_PatchById
    intent: Move a user assignment to another website
    question: Can I switch an existing assignment to a different website?
  - id: UserProfileWebsites_Default
    intent: Call the Default function on user websites
    question: What does the Default OData function on user profile websites return?
  - id: UserProfileWebsites_DeleteRoute
    intent: Bulk remove user website assignments
    question: Can I revoke many user website assignments in one request?
  phrasing_ops: 9
  slug: optimizely-user-profile-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Wish List Favorites API from Optimizely — 5 operation(s) for user profile wish list favorites.
  name: Optimizely User Profile Wish List Favorites API
  phrasing_intents:
  - id: UserProfileWishListFavorites_Get
    intent: List users' favorite wish lists
    question: Which wish lists have shoppers marked as favorites?
  - id: UserProfileWishListFavorites_Post
    intent: Mark a wish list as a user's favorite
    question: How do I mark a wish list as a favorite for a particular user?
  - id: UserProfileWishListFavorites_GetById
    intent: Get one wish list favorite
    question: Which user and wish list does a specific favorite record connect?
  - id: UserProfileWishListFavorites_PutById
    intent: Replace a wish list favorite record
    question: Is there a way to overwrite a whole wish list favorite record at once?
  - id: UserProfileWishListFavorites_DeleteById
    intent: Unfavorite a wish list
    question: How do I remove a wish list from a user's favorites?
  - id: UserProfileWishListFavorites_PatchById
    intent: Update a wish list favorite
    question: Can I point an existing favorite at a different wish list?
  - id: UserProfileWishListFavorites_Default
    intent: Call the Default function on wish list favorites
    question: What does the Default function on user profile wish list favorites return?
  - id: UserProfileWishListFavorites_DeleteRoute
    intent: Bulk delete wish list favorites by ID
    question: Can I remove many wish list favorites in one call?
  phrasing_ops: 9
  slug: optimizely-user-profile-wish-list-favorites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Wish List Hides API from Optimizely — 5 operation(s) for user profile wish list hides.
  name: Optimizely User Profile Wish List Hides API
  phrasing_intents:
  - id: UserProfileWishListHides_Get
    intent: List wish lists hidden by users
    question: How do I see which shared wish lists users have hidden?
  - id: UserProfileWishListHides_Post
    intent: Hide a wish list for a user
    question: How do I hide a wish list from a particular user's view?
  - id: UserProfileWishListHides_GetById
    intent: Get one wish list hide record
    question: How do I look up a single wish list hide by its id?
  - id: UserProfileWishListHides_PutById
    intent: Replace a wish list hide record
    question: How do I overwrite a wish list hide record entirely?
  - id: UserProfileWishListHides_DeleteById
    intent: Unhide a wish list for a user
    question: How do I make a hidden wish list visible to a user again?
  - id: UserProfileWishListHides_PatchById
    intent: Update a wish list hide record
    question: How do I change which wish list a hide record points to?
  - id: UserProfileWishListHides_Default
    intent: Get the default wish list hide record
    question: What does a default wish list hide record look like?
  - id: UserProfileWishListHides_DeleteRoute
    intent: Bulk delete wish list hides
    question: How do I remove many wish list hide records at once?
  phrasing_ops: 9
  slug: optimizely-user-profile-wish-list-hides-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profile Wish List Tags API from Optimizely — 5 operation(s) for user profile wish list tags.
  name: Optimizely User Profile Wish List Tags API
  phrasing_intents:
  - id: UserProfileWishListTags_Get
    intent: List wish list tags
    question: What tags have shoppers put on their wish lists?
  - id: UserProfileWishListTags_Post
    intent: Tag a user's wish list
    question: How do I add a tag to a customer's wish list?
  - id: UserProfileWishListTags_GetById
    intent: Get a wish list tag by id
    question: What tag text and wish list does a given tag record hold?
  - id: UserProfileWishListTags_PutById
    intent: Replace a wish list tag
    question: Can I fully rewrite a wish list tag record?
  - id: UserProfileWishListTags_DeleteById
    intent: Delete a wish list tag
    question: How do I remove a tag from someone's wish list?
  - id: UserProfileWishListTags_PatchById
    intent: Rename a wish list tag
    question: Can I rename an existing wish list tag without recreating it?
  - id: UserProfileWishListTags_Default
    intent: Call the wish list tags Default function
    question: What does the Default function on wish list tags return?
  - id: UserProfileWishListTags_DeleteRoute
    intent: Bulk delete wish list tags
    question: Can I clear several wish list tags in one call?
  phrasing_ops: 9
  slug: optimizely-user-profile-wish-list-tags-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The User Profiles API from Optimizely — 26 operation(s) for user profiles.
  name: Optimizely User Profiles API
  phrasing_intents:
  - id: UserProfiles_Get
    intent: List user profiles
    question: How do I pull a list of every user profile in the commerce admin?
  - id: UserProfiles_Post
    intent: Create a user profile
    question: What fields are required to add a new user profile to the storefront admin?
  - id: UserProfiles_GetById
    intent: Get a user profile by id
    question: How can I look up a single user profile when I know its id?
  - id: UserProfiles_PutById
    intent: Replace a user profile
    question: Is there a way to overwrite an entire user profile record in one call?
  - id: UserProfiles_DeleteById
    intent: Delete a user profile
    question: Can I permanently remove one user profile by its id?
  - id: UserProfiles_PatchById
    intent: Update fields on a user profile
    question: How do I change just a user's phone number without resending the whole profile?
  - id: UserProfiles_Default
    intent: Get a blank user profile template
    question: What default values does a brand-new user profile start with?
  - id: UserProfiles_GetRolesById
    intent: Get a user's roles via the Roles function
    question: Which roles are attached to a user profile, using the Default.Roles() function?
  phrasing_ops: 33
  slug: optimizely-user-profiles-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: User Management
  name: Optimizely Users API
  phrasing_intents:
  - id: getAuthenticatedUser
    intent: Get the currently authenticated Campaign user
    question: How do I check which user my Campaign credentials are signed in as?
  - id: rotatePassword
    intent: Rotate a Campaign user's password
    question: How do I rotate the password for a Campaign API user?
  - id: listUsers
    intent: List users page by page
    question: How can I page through the full list of users?
  - id: findUserByEmail
    intent: Find a user by email address
    question: Is there a user registered with a particular email address?
  - id: userCreate
    intent: Create a new user
    question: What fields are supported when creating a user?
  - id: getUser
    intent: Get a user by id
    question: How do I fetch one user's profile by their id?
  - id: userUpdate
    intent: Update an existing user
    question: Which user fields can actually be changed after creation?
  - id: userDelete
    intent: Permanently delete a user
    question: How do I permanently remove a user?
  phrasing_ops: 10
  slug: optimizely-users-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Variable Definitions
  name: Optimizely Variable Definitions API
  phrasing_intents:
  - id: list_variable_definitions
    intent: List a flag's variable definitions
    question: Which variables are defined on my feature flag?
  - id: update_variable_definitions
    intent: Bulk update a flag's variable definitions
    question: Can I change several variable definitions on a flag with one JSON patch?
  - id: create_variable_definition
    intent: Add a variable to a feature flag
    question: How do I add a new variable to a feature flag?
  - id: brainstorm_variable_definitions
    intent: Brainstorm flag variables with AI
    question: Can AI suggest variable definitions for my feature flag?
  - id: delete_variable_definition
    intent: Delete a flag variable definition
    question: How do I remove a variable from a feature flag?
  - id: fetch_variable_definition
    intent: Get one flag variable definition
    question: What type and default value does a particular flag variable have?
  phrasing_ops: 6
  slug: optimizely-variable-definitions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: APIs to interact with Variations
  name: Optimizely Variations API
  phrasing_intents:
  - id: list_variations
    intent: List a flag's variations
    question: What variations does a feature flag have in my Optimizely Feature Experimentation project?
  - id: update_variations
    intent: Update a flag's variations with a JSON patch
    question: How do I edit several variations of a flag in one JSON patch request?
  - id: create_variation
    intent: Create a flag variation
    question: How do I add a new variation to a feature flag?
  - id: archive_variations
    intent: Archive flag variations
    question: How do I hide variations I no longer use without permanently deleting them?
  - id: brainstorm_variations
    intent: Brainstorm variation ideas with AI
    question: Can Optimizely's AI suggest new variation definitions for a flag?
  - id: unarchive_variations
    intent: Restore archived flag variations
    question: How do I bring back variations I archived earlier?
  - id: delete_variation
    intent: Permanently delete a flag variation
    question: How do I permanently delete a variation so its data is gone for good?
  - id: fetch_variation
    intent: Get a single flag variation
    question: What variables and settings does a specific variation of a flag have?
  phrasing_ops: 8
  slug: optimizely-variations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vat Codes API from Optimizely — 6 operation(s) for vat codes.
  name: Optimizely Vat Codes API
  phrasing_intents:
  - id: VatCodes_Get
    intent: List VAT codes
    question: How do I list every VAT code configured in the commerce admin?
  - id: VatCodes_Post
    intent: Create a VAT code
    question: How do I add a new VAT code for taxing products?
  - id: VatCodes_GetById
    intent: Get a VAT code
    question: How do I look up a single VAT code by ID?
  - id: VatCodes_PutById
    intent: Replace a VAT code
    question: How do I overwrite a VAT code record in full?
  - id: VatCodes_DeleteById
    intent: Delete a VAT code
    question: How do I delete one VAT code?
  - id: VatCodes_PatchById
    intent: Update a VAT code
    question: How do I rename an existing VAT code?
  - id: VatCodes_Default
    intent: Get a default VAT code template
    question: What default values does a new VAT code start with?
  - id: VatCodes_DeleteRoute
    intent: Bulk delete VAT codes
    question: How do I delete several VAT codes at once?
  phrasing_ops: 10
  slug: optimizely-vat-codes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vendors API from Optimizely — 6 operation(s) for vendors.
  name: Optimizely Vendors API
  phrasing_intents:
  - id: Vendors_Get
    intent: List vendors
    question: How do I list all the vendors supplying products in Optimizely Configured Commerce?
  - id: Vendors_Post
    intent: Add a new vendor
    question: What contact and address details are required to set up a vendor?
  - id: Vendors_GetById
    intent: Get one vendor
    question: How can I pull a single vendor's contact details by ID?
  - id: Vendors_PutById
    intent: Replace a vendor record
    question: Can I overwrite a vendor with a complete new record?
  - id: Vendors_DeleteById
    intent: Delete a vendor
    question: How do I delete a single vendor?
  - id: Vendors_PatchById
    intent: Update a vendor's details
    question: Can I change just a vendor's contact person without resending the address?
  - id: Vendors_Default
    intent: Get default values for a new vendor
    question: What defaults are pre-filled for a vendor before it's created?
  - id: Vendors_DeleteRoute
    intent: Delete several vendors
    question: Can I bulk delete a list of vendors in one call?
  phrasing_ops: 10
  slug: optimizely-vendors-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Version Histories API from Optimizely — 6 operation(s) for version histories.
  name: Optimizely Version Histories API
  phrasing_intents:
  - id: VersionHistories_Get
    intent: List version history records
    question: Where can I see the version history entries recorded by my commerce platform?
  - id: VersionHistories_Post
    intent: Record a new version history entry
    question: How do I log a new version history entry with a version number and type?
  - id: VersionHistories_GetById
    intent: Get one version history record
    question: How do I read a single version history entry by ID?
  - id: VersionHistories_PutById
    intent: Replace a version history record
    question: How do I overwrite an entire version history entry?
  - id: VersionHistories_DeleteById
    intent: Delete a version history record
    question: How do I remove one version history entry?
  - id: VersionHistories_PatchById
    intent: Update fields on a version history record
    question: Can I correct just the version number on an existing history entry?
  - id: VersionHistories_Default
    intent: Call the Default function on version histories
    question: What does the Default OData function on version histories return?
  - id: VersionHistories_DeleteRoute
    intent: Bulk delete version history records
    question: Can I prune several version history entries in one request?
  phrasing_ops: 10
  slug: optimizely-version-histories-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Version History Actions API from Optimizely — 5 operation(s) for version history actions.
  name: Optimizely Version History Actions API
  phrasing_intents:
  - id: VersionHistoryActions_Get
    intent: List version history actions
    question: What actions have been recorded against version history entries?
  - id: VersionHistoryActions_Post
    intent: Record a version history action
    question: How do I log a named action against a version history entry?
  - id: VersionHistoryActions_GetById
    intent: Get a version history action
    question: Can I look up one version history action by its id?
  - id: VersionHistoryActions_PutById
    intent: Replace a version history action
    question: Is there a way to overwrite a version history action completely?
  - id: VersionHistoryActions_DeleteById
    intent: Delete a version history action
    question: Can I delete one version history action by id?
  - id: VersionHistoryActions_PatchById
    intent: Rename a version history action
    question: How do I rename an existing version history action?
  - id: VersionHistoryActions_Default
    intent: Get a blank version history action template
    question: What default values does a new version history action start with?
  - id: VersionHistoryActions_DeleteRoute
    intent: Bulk delete version history actions
    question: Can I delete many version history actions at once?
  phrasing_ops: 9
  slug: optimizely-version-history-actions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Bins API from Optimizely — 9 operation(s) for vmi bins.
  name: Optimizely Vmi Bins API
  phrasing_intents:
  - id: VmiBins_Get
    intent: List VMI bins
    question: Which vendor-managed inventory bins are set up?
  - id: VmiBins_Post
    intent: Create a VMI bin
    question: How do I add a new vendor-managed inventory bin at a location?
  - id: VmiBins_GetById
    intent: Get a VMI bin
    question: Can I see one VMI bin's last count and quantities?
  - id: VmiBins_PutById
    intent: Replace a VMI bin
    question: How do I overwrite a VMI bin record in full?
  - id: VmiBins_DeleteById
    intent: Delete a VMI bin
    question: How do I permanently delete a single VMI bin?
  - id: VmiBins_PatchById
    intent: Update fields on a VMI bin
    question: Can I change just the reorder thresholds on a VMI bin?
  - id: VmiBins_Default
    intent: Get default values for a new VMI bin
    question: What defaults does a new VMI bin start with?
  - id: VmiBins_Archive
    intent: Archive VMI bins via OData action
    question: Can I archive VMI bins using the OData archive action?
  phrasing_ops: 14
  slug: optimizely-vmi-bins-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Counts API from Optimizely — 5 operation(s) for vmi counts.
  name: Optimizely Vmi Counts API
  phrasing_intents:
  - id: VmiCounts_Get
    intent: List VMI bin counts
    question: What inventory counts have been recorded for vendor managed inventory bins in Optimizely commerce?
  - id: VmiCounts_Post
    intent: Record a VMI bin count
    question: How do I record how many units of a product are in a VMI bin?
  - id: VmiCounts_GetById
    intent: Get a VMI count
    question: What count was recorded in a specific VMI count record?
  - id: VmiCounts_PutById
    intent: Replace a VMI count record
    question: How do I overwrite a whole VMI count record?
  - id: VmiCounts_DeleteById
    intent: Delete a VMI count
    question: How do I remove an incorrect VMI count?
  - id: VmiCounts_PatchById
    intent: Correct a VMI count quantity
    question: How do I fix the quantity on an existing VMI count?
  - id: VmiCounts_Default
    intent: Get a blank default VMI count
    question: What does an empty VMI count object look like?
  - id: VmiCounts_DeleteRoute
    intent: Delete several VMI counts
    question: Can I delete multiple VMI counts at once?
  phrasing_ops: 9
  slug: optimizely-vmi-counts-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Locations API from Optimizely — 8 operation(s) for vmi locations.
  name: Optimizely Vmi Locations API
  phrasing_intents:
  - id: VmiLocations_Get
    intent: List vendor-managed inventory locations
    question: Which VMI locations are set up in my Optimizely Configured Commerce admin?
  - id: VmiLocations_Post
    intent: Create a VMI location
    question: How do I add a new vendor-managed inventory location for a customer?
  - id: VmiLocations_GetById
    intent: Get one VMI location
    question: What are the settings of a specific VMI location?
  - id: VmiLocations_PutById
    intent: Replace a VMI location record
    question: How do I overwrite every field of an existing VMI location in one call?
  - id: VmiLocations_DeleteById
    intent: Delete a VMI location
    question: How do I delete a single VMI location by its ID?
  - id: VmiLocations_PatchById
    intent: Partially update a VMI location
    question: Can I change just one setting of a VMI location, like deactivating it?
  - id: VmiLocations_Default
    intent: Get the default VMI location template
    question: What does a blank VMI location look like with its default values?
  - id: VmiLocations_Archive
    intent: Archive VMI locations via the archive action
    question: How do I archive several VMI locations at once with the archive action?
  phrasing_ops: 35
  slug: optimizely-vmi-locations-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Vmi Notes API from Optimizely — 5 operation(s) for vmi notes.
  name: Optimizely Vmi Notes API
  phrasing_intents:
  - id: VmiNotes_Get
    intent: List vendor-managed inventory notes
    question: Which notes have been left on my vendor-managed inventory bins?
  - id: VmiNotes_Post
    intent: Add a note to a VMI bin
    question: How do I leave a note on a vendor-managed inventory bin?
  - id: VmiNotes_GetById
    intent: Get a VMI note
    question: What does a particular vendor-managed inventory note say?
  - id: VmiNotes_PutById
    intent: Replace a VMI note
    question: How do I overwrite a VMI note record entirely?
  - id: VmiNotes_DeleteById
    intent: Delete one VMI note
    question: How do I remove a note from a VMI bin?
  - id: VmiNotes_PatchById
    intent: Edit a VMI note
    question: Can I change only the text of a VMI note?
  - id: VmiNotes_Default
    intent: Get default values for a new VMI note
    question: What defaults does a new VMI note start with?
  - id: VmiNotes_DeleteRoute
    intent: Bulk delete VMI notes
    question: Can I remove many VMI notes in one request?
  phrasing_ops: 9
  slug: optimizely-vmi-notes-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Warehouse Alternates API from Optimizely — 5 operation(s) for warehouse alternates.
  name: Optimizely Warehouse Alternates API
  phrasing_intents:
  - id: WarehouseAlternates_Get
    intent: List alternate warehouse pairings
    question: Which backup warehouses are configured in Optimizely Commerce?
  - id: WarehouseAlternates_Post
    intent: Set a fallback warehouse for another
    question: How do I set up a backup warehouse to fulfill from when the primary is short?
  - id: WarehouseAlternates_GetById
    intent: Get one alternate warehouse pairing
    question: Which warehouses does a given alternate pairing connect?
  - id: WarehouseAlternates_PutById
    intent: Replace an alternate warehouse pairing
    question: Can I overwrite a warehouse alternate pairing in full?
  - id: WarehouseAlternates_DeleteById
    intent: Remove an alternate warehouse pairing
    question: How do I stop a warehouse from being used as another's backup?
  - id: WarehouseAlternates_PatchById
    intent: Swap the backup in a warehouse pairing
    question: Can I swap which warehouse acts as the backup in an existing pairing?
  - id: WarehouseAlternates_Default
    intent: Get default values for a warehouse alternate
    question: What defaults does a new warehouse alternate start with?
  - id: WarehouseAlternates_DeleteRoute
    intent: Bulk delete warehouse alternate pairings
    question: Can I remove many warehouse alternate pairings at once?
  phrasing_ops: 9
  slug: optimizely-warehouse-alternates-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Warehouse Websites API from Optimizely — 5 operation(s) for warehouse websites.
  name: Optimizely Warehouse Websites API
  phrasing_intents:
  - id: WarehouseWebsites_Get
    intent: List warehouse-to-website assignments
    question: Which warehouses serve which websites in Optimizely Configured Commerce?
  - id: WarehouseWebsites_Post
    intent: Assign a warehouse to a website
    question: How do I make a warehouse available to a specific website?
  - id: WarehouseWebsites_GetById
    intent: Get one warehouse website assignment
    question: How do I look up a single warehouse-website link by its ID?
  - id: WarehouseWebsites_PutById
    intent: Replace a warehouse website assignment
    question: Can I overwrite a warehouse-website link with a different pair?
  - id: WarehouseWebsites_DeleteById
    intent: Unassign a warehouse from a website
    question: How do I stop a warehouse from serving a website?
  - id: WarehouseWebsites_PatchById
    intent: Update a warehouse website assignment
    question: Can I switch just the warehouse on an existing website assignment?
  - id: WarehouseWebsites_Default
    intent: Get default values for a warehouse website
    question: What defaults does the admin pre-fill for a new warehouse website assignment?
  - id: WarehouseWebsites_DeleteRoute
    intent: Bulk delete warehouse website assignments
    question: How do I remove many warehouse-website links in one request?
  phrasing_ops: 9
  slug: optimizely-warehouse-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Warehouses API from Optimizely — 13 operation(s) for warehouses.
  name: Optimizely Warehouses API
  phrasing_intents:
  - id: Warehouses_Get
    intent: List warehouses in commerce admin
    question: Which warehouses are configured in my commerce admin?
  - id: Warehouses_Post
    intent: Create a warehouse
    question: How do I add a new warehouse with its address, phone and opening hours?
  - id: Warehouses_GetById
    intent: Get a warehouse's admin record
    question: What address and contact details are stored for one warehouse?
  - id: Warehouses_PutById
    intent: Replace a warehouse record
    question: How do I overwrite an existing warehouse's entire record, address included?
  - id: Warehouses_DeleteById
    intent: Delete one warehouse
    question: How do I remove a single warehouse by its id?
  - id: Warehouses_PatchById
    intent: Update selected fields on a warehouse
    question: Can I change just the phone number of a warehouse without resending everything?
  - id: Warehouses_Default
    intent: Get default values for a new warehouse
    question: What default values does a brand-new warehouse start with?
  - id: Warehouses_Archive
    intent: Archive warehouses via the archive action
    question: Can I archive several warehouses at once instead of deleting them?
  phrasing_ops: 17
  slug: optimizely-warehouses-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: Manage webhooks
  name: Optimizely Webhooks API
  phrasing_intents:
  - id: activateWebhook
    intent: Activate a client's event webhook
    question: How do I switch on a webhook so it starts sending event data for my client account?
  - id: selectWebhooks
    intent: List a client's event webhooks
    question: Which webhooks are set up for my client account and are they active?
  - id: createWebhook
    intent: Create an event webhook for a client
    question: How do I create a webhook that pushes event data to my URL for a client account?
  - id: deactivateWebhook
    intent: Pause a client's event webhook
    question: How do I stop a webhook from sending event data without deleting it?
  - id: updateWebhook
    intent: Change a client webhook's target or format
    question: How do I point an existing client webhook at a new target URL?
  - id: deleteWebhook
    intent: Delete a client's event webhook
    question: How do I permanently remove a webhook from my client account?
  - id: verifyWebhook
    intent: Test a client webhook against its target URL
    question: How do I check that my webhook's target URL is ready before going live?
  - id: list-WebhookHandler
    intent: List registered content webhooks
    question: What webhooks are registered on the /api/webhooks endpoint for content events?
  phrasing_ops: 16
  slug: optimizely-webhooks-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Allowed Customers API from Optimizely — 5 operation(s) for website allowed customers.
  name: Optimizely Website Allowed Customers API
  phrasing_intents:
  - id: WebsiteAllowedCustomers_Get
    intent: List customers allowed on websites
    question: Which customers are allowed to use which storefront websites?
  - id: WebsiteAllowedCustomers_Post
    intent: Allow a customer on a website
    question: How do I give a customer access to a restricted storefront website?
  - id: WebsiteAllowedCustomers_GetById
    intent: Get one website allowed customer record
    question: Where do I look up a single website allowed customer record by id?
  - id: WebsiteAllowedCustomers_PutById
    intent: Replace a website allowed customer record
    question: Can I fully overwrite a website allowed customer record?
  - id: WebsiteAllowedCustomers_DeleteById
    intent: Remove a customer's access to a website
    question: Can I revoke a customer's access to a storefront website?
  - id: WebsiteAllowedCustomers_PatchById
    intent: Update a website allowed customer record
    question: Can I move an existing access record to a different website?
  - id: WebsiteAllowedCustomers_Default
    intent: Call the Default function on allowed customers
    question: What does the Default function on WebsiteAllowedCustomers return?
  - id: WebsiteAllowedCustomers_DeleteRoute
    intent: Bulk remove website allowed customers
    question: Can I revoke many customers' website access at once by id?
  phrasing_ops: 9
  slug: optimizely-website-allowed-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Carriers API from Optimizely — 5 operation(s) for website carriers.
  name: Optimizely Website Carriers API
  phrasing_intents:
  - id: WebsiteCarriers_Get
    intent: List carriers enabled on websites
    question: Which shipping carriers are enabled on each website?
  - id: WebsiteCarriers_Post
    intent: Enable a carrier on a website
    question: How do I offer a shipping carrier on a specific website?
  - id: WebsiteCarriers_GetById
    intent: Get a website carrier assignment
    question: Is there a call to read one website-carrier assignment by ID?
  - id: WebsiteCarriers_PutById
    intent: Replace a website carrier assignment
    question: What's the call to overwrite a website-carrier assignment entirely?
  - id: WebsiteCarriers_DeleteById
    intent: Remove a carrier from a website
    question: How do I stop offering a carrier on a website?
  - id: WebsiteCarriers_PatchById
    intent: Update a website carrier assignment
    question: How do I swap the carrier on an existing website assignment?
  - id: WebsiteCarriers_Default
    intent: Get the default website carrier template
    question: What does a blank website carrier assignment look like?
  - id: WebsiteCarriers_DeleteRoute
    intent: Bulk delete website carrier assignments
    question: Can I remove many carrier assignments at once?
  phrasing_ops: 9
  slug: optimizely-website-carriers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Countries API from Optimizely — 5 operation(s) for website countries.
  name: Optimizely Website Countries API
  phrasing_intents:
  - id: WebsiteCountries_Get
    intent: List countries enabled on websites
    question: Which countries are enabled on each of my commerce websites?
  - id: WebsiteCountries_Post
    intent: Enable a country on a website
    question: How do I make a new country available on one of my websites?
  - id: WebsiteCountries_GetById
    intent: Get a website country link by id
    question: Which website and country does one website-country record connect?
  - id: WebsiteCountries_PutById
    intent: Replace a website country link
    question: How do I overwrite a website-country record entirely?
  - id: WebsiteCountries_DeleteById
    intent: Remove a country from a website
    question: Can I stop offering a country on a website by deleting its link?
  - id: WebsiteCountries_PatchById
    intent: Change the country on a website link
    question: How do I point an existing website-country link at a different country?
  - id: WebsiteCountries_Default
    intent: Get a blank website country template
    question: What default values does a new website country link start with?
  - id: WebsiteCountries_DeleteRoute
    intent: Bulk delete website country links
    question: Can I remove several website-country links in one request?
  phrasing_ops: 9
  slug: optimizely-website-countries-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Currencies API from Optimizely — 5 operation(s) for website currencies.
  name: Optimizely Website Currencies API
  phrasing_intents:
  - id: WebsiteCurrencies_Get
    intent: List currencies enabled on websites
    question: Which currencies can shoppers use on each storefront website?
  - id: WebsiteCurrencies_Post
    intent: Enable a currency on a website
    question: How do I add a currency to a storefront website?
  - id: WebsiteCurrencies_GetById
    intent: Get a website currency
    question: Can I look up one website currency assignment by ID?
  - id: WebsiteCurrencies_PutById
    intent: Replace a website currency
    question: Can I overwrite a website currency record completely?
  - id: WebsiteCurrencies_DeleteById
    intent: Remove a currency from a website
    question: How do I stop offering a currency on a website?
  - id: WebsiteCurrencies_PatchById
    intent: Make a website currency live or default
    question: Can I switch a website currency live without resending the rest?
  - id: WebsiteCurrencies_Default
    intent: Get default values for a website currency
    question: What defaults are pre-filled for a new website currency?
  - id: WebsiteCurrencies_DeleteRoute
    intent: Remove several website currencies
    question: Can I bulk delete website currencies in one call?
  phrasing_ops: 9
  slug: optimizely-website-currencies-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Dealers API from Optimizely — 5 operation(s) for website dealers.
  name: Optimizely Website Dealers API
  phrasing_intents:
  - id: WebsiteDealers_Get
    intent: List dealer-to-website assignments
    question: Which dealers are shown on which of my commerce websites?
  - id: WebsiteDealers_Post
    intent: Assign a dealer to a website
    question: How do I make a dealer available on a particular website?
  - id: WebsiteDealers_GetById
    intent: Get one dealer-to-website assignment
    question: How do I look up a single website dealer link by its ID?
  - id: WebsiteDealers_PutById
    intent: Replace a dealer-to-website assignment
    question: How do I overwrite a website dealer record entirely?
  - id: WebsiteDealers_DeleteById
    intent: Unassign a dealer from a website
    question: How do I stop showing a dealer on one of my websites?
  - id: WebsiteDealers_PatchById
    intent: Point a dealer assignment at another dealer or site
    question: How do I switch an existing website dealer link to a different dealer?
  - id: WebsiteDealers_Default
    intent: Get a blank website dealer template
    question: What default values does a new website dealer link start with?
  - id: WebsiteDealers_DeleteRoute
    intent: Bulk unassign dealers from websites
    question: How do I delete several website dealer links at once?
  phrasing_ops: 9
  slug: optimizely-website-dealers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Languages API from Optimizely — 5 operation(s) for website languages.
  name: Optimizely Website Languages API
  phrasing_intents:
  - id: WebsiteLanguages_Get
    intent: List website languages
    question: Which languages are enabled on each of my storefront websites?
  - id: WebsiteLanguages_Post
    intent: Add a language to a website
    question: How do I enable a new language on a storefront website?
  - id: WebsiteLanguages_GetById
    intent: Get a website language
    question: How do I check whether one website language is live?
  - id: WebsiteLanguages_PutById
    intent: Replace a website language
    question: How do I overwrite a website language record completely?
  - id: WebsiteLanguages_DeleteById
    intent: Remove a language from a website
    question: How do I remove a language from a storefront website?
  - id: WebsiteLanguages_PatchById
    intent: Update a website language
    question: How do I take a website language live?
  - id: WebsiteLanguages_Default
    intent: Get the default website language template
    question: What default values does a new website language start with?
  - id: WebsiteLanguages_DeleteRoute
    intent: Bulk delete website languages
    question: How do I remove several website languages at once?
  phrasing_ops: 9
  slug: optimizely-website-languages-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Product Cross Sells API from Optimizely — 5 operation(s) for website product cross sells.
  name: Optimizely Website Product Cross Sells API
  phrasing_intents:
  - id: WebsiteProductCrossSells_Get
    intent: List website product cross-sells
    question: Which products are set up as cross-sells on each website?
  - id: WebsiteProductCrossSells_Post
    intent: Add a product as a website cross-sell
    question: How do I promote a product as a cross-sell on one storefront?
  - id: WebsiteProductCrossSells_GetById
    intent: Get a website cross-sell record
    question: Which product and website does a cross-sell record point to?
  - id: WebsiteProductCrossSells_PutById
    intent: Replace a website cross-sell record
    question: How do I overwrite a website cross-sell completely?
  - id: WebsiteProductCrossSells_DeleteById
    intent: Remove a website cross-sell
    question: How do I stop cross-selling a product on a website?
  - id: WebsiteProductCrossSells_PatchById
    intent: Swap the product on a website cross-sell
    question: How do I change which product an existing cross-sell promotes?
  - id: WebsiteProductCrossSells_Default
    intent: Get defaults for a new website cross-sell
    question: What defaults does a new website cross-sell start with?
  - id: WebsiteProductCrossSells_DeleteRoute
    intent: Delete several website cross-sells
    question: How do I bulk remove website cross-sell records?
  phrasing_ops: 9
  slug: optimizely-website-product-cross-sells-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Promotions API from Optimizely — 5 operation(s) for website promotions.
  name: Optimizely Website Promotions API
  phrasing_intents:
  - id: WebsitePromotions_Get
    intent: List website-promotion assignments
    question: Which promotions are running on which websites?
  - id: WebsitePromotions_Post
    intent: Run a promotion on a website
    question: How do I make a promotion available on a specific website?
  - id: WebsitePromotions_GetById
    intent: Get a website-promotion assignment
    question: Can I look up one website-promotion link by ID?
  - id: WebsitePromotions_PutById
    intent: Replace a website-promotion assignment
    question: How do I overwrite a website-promotion link entirely?
  - id: WebsitePromotions_DeleteById
    intent: Remove a promotion from a website
    question: How do I stop a promotion running on a website?
  - id: WebsitePromotions_PatchById
    intent: Change a website-promotion assignment
    question: Can I move a promotion assignment to a different website?
  - id: WebsitePromotions_Default
    intent: Get default values for a new website promotion
    question: What defaults does a new website-promotion assignment start with?
  - id: WebsitePromotions_DeleteRoute
    intent: Bulk remove website-promotion assignments
    question: Can I delete many website-promotion links in one call?
  phrasing_ops: 9
  slug: optimizely-website-promotions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website Sitemaps API from Optimizely — 5 operation(s) for website sitemaps.
  name: Optimizely Website Sitemaps API
  phrasing_intents:
  - id: WebsiteSitemaps_Get
    intent: List website sitemaps
    question: Which XML sitemaps have been generated for my storefront websites?
  - id: WebsiteSitemaps_Post
    intent: Create a website sitemap
    question: How do I store a new XML sitemap for a domain?
  - id: WebsiteSitemaps_GetById
    intent: Get a website sitemap
    question: What XML does a particular sitemap record contain?
  - id: WebsiteSitemaps_PutById
    intent: Replace a website sitemap
    question: How do I overwrite a sitemap record with regenerated XML?
  - id: WebsiteSitemaps_DeleteById
    intent: Delete a website sitemap
    question: How do I delete an outdated sitemap?
  - id: WebsiteSitemaps_PatchById
    intent: Update a website sitemap
    question: Can I swap in new XML on a sitemap without resending the rest?
  - id: WebsiteSitemaps_Default
    intent: Get a blank sitemap template
    question: What default values does a new sitemap record start with?
  - id: WebsiteSitemaps_DeleteRoute
    intent: Bulk delete website sitemaps
    question: How do I delete many sitemaps at once?
  phrasing_ops: 9
  slug: optimizely-website-sitemaps-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Website States API from Optimizely — 5 operation(s) for website states.
  name: Optimizely Website States API
  phrasing_intents:
  - id: WebsiteStates_Get
    intent: List website state assignments
    question: Which states or provinces are enabled on each of my commerce websites?
  - id: WebsiteStates_Post
    intent: Enable a state on a website
    question: How do I make a state or province available on a website?
  - id: WebsiteStates_GetById
    intent: Get a website state assignment
    question: Which website and state does one website state record link?
  - id: WebsiteStates_PutById
    intent: Replace a website state assignment
    question: How do I overwrite a website state record completely?
  - id: WebsiteStates_DeleteById
    intent: Remove a state from a website
    question: Can I stop offering a state on a website by deleting its record?
  - id: WebsiteStates_PatchById
    intent: Update a website state assignment
    question: How do I point an existing website state record at a different state?
  - id: WebsiteStates_Default
    intent: Get a blank website state template
    question: What default values does a new website state record have?
  - id: WebsiteStates_DeleteRoute
    intent: Bulk delete website states
    question: Can I remove several states from websites at once?
  phrasing_ops: 9
  slug: optimizely-website-states-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Websites API from Optimizely — 41 operation(s) for websites.
  name: Optimizely Websites API
  phrasing_intents:
  - id: Websites_Get
    intent: List the websites configured in the admin
    question: How do I list every website set up in the Optimizely Commerce admin?
  - id: Websites_Post
    intent: Create a new website
    question: How do I create a new storefront website in the commerce admin?
  - id: Websites_GetById
    intent: Get one website by its id
    question: How can I look up the settings of a single website by its id?
  - id: Websites_PutById
    intent: Replace a website's full record
    question: How do I overwrite a website's entire configuration in one request?
  - id: Websites_DeleteById
    intent: Delete a single website
    question: How do I permanently delete one website by its id?
  - id: Websites_PatchById
    intent: Update selected fields on a website
    question: How do I switch a website into maintenance mode without resending everything?
  - id: Websites_Default
    intent: Get the default website record
    question: What does the default website record look like in the admin API?
  - id: Websites_Archive
    intent: Archive websites with the archive action
    question: How do I archive several websites at once with the OData archive action?
  phrasing_ops: 45
  slug: optimizely-websites-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Customer Additions API from Optimizely — 5 operation(s) for wish list customer additions.
  name: Optimizely Wish List Customer Additions API
  phrasing_intents:
  - id: WishListCustomerAdditions_Get
    intent: List customers added to wish lists
    question: Which customers have been added to shared wish lists?
  - id: WishListCustomerAdditions_Post
    intent: Add a customer to a wish list
    question: How do I give another customer access to a wish list?
  - id: WishListCustomerAdditions_GetById
    intent: Get a wish list customer addition by ID
    question: Which customer and wish list does one addition record link?
  - id: WishListCustomerAdditions_PutById
    intent: Replace a wish list customer addition
    question: Can I overwrite a whole wish list customer addition record at once?
  - id: WishListCustomerAdditions_DeleteById
    intent: Remove a customer from a wish list
    question: How do I revoke a customer's access to a shared wish list?
  - id: WishListCustomerAdditions_PatchById
    intent: Update a wish list customer addition
    question: How do I move a customer addition to a different wish list?
  - id: WishListCustomerAdditions_Default
    intent: Get a default wish list customer addition template
    question: What default values does a new wish list customer addition start with?
  - id: WishListCustomerAdditions_DeleteRoute
    intent: Bulk delete wish list customer additions
    question: How do I delete several wish list customer additions at once?
  phrasing_ops: 9
  slug: optimizely-wish-list-customer-additions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Customer Exceptions API from Optimizely — 5 operation(s) for wish list customer exceptions.
  name: Optimizely Wish List Customer Exceptions API
  phrasing_intents:
  - id: WishListCustomerExceptions_Get
    intent: List wish list customer exceptions
    question: How can I see which customers are excluded from wish lists?
  - id: WishListCustomerExceptions_Post
    intent: Exclude a customer from a wish list
    question: How do I stop a customer from seeing a shared wish list?
  - id: WishListCustomerExceptions_GetById
    intent: Get one wish list customer exception
    question: How can I look up a single wish list customer exception?
  - id: WishListCustomerExceptions_PutById
    intent: Replace a wish list customer exception
    question: How do I overwrite a wish list customer exception record?
  - id: WishListCustomerExceptions_DeleteById
    intent: Remove a wish list customer exception
    question: How do I let an excluded customer see a wish list again?
  - id: WishListCustomerExceptions_PatchById
    intent: Update a wish list customer exception
    question: How can I switch which customer an exception applies to?
  - id: WishListCustomerExceptions_Default
    intent: Get defaults for a new customer exception
    question: What default values does a new wish list customer exception have?
  - id: WishListCustomerExceptions_DeleteRoute
    intent: Bulk delete wish list customer exceptions
    question: How do I clear several wish list customer exceptions at once?
  phrasing_ops: 9
  slug: optimizely-wish-list-customer-exceptions-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Customers API from Optimizely — 5 operation(s) for wish list customers.
  name: Optimizely Wish List Customers API
  phrasing_intents:
  - id: WishListCustomers_Get
    intent: List wish list sharing with customers
    question: Which customers have access to which wish lists in my commerce store?
  - id: WishListCustomers_Post
    intent: Link a customer to a wish list
    question: How do I give a customer account access to a wish list?
  - id: WishListCustomers_GetById
    intent: Get one wish list customer link
    question: Which wish list and customer does a specific link record connect?
  - id: WishListCustomers_PutById
    intent: Replace a wish list customer link
    question: How do I overwrite a wish list customer link entirely?
  - id: WishListCustomers_DeleteById
    intent: Unlink a customer from a wish list
    question: How do I remove a customer's access to a wish list?
  - id: WishListCustomers_PatchById
    intent: Reassign a wish list customer link
    question: Can I switch an existing wish list link to a different customer?
  - id: WishListCustomers_Default
    intent: Get the default wish list customer template
    question: What default values does a new wish list customer link start with?
  - id: WishListCustomers_DeleteRoute
    intent: Bulk delete wish list customer links
    question: How do I remove many wish list customer links at once?
  phrasing_ops: 9
  slug: optimizely-wish-list-customers-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Email Schedules API from Optimizely — 5 operation(s) for wish list email schedules.
  name: Optimizely Wish List Email Schedules API
  phrasing_intents:
  - id: WishListEmailSchedules_Get
    intent: List wish list email schedules
    question: Which wish lists are set up to be emailed on a recurring schedule?
  - id: WishListEmailSchedules_Post
    intent: Schedule recurring emails of a wish list
    question: How do I set up a wish list to be emailed every week?
  - id: WishListEmailSchedules_GetById
    intent: Get one wish list email schedule
    question: How do I look up one wish list email schedule?
  - id: WishListEmailSchedules_PutById
    intent: Replace a wish list email schedule
    question: Can I overwrite a whole wish list email schedule?
  - id: WishListEmailSchedules_DeleteById
    intent: Stop a single wish list email schedule
    question: How do I stop one wish list from being emailed on a schedule?
  - id: WishListEmailSchedules_PatchById
    intent: Change the day or message of a wish list email
    question: Can I move an existing wish list email to a different weekday?
  - id: WishListEmailSchedules_Default
    intent: Get default values for a new wish list schedule
    question: What defaults does a new wish list email schedule start with?
  - id: WishListEmailSchedules_DeleteRoute
    intent: Delete several wish list email schedules
    question: How do I bulk delete wish list email schedules?
  phrasing_ops: 9
  slug: optimizely-wish-list-email-schedules-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Products API from Optimizely — 5 operation(s) for wish list products.
  name: Optimizely Wish List Products API
  phrasing_intents:
  - id: WishListProducts_Get
    intent: List products on wish lists
    question: How do I see every product saved on customers' wish lists?
  - id: WishListProducts_Post
    intent: Add a product to a wish list
    question: How do I add a product to a customer's wish list?
  - id: WishListProducts_GetById
    intent: Get a wish list product
    question: How do I look up one wish list line by ID?
  - id: WishListProducts_PutById
    intent: Replace a wish list product
    question: How do I overwrite a wish list item record entirely?
  - id: WishListProducts_DeleteById
    intent: Remove a product from a wish list
    question: How do I take a product off a wish list?
  - id: WishListProducts_PatchById
    intent: Update a wish list product
    question: How do I change the quantity of a product on a wish list?
  - id: WishListProducts_Default
    intent: Get a default wish list product template
    question: What default values does a new wish list item start with?
  - id: WishListProducts_DeleteRoute
    intent: Bulk remove wish list products
    question: How do I remove several products from wish lists at once?
  phrasing_ops: 9
  slug: optimizely-wish-list-products-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wish List Shares API from Optimizely — 5 operation(s) for wish list shares.
  name: Optimizely Wish List Shares API
  phrasing_intents:
  - id: WishListShares_Get
    intent: List wish list shares
    question: How do I see which wish lists have been shared and with whom in Optimizely Configured Commerce?
  - id: WishListShares_Post
    intent: Share a wish list with someone
    question: Can I share a wish list with a person by email?
  - id: WishListShares_GetById
    intent: Get one wish list share
    question: How can I check the details of a single wish list share?
  - id: WishListShares_PutById
    intent: Replace a wish list share
    question: Can I overwrite a wish list share record with new values?
  - id: WishListShares_DeleteById
    intent: Stop sharing a wish list
    question: How do I revoke a wish list share?
  - id: WishListShares_PatchById
    intent: Update a wish list share
    question: Can I mark an existing wish list share as activated?
  - id: WishListShares_Default
    intent: Get default values for a wish list share
    question: What defaults are pre-filled for a new wish list share?
  - id: WishListShares_DeleteRoute
    intent: Delete several wish list shares
    question: Can I bulk revoke many wish list shares?
  phrasing_ops: 9
  slug: optimizely-wish-list-shares-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Wishlists API from Optimizely — 12 operation(s) for wishlists.
  name: Optimizely Wishlists API
  phrasing_intents:
  - id: WishLists_Get
    intent: List and filter wish lists
    question: How can I see every wish list in my commerce admin?
  - id: WishLists_Post
    intent: Create a wish list
    question: How do I create a new wish list for a customer through the admin API?
  - id: WishLists_GetById
    intent: Get one wish list by id
    question: How can I look up a single wish list when I know its id?
  - id: WishLists_PutById
    intent: Replace a wish list entirely
    question: How do I overwrite every field of an existing wish list in one request?
  - id: WishLists_DeleteById
    intent: Delete one wish list
    question: How do I permanently remove one specific wish list?
  - id: WishLists_PatchById
    intent: Update some fields of a wish list
    question: How can I just rename a wish list without resending the whole thing?
  - id: WishLists_Default
    intent: Get default values for a new wish list
    question: What default values does a brand-new wish list start with?
  - id: WishLists_Archive
    intent: Archive wish lists with the archive action
    question: How do I archive several wish lists at once using the archive action?
  phrasing_ops: 42
  slug: optimizely-wishlists-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Work Requests API from Optimizely — 13 operation(s) for work requests.
  name: Optimizely Work Requests API
  phrasing_intents:
  - id: listWorkRequests
    intent: List work requests
    question: Which marketing work requests are still open?
  - id: createWorkRequest
    intent: Submit a work request
    question: How do I submit a new work request from one of our intake templates?
  - id: getWorkRequest
    intent: Get a work request
    question: How do I pull up the details of one work request?
  - id: updateWorkRequest
    intent: Update a work request's status, priority or assignees
    question: How do I change the status of a work request?
  - id: listWorkRequestComments
    intent: List comments on a work request
    question: What has the team said in the comments on a work request?
  - id: addCommentToWorkRequest
    intent: Comment on a work request
    question: How do I post a comment on a work request and mention a colleague?
  - id: getWorkRequestComment
    intent: Get a work request comment
    question: How do I fetch one particular comment from a work request?
  - id: addAttachmentToWorkRequest
    intent: Attach a file to a work request
    question: How do I attach an uploaded file to a work request?
  phrasing_ops: 16
  slug: optimizely-work-requests-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Workflows API from Optimizely — 2 operation(s) for workflows.
  name: Optimizely Workflows API
  phrasing_intents:
  - id: listWorkflows
    intent: List CMP workflows
    question: Which workflows exist in my content marketing platform?
  - id: getWorkflow
    intent: Get a CMP workflow
    question: What does a particular workflow look like in CMP?
  phrasing_ops: 2
  slug: optimizely-workflows-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Oauth API from Optimizely — 1 operation(s) for oauth.
  name: Optimizely OAUTH API
  phrasing_intents:
  - id: getToken
    intent: Get a JWT token for Optimizely Agent
    question: How do I get a JWT to authenticate my requests to Optimizely Agent?
  phrasing_ops: 1
  slug: optimizely-oauth-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Apple Pay API from Optimizely — 2 operation(s) for apple pay.
  name: Optimizely Apple Pay API
  phrasing_intents:
  - id: ApplePaySession_ValidateSessionAsync
    intent: Validate an Apple Pay merchant session
    question: How does my storefront validate an Apple Pay merchant session before checkout?
  - id: ApplePayV1_Get
    intent: Get the Apple Pay configuration
    question: Is Apple Pay configured for my commerce storefront?
  phrasing_ops: 2
  slug: optimizely-apple-pay-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Best Bets API from Optimizely — 2 operation(s) for best bets.
  name: Optimizely Best Bets API
  phrasing_intents:
  - id: get-BestBetCollectionHandler
    intent: Get best bet collections
    question: How do I list the best bet collections that pin results in search?
  - id: create-BestBetCollectionHandler
    intent: Create a best bet collection
    question: How do I register a new best bet collection for promoted search results?
  - id: update-BestBetCollectionHandler
    intent: Rename a best bet collection
    question: How do I change the title of an existing best bet collection?
  - id: delete-BestBetCollectionHandler
    intent: Delete a best bet collection
    question: How do I remove a best bet collection I no longer use?
  phrasing_ops: 4
  slug: optimizely-best-bets-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Data File API from Optimizely — 1 operation(s) for data file.
  name: Optimizely Data File API
  phrasing_intents:
  - id: getDatafile
    intent: Get the feature flag datafile
    question: How do I get the JSON datafile the agent is using for an environment?
  phrasing_ops: 1
  slug: optimizely-data-file-api
- baseURL: https://exp.mcp.opal.optimizely.com/mcp
  baseurl_source: declared
  description: The Google Pay API from Optimizely — 1 operation(s) for google pay.
  name: Optimizely Google Pay API
  phrasing_intents:
  - id: GooglePayV1_Get
    intent: Get the storefront Google Pay configuration
    question: What Google Pay settings does my commerce storefront use?
  phrasing_ops: 1
  slug: optimizely-google-pay-api
- description: GraphQL Content Graph API that indexes CMS/Commerce content for fast, federated querying across the Optimizely platform.
  name: Optimizely Graph (Content Graph)
  slug: optimizely-graph-content-graph
- description: REST API and multi-language SDKs for feature flags, experimentation and rollouts, with the self-hosted Optimizely Agent as a microservice front end.
  name: Optimizely Feature Experimentation REST API
  slug: optimizely-feature-experimentation-rest-api
- description: Headless Content Delivery, Content Management and Content Definitions REST APIs for the Optimizely (Episerver) CMS.
  name: Content Management REST API (CMS 12)
  slug: content-management-rest-api-cms-12
artifact_total: 763
asyncapis:
- description: The Optimizely Content Marketing Platform (CMP) provides webhook notifications when content events occur, such as when assets are published, tasks are completed or modified, and content items are upda
  name: Optimizely CMP Webhooks
  slug: optimizely-cmp-asyncapi
- description: Optimizely Feature Experimentation provides webhook notifications when configuration changes occur, such as datafile updates. Webhooks notify external servers of changes, eliminating the need to const
  name: Optimizely Feature Experimentation Webhooks
  slug: optimizely-feature-experimentation-asyncapi
- description: ''
  name: Optimizely Webhooks
  slug: optimizely-webhooks
collections:
- collection_type: postman
  name: Optimizely Campaign REST Assets API
  slug: postman-optimizely-assets-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Attributes API
  slug: postman-optimizely-attributes-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Audiences API
  slug: postman-optimizely-audiences-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Campaigns API
  slug: postman-optimizely-campaigns-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Entries API
  slug: postman-optimizely-catalog-entries-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Entry Relations API
  slug: postman-optimizely-catalog-entry-relations-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalog Nodes API
  slug: postman-optimizely-catalog-nodes-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Catalogs API
  slug: postman-optimizely-catalogs-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Content API
  slug: postman-optimizely-content-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Content Types API
  slug: postman-optimizely-content-types-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Customers API
  slug: postman-optimizely-customers-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Environments API
  slug: postman-optimizely-environments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Events API
  slug: postman-optimizely-events-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Experiments API
  slug: postman-optimizely-experiments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Extensions API
  slug: postman-optimizely-extensions-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Features API
  slug: postman-optimizely-features-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Flags API
  slug: postman-optimizely-flags-api
- collection_type: postman
  name: Optimizely Campaign REST Assets GraphQL API
  slug: postman-optimizely-graphql-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Labels API
  slug: postman-optimizely-labels-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Mailing Lists API
  slug: postman-optimizely-mailing-lists-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Objects API
  slug: postman-optimizely-objects-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Orders API
  slug: postman-optimizely-orders-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Pages API
  slug: postman-optimizely-pages-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Profiles API
  slug: postman-optimizely-profiles-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Projects API
  slug: postman-optimizely-projects-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Recipients API
  slug: postman-optimizely-recipients-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Rulesets API
  slug: postman-optimizely-rulesets-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Schema API
  slug: postman-optimizely-schema-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Segments API
  slug: postman-optimizely-segments-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Sites API
  slug: postman-optimizely-sites-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Smart Campaigns API
  slug: postman-optimizely-smart-campaigns-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Tasks API
  slug: postman-optimizely-tasks-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Transactional Mail API
  slug: postman-optimizely-transactional-mail-api
- collection_type: postman
  name: Optimizely Campaign REST Assets Unsubscribes API
  slug: postman-optimizely-unsubscribes-api
- collection_type: open
  name: Optimizely Campaign REST Assets API
  slug: open-optimizely-assets-api
- collection_type: open
  name: Optimizely Campaign REST Assets Attributes API
  slug: open-optimizely-attributes-api
- collection_type: open
  name: Optimizely Campaign REST Assets Audiences API
  slug: open-optimizely-audiences-api
- collection_type: open
  name: Optimizely Campaign REST API
  slug: open-optimizely-campaign
- collection_type: open
  name: Optimizely Campaign REST Assets Campaigns API
  slug: open-optimizely-campaigns-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Entries API
  slug: open-optimizely-catalog-entries-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Entry Relations API
  slug: open-optimizely-catalog-entry-relations-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalog Nodes API
  slug: open-optimizely-catalog-nodes-api
- collection_type: open
  name: Optimizely Campaign REST Assets Catalogs API
  slug: open-optimizely-catalogs-api
- collection_type: open
  name: Optimizely CMP Open REST API
  slug: open-optimizely-cmp
- collection_type: open
  name: Optimizely Commerce Service API
  slug: open-optimizely-commerce-service
- collection_type: open
  name: Optimizely Campaign REST Assets Content API
  slug: open-optimizely-content-api
- collection_type: open
  name: Optimizely Content Delivery API
  slug: open-optimizely-content-delivery
- collection_type: open
  name: Optimizely Content Management API
  slug: open-optimizely-content-management
- collection_type: open
  name: Optimizely Campaign REST Assets Content Types API
  slug: open-optimizely-content-types-api
- collection_type: open
  name: Optimizely Campaign REST Assets Customers API
  slug: open-optimizely-customers-api
- collection_type: open
  name: Optimizely Data Platform REST API
  slug: open-optimizely-data-platform
- collection_type: open
  name: Optimizely Campaign REST Assets Environments API
  slug: open-optimizely-environments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Events API
  slug: open-optimizely-events-api
- collection_type: open
  name: Optimizely Campaign REST Assets Experiments API
  slug: open-optimizely-experiments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Extensions API
  slug: open-optimizely-extensions-api
- collection_type: open
  name: Optimizely Feature Experimentation REST API
  slug: open-optimizely-feature-experimentation
- collection_type: open
  name: Optimizely Campaign REST Assets Features API
  slug: open-optimizely-features-api
- collection_type: open
  name: Optimizely Campaign REST Assets Flags API
  slug: open-optimizely-flags-api
- collection_type: open
  name: Optimizely Graph API
  slug: open-optimizely-graph
- collection_type: open
  name: Optimizely Campaign REST Assets GraphQL API
  slug: open-optimizely-graphql-api
- collection_type: open
  name: Optimizely Campaign REST Assets Labels API
  slug: open-optimizely-labels-api
- collection_type: open
  name: Optimizely Campaign REST Assets Mailing Lists API
  slug: open-optimizely-mailing-lists-api
- collection_type: open
  name: Optimizely Campaign REST Assets Objects API
  slug: open-optimizely-objects-api
- collection_type: open
  name: Optimizely Campaign REST Assets Orders API
  slug: open-optimizely-orders-api
- collection_type: open
  name: Optimizely Campaign REST Assets Pages API
  slug: open-optimizely-pages-api
- collection_type: open
  name: Optimizely Campaign REST Assets Profiles API
  slug: open-optimizely-profiles-api
- collection_type: open
  name: Optimizely Campaign REST Assets Projects API
  slug: open-optimizely-projects-api
- collection_type: open
  name: Optimizely Campaign REST Assets Recipients API
  slug: open-optimizely-recipients-api
- collection_type: open
  name: Optimizely Campaign REST Assets Rulesets API
  slug: open-optimizely-rulesets-api
- collection_type: open
  name: Optimizely Campaign REST Assets Schema API
  slug: open-optimizely-schema-api
- collection_type: open
  name: Optimizely Campaign REST Assets Segments API
  slug: open-optimizely-segments-api
- collection_type: open
  name: Optimizely Campaign REST Assets Sites API
  slug: open-optimizely-sites-api
- collection_type: open
  name: Optimizely Campaign REST Assets Smart Campaigns API
  slug: open-optimizely-smart-campaigns-api
- collection_type: open
  name: Optimizely Campaign REST Assets Tasks API
  slug: open-optimizely-tasks-api
- collection_type: open
  name: Optimizely Campaign REST Assets Transactional Mail API
  slug: open-optimizely-transactional-mail-api
- collection_type: open
  name: Optimizely Campaign REST Assets Unsubscribes API
  slug: open-optimizely-unsubscribes-api
- collection_type: open
  name: Optimizely Web Experimentation REST API
  slug: open-optimizely-web-experimentation
common:
- group: design
  href: https://artifacts.apis.io/optimizely/rules/optimizely-rules.yml
  title: ''
  type: Spectral
  url: rules/optimizely-rules.yml
- group: design
  href: https://artifacts.apis.io/optimizely/rules/optimizely-jsonschema-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/optimizely-jsonschema-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/optimizely/rules/optimizely-asyncapi-spectral-rules.yml
  title: ''
  type: Spectral
  url: rules/optimizely-asyncapi-spectral-rules.yml
- group: design
  href: https://artifacts.apis.io/optimizely/json-ld/optimizely-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/optimizely-context.jsonld
- group: docs
  href: https://artifacts.apis.io/optimizely/asyncapi/optimizely-cmp-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/optimizely-cmp-asyncapi.yml
- group: operate
  href: https://artifacts.apis.io/optimizely/lifecycle/optimizely-lifecycle.yml
  title: ''
  type: Deprecation
  url: lifecycle/optimizely-lifecycle.yml
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-web-experimentation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-web-experimentation-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-recommendations-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-recommendations-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-platform-optimizely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-platform-optimizely-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-performance-edge-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-performance-edge-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-feature-experimentation-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-feature-experimentation-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-experimentation-data-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-experimentation-data-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-digital-experience-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-digital-experience-platform-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-data-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-data-platform-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-content-marketing-platform-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-content-marketing-platform-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-content-management-system-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-content-management-system-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-configured-commerce-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-configured-commerce-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-campaign-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-campaign-llms.txt
- group: other
  href: https://artifacts.apis.io/optimizely/hosts/optimizely-hosts.yml
  title: ''
  type: Hosts
  url: hosts/optimizely-hosts.yml
- group: build
  href: https://artifacts.apis.io/optimizely/integrations/optimizely-integration-edges.yml
  title: ''
  type: IntegrationEdges
  url: integrations/optimizely-integration-edges.yml
- group: other
  href: https://artifacts.apis.io/optimizely/vendors/optimizely-vendors.yml
  title: ''
  type: Vendors
  url: vendors/optimizely-vendors.yml
- group: company
  title: ''
  type: Newsroom
  url: https://www.optimizely.com/company/press
- group: commercial
  href: https://artifacts.apis.io/optimizely/finops/optimizely-finops.yml
  title: ''
  type: FinOps
  url: finops/optimizely-finops.yml
- group: other
  href: https://artifacts.apis.io/optimizely/capabilities/optimizely-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/optimizely-capability-edges.yml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-feature-experimentation-flags-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-feature-experimentation-flags-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-flags-scheduling-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-flags-scheduling-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-permission-service-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-permission-service-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-agent-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-agent-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-event-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-event-api-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-edge-decider-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-edge-decider-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-odp-advanced-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-odp-advanced-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-graph-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-graph-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-cmp-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-cmp-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-campaign-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-campaign-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-configured-commerce-admin-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-configured-commerce-admin-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-cms-content-delivery-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-cms-content-delivery-overlay.yaml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-content-recommendations-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-content-recommendations-overlay.yaml
- group: agent
  href: https://artifacts.apis.io/optimizely/well-known/optimizely-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/optimizely-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://docs.developers.optimizely.com/.well-known/api-catalog
- group: agent
  href: https://artifacts.apis.io/optimizely/mcp/optimizely-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/optimizely-mcp.yml
- group: build
  href: https://artifacts.apis.io/optimizely/mcp/optimizely-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/optimizely-tool-crosswalk.yml
- group: agent
  href: https://artifacts.apis.io/optimizely/llms/optimizely-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/optimizely-llms.txt
- group: agent
  href: https://artifacts.apis.io/optimizely/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://artifacts.apis.io/optimizely/packages/optimizely-packages.yml
  title: ''
  type: Packages
  url: packages/optimizely-packages.yml
- group: build
  href: https://artifacts.apis.io/optimizely/packages/optimizely-packages.yml
  title: ''
  type: SDKs
  url: packages/optimizely-packages.yml
- group: build
  href: https://artifacts.apis.io/optimizely/cli/optimizely-cli.yml
  title: ''
  type: CLI
  url: cli/optimizely-cli.yml
- group: design
  href: https://artifacts.apis.io/optimizely/components/optimizely-components.yml
  title: ''
  type: Components
  url: components/optimizely-components.yml
- group: start
  href: https://artifacts.apis.io/optimizely/sandbox/optimizely-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/optimizely-sandbox.yml
- group: design
  href: https://artifacts.apis.io/optimizely/conventions/optimizely-conventions.yml
  title: ''
  type: Conventions
  url: conventions/optimizely-conventions.yml
- group: design
  href: https://artifacts.apis.io/optimizely/errors/optimizely-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/optimizely-problem-types.yml
- group: design
  href: https://artifacts.apis.io/optimizely/data-model/optimizely-data-model.yml
  title: ''
  type: DataModel
  url: data-model/optimizely-data-model.yml
- group: design
  href: https://artifacts.apis.io/optimizely/conformance/optimizely-conformance.yml
  title: ''
  type: Conformance
  url: conformance/optimizely-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.optimizely.com/trust-center/compliance
- group: auth
  title: ''
  type: Security
  url: https://www.optimizely.com/trust-center/security
- group: design
  href: https://artifacts.apis.io/optimizely/lifecycle/optimizely-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/optimizely-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.optimizely.com/
- group: operate
  href: https://artifacts.apis.io/optimizely/changelog/optimizely-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/optimizely-changelog.yml
- group: design
  href: https://artifacts.apis.io/optimizely/asyncapi/optimizely-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/optimizely-webhooks.yml
- group: docs
  href: https://artifacts.apis.io/optimizely/asyncapi/optimizely-feature-experimentation-asyncapi.yml
  title: ''
  type: AsyncAPI
  url: asyncapi/optimizely-feature-experimentation-asyncapi.yml
- group: operate
  href: https://artifacts.apis.io/optimizely/rate-limits/optimizely-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/optimizely-rate-limits.yml
- group: commercial
  href: https://artifacts.apis.io/optimizely/plans/optimizely-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/optimizely-plans-pricing.yml
- group: other
  href: https://artifacts.apis.io/optimizely/overlays/optimizely-experimentation-v2-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/optimizely-experimentation-v2-overlay.yaml
- group: docs
  title: ''
  type: Documentation
  url: https://docs.developers.optimizely.com/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developers.optimizely.com/web-experimentation/reference
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.developers.optimizely.com/feature-experimentation/docs/get-started
- group: commercial
  title: ''
  type: Pricing
  url: https://www.optimizely.com/pricing/
- group: start
  title: ''
  type: SignUp
  url: https://www.optimizely.com/free-trial/
- group: operate
  title: ''
  type: HelpCenter
  url: https://support.optimizely.com/hc/en-us/
- group: operate
  title: ''
  type: Community
  url: https://world.optimizely.com/
- group: design
  href: https://artifacts.apis.io/optimizely/vocabulary/optimizely-vocabulary.yml
  title: ''
  type: Vocabulary
  url: vocabulary/optimizely-vocabulary.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/optimizely/overview
- group: agent
  href: https://artifacts.apis.io/optimizely/agentic-access/optimizely-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/optimizely-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/optimizely/security/optimizely-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/optimizely-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/optimizely/security/optimizely-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/optimizely-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/optimizely/security/optimizely-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/optimizely-domain-security.yml
- group: auth
  href: https://artifacts.apis.io/optimizely/authentication/optimizely-authentication.yml
  title: ''
  type: Authentication
  url: authentication/optimizely-authentication.yml
- group: auth
  href: https://artifacts.apis.io/optimizely/scopes/optimizely-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/optimizely-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/optimizely
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/optimizely
- group: start
  title: ''
  type: DeveloperPortal
  url: https://docs.developers.optimizely.com/
- group: company
  title: ''
  type: Website
  url: https://www.optimizely.com/
- group: company
  title: ''
  type: Blog
  url: https://www.optimizely.com/blog/
- group: operate
  title: ''
  type: Support
  url: https://support.optimizely.com/
- group: start
  title: ''
  type: Login
  url: https://app.optimizely.com/signin
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.optimizely.com/legal/privacy-policy/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.optimizely.com/legal/terms/
- group: docs
  title: ''
  type: APIReference
  url: https://docs.developers.optimizely.com/content-management-system/reference
- group: company
  title: ''
  type: Blog
  url: https://www.optimizely.com/insights/blog/
created: '2025-03-04'
description: Optimizely is a digital experience platform that provides A/B testing, feature flagging, content management, and commerce solutions for enterprises. Their developer platform offers a comprehensive suite of REST and GraphQL APIs spanning experimentation, content delivery, customer data, campaign management, and e-commerce capabilities.
features:
- 'Entry: ~$36K/year for basic Optimizely use'
- 'Mid: ~$63,700 per 10M impressions for Web Experimentation'
- 'Enterprise: $200K-$400K+/year for full DXP suite'
- 'Modular: pick CMS / Commerce / Experimentation independently'
- Web Experimentation (A/B + multivariate)
- Feature Experimentation (server-side flags)
- Personalization with audiences and Stats Engine
- Content Cloud (CMS)
- Commerce Cloud and Configured Commerce
- Optimizely AI Copilot
- REST API at api.optimizely.com
- Default 100 req/min/project
- OAuth 2.0 + Personal API tokens
- Webhooks for project events
- Datafile-based Feature Experimentation SDKs (10+)
- Stats Engine with Sequential Testing
finops:
- has_sources: true
  method: derived
  name: Optimizely Finops
  primary_unit: ''
  service_category: ''
  slug: optimizely-finops
  template: true
graphqls:
- description: Optimizely Graph is a unified content query and delivery service that provides access to content across Optimizely products through a single GraphQL API. It enables flexible data retrieval, high-perfo
  name: Optimizely GraphQL API
  slug: optimizely-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/optimizely.png
json_schemas:
- name: ActivateContext
  property_count: 2
  slug: optimizely-activate-context
- name: Asset_2
  property_count: 12
  slug: optimizely-asset-2
- name: AssetInput
  property_count: 3
  slug: optimizely-asset-input
- name: Asset
  property_count: 6
  slug: optimizely-asset
- name: AssetInput
  property_count: 3
  slug: optimizely-assetinput
- name: AttachmentRequestData
  property_count: 3
  slug: optimizely-attachment-request-data
- name: Attribute_3
  property_count: 8
  slug: optimizely-attribute-3
- name: Attribute
  property_count: 6
  slug: optimizely-attribute
- name: AttributeUpdate
  property_count: 4
  slug: optimizely-attribute-update
- name: AudienceInput
  property_count: 4
  slug: optimizely-audience-input
- name: Audience
  property_count: 7
  slug: optimizely-audience
- name: AudienceInput
  property_count: 4
  slug: optimizely-audienceinput
- name: BatchContext
  property_count: 1
  slug: optimizely-batch-context
- name: BatchResponse
  property_count: 4
  slug: optimizely-batch-response
- name: BlacklistEntryRequestData
  property_count: 2
  slug: optimizely-blacklist-entry-request-data
- name: BrandComplianceCategoriesResponse
  property_count: 3
  slug: optimizely-brand-compliance-categories-response
- name: BucketingInformation
  property_count: 3
  slug: optimizely-bucketing-information
- name: CampaignBriefResponse
  property_count: 5
  slug: optimizely-campaign-brief-response
- name: CampaignCommentResponse
  property_count: 9
  slug: optimizely-campaign-comment-response
- name: CampaignCreateRequest
  property_count: 7
  slug: optimizely-campaign-create-request
- name: CampaignFieldUpdateRequest
  property_count: 0
  slug: optimizely-campaign-field-update-request
- name: CampaignResponse
  property_count: 12
  slug: optimizely-campaign-response
- name: Campaign
  property_count: 8
  slug: optimizely-campaign
- name: CampaignInput
  property_count: 3
  slug: optimizely-campaigninput
- name: CatalogEntryInput
  property_count: 5
  slug: optimizely-catalog-entry-input
- name: CatalogEntry
  property_count: 8
  slug: optimizely-catalog-entry
- name: CatalogInput
  property_count: 4
  slug: optimizely-catalog-input
- name: CatalogNodeInput
  property_count: 5
  slug: optimizely-catalog-node-input
- name: CatalogNode
  property_count: 8
  slug: optimizely-catalog-node
- name: Catalog
  property_count: 6
  slug: optimizely-catalog
- name: CatalogEntry
  property_count: 8
  slug: optimizely-catalogentry
- name: CatalogEntryInput
  property_count: 5
  slug: optimizely-catalogentryinput
- name: CatalogInput
  property_count: 4
  slug: optimizely-cataloginput
- name: CatalogNode
  property_count: 8
  slug: optimizely-catalognode
- name: CatalogNodeInput
  property_count: 5
  slug: optimizely-catalognodeinput
- name: CmpContent
  property_count: 9
  slug: optimizely-cmp-content
- name: CmpCampaign
  property_count: 9
  slug: optimizely-cmpcampaign
- name: CmpContent
  property_count: 9
  slug: optimizely-cmpcontent
- name: ContentInput
  property_count: 7
  slug: optimizely-content-input
- name: ContentItem_2
  property_count: 10
  slug: optimizely-content-item-2
- name: ContentItem
  property_count: 13
  slug: optimizely-content-item
- name: content
  property_count: 15
  slug: optimizely-content
- name: ContentType
  property_count: 5
  slug: optimizely-content-type
- name: ContentInput
  property_count: 7
  slug: optimizely-contentinput
- name: ContentItem
  property_count: 13
  slug: optimizely-contentitem
- name: ContentPatch
  property_count: 3
  slug: optimizely-contentpatch
- name: ContentType
  property_count: 5
  slug: optimizely-contenttype
- name: CustomEvent
  property_count: 12
  slug: optimizely-custom-event
- name: Optimizely Customer Profile
  property_count: 5
  slug: optimizely-customer-profile
- name: Customer
  property_count: 5
  slug: optimizely-customer
- name: Decision
  property_count: 7
  slug: optimizely-decision
- name: EnvironmentInput
  property_count: 3
  slug: optimizely-environment-input
- name: Environment
  property_count: 8
  slug: optimizely-environment
- name: EnvironmentInput
  property_count: 3
  slug: optimizely-environmentinput
- name: Environments
  property_count: 12
  slug: optimizely-environments
- name: EventCreateRequest
  property_count: 7
  slug: optimizely-event-create-request
- name: EventFieldsUpdateRequest
  property_count: 0
  slug: optimizely-event-fields-update-request
- name: EventResponse
  property_count: 11
  slug: optimizely-event-response
- name: Event
  property_count: 7
  slug: optimizely-event
- name: EventInput
  property_count: 4
  slug: optimizely-eventinput
- name: ExperimentInput
  property_count: 4
  slug: optimizely-experiment-input
- name: ExperimentResults
  property_count: 5
  slug: optimizely-experiment-results
- name: Optimizely Experiment
  property_count: 13
  slug: optimizely-experiment
- name: ExperimentTimeseries
  property_count: 7
  slug: optimizely-experiment-timeseries
- name: ExperimentInput
  property_count: 4
  slug: optimizely-experimentinput
- name: ExperimentResults
  property_count: 5
  slug: optimizely-experimentresults
- name: Extension_2
  property_count: 12
  slug: optimizely-extension-2
- name: Extension
  property_count: 6
  slug: optimizely-extension
- name: ExtensionUpdate
  property_count: 7
  slug: optimizely-extension-update
- name: Feature_2
  property_count: 10
  slug: optimizely-feature-2
- name: Optimizely Feature Flag
  property_count: 9
  slug: optimizely-feature-flag
- name: Feature
  property_count: 6
  slug: optimizely-feature
- name: FeatureUpdate
  property_count: 6
  slug: optimizely-feature-update
- name: FieldListResponseItem
  property_count: 0
  slug: optimizely-field-list-response-item
- name: FlagInput
  property_count: 5
  slug: optimizely-flag-input
- name: Flag
  property_count: 9
  slug: optimizely-flag
- name: FlagEnvironment
  property_count: 2
  slug: optimizely-flagenvironment
- name: FlagInput
  property_count: 5
  slug: optimizely-flaginput
- name: FlagVariation
  property_count: 3
  slug: optimizely-flagvariation
- name: FlagVariationInput
  property_count: 3
  slug: optimizely-flagvariationinput
- name: GenerateBlobContainerSasLinkApiResponse
  property_count: 3
  slug: optimizely-generate-blob-container-sas-link-api-response
- name: GenerateBlobContainerSasLinkRequestParameters
  property_count: 1
  slug: optimizely-generate-blob-container-sas-link-request-parameters
- name: GenericUpdateResponse
  property_count: 3
  slug: optimizely-generic-update-response
- name: GetBlobStorageContainersApiResponse
  property_count: 3
  slug: optimizely-get-blob-storage-containers-api-response
- name: GraphQLRequest
  property_count: 3
  slug: optimizely-graphqlrequest
- name: GraphQLResponse
  property_count: 3
  slug: optimizely-graphqlresponse
- name: InPageEvent
  property_count: 13
  slug: optimizely-in-page-event
- name: Insite.Account.WebApi.V1.ApiModels.AccountCollectionModel
  property_count: 4
  slug: optimizely-insite-account-web-api-v1-api-models-account-collection-model
- name: Insite.Account.WebApi.V1.ApiModels.AccountModel
  property_count: 32
  slug: optimizely-insite-account-web-api-v1-api-models-account-model
- name: Insite.Account.WebApi.V1.ApiModels.AccountPaymentProfileCollectionModel
  property_count: 4
  slug: optimizely-insite-account-web-api-v1-api-models-account-payment-profile-collection-model
- name: Insite.Account.WebApi.V1.ApiModels.AccountPaymentProfileModel
  property_count: 20
  slug: optimizely-insite-account-web-api-v1-api-models-account-payment-profile-model
- name: Insite.Account.WebApi.V1.ApiModels.AccountShipToCollectionModel
  property_count: 5
  slug: optimizely-insite-account-web-api-v1-api-models-account-ship-to-collection-model
- name: Insite.Account.WebApi.V1.ApiModels.VmiUserModel
  property_count: 6
  slug: optimizely-insite-account-web-api-v1-api-models-vmi-user-model
- name: Insite.Brands.WebApi.V1.ApiModels.BrandAlphabetModel
  property_count: 3
  slug: optimizely-insite-brands-web-api-v1-api-models-brand-alphabet-model
- name: Insite.Brands.WebApi.V1.ApiModels.BrandCategoryCollectionModel
  property_count: 4
  slug: optimizely-insite-brands-web-api-v1-api-models-brand-category-collection-model
- name: Insite.Brands.WebApi.V1.ApiModels.BrandCategoryModel
  property_count: 12
  slug: optimizely-insite-brands-web-api-v1-api-models-brand-category-model
- name: Insite.Brands.WebApi.V1.ApiModels.BrandModel
  property_count: 18
  slug: optimizely-insite-brands-web-api-v1-api-models-brand-model
- name: Insite.Brands.WebApi.V1.ApiModels.BrandProductLineModel
  property_count: 10
  slug: optimizely-insite-brands-web-api-v1-api-models-brand-product-line-model
- name: Insite.Budget.WebApi.V1.ApiModels.BudgetCalendarCollectionModel
  property_count: 3
  slug: optimizely-insite-budget-web-api-v1-api-models-budget-calendar-collection-model
- name: Insite.Budget.WebApi.V1.ApiModels.BudgetCalendarModel
  property_count: 5
  slug: optimizely-insite-budget-web-api-v1-api-models-budget-calendar-model
- name: Insite.Budget.WebApi.V1.ApiModels.BudgetCollectionModel
  property_count: 3
  slug: optimizely-insite-budget-web-api-v1-api-models-budget-collection-model
- name: Insite.Budget.WebApi.V1.ApiModels.BudgetModel
  property_count: 7
  slug: optimizely-insite-budget-web-api-v1-api-models-budget-model
- name: Insite.Catalog.WebApi.V1.ApiModels.AutocompleteModel
  property_count: 10
  slug: optimizely-insite-catalog-web-api-v1-api-models-autocomplete-model
- name: Insite.Catalog.WebApi.V1.ApiModels.AutocompleteProductCollectionModel
  property_count: 3
  slug: optimizely-insite-catalog-web-api-v1-api-models-autocomplete-product-collection-model
- name: Insite.Catalog.WebApi.V1.ApiModels.ProductCollectionModel
  property_count: 16
  slug: optimizely-insite-catalog-web-api-v1-api-models-product-collection-model
- name: Insite.Customers.WebApi.V1.ApiModels.BillToCollectionModel
  property_count: 4
  slug: optimizely-insite-customers-web-api-v1-api-models-bill-to-collection-model
- name: Insite.Customers.WebApi.V1.ApiModels.BillToModel
  property_count: 35
  slug: optimizely-insite-customers-web-api-v1-api-models-bill-to-model
- name: Insite.Customers.WebApi.V1.ApiModels.ShipToCollectionModel
  property_count: 4
  slug: optimizely-insite-customers-web-api-v1-api-models-ship-to-collection-model
- name: Insite.Customers.WebApi.V1.ApiModels.ShipToModel
  property_count: 29
  slug: optimizely-insite-customers-web-api-v1-api-models-ship-to-model
- name: Insite.Data.Entities.AdminActionConfiguration
  property_count: 10
  slug: optimizely-insite-data-entities-admin-action-configuration
- name: Insite.Data.Entities.AdminActionPermission
  property_count: 8
  slug: optimizely-insite-data-entities-admin-action-permission
- name: Insite.Data.Entities.AdminUserProfilePassword
  property_count: 8
  slug: optimizely-insite-data-entities-admin-user-profile-password
- name: Insite.Data.Entities.AdminUserProfilePreference
  property_count: 8
  slug: optimizely-insite-data-entities-admin-user-profile-preference
- name: Insite.Data.Entities.AdminUserProfile
  property_count: 24
  slug: optimizely-insite-data-entities-admin-user-profile
- name: Insite.Data.Entities.AdminUserProfileWebsite
  property_count: 7
  slug: optimizely-insite-data-entities-admin-user-profile-website
- name: Insite.Data.Entities.Affiliate
  property_count: 11
  slug: optimizely-insite-data-entities-affiliate
- name: Insite.Data.Entities.ApplicationLog
  property_count: 12
  slug: optimizely-insite-data-entities-application-log
- name: Insite.Data.Entities.ApplicationMessage
  property_count: 9
  slug: optimizely-insite-data-entities-application-message
- name: Insite.Data.Entities.AttributeType
  property_count: 12
  slug: optimizely-insite-data-entities-attribute-type
- name: Insite.Data.Entities.AttributeValue
  property_count: 9
  slug: optimizely-insite-data-entities-attribute-value
- name: Insite.Data.Entities.Audit
  property_count: 10
  slug: optimizely-insite-data-entities-audit
- name: Insite.Data.Entities.BadgeAttributeValue
  property_count: 7
  slug: optimizely-insite-data-entities-badge-attribute-value
- name: Insite.Data.Entities.BadgeProduct
  property_count: 8
  slug: optimizely-insite-data-entities-badge-product
- name: Insite.Data.Entities.Badge
  property_count: 26
  slug: optimizely-insite-data-entities-badge
- name: Insite.Data.Entities.BillToAddressField
  property_count: 13
  slug: optimizely-insite-data-entities-bill-to-address-field
- name: Insite.Data.Entities.BrandCategoryImage
  property_count: 14
  slug: optimizely-insite-data-entities-brand-category-image
- name: Insite.Data.Entities.Brand
  property_count: 21
  slug: optimizely-insite-data-entities-brand
- name: Insite.Data.Entities.BudgetCalendar
  property_count: 21
  slug: optimizely-insite-data-entities-budget-calendar
- name: Insite.Data.Entities.Customer
  property_count: 73
  slug: optimizely-insite-data-entities-customer
- name: Insite.Data.Entities.Experiment
  property_count: 30
  slug: optimizely-insite-data-entities-experiment
- name: Insite.Data.Entities.Page
  property_count: 13
  slug: optimizely-insite-data-entities-page
- name: Insite.Email.WebApi.V1.ApiModels.ShareEntityModel
  property_count: 8
  slug: optimizely-insite-email-web-api-v1-api-models-share-entity-model
- name: Insite.Order.WebApi.V1.ApiModels.OrderCollectionModel
  property_count: 5
  slug: optimizely-insite-order-web-api-v1-api-models-order-collection-model
- name: Insite.Order.WebApi.V1.ApiModels.OrderModel
  property_count: 74
  slug: optimizely-insite-order-web-api-v1-api-models-order-model
- name: Insite.Order.WebApi.V1.ApiModels.RmaModel
  property_count: 6
  slug: optimizely-insite-order-web-api-v1-api-models-rma-model
- name: Insite.Order.WebApi.V1.ApiModels.ShareOrderModel
  property_count: 10
  slug: optimizely-insite-order-web-api-v1-api-models-share-order-model
- name: Insite.Spire.Services.RetrievePageResult
  property_count: 9
  slug: optimizely-insite-spire-services-retrieve-page-result
- name: LabelGroup
  property_count: 4
  slug: optimizely-label-group
- name: Label
  property_count: 3
  slug: optimizely-label
- name: MailingList
  property_count: 4
  slug: optimizely-mailing-list
- name: MailingList
  property_count: 4
  slug: optimizely-mailinglist
- name: MessageRequestData
  property_count: 27
  slug: optimizely-message-request-data
- name: Metric
  property_count: 5
  slug: optimizely-metric
- name: ModifyRecipientAttributesRequestData
  property_count: 2
  slug: optimizely-modify-recipient-attributes-request-data
- name: ModifyRecipientsAttributesRequestData
  property_count: 3
  slug: optimizely-modify-recipients-attributes-request-data
- name: NodeRelationInput
  property_count: 2
  slug: optimizely-node-relation-input
- name: NodeRelation
  property_count: 3
  slug: optimizely-node-relation
- name: NodeRelation
  property_count: 3
  slug: optimizely-noderelation
- name: NodeRelationInput
  property_count: 2
  slug: optimizely-noderelationinput
- name: ObjectInput
  property_count: 2
  slug: optimizely-object-input
- name: Object
  property_count: 0
  slug: optimizely-object
- name: ObjectInput
  property_count: 2
  slug: optimizely-objectinput
- name: ODataResponseStringList
  property_count: 2
  slug: optimizely-odata-response-string-list
- name: OdpObject
  property_count: 5
  slug: optimizely-odp-object
- name: OdpObject
  property_count: 5
  slug: optimizely-odpobject
- name: Order
  property_count: 9
  slug: optimizely-order
- name: PageInput
  property_count: 5
  slug: optimizely-page-input
- name: Page
  property_count: 8
  slug: optimizely-page
- name: PageInput
  property_count: 5
  slug: optimizely-pageinput
- name: Pagination
  property_count: 3
  slug: optimizely-pagination
- name: PatchRequestBody
  property_count: 4
  slug: optimizely-patch-request-body
- name: PrepareSendingBatchRequest
  property_count: 3
  slug: optimizely-prepare-sending-batch-request
- name: ProfileInput
  property_count: 2
  slug: optimizely-profile-input
- name: Profile
  property_count: 11
  slug: optimizely-profile
- name: ProfileUpdateRequest
  property_count: 1
  slug: optimizely-profile-update-request
- name: ProfileInput
  property_count: 2
  slug: optimizely-profileinput
- name: ProjectInput
  property_count: 2
  slug: optimizely-project-input
- name: Project
  property_count: 8
  slug: optimizely-project
- name: ProjectInput
  property_count: 2
  slug: optimizely-projectinput
- name: RecipientInput
  property_count: 4
  slug: optimizely-recipient-input
- name: Recipient
  property_count: 8
  slug: optimizely-recipient
- name: RecipientInput
  property_count: 4
  slug: optimizely-recipientinput
- name: RecipientsChunkRequestData
  property_count: 2
  slug: optimizely-recipients-chunk-request-data
- name: RestAttachment
  property_count: 11
  slug: optimizely-rest-attachment
- name: RestAttachmentStreamingCollection
  property_count: 5
  slug: optimizely-rest-attachment-streaming-collection
- name: RestBlacklistEntry
  property_count: 6
  slug: optimizely-rest-blacklist-entry
- name: RestBlacklistEntryStreamingCollection
  property_count: 5
  slug: optimizely-rest-blacklist-entry-streaming-collection
- name: RestBlacklistedEntry
  property_count: 2
  slug: optimizely-rest-blacklisted-entry
- name: RestChunk
  property_count: 2
  slug: optimizely-rest-chunk
- name: RestCount
  property_count: 2
  slug: optimizely-rest-count
- name: RestImage
  property_count: 7
  slug: optimizely-rest-image
- name: RestImageStreamingCollection
  property_count: 5
  slug: optimizely-rest-image-streaming-collection
- name: RestMessageNode
  property_count: 34
  slug: optimizely-rest-message-node
- name: RestMultiPartRequestSchema
  property_count: 2
  slug: optimizely-rest-multi-part-request-schema
- name: RestPersonalizedAttachmentUpload
  property_count: 2
  slug: optimizely-rest-personalized-attachment-upload
- name: RestRecipient
  property_count: 5
  slug: optimizely-rest-recipient
- name: RestRecipientValid
  property_count: 4
  slug: optimizely-rest-recipient-valid
- name: RestSendingBatch
  property_count: 7
  slug: optimizely-rest-sending-batch
- name: RestSendingBatchStreamingCollection
  property_count: 5
  slug: optimizely-rest-sending-batch-streaming-collection
- name: RestSmartCampaign
  property_count: 15
  slug: optimizely-rest-smart-campaign
- name: RestTrackingLink
  property_count: 9
  slug: optimizely-rest-tracking-link
- name: ResultsShareLink
  property_count: 1
  slug: optimizely-results-share-link
- name: Rule
  property_count: 6
  slug: optimizely-rule
- name: RuleInput
  property_count: 5
  slug: optimizely-ruleinput
- name: RulesetInput
  property_count: 1
  slug: optimizely-ruleset-input
- name: Ruleset
  property_count: 1
  slug: optimizely-ruleset
- name: RulesetInput
  property_count: 1
  slug: optimizely-rulesetinput
- name: SchemaFieldInput
  property_count: 4
  slug: optimizely-schema-field-input
- name: SchemaObjectInput
  property_count: 2
  slug: optimizely-schema-object-input
- name: SchemaObject
  property_count: 4
  slug: optimizely-schema-object
- name: SchemaField
  property_count: 4
  slug: optimizely-schemafield
- name: SchemaFieldInput
  property_count: 4
  slug: optimizely-schemafieldinput
- name: SchemaObject
  property_count: 4
  slug: optimizely-schemaobject
- name: SchemaObjectInput
  property_count: 2
  slug: optimizely-schemaobjectinput
- name: Segment
  property_count: 3
  slug: optimizely-segment
- name: Site
  property_count: 4
  slug: optimizely-site
- name: SmartCampaign
  property_count: 5
  slug: optimizely-smartcampaign
- name: SplitRequestData
  property_count: 12
  slug: optimizely-split-request-data
- name: TaskArticle
  property_count: 9
  slug: optimizely-task-article
- name: TaskAssetDraftBrandComplianceRequest
  property_count: 2
  slug: optimizely-task-asset-draft-brand-compliance-request
- name: TaskAssetDraftBrandComplianceResponse
  property_count: 4
  slug: optimizely-task-asset-draft-brand-compliance-response
- name: TaskAssetResponse
  property_count: 9
  slug: optimizely-task-asset-response
- name: TaskImage
  property_count: 11
  slug: optimizely-task-image
- name: TaskRawFile
  property_count: 10
  slug: optimizely-task-raw-file
- name: TaskResponse
  property_count: 15
  slug: optimizely-task-response
- name: Task
  property_count: 11
  slug: optimizely-task
- name: TaskVideo
  property_count: 10
  slug: optimizely-task-video
- name: TaskInput
  property_count: 6
  slug: optimizely-taskinput
- name: TransactionalMailInput
  property_count: 3
  slug: optimizely-transactional-mail-input
- name: TransactionalMailResponse
  property_count: 2
  slug: optimizely-transactional-mail-response
- name: TransactionalMailInput
  property_count: 3
  slug: optimizely-transactionalmailinput
- name: TransactionalMailResponse
  property_count: 2
  slug: optimizely-transactionalmailresponse
- name: UnsubscribeInput
  property_count: 1
  slug: optimizely-unsubscribe-input
- name: Unsubscribe
  property_count: 3
  slug: optimizely-unsubscribe
- name: UnsubscribeInput
  property_count: 1
  slug: optimizely-unsubscribeinput
- name: Variable
  property_count: 3
  slug: optimizely-variable
- name: VariableInput
  property_count: 3
  slug: optimizely-variableinput
- name: Variation
  property_count: 4
  slug: optimizely-variation
- name: VariationInput
  property_count: 2
  slug: optimizely-variationinput
- name: WaitRequestData
  property_count: 10
  slug: optimizely-wait-request-data
json_structures:
- name: Optimizely Structure
  property_count: 0
  slug: optimizely-structure
jsonld:
- class_count: 0
  name: Optimizely Context
  property_count: 12
  slug: optimizely-context
layout: provider
mcp_servers:
- description: Remote MCP server at exp.mcp.opal.optimizely.com requiring OAuth.
  name: Optimizely MCP Server
  slug: optimizely-mcp-yml
modified: '2026-09-16'
name: Optimizely
nav: Providers
network: true
overview: 'Optimizely publishes 414 API contracts indexed on the [APIs.io](https://apis.io/) network, including Assets API, Attributes API, Audiences API, and 411 more. Tagged areas include A/B Testing, Content Management, Customer Data, E-Commerce, and Experimentation.


  The Optimizely catalog on APIs.io includes 3 event-driven AsyncAPI specifications, 1 JSON-LD context, and 3 Spectral governance rulesets.


  Optimizely''s developer surface includes CLI, sandbox, changelog, documentation, API reference, getting-started guide, pricing, and 81 more developer resources.'
plans:
- name: Optimizely Plans Pricing
  plan_count: 0
  slug: optimizely-plans-pricing
random_paper: 6
rate_limits:
- limit_count: 8
  name: Optimizely Rate Limits
  slug: optimizely-rate-limits
rules:
- authorship: generated
  effective_rule_count: 35
  extends:
  - spectral:asyncapi
  name: Optimizely — asyncapi rules
  rule_count: 8
  severity_counts:
    error: 1
    hint: 0
    info: 0
    warn: 7
  slug: optimizely-asyncapi-spectral-rules
- authorship: generated
  effective_rule_count: 6
  extends: []
  name: Optimizely — jsonschema rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: optimizely-jsonschema-spectral-rules
- authorship: generated
  effective_rule_count: 51
  extends:
  - spectral:oas
  name: Optimizely API Rules
  rule_count: 10
  severity_counts:
    error: 6
    hint: 0
    info: 1
    warn: 3
  slug: optimizely-rules
scopes:
- name: Optimizely Scopes
  scope_count: 6
  slug: optimizely-scopes
  summary_line: 6 scopes · authorizationCode/clientCredentials/refreshToken
score:
  band: exemplar
  composite: 77.7
  coverage:
    artifact_dirs: 43
    catalog_earned: 74.8
    catalog_earned_first_party: 12.0
    catalog_gap: 40.3
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -1.9
  facets:
    access_clarity: 60.5
    contract_governance: 35.6
    contract_quality: 70.3
    developer_ergonomics: 58.3
    discoverability: 90.8
    operational_transparency: 92.1
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - united-states
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 79.6
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 97.0
      derived: 3
      marker_coverage: 4.1
      total: 410
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    - jurisdiction: US
      standard: hipaa
    jurisdictions_satisfied: 2
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: flat
  upsert:
    applies: true
    score: 72.2
screenshot: https://apis.io/screenshots/optimizely/optimizely-2026-08-07T190808.png
security:
- kind: authentication
  name: Optimizely Authentication
  slug: optimizely-authentication
  summary_line: oauth2/http/apiKey · 10 schemes
- kind: domain-security
  name: Optimizely Domain Security
  slug: optimizely-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Optimizely Vulnerability Disclosure
  slug: optimizely-vulnerability-disclosure
  summary_line: no policy recorded
- kind: trust-center
  name: Optimizely Trust Center
  slug: optimizely-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA
skill_count: 7
skills:
- name: optimizely-create-flag-and-roll-out
  slug: optimizely-create-flag-and-roll-out
- name: ocp-app-development
  slug: optimizely-ocp-app-development
- name: ocp-app-sdk-v3-migration
  slug: optimizely-ocp-app-sdk-v3-migration
- name: ocp-local-testing
  slug: optimizely-ocp-local-testing
- name: ocp-node22-runtime-migration
  slug: optimizely-ocp-node22-runtime-migration
- name: optimizely-run-a-web-experiment
  slug: optimizely-run-a-web-experiment
- name: optimizely-sync-customer-data-to-odp
  slug: optimizely-sync-customer-data-to-odp
slug: optimizely
tags:
- A/B Testing
- Content Management
- Customer Data
- E-Commerce
- Experimentation
- Feature Flags
- Marketing
- Enterprise
- Digital Experience Platform
- CMS
- Commerce
- Personalization
- GraphQL
- SDK
website: https://www.optimizely.com/
---

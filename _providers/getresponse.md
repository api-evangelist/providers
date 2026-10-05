---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
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
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: true
  schema_version: '0.2'
  score: 47.8
  scored_at: '2026-10-04'
agentic_access:
- acting_count: 94
  human_in_the_loop: 1
  name: Getresponse Agentic Access
  operation_count: 220
  slug: getresponse-agentic-access
  summary_line: 220 operations · 94 acting · 1 human-in-the-loop
api_count: 50
apis:
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: A/B tests API documentation
  name: GetResponse A/B tests API
  phrasing_intents:
  - id: getSplittest
    intent: Get a legacy A/B split test
    question: What are the details of one of my older split tests?
  - id: getSplittestList
    intent: List legacy A/B split tests
    question: Which split tests have I run in the past?
  phrasing_ops: 2
  slug: getresponse-a-b-tests-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: A/B tests - subject API documentation
  name: GetResponse A/B tests - subject API
  phrasing_intents:
  - id: postAbtestsSubjectByIdWinner
    intent: Pick the winner of a subject A/B test
    question: Can I manually choose the winning subject line in an A/B test?
  - id: getAbTestSubjectById
    intent: Get a subject A/B test
    question: What variants and stage is a specific subject-line test in?
  - id: cancelAbTest
    intent: Cancel an A/B test
    question: Can I stop an A/B test that's in progress?
  - id: deleteAbTest
    intent: Delete an A/B test
    question: Which A/B test states allow deletion?
  - id: GetAbTestSubjectList
    intent: List subject A/B tests
    question: Which subject-line A/B tests have I run?
  - id: createSubjectAbTest
    intent: Create a subject A/B test
    question: How do I test two subject lines against each other?
  phrasing_ops: 6
  slug: getresponse-a-b-tests-subject-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Accounts API documentation
  name: GetResponse Accounts API
  phrasing_intents:
  - id: getAccountBlocklist
    intent: View the account blocklist
    question: Which email addresses and domains are on my account-wide blocklist?
  - id: updateAccountBlocklist
    intent: Update the account blocklist
    question: Can I add email addresses or domains to my account-wide blocklist in bulk?
  - id: getAccount
    intent: Get account profile details
    question: What company name, email and time zone are set on my account?
  - id: updateAccount
    intent: Update account profile details
    question: Can I change the company name and phone number on my account through the API?
  - id: getAccountBilling
    intent: Get account billing information
    question: What plan am I on and what are my billing details?
  - id: getTimezones
    intent: List available time zones
    question: Which time zone values can I choose from for my account?
  - id: getCallbacks
    intent: View the callbacks configuration
    question: Are callbacks turned on for my account, and which URL do they hit?
  - id: updateCallbacks
    intent: Enable or change callbacks
    question: How do I get notified at my own URL when contacts subscribe or unsubscribe?
  phrasing_ops: 14
  slug: getresponse-accounts-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Addresses API documentation
  name: GetResponse Addresses API
  phrasing_intents:
  - id: getAddress
    intent: Get a saved address
    question: Can I look up one stored address by its ID?
  - id: updateAddress
    intent: Update a saved address
    question: Can I fix the street or zip on an address I already saved?
  - id: deleteAddress
    intent: Delete a saved address
    question: How do I remove an address record I no longer use?
  - id: getAddressList
    intent: Search saved addresses
    question: Which saved addresses are in a particular city or zip code?
  - id: createAddress
    intent: Save a new address
    question: How do I store a customer shipping or billing address?
  phrasing_ops: 5
  slug: getresponse-addresses-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Autoresponders API documentation
  name: GetResponse Autoresponders API
  phrasing_intents:
  - id: getAutoresponder
    intent: Get an autoresponder
    question: What subject and trigger settings does one of my autoresponders use?
  - id: updateAutoresponder
    intent: Update an autoresponder
    question: Can I change the subject or content of an existing autoresponder?
  - id: deleteAutoresponder
    intent: Delete an autoresponder
    question: How can I remove an autoresponder I don't use anymore?
  - id: getSingleAutoresponderStatistics
    intent: Get statistics for one autoresponder
    question: How well is a particular autoresponder performing?
  - id: getAutoresponderThumbnail
    intent: Get an autoresponder thumbnail image
    question: Is there a preview image of an autoresponder message?
  - id: getAutoresponderList
    intent: List autoresponders
    question: Which autoresponders do I have set up across my lists?
  - id: createAutoresponder
    intent: Create an autoresponder
    question: Can I set up a new time-based autoresponder through the API?
  - id: getAutoresponderStatisticsCollection
    intent: Get combined autoresponder statistics
    question: What are the overall results across all autoresponders in a list?
  phrasing_ops: 8
  slug: getresponse-autoresponders-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: 'Our API v3 uses the terminology from the previous version of GetResponse. **Campaigns and lists are the same resource under a different name.** For now, please refer to lists as campaigns. Our API v4 '
  name: GetResponse Campaigns (Lists) API
  phrasing_intents:
  - id: getCampaignBlocklist
    intent: View a list's blocklist masks
    question: Which emails and domains are blocked from joining one of my GetResponse lists?
  - id: updateCampaignBlocklist
    intent: Update a list's blocklist masks
    question: Can I block certain email domains from subscribing to one specific list?
  - id: getCampaign
    intent: Get one contact list's details
    question: Where can I see the full settings of a single contact list?
  - id: updateCampaign
    intent: Change a contact list's settings
    question: Can I rename or reconfigure an existing contact list?
  - id: getCampaignList
    intent: List my contact lists
    question: What contact lists do I have in my GetResponse account?
  - id: createCampaign
    intent: Create a new contact list
    question: How do I set up a brand new contact list for subscribers?
  - id: getCampaignStatisticsOrigins
    intent: See where a list's subscribers came from
    question: Which sources, like forms or imports, brought subscribers into my list?
  - id: getCampaignStatisticsLocations
    intent: See subscriber locations for a list
    question: What countries are the subscribers on my list located in?
  phrasing_ops: 13
  slug: getresponse-campaigns-lists-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Carts API documentation
  name: GetResponse Carts API
  phrasing_intents:
  - id: getCarts
    intent: List a shop's carts
    question: Which shopping carts exist in my shop, for example abandoned ones?
  - id: createCart
    intent: Record a new shopping cart
    question: How do I send a customer's cart into GetResponse for abandoned cart emails?
  - id: getCart
    intent: Get a cart's details
    question: What items are in one specific cart?
  - id: updateCart
    intent: Update a shopping cart
    question: Can I change the items or total of a cart that already exists?
  - id: deleteCart
    intent: Delete a shopping cart
    question: How do I remove a cart once it's been converted or emptied?
  phrasing_ops: 5
  slug: getresponse-carts-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Categories API documentation
  name: GetResponse Categories API
  phrasing_intents:
  - id: getCategories
    intent: List a shop's product categories
    question: Which product categories exist in my shop?
  - id: createCategory
    intent: Create a shop category
    question: How do I add a new product category to my shop?
  - id: getCategory
    intent: Get a shop category
    question: What are the details of one category in my shop?
  - id: updateCategory
    intent: Update a shop category
    question: Can I rename an existing shop category?
  - id: deleteCategory
    intent: Delete a shop category
    question: How can I remove a category from my shop?
  phrasing_ops: 5
  slug: getresponse-categories-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Click tracking refers to the data collected about each link click, such as how many people clicked it, how many clicks resulted in desired actions such as sales, forwards or subscriptions.
  name: GetResponse Click Tracks API
  phrasing_intents:
  - id: getClickTrackById
    intent: Get a tracked link
    question: How many clicks did one tracked link get?
  - id: getClickTrackList
    intent: List tracked links
    question: Which links in my messages are being click-tracked?
  phrasing_ops: 2
  slug: getresponse-click-tracks-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: API documentation for contacts and their properties (e.g., tags, custom fields)
  name: GetResponse Contacts API
  phrasing_intents:
  - id: getActivities
    intent: List a contact's recent activities
    question: What has a particular contact opened or clicked recently?
  - id: getContactsFromCampaign
    intent: List the contacts on one list
    question: Who is subscribed to one specific contact list?
  - id: upsertContactCustoms
    intent: Add or update a contact's custom fields
    question: Can I set custom field values on a contact without wiping the others?
  - id: upsertTags
    intent: Add tags to a contact
    question: How do I tag a subscriber without losing the tags they already have?
  - id: getContactById
    intent: Get a contact's details
    question: What information is stored about one particular subscriber?
  - id: updateContact
    intent: Update a contact's details
    question: Can I change a subscriber's name or move them to another list?
  - id: deleteContact
    intent: Delete a contact
    question: How do I permanently remove a subscriber from my account?
  - id: getContactList
    intent: Search contacts across all lists
    question: Which contacts across my whole account match a given email?
  phrasing_ops: 11
  slug: getresponse-contacts-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Custom Events API documentation
  name: GetResponse Custom Events API
  phrasing_intents:
  - id: getCustomEventById
    intent: Get a custom event
    question: What attributes does one of my custom events define?
  - id: updateCustomEvent
    intent: Update a custom event
    question: Can I rename a custom event or change its attributes?
  - id: deleteCustomEvent
    intent: Delete a custom event
    question: How do I remove a custom event definition I no longer track?
  - id: getCustomEventsList
    intent: List custom events
    question: Which custom events are defined on my account?
  - id: createCustomEvent
    intent: Define a new custom event
    question: Can I define my own event type to use in automation workflows?
  - id: triggerCustomEvent
    intent: Trigger a custom event for a contact
    question: How do I fire a custom event for a specific contact?
  phrasing_ops: 6
  slug: getresponse-custom-events-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Custom Fields API documentation
  name: GetResponse Custom Fields API
  phrasing_intents:
  - id: getCustomFieldById
    intent: Get a custom field definition
    question: What type and allowed values does one of my custom fields have?
  - id: updateCustomField
    intent: Change a custom field's values or visibility
    question: Can I change the allowed values of an existing custom field?
  - id: deleteCustomField
    intent: Delete a custom field
    question: How do I get rid of a custom field I no longer use?
  - id: getCustomFieldList
    intent: List custom fields
    question: Which custom fields are defined in my account?
  - id: createCustomField
    intent: Create a custom field
    question: How do I add a new custom field like birthday or company to contacts?
  phrasing_ops: 5
  slug: getresponse-custom-fields-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Custom Reports API documentation
  name: GetResponse Custom Reports API
  phrasing_intents:
  - id: getCustomReportDetails
    intent: Get a custom report's data
    question: Can I see the results of one scheduled custom report?
  - id: getCustomReportList
    intent: List custom reports
    question: Which custom reports have I scheduled?
  - id: createCustomReport
    intent: Schedule a custom report
    question: How do I schedule a recurring report for a specific time period?
  phrasing_ops: 3
  slug: getresponse-custom-reports-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Ecommerce API from GetResponse — 2 operation(s) for ecommerce.
  name: GetResponse Ecommerce API
  phrasing_intents:
  - id: getRevenueStats
    intent: Get ecommerce revenue statistics
    question: How much revenue did my shops generate from email marketing?
  - id: getGeneralPerformanceStats
    intent: Get ecommerce performance statistics
    question: What are my overall ecommerce performance metrics like orders and conversions?
  phrasing_ops: 2
  slug: getresponse-ecommerce-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: File Library API documentation
  name: GetResponse File Library API
  phrasing_intents:
  - id: getFileById
    intent: Get a file from the file library
    question: Can I get the details and URL of one file in my library?
  - id: deleteFile
    intent: Delete a file from the library
    question: How do I remove an uploaded file I no longer need?
  - id: deleteFolder
    intent: Delete a file library folder
    question: Can I delete a whole folder from my file library?
  - id: quota
    intent: Check file library storage usage
    question: How much storage space do I have left in my file library?
  - id: getFileList
    intent: List files in the file library
    question: Which files are in my library, including those in subfolders?
  - id: createFile
    intent: Upload a file to the library
    question: How do I upload a file to my GetResponse file library?
  - id: getFolderList
    intent: List file library folders
    question: What folders exist in my file library?
  - id: createFolder
    intent: Create a file library folder
    question: Can I organise my uploads into a new folder?
  phrasing_ops: 8
  slug: getresponse-file-library-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Form and Popup API from GetResponse — 1 operation(s) for form and popup.
  name: GetResponse Form and Popup API
  phrasing_intents:
  - id: getPopupGeneralPerformance
    intent: Get a form or popup's performance
    question: How is a particular form or popup performing on views and signups?
  phrasing_ops: 1
  slug: getresponse-form-and-popup-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Forms and Popups API documentation
  name: GetResponse Forms and Popups API
  phrasing_intents:
  - id: getPopupDetails
    intent: Get a form or popup
    question: What are the settings of one of my signup forms or popups?
  - id: getPopupsList
    intent: List forms and popups
    question: Which of my forms and popups collect the most leads?
  phrasing_ops: 2
  slug: getresponse-forms-and-popups-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Forms API documentation
  name: GetResponse Forms API
  phrasing_intents:
  - id: getForm
    intent: Get a signup form
    question: Can I look up one of my signup forms by ID?
  - id: getFormVariantList
    intent: List a form's A/B test variants
    question: Which A/B test variants exist for one of my forms?
  - id: getFormList
    intent: List my signup forms
    question: Which of my signup forms have the best subscription rate?
  phrasing_ops: 3
  slug: getresponse-forms-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: From Fields API documentation
  name: GetResponse From Fields API
  phrasing_intents:
  - id: getFromFieldById
    intent: Get a sender (From) address
    question: What name and email does one of my From addresses use?
  - id: deleteFromField
    intent: Delete a sender (From) address
    question: Can I remove a sender address and swap in another one where it was used?
  - id: setFromFieldAsDefault
    intent: Make a sender address the default
    question: How do I change which From address is used by default?
  - id: getFromFieldList
    intent: List sender (From) addresses
    question: Which sender addresses are set up on my account?
  - id: createFromField
    intent: Add a sender (From) address
    question: How do I add a new sender email address?
  phrasing_ops: 5
  slug: getresponse-from-fields-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The GDPR Fields API from GetResponse — 2 operation(s) for gdpr fields.
  name: GetResponse GDPR Fields API
  phrasing_intents:
  - id: getGDPRField
    intent: Get a GDPR consent field
    question: What consent text does one of my GDPR fields contain?
  - id: getGDPRFieldList
    intent: List GDPR consent fields
    question: Which GDPR consent fields have I defined?
  phrasing_ops: 2
  slug: getresponse-gdpr-fields-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Imports API documentation
  name: GetResponse Imports API
  phrasing_intents:
  - id: getImportById
    intent: Get a contact import
    question: Has my contact import finished, and how many contacts were added?
  - id: getImportList
    intent: List contact imports
    question: Which contact imports have I run?
  - id: createImport
    intent: Schedule a contact import
    question: How do I add many contacts to a list in one call?
  phrasing_ops: 3
  slug: getresponse-imports-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Landing Page API from GetResponse — 1 operation(s) for landing page.
  name: GetResponse Landing Page API
  phrasing_intents:
  - id: getLpsGeneralPerformanceStats
    intent: Get a landing page's performance
    question: How many visits and conversions did one landing page get?
  phrasing_ops: 1
  slug: getresponse-landing-page-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Landing Pages API from GetResponse — 2 operation(s) for landing pages.
  name: GetResponse Landing Pages API
  phrasing_intents:
  - id: getLpsById
    intent: Get a landing page
    question: What are the details of one of my current landing pages?
  - id: getLpsList
    intent: List landing pages
    question: Which landing pages have the best subscription rate?
  phrasing_ops: 2
  slug: getresponse-landing-pages-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Legacy Forms API documentation
  name: GetResponse Legacy Forms API
  phrasing_intents:
  - id: getLegacyFormById
    intent: Get a legacy web form
    question: Can I look up one of my older legacy web forms by ID?
  - id: getLegacyFormList
    intent: List legacy web forms
    question: Which legacy web forms do I still have?
  phrasing_ops: 2
  slug: getresponse-legacy-forms-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Legacy Landing Pages description
  name: GetResponse Legacy Landing Pages API
  phrasing_intents:
  - id: getLandingPageById
    intent: Get a legacy landing page
    question: What are the details of one landing page built in the old editor?
  - id: getLandingPageList
    intent: List legacy landing pages
    question: Which legacy landing pages are published on which domains?
  phrasing_ops: 2
  slug: getresponse-legacy-landing-pages-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Meta Fields API documentation
  name: GetResponse Meta Fields API
  phrasing_intents:
  - id: getMetaFields
    intent: List a shop's meta fields
    question: What meta fields are defined for my shop?
  - id: createMetaField
    intent: Create a shop meta field
    question: How do I add a custom meta field to my shop?
  - id: getMetaField
    intent: Get a shop meta field
    question: Can I look up one meta field by ID in my shop?
  - id: updateMetaField
    intent: Update a shop meta field
    question: Can I change the value of an existing shop meta field?
  - id: deleteMetaField
    intent: Delete a shop meta field
    question: How do I remove a meta field from my shop?
  phrasing_ops: 5
  slug: getresponse-meta-fields-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Multimedia API documentation
  name: GetResponse Multimedia API
  phrasing_intents:
  - id: getImageList
    intent: List uploaded images
    question: What images have I uploaded for use in my emails?
  - id: uploadImage
    intent: Upload an image
    question: How do I upload an image to use in my newsletters?
  phrasing_ops: 2
  slug: getresponse-multimedia-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Newsletters API documentation
  name: GetResponse Newsletters API
  phrasing_intents:
  - id: getNewsletter
    intent: Get a newsletter
    question: What subject, content and send settings does a particular newsletter have?
  - id: deleteNewsletter
    intent: Delete a newsletter
    question: Can I permanently remove a newsletter I no longer need?
  - id: getNewsletterActivities
    intent: List a newsletter's contact activities
    question: Which contacts opened or clicked a specific newsletter?
  - id: cancelMessageSend
    intent: Cancel sending a newsletter
    question: Can I stop a newsletter that's already queued to go out?
  - id: getSingleNewsletterStatistics
    intent: Get statistics for one newsletter
    question: How did one specific newsletter perform on opens and clicks?
  - id: getNewsletterThumbnail
    intent: Get a newsletter thumbnail image
    question: Is there a preview image of what a newsletter looks like?
  - id: getNewsletterList
    intent: List newsletters
    question: Which newsletters have I sent or scheduled recently?
  - id: createNewsletter
    intent: Create and queue a newsletter
    question: How do I create a new newsletter and send it to a list?
  phrasing_ops: 10
  slug: getresponse-newsletters-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Orders API documentation
  name: GetResponse Orders API
  phrasing_intents:
  - id: getOrderList
    intent: List a shop's orders
    question: Which orders have come into my shop recently?
  - id: createOrder
    intent: Record a new shop order
    question: How do I record a purchase made by a contact?
  - id: getOrderById
    intent: Get a shop order
    question: What are the details of one particular order?
  - id: updateOrder
    intent: Update a shop order
    question: Can I change the status of an order I already recorded?
  - id: deleteOrder
    intent: Delete a shop order
    question: How can I remove an order from my shop?
  phrasing_ops: 5
  slug: getresponse-orders-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Predefined Fields API documentation
  name: GetResponse Predefined Fields API
  phrasing_intents:
  - id: getPredefinedFieldById
    intent: Get a predefined field
    question: What value does one of my predefined fields hold?
  - id: updatePredefinedField
    intent: Change a predefined field's value
    question: Can I change the text a predefined field inserts into my messages?
  - id: deletePredefinedField
    intent: Delete a predefined field
    question: How do I remove a predefined field I don't use anymore?
  - id: getPredefinedFieldList
    intent: List predefined fields
    question: What predefined fields exist for my lists?
  - id: createPredefinedField
    intent: Create a predefined field
    question: Can I create a reusable value to insert into emails for a list?
  phrasing_ops: 5
  slug: getresponse-predefined-fields-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Product Variants API documentation
  name: GetResponse Product Variants API
  phrasing_intents:
  - id: getProductVariantList
    intent: List a product's variants
    question: Which variants exist for a given product in my shop?
  - id: createProductVariant
    intent: Add a product variant
    question: How do I add a new size or color variant to a product?
  - id: getProductVariantById
    intent: Get a product variant
    question: What are the price and stock details of one product variant?
  - id: updateProductVariant
    intent: Update a product variant
    question: Can I change an existing variant's properties?
  - id: deleteProductVariant
    intent: Delete a product variant
    question: How do I remove a variant from a product?
  phrasing_ops: 5
  slug: getresponse-product-variants-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Products API documentation
  name: GetResponse Products API
  phrasing_intents:
  - id: getProductList
    intent: List a shop's products
    question: Which products are in one of my GetResponse shops?
  - id: createProduct
    intent: Add a product to a shop
    question: How do I add a new product to my shop catalog?
  - id: getProductById
    intent: Get a product's details
    question: What details are stored for one product in my shop?
  - id: updateProduct
    intent: Update a product's properties
    question: Can I change just the price or name of an existing product?
  - id: deleteProduct
    intent: Delete a product
    question: How do I remove a discontinued product from my shop?
  - id: upsertProductCategories
    intent: Assign categories to a product
    question: Can I put a product into categories and set its default category?
  - id: upsertMetaFields
    intent: Assign meta fields to a product
    question: Can I attach extra metadata fields to a product?
  phrasing_ops: 7
  slug: getresponse-products-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: RSS Newsletters API documentation
  name: GetResponse RSS Newsletters API
  phrasing_intents:
  - id: getRssNewsletterById
    intent: Get an RSS newsletter's settings
    question: What feed URL and send settings does one RSS newsletter use?
  - id: updateRssNewsletter
    intent: Update an RSS newsletter
    question: Can I change the feed URL or subject of an existing RSS newsletter?
  - id: deleteRssNewsletter
    intent: Delete an RSS newsletter
    question: How do I stop and remove an RSS-driven newsletter for good?
  - id: getSingleRssNewsletterStatisticsCollection
    intent: Get stats for one RSS newsletter
    question: How is one particular RSS newsletter performing?
  - id: getRssNewslettersList
    intent: List my RSS newsletters
    question: What RSS newsletters have I set up?
  - id: createRssNewsletter
    intent: Create an RSS-to-email newsletter
    question: How do I turn a blog RSS feed into an automatic email newsletter?
  - id: getRssNewsletterStatisticsCollection
    intent: Get stats across all RSS newsletters
    question: What are the combined statistics for all my RSS newsletters?
  phrasing_ops: 7
  slug: getresponse-rss-newsletters-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Search Contacts API documentation API documentation
  name: GetResponse Search Contacts API
  phrasing_intents:
  - id: getSearchContactsById
    intent: Get a saved segment definition
    question: What conditions make up one of my saved contact segments?
  - id: updateSearchContacts
    intent: Update a saved segment
    question: Can I change the conditions of a segment I already saved?
  - id: deleteSearchContacts
    intent: Delete a saved segment
    question: How do I remove a saved contact segment I no longer use?
  - id: getContactsByIdSearchContacts
    intent: List contacts in a saved segment
    question: Which contacts currently match one of my saved segments?
  - id: upsertCustomFieldsBySearchContactId
    intent: Set custom fields for a whole segment
    question: Can I update a custom field for every contact in a segment at once?
  - id: getSearchContactsList
    intent: List saved segments
    question: Which saved contact segments (custom filters) do I have?
  - id: newSearchContacts
    intent: Create a saved segment
    question: How do I save a new contact segment for later reuse?
  - id: getContactsFromSearchContactsConditions
    intent: Find contacts matching ad-hoc conditions
    question: Can I search contacts by conditions without saving a segment first?
  phrasing_ops: 8
  slug: getresponse-search-contacts-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Shops API documentation
  name: GetResponse Shops API
  phrasing_intents:
  - id: getShopById
    intent: Get a shop's details
    question: What settings does one of my GetResponse shops have?
  - id: updateShop
    intent: Update shop preferences
    question: Can I change a shop's name, currency or locale?
  - id: deleteShop
    intent: Delete a shop
    question: How do I delete a shop I no longer sell through?
  - id: getShopList
    intent: List my shops
    question: Which ecommerce shops are connected to my account?
  - id: createShop
    intent: Create a shop
    question: How do I set up a new shop to sync ecommerce data?
  phrasing_ops: 5
  slug: getresponse-shops-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Sms API from GetResponse — 1 operation(s) for sms.
  name: GetResponse Sms API
  phrasing_intents:
  - id: getSmsStats
    intent: Get statistics for an SMS message
    question: How many recipients received and clicked one SMS message?
  phrasing_ops: 1
  slug: getresponse-sms-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: SMS Automation Messages API documentation
  name: GetResponse SMS Automation Messages API
  phrasing_intents:
  - id: getSmsAutomationById
    intent: Get an automated SMS message
    question: What does one of my automated SMS messages say?
  - id: getSMSAutomationList
    intent: List automated SMS messages
    question: Which automated SMS messages do I have in workflows?
  phrasing_ops: 2
  slug: getresponse-sms-automation-messages-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: SMS Messages API documentation
  name: GetResponse SMS Messages API
  phrasing_intents:
  - id: getSmsById
    intent: Get an SMS message
    question: What content and sending status does one SMS message have?
  - id: getSMSList
    intent: List SMS messages
    question: Which SMS messages have I sent or scheduled?
  - id: sendSms
    intent: Send an SMS message
    question: How do I send a text message to my contacts?
  - id: getSmsSenderNameList
    intent: List SMS sender names
    question: Which sender names can I use for text messages?
  phrasing_ops: 4
  slug: getresponse-sms-messages-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Subscription Confirmations API documentation
  name: GetResponse Subscription Confirmations API
  phrasing_intents:
  - id: getSubscriptionConfirmationBodyList
    intent: List confirmation email bodies
    question: What message body templates are available for double opt-in confirmation emails?
  - id: getSubscriptionConfirmationSubjectList
    intent: List confirmation email subjects
    question: Which subject lines can I use for subscription confirmation emails?
  phrasing_ops: 2
  slug: getresponse-subscription-confirmations-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Suppressions API documentaion
  name: GetResponse Suppressions API
  phrasing_intents:
  - id: getSuppressionById
    intent: Get a suppression list
    question: Which masks are in one of my suppression lists?
  - id: updateSuppression
    intent: Update a suppression list
    question: Can I rename a suppression list or change its masks?
  - id: deleteSuppression
    intent: Delete a suppression list
    question: How do I remove a suppression list I don't need?
  - id: getSuppressionsList
    intent: List suppression lists
    question: Which suppression lists have I created?
  - id: createSuppression
    intent: Create a suppression list
    question: How do I make a list of addresses to exclude from sends?
  phrasing_ops: 5
  slug: getresponse-suppressions-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Tags API documentation
  name: GetResponse Tags API
  phrasing_intents:
  - id: getTagById
    intent: Get a tag
    question: Can I look up one tag by its ID?
  - id: updateTag
    intent: Fetch a tag via the no-op update call
    question: Can I rename a tag or change its color after creating it?
  - id: deleteTag
    intent: Delete a tag
    question: How do I delete a tag I don't use anymore?
  - id: getTagsList
    intent: List my tags
    question: Which tags exist in my account?
  - id: createTag
    intent: Create a tag
    question: How do I create a new tag for segmenting contacts?
  phrasing_ops: 5
  slug: getresponse-tags-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Taxes API documentation
  name: GetResponse Taxes API
  phrasing_intents:
  - id: getTaxList
    intent: List a shop's taxes
    question: Which tax rates are defined in my shop?
  - id: createTax
    intent: Create a shop tax
    question: How do I add a new tax rate to my shop?
  - id: getTaxById
    intent: Get a shop tax
    question: What rate is set on one particular tax?
  - id: updateTax
    intent: Update a shop tax
    question: Can I change the rate of an existing tax?
  - id: deleteTax
    intent: Delete a shop tax
    question: How do I remove a tax from my shop?
  phrasing_ops: 5
  slug: getresponse-taxes-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Tracking API documentation
  name: GetResponse Tracking API
  phrasing_intents:
  - id: getTracking
    intent: Get tracking code snippets
    question: Where do I get the JavaScript to track purchases and abandoned carts?
  - id: getFacebookPixelList
    intent: List connected Facebook Pixels
    question: Which Facebook Pixels are connected to my account?
  phrasing_ops: 2
  slug: getresponse-tracking-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Transactional Emails API documentation
  name: GetResponse Transactional Emails API
  phrasing_intents:
  - id: getTransactionalEmailsById
    intent: Get a transactional email
    question: What was sent in one specific transactional email?
  - id: getTransactionalEmailsList
    intent: List transactional emails
    question: Which transactional emails went out in a given period?
  - id: createTransactionalEmail
    intent: Send a transactional email
    question: How do I send a one-off transactional email like a receipt?
  - id: getTransactionalEmailsStatistics
    intent: Get transactional email statistics
    question: How are my transactional emails performing overall?
  phrasing_ops: 4
  slug: getresponse-transactional-emails-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Transactional Emails Templates API from GetResponse — 2 operation(s) for transactional emails templates.
  name: GetResponse Transactional Emails Templates API
  phrasing_intents:
  - id: getTransactionalEmailsTemplatesById
    intent: Get a transactional email template
    question: Can I view the content of one transactional email template?
  - id: updateTransactionalEmailsTemplate
    intent: Update a transactional email template
    question: Can I change the subject or HTML of an existing transactional template?
  - id: deleteTransactionalEmailsTemplate
    intent: Delete a transactional email template
    question: How do I remove a transactional email template I no longer send?
  - id: getTransactionalEmailsTemplatesList
    intent: List transactional email templates
    question: Which transactional email templates do I have?
  - id: createTransactionalEmailTemplate
    intent: Create a transactional email template
    question: How do I create a template for order confirmation emails?
  phrasing_ops: 5
  slug: getresponse-transactional-emails-templates-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Webinars API documentation
  name: GetResponse Webinars API
  phrasing_intents:
  - id: getWebinarById
    intent: Get a webinar's details
    question: Can I look up one webinar by ID?
  - id: getWebinarList
    intent: List my webinars
    question: Which webinars do I have scheduled or finished?
  phrasing_ops: 2
  slug: getresponse-webinars-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: The Website API from GetResponse — 1 operation(s) for website.
  name: GetResponse Website API
  phrasing_intents:
  - id: getWbeGeneralPerformanceStats
    intent: Get a website's performance
    question: How much traffic did one of my websites get?
  phrasing_ops: 1
  slug: getresponse-website-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Websites API documentation
  name: GetResponse Websites API
  phrasing_intents:
  - id: getWebsiteById
    intent: Get a website
    question: What are the details of one website I built?
  - id: getWebsitesList
    intent: List websites
    question: Which of my websites get the most page views?
  phrasing_ops: 2
  slug: getresponse-websites-api
- baseURL: https://api.getresponse.com/v3
  baseurl_source: declared
  description: Workflows API documentation
  name: GetResponse Workflows API
  phrasing_intents:
  - id: getWorkflow
    intent: Get an automation workflow
    question: Can I see the details of one automation workflow?
  - id: updateWorkflow
    intent: Turn an automation workflow on or off
    question: How do I pause or activate an automation workflow?
  - id: getWorkflowList
    intent: List automation workflows
    question: Which automation workflows exist in my account?
  phrasing_ops: 3
  slug: getresponse-workflows-api
artifact_total: 106
asyncapis:
- description: ''
  name: Getresponse Webhooks
  slug: getresponse-webhooks
collections:
- collection_type: open
  name: GetResponse APIv3 A/B tests - subject
  slug: open-getresponse-a-b-tests-subject
- collection_type: open
  name: GetResponse APIv3 A/B tests
  slug: open-getresponse-a-b-tests
- collection_type: open
  name: GetResponse APIv3 Accounts
  slug: open-getresponse-accounts
- collection_type: open
  name: GetResponse APIv3 Addresses
  slug: open-getresponse-addresses
- collection_type: open
  name: GetResponse APIv3 Autoresponders
  slug: open-getresponse-autoresponders
- collection_type: open
  name: GetResponse APIv3 Campaigns (Lists)
  slug: open-getresponse-campaigns-lists
- collection_type: open
  name: GetResponse APIv3 Carts
  slug: open-getresponse-carts
- collection_type: open
  name: GetResponse APIv3 Categories
  slug: open-getresponse-categories
- collection_type: open
  name: GetResponse APIv3 Click Tracks
  slug: open-getresponse-click-tracks
- collection_type: open
  name: GetResponse APIv3 Contacts
  slug: open-getresponse-contacts
- collection_type: open
  name: GetResponse APIv3 Custom Events
  slug: open-getresponse-custom-events
- collection_type: open
  name: GetResponse APIv3 Custom Fields
  slug: open-getresponse-custom-fields
- collection_type: open
  name: GetResponse APIv3 Custom Reports
  slug: open-getresponse-custom-reports
- collection_type: open
  name: GetResponse APIv3 Ecommerce
  slug: open-getresponse-ecommerce
- collection_type: open
  name: GetResponse APIv3 File Library
  slug: open-getresponse-file-library
- collection_type: open
  name: GetResponse APIv3 Form and Popup
  slug: open-getresponse-form-and-popup
- collection_type: open
  name: GetResponse APIv3 Forms and Popups
  slug: open-getresponse-forms-and-popups
- collection_type: open
  name: GetResponse APIv3 Forms
  slug: open-getresponse-forms
- collection_type: open
  name: GetResponse APIv3 From Fields
  slug: open-getresponse-from-fields
- collection_type: open
  name: GetResponse APIv3 GDPR Fields
  slug: open-getresponse-gdpr-fields
- collection_type: open
  name: GetResponse APIv3 Imports
  slug: open-getresponse-imports
- collection_type: open
  name: GetResponse APIv3 Landing Page
  slug: open-getresponse-landing-page
- collection_type: open
  name: GetResponse APIv3 Landing Pages
  slug: open-getresponse-landing-pages
- collection_type: open
  name: GetResponse APIv3 Legacy Forms
  slug: open-getresponse-legacy-forms
- collection_type: open
  name: GetResponse APIv3 Legacy Landing Pages
  slug: open-getresponse-legacy-landing-pages
- collection_type: open
  name: GetResponse APIv3 Meta Fields
  slug: open-getresponse-meta-fields
- collection_type: open
  name: GetResponse APIv3 Multimedia
  slug: open-getresponse-multimedia
- collection_type: open
  name: GetResponse APIv3 Newsletters
  slug: open-getresponse-newsletters
- collection_type: open
  name: GetResponse APIv3 Orders
  slug: open-getresponse-orders
- collection_type: open
  name: GetResponse APIv3 Predefined Fields
  slug: open-getresponse-predefined-fields
- collection_type: open
  name: GetResponse APIv3 Product Variants
  slug: open-getresponse-product-variants
- collection_type: open
  name: GetResponse APIv3 Products
  slug: open-getresponse-products
- collection_type: open
  name: GetResponse APIv3 RSS Newsletters
  slug: open-getresponse-rss-newsletters
- collection_type: open
  name: GetResponse APIv3 Search Contacts
  slug: open-getresponse-search-contacts
- collection_type: open
  name: GetResponse APIv3 Shops
  slug: open-getresponse-shops
- collection_type: open
  name: GetResponse APIv3 SMS Automation Messages
  slug: open-getresponse-sms-automation-messages
- collection_type: open
  name: GetResponse APIv3 SMS Messages
  slug: open-getresponse-sms-messages
- collection_type: open
  name: GetResponse APIv3 Sms
  slug: open-getresponse-sms
- collection_type: open
  name: GetResponse APIv3 Subscription Confirmations
  slug: open-getresponse-subscription-confirmations
- collection_type: open
  name: GetResponse APIv3 Suppressions
  slug: open-getresponse-suppressions
- collection_type: open
  name: GetResponse APIv3 Tags
  slug: open-getresponse-tags
- collection_type: open
  name: GetResponse APIv3 Taxes
  slug: open-getresponse-taxes
- collection_type: open
  name: GetResponse APIv3 Tracking
  slug: open-getresponse-tracking
- collection_type: open
  name: GetResponse APIv3 Transactional Emails Templates
  slug: open-getresponse-transactional-emails-templates
- collection_type: open
  name: GetResponse APIv3 Transactional Emails
  slug: open-getresponse-transactional-emails
- collection_type: open
  name: GetResponse APIv3 Webinars
  slug: open-getresponse-webinars
- collection_type: open
  name: GetResponse APIv3 Website
  slug: open-getresponse-website
- collection_type: open
  name: GetResponse APIv3 Websites
  slug: open-getresponse-websites
- collection_type: open
  name: GetResponse APIv3 Workflows
  slug: open-getresponse-workflows
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/capabilities/getresponse-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/getresponse-capability-edges.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/openapi/_original/getresponse-open-api-original.json
  title: ''
  type: OpenAPI
  url: openapi/_original/getresponse-open-api-original.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/well-known/getresponse-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/getresponse-well-known.yml
- group: other
  title: ''
  type: APICatalog
  url: https://www.getresponse.com/.well-known/api-catalog
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/llms/getresponse-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/getresponse-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/packages/getresponse-packages.yml
  title: ''
  type: Packages
  url: packages/getresponse-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/packages/getresponse-packages.yml
  title: ''
  type: SDKs
  url: packages/getresponse-packages.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/authentication/getresponse-authentication.yml
  title: ''
  type: Authentication
  url: authentication/getresponse-authentication.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/scopes/getresponse-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/getresponse-scopes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/conventions/getresponse-conventions.yml
  title: ''
  type: Conventions
  url: conventions/getresponse-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/errors/getresponse-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/getresponse-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/errors/getresponse-problem-types.yml
  title: ''
  type: ErrorCodes
  url: errors/getresponse-problem-types.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/rate-limits/getresponse-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/getresponse-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/plans/getresponse-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/getresponse-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/lifecycle/getresponse-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/getresponse-lifecycle.yml
- group: operate
  title: ''
  type: StatusPage
  url: https://status.getresponse.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/asyncapi/getresponse-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/getresponse-webhooks.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/conformance/getresponse-conformance.yml
  title: ''
  type: Conformance
  url: conformance/getresponse-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.getresponse.com/security
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/security/getresponse-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/getresponse-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/security/getresponse-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/getresponse-domain-security.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/data-model/getresponse-data-model.yml
  title: ''
  type: DataModel
  url: data-model/getresponse-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/overlays/getresponse-openapi-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/getresponse-openapi-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/agentic-access/getresponse-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/getresponse-agentic-access.yml
- group: build
  title: ''
  type: Postman
  url: https://apidocs.getresponse.com/v3/collections
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/collections/getresponse.postman_collection.json
  title: ''
  type: PostmanCollection
  url: collections/getresponse.postman_collection.json
- group: company
  title: ''
  type: Website
  url: https://www.getresponse.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://apidocs.getresponse.com/v3
- group: docs
  title: ''
  type: Documentation
  url: https://apidocs.getresponse.com/v3
- group: docs
  title: ''
  type: APIReference
  url: https://apireference.getresponse.com/
- group: start
  title: ''
  type: GettingStarted
  url: https://apidocs.getresponse.com/v3/authentication
- group: operate
  title: ''
  type: Support
  url: https://www.getresponse.com/help
- group: company
  title: ''
  type: Blog
  url: https://www.getresponse.com/blog
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/GetResponse
- group: commercial
  title: ''
  type: Pricing
  url: https://www.getresponse.com/pricing
- group: start
  title: ''
  type: SignUp
  url: https://app.getresponse.com/create_account
- group: start
  title: ''
  type: Login
  url: https://app.getresponse.com/login
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.getresponse.com/legal/terms-us
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.getresponse.com/legal/privacy-us
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/getresponse
created: '2026-05-11'
description: GetResponse is an all-in-one marketing platform for email marketing, marketing automation, landing pages, websites, webinars, SMS, web push, ecommerce and content monetization, used by small businesses, marketers and enterprises. The GetResponse API v3 is a JSON REST API authenticated with an X-Auth-Token header carrying an API key prefixed with "api-key ", or with OAuth 2.0. The provider publishes a machine-readable OpenAPI 3.0.0 describing 220 operations across 141 paths and 42 product areas — contacts, campaigns, newsletters, autoresponders, transactional email, SMS, forms and popups, landing pages, websites, webinars, workflows, imports, suppressions and a full ecommerce tree of shops, products, variants, categories, carts, orders and taxes. The spec is discoverable through an RFC 9727 API catalog at /.well-known/api-catalog, and GetResponse also publishes an llms.txt and its own Agent Skill for the public API. Enterprise customers run on the separate GetResponse MAX platform,
  which requires an additional X-Domain header.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/getresponse.png
layout: provider
modified: '2026-08-13'
name: GetResponse
nav: Providers
network: true
overview: 'GetResponse publishes 49 APIs on the [APIs.io](https://apis.io/) network, including A/B tests API, A/B tests - subject API, Accounts API, and 46 more. Tagged areas include Email Marketing, Marketing Automation, Landing Pages, Webinars, and Conversion Funnels.


  The GetResponse catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  GetResponse''s developer surface includes authentication, documentation, API reference, getting-started guide, support, engineering blog, pricing, and 34 more developer resources.'
plans:
- name: Getresponse Plans Pricing
  plan_count: 4
  slug: getresponse-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 3
  name: Getresponse Rate Limits
  slug: getresponse-rate-limits
scopes:
- name: Getresponse Scopes
  scope_count: 1
  slug: getresponse-scopes
  summary_line: 1 scope · implicit/authorizationCode/clientCredentials
score:
  band: exemplar
  composite: 72.1
  coverage:
    artifact_dirs: 24
    catalog_earned: 64.0
    catalog_earned_first_party: 24.0
    catalog_gap: 51.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 85.5
    contract_governance: 4.5
    contract_quality: 60.0
    developer_ergonomics: 76.2
    discoverability: 89.3
    operational_transparency: 57.9
  previous_composite: 71.6
  provenance:
    agentic_access: derived
    conformance: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 49
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    jurisdictions:
    - jurisdiction: EU
      standard: gdpr
    jurisdictions_satisfied: 1
    matched_via: tags
    regime: Telecommunications
    regime_id: telecommunications
    score: 43.3
  schema_version: 0.23.0
  scored_at: '2026-10-04'
  trend: flat
  upsert:
    applies: true
    score: 50.0
screenshot: https://raw.githubusercontent.com/api-evangelist/getresponse/refs/heads/main/screenshots/getresponse-2026-06-20T181811.png
security:
- kind: authentication
  name: Getresponse Authentication
  slug: getresponse-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Getresponse Domain Security
  slug: getresponse-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Getresponse Trust Center
  slug: getresponse-trust-center
  summary_line: SOC 2, PCI DSS, GDPR
slug: getresponse
tags:
- Email Marketing
- Marketing Automation
- Landing Pages
- Webinars
- Conversion Funnels
- CRM
- Transactional Email
- SMS
- E-Commerce
- Web Push
- Forms
- Newsletters
- Autoresponders
- Contacts
- Marketing
website: https://www.getresponse.com
---

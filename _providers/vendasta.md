---
access_model:
  confidence: high
  label: Paid
  onboarding: unknown
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  - scopes
  - rate-limits
  - security
  - sandbox
  trial: false
  try_now: false
agent_readiness:
  band: agent-native
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: documented
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: true
    idempotency: verified
    mcp_server: false
    mcp_tool_quality: na
    openapi_examples: partial
    operation_distinctiveness: false
    pagination_ratio: partial
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 40.2
  scored_at: '2026-11-06'
agentic_access:
- acting_count: 128
  human_in_the_loop: 0
  name: Vendasta Agentic Access
  operation_count: 396
  slug: vendasta-agentic-access
  summary_line: 396 operations · 128 acting
api_count: 31
apis:
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Account APIs allow you to perform actions against a single account that your application has been added to.
  name: Vendasta Account API
  phrasing_intents:
  - id: getAccount
    intent: List business accounts
    question: Which business accounts can my app see on Vendasta?
  - id: getAccountByAccountId
    intent: Get a business account
    question: What basic details does a single business account record hold?
  - id: getAccountByAccountIdRichdata
    intent: Get an account's hours, images and extended data
    question: Where can I find a business's hours of operation and images?
  - id: getAccountByAccountIdSettings
    intent: Get an account's market and branding settings
    question: Which market is an account assigned to, and what partner branding applies?
  - id: getAccountByAccountIdSessionTransfer
    intent: Get a session transfer URL for an account
    question: How do I send a user straight into an account's Business App session from my app?
  - id: getAccountByAccountIdUsers
    intent: List the users on an account
    question: Who are the users that belong to a particular business account?
  - id: getAccountByAccountIdAddons
    intent: List an account's activated addons
    question: Which marketplace addons has a business activated?
  - id: postAccountByAccountIdFileGroup
    intent: Share a new group of files with a business
    question: How do I deliver a set of files to a business so they can download them in Business App?
  phrasing_ops: 14
  slug: vendasta-account-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: 'The Activity API lets you inform us of new activity from your Marketplace App. It will be displayed in the user''s activity stream and used for notifications. Note: This endpoint has duplicate detectio'
  name: Vendasta Activity API
  phrasing_intents:
  - id: postActivity
    intent: Post an activity to a business's stream
    question: How do I notify a business in Business App that something happened in my app?
  phrasing_ops: 1
  slug: vendasta-activity-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Change Spend APIs allow interact with change spend requests, like resolving them by approving or rejecting
  name: Vendasta Change Spend API
  phrasing_intents:
  - id: postChangeSpendResolve
    intent: Approve or reject a change spend request
    question: How do I approve a business's request to change its spend on my product?
  phrasing_ops: 1
  slug: vendasta-change-spend-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Customer APIs allow you to perform actions against customers of the account that your application has been added to.
  name: Vendasta Customer API
  phrasing_intents:
  - id: postCustomer
    intent: Create a customer for a business
    question: How do I add a new customer contact to a business account?
  - id: postCustomerListCustomers
    intent: List or search a business's customers
    question: Can I search a business's customers by name, email or phone?
  - id: postCustomerGetCustomer
    intent: Get a customer by vendor customer ID
    question: Can I fetch one customer using the ID my app assigned to them?
  - id: postCustomerAssociateId
    intent: Map my app's ID onto an existing customer
    question: How do I attach my own system's ID to a customer created elsewhere?
  - id: postCustomerUpdateCustomer
    intent: Update an existing customer's details
    question: Can I change the email or phone on a customer I already created?
  - id: postCustomerDeleteCustomer
    intent: Delete a customer
    question: How do I remove a customer from a business account?
  phrasing_ops: 6
  slug: vendasta-customer-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The executive report APIs are used to submit data to the executive report for a single app on an account.
  name: Vendasta Executive Report API
  phrasing_intents:
  - id: postExecutiveReportWeekly
    intent: Submit weekly executive report data
    question: How do I feed my app's weekly numbers into a business's Executive Report?
  - id: postExecutiveReportMonthly
    intent: Submit monthly executive report data
    question: Can I push monthly aggregated numbers into the Executive Report?
  phrasing_ops: 2
  slug: vendasta-executive-report-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Marketplace App APIs allow you to perform actions against your applications, as well as certain operations against all marketplace apps.
  name: Vendasta Marketplace App API
  phrasing_intents:
  - id: getMarketplaceAppByMarketplaceAppId
    intent: Get a marketplace application
    question: What details are listed for a Vendasta Marketplace application?
  phrasing_ops: 1
  slug: vendasta-marketplace-app-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The User APIs allow you to perform operations against Vendasta Users. Each user has a unique identifier in the format UID-{}. This ID is guaranteed to stay the same, while the email associated to a us
  name: Vendasta User API
  phrasing_intents:
  - id: getUserByUserId
    intent: Get a platform user by user ID
    question: Can I pull a Vendasta user's profile with just their user ID, outside of SCIM?
  - id: headUserByUserIdPermissionsByAccountId
    intent: Check whether a user can access an account
    question: Is there a quick check for whether a given user has permission on a business account?
  - id: scim-search-users
    intent: Search or list users under a partner
    question: Can I find partner users by a SCIM filter such as userName or email?
  - id: scim-create-user
    intent: Provision a new user via SCIM
    question: How do I provision a brand-new user for my partner account through SCIM?
  - id: scim-get-user
    intent: Get one user by ID
    question: Can I look up a single SCIM user when I already know their user ID?
  - id: scim-replace-user
    intent: Replace all attributes of a user
    question: If I overwrite a SCIM user entirely, do attributes I leave out get blanked?
  - id: scim-update-user
    intent: Patch selected attributes of a user
    question: Can I change just one attribute on a user and leave the rest untouched?
  - id: scim-delete-user
    intent: Delete a user
    question: Can I deprovision and remove a user from my partner account through SCIM?
  phrasing_ops: 9
  slug: vendasta-user-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Account Stats API from Vendasta — 2 operation(s) for account stats.
  name: Vendasta Account Stats API
  phrasing_intents:
  - id: get-accountStats
    intent: List ad account stats for a business location
    question: How are all the connected advertising accounts for a location performing?
  - id: get-accountStats-id
    intent: Get stats for one connected ad account
    question: What results did one specific connected ad account deliver?
  phrasing_ops: 2
  slug: vendasta-account-stats-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The AnalyticsService API from Vendasta — 2 operation(s) for analyticsservice.
  name: Vendasta Analytics Service API
  phrasing_intents:
  - id: AnalyticsService_GetAvailableMetrics
    intent: Discover available analytics metrics
    question: Which analytics metrics, measures and dimensions can I query for a business?
  - id: AnalyticsService_QueryMetrics
    intent: Query multi-location analytics metrics
    question: What are the top 10 businesses by review count this quarter?
  phrasing_ops: 2
  slug: vendasta-analyticsservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Assistants API from Vendasta — 1 operation(s) for assistants.
  name: Vendasta Assistants API
  phrasing_intents:
  - id: Assistants_ListAssistants
    intent: List an account's AI Employees
    question: Which AI Employees are set up on an account?
  phrasing_ops: 1
  slug: vendasta-assistants-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Automation Runs API from Vendasta — 1 operation(s) for automation runs.
  name: Vendasta Automation Runs API
  phrasing_intents:
  - id: post-autoamtionruns
    intent: Trigger an automation
    question: How do I kick off one of my preconfigured automations from code?
  - id: options-automationruns-id
    intent: Check allowed methods on automation runs
    question: Which HTTP verbs does the automation runs endpoint accept for CORS?
  phrasing_ops: 2
  slug: vendasta-automation-runs-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Automations API from Vendasta — 2 operation(s) for automations.
  name: Vendasta Automations API
  phrasing_intents:
  - id: options-automations
    intent: Check allowed methods on the automations list
    question: Which HTTP verbs does the automations collection allow for browsers?
  - id: list-automations
    intent: List automations in a namespace
    question: What automations are set up for an account or partner?
  - id: options-automations-id
    intent: Check allowed methods on one automation
    question: Which verbs can a browser use on a single automation URL?
  - id: get-automation-by-id
    intent: Get one automation
    question: What does a specific automation do and how is it set up?
  phrasing_ops: 4
  slug: vendasta-automations-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The BlogPostsService API from Vendasta — 2 operation(s) for blogpostsservice.
  name: Vendasta Blog Posts Service API
  phrasing_intents:
  - id: BlogPostsService_DeleteBlogPost
    intent: Delete a blog post
    question: Can I delete a blog post that was published through social posting?
  - id: BlogPostsService_UpdateBlogPost
    intent: Edit a blog post
    question: Can I change the content of a blog post after it's been created?
  phrasing_ops: 2
  slug: vendasta-blogpostsservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Business Categories API from Vendasta — 1 operation(s) for business categories.
  name: Vendasta Business Categories API
  phrasing_intents:
  - id: get-businessCategories
    intent: List or search business categories
    question: What business categories can I assign to a location?
  - id: options-businessCategories
    intent: Check allowed methods for business categories
    question: Which HTTP verbs does the business categories endpoint allow cross-origin?
  phrasing_ops: 2
  slug: vendasta-business-categories-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Business Location Reviews API from Vendasta — 2 operation(s) for business location reviews.
  name: Vendasta Business Location Reviews API
  phrasing_intents:
  - id: get-businessLocationReviews
    intent: List reviews for a business location
    question: What reviews has one of my business locations received?
  - id: options-businessLocationReviews
    intent: Check allowed methods on location reviews
    question: Which HTTP verbs does the business location reviews endpoint accept for CORS?
  - id: get-businessLocationReviews-id-actions-suggestResponse
    intent: Get an AI-suggested reply to a review
    question: Can AI draft a response to a customer review for me?
  phrasing_ops: 3
  slug: vendasta-business-location-reviews-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Business Locations API from Vendasta — 2 operation(s) for business locations.
  name: Vendasta Business Locations API
  phrasing_intents:
  - id: post-businessLocations
    intent: Create a business location
    question: How do I add a new business location under my partner?
  - id: options-businessLocations
    intent: Check allowed methods on the locations list
    question: Which HTTP verbs does the business locations collection accept for CORS?
  - id: get-businessLocations
    intent: List business locations
    question: Which business locations belong to my partner account?
  - id: get-businessLocations-id
    intent: Get a business location
    question: What basic data is stored for one business location?
  - id: options-businessLocations-id
    intent: Check allowed methods on a single location
    question: Which HTTP verbs are allowed on one business location resource?
  - id: patch-businessLocations-id
    intent: Update a business location
    question: Can I change a location's details without resending every field?
  phrasing_ops: 6
  slug: vendasta-business-locations-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Cache API from Vendasta — 1 operation(s) for cache.
  name: Vendasta Cache API
  phrasing_intents:
  - id: Cache_InvalidateCache
    intent: Clear the cache for a hosted site
    question: Why aren't my site changes showing, and can I clear the hosted site cache?
  phrasing_ops: 1
  slug: vendasta-cache-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Campaign Info API from Vendasta — 2 operation(s) for campaign info.
  name: Vendasta Campaign Info API
  phrasing_intents:
  - id: get-campaignInfo
    intent: List ad campaigns for a connected account
    question: Which ad campaigns are running under a connected advertising account?
  - id: get-campaignInfo-id
    intent: Get an ad campaign
    question: What details are available for one ad campaign?
  phrasing_ops: 2
  slug: vendasta-campaign-info-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Campaign Stats API from Vendasta — 2 operation(s) for campaign stats.
  name: Vendasta Campaign Stats API
  phrasing_intents:
  - id: get-campaignStats
    intent: List ad campaign stats for a connected account
    question: How are all the ad campaigns on a connected advertising account performing?
  - id: get-campaignStats-id
    intent: Get stats for one ad campaign
    question: What are the results for one particular advertising campaign?
  phrasing_ops: 2
  slug: vendasta-campaign-stats-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Citations API from Vendasta — 2 operation(s) for citations.
  name: Vendasta Citations API
  phrasing_intents:
  - id: Citations_GetCitationData
    intent: Get citation data for a business over a period
    question: Where is my business cited online between two dates?
  - id: get-citationData
    intent: List a location's citations, newest first
    question: Which citations have been found for my business location, most recent first?
  - id: options-citationData
    intent: Check allowed methods on citations
    question: Which HTTP verbs does the citations endpoint allow for CORS?
  phrasing_ops: 3
  slug: vendasta-citations-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Composer API from Vendasta — 1 operation(s) for composer.
  name: Vendasta Composer API
  phrasing_intents:
  - id: Composer_UpdatePosts
    intent: Update social posts in the composer
    question: Can I edit several scheduled social posts in one request?
  phrasing_ops: 1
  slug: vendasta-composer-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Connected Accounts API from Vendasta — 2 operation(s) for connected accounts.
  name: Vendasta Connected Accounts API
  phrasing_intents:
  - id: get-connectedAccounts-connectedAccount.id
    intent: Get one connected advertising account
    question: What metadata is stored for a specific connected ad account?
  - id: get-connectedAccounts
    intent: List a location's connected ad accounts
    question: Which advertising accounts are connected to a business location?
  phrasing_ops: 2
  slug: vendasta-connected-accounts-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The ConversationService API from Vendasta — 2 operation(s) for conversationservice.
  name: Vendasta Conversation Service API
  phrasing_intents:
  - id: ConversationService_ListCommunicationChannelsInfo
    intent: List a business's communication channels
    question: Which messaging channels are set up for a business?
  - id: ConversationService_ListWidgets
    intent: List chat widgets
    question: What chat widgets are configured in a namespace?
  phrasing_ops: 2
  slug: vendasta-conversationservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Countries API from Vendasta — 4 operation(s) for countries.
  name: Vendasta Countries API
  phrasing_intents:
  - id: get-countries
    intent: List countries
    question: Which countries does Vendasta support for addresses?
  - id: options-countries
    intent: Check allowed methods on the countries list
    question: Which HTTP verbs does the countries collection allow for CORS?
  - id: get-countries-id
    intent: Get a country
    question: How can I look up one country by its ID?
  - id: options-countries-id
    intent: Check allowed methods on a single country
    question: Which HTTP verbs are allowed on one country resource?
  - id: get-country-regions
    intent: List states or provinces in a country
    question: What states or provinces are available for a given country?
  - id: options-countryRegions
    intent: Check allowed methods on country regions
    question: Which HTTP verbs does the country regions list accept for CORS?
  - id: get-country-regions-id
    intent: Get a state or province
    question: Can I get the name of one state or province by its ID?
  - id: options-countryRegions-id
    intent: Check allowed methods on a single region
    question: Which HTTP verbs does a single state or province endpoint permit?
  phrasing_ops: 8
  slug: vendasta-countries-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMAssociationService API from Vendasta — 6 operation(s) for crmassociationservice.
  name: Vendasta CRM Association Service API
  phrasing_intents:
  - id: CRMAssociationService_CreateAssociation
    intent: Link two CRM records
    question: How do I link a contact to a company in the CRM?
  - id: CRMAssociationService_DeleteAssociation
    intent: Remove a link between CRM records
    question: Can I unlink two CRM records without deleting either of them?
  - id: CRMAssociationService_ListAssociationFieldOptions
    intent: List options for an association field
    question: What values can a field on a CRM association take?
  - id: CRMAssociationService_GetMultiAssociation
    intent: Fetch several associations by ID
    question: Can I look up a batch of CRM associations when I have their IDs?
  - id: CRMAssociationService_ListAssociation
    intent: List associations between CRM records
    question: Which CRM records are linked to each other in my account?
  - id: CRMAssociationService_UpdateAssociation
    intent: Update tags on a CRM association
    question: Can I tag an existing link between two CRM records?
  phrasing_ops: 6
  slug: vendasta-crmassociationservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMCompanyService API from Vendasta — 6 operation(s) for crmcompanyservice.
  name: Vendasta CRM Company Service API
  phrasing_intents:
  - id: CRMCompanyService_CreateCompany
    intent: Create a company in the CRM
    question: How do I add a new company record to the CRM?
  - id: CRMCompanyService_DeleteCompany
    intent: Delete a CRM company
    question: Can I remove a company from the CRM?
  - id: CRMCompanyService_ListCompanyFieldOptions
    intent: List allowed values for a company field
    question: What options can a company dropdown field take?
  - id: CRMCompanyService_GetMultiCompany
    intent: Get several CRM companies by ID
    question: Can I load a few company records at once when I know their IDs?
  - id: CRMCompanyService_ListCompanies
    intent: List and search CRM companies
    question: Which companies are in my CRM?
  - id: CRMCompanyService_UpdateCompany
    intent: Update a CRM company
    question: Can I change details on a company already in the CRM?
  phrasing_ops: 6
  slug: vendasta-crmcompanyservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMCustomObjectService API from Vendasta — 9 operation(s) for crmcustomobjectservice.
  name: Vendasta CRM Custom Object Service API
  phrasing_intents:
  - id: CRMCustomObjectService_BulkDeleteCustomObjects
    intent: Bulk delete custom CRM objects
    question: Can I delete many custom CRM objects at once using a filter or search?
  - id: CRMCustomObjectService_CreateCustomObject
    intent: Create a custom CRM object
    question: How do I add a new record of a custom object type to the CRM?
  - id: CRMCustomObjectService_DeleteCustomObject
    intent: Delete one custom CRM object
    question: Can I delete a single custom object record by its ID?
  - id: CRMCustomObjectService_ListCustomObjectFieldOptions
    intent: List options for a custom object field
    question: What values can a dropdown field on a custom object take?
  - id: CRMCustomObjectService_GetMultiCustomObject
    intent: Fetch several custom objects by ID
    question: Can I retrieve a batch of custom objects when I already know their IDs?
  - id: CRMCustomObjectService_ListCustomObjects
    intent: List and search custom CRM objects
    question: Which custom object records exist in my CRM?
  - id: CRMCustomObjectService_ListCustomObjectFilters
    intent: List available filters for custom objects
    question: What filters can I apply when listing custom objects?
  - id: CRMCustomObjectService_UpdateCustomObject
    intent: Update a custom CRM object
    question: Can I change only certain fields on an existing custom object?
  phrasing_ops: 9
  slug: vendasta-crmcustomobjectservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMCustomObjectTypeService API from Vendasta — 5 operation(s) for crmcustomobjecttypeservice.
  name: Vendasta CRM Custom Object Type Service API
  phrasing_intents:
  - id: CRMCustomObjectTypeService_CreateCustomObjectType
    intent: Define a new custom object type
    question: How do I define a new kind of custom object in the CRM?
  - id: CRMCustomObjectTypeService_DeleteCustomObjectType
    intent: Delete a custom object type
    question: Can I delete a custom object type I no longer need?
  - id: CRMCustomObjectTypeService_GetMultiCustomObjectType
    intent: Fetch custom object types by ID
    question: Can I look up several custom object types by their IDs?
  - id: CRMCustomObjectTypeService_ListCustomObjectTypes
    intent: List custom object types
    question: Which custom object types are defined in my CRM?
  - id: CRMCustomObjectTypeService_UpdateCustomObjectType
    intent: Update a custom object type
    question: Can I rename or change the definition of a custom object type?
  phrasing_ops: 5
  slug: vendasta-crmcustomobjecttypeservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMFieldSchemaCustomizationService API from Vendasta — 5 operation(s) for crmfieldschemacustomizationservice.
  name: Vendasta CRM Field Schema Customization Service API
  phrasing_intents:
  - id: CRMFieldSchemaCustomizationService_CreateFieldSchemaCustomization
    intent: Customize a CRM field's schema
    question: Can I customize how a standard CRM field behaves for contacts or companies?
  - id: CRMFieldSchemaCustomizationService_DeleteFieldSchemaCustomization
    intent: Remove a CRM field customization
    question: How do I revert a CRM field back to its default schema?
  - id: CRMFieldSchemaCustomizationService_GetMultiFieldSchemaCustomization
    intent: Get customizations for specific CRM fields
    question: What customizations are applied to particular CRM fields?
  - id: CRMFieldSchemaCustomizationService_ListFieldSchemaCustomization
    intent: List CRM field schema customizations
    question: Which CRM fields have been customized in this namespace?
  - id: CRMFieldSchemaCustomizationService_UpdateFieldSchemaCustomization
    intent: Change an existing CRM field customization
    question: Can I edit a field customization I already made?
  phrasing_ops: 5
  slug: vendasta-crmfieldschemacustomizationservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMFieldSchemaService API from Vendasta — 5 operation(s) for crmfieldschemaservice.
  name: Vendasta CRM Field Schema Service API
  phrasing_intents:
  - id: CRMFieldSchemaService_ArchiveFieldSchema
    intent: Archive a CRM custom field
    question: Can I retire a CRM field I no longer use without creating a new one?
  - id: CRMFieldSchemaService_CreateFieldSchema
    intent: Create a CRM custom field
    question: How do I add a new custom field to CRM contacts or companies?
  - id: CRMFieldSchemaService_GetMultiFieldSchema
    intent: Get definitions of specific CRM fields
    question: What type and label does a given set of CRM field IDs have?
  - id: CRMFieldSchemaService_ListFieldSchema
    intent: List CRM field schemas
    question: Which fields exist on my CRM contacts, companies or opportunities?
  - id: CRMFieldSchemaService_UpdateFieldSchema
    intent: Update a CRM custom field definition
    question: Can I rename or change the settings of an existing CRM field?
  phrasing_ops: 5
  slug: vendasta-crmfieldschemaservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMOpportunityService API from Vendasta — 6 operation(s) for crmopportunityservice.
  name: Vendasta CRM Opportunity Service API
  phrasing_intents:
  - id: CRMOpportunityService_CreateOpportunity
    intent: Create a CRM opportunity
    question: How do I add a new sales opportunity to the CRM?
  - id: CRMOpportunityService_DeleteOpportunity
    intent: Delete a CRM opportunity
    question: Can I remove an opportunity from the CRM once a deal is dead?
  - id: CRMOpportunityService_ListOpportunityFieldOptions
    intent: List allowed values for an opportunity field
    question: What values can I pick for a dropdown field on opportunities, like stage?
  - id: CRMOpportunityService_GetMultiOpportunity
    intent: Fetch several opportunities by ID
    question: Can I load a batch of specific opportunities in one call when I have their IDs?
  - id: CRMOpportunityService_ListOpportunities
    intent: List and search CRM opportunities
    question: Which opportunities are open in my CRM pipeline right now?
  - id: CRMOpportunityService_UpdateOpportunity
    intent: Update a CRM opportunity
    question: Can I move an existing opportunity to a new stage or change its amount?
  phrasing_ops: 6
  slug: vendasta-crmopportunityservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The CRMService API from Vendasta — 6 operation(s) for crmservice.
  name: Vendasta CRM Service API
  phrasing_intents:
  - id: CRMService_CreateContact
    intent: Create a CRM contact
    question: How do I add a new contact to the CRM?
  - id: CRMService_DeleteContact
    intent: Delete a CRM contact
    question: Can I delete a contact from the CRM by its ID?
  - id: CRMService_ListContactFieldOptions
    intent: List options for a contact field
    question: What values are allowed for a picklist field on contacts?
  - id: CRMService_GetMultiContact
    intent: Fetch several contacts by ID
    question: Can I retrieve a batch of contacts when I already have their IDs?
  - id: CRMService_ListContacts
    intent: List and search CRM contacts
    question: Which contacts are in my CRM?
  - id: CRMService_UpdateContact
    intent: Update a CRM contact
    question: Can I change a contact's phone number or email?
  phrasing_ops: 6
  slug: vendasta-crmservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Customers API from Vendasta — 2 operation(s) for customers.
  name: Vendasta Customers API
  phrasing_intents:
  - id: post-customers
    intent: Create a customer (legacy)
    question: Can I still create a customer record in Business App with the deprecated customers endpoint?
  - id: get-customers
    intent: List customers of a business location
    question: Which customers are recorded for one of my business locations?
  - id: options-customers
    intent: Check allowed methods on the customers list
    question: Which HTTP verbs does the customers collection accept for CORS?
  - id: get-customers-id
    intent: Get a customer
    question: How can I fetch the current values for one customer?
  - id: delete-customers-id
    intent: Delete a customer
    question: Can I delete a customer record from a business location?
  - id: patch-customers-id
    intent: Update a customer
    question: Can I update a few fields on a customer and keep the rest unchanged?
  - id: options-customers-id
    intent: Check allowed methods on a single customer
    question: Which HTTP verbs are allowed on one customer resource?
  phrasing_ops: 7
  slug: vendasta-customers-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Drafts API from Vendasta — 8 operation(s) for drafts.
  name: Vendasta Drafts API
  phrasing_intents:
  - id: Drafts_CreateDraft
    intent: Save a social post draft
    question: How do I save a social media post as a draft instead of publishing it?
  - id: Drafts_CreateMultiDrafts
    intent: Save several social drafts at once
    question: Can I create a batch of social post drafts in one request?
  - id: Drafts_DeleteDraft
    intent: Delete a social post draft
    question: Can I throw away a social draft I no longer need?
  - id: Drafts_DeleteMultiMLDrafts
    intent: Delete multi-location drafts for a brand
    question: How can I clear out several multi-location drafts for a brand at once?
  - id: Drafts_GetDraft
    intent: Get a social post draft
    question: What does a particular saved draft contain?
  - id: Drafts_ListDrafts
    intent: List an account's social drafts
    question: Which social drafts are waiting on an account?
  - id: Drafts_UpdateDraft
    intent: Edit a social post draft
    question: Can I change the text or scheduled time of a draft I already saved?
  - id: Drafts_UpdateMultiMLDrafts
    intent: Update several multi-location drafts
    question: Can I edit a set of multi-location drafts together?
  phrasing_ops: 8
  slug: vendasta-drafts-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Forms API from Vendasta — 9 operation(s) for forms.
  name: Vendasta Forms API
  phrasing_intents:
  - id: Forms_CreateForm
    intent: Create a lead capture form
    question: How do I build a new contact form with name, email and message fields?
  - id: Forms_GetEmbedCode
    intent: Get the embed code for a form
    question: Where do I get the snippet to put a form on my website?
  - id: Forms_GenerateCustomCSS
    intent: Generate custom CSS styling for a form with AI
    question: Can I describe a look in plain words and get CSS styles generated for my form?
  - id: Forms_GetForm
    intent: Get a form's configuration
    question: What fields and settings does an existing form have?
  - id: Forms_HasEnterpriseAPIKeyInNamespace
    intent: Check for a reCAPTCHA Enterprise key in a namespace
    question: Does this namespace already have an enterprise API key set up for forms?
  - id: Forms_ListForms
    intent: List and search forms
    question: What forms have been created so far?
  - id: Forms_ListMappedFieldSchema
    intent: List CRM fields a form can map to
    question: Which CRM contact or company fields can a form field be mapped to?
  - id: Forms_ProvisionRecaptchaEnterprise
    intent: Turn on reCAPTCHA Enterprise for a form
    question: How can I protect a form from spam with reCAPTCHA Enterprise?
  phrasing_ops: 9
  slug: vendasta-forms-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Glossary-Contexts API from Vendasta — 3 operation(s) for glossary-contexts.
  name: Vendasta Glossary Contexts API
  phrasing_intents:
  - id: get-contexts
    intent: List glossary contexts
    question: What glossary contexts are defined?
  - id: get-contexts-id
    intent: Get a glossary context
    question: What does a particular glossary context describe?
  - id: get-contexts-id-terms
    intent: List the terms in a glossary context
    question: Which glossary terms belong to a given context?
  phrasing_ops: 3
  slug: vendasta-glossary-contexts-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Glossary-Terms API from Vendasta — 3 operation(s) for glossary-terms.
  name: Vendasta Glossary Terms API
  phrasing_intents:
  - id: glossary-list-terms
    intent: Look up glossary term definitions
    question: What does the term customer mean across different platform contexts?
  - id: get-terms-id
    intent: Get one glossary term
    question: What is the definition behind a specific glossary term ID?
  - id: get-contexts-id-terms
    intent: List the terms within one context
    question: Which terms belong to a particular glossary context?
  phrasing_ops: 3
  slug: vendasta-glossary-terms-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: Group resource
  name: Vendasta Group API
  phrasing_intents:
  - id: getByNamespaceGroups
    intent: Search a partner's user groups
    question: Can I find a SCIM group by its display name, like Platform Admin?
  - id: getByNamespaceGroupsById
    intent: Get one user group
    question: Who are the members of a particular SCIM group?
  - id: patchByNamespaceGroupsById
    intent: Update a user group's members or attributes
    question: How do I add or remove members from a SCIM group?
  phrasing_ops: 3
  slug: vendasta-group-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Knowledge API from Vendasta — 5 operation(s) for knowledge.
  name: Vendasta Knowledge API
  phrasing_intents:
  - id: Knowledge_CreateKnowledgeFileUpload
    intent: Get a signed URL to upload a knowledge file
    question: How do I upload a file to an AI Employee's knowledge base?
  - id: Knowledge_ListKnowledge
    intent: List knowledge sources
    question: Which knowledge sources are in an account's knowledge base?
  - id: Knowledge_RemoveKnowledge
    intent: Remove or unlink a knowledge source
    question: Can I delete a knowledge source from the knowledge base?
  - id: Knowledge_GetKnowledgeStatus
    intent: Check a knowledge source's processing status
    question: Has my uploaded knowledge finished processing yet?
  - id: Knowledge_UpsertKnowledge
    intent: Create or update a knowledge source
    question: Can I add text content to an AI Employee's knowledge base?
  phrasing_ops: 5
  slug: vendasta-knowledge-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Listing Profiles API from Vendasta — 1 operation(s) for listing profiles.
  name: Vendasta Listing Profiles API
  phrasing_intents:
  - id: patch-listingProfiles-id
    intent: Update a business listing profile
    question: Can I change hours or contact details on a listing profile?
  - id: get-listingProfiles-id
    intent: Get a business listing profile
    question: What business details are stored in a listing profile?
  phrasing_ops: 2
  slug: vendasta-listing-profiles-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Listing Scores API from Vendasta — 1 operation(s) for listing scores.
  name: Vendasta Listing Scores API
  phrasing_intents:
  - id: get-listingScores
    intent: Get a business's listing score
    question: How healthy are a business's online directory listings?
  - id: options-listingScores-id
    intent: Check allowed methods for listing scores
    question: Which HTTP verbs does the listing score endpoint accept cross-origin?
  phrasing_ops: 2
  slug: vendasta-listing-scores-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Listing Sync Listings API from Vendasta — 1 operation(s) for listing sync listings.
  name: Vendasta Listing Sync Listings API
  phrasing_intents:
  - id: list-listingSyncListings
    intent: List a location's synced listings
    question: Which directory listings are on a location's Local SEO business profile?
  - id: options-listingSyncListings
    intent: Check allowed methods on listing sync
    question: Which HTTP verbs does the listing sync endpoint accept for CORS?
  phrasing_ops: 2
  slug: vendasta-listing-sync-listings-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The ListingProductsService API from Vendasta — 1 operation(s) for listingproductsservice.
  name: Vendasta Listing Products Service API
  phrasing_intents:
  - id: ListingProductsService_GetSyncData
    intent: Get listing sync data for a business
    question: What is the listing sync status for my business across directories?
  phrasing_ops: 1
  slug: vendasta-listingproductsservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The ListingProfileService API from Vendasta — 1 operation(s) for listingprofileservice.
  name: Vendasta Listing Profile Service API
  phrasing_intents:
  - id: ListingProfileService_Update
    intent: Apply updates to a business's listing profile
    question: Can I apply a set of edits to a business's listing profile keywords and details?
  phrasing_ops: 1
  slug: vendasta-listingprofileservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The ListingService API from Vendasta — 3 operation(s) for listingservice.
  name: Vendasta Listing Service API
  phrasing_intents:
  - id: ListingService_ForceRefreshListing
    intent: Force a listing to refresh
    question: Can I force a directory listing to re-sync right now?
  - id: ListingService_GetListings
    intent: Get listings by ID
    question: Can I fetch directory listings when I know their IDs?
  - id: ListingService_LookupListings
    intent: Look up a business's listings across sources
    question: Which directory listings have been found for my business?
  phrasing_ops: 3
  slug: vendasta-listingservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The ListingSourceService API from Vendasta — 2 operation(s) for listingsourceservice.
  name: Vendasta Listing Source Service API
  phrasing_intents:
  - id: ListingSourceService_GetListingSourceById
    intent: Get a listing source by ID
    question: What are the details of one listing source, such as a directory site?
  - id: ListingSourceService_GetListingSources
    intent: List listing sources
    question: Which listing sources are supported?
  phrasing_ops: 2
  slug: vendasta-listingsourceservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The MeetingExternal API from Vendasta — 9 operation(s) for meetingexternal.
  name: Vendasta Meeting External API
  phrasing_intents:
  - id: MeetingExternal_BookMeeting
    intent: Book a meeting
    question: How do I book a meeting for a business on one of its event types?
  - id: MeetingExternal_CancelMeeting
    intent: Cancel a booked meeting
    question: Can I cancel a meeting that has already been booked?
  - id: MeetingExternal_ListAvailableTimeSlots
    intent: Find open time slots for an event type
    question: What times are still open to book for an event type?
  - id: MeetingExternal_ListTeamEventTypes
    intent: List a business's team event types
    question: Which team meeting types has a business set up?
  - id: MeetingExternal_ListGroups
    intent: List meeting groups for a business
    question: What meeting groups exist for a business?
  - id: MeetingExternal_RescheduleMeeting
    intent: Reschedule a meeting
    question: Can I move a booked meeting to a different time?
  - id: MeetingExternal_ListServices
    intent: List bookable services for a business
    question: Which services can customers book with a business?
  - id: MeetingExternal_ListUserEventTypes
    intent: List a user's event types
    question: What personal and team event types does one staff member have?
  phrasing_ops: 9
  slug: vendasta-meetingexternal-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Messages API from Vendasta — 1 operation(s) for messages.
  name: Vendasta Messages API
  phrasing_intents:
  - id: options-messages
    intent: Check allowed methods on the messages endpoint
    question: Which HTTP verbs does the /messages endpoint accept from a browser?
  - id: get-messages
    intent: List a business's social posts
    question: What social posts has a business published or scheduled?
  - id: post-messages
    intent: Schedule a social message
    question: Can I schedule a social media message to go out later?
  phrasing_ops: 3
  slug: vendasta-messages-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Monitor API from Vendasta — 2 operation(s) for monitor.
  name: Vendasta Monitor API
  phrasing_intents:
  - id: Monitor_Search
    intent: Find uptime monitors for a partner
    question: Which sites have uptime monitors set up under my partner account?
  - id: Monitor_FetchUptimeData
    intent: Get uptime history for an account
    question: Was my site up or down over the last week?
  phrasing_ops: 2
  slug: vendasta-monitor-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The NetPromoterScoreService API from Vendasta — 4 operation(s) for netpromoterscoreservice.
  name: Vendasta Net Promoter Score Service API
  phrasing_intents:
  - id: NetPromoterScoreService_LeaveNetPromoterScore
    intent: Submit a customer's NPS score
    question: Can I record the 1 to 10 score a customer picked on an NPS request?
  - id: NetPromoterScoreService_GetNetPromoterScoreDetails
    intent: Get redirect details for an NPS record
    question: Where should a customer be redirected after answering an NPS survey?
  - id: NetPromoterScoreService_ImportNPS
    intent: Import an NPS result from an outside system
    question: Can I bring in NPS survey results collected by another tool?
  - id: NetPromoterScoreService_ListNetPromoterScores
    intent: List NPS feedback for a business
    question: What NPS feedback has a business received from its customers?
  phrasing_ops: 4
  slug: vendasta-netpromoterscoreservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Options API from Vendasta — 55 operation(s) for options.
  name: Vendasta Options API
  phrasing_intents:
  - id: options-accountStats
    intent: Check allowed methods for the account stats list
    question: Which HTTP verbs can a browser use against the account stats listing endpoint?
  - id: options-accountStats-id
    intent: Check allowed methods for one account's stats
    question: What methods are permitted on the stats endpoint for a single connected ad account?
  - id: options-connectedAccounts-connectedAccount.id
    intent: Check allowed methods for one connected account
    question: Which verbs does the endpoint for an individual connected advertising account support?
  - id: options-connectedAccounts
    intent: Check allowed methods for the connected accounts list
    question: What HTTP methods does the connected accounts collection expose to browsers?
  - id: options-campaignInfo
    intent: Check allowed methods for campaign info list
    question: Which methods does the campaign info listing accept from a browser client?
  - id: options-campaignInfo-id
    intent: Check allowed methods for one campaign's info
    question: What verbs are allowed on the info endpoint for one specific campaign?
  - id: options-campaignStats
    intent: Check allowed methods for campaign stats list
    question: Which HTTP methods can I call on the campaign statistics collection from the browser?
  - id: options-campaignStats-id
    intent: Check allowed methods for one campaign's stats
    question: What methods does the statistics endpoint for a single campaign accept?
  phrasing_ops: 55
  slug: vendasta-options-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Order Custom Fields API from Vendasta — 1 operation(s) for order custom fields.
  name: Vendasta Order Custom Fields API
  phrasing_intents:
  - id: patch-orderCustomFields-by-id
    intent: Update a sales order's custom field values
    question: Can I change a custom field value on an existing order?
  - id: get-orderCustomFields-by-id
    intent: Get a sales order's custom field values
    question: What custom field values were captured on a sales order?
  - id: options-orderCustomFields-by-id
    intent: Check allowed methods for order custom fields
    question: Which HTTP verbs does an order custom fields record accept cross-origin?
  phrasing_ops: 3
  slug: vendasta-order-custom-fields-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Order Fulfillment Forms API from Vendasta — 3 operation(s) for order fulfillment forms.
  name: Vendasta Order Fulfillment Forms API
  phrasing_intents:
  - id: get-orderFulfillmentForms
    intent: List fulfillment forms for an order
    question: Which fulfillment forms need filling out for the apps in an order?
  - id: options-orderFulfillmentForms
    intent: Check allowed methods on fulfillment forms
    question: Which HTTP verbs does the orderFulfillmentForms collection allow?
  - id: get-orderFulfillmentForms-by-id
    intent: Get one app's fulfillment form
    question: What was last submitted on the fulfillment form for one app in an order?
  - id: patch-orderFulfillmentForms-by-id
    intent: Save answers on a fulfillment form
    question: How do I fill in the fulfillment details a vendor needs for an order?
  - id: options-orderFulfillmentForms-by-id
    intent: Check allowed methods on one fulfillment form
    question: Which verbs can a browser use on a single fulfillment form URL?
  - id: post-orderFulfillmentForms-submit
    intent: Submit a fulfillment form to the vendor
    question: Can I force a fulfillment form into review before every required field is filled?
  phrasing_ops: 6
  slug: vendasta-order-fulfillment-forms-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Orders API from Vendasta — 4 operation(s) for orders.
  name: Vendasta Orders API
  phrasing_intents:
  - id: post-orders
    intent: Create an order for a business
    question: How do I place an order for products on behalf of a business?
  - id: options-orders
    intent: Check allowed methods on the orders collection
    question: Which HTTP methods does the orders collection accept from a browser?
  - id: get-orders
    intent: List a partner's orders
    question: What orders has my partner account placed?
  - id: get-orders-id
    intent: Get one order
    question: What is the current status and contents of a specific order?
  - id: options-order-id
    intent: Check allowed methods on a single order
    question: Which verbs can a browser use on one order's URL?
  - id: get-orderCustomFieldsID-by-order
    intent: Get the custom fields reference of an order
    question: What is the ID of the custom metadata record linked to an order?
  - id: options-orderCustomFieldsID-by-order
    intent: Check methods on an order's custom field link
    question: Which verbs are allowed on an order's relationships/customFields link?
  - id: get-orderCustomFields-by-order
    intent: Get an order's custom field values
    question: What custom field values were captured on an order?
  phrasing_ops: 9
  slug: vendasta-orders-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The PageSpeedService API from Vendasta — 1 operation(s) for pagespeedservice.
  name: Vendasta Page Speed Service API
  phrasing_intents:
  - id: PageSpeedService_GetScore
    intent: Get a site's page speed score
    question: How fast does my website load on mobile compared to desktop?
  phrasing_ops: 1
  slug: vendasta-pagespeedservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Partner Activatable Products API from Vendasta — 2 operation(s) for partner activatable products.
  name: Vendasta Partner Activatable Products API
  phrasing_intents:
  - id: get-partnerActivatableProducts-id
    intent: Get a product from a reseller's store
    question: What are the details of a product a reseller can activate for customers?
  - id: options-partnerActivatableProducts-id
    intent: Check allowed methods on one activatable product
    question: Which verbs can a browser use on a single partner activatable product URL?
  - id: get-partnerActivatableProducts
    intent: List products a partner can activate
    question: Which products can my partner account activate for its customers?
  - id: options-partnerActivatableProducts
    intent: Check allowed methods on the activatable products list
    question: Which HTTP verbs does the partnerActivatableProducts collection allow?
  phrasing_ops: 4
  slug: vendasta-partner-activatable-products-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Pipelines API from Vendasta — 5 operation(s) for pipelines.
  name: Vendasta Pipelines API
  phrasing_intents:
  - id: Pipelines_CreatePipeline
    intent: Create a sales pipeline
    question: How do I set up a new sales pipeline in the CRM?
  - id: Pipelines_DeletePipeline
    intent: Delete a sales pipeline
    question: Can I remove a pipeline I no longer use?
  - id: Pipelines_GetMultiPipeline
    intent: Get several pipelines by ID
    question: Can I fetch a couple of pipelines at once when I know their IDs?
  - id: Pipelines_ListPipelines
    intent: List CRM pipelines
    question: Which sales pipelines exist in my CRM?
  - id: Pipelines_UpdatePipeline
    intent: Update a sales pipeline
    question: Can I rename a pipeline or change its stages?
  phrasing_ops: 5
  slug: vendasta-pipelines-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Product Custom Fields API from Vendasta — 1 operation(s) for product custom fields.
  name: Vendasta Product Custom Fields API
  phrasing_intents:
  - id: patch-productCustomFields-by-id
    intent: Update a product's custom fields
    question: How do I change custom field values on a product?
  - id: get-productCustomFields-by-id
    intent: Get a product's custom fields
    question: Can I read the custom fields attached to a product?
  - id: options-productCustomFields-by-id
    intent: Check allowed methods on product custom fields
    question: Which HTTP verbs are allowed on a product's custom fields endpoint?
  phrasing_ops: 3
  slug: vendasta-product-custom-fields-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Purchases API from Vendasta — 1 operation(s) for purchases.
  name: Vendasta Purchases API
  phrasing_intents:
  - id: get-purchases
    intent: List wholesale purchases
    question: What wholesale purchases has my partner account made?
  - id: options-purchases
    intent: Check allowed methods on purchases
    question: Which HTTP verbs does the purchases endpoint accept for CORS?
  phrasing_ops: 2
  slug: vendasta-purchases-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: Endpoints related to Resource Operations
  name: Vendasta Resource Operations API
  phrasing_intents:
  - id: ListFieldSchema
    intent: Get the field schema for a CRM record type
    question: What fields exist on CRM contacts or companies in my account?
  - id: GetFieldOptions
    intent: Get the options for a CRM field
    question: What values are allowed for a picklist field on a CRM record type?
  - id: UpsertCrmRecord
    intent: Create or merge a CRM record
    question: Can I create a contact but merge it into an existing one if it already exists?
  - id: CreateCrmRecord
    intent: Create a CRM record
    question: How do I create a brand-new CRM record without matching existing ones?
  - id: GetCrmRecord
    intent: Get a CRM record
    question: How can I read one CRM record by its ID?
  - id: DeleteCrmRecord
    intent: Delete a CRM record
    question: Can I delete a CRM contact or company by its ID?
  - id: UpdateCrmRecord
    intent: Update a CRM record
    question: Can I edit fields on a CRM record I already know the ID of?
  - id: ListCrmRecords
    intent: List CRM records
    question: Which contacts, companies or activities are stored in my CRM?
  phrasing_ops: 8
  slug: vendasta-resource-operations-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Review Requests API from Vendasta — 1 operation(s) for review requests.
  name: Vendasta Review Requests API
  phrasing_intents:
  - id: post-reviewRequests
    intent: Send a customer a review request
    question: How do I ask a customer for a review by email or text message?
  - id: options-reviewRequests
    intent: Check allowed methods on review requests
    question: Which HTTP verbs does the reviewRequests endpoint allow cross-origin?
  phrasing_ops: 2
  slug: vendasta-review-requests-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The ReviewService API from Vendasta — 10 operation(s) for reviewservice.
  name: Vendasta Review Service API
  phrasing_intents:
  - id: ReviewService_CanRespondToReview
    intent: Check whether a review can be responded to
    question: Can this business actually post a reply to a particular review?
  - id: ReviewService_CreateReviewComment
    intent: Post a reply comment on a review
    question: How do I reply to a customer review from the reputation tools?
  - id: ReviewService_UpdateReviewComment
    intent: Edit an existing reply on a review
    question: Can I change the wording of a reply I already posted to a review?
  - id: ReviewService_GetReviews
    intent: Fetch several reviews by their IDs
    question: Can I pull the full details for a handful of reviews when I already have their IDs?
  - id: ReviewService_GetReviewHistory
    intent: Get the change history of a review
    question: What has changed on a review over time, and when?
  - id: ReviewService_GetReviewMetrics
    intent: Get review metrics for a partner's namespaces
    question: What review metrics can I get across all the accounts a partner manages?
  - id: ReviewService_SearchReviews
    intent: Search a business's reviews by rating, source or text
    question: How can I find all the one-star reviews a business received last month?
  - id: ReviewService_GetMultiThirdPartyReviewPublishSettings
    intent: Get third-party review publish settings
    question: Are third-party reviews set to be published for these accounts?
  phrasing_ops: 10
  slug: vendasta-reviewservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Sales Account Custom Fields API from Vendasta — 1 operation(s) for sales account custom fields.
  name: Vendasta Sales Account Custom Fields API
  phrasing_intents:
  - id: patch-salesAccountCustomFields-by-id
    intent: Update a sales account's custom fields
    question: Can I set extra custom information on a sales account?
  - id: get-salesAccountCustomFields-by-id
    intent: Get a sales account custom field record
    question: What custom attributes are stored in a sales account's custom field record?
  - id: options-salesAccountCustomFields-by-id
    intent: Check allowed methods on a custom field record
    question: Which verbs can a browser use on a salesAccountCustomFields record?
  phrasing_ops: 3
  slug: vendasta-sales-account-custom-fields-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Sales Accounts API from Vendasta — 4 operation(s) for sales accounts.
  name: Vendasta Sales Accounts API
  phrasing_intents:
  - id: post-salesAccounts
    intent: Create a sales account for a new location
    question: How do I add a new business location as a sales account?
  - id: options-salesAccounts
    intent: Check allowed methods on the sales accounts list
    question: Which HTTP verbs does the sales accounts collection endpoint accept for CORS?
  - id: get-salesAccounts
    intent: List a partner's sales accounts
    question: Which business locations does my partner account have on record?
  - id: get-salesAccounts-by-id
    intent: Get one sales account
    question: What basic data is stored on a single sales account?
  - id: options-salesAccounts-by-id
    intent: Check allowed methods on a single sales account
    question: Which methods can a browser use against one sales account's URL?
  - id: patch-salesAccounts-by-id
    intent: Update a sales account's details
    question: Can I change a business location's address without resending every field?
  - id: get-salesAccountCustomFieldsID-by-salesAccount
    intent: Get the custom fields reference of a sales account
    question: What is the ID of the custom field record linked to a sales account?
  - id: options-salesAccountCustomFieldsID-by-salesAccount
    intent: Check methods on the custom fields relationship
    question: Which verbs are allowed on the relationships/customFields link of a sales account?
  phrasing_ops: 10
  slug: vendasta-sales-accounts-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The SalesOrdersAuxiliaryFieldSchema API from Vendasta — 2 operation(s) for salesordersauxiliaryfieldschema.
  name: Vendasta Sales Orders Auxiliary Field Schema API
  phrasing_intents:
  - id: SalesOrdersAuxiliaryFieldSchema_GetAuxiliaryDataFieldSchema
    intent: Get one order custom field definition
    question: What type and settings does a specific sales order custom field have?
  - id: SalesOrdersAuxiliaryFieldSchema_ListAuxiliaryDataFieldSchema
    intent: List order custom field definitions
    question: Which custom fields has my partner defined for sales orders?
  phrasing_ops: 2
  slug: vendasta-salesordersauxiliaryfieldschema-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Send Welcome Email API from Vendasta — 1 operation(s) for send welcome email.
  name: Vendasta Send Welcome Email API
  phrasing_intents:
  - id: get-sendWelcomeEmail-by-userid
    intent: Send a welcome email to a user
    question: How do I send the welcome email to a user I've already created?
  - id: options-sendWelcomeEmail-by-userid
    intent: Check allowed methods on the welcome email action
    question: Which HTTP verbs does the sendWelcomeEmail action allow for browsers?
  phrasing_ops: 2
  slug: vendasta-send-welcome-email-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The SEOService API from Vendasta — 2 operation(s) for seoservice.
  name: Vendasta SEO Service API
  phrasing_intents:
  - id: SEOService_GetLocalSearchSEOData
    intent: Get local search ranking data for a keyword
    question: How does a business rank in local search for one keyword around its area?
  - id: SEOService_SaveSEOSettings
    intent: Save a business's SEO keyword settings
    question: Can I mark favorite keywords to track for a business?
  phrasing_ops: 2
  slug: vendasta-seoservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: Partner-facing endpoints for WordPress site information.
  name: Vendasta SiteDetail Service API
  phrasing_intents:
  - id: PartnerApi_ListSiteDetails
    intent: List domains for a partner's WordPress sites
    question: What primary and alternate domains do my partner's WordPress sites use?
  phrasing_ops: 1
  slug: vendasta-sitedetail-service-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The SiteManager API from Vendasta — 5 operation(s) for sitemanager.
  name: Vendasta Site Manager API
  phrasing_intents:
  - id: SiteManager_ChatCompletion
    intent: Ask the site support assistant a question
    question: Can I get an AI chat answer to a WordPress hosting support question?
  - id: SiteManager_ListPlugins
    intent: List plugins installed on a site
    question: Which WordPress plugins are installed on my hosted site?
  - id: SiteManager_ActivatePlugin
    intent: Activate plugins on a site
    question: Can I turn on several installed plugins for a site in one request?
  - id: SiteManager_DeactivatePlugin
    intent: Deactivate plugins on a site
    question: Can I switch off a misbehaving plugin on my site remotely?
  - id: SiteManager_GetSiteResourceUsagesSummary
    intent: Get a site's monthly resource usage
    question: How much hosting resource did my site consume this month?
  phrasing_ops: 5
  slug: vendasta-sitemanager-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The SiteOptionsService API from Vendasta — 1 operation(s) for siteoptionsservice.
  name: Vendasta Site Options Service API
  phrasing_intents:
  - id: SiteOptionsService_GetSiteUpdate
    intent: Check pending updates for a site
    question: Are there updates waiting to be applied on my hosted WordPress site?
  phrasing_ops: 1
  slug: vendasta-siteoptionsservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Social Profiles API from Vendasta — 1 operation(s) for social profiles.
  name: Vendasta Social Profiles API
  phrasing_intents:
  - id: get-socialProfiles
    intent: List a location's social profiles
    question: Which social profiles are connected to a business location?
  - id: options-socialProfiles
    intent: Check allowed methods on social profiles
    question: Which HTTP verbs does the social profiles endpoint accept for CORS?
  phrasing_ops: 2
  slug: vendasta-social-profiles-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The SocialPostsV2 API from Vendasta — 2 operation(s) for socialpostsv2.
  name: Vendasta Social Posts V2 API
  phrasing_intents:
  - id: SocialPostsV2_ListPostableSocialServices
    intent: List social accounts a business can post to
    question: Which connected social accounts can a business publish posts to?
  - id: SocialPostsV2_ScheduleSocialPosts
    intent: Schedule social posts
    question: How do I schedule posts across a business's social accounts?
  phrasing_ops: 2
  slug: vendasta-socialpostsv2-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Subscription Assignments API from Vendasta — 4 operation(s) for subscription assignments.
  name: Vendasta Subscription Assignments API
  phrasing_intents:
  - id: get-subscriptionAssignments
    intent: List a location's subscription assignments
    question: Which product subscriptions are assigned to a business location?
  - id: options-subscriptionAssignments
    intent: Check allowed methods on subscription assignments
    question: Which HTTP verbs does the subscriptionAssignments collection allow for browsers?
  - id: get-subscriptionAssignments-by-id
    intent: Get one subscription assignment
    question: What are the details of a single subscription assignment?
  - id: options-subscriptionAssignment-id
    intent: Check methods on one subscription assignment
    question: Which verbs can a browser use on a single subscription assignment URL?
  - id: cancel-subscriptionAssignments-by-id
    intent: Cancel a product subscription assignment
    question: How do I cancel a customer's product subscription?
  - id: options-subscriptionAssignment-requestCancellationAction
    intent: Check methods on the cancel subscription action
    question: Which verbs does the requestCancellation action endpoint accept cross-origin?
  - id: restore-subscriptionAssignments-by-id
    intent: Undo a subscription cancellation
    question: Can I reverse a subscription cancellation before it takes effect?
  - id: options-subscriptionAssignment-undoCancellationAction
    intent: Check methods on the undo cancellation action
    question: Which verbs does the undoCancellation action endpoint accept from a browser?
  phrasing_ops: 8
  slug: vendasta-subscription-assignments-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Subscriptions API from Vendasta — 1 operation(s) for subscriptions.
  name: Vendasta Subscriptions API
  phrasing_intents:
  - id: get-subscriptions
    intent: List product subscriptions for a partner
    question: Which products has a business location subscribed to through my partner account?
  - id: options-subscriptions
    intent: Check allowed methods for subscriptions
    question: Which HTTP verbs does the subscriptions endpoint accept from a browser?
  phrasing_ops: 2
  slug: vendasta-subscriptions-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: System Operations
  name: Vendasta System Operations API
  phrasing_intents:
  - id: get-namespace-ResourceTypes
    intent: List SCIM resource types supported
    question: Which SCIM resource types, like Users or Groups, does the platform support?
  - id: get-ResourceTypes-id
    intent: Get one SCIM resource type
    question: What endpoint and schema back the SCIM User resource type?
  - id: get-namespace-Schemas
    intent: List SCIM schemas
    question: Which data schemas can SCIM resource types use here?
  - id: get-Schemas-id
    intent: Get one SCIM schema
    question: What attributes does the core User schema define?
  - id: get-ServiceProviderConfig
    intent: Get SCIM feature support config
    question: Which SCIM features, such as patch, filter or sort, does Vendasta support?
  - id: get-namespace-Bulk
    intent: Check SCIM bulk operation support
    question: Can I run many SCIM operations at once with a bulk request?
  phrasing_ops: 6
  slug: vendasta-system-operations-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Templates API from Vendasta — 2 operation(s) for templates.
  name: Vendasta Templates API
  phrasing_intents:
  - id: post-templates
    intent: Create a review request template
    question: How do I create a new email template for asking customers for reviews?
  - id: get-templates
    intent: List review request templates for a location
    question: Which review request templates does a business location have?
  - id: options-templates
    intent: Check allowed methods on the templates collection
    question: Which HTTP verbs does the reviewRequestTemplates collection allow?
  - id: get-templates-id
    intent: Get a review request template
    question: What does a specific review request template currently say?
  - id: delete-templates-id
    intent: Delete a review request template
    question: Can I remove a review request template I no longer use?
  - id: patch-templates-id
    intent: Update a review request template
    question: Can I edit the wording of an existing review request template?
  - id: options-templates-id
    intent: Check allowed methods on one template
    question: Which verbs can a browser use on a single review request template?
  phrasing_ops: 7
  slug: vendasta-templates-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Terms API from Vendasta — 2 operation(s) for terms.
  name: Vendasta Terms API
  phrasing_intents:
  - id: glossary-post-terms
    intent: Create a glossary term
    question: How do I add a new term to the glossary?
  - id: patch-glossary-terms-id
    intent: Update a glossary term
    question: Can I change the definition of an existing glossary term?
  phrasing_ops: 2
  slug: vendasta-terms-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The User Custom Fields API from Vendasta — 2 operation(s) for user custom fields.
  name: Vendasta User Custom Fields API
  phrasing_intents:
  - id: options-userCustomFields-by-userid
    intent: Check allowed methods for a user's custom fields
    question: Which HTTP verbs does the custom fields list nested under a user accept?
  - id: patch-userCustomFields-by-id
    intent: Update a user's custom field values
    question: Can I change the value of a custom field on a user?
  - id: get-userCustomFields-by-id
    intent: Get a user's custom field values
    question: What partner-defined custom field values are stored on a user?
  - id: options-userCustomFields-by-id
    intent: Check allowed methods for a user custom fields record
    question: What verbs does the standalone userCustomFields record permit cross-origin?
  phrasing_ops: 4
  slug: vendasta-user-custom-fields-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Users API from Vendasta — 5 operation(s) for users.
  name: Vendasta Users API
  phrasing_intents:
  - id: post-users
    intent: Create a user
    question: Can I add a new user account under my partner through the API?
  - id: options-users
    intent: Check allowed HTTP methods on the users collection
    question: Which HTTP verbs does the users collection endpoint accept for CORS preflight?
  - id: get-users
    intent: List platform users
    question: Which users belong to my partner account in Vendasta?
  - id: get-users-id
    intent: Get a user's details
    question: How can I look up a single user's profile by ID?
  - id: options-users-id
    intent: Check allowed HTTP methods on a single user
    question: Which HTTP verbs are permitted on an individual user resource?
  - id: patch-users-id
    intent: Update a user
    question: Can I change just a few fields on an existing user without resending everything?
  - id: delete-users-id
    intent: Delete a user
    question: Can I permanently delete a user and remove their personal data?
  - id: options-users-id-relationships-businessLocations
    intent: Check allowed methods on user-location links
    question: Which HTTP verbs does the user-to-location relationship endpoint support for CORS?
  phrasing_ops: 14
  slug: vendasta-users-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The VAnalytics API from Vendasta — 5 operation(s) for vanalytics.
  name: Vendasta V Analytics API
  phrasing_intents:
  - id: VAnalytics_PushBusinessMetric
    intent: Push business metric data points
    question: How do I send my own metric values into business reports?
  - id: VAnalytics_DeleteBusinessMetric
    intent: Delete a business metric point
    question: Can I delete one metric data point I pushed by mistake?
  - id: VAnalytics_DeleteMultiBusinessMetrics
    intent: Delete several business metric points
    question: Can I delete many metric points in one call?
  - id: VAnalytics_GetBusinessMetric
    intent: Get a business metric over a date range
    question: What values were recorded for a metric over a date range?
  - id: VAnalytics_GetBusinessMetricPoint
    intent: Get one business metric point
    question: Can I see the full details of a single metric data point?
  phrasing_ops: 5
  slug: vendasta-vanalytics-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The WordpressPluginService API from Vendasta — 1 operation(s) for wordpresspluginservice.
  name: Vendasta Wordpress Plugin Service API
  phrasing_intents:
  - id: WordpressPluginService_PublishPost
    intent: Publish a blog post
    question: Can I publish a blog post straight to a business's WordPress site?
  phrasing_ops: 1
  slug: vendasta-wordpresspluginservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The WordpressService API from Vendasta — 3 operation(s) for wordpressservice.
  name: Vendasta Wordpress Service API
  phrasing_intents:
  - id: WordpressService_UpdateCore
    intent: Update WordPress core on a hosted site
    question: How do I upgrade WordPress core on a hosted site to the latest version?
  - id: WordpressService_UpdatePlugins
    intent: Update plugins on a WordPress site
    question: Can I update several WordPress plugins on a site at once?
  - id: WordpressService_UpdateTheme
    intent: Update a theme on a WordPress site
    question: Is there a way to update the theme on a hosted WordPress site?
  phrasing_ops: 3
  slug: vendasta-wordpressservice-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The OAuth APIs allow applications to retrieve a bearer token that must be supplied with all API calls. See the Authentication documentation for more details.
  name: Vendasta OAUTH API
  phrasing_intents:
  - id: postOauthToken
    intent: Exchange a signed JWT for an access token
    question: How do I get an OAuth access token for server-to-server calls?
  phrasing_ops: 1
  slug: vendasta-oauth-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Sales Orders API from Vendasta — 3 operation(s) for sales orders.
  name: Vendasta Sales Orders API
  phrasing_intents:
  - id: SalesOrders_CreateSalesOrder
    intent: Create a sales order
    question: How do I place a sales order for a business with line items?
  - id: SalesOrders_GetSalesOrder
    intent: Get one sales order
    question: What's the status and content of a specific sales order?
  - id: SalesOrders_ListSalesOrder
    intent: List a partner's sales orders
    question: Which sales orders has my partner account received?
  phrasing_ops: 3
  slug: vendasta-sales-orders-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Search Service API from Vendasta — 2 operation(s) for search service.
  name: Vendasta Search Service API
  phrasing_intents:
  - id: SearchService_GetPluginUpdatesCount
    intent: Count pending WordPress plugin updates
    question: How many WordPress plugin updates are waiting across my partner's sites?
  - id: SearchService_GetSiteHealthChecks
    intent: Get WordPress site health checks
    question: What does the site health report say for a WordPress site?
  phrasing_ops: 2
  slug: vendasta-search-service-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Site Info API from Vendasta — 1 operation(s) for site info.
  name: Vendasta Site Info API
  phrasing_intents:
  - id: SiteInfo_List
    intent: List hosted website info
    question: What hosted websites exist and what info is kept about them?
  phrasing_ops: 1
  slug: vendasta-site-info-api
- baseURL: https://developers.vendasta.com/api/v1
  baseurl_source: declared
  description: The Social Posts API from Vendasta — 3 operation(s) for social posts.
  name: Vendasta Social Posts API
  phrasing_intents:
  - id: SocialPosts_DeleteSocialPost
    intent: Delete a social post
    question: Can I delete a social media post a business published?
  - id: SocialPosts_GetMultiSocialPosts
    intent: Fetch social posts by ID
    question: Can I retrieve specific social posts when I know their IDs?
  - id: SocialPosts_List
    intent: List a business's social posts
    question: Which social posts has a business published?
  phrasing_ops: 3
  slug: vendasta-social-posts-api
artifact_total: 111
asyncapis:
- description: ''
  name: Vendasta Webhooks
  slug: vendasta-webhooks
collections:
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account API
  slug: open-vendasta-account-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account activity API
  slug: open-vendasta-activity-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account change_spend API
  slug: open-vendasta-change-spend-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account customer API
  slug: open-vendasta-customer-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account executive_report API
  slug: open-vendasta-executive-report-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account marketplace_app API
  slug: open-vendasta-marketplace-app-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account oauth API
  slug: open-vendasta-oauth-api
- collection_type: open
  name: Vendasta Marketplace API V1 Endpoints account user API
  slug: open-vendasta-user-api
common:
- group: company
  title: ''
  type: Blog
  url: https://www.vendasta.com/newsroom/
- group: company
  title: ''
  type: BlogRSS
  url: https://www.vendasta.com/feed/
- group: other
  href: https://artifacts.apis.io/vendasta/capabilities/vendasta-capability-edges.yml
  title: ''
  type: CapabilityMap
  url: capabilities/vendasta-capability-edges.yml
- group: auth
  href: https://artifacts.apis.io/vendasta/security/vendasta-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/vendasta-trust-center.yml
- group: auth
  href: https://artifacts.apis.io/vendasta/security/vendasta-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/vendasta-vulnerability-disclosure.yml
- group: auth
  href: https://artifacts.apis.io/vendasta/security/vendasta-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/vendasta-domain-security.yml
- group: agent
  href: https://artifacts.apis.io/vendasta/agentic-access/vendasta-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/vendasta-agentic-access.yml
- group: auth
  href: https://artifacts.apis.io/vendasta/authentication/vendasta-authentication.yml
  title: ''
  type: Authentication
  url: authentication/vendasta-authentication.yml
- group: build
  href: https://artifacts.apis.io/vendasta/packages/vendasta-packages.yml
  title: ''
  type: Packages
  url: packages/vendasta-packages.yml
- group: build
  href: https://artifacts.apis.io/vendasta/packages/vendasta-packages.yml
  title: ''
  type: SDKs
  url: packages/vendasta-packages.yml
- group: agent
  href: https://artifacts.apis.io/vendasta/mcp/vendasta-mcp.yml
  title: ''
  type: X-MCPServerCandidate
  url: mcp/vendasta-mcp.yml
- group: agent
  href: https://artifacts.apis.io/vendasta/llms/vendasta-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/vendasta-llms.txt
- group: other
  href: https://artifacts.apis.io/vendasta/overlays/vendasta-marketplace-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vendasta-marketplace-overlay.yaml
- group: design
  href: https://artifacts.apis.io/vendasta/conformance/vendasta-conformance.yml
  title: ''
  type: Conformance
  url: conformance/vendasta-conformance.yml
- group: design
  href: https://artifacts.apis.io/vendasta/errors/vendasta-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/vendasta-problem-types.yml
- group: design
  href: https://artifacts.apis.io/vendasta/lifecycle/vendasta-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/vendasta-lifecycle.yml
- group: design
  href: https://artifacts.apis.io/vendasta/conventions/vendasta-conventions.yml
  title: ''
  type: Conventions
  url: conventions/vendasta-conventions.yml
- group: design
  href: https://artifacts.apis.io/vendasta/data-model/vendasta-data-model.yml
  title: ''
  type: DataModel
  url: data-model/vendasta-data-model.yml
- group: start
  href: https://artifacts.apis.io/vendasta/sandbox/vendasta-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/vendasta-sandbox.yml
- group: agent
  href: https://artifacts.apis.io/vendasta/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: company
  title: ''
  type: Website
  url: https://www.vendasta.com
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developers.vendasta.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developers.vendasta.com/vendor
- group: docs
  title: ''
  type: APIReference
  url: https://developers.vendasta.com/api/v1
- group: start
  title: ''
  type: GettingStarted
  url: https://developers.vendasta.com/vendor
- group: auth
  title: ''
  type: Security
  url: https://www.vendasta.com/developers/vulnerability-disclosure-program/
- group: auth
  title: ''
  type: Compliance
  url: https://trust.vendasta.com/
- group: operate
  title: ''
  type: Support
  url: https://support.vendasta.com/
- group: company
  title: ''
  type: Blog
  url: https://www.vendasta.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.vendasta.com/pricing/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://trust.vendasta.com/resources?name=terms-of-service
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://trust.vendasta.com/resources?name=customer-privacy-policy
- group: operate
  title: ''
  type: StatusPage
  url: https://status.vendasta.com/
- group: commercial
  href: https://artifacts.apis.io/vendasta/plans/vendasta-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/vendasta-plans-pricing.yml
- group: operate
  href: https://artifacts.apis.io/vendasta/rate-limits/vendasta-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/vendasta-rate-limits.yml
- group: operate
  href: https://artifacts.apis.io/vendasta/changelog/vendasta-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/vendasta-changelog.yml
- group: auth
  href: https://artifacts.apis.io/vendasta/scopes/vendasta-scopes.yml
  title: ''
  type: OAuthScopes
  url: scopes/vendasta-scopes.yml
- group: design
  href: https://artifacts.apis.io/vendasta/asyncapi/vendasta-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/vendasta-webhooks.yml
- group: build
  href: https://artifacts.apis.io/vendasta/cli/vendasta-cli.yml
  title: ''
  type: CLI
  url: cli/vendasta-cli.yml
- group: design
  href: https://artifacts.apis.io/vendasta/errors/vendasta-error-codes.yml
  title: ''
  type: ErrorCodes
  url: errors/vendasta-error-codes.yml
- group: other
  href: https://artifacts.apis.io/vendasta/overlays/vendasta-platform-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/vendasta-platform-overlay.yaml
- group: operate
  title: ''
  type: Deprecation
  url: https://github.com/vendasta/api-gateway-docs/blob/master/docs/Overview/Versioning.md
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/vendasta
- group: start
  title: ''
  type: SignUp
  url: https://signup.vendasta.com/
- group: start
  title: ''
  type: Login
  url: https://login-prod.apigateway.co/account-selector/login?serviceProviderId=AA
- group: other
  href: https://artifacts.apis.io/vendasta/openapi/vendasta-scim-openapi.yml
  title: ''
  type: SCIM
  url: openapi/vendasta-scim-openapi.yml
created: '2026-07-17'
description: 'Vendasta is an end-to-end commerce and operating platform that lets agencies, media companies, banks, telcos and other channel partners sell digital products and services to small and medium-sized businesses under their own brand. The platform bundles a white-label Marketplace of resellable products, a Business App client dashboard, CRM and sales pipeline, marketing automation, billing, managed WordPress hosting and a family of AI Employees. Vendasta exposes two distinct API surfaces. The API Gateway at prod.apigateway.co is the current one: 30 first-party OpenAPI documents covering Platform (business locations, users, orders, subscriptions, automations), CRM, SCIM 2.0 user provisioning, Local SEO, Reputation, Social, Customer Voice, Advertising Intelligence, AI Employees, AI Knowledge, Meetings, Forms and Website Pro — JSON:API over application/vnd.api+json, secured by OAuth2 with 73 published scopes, deliberately unversioned with per-operation x-lifecycle maturity. The legacy
  Marketplace API V1 at developers.vendasta.com/api/v1 remains for vendor apps: accounts, users, customers, add-ons, activities, executive reports and file groups, plus eight JWT-signed Marketplace webhooks. Headquartered in Saskatoon, Canada, Vendasta was founded in 2008.'
finops:
- has_sources: true
  method: derived
  name: Vendasta Finops
  primary_unit: monthly minimum spend
  service_category: ''
  slug: vendasta-finops
  template: false
image: https://www.vendasta.com/wp-content/uploads/2021/03/vendasta-logo.png
layout: provider
modified: '2026-10-06'
name: Vendasta
nav: Providers
network: true
overview: 'Vendasta publishes 87 API contracts indexed on the [APIs.io](https://apis.io/) network, including Account API, Activity API, Change Spend API, and 84 more. Tagged areas include Company, Software-as-a-Service, Marketplace, Small Business, and White Label.


  The Vendasta catalog on APIs.io includes 1 event-driven AsyncAPI specification and 1 Spectral governance ruleset.


  Vendasta''s developer surface includes engineering blog, authentication, sandbox, documentation, API reference, getting-started guide, support, and 39 more developer resources.'
plans:
- name: Vendasta Plans Pricing
  plan_count: 4
  slug: vendasta-plans-pricing
- name: Vendasta Price Estimates
  plan_count: 0
  slug: vendasta-price-estimates
random_paper: 14
rate_limits:
- limit_count: 2
  name: Vendasta Rate Limits
  slug: vendasta-rate-limits
rules:
- authorship: generated
  effective_rule_count: 91
  extends:
  - spectral:oas
  name: Vendasta API Rules
  rule_count: 50
  severity_counts:
    error: 33
    hint: 0
    info: 4
    warn: 13
  slug: vendasta-rules
scopes:
- name: Vendasta Scopes
  scope_count: 73
  slug: vendasta-scopes
  summary_line: 73 scopes · authorizationCode
score:
  band: exemplar
  composite: 81.2
  coverage:
    artifact_dirs: 33
    catalog_earned: 67.5
    catalog_earned_first_party: 20.0
    catalog_gap: 47.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 7.1
  facets:
    access_clarity: 93.4
    contract_governance: 31.8
    contract_quality: 57.2
    developer_ergonomics: 80.4
    discoverability: 78.6
    operational_transparency: 81.6
  jurisdiction:
    basis: provider tags (build_countries.py / build_regions.py)
    countries:
    - canada
    note: A first approximation of where this provider operates, derived from the tags on its profile. NOT a legal determination of domicile or regulatory scope, and it does not yet decide which regimes the regulatory facet evaluates (roadmap#85).
  previous_composite: 74.1
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 87
    mcp: derived
    skills: derived
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 45.1
  schema_version: 0.27.0
  scored_at: '2026-11-06'
  trend: rising
  upsert:
    applies: true
    score: 61.1
screenshot: https://apis.io/screenshots/vendasta/vendasta-2026-08-17T080435.png
security:
- kind: authentication
  name: Vendasta Authentication
  slug: vendasta-authentication
  summary_line: oauth2/http/openIdConnect · 6 schemes
- kind: domain-security
  name: Vendasta Domain Security
  slug: vendasta-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Vendasta Vulnerability Disclosure
  slug: vendasta-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Vendasta Trust Center
  slug: vendasta-trust-center
  summary_line: SOC 2
skill_count: 4
skills:
- name: Manage a Vendasta account and its users
  slug: vendasta-manage-account
- name: Create and manage Vendasta customers
  slug: vendasta-manage-customers
- name: Provision platform users and grant them business locations
  slug: vendasta-provision-users
- name: Sell a product to a business and confirm activation
  slug: vendasta-sell-and-activate
slug: vendasta
tags:
- Company
- Software-as-a-Service
- Marketplace
- Small Business
- White Label
- Reseller
- Marketing
- CRM
- Digital Agency
- Platform
website: https://www.vendasta.com
---
